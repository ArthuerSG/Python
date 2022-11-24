# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva outro número: '))
n3 = int(input('Escreva outro numero: '))
if n1 > n2 and n1 > n3:
    print('O número maior é {}'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O número maior é {}'.format(n2))
else:
    print('O número maior é {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('O número maior é {}'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O número maior é {}'.format(n2))
else:
    print('O número menor é {}'.format(n3))

