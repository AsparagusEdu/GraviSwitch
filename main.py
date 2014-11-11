import pygame, os, sys, constants as C
from classReadLevel import ReadFile
from classWall import Wall
screen = pygame.display.set_mode((C.SCREEN_WIDTH, C.SCREEN_HEIGHT))

def load_level(mapa, fondo):
	wall_list = pygame.sprite.Group()
	pos_y = 0
	for linea in mapa:
		pos_x = 0
		for cuadro in linea:
			if cuadro == 'W':
				wall = Wall(pos_x*32, pos_y*32)
				wall_list.add(wall)
			pos_x += 1
		pos_y += 1
	return wall_list

def main():
	pygame.init()
	pygame.display.set_caption(C.GAME_NAME)
	clock = pygame.time.Clock()
	done = False
	mapa1, fondo1 = ReadFile('level0.txt')
	wall_list = load_level(mapa1, fondo1)
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					done = True
				'''
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
		'''
		wall_list.draw(screen)
		pygame.display.flip()
		'''
		if player.rect.y >= SCREEN_HEIGHT: #En caso de salirse de la pantalla
			return False
		if player.rect.bottom <= 0:
			return False
		if player.rect.right <= 0:
			return False
		if player.rect.left >= SCREEN_WIDTH:
			return False
		'''
		clock.tick(60)

	
	
	
main()
