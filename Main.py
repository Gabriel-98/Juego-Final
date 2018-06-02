from lib.Eventos import *
from lib.Game import *

if __name__=='__main__':
	eventos = Eventos()
	game = Game(eventos)
	while game.ventanaActiva():
		eventos.read()
		game.next()
