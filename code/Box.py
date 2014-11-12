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
		self.state = 'STOP'
	
	def calc_grav(self, grav): 
		if grav == 'N':
			self.rect.y -=1
			hit_list = pygame.sprite.spritecollide(self, self.level, False)
			self.rect.y +=1
			if len(hit_list) <= 1 and self.spd_y == 0:
				self.spd_y = -4
				self.state = 'AIR'
		elif grav == 'S':
			self.rect.y +=1
			hit_list = pygame.sprite.spritecollide(self, self.level, False)
			self.rect.y -=1
			if len(hit_list) <= 1 and self.spd_y == 0:
				self.spd_y = 4
				self.state = 'AIR'
		elif grav == 'E':
			self.rect.x +=1
			hit_list = pygame.sprite.spritecollide(self, self.level, False)
			self.rect.x -=1
			if len(hit_list) <= 1 and self.spd_y == 0:
				self.spd_x = 4
				self.state = 'AIR'
		elif grav == 'O':
			self.rect.x -=1
			hit_list = pygame.sprite.spritecollide(self, self.level, False)
			self.rect.x +=1
			if len(hit_list) <= 1 and self.spd_y == 0:
				self.spd_x = -4
				self.state = 'AIR'
		
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
	
	def update(self, grav):
		self.rect.y += self.spd_y
		self.collision_y()
		self.rect.x += self.spd_x
		self.collision_x()
		self.calc_grav(grav)
		
		
