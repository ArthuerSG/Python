### DataFrame

## Resumo
# É como se fosse uma tabela
# As colunas funcionam como "chaves de dicionario"
# As linhas funcionam "como listas"

## Funcionamento
# Temos um dataframe chamado vendas_df

# vendas_df['coluna_x']-> uma lista com os valores da coluna_x(em formato dataframe,é um dataframe com 1 coluna só)
# vendas df[0]-> pega a primeira linha do dataframe
# vendas_df[:3]-> pega até a linha de indice 3 do dataframe
# vendas_df[['coluna_x','coluna_y','coluna_z']]-> cria um novo dataframe com as colunas coluna_x,coluna_y e coluna_z
# vendas_df['coluna_x'][0]-> pega o item da 1ª linha da coluna coluna_x

## Vamos ler um arquivo real, com a Base de Dados de Vendas da Empresa "Contoso"

import pandas as pd

vendas_df = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';')
# pode pegar mais de uma
print(vendas_df['ID Cliente'])
# print (vendas_df[0]) Erro
# Se i indice da "lista" for 0 vai dá erro pq você sempre tem que pegar a partir do cabeçario até alguma linha Exemplo:
# print (vendas_df[:1]) Certo

# Você consegue pegar mais de uma coluna de uma vez
# Pra fazer isso você tem que passar uma lista
# Exemplo: print (vendas_df[['Numero da Vendas', 'Data da Venda', 'ID Produto'])
# Se você tiver trabalhando com uma base de dados que tenha muitas linhas e muitas colunas ele não vai exibir bonitinho, mas em outo formato
# Para pegar um linha especifica é só colocar print (vendas_df['ID Produtos][0])
#                     coluna   linha
# print (vendas_df['ID Produtos][0])


## Aplicação

# O 1 passo de toda Análise de Dados é você entender o que existe na sua base de dados
# Usaremos o .info() para isso
# vendas_df.info() ele mostra o resumo que caso a tabela for muito grande mostra tambem se é int,etc...

# Vamos criar então agora uma lista de Clientes
# lista_clientes = vendas_df['ID Clinete']
# print(lista_cliente)

# Vamos criar agora uma lista com os produtos e as quantidades de vendas dele, caso a gente queira analisar só os produtos(independente de data ou de cliente)
# lista_colunas = ['ID Produto', 'Quantidade Vendida', 'Quantidade Devolvida']
# produtos_quantidade = vendas_df[lista_colunas]
# print(produtos_quantidade)

# OBS: O nome que colocar na listas tem que ser exatamente o mesmo que está no documento

