import os
import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()
pygame.mixer.init()

LARGURA = 500
ALTURA = 800

diretorio_principal = os.path.dirname(__file__)
IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png'))),
]
diretorio_sons = os.path.join(diretorio_principal, 'sons')

som_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'sons_death_sound.wav'))
som_colisao.set_volume(1)

som_pontuacao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'sons_score_sound.wav'))
som_pontuacao.set_volume(1)

colidiu = False

velocidade_jogo = 10

tela = pygame.display.set_mode((LARGURA, ALTURA))


def exibe_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont('comicsansms', tamanho, True, False)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado


def reiniciar_jogo():
    global pontos, velocidade_jogo, colidiu
    pontos = 0
    velocidade_jogo = 10
    colidiu = False
    Passaro.rect.y = ALTURA - 64 - 96 // 2
    Passaro.pulo = False
    Cano.rect.x = LARGURA


class Passaro:
    IMGS = IMAGENS_PASSARO
    # animações da rotação
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):

        self.som_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons, 'sons_jump_sound.wav'))
        self.som_pulo.set_volume(1)
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]
        self.pos_y_inicial = ALTURA - 64 - 96 // 2
        self.rect.center = (100, ALTURA - 64)

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        # calcular o deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo ** 2) + self.velocidade * self.tempo

        # restringir o deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

        # o angulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO

    def desenhar(self, tela):
        # definir qual imagem do passaro vai usar
        self.contagem_imagem += 1

        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem >= self.TEMPO_ANIMACAO * 4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

        # se o passaro tiver caindo eu não vou bater asa
        if self.angulo <= -80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO * 2

        # desenhar a imagem
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)


class Cano:
    DISTANCIA = 200
    VELOCIDADE = 5

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True)
        self.CANO_BASE = IMAGEM_CANO
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(50, 450)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
        self.pos_base = self.altura + self.DISTANCIA

    def mover(self):
        self.x -= self.VELOCIDADE

    def desenhar(self, tela):
        tela.blit(self.CANO_TOPO, (self.x, self.pos_topo))
        tela.blit(self.CANO_BASE, (self.x, self.pos_base))

    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.CANO_TOPO)
        base_mask = pygame.mask.from_surface(self.CANO_BASE)

        distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y))
        distancia_base = (self.x - passaro.x, self.pos_base - round(passaro.y))

        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)
        base_ponto = passaro_mask.overlap(base_mask, distancia_base)

        if base_ponto or topo_ponto:
            return True
        else:
            return False

class Chao:
    VELOCIDADE = 5
    LARGURA = IMAGEM_CHAO.get_width()
    IMAGEM = IMAGEM_CHAO

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.LARGURA

    def mover(self):
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE

        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x2 + self.LARGURA
        if self.x2 + self.LARGURA < 0:
            self.x2 = self.x1 + self.LARGURA

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x1, self.y))
        tela.blit(self.IMAGEM, (self.x2, self.y))


def desenhar_tela(tela, passaros, canos, chao, pontos):
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    for passaro in passaros:
        passaro.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela)

    tela.blit(exibe_mensagem, (LARGURA - 10 - exibe_mensagem.get_width(), 10))
    chao.desenhar(tela)
    pygame.display.update()



passaro = [Passaro(230, 350)]
chao = Chao(730)
canos = [Cano(700)]
tela = pygame.display.set_mode((LARGURA, ALTURA))
pontos = 0
relogio = pygame.time.Clock()

rodando = True


rodando = True
while rodando:
    relogio.tick(30)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            pygame.quit()
            exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and colidiu == False:
                if passaro.rect.y != passaro.pos_y_inicial:
                    pass
                else:
                    passaro.pular()
            for passaro in passaro:
                passaro.pular()
        if evento.key == K_r and colidiu == True:
            reiniciar_jogo()

    for passaro in passaro:
        passaro.mover()
    Chao.mover()

    adicionar_cano = False
    remover_canos = []
    for cano in cano:
        for i, passaro in enumerate(passaro):
            if cano.colidir(passaro):
                passaro.pop(i)
            if not cano.passou and passaro.x > cano.x:
                cano.passou = True
                adicionar_cano = True
        cano.mover()
        if cano.x + cano.CANO_TOPO.get_width() < 0:
            remover_canos.append(cano)

    colisoes = pygame.collide(passaro, cano, False, pygame.collide_mask)

    if adicionar_cano:
        pontos += 1
        cano.append(Cano(600))
    for cano in remover_canos:
        cano.remove(cano)

    for i, passaro in enumerate(passaro):
        if (passaro.y + passaro.imagem.get_height()) > Chao.y or passaro.y < 0:
            passaro.pop(i)

    if colisoes and colidiu == False:
        som_colisao.play()
        colidiu = True

    if colidiu == True:
        if pontos % 100 == 0:
            pontos += 1
        gamer_over = exibe_mensagem('GAMER OVER', 40, (0, 0, 0))
        tela.blit(gamer_over, ((LARGURA // 2) - 150, (ALTURA // 2) - 50))
        restart = exibe_mensagem('Pressione r para reiniciar', 20, (0, 0, 0))
        tela.blit(restart, ((LARGURA // 2) - 150, (ALTURA // 2)))

    else:
        pontos += 1
        passaro.update()
        texto_pontos = exibe_mensagem(pontos, 40, (0, 0, 0))

    if pontos % 100 == 0:
        som_pontuacao.play()
        if velocidade_jogo >= 30:
            velocidade_jogo += 0
        else:
            velocidade_jogo += 1

        print(velocidade_jogo)

    tela.blit(texto_pontos, (520, 30))

    desenhar_tela(tela, passaro, cano, Chao, pontos)

    pygame.display.flip()



