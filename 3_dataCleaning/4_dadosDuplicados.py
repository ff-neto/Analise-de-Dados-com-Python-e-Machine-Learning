import pandas as pd

# -----------------------------------------------------
# Lendo arquivo excel
dfClientes   = pd.read_excel('caso_estudo.xlsx', sheet_name = 'clientes')
dfLojas      = pd.read_excel('caso_estudo.xlsx', sheet_name = 'lojas')
dfProdutos   = pd.read_excel('caso_estudo.xlsx', sheet_name = 'produtos')
dfVendas     = pd.read_excel('caso_estudo.xlsx', sheet_name = 'vendas')
dfPagamentos = pd.read_excel('caso_estudo.xlsx', sheet_name = 'pagamentos')


# -----------------------------------------------------
# Verificando se existe algum registro (nome) duplicado
dfClientes.nome.duplicated()



# Verificando se existe algum registro (nome) duplicado
# Aplicando uma soma
dfClientes.nome.duplicated().sum()
# 109 nomes duplicado


# Verificando se esses nomes duplicado são realmente dados duplicados
# Avaliar os dados duplicados
dfClientes[ dfClientes.nome.duplicated() ]


# Vamos ver o nome: Anna Melo
dfClientes[ dfClientes.nome == 'Anna Melo' ]
# Pela data de nascimento percebesse que são pessoas distintas


# Verificando se todo data Frame se tem algum registos distintos
# tem que verificar se tem alguma linha que se repete.
# E tem que aplicar uma soma nesse registro.
dfClientes.duplicated().sum()



# -----------------------------------------------------
# Verificando se todo data Frame se tem algum registos distintos
# tem que verificar se tem alguma linha que se repete.
# E tem que aplicar uma soma nesse registro.
# ---
# Eliminado a coluna id
# drop() -> retirar uma coluna ou linha e () coloca qual é a coluna/linha.
# Só que tem que referenciar o eixo dessa coluna
# axis = 0 -> se for 0 representa linha
# axis = 1 -> se for 1 representa coluna
dfClientes.drop('id', axis = 1).duplicated().sum()


# -----------------------------------------------------
# Está avaliando se existe algum nome de loja duplicado dentro do data frame Vendas
dfVendas.drop('id', axis = 1).duplicated().sum()


# Está avaliando se existe algum nome de produto duplicado dentro do data frame produtos
dfProdutos.produto.duplicated().sum()

# Está avaliando se existe algum nome de loja duplicado dentro do data frame lojas
dfLojas.cidade.duplicated().sum()


# verificando se apresenta dados de vendas
dfVendas.drop('id', axis = 1).duplicated().sum()


# Verificando esse dado dupliccado
# Está analizando o data frame vendas, aplicando filtro entre cocheite para os dados duplicados 
dfVendas[ dfVendas.drop('id', axis = 1).duplicated() ]



# -----------------------------------------------------
# analisando esse dado repetindo.
dfVendas[ (dfVendas.id_cliente == 559) & (dfVendas.id_loja == 2) & (dfVendas.id_produto == 5) ]


dfPagamentos.drop('id', axis = 1).duplicated().sum()
