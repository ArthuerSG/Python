from random import shuffle
n1 = str(input('Primero aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
l = [n1, n2, n3, n4]
shuffle(l)
print('A ordem de apresentação será\n{}'.format(l))
