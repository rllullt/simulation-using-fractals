# -*- coding: utf-8 -*-

'''
Clase Vista
Crea la ventana y llama a Controlador y a los Modelos
'''

# Importación de librerías
import os
from init_pygame import *
from init_opengl import *

# Constantes
FPS= 6.0 # cuadros por segundo
ANCHO_ESCENA= 800
ALTO_ESCENA= 600

# Tiempo [s] que pasa entre cada cuadro:
DT= 1.0/FPS

# Clase Vista
# Campos:
# modelo (los objetos): Modelo
# reloj (para llevar la cuenta del tiempo): Clock
# t (tiempo transcurrido): float
# dt (intervalos de tiempo que se van sumando): float
class Vista:
    # Constructor:
    def __init__(self, modelo):
        # Se guarda el modelo
        self.modelo= modelo
        
        # Se inicializan Pygame y OpenGL
        os.environ["SDL_VIDEO_CENTERED"]= "1" # centra la pantalla
        init_pygame(ANCHO_ESCENA, ALTO_ESCENA, "Pruebas de dibujo")
        init_opengl(ANCHO_ESCENA, ALTO_ESCENA)
        
        # Temporizador (para el tiempo de los rayos)
        self.reloj= pygame.time.Clock()
        self.t= 0.0 # Timepo de simulación
        self.dt= DT
    
    # dibujar: None -> None
    # Genera el dibujo para proyectarlo en la aplicación
    def dibujar(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # limpia la pantalla
        
        # Se ajusta el reloj
        self.reloj.tick(FPS)
        
        # Se define el título de la ventana
        pygame.display.set_caption(u"Simulación con fractales (FPS= {0})".format(int(self.reloj.get_fps())))
        
        # Se actualiza el modelo según el tiempo de la aplicación
        self.modelo.actualizar(self.dt)
        
        # Se dibuja el modelo
        self.modelo.dibujar()
        
        # Se vuelca en la pantalla
        pygame.display.flip()
        
        # Se actualiza el tiempo de la aplicación
        self.t+= self.dt
