distancia = float(input('Qual é a distancia de sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passaem será de R${:.2f}'.format(preço))
