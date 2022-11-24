from math import trunc

n = float(input('Digite um numero:'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, trunc(n)))

### OU ###

n = float(input('Digite um numero:'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, int(n)))