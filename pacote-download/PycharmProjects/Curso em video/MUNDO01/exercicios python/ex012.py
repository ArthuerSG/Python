p = float(input('Qual é o preço do produto? R$'))
d = p - (p * 5 / 100)
print('O produto custava {:.2f}, na promoção com 5% de desconto vai custar {:.2f}'.format(p, d))