import pygame
pygame.init()
win = pygame.display.set_mode((800 , 600))
pygame.display.set_caption("Igor Kalafior 11")
x = 500
y = 500
szerokosc = 20
wysokosc = 20
krok = 4
run = True
while run:
    # opóźnienie w grze
    pygame.time.delay(6)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # obsługa zdarzeń
    keys = pygame.key.get_pressed()
    file = "C:\ "
    tlo = pygame.image.load(file)
    win.blit(tlo,(0,0))

    ####################
    # warunki do zmiany pozycji obiektu

    if keys[pygame.K_LEFT]:
        x -= krok
    if keys[pygame.K_RIGHT]:
        x += krok
    if keys[pygame.K_UP]:
        y -= krok
    if keys[pygame.K_DOWN] :
        y += krok

    ###################
    # if keys[pygame.K_SPACE]:
    #     run = False
    # "czyszczenie" ekranu // brak śladu
    win.fill((0, 0, 0))

    ##################################################
    # rysowanie prostokąta // obiekt
    pygame.draw.rect(win, (255,0,0), (x, y, szerokosc, wysokosc))


    # odświeżenie ekranu
    pygame.display.update()