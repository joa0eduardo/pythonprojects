# 1. A imobiliária Imóbilis vende apenas terrenos retangulares. Faça um algoritmo para ler as dimensões de um
# terreno e depois exibir a área do terreno.

from time import sleep
from Functions import Math

print('-' * 40)
print('Bem Vindo à Imobiliária Imóbilis!')
print('-' * 40)

print('Para calcularmos a área de seu terreno, informe:')

largura = float(input(' - Largura: '))
comprimento = float(input(' - Comprimento: '))

sleep(1)
print('Calculando...')
sleep(1)
print(f'A área de seu terreno é de {Math.area(largura, comprimento)} m².')