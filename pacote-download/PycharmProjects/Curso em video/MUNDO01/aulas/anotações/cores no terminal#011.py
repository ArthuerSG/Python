### CORES NO TERMINAL ###

#       Ansi
#  escape sequence
# todu dentro de Ansi começa com contra barra(\) e um codigo
# exemplo:
# \033[m
# entre o '[' e o 'm' é onde voce colocara o codigo
# esses codigos podem ser nehum codigo, 1 codigo, 2 codigos e 3 codigos
# o 1 codigo (o estilo da fonte), 2(texto) e o 3(cor de fundo) obs(todos opecionais e pode colocar na ordem que quiser
# exemplo:
# \033[0;33;44m
# style(estilo)         text(texto)         back(cor de fundo)
# 0 none                30     >branco<     40
# 1 bold                31    >vermelho<    41
# 4 underline           32     >verde<      42
# 7 negative            33    >amarelo<     43
#                       34     >azul<       44
#                       35     >roxo<       45
#                       36    >azul bb<     46
#                       37     >cinza<      47
# OBS(Só com o negative da para deixar em preto e branco)
