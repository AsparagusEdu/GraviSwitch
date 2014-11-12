import pygame
from Wall import Wall
from constants import screen
from player import *

def ReadFile(nombre):
	archivo = open("levels/" + nombre)
	mapa = []
	for linea in archivo:
		linea = linea.strip("\n")
		if linea[0] != '#':
			linea.split()
			mapa.append(linea)
			print linea
		else:
			fondo = linea.strip('#')
			print fondo

	archivo.close()
	return mapa, fondo
	
def load_level(mapa):
	sprite_list = pygame.sprite.Group()
	updatable_list = pygame.sprite.Group()
	player_list = pygame.sprite.Group()
	id_given = 0
	pos_y = 0
	for linea in mapa:
		pos_x = 0
		for cuadro in linea:
			if cuadro == 'W':
				wall = Wall(pos_x*32, pos_y*32)
				sprite_list.add(wall)
				wall.ID = id_given #Cada bloque va a tener su propio ID, para comparar colisiones.
				id_given += 1 
			if cuadro == 'P':
				p_inicio = (pos_x*32, pos_y*32)
				p_id = id_given
				id_given += 1
			pos_x += 1
		pos_y += 1
	return sprite_list, updatable_list, p_inicio, p_id

def Level(nombre):
	clock = pygame.time.Clock()
	exit_lvl = False
	mapa, fondo = ReadFile(nombre + '.txt')
	fondo = pygame.image.load('images/' + fondo)
	sprite_list, updatable_list, p_inicio, p_id = load_level(mapa)
	
	pos_x, pos_y = p_inicio
	player = Player(pos_x, pos_y)
	player.ID = p_id
	player.level = sprite_list #Definimos el nivel dentro del usuario para que tenga referencia de este
	
	sprite_list.add(player)
	updatable_list.add(player)
	
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
					
				'''
				if event.key == pygame.K_w:
					gravity = 'N'
				if event.key == pygame.K_s:
					gravity = 'S'
				if event.key == pygame.K_d:
					gravity = 'E'
				if event.key == pygame.K_a:
					gravity = 'O'
				'''
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT and player.spd_x < 0:
					player.stop()
				if event.key == pygame.K_RIGHT and player.spd_x > 0:
					player.stop()
				
			'''
		
		lista_cajas = room.box_list.sprites()
		
		# --- Actualizar pantalla ---
		'''
		updatable_list.update()
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
		clock.tick(60)
	
