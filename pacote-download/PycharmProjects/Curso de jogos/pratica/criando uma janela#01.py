# Primeiro sempre importa as bibliotecas nessessarias
import pygame
from pygame.locals import *
from sys import exit

# Segundo sempre usar esse codigo para o jogo rodar
pygame.init()

# Criar uma variavel da largura(x) e altura(y)
LARGURA = 640
ALTURA = 480

# para criar a tela use esse codigo
tela = pygame.display.set_mode((LARGURA, ALTURA))
# para trocaar o nome do jogo
pygame.display.set_caption('JOGO')

# Criar um loop para o jogo rodar e definir os seus eventos, exemplo:
# pular, andar, fechar janela, etc...
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
# para o jogo sempre atualizar
    pygame.display.update()
