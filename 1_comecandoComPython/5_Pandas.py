"""
    Pandas é uma biblioteca para manipular dados de forma
    estruturadas.
"""
# O pandas tem a facilidade a manipulação de dados.
# A sua performace é inferior a do Numpy
import pandas as pd


# data frame: são estrutura cimilares a tabela, como se fosse banco de dados
tabela = pd.DataFrame({ 
    'nome': [
        'rafael',
        'joao',
        'Felipe',
        'Maria'
        ],
    'nota': [
        10,
        9,
        8,
        7
    ] 
})

tabela

tabela.nome

tabela.nome[2]

# número da linha depois o nome da coluna
tabela.loc[2, 'nome']

# Criar uma média baseado em nome
tabela.groupby('nome').mean()

# Filtro: bscar nota de felipe
tabela.nota[tabela.nome == 'Felipe']
