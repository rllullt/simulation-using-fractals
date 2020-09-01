''' Inicializador de pygame para dibujarLinea '''

import pygame
from pygame.locals import *

def init_pygame(w, h, title):
	pygame.init()
	pygame.display.set_mode((w,h), OPENGL | DOUBLEBUF)
	pygame.display.set_caption(title)