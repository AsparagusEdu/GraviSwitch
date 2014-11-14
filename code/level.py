import pygame
from load_level import load_level
from constants import screen, BLOCK_SIZE, FPS
from player import *
from read_file import ReadFile

def Level(nombre):
	clock = pygame.time.Clock() #Reloj
	
	mapa, fondo = ReadFile(nombre + '.txt') #mapa es matriz y fondo es el nombre del archivo + extension del fondo
	fondo = pygame.image.load('images/' + fondo).convert()
	sprite_list, updatable_list, box_list, col_list, p_inicio, p_id = load_level(mapa)
	
	pos_x, pos_y = p_inicio
	player = Player(pos_x, pos_y)
	player.ID = p_id
	player.level = col_list #Definimos el nivel dentro del usuario para que tenga referencia de este
	
	for box in box_list.sprites():
		box.level = col_list
		box.boxes = box_list
	
	
	sprite_list.add(player)
	updatable_list.add(player)
	
	gravity = 'S'
	lvl_exit = False
	
	while not lvl_exit:
		lvl_retry = True
		while lvl_retry:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					lvl_retry = False
					lvl_exit = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						lvl_retry = False
					if event.key == pygame.K_r:
						player.dead = True
					if event.key == pygame.K_LEFT and not player.touch_O():
						player.go_left()
						print 'Tecla - Izquierda'
					if event.key == pygame.K_RIGHT and not player.touch_E():
						player.go_right()
						print 'Tecla - Derecha'
					if event.key == pygame.K_UP and player.touch_S():
						player.jump()
						print 'Tecla - Salto'
					if event.key == pygame.K_w:
						switch = True
						for box in box_list.sprites():
							if box.state == 'AIR':
								switch = False
						if switch:
							gravity = 'N'
							print 'Gravedad - NORTE' #DEBUG
					if event.key == pygame.K_s:
						switch = True
						for box in box_list.sprites():
							if box.state == 'AIR':
								switch = False
						if switch:
							gravity = 'S'
							print 'Gravedad - SUR' #DEBUG
					if event.key == pygame.K_d:
						switch = True
						for box in box_list.sprites():
							if box.state == 'AIR':
								switch = False
						if switch:
							gravity = 'E'
							print 'Gravedad - ESTE'
					if event.key == pygame.K_a:
						switch = True
						for box in box_list.sprites():
							if box.state == 'AIR':
								switch = False
						if switch:
							gravity = 'O'
							print 'Gravedad - OESTE'
					
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT and player.spd_x < 0:
						player.stop()
					if event.key == pygame.K_RIGHT and player.spd_x > 0:
						player.stop()
					
			updatable_list.update(gravity)
			if player.dead == True:
				lvl_retry = False
			screen.blit(fondo, (0,0))
			sprite_list.draw(screen)
			
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
			clock.tick(FPS)
	
