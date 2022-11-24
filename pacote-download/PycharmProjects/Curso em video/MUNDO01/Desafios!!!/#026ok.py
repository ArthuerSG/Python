# Faça um programa que leia frase pelo teclado e mostre:
# 1-Quantas vezes aparece a letra "A"
# 2-Em que posição ela aparece a primeira vez
# 3-Em que posição ela aprece a ultima vez

f = str(input('Escreva uma frase? ')).strip()
u = f.upper()
print('A letra A aparece {} vezes na frase'.format(u.count('A')))
print('A primeira letra A aparece na posição {}'.format(u.find('A')+1))
print('A última letra A aperece na posição {}'.format(u.rfind('A')+1))