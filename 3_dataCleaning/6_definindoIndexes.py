import pandas as pd

# -----------------------------------------------------
# Lendo arquivo excel
dfClientes   = pd.read_excel('caso_estudo.xlsx', sheet_name = 'clientes')
dfLojas      = pd.read_excel('caso_estudo.xlsx', sheet_name = 'lojas')
dfProdutos   = pd.read_excel('caso_estudo.xlsx', sheet_name = 'produtos')
dfVendas     = pd.read_excel('caso_estudo.xlsx', sheet_name = 'vendas')
dfPagamentos = pd.read_excel('caso_estudo.xlsx', sheet_name = 'pagamentos')


# -----------------------------------------------------
# Corrigindo o index
dfClientes   = dfClientes.set_index('id')
dfLojas      = dfLojas.set_index('id')
dfProdutos   = dfProdutos.set_index('id')
dfVendas     = dfVendas.set_index('id')
dfPagamentos = dfPagamentos.set_index('id')


# Acessando a coluna do id
dfClientes.index


dfClientes

dfLojas

dfProdutos

dfVendas

dfPagamentos
