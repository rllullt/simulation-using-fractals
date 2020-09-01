# -*- coding= utf-8 -*-

'''
Tarea 2
Autor: Rodrigo Llull Torres
La estructura está basada en la de la clase auxiliar
'''

# Importación de los modelos
from Modelos import Modelos
from Vista import Vista
from Controlador import Controlador

# Creación de objetos
# Se crea un contenedor de modelos (una escena, en este caso)
modelo = Modelos()
# Se crea la vista
vista = Vista(modelo)
# Se crea el controlador de la aplicación
controlador = Controlador(modelo, vista)


# Bucle de aplicación
while True:
    controlador.chequearInput()
    vista.dibujar()

pygame.quit()
