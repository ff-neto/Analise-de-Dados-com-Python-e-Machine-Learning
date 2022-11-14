import pandas as pd

# -----------------------------------------------------
# Lendo arquivo excel
dfClientes   = pd.read_excel('caso_estudo.xlsx', sheet_name = 'clientes')
dfLojas      = pd.read_excel('caso_estudo.xlsx', sheet_name = 'lojas')
dfProdutos   = pd.read_excel('caso_estudo.xlsx', sheet_name = 'produtos')
dfVendas     = pd.read_excel('caso_estudo.xlsx', sheet_name = 'vendas')
dfPagamentos = pd.read_excel('caso_estudo.xlsx', sheet_name = 'pagamentos')


# -----------------------------------------------------
# Alterando o formato de data
dfClientes.dt_nasc = pd.to_datetime(dfClientes.dt_nasc, format = '%m/%d/%Y')
dfClientes