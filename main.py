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
- Eduardo Quezada
- Matias Ruiz
- Leonora Quezada
- Carlos Barahora

External Resourcing
- Matias Ruiz

Music (OpenGameArt.org)
- Bond Esque by BBandRage
- Adventure HO! by BBandRage
- Rock You by Snabisch
- Jumping Bat by Snabisch

Sound Effect rips (www.sounds-resource.com)
- Mr Lange

Testing
- Isidora Quezada
- "Zadaka"
- Felipe "DiFroggy" Vasquez
- Felipe Moscoso
- Yerko *Ingrese Apellido* :)
- Francisco Amaro
- Daniel Nahum
- Cristian Arancibia
- Pablo Saez
- Gabriel Como Se Llame :P


'''
