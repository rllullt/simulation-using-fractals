''' Inicializador de OpenGL para dibujar linea '''

from OpenGL.GL import *
from OpenGL.GLU import *

def init_opengl(ancho, alto):
	# Inicializar OpenGL
	glViewport(0, 0, ancho, alto)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0, ancho, 0.0, alto)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	
	# Definir variables de OpenGL
	glClearColor(0.0, 0.0, 0.0, 0.0) # color de fondo
	glShadeModel(GL_SMOOTH)
	glClearDepth(1.0)
	# glDisable(GL_DEPTH_TEST)
	return
