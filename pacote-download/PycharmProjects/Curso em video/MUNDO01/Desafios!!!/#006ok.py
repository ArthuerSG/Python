### Crie um algoritmo que leia o seu dobro, triplo e a raiz quadrada
n = int(input('Digite um numero:'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}.\n A raiz quadrada de {} é igual a {:.2f}.'.format(n, t , n, r))