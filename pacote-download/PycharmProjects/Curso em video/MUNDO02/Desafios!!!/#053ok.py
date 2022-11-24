#  Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

f = str(input('Digite uma frase: '))
palavras = f.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, - 1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não pe um palíndromo!')
