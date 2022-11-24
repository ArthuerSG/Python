# Quando a gente for criar algum obj em nosso codigo temos que entender um pouco de PLANO CARTESIANO
#                     y Eixo
#                     ^
#                     |
#                     |
#     2°Quadrante    4|
#      (-3,2)        3| 1°Quadrante
#         o----------2|   (2,1)
#         |          1|-----o
# --------------------|-----|---------> x
#    -4  -3  -2  -1  0|  1  2  3  4    Eixo
#             |     -1|        |
#             o------2|        |
#          (-2,-2)  -3|--------o
#       3°Quadrante -4|      (3,-3)
#                     |   4°Quadrante
# O PLANO CARTESIANO serve para indentificar onde eu quero o meu obj criado
#
# No pygame o Eixo x é representado pela largura da tela e o Eixo y é a altura
#     Eixo y ^
#            |
#            |
#            |
#            |
#            |----------------->
#           0               Eixo x
# Porem no pygame é invetido o Eixo x continua na horizontal mas o Eixo y ele vai para a vertical para baixo, Exemplo:
#            0   x_pos=3        x_pos=5     Eixo x
#             |------------------------------->
#             |      |             |
#             |      |             |
#             | (3,5)|        (5,5)|
#     y_pos=5 |------o-------------o
#             |      |             |
#             |      |             |
#    y_pos=8  | (3,8)|        (5,8)|
#             |------o-------------o
#             |
#     Eixo y  v
#
# O sistema de cor do pygame ele segui o sistema RGB(red,green,blue)
# COR = (R, G, B)
# 255 = MÁXIMO
# 0 = MÍNIMO
# Quando você quiser dar uma cor a um obj voce tem que detro dos parentese() colocar 3 variaveis Exemplo:
# (255,0,0) = Vermelho, (0,255,0) = Verde, (0,0,255) = Azul,
# (0,0,0) = Preto e (255,255,255) = Branco
#
#
