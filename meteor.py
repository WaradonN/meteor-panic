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
            meteor_rect.y += 3.777
            screen.blit(meteor2,meteor_rect)
        meteor_rect_list = [meteor for meteor in  meteor_rect_list if meteor.y < 700]
        return meteor_rect_list
    else:
        return []

def meteor3_movment(thing, meteor_rect_list):
    if meteor_rect_list:
        for meteor_rect in meteor_rect_list:
            meteor_rect.y += 4.125
            screen.blit(thing,meteor_rect)
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

def mili2format(time, power): #00:00:000
    mili = time
    sec = mili // 1000
    mili_left = mili % 1000
    minu = sec // 60
    sec_left = sec % 60
    if power:
        return "%02d:%03d" %(sec_left, mili_left)
    else:
        return "%02d:%02d:%03d" %(minu,sec_left, mili_left)

def display_score():
    """displaying times simple"""
    survive_time = pygame.time.get_ticks() - start_time
    time_surf = gamefont.render(mili2format(survive_time, False), False, 'white')
    time_rect = time_surf.get_rect(topright = (430,58))
    time_rect_rtt = pygame.transform.rotozoom(time_surf,7,1)
    screen.blit(time_rect_rtt, time_rect)
    return survive_time

def char_animation():
    global character_surf, char_index
    if key[pygame.K_a] and key[pygame.K_d]:
        character_surf = char_ani[0]
    elif key[pygame.K_a]:
        char_index += 0.1
        if char_index >= len(char_ani):
            char_index = 1
        character_surf = char_ani[int(char_index)]
    elif key[pygame.K_d]:
        char_index += 0.1
        if char_index >= len(char_ani):
            char_index = 1
        character_surf = char_ani[int(char_index)]
        character_surf = pygame.transform.flip(character_surf,True,False)
    else:
        character_surf = char_ani[0]

# meta and inner works
pygame.init()
screen = pygame.display.set_mode((450, 600)) #450*600
icon = pygame.image.load('asset/meteor_var_1.png').convert_alpha() # 100*100 or smaller
pygame.display.set_caption('Meteor Panic!')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
gamefont = pygame.font.Font('asset/PressStart2P.ttf', 13)

# initial state
menu = True
alive = False
how_to = False
speed_up_status = False
start_time = 0
final_time = mili2format(0, False)
speed = 3.5
speed_up_timer = 0

# stuff to draw
gameover = pygame.image.load('asset/gameover.png').convert_alpha() # 450*600
ground_surface = pygame.image.load('asset/ground.png').convert() # 450*100
sky_surface = pygame.image.load('asset/sky.png').convert() # 450*600 
exo_surface = pygame.image.load('asset/fallen_sky.png').convert_alpha() # 450*125
main_menu = pygame.image.load('asset/main_menu.png').convert() # 450*600
tutorial = pygame.image.load('asset/how_to_screen_test.png').convert() # 450*600
score_border = pygame.image.load('asset/scoreborder.png').convert_alpha()

# sound
mainsong = pygame.mixer.Sound('audio/8_bit_ad.mp3')
speedup = pygame.mixer.Sound('audio/testsound.mp3')

# event
meteor_time_1 = pygame.USEREVENT + 1
pygame.time.set_timer(meteor_time_1, random.randint(2750, 4000)) ## biggest one
meteor_time_2 = pygame.USEREVENT + 2
pygame.time.set_timer(meteor_time_2, random.randint(1200, 1750)) ## long
meteor_time_3 = pygame.USEREVENT + 3
pygame.time.set_timer(meteor_time_3, random.randint(550, 1150)) ## smallest
power_up_time = pygame.USEREVENT + 4
pygame.time.set_timer(power_up_time, 5000)

# meteor
meteor1 = pygame.image.load('asset/meteor_var_1.png').convert_alpha() #50*50
meteor1_rect = meteor1.get_rect(center = (random.randint(-50, 550), -100))
meteor1_rect_list = []
meteor2 = pygame.image.load('asset/meteor_var_2.png').convert_alpha() #40*55
meteor2_rect = meteor2.get_rect(center = (random.randint(-50, 550), -100))
meteor2_rect_list = []
meteor3 = pygame.image.load('asset/meteor_var_3.png').convert_alpha() #30*30
meteor3_rect = meteor3.get_rect(center = (random.randint(-50, 550), -100))
meteor3_rect_list = []
speed_up = pygame.image.load('asset/speed_pu.png').convert()
speed_up_rect = speed_up.get_rect(center = (random.randint(-50, 550), -100))
power_up_rect_list = []

# charecter
char_stand = pygame.image.load('asset/character_1.png').convert_alpha() # 65*100
char_walk_2 = pygame.image.load('asset/character_2.png').convert_alpha() # 65*100
char_walk_3 = pygame.image.load('asset/character_3.png').convert_alpha() # 65*100
char_ani = [char_stand, char_walk_2, char_walk_3]
char_index = 0
character_surf = char_ani[char_index]
character_rect = character_surf.get_rect(topleft = (210, 425))


while True:
    mainsong.play()
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
            if event.type == power_up_time:
                power_up_rect_list.append(speed_up.get_rect(center = (random.randint(0, 550), 0)))
    ###########################

    ########## Input ##########
    if alive and menu == False:
        if key[pygame.K_d] and character_rect.x < 385: # Go Right
            character_rect.x += speed
        if key[pygame.K_a] and character_rect.x > 0: # Go Left
            character_rect.x -= speed
    ########## Menu Navigation ##########
    if key[pygame.K_SPACE]:
        if menu == False and how_to == False:
            character_rect.x = 200
            alive = True
            start_time = pygame.time.get_ticks()
        elif menu:
            alive = True
            menu = False
    if key[pygame.K_TAB]:
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
            power_up_rect_list.clear()
        if alive == True and menu == False and how_to == False:
            menu = True
            how_to = False
            alive = False
            meteor1_rect_list.clear()
            meteor2_rect_list.clear()
            meteor3_rect_list.clear()
            power_up_rect_list.clear()
        elif alive == False and menu == False and how_to == True:
            menu = True
            how_to = False
    ###########################
    
    ########## The Game Itself ##########
    if alive == True and menu == False and how_to == False:
        pygame.mixer.music.set_volume(0.3)
        ### enviroment
        final_time = mili2format(display_score(), False)
        screen.blit(sky_surface, (0,-30))
        ### stuff that change
        meteor1_rect_list = meteor1_movment(meteor1_rect_list)
        meteor2_rect_list = meteor2_movment(meteor2_rect_list)
        meteor3_rect_list = meteor3_movment(meteor3, meteor3_rect_list)
        power_up_rect_list = meteor3_movment(speed_up, power_up_rect_list)
        if alive:
            char_animation()
            screen.blit(character_surf, character_rect)
        ### die condition
        if collision(character_rect,meteor1_rect_list):
            pygame.mixer.music.load('audio/gameover.mp3')
            pygame.mixer.music.play()
            alive = False
            how_to == False
        if collision(character_rect,meteor2_rect_list):
            pygame.mixer.music.load('audio/gameover.mp3')
            pygame.mixer.music.play()
            alive = False
            how_to == False
        if collision(character_rect,meteor3_rect_list):
            pygame.mixer.music.load('audio/gameover.mp3')
            pygame.mixer.music.play()
            alive = False
            how_to == False
        if collision(character_rect,power_up_rect_list):
            pygame.mixer.music.load('audio/testsound.mp3')
            pygame.mixer.music.play()
            speed_up_timer = 500
            speed_up_status = True
            power_up_rect_list.clear()
            speed = 5.3333333
        if speed_up_status:
            speed_up_timer -= 1
            spped_time_dis = gamefont.render(mili2format(speed_up_timer, True), False, 'white')
            screen.blit(spped_time_dis, (10,10))
        if speed_up_timer <= 0:
            speed_up_status = False
            speed_up_timer = 0
            speed = 4
        screen.blit(exo_surface, (0,0))
        screen.blit(ground_surface,(0,525))
        screen.blit(score_border, (250,25))
        if speed_up_status:
            screen.blit(spped_time_dis, (375,545))
            screen.blit(speed_up, (400,565))
        display_score()
    elif alive == False and menu == False and how_to == False:
        meteor1_rect_list.clear()
        meteor2_rect_list.clear()
        meteor3_rect_list.clear()
        power_up_rect_list.clear()
        speed = 4
        speed_up_timer = 0
        final = gamefont.render('Your time : %s' %final_time, False, 'white')
        final_rect = final.get_rect(center = (220, 300))
        screen.blit(gameover, (0,0))
        pygame.draw.rect(screen,'black',(75,275,300,50))
        screen.blit(final, final_rect)
    elif alive == False and menu == True and how_to == False:
        screen.blit(main_menu, (0,0))
    elif alive == False and menu == False and how_to == True:
        screen.blit(tutorial, (0,1))
    #####################################
    # print('menu: %r | alive: %r | how_to: %r' %(menu,alive,how_to))
    pygame.display.update()
    clock.tick(60)
