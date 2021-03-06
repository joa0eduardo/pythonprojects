from datetime import date

def soma(list):
    r = 0
    for n in list:
        r += n
    return r

def area(a, b):
    r = a * b
    return r

def calcula_idade(ano):
    r = date.today().year - ano
    return r

def calcula_dias_vividos(ano):
    r = calcula_idade(ano) * 365
    return r
