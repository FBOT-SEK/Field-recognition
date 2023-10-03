#!/usr/bin/env python3

# Import the necessary libraries
import time
import math
from threading import Thread
from ev3dev2.motor import SpeedPercent, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from odometry import Odometry
from time import sleep
import threading
import rpyc


# Faço a conexão do Ev3 master com o slave
slave = '192.168.137.3' # IP do ev3 slave
master = '192.168.0.2' # IP do ev3 master
config = {"sync_request_timeout": 240}
conn = rpyc.classic.connect(slave) # Conecta com o slave


ev3dev2_motor = conn.modules['ev3dev2.motor'] # Importa a biblioteca de motores do slave
ev3dev2_sensor = conn.modules['ev3dev2.sensor'] # Importa a biblioteca de sensores do slave
ev3dev2_sensor_lego = conn.modules['ev3dev2.sensor.lego']


odometry = Odometry(OUTPUT_A, OUTPUT_B, 6.88, 17.2, 360, 360, debug=True)

# Define os motores e sensores
CS1 = ColorSensor(INPUT_1)
CS2 = ColorSensor(INPUT_2)
cor_do_cone = ColorSensor(INPUT_3)
IRS = InfraredSensor(INPUT_4)

gyro = ev3dev2_sensor_lego.GyroSensor(ev3dev2_sensor.INPUT_2)
US = ev3dev2_sensor_lego.UltrasonicSensor(ev3dev2_sensor.INPUT_1)

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

# Modo de leitura dos sensores de cor
CS1.mode = 'RGB-RAW'
CS2.mode = 'RGB-RAW'
cor_do_cone.mode = 'RGB-RAW'

# Classe para representar uma cor em RGB
class Cor:
    def __init__(self, r, g, b, nome):
        self.r = r
        self.g = g
        self.b = b
        self.nome = nome

    def distancia(self, r, g, b):
        return math.sqrt((self.r - r) ** 2 + (self.g - g) ** 2 + (self.b - b) ** 2)

# Definindo algumas cores

# vermelho
vermelho = Cor(230, 41, 40, "vermelho")
vermelho2 = Cor(240, 63, 26, "vermelho 2")
vermelho3 = Cor(100, 20, 4, "vermelho 3")

# verde
verde = Cor(40, 70, 61, "verde")
verde2 = Cor(40, 150, 40, "verde 2")
verde3 = Cor(12, 70, 12, "verde 3")

# azul
azul = Cor(36, 49, 95, "azul")
azul2 = Cor(62, 100, 100, "azul 2")
azul3 = Cor(15, 23, 14, "azul 3")

# preto
preto = Cor(35, 30, 30, "preto")
preto2 = Cor(47, 65, 40, "preto 2")
nada = Cor(0, 0, 0, "nada")

# branco
branco = Cor(255, 180, 180, "branco")
branco2 = Cor(250, 255, 230, "branco 2")

# amarelo
amarelo = Cor(220, 190, 40, "amarelo")
amarelo2 = Cor(220, 255, 40, "amarelo 2")

# marrom
marrom = Cor(61, 35, 43, "marrom")
marrom2 = Cor(62, 77, 43, "marrom 2")
marrom3 = Cor(20, 20, 3, "marrom 3")

# Lista de cores para o sensor 1
cores1 = [vermelho, verde, azul, marrom, amarelo, preto, branco]

# Lista de cores para o sensor 2
cores2 = [vermelho2, verde2, azul2, marrom2, amarelo2, preto2, branco2]

# Lista de cores para o sensor 3
cores3 = [vermelho3, verde3, azul3, marrom3, nada]

def encontrar_cor_mais_proxima(r, g, b, cores): # Encontra a cor mais próxima da leitura do sensor em relação a lista de cores
    cor_mais_proxima = None
    menor_distancia = float('inf')

    for cor in cores:
        distancia = cor.distancia(r, g, b)
        if distancia < menor_distancia:
            menor_distancia = distancia
            cor_mais_proxima = cor

    return cor_mais_proxima.nome

def esquerda(): # Vira para a direita
    gyro.reset()  
    while gyro.angle < 84:
        tank_drive.on(-5, 5)
        odometry.get_pos()
        print(gyro.angle)
    tank_drive.off(brake=True)

def direita(): # Vira para a esquerda
    gyro.reset()
    while gyro.angle > -82:
        tank_drive.on(5, -5)
        odometry.get_pos()
        print(gyro.angle)
    tank_drive.off(brake=True)

def virar_180(): # Vira 180 graus
    gyro.reset()
    while gyro.angle > -82*2:
        tank_drive.on(5, -5)
        odometry.get_pos() 
        print(gyro.angle)
    tank_drive.off(brake=True)

# Anda x centimetros, basta fazer a multiplicação "x*andar"
circ_roda = 6.88*math.pi
andar = 360/circ_roda

# Aumenta a velocidade gradativamente
speed = 0
def increase_speed():
    global speed
    for i in range(10):  # Aumente o número de iterações para incrementos menores de velocidade
        speed += 1  # Aumente a velocidade em 0.1
        time.sleep(0.3)  # Espere por 0.1 segundo
        




# Função de navegação até chegar no ponto 0
def init():
    print(cor_mais_proxima1,'', cor_mais_proxima2) # Printa a leitura e os valores RGB dos sensores 1 e 2
    print(CS1.rgb)
    print(CS2.rgb)
    print('')
        
    if cor_mais_proxima1 == branco.nome and cor_mais_proxima2 == branco2.nome: # Se os dois sensores estiverem lendo branco, anda para a frente

    # Inicia uma thread para aumentar a velocidade gradativamente para que não haja derrapagem
        threading.Thread(target=increase_speed).start()
        while speed < 10:
            tank_drive.on(SpeedPercent(speed), SpeedPercent(speed))


    # Se o sensor 1 leu azul e o sensor 2 leu branco, vire para a esquerda até alinhar os sensores e os dois lerem azul
    elif cor_mais_proxima1 == azul.nome and cor_mais_proxima2 == branco2.nome:
        tank_drive.off()
        while cor_mais_proxima1 == azul.nome and cor_mais_proxima2 != azul2.nome:
            tank_drive.on(-2,2)
        if cor_mais_proxima1 == azul.nome and cor_mais_proxima2 == azul2.nome: # Se os dois leram azul, então chegou na zona de embarque
            return zona_de_embarque()
        
    # Se o sensor 1 leu azul e o sensor 2 leu branco, vire para a esquerda até alinhar os sensores e os dois lerem azul
    elif cor_mais_proxima1 == branco.nome and cor_mais_proxima2 == azul2.nome:
        tank_drive.off()
        while cor_mais_proxima1 != azul.nome and cor_mais_proxima2 == azul2.nome: 
            tank_drive.on(2.5,-2.5)
        if cor_mais_proxima1 == azul.nome and cor_mais_proxima2 == azul2.nome: # Se os dois leram azul, então chegou na zona de embarque
            return zona_de_embarque()

    # Se os sensores 1 e 2 lerem preto, então ele está na parede de um estabelecimento
    elif cor_mais_proxima1 == preto.nome and cor_mais_proxima2 == preto2.nome: 
        tank_drive.off()
        tank_drive.on_for_degrees(-10,-10, 5*andar) # Volto 5cm e viro a direita
        direita()
            
    # Se o sensor 1 leu preto e o sensor 2 leu amarelo, então está na entrada de um estabelecimento        
    elif cor_mais_proxima1 == preto and cor_mais_proxima2 == amarelo2: 
            tank_drive.off()
            tank_drive.on_for_degrees(-10,-10, 5*andar) # Volto 5cm e viro a direita
            direita()
            
    # Se o sensor 1 leu amarelo e o sensor 2 leu preto, então está na entrada de um estabelecimento        
    elif cor_mais_proxima1 == amarelo and cor_mais_proxima2 == preto2.nome: 
            tank_drive.off()
            tank_drive.on_for_degrees(-10,-10, 5*andar) # Volto 5cm e viro a direita
            direita()
    
    # Se os dois sensores lerem vermelho, então chegou na delimitação vermelha da arena
    if cor_mais_proxima1 == vermelho.nome and cor_mais_proxima2 == vermelho2.nome:
        tank_drive.off()
        tank_drive.on_for_degrees(-10,-10, andar*37.5) # Volta 37.5cm, vira a direita e anda até ler azul
        print('ue')
        direita()
        tank_drive.on(10, 10)
    
    # Se a última cor que os sensores leram for branco e a cor atual for azul, então chegou na zona de embarque
    if ultima_cor1 == branco.nome and cor_mais_proxima1 == azul.nome and ultima_cor2 == branco2.nome and cor_mais_proxima2 == azul2.nome: 
        print('entrou')
        return zona_de_embarque()
        

def zona_de_embarque(): # Entrou na zona de embarque
        print('Zona de embarque')
        tank_drive.off()
        tank_drive.on_for_degrees(-10,-10, 6*andar) # Volta 6cm e vira a direita
        direita()
        tank_drive.on(10, 10) # Ando até achar a delimitação vermelha
        
        if cor_mais_proxima1 == vermelho.nome and cor_mais_proxima2 == vermelho2.nome: # Se os dois sensores lerem vermelho, então chegou no ponto 0
            tank_drive.off()
            tank_drive.on_for_degrees(-10,-10, 3*andar) # Volta 5cm e vira 180 graus
            virar_180()
            tank_drive.off()
            return embarque() # Começo o embarque
        
        
# Procura um cano e assim que acha reconhece se é adulto ou criança
def embarque():
    while US > 15: # Enquanto o ultrassônico não detectar um cano anda pra frente
        tank_drive.on(20,20)
    if US < 15: # Quando o ultrassônico detectar um cano vira a direita e anda 9cm para frente
        tank_drive.off()
        direita()
        tank_drive.on_for_degrees(2.5,2.5, 9*andar)
        if IRS.proximity <= 10: # Se o infravermelho detectar algo, então é um adulto
            print('Adulto')
            return Adultos()
        elif IRS.proximity >= 10: # Caso não detectar, é uma criança
            print('Crianca')
            return Criancas()
        else:
            return

# Reconhece o estabelecimento do adulto e retorna a função para o estabelecimento correspondente           
def Adultos():
    
        if cano_mais_proximo == vermelho3.nome: # Se vermelho é farmacia
            print('Farmacia')
            #return Drugstore()
        if cano_mais_proximo == verde3.nome: # Se verde é prefeitura
            print("Prefeitura")
            #return City_hall()
        if cano_mais_proximo == azul3.nome: # Se azul é museu
            print("Museu")
            #return Museum()
        if cano_mais_proximo == marrom3.nome: # Se marrom é padaria
            print('Padaria')
            #return Bakery()
        else:
            print('nao existe')
            return False

# Reconhece o estabelecimento da criança e retorna a função para o estabelecimento correspondente           
def Criancas():
        if cano_mais_proximo == verde3.nome: # Se verde é parque
            print('Parque')
            #return Park()
        if cano_mais_proximo == azul3.nome: # se azul é escola
            print('Escola')
            #return School()
        if cano_mais_proximo == marrom3.nome: # Se marrom é biblioteca
            print('Biblioteca')
            #return Library()
        else:
            print('nao existe')
            return False
            

#               Arena
# [0,0]-----------------------[178,0]
#   |             |              |
#   |             |              |
#   |             |              |
#   |             |              |
#   |             |              |
# [0,150]--------------------[178,150]



# Crio uma variável que armazena a última cor que o sensor leu para compará-la com a cor atual
ultima_cor1 = None # Última cor que o sensor 1 leu
ultima_cor2 = None # Última cor que o sensor 2 leu

print("inicio")
while True:
    time.sleep(1)
    r1,g1,b1 = CS1.rgb
    cor_mais_proxima1 = encontrar_cor_mais_proxima(r1,g1,b1, cores1)

    r2,g2,b2 = CS2.rgb
    cor_mais_proxima2 = encontrar_cor_mais_proxima(r2,g2,b2, cores2)
    
    r3,g3,b3 = cor_do_cone.rgb
    cano_mais_proximo = encontrar_cor_mais_proxima(r3,g3,b3, cores3)
    
    init()
    
    ultima_cor1 = cor_mais_proxima1 # Atualiza a última cor lida pelo sensor 1
    ultima_cor2 = cor_mais_proxima2 # Atualiza a última cor lida pelo sensor 2
