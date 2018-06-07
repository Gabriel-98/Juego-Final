import pygame
from lib.configuracion_ventana import *

class Personaje(pygame.sprite.Sprite):
	def __init__(self, imagenes, usuario, movimientos):
		pygame.sprite.Sprite.__init__(self)
		self.imagenes = pygame.image.load(imagenes)
		self.usuario = usuario
		self.movimientos = movimientos
		self.movimientoActual = "movimientoDerecha"
		self.secuencia = SecuenciaImagenes(self.movimientos[self.movimientoActual])
	def hasNext(self):
		if self.secuencia.hasNext():
			return True
		return False
	def next(self):
		rect = self.secuencia.next()
		return self.imagenes.subsurface(rect).convert_alpha()
	def setMovimiento(self, movimiento):
		if movimiento in self.movimientos:
			self.movimientoActual = movimiento
			self.secuencia = SecuenciaImagenes(self.movimientos[self.movimientoActual])
		


class SecuenciaImagenes(object):
	def __init__(self, lista_rect):
		self.lista_rect = lista_rect
		self.id_rect = 0
	def hasNext(self):
		if self.id_rect < len(self.lista_rect):
			return True
		return False
	def next(self):
		while self.id_rect < len(self.lista_frecuencias) - 1 and self.lista_frecuencias[self.id_rect] < 1:
			self.id_rect += 1
		if self.id_rect < len(self.lista_frecuencias):
			self.lista_frecuencias[self.id_rect] -= 1
		return self.lista_rect[self.id_rect]

