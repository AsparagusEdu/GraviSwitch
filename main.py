import pygame
import os
import sys
import classPlayer

VERSION_NAME = "GraviSwitch"

BLOCK_SCALE = 50
RESIZE = BLOCK_SCALE/50.0

SCREEN_WIDTH = 18*BLOCK_SCALE
SCREEN_HEIGHT = 12*BLOCK_SCALE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



#OBJETOS

class Wall(pygame.sprite.Sprite):
	def __init__(self, x, y):
		
		#Generar sprite
		pygame.sprite.Sprite.__init__(self)

		self.image = load_image("pared.png", "images")#Va a cargar la pared para
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

		self.image = load_image("caja.png", "images")#Va a cargar la pared para
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
#FUNCIONES
class Build_Room():
	wall_list = None
	box_list = None
	def __init__(self, lvl_name):

		archivo = open("levels/"+lvl_name+".txt") #Lee el nivel a partir del archivo

		self.wall_list = pygame.sprite.Group() #Crea el grupo de paredes
		self.box_list =pygame.sprite.Group() #Crea el grupo de cajas

		c_inicio = None
		i_fondo = "fondo_0.png"
		
		y_coor = 0 #Coordenada Y del cuadro leido actualmente
		box_num = 0
		
		for linea in archivo:
			linea = linea.strip("\n")
			x_coor = 0 #Coordenada X del cuadro leido actualmente
			if y_coor == SCREEN_HEIGHT/BLOCK_SCALE: #Imagen de fondo
				i_fondo = linea
			elif y_coor == SCREEN_HEIGHT/BLOCK_SCALE +1:
				print linea

			for cuadro in linea:
				if cuadro == 'W':#Revisa si el tipo de cuadro leido corresponde a la pared.
					wall = Wall(x_coor*BLOCK_SCALE, y_coor*BLOCK_SCALE) #Como es un juego con niveles en forma de grilla, ajustamos la coordenada leida al juego
					self.wall_list.add(wall) #A?ade al grupo la pared
				if cuadro == 'I': #Busca el cuadro de inicio
					c_inicio = (x_coor*BLOCK_SCALE,y_coor*BLOCK_SCALE)
				if cuadro == 'B':
					box_num +=1
					box = Box(x_coor*BLOCK_SCALE, y_coor*BLOCK_SCALE, box_num) #Como es un juego con niveles en forma de grilla, ajustamos la coordenada leida al juego
					self.box_list.add(box)
				x_coor +=1
			y_coor += 1
		archivo.close()
		
		lista_cajas = self.box_list.sprites()
	
		for box in lista_cajas: #Annade a cada caja sus colisiones
			box.level = self
			box.level.platform_list = self.wall_list
			box.level.platform_list.add(box)
		
		self.inicio = c_inicio
		self.fondo = load_image(i_fondo)
		self.fondo = pygame.transform.scale(self.fondo,(SCREEN_WIDTH,SCREEN_HEIGHT))
	
def Play_Level(lvl_name):
	player = classPlayer.Player() #Crea al jugador
	movingsprites = pygame.sprite.Group()
	movingsprites.add(player)

	room = Build_Room(lvl_name) #Crea el objeto de la habitacion

	active_sprite_list = pygame.sprite.Group()
	
	player.level = room #Toma la informacion del mapa y la introduce a player para que pueda usar la info
	player.level.platform_list = room.wall_list

	active_sprite_list.add(player)
	
	try: #Si no encontro el cuadro inicial, avisara.
		player.rect.y = room.inicio[1] 
		player.rect.x = room.inicio[0]
	except:
		print 'ERROR: No hay un cuadro de inicio en el mapa ' + str(lvl_name)
		sys.exit(1)

	clock = pygame.time.Clock()
	score = 0
	
	gravity = 'S'
	
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sys.exit()
				if event.key == pygame.K_r:
					return False
				if event.key == pygame.K_LEFT:
					player.go_left()
				if event.key == pygame.K_RIGHT:
					player.go_right()
				if event.key == pygame.K_UP:
					player.jump()
				if event.key == pygame.K_w:
					gravity = 'N'
				if event.key == pygame.K_s:
					gravity = 'S'
				if event.key == pygame.K_d:
					gravity = 'E'
				if event.key == pygame.K_a:
					gravity = 'O'
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT and player.change_x < 0:
					player.stop()
				if event.key == pygame.K_RIGHT and player.change_x > 0:
					player.stop()

		player.update()
		
		room.box_list.update(gravity)
		lista_cajas = room.box_list.sprites()
		
		# --- Actualizar pantalla ---
		screen.blit(room.fondo, (0,0))

		movingsprites.draw(screen)
		room.wall_list.draw(screen)
		room.box_list.draw(screen)

		pygame.display.flip()
		
		if player.rect.y >= SCREEN_HEIGHT: #En caso de salirse de la pantalla
			return False
		if player.rect.bottom <= 0:
			return False
		if player.rect.right <= 0:
			return False
		if player.rect.left >= SCREEN_WIDTH:
			return False

		clock.tick(60)

def load_image(nombre, dir_imagen = "images", alpha = False): #Funcion que facilita la importacion de imagenes
	ruta = os.path.join(dir_imagen, nombre)
	try:
		image = pygame.image.load(ruta)
	except:
		print "Error, no se puede cargar la imagen: ", ruta
		sys.exit(1)
	if alpha == True: #El 3er parametro es opcional, y en caso de ser True, activa la transparencia
		image = image.convert_alpha()
	else:
		image = image.convert()
	return image



#MAIN
def main():

	pygame.init()

	pygame.display.set_caption(VERSION_NAME)

	# Esto es solo por motivos de prueba.
	# Se podra llamar a cualquier nivel usando la funcin Play_Level(numero del nivel)
	level = "level0"
	done = False #El nivel aun no ha sido vencido
	while not done:
		done = Play_Level(level)
		



	pygame.quit()

if __name__ == "__main__":
	main()
