from lib.configuracion_ventana import *

class Escenario(object):
	def __init__(self):
		self.fondo = pygame.image.load("imagenes/FondoMenu.jpg")
		self.plataformas = pygame.sprite.Group()
	def updateSprite(self):
		pass
	def draw(self):
		ventana.blit(self.fondo, [0,0])
		for plataforma in self.plataformas:
			plataforma.draw()

class Escenario1(Escenario):
	def __init__(self):
		Escenario.__init__(self)
		self.plataformas.add(Plataforma([0,430,400,50]))
		self.plataformas.add(Plataforma([450,430,150,50]))
		self.plataformas.add(Plataforma([700,430,150,50]))
		self.plataformas.add(Plataforma([200,180,100,50]))
		self.plataformas.add(Plataforma([740,380,100,50]))
		self.plataformas.add(Plataforma([150,400,200,10]))

class Escenario2(Escenario):
	def __init__(self):
		Escenario.__init__(self)
		self.plataformas.add(Plataforma([0,430,400,50]))
		self.plataformas.add(Plataforma([450,430,150,50]))
		self.plataformas.add(Plataforma([700,430,150,50]))
		self.plataformas.add(Plataforma([200,180,100,50]))

class Escenario3(Escenario):
	def __init__(self):
		Escenario.__init__(self)
		self.plataformas.add(Plataforma([0,430,400,50]))
		self.plataformas.add(Plataforma([450,430,150,50]))
		self.plataformas.add(Plataforma([700,430,150,50]))
		self.plataformas.add(Plataforma([200,180,100,50]))

class Plataforma(pygame.sprite.Sprite):
	def __init__(self, rect):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([rect[2],rect[3]])
		self.rect = self.image.get_rect()
		self.rect.x = rect[0]
		self.rect.y = rect[1]
		self.image.fill((0,255,0))
	def draw(self):
		ventana.blit(self.image, [self.rect.x, self.rect.y])
	def update(self):
		pass

