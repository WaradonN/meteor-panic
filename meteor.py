import pygame
import random
from sys import exit

###### functions and good stuffs ######
def meteor1_movment(meteor_rect_list):
    if meteor_rect_list:
        for meteor_rect in meteor_rect_list:
            meteor_rect.y += 2.3
            screen.blit(meteor1,meteor_rect)
        meteor_rect_list = [meteor for meteor in  meteor_rect_list if meteor.y < 700]
        return meteor_rect_list
    else:
        return []

def meteor2_movment(meteor_rect_list):
    if meteor_rect_list:
        for meteor_rect in meteor_rect_list:
            meteor_rect.y += 4
            screen.blit(meteor2,meteor_rect)
        meteor_rect_list = [meteor for meteor in  meteor_rect_list if meteor.y < 700]
        return meteor_rect_list
    else:
        return []

def meteor3_movment(meteor_rect_list):
    if meteor_rect_list:
        for meteor_rect in meteor_rect_list:
            meteor_rect.y += 4.777
            screen.blit(meteor3,meteor_rect)
        meteor_rect_list = [meteor for meteor in  meteor_rect_list if meteor.y < 700]
        return meteor_rect_list
    else:
        return []

def collision(player,meteor):
    if meteor:
        for meteor_rect in meteor:
            if player.colliderect(meteor_rect):
                return True
    return False

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
menu = True
alive = False
how_to = False
start_time = 0
final_time = mili2format(0)
speed = 4

# stuff to draw
gameover = pygame.image.load('asset/gameover.png').convert_alpha() # 450*600
ground_surface = pygame.image.load('asset/ground.png').convert() # 450*100
sky_surface = pygame.image.load('asset/sky.png').convert() # 450*600 
exo_surface = pygame.image.load('asset/fallen_sky.png').convert() # 450*125
main_menu = pygame.image.load('asset/main_menu.png') # 450*600
tutorial = pygame.image.load('asset/how_to_screen.png') # 450*600

# event
meteor_time_1 = pygame.USEREVENT + 1
pygame.time.set_timer(meteor_time_1, random.randint(2500, 3500)) ## biggest one
meteor_time_2 = pygame.USEREVENT + 2
pygame.time.set_timer(meteor_time_2, random.randint(1000, 1500)) ## long
meteor_time_3 = pygame.USEREVENT + 3
pygame.time.set_timer(meteor_time_3, random.randint(500, 1250)) ## smallest

# meteor
meteor1 = pygame.image.load('asset/meteor_var_1.png').convert() #50*50
meteor1_rect = meteor1.get_rect(center = (random.randint(-50, 550), -100))
meteor1_rect_list = []
meteor2 = pygame.image.load('asset/meteor_var_2.png').convert() #40*55
meteor2_rect = meteor2.get_rect(center = (random.randint(-50, 550), -100))
meteor2_rect_list = []
meteor3 = pygame.image.load('asset/meteor_var_3.png').convert() #30*30
meteor3_rect = meteor3.get_rect(center = (random.randint(-50, 550), -100))
meteor3_rect_list = []

# charecter
character_surf = pygame.image.load('asset/character_1_hitbox.png').convert_alpha() # 65*100
character_rect = character_surf.get_rect(topleft = (210, 400))


while True:
    ########## Event ##########
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if alive:
            if event.type == meteor_time_1:
                meteor1_rect_list.append(meteor1.get_rect(center = (random.randint(0, 550), 0)))
            if event.type == meteor_time_2:
                meteor2_rect_list.append(meteor2.get_rect(center = (random.randint(0, 550), 0)))
            if event.type == meteor_time_3:
                meteor3_rect_list.append(meteor3.get_rect(center = (random.randint(0, 550), 0)))
    ###########################

    ########## Input ##########
    if alive and menu == False:
        if key[pygame.K_d] and character_rect.x < 385: # Go Right
            character_rect.x += speed
        if key[pygame.K_a] and character_rect.x > 0: # Go Left
            character_rect.x -= speed
    if key[pygame.K_SPACE]:
        if menu == False and how_to == False:
            character_rect.x = 200
            alive = True
            start_time = pygame.time.get_ticks()
        elif menu:
            alive = True
            menu = False
    if key[pygame.K_LSHIFT]:
        if menu:
            menu = False
            alive = False
            how_to = True
    if key[pygame.K_ESCAPE]:
        if alive == False and menu == False and how_to == False:
            menu = True
            how_to = False
            alive = False
            meteor1_rect_list.clear()
            meteor2_rect_list.clear()
            meteor3_rect_list.clear()
        if alive == True and menu == False and how_to == False:
            menu = True
            how_to = False
            alive = False
            meteor1_rect_list.clear()
            meteor2_rect_list.clear()
            meteor3_rect_list.clear()
        elif alive == False and menu == False and how_to == True:
            menu = True
            how_to = False
    ###########################
    
    ########## The Game Itself ##########
    if alive == True and menu == False and how_to == False:
        ### enviroment
        final_time = mili2format(display_score())
        screen.blit(sky_surface, (0,0))
        ### stuff that change
        meteor1_rect_list = meteor1_movment(meteor1_rect_list)
        meteor2_rect_list = meteor2_movment(meteor2_rect_list)
        meteor3_rect_list = meteor3_movment(meteor3_rect_list)
        if alive:
            screen.blit(character_surf, character_rect)
        ### die condition
        if collision(character_rect,meteor1_rect_list):
            alive = False
            how_to == False
        if collision(character_rect,meteor2_rect_list):
            alive = False
            how_to == False
        if collision(character_rect,meteor3_rect_list):
            alive = False
            how_to == False
        screen.blit(exo_surface, (0,0))
        screen.blit(ground_surface,(0,500))
        display_score()
    elif alive == False and menu == False and how_to == False:
        meteor1_rect_list.clear()
        meteor2_rect_list.clear()
        meteor3_rect_list.clear()
        final = gamefont.render('Your time : %s' %final_time, False, 'white')
        final_rect = final.get_rect(center = (220, 300))
        screen.blit(gameover, (0,0))
        pygame.draw.rect(screen,'black',(75,275,300,50))
        screen.blit(final, final_rect)
    elif alive == False and menu == True and how_to == False:
        screen.blit(main_menu, (0,0))
    elif alive == False and menu == False and how_to == True:
        screen.blit(tutorial, (0,0))
    #####################################
    print('menu: %r | alive: %r | how_to: %r' %(menu,alive,how_to))
    pygame.display.update()
    clock.tick(60)
