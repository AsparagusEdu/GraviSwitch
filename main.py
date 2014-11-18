import pygame, os, sys, code.constants as C
from code.level import Level
from code.titlescreen import TitleScreen
from code.menu import Menu

def main():
	pygame.init()
	pygame.display.set_caption(C.GAME_NAME)
	Menu()
	'''
	done = False
	while not done:
		TitleScreen()
		done = Level('levelTest1')
		
	done = False
	while not done:
		TitleScreen()
		done = Level('level0')
	'''
	
	#Level('level0')
	#Level('Level2')
main()


#-------TO DO------
'''
- BUG: A veces el jugador se queda atascado al intentar subir un bloque.
- BUG: Si un jugador cae de una caja a otra, cuenta como si muriera aplastado.
	
- Crear un switch y un sistema de "corriente"


'''
