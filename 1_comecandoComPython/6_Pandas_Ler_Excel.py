import pandas as pd

# -----------------------------------------------------
dados_pessoas = pd.read_excel('dados.xlsx', sheet_name='pessoas')
dados_notas = pd.read_excel('dados.xlsx', sheet_name='notas')


# -----------------------------------------------------
# dentro da variavel notas, a coluna nome é a variavel chave,
# que está fazendo um join com data frame dados pessoas, informando que o nome é a chave.
dados_todos = dados_notas.set_index('nome').join(dados_pessoas.set_index('nome'))


# -----------------------------------------------------
# Esté fazendo um agrupamento por nome com dados_todos
# define qual a coluna que exibe o resultado. Nota
medias = dados_todos.groupby('nome').nota.mean()


# -----------------------------------------------------
# A máxima nota de cada pessoas
maxima = dados_todos.groupby('nome').nota.max()
maxima


# -----------------------------------------------------
# Salvar os dados em excel.
medias.to_excel('saida.xlsx')
