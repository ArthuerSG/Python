import pygame
from .locals import *
from sys import exit
from random import randint

.init()

LARGURA = 800
ALTURA = 700

x = (LARGURA / 2) - 100
y = (ALTURA / 2) - 40

x1 = (LARGURA / 2) + 100
y1 = (ALTURA / 2) - 40

tela = .display.set_mode((LARGURA, ALTURA))

.display.set_caption('Sua mãe')

PRETO = (0, 0, 0)

colidiu = False


def exibe_mensagem(msg, tamanho, cor):
    fonte = .font.SysFont('comicsansms', tamanho, True, False)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado

def reiniciar_jogo():
    global colidiu, x, y, x1, y1
    colidiu = False
    x = (LARGURA / 2) - 100
    y = (ALTURA / 2) - 40
    x1 = (LARGURA / 2) + 100
    y1 = (ALTURA / 2) - 40

relogio = .time.Clock()

while True:
    relogio.tick(30)
    tela.fill(PRETO)
    for event in .event.get():
        if event.type == QUIT:
            .quit()
            exit()

    if .key.get_pressed()[K_UP]:
        y1 -= 20
    if .key.get_pressed()[K_DOWN]:
        y1 += 20
    if .key.get_pressed()[K_RIGHT]:
        x1 += 20
    if .key.get_pressed()[K_LEFT]:
        x1 -= 20

    if .key.get_pressed()[K_w]:
        y -= 20
    if .key.get_pressed()[K_s]:
        y += 20
    if .key.get_pressed()[K_d]:
        x += 20
    if .key.get_pressed()[K_a]:
        x -= 20

    ret_vermelho = .draw.rect(tela, (255, 0, 0), (x, y, 60, 80))
    ret_azul = .draw.rect(tela, (0, 0, 255), (x1, y1, 60, 80))

    if ret_vermelho.colliderect(ret_azul):
        x = randint(40, 700)
        y = randint(50, 600)
        if colidiu == True:
            gamer_over = exibe_mensagem('GAMER OVER', 40, (0, 255, 0))
            tela.blit(gamer_over, ((LARGURA // 2) - 100, (ALTURA // 2) - 40))

    .display.update()
