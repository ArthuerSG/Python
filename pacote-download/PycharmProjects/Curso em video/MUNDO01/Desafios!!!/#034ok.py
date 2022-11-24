# Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%.
s = int(input('Qual é o seu salário? '))
if s <= 1250:
    a = s + (s * 0.15)
    print(f'Seu salário era {s} e você teve um aumento de {a}')
else:
    a = s + (s * 0.1)
    print(f'Seu salário era {s} e você ganhou um aumento de {a}')
