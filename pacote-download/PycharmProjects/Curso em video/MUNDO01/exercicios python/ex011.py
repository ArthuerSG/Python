larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
are = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, are))
tin = are / 2
print('Para pintar essa parede, você precisará de {}L de tinta'.format(tin))