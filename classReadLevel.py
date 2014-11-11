import pygame
from classWall import *
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
	wall_list = pygame.sprite.Group()
	pos_y = 0
	for linea in mapa:
		pos_x = 0
		for cuadro in linea:
			if cuadro == 'W':
				wall = Wall(pos_x*32, pos_y*32)
				wall_list.add(wall)
			pos_x += 1
		pos_y += 1
	return wall_list


