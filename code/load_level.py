import pygame
from Wall import Wall
from Box import Box
from Spike import Spike
from constants import BLOCK_SIZE

def load_level(mapa):
	sprite_list = pygame.sprite.Group()
	updatable_list = pygame.sprite.Group() #Un grupo por tipo de accion a sprites.
	box_list = pygame.sprite.Group()
	col_list = pygame.sprite.Group()
	world = pygame.sprite.Group()
	
	id_given = 0
	pos_y = 0
	lvl_width = 0
	for linea in mapa:
		pos_x = 0
		for cuadro in linea:
			if cuadro == 'W':
				wall = Wall(pos_x*BLOCK_SIZE, pos_y*BLOCK_SIZE)
				sprite_list.add(wall)
				col_list.add(wall)
				world.add(wall)
				wall.ID = id_given #Cada bloque va a tener su propio ID, para comparar colisiones.
				id_given += 1 
			if cuadro == 'P':
				p_inicio = (pos_x*BLOCK_SIZE, pos_y*BLOCK_SIZE)
				p_id = id_given
				id_given += 1
			if cuadro == 'B':
				box = Box(pos_x*BLOCK_SIZE, pos_y*BLOCK_SIZE)
				sprite_list.add(box)
				col_list.add(box)
				updatable_list.add(box)
				box_list.add(box)
				world.add(box)
				box.ID = id_given #Cada bloque va a tener su propio ID, para comparar colisiones.
				id_given += 1
			if cuadro == 'S':
				spike = Spike(pos_x*BLOCK_SIZE, pos_y*BLOCK_SIZE)
				sprite_list.add(spike)
				col_list.add(spike)
				world.add(spike)
				spike.ID = id_given
				id_given += 1
			pos_x += 1
		if pos_x > lvl_width:
			lvl_width = pos_x
		pos_y += 1
	lvl_dims =(lvl_width, pos_y)
	ex = id_given -1,lvl_dims, world, sprite_list, updatable_list, box_list, col_list, p_inicio, p_id
	return ex
