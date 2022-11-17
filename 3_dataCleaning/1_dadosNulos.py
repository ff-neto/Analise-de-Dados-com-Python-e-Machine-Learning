import pandas as pd

# -----------------------------------------------------
# Lendo arquivo excel
dfClientes   = pd.read_excel('caso_estudo.xlsx', sheet_name = 'clientes')
dfLojas      = pd.read_excel('caso_estudo.xlsx', sheet_name = 'lojas')
dfProdutos   = pd.read_excel('caso_estudo.xlsx', sheet_name = 'produtos')
dfVendas     = pd.read_excel('caso_estudo.xlsx', sheet_name = 'vendas')
dfPagamentos = pd.read_excel('caso_estudo.xlsx', sheet_name = 'pagamentos')



# -----------------------------------------------------
# conferir as venda de um cliente
dfVendas[dfVendas.id_cliente == 264]


# Estar acessando uma localização do data Secience cliente em que a linha é 1 e a coluna é nome
dfClientes.loc[1, 'nome']



# -----------------------------------------------------
# Estar acessando uma localização do data Secience cliente em que a linha é 1 e a coluna é nome
# O faremos?
# Substituiremos as linhas, por aquelas linhas que tem dados nulos. 
# dfClientes.nome.isnull() -> Esse filtro vai buscar todas as linhas que tem dados nulos e a coluna nome do data frame clientes.
# Faremos com esse registro fique sem nome.
# O -> Outro.
# data -> informe que a pessoa tenha menos de 1 ano, para facilitar achar ela depois.

dfClientes.loc[dfClientes.nome.isnull(), 'nome'] = 'Sem nome'
dfClientes.loc[dfClientes.sexo.isnull(), 'sexo'] = 'O'
dfClientes.loc[dfClientes.dt_nasc.isnull(), 'dt_nasc'] = '1/1/2021'


# -----------------------------------------------------
# a localização do id 269 e 287 do data frame clientes
# : -> todas as colunas
dfClientes.loc[[269, 287], :]


# No Data Frame Cliente verifique se os dados são nulos ou não. E quando é aplicado uma soma nesse resultado.
dfClientes.isnull().sum()


# No Data Frame Lojas Produtos se os dados são nulos ou não. E quando é aplicado uma soma nesse resultado.
dfProdutos.isnull().sum()


# No Data Frame Lojas verifique se os dados são nulos ou não. E quando é aplicado uma soma nesse resultado.
dfLojas.isnull().sum()


# No Data Frame Vendas verifique se os dados são nulos ou não. E quando é aplicado uma soma nesse resultado.
dfVendas.isnull().sum()


# No Data Frame Pagamentos verifique se os dados são nulos ou não. E quando é aplicado uma soma nesse resultado.
dfPagamentos.isnull().sum()
