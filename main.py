import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))  #,flags=pygame.NOFRAME  no frame around app
pygame.display.set_caption("Sobolev Game")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

square = pygame.Surface((100, 100))
square.fill('Blue')

running = True
backgroungColor=(3, 252, 186)

myfont = pygame.font.Font('fonts/RubikVinyl-Regular.ttf', 60)
text_surface = myfont.render('SobolevGameDev', True, 'black')

player = pygame.image.load('images/icon.png')

x_coord = 300
x_dir = 1

while running:

    screen.fill(backgroungColor)

    screen.blit(square, (50, 50))

    pygame.draw.circle(screen, 'red', (250,250), 50)
    pygame.draw.circle(square, 'red', (25, 25), 10)
    screen.blit(text_surface,(500,0))




    screen.blit(player, (x_coord,100))
    x_coord+=x_dir
    if x_coord >600:
        x_dir = -1
    elif x_coord <300:
        x_dir = 1


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()



