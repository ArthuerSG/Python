
# Escreva um programa que faça o computador 'pensar' em um numero inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
com = random.randint(0, 5)
j = int(input('Em que numero eu pensei? '))
if j == com:
    print('Você venceu!')
else:
    print("Ganhei, eu pensei no número {} e não no {}".format(com, j))
