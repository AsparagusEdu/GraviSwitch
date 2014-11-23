import pygame
import constants as C
class Box(pygame.sprite.Sprite):
	spd_x = 0
	spd_y = 0
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load('images/tiles/box.png').convert()
		self.rect = self.image.get_rect()		
		self.rect.x = x
		self.rect.y = y
		self.state = 'STOP'
		
		self.init_x = x
		self.init_y = y
	
	def reboot(self,grav):
		
		self.rect.x = self.init_x
		self.rect.y = self.init_y
		self.spd_y = 0
		self.spd_x = 0
		self.state = 'STOP'
		
	def calc_grav(self, grav): 
		if grav == 'N':
			if not self.touch_N() and self.spd_y == 0:
				self.spd_y = -4
				self.state = 'AIR'
		elif grav == 'S':
			if not self.touch_S() and self.spd_y == 0:
				self.spd_y = 4
				self.state = 'AIR'
		elif grav == 'E':
			if not self.touch_E() and self.spd_y == 0:
				self.spd_x = 4
				self.state = 'AIR'
		elif grav == 'O':
			if not self.touch_O() and self.spd_y == 0:
				self.spd_x = -4
				self.state = 'AIR'
		
	def touch_N(self):
		self.rect.y -=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.y +=1
		if len(hit_list) <= 1:
			return False
		return True
	def touch_S(self):
		self.rect.y +=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.y -=1
		if len(hit_list) <= 1:
			return False
		return True
	def touch_E(self):
		self.rect.x +=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.x -=1
		if len(hit_list) <= 1:
			return False
		return True	
	def touch_O(self):
		self.rect.x -=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.x +=1
		if len(hit_list) <= 1:
			return False
		return True
	
	def collision_y(self):
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		for block in hit_list:
			if block.ID != self.ID:
				if self.spd_y > 0:
					self.rect.bottom = block.rect.top
				elif self.spd_y < 0:
					self.rect.top = block.rect.bottom
					
				# Detener movimiento vertical
				self.spd_y = 0
				self.state = 'STOP'
	def collision_x(self):
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		for block in hit_list:
			if block.ID != self.ID:
				if self.spd_x > 0:
					self.rect.right = block.rect.left
				elif self.spd_x < 0:
					self.rect.left = block.rect.right
					
				# Detener movimiento vertical
				self.spd_x = 0
				self.state = 'STOP'	
	
	def update(self, grav, times):
		
		if self.state == 'STOP':
			self.calc_grav(grav)
		else:
			if not C.SLOW_MODE:
				self.rect.y += self.spd_y
			else:
				self.rect.y += self.spd_y * times                
			self.collision_y()
			
			if not C.SLOW_MODE:
				self.rect.x += self.spd_x
			else:
				self.rect.x += self.spd_x * times
			self.collision_x()
		
		
