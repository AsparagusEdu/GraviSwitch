import pygame, os, sys, code.constants as C
from code.level import Level
from code.titlescreen import TitleScreen
from code.menu import Menu

def main():
	pygame.init()
	pygame.display.set_caption(C.GAME_NAME)
	Menu()
main()
#-------TO DO------
'''
- SOLUCIONAR FRAMERATE RASPBERRY!!

- Hacer la animacion de forma eficiente.
- Calcular la cantidad de veces que se debe actualizar una animacion.

- BUG: El jugador no puede saltar de cajas que van cayendo hacia arriba.

- Optimizar para el Raspberry contando la cantidad de objetos.

- Crear un switch y un sistema de "corriente"
- Permitir al jugador oprimir abajo para que monte una caja de forma horizontal.

'''

#Creditz
'''
Game Director
- Eduardo Quezada

Programming
- Eduardo Quezada
- Matias Ruiz
- Carlos Barahona

Programming Director
- Eduardo Quezada

Character Design
- Matias Ruiz
-  "Zadaka"

Testing
- Francisco Amaro
- Yerko 
- "DiFroggy"
- 
'''
