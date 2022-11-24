# nome = str(input('Qual é seu nome? '))
# if nome == 'Arthur':
#    print('Que nome lindo você tem!!')
# else:
#   print('Seu nome é tão normal!')
# print('Bom dia, {}'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input("DIgite a segunda nota: "))
m = (n1 + n2) / 2
print(('A sua média foi {:.1f}'.format(m)))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
