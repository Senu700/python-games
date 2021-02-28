import pygame
from random import randint as ri
from math import sqrt

gamedisplay = pygame.display.set_mode((800, 600))  # Создаем игровой дисплей.
law = pygame.image.load("957cbd72dd2bd29a441d2d9a1f83b8cb_907.jpg")
small_law = pygame.transform.scale(law, (800,600))
gamedisplay.blit(small_law,(0,0) )

#gamedisplay.fill((255, 255, 255))  # Цвет окна

def get_distance(mousepos, rect):
    mouseX, mouseY = mousepos # Координаты мышки
    cowX, cowY = rect.center # Координаты коровы

    distance = sqrt((mouseX-cowX)**2 + (mouseY-cowY)**2)
    return distance


cow = pygame.image.load("corowa.png")
small_cow = pygame.transform.scale(cow, (130,80))
small_rect = small_cow.get_rect()
small_rect.x = ri(0, 700)
small_rect.y = ri(0, 500)

game = True
while game:

    for event in pygame.event.get():  # Проверяем события в окне и реагируем на них.

        if event == pygame.QUIT:
            game = False

        if event.type == pygame.MOUSEBUTTONDOWN:
           if small_rect.collidepoint(event.pos):
               gamedisplay.blit(small_cow,small_rect )
           else:
               d = get_distance(event.pos, small_rect)
               pygame.draw.circle(gamedisplay, (0, 0,255), event.pos, d//10)


    pygame.display.update()

pygame.quit()
