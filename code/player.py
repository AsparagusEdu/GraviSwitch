import pygame
import sound

import Box
import Spike
import constants as C
import Door
import Checkpoint
import GraviSwitch

from misc_functions import check_if_box, get_image

class Player(pygame.sprite.Sprite):
	spd_x = 0
	spd_y = 0
	level = None
	def __init__(self, x_init, y_init, gravi):
		pygame.sprite.Sprite.__init__(self)
		
		self.load_images()
		self.set_states(gravi)
		
		self.image = pygame.image.load('images/Isaac/IsaacCol.png').convert()
		self.rect = self.image.get_rect()
		self.image = self.jump_ani[4]
		self.jump_ani_frame = 25
		
		#self.image = pygame.image.load('images/Isaac2.png').convert()
		self.rect.x = x_init + 8
		self.rect.y = y_init
		
		
		self.init_x = self.rect.x
		self.init_y = self.rect.y	
	
	def set_states(self, gravi):
		self.state = 'Stand'
		self.air = True
		self.direction = 'Right'
		self.dead = False
		self.win = False
		self.bounce = False
		self.crouch = False
		self.firstgravi = False
		if gravi:
			self.graviswitch = True
		else:
			self.graviswitch = False
	def load_images(self):
		sheet = pygame.image.load('images/Isaac/yirorescale.png').convert()
		
		self.stand_image = get_image(sheet, 0, 0, 32, 32)
		self.stand_image.set_colorkey(C.CHROMA_KEY)
		
		self.crouch_image = get_image(sheet, 0, 32, 32, 32)
		self.crouch_image.set_colorkey(C.CHROMA_KEY)
		
		self.dead_image = get_image(sheet, 192, 32, 32, 38)
		self.dead_image.set_colorkey(C.CHROMA_KEY)
		
		self.walk_ani = []
		self.walk_ani_cod = [(32,0),(64,0),(96,0), (128,0), (160,0), (192,0), (224,0), (256,0), (288,0), (320,0), (352,0)]
		self.walk_ani_frame = 0
		for i in self.walk_ani_cod:
			cuadro = get_image(sheet, i[0], i[1], 32,32).convert()
			cuadro.set_colorkey(C.CHROMA_KEY)
			self.walk_ani.append(cuadro)
		
		self.jump_ani = []
		self.jump_ani_cod = [(32,32), (64,32), (96,32), (128,32), (160,32)]
		self.jump_ani_frame = 0
		for i in self.jump_ani_cod:
			cuadro = get_image(sheet, i[0], i[1], 32,38).convert()
			cuadro.set_colorkey(C.CHROMA_KEY)
			self.jump_ani.append(cuadro)
		
	def reboot(self, grav):
		self.dead = False
		self.bounce = False
		self.crouch = False
		self.image = self.stand_image
		self.direction = 'Right'
		self.state = 'Stand'
		self.image = self.jump_ani[4]
		self.jump_ani_frame = 25
		
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
			#if (type(hit_list[0]) is Box.Box or type(hit_list[0]) is Box.JumpBox) and (type(hit_list[1]) is Box.Box and type(hit_list[1]) is Box.JumpBox):
			
			if check_if_box(hit_list[0]) and check_if_box(hit_list[1]):
				bloxy = hit_list[1]
				if bloxy.spd_x > 0:
					self.rect.left = bloxy.rect.right
				elif bloxy.spd_x < 0:
					self.rect.right = bloxy.rect.left
				elif bloxy.spd_y > 0:
					self.spd_y = 0
					self.rect.top = bloxy.rect.bottom
				elif bloxy.spd_y < 0:
					self.spd_y = 0
					self.rect.bottom = bloxy.rect.top
					self.air = False
					self.walk_ani_frame = 0
					self.image = self.stand_image
					if self.direction == 'Left':
						self.image = pygame.transform.flip(self.image, True, False)
			else:
				self.dead = True
				sound.dead.play()
				return True
		elif colis == 1:
			bloxy = hit_list[0]
			if bloxy.spd_x > 0 and not self.touch_E(colis):
				self.rect.left = bloxy.rect.right
			elif bloxy.spd_x < 0 and not self.touch_O(colis):
				self.rect.right = bloxy.rect.left
			
			#elif bloxy.spd_x < 0 and self.spd_x < 0 and self.rect.x < bloxy.rect.x:
				#self.rect.right = bloxy.rect.left
			
			elif bloxy.spd_y > 0 and not self.touch_S(colis):
				self.spd_y = 0
				self.rect.top = bloxy.rect.bottom
			elif bloxy.spd_y < 0 and not self.touch_N(colis):
				self.spd_y = 0
				self.rect.bottom = bloxy.rect.top
				self.air = False
				self.walk_ani_frame = 0
				self.image = self.stand_image
				if self.direction == 'Left':
					self.image = pygame.transform.flip(self.image, True, False)
			elif bloxy.spd_y < 0 and self.spd_y > 0: #BUGFIX para que el jugador pueda caer de una caja en movimiento a otra
				self.spd_y = 0
				self.rect.bottom = bloxy.rect.top
				self.air = False
				self.walk_ani_frame = 0
				self.image = self.stand_image
				if self.direction == 'Left':
					self.image = pygame.transform.flip(self.image, True, False)
			elif bloxy.spd_y > 0 and self.spd_y < 0:
				self.spd_y = 0
				self.rect.top = bloxy.rect.bottom
			elif bloxy.spd_y < 0 and self.spd_y < 0:
				self.spd_y = 0
				if bloxy.rect.y > self.rect.y:
					self.rect.bottom = bloxy.rect.top
				else:
					self.rect.top = bloxy.rect.bottom
			
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
					return True
		self.rect.y +=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.y -=1
		if len(hit_list) > 0:
			for hit in hit_list:
				if type(hit) is Spike.Spike:
					return True
		self.rect.x -=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.x +=1
		if len(hit_list) > 0:
			for hit in hit_list:
				if type(hit) is Spike.Spike:
					return True
		self.rect.x +=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.x -=1
		if len(hit_list) > 0:
			for hit in hit_list:
				if type(hit) is Spike.Spike:
					return True 
	def out_screen_death(self):
		if self.rect.top >= C.SCREEN_HEIGHT:
			return True
		elif self.rect.bottom <= 0:
			return True
		elif self.rect.left >= C.SCREEN_WIDTH:
			return True
		elif self.rect.right <= 0:
			return True
		return False
	def death(self):
		if self.crush() or self.touch_death() or self.out_screen_death():
			self.dead = True
			sound.dead.play()
	
	def jumpbox(self):
		self.rect.y -=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.y +=1
		if len(hit_list) > 0:
			for hit in hit_list:
				if type(hit) is Box.JumpBox:
					self.spd_y = 6
					self.air = True
					self.jump_ani_frame = 24
		self.rect.y +=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.y -=1
		if len(hit_list) > 0:
			for hit in hit_list:
				if type(hit) is Box.JumpBox:
					self.spd_y = -6
					self.air = True
					self.jump_ani_frame = 0
		self.rect.x -=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.x +=1
		if len(hit_list) > 0:
			for hit in hit_list:
				if type(hit) is Box.JumpBox:
					self.bounce = True
					self.spd_x = 4
					self.air = True
					self.jump_ani_frame = 24
		self.rect.x +=1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.x -=1
		if len(hit_list) > 0:
			for hit in hit_list:
				if type(hit) is Box.JumpBox:
					self.bounce = True
					self.spd_x = -4
					self.air = True
					self.jump_ani_frame = 24
	def door(self): #Detecta cuando el jugador llego a una puerta
		hit_list = pygame.sprite.spritecollide(self, self.doors, False)
		for hit in hit_list:
			if type(hit) is Door.Door:
				if (hit.rect.left + 10 < self.rect.centerx < hit.rect.right - 10) and (hit.rect.bottom == self.rect.bottom):
					self.win = True
	def checkpoint(self, times):
		hit_list = pygame.sprite.spritecollide(self, self.checkpoints, False)
		for hit in hit_list:
			if type(hit) is Checkpoint.Checkpoint:
				if hit.rect.left + 1 < self.rect.centerx < hit.rect.right - 1 and not hit.on:
					self.init_x = hit.rect.x + 8
					self.init_y = hit.rect.y
					hit.on = True
	def graviswitch_touch(self):
		hit_list = pygame.sprite.spritecollide(self, self.gravis, False)
		for hit in hit_list:
			if type(hit) is GraviSwitch.GraviSwitch:
				if hit.rect.left + 1 < self.rect.centerx < hit.rect.right - 1:
					self.graviswitch = True
					self.firstgravi = True
					pygame.mixer.music.pause()
					sound.itemget.play()
					hit.state = 'None'
					hit.image = hit.ani1[4]
					pygame.time.wait(5000)
					pygame.event.clear()
					self.spd_x = 0
					self.state = 'Stand'
					self.image = self.stand_image
					pygame.mixer.music.unpause()
					
	def box_ride(self):
		self.rect.y += 1
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.y -= 1
		for hit in hit_list:
			if type(hit) is Box.Box:
				self.rect.x += hit.spd_x
	
	def collision_y(self):
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		for block in hit_list:
			if block.ID != self.ID:
				if self.spd_y > 0 or block.spd_y < 0:
					self.rect.bottom = block.rect.top
					self.air = False
					self.walk_ani_frame = 0
					self.image = self.stand_image
					if self.direction == 'Left':
						self.image = pygame.transform.flip(self.image, True, False)
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
				
	def update(self,grav, times):
		self.death()
		if self.dead:
			return
		self.door()
		self.checkpoint(times)
		self.ani_update()
		if not self.graviswitch:
			self.graviswitch_touch()
		self.jumpbox()
		
		if self.crouch:
			self.box_ride()
		
		if not C.SLOW_MODE:
			self.rect.x += self.spd_x
		else:
			self.rect.x += self.spd_x * times
		self.collision_x()
		
		
		if not C.SLOW_MODE:
			self.rect.y += self.spd_y
		else:
			self.rect.y += self.spd_y * times              
		self.collision_y()
		
		if not self.touch_S(0):
			self.spd_y += .15
		if self.bounce:
			self.image = self.jump_ani[4]
			if self.spd_x > 0.3:
				self.spd_x -= .09
			elif self.spd_x < -0.3:
				self.spd_x += .09
			else:
				self.spd_x = 0
				
				self.bounce = False
				
	def ani_update(self):
		#print self.walk_ani_frame
		if self.state == 'Walk' and not self.air:
			
			if self.walk_ani_frame % 4 == 0:
				self.image = self.walk_ani[self.walk_ani_frame / 4]
				if self.direction == 'Left':
					self.image = pygame.transform.flip(self.image, True, False)
					
				if self.walk_ani_frame == 40:
					self.walk_ani_frame = 1
			
			self.walk_ani_frame += 1
		
		elif self.air:
			#print self.jump_ani_frame
			if self.jump_ani_frame < 30:
				if self.jump_ani_frame % 6 == 0:
					self.image = self.jump_ani[self.jump_ani_frame / 6]
					if self.direction == 'Left':
						self.image = pygame.transform.flip(self.image, True, False)
						
					#if self.jump_ani_frame == 16:
						#self.jump_ani_frame = 1
				
				self.jump_ani_frame += 1
		
	def go_left(self):
		self.state = 'Walk'
		self.spd_x = -2
		if self.direction == 'Right':
			#self.image = pygame.transform.flip(self.image, True, False)
			self.direction = 'Left'
	def go_right(self):
		self.state = 'Walk'
		self.spd_x = 2
		if self.direction == 'Left':
			#self.image = pygame.transform.flip(self.image, True, False)
			self.direction = 'Right'
	def stop(self):
		self.spd_x = 0
		self.state = 'Stand'
		if not self.air:
			self.image = self.stand_image
		if self.direction == 'Left':
			self.image = pygame.transform.flip(self.image, True, False)
		self.walk_ani_frame = 0
		
	def jump(self):
		self.rect.y +=2
		hit_list = pygame.sprite.spritecollide(self, self.level, False)
		self.rect.y -=2
		self.air = True
		self.jump_ani_frame = 0
		for i in hit_list:
			if i.ID != self.ID:
				self.spd_y = -3
