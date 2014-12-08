import pygame
from constants import SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH, MAX_FPS, CHROMA_KEY, SHOW_FPS
import sound
from misc_functions import show_fps
import level
import level_editor

def Custom_Select(MUTE_MUSIC, prev_song, prev_screen = 0): #Utiliza la pantalla anterior para poder blitearse en ella.
	back = pygame.image.load('images/backgrounds/fondo_marble2.png').convert()
	back_rect = back.get_rect()
	back2 = pygame.image.load('images/gui/file_menu.png').convert()
	back2_rect = back2.get_rect()
	
	menu_image = pygame.image.load('images/gui/customselect.png').convert()
	menu_rect = menu_image.get_rect()
	menu_pos = (SCREEN_WIDTH/2 - menu_rect.w/2 , SCREEN_HEIGHT/2 - menu_rect.h/2)
	menu_list = [(399,284),(518,284)]
	
	lvl_state = 1
	cursor_state = 0
	cursor_points = [(461,246),(439,326)]
	
	cursor_image1 = pygame.image.load('images/gui/cursor/customselect1.png').convert()
	cursor_image1.set_colorkey(CHROMA_KEY)
	cursor_image2 = pygame.image.load('images/gui/cursor/customselect2.png').convert()
	cursor_image2.set_colorkey(CHROMA_KEY)
	
	cursor_image = cursor_image1
	
	demo = 1

	clock = pygame.time.Clock()
	
	fonty = pygame.font.Font('I-Choose-You.ttf', 60) #Pokemon FireLeaf
	#music = pygame.mixer.music.load('sound/music/s3kfileselect.mp3')
	#prev_song = 's3kfileselect'
	#pygame.mixer.music.play(-1)
	if MUTE_MUSIC:
		pygame.mixer.music.pause()
		
	EXIT_MENU = False
	EXIT_GAME = False
	
	while not EXIT_MENU:
		
		if lvl_state <= demo -1: #Precaucion para que no salga fuera de rango. Modificado cuando se activan los niveles demo.
			lvl_state = 30
		elif lvl_state == 31:
			lvl_state = demo
		
		FPS = clock.get_fps()
		if SHOW_FPS:
			#SCREEN.blit(prev_screen, (0,0))
			show_fps(FPS)
			
		SCREEN.blit(back, (0,0))
		back2_rect.center = back_rect.center
		#SCREEN.blit(back2, back2_rect.topleft)
		SCREEN.blit(menu_image, menu_pos)
		lvl_image = fonty.render(str(lvl_state), False, (255,255,255))
		lvl_rect = lvl_image.get_rect()
		#cursor_rect.topleft = cursor_points[cursor_state]
		SCREEN.blit(cursor_image, cursor_points[cursor_state])
		SCREEN.blit(lvl_image, (SCREEN_WIDTH/2 - lvl_rect.w/2 +4,250))
		
		pygame.display.flip()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True, MUTE_MUSIC, prev_song
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					if cursor_state == 0:
						try:
							finished_level, EXIT_MENU, EXIT_GAME, MUTE_MUSIC, prev_song = level.Level('custom' + str(lvl_state), MUTE_MUSIC, prev_song, 'custom/', 'NivComp')
						except:
							finished_level, EXIT_MENU, EXIT_GAME, MUTE_MUSIC, prev_song = level.Level('base_lvl', MUTE_MUSIC, prev_song, 'custom/', 'NivComp')
						
						if EXIT_GAME:
							return True, MUTE_MUSIC, prev_song
						music = pygame.mixer.music.load('sound/music/JumpingBat.wav')
						pygame.mixer.music.set_volume(1.0)
						pygame.mixer.music.play(-1)
						if MUTE_MUSIC:
							pygame.mixer.music.pause()
						prev_song = 's3kfileselect'
					else:
						EXIT_GAME, MUTE_MUSIC = level_editor.Edit_Level(lvl_state, MUTE_MUSIC)
				elif event.key == pygame.K_ESCAPE:
					return False, MUTE_MUSIC, prev_song
					
				elif event.key == pygame.K_m:
					if not MUTE_MUSIC:
						print 'MUSIC - OFF'
						MUTE_MUSIC = True
						pygame.mixer.music.pause()
						
					else:
						print 'MUSIC - ON'
						MUTE_MUSIC = False
						pygame.mixer.music.unpause()
				
				elif event.key == pygame.K_RIGHT and cursor_state == 0:
					lvl_state +=1
					sound.cursor.play()
				elif event.key == pygame.K_LEFT and cursor_state == 0:
					lvl_state -=1
					sound.cursor.play()
				elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					sound.cursor.play()
					if cursor_state == 0:
						cursor_state = 1
						cursor_image = cursor_image2
					else:
						cursor_state = 0
						cursor_image = cursor_image1
		
		clock.tick(MAX_FPS)
	return True, MUTE_MUSIC, prev_song
