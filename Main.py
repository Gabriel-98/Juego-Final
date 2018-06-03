from lib.Eventos import *
from lib.Game import *
from lib.configuracion_ventana import *

if __name__=='__main__':
	game = Game()
	while game.ventanaActiva():
		eventos.read()
		game.next()
