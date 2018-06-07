import pygame

class Eventos(object):
	def __init__(self):
		#self.teclas = {chr(x): False for x in range(97,123)}
		self.observadoresVentana = []
		self.observadoresTeclado = []
		self.observadoresMouse = []
		self.teclas = { pygame.K_a: "a",
						pygame.K_b: "b",
						pygame.K_c: "c",
						pygame.K_d: "d",
						pygame.K_e: "e",
						pygame.K_f: "f",
						pygame.K_g: "g",
						pygame.K_h: "h",
						pygame.K_i: "i",
						pygame.K_j: "j",
						pygame.K_k: "k",
						pygame.K_l: "l",
						pygame.K_m: "m",
						pygame.K_n: "n",
						pygame.K_o: "o",
						pygame.K_p: "p",
						pygame.K_q: "q",
						pygame.K_r: "r",
						pygame.K_s: "s",
						pygame.K_t: "t",
						pygame.K_u: "u",
						pygame.K_v: "v",
						pygame.K_w: "w",
						pygame.K_x: "x",
						pygame.K_y: "y",
						pygame.K_z: "z",
						pygame.K_KP0: "0",
						pygame.K_KP1: "1",
						pygame.K_KP2: "2",
						pygame.K_KP3: "3",
						pygame.K_KP4: "4",
						pygame.K_KP5: "5",
						pygame.K_KP6: "6",
						pygame.K_KP7: "7",
						pygame.K_KP8: "8",
						pygame.K_KP9: "9",
						pygame.K_LEFT: "left",
						pygame.K_RIGHT: "right",
						pygame.K_UP: "up",
						pygame.K_DOWN: "down",
						pygame.K_SPACE: "space",
						pygame.K_RETURN: "enter"}
		self.estadoTeclas = {self.teclas[key]: False for key in self.teclas}
	def addObserverVentana(self, observer):
		self.observadoresVentana.append(observer)
	def deleteObserverVentana(self, observer):
		if observer in self.observadoresVentana:
			self.observadoresVentana.remove(observer)
	def updateObserverVentana(self):
		for observer in self.observadoresVentana:
			observer.updateVentana()

	def addObserverTeclado(self, observer):
		self.observadoresTeclado.append(observer)
	def deleteObserverTeclado(self, observer):
		if observer in self.observadoresTeclado:
			self.observadoresTeclado.remove(observer)
	def updateObserverTeclado(self, tecla):
		for observer in self.observadoresTeclado:
			observer.updateTeclado(tecla)

	def addObserverMouse(self, observer):
		self.observadoresMouse.append(observer)
	def deleteObserverMouse(self, observer):
		if observer in self.observadoresMouse:
			self.observadoresMouse.remove(observer)
	def updateObserverMouse(self):
		for observer in self.observadoresMouse:
			observer.updateMouse()

	def key_get_pressed(self):
		teclas = pygame.key.get_pressed()
		for key in self.teclas:
			self.estadoTeclas[self.teclas[key]] = teclas[key]
		return self.estadoTeclas

	def read(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.updateObserverVentana()
			if event.type == pygame.KEYDOWN:
				if event.key in self.teclas:
					self.updateObserverTeclado(self.teclas[event.key])
			if event.type == pygame.MOUSEBUTTONDOWN:
				self.updateObserverMouse()