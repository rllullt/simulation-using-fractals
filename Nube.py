# -*- coding: utf-8 -*-

'''
Clase Nube
Crea una nube fractal
'''

import random
import math
import numpy as np
from OpenGL.GL import *

# Clase Nube
# Campos:
# anchoEscena (ancho de la escena): int
# altoEscena (alto de la escena): int
# alturaCumulo (altura de los cúmulos): int
# x (posición central de la nube en eje x): int
# y (posición central de la nube en eje y): int
# ancho (ancho de la nube): int
# alto (alto de la nube): int
# radio (para los círculos que conforman la nube): int
# s (rugosidad de la nube): int
# posiciones (arreglo matricial con los centros de los círculos): int
# sumador (cantidad a desplazar la nube): float
class Nube:
    # Constructor:
    def __init__(self, anchoEscena, altoEscena):
        self.anchoEscena= anchoEscena
        self.altoEscena= altoEscena
        self.alturaCumulo= 5*self.altoEscena/6
        
        # Se generan las coordenadas centrales de la nube
        self.x= random.randint(0, self.anchoEscena)
        self.y= random.randint(self.alturaCumulo, 8*self.altoEscena/9)
        
        # Se crean las dimensiones de la nube
        self.ancho= random.randint(self.anchoEscena/7, self.anchoEscena/5)
        self.alto= random.randint(self.altoEscena/7, self.altoEscena/5)
        
        # Se crea un radio para los círculos
        self.radio= random.randint(self.ancho/10, self.ancho/5)
        
        # Rugosidad de la nube
        self.s= random.randint(1, 2)
        
        # Se genera una matriz con las posiciones x e y de los círculos en la nube
        self.posiciones= self.calcularPosiciones()
        
        # Variable para saber si la nube va hacia la izquierda o la derecha
        a= random.randint(0, 1)
        if a == 0:
            a = -1
        self.sumador= a*2.0
        
    # calcularPosiciones: None -> arreglo matriz
    # Retorna una matriz con las coordenadas de cada círculo generador de la nube
    def calcularPosiciones(self):
        # Se crea matriz de ceros con los valores para x en [0] y para y en los otros
        numFilas= self.alto/self.radio
        numColumnas= self.ancho/self.radio
        coordenadas= np.zeros((numFilas+1, numColumnas))
        
        # La coordenadas centrales siempre deben estar
        coordenadas[(numFilas+1)/2][numColumnas/2]= self.y # +1 porque la primera es de las equis
        range1= range(1, (numFilas+1)/2)
        for i in range1:
            for j in range(len(range1)):
                coordenadas[i][numColumnas/2]= self.y - j*self.radio
        range2= range((numFilas+1)/2+1, numFilas+1)
        for i in range2:
            for j in range(len(range2)):
                coordenadas[i][numColumnas/2]= self.y + j*self.radio
        
        # Las coordenadas de los bordes siempre deben estar son iguales entre ellas
        valor= self.y + random.randint(-200,200)/100*self.radio # entre -2 y 2 con decimales
        for i in range(1, numFilas+1):
            coordenadas[i][0]= valor
        valor= self.y + random.randint(-200,200)/100*self.radio # entre -2 y 2 con decimales
        for i in range(1, numFilas+1):
            coordenadas[i][numColumnas-1]= valor
        
        # Se ubican las posiciones de x
        for j in range(coordenadas.shape[1]):
            coordenadas[0][j]= self.x-self.ancho/2 + j*self.radio
        
        # Se calculan las posiciones de los círculos
        for i in range(1, numFilas+1): # por fila, exceptuando la primera
            coordenadas[i]= self.calcularPuntosMedios(coordenadas[i], 0, numColumnas/2)
            coordenadas[i]= self.calcularPuntosMedios(coordenadas[i], numColumnas/2, numColumnas-1)
        return coordenadas
        
    # calcularPuntosMedios: array int int -> array
    # Calcula las coordenadas de los puntos para dibujar la nube
    def calcularPuntosMedios(self, puntos, i, j):
        if (j-i) <= 1: # Caso base, no hay más puntos medios
            return puntos
        medio= (i+j)/2
        r= self.s*random.gauss(0,1)*abs(j-i)
        puntos[medio]= round(0.5*(puntos[i] + puntos[j]) + r)
        puntos= self.calcularPuntosMedios(puntos, i, medio)
        puntos= self.calcularPuntosMedios(puntos, medio, j)
        return puntos
    
    # getPosicion: None -> list
    # Retorna las coordenadas centrales de la nube
    def getPosicion(self):
        return [int(round(self.x)), self.y]
    
    # actualizar: None -> None
    # Desplaza el centro de la nube,
    # también revisa si ha impactado el centro
    def actualizar(self):
        # Se cambia el signo de sumador si va a la izq y se acabó la escena, o va a la derecha y se acabó la escena
        if ((self.x <= 0) and (self.sumador < 0)) or ((self.x >= self.anchoEscena) and (self.sumador > 0)):
            self.sumador= -self.sumador # se le cambia el signo para que se desplace hacia otro lado
        for j in range(self.posiciones.shape[1]):
            self.posiciones[0][j]+= self.sumador
        self.x+= self.sumador
    
    # dibujar: None -> None
    # Dibuja la nube
    def dibujar(self):
        glColor3f(0.5412, 0.5843, 0.5922) # gris plata (simula nube)
        for i in range(1, self.posiciones.shape[0]):
            for j in range(self.posiciones.shape[1]):
                if self.posiciones[i][j] != 0:
                    glBegin(GL_TRIANGLE_FAN)
                    glVertex2f(self.posiciones[0][j], self.posiciones[i][j]) # es el centro
                    n= 18
                    ang= 2*math.pi/n
                    for k in range(n+1):
                        ang_k= ang*k
                        glVertex2f(self.posiciones[0][j] + self.radio*math.cos(ang_k), self.posiciones[i][j] + self.radio*math.sin(ang_k))
                    glEnd()
        
        glColor3f(0.2, 0.1843, 0.1725) # gris sombra
        glLineWidth(2.0) # grosor en pixeles de la linea
        for i in range(self.posiciones.shape[0]-1, 0, -1):
            for j in range(self.posiciones.shape[1]):
                if self.posiciones[i][j]:
                    glBegin(GL_LINE_STRIP)
                    n= 18
                    ang= -(math.pi/2)/n # cuarto cuadrante
                    for k in range(n+1):
                        ang_k= ang*k
                        glVertex2f(self.posiciones[0][j] + self.radio*math.cos(ang_k), self.posiciones[i][j] + self.radio*math.sin(ang_k))
                    glEnd()
        
        
