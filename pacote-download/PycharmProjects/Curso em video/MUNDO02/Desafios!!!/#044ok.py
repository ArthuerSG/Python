# Elabore um programa que calcule o valor a ser pago por um produto, considerando o ser preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
print('='*20, 'LOJAS AET', '='*20)
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO\n [ 1 ] à vista dinheiro/cheque\n [ 2 ] à vista cartão\n [ 3 ] 2x no cartão\n [ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    parcela_total = int(input('Quanta parcelas? '))
    parcela = total / parcela_total
    print(f'Sua compra será parcelada em {parcela_total}x de R${parcela:.2f} COM JUROS')
else:
    total = 0
    print('\033[4;7;31mOPÇÃO IVÁLIDA\033[m de pagamento. Tente novamente!')
print(f'Sua compra de R${preco:.2f}, vai custar {total}')
