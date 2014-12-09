import pygame
from constants import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, SHOW_FPS, MAX_FPS, CHROMA_KEY
from level import Level
from load_level import Read_File
from misc_functions import show_fps
from confirmation import Confirmation
import sound

def Save_Level(map_data, archivo):
	for linea in map_data['mapa']:
		archivo.write(linea)
		archivo.write('\n')
	archivo.write(':Fondo ' + map_data['fondo'] + '\n')
	archivo.write(':Musica ' + map_data['musica'] + '\n')
	archivo.write(':Pared ' + map_data['pared'] + '\n')

def Test_Level(map_data, archivo, MUTE_MUSIC):
	Save_Level(map_data, archivo)
	archivo.close()
	#print map_data['mapa'][1]
	return Level('temp', MUTE_MUSIC, 's3kfileselect', 'custom/', 'NivComp')

def Edit_Level(lvl_num, MUTE_MUSIC):
	
	try:
		lvl_name = 'custom' + str(lvl_num)
		base = open('levels/custom/' + lvl_name +'.txt', 'r')
		base.close()
		
	except:
		lvl_name = 'base_lvl'
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
	
	wall_image = pygame.image.load('images/tiles/wall_base.png').convert()
	box_image = pygame.image.load('images/tiles/box.png').convert()
	player_image = pygame.image.load('images/Isaac/stand.png').convert()
	player_image.set_colorkey(CHROMA_KEY)
	jump_image = pygame.image.load('images/tiles/jumpbox.png').convert()
	door_image = pygame.image.load('images/tiles/door.png').convert()
	door_image.set_colorkey(CHROMA_KEY)
	spike_image = pygame.image.load('images/tiles/spike.png').convert()
	spike_image.set_colorkey(CHROMA_KEY)
	filter_image = pygame.image.load('images/tiles/boxfilter.png').convert()
	filter_image.set_colorkey(CHROMA_KEY)
	gravi_image = pygame.image.load('images/tiles/gravi_base.png').convert()
	gravi_image.set_colorkey(CHROMA_KEY)
	checkpoint_image = pygame.image.load('images/tiles/checkpoint_base.png').convert()
	checkpoint_image.set_colorkey(CHROMA_KEY)
	eraser_image = pygame.image.load('images/tiles/blank.png').convert()
	eraser_image.set_colorkey(CHROMA_KEY)
	
	editor_screen = pygame.Surface((1024,576))
	editor_screen.fill((175,167,124))
	
	data = {} #info del mapa
	if lvl_name == 'base_lvl':
		data['mapa'], data['fondo'], data['musica'], data['pared'], data['graviswitch'], data['g_spin'], data['g_spin_spd'] = Read_File('custom/base_lvl.txt')
	else:
		data['mapa'], data['fondo'], data['musica'], data['pared'], data['graviswitch'], data['g_spin'], data['g_spin_spd'] = Read_File('custom/'+ lvl_name + '.txt')
		
	current_y1 = 0
	for linea in data['mapa']:
		current_x1 = 0
		for cuadro in linea.strip('\n'):
			if cuadro == 'W':
				editor_screen.blit(wall_image, (current_x1*32,current_y1*32))
			elif cuadro == 'P':
				editor_screen.blit(player_image, (current_x1*32,current_y1*32))
			elif cuadro == 'B':
				editor_screen.blit(box_image, (current_x1*32,current_y1*32))
			elif cuadro == 'J':
				editor_screen.blit(jump_image, (current_x1*32,current_y1*32))
			elif cuadro == 'S':
				editor_screen.blit(spike_image, (current_x1*32,current_y1*32))
			elif cuadro == 'D':
				editor_screen.blit(door_image, (current_x1*32,current_y1*32))
			elif cuadro == 'F':
				editor_screen.blit(filter_image, (current_x1*32,current_y1*32))
			elif cuadro == 'C':
				editor_screen.blit(checkpoint_image, (current_x1*32,current_y1*32))
			elif cuadro == 'G':
				editor_screen.blit(graviswitch_image, (current_x1*32,current_y1*32))
			current_x1 += 1
		current_y1 +=1

	pygame.display.set_mode((SCREEN_WIDTH +192, SCREEN_HEIGHT))
	fondo = pygame.image.load('images/backgrounds/lvl_editor.png').convert()
	
	current_x1 = 0#Reciclando variables
	current_y1 = 0
	cursor_image1 = pygame.image.load('images/gui/cursor/lvl_editor1.png').convert()
	cursor_image1.set_colorkey(CHROMA_KEY)
	cursor_rect1 = cursor_image1.get_rect()
	
	x2_pos = [1035, 1099, 1037]
	y2_pos = [69,133,197, 255, 312, 413,466,519]
	states = [['W','B','F','G','P','B1','B2','B3'],['D','J','S','C', ' ','B1','B2','B3'], ['W','B','F','G',' ','B1','B2','B3']]
	
	current_x2 = 0
	current_y2 = 0
	cursor_image2a = pygame.image.load('images/gui/cursor/lvl_editor2.png').convert()
	cursor_image2a.set_colorkey(CHROMA_KEY)
	cursor_image2b = pygame.image.load('images/gui/cursor/lvl_editor3.png').convert()
	cursor_image2b.set_colorkey(CHROMA_KEY)
	cursor_image2 = cursor_image2a
	cursor_rect2 = cursor_image2.get_rect()
	cursor2_state = 'W'
	
	players_count = 1
	
	clock = pygame.time.Clock()
	
	while not EXIT_MENU:
		cursor_pos1 = [x_position[current_x1], y_position[current_y1]] #Actualiza la posicion del cursor
		cursor_pos2 = [x2_pos[current_x2], y2_pos[current_y2]]
		cursor_rect1.topleft = cursor_pos1
		cursor_rect2.topleft = cursor_pos2
		cursor2_state = states[current_x2][current_y2]
		#print cursor2_state
		SCREEN.blit(fondo,(0,0))
		SCREEN.blit(editor_screen,(0,0))
		SCREEN.blit(cursor_image1,cursor_rect1)
		SCREEN.blit(cursor_image2,cursor_rect2)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_d:
					sound.cursorleft.play()
					if current_x1 == 31:
						current_x1 = 0
					else:
						current_x1 += 1
				elif event.key == pygame.K_a:
					sound.cursorleft.play()
					if current_x1 == 0:
						current_x1 = 31
					else:
						current_x1 -= 1		
				elif event.key == pygame.K_w:
					sound.cursorleft.play()
					if current_y1 == 0:
						current_y1 = 17
					else:
						current_y1 -= 1
				elif event.key == pygame.K_s:
					sound.cursorleft.play()
					if current_y1 == 17:
						current_y1 = 0
					else:
						current_y1 += 1
				elif event.key == pygame.K_RIGHT:
					sound.cursorright.play()
					if current_x2 == 1:
						current_x2 = 0
					elif current_x2 == 3 or current_x2 == 2:
						pass
					else:
						current_x2 += 1
				elif event.key == pygame.K_LEFT:
					sound.cursorright.play()
					if current_x2 == 0:
						current_x2 = 1
					elif current_x2 == 3 or current_x2 == 2:
						pass
					else:
						current_x2 -= 1		
				elif event.key == pygame.K_UP:
					sound.cursorright.play()
					if current_y2 == 0:
						current_y2 = 7
						current_x2 = 2
						cursor_image2 = cursor_image2b
					elif current_y2 == 5:
						current_x2 = 0
						cursor_image2 = cursor_image2a
						current_y2 -=1
					else:
						current_y2 -= 1
				elif event.key == pygame.K_DOWN:
					sound.cursorright.play()
					
					if current_y2 == 4:
						current_x2 = 2
						current_y2 +=1
						cursor_image2 = cursor_image2b
					elif current_y2 == 7:
						current_y2 = 0
						current_x2 = 0
						cursor_image2 = cursor_image2a
					else:
						current_y2 += 1
				elif event.key == pygame.K_RETURN:
					if cursor2_state == 'B1':
						if players_count == 1:
							finished_level, null, null, MUTE_MUSIC, prev_song = Test_Level(data, templvl, MUTE_MUSIC)
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
						else:
							sound.no.play()
					elif cursor2_state == 'B2':
						if finished_level:
							archivo = open('levels/custom/custom' + str(lvl_num) + '.txt', 'w')
							for linea in data['mapa']:
								archivo.write(linea + '\n')
							archivo.write(':Fondo ' + data['fondo'] + '\n')
							archivo.write(':Musica ' + data['musica'] + '\n')
							archivo.write(':Pared ' + data['pared'] + '\n')
							archivo.close()
							sound.lvlsaved.play()
							#print 'GUADADO'
						else:
							sound.no.play()
							#print 'NOOOOO'
					elif cursor2_state == 'B3' and Confirmation():
						EXIT_MENU = True
					#elif players_count == 1 and data['mapa'][current_y1][current_x1] == 'P':
						#sound.no.play()
					else:
						if cursor2_state == 'W':
							paste_image = wall_image
						elif cursor2_state == 'B':
							paste_image = box_image
						elif cursor2_state == 'J':
							paste_image = jump_image
						elif cursor2_state == 'S':
							paste_image = spike_image
						elif cursor2_state == 'D':
							paste_image = door_image
						elif cursor2_state == 'F':
							paste_image = filter_image
						elif cursor2_state == 'C':
							paste_image = checkpoint_image
						elif cursor2_state == 'G':
							paste_image = gravi_image
						elif cursor2_state == 'P':
							paste_image = player_image
							editor_screen.blit(eraser_image, (current_x1*32,current_y1*32))
							players_count += 1
						elif cursor2_state == ' ':
							paste_image = eraser_image
							if data['mapa'][current_y1][current_x1] == 'P':
								players_count -=1
						editor_screen.blit(paste_image, (current_x1*32,current_y1*32))
						
						templine = ''
						temp_x = 0
						for cuadro in data['mapa'][current_y1]:
							if temp_x == current_x1:
								templine += cursor2_state
							else:
								templine += cuadro
							temp_x += 1
						
						data['mapa'][current_y1] = templine
		#fsdfsdfsdfsdf
		FPS = clock.get_fps()
		if SHOW_FPS:
			show_fps(FPS)
		clock.tick(MAX_FPS)
		
	
	pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	return EXIT_GAME, MUTE_MUSIC
	

