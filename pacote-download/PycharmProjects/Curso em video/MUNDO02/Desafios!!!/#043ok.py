# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre se status, de acordo com a tabela abixo:
# Abaixo de 18,25: Abaixo do peso
# Entre 18,5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida
peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
print(f'Seu peso é {peso:.1f} e sua altura {altura:.1f} com isso seu imc fica {imc:.1f}')
