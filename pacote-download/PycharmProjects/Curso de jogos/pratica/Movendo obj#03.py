# Primeiro sempre importa as bibliotecas nessessarias
import pygame
from pygame.locals import *
from sys import exit

# Segundo sempre usar esse codigo para o jogo rodar
pygame.init()

# Criar uma variavel da largura(x) e altura(y)
LARGURA = 640
ALTURA = 480
# cria uma variavel para o movimento do obj
x = LARGURA / 2
y = 0
# Para o obj ficar centrelizado no meio da tela tem: MEIO = LARGURA_TELA / 2 - LARGURA_OBJ / 2

# para criar a tela use esse codigo
tela = pygame.display.set_mode((LARGURA, ALTURA))
# para trocaar o nome do jogo
pygame.display.set_caption('JOGO')
# controlar a taxa de fps do jogo
relogio = pygame.time.Clock()

# Criar um loop para o jogo rodar e definir os seus eventos, exemplo:
# pular, andar, fechar janela, etc...
while True:
# add o relogio no loop
    relogio.tick(30)
# para "limpar a tela" e deixar o retangulo animado
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

# criando um retangulo 1(onde eu quero add),2(cor),3(onde na tela eu vou add(x,y), o comprimento e a altura do retangulo)
    pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
# para o retangulo voltar no inicio
    if y >= ALTURA:
        y = 0
# para alteral o valor das variaveis, serve tambem para alterar a velocidade do obj
    y = y + 5



# para o jogo sempre atualizar
    pygame.display.update()
