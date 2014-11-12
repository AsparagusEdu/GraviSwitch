import pygame
class Box(pygame.sprite.Sprite):
	spd_x = 0
	spd_y = 0
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load('images/box.png').convert()
		self.rect = self.image.get_rect()		
		self.rect.y = y
		self.rect.x = x
	
	def calc_grav(self, grav):
		if grav == 'N':
			#if self.spd_y == 0:
				self.spd_y = -6
		elif grav == 'S':
			#if self.spd_y == 0:
				self.spd_y = 6
		
		
	def update(self, grav):
		self.calc_grav(grav)
		self.rect.x += self.spd_x
		self.rect.y += self.spd_y
