from lib.personaje import *

class Guerrero(Personaje):
	def __init__(self, usuario):
		self.movimientos = {"movimientoIzquierda": [(0,0,80,80),(80,0,80,80),(170,0,70,80)],
							"movimientoDerecha": [(0,0,80,80),(80,0,80,80),(170,0,70,80)],
							"correrIzquierda": [(0,0,80,80),(80,0,80,80),(170,0,70,80)],
							"correrDerecha": [(0,0,80,80),(80,0,80,80),(170,0,70,80)],
							"saltarIzquierda": [(0,0,80,80)],
							"saltarDerecha": [(0,0,80,80)],
							"caerIzquierda": [(0,0,80,80)],
							"caerDerecha": [(0,0,80,80)]}
		Personaje.__init__(self, "imagenes/jugador.png", usuario, self.movimientos)