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

- BUG: Si el jugador esta saltando y choca con una caja que va cayendo hacia abajo, es aplastado
Relacionados?
- BUG: El jugador no puede saltar de cajas que van cayendo hacia arriba.

- Optimizar para el Raspberry contando la cantidad de objetos.

- Crear Checkpoints
- Crear un switch y un sistema de "corriente"
- Permitir al jugador oprimir abajo para que monte una caja de forma horizontal.

'''
