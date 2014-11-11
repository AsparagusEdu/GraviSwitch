import pygame
class Wall(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load('images/wall.png')
		self.rect = self.image.get_rect()		
		self.rect.y = y
		self.rect.x = x
