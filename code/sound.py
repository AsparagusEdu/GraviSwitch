import pygame
pygame.mixer.init(22050, -16, 3, 512)

checkpoint = pygame.mixer.Sound('sound/effects/checkpoint.wav')
dead = pygame.mixer.Sound('sound/effects/dead.wav')
cursor = pygame.mixer.Sound('sound/effects/cursormove.wav')
graviswitch = pygame.mixer.Sound('sound/effects/graviswitch2.wav')
openmenu = pygame.mixer.Sound('sound/effects/openmenu.wav')
jump = pygame.mixer.Sound('sound/effects/jump.wav')

checkpoint.set_volume(0.7)
graviswitch.set_volume(0.7)
