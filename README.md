# [EN] Simulation using fractals

This is a simulation-game made with Python 2.7 in “Modelation and Graphic Computation” course.
It follows the methodology of Model View Controller.

Some time a newer version for Python 3.x will be available.

A simulated thunderstorm features a landscape (mountains, lakes, clouds, and trees) and lightning, all modeled using fractals.

<div align="center">
  <img src="Imágenes/Jugabilidad_3fps.gif" height="300" alt="Gamplay experience">
</div>


## Before using the application

Before you can use the application, you must have installed the requirement packages listed on ‘Requirements.txt’.
You can install them with pip, by the command `pip install -r requirements.txt`.


## Running the application

To run the application, you need to execute the ‘main.py’ file.
This can be done by the command `python main.py`.


## Controls

- A: Add a tree
- Space: Throw a lightning
- M: Throw many lightnings
- Q: Quit the game


## Models

Each model was implemented in a class of the same name, with a constructor and at least the draw method, responsible for drawing the object in each cycle.
In the controller, the models were drawn in a specific order to ensure correct superposition in the scene: first the background, then the mountain range, then the trees, and finally the clouds. When lightning was generated, it was drawn after the trees and before the clouds, to simulate “being cast” from them.

<div align="center">
  <img src="Imágenes/Paisaje general con rayo.png" height="300" alt="General landscape with lightning">
</div>

### Mountain Range

Based on the scene window's width and height, the ground height, the roughness factor, the spacing of the mesh to be drawn, and the width of the mountain range, the `puntosBorde` (border points) array is generated. This array defines the ground's border points with equally spaced points. Each index i of the array corresponds to the x coordinate of the point, while the value $\text{puntosBorde}_i$ corresponds to the ground's height at that point.

Given $h$ as the ground height, $dh$ as the mesh spacing in pixels, $m$ as the generated height to control the mountain range's height, and $a$ as the random heights calculated by the random walk, each point $(x,y)$ is defined as follows:

$$(x, y)_i := (dh\cdot i, puntosBorde_i)$$

#### Random Walk

The array is processed with a kind of quicksort, taking two points $x_i$ and $x_j$ to calculate the height $y$ of the midpoint between them.
That is, $(x_m ,y_m)$ is calculated, where $m=(i+j)/2$, as follows:

$$(x_m, y_m) := (x_m, (y_i + y_j) / + r)$$

where $r$ is a coefficient randomly obtained to generate the fractal, using the formula

$$r = s\cdot \text{random.gauss}(0, 1)\cdot \text{abs}(j - i)$$

where $s$ is the surface roughness factor. From this, it follows that the greater $s$, the rougher the surface.


#### Drawing

To draw the ground, each point in `puntosBorde` is iterated through, drawing 4-sided polygons with `GL_POLYGON`, similar to a Riemann Integral.
In this way, the contour is drawn and simultaneously “painted” internally.

<div align="center">
  <img src="Imágenes/Diagrama dibujo cordillera.png" height="270" alt="Mountain range draw diagram">
  <img src="Imágenes/400px-Riemann_Integration_4.png" height="240" alt="Riemann Integral">
</div>


# [ES] Simulación con fractales

Esta es una simulación juego realizada en Python 2.7 durante el curso «Modelación y computación gráfica».
Sigue la metodología Modelo Vista Controlador.

En algún momento se tendrá una versión más actualizada para Python 3.x.

Se simula una tempestad donde se modela el paisaje (montañas, lagos, nubes y árboles) y los rayos usando fractales.

<div align="center">
  <img src="Imágenes/Jugabilidad_3fps.gif" height="300" alt="Experiencia de uso">
</div>


## Antes de utilizar la aplicación

Antes de que usted pueda usar la aplicación, debe contar con los paquetes mencionados en el archivo ‘Requirements.txt’.
Se pueden instalar mediante la herramienta pip, con el comando `pip install -r requirements.txt`.


## Ejecutar la aplicación

Para ejectar la aplicación, se debe ejectar el archivo ‘main.py’.
Esto se puede hacer mediante el comando `python main.py`.


## Controles

- A: Agregar un árbol
- Espacio: Lanzar un rayo
- M: Lanzar muchos rayos
- Q: Salir del programa


## Modelos

Cada modelo fue implementado en una clase de su mismo nombre, con un constructor y por lo menos el método `dibujar`, encargado de dibujar el objeto por cada ciclo.
En el controlador, los modelos se dibujaban en un orden específico para garantizar la correcta superposición en la escena: primero el fondo, después la cordillera, luego los árboles y finalmente las nubes. Cuando se generaban rayos, estos se dibujaban después de los árboles y antes de las nubes, para simular «ser lanzados» desde ellas.

<div align="center">
  <img src="Imágenes/Paisaje general con rayo.png" height="300" alt="Paisaje general con rayo">
</div>

### Cordillera

A partir del ancho y alto de la ventana de la escena, y la altura del suelo, el factor de rugosidad, el espaciado de la malla a dibujar y el ancho de la cordillera, se genera el arreglo `puntosBorde`, que delimita los puntos de borde del suelo, con puntos equiespaciados. Cada índice $i$ del arreglo corresponde a la coordenada $x$ del punto, mientras que el valor $\text{puntosBorde}_i$ corresponde a la altura del suelo en ese punto.

Dados $h$ la altura del suelo, $dh$ el espaciado de la malla en pixeles, $m$ la altura generada para controlar la altura de la cordillera y $a$ las alturas aleatorias calculadas por el paseo aleatorio, cada punto $(x, y)$ se define según:

$$(x, y)_i := (dh\cdot i, puntosBorde_i)$$

#### Paseo aleatorio

Se trabaja en el arreglo con una especie de quicksort, tomando dos puntos $x_i$ y $x_j$ para calcular la altura $y$ del punto medio entre ellos.
Es decir, se calcula $(x_m, y_m)$, siendo $m=(i+j)/2$, de la siguiente manera:

$$(x_m, y_m) := (x_m, (y_i + y_j) / + r)$$

donde $r$ es un coeficiente aleatoriamente obtenido para generar el fractal, mediante la fórmula

$$r = s\cdot \text{random.gauss}(0, 1)\cdot \text{abs}(j - i)$$

donde $s$ es el factor de rugosidad de la superficie. De aquí se desprende que a mayor $s$, más rugosa es la superficie.

#### Dibujar

Para dibujar el suelo, se itera por cada punto en `puntosBorde`, dibujándose polígonos de 4 lados con `GL_POLYGON`, de forma similar a la Integral de Riemann.
De esta manera, se dibuja el contorno y al mismo tiempo se «pinta» por dentro.

<div align="center">
  <img src="Imágenes/Diagrama dibujo cordillera.png" height="270" alt="Diagrama de dibujo de la cordillera">
  <img src="Imágenes/400px-Riemann_Integration_4.png" height="240" alt="Integral de Riemann">
</div>

### Árbol

<div align="center">
  <img src="Imágenes/Arbol Pitágoras fractal orden 6.png" height="180" alt="Paisaje general con rayo">
</div>

#### Dibujar

<div align="center">
  <img src="Imágenes/Diagrama dibujo árbol fractal.png" height="150" alt="Diagrama de las formas, traslaciones y rotaciones para agregar un árbol al mapa.">
</div>


### Rayo

<div align="center">
  <img src="Imágenes/Rayo paseo aleatorio punto medio.png" height="200" alt="Rayo golpeando un árbol">
</div>


### Nube

<div align="center">
  <img src="Imágenes/Nube fractal.png" height="130" alt="Nube">
</div>

#### Dibujar

<div align="center">
  <img src="Imágenes/Diagrama dibujo nube.png" height="200" alt="Diagrama dibujo nube">
</div>


### Fondo

<div align="center">
  <img src="Imágenes/Fondo.png" height="200" alt="Fondo">
</div>

