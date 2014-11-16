import pygame
from load_level import load_level
from constants import SCREEN, BLOCK_SIZE, MAX_FPS, SLOW_MODE
from player import *
from read_file import ReadFile
from misc_functions import *

def Level(nombre):
	
	
	mapa, fondo = ReadFile(nombre + '.txt') #mapa es matriz y fondo es el nombre del archivo + extension del fondo
	fondo = pygame.image.load('images/' + fondo).convert()
	music = pygame.mixer.music.load('sound/music/cheetah2.mp3')
	pygame.mixer.music.play(-1, 0.7)
	
	world_objects, lvl_dims, world, sprite_list, updatable_list, box_list, col_list, p_inicio, p_id = load_level(mapa)
	
	Retry = pygame.image.load('images/retry.png').convert()
	
	pos_x, pos_y = p_inicio #Posiciones de inicio
	player = Player(pos_x, pos_y)
	player.ID = p_id
	player.level = col_list #Definimos el nivel dentro del usuario para que tenga referencia de este
	
	for box in box_list.sprites(): #Annade propiedades del nivel a las cajas
		box.level = col_list
		box.boxes = box_list
		box.player = player
	
	sprite_list.add(player) 
	updatable_list.add(player)
	
	gravity = 'S'
	lvl_exit = False #Variable para terminar de procesar el nivel
	lvl_retry = True #Variable para reintentar
	milisecs = 16 #Milisegundos ideales que se demoraria en cada cuadro.
	
	world_spd = [0,0] #Velocidades con las que se mueve el mundo
	
	world_pos = [0,0] #Posicion de la esquina superior izquierda del mundo	
	
	while not lvl_exit:
		
		while lvl_retry:
			#print world_pos
			clock = pygame.time.Clock() #Reloj
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
					elif event.key == pygame.K_r:
						player.dead = True
					elif event.key == pygame.K_LEFT and not player.touch_O(0):
						player.go_left()
						print 'Tecla - Izquierda'
					elif event.key == pygame.K_RIGHT and not player.touch_E(0):
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
					elif event.key == pygame.K_i: #DEBUG
						world_spd[1] = -2
					elif event.key == pygame.K_k: #DEBUG
						world_spd[1] = 2
					elif event.key == pygame.K_l: #DEBUG
						world_spd[0] = 2
					elif event.key == pygame.K_j: #DEBUG
						world_spd[0] = -2
				elif event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT and player.spd_x < 0:
						player.stop()
					elif event.key == pygame.K_RIGHT and player.spd_x > 0:
						player.stop()
					elif event.key == pygame.K_i: #DEBUG
						world_spd[1] = 0
					elif event.key == pygame.K_k: #DEBUG
						world_spd[1] = 0
					elif event.key == pygame.K_l: #DEBUG
						world_spd[0] = 0
					elif event.key == pygame.K_j: #DEBUG
						world_spd[0] = 0
					
			if SLOW_MODE:
				times_to_update = milisecs/16 #Veces en la que el juego actualiza sus objetos.
				print 'Mili -', milisecs #DEBUG
				print 'Upda -', times_to_update #DEBUG
			else:
				times_to_update = 1
				
			for times in range(times_to_update):
				updatable_list.update(gravity)
				for worldy in world.sprites(): #Mueve al mundo dependiendo del parametro.
					world_pos, world_spd[0] = worldy.world_shift(world_spd, world_pos, lvl_dims)
					#world_pos[0] = world_temp_pos[0] /world_objects
					#world_pos[1] = world_temp_pos[1] /world_objects
					#Todo menos player forma parte de world
					
			if player.dead == True:
				lvl_retry = False
			
			if not player.dead:
				SCREEN.blit(fondo, (0,0))
				sprite_list.draw(SCREEN)
				pygame.display.flip()
			'''
			if player.rect.y >= SCREEN_HEIGHT: #En caso de salirse de la pantalla
				return False
			if player.rect.bottom <= 0:
				return False
			if player.rect.right <= 0:
				return False
			if player.rect.left >= SCREEN_WIDTH:
				return False
			'''
			clock.tick(MAX_FPS)
			milisecs = clock.get_time() # Milisegundos que demora en hacer un cuadro.
		#Menu al morir D:
		
		SCREEN.blit(Retry, (0,0))
		pygame.display.flip()
		
		
		
		for event in pygame.event.get():
			clock = pygame.time.Clock() #Reloj
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_n:
					return False
				elif event.key == pygame.K_y:
					lvl_retry = True
					for obj in sprite_list.sprites():
						gravity = 'S'
						world_spd = [0,0]
						world_pos = [0,0]
						obj.reboot(gravity)
			clock.tick(10)
		
#def shift_world(shift_x, shift_y):
	
