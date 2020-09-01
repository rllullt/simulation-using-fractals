# -*- coding= utf-8 -*-

'''
Clase Modelos
Maneja todos los OBJETOS de la aplicación
Revisa sus interacciones
'''

import random

# Importación de la vista
from Vista import ANCHO_ESCENA, ALTO_ESCENA

# Importación de modelos
from Cordillera import Cordillera
from Fondo import Fondo
from Nube import Nube
from Arbol import Arbol
from Rayo import Rayo

# Clase Modelos
# Campos:
# arboles (lista que contiene los árboles): list
# nubes (lista que contiene las nubes): list
# rayos (lista que contiene los rayos): list
# fondo (obj. que rellena la escena): Fondo
# cordillera (obj. que forma la cordillera): Cordillera
class Modelos:
    # Constructor:
    def __init__(self):
        # Listas de objetos
        self.arboles= []
        self.nubes= []
        self.rayos= []
        
        # Crea el fondo y la cordillera
        self.fondo= Fondo(ANCHO_ESCENA, ALTO_ESCENA)
        self.cordillera= Cordillera(ANCHO_ESCENA, ALTO_ESCENA)
        
        # Se crean 4 nubes
        self.generarCuatroNubes()
        
        # Se crean 10 árboles (no más porque con más ya corre muy lento)
        self.generarDiezArboles()
    
    # lanzarRayo: None -> None
    # Lanza un rayo a en la escena, azarosamente
    # Se ejecuta cada vez que el usuario presiona 'SPACE'
    def lanzarRayo(self):
        if self.arboles != []:
            a= random.randint(1, len(self.arboles)+1) # verifica si le llega a un árbol directo o al suelo
        else: # no hay árboles, solo suelo
            a= 1
        if a == 1: # suelo, es menos probable que llegue al suelo que a un árbol
            suelo= self.cordillera.getPuntosBorde()
            al= random.randint(0, len(self.nubes)-1)
            nube= self.nubes[al]
            al= random.randint(0, len(suelo[0])-1) # el largo del arreglo a lo ancho
            coordSuelo= [al*suelo[1], suelo[0][al]] # coords. [x, y]
            rayo= Rayo(nube.getPosicion(), coordSuelo)
            self.rayos.append(rayo)
        else: # árbol
            al= random.randint(0, len(self.arboles)-1)
            arbol= self.arboles[al]
            arbol.atacar(1)
            al= random.randint(0, len(self.nubes)-1)
            nube= self.nubes[al] # desde alguna nube aleatoria
            rayo= Rayo(nube.getPosicion(), arbol.getBlanco()) # Se genera desde alguna nube hasta algún árbol
            self.rayos.append(rayo)
                        
    # lanzarMuchosRayos: None -> None
    # Lanza muchos rayos a diferentes árboles (al azar entre 2 y 10)
    # Se ejecuta cada vez que el usuario presiona 'M'
    def lanzarMuchosRayos(self):
        al= random.randint(2,10)
        for i in range(al):
            self.lanzarRayo()
        
    # generarNube: None -> None
    # Agrega una nube aleatoria a la lista de nubes
    # Solo se ejecuta al inicio
    def generarNube(self):
        nube= Nube(ANCHO_ESCENA, ALTO_ESCENA)
        self.nubes.append(nube)
    
    # generarCuatroNubes: None -> None
    # Agrega 4 nubes aleatorias a la lista de nubes
    # Se ejecuta al inicio
    def generarCuatroNubes(self):
        for i in range(4):
            self.generarNube()
    
    # generarArbol: None -> None
    # Agrega un árbol aleatorio a la lista de árboles
    # Se ejecuta cada vez que el usuario preiona 'A'
    def generarArbol(self):
        suelo= self.cordillera.getPuntosBorde()
        arbol= Arbol(suelo, ALTO_ESCENA)
        self.arboles.append(arbol)
    
    # generarDiezArboles: None -> None
    # Agrega 10 árboles aleatorios a la lista de árboles
    # Se ejecuta al inicio
    def generarDiezArboles(self):
        for i in range(10):
            self.generarArbol()
    
    
    # actualizar: None -> None
    # Actualiza los elementos que pueden haber cambiado
    def actualizar(self, dt):
        for nube in self.nubes:
            nube.actualizar()
        if self.arboles != []:
            for arbol in self.arboles:
                if arbol.estaDebilitado():
                    self.arboles.remove(arbol)
        if self.rayos != []:
            for rayo in self.rayos:
                rayo.actualizar(dt)
                if rayo.estaDebilitado():
                    self.rayos.remove(rayo)
    
    # dibujar: None -> None
    # Dibuja todos los elementos presentes en la escena
    def dibujar(self):
        self.fondo.dibujar()
        self.cordillera.dibujar()
        if self.arboles != []:
            for arbol in self.arboles:
                arbol.dibujar()
        if self.rayos != []:
            for rayo in self.rayos:
                rayo.dibujar()
        for nube in self.nubes:
            nube.dibujar()
