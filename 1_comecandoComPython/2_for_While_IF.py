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
# O nome vai receber os valores dentro de nomes
for nome in nomes:
    print(nome)



# -----------------------------------------------------
# A idade vai receber os valores dentro de idades e mostrar na tela idades positivas
for idade in idades:
    print(idade)


# O i variando de 0 à 9
for i in range(0, 10):
    print(i)



# -----------------------------------------------------
# O i vai pecorrer todas as idade, até que idade seja <= 10
i = 0
idade = idades[i]

while idade <= 10:
    print(idade)
    i += 1
    idade = idades[i]
