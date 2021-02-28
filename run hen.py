import pygame

gamedisplay = pygame.display.set_mode((1200, 600))  # Создаем игровой дисплей.

kontur = pygame.image.load("контур курицы.png")
hen = pygame.image.load("hen.png")
hRect = hen.get_rect()

speed = 200
stop = False
game = True

while game:

    for event in pygame.event.get():  # Проверяем события в окне и реагируем на них.
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                stop = not stop
    if stop != True:
        if hRect.left <= 1200:
            hRect.x += speed
        else:
            hRect.right = 0
    else:
        if hRect.centerx >= 550 and hRect.centerx <= 650:
            print("You win!")

    gamedisplay.fill((255, 255, 255))
    gamedisplay.blit(kontur, (200, 0))
    gamedisplay.blit(hen, hRect)
    pygame.display.update()
pygame.quit()
