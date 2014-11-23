import pygame
class Box_Filter(pygame.sprite.Sprite):
	spd_x = 0
	spd_y = 0
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load('images/tiles/boxfilter.png').convert_alpha()
		self.rect = self.image.get_rect()		
		self.rect.y = y
		self.rect.x = x
