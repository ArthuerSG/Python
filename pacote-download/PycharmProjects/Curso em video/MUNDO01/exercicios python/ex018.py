from math import radians, sin, cos, tan
a = float(input('Digite o Ângulo que você deseja:'))
s = sin(radians(a))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a, s))
c = cos(radians(a))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, c))
t = tan(radians(a))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(a, t))