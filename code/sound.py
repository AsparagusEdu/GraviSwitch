import pygame
pygame.mixer.init(22050, -16, 3, 512)

checkpoint = pygame.mixer.Sound('sound/effects/checkpoint.wav')
dead = pygame.mixer.Sound('sound/effects/dead.wav')
cursor = pygame.mixer.Sound('sound/effects/cursormove.wav')
