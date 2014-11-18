import pygame
import Box
import Spike
import constants as C
import Door
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
		self.win = False
		self.init_x = self.rect.x
		self.init_y = self.rect.y
		
	def reboot(self, grav):
		self.dead = False
		self.spd_y = 0
		self.spd_x = 0
		self.rect.x = self.init_x
		self.rect.y = self.init_y
		
	def touch_N(self, colis): #colis == numero de colisiones originales
		self.rect.y -=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.y +=1
		if len(hit_list) == colis:
			return False
		return True
	def touch_S(self, colis):
		self.rect.y +=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.y -=1
		if len(hit_list) == colis:
			return False
		return True
	def touch_E(self, colis):
		self.rect.x +=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.x -=1
		if len(hit_list) == colis:
			return False
		return True	
	def touch_O(self, colis):
		self.rect.x -=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.x +=1
		if len(hit_list) == colis:
			return False
		return True
		
	def crush(self):
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		colis = len(hit_list) #Numero de colisiones originalmente.
		#print colis
		if colis >= 3:
			self.dead = True
			return True
		elif colis == 2:
			if type(hit_list[0]) is Box.Box and type(hit_list[1]) is Box.Box:
				bloxy = hit_list[1]
				if bloxy.spd_x > 0:
					self.rect.left = bloxy.rect.right
				elif bloxy.spd_x < 0:
					self.rect.right = bloxy.rect.left
				elif bloxy.spd_y > 0:
					self.spd_y = 0
					self.rect.bottom = bloxy.rect.top
				elif bloxy.spd_y < 0:
					self.spd_y = 0
					self.rect.top = bloxy.rect.bottom
			else:
				self.dead = True
				return True
		elif colis == 1:
			bloxy = hit_list[0]
			if bloxy.spd_x > 0 and not self.touch_E(colis):
				self.rect.left = bloxy.rect.right
			elif bloxy.spd_x < 0 and not self.touch_O(colis):
				self.rect.right = bloxy.rect.left
			elif bloxy.spd_y > 0 and not self.touch_S(colis):
				self.spd_y = 0
				self.rect.top = bloxy.rect.bottom
			elif bloxy.spd_y < 0 and not self.touch_N(colis):
				self.spd_y = 0
				self.rect.bottom = bloxy.rect.top
			else:
				self.dead = True
				return True
				
		return False
	def touch_death(self):
		self.rect.y -=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.y +=1
		if len(hit_list) > 0:
			for hit in hit_list:
				if type(hit) is Spike.Spike:
					self.dead = True
		self.rect.y +=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.y -=1
		if len(hit_list) > 0:
			for hit in hit_list:
				if type(hit) is Spike.Spike:
					self.dead = True 
		self.rect.x -=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.x +=1
		if len(hit_list) > 0:
			for hit in hit_list:
				if type(hit) is Spike.Spike:
					self.dead = True 
		self.rect.x +=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.x -=1
		if len(hit_list) > 0:
			for hit in hit_list:
				if type(hit) is Spike.Spike:
					self.dead = True 
	def out_screen_death(self):
		if self.rect.top >= C.SCREEN_HEIGHT:
			self.dead = True
		elif self.rect.bottom <= 0:
			self.dead = True
		elif self.rect.left >= C.SCREEN_WIDTH:
			self.dead = True
		elif self.rect.right <= 0:
			self.dead = True
	
	def death(self):
		self.crush()
		self.touch_death()
		self.out_screen_death()
	def door(self): #Detecta cuando el jugador llego a una puerta
		hit_list = pygame.sprite.spritecollide(self, self.doors, False)
		for hit in hit_list:
			if type(hit) is Door.Door:
				if (hit.rect.left + 10 < self.rect.centerx < hit.rect.right - 10) and (hit.rect.bottom == self.rect.bottom):
					self.win = True
	
	def collision_y(self):
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		for block in hit_list:
			if block.ID != self.ID:
				if self.spd_y > 0 or block.spd_y < 0:
					self.rect.bottom = block.rect.top
				elif self.spd_y < 0 or block.spd_y > 0:
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
		self.death()
		self.door()
		self.rect.x += self.spd_x
		self.collision_x()
		
		self.rect.y += self.spd_y
		self.collision_y()
		
		if not self.touch_S(0):
			self.spd_y += .15
		
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
		
