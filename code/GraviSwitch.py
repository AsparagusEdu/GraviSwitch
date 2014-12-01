import pygame
import sound
from misc_functions import get_image, static_boxes
from constants import CHROMA_KEY

class GraviSwitch(pygame.sprite.Sprite):
	spd_x = 0
	spd_y = 0
	def __init__(self, x, y, graviswitch, spin = 1):
		pygame.sprite.Sprite.__init__(self)
		
		self.ani1 = []
		self.frame = 0 #60 frames total (1 sec of animation)
		ani1_cod = [(0,0),(32,0),(64,0),(96,0), (124,0)]
		ani1_sheet = pygame.image.load('images/tiles/graviswitch.png').convert()
		
		for i in ani1_cod:
			cuadro = get_image(ani1_sheet, i[0], i[1], 32,32).convert()
			cuadro.set_colorkey(CHROMA_KEY)
			self.ani1.append(cuadro)
		
		self.spin_spd = 60 #Cuanto demora en cambiar al sgte estado
		if spin == 0:
			self.spin_dir = ['S']
			self.spin_frame = [0]
			self.image = self.ani1[0]
		elif spin == 1:
			self.spin_dir = ['S','O','N','E']
			self.spin_frame = [0,1,2,3]
			self.image = self.ani1[0]
		elif spin == 2:
			self.spin_dir = ['S','E','N','O']
			self.spin_frame = [0,3,2,1]
			self.image = self.ani1[0]
		elif spin == 3:
			self.spin_dir = ['S','N']
			self.spin_frame = [0,2]
			self.image = self.ani1[0]
		elif spin == 4:
			self.spin_dir = ['E','O']
			self.spin_frame = [3,1]
			self.image = self.ani1[3]
		
		
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
			elif grav == 'O':
				self.image = self.ani1[1]
			elif grav == 'N':
				self.image = self.ani1[2]
			elif grav == 'E':
				self.image = self.ani1[3]
			return grav
		elif self.state == 'Auto': #Un ciclo cada 240 segundos
			for i in range(len(self.spin_dir)):
				if self.frame % (self.spin_spd * len(self.spin_dir)) == i*self.spin_spd:
					self.image = self.ani1[self.spin_frame[i]]
					print 'Gravedad - ' + self.spin_dir[i]
					return self.spin_dir[i]
			'''
			if self.spin == 0:
				return grav
			elif self.spin == 1:
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
			elif self.spin == 2:
				if self.frame % 240 == 0: 
					self.image = self.ani1[0]
					return 'S'
				elif self.frame % 240 == 60:
					self.image = self.ani1[3]
					return 'E'
				elif self.frame % 240  == 120:
					self.image = self.ani1[1]
					return 'N'
				elif self.frame % 240  == 180:
					self.image = self.ani1[2]
					return 'O'
				else:
					return grav
			'''
		elif self.state == 'None':
			return grav
		
			
