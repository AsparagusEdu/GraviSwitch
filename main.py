import pygame, os, sys, code.constants as C
from code.level import Level
from code.titlescreen import TitleScreen

def main():
	pygame.init()
	pygame.display.set_caption(C.GAME_NAME)
	done = False
	while not done:
		TitleScreen()
		#done = Level('levelTest1')
		done = Level('level2')
	#Level('level0')
	#Level('Level2')
main()


#-------TO DO------
'''
- PROBAR FRAMESKIP EN EL RASPBERRY!!

- "World Shift"
- Crear un final de nivel exitoso

- Crear un switch y un sistema de "corriente"
- Puertas?
- Crear un bloque que player pueda atravesar, pero no las cajas

- Menus
- CREAR NIVELES
'''
