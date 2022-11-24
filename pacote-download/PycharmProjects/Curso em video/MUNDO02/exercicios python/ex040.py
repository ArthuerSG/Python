nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}')
if 7 > media >= 5:
    print('O aluno está em RECUPERAÇAO.')
elif media < 5:
    print('O aluno está REPROVADO.')
else:
    print('O aluno está APROVADO.')
