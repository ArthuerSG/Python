# from math import factorial
# n = int(input('Digite um número para calcular se Fatorial: '))
# f = factorial(n)
# print(f'O fatorial de {n} é {f}.')

# OU sem modulo

n = int(input('Digite um número para calcular se Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}.')

### OBS : sempre que for usar fatorial e sempre que for multiplicar um numero por outro e ele se mantem é 1