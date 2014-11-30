import pygame
from constants import SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH, MAX_FPS, CHROMA_KEY, SHOW_FPS, MUSIC
import sound
from misc_functions import show_fps
import level

def Adventure():
	clock = pygame.time.Clock()
	
	EXIT_MENU = True
	EXIT_GAME = False
	lvl = 1
	
	while EXIT_MENU:
		finished_level, EXIT_MENU, EXIT_GAME = level.Level('level' + str(lvl))
		lvl += 1
		if EXIT_GAME:
			return True
		elif lvl > 6:
			return False
		
		clock.tick(MAX_FPS)
	
		
