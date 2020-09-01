# -*- coding: utf-8 -*-

'''
Clase Arbol
Crea un árbol fractal
'''

import random
import math
import numpy as np
from OpenGL.GL import *

# Clase Arbol
# Campos:
# puntosBorde (puntos donde se pueden ubucar árboles): arreglo numpy
# dh (espaciado de los puntosBorde): int
# altoEscena (alto de la escena): int
# vida (cantidad de vida del árbol): int
# x_pos (posición horizontal absoluta en la escena): int
# y_pos (posición vertical absoluta en la escena): int
# orden (para dibujar el fractal): int
# ancho (grueso del tronco): int
class Arbol:
    # Constructor:
    def __init__(self, suelo, altoEscena):
        # Condiciones de dibujado
        self.puntosBorde= suelo[0]
        self.dh= suelo[1]
        self.altoEscena= altoEscena
        
        # Resistencia del árbol
        self.vida= 4
        
        # Altura y posición en la escena
        indice= random.randint(0, self.puntosBorde.size-1)
        self.x_pos= indice*self.dh
        self.y_pos= self.puntosBorde[indice]

        # Orden del árbol y el ancho del tronco
        self.orden= random.randint(3, 8)
        self.ancho= self.puntosBorde.size*self.dh/40
        
    # getBlanco: None -> list
    # Retorna una lista con la posición [x, y] donde recibe el impacto
    def getBlanco(self):
        return [self.x_pos, self.y_pos + 3*self.ancho/2]
    
    # atacar: int -> None
    # Le quita vida al árbol según la cantidad ingresada
    def atacar(self, ataque):
        self.vida-= ataque
    
    # estaDebilitado: None -> bool
    # Retorna True si la vida es menor o igual que cero, False si no
    def estaDebilitado(self):
        return self.vida <= 0
    
    # dibujarPitagoras: int int int|float float int -> None
    # Dibuja un árbol de pitágoras de base a de orden n con punto inf. izq. en (x,y)
    # orientado según el ángulo theta
    def dibujarPitagoras(self, x, y, a, angulo, n):
        if n == 0: # es hoja
            # Minetras menos vida, más rojo
            rojo= 1 + (0.1765 - 1)*self.vida/4
            glColor3f(rojo, 0.3412, 0.1725) # verde hoja
        else: # es tronco
            rojo= 1 + (0.3569 - 1)*self.vida/4
            glColor3f(rojo, 0.2275, 0.1608) # pardo nuez
        
        # Dibujar la base. Se dibujará la figura en el origen y se montará donde corresponda
        
        # Matriz de traslación de la figura
        T= np.array([[1, 0, x],
                      [0, 1, y],
                      [0, 0, 1]])
        
        # Matriz de rotación de la figura
        R= np.array([[math.cos(angulo), -math.sin(angulo), 0],
                      [math.sin(angulo), math.cos(angulo), 0],
                      [0, 0, 1]])
        
        # Se calculan los vectores de puntos
        # Cada fila de esta matriz son las coordenadas x, y y z del punto a trasladar
        # Se anotó así solo para entender mejor el código (para trabajarla es necesario transponerla)
        v= np.array([[0, 0, 1],
                     [a, 0, 1],
                     [a, a, 1],
                     [a/2, 3*a/2, 1],
                     [0, a, 1]])
        v= T.dot(R).dot(np.transpose(v))
       
        # Se calculan los puntos
        # Primera fila: valores para x
        # Segunda fila: valores para y
        x0, y0= int(round(v[0][0])), int(round(v[1][0]))
        x1, y1= int(round(v[0][1])), int(round(v[1][1]))
        x2, y2= int(round(v[0][2])), int(round(v[1][2]))
        x3, y3= int(round(v[0][3])), int(round(v[1][3]))
        x4, y4= int(round(v[0][4])), int(round(v[1][4]))
        
        # Se dibuja el pilígono
        glBegin(GL_POLYGON)
        glVertex2f(x0, y0)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glVertex2f(x3, y3)
        glVertex2f(x4, y4)
        glEnd()
        
        # Dibujar ramas si lo amerita
        if n != 0:
            # Dibujar a ambos lados recursivamente
            self.dibujarPitagoras(x4, y4, a*math.sqrt(2)/2, angulo + math.pi/4, n-1)
            self.dibujarPitagoras(x3, y3, a*math.sqrt(2)/2, angulo - math.pi/4, n-1)
    
    # dibujar: None -> None
    # Dibuja el árbol fractal
    def dibujar(self):
        self.dibujarPitagoras(self.x_pos-self.ancho/2, self.y_pos, self.ancho, 0, self.orden)
        
