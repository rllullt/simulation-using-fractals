# -*- coding= utf-8 -*-

'''
Clase Controlador
Recibe puntero al sistema de objetos y los modifica según input del usuario
'''

# Se importan las librerías
import pygame
from pygame.locals import *

# Clase Controlador
# Campos:
# modelos (provoca interacciones entre objetos): Modelos
# vista (encargada de la vista de la simulación): Vista
class Controlador:
    # Constructor
    def __init__(self, modelos, vista):
        self.modelos= modelos
        self.vista= vista

    # chequearInput: None -> None
    # Efecto: provoca acciones en la escena dado el input del usuario
    def chequearInput(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    exit()
                elif event.key == K_a:
                    self.modelos.generarArbol()
                elif event.key == K_SPACE:
                    self.modelos.lanzarRayo()
                elif event.key == K_m:
                    self.modelos.lanzarMuchosRayos()
