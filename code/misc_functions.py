import pygame
from constants import SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH
from Box import *

def static_boxes(box_list):#Recibe lista de objetos "Box" como parametro
	for box in box_list.sprites():
		if box.state == 'AIR':
			return False
	return True

def get_image(sheet, x, y, width, height):
		image = pygame.Surface([width, height])
		image.blit(sheet, (0, 0), (x, y, width, height))
		return image

def show_fps(FPS):
	fonty = pygame.font.SysFont('Arial', 20) #Pokemon FireLeaf
	image = fonty.render('FPS:' + str(int(FPS)), False, (0,0,0))
	SCREEN.blit(image, (0,0))

def check_if_box(block):
	if type(block) is Box:
		return True
	elif type(block) is JumpBox:
		return True
	return False
	
	
	
	
