print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
count = 1
while count <= 10:
    print(f'{termo} → ', end='')
    termo += razao
    count += 1
print('FIM')
