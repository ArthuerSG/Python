# Crie um programa que leia o nome de uma cidade e diga se ela começa ou nãp com o nome 'SANTOS'
c = str(input('Qual cidade você nasceu? ')).strip()
s = c[:5].upper() in 'SANTO'
print(s)
