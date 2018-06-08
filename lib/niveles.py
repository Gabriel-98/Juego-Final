from lib.configuracion_ventana import *
from lib.menus import *
from lib.escenarios import *
from lib.jugador import *
from lib.enemigos import *
from lib.niveles import *

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
		self.enemigos = pygame.sprite.Group()
		self.vista = self.nombre_nivel
		self.juegoGanado = False
		self.juegoPerdido = False
		self.activo = False
	def iniciar(self):
		self.activo = True
		self.juegoGanado = False
		self.juegoPerdido = False
		self.vista = self.nombre_nivel
		self.jugador.iniciar()
		self.jugadores.add(self.jugador)
	def finalizar(self):
		self.activo = False
		self.juegoGanado = False
		self.juegoPerdido = False
	def updateTeclado(self, tecla):
		if self.activo:
			if tecla == botonPausa:
				if self.vista != "MenuPausa":
					self.vista = "MenuPausa"
					self.menuPausa.iniciar()
	def ejecutarMenuPausa(self):
		self.vista = self.menuPausa.next()
		if self.vista != "MenuPausa":
			self.menuPausa.finalizar()
			if self.vista == "MenuPrincipal" or self.vista == "Salir":
				self.activo = False
			elif self.vista == "MenuControles":
				pass
	def actualizarPosicionSprite(self, sprite):
		'''
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
		'''
		if sprite.posX <= 60:
			sprite.posX = 60
		ls = pygame.sprite.spritecollide(sprite, self.escenario.plataformas, False)
		for plataforma in ls:
			top1 = sprite.rect.top
			bottom1 = sprite.rect.bottom
			left1 = sprite.rect.x
			right1 = sprite.rect.x + sprite.rect.w
			top2 = plataforma.rect.top
			bottom2 = plataforma.rect.bottom
			left2 = plataforma.rect.x
			right2 = plataforma.rect.x + plataforma.rect.w
			if left2 <= right1 and right1 <= right2:
				if sprite.rectAnterior.x + sprite.rectAnterior.w <= left2:
					sprite.posX = left2 - ((sprite.rect.w / 2)+5)
			if left2 <= left1 and left1 <= right2:
				if sprite.rectAnterior.x >= right2:
					sprite.posX = right2 + (sprite.rect.w / 2)
			if top2 <= bottom1 and bottom1 <= bottom2:
				if sprite.rectAnterior.bottom <= top2:
					sprite.posY = ALTO - top2
			if top2 <= top1 and top1 <= bottom2:
				if sprite.rectAnterior.top >= bottom2:
					sprite.posY = ALTO - (bottom2 + sprite.rect.h)
			sprite.actualizarRect()
	def usuarioAtacaEnemigos(self):
		ls = pygame.sprite.spritecollide(self.jugador, self.enemigos, False)
		for enemigo in ls:
			if self.jugador.movimiento == "golpeSuave":
				enemigo.kill()
	def actualizar(self):
		self.jugador.update()
		self.actualizarPosicionSprite(self.jugador)
	def dibujar(self):
		self.escenario.draw()
		self.dibujarNivel()
		self.jugadores.draw(ventana)
	def actualizarNivel(self):
		pass
	def dibujarNivel(self):
		pass
	def next(self):
		if self.vista == self.nombre_nivel:
			self.actualizar()
			self.actualizarNivel()
		for enemigo in self.enemigos:
			self.actualizarPosicionSprite(enemigo)
		self.usuarioAtacaEnemigos()
		self.dibujar()

		if self.vista == "MenuPausa":
			self.ejecutarMenuPausa()
		elif self.vista == "MenuControles":
			self.ejecutarMenuControles()


		if self.activo:
			return self.nombre_nivel
		else:
			if self.juegoGanado:
				return self.siguiente_vista
			elif self.juegoPerdido:
				return "MenuPrincipal"
			else:
				return self.vista

class Prologo(Nivel):
	def __init__(self):
		Nivel.__init__(self, "Prologo", "MenuPrincipal")
		self.escenario = EscenarioPrologo()
		self.npc = NPC([700,40])
		self.lagartos = pygame.sprite.Group()
		self.todos = pygame.sprite.Group()
		self.todos.add(self.npc)
		self.crearLagartos()
	def crearLagartos(self):
		lagarto = Lagarto([450,40])
		self.enemigos.add(lagarto)
		self.todos.add(lagarto)
		lagarto = Lagarto([100,40])
		self.enemigos.add(lagarto)
		self.todos.add(lagarto)
		lagarto = Lagarto([750,40])
		self.enemigos.add(lagarto)
		self.todos.add(lagarto)
	def actualizarNivel(self):
		self.todos.update()
		self.enemigos.update()
		if len(self.enemigos) == 0:
			self.activo = False
			self.juegoGanado = True
	def dibujarNivel(self):
		self.todos.draw(ventana)

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