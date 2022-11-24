# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segunto segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Essas retas {r1:.1f}, {r2:.1f} e {r3:.1f} PODEM FORMAR um triângulo!')
else:
    print(f'Essas retas {r1:.1f}, {r2:.1f} e {r3:.1f} NÃO PODEM FORMA um triângulo!')
