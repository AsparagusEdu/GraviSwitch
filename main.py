import pygame, os, sys, constants as C
from level import Level

def main():
	pygame.init()
	pygame.display.set_caption(C.GAME_NAME)
	
	Level('level0')
	
main()
