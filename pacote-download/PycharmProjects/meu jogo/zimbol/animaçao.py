import pygame
from pygame.locals import *
from sys import exit

pygame.init()

LARGURA = 640
ALTURA = 480

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Sprites')

PRETO = (0, 0, 0)

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('zimboll parado/sprite_0.png'))
        self.sprites.append(pygame.image.load('zimboll parado/sprite_1.png'))
        self.sprites.append(pygame.image.load('zimboll parado/sprite_2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (96 * 5, 32 * 5))

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 315

class Cachorro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.append(pygame.image.load('cachorro.png'))
        self.atual = 0
        self.image = self[self.atual]
        self.image = pygame.transform.scale(self.image, (32, 32))

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 315

    def update(self):
            self.atual = self.atual + 0.2
            if self.atual >= len(self.sprites):
                self.atual = 0
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (96 * 5, 32 * 5))


todas_sprites = pygame.sprite.Group()
cachorro = Cachorro()
personagem = Personagem()
todas_sprites.add(personagem, cachorro)

imagem_fundo = pygame.image.load('cidade_fundo.jpg').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill(PRETO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    tela.blit(imagem_fundo, (0, 0))
    todas_sprites.draw(tela)
    todas_sprites.update()
    pygame.display.flip()
