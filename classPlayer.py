import pygame
from GraviSwitch import *
import classObjects

class Player(pygame.sprite.Sprite):
	""" Jugador """

	# Factor velocidad
	change_x = 0
	change_y = 0

	level = None

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = load_image("player.png", "images", True)
		self.rect = self.image.get_rect()
		self.image = pygame.transform.scale(self.image,(int(self.rect.w*RESIZE),int(self.rect.h*RESIZE)))
		self.rect = self.image.get_rect()		

	def update(self):
		""" Mover al jugador. """
		# Gravedad
		self.calc_grav()

		# Moverse izquierda-derecha
		self.rect.x += self.change_x

		# block_hit_list es la lista de objetos que esta golpeando el avatar en ese momento
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
			# Si nos estamos moviendo a la derecha
			# actualizamos el lado derecho del avatar como el como el lado izquierdo del objeto
			if self.change_x > 0:
				self.rect.right = block.rect.left
			elif self.change_x < 0:
				# Si es a la izquierda, hacer lo contrario.
				self.rect.left = block.rect.right

		# Moverse arriba-abajo
		self.rect.y += self.change_y

		# Lo mismo, pero con arriba-abajo
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:

			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			elif self.change_y < 0:
				self.rect.top = block.rect.bottom

			# Detener movimiento vertical
			self.change_y = 0

	def calc_grav(self):
		""" Calcular el efecto de la gravedad. """
		if self.change_y == 0:
			self.change_y = RESIZE
		else:
			self.change_y += .35*RESIZE
			
		'''
		# Revisa si estamos en el piso.
		if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
			self.change_y = 0
			self.rect.y = SCREEN_HEIGHT - self.rect.height
		'''

	def jump(self):
		""" Salto """

		# Se mueve un poco para comprobar si esta en suelo solido.
		# Movemos 2 pixeles ya que de asi funcionara el salto cuando
		# la plataforma en la que esta se mueve hacia abajo
		self.rect.y += 2
		platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		
		self.rect.y -= 2

		# Si puede saltar, ajustar la velocidad hacia arriba
		if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
			self.change_y = -6*BLOCK_SCALE/50.0

	# Movimientos del jugador:
	def go_left(self):
		""" Cuando presiona hacia la izquierda """
		self.change_x = -3*RESIZE

	def go_right(self):
		""" Cuando presiona hacia la derecha """
		self.change_x = 3*RESIZE

	def stop(self):
		""" Llamado cuando el jugador suelta el teclado. """
		self.change_x = 0
