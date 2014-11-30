import pygame
from constants import SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH, MAX_FPS, CHROMA_KEY, SHOW_FPS
import sound
from misc_functions import show_fps
import level

def Adventure(MUTE_MUSIC):
	clock = pygame.time.Clock()
	
	EXIT_MENU = True
	EXIT_GAME = False
	lvl = 1 #Nivel de donde continua el modo aventura
	
	while EXIT_MENU:
		finished_level, EXIT_MENU, EXIT_GAME, MUTE_MUSIC = level.Level('level' + str(lvl), MUTE_MUSIC)
		lvl += 1
		if EXIT_GAME: #Si en algun momento se necesita salir del juego
			return True, MUTE_MUSIC
		elif lvl > 6: #Ultimo nivel del modo aventura
			return False, MUTE_MUSIC
		
		clock.tick(MAX_FPS)
	
		
