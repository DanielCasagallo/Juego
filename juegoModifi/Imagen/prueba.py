# Importamos la librería
import pygame

import sys

# Importamos constantes locales de pygame
from pygame.locals import *

# Iniciamos Pygame
evento = 0
pygame.init()

# Creamos una surface (la ventana de juego), asignándole un alto y un ancho
Ventana = pygame.display.set_mode((900, 900))

# Le ponemos un título a la ventana
pygame.display.set_caption("Poniendo Imágenes")

# Cargamos las imágenes
Fondo = pygame.image.load("fondo.jpg")
ancho = 500
while True:
    if evento < 5:
        Rect = (0,100,ancho,700)
        ImagenTrozo = Fondo.subsurface(Rect)
        evento += 1
        ancho = 100
    


# posiciona las imágenes en Ventana
Ventana.blit(ImagenTrozo, (0, 0))

# refresca los gráficos
pygame.display.flip()

# Bucle infinito para mantener el programa en ejecución
while True:

    # Manejador de eventos
    for evento in pygame.event.get():
        # Pulsación de la tecla escape
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                sys.exit()
