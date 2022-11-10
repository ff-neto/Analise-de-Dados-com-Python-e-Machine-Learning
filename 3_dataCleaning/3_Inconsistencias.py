"""
O que seria a consistência?
    A consistência é garantir que uma tabela consiga comunicar com a outra.
"""
import pandas as pd

# -----------------------------------------------------
# Lendo arquivo excel
dfClientes   = pd.read_excel('caso_estudo.xlsx', sheet_name = 'clientes')
dfLojas      = pd.read_excel('caso_estudo.xlsx', sheet_name = 'lojas')
dfProdutos   = pd.read_excel('caso_estudo.xlsx', sheet_name = 'produtos')
dfVendas     = pd.read_excel('caso_estudo.xlsx', sheet_name = 'vendas')
dfPagamentos = pd.read_excel('caso_estudo.xlsx', sheet_name = 'pagamentos')



# -----------------------------------------------------
# Vamos buscar por vendas que não possui clientes
# dfVendas.id_clientedfVendas.id_cliente -> Está pegando apenas o id da coluna de vendas
# isin -> está avaliando quais daqueles id estão dentro da coluna id Clientes.
dfVendas.id_cliente.isin(dfClientes.id)


# Vamos buscar por vendas que não possui clientes
# dfVendas.id_clientedfVendas.id_cliente -> Está pegando apenas o id da coluna de vendas
# isin -> está avaliando quais daqueles id NÃO estão dentro da coluna id Clientes.
# .any() -> fala se algum valor é verdadeiro ou não
~dfVendas.id_cliente.isin(dfClientes.id).any()


# Vamos buscar por vendas que não possui clientes
# dfVendas.id_clientedfVendas.id_cliente -> Está pegando apenas o id da coluna de vendas
# isin -> está avaliando quais daqueles id NÃO estão dentro da coluna id Clientes.
# .any() -> fala se algum valor é verdadeiro ou não
# vizualizar os dados (visualisar o id clientes que não estão dentro do conjunto do id clientes)
dfVendas [ ~dfVendas.id_cliente.isin(dfClientes.id)]


dfVendas [ ~dfVendas.id_loja.isin(dfLojas.id) ]


dfVendas [ ~dfVendas.id_produto.isin(dfProdutos.id) ]



# -----------------------------------------------------
# filtro: Busque os pagamentos que não tem o id de venda
dfPagamentos[ ~dfPagamentos.id_venda.isin(dfVendas.id) ]



# -----------------------------------------------------
# filtro: Busque se todas as vendas que não geraram pagamentos
# está vizualizando o data frame Vendas que está gerando um filtro nele.
# De forma em que a coluna id de vendas NÃO está dentro do data frame pagamento
# da coluna id vendas
dfVendas[ ~dfVendas.id.isin(dfPagamentos.id_venda) ]



# -----------------------------------------------------
# filtro: Busque se todas as vendas que não geraram pagamentos
dfVendas[ ~dfVendas.id.isin(dfPagamentos.id_venda) ].count()
# Temos 928 vendas que não geraram pagamentos