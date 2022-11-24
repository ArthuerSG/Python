# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Quanto anos você pretende quitar essa casa? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar a casa de {casa:.2f} em {anos:.2f} anos a prestaçao sera de {prestacao:.2f}')
if salario <= minimo:
    print('Seu emprestimo pode ser concedido!')
else:
    print('NEGADO!!!')


