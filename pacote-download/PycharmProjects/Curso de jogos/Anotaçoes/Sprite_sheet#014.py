### Sprite sheet

# é uma imagem que contém todos os frames de uma animação

## Vantagens de se utilizar sprite sheets

# Trabalhar com apenas um arquivo contendo todas as imagens
# Ocupar menos espaço na memória
# Processamento fica mais rápido
# Game mais otimizado

## Organização

# Nas sprite sheets, os frames (o as imagens) estão visualmente organizadas em kinhas e coulunas
#  0,0 | 0,1 | 0,2 |linha 0
# -----|-----|-----|
#  1,0 | 1,1 | 1,2 |linha 1
# -----|-----|-----|
#  2,0 | 2,1 | 2,2 |linha 2
# colunas
#   0     1     2

## Como usar sprite sheets?
#                 32px
#                  |
#                -----
#               |     |
#     32--- 0,0 | 0,32| 0,64|linha 0
#      |   -----|-----|-----|
# 96px-|32- 32,0|32,32|32,64|linha 1
#      |   -----|-----|-----|
#     32--- 64,0|64,32|64,64|linha 2
#          colunas
#            0     1     2

# o primeiro frame é x = 0, y = 0 igual a tela começa a contar de cima
# o segundo frame sera x = 32, y = 0
# depende do tamanho do pixel da sua sprite sheet


