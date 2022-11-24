### Manipulando textos!!!

## Índices
# frase = arthur
# [a] [r] [t] [h] [u] [r]
#  0   1   2   3   4   5

## Fatiamento
#1
# print = frase[4]
# u

#2
# frase[1:4]
# rth
# Para o final sempre um a menos por exemplo a cima [1:4] foi do r[1] ao h[3]

#3
# frase[1:6:2]
# rhr                                                                        1   2   3   4   5
# Assim ele vai pulando ignoarando as casa que tiver na contagem. [1:6:2] = [r] [x] [h] [x] [r]

#4
# frase[:5]
# arthu
# É a mesma coisa do que frase[0:5], ele irá começar do 0 e acabar no 5

#5
# frase[1:]
#rthur
# Diferente do de cima ele faz oposto começa no [1] e vai até acabar (é bom usar quando você não sabe até que índece vai acabar)

#6
# frase [0::2]
# atu
# Ele vai começar do 0 e como nao fala até onde vai ele vai até o final, mas como tem o 2 ele vai pulando em 2 em 2 como pode ver no #3 ali em cima

## Análise
#1
# len(frase)                                     0   1   2   3   4   5
# mostraria as "caracteres" de frase que seria: [a] [r] [t] [h] [u] [r]

#2
# frase.count('r')
# Você esta pedindo para o programa contar quantas vezes apareceram a letra "r" minuscula ele irá te mostrar 2
# frase.count('r', 0, 5)
# Ele irá mostrar do 0 ao 4 entao seira 1 letra 'r'

#3
# frase.find('art')
# Ele irá te indicar onde começou o 'art' que seria no 0
# frase.find('android')
# Ele irá te mostrar -1 que significa que ele n encontrou a 'android', entao se der -1 é pq nao encotrou

#4
# 'art' in frase
# O operador 'in' vai esta perguntando se tem 'art' na frase então aparecera True

## Tranformação
#1
# frase.replace('arthur', 'Android')
# Ele irá procurar e substituir a palavra 'arthur' por 'Android'

#2
# frase.upper()
# Ele deixara tudo que nao estiver maiusculo em maiusculo

#3
# frase.lower()
# Faz ao contrario do upper deixando tudo em minusculo

#4
# frase.capitalize()
# Ele vai pegar todos os caracteres e jogar em minusculo e só o primeiro caractere ele vai joagar para maiusculo

#5
# frase.title()
# Ele vai analizar quantas palavras tem e vai fazer basicamente igual o capitalize só que com todas as palavras na frase exemplo: Arthur Sipioni Grasso

#6
# frase.strip()
# Ele irá remover todos os espaços inuteis do inicio e do fim, ai o 'a' voltara a ser o incio 0 novamente
# exemplo:
# [x] [x] [x] [a] [r] [t] [h] [u] [r] [x] [x]
# frase.rstrip()
# O 'r' de strip é rigth em ingles que seguinifica direita que removera os espaços so no final
# frase.lstrip()
# O 'l' de stip é o oposto, esquerda que só removera os espaços do inicio

#7
# frase.split()
# Ele pegara os espaços do meio e fará uma divisão, ao inves de continuar a contagem. Ele gerá uma lista de cada palavra na frase
# exemplo:
# arthur sipioni
# [a][r][t][h][u][r]  [s][i][p][i][o][n][i]
#  0  1  2  3  4  5    0  1  2  3  4  5  6
#        0                      1

## Junçao
# '-'.join(frase)
# Ele vai juntar cada palavra com str '-' colocado no inicio
# exemplo:
# [a][r][t][h][u][r][-][s][i][p][i][o][n][i]

### OBS:
# Se voce quiser printar o texta grande e ele estiver em outra linha é só colocar """ (3 aspas) assim pegará o texto todo
# exemplo:
# print(""" jkjkljlçjçljaçljfdljsçlfjdçljfaçsldfjçl
# lakdsjfçlasdjflksadjflajadfasdfasdfadsfasdfdsfasd
# açfjlkdsjfçaskjfdsjaçladfdafsdasfasfdfdsafdsfgfgs
# alsfjsdfjçlskdjfadsjfadfadfhçklashdfjshkjfhasjhjj""")

