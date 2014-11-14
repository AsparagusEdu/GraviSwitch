import pygame
from load_level import load_level
from constants import screen, BLOCK_SIZE, FPS
from player import *
from read_file import ReadFile

def Level(nombre):
	
	
	mapa, fondo = ReadFile(nombre + '.txt') #mapa es matriz y fondo es el nombre del archivo + extension del fondo
	fondo = pygame.image.load('images/' + fondo).convert()
	sprite_list, updatable_list, box_list, col_list, p_inicio, p_id = load_level(mapa)
	
	Retry = pygame.image.load('images/retry.png').convert()
	
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
	lvl_retry = True
	while not lvl_exit:
		while lvl_retry:
			clock = pygame.time.Clock() #Reloj
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					lvl_retry = False
					lvl_exit = True
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						lvl_retry = False
					elif event.key == pygame.K_r:
						player.dead = True
					elif event.key == pygame.K_LEFT and not player.touch_O():
						player.go_left()
						print 'Tecla - Izquierda'
					elif event.key == pygame.K_RIGHT and not player.touch_E():
						player.go_right()
						print 'Tecla - Derecha'
					elif event.key == pygame.K_UP and player.touch_S():
						player.jump()
						print 'Tecla - Salto'
					elif event.key == pygame.K_w:
						switch = True
						for box in box_list.sprites():
							if box.state == 'AIR':
								switch = False
						if switch:
							gravity = 'N'
							print 'Gravedad - NORTE' #DEBUG
					elif event.key == pygame.K_s:
						switch = True
						for box in box_list.sprites():
							if box.state == 'AIR':
								switch = False
						if switch:
							gravity = 'S'
							print 'Gravedad - SUR' #DEBUG
					elif event.key == pygame.K_d:
						switch = True
						for box in box_list.sprites():
							if box.state == 'AIR':
								switch = False
						if switch:
							gravity = 'E'
							print 'Gravedad - ESTE'
					elif event.key == pygame.K_a:
						switch = True
						for box in box_list.sprites():
							if box.state == 'AIR':
								switch = False
						if switch:
							gravity = 'O'
							print 'Gravedad - OESTE'
				elif event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT and player.spd_x < 0:
						player.stop()
					elif event.key == pygame.K_RIGHT and player.spd_x > 0:
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
		screen.blit(Retry, (0,0))
		pygame.display.flip()
		for event in pygame.event.get():
			clock = pygame.time.Clock() #Reloj
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
				elif event.key == pygame.K_n:
					pygame.quit()
				elif event.key == pygame.K_y:
					lvl_retry = True
					for obj in updatable_list.sprites():
						gravity = 'S'
						obj.reboot(gravity)
			clock.tick(FPS)
		
