# Crie um programa que leia um numero real qualquer pelo teclado e mostre a sua porção inteira.
# EX: Digite um numero:6.127
# O numero 6.127 tem a parte inteira 6.

import math

n = float(input('Digite um numero:'))

print('O numero digitado foi {} e sua poção inteira é {}'.format(n, math.trunc(n)))
