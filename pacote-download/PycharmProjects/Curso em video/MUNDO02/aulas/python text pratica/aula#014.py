'''for c in range(1, 10):
    print(c)
print("FIM")

c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')

for c in range(1, 5):
    n = int(input('Digite um valor: '))
print("FIM")

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print("FIM")

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('FIM')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímares!')
