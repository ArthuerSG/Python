#  Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opcao = 0
while opcao != 5:
    print('''
[ 1 ] somar 
[ 2 ] multiplicar
[ 3 ] maior 
[ 4 ] novos números
[ 5 ] sair do programa
''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        print(n1 + n2)
    elif opcao == 2:
        print(n1 * n2)
    elif opcao == 3:
        if n1 > n2:
            print(n1)
        else:
            print(n2)
    elif opcao == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif opcao == 5:
        print('Finalizando')
    else:
        print('Opção invalida! Tente novamente!')
    print('Fim do progrma!!!')
