### Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento
s = float(input('Qual é o salario do funcionario? R$'))
a = s + (s * 15 / 100)
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(s, a))
