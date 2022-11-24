### Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# OBS: US$ 1,00 = R$ 3,27
r = float(input('Quanto dinheiro você tem na sua carteira? R$'))
d = r / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(r, d))
