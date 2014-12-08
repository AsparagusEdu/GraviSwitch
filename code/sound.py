import pygame
pygame.mixer.init(22050, -16, 3, 512)

checkpoint = pygame.mixer.Sound('sound/effects/checkpoint.wav')
dead = pygame.mixer.Sound('sound/effects/dead.wav')
cursor = pygame.mixer.Sound('sound/effects/cursormove.wav')
cursorleft = pygame.mixer.Sound('sound/effects/cursormoveleft.wav')
cursorright = pygame.mixer.Sound('sound/effects/cursormoveright.wav')
graviswitch = pygame.mixer.Sound('sound/effects/graviswitch2.wav')
openmenu = pygame.mixer.Sound('sound/effects/openmenu.wav')
jump = pygame.mixer.Sound('sound/effects/jump.wav')
bounce = pygame.mixer.Sound('sound/effects/bounce.wav')
no = pygame.mixer.Sound('sound/effects/nonono.wav')
lvlsaved = pygame.mixer.Sound('sound/effects/levelsaved.wav')

itemget = pygame.mixer.Sound('sound/jingles/itemget.wav')

checkpoint.set_volume(0.6)
graviswitch.set_volume(0.7)
