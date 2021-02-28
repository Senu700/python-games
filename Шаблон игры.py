import pygame

gamedisplay = pygame.display.set_mode((800, 600))  # Создаем игровой дисплей.
gamedisplay.fill((255, 255, 255))  # Цвет окна

game = True
color = (0, 0, 0)
while game:

    for event in events = pygame.event.get()  # Проверяем события в окне и реагируем на них.
        if event == pygame.QUIT:
            game = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            pass


        if event.type == pygame.MOUSEBUTTONUP:
            draw = False

        if event.type == pygame.KEYDOWN: # Если нажали кнопку на клавиатуре
            if event.key == pygame.K_s: # Если это была буква S
                pygame.image.save(gamedisplay, 'myImage.png') # Сохраняем картинку

    if draw == True:
        mousepos = pygame.mouse.get_pos()
        pygame.draw.circle(gamedisplay, color, event.pos, 20)

     pygame.display.update()


pygame.quit()
