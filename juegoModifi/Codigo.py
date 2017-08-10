
import pygame,sys
from pygame.locals import *
from random import randint
import pygame.event as GAME_EVENTOS
import pygame.locals as GAME_GLOBALS
import time
import random
import threading #hilos para la ejecucion del hiloi


Ancho = 1200
Alto = 630
puntos = 0
vida = 0
cont =0
GameOver = True
control2 =0
ListaEnemigo = []
ListaEnemigo2 = []
ListaAsteroides = []
ListaAsteroidesGigantes= []

#Ventana del juego
Ventana = pygame.display.set_mode((Ancho, Alto))

# variables globales para el reloj y tiempo
global minutos
minutos = 0
global segundos
segundos = 0
global segundosReloj
segundosReloj = 0

ImagenMisil =  pygame.image.load("Imagen/misil.png")
#ASTEROIDES
ImagenAsteroide1 = pygame.image.load("Imagen/A1.png")
ImagenAsteroide2 = pygame.image.load("Imagen/A2.png")
ImagenAsteroide3 = pygame.image.load("Imagen/A3.png")
ImagenAsteroide4 = pygame.image.load("Imagen/A4.png")
ImagenAsteroide5 = pygame.image.load("Imagen/A5.png")
ImagenAsteroide6 = pygame.image.load("Imagen/A6.png")
ImagenAsteroide7 = pygame.image.load("Imagen/A7.png")
ImagenAsteroide8 = pygame.image.load("Imagen/A8.png")
ImagenAsteroide9 = pygame.image.load("Imagen/A9.png")
ImagenAsteroide10 = pygame.image.load("Imagen/A10.png")

ImagenAsteroideGigante1 =  pygame.image.load("Imagen/AG1.png")
ImagenAsteroideGigante2 =  pygame.image.load("Imagen/AG2.png")



#clase para la nave espacial
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNave = pygame.image.load("Imagen/1.png")
        self.ImagenNave = pygame.transform.scale(self.ImagenNave, (120, 70))
        self.Explosion = pygame.image.load("Imagen/explosion.png")
        self.Explosion = pygame.transform.scale(self.Explosion, (120, 70))
        self.rect = self.ImagenNave.get_rect()

        self.rect.centerx = 100
        self.rect.centery = Alto/2

        self.vida = True
        self.Listadisparos = []
        self.ListaMisiles = []
        self.velocidad = 10
        self.sonidoDisparo = pygame.mixer.Sound("Musica/disparo.wav")
        self.sonidoExplosion = pygame.mixer.Sound("Musica/explosion.wav")

    def movientoDerecha(self):
        if self.rect.right <=Ancho:
            self.rect.right += self.velocidad
    def movientoIzquierda(self):
        if self.rect.left > -10:
            self.rect.right -= self.velocidad
    def movientoArriba(self):
        if self.rect.top >40:
            self.rect.top -= self.velocidad
    def movientoAbajo(self):
        if self.rect.bottom <=600:
            self.rect.bottom += self.velocidad

    def disparar(self, x, y):
        proyectil = Bala(x , y ,"Imagen/bala.png",True )
        self.Listadisparos.append(proyectil)
        self.sonidoDisparo.play()

    def destruccion(self):
        self.sonidoExplosion.play()
        self.vida = False
        self.velocidad =0
        self.ImagenNave = self.Explosion

    def dispararMisil(self, x, y):
        Misil = Coete(x , y)
        self.ListaMisiles.append(Misil)

    def dibujar(self, Superficie):
        Superficie.blit(self.ImagenNave, self.rect)


class Bala(pygame.sprite.Sprite):
    def __init__(self, posx, posy, ruta , personaje):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenProyectil = pygame.image.load(ruta)
        self.rect = self.ImagenProyectil.get_rect()
        self.VelocidadDisparo = 17

        self.rect.right = posx
        self.rect.top = posy

        self.disparoPersonaje = personaje


    def trayectoria(self):
        if self.disparoPersonaje == True:
            self.rect.right = self.rect.right + self.VelocidadDisparo
        else:
            self.rect.right = self.rect.right - self.VelocidadDisparo

    def dibujar(self, Superficie):
        Superficie.blit(self.ImagenProyectil, self.rect)


class Coete(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenMisil = pygame.transform.scale(ImagenMisil, (30, 10))
        self.rect = self.ImagenMisil.get_rect()
        self.VelocidadDisparo = 6
        self.rect.right = posx
        self.rect.top = posy

    def trayectoriaMisil(self):
        self.rect.right = self.rect.right + self.VelocidadDisparo

    def dibujarMisil(self, Superficie):
        Superficie.blit(self.ImagenMisil, self.rect)


#clases enemigos
class Invasor(pygame.sprite.Sprite):
    def __init__(self, posx, posy,resistencia,ruta,dimensionA,dimensionB):
        pygame.sprite.Sprite.__init__(self)
        ImagenInvasor = pygame.image.load(ruta)
        self.ImagenInvasor =  pygame.transform.scale(ImagenInvasor,(dimensionA,dimensionB))
        self.rect = self.ImagenInvasor.get_rect()

        self.resitencia = resistencia

        self.ListaDisparo = []
        self.velocidad = 10

        self.rect.right = posx
        self.rect.top = posy

        self.rangoDisparo = 10
        self.conquista = False

        self.CambioDireccion = True
        self.contador=0

    def dibujar(self, Superficie):
        Superficie.blit(self.ImagenInvasor, self.rect)

    def AtaqueNavesEnemigas(self):
        if self.conquista == False:
            self.__ataque()
            if self.contador == 0 or self.contador ==1:
                if self.CambioDireccion == True:
                    self.__movimientoDiagonalAsendente()
                    if self.rect.top < 50:
                        self.CambioDireccion = False
                        self.contador = 1
                else:
                    self.rect.left = self.rect.left + self.velocidad
                    if self.rect.left > Ancho - 200:
                        self.contador = 2

            if self.contador == 2 or self.contador ==3:
                if self.CambioDireccion == False:
                    self.__movimientoDiagonalDesendente()
                    if self.rect.bottom > Alto - 40:
                        self.CambioDireccion = True
                        self.contador = 3
                else:
                    self.rect.left = self.rect.left + self.velocidad
                    if self.rect.left > Ancho - 200:
                        self.contador = 4

            if self.contador == 4:
                if self.CambioDireccion == True:
                    self.__movimientoRecta()

    def AtaqueNavesEnemigas3(self):
        if self.conquista == False:
            self.__ataque()
            if self.contador == 0 or self.contador ==1:
                if self.CambioDireccion == True:
                    self.__movimientoDiagonalAsendente()
                    if self.rect.top < 50:
                        self.CambioDireccion = False
                        self.contador = 1
                else:
                    self.rect.left = self.rect.left + self.velocidad
                    if self.rect.left > Ancho - 200:
                        self.contador = 2

            if self.contador == 2 or self.contador ==3:
                if self.CambioDireccion == False:
                    self.__movimientoDiagonalDesendente()
                    if self.rect.bottom > Alto - 40:
                        self.CambioDireccion = True
                        self.contador = 3
                else:
                    self.rect.left = self.rect.left + self.velocidad
                    if self.rect.left > Ancho - 200:
                        self.contador = 0


    def AtaqueNavesEnemigas2(self):
        if self.conquista == False:
            self.__ataque()
            if self.contador == 0 or self.contador ==1:
                if self.CambioDireccion == True:
                    self.__movimientoRecta()
                    if self.rect.top < 50:
                        self.CambioDireccion = False
                        self.contador = 1
                else:
                        self.contador = 2

            if self.contador == 2 or self.contador ==3:
                if self.CambioDireccion == False:
                    self.__movimientoDiagonalDesendente()
                    if self.rect.top > Alto+60:
                        self.CambioDireccion = True
                        self.contador = 3
                else:
                    self.contador = 0

    def __movimientoDiagonalDesendente(self):
            self.rect.left = self.rect.left - self.velocidad
            self.rect.bottom = self.rect.bottom + self.velocidad

    def __movimientoDiagonalAsendente(self):
        self.rect.left = self.rect.left - self.velocidad
        self.rect.bottom = self.rect.bottom - self.velocidad

    def __movimientoRecta(self):
        self.rect.bottom = self.rect.bottom - self.velocidad

    def __movimientoIzquierda(self):
        self.rect.bottom = self.rect.left-self.velocidad

    def __movimientoCaida(self):
        self.rect.right = Ancho
        self.rect.top= self.rect.top+self.velocidad

    def __ataque(self):
        if (randint(0,600) < self.rangoDisparo):
            self.__disparo()

    def __disparo(self):
        posx , posy = self.rect.center
        ProyectilEnemigo = Bala(posx ,posy ,"Imagen/bala_enemigo.png",False)
        self.ListaDisparo.append(ProyectilEnemigo)

    def getResistencia(self):
        return self.resitencia
    def setResistencia(self,x):
        self.resitencia = self.resitencia-x


class Asteroide(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.A1 = pygame.transform.scale(ImagenAsteroide1,(30,30))
        self.A2 = pygame.transform.scale(ImagenAsteroide2,(30,30))
        self.A3 = pygame.transform.scale(ImagenAsteroide3, (30, 30))
        self.A4 = pygame.transform.scale(ImagenAsteroide4, (30, 30))
        self.A5 = pygame.transform.scale(ImagenAsteroide5, (30, 30))
        self.A6 = pygame.transform.scale(ImagenAsteroide6, (30, 30))
        self.A7 = pygame.transform.scale(ImagenAsteroide7, (30, 30))
        self.A8 = pygame.transform.scale(ImagenAsteroide8, (30, 30))
        self.A9 = pygame.transform.scale(ImagenAsteroide9, (30, 30))
        self.A10 = pygame.transform.scale(ImagenAsteroide10, (30, 30))

        self.AG11 = pygame.transform.scale(ImagenAsteroideGigante1, (50, 50))

        self.ListaImagenes = [self.A1,self.A2,self.A3,self.A4,self.A5,self.A6,self.A7,self.A8,self.A9,self.A10]
        self.posimagen = 0
        self.asteroide = self.ListaImagenes[self.posimagen]
        self.rect = self.asteroide.get_rect()

        self.velocidad = 15
        self.CaidaProyectil = 25

        self.rect.right = posx
        self.rect.top = posy

        self.tiempodecambio = 1

    def trayectoriaAsteroide(self):
        self.rect.right = self.rect.right - self.velocidad

    def trayectoriaAsteroideG(self):
        self.rect.left = self.rect.left - 15

    def animacion(self, tiempo):
        #print("se imprime")
        self.trayectoriaAsteroide()
        if self.tiempodecambio < tiempo:
            self.posimagen += 1
            self.tiempodecambio +=1

            if self.posimagen > len(self.ListaImagenes)-1:
                self.posimagen = 0
    def dibujar(self, Superficie):
        self.asteroide = self.ListaImagenes[self.posimagen]
        Superficie.blit(self.asteroide, self.rect)

    def dibujarGigante(self,Superficie):
        Superficie.blit(self.AG11,self.rect)

def cargarEnemigos(Lista, orden):
    Lista.clear()
    incremento = 50
    if orden == 1:
        for x in range (1,20): #19 enemigos primer grupo
            enemigo = Invasor(Ancho+ incremento,Alto+ incremento,1,"Imagen/NaveEnemiga2.png",50,50)
            Lista.append(enemigo)
            incremento = incremento+ 50

    if orden ==2:
        for x in range(1, 50):  # 19 enemigos primer grupo
            enemigo = Invasor(Ancho - 50, Alto + incremento, 1,"Imagen/NaveEnemiga2.png",50,50)
            Lista.append(enemigo)
            incremento = incremento + 100

    if orden == 3:
        for i in range(10):
            x = random.randrange(Ancho, Ancho*2)
            y = random.randrange(0, Alto)
            asteroide = Asteroide(x, y)
            Lista.append(asteroide)

    if orden == 4:
        for i in range(20):
            x = random.randrange(Ancho, Ancho*2)
            y = random.randrange(0, Alto)
            asteroide = Asteroide(x, y)
            Lista.append(asteroide)
    if orden ==5:
        incremento = 50
        enemigo = Invasor(Ancho + incremento, Alto + incremento, 25,"Imagen/enemigo.png",250,100)
        Lista.append(enemigo)

def detenerJuego():
    for enemigo in ListaEnemigo:
        for disparo in enemigo.ListaDisparo:
            enemigo.ListaDisparo.remove(disparo)

        #enemigo.conquista = True

def SecuenciaAsteroides(tiempo,Animacion):
    if Animacion==True:
        MiFuente = pygame.font.SysFont("Arial", 18)
        texto = MiFuente.render("Peligro: Meteoritos", 9, (255, 255, 255))
        Ventana.blit(texto, (380, 15))

        for asteroide in ListaAsteroides:
            asteroide.animacion(tiempo)
            asteroide.dibujar(Ventana)
            if asteroide.rect.left < 0:
               y = random.randrange(0, Alto)
               x = random.randrange(Ancho+10, Ancho+50)
               asteroideNuevaposicion= Asteroide(x,y)
               ListaAsteroides.remove(asteroide)
               ListaAsteroides.append(asteroideNuevaposicion)
    else:
        if len(ListaAsteroides)>0:
            for asteroide in ListaAsteroides:
                asteroide.animacion(tiempo)
                asteroide.dibujar(Ventana)
                if asteroide.rect.left < -30:
                    ListaAsteroides.remove(asteroide)


def SecuenciaAsteroidesGigantes(Animacion,jugador):
    global GameOver
    if Animacion==True:
        for asteroide in ListaAsteroidesGigantes:
            asteroide.trayectoriaAsteroideG()
            asteroide.dibujarGigante(Ventana)
            #if asteroide.rect.colliderect(jugador.rect):
                #jugador.destruccion()
                #GameOver = False
            if asteroide.rect.left < -30:
               y = random.randrange(0, Alto)
               x = random.randrange(Ancho+10, Ancho+50)
               asteroideNuevaposicion= Asteroide(x,y)
               ListaAsteroidesGigantes.remove(asteroide)
               ListaAsteroidesGigantes.append(asteroideNuevaposicion)
    else:
        if len(ListaAsteroidesGigantes) > 0:
            for asteroide in ListaAsteroidesGigantes:
                asteroide.trayectoriaAsteroideG()
                asteroide.dibujarGigante(Ventana)
                if asteroide.rect.left < -30:
                    ListaAsteroidesGigantes.remove(asteroide)


def tiempo():  # desarrolla tiempo del juego
    global segundos
    global minutos
    global segundosReloj
    if segundosReloj == 59:
        segundosReloj = 0
        minutos += 1
        return tiempo()
    else:
        segundos += 1
        segundosReloj +=1
        time.sleep(1)
        return tiempo()

def Vida():
    global vida
    global GameOver
    if vida == 0:
        ImagenVida = pygame.image.load("Imagen/ProgressBar.png")
    if vida == 1:
        ImagenVida = pygame.image.load("Imagen/vida95.png")
    if vida == 2:
        ImagenVida = pygame.image.load("Imagen/vida70.png")
    if vida == 3:
        ImagenVida = pygame.image.load("Imagen/vida40.png")
    if vida == 4:
        ImagenVida = pygame.image.load("Imagen/vida5.png")
    if vida == 5:
        ImagenVida = pygame.image.load("Imagen/vida0.png")
        #GameOver = False
        vida=0

    progres= pygame.transform.scale(ImagenVida, (350, 30))
    Ventana.blit(progres, (10,10))

def Reloj():
    fuente = pygame.font.SysFont("Arial", 16)
    Reloj = str("Tiempo: " + str(minutos)+"  min" + ": " + str(segundosReloj)+" seg")
    mensaje = fuente.render(Reloj, 1, (255, 255, 255))
    Ventana.blit(mensaje, (940, 15))

def Score(Puntos):
    fuente = pygame.font.SysFont("Arial", 16)
    score = str("Score:  " + str(Puntos) + "   Ptos")
    mensaje1 = fuente.render(score, 1, (255, 255, 255))
    Ventana.blit(mensaje1, (750, 15))


#Crear hilo de ejecucion
hilo = threading.Thread(target = tiempo, args = ())
hilo.start()



def Space():
    global puntos
    global vida
    global control2
    control1=0
    control=0
    paso = 0
    control2 = 19
    pygame.init()

    pygame.display.set_caption("Proyect Zero")
    pygame.mixer.music.load("Musica/fondo1.mp3")
    pygame.mixer.music.play()

    ImagenFondo = pygame.image.load("Imagen/fondo.jpg")
    ImagenFondoPanel = pygame.image.load("Imagen/puntaje3.jpg")

    MiFuente = pygame.font.SysFont("Arial",60)
    texto = MiFuente.render("Termino El Juego",0,(120,100,40))


    jugador = Nave()
    cargarEnemigos(ListaEnemigo,1)
    cargarEnemigos(ListaAsteroidesGigantes, 3)
    cargarEnemigos(ListaAsteroides, 4)

    reloj = pygame.time.Clock()
    while True:
        reloj.tick(60)
        tiempo = pygame.time.get_ticks()/100 # Es utilizado para la animacion de la lluvia de meteoritos
        Ventana.fill((0,0,0))
        Ventana.blit(ImagenFondo,(0,0))
        Ventana.blit(ImagenFondoPanel,(0,0))

        if GameOver == True:
            Teclado = pygame.key.get_pressed()
            if Teclado[K_RIGHT]:
                jugador.movientoDerecha()
            if Teclado[K_LEFT]:
                jugador.movientoIzquierda()
            if Teclado[K_UP]:
                jugador.movientoArriba()
            if Teclado[K_DOWN]:
                jugador.movientoAbajo()

        for event in GAME_EVENTOS.get():
            if event.type == GAME_GLOBALS.QUIT:
                pygame.quit()
                sys.exit()
            if GameOver == True:
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:
                        x , y = jugador.rect.center
                        jugador.disparar(x ,y)

                    elif event.key == pygame.K_v:
                        x, y = jugador.rect.center
                        jugador.dispararMisil(x ,y)

        if len(jugador.ListaMisiles)>0:
            for x in jugador.ListaMisiles:
                x.dibujarMisil(Ventana)
                x.trayectoriaMisil()

                if x.rect.right > Ancho:
                    jugador.ListaMisiles.remove(x)

        if segundos >2 and segundos <14 and GameOver == True:
            control = 1

        if segundos ==15and GameOver == True :

            cargarEnemigos(ListaEnemigo, 2)

        if segundos >15 and segundos < 28 and GameOver == True :
            control = 2

        if segundos >=26 and segundos < 60 and GameOver == True :
            SecuenciaAsteroides(tiempo, True)

        if segundos >=56 and segundos < 70 and GameOver == True :
            SecuenciaAsteroides(tiempo, False)

        if segundos >=30 and segundos < 60 and GameOver == True :
            SecuenciaAsteroidesGigantes(True,jugador)

        if segundos >=60 and segundos < 70 and GameOver == True :
            SecuenciaAsteroidesGigantes(False,jugador)

        if segundos ==70 and GameOver == True :
            cargarEnemigos(ListaEnemigo, 1)
            cargarEnemigos(ListaAsteroides, 4)

        if segundos >70 and GameOver == True and paso == 0:
            control = 3
            if((len(ListaEnemigo)-1) == 0):
                paso = 1
                cargarEnemigos(ListaEnemigo, 5)

        if paso == 1 and GameOver==True:
            control = 3
            if ((len(ListaEnemigo) - 1) == 0):
                pass
                #GameOver = False










        if len(jugador.Listadisparos) > 0:
            for x in jugador.Listadisparos:
                x.dibujar(Ventana)
                x.trayectoria()

                if x.rect.right > Ancho:
                    jugador.Listadisparos.remove(x)
                for enemigo in ListaEnemigo:
                    if x.rect.colliderect(enemigo.rect):
                        if enemigo.getResistencia() == 0:
                            ListaEnemigo.remove(enemigo)
                            puntos = puntos+10
                            control2 -=1
                        else:
                            enemigo.setResistencia(1)
                        try:
                            jugador.Listadisparos.remove(x)
                        except ValueError as e:
                            print(e)


        if len(ListaEnemigo) > 0:
            for enemigo in ListaEnemigo[control1:control2]:
                if control == 1:
                    enemigo.AtaqueNavesEnemigas()
                if control == 2:
                    enemigo.AtaqueNavesEnemigas2()
                if control == 3:
                    enemigo.AtaqueNavesEnemigas3()

                enemigo.dibujar(Ventana)
                if enemigo.rect.colliderect(jugador.rect):
                    detenerJuego()
                    #jugador.destruccion()
                    # GameOver = False
                    vida = vida + 1

                if len(enemigo.ListaDisparo) > 0:
                    for x in enemigo.ListaDisparo:
                        x.dibujar(Ventana)
                        x.trayectoria()
                        if x.rect.colliderect(jugador.rect):

                            detenerJuego()
                            #jugador.destruccion()
                            # GameOver = False
                            vida = vida + 1

                        if x.rect.right < 0:
                            enemigo.ListaDisparo.remove(x)
                        else:
                            for disparo in jugador.Listadisparos:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.Listadisparos.remove(disparo)
                                    try:
                                        enemigo.ListaDisparo.remove(x)
                                    except ValueError as e:
                                        print(e)




        if GameOver == False:
            pygame.mixer.music.fadeout(3000)
            Ventana.blit(texto,(300,300))
        #Vida()
        jugador.dibujar(Ventana)
        Reloj()
        Score(puntos)
        pygame.display.update()

Space()

