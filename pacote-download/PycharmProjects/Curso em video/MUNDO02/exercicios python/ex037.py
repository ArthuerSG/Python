num = int(input('Digite um numero inteiro:'))
print('''Escolha uma das bases para converção:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opçao = int(input('Sua opção: '))
if opçao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opçao == 2:
    print(f'{num} convertido para OCTAL é igul a {oct(num)[2:]}')
elif opçao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente!')
