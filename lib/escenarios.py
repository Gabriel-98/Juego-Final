from lib.configuracion_ventana import *

class Escenario(object):
	def __init__(self, imagen_fondo, ancho, alto):
		self.fondo = pygame.image.load(imagen_fondo)
		self.plataformas = pygame.sprite.Group()
		self.ancho = ancho
		self.alto = alto
	def updateSprite(self):
		pass
	def draw(self):
		ventana.blit(self.fondo, [0,0])
		for plataforma in self.plataformas:
			plataforma.draw()

class EscenarioPrologo(Escenario):
	def __init__(self):
		Escenario.__init__(self, "imagenes/FondoPrologo.png", 860, 480)
		self.plataformas.add(Plataforma([0,440,860,40]))
		self.plataformas.add(PlataformaImagen("imagenes/caja.png", (300,390)))

class Escenario1(Escenario):
	def __init__(self):
		Escenario.__init__(self, "imagenes/FondoPrologo.png",860, 2000)
		self.plataformas.add(Plataforma([0,430,400,50]))
		self.plataformas.add(Plataforma([450,430,150,50]))
		self.plataformas.add(Plataforma([700,430,150,50]))
		self.plataformas.add(Plataforma([200,180,100,50]))
		self.plataformas.add(Plataforma([740,380,100,50]))
		self.plataformas.add(Plataforma([150,400,200,10]))

class Escenario2(Escenario):
	def __init__(self):
		Escenario.__init__(self, "imagenes/FondoPrologo.png", 860, 3000)
		self.plataformas.add(Plataforma([0,430,400,50]))
		self.plataformas.add(Plataforma([450,430,150,50]))
		self.plataformas.add(Plataforma([700,430,150,50]))
		self.plataformas.add(Plataforma([200,180,100,50]))

class Escenario3(Escenario):
	def __init__(self):
		Escenario.__init__(self, "imagenes/FondoPrologo.png", 860, 2000)
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

class PlataformaImagen(pygame.sprite.Sprite):
	def __init__(self, link_imagen, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("imagenes/caja.png")
		self.rect = self.image.get_rect()
		self.rect.x = pos[0]
		self.rect.y = pos[1]
	def draw(self):
		ventana.blit(self.image, [self.rect.x, self.rect.y])
	def update(self):
		pass