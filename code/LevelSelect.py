import pygame
from constants import SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH, MAX_FPS, CHROMA_KEY, SHOW_FPS
import sound
from misc_functions import show_fps
import level

def Level_Select(prev_screen, MUTE_MUSIC): #Utiliza la pantalla anterior para poder blitearse en ella.
		
	menu_image = pygame.image.load('images/gui/levelselect.png').convert()
	menu_rect = menu_image.get_rect()
	menu_pos = (SCREEN_WIDTH/2 - menu_rect.w/2 , SCREEN_HEIGHT/2 - menu_rect.h/2)
	menu_list = [(399,284),(518,284)]
	
	cursor_state = 1
	demo = 1

	clock = pygame.time.Clock()
	
	fonty = pygame.font.SysFont('Pokemon FireLeaf', 60) #Pokemon FireLeaf
	music = pygame.mixer.music.load('sound/music/s3kfileselect.mp3')
	prev_song = 's3kfileselect'
	pygame.mixer.music.play(-1)
	if MUTE_MUSIC:
		pygame.mixer.music.pause()
		
	EXIT_MENU = False
	EXIT_GAME = False
	
	while not EXIT_MENU:
		
		if cursor_state <= demo -1: #Precaucion para que no salga fuera de rango. Modificado cuando se activan los niveles demo.
			cursor_state = 12
		elif cursor_state == 13:
			cursor_state = demo
		
		FPS = clock.get_fps()
		if SHOW_FPS:
			SCREEN.blit(prev_screen, (0,0))
			show_fps(FPS)
		SCREEN.blit(menu_image, menu_pos)
		cursor_image = fonty.render(str(cursor_state), False, (255,255,255))
		if cursor_state >= 10:
			SCREEN.blit(cursor_image, (491,304))
		else:	
			SCREEN.blit(cursor_image, (502,304))
		
		pygame.display.flip()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					finished_level, EXIT_MENU, EXIT_GAME, MUTE_MUSIC, prev_song = level.Level('level' + str(cursor_state), MUTE_MUSIC, prev_song, 'NivComp')
					
					if EXIT_GAME:
						return True, MUTE_MUSIC
					music = pygame.mixer.music.load('sound/music/s3kfileselect.mp3')
					pygame.mixer.music.set_volume(1.0)
					pygame.mixer.music.play(-1)
					if MUTE_MUSIC:
						pygame.mixer.music.pause()
					prev_song = 's3kfileselect'
				elif event.key == pygame.K_ESCAPE:
					return False, MUTE_MUSIC
					
				elif event.key == pygame.K_p:
					if demo == 1:
						demo = -6
					else:
						demo = 1
				elif event.key == pygame.K_m:
					if not MUTE_MUSIC:
						print 'MUSIC - OFF'
						MUTE_MUSIC = True
						pygame.mixer.music.pause()
						
					else:
						print 'MUSIC - ON'
						MUTE_MUSIC = False
						pygame.mixer.music.unpause()
				
				elif event.key == pygame.K_RIGHT:
					cursor_state +=1
					sound.cursor.play()
				elif event.key == pygame.K_LEFT:
					cursor_state -=1
					sound.cursor.play()
		
		clock.tick(MAX_FPS)
	return True, MUTE_MUSIC
