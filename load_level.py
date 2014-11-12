import pygame
from Wall import Wall
from Box import Box
from constants import BLOCK_SIZE

def load_level(mapa):
	sprite_list = pygame.sprite.Group()
	updatable_list = pygame.sprite.Group() #Un grupo por tipo de accion a sprites.
	box_list = pygame.sprite.Group()
	col_list = pygame.sprite.Group()
	
	id_given = 0
	pos_y = 0
	for linea in mapa:
		pos_x = 0
		for cuadro in linea:
			if cuadro == 'W':
				wall = Wall(pos_x*BLOCK_SIZE, pos_y*BLOCK_SIZE)
				sprite_list.add(wall)
				col_list.add(wall)
				wall.ID = id_given #Cada bloque va a tener su propio ID, para comparar colisiones.
				id_given += 1 
			if cuadro == 'P':
				p_inicio = (pos_x*BLOCK_SIZE, pos_y*BLOCK_SIZE)
				p_id = id_given
				id_given += 1
			if cuadro == 'B':
				box = Box(pos_x*BLOCK_SIZE, pos_y*BLOCK_SIZE)
				sprite_list.add(box)
				col_list.add(wall)
				updatable_list.add(box)
				box.ID = id_given #Cada bloque va a tener su propio ID, para comparar colisiones.
				id_given += 1 
			pos_x += 1
		pos_y += 1
	ex = sprite_list, updatable_list, box_list, col_list, p_inicio, p_id
	return ex
