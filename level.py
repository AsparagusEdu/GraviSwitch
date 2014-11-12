import pygame
from load_level import load_level
from constants import screen, BLOCK_SIZE, FPS
from player import *
from read_file import ReadFile

def Level(nombre):
	clock = pygame.time.Clock()
	exit_lvl = False
	mapa, fondo = ReadFile(nombre + '.txt')
	fondo = pygame.image.load('images/' + fondo).convert()
	sprite_list, updatable_list, box_list, col_list, p_inicio, p_id = load_level(mapa)
	
	pos_x, pos_y = p_inicio
	player = Player(pos_x, pos_y)
	player.ID = p_id
	player.level = col_list #Definimos el nivel dentro del usuario para que tenga referencia de este
	
	sprite_list.add(player)
	updatable_list.add(player)
	
	gravity = 'S'
	
	while not exit_lvl:
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				exit_lvl = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					exit_lvl = True
				'''
				if event.key == pygame.K_r:
					return False
				'''
			
				if event.key == pygame.K_LEFT:
					player.go_left()
				if event.key == pygame.K_RIGHT:
					player.go_right()
				if event.key == pygame.K_UP:
					player.jump()
				if event.key == pygame.K_w:
					gravity = 'N'
				if event.key == pygame.K_s:
					gravity = 'S'
				if event.key == pygame.K_d:
					gravity = 'E'
				if event.key == pygame.K_a:
					gravity = 'O'
				
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT and player.spd_x < 0:
					player.stop()
				if event.key == pygame.K_RIGHT and player.spd_x > 0:
					player.stop()
				
		updatable_list.update(gravity)
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
	
