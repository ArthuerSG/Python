# Faça um programa que leia 0 a 9999 e mostre na tela cada um dos digito separados

# Ex:
# Digite um numero:1834
# unidade:4
# dezenas:3
# centenas:8
# milhar:1

num = int(input('Digite um numero:'))
n = str(num)
print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))
