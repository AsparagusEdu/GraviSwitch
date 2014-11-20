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
- BUG: Si un jugador cae de una caja a otra mientras ambas van subiendo, cuenta como si muriera aplastado.
- BUG: Si el jugador esta saltando y choca con una caja que va cayendo hacia abajo, es aplastado
Relacionados?

- Optimizar para el Raspberry contando la cantidad de objetos.

- Crear un switch y un sistema de "corriente"
- Crear Checkpoints

'''
