from lib.configuracion_ventana import *
from lib.menus import *

class Game(object):
	def __init__(self):
		eventos.addObserverVentana(self)
		self.cerrar = False
		self.vista = "MenuPrincipal"
		#self.nivel = Nivel()
		self.menuPrincipal = MenuPrincipal()
		self.menuControles = MenuControles()
		self.menuCreditos = MenuCreditos()
		self.menuPrincipal.iniciar()
		# Vistas = "MenuPrincipal", "MenuControles", "MenuSonido, "MenuCreditos", "MenuPausa"
		# "Juego", "Tutorial"
	def updateVentana(self):
		self.cerrar = True
	def iniciarVistaActual(self):
		#if self.vista == "Juego":
		#	self.nivel
		if self.vista == "MenuPrincipal":
			self.menuPrincipal.iniciar()
		elif self.vista == "MenuControles":
			self.menuControles.iniciar()
		elif self.vista == "MenuCreditos":
			self.menuCreditos.iniciar()
	def next(self):
		if self.vista == "MenuPrincipal":
			self.ejecutarMenuPrincipal()
		elif self.vista == "MenuControles":
			self.ejecutarMenuControles()
		elif self.vista == "MenuCreditos":
			self.ejecutarMenuCreditos()
		elif self.vista == "Salir":
			self.cerrar = True
		pygame.display.update()
		#print(self.vista)
	def ejecutarMenuPrincipal(self):
		self.vista = self.menuPrincipal.next()
		if self.vista != "MenuPrincipal":
			self.menuPrincipal.finalizar()
			self.iniciarVistaActual()
	def ejecutarMenuControles(self):
		self.vista = self.menuControles.next()
		if self.vista != "MenuControles":
			self.menuControles.finalizar()
			self.iniciarVistaActual()
	def ejecutarMenuCreditos(self):
		self.vista = self.menuCreditos.next()
		if self.vista != "MenuCreditos":
			self.menuCreditos.finalizar()
			self.iniciarVistaActual()
	def ventanaActiva(self):
		return not self.cerrar