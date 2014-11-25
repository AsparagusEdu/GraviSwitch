import pygame
from constants import SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH, MAX_FPS, CHROMA_KEY, SHOW_FPS
import sound
from misc_functions import show_fps
from confirmation import Confirmation

def Pause_Screen(prev_screen):
		
	menu_image = pygame.image.load('images/gui/pause_menu.png').convert()
	menu_rect = menu_image.get_rect()
	menu_pos = (SCREEN_WIDTH/2 - menu_rect.w/2 , SCREEN_HEIGHT/2 - menu_rect.h/2)
	menu_list = [(425,221),(425,269),(425,317), (425,365)] #48
	
	cursor_image = pygame.image.load('images/gui/cursor/pause_menu_cursor.png').convert()
	cursor_image.set_colorkey(CHROMA_KEY)
	cursor_rect = cursor_image.get_rect()
	
	cursor_state = 0

	clock = pygame.time.Clock()
	
	pause = True
	
	while pause:
		if SHOW_FPS:
			SCREEN.blit(prev_screen, (0,0))
		SCREEN.blit(menu_image, menu_pos)
		FPS = clock.get_fps()
		if SHOW_FPS:
			show_fps(FPS)
			
		if cursor_state == -1: #Precaucion para que no salga fuera de rango
			cursor_state = 3
		elif cursor_state == 4:
			cursor_state = 0
		SCREEN.blit(cursor_image, menu_list[cursor_state])
		pygame.display.flip()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False, True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					if cursor_state == 0:
						return 'Continuar'
					elif cursor_state == 1:
						if Confirmation(prev_screen):
							return 'Reiniciar'
					elif cursor_state == 2:
						if Confirmation(prev_screen):
							return 'Menu'
					elif cursor_state == 3:
						if Confirmation(prev_screen):
							return 'Salir'
				elif event.key == pygame.K_DOWN:
					cursor_state +=1
					sound.cursor.play()
				elif event.key == pygame.K_UP:
					cursor_state -=1
					sound.cursor.play()
		
		clock.tick(MAX_FPS)
		
