import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((450, 600)) #450*600 
icon = pygame.image.load('asset/icon.png') # 100*100 or smaller
pygame.display.set_caption('Meteor Panic!')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
gamefont = pygame.font.Font('asset/PressStart2P.ttf', 20)

### stuff to draw
ground_surface = pygame.image.load('asset/ground.png').convert() # 450*100
sky_surface = pygame.image.load('asset/sky.png').convert() # 450*600 
exo_surface = pygame.image.load('asset/fallen_sky.png').convert() # 450*125
character = pygame.image.load('asset/character.png').convert_alpha() # 65*100
char_pos_x = 190

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw stuff
    screen.blit(sky_surface, (0,0))
    screen.blit(exo_surface, (0,0))
    screen.blit(ground_surface, (0, 500))
    screen.blit(character, (char_pos_x, 400))
    char_pos_x += 3
    if char_pos_x > 500:
        char_pos_x = - 65
    # update thing
    pygame.display.update()
    clock.tick(60)
