casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestaçao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos', end='')
print(f' a prestação será de R${prestaçao:.2f}')
if prestaçao <= minimo:
    print('Empretimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')
