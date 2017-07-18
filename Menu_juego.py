import pygame, sys, os
from pygame.locals import *

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 360

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, 0, 0, 1, 1)
    def update(self):
        self.left, self.top = pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):
    def __init__(self, imagen1, imagen2, x, y):
        self.imagen_normal = imagen1
        self.imagen_seleccion = imagen2
        self.imagen_actual = self.imagen_normal
        self.rect = self.imagen_actual.get_rect()
        self.rect.left, self.rect.top = (x, y)
        
    def update(self, menu, cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen_seleccion
        else: self.imagen_actual = self.imagen_normal

        menu.blit(self.imagen_actual, self.rect)

pygame.init()
menu = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Menu")
fondo = pygame.image.load("fondo.jpg")
pygame.mixer.music.load("menu.wav")

logo = pygame.image.load("logo.png")
logo = pygame.transform.scale(logo, (220, 170))

reloj = pygame.time.Clock()
inicio1 = pygame.image.load("inicio.png")
inicio2 = pygame.image.load("inicio1.png")
tuto1 = pygame.image.load("tuto.png")
tuto2 = pygame.image.load("tuto1.png")
score1 = pygame.image.load("score.png")
score2 = pygame.image.load("score1.png")
boton1 = Boton(inicio1, inicio2, 100, 115)
boton2 = Boton(tuto1, tuto2, 100, 270)
boton3 = Boton(score1, score2, 100, 410)

cursor1 = Cursor()

pygame.mixer.music.play(2)

blanco = (255, 255, 255)

while True:
    menu.fill(blanco)
    menu.blit(fondo, (0, 0))
    menu.blit(logo, (1150, 25))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    reloj.tick(20)
    cursor1.update()
    boton1.update(menu, cursor1)
    boton2.update(menu, cursor1)
    boton3.update(menu, cursor1)
    pygame.display.flip()
    pygame.display.update()
