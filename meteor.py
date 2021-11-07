import pygame
import random
from sys import exit

# meta and inner works
pygame.init()
screen = pygame.display.set_mode((450, 600)) #450*600 
icon = pygame.image.load('asset/icon.png').convert() # 100*100 or smaller
pygame.display.set_caption('Meteor Panic!')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
gamefont = pygame.font.Font('asset/PressStart2P.ttf', 13)

# initial state
alive = True

# stuff to draw
ground_surface = pygame.image.load('asset/ground.png').convert() # 450*100
sky_surface = pygame.image.load('asset/sky.png').convert() # 450*600 
exo_surface = pygame.image.load('asset/fallen_sky.png').convert() # 450*125
character = pygame.image.load('asset/character_hitbox.png').convert_alpha() # 65*100
character_expired = pygame.image.load('asset/character_expired.png')
meteor = pygame.image.load('asset/meteor.png').convert()

# rect(temporary dont know about sprite class yet)
character_rect = character.get_rect(topleft = (200, 400))
meteor_rect = meteor.get_rect(center = (400, 475))

# input and updates
while True:
    ## input
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if alive != True:
        if key[pygame.K_ESCAPE]:
            character_rect.x = 200
            alive = True
    if alive:
        if key[pygame.K_d]: # Go Right
            if character_rect.x >= 385:
                character_rect.x += 0
            elif character_rect.x < 385:
                character_rect.x += 4
        if key[pygame.K_a]: # Go Left
            if character_rect.x <= 0:
                character_rect.x -= 0
            if character_rect.x > 0:
                character_rect.x -= 4
    ## draw stuff
    ### enviroment
    screen.blit(sky_surface, (0,0))
    screen.blit(exo_surface, (0,0))
    screen.blit(ground_surface, (0, 500))
    screen.blit(gamefont.render('minus zeta build', False, 'black'), (10, 10))
    ### stuff that change
    screen.blit(meteor, meteor_rect)
    if alive:
        screen.blit(character, character_rect)
    else:
        screen.blit(character_expired, character_rect)
    ### game state (wrongly used technical word, wow!)
    if character_rect.colliderect(meteor_rect):
        screen.blit(gamefont.render("You touched the cube lmao", False, '#1f1e33'), (65, 150))
        screen.blit(gamefont.render("Press 'Esc' to restart", False, '#1f1e33'), (85, 165))
        alive = False
    ## update thing
    pygame.display.update()
    clock.tick(60)
