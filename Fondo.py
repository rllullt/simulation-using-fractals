# -*- coding: utf-8 -*-

'''
Clase Fondo
Le da color al fondo del juego
'''

from OpenGL.GL import *

# Clase Fondo
# Campos:
# anchoEscena (ancho de la escena): int
# altoEscena (alto de la escena): int
# alturaCumulo (altura a la que cambia de color por cúmulo de nubes): int
# alturaSuelo (la altura de la tierra): int
class Fondo:
    # Constructor
    def __init__(self, anchoEscena, altoEscena):
        self.anchoEscena= anchoEscena
        self.altoEscena= altoEscena
        self.alturaCumulo= 5*self.altoEscena/6
        self.alturaSuelo= self.altoEscena/3
        
    def dibujar(self):
        # El fondo consta de 3 partes:
        glBegin(GL_QUADS)
        
        # 1. Cúmulo de nubes en la parte superior
        # Va desde arriba y tiene grosor 1/6 del alto de la escena        
        glColor3f(0.2, 0.1843, 0.1725) # gris sombra
        glVertex2f(0, self.altoEscena)
        glVertex2f(self.anchoEscena, self.altoEscena)
        # Se genera el degradé
        glColor3f(0.5451, 0.549, 0.4784) # gris piedra
        glVertex2f(self.anchoEscena, self.alturaCumulo)
        glVertex2f(0, self.alturaCumulo)
        
        # 2. Cielo en general
        # Se conserva el color anterior
        glVertex2f(0, self.alturaCumulo)
        glVertex2f(self.anchoEscena, self.alturaCumulo)
        glVertex2f(self.anchoEscena, self.alturaSuelo)
        glVertex2f(0, self.alturaSuelo)
        
        # 3. Bajo el nivel del suelo, agua (si se da)
        glColor3f(0.1451, 0.4275, 0.4824) # azul agua
        glVertex2f(0, self.alturaSuelo)
        glVertex2f(self.anchoEscena, self.alturaSuelo)
        glVertex2f(self.anchoEscena, 0)
        glVertex2f(0, 0)
        
        glEnd()