from lib.configuracion_ventana import *
from lib.menus import *
from lib.niveles import *

class Game(object):
	def __init__(self):
		eventos.addObserverVentana(self)
		self.cerrar = False
		self.vista = "Prologo"
		self.prologo = Prologo()
		self.nivel1 = Nivel1()
		self.nivel2 = Nivel2()
		self.nivel3 = Nivel3()
		self.menuPrincipal = MenuPrincipal()
		self.menuControles = MenuControles("Menu Principal")
		self.menuCreditos = MenuCreditos()
		self.prologo.iniciar()
	def updateVentana(self):
		self.cerrar = True
	def iniciarVistaActual(self):
		if self.vista == "MenuPrincipal":
			self.menuPrincipal.iniciar()
		elif self.vista == "Prologo":
			self.prologo.iniciar()
		elif self.vista == "Nivel1":
			self.nivel1.iniciar()
		elif self.vista == "Nivel2":
			self.nivel2.iniciar()
		elif self.vista == "Nivel3":
			self.nivel3.iniciar()
		elif self.vista == "MenuControles":
			self.menuControles.iniciar()
		elif self.vista == "MenuCreditos":
			self.menuCreditos.iniciar()
	def next(self):
		if self.vista == "MenuPrincipal":
			self.ejecutarMenuPrincipal()
		if self.vista == "Prologo":
			self.ejecutarPrologo()
		elif self.vista == "Nivel1":
			self.ejecutarNivel1()
		elif self.vista == "Nivel2":
			self.ejecutarNivel2()
		elif self.vista == "Nivel3":
			self.ejecutarNivel3()
		elif self.vista == "MenuControles":
			self.ejecutarMenuControles()
		elif self.vista == "MenuCreditos":
			self.ejecutarMenuCreditos()
		elif self.vista == "Salir":
			self.cerrar = True
		pygame.display.update()
	def ejecutarPrologo(self):
		print(self.vista)
		self.vista = self.prologo.next()
		if self.vista != "Prologo":
			self.prologo.finalizar()
			self.iniciarVistaActual()
	def ejecutarNivel1(self):
		self.vista = self.nivel1.next()
		if self.vista != "Nivel1":
			self.nivel1.finalizar()
			self.iniciarVistaActual()
	def ejecutarNivel2(self):
		self.vista = self.nivel2.next()
		if self.vista != "Nivel2":
			self.nivel2.finalizar()
			self.iniciarVistaActual()
	def ejecutarNivel3(self):
		self.vista = self.nivel3.next()
		if self.vista != "Nivel3":
			self.nivel3.finalizar()
			self.iniciarVistaActual()
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