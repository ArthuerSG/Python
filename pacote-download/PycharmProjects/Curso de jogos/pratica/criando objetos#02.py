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
# criando um retangulo 1(onde eu quero add),2(cor),3(onde na tela eu vou add, o comprimento e a altura do retangulo)
    pygame.draw.rect(tela, (255, 0, 0), (200, 300, 40, 50))
# criando um circulo quase a mesma coisa do retangulo, no ultimo parametro é o raio do circulo
    pygame.draw.circle(tela, (0, 0, 255), (300, 260), 40)
# criando uma linha no 3(cola onde a linha vai) 4(onde ela vai se encontrar) 5(a espessura)
    pygame.draw.line(tela, (255, 255, 0), (390, 0), (390, 600), 5)

# para o jogo sempre atualizar
    pygame.display.update()
