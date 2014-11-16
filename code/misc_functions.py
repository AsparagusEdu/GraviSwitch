import pygame

def static_boxes(box_list):#Recibe lista de objetos "Box" como parametro
	for box in box_list.sprites():
		if box.state == 'AIR':
			return False
	return True
