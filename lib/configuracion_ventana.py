import pygame
from lib.Eventos import *
ANCHO = 800
ALTO = 600

pygame.init()
ventana = pygame.display.set_mode((ANCHO,ALTO))
eventos = Eventos()

botonIzquierda = "left"
botonDerecha = "right"
botonSaltar = "space"
botonDash = "d"
botonGolpe1 = "a"
botonGolpe2 = "s"
botonAtras = "s"
botonAceptar = "enter"