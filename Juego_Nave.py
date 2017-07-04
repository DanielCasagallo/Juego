import pygame, sys, os
from pygame.locals import *

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 500

pygame.init()
ventana = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Juego")
fondo = pygame.image.load("fondo.jpg") 
ventana.blit(fondo,(0,0))



while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    pygame.display.update()
