# 4. Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos dias de vida ela possui.
# Considere sempre anos completos, e que um ano possui 365 dias. Ex: uma pessoa com 19 anos possui 6935 dias
# de vida; veja um exemplo de saída:
#
# MARIA, VOCÊ JÁ VIVEU 6935 DIAS

from Functions import Math

titulo = 'CALCULO DE DIAS VIVIDOS'

print('-' * len(titulo))
print(titulo)
print('-' * len(titulo))

nome = str(input('Informe seu nome: '))
ano = int(input('Informe o ano de seu nascimento: '))
print(f'{nome} você viveu {Math.calcula_dias_vividos(ano)} dias até hoje!')
