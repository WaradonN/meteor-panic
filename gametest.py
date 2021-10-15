import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((450, 600))
icon = pygame.image.load('asset/icon.png') # 100*100 or smaller
pygame.display.set_caption('Meteor Panic!')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

ground_surface = pygame.image.load('asset/ground.png') # 450*100
sky_surface = pygame.image.load('asset/sky.png') # 450*600 
exo_surface = pygame.image.load('asset/fallen_sky.png') # 450*125
character = pygame.image.load('asset/character.png') # 65*100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw stuff
    screen.blit(sky_surface, (0,0))
    screen.blit(exo_surface, (0,0))
    screen.blit(ground_surface, (0, 500))
    screen.blit(character, (190, 400))
    # update thing
    pygame.display.update()
    clock.tick(60)
