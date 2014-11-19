import pygame
from constants import SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH, MUSIC
from level import Level
from titlescreen import TitleScreen


class Menu():
	def __init__(self):
		TitleScreen()
		TScreen = pygame.image.load('images/titlescreen.png').convert()
		
		self.menu_image = pygame.image.load('images/stageselect.png').convert()
		self.menu_rect = self.menu_image.get_rect()
		self.menu_pos = (SCREEN_WIDTH/2 - self.menu_rect.w/2 , SCREEN_HEIGHT/2 - self.menu_rect.h/2)
		
		self.cursor_image = pygame.image.load('images/stageselect_cursor.png').convert_alpha()
		self.cursor_rect = self.cursor_image.get_rect()
		
		self.state = 'level1'
		while True:
			if MUSIC:
				music = pygame.mixer.music.load('sound/music/s3kfileselect.mp3')
				pygame.mixer.music.play(-1)
			SCREEN.blit(TScreen, (0,0))
			SCREEN.blit(self.menu_image, self.menu_pos)
			pygame.display.flip()
			
			selected = False
			while not selected:
				change = False
				while not change:
					if self.state == 'level1':
						selected, change = self.level_1()
					elif self.state == 'level2':
						selected, change = self.level_2()
					elif self.state == 'level3':
						selected, change = self.level_3()
					elif self.state == 'level4':
						selected, change = self.level_4()	
					elif self.state == 'level5':
						selected, change = self.level_5()
					elif self.state == 'level6':
						selected, change = self.level_6()	
					if change != True:
						self.state = change
						change = False
			
			Level(self.state)

	def level_1(self):
		clock = pygame.time.Clock()
		
		SCREEN.blit(self.menu_image, self.menu_pos)
		SCREEN.blit(self.cursor_image, (155,103))
		pygame.display.flip()
		
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
					if event.key == pygame.K_RETURN:
						return (True, True)
					elif event.key == pygame.K_DOWN:
						return (False, 'level4')
					elif event.key == pygame.K_RIGHT:
						return (False, 'level2')
			clock.tick(10)
				
	def level_2(self):
		clock = pygame.time.Clock()
		
		SCREEN.blit(self.menu_image, self.menu_pos)
		SCREEN.blit(self.cursor_image, (391,103))
		pygame.display.flip()
		
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
					if event.key == pygame.K_RETURN:
						return (True, True)
					elif event.key == pygame.K_DOWN:
						return (False, 'level5')
					elif event.key == pygame.K_RIGHT:
						return (False, 'level3')
					elif event.key == pygame.K_LEFT:
						return (False, 'level1')
			clock.tick(10)			
	
	def level_3(self):
		clock = pygame.time.Clock()
		
		SCREEN.blit(self.menu_image, self.menu_pos)
		SCREEN.blit(self.cursor_image, (625,103))
		pygame.display.flip()
		
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
					if event.key == pygame.K_RETURN:
						return (True, True)
					elif event.key == pygame.K_DOWN:
						return (False, 'level6')
					elif event.key == pygame.K_LEFT:
						return (False, 'level2')
			clock.tick(10)

	def level_4(self):
		clock = pygame.time.Clock()
		
		SCREEN.blit(self.menu_image, self.menu_pos)
		SCREEN.blit(self.cursor_image, (155,287))
		pygame.display.flip()
		
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
					if event.key == pygame.K_RETURN:
						return (True, True)
					elif event.key == pygame.K_UP:
						return (False, 'level1')
					elif event.key == pygame.K_RIGHT:
						return (False, 'level5')
			clock.tick(10)
				
	def level_5(self):
		clock = pygame.time.Clock()
		
		SCREEN.blit(self.menu_image, self.menu_pos)
		SCREEN.blit(self.cursor_image, (391,287))
		pygame.display.flip()
		
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
					if event.key == pygame.K_RETURN:
						return (True, True)
					elif event.key == pygame.K_UP:
						return (False, 'level2')
					elif event.key == pygame.K_RIGHT:
						return (False, 'level6')
					elif event.key == pygame.K_LEFT:
						return (False, 'level4')
			clock.tick(10)			
	
	def level_6(self):
		clock = pygame.time.Clock()
		
		SCREEN.blit(self.menu_image, self.menu_pos)
		SCREEN.blit(self.cursor_image, (625,287))
		pygame.display.flip()
		
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
					if event.key == pygame.K_RETURN:
						return (True, True)
					elif event.key == pygame.K_UP:
						return (False, 'level3')
					elif event.key == pygame.K_LEFT:
						return (False, 'level5')
			clock.tick(10)

