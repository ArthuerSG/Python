import pygame
from pygame.locals import *
from sys import exit
import os

pygame.init()


LARGURA = 640
ALTURA = 480

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Sprites')

sprite_sheet = pygame.image.load(os.path.join('zimboll parado.png')).convert_alpha()


PRETO = (0, 0, 0)

class Zimbol(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        for i in range(3):
            img = sprite_sheet.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32 * 3, 32 * 3))
            self.sprite_sheet.append(img)



    def update(self):
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (32 * 5, 32 * 5))


todas_sprites = pygame.sprite.Group()
zimbol = Zimbol()
todas_sprites.add(zimbol)

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