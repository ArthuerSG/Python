# Faça um programa que leia o nome de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
# Ex:Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
