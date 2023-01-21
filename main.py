import pygame


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1280, 720))  #,flags=pygame.NOFRAME  no frame around app
pygame.display.set_caption("Sobolev Game")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)



running = True
backgroungColor=(3, 252, 186)

myfont = pygame.font.Font('fonts/RubikVinyl-Regular.ttf', 40)
text_surface = myfont.render('SobolevGameDev', True, 'aquamarine')

bg = pygame.image.load('images/background.png')

walk_left = [
    pygame.image.load('images/player_left/left1.png'),
    pygame.image.load('images/player_left/left2.png'),
    pygame.image.load('images/player_left/left3.png'),
    pygame.image.load('images/player_left/left4.png')
]

walk_right = [
    pygame.image.load('images/player_right/right1.png'),
    pygame.image.load('images/player_right/right2.png'),
    pygame.image.load('images/player_right/right4.png'),
    pygame.image.load('images/player_right/right3.png')
]

player_anim_count = 0  #changing the picture of player for animated motion

bg_x = 0  #position of starting background

player_speed = 10
player_x = 100
player_y = 500

is_jump = False
jump_force = 10 #power of jump
jump_count = jump_force  #iterration for jump function

bg_sound = pygame.mixer.Sound('sounds/music.mp3')
bg_sound.play()


while running:


    screen.blit(bg,(bg_x,0))
    screen.blit(bg, (bg_x + 1280, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        screen.blit(walk_left[player_anim_count],(player_x,player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))



    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_x > 50:
        player_x -= player_speed
    elif (keys[pygame.K_RIGHT]or keys[pygame.K_d]) and player_x < 1180:
        player_x += player_speed

    if not is_jump:
        if keys[pygame.K_SPACE]:
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

    screen.blit(text_surface,(900,10))


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(70)



