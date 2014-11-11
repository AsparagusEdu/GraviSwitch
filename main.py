import pygame, os, sys, constants as C
from ReadLevel import *
from Wall import Wall
from level import *

def main():
	pygame.init()
	pygame.display.set_caption(C.GAME_NAME)
	
	Level('level0')
	
main()
