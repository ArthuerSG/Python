#  Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite um numero: '))
for c in range(1, 11):
    s = n * c
    print(f'{n} x {c} = {s}')
