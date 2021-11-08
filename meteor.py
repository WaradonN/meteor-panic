import pygame
import random
from sys import exit

###### functions and good stuffs ######
def mili2format(time): #00:00:000
    mili = time
    sec = mili // 1000
    mili_left = mili % 1000
    minu = sec // 60
    sec_left = sec % 60
    return "%02d:%02d:%03d" %(minu,sec_left,mili_left)

def display_score():
    """displaying times simple"""
    survive_time = pygame.time.get_ticks() - start_time
    time_surf = gamefont.render(mili2format(survive_time), False, 'black')
    time_rect = time_surf.get_rect(topright = (425,60))
    time_rect_rtt = pygame.transform.rotozoom(time_surf,10,1)
    screen.blit(time_rect_rtt, time_rect)
    return survive_time

# meta and inner works
pygame.init()
screen = pygame.display.set_mode((450, 600)) #450*600 
icon = pygame.image.load('asset/icon.png').convert() # 100*100 or smaller
pygame.display.set_caption('Meteor Panic!')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
gamefont = pygame.font.Font('asset/PressStart2P.ttf', 13)

# initial state
main_menu = True
alive = False
start_time = 0
final_time = mili2format(0)

# stuff to draw
main_menu_surf = pygame.image.load('asset/main_menu.png').convert()
ground_surface = pygame.image.load('asset/ground.png').convert() # 450*100
sky_surface = pygame.image.load('asset/sky.png').convert() # 450*600 
exo_surface = pygame.image.load('asset/fallen_sky.png').convert() # 450*125
character = pygame.image.load('asset/character_hitbox.png').convert_alpha() # 65*100
character_expired = pygame.image.load('asset/character_expired.png').convert_alpha()
meteor = pygame.image.load('asset/meteor.png').convert()
gameover = pygame.image.load('asset/gameover.png').convert_alpha()

# rect(temporary dont know about sprite class yet)
character_rect = character.get_rect(topleft = (200, 400))
meteor_rect = meteor.get_rect(center = (400, 475))

# game state
meteor_time = pygame.USEREVENT + 1
pygame.time.set_timer(meteor_time, random.randint(900, 1100))

while True:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    ########## Main Menu ##########
    if main_menu == True:
        screen.blit(main_menu_surf, (0,0))
        if key[pygame.K_SPACE]:
            main_menu = False
            alive = True
    ###############################

    ########## Input ##########
    if key[pygame.K_d] and alive: # Go Right
        if character_rect.x >= 385:
            character_rect.x += 0
        elif character_rect.x < 385:
            character_rect.x += 4
    if key[pygame.K_a] and alive: # Go Left
        if character_rect.x <= 0:
            character_rect.x -= 0
        if character_rect.x > 0:
            character_rect.x -= 4
    if key[pygame.K_SPACE] and alive == False:
        character_rect.x = 200
        alive = True
        start_time = pygame.time.get_ticks()
    if key[pygame.K_ESCAPE]:
            main_menu = True
    ###########################
    
    ########## The Game Itself ##########
    if alive and main_menu == False:
        ### enviroment
        final_time = mili2format(display_score())
        screen.blit(sky_surface, (0,0))
        screen.blit(exo_surface, (0,0))
        screen.blit(ground_surface, (0, 500))
        screen.blit(gamefont.render('Press \'esc\' to quit', False, 'black'), (10, 10))
        display_score()
        ### stuff that changeddd
        screen.blit(meteor, meteor_rect)
        if alive:
            screen.blit(character, character_rect)
        else:
            screen.blit(character_expired, character_rect)
        ### game condition
        if character_rect.colliderect(meteor_rect):
            alive = False
    elif alive == False and main_menu == False:
        final = gamefont.render('Your time : %s' %final_time, False, 'white')
        final_rect = final.get_rect(center = (220, 300))
        screen.blit(character_expired, character_rect)
        screen.blit(gameover, (0,0))
        pygame.draw.rect(screen,'black',(75,275,300,50))
        screen.blit(final, final_rect)
    #####################################

    pygame.display.update()
    clock.tick(60)
