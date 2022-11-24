# Ecreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensgem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

numero1 = int(input('Escreva um numero: '))
numero2 = int(input('Escreva outro numero: '))

if numero1 > numero2:
    print('O primeiro numero é maior!')
elif numero2 > numero1:
    print('O segundo numero é maior!')
else:
    print('Não existe valor maior, os dois são iguais!')
