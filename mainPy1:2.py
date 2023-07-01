import pygame
import time
pygame.init()

# wielkość ekranu
width_screen = 800
height_screen = 600

# wyświetlanie i definiowanie ekranu
win = pygame.display.set_mode((width_screen , height_screen))
pygame.display.set_caption("Igor Kalafior 11")

# x, y  / postaci // podzielone przez dwa dla align center
x = width_screen / 2
y = height_screen / 2
file_postac = "images/flygon_repose_by_keh_ven_d24f76c.png"

# Dodatowe obiekty do pomocy
szerokosc = 10
wysokosc = 10
krok = 1



# main loop
run = True
while run:
    # opóźnienie w grze
    pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # funkcje
    def dasz():
        time.sleep(1)
        time.sleep(1)


    # wallpaper // grafiki robione przez Łukasza Haładewicza
    file_tlo = "images/gra.jpg"
    tlo = pygame.image.load(file_tlo)
    win.blit(tlo,(0,0))

    # obsługa zdarzeń
    keys = pygame.key.get_pressed()
    color = (255, 0 , 0)

    # postac main character
    postac = pygame.image.load(file_postac)
    win.blit(postac,(x,y))

    # warunki do zmiany pozycji obiektu // kierunek postaci
    if keys[pygame.K_LEFT]:
        x -= krok
        file_postac = "images/flygon_repose_by_keh_ven_d24f76c2.png"

    if keys[pygame.K_RIGHT]:
        x += krok
        file_postac = "images/flygon_repose_by_keh_ven_d24f76c1.png"

    if keys[pygame.K_UP]:
        y -= krok
        file_postac = "images/flygon_repose_by_keh_ven_d24f76c.png"

    if keys[pygame.K_DOWN] :
        y += krok
        file_postac = "images/flygon_repose_by_keh_ven_d24f76c.png"

    if keys[pygame.K_u]:
        krok += 0.1

    if keys[pygame.K_l]:
        krok -= 0.1

    if keys[pygame.K_c]:
        color = (0,255,0)

    if keys[pygame.K_LSHIFT]:
        dasz()

    ##################################################
    # rysowanie prostokąta // obiekt
    pygame.draw.rect(win, color, (450, 558, szerokosc, wysokosc))
    # ściany istnieją // top
    if y <= 128:            # top
        y += krok

    if x >= 680:            # right
        x -= krok

    if x <= 30:             # left
        x += krok

    if y <= 480:            # botttom
        if x >= 250 or 350:
            y += krok
    y -= krok






            # odświeżenie ekranu
    # print(krok)
    pygame.display.update()