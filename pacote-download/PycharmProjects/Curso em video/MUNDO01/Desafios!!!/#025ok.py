# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

n = str(input('Qual é seu nome completo? ')).strip()
s = 'SILVA' in n.upper()
print('Seu nome tem Silva? {}'.format(s))