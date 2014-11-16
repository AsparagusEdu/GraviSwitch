import pygame
import worldshift
class Wall(pygame.sprite.Sprite, worldshift.World_Shift):
	spd_x = 0
	spd_y = 0
	def __init__(self, init_x, init_y):
		pygame.sprite.Sprite.__init__(self)
	
		self.image = pygame.image.load('images/wall.png').convert()
		self.rect = self.image.get_rect() 
		
		self.init_x = init_x
		self.init_y = init_y
		
		self.rect.x = init_x
		self.rect.y = init_y
		
	def reboot(self, grav):
		self.rect.x = self.init_x
		self.rect.y = self.init_y
		
