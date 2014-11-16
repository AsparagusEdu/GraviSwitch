import pygame
class Spike(pygame.sprite.Sprite):
	spd_x = 0
	spd_y = 0
	def __init__(self, init_x, init_y):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load('images/spike.png').convert_alpha()
		self.rect = self.image.get_rect() 
		
		self.init_x = init_x
		self.init_y = init_y
		
		self.rect.x = init_x
		self.rect.y = init_y
		
	def world_shift(self, shift_x, shift_y):
		self.rect.x += shift_x
		self.rect.y += shift_y
		
	def reboot(self, grav):
		self.rect.x = self.init_x
		self.rect.y = self.init_y
