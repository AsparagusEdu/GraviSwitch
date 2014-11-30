import pygame, os, sys, code.constants as C
from code.menu import Demo_Menu, Main_Menu

def main():
	pygame.init()
	icon = pygame.image.load('images/icon.png').convert()
	icon.set_colorkey(C.CHROMA_KEY)
	pygame.display.set_icon(icon)
	pygame.display.set_caption(C.GAME_NAME)
	
	Main_Menu()
	pygame.quit()
main()
#-------TO DO------
'''
- Terminar con el menu.
- SOLUCIONAR FRAMERATE RASPBERRY!!

- Sistema de guardado
- Arreglar animacion del checkpoint.
- Mostrar al jugador muriendo.

- BUG?: El jugador no puede saltar de cajas que van cayendo hacia arriba.
  Y si utilizamos esto como explicacion para permitir que las cajas puedan lanzar al jugador hacia arriba?

- Crear un switch y un sistema de "corriente"

'''

#------Creditz-----
'''
Game Director
- Eduardo Quezada

Programming
- Eduardo Quezada
- Carlos Barahona

Level Design
- Carlos Barahona
- Matias Ruiz
- Eduardo Quezada

Character Design
- Matias Ruiz
- "Zadaka"

Graphics
- Matias Ruiz
- Eduardo Quezada

External Resourcing
- Matias Ruiz

Music (from OpenGameArt.org)
- BBandRage

Testing
- "Zadaka"
- Felipe "DiFroggy" Vasquez
- Felipe Moscoso
- Yerko
- Francisco Amaro
- Daniel Nahum
- Cristian Arancibia

'''
