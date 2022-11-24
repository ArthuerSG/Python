### Pandas e CSV

## Resumo
# Quase sempre quando formos "ler" um arquivo csv, vamos usar o pandas.É prático e bem eficiente.

## Funcionamento
# Formas mais básica: (muitas vezes não usaremos a forma mais básica)
# dataframe = pd.read_csv(arquivo_com_extensao)

## Vamos ler um arquivo real, com a Base de Dados de Vendaas da Empresa "Contoso"

import pandas as pd

# vendas_df = pd.read_csv('Contoso - Cadastro Produtos.csv')
# print(vendas_df)
vendas_df = pd.read_csv('Contoso - Vendas - 2017.csv', sep=';')
# ou vendas_df = pd.read_csv(r'C:\Users\arthu\PycharmProjects\Curso #\Pandas\Contoso - Vendas - 2017.csv', sep=';')
print(vendas_df)

# O que é um dataframe? dataframe é um obj do pandas que esencialmente é uma tabela então ele é uma tabela

# O 'r' que esta antes do arquivo é uma raw_string
# O que é uma raw_string? siginifica que ele é um texti bruto
# Normalmente quando passa o caminho no python coloca o 'r' antes

# Essas são as duas maneiras ou você garante que o arquivo ta na mesma pasta ou você coloca o caminho
