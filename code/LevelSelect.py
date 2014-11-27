import pygame
from constants import SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH, MAX_FPS, CHROMA_KEY, SHOW_FPS, MUSIC
import sound
from misc_functions import show_fps
import level

def Level_Select(prev_screen):
		
	menu_image = pygame.image.load('images/gui/levelselect.png').convert()
	menu_rect = menu_image.get_rect()
	menu_pos = (SCREEN_WIDTH/2 - menu_rect.w/2 , SCREEN_HEIGHT/2 - menu_rect.h/2)
	menu_list = [(399,284),(518,284)]
	
	cursor_state = 1
	demo = 1

	clock = pygame.time.Clock()
	
	fonty = pygame.font.SysFont('Pokemon FireLeaf', 60) #Pokemon FireLeaf
	if MUSIC:
		music = pygame.mixer.music.load('sound/music/s3kfileselect.mp3')
		pygame.mixer.music.play(-1)
		
	EXIT_MENU = False
	EXIT_GAME = False
	
	while not EXIT_MENU:
		
		if cursor_state <= demo -1: #Precaucion para que no salga fuera de rango. Modificado cuando se activan los niveles demo.
			cursor_state = 6
		elif cursor_state == 7:
			cursor_state = demo
		
		FPS = clock.get_fps()
		if SHOW_FPS:
			SCREEN.blit(prev_screen, (0,0))
			show_fps(FPS)
		SCREEN.blit(menu_image, menu_pos)
		cursor_image = fonty.render(str(cursor_state), False, (255,255,255))
		SCREEN.blit(cursor_image, (502,304))
		
		pygame.display.flip()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					finished_level, EXIT_GAME = level.Level('level' + str(cursor_state))
					if EXIT_GAME:
						return True
					if MUSIC:
						music = pygame.mixer.music.load('sound/music/s3kfileselect.mp3')
						pygame.mixer.music.play(-1)
				elif event.key == pygame.K_ESCAPE:
					return True
					
				elif event.key == pygame.K_p:
					if demo == 1:
						demo = -6
					else:
						demo = 1
				
				elif event.key == pygame.K_RIGHT:
					cursor_state +=1
					sound.cursor.play()
				elif event.key == pygame.K_LEFT:
					cursor_state -=1
					sound.cursor.play()
		
		clock.tick(MAX_FPS)
		
