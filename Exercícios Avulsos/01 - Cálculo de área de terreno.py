# 1. A imobiliária Imóbilis vende apenas terrenos retangulares. Faça um algoritmo para ler as dimensões de um
# terreno e depois exibir a área do terreno.

from time import sleep

print('-' * 40)
print('Bem Vindo à Imobiliária Imóbilis!')
print('-' * 40)

print('Para calcularmos a área de seu terreno, informe:')

largura = float(input(' - Largura: '))
cumprimento = float(input(' - Cumprimento: '))

sleep(1)
print('Calculando...')
sleep(1)
print(f'A área de seu terreno é de {largura*cumprimento} m².')