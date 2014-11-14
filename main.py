import pygame, os, sys, code.constants as C
from code.level import Level

def main():
	pygame.init()
	pygame.display.set_caption(C.GAME_NAME)
	
	Level('levelTest1')
	
main()
