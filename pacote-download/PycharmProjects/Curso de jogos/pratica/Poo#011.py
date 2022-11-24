class Cachorros:
    # Atributos
    def __init__(self, nome, cor_de_pelo, idade, tamanho):
        self.nome = nome
        self.cor_de_pelo = cor_de_pelo
        self.idade = idade
        self.tamanho = tamanho
    # Métodos
    def latir(self):
        print('AU AU')
    def corre(self):
        print(f'{self.nome} está correndo')
cachorro_1 = Cachorros('Tobby', 'marrom', 5, 'grande')

print(cachorro_1.nome)
print(cachorro_1.idade)
cachorro_1.idade = 8
print(cachorro_1.idade)
cachorro_1.latir()
cachorro_1.corre()

cachorro_2 = Cachorros('Max', 'Preto', 3, 'pequeno')
print(cachorro_2.tamanho)
