from lib.configuracion_ventana import *
from lib.Teclado import *

class MenuPrincipal(object):
	def __init__(self):
		eventos.addObserverTeclado(self)
		self.fondo = pygame.image.load("imagenes/FondoMenu.jpg")
		self.musicaFondo = pygame.mixer.Sound("sonidos/Musicamenu.wav")
		self.opcionJugar = OpcionMenu("imagenes/jugar1.png", "imagenes/jugar2.png", 400, 290)
		self.opcionControles = OpcionMenu("imagenes/controles1.png", "imagenes/controles2.png", 400, 360)
		self.opcionCreditos = OpcionMenu("imagenes/creditos1.png", "imagenes/creditos2.png", 400, 430)
		self.opcionSalir = OpcionMenu("imagenes/salir1.png", "imagenes/salir2.png", 400, 500)
		self.opciones = [self.opcionJugar, self.opcionControles, self.opcionCreditos, self.opcionSalir]
		self.vistas = ["Juego", "MenuControles", "MenuCreditos", "Salir"]
		self.idOpcion = 0
		self.activo = False
	def iniciar(self):
		self.activo = True
		self.musicaFondo.play(1000)
		for opcion in self.opciones:
			opcion.desactivarEstado()
		self.opciones[0].activarEstado()
		self.idOpcion = 0
	def finalizar(self):
		self.activo = False
		self.musicaFondo.stop()
		for opcion in self.opciones:
			opcion.desactivarEstado()
	def updateTeclado(self, tecla):
		if self.activo:
			if tecla == "up":
				self.idOpcion = (len(self.opciones) + self.idOpcion - 1) % len(self.opciones)
			elif tecla == "down":
				self.idOpcion = (self.idOpcion + 1) % len(self.opciones)
			elif tecla == "enter":
				self.activo = False
			for opcion in self.opciones:
				opcion.desactivarEstado()
			self.opciones[self.idOpcion].activarEstado()
	def draw(self):
		ventana.blit(self.fondo, [0,0])
		for opcion in self.opciones:
			opcion.draw()
	def next(self):
		self.draw()
		if self.activo:
			return "MenuPrincipal"
		else:
			return self.vistas[self.idOpcion]

class MenuControles(object):
	def __init__(self):
		eventos.addObserverTeclado(self)
		self.descripcionBotonIzquierda = DescripcionBoton(botonIzquierda, "", 100, 100)
		self.descripcionBotonDerecha = DescripcionBoton(botonDerecha, "", 100, 150)
		self.descripcionBotonSaltar = DescripcionBoton(botonSaltar, "", 100, 200)
		self.descripcionBotonDash = DescripcionBoton(botonDash, "", 100, 250)
		self.descripcionBotonGolpe1 = DescripcionBoton(botonGolpe1, "", 100, 300)
		self.descripcionBotonGolpe2 = DescripcionBoton(botonGolpe2, "", 100, 350)
		self.descripcionBotones = [self.descripcionBotonIzquierda, self.descripcionBotonDerecha, self.descripcionBotonSaltar,
									self.descripcionBotonSaltar, self.descripcionBotonDash,
									self.descripcionBotonGolpe1, self.descripcionBotonGolpe2]
		self.activo = False
	def iniciar(self):
		self.activo = True
	def finalizar(self):
		self.activo = False
	def updateTeclado(self, tecla):
		if self.activo:
			if tecla == "s":
				self.activo = False
	def draw(self):
		ventana.fill((255,125,0))
		for descripcionBoton in self.descripcionBotones:
			descripcionBoton.draw()
	def next(self):
		self.draw()
		if self.activo:
			return "MenuControles"
		else:
			return "MenuPrincipal"

class MenuCreditos(object):
	def __init__(self):
		eventos.addObserverTeclado(self)
		self.activo = False
	def iniciar(self):
		self.activo = True
	def finalizar(self):
		self.activo = False
	def updateTeclado(self, tecla):
		if self.activo:
			if tecla == "s":
				self.activo = False
	def draw(self):
		pass
	def next(self):
		self.draw()
		if self.activo:
			return "MenuCreditos"
		else:
			return "MenuPrincipal"

class OpcionMenu(object):
	def __init__(self, image_link1, image_link2, posX, posY):
		self.image1 = pygame.image.load(image_link1)
		self.image2 = pygame.image.load(image_link2)
		self.image = self.image1
		self.rect = self.image.get_rect()
		self.posX = posX
		self.posY = posY
	def activarEstado(self):
		self.image = self.image2
		self.rect = self.image.get_rect()
	def desactivarEstado(self):
		self.image = self.image1
		self.rect = self.image.get_rect()
	def draw(self):
		x = self.posX - (self.rect.w / 2)
		y = self.posY - self.rect.h
		ventana.blit(self.image, [x,y])

class DescripcionBoton(object):
	def __init__(self, tecla, link_texto, x, y):
		self.teclado = Teclado()
		self.tecla = tecla
		#self.imagenTexto = pygame.image.load(link_texto)
		self.x = x
		self.y = y
	def draw(self):
		self.teclado.drawKey(self.tecla, self.x, self.y)
		#ventana.blit(self.imagenTexto, [self.x+50, self.y])