import pygame
from constants import SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH, MAX_FPS, SHOW_FPS
from level import *
from titlescreen import Demo_TitleScreen, Main_TitleScreen
from LevelSelect import Level_Select
from Adventure import Adventure
from savegame import save_read, save_menu
import sound
#import music

class Demo_Menu():
	def __init__(self):
		TScreen = pygame.image.load('images/demo/titlescreen.png').convert()
		
		self.menu_image = pygame.image.load('images/demo/stageselect.png').convert()
		self.menu_rect = self.menu_image.get_rect()
		self.menu_pos = (SCREEN_WIDTH/2 - self.menu_rect.w/2 , SCREEN_HEIGHT/2 - self.menu_rect.h/2)
		
		self.cursor_image = pygame.image.load('images/demo/stageselect_cursor.png').convert_alpha()
		self.cursor_rect = self.cursor_image.get_rect()
		
		self.state = 'level1'
		
		EXIT_GAME = Demo_TitleScreen()
		while not EXIT_GAME:
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
						selected, change, EXIT_GAME = self.level_1()
					elif self.state == 'level2':
						selected, change, EXIT_GAME = self.level_2()
					elif self.state == 'level3':
						selected, change, EXIT_GAME = self.level_3()
					elif self.state == 'level4':
						selected, change, EXIT_GAME = self.level_4()
					elif self.state == 'level5':
						selected, change, EXIT_GAME = self.level_5()
					elif self.state == 'level6':
						selected, change, EXIT_GAME = self.level_6()
						
					if change != True:
						self.state = change
						change = False
			
			if MUSIC:
				pygame.mixer.music.fadeout(1000)
			if not EXIT_GAME:
				Finished, EXIT_GAME = Level(self.state) #Demo_Level(self.state)
				pygame.mixer.music.fadeout(250)

	def level_1(self):
		clock = pygame.time.Clock()
		
		SCREEN.blit(self.menu_image, self.menu_pos)
		SCREEN.blit(self.cursor_image, (155,103))
		pygame.display.flip()
		
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return (True, True, True)
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						return (True, True, True)
					elif event.key == pygame.K_RETURN:
						return (True, True, False)
					elif event.key == pygame.K_DOWN:
						sound.cursor.play()
						return (False, 'level4', False)
					elif event.key == pygame.K_RIGHT:
						sound.cursor.play()
						return (False, 'level2', False)
			clock.tick(10)		
	def level_2(self):
		clock = pygame.time.Clock()
		
		SCREEN.blit(self.menu_image, self.menu_pos)
		SCREEN.blit(self.cursor_image, (391,103))
		pygame.display.flip()
		
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return (True, True, True)
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						return (True, True, True)
					elif event.key == pygame.K_RETURN:
						return (True, True, False)
					elif event.key == pygame.K_DOWN:
						sound.cursor.play()
						return (False, 'level5', False)
					elif event.key == pygame.K_RIGHT:
						sound.cursor.play()
						return (False, 'level3', False)
					elif event.key == pygame.K_LEFT:
						sound.cursor.play()
						return (False, 'level1', False)
			clock.tick(10)			
	def level_3(self):
		clock = pygame.time.Clock()
		
		SCREEN.blit(self.menu_image, self.menu_pos)
		SCREEN.blit(self.cursor_image, (625,103))
		pygame.display.flip()
		
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return (True, True, True)
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						return (True, True, True)
					elif event.key == pygame.K_RETURN:
						return (True, True, False)
					elif event.key == pygame.K_DOWN:
						sound.cursor.play()	
						return (False, 'level6', False)
					elif event.key == pygame.K_LEFT:
						sound.cursor.play()
						return (False, 'level2', False)
			clock.tick(10)
	def level_4(self):
		clock = pygame.time.Clock()
		
		SCREEN.blit(self.menu_image, self.menu_pos)
		SCREEN.blit(self.cursor_image, (155,287))
		pygame.display.flip()
		
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return (True, True, True)
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						return (True, True, True)
					elif event.key == pygame.K_RETURN:
						return (True, True, False)
					elif event.key == pygame.K_UP:
						sound.cursor.play()
						return (False, 'level1', False)
					elif event.key == pygame.K_RIGHT:
						sound.cursor.play()
						return (False, 'level5', False)
			clock.tick(10)			
	def level_5(self):
		clock = pygame.time.Clock()
		
		SCREEN.blit(self.menu_image, self.menu_pos)
		SCREEN.blit(self.cursor_image, (391,287))
		pygame.display.flip()
		
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return (True, True, True)
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						return (True, True, True)
					elif event.key == pygame.K_RETURN:
						return (True, True, False)
					elif event.key == pygame.K_UP:
						sound.cursor.play()
						return (False, 'level2', False)
					elif event.key == pygame.K_RIGHT:
						sound.cursor.play()
						return (False, 'level6', False)
					elif event.key == pygame.K_LEFT:
						sound.cursor.play()
						return (False, 'level4', False)
			clock.tick(10)			
	def level_6(self):
		clock = pygame.time.Clock()
		
		SCREEN.blit(self.menu_image, self.menu_pos)
		SCREEN.blit(self.cursor_image, (625,287))
		pygame.display.flip()
		
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return (True, True, True)
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						return (True, True, True)
					elif event.key == pygame.K_RETURN:
						return (True, True, False)
					elif event.key == pygame.K_UP:
						sound.cursor.play()
						return (False, 'level3', False)
					elif event.key == pygame.K_LEFT:
						sound.cursor.play()
						return (False, 'level5', False)
			clock.tick(10)

class Main_Menu():
	def __init__(self):
		MMenu = pygame.image.load('images/gui/main_menu.png').convert()
		clock = pygame.time.Clock()
		EXIT_GAME = False
		EXIT_MENU = False
		
		MUTE_MUSIC = False
		while not EXIT_GAME:
			EXIT_GAME, EXIT_MENU = Main_TitleScreen(MUTE_MUSIC)
			if not EXIT_MENU:
				EXIT_MENU = save_menu(MUTE_MUSIC)
			
						
