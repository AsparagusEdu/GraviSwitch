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
		
	def check_terrain_1(self): #Cambia la imagen de terreno dependiendo de que otras paredes hayan.
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
		
		return top, bottom, left, right
		
	def check_terrain_2(self, top, bottom, left, right):
		if top and left:
			self.rect.x -=2
			self.rect.y -=2
			hit_list = pygame.sprite.spritecollide(self, self.level, False)
			self.rect.x +=2
			self.rect.y +=2
			if len(hit_list) == 3:
				topleft = False
			else:
				topleft = True
		else:
			topleft = True
			
		if top and right:
			self.rect.x +=2
			self.rect.y -=2
			hit_list = pygame.sprite.spritecollide(self, self.level, False)
			self.rect.x -=2
			self.rect.y +=2
			if len(hit_list) == 3:
				topright = False
			else:
				topright = True
		else:
			topright = True
			
		if bottom and left:
			self.rect.x -=2
			self.rect.y +=2
			hit_list = pygame.sprite.spritecollide(self, self.level, False)
			self.rect.x +=2
			self.rect.y -=2
			if len(hit_list) == 3:
				bottomleft = False
			else:
				bottomleft = True
		else:
			bottomleft = True
			
		if bottom and right:
			self.rect.x +=2
			self.rect.y +=2
			hit_list = pygame.sprite.spritecollide(self, self.level, False)
			self.rect.x -=2
			self.rect.y -=2
			if len(hit_list) == 3:
				bottomright = False
			else:
				bottomright = True
		else:
			bottomright = True
			
		return topleft, topright, bottomleft, bottomright
	
	def change_terrain(self, pared):
		archivo = open('images/tiles/typesofsheets.txt', 'r')
		tipo = 1
		for linea in archivo:
			if pared in linea.strip().split(':'):
				break
			tipo += 1
		archivo.close()
		
		sheet = pygame.image.load('images/tiles/' + pared).convert()
		top, bottom, left, right = self.check_terrain_1()
		
		if tipo == 1:
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
		
		elif tipo == 2:
			topleft, topright, bottomleft, bottomright = self.check_terrain_2(top, bottom, left, right)
			cuadro = pygame.image.load('images/tiles/box.png').convert()
			
			if top:
				if left:
					if topleft:
						parte1 = get_image(sheet, 64,16, 16,16).convert()
					else:
						parte1 = get_image(sheet, 32,16, 16,16).convert()
				else:
					parte1 = get_image(sheet, 16,16, 16,16).convert()
				
				if right:
					if topright:
						parte2 = get_image(sheet, 64,32, 16,16).convert()
					else:
						parte2 = get_image(sheet, 32,32, 16,16).convert()
				else:
					parte2 = get_image(sheet, 16,32, 16,16).convert()
			
			else:
				if left:
					parte1 = get_image(sheet, 0,16, 16,16).convert()
				else:
					parte1 = get_image(sheet, 48,16, 16,16).convert()
				
				if right:
					parte2 = get_image(sheet, 0,32, 16,16).convert()
				else:
					parte2 = get_image(sheet, 48,32, 16,16).convert()
					
			if bottom:
				if left:
					if bottomleft:
						parte4 = get_image(sheet, 64,64, 16,16).convert()
					else:
						parte4 = get_image(sheet, 32,64, 16,16).convert()
				else:
					parte4 = get_image(sheet, 16,64, 16,16).convert()
				
				if right:
					if bottomright:
						parte3 = get_image(sheet, 64,48, 16,16).convert()
					else:
						parte3 = get_image(sheet, 32,48, 16,16).convert()
				else:
					parte3 = get_image(sheet, 16,48, 16,16).convert()
			
			else:
				if left:
					parte4 = get_image(sheet, 0,64, 16,16).convert()
				else:
					parte4 = get_image(sheet, 48,64, 16,16).convert()
				
				if right:
					parte3 = get_image(sheet, 0,48, 16,16).convert()
				else:
					parte3 = get_image(sheet, 48,48, 16,16).convert()
					
			cuadro.blit(parte1, (0,0))
			cuadro.blit(parte2, (16,0))
			cuadro.blit(parte4, (0,16))
			cuadro.blit(parte3, (16,16))
		
		#cuadro.set_colorkey(CHROMA_KEY)
		
		self.image = cuadro
		

