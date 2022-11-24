nome = str(input('Qual é seu nome? '))
if nome == 'Arthur':
    print('Que nome bonito!!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nomde é bem popular no Brasil.')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia \033[4;34m{nome}\033[m!!!')
