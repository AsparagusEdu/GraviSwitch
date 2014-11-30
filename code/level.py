import pygame
import constants as C
from load_level import load_level
import sound
from player import *
from misc_functions import static_boxes, show_fps
from PauseScreen import Pause_Screen
from dead_player import DeadPlayer

def Level(nombre, MUTE_MUSIC, evento_final = None):
	
	C.SCREEN.blit(pygame.image.load('images/gui/loading.png'),(0,0))
	pygame.display.flip()
	
	lvl_info, lvl_lists = load_level('main/' + nombre + '.txt')
	
	p_id = lvl_info[0]
	p_inicio = lvl_info[1]
	fondo = lvl_info[2]
	fondo = pygame.image.load('images/backgrounds/' + fondo).convert()
	musica = lvl_info[3]
	pared = lvl_info[4]
	graviswitch = lvl_info[5]
	
	col_list = lvl_lists[0]
	box_list = lvl_lists[1]
	wall_list = lvl_lists[2]
	door_list = lvl_lists[3]
	updatable_list = lvl_lists[4]
	sprite_list = lvl_lists[5]
	bfilter_list = lvl_lists[6]
	checkpoint_list = lvl_lists[7]
	
	#-----IMAGENES, RECTANGULOS Y POSICIONES DE MENSAJES DE VICTORIA Y DERROTA--------|
																					 #|
	Win_image = pygame.image.load('images/gui/win.png').convert()                        #|
	Win_rect = Win_image.get_rect()                                                  #|
	Win_pos = (C.SCREEN_WIDTH/2 - Win_rect.w/2 , C.SCREEN_HEIGHT/2 - Win_rect.h/2)   #|
	
	NOFPS_SCREEN = pygame.image.load('images/demo/ben.png').convert()
	#---------------------------------------------------------------------------------|
	
	pos_x, pos_y = p_inicio #Posiciones de inicio
	player = Player(pos_x, pos_y)
	player.ID = p_id
	player.level = col_list #Definimos el nivel dentro del usuario para que tenga referencia de este
	player.doors = door_list
	player.checkpoints = checkpoint_list
	
	for box in box_list.sprites(): #Annade propiedades del nivel a las cajas
		box.level = bfilter_list
		for coli in col_list.sprites():
			box.level.add(coli)
		box.boxes = box_list
		box.player = player
	
	
	for wall in wall_list.sprites():
		wall.level = wall_list
		wall.change_terrain(pared)
	
	
	#sprite_list.add(player) 
	updatable_list.add(player)
	
	gravity = 'S'
	lvl_exit = False #Variable para terminar de procesar el nivel
	
	music = pygame.mixer.music.load('sound/music/' + musica)
	pygame.mixer.music.play(-1)
	if MUTE_MUSIC:
		pygame.mixer.music.pause()
	
	clock = pygame.time.Clock() #Reloj
	while not lvl_exit:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False, False, True #Nivel terminado, Volver al Menu, Salir del juego
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pause, MUTE_MUSIC = Pause_Screen(NOFPS_SCREEN, MUTE_MUSIC)
					player.spd_x = 0
					if pause == 'Continuar':
						pass
					elif pause == 'Reiniciar':
						pygame.mixer.music.fadeout(500)
						C.SCREEN.blit(pygame.image.load('images/gui/loading.png'),(0,0))
						pygame.display.flip()
						for obj in updatable_list.sprites():
							gravity = 'S'
							obj.reboot(gravity)
						for che in checkpoint_list.sprites():
							che.reboot()
						player.rect.x, player.rect.y = pos_x, pos_y
						player.init_x, player.init_y = pos_x, pos_y
						pygame.time.wait(1000)
						pygame.mixer.music.play(-1)
					elif pause == 'Menu':
						return False, False, False, MUTE_MUSIC
					elif pause == 'Salir':
						return False, False, True, MUTE_MUSIC
				elif event.key == pygame.K_m:
					if MUTE_MUSIC:
						print 'MUSIC - ON'
						MUTE_MUSIC = False
						pygame.mixer.music.unpause()
					else:
						print 'MUSIC - OFF'
						MUTE_MUSIC = True
						pygame.mixer.music.pause()
						
				elif event.key == pygame.K_LEFT and not player.bounce and not player.crouch:
					player.go_left()
					print 'Tecla - Izquierda'
				elif event.key == pygame.K_RIGHT and not player.bounce and not player.crouch:
					player.go_right()
					print 'Tecla - Derecha'
				elif event.key == pygame.K_UP and player.touch_S(0) and not player.crouch:
					sound.jump.play()
					player.jump()
					print 'Tecla - Salto'
				elif event.key == pygame.K_DOWN and player.touch_S(0) and player.spd_x == 0:
					player.crouch = True
					player.image = player.crouch_image
					if player.direction == 'Left':
						player.image = pygame.transform.flip(player.image, True, False)
					print 'Crouch - ON'
					#player.spd_x = 0
				
				if graviswitch:
					if event.key == pygame.K_w:
						switch = True
						if static_boxes(box_list):
							sound.graviswitch.play()
							gravity = 'N'
							#print 'Gravedad - NORTE' #DEBUG
					elif event.key == pygame.K_s:
						if static_boxes(box_list):
							gravity = 'S'
							sound.graviswitch.play()
							#print 'Gravedad - SUR' #DEBUG
					elif event.key == pygame.K_d:
						if static_boxes(box_list):
							gravity = 'E'
							sound.graviswitch.play()
							#print 'Gravedad - ESTE'
					elif event.key == pygame.K_a:
						if static_boxes(box_list):
							gravity = 'O'
							sound.graviswitch.play()
							#print 'Gravedad - OESTE'
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT and player.spd_x < 0:
					player.stop()
				elif event.key == pygame.K_RIGHT and player.spd_x > 0:
					player.p_input_l = False
					player.p_input_r = False
					player.stop()
				elif event.key == pygame.K_DOWN and player.crouch:
					player.crouch = False
					player.image = player.stand_image
					if player.direction == 'Left':
						player.image = pygame.transform.flip(player.image, True, False)
					print 'Crouch - OFF'

		FPS = clock.get_fps()
		
		box_list.update(gravity, FPS/60)
		player.update(gravity, FPS/60)
		#updatable_list.update(gravity)
			
		if player.dead == True:
			print 'DEAD'
			if not MUTE_MUSIC:
				pygame.mixer.music.pause()
			revive, G_OVER = DeadPlayer(NOFPS_SCREEN) #dead_player()
			if revive:
				if not MUTE_MUSIC:
					pygame.mixer.music.unpause()
				
				for obj in updatable_list.sprites():
					gravity = 'S'
					obj.reboot(gravity)
			elif not G_OVER:
				return False, False, False, MUTE_MUSIC
			else:
				return False, False, True, MUTE_MUSIC
			
		elif player.win == True:
			if evento_final == 'NivComp':
				while True:
					C.SCREEN.blit(Win_image, Win_pos)
					pygame.display.flip()
					pygame.time.wait(500)
					for event in pygame.event.get():
						clock = pygame.time.Clock() #Reloj
						if event.type == pygame.QUIT:
							return True, False, True, MUTE_MUSIC
						if event.type == pygame.KEYDOWN:
							return True, False, False, MUTE_MUSIC
						clock.tick(60)
			else:
				return True, True, False, MUTE_MUSIC
			
		else:
			C.SCREEN.blit(fondo, (0,0))
			door_list.draw(C.SCREEN)
			C.SCREEN.blit(player.image, (player.rect.x - 8, player.rect.y -4)) #Modificable
			sprite_list.draw(C.SCREEN)
			bfilter_list.draw(C.SCREEN)
			checkpoint_list.draw(C.SCREEN)
			
			if C.SHOW_FPS:
				NOFPS_SCREEN.blit(C.SCREEN, (0,0))
				show_fps(FPS)
			pygame.display.flip()

		clock.tick(C.MAX_FPS)
	
	
		''' #DEMO
def Demo_Level(nombre):
	
	SCREEN.blit(pygame.image.load('images/loading.png'),(0,0))
	pygame.display.flip()
	
	lvl_info, lvl_lists = load_level('demo/' + nombre + '.txt')
	
	p_id = lvl_info[0]
	p_inicio = lvl_info[1]
	fondo = lvl_info[2]
	fondo = pygame.image.load('images/backgrounds/' + fondo).convert()
	musica = lvl_info[3]
	pared = lvl_info[4]
	
	col_list = lvl_lists[0]
	box_list = lvl_lists[1]
	wall_list = lvl_lists[2]
	door_list = lvl_lists[3]
	updatable_list = lvl_lists[4]
	sprite_list = lvl_lists[5]
	bfilter_list = lvl_lists[6]
	checkpoint_list = lvl_lists[7]
	
	#-----IMAGENES, RECTANGULOS Y POSICIONES DE MENSAJES DE VICTORIA Y DERROTA--------|
	Retry_image = pygame.image.load('images/retry.png').convert()					 #|
	Retry_rect = Retry_image.get_rect()												 #|
	Retry_pos = (SCREEN_WIDTH/2 - Retry_rect.w/2 , SCREEN_HEIGHT/2 - Retry_rect.h/2) #|
																					 #|
	Win_image = pygame.image.load('images/win.png').convert()                        #|
	Win_rect = Win_image.get_rect()                                                  #|
	Win_pos = (SCREEN_WIDTH/2 - Retry_rect.w/2 , SCREEN_HEIGHT/2 - Retry_rect.h/2)   #|
	#---------------------------------------------------------------------------------|
	
	pos_x, pos_y = p_inicio #Posiciones de inicio
	player = Player(pos_x, pos_y)
	player.ID = p_id
	player.level = col_list #Definimos el nivel dentro del usuario para que tenga referencia de este
	player.doors = door_list
	player.checkpoints = checkpoint_list
	
	for box in box_list.sprites(): #Annade propiedades del nivel a las cajas
		box.level = bfilter_list
		for coli in col_list.sprites():
			box.level.add(coli)
		box.boxes = box_list
		box.player = player
	
	
	for wall in wall_list.sprites():
		wall.level = wall_list
		wall.check_terrain(pared)
	
	
	sprite_list.add(player) 
	updatable_list.add(player)
	
	gravity = 'S'
	lvl_exit = False #Variable para terminar de procesar el nivel
	lvl_retry = True #Variable para reintentar
	milisecs = 170 #Milisegundos ideales que se demoraria en cada cuadro.
	
	if MUSIC:
		music = pygame.mixer.music.load('sound/music/' + musica)
		pygame.mixer.music.play(-1)
	
	clock = pygame.time.Clock() #Reloj
	while not lvl_exit:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False, True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					return False, False
				elif event.key == pygame.K_r:
					player.dead = True
				elif event.key == pygame.K_LEFT:
					player.go_left()
					print 'Tecla - Izquierda'
				elif event.key == pygame.K_RIGHT:
					player.go_right()
					print 'Tecla - Derecha'
				elif event.key == pygame.K_UP and player.touch_S(0):
					player.jump()
					print 'Tecla - Salto'
				elif event.key == pygame.K_w:
					switch = True
					if static_boxes(box_list):
						gravity = 'N'
						print 'Gravedad - NORTE' #DEBUG
				elif event.key == pygame.K_s:
					if static_boxes(box_list):
						gravity = 'S'
						print 'Gravedad - SUR' #DEBUG
				elif event.key == pygame.K_d:
					if static_boxes(box_list):
						gravity = 'E'
						print 'Gravedad - ESTE'
				elif event.key == pygame.K_a:
					if static_boxes(box_list):
						gravity = 'O'
						print 'Gravedad - OESTE'
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT and player.spd_x < 0:
					player.stop()
				elif event.key == pygame.K_RIGHT and player.spd_x > 0:
					player.stop()
		
		FPS = clock.get_fps()
		print FPS
		box_list.update(gravity, FPS/60)
		player.update(gravity, FPS/60)
		#updatable_list.update(gravity)
			
		if player.dead == True:
			lvl_retry = False
			print 'DEAD'
			SCREEN.blit(Retry_image, Retry_pos)
			pygame.display.flip()
			while not lvl_retry	:	
				for event in pygame.event.get():
					clock = pygame.time.Clock() #Reloj
					if event.type == pygame.QUIT:
						return False, True
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_n:
							return False, False
						elif event.key == pygame.K_y:
							lvl_retry = True
							for obj in updatable_list.sprites():
								gravity = 'S'
								obj.reboot(gravity)
					clock.tick(10)
		elif player.win == True:
			while True:
				SCREEN.blit(Win_image, Win_pos)
				pygame.display.flip()
				for event in pygame.event.get():
					clock = pygame.time.Clock() #Reloj
					if event.type == pygame.QUIT:
						return True, True
					if event.type == pygame.KEYDOWN:
						return True, False
					clock.tick(60)
			
		else:
			SCREEN.blit(fondo, (0,0))
			door_list.draw(SCREEN)
			sprite_list.draw(SCREEN)
			bfilter_list.draw(SCREEN)
			checkpoint_list.draw(SCREEN)
			pygame.display.flip()
		
		clock.tick(MAX_FPS)
		
		milisecs = clock.get_time() # Milisegundos que demora en hacer un cuadro.
		'''	
		
		
	#Menu al morir D:
		
		
