# -*- coding: utf-8 -*-

'''
Clase Rayo
Crea un rayo fractal
'''

import random
import math
import numpy as np
from OpenGL.GL import *

# Clase Rayo
# Campos:
# x_ini, y_ini (posición inicial del rayo): int, int
# x_fin, y_fin (posición final del rayo): int, int
# t (tiempo de vida del rayo)
# dh (espaciado de la malla): int
# s (factor de rugosidaad): int
# puntos (posiciones donde se dibujará): int
class Rayo:
    # Constructor:
    def __init__(self, pos_nube, pos_arbol):
        # Posiciones de inicio y fin
        self.x_ini= pos_nube[0]
        self.y_ini= pos_nube[1]
        self.x_fin= pos_arbol[0]
        self.y_fin= pos_arbol[1]
        
        if self.x_ini > self.x_fin:
            self.x_ini, self.x_fin= self.x_fin, self.x_ini
            self.y_ini, self.y_fin= self.y_fin, self.y_ini

        # Tiempos
        self.t= 0 # se originó recién
        self.t_fin= 0.4 # tiempo de duración del rayo
        
        # Espaciado de la malla
        self.dh= 5
        
        # Factor de rugosidad del rayo
        self.s= 1.2
        
        # Puntos donde se dibujará
        if self.x_ini == self.x_fin or self.x_ini/self.dh == self.x_fin/self.dh:
            self.puntos= np.array([self.y_ini, self.y_fin])
        else:
            self.puntos= self.calcularPuntos()
        
    # calcularPuntos: None -> arreglo
    # Retorna la lista puntos ubicando las coordenas en x e y de cada punto a dibujar
    # La lista tiene listas de pares representando cada x e y.
    def calcularPuntos(self):
        dx= self.x_fin - self.x_ini
        puntos= np.zeros(dx/self.dh + 1) # el "ancho" del rayo en índices
        puntos[0]= self.y_ini
        puntos[puntos.size-1]= self.y_fin
        
        # Se calculan recursivamente los valores para el paseo aleatorio
        puntos= self.calcularPuntosMedios(puntos, 0, puntos.size-1)
        return puntos
        
    # calcularPuntosMedios: arreglo int int -> arreglo
    # Recibe una lista y dos valores extremos, y determina el valor "y" de altura del punto medio entre ellos
    def calcularPuntosMedios(self, puntos, i, j):
        if (j-i) <= 1: # Caso base, no hay más puntos medios
            return puntos
        medio= (i+j)/2
        r= self.s*random.gauss(0,1)*abs(j-i)
        puntos[medio]= round(0.5*(puntos[i] + puntos[j]) + r)
        puntos= self.calcularPuntosMedios(puntos, i, medio)
        puntos= self.calcularPuntosMedios(puntos, medio, j)
        return puntos
        
    # actualizar: float -> None
    # Le actualiza el tiempo de vida al rayo
    def actualizar(self, dt):
        self.t+= dt
    
    # estaDebilitado: None -> bool
    # Retorna True si el rayo ya cumplió su ciclo de vida, False si no
    def estaDebilitado(self):
        return self.t >= self.t_fin
    
    def dibujar(self):
        #glColor3f(0.2313, 0.5137, 0.7411) # azul luminoso
        glColor3f(1.0, 1.0, 0) # amarillo luminoso
        glLineWidth(3.0) # grosor en pixeles de la linea
        glBegin(GL_LINE_STRIP)
        for i in range(self.puntos.size-1):
            glVertex2f(self.x_ini + i*self.dh, self.puntos[i])
        glEnd()
        
        
        
        
