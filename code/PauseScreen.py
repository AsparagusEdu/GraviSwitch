import pygame
from constants import SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH, MAX_FPS, CHROMA_KEY

def Pause_Screen():
	
	menu_image = pygame.image.load('images/pause_menu.png').convert()
	menu_rect = menu_image.get_rect()
	menu_pos = (SCREEN_WIDTH/2 - menu_rect.w/2 , SCREEN_HEIGHT/2 - menu_rect.h/2)
	menu_list = [(425,240),(425,288),(425,336)] #48
	
	cursor_image = pygame.image.load('images/pause_menu_cursor.png').convert()
	cursor_image.set_colorkey(CHROMA_KEY)
	cursor_rect = cursor_image.get_rect()
	
	cursor_state = 0

	clock = pygame.time.Clock()
	
	pause = True
	
	while pause:
		SCREEN.blit(menu_image, menu_pos)
		SCREEN.blit(cursor_image, menu_list[cursor_state])
		pygame.display.flip()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False, True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pass
		
		clock.tick(MAX_FPS)
		FPS = clock.get_fps()
		print FPS
