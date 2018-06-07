from lib.configuracion_ventana import *
from lib.teclado import *

class MenuPrincipal(object):
	def __init__(self):
		eventos.addObserverTeclado(self)
		self.fondo = pygame.image.load("imagenes/FondoMenu.jpg")
		self.musicaFondo = pygame.mixer.Sound("sonidos/Musicamenu.wav")
		self.opcionJugar = OpcionMenu("imagenes/jugar1.png", "imagenes/jugar2.png", 430, 250)
		self.opcionControles = OpcionMenu("imagenes/controles1.png", "imagenes/controles2.png", 430, 310)
		self.opcionCreditos = OpcionMenu("imagenes/creditos1.png", "imagenes/creditos2.png", 430, 370)
		self.opcionSalir = OpcionMenu("imagenes/salir1.png", "imagenes/salir2.png", 430, 430)
		self.opciones = [self.opcionJugar, self.opcionControles, self.opcionCreditos, self.opcionSalir]
		self.vistas = ["Nivel1", "MenuControles", "MenuCreditos", "Salir"]
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
			if tecla == botonArriba:
				self.idOpcion = (len(self.opciones) + self.idOpcion - 1) % len(self.opciones)
			elif tecla == botonAbajo:
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
	def __init__(self, vistaSuperior):
		eventos.addObserverTeclado(self)
		self.vistaSuperior = vistaSuperior
		self.FondoMenu = pygame.image.load("imagenes/FondoMenu.jpg")
		self.imagenTitulo = pygame.image.load("imagenes/controles_menu.png")
		self.descripcionBotonIzquierda = DescripcionBoton(botonIzquierda, "imagenes/izquierda.png", (290,100), (360,100))
		self.descripcionBotonDerecha = DescripcionBoton(botonDerecha, "imagenes/derecha.png", (290,140), (360,140))
		self.descripcionBotonSaltar = DescripcionBoton(botonSaltar, "imagenes/saltar.png", (260,180), (360,180))
		self.descripcionBotonDash = DescripcionBoton(botonDash, "imagenes/dash.png", (290,220), (360,220))
		self.descripcionBotonGolpe1 = DescripcionBoton(botonGolpe1, "imagenes/golpe_suave.png", (290,260), (360,260))
		self.descripcionBotonGolpe2 = DescripcionBoton(botonGolpe2, "imagenes/golpe_fuerte.png", (290,300), (360,300))
		self.descripcionBotonPausa = DescripcionBoton(botonPausa, "imagenes/atras.png", (260,340), (360,340))
		self.descripcionBotonSeleccionar = DescripcionBoton(botonSeleccionar, "imagenes/seleccionar.png", (290,380), (360,380))
		self.descripcionBotonAtras = DescripcionBoton(botonAtras, "imagenes/atras.png", (290,420), (360,420))
		self.descripcionBotones = [self.descripcionBotonIzquierda, self.descripcionBotonDerecha,
									self.descripcionBotonSaltar, self.descripcionBotonDash,
									self.descripcionBotonGolpe1, self.descripcionBotonGolpe2, self.descripcionBotonPausa,
									self.descripcionBotonSeleccionar, self.descripcionBotonAtras]
		self.activo = False
	def iniciar(self):
		self.activo = True
	def finalizar(self):
		self.activo = False
	def updateTeclado(self, tecla):
		if self.activo:
			if tecla == botonAtras:
				self.activo = False
	def draw(self):
		ventana.blit(self.FondoMenu, (0,0))
		#ventana.fill((255,125,0))
		s = pygame.Surface([360,440])
		s.fill((0,0,0))
		s.set_alpha(150)
		ventana.blit(s, (250,0))
		#ventana.fill((255,125,0))
		ventana.blit(self.imagenTitulo, (260,30))
		for descripcionBoton in self.descripcionBotones:
			descripcionBoton.draw()
	def next(self):
		self.draw()
		if self.activo:
			return "MenuControles"
		else:
			return self.vistaSuperior

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
			if tecla == botonAtras:
				self.activo = False
	def draw(self):
		pass
	def next(self):
		self.draw()
		if self.activo:
			return "MenuCreditos"
		else:
			return "MenuPrincipal"

class MenuPausa(object):
	def __init__(self, vistaSuperior):
		eventos.addObserverTeclado(self)
		self.vistaSuperior = vistaSuperior
		self.textoTitulo = Texto("imagenes/pausa.png", (430,150))
		self.opcionReanudar = OpcionMenuPausa("imagenes/reanudar.png", (430,200))
		self.opcionControles = OpcionMenuPausa("imagenes/controles.png", (430,240))
		self.opcionMenuPrincipal = OpcionMenuPausa("imagenes/menu_principal.png", (430,280))
		self.opcionSalir = OpcionMenuPausa("imagenes/salir.png", (430,320))
		self.opciones = [self.opcionReanudar, self.opcionControles,
									self.opcionMenuPrincipal, self.opcionSalir]
		self.vistas = [self.vistaSuperior, "MenuControles", "MenuPrincipal", "Salir"]
		self.idOpcion = 0
		self.activoOpcion = False
		self.activo = False
	def iniciar(self):
		self.activo = True
		self.activoOpcion = False
		for opcion in self.opciones:
			opcion.desactivarEstado()
		self.opciones[0].activarEstado()
		self.idOpcion = 0
	def finalizar(self):
		self.activo = False
		self.activoOpcion = False
		for opcion in self.opciones:
			opcion.desactivarEstado()
	def updateTeclado(self, tecla):
		if self.activo:
			if tecla == botonArriba:
				self.idOpcion = (len(self.opciones) + self.idOpcion - 1) % len(self.opciones)
			elif tecla == botonAbajo:
				self.idOpcion = (self.idOpcion + 1) % len(self.opciones)
			elif tecla == botonSeleccionar:
				self.activo = False
				self.activoOpcion = True
		#	elif tecla == botonAtras or tecla == botonPausa:
		#		self.activo = False
			for opcion in self.opciones:
				opcion.desactivarEstado()
			self.opciones[self.idOpcion].activarEstado()
	def draw(self):
		self.textoTitulo.draw()
		for opcion in self.opciones:
			opcion.draw()
	def next(self):
		self.draw()
		if self.activo:
			return "MenuPausa"
		else:
			if self.activoOpcion:
				return self.vistas[self.idOpcion]
			return self.vistaSuperior

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

class OpcionMenuPausa(object):
	def __init__(self, image_link, pos):
		self.image = pygame.image.load(image_link)
		self.rect = self.image.get_rect()
		self.posX = pos[0]
		self.posY = pos[1]
		self.ancho = 300
		self.alto = 40
		self.color = (255,0,0)
		self.barra = pygame.Surface([self.ancho, self.alto])
		self.barra.fill(self.color)
		self.barraX = self.posX - (self.ancho / 2)
		self.barraY = self.posY - self.alto
		self.estado = False
	def activarEstado(self):
		self.estado = True
	def desactivarEstado(self):
		self.estado = False
	def draw(self):
		if self.estado:
			self.barra.set_alpha(200)
		else:
			self.barra.set_alpha(80)
		ventana.blit(self.barra, (self.barraX, self.barraY))

		x = self.posX - (self.rect.w / 2)
		y = self.posY - self.rect.h
		ventana.blit(self.image, [x,y])
		

class DescripcionBoton(object):
	def __init__(self, tecla, link_texto, posTecla, posTexto):
		self.teclado = Teclado()
		self.tecla = tecla
		self.imagenTexto = pygame.image.load(link_texto)
		self.posTecla = posTecla
		self.posTexto = posTexto
	def draw(self):
		self.teclado.drawKey(self.tecla, self.posTecla[0], self.posTecla[1])
		ventana.blit(self.imagenTexto, self.posTexto)

class Texto(object):
	def __init__(self, link_texto, pos):
		self.imagenTexto = pygame.image.load(link_texto)
		self.rect = self.imagenTexto.get_rect()
		self.x = pos[0] - (self.rect.w / 2)
		self.y = pos[1] - self.rect.h
	def draw(self): 
		ventana.blit(self.imagenTexto, [self.x, self.y])