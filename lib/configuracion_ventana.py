import pygame
from lib.eventos import *
ANCHO = 860
ALTO = 480

pygame.init()
ventana = pygame.display.set_mode((ANCHO,ALTO))
eventos = Eventos()

botonArriba = "up"
botonAbajo = "down"
botonIzquierda = "left"
botonDerecha = "right"
botonSaltar = "up"
botonDash = "e"
botonGolpe1 = "q"
botonGolpe2 = "w"
botonPausa = "enter"
botonSeleccionar = "q"
botonAtras = "w"