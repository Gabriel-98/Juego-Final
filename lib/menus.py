from lib.configuracion_ventana import *

class MenuPrincipal(object):
	def __init__(self, eventos):
		self.eventos = eventos
		self.eventos.addObserverTeclado(self)
		self.fondo = pygame.image.load("imagenes/FondoMenu.jpg")
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
		for opcion in self.opciones:
			opcion.desactivarEstado()
		self.opciones[0].activarEstado()
	def finalizar(self):
		self.activo = False
	def updateTeclado(self, tecla):
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