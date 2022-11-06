import pandas as pd

# -----------------------------------------------------
# Lendo arquivo excel
dfClientes   = pd.read_excel('caso_estudo.xlsx', sheet_name = 'clientes')
dfLojas      = pd.read_excel('caso_estudo.xlsx', sheet_name = 'lojas')
dfProdutos   = pd.read_excel('caso_estudo.xlsx', sheet_name = 'produtos')
dfVendas     = pd.read_excel('caso_estudo.xlsx', sheet_name = 'vendas')
dfPagamentos = pd.read_excel('caso_estudo.xlsx', sheet_name = 'pagamentos')

dfClientes



# -----------------------------------------------------
# Análise Preliminar

"""
    sample -> Dados aleatórios
    head   -> 5 primeiros registros
    tail   -> 5 últimos registos
"""
dfClientes.sample(5)



# -----------------------------------------------------
# Descobriremos se existe algum dados nulo nesse data frame
# Para cada célula existe falso, e tiver algum nullo estaria verdadeiro.
dfClientes.isnull()



# -----------------------------------------------------
# primeiro está identificando quais registro são nulos e depois aplicando uma soma nesses dados.
dfClientes.isnull().sum()
# Na coluna id temos 0 dados nulos, porem nome, sexo, dt_nasc temos 4 dados NULL.



# -----------------------------------------------------
# T -> Transpor dados (girar) de linhas para colunas ou vice-versa;
# any() -> A função retornará True se algum item em um iterável for true, caso contrário, retornará False.
dfClientes.isnull().T.any()
# Para cada linha tem a informação se ele é null o não.



# -----------------------------------------------------
# Quais são esses registros?
dfClientes[dfClientes.isnull().T.any()]


dfLojas # saudavel

dfProdutos
# Como identificar se a coluna é numericco?
# dfProdutos.describe()



# -----------------------------------------------------
# Gera o boxplot completo
dfProdutos.boxplot(column = [ 'valor' ])



# -----------------------------------------------------
# Como identificar no registro o valor máximo apresentado?
dfProdutos[ dfProdutos.valor > 3_000_000 ]



# -----------------------------------------------------
# Gerando um boxplot retirando o produto com o maior valor
dfProdutos[dfProdutos.valor < 3_000_000].boxplot(column = ['valor'])



# -----------------------------------------------------
# Vamos verificar se o produto já foi vendido?
dfVendas[ dfVendas.id_produto == 10 ]
# Quantas vendas?
# dfVendas[ dfVendas.id_produto == 10 ].count()



dfVendas.isnull().sum() # saudavel


dfVendas.describe()
# Temos 1 à 1 000 clientes
# Temos 1 à 10 lojas
# Temos 1 à 10 produtos


dfPagamentos.isnull().sum() # saudavel


dfPagamentos.describe()
# Temos 1 à 2997.000000 vendas
