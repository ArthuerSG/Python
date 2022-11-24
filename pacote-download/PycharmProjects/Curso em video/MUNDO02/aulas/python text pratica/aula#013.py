# repetindo quantas vezes voce quiser
for c in range(0, 6):
    print('Oi')
print('FIM')
# contando de 0 a 6
for c in range(0, 7):
    print(c)
print('FIM')
# contando de 6 ate 0
for c in range(6, 0, -1):
    print(c)
print('FIM')
# contando 2 em 2
for c in range(0, 7, 2):
    print(c)
print('FIM')
# fazer uma contagem ate da sua escolha menos o ultimo numero
n = int(input('Digite um número: '))
for c in range(0, n):
    print(c)
print('FIM')
# fazer uma contagem ate da sua escolha ate mesmo o ultimo numero
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')
# fazer uma contagem de quando começa, o fim e enquantos vai pular
i = int(input('Incinio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f, p):
    print(c)
print('FIM')
# fazer a pessoal digitar quantas vezes você quiser
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')
#  fazer um somatario
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor:'))
    s += n
print('0 somatócio de todos os valores foi {}'.format(s))
