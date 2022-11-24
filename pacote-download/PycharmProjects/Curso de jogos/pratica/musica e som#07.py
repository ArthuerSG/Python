# Primeiro sempre importa as bibliotecas nessessarias
import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Segundo sempre usar esse codigo para o jogo rodar
pygame.init()

# para controlar o valume(de 0 a 1)
pygame.mixer.music.set_volume(0.5)

# criar trilha sonora para o jogo (obs: para rodar com esse codigo a musica tem que estar na mesma pasta do codigo)
musica_fundo = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')

# para fazer a musica tocar(o -1 serve para fazer a musica tocar repetidamente)
pygame.mixer.music.play(-1)

# criando a varialvel do som da colissao(obs: tirando a musica do fundo tds os arquivos de musica tem que ser '.wav', caso contrario vai dar ERRO)
barulho_colissao = pygame.mixer.Sound('smw_coin.wav')
# para aumentar o barulho da colissao
barulho_colissao.set_volume(1)

# Criar uma variavel da largura(x) e altura(y)
LARGURA = 640
ALTURA = 480

# Para o obj ficar centrelizado no meio da tela tem: MEIO = LARGURA_TELA / 2 - LARGURA_OBJ / 2
# cria uma variavel para o movimento do obj
x = int((LARGURA / 2) - 30)
y = int((ALTURA / 2) - 40)

# toda vez que rodar esse codigo o obj vai escolher um lugar aleatorio para aparecer entre os numero que você escolher
x_azul = randint(40, 600)
y_azul = randint(50, 430)

# criando fonte do texto(1 a fonte que voce escolher, 2 tamanho, 3 texto em negrito, 4 texto em intalico
fonte = pygame.font.SysFont('arial', 40, True, True)
pontos = 0

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
# criar uma variavel para o texto aparecer na janela
    mensagem = f'Pontos: {pontos}'
# juntar a fonte com a variavel criada(1 o que voce juntar na fonte, 2 se voce quiser um texto mais pixelado(False) se nao (True), 3 cor
    texto_formatado = fonte.render(mensagem, False, (0, 255, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
# fazer o personagem se movimentar com alguma tecla do teclado(tem que estar dentro do for)
        '''if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20'''
# Aqui faz o mesmo que o de cima só que se eu clicar e precionar a tecla ele continua a se movimentar(fora do for)
    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20


# criando um retangulo 1(onde eu quero add),2(cor),3(onde na tela eu vou add(x,y), o comprimento e a altura do retangulo)
    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 50))
# criar um condiçao de colisão
    if ret_vermelho.colliderect(ret_azul):
# toda vez que o retangulo vermelho colidir com o zul, o azul irá sortiar um outro lugar
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
# fazer a variavel pontos receber quando os obj colidir
        pontos = pontos + 1
# fazendo sair o som quando os obj colidirem
        barulho_colissao.play()

# para exibir a mensagem(o texto que voce criou, posissao(x,y))
    tela.blit(texto_formatado, (430, 40))
# para o jogo sempre atualizar
    pygame.display.update()

