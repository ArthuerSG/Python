# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1-O nome com todas as letras maiusculas
# 2-O nome com todas minusculas
# 3-Quantas letras ao todo(sem considerar espaços)
# 4-Quantas letras tem o primeiro nome

n = input('Digite seu nome completo:').strip()
print(n.upper())
print(n.lower())
print(len(n) - n.count(' '))
print(n.find(' '))
