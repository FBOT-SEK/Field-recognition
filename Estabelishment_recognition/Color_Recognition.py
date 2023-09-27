#!/usr/bin/env python3

#Importa as bibliotecas necessarias
import time # importando o tempo para a logica de programacao
import math # importando a matematica para a logica de programaaao
from ev3dev2.motor import * # importando tudo da biblioteca ev3dev2.motor
from ev3dev2.sound import Sound # importando o som da biblioteca ev3dev2.sound
from ev3dev2.button import Button # importando os botoes da biblioteca ev3dev2.button
from ev3dev2.sensor import * # importando tudo da biblioteca ev3dev2.sensor
from ev3dev2.sensor.lego import * # importando tudo da biblioteca ev3dev2.sensor.lego
from variaves import *
#from ev3dev2.sensor.virtual import * # importando tudo da biblioteca ev3dev2.sensor.virtual

CS1 = ColorSensor(INPUT_1)  # setando sensor de cor na entrada 
CS2 = ColorSensor(INPUT_2) # setando sensor de cor na entrada 

CS1.mode = 'RGB-RAW'
CS2.mode = 'RGB-RAW'




#Aqui é onde seus codigos começam

#Funções
corCS1 = 0
Ab = [0,0,0]
Au = [0,0,0]

def ajustes():
    global Ab, Au

    print("Coloque no branco")
    time.sleep(5)
    CS1.calibrate_white()
    print("Parametros iniciais concluidos")
    Ab = CS1.rgb
    print(Ab)
    for i in range(2):
        Ab = list(Ab)
        r, g, b = CS1.rgb
        Ab[0] = Ab[0] + r
        Ab[1] = Ab[1] + g
        Ab[2] = Ab[2] + b
    print(Ab)
    Ab[0] = Ab[0] / 3
    Ab[1] = Ab[1] / 3
    Ab[2] = Ab[2] / 3
    Ab = tuple(Ab)
    print(Ab)
    time.sleep(5)
    print("Coloque no azul")
    time.sleep(5)
    Au = CS1.rgb
    print(Au)
    for i in range(2):
        Au = list(Au)
        r, g, b = CS1.rgb
        Au[0] = Au[0] + r
        Au[1] = Au[1] + g
        Au[2] = Au[2] + b
    print(Au)
    Au[0] = Au[0] / 3
    Au[1] = Au[1] / 3
    Au[2] = Au[2] / 3
    Au = tuple(Au)
    print(Au)
    print("Parametros finais concluidos")
    
ajustes()
while True:
#def qualCor1():
    if (math.isclose(CS1.rgb[0], Au[0], rel_tol=1) == True, 
        math.isclose(CS1.rgb[1], Au[1], rel_tol=1) == True,
        math.isclose(CS1.rgb[2], Au[2], rel_tol=1) == True):
        corCS1 = 2
    if (math.isclose(CS1.rgb[0], Ab[0], rel_tol=1) == True, 
        math.isclose(CS1.rgb[1], Ab[1], rel_tol=1) == True,
        math.isclose(CS1.rgb[2], Ab[2], rel_tol=1) == True):
        corCS1 = 6
    #if (cor1 >= verdeMin1 and cor1 <= verdeMax1):
    #    corCS1 = 3
    #if (cor1 >= marromMin1 and cor1 <= marromMax1):
    #    corCS1 = 7
    #if (cor1 >= pretoMin1 and cor1 <= pretoMax1):
    #    corCS1 = 1
    #if (corr >= vermelho1[1] and corr <= vermelho1[2] and
    #    corg >= vermelho1[3] and corg <= vermelho1[4] and
    #    corb >= vermelho1[5] and corb <= vermelho1[6]):
    #    corCS1 = 5
    #if (cor1 >= amareloMin1 and cor1 <= amareloMax1):
    #    corCS1 = 4
    
    #print(corr, corg, corb)
    print(corCS1)
    print("Branco")
    print(Ab[0], Ab[1], Ab[2])
    print("Azul")
    print(Au[0], Au[1], Au[2])
    print(CS1.rgb)
    time.sleep(10)