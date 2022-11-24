### Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m²
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
are = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, are))
tin = are / 2
print('Para pintar essa parede, você precisará de {}L de tinta'.format(tin))