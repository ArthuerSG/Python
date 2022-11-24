# Faça um programa que leia um angulo quelquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

import math
a = float(input('Digite o Ângulo que você deseja:'))
s = math.sin(math.radians(a))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a, s))
c = math.cos(math.radians(a))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, c))
t = math.tan(math.radians(a))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(a, t))