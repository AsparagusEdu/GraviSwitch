import pygame, os, sys, constants as C
from classReadLevel import *
from classWall import Wall
from level import *



def main():
	pygame.init()
	pygame.display.set_caption(C.GAME_NAME)
	
	Level('level0')
	
	
	
main()
