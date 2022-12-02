#   Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
v = 0
while True:
    j = int(input('Digite um número: '))
    c = randint(0, 10)
    tt = j + c
    t = ' '
    while t not in 'PI':
        t = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {j} e o computador {c}. Total de {tt}', end='')
    print('DEU PAR!' if tt % 2 == 0 else 'DEU ÍMPAR!')
    if t == 'P':
        if tt % 2 == 0:
            print('Você VENCEU!')
            v =+ 1
        else:
            print('Você PERDEU!')
            break
    elif t == 'I':
        if tt % 2 == 1:
            print('Você VENCEU!')
            v =+ 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAMER OVER! Você venceu {v} vezes.')

