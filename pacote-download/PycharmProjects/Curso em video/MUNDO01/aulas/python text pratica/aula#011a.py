print('\033[1;31;43mOla mundo\033[m')
print('\033[30;mArthur Sipioni Grasso\033[m')

a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m!!!')

nome = 'Arthur'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

nome = 'Arthur'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amerelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
