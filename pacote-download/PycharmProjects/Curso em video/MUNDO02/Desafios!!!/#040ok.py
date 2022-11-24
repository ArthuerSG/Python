# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5,0: Reprovado
# Média entre 5,0 e 6,9: Recuperação
# Média entre 7,0 ou superior: Aprovado
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}')
if media < 5:
    print('REPOVADO')
elif media >= 5 and media <= 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
