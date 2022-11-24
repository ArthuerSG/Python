# Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um que ajude ele, lendo o nome deles e esvendo o nome do escolhido.
import random
n1 = input('Escreva seu nome:')
n2 = input('Escreva seu nome:')
n3 = input('Escreva seu nome:')
n4 = input('Escreva seu nome:')

l = [n1, n2, n3, n4]

e = random.choice(l)

print('O aluno ecolhido foi {}'.format(e))