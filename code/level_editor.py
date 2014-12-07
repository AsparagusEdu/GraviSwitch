import pygame
from constants import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, SHOW_FPS, MAX_FPS, CHROMA_KEY
from level import Level
from load_level import Read_File
from misc_functions import show_fps


def Save_Level(map_data, archivo):
	for linea in map_data['mapa']:
		archivo.write(linea)
		archivo.write('\n')

def Test_Level(map_data, archivo, MUTE_MUSIC):
	Save_Level(map_data, archivo)
	archivo.close()
	#print map_data['mapa'][1]
	return Level('temp', MUTE_MUSIC, 's3kfileselect', 'custom/')

def Edit_Level(lvl_num, MUTE_MUSIC):
	lvl_name = 'custom' + str(lvl_num)
	base = open('levels/custom/base_lvl.txt', 'r')
	templvl = open('levels/custom/temp.txt', 'w')
	EXIT_MENU = False
	EXIT_GAME = False
	finished_level = False
	
	x_position = []
	y_position = []
	for i in range(32):
		x_position.append(i*32)
		if i < 18:
			y_position.append(i*32)
	#print x_position
	#print y_position
	
	data = {} #info del mapa
	data['mapa'], data['fondo'], data['musica'], data['pared'], data['graviswitch'], data['g_spin'], data['g_spin_spd'] = Read_File('custom/base_lvl.txt')
	base.close()
	
	pygame.display.set_mode((SCREEN_WIDTH +192, SCREEN_HEIGHT))
	fondo = pygame.image.load('images/backgrounds/lvl_editor.png').convert()
	
	current_x1 = 0
	current_y1 = 0
	cursor_image1 = pygame.image.load('images/gui/cursor/lvl_editor1.png').convert()
	cursor_image1.set_colorkey(CHROMA_KEY)
	cursor_rect1 = cursor_image1.get_rect()
	
	x2_pos = [1039, 1123]
	y2_pos = [78,164,249, 325]
	
	current_x2 = 0
	current_y2 = 0
	cursor_image2 = pygame.image.load('images/gui/cursor/lvl_editor2.png').convert()
	cursor_image2.set_colorkey(CHROMA_KEY)
	cursor_rect2 = cursor_image2.get_rect()
	
	clock = pygame.time.Clock()
	
	while not EXIT_MENU:
		cursor_pos1 = [x_position[current_x1], y_position[current_y1]] #Actualiza la posicion del cursor
		cursor_pos2 = [x2_pos[current_x2], y2_pos[current_y2]]
		cursor_rect1.topleft = cursor_pos1
		cursor_rect2.topleft = cursor_pos2
		SCREEN.blit(fondo,(0,0))
		SCREEN.blit(cursor_image1,cursor_rect1)
		SCREEN.blit(cursor_image2,cursor_rect2)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					EXIT_MENU = True
				elif event.key == pygame.K_d:
					if current_x1 == 31:
						current_x1 = 0
					else:
						current_x1 += 1
				elif event.key == pygame.K_a:
					if current_x1 == 0:
						current_x1 = 31
					else:
						current_x1 -= 1		
				elif event.key == pygame.K_w:
					if current_y1 == 0:
						current_y1 = 17
					else:
						current_y1 -= 1
				elif event.key == pygame.K_s:
					if current_y1 == 17:
						current_y1 = 0
					else:
						current_y1 += 1
				elif event.key == pygame.K_RIGHT:
					if current_x2 == 1:
						current_x2 = 0
					else:
						current_x2 += 1
				elif event.key == pygame.K_LEFT:
					if current_x2 == 0:
						current_x2 = 1
					else:
						current_x2 -= 1		
				elif event.key == pygame.K_UP:
					if current_y2 == 0:
						current_y2 = 3
					else:
						current_y2 -= 1
				elif event.key == pygame.K_DOWN:
					if current_y2 == 3:
						current_y2 = 0
					else:
						current_y2 += 1
				
				elif event.key == pygame.K_RETURN:
					finished_level, EXIT_MENU, EXIT_GAME, MUTE_MUSIC, prev_song = Test_Level(data, templvl, MUTE_MUSIC)
					if EXIT_MENU:
						return EXIT_GAME, MUTE_MUSIC
					templvl = open('levels/custom/temp.txt', 'w')
					SCREEN.blit(fondo,(0,0))
					pygame.display.flip()
					music = pygame.mixer.music.load('sound/music/JumpingBat.wav')
					prev_song = 's3kfileselect'
					pygame.mixer.music.set_volume(1.0)
					pygame.mixer.music.play(-1)
					if MUTE_MUSIC:
						pygame.mixer.music.pause()
				
		
		#fsdfsdfsdfsdf
		FPS = clock.get_fps()
		if SHOW_FPS:
			show_fps(FPS)
		clock.tick(MAX_FPS)
		
	
	pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	return EXIT_GAME, MUTE_MUSIC
	

