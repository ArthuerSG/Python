#  Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

com = randint(0, 10)
acertou = False
tentativas = 0

while not acertou:
    tentativas += 1
    j = int(input('Em que numero eu pensei? '))
    if j == com:
        acertou = True
    else:
        if j < com:
            print('Mais... tente novamente: ')
        else:
            print('Menos... tente novamente: ')

print(f'Acertou! com {tentativas} tentativas. Parabéns!')
