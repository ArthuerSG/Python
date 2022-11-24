# Escreva um program que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# -1 para binário
# -2 para octal
# -3 para hexadecimal
numero = int(input('Digite um numero: '))
print('''Escolha as opções a baixo para converte o seu numero
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
opcao = int(input('Escolha um das opções a cima: '))
if opcao == 1:
    print(f'{numero} convertido para BINÁRIO fica {bin(numero)[2:]}')
elif opcao == 2:
    print(f'{numero} convertido para OCTAL fica {oct(numero)[2:]}')
elif opcao == 3:
    print(f'{numero} convertido para HEXADECIMAL fica {hex(numero)[2:]}')
else:
    print('Opção invalida. Tente novamente.')

