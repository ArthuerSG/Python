frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aperece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A aperceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
