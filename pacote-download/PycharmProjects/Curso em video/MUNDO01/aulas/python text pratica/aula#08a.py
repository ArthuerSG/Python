import math
n = int(input('Digite um numero:'))
r = math.sqrt(n)
print(('A raiz de {} é igual a {}'.format(n, math.ceil(r))))

### OU ###

from math import sqrt, floor
n = int(input('Digite um numero:'))
r = sqrt(n)
print(('A raiz de {} é igual a {}'.format(n, floor(r))))

