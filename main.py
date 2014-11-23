import pygame, os, sys, code.constants as C
from code.menu import Demo_Menu

def main():
	pygame.init()
	icon = pygame.image.load('images/icon.png').convert()
	icon.set_colorkey(C.CHROMA_KEY)
	pygame.display.set_icon(icon)
	pygame.display.set_caption(C.GAME_NAME)
	
	Demo_Menu()
main()
#-------TO DO------
'''
- SOLUCIONAR FRAMERATE RASPBERRY!!

- Sistema de guardado
- Arreglar animacion y colision del checkpoint.

- BUG: El jugador no puede saltar de cajas que van cayendo hacia arriba.

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

Level Design
- Carlos Barahona
- Matias Ruiz
- Eduardo Quezada

Character Design
- Matias Ruiz
-  "Zadaka"

External Resourcing
- Matias Ruiz

Testing
- Francisco Amaro
- Yerko 
- "DiFroggy"
- "Zadaka"
- Moscoso
- Leonora Quezada
'''
