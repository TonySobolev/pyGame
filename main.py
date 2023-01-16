import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))  #,flags=pygame.NOFRAME  no frame around app
pygame.display.set_caption("Sobolev Game")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

running = True
backgroungColor=  (3, 252, 186)
while running:

    screen.fill(backgroungColor)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                backgroungColor= (92, 211, 250)


