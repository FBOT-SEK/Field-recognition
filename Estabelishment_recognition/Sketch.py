#!/usr/bin/env python3

# Import the necessary libraries
import time
import math
from threading import Thread
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from odometry import Odometry
from time import sleep

odometry = Odometry(OUTPUT_A, OUTPUT_B, 6.88, 17.12, 360, 360, debug=True)
CS1 = ColorSensor(INPUT_1)
CS2 = ColorSensor(INPUT_2)
#cor_do_cone = ColorSensor(INPUT_3)
IRS = InfraredSensor(INPUT_4)
# US = UltrasonicSensor(INPUT_5)
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)


CS1.mode = 'RGB-RAW'
CS2.mode = 'RGB-RAW'

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
vermelho = Cor(200, 27, 37, "vermelho")
vermelho2 = Cor(230, 93, 46, "vermelho 2")
verde = Cor(36, 70, 50, "verde")
verde2 = Cor(45, 141, 41, "verde 2")
azul = Cor(36, 49, 95, "azul")
azul2 = Cor(28, 77, 71, "azul 2")
preto = Cor(30, 30, 37, "preto")
preto2 = Cor(30, 60, 20, "preto 2")
branco = Cor(255, 255, 255, "branco")
branco2 = Cor(170, 255, 204, "branco 2")
amarelo = Cor(220, 190, 70, "amarelo")
amarelo2 = Cor(180, 255, 40, "amarelo 2")
marrom = Cor(61, 35, 43, "marrom")
marrom2 = Cor(62, 77, 43, "marrom 2")

# Lista de cores para o sensor 1
cores1 = [vermelho, verde, azul, marrom, amarelo, preto, branco]

# Lista de cores para o sensor 2
cores2 = [vermelho2, verde2, azul2, marrom2, amarelo2, preto2, branco2]

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

circ_roda = 6.8*math.pi
circ_robo = 17*math.pi
odo = circ_robo/circ_roda
andar = 360/circ_roda

def zona_de_embarque():
        tank_drive.off()
        tank_drive.on_for_seconds(-5,-5, 2)
        tank_drive.on_for_degrees(5,-5, 90*odo)
        tank_drive.on(5, 5)
        if cor_mais_proxima1 == vermelho.nome and cor_mais_proxima2 == vermelho2.nome:
            tank_drive.off()
            tank_drive.on_for_seconds(-5,-5, 2)
            tank_drive.on_for_degrees(-5,5, 90*odo)
            # return embarque(True)
        

# def embarque():
#     if embarque(True):
#         while US > 15*andar:
#             tank_drive.on(20,20)
#         if US < 15*andar:
#             tank_drive.off()
#             tank_drive.on_for_degrees(5,-5, 90*odo)
#             tank_drive.on_for_degrees(5,5, 90*odo)
#             if IRS <= 6 and cor_do_cone == True:
#                 return Adultos(True)
#             elif IRS > 6 and cor_do_cone == True:
#                 return Criancas(True)
#             else:
#                 return 

'''
# Reconhece se é adulto ou criança            
def Adultos():
    if Adultos(True):
 == vermelho        if cor_do_cone == vermelho or vermelho2:
            return Drugstore(True)
        if cor_do_cone == Verde:
            return City_hall(True)
        if cor_do_cone == azul:
            return Museum(True)
        if cor_do_cone == Marrom:
            return Bakery(True)
        else:
            return False

def Criancas(x):
    if Criancas(True):
 == vermelho        if cor_do_cone == vermelho or vermelho2:
            return Drugstore()
        if cor_do_cone == Verde:
            return Park()
        if cor_do_cone == azul:
            return School()
        if cor_do_cone == Marrom:
            return Library()
        else:
            return False
    '''
# Cria uma função para cada estabelecimento
def Drugstore():
    if Drugstore(True):
        tank_drive.on_for_degrees(5,5, 15*andar) # Andou até o meio da primeira rua
        tank_drive.on_for_degrees(-5,5, 90*odo) # Virou para a esquerda
        tank_drive.on_for_degrees(5,5, 60*andar) # Andou até a última rua antes do parque
        tank_drive.on_for_degrees(5,-5, 90*odo) # Virou para a direita
        tank_drive.on_for_degrees(5,5, 15*andar) # Andou até o meio da rua
        tank_drive.on_for_degrees(5,-5, 90*odo) # Virou para a direita
        tank_drive.on_for_degrees(5,5, 15*andar) # Entrou no estabelecimento
        
        # Verifica se entrou no estabelecimento e faz o desembarque do passageiro
        tank_drive.on_for_degrees(-5,-5, 15*andar) # Saiu do estabelecimento
        tank_drive.on_for_degrees(5,-5, 90*odo) # Virou para a direita
        tank_drive.on_for_degrees(5,5, 15*andar) # Andou até o meio da rua
        tank_drive.on_for_degrees(-5,5, 90*odo) # Virou para a esquerda
        tank_drive.on(20,20) # Anda até achar a zona de embarque
        if cor_mais_proxima1 == azul.nome and cor_mais_proxima2 == azul2.nome:
            return zona_de_embarque()

def City_hall():
    if City_hall(True):
        tank_drive.on_for_degrees(5,5, 15*andar) # Andou até o meio da primeira rua
        tank_drive.on_for_degrees(-5,5, 90*odo) # Virou para a esquerda
        tank_drive.on_for_degrees(5,5, 15*andar) # Andou até a última rua antes do parque
        tank_drive.on_for_degrees(5,-5, 90*odo) # Virou para a direita
        tank_drive.on_for_degrees(5,5, 15*andar) # Andou até o meio da rua
        tank_drive.on_for_degrees(5,-5, 90*odo) # Virou para a direita
        tank_drive.on_for_degrees(5,5, 15*andar) # Entrou no estabelecimento
        
        # Verifica se entrou no estabelecimento e faz o desembarque do passageiro
        tank_drive.on_for_degrees(-5,-5, 15*andar) # Saiu do estabelecimento
        tank_drive.on_for_degrees(5,-5, 90*odo) # Virou para a direita
        tank_drive.on_for_degrees(5,5, 15*andar) # Andou até o meio da rua
        tank_drive.on_for_degrees(-5,5, 90*odo) # Virou para a esquerda
        tank_drive.on(20,20) # Anda até achar a zona de embarque
        if cor_mais_proxima1 == azul.nome and cor_mais_proxima2 == azul2.nome:
            return zona_de_embarque()

def Museum():
    if Museum(True):
        tank_drive.on_for_degrees(5,5, 15*andar) # Andou até o meio da primeira rua
        tank_drive.on_for_degrees(-5,5, 90*odo) # Virou para a esquerda
        tank_drive.on_for_degrees(5,5, 30) # Andou até a última rua antes do parque
        tank_drive.on_for_degrees(-5,5, 90*odo) # Virou para a esquerda
        tank_drive.on_for_degrees(5,5, 15*andar) # Entrou no estabelecimento
        
        # Verifica se entrou no estabelecimento e faz o desembarque do passageiro
        tank_drive.on_for_degrees(-5,-5, 15*andar) # Saiu do estabelecimento
        tank_drive.on_for_degrees(-5,5, 90*odo) # Virou para a esquerda
        tank_drive.on_for_degrees(5,5, 15*andar) # Andou até o meio da rua
        tank_drive.on_for_degrees(-5,5, 90*odo) # Virou para a esquerda
        tank_drive.on(20,20) # Anda até achar a zona de embarque
        if cor_mais_proxima1 == azul.nome and cor_mais_proxima2 == azul2.nome:
            return zona_de_embarque() 
        
def Bakery():
    if Bakery(True):
        tank_drive.on_for_degrees(5,5, 15*andar) # Andou até o meio da primeira rua
        tank_drive.on_for_degrees(-5,5, 90*odo) # Virou para a esquerda
        tank_drive.on_for_degrees(5,5, 40) # Andou até a última rua antes do parque
        tank_drive.on_for_degrees(5,-5, 90*odo) # Virou para a direita
        tank_drive.on_for_degrees(5,5, 30) # Andou até o meio da rua
        tank_drive.on_for_degrees(5,-5, 90*odo) # Virou para a direita
        tank_drive.on_for_degrees(5,5, 15*andar) # Entrou no estabelecimento
        
        # Verifica se entrou no estabelecimento e faz o desembarque do passageiro
        tank_drive.on_for_degrees(-5,-5, 15*andar) # Saiu do estabelecimento
        tank_drive.on_for_degrees(5,-5, 90*odo) # Virou para a direita
        tank_drive.on_for_degrees(5,5, 15*andar) # Andou até o meio da rua
        tank_drive.on_for_degrees(-5,5, 90*odo) # Virou para a esquerda
        tank_drive.on(20,20) # Anda até achar a zona de embarque
        if cor_mais_proxima1 == azul.nome and cor_mais_proxima2 == azul2.nome:
            return zona_de_embarque()

def Park():
    if Park(True):
        tank_drive.on_for_degrees(5,5, 15*andar) # Andou até o meio da primeira rua
        tank_drive.on_for_degrees(-5,5, 90*odo) # Virou para a esquerda
        tank_drive.on_for_degrees(5,5, 40) # Andou até a última rua antes do parque
        tank_drive.on_for_degrees(5,-5, 90*odo) # Virou para a direita
        tank_drive.on_for_degrees(5,5, 15*andar) # Andou até o meio da rua
        tank_drive.on_for_degrees(-5,5, 90*odo) # Virou para a esquerda
        tank_drive.on_for_degrees(5,5, 15*andar) # Entrou no estabelecimento
        
        # Verifica se entrou no estabelecimento e faz o esembarque do passageiro
        tank_drive.on_for_degrees(-5,-5, 15*andar) # Saiu do estabelecimento
        tank_drive.on_for_degrees(-5,5, 90*odo) # Virou para a esquerda
        tank_drive.on_for_degrees(5,5, 15*andar) # Andou até o meio da rua
        tank_drive.on_for_degrees(-5,5, 90*odo) # Virou para a esquerda
        tank_drive.on(20,20) # Anda até achar a zona de embarque
        if cor_mais_proxima1 == azul.nome and cor_mais_proxima2 == azul2.nome:
            return zona_de_embarque()

def School():
    if School(True):
        tank_drive.on_for_degrees(5,5, 30) # Andou até o meio da primeira rua
        tank_drive.on_for_degrees(-5,5, 90*odo) # Virou para a esquerda
        tank_drive.on_for_degrees(5,5, 15*andar) # Andou até a última rua antes do parque
        tank_drive.on_for_degrees(5,-5, 90*odo) # Virou para a direita
        tank_drive.on_for_degrees(5,5, 15*andar) # Entrou no estabelecimento
        
        # Verifica se entrou no estabelecimento e faz o esembarque do passageiro
        tank_drive.on_for_degrees(-5,-5, 15*andar) # Saiu do estabelecimento
        tank_drive.on_for_degrees(5,-5, 90*odo) # Virou para a direita
        tank_drive.on(20,20) # Anda até achar a zona de embarque
        if cor_mais_proxima1 == azul.nome and cor_mais_proxima2 == azul2.nome:
            return zona_de_embarque()

def Library():
    if Library(True):
        tank_drive.on_for_degrees(-5,5, 90*odo) # Virou para a esquerda
        tank_drive.on_for_degrees(5,5, 15*andar) # Entrou no estabelecimento
        
        # Verifica se entrou no estabelecimento e faz o esembarque do passageiro
        tank_drive.on_for_degrees(-5,-5, 15*andar) # Saiu do estabelecimento
        tank_drive.on_for_degrees(-5,5, 1) # Virou para a esquerda
        tank_drive.on(20,20) # Anda até achar a zona de embarque
        if cor_mais_proxima1 == azul.nome and cor_mais_proxima2 == azul2.nome:
            return zona_de_embarque()
        

def init():
    print(cor_mais_proxima1,'', cor_mais_proxima2)
    if cor_mais_proxima1 == preto.nome and cor_mais_proxima2 == preto2.nome:
        tank_drive.on_for_degrees(-5, 5, 90*odo)
    if cor_mais_proxima1 == branco.nome and cor_mais_proxima2 == branco2.nome:
        print("pq nao entra?")
        tank_drive.on(20,20)
    if ultima_cor1 == branco.nome and cor_mais_proxima1 == azul.nome and ultima_cor2 == branco2.nome and cor_mais_proxima2 == azul2.nome: # PAREI AQUIIIIIII!!!!!!!!!!!!!!!!!
        print('entrou')
        return zona_de_embarque()
            
        
    elif cor_mais_proxima1 == azul.nome and cor_mais_proxima2 == branco2.nome:
        tank_drive.off()
        while cor_mais_proxima1 == azul.nome and cor_mais_proxima2 != azul.nome:
            tank_drive.on(-5,5)
            if cor_mais_proxima1 == azul.nome and cor_mais_proxima2 == azul2.nome:
                return zona_de_embarque()
        
    elif cor_mais_proxima1 == branco.nome and cor_mais_proxima2 == azul.nome:
        tank_drive.off()
        while cor_mais_proxima1 != azul.nome and cor_mais_proxima2 == azul.nome:
            tank_drive.on(5,-5)
            if cor_mais_proxima1 == azul.nome and cor_mais_proxima2 == azul2.nome:
                return zona_de_embarque()
                    
    elif cor_mais_proxima1 == preto.nome and cor_mais_proxima2 == preto2.nome: # Na parede de um estabelecimento
        tank_drive.off()
        tank_drive.on_for_degrees(-5,-5, 90*odo)
        tank_drive.on_for_degrees(5,-5, 90*odo)
            
    elif cor_mais_proxima1 == preto and cor_mais_proxima2 == amarelo2: # Está na entrada de um estabelecimento
            tank_drive.off()
            tank_drive.on_for_degrees(-5,-5, 90*odo)
            tank_drive.on_for_degrees(5,-5, 90*odo)
            
    elif cor_mais_proxima1 == amarelo and cor_mais_proxima2 == preto2.nome: # Está na entrada de um estabelecimento
            tank_drive.off()
            tank_drive.on_for_degrees(-5,-5, 90*odo)
            tank_drive.on_for_degrees(5,-5, 90*odo)
            
    elif cor_mais_proxima1 == vermelho.nome and cor_mais_proxima2 == vermelho2.nome: # Chega na delimitação vermelha da área
            tank_drive.off()
            tank_drive.on_for_degrees(-5,-5, 90*odo)
            tank_drive.on_for_degrees(5, -5, 90*odo)
            tank_drive.on_for_degrees(5,5, 15*andar)
            tank_drive.on_for_degrees(5,-5, 90*odo)
        
            
            
            
# Create the sensors and motors objects

#               Arena
# [0,0]-----------------------[178,0]
#   |             |              |
#   |             |              |
#   |             |              |
#   |             |              |
#   |             |              |
# [0,150]--------------------[178,150]

def init_pos0(initial_position, ):
    if cor_mais_proxima1.color == 6 and cor_mais_proxima2.color == 6:
        tank_drive.on(20,20)
        if cor_mais_proxima1.color == 2 and cor_mais_proxima2.color == 2:
            tank_drive.off()
            tank_drive.on_for_degrees(-5,-5, 90*odo)
            
            
            initial_position = True 
        initial_position = True

    initial_position = True
    
def init1(x, y):
        if initial_position == True:
            arena = [[0 for y in range(4)] for x in range(6)]
            for i in range(6):
                for j in range(4):
                    arena[i][j] = i*4 + j + 1
                    for linha in arena:
                        print(linha)

# Criando uma matriz 7x5
matriz = [[0 for col in range(5)] for row in range(7)]
# Armazenando valores na matriz
    # matriz[0][0] = 0 Armazena a posição 0 na primeira linha, primeira coluna
    # matriz[1][0] = 1
    # matriz[2][0] = 2
    # matriz[3][0] = 3
    # matriz[4][0] = 4
    # matriz[5][0] = 5
    # matriz[6][0] = 6
    # matriz[0][1] = 7
    # matriz[1][1] = 8
    # matriz[2][1] = 9
    # matriz[3][1] = 15*andar
    # matriz[4][1] = 11
    # matriz[5][1] = 12
    # matriz[6][1] = 13
    # matriz[0][2] = 14
    # matriz[1][2] = 15*andar
    # matriz[2][2] = 16
    # matriz[3][2] = 17
    # matriz[4][2] = 18
    # matriz[5][2] = 19
    # matriz[6][2] = 20
    # matriz[0][3] = 21
    # matriz[1][3] = 22
    # matriz[2][3] = 23
    # matriz[3][3] = 24
    # matriz[4][3] = 25
    # matriz[5][3] = 26
    # matriz[6][3] = 27
    # matriz[0][4] = 28
    # matriz[1][4] = 29
    # matriz[2][4] = 30
    # matriz[3][4] = 31
    # matriz[4][4] = 32
    # matriz[5][4] = 33
    # matriz[6][4] = 34
    
    # Percorrendo a matriz
for x in range(7):
    for y in range(5):
        valor = matriz[x][y]
        # Verifica o valor na posição atual e orienta o robô de acordo
        if valor == 1:
            # Orienta o robô para a direita
            pass
        elif valor == 2:
            # Orienta o robô para a esquerda
            pass
        elif valor == 3:
            # Orienta o robô para a direita
            pass
        elif valor == 4:
            # Orienta o robô para a esquerda
            pass
        elif valor == 5:
            # Orienta o robô para a direita
            pass
        elif valor == 6:
            # Orienta o robô para a esquerda
            pass
        elif valor == 7:
            # Orienta o robô para a direita
            pass
        elif valor == 8:
            # Orienta o robô para a esquerda
            pass
            

arenax = [0, 1, 2, 3, 4, 5, 6]
arenay = [0, 1, 2, 3, 4]
pos_robot=[arenax,arenay]

ultima_cor1 = None
ultima_cor2 = None
print("inicio")
while True:
    r1,g1,b1 = CS1.rgb
    cor_mais_proxima1 = encontrar_cor_mais_proxima(r1,g1,b1, cores1)

    r2,g2,b2 = CS2.rgb
    cor_mais_proxima2 = encontrar_cor_mais_proxima(r2,g2,b2, cores2)
    init()
    ultima_cor1 = cor_mais_proxima1
    ultima_cor2 = cor_mais_proxima2
    # leitura += 1
    # print('')
    # print("leitura numero: {}".format(leitura))
    # print('')
    # r1,g1,b1 = CS1.rgb
    # cor_mais_proxima1 = encontrar_cor_mais_proxima(r1,g1,b1, cores1)
    # print("A cor mais proxima lida pelo sensor CS1 e: {}".format(cor_mais_proxima1))

    # r2,g2,b2 = CS2.rgb
    # cor_mais_proxima2 = encontrar_cor_mais_proxima(r2,g2,b2, cores2)
    # print("A cor mais proxima lida pelo sensor CS2 e: {}".format(cor_mais_proxima2))
    # print('')
    # print('')
    # print(CS1.rgb)
    # print(CS2.rgb)
    # print('---------------------------------')
    # time.sleep(2)