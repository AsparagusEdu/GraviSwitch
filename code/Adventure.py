import pygame
from constants import SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH, MAX_FPS, CHROMA_KEY, SHOW_FPS
import sound
from misc_functions import show_fps
from LevelSelect import Level_Select
import level

def Adventure(save_num, MUTE_MUSIC, prev_song, lvl = 0):
	clock = pygame.time.Clock()
	
	EXIT_MENU = True
	EXIT_GAME = False
	if lvl == 'COMPLETADO':
		return Level_Select(MUTE_MUSIC, prev_song)
	
	lvl += 1 #Nivel de donde continua el modo aventura
	prev_song = 'None'
	
	while EXIT_MENU:
		finished_level, EXIT_MENU, EXIT_GAME, MUTE_MUSIC, prev_song = level.Level('level' + str(lvl), MUTE_MUSIC, prev_song)
		lvl += 1
		if EXIT_GAME: #Si en algun momento se necesita salir del juego
			return True, MUTE_MUSIC, prev_song
		elif lvl > 12: #Ultimo nivel del modo aventura
			return False, MUTE_MUSIC, prev_song
		
		clock.tick(MAX_FPS)
	return False, MUTE_MUSIC, prev_song
		
