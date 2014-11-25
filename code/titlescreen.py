import pygame
from constants import SCREEN, MUSIC
def Demo_TitleScreen():
	title = pygame.image.load('images/demo/titlescreen.png').convert()
	'''
	if MUSIC:
		music = pygame.mixer.music.load('sound/music/cheetah.mp3')
		pygame.mixer.music.play(-1)
	'''
	clock = pygame.time.Clock()
	over = False
	while not over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					return True
				elif event.key == pygame.K_RETURN:
					return False
				
		SCREEN.blit(title, (0,0))
		pygame.display.flip()
		clock.tick(10)

def Main_TitleScreen():
	title = pygame.image.load('images/demo/titlescreen.png').convert()
	'''
	if MUSIC:
		music = pygame.mixer.music.load('sound/music/cheetah.mp3')
		pygame.mixer.music.play(-1)
	'''
	clock = pygame.time.Clock()
	over = False
	while not over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					return True
				elif event.key == pygame.K_RETURN:
					return False
				
		SCREEN.blit(title, (0,0))
		pygame.display.flip()
		clock.tick(10)
