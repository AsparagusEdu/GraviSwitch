import pygame
class Player(pygame.sprite.Sprite):
	spd_x = 0
	spd_y = 0
	level = None
	def __init__(self, x_init, y_init):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.image.load('images/Isaac1.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = x_init + 8
		self.rect.y = y_init
		
		self.dead = False
		self.init_x = self.rect.x
		self.init_y = self.rect.y
		
	def reboot(self, grav):
		self.dead = False
		self.spd_y = 0
		self.spd_x = 0
		self.rect.x = self.init_x
		self.rect.y = self.init_y
		
	
	def touch_N(self):
		self.rect.y -=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.y +=1
		if len(hit_list) == 0:
			return False
		return True
	def touch_S(self):
		self.rect.y +=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.y -=1
		if len(hit_list) == 0:
			return False
		return True
	def touch_E(self):
		self.rect.x +=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.x -=1
		if len(hit_list) == 0:
			return False
		return True	
	def touch_O(self):
		self.rect.x -=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.x +=1
		if len(hit_list) == 0:
			return False
		return True
	
	def crush(self):
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		if len(hit_list) == 1:
			bloxy = hit_list[0]
			if bloxy.spd_x > 0:
				self.rect.left = bloxy.rect.right
			elif bloxy.spd_x < 0:
				self.rect.right = bloxy.rect.left
			elif bloxy.spd_y > 0:
				self.rect.top = bloxy.rect.bottom
			elif bloxy.spd_y < 0:
				self.rect.bottom = bloxy.rect.top
				
		elif len(hit_list) >= 2:
			self.dead = True
	
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
				
	def update(self,grav):
		self.crush()
		self.rect.x += self.spd_x
		self.collision_x()
		
		self.rect.y += self.spd_y
		self.collision_y()
		
		if not self.touch_S():
			self.spd_y += .15
			#self.calc_grav(grav)
		
		
	def go_left(self):
		self.spd_x = -2
	def go_right(self):
		self.spd_x = 2
	def stop(self):
		self.spd_x = 0
	def jump(self):
		self.rect.y +=2
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.y -=2
		for i in hit_list:
			if i.ID != self.ID:
				#if len(hit_list) > 0 and:
				
				self.spd_y = -3
		
