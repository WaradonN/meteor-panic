import pygame
from sys import exit

from pygame.constants import KEYDOWN, K_d

# meta and inner works
pygame.init()
screen = pygame.display.set_mode((450, 600)) #450*600 
icon = pygame.image.load('asset/icon.png') # 100*100 or smaller
pygame.display.set_caption('Meteor Panic!')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
gamefont = pygame.font.Font('asset/PressStart2P.ttf', 20)

# stuff to draw
ground_surface = pygame.image.load('asset/ground.png').convert() # 450*100
sky_surface = pygame.image.load('asset/sky.png').convert() # 450*600 
exo_surface = pygame.image.load('asset/fallen_sky.png').convert() # 450*125
character = pygame.image.load('asset/character.png').convert_alpha() # 65*100
char_pos_x = 190

# input and updates
while True:
    ## input
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if key[pygame.K_d]: # Go Right
            if char_pos_x >= 385:
                char_pos_x += 0
            elif char_pos_x < 385:
                char_pos_x += 6
        elif key[pygame.K_a]: # Go Left
            if char_pos_x <= 0:
                char_pos_x -= 0
            if char_pos_x > 0:
                char_pos_x -= 6
    ## draw stuff
    ### enviroment
    screen.blit(sky_surface, (0,0))
    screen.blit(exo_surface, (0,0))
    screen.blit(ground_surface, (0, 500))
    ### stuff that change
    screen.blit(character, (char_pos_x, 400))
    ### game state (wrongly used technical word, wow!)
    # if char_pos_x <= 0:
    #     char_pos_x = 0
    # if char_pos_x >= 385:
    #     char_pos_x = 385
    ## update thing
    pygame.display.update()
    clock.tick(90)
