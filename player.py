import pygame
class Player(pygame.sprite.Sprite):
	spd_x = 0
	spd_y = 0
	def __init__(self, x_init, y_init):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.image.load('images/Isaac1.png')
		self.rect = self.image.get_rect()
		self.rect.x = x_init + 8
		self.rect.y = y_init
	#def calc_grav():
		
	def update(self):
		self.rect.x += self.spd_x
		self.rect.y += self.spd_y
	
	def go_left(self):
		self.spd_x = -3
	def go_right(self):
		self.spd_x = 3
	def stop(self):
		self.spd_x = 0
		
		
