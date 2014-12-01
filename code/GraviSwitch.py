import pygame
import sound
from misc_functions import get_image, static_boxes
from constants import CHROMA_KEY

class GraviSwitch(pygame.sprite.Sprite):
	spd_x = 0
	spd_y = 0
	def __init__(self, x, y, graviswitch):
		pygame.sprite.Sprite.__init__(self)
		
		self.ani1 = []
		self.frame = 0 #60 frames total (1 sec of animation)
		ani1_cod = [(0,0),(32,0),(64,0),(96,0), (124,0)]
		ani1_sheet = pygame.image.load('images/tiles/graviswitch.png').convert()
		
		for i in ani1_cod:
			cuadro = get_image(ani1_sheet, i[0], i[1], 32,32).convert()
			cuadro.set_colorkey(CHROMA_KEY)
			self.ani1.append(cuadro)
		
		self.image = self.ani1[0]
		if graviswitch:
			self.state = 'Manual'
		else:
			self.state = 'Auto'
		
		self.rect = self.image.get_rect()		
		self.rect.y = y
		self.rect.x = x
		
	def reboot(self, grav):
		self.image = self.ani1[0]
		self.frame = 0

	def update(self, grav):
		self.frame += 1
		if self.state == 'Manual':
			if grav == 'S':
				self.image = self.ani1[0]
			elif grav == 'N':
				self.image = self.ani1[1]
			elif grav == 'O':
				self.image = self.ani1[2]
			elif grav == 'E':
				self.image = self.ani1[3]
			return grav
		elif self.state == 'Auto': #Un ciclo cada 240 segundos
			if self.frame % 240 == 0: 
				self.image = self.ani1[0]
				return 'S'
			elif self.frame % 240 == 60:
				self.image = self.ani1[2]
				return 'O'
			elif self.frame % 240  == 120:
				self.image = self.ani1[1]
				return 'N'
			elif self.frame % 240  == 180:
				self.image = self.ani1[3]
				return 'E'
			else:
				return grav
		elif self.state == 'None':
			return grav
		
			
