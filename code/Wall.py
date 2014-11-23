import pygame
from constants import CHROMA_KEY, SCREEN_HEIGHT, SCREEN_WIDTH
from misc_functions import get_image
class Wall(pygame.sprite.Sprite):
	spd_x = 0
	spd_y = 0
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load('images/tiles/box.png').convert()
		self.rect = self.image.get_rect()		
		self.rect.y = y
		self.rect.x = x
		
	def check_terrain(self, pared): #Cambia la imagen de terreno dependiendo de que otras paredes hayan.
		hit_list1 = pygame.sprite.spritecollide(self, self.level, False)
		
		self.rect.y -=2
		hit_list2 = pygame.sprite.spritecollide(self, self.level, False)
		
		if len(hit_list2) > len(hit_list1) or self.rect.top < 0:
			top = True
		else:
			top = False
			
		self.rect.y +=4
		
		hit_list2 = pygame.sprite.spritecollide(self, self.level, False)
		
		if len(hit_list2) > len(hit_list1) or self.rect.bottom > SCREEN_HEIGHT:
			bottom = True
		else:
			bottom = False
		self.rect.y -=2
			
		self.rect.x -=2
		hit_list2 = pygame.sprite.spritecollide(self, self.level, False)
		if len(hit_list2) > len(hit_list1) or self.rect.left < 0:
			left = True
		else:
			left = False
					
		self.rect.x +=4
		
		hit_list2 = pygame.sprite.spritecollide(self, self.level, False)
		
		if len(hit_list2) > len(hit_list1) or self.rect.right > SCREEN_WIDTH:
			right = True
		else:
			right = False
		self.rect.x -=2
		
		self.change_terrain(pared, top, bottom, left, right)
		
	def change_terrain(self, pared, top, bottom, left, right):
		sheet = pygame.image.load('images/tiles/' + pared).convert()
		
		if top:
			if bottom:
				if left:
					if right:
						cuadro = get_image(sheet, 0,0, 32,32).convert()
					else:
						cuadro = get_image(sheet, 32, 0, 32,32).convert()
				else:
					if right:
						cuadro = get_image(sheet, 64, 0, 32,32).convert()
					else:
						cuadro = get_image(sheet, 96, 0, 32,32).convert()
						
			else:
				if left:
					if right:
						cuadro = get_image(sheet, 0, 32, 32,32).convert()
					else:
						cuadro = get_image(sheet, 32, 32, 32,32).convert()
				else:
					if right:
						cuadro = get_image(sheet, 64, 32, 32,32).convert()
					else:
						cuadro = get_image(sheet, 96, 32, 32,32).convert()
		else:
			if bottom:
				if left:
					if right:
						cuadro = get_image(sheet, 0, 64, 32,32).convert()
					else:
						cuadro = get_image(sheet, 32, 64, 32,32).convert()
				else:
					if right:
						cuadro = get_image(sheet, 64, 64, 32,32).convert()
					else:
						cuadro = get_image(sheet, 96, 64, 32,32).convert()
			else:
				if left:
					if right:
						cuadro = get_image(sheet, 0, 96, 32,32).convert()
					else:
						cuadro = get_image(sheet, 32, 96, 32,32).convert()
				else:
					if right:
						cuadro = get_image(sheet, 64, 96, 32,32).convert()
					else:
						cuadro = get_image(sheet, 96, 96, 32,32).convert()
		
		#cuadro.set_colorkey(CHROMA_KEY)
		self.image = cuadro
		

