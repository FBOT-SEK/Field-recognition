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

# Create a RPyC connection to the remote ev3dev device.
# Use the hostname or IP address of the ev3dev device.
# If this fails, verify your IP connectivty via ``ping X.X.X.X``
slave = '192.168.137.3'
master = '192.168.0.2'
config = {"sync_request_timeout": 240}
conn = rpyc.classic.connect(slave)

ev3dev2_motor = conn.modules['ev3dev2.motor']
ev3dev2_sensor = conn.modules['ev3dev2.sensor']
ev3dev2_sensor_lego = conn.modules['ev3dev2.sensor.lego']


odometry = Odometry(OUTPUT_A, OUTPUT_B, 6.88, 17.2, 360, 360, debug=True)
CS1 = ColorSensor(INPUT_1)
CS2 = ColorSensor(INPUT_2)
cor_do_cone = ColorSensor(INPUT_3)
IRS = InfraredSensor(INPUT_4)

gyro = ev3dev2_sensor_lego.GyroSensor(ev3dev2_sensor.INPUT_2)
US = ev3dev2_sensor_lego.UltrasonicSensor(ev3dev2_sensor.INPUT_1)


tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)


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

# branco
branco = Cor(255, 245, 240, "branco")
branco2 = Cor(250, 255, 230, "branco 2")

# amarelo
amarelo = Cor(220, 190, 70, "amarelo")
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
cores3 = [vermelho3, verde3, azul3, marrom3]

def esquerda():
    gyro.reset()
    while gyro.angle < 84:
        tank_drive.on(-5, 5)
        odometry.get_pos()
        print(gyro.angle)
    tank_drive.off(brake=True)

def direita():
    gyro.reset()
    while gyro.angle > -80:
        tank_drive.on(5, -5)
        odometry.get_pos() 
        print(gyro.angle)
    tank_drive.off(brake=True)
    
def encontrar_cor_mais_proxima(r, g, b, cores):
    cor_mais_proxima = None
    menor_distancia = float('inf')

    for cor in cores:
        distancia = cor.distancia(r, g, b)
        if distancia < menor_distancia:
            menor_distancia = distancia
            cor_mais_proxima = cor

    return cor_mais_proxima.nome


leitura = 0

circ_roda = 6.88*math.pi
circ_robo = 17.3*math.pi
odo = circ_robo/circ_roda
andar = 360/circ_roda
girar_90 = 0.63*100*odo
girar_180 = 1.26*odo*100

speed = 0

def increase_speed():
    global speed
    for i in range(10):  # Aumente o número de iterações para incrementos menores de velocidade
        speed += 1  # Aumente a velocidade em 0.1
        time.sleep(0.3)  # Espere por 0.1 segundo

def zona_de_embarque():
        print('foi?')
        tank_drive.off()
        tank_drive.on_for_degrees(-10,-10, 6*andar)
        direita()
        tank_drive.on(5, 5)
        if cor_mais_proxima1 == vermelho.nome and cor_mais_proxima2 == vermelho2.nome:
            tank_drive.off()
            tank_drive.on_for_degrees(-10,-10, 5*andar)
            tank_drive.on_for_degrees(10, -10, girar_180)
            return embarque(True)
        

def embarque():
    while US > 15*andar:
        tank_drive.on(20,20)
    if US < 15*andar:
        tank_drive.off()
        direita()
        tank_drive.on_for_degrees(2.5,2.5, 90*odo)
        if IRS <= 6 and cor_do_cone == True:
            return Adultos(True)
        elif IRS > 6 and cor_do_cone == True:
            return Criancas(True)
        else:
            return 

# Reconhece se é adulto ou criança            
def Adultos():
    if Adultos(True):
        if cano_mais_proximo == vermelho3.nome:
            return Drugstore(True)
        if cano_mais_proximo == verde3.nome:
            return City_hall(True)
        if cano_mais_proximo == azul3.nome:
            return Museum(True)
        if cano_mais_proximo == marrom.nome:
            return Bakery(True)
        else:
            return False

def Criancas(x):
    if Criancas(True):
        if cano_mais_proximo == vermelho3.nome:
            return Drugstore()
        if cano_mais_proximo == verde3.nome:
            return Park()
        if cano_mais_proximo == azul3.nome:
            return School()
        if cano_mais_proximo == marrom3.nome:
            return Library()
        else:
            return False
            
# Cria uma função para cada estabelecimento

def init():
    print(cor_mais_proxima1,'', cor_mais_proxima2)
    print(CS1.rgb)
    print(CS2.rgb)
    print('')      
    if cor_mais_proxima1 == preto.nome and cor_mais_proxima2 == preto2.nome:
        tank_drive.off()
        tank_drive.on_for_degrees(-10,-10, 5*andar)
        tank_drive.on_for_degrees(-2.5, 2.5, girar_90)
        
    if cor_mais_proxima1 == branco.nome and cor_mais_proxima2 == branco2.nome:
    # Inicie um thread para aumentar a velocidade
        threading.Thread(target=increase_speed).start()

    # Continue movendo os motores na velocidade atualizada
        while speed < 10:
            tank_drive.on(SpeedPercent(speed), SpeedPercent(speed))

    if ultima_cor1 == branco.nome and cor_mais_proxima1 == azul.nome and ultima_cor2 == branco2.nome and cor_mais_proxima2 == azul2.nome: 
        print('entrou')
        return zona_de_embarque()
            
        
    elif cor_mais_proxima1 == azul.nome and cor_mais_proxima2 == branco2.nome:
        tank_drive.off()
        while cor_mais_proxima1 == azul.nome and cor_mais_proxima2 != azul.nome:
            tank_drive.on(-2.5,2.5)
            if cor_mais_proxima1 == azul.nome and cor_mais_proxima2 == azul2.nome:
                return zona_de_embarque()
        
    elif cor_mais_proxima1 == branco.nome and cor_mais_proxima2 == azul.nome:
        tank_drive.off()
        while cor_mais_proxima1 != azul.nome and cor_mais_proxima2 == azul.nome:
            tank_drive.on(2.5,-2.5)
            if cor_mais_proxima1 == azul.nome and cor_mais_proxima2 == azul2.nome:
                return zona_de_embarque()
                    
    elif cor_mais_proxima1 == preto.nome and cor_mais_proxima2 == preto2.nome: # Na parede de um estabelecimento
        tank_drive.off()
        tank_drive.on_for_degrees(-10,-10, 5*andar)
        direita()
            
    elif cor_mais_proxima1 == preto and cor_mais_proxima2 == amarelo2: # Está na entrada de um estabelecimento
            tank_drive.off()
            tank_drive.on_for_degrees(-10,-10, 5*andar)
            direita()
            
    elif cor_mais_proxima1 == amarelo and cor_mais_proxima2 == preto2.nome: # Está na entrada de um estabelecimento
            tank_drive.off()
            tank_drive.on_for_degrees(-10,-10, 5*andar)
            direita()
            
    if cor_mais_proxima1 == vermelho.nome and cor_mais_proxima2 == vermelho2.nome: # Chega na delimitação vermelha da área
        tank_drive.off()
        tank_drive.on_for_degrees(-10,-10, andar*37.5)
        print('ue')
        direita()
        print('??')
        tank_drive.on(10, 10)
            
            
            
            
            
# Create the sensors and motors objects

#               Arena
# [0,0]-----------------------[178,0]
#   |             |              |
#   |             |              |
#   |             |              |
#   |             |              |
#   |             |              |
# [0,150]--------------------[178,150]


arenax = [0, 1, 2, 3, 4, 5, 6]
arenay = [0, 1, 2, 3, 4]
pos_robot=[arenax,arenay]

ultima_cor1 = None
ultima_cor2 = None
print("inicio")
while True:
    time.sleep(0.3)
    r1,g1,b1 = CS1.rgb
    cor_mais_proxima1 = encontrar_cor_mais_proxima(r1,g1,b1, cores1)

    r2,g2,b2 = CS2.rgb
    cor_mais_proxima2 = encontrar_cor_mais_proxima(r2,g2,b2, cores2)
    
    r3,g3,b3 = cor_do_cone.rgb
    cano_mais_proximo = encontrar_cor_mais_proxima(r3,g3,b3, cores3)
    init()
    ultima_cor1 = cor_mais_proxima1
    ultima_cor2 = cor_mais_proxima2