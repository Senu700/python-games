import pygame

gamedisplay = pygame.display.set_mode((800, 600))  # Создаем игровой дисплей.
gamedisplay.fill((255, 255, 255))  # Цвет окна

draw = False

game = True

color = (0, 0, 0)

while game:
    events = pygame.event.get()

    for event in events:  # Проверяем события в окне и реагируем на них.
        if event == pygame.QUIT:
            game = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            draw = True
            if event.button == 1:
                color = (255, 0, 0)  # Red
            if event.button == 3:
                color = (0, 0, 255)  # Blue
            if event.button == 2:
                color = (125, 0, 0)

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
