from lib.configuracion_ventana import *
from lib.menus import *

class Game(object):
	def __init__(self, eventos):
		self.eventos = eventos
		self.eventos.addObserverVentana(self)
		self.cerrar = False
		self.vista = "MenuPrincipal"
		self.menuPrincipal = MenuPrincipal(self.eventos)
		self.menuPrincipal.iniciar()
		# Vistas = "MenuPrincipal", "MenuControles", "MenuSonido, "MenuCreditos", "MenuPausa"
		# "Juego", "Tutorial"
	def updateVentana(self):
		self.cerrar = True
	def next(self):
		if self.vista == "MenuPrincipal":
			self.ejecutarMenuPrincipal()
		pygame.display.update()
	def ejecutarMenuPrincipal(self):
		self.vista = self.menuPrincipal.next()
		if self.vista == "MenuPrincipal":
			pass
		else:
			self.menuPrincipal.finalizar()
	def ventanaActiva(self):
		return not self.cerrar