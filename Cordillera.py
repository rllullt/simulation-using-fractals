# -*- coding: utf-8 -*-

'''
Clase Cordillera
Ocupa el método de desplazamiento del punto medio para generar un paseo aleatorio similar al browniano
'''

# random.gauss(mu, sigma)
# Gaussian distribution. mu is the mean, and sigma is the standard deviation.

import random
import numpy as np
from OpenGL.GL import *

# Clase Cordillera
# Campos:
# anchoEscena (ancho de la escena): int
# altoEscena (alto de la escena): int
# alturaSuelo (la altura de la tierra): int
# s (factor de rugosidad): int
# dh (espaciado de la malla, cada cuántos pixeles habrá un punto crítico): int
# ini (coordenada en x del punto crítico donde comenzará a dibujarse el cerro): int
# fin (coordenada en x del punto crítico donde terminará de dibujarse el cerro)
# altura (alto predefinido para controlar la altitud de la cordillera): int
# puntosBorde (puntos de borde): arreglo numpy
# alturaMaxima (coordenadas del punto de máxima altura): list
class Cordillera:
    # Constructor:
    def __init__(self, anchoEscena, altoEscena):
        # Parámetros máximos
        self.anchoEscena= anchoEscena
        self.altoEscena= altoEscena
        self.alturaSuelo= self.altoEscena/3
        
        # Factor de rugosidad de la superficie
        self.s= 1.0
        
        # Espaciado de la malla
        self.dh= 5
        
        # Calcula el ancho que tendrá la montaña de la cordillera
        # ini estará entre el primer quinto y la mitad de pantalla
        self.ini= random.randint(self.anchoEscena/5, self.anchoEscena/2)
        
        # fin estará entre ini + un tercio de pantalla (máximo 5/6 de pantalla) y el final
        self.fin= random.randint(self.ini+self.anchoEscena/3, self.anchoEscena)
        
        # Calcula el alto que tendrá la cordillera
        # Será entre 4/6 y 5/6 de la altura de la escena
        self.altura= random.randint(2*self.altoEscena/3, 5*self.altoEscena/6)
        
        # Puntos borde
        # el i-ésimo elemento corresponte a la coordenada y, i corresponde a x
        # Ej. puntosBorde[2]= 3 significa que es el par (2,3)
        self.puntosBorde= self.calcularPuntos() # la numeración va de 0 a anchoEscena
        
        self.alturaMaxima= self.calcularPuntoMaximo() # calcula el punto más alto
    
    # Métodos
    
    # calcularPuntos: None -> arreglo
    # Retorna la lista puntosBorde ubicando las coordenas en x e y de cada punto a dibujar
    # La lista tiene listas de pares representando cada x e y.
    def calcularPuntos(self):
        puntosBorde= np.zeros(self.anchoEscena/self.dh + 1)
        
        # La altura mínima de la cordillera será altoEscena/3
        # Todos los puntos anteriores a ini son planos (incluyendo ini)
        for i in range(self.ini/self.dh+1):
            puntosBorde[i]= self.alturaSuelo
        # Todos los puntos posteriores a fin son planos (incluyendo fin)
        for i in range(self.fin/self.dh, self.anchoEscena/self.dh+1):
            puntosBorde[i]= self.alturaSuelo
        
        # Se calculan los puntos en el cerro
        # Se busca valor de 'x' para altura máxima
        if (self.fin - self.ini > 2*self.dh):
            al= int(round(random.gauss((self.fin+self.ini)/2, self.dh))) # valor cercano a la mitad
            if (self.ini < al < self.fin):
                x_altura= al
            else:
                x_altura= random.randint(self.ini+self.dh, self.fin-self.dh)
        else:
            x_altura= random.randint(self.ini, self.fin)
        puntosBorde[x_altura/self.dh]= self.altura
        # Se calculan recursivamente los valores para el paseo aleatorio
        puntosBorde= self.calcularPuntosCerro(puntosBorde, self.ini/self.dh, x_altura/self.dh, self.fin/self.dh)
        return puntosBorde
    
    # calcularPuntosCerro: arreglo int int int -> arreglo
    # Recibe una lista con puntos de borde incompleta y retorna otra completa
    def calcularPuntosCerro(self, puntosBorde, i, medio, j):
        puntosBorde= self.calcularPuntosMedios(puntosBorde, i, medio)
        puntosBorde= self.calcularPuntosMedios(puntosBorde, medio, j)
        return puntosBorde
    
    # calcularPuntosMedios: arreglo int int -> arreglo
    # Recibe una lista y dos valores extremos, y determina el valor "y" de altura del punto medio entre ellos
    def calcularPuntosMedios(self, puntosBorde, i, j):
        if (j-i) <= 1: # Caso base, no hay más puntos medios
            return puntosBorde
        medio= (i+j)/2
        r= self.s*random.gauss(0,1)*abs(j-i)
        puntosBorde[medio]= round(0.5*(puntosBorde[i] + puntosBorde[j]) + r)
        puntosBorde= self.calcularPuntosMedios(puntosBorde, i, medio)
        puntosBorde= self.calcularPuntosMedios(puntosBorde, medio, j)
        return puntosBorde
                
    # calcularPuntoMaximo: None -> lista
    # Retorna las coordenadas del punto más alto del cerro
    def calcularPuntoMaximo(self):
        # Se busca el punto de altura máxima
        x_max= 0
        y_max= self.puntosBorde[0]
        for i in range(1, self.puntosBorde.size):
            if (y_max < self.puntosBorde[i]):
                y_max= self.puntosBorde[i]
                x_max= i
        return [x_max, y_max]
    
    # getPuntosBorde: None -> list
    # Retorna la lista de puntos de borde para permitir el dibujo de árboles
    def getPuntosBorde(self):
        return [self.puntosBorde, self.dh]
    
    # getAlturaMaxima: None -> [int, int]
    # Retorna un par con la coordenada x y la y de la altura máxima en el cerro
    def getAlturaMaxima(self):
        return self.alturaMaxima

    # dibujar: None -> None
    # Genera el dibujo para proyectarlo en la simulación
    def dibujar(self):
        glColor3f(0.3059, 0.2314, 0.1922) # café tierra
        
        for i in range(self.puntosBorde.size-1):
            glBegin(GL_POLYGON) # Dibujará polígonos de 4 lados (como la integral de Riemann!)
            glVertex2f(i*self.dh, self.puntosBorde[i])
            glVertex2f(i*self.dh, 0)
            glVertex2f((i+1)*self.dh, 0)
            glVertex2f((i+1)*self.dh, self.puntosBorde[i+1])
            glEnd()
        
        
