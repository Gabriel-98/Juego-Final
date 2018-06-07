from lib.configuracion_ventana import *
from lib.menus import *
from lib.escenarios import *
from lib.jugador import *

class Nivel(object):
	def __init__(self, nombre_nivel, siguiente_vista):
		eventos.addObserverTeclado(self)
		self.nombre_nivel = nombre_nivel
		self.siguiente_vista = siguiente_vista
		self.menuPausa = MenuPausa(self.nombre_nivel)
		self.menuControles = MenuControles(self.nombre_nivel)
		self.escenario = None
		self.jugador = Jugador(80,80)
		self.jugadores = pygame.sprite.Group()
		self.vista = self.nombre_nivel
		self.juegoGanado = False
		self.juegoPerdido = False
		self.pausa = False
		self.activo = False
	def iniciar(self):
		self.activo = True
		self.pausa = False
		self.juegoGanado = False
		self.juegoPerdido = False
		self.vista = self.nombre_nivel
		self.jugador.iniciar()
		self.jugadores.add(self.jugador)
	def finalizar(self):
		self.activo = False
		self.pausa = False
		self.juegoGanado = False
		self.juegoPerdido = False
	def updateTeclado(self, tecla):
		if self.activo:
			if tecla == botonPausa:
				self.pausa = not self.pausa
				if self.pausa:
					self.vista = "MenuPausa"
					self.menuPausa.iniciar()
	def ejecutarMenuPausa(self):
		self.vista = self.menuPausa.next()
		if self.vista != "MenuPausa":
			self.menuPausa.finalizar()
			if self.vista == "MenuPrincipal" or self.vista == "Salir":
				self.activo = False

	def actualizarPosicionJugador(self):
		ls = pygame.sprite.spritecollide(self.jugador, self.escenario.plataformas, False)
		for plataforma in ls:
			top1 = self.jugador.rect.top
			bottom1 = self.jugador.rect.bottom
			left1 = self.jugador.rect.x
			right1 = self.jugador.rect.x + self.jugador.rect.w
			top2 = plataforma.rect.top
			bottom2 = plataforma.rect.bottom
			left2 = plataforma.rect.x
			right2 = plataforma.rect.x + plataforma.rect.w
			if left2 <= right1 and right1 <= right2:
				if self.jugador.rectAnterior.x + self.jugador.rectAnterior.w <= left2:
					self.jugador.posX = left2 - (self.jugador.rect.w / 2)
			if left2 <= left1 and left1 <= right2:
				if self.jugador.rectAnterior.x >= right2:
					self.jugador.posX = right2 + (self.jugador.rect.w / 2)
			if top2 <= bottom1 and bottom1 <= bottom2:
				if self.jugador.rectAnterior.bottom <= top2:
					self.jugador.posY = ALTO - top2
			if top2 <= top1 and top1 <= bottom2:
				if self.jugador.rectAnterior.top >= bottom2:
					self.jugador.posY = ALTO - (bottom2 + self.jugador.rect.h)
			self.jugador.actualizarRect()
	def actualizar(self):
		if not self.pausa:
			self.jugador.update()
			self.actualizarPosicionJugador()
	def dibujar(self):
		self.escenario.draw()
		self.jugadores.draw(ventana)
	def next(self):
		#if self.pausa:
		#	self.ejecutarMenuPausa()
		#	self.dibujar()
		#else:

		if not self.pausa:
			self.actualizar()
		self.dibujar()

		if self.pausa:
			self.ejecutarMenuPausa()


		if self.activo:
			return self.nombre_nivel
		else:
			if self.juegoGanado:
				return self.siguiente_vista
			elif self.juegoPerdido:
				return "MenuPrincipal"
			else:
				return self.vista



class Nivel1(Nivel):
	def __init__(self):
		Nivel.__init__(self, "Nivel1", "Nivel2")
		self.escenario = Escenario1()
		#self.jugador



class Nivel2(Nivel):
	def __init__(self):
		Nivel.__init__(self, "Nivel2", "Nivel3")
		self.escenario = Escenario2()
	def next(self):
		self.actualizar()
		if self.activo:
			return "Nivel2"
		else:
			return "MenuPrincipal"
			return "Nivel3"

class Nivel3(Nivel):
	def __init__(self):
		Nivel.__init__(self, "Nivel3", "MenuPrincipal")
		self.escenario = Escenario3()
	def next(self):
		self.actualizar()
		if self.activo:
			return "Nivel3"
		else:
			return "MenuPrincipal"