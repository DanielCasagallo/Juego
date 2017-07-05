import pygame, sys, os
from pygame.locals import *

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

def teclado():
    teclado = pygame.key.get_pressed()

    global NaveposX

    if teclado[K_RIGHT]:
        if NaveposX <=1032:
            NaveposX += 5

    if teclado[K_LEFT]:
        if NaveposX > 0:
            NaveposX -= 5

pygame.init()
ventana = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Juego")

fondo = pygame.image.load("fondo.jpg")

reloj = pygame.time.Clock()

#Creacion y posicion de la nave
imagen = pygame.image.load("nave.png")
NaveposX = 500
#La variable de la posicion Y sera constante ya que esta no variara durante el transcurso del juego
CNaveposY = 590

#Variables para uso de colores
blanco = (255, 255, 255)

while True:
    teclado()
    ventana.fill(blanco)
    ventana.blit(fondo, (0, 0))
    ventana.blit(imagen, (NaveposX, CNaveposY))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    reloj.tick(60)
    pygame.display.flip()
    pygame.display.update()
