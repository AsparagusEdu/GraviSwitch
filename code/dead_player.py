import pygame
from constants import SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH, MAX_FPS, CHROMA_KEY, SHOW_FPS
import sound
from misc_functions import show_fps
from confirmation import Confirmation

def DeadPlayer(prev_screen):
		
	menu_image = pygame.image.load('images/gui/retry.png').convert()
	menu_rect = menu_image.get_rect()
	menu_pos = (SCREEN_WIDTH/2 - menu_rect.w/2 , SCREEN_HEIGHT/2 - menu_rect.h/2)
	menu_list = [(399,284),(518,284)]
	
	cursor_image = pygame.image.load('images/gui/cursor/confirmation_cursor.png').convert()
	cursor_image.set_colorkey(CHROMA_KEY)
	cursor_rect = cursor_image.get_rect()
	
	cursor_state = 0

	clock = pygame.time.Clock()
	
	pause = True
	pygame.time.wait(1000)
	
	while pause:
		if SHOW_FPS:
			SCREEN.blit(prev_screen, (0,0))
		SCREEN.blit(menu_image, menu_pos)
		FPS = clock.get_fps()
		if SHOW_FPS:
			show_fps(FPS)
			
		if cursor_state == -1: #Precaucion para que no salga fuera de rango
			cursor_state = 1
		elif cursor_state == 2:
			cursor_state = 0
		SCREEN.blit(cursor_image, menu_list[cursor_state])
		pygame.display.flip()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False, True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					if cursor_state == 0:
						return True, False
					elif cursor_state == 1 and Confirmation(prev_screen):
						return False, False
				elif event.key == pygame.K_RIGHT:
					if cursor_state == 0:
						cursor_state +=1
						sound.cursor.play()
				elif event.key == pygame.K_LEFT:
					if cursor_state == 1:
						cursor_state -=1
						sound.cursor.play()
		
		clock.tick(MAX_FPS)
		
