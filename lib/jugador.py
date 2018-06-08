from lib.configuracion_ventana import *
from lib.personaje import *
from lib.guerrero import *

class Jugador(pygame.sprite.Sprite):
	def __init__(self, posX, posY):
		pygame.sprite.Sprite.__init__(self)
		self.personaje = Guerrero()
		#self.image = pygame.Surface([80,80])
		self.personaje.setMovimiento("movimiento")
		self.image = self.personaje.next()
		self.rect = self.image.get_rect()
		self.posX = posX
		self.posY = posY
		self.actualizarRect()
		self.rectAnterior = self.rect			# Almacenara la posicion vieja
		#self.image.fill((255,0,0))
		self.alturaSalto = 80
		self.varAlturaSalto = 0
		self.movimiento = "movimiento"
		self.nuevoMovimiento = "movimiento"
		self.direccionHorizontal = "right"
		self.activoMovimientoHorizontal = False
		self.activoSalto = False
		self.cambioDireccionHorizontal = False
		self.tiempo = pygame.time.get_ticks()
		self.retardo = 80						# velocidad normal
		self.retardo2 = 20						# velocidad alta
	def iniciar(self):
		eventos.addObserverTeclado(self)
	def finalizar(self):
		eventos.deleteObserverTeclado(self)
	def updateTeclado(self, tecla):
		if tecla == botonGolpeSuave:
			self.nuevoMovimiento = "golpeSuave"
		elif tecla == botonGolpeFuerte:
			self.nuevoMovimiento = "golpeFuerte"
		elif tecla == botonDash:
			self.nuevoMovimiento = "dash"
		elif tecla == botonSaltar:
			self.nuevoMovimiento = "saltar"
		else:
			self.nuevoMovimiento = "movimiento"
	def leerTeclasContinuas(self):
		teclas = eventos.key_get_pressed()
		if teclas[botonIzquierda]:
			if self.direccionHorizontal != "left":
				self.cambioDireccionHorizontal = True
			self.activoMovimientoHorizontal = True
			self.direccionHorizontal = "left"
		elif teclas[botonDerecha]:
			if self.direccionHorizontal != "right":
				self.cambioDireccionHorizontal = True
			self.activoMovimientoHorizontal = True
			self.direccionHorizontal = "right"
		else:
			self.activoMovimientoHorizontal = False
	def actualizarRect(self):
		self.rect.x = self.posX - (self.rect.w / 2)
		self.rect.y = ALTO - (self.posY + self.rect.h)
	#def actualizarPosicion(self):
	#	self.posX = self.rect.x + (self.rect.w / 2)
	#	self.posY = ALTO - (self.rect.y + self.h)
	def setRect(self, x, y):
		self.rect.x = x
		self.rect.y = y
		self.actualizarPosicion()
	def setPosicion(self, posX, posY):
		self.posX = posX
		self.posY = posY
		self.actualizarRect()
	def actualizarListaImagenes(self):
		movimiento = self.movimiento
		if self.direccionHorizontal == "left":
			self.personaje.setMovimiento(movimiento + "Izquierda")
		else:
			self.personaje.setMovimiento(movimiento + "Derecha")
	def actualizarPosicion(self):
		self.rectAnterior = self.rect.copy()
		if self.movimiento == "saltar":
			if self.varAlturaSalto >= 10:
				self.posY += 10
				self.varAlturaSalto -= 10
			else:
				self.posY += self.varAlturaSalto
				self.varAlturaSalto = 0
		else:
			self.posY -= 10
		if self.activoMovimientoHorizontal:
			if self.direccionHorizontal == "left":
				self.posX -= 10
			elif self.direccionHorizontal == "right":
				self.posX += 10
		self.actualizarRect()
	def actualizarMovimiento(self):
		self.activoSalto = True
		if not self.personaje.hasNext():
			self.movimiento = "movimiento"
			if self.nuevoMovimiento in ["golpeSuave", "golpeFuerte"]:
				self.movimiento = self.nuevoMovimiento
			elif self.activoMovimientoHorizontal:
				self.movimiento = "correr"
			self.actualizarListaImagenes()
			self.nuevoMovimiento = "movimiento"
		else:
			if self.movimiento == "saltar":
				if self.varAlturaSalto == 0:
					self.movimiento = "movimiento"
			elif self.movimiento == "correr":
				if self.nuevoMovimiento in ["golpeSuave", "golpeFuerte"]:
					self.movimiento = self.nuevoMovimiento
					self.actualizarListaImagenes()
				elif self.cambioDireccionHorizontal:
					self.actualizarListaImagenes()
					self.cambioDireccionHorizontal = False
			elif self.movimiento == "golpeFuerte":
				pass
			elif self.movimiento == "golpeSuave":
				pass
			elif self.movimiento == "dash":
				pass
			elif self.movimiento == "movimiento":
				self.movimiento = self.nuevoMovimiento
				if self.nuevoMovimiento in ["golpeSuave", "golpeFuerte"]:
					self.movimiento = self.nuevoMovimiento
					self.actualizarListaImagenes()
				if self.activoMovimientoHorizontal:
					self.movimiento = "correr"
					self.actualizarListaImagenes()

			if self.nuevoMovimiento == "saltar":
				self.activoSalto = True
				self.movimiento = "saltar"
				self.varAlturaSalto = self.alturaSalto
				self.actualizarListaImagenes()
			self.nuevoMovimiento = "movimiento"
	def move(self):
		self.leerTeclasContinuas()
		self.actualizarMovimiento()
		tiempoActual = pygame.time.get_ticks()
		if tiempoActual >= self.tiempo + self.retardo:
			self.tiempo = tiempoActual
			if self.personaje.hasNext():
				self.image = self.personaje.next()
			self.actualizarPosicion()
	def update(self):
		self.move()