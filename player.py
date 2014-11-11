import pygame
class Player(pygame.sprite.Sprite):
	spd_x = 0
	spd_y = 0
	
	def __init__(self, x_init, y_init):
		self.image = pygame.image.load('images/Isaac1')
		self.rect = self.image.get_rect()
		self.rect.x = x_init + 8
		self.rect.y = y_init
	#def calc_grav():
		
	def update():
		self.rect.x += spd_x
		self.rect.y += spd_y
		
