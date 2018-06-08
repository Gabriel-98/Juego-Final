from lib.configuracion_ventana import *
from lib.personaje import *
from lib.guerrero import *

class Enemigo(pygame.sprite.Sprite):
	def __init__(self, pos, personaje):
		pygame.sprite.Sprite.__init__(self)
		self.personaje = personaje
		self.personaje.setMovimiento("movimientoIzquierda")
		self.image = self.personaje.next()
		self.rect = self.image.get_rect()
		self.posX = pos[0]
		self.posY = pos[1]
		self.actualizarRect()
		self.rectAnterior = self.rect
		self.direccionHorizontal = "left"
		self.tiempo = pygame.time.get_ticks()
	def actualizarRect(self):
		self.rect.x = self.posX - (self.rect.w / 2)
		self.rect.y = ALTO - (self.posY + self.rect.h)
	def actualizarListaImagenes(self):
		movimiento = self.movimiento
		if self.direccionHorizontal == "left":
			self.personaje.setMovimiento(movimiento + "Izquierda")
		else:
			self.personaje.setMovimiento(movimiento + "Derecha")
	def actualizarMovimiento(self):
		if not self.personaje.hasNext():
			self.movimiento = "movimiento"
			self.actualizarListaImagenes()
	def move(self):
		self.actualizarMovimiento()
		tiempoActual = pygame.time.get_ticks()
		if tiempoActual >= self.tiempo + self.retardo:
			self.tiempo = tiempoActual
			if self.personaje.hasNext():
				self.image = self.personaje.next()
			self.actualizarPosicion()

class NPC(Enemigo):
	def __init__(self, pos):
		Enemigo.__init__(self, pos, PersonajeNPC())
		#self.movimiento = "movimiento"
	def move(self):
		pass
	def update(self):
		self.move()

class Lagarto(Enemigo):
	def __init__(self, pos):
		Enemigo.__init__(self, pos, PersonajeLagarto())
		self.retardo = 100
		self.rango = 200
		self.rangoTemp = 0
	def actualizarPosicion(self):
		self.rectAnterior = self.rect.copy()
		if self.rangoTemp >= self.rango:
			self.rangoTemp = 0
			if self.direccionHorizontal == "left":
				self.direccionHorizontal = "right"
			else:
				self.direccionHorizontal = "left"
		if self.direccionHorizontal == "left":
			self.posX -= 5
			self.rangoTemp += 5
		else:
			self.posX += 5
			self.rangoTemp += 5
		self.actualizarRect()
	def update(self):
		self.move()