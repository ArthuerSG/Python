# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

atual = date.today().year
maior = 0
menor = 0
for i in range(1, 8):
    nascimento = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    idade = atual - nascimento
    if idade <= 18:
        menor += 1
    else:
        maior += 1
print(f'Tivemos {maior} de pessoas maiores')
print(f'Tivemos {menor} de pessoas menores')
