import pygame, sys, os
from pygame.locals import *

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

def teclado():
    teclado = pygame.key.get_pressed()

    global NaveposX
    global NaveposY

    if teclado[K_RIGHT]:
        if NaveposX <=1130:
            NaveposX += 5

    if teclado[K_LEFT]:
        if NaveposX > -10:
            NaveposX -= 5
            
    if teclado[K_DOWN]:
        if NaveposY <=615:
            NaveposY += 5

    if teclado[K_UP]:
        if NaveposY > 0:
            NaveposY -= 5
    if teclado[K_b]:
        sonido.play()
    if teclado[K_m]:
        sonido1.play()
    if teclado[K_d]:
        sonido2.play()
    if teclado[K_e]:
        sonido3.play()
        
        

pygame.init()
ventana = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Juego")
pygame.mixer.music.load("fondos.mp3")
fondo = pygame.image.load("fondo.jpg")

sonido = pygame.mixer.Sound("boss.wav")
sonido1 = pygame.mixer.Sound("menu.wav")
sonido2 = pygame.mixer.Sound("disparo.wav")
sonido3 = pygame.mixer.Sound("explosion.wav")

reloj = pygame.time.Clock()

#Creacion y posicion de la nave
pygame.mixer.music.play()
imagen = pygame.image.load("nave1.png")
imagen = pygame.transform.scale(imagen, (200, 100))
NaveposX = 500
#La variable de la posicion Y sera constante ya que esta no variara durante el transcurso del juego
NaveposY = 590

#Variables para uso de colores
blanco = (255, 255, 255)

while True:
    teclado()
    ventana.fill(blanco)
    ventana.blit(fondo, (0, 0))
    ventana.blit(imagen, (NaveposX, NaveposY))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    reloj.tick(640)
    pygame.display.flip()
    pygame.display.update()
