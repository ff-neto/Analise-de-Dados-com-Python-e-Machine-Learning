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
# Lendo arquivo csv
# CSV é mas utilizado, porque ele suporta infinitos dados e o execel tem um limite de 1.048.576 linhas
dfClientes = pd.read_csv('caso_estudo_clientes.csv', sep = ';')

dfClientes
