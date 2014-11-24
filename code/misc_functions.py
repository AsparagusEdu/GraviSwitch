import pygame
from constants import SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH

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

def dead_player():
	menu_image = pygame.image.load('images/retry.png').convert()					 #|
	menu_rect = menu_image.get_rect()												 #|
	menu_pos = (SCREEN_WIDTH/2 - menu_rect.w/2 , SCREEN_HEIGHT/2 - menu_rect.h/2) #|
	
	SCREEN.blit(menu_image, menu_pos)
	pygame.display.flip()
	while True	:	
		for event in pygame.event.get():
			clock = pygame.time.Clock() #Reloj
			if event.type == pygame.QUIT:
				return False, True #Reintentar, Salir del Juego
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_n:
					return False, False
				elif event.key == pygame.K_y:
					return True, False
			clock.tick(10)
	
