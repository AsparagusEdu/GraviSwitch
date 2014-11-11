import pygame
import GraviSwitch

class Wall(pygame.sprite.Sprite):
	def __init__(self, x, y):
		
		#Generar sprite
		pygame.sprite.Sprite.__init__(self)

		self.image = GraviSwitch.load_image("pared.png", "images")#Va a cargar la pared para
		self.rect = self.image.get_rect()
		self.image = pygame.transform.scale(self.image,(int(self.rect.w*RESIZE),int(self.rect.h*RESIZE)))
		self.rect = self.image.get_rect()
		
		self.rect.y = y
		self.rect.x = x
		
class Box(pygame.sprite.Sprite):
	# Factor velocidad
	change_x = 0
	change_y = 0

	level = None
	
	def __init__(self, x, y, box_number):
		#Generar sprite
		pygame.sprite.Sprite.__init__(self)
		
		self.boxnum = box_number

		self.image = GraviSwitch.load_image("caja.png", "images")#Va a cargar la pared para
		self.rect = self.image.get_rect()
		self.image = pygame.transform.scale(self.image,(int(self.rect.w*RESIZE),int(self.rect.h*RESIZE)))
		self.rect = self.image.get_rect()
		
		self.rect.y = y
		self.rect.x = x
		
	def update(self, grav = 'S'):
		""" Mover al jugador. """
		# Gravedad
		self.calc_grav(grav)

		# Moverse izquierda-derecha
		self.rect.x += self.change_x

		# block_hit_list es la lista de objetos que esta golpeando el avatar en ese momento
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
			try: #Hago un try porque solamente las cajas van a tener el metodo boxnum
				if self.boxnum != block.boxnum:
					if self.change_x > 0:
						self.rect.right = block.rect.left
					elif self.change_x < 0:
						self.rect.left = block.rect.right

					# Detener movimiento vertical
					self.change_x = 0
			except: 
				if self.change_x > 0:
					self.rect.right = block.rect.left
				elif self.change_x < 0:
					self.rect.left = block.rect.right

				# Detener movimiento vertical
				self.change_x = 0
			

		# Moverse arriba-abajo
		self.rect.y += self.change_y
		
		# Lo mismo, pero con arriba-abajo
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False) #Nota: Con True erosiona el piso xD
		for block in block_hit_list:
			try: #Hago un try porque solamente las cajas van a tener el metodo boxnum
				if self.boxnum != block.boxnum:
					if self.change_y > 0:
						self.rect.bottom = block.rect.top
					elif self.change_y < 0:
						self.rect.top = block.rect.bottom

					# Detener movimiento vertical
					self.change_y = 0
			except: 
				if self.change_y > 0:
					self.rect.bottom = block.rect.top
				elif self.change_y < 0:
					self.rect.top = block.rect.bottom

				# Detener movimiento vertical
				self.change_y = 0


	def calc_grav(self, grav = 'S'):
		""" Calcular el efecto de la gravedad. """
		if grav == 'S':
			if self.change_y == 0:
				self.change_y = 1*BLOCK_SCALE/50.0
			else:
				self.change_y += .35*BLOCK_SCALE/50.0
		elif grav == 'N':
			if self.change_y == 0:
				self.change_y = -1*BLOCK_SCALE/50.0
			else:
				self.change_y -= .35*BLOCK_SCALE/50.0
		elif grav == 'E':
			if self.change_x == 0:
				self.change_x = 1*BLOCK_SCALE/50.0
			else:
				self.change_x += .35*BLOCK_SCALE/50.0
		elif grav == 'O':
			if self.change_x == 0:
				self.change_x = -1*BLOCK_SCALE/50.0
			else:
				self.change_x -= .35*BLOCK_SCALE/50.0

