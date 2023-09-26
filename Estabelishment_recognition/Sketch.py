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

Sem_cor = 0
Preto = 1
Azul = 2
Verde = 3
Amarelo = 4
Vermelho = 5
Branco = 6
Marrom = 7

def zona_de_embarque():
    if zona_de_embarque(True):
        tank_drive.off()
        tank_drive.on_for_rotations(-5,-5, 0.5)
        tank_drive.on_for_rotations(5,-5, 0.5)
        tank_drive.on_for_rotations(5,5, 0.5)
        tank_drive.on_for_rotations(-5,5, 1)
    return embarque(True)

def embarque():
    if embarque(True):
        while US > 10:
            tank_drive.on(20,20)
        if US < 10:
            tank_drive.off()
            tank_drive.on_for_rotations(5,-5, 0.5)
            tank_drive.on_for_rotations(5,5, 0.5)
            if IRS < 6 and CS3 == True:
                return Adultos(True)
            elif IRS > 6 and CS3 == True:
                return Criancas(True)
            else:
                return 

# Reconhece se é adulto ou criança            
def Adultos():
    if Adultos(True):
        if CS3 == Vermelho:
            return Drugstore(True)
        if CS3 == Verde:
            return City_hall(True)
        if CS3 == Azul:
            return Museum(True)
        if CS3 == Marrom:
            return Bakery(True)
        else:
            return False

def Criancas(x):
    if Criancas(True):
        if CS3 == Vermelho:
            return Drugstore()
        if CS3 == Verde:
            return Park()
        if CS3 == Azul:
            return School()
        if CS3 == Marrom:
            return Library()
        else:
            return False
    
# Cria uma função para cada estabelecimento
def Drugstore():
    if Drugstore(True):
        tank_drive.on_for_rotations(5,5, 10) # Andou até o meio da primeira rua
        tank_drive.on_for_rotations(-5,5, 0.5) # Virou para a esquerda
        tank_drive.on_for_rotations(5,5, 40) # Andou até a última rua antes do parque
        tank_drive.on_for_rotations(5,-5, 0.5) # Virou para a direita
        tank_drive.on_for_rotations(5,5, 10) # Andou até o meio da rua
        tank_drive.on_for_rotations(5,-5, 0.5) # Virou para a direita
        tank_drive.on_for_rotations(5,5, 10) # Entrou no estabelecimento
        # Desembarque do passageiro
        tank_drive.on_for_rotations(-5,-5, 10) # Saiu do estabelecimento
        tank_drive.on_for_rotations(5,-5, 0.5) # Virou para a direita
        tank_drive.on_for_rotations(5,5, 10) # Andou até o meio da rua
        tank_drive.on_for_rotations(-5,5, 0.5) # Virou para a esquerda
        tank_drive.on(20,20) # Anda até achar a zona de embarque
        if CS1 and CS2 == Azul:
            return zona_de_embarque(True)

def City_hall():
    if City_hall(True):
        tank_drive.on_for_rotations(5,5, 10) # Andou até o meio da primeira rua
        tank_drive.on_for_rotations(-5,5, 0.5) # Virou para a esquerda
        tank_drive.on_for_rotations(5,5, 20) # Andou até a última rua antes do parque
        tank_drive.on_for_rotations(5,-5, 0.5) # Virou para a direita
        tank_drive.on_for_rotations(5,5, 10) # Andou até o meio da rua
        tank_drive.on_for_rotations(5,-5, 0.5) # Virou para a direita
        tank_drive.on_for_rotations(5,5, 10) # Entrou no estabelecimento
        # Desembarque do passageiro
        tank_drive.on_for_rotations(-5,-5, 10) # Saiu do estabelecimento
        tank_drive.on_for_rotations(5,-5, 0.5) # Virou para a direita
        tank_drive.on_for_rotations(5,5, 10) # Andou até o meio da rua
        tank_drive.on_for_rotations(-5,5, 0.5) # Virou para a esquerda
        tank_drive.on(20,20) # Anda até achar a zona de embarque
        if CS1 and CS2 == Azul:
            return zona_de_embarque(True)

def Museum():
    if Museum(True):
        tank_drive.on_for_rotations(5,5, 10) # Andou até o meio da primeira rua
        tank_drive.on_for_rotations(-5,5, 0.5) # Virou para a esquerda
        tank_drive.on_for_rotations(5,5, 30) # Andou até a última rua antes do parque
        tank_drive.on_for_rotations(-5,5, 0.5) # Virou para a esquerda
        tank_drive.on_for_rotations(5,5, 10) # Entrou no estabelecimento
        # Desembarque do passageiro
        tank_drive.on_for_rotations(-5,-5, 10) # Saiu do estabelecimento
        tank_drive.on_for_rotations(-5,5, 0.5) # Virou para a esquerda
        tank_drive.on_for_rotations(5,5, 10) # Andou até o meio da rua
        tank_drive.on_for_rotations(-5,5, 0.5) # Virou para a esquerda
        tank_drive.on(20,20) # Anda até achar a zona de embarque
        if CS1 and CS2 == Azul:
            return zona_de_embarque(True) 
        
def Bakery():
    if Bakery(True):
        tank_drive.on_for_rotations(5,5, 10) # Andou até o meio da primeira rua
        tank_drive.on_for_rotations(-5,5, 0.5) # Virou para a esquerda
        tank_drive.on_for_rotations(5,5, 40) # Andou até a última rua antes do parque
        tank_drive.on_for_rotations(5,-5, 0.5) # Virou para a direita
        tank_drive.on_for_rotations(5,5, 30) # Andou até o meio da rua
        tank_drive.on_for_rotations(5,-5, 0.5) # Virou para a direita
        tank_drive.on_for_rotations(5,5, 10) # Entrou no estabelecimento
        # Verifica se entrou no estabelecimento e faz o esembarque do passageiro
        tank_drive.on_for_rotations(-5,-5, 10) # Saiu do estabelecimento
        tank_drive.on_for_rotations(5,-5, 0.5) # Virou para a direita
        tank_drive.on_for_rotations(5,5, 10) # Andou até o meio da rua
        tank_drive.on_for_rotations(-5,5, 0.5) # Virou para a esquerda
        tank_drive.on(20,20) # Anda até achar a zona de embarque
        if CS1 and CS2 == Azul:
            return zona_de_embarque(True)

def Park():
    if Park(True):
        tank_drive.on_for_rotations(5,5, 10) # Andou até o meio da primeira rua
        tank_drive.on_for_rotations(-5,5, 0.5) # Virou para a esquerda
        tank_drive.on_for_rotations(5,5, 40) # Andou até a última rua antes do parque
        tank_drive.on_for_rotations(5,-5, 0.5) # Virou para a direita
        tank_drive.on_for_rotations(5,5, 10) # Andou até o meio da rua
        tank_drive.on_for_rotations(-5,5, 0.5) # Virou para a esquerda
        tank_drive.on_for_rotations(5,5, 10) # Entrou no estabelecimento
        # Verifica se entrou no estabelecimento e faz o esembarque do passageiro
        tank_drive.on_for_rotations(-5,-5, 10) # Saiu do estabelecimento
        tank_drive.on_for_rotations(-5,5, 0.5) # Virou para a esquerda
        tank_drive.on_for_rotations(5,5, 10) # Andou até o meio da rua
        tank_drive.on_for_rotations(-5,5, 0.5) # Virou para a esquerda
        tank_drive.on(20,20) # Anda até achar a zona de embarque
        if CS1 and CS2 == Azul:
            return zona_de_embarque(True)

def School():
    if School(True):
        tank_drive.on_for_rotations(5,5, 30) # Andou até o meio da primeira rua
        tank_drive.on_for_rotations(-5,5, 0.5) # Virou para a esquerda
        tank_drive.on_for_rotations(5,5, 10) # Andou até a última rua antes do parque
        tank_drive.on_for_rotations(5,-5, 0.5) # Virou para a direita
        tank_drive.on_for_rotations(5,5, 10) # Entrou no estabelecimento
        # Verifica se entrou no estabelecimento e faz o esembarque do passageiro
        tank_drive.on_for_rotations(-5,-5, 10) # Saiu do estabelecimento
        tank_drive.on_for_rotations(5,-5, 0.5) # Virou para a direita
        tank_drive.on(20,20) # Anda até achar a zona de embarque
        if CS1 and CS2 == Azul:
            return zona_de_embarque(True)

def Library():
    if Library(True):
        tank_drive.on_for_rotations(-5,5, 0.5) # Virou para a esquerda
        tank_drive.on_for_rotations(5,5, 10) # Entrou no estabelecimento
        # Verifica se entrou no estabelecimento e faz o esembarque do passageiro
        tank_drive.on_for_rotations(-5,-5, 10) # Saiu do estabelecimento
        tank_drive.on_for_rotations(-5,5, 1) # Virou para a esquerda
        tank_drive.on(20,20) # Anda até achar a zona de embarque
        if CS1 and CS2 == Azul:
            return zona_de_embarque(True)
        

def init():
    if CS1 and CS2 == Branco:
        tank_drive.on(20,20)
        if CS1 and CS2 == Azul: 
            zona_de_embarque(True)
        elif CS1 == Azul and CS2 == Branco:
            tank_drive.off()
            while CS1 == Azul and CS2 != Azul:
                tank_drive.on(-5,5)
        elif CS1 == Branco and CS2 == Azul:
            tank_drive.off()
            while CS1 != Azul and CS2 == Azul:
                tank_drive.on(5,-5)
        elif CS1 and CS2 == Preto:
            tank_drive.off()
            tank_drive.on_for_rotations(-5,-5, 0.5)
            tank_drive.on_for_rotations(5,-5, 0.5)
        elif CS1 == Preto and CS2 == Amarelo:
            tank_drive.off()
            tank_drive.on_for_rotations(-5,-5, 0.5)
            tank_drive.on_for_rotations(5,-5, 0.5)
        elif CS1 == Amarelo and CS2 == Preto:
            tank_drive.off()
            tank_drive.on_for_rotations(-5,-5, 0.5)
            tank_drive.on_for_rotations(5,-5, 0.5)
        
        
            
            
            
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
    if color_sensor1.color == 6 and color_sensor2.color == 6:
        tank_drive.on(20,20)
        if color_sensor1.color == 2 and color_sensor2.color == 2:
            tank_drive.off()
            tank_drive.on_for_rotations(-5,-5, 0.5)
            
            
            initial_position = True 
        initial_position = True

    initial_position = True
    
def init(x, y):
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
    # matriz[3][1] = 10
    # matriz[4][1] = 11
    # matriz[5][1] = 12
    # matriz[6][1] = 13
    # matriz[0][2] = 14
    # matriz[1][2] = 15
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
