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
text_surface = myfont.render('SobolevGameDev', True, 'black')

bg = pygame.image.load('images/background.png')

walk_left = [
    pygame.image.load('images/player_left/left1.png'),
    pygame.image.load('images/player_left/left2.png'),
    pygame.image.load('images/player_left/left3.png'),
    pygame.image.load('images/player_left/left4.png')
]

walk_right = [
    pygame.image.load('images/player_right/right2.png'),
    pygame.image.load('images/player_right/right3.png'),
    pygame.image.load('images/player_right/right1.png'),
    pygame.image.load('images/player_right/right4.png')
]

player_anim_count = 0

bg_x = 0

bg_sound = pygame.mixer.Sound('sounds/music.mp3')
bg_sound.play()


while running:


    screen.blit(bg,(bg_x,0))
    screen.blit(bg, (bg_x + 1280, 0))
    screen.blit(walk_right[player_anim_count],(100,430))


    if player_anim_count == 3 :
        player_anim_count = 0
    else:
        player_anim_count +=1

    bg_x -= 5
    if bg_x == -1280:
        bg_x = 0

    screen.blit(text_surface,(900,670))


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(15)



