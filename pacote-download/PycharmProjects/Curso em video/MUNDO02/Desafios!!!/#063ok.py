#  Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

print('-' * 20)
print('Sequência Fibonacci')
print('-' * 20)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
c = 3
print('~' * 20)
print(f'{t1} → {t2}', end='')
while c <= n:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    c += 1
print(' → FIM')
print('~' * 20)
