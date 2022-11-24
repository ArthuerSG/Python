#  Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for i in range(1, 6):
    pess = float(input(f'Peso da {i}ª pessoa: '))
    if i == 1:
        maior = pess
        menor = pess
    else:
        if pess > maior:
            maior = pess
        if pess < menor:
            menor = pess
print(f'O maior peso lido foi {maior}Kg')
print(f'O menor peso lido foi {menor}Kg')
