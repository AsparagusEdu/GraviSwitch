import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
class World_Shift(): #Los objetos del mundo no solo importaran la clase
	#Sprite, sino World_Shift.
	init_x = None
	init_y = None
	def world_shift(self, shift, world_pos, lvl_dims):
		#print shift
		if world_pos[0] > 0: #Verifica si el punto x del mundo esta dentro de pantalla (fuera de su lugar)
			world_pos[0] = 0
			shift[0] = 0
			self.rect.x = self.init_x	
		#elif world_pos[0] <
		
		else: #Al estar fuera de pantalla, puede moverse libremente el mundo.
			world_pos[0] += shift[0]
			self.rect.x += shift[0]
		
		
		self.rect.y += shift[1]
		#print world_pos
		return world_pos, shift[0]
