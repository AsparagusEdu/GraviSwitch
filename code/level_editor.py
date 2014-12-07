import pygame
from constants import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT
from level import Level
from load_level import Read_File


def Save_Level(map_data, archivo):
	for linea in map_data['mapa']:
		archivo.write(linea)
		archivo.write('\n')

def Test_Level(map_data, archivo, MUTE_MUSIC):
	Save_Level(map_data, archivo)
	archivo.close()
	#print map_data['mapa'][1]
	Level('temp', MUTE_MUSIC, 's3kfileselect', 'custom/')

def Edit_Level(lvl_num, MUTE_MUSIC):
	lvl_name = 'custom' + str(lvl_num)
	base = open('levels/custom/base_lvl.txt', 'r')
	templvl = open('levels/custom/temp.txt', 'w')
	EXIT_MENU = False
	
	data = {}
	data['mapa'], data['fondo'], data['musica'], data['pared'], data['graviswitch'], data['g_spin'], data['g_spin_spd'] = Read_File('custom/base_lvl.txt')
	base.close()
	
	pygame.display.set_mode((SCREEN_WIDTH +96, SCREEN_HEIGHT +96))
	fondo = pygame.image.load('images/backgrounds/fondo_test0.png').convert()
	SCREEN.blit(fondo,(0,0))
	pygame.display.flip()
	while not EXIT_MENU:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_t:
					Test_Level(data, templvl, MUTE_MUSIC)
					templvl = open('levels/custom/temp.txt', 'w')
					SCREEN.blit(fondo,(0,0))
					pygame.display.flip()
					music = pygame.mixer.music.load('sound/music/JumpingBat.wav')
					prev_song = 's3kfileselect'
					pygame.mixer.music.set_volume(1.0)
					pygame.mixer.music.play(-1)
					if MUTE_MUSIC:
						pygame.mixer.music.pause()
				elif event.key == pygame.K_ESCAPE:
					EXIT_MENU = True
	
	
	pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	

