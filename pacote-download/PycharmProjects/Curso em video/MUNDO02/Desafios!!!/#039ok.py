# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# Se ele ainda vai se alistar ao seviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

atual = date.today().year
nascimento = int(input('Qual ano você nasceu? '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}')
if idade < 18:
    saldo = 18 - idade
    print(f'Você ainda não tem 18 anos. ainda faltam {saldo} para o alistamento')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')
elif idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
else:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos')
    ano = atual - saldo
    print(f'seu alistamento foi em {ano}')
