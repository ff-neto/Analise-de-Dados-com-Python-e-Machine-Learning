import numpy as np

# O pandas tem a facilidade a manipulação de dados.
# A sua performace é inferior a do Numpy

# Um array no numpy
idades = np.array([ 10, 15, 20, 18, 20 ])

notas = np.array([ 8, 8, 5, 7, 10 ])

print(notas[ idades == 20 ])


# Funções especifica do numpy como máxima, média e mínima
np.mean(idades)

# Um array multidimensional
salario = np.array([ [ 1000, 1200, 1300 ], [ 800, 900, 950 ], [ 2000, 2100, 2110 ]])
