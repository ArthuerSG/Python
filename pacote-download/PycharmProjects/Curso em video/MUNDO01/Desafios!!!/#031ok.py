# Desenvolva um programa que pergunte a distância de uma viagem em km.Calcule o preço da passagem, cobrando R$0,50 por km para a viagens de até 200km e R$0,45 para viagens mais longas.
distancia = float(input('Qual é a distancia de sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passaem será de R${:.2f}'.format(preço))
