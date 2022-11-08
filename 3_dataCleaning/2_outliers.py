import pandas as pd

# -----------------------------------------------------
# Lendo arquivo excel
dfClientes   = pd.read_excel('caso_estudo.xlsx', sheet_name = 'clientes')
dfLojas      = pd.read_excel('caso_estudo.xlsx', sheet_name = 'lojas')
dfProdutos   = pd.read_excel('caso_estudo.xlsx', sheet_name = 'produtos')
dfVendas     = pd.read_excel('caso_estudo.xlsx', sheet_name = 'vendas')
dfPagamentos = pd.read_excel('caso_estudo.xlsx', sheet_name = 'pagamentos')


# -----------------------------------------------------
# o número do ID: 10 foi inserido incorretamente, pois deveria ter 4 casas decimais, então é necessario dividir por 10_000
dfProdutos


dfProdutos.loc[9, 'valor'] = dfProdutos.valor[9] / 10_000
dfProdutos


dfProdutos.boxplot(column = ['valor'])
