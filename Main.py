import pygame
import time
pygame.init()



# wielkość ekranu
width_screen = 800
height_screen = 600

# wyświetlanie i definiowanie ekranu
win = pygame.display.set_mode((width_screen , height_screen))
pygame.display.set_caption("nwoijfgowsmowjngh")

# x, y  / postaci // podzielone przez dwa dla align center
x = width_screen / 2
y = height_screen / 2
file_postac = "D:\pygame hehe\postac.png"          #w razie czego sama postacstanieodprzodu128x128.png

# Dodatowe obiekty do pomocy
szerokosc = 10
wysokosc = 10
krok = 1



# main loop
run = True
while run:
    # opóźnienie w grze
    pygame.time.delay(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # funkcje
    def dasz():
        time.sleep(1)
        time.sleep(1)


    # wallpaper // grafiki robione przez Łukasza Haładewicza
    file_tlo = "D:\pygame hehe\gra.png"            #w razie czego zmienic na gra.png
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
        file_postac = "D:\pygame hehe\postac.png"                 #tutaj trzeba zmienic postac jesli nie bedzie dzialac na     postacchodzenieodprzodu128x128.gif
    
    if keys[pygame.K_RIGHT]:
        x += krok
        file_postac = "D:\pygame hehe\postac.png"                               # TYMCZASOWE DANE (POSTAĆ)

    if keys[pygame.K_UP]:
        y -= krok
        file_postac = "D:\pygame hehe\postac.png"

    if keys[pygame.K_DOWN] :
        y += krok
        file_postac = "D:\pygame hehe\postac.png"

    if keys[pygame.K_u]:
        krok += 0.7

    if keys[pygame.K_l]:
        krok -= 0.7

    if keys[pygame.K_c]:
        color = (0,255,0)

    if keys[pygame.K_LSHIFT]:
        dasz()

    ##################################################
    # rysowanie prostokąta // obiekt
    pygame.draw.rect(win, color, (450, 558, szerokosc, wysokosc))
    # ściany istnieją // top
    if y <= 20:            # top
        y += krok

    if x >= 665:            # right
        x -= krok

    if x <= 10:             # left
        x += krok

    if y <= 425:            # botttom
        if x >= 200 or 400:
            y += krok
    y -= krok






            # odświeżenie ekranu
    # print(krok)
    pygame.display.update()