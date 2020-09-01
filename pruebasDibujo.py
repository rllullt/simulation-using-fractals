# -*- coding: utf-8 -*-

'''
Tarea 2
Autor: Rodrigo Llull Torres
'''

import os
import random
import math

from init_pygame import *
from init_opengl import *
from OpenGL.GLUT import *
from Cordillera import Cordillera
from Fondo import Fondo
from Arbol import Arbol
from Rayo import Rayo
from Nube import Nube

# Se inicializan Pygame y OpenGL
os.environ["SDL_VIDEO_CENTERED"]= "1" # centra la pantalla

ancho= 800
alto= 600
init_pygame(ancho, alto, "Pruebas de dibujo")
init_opengl(ancho, alto)

objs= []
arboles= []
rayos= []
nubes= []

fondo= Fondo(ancho, alto)
cordillera= Cordillera(ancho, alto)
objs.append(fondo)
objs.append(cordillera)

reloj= pygame.time.Clock()
FPS= 6.0

for i in range(10):
    suelo= cordillera.getPuntosBorde()
    arbol= Arbol(suelo, alto)
    arboles.append(arbol)

for i in range(4):
    nube= Nube(ancho, alto)
    nubes.append(nube)

def lanzarRayo():
    if arboles != []:
        al= random.randint(0, len(arboles)-1)
        arbol= arboles[al]
        arbol.atacar(1)
        al= random.randint(0, len(nubes)-1)
        nube= nubes[al]
        rayo= Rayo(nube.getPosicion(), arbol.getBlanco())
        rayos.append(rayo)
        if arbol.estaDebilitado():
            arboles.remove(arbol)
        print('Atacaste al árbol de blanco '+str(arbol.getBlanco()[0])+','+str(arbol.getBlanco()[1]))
    else:
        print("No hay árboles")
    
def lanzarMuchosRayos():
    al= random.randint(2, 10)
    if al <= len(arboles):
        for i in range(al):
            lanzarRayo()
    else:
        for i in arboles:
            lanzarRayo()
    
run= True
dibujarPunto= False
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run= False
        elif event.type == KEYDOWN:
            if event.key == K_q:
                run= False
            elif event.key == K_a:
                arbol= Arbol(suelo, alto)
                arboles.append(arbol)
            elif event.key == K_SPACE:
                lanzarRayo()
                dibujarPunto= True
            elif event.key == K_m:
                lanzarMuchosRayos()
    
    # Dibujaremos algo de prueba
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # limpia la pantalla
    
    reloj.tick(FPS)
    
    fondo.dibujar()
    cordillera.dibujar()
    
    if arboles != []:
        for arbol in arboles:
            arbol.dibujar()
    
    if rayos != []:
        for rayo in rayos:
            rayo.dibujar()
            rayo.actualizar(1/FPS)
            if rayo.estaDebilitado():
                rayos.remove(rayo)
    
    for nube in nubes:
        nube.dibujar()
        nube.actualizar()
    
    if glutSwapBuffers:
        glutSwapBuffers()
    
    pygame.display.flip()

pygame.quit()
