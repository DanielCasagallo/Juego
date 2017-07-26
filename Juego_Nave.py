import pygame, sys, os
from pygame.locals import *
import time #para el reloj
import threading #para el reloj
from random import randint

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
#Variables globales para el tiempo
global minutos
minutos = 0
global segundos
segundos = 0

#Funcion relok o tiempo de juego
def tiempo():
    global segundos
    global minutos
    segundos = int(segundos)
    if segundos == 59:
        segundos = 0
        minutos += 1
        return tiempo()
    else:
        segundos += 1
        time.sleep(1)
        return tiempo()

def Reloj():
    fuente = pygame.font.Font(None, 20)
    Reloj = str("Tiempo "+str(minutos)+":"+str(segundos))
    mensaje = fuente.render(Reloj, 1, (255, 255, 255))
    ventana.blit(mensaje, (200, 10))
    
#Funcion Scores o puntajes
def puntaje():
    vida = pygame.image.load("vida.png")
    vida = pygame.transform.scale(vida,(20,20))
    ventana.blit(vida, (100, 10))
    ventana.blit(vida, (120, 10))
    ventana.blit(vida, (140, 10))
    fuente = pygame.font.Font(None, 20)
    text = "Score: 500"
    mensaje = fuente.render(text, 1, (255, 255, 255))
    ventana.blit(mensaje, (10, 10))

    

def teclado():
    teclado = pygame.key.get_pressed()

    global NaveposX
    global NaveposY
    global BalaX
    global BalaY

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

    if teclado[K_a]:
        BalaX=NaveposX+120
        BalaY=NaveposY+70
        balita= rayos(BalaX,BalaY)
        sonido2.play()
        return balita
        
        
        
    if teclado[K_b]:
        sonido.play()
    if teclado[K_m]:
        sonido1.play()
    if teclado[K_d]:
        sonido2.play()
    if teclado[K_e]:
        sonido3.play()

        
class naves():
    def __init__(self, posx,posy):
        self.posx=posx
        self.posy=posy
        
    @property    
    def get_posx(self):
        return self.posx
    
    @property
    def set_posx(self, posx):
        self.posx = posx
        
    @property    
    def get_posy(self):
        return self.posy
    
    @property
    def set_posy(self, posy):
        self.posy = posy
        
class rayos():
    def __init__(self, posx,posy):
        self.posx=posx
        self.posy=posy
        
    @property    
    def get_posx(self):
        return self.posx
    
    @property
    def set_posx(self, posx):
        self.posx = posx
        
    @property    
    def get_posy(self):
        return self.posy
    
    @property
    def set_posy(self, posy):
        self.posy = posy

def crearPersonajes():
    if segundos%3 == 0:
        EnemyX = -1500
        EnemyY = randint(0,650)
        newEnemy = enemigos(EnemyX,EnemyY)
        return newEnemy

class enemigos():
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy

    @property
    def get_posx(self):
        return self.posx

    @property
    def set_posx(self, posx):
        self.posx = posx

    @property
    def get_posy(self):
        return self.posy

    @property
    def set_posy(self, posy):
        self.posy = posy

def crearEnemigos():
    if enemy != None:
        enemigosA.append(enemy)
        acumuladoresEnemigos.append(0)
    r = int(len(enemigosA))

    for i in range(0, r):
        acuE = -20 + acumuladoresEnemigos[i]
        x = -acuE + enemigosA[i].get_posx
        x1 = -x
        y = enemigosA[i].get_posy
        ventana.blit(imagen2, (x1, y))
        acumuladoresEnemigos[i] = acuE
    acuE = 0

    for i in range(0, r):
        x1 = acuE + enemigosA[i].get_posx
        if (x1 > 0):
            del enemigosA[i]
            del acumuladoresEnemigos[i]
            break

pygame.init()
ventana = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Juego")
pygame.mixer.music.load("RobotRock-fondo1.mp3")
fondo = pygame.image.load("fondo1.jpg")

sonido = pygame.mixer.Sound("boss.wav")
sonido1 = pygame.mixer.Sound("menu.wav")
sonido2 = pygame.mixer.Sound("disparo.wav")
sonido3 = pygame.mixer.Sound("explosion.wav")

reloj = pygame.time.Clock()

#Creacion y posicion de la nave

imagen = pygame.image.load("nave2.png")
imagen=pygame.transform.scale(imagen,(200,100))
imagen2 = pygame.image.load("nave3.png")
imagen2=pygame.transform.scale(imagen2,(200,100))
imagen3 = pygame.image.load("nave4.png")
imagen3=pygame.transform.scale(imagen3,(400,400))
disparo = pygame.image.load("disparo.png")
disparo=pygame.transform.scale(disparo,(40,40))


pygame.mixer.music.play()
imagen = pygame.image.load("nave2.png")
imagen = pygame.transform.scale(imagen, (200, 100))

NaveposX = 500

pygame.mixer.music.play(2)
imagen = pygame.image.load("nave2.png")
imagen = pygame.transform.scale(imagen, (200, 100))
NaveposX = -10

#La variable de la posicion Y sera constante ya que esta no variara durante el transcurso del juego
NaveposY = 350

#Variables para uso de colores
blanco = (255, 255, 255)
BalaX=NaveposX
BalaY=NaveposY
movdis=False
nave1=naves(NaveposX,NaveposY)
disparos=[]
acumuladores=[]
enemigosA=[]
acumuladoresEnemigos=[]
x=0
y=0
acu=0

#Creacion de thread o hilo
hilo = threading.Thread(target = tiempo, args = ())
hilo.start()

while True:
    teclado()
    dis=teclado()
    enemy = crearPersonajes()
    
    ventana.fill(blanco)
    ventana.blit(fondo, (0, 0))
    ventana.blit(imagen, (NaveposX, NaveposY))
    ventana.blit(imagen3, (700, 400))
    puntaje() #Llamada a la funcion puntaje
    Reloj()

    crearEnemigos()
    if dis != None:
        disparos.append(dis)
        acumuladores.append(0)
    r=int(len(disparos))
    
    for i in range(0,r):       
        acu=20+acumuladores[i]
        x=acu+disparos[i].get_posx
        y=disparos[i].get_posy   
        ventana.blit(disparo,(x,y))
        acumuladores[i]=acu
    acu=0 
    for i in range(0,r):
        x=acu+disparos[i].get_posx 
        if(x>1280):
            del disparos[i]
            del acumuladores[i]
            break

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
            
    reloj.tick(850)
    pygame.display.flip()
    pygame.display.update()


