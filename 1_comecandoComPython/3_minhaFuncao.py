"""
    Essa função deve receber um número que sera uma idade
    e retornar se essa idade é de uma criança, adolescente,
    adulto ou idoso.
"""
def faixaIdade(idade):
    if idade <= 12:
        return 'Criança'
    elif idade <= 18:
        return 'Adolescente'
    elif idade <= 80:
        return 'Adulto'
    else:
        return 'Idoso'
    
def somaQuadrdo(n1, n2):
    return n1**2 + n2**2
