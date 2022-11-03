# -----------------------------------------------------
# Lista com três nomes dentro da variavel nome
"""
    A lista é um conjunto de informação que pode ter uma dimensão ou mais, 
    e ela pode sofrer alteração na execução do código. Então pode ter inserção
    ou retirada de registro.
"""
nomes = ['Felipe', 'Maria', 'Anna']

idades = [10, 20, 15]


# -----------------------------------------------------
# Quando os dados é colocado em () esse dados numca será alterado
"""
    A tupla não muda de alteração ao longo do código. Após criada não pode
    inserir novas informações dentro.
"""
sexo = ('M', 'F', 'O')


# -----------------------------------------------------
# Dicionáros
"""
    O dicionário não tem dependência de uma coluna a outra em uma tabela. É uma
    estrutura que você pode guardar essa informação de forma simples e regular no algoritmo
"""
# cadastro = {'nomes': ['Rafael', 'Joana']}
cadastro = {
    'nomes': nomes,
    'idades': idades,
    'cidade': ['A', 'B', 'C']
}



# -----------------------------------------------------
nomes[1]

idades[0]

sexo[0]

cadastro['nomes']

cadastro['nomes'][0]

cadastro['idades']

sum(cadastro['idades'])
