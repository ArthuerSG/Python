#  Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0
media_idade = 0
idade_velho = 0
nome_velho = ''
total_mulher_20 = 0

for p in range(1, 5):
    print('-'f'{p}ª PESSOA''-')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade

    if p == 1 and sexo == 'Mm':
        idade_velho = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > idade_velho:
        idade_velho = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher_20 += 1

media_idade = soma_idade / 4

print(f'A media de idade do grupo é de {media_idade} anos')
print(f'O homem mais velho tem {idade_velho} anos e se chama {nome_velho}')
print(f'O total de mulheres menores de 20 anos são {total_mulher_20}')
