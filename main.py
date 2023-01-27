import pygame


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1280, 720))  #,flags=pygame.NOFRAME  no frame around app
pygame.display.set_caption("Sobolev Game")
icon = pygame.image.load('images/icon.png').convert_alpha()
pygame.display.set_icon(icon)




backgroungColor=(3, 252, 186)

myfont = pygame.font.Font('fonts/RubikVinyl-Regular.ttf', 40)   #text for logo
text_surface = myfont.render('SobolevGameDev', True, 'aquamarine')

myfont_lose = pygame.font.Font('fonts/RubikVinyl-Regular.ttf', 90) #text for lose
text_lose = myfont_lose.render('You lose, feels bad', True, 'orange')

myfont_restart = pygame.font.Font('fonts/RubikVinyl-Regular.ttf', 55) #text for restart
text_restart = myfont_restart.render('Press here to try again', True, 'orange')
text_restart_rect = text_restart.get_rect(topleft=(290,350))   #creating rect to check if we click on restart

arrows_left = 15
arrow = pygame.image.load('images/arrow.png').convert_alpha()  #creating projectile
arrows = []


bg = pygame.image.load('images/background.png').convert()

bg_sound = pygame.mixer.Sound('sounds/music.mp3')
lose_sound = pygame.mixer.Sound('sounds/lose_music.mp3')
bg_sound.play()


walk_left = [
    pygame.image.load('images/player_left/left1.png').convert_alpha(),
    pygame.image.load('images/player_left/left2.png').convert_alpha(),
    pygame.image.load('images/player_left/left3.png').convert_alpha(),
    pygame.image.load('images/player_left/left4.png').convert_alpha()
]

walk_right = [
    pygame.image.load('images/player_right/right1.png').convert_alpha(),
    pygame.image.load('images/player_right/right2.png').convert_alpha(),
    pygame.image.load('images/player_right/right4.png').convert_alpha(),
    pygame.image.load('images/player_right/right3.png').convert_alpha()
]


ghost = pygame.image.load('images/ghost.png').convert_alpha()

ghost_list_in_game = []



player_anim_count = 0  #changing the picture of player for animated motion

bg_x = 0  #position of starting background

player_speed = 10
player_x = 100
player_y = 500

is_jump = False  #status of jump by def is false, so when jump is pressed animation started
jump_force = 11 #power of jump
jump_count = jump_force  #iterration for jump function



ghost_timer = pygame.USEREVENT + 1  #creating timer
ghost_respawn_time = 2500 # 1k equals 1 s
pygame.time.set_timer(ghost_timer, ghost_respawn_time)       #settting the timer, 1000 ms equals 1 sec


gameplay = True   #var for lose condition

running = True
while running:



    if gameplay:

        screen.blit(bg,(bg_x,0))           #adding first bg image to draw
        screen.blit(bg, (bg_x + 1280, 0))  #adding second bg image to cycle it
       # screen.blit(ghost,(ghost_x, 550)) #placing enemy

        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))   #drawing the rect around player to check collision
        #ghost_rect = ghost.get_rect(topleft=(ghost_x,550))  #rect around enemy for collison
        if ghost_list_in_game:   #creating the list of enemies
            for (i, el) in enumerate(ghost_list_in_game):
                screen.blit(ghost, el)
                el.x -= 5

                if el.x < -30:   #destroing enemies which already pass the screen
                    ghost_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    gameplay = False

      #  if player_rect.colliderect(ghost_rect):  #checking if collison happend
       #     print('You lose')

        keys = pygame.key.get_pressed()       #check what key is pressed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            screen.blit(walk_left[player_anim_count],(player_x,player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_x > 50:   #movement
            player_x -= player_speed
        elif (keys[pygame.K_RIGHT]or keys[pygame.K_d]) and player_x < 1180:
            player_x += player_speed

        if not is_jump:
            if (keys[pygame.K_SPACE] or keys[pygame.K_w]) :
                is_jump = True
        else:
            if jump_count >= -jump_force:
                if jump_count > 0 :
                    player_y -= (jump_count**2) / 2
                else:
                    player_y += (jump_count**2) / 2
                jump_count -=1
            else:
                is_jump = False
                jump_count = jump_force

        if player_anim_count == 3 :
            player_anim_count = 0
        else:
            player_anim_count +=1

        bg_x -= 2
        if bg_x <= -1280:
            bg_x = 0



        if arrows: #behavior of arrows, spawn on player location, destroy after it leaves the screen
            for (i, el) in enumerate(arrows):
                screen.blit(arrow, (el.x, el.y))
                el.x +=10

                if el.x > 1300:
                    arrows.pop(i)

                if ghost_list_in_game:     #checking collision of arrows with enemies, annihillate both
                    for (index, ghost_el) in enumerate(ghost_list_in_game):
                        if el.colliderect(ghost_el):
                            ghost_list_in_game.pop(index)
                            arrows.pop(i)

        screen.blit(text_surface,(900,10))





    else:
        screen.fill((130, 232, 250))
        bg_sound.stop()
        screen.blit(text_surface, (900, 10))

        screen.blit(text_lose, (250, 240))
        screen.blit(text_restart, text_restart_rect)
        lose_sound.play()

        mouse = pygame.mouse.get_pos()   #var for mouse positon

        if text_restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:  #1st is positon of mouse over restart and second is left_click is pressed (1 is right,2 is wheel)
            lose_sound.stop()
            gameplay = True
            bg_sound.play()
            player_x =100
            ghost_list_in_game.clear()
            arrows.clear()
            arrows_left = 15

    pygame.display.update()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:      #exit the game
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(1285,530)))  #creating enemy at starting position

        if gameplay and event.type ==pygame.KEYUP and event.key == pygame.K_q and arrows_left>0: #shooting mechanic, shooting allowed only while gaming, with single click on button
            arrows.append(arrow.get_rect(topleft=(player_x + 30, player_y + 30)))
            arrows_left -= 1


    clock.tick(70)



