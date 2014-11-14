import pygame, os, sys, code.constants as C
from code.level import Level

def main():
	pygame.init()
	pygame.display.set_caption(C.GAME_NAME)
	
	Level('levelTest1')
	#Level('level0')
	#Level('Level2')
main()


#-------TO DO------
'''
- FPS!!!

- BUG: A veces Player no es cuando salta mientras las cajas van hacia abajo
- BUG: Uno es aplastado cuando salta entre 2 cajas adyacentes que van cayendo hacia abajo

- Pantalla de titulo

- Crear pinchos
- Crear un switch y un sistema de "corriente"
- Puertas?
- Crear un bloque que player pueda atravesar, pero no las cajas

- Menus
- CREAR NIVELES



- Crear archivo funciones.py
'''
