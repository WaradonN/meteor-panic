import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((450, 600))
icon = pygame.image.load('meteor/asset/icon.png')
pygame.display.set_caption('Meteor Panic!')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

ground_surface = pygame.image.load('meteor/asset/ground.png')
sky_surface = pygame.image.load('meteor/asset/sky.png')
exo_surface = pygame.image.load('meteor/asset/fallen_sky.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw stuff
    screen.blit(sky_surface, (0,0))
    screen.blit(exo_surface, (0,0))
    screen.blit(ground_surface, (0, 500))
    # update thing
    pygame.display.update()
    clock.tick(60)
