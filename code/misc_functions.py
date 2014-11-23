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

#def confirmation(): "Are you sure?"
	

def show_fps(FPS):
	fonty = pygame.font.SysFont('Pokemon FireLeaf', 20)
	image = fonty.render('FPS:' + str(int(FPS)), False, (0,0,0))
	SCREEN.blit(image, (0,0))

def dead_player():
	Retry_image = pygame.image.load('images/retry.png').convert()					 #|
	Retry_rect = Retry_image.get_rect()												 #|
	Retry_pos = (SCREEN_WIDTH/2 - Retry_rect.w/2 , SCREEN_HEIGHT/2 - Retry_rect.h/2) #|
	
	SCREEN.blit(Retry_image, Retry_pos)
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
	
