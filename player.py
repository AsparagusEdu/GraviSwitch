import pygame
class Player(pygame.sprite.Sprite):
	spd_x = 0
	spd_y = 0
	level = None
	def __init__(self, x_init, y_init):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.image.load('images/Isaac1.png')
		self.rect = self.image.get_rect()
		self.rect.x = x_init + 8
		self.rect.y = y_init
	
	def calc_grav(self):
		if self.spd_y == 0:
			self.spd_y = 1
		else:
			self.spd_y += .3
			
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
	
	def collision_x(self):
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		for block in hit_list:
			if block.ID != self.ID:
				if self.spd_x > 0:
					self.rect.right = block.rect.left
				elif self.spd_x < 0:
					self.rect.left = block.rect.right
				# Detener movimiento horizontal
				self.spd_x = 0
		
	def update(self):
		self.rect.x += self.spd_x
		self.collision_x()
		
		self.rect.y += self.spd_y
		self.collision_y()
		
		self.calc_grav()
		
	def go_left(self):
		self.spd_x = -3
	def go_right(self):
		self.spd_x = 3
	def stop(self):
		self.spd_x = 0
	def jump(self):
		self.rect.y +=2
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		print hit_list
		self.rect.y -=2
		for i in hit_list:
			if i.ID != self.ID:
				#if len(hit_list) > 0 and:
				
				self.spd_y = -4
		
