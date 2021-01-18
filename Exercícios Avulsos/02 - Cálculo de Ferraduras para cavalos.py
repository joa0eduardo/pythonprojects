# 2. Faça um algoritmo para calcular quantas ferraduras são necessárias para equipar todos os cavalos
# comprados para um haras.

total = 0

print('-' * 22)
print('CÁLCULO DE FERRADURAS')
print('-' * 22)

qtde = int(input('Quantos cavalos foram comprados? '))

while True:
    resp = str(input('Todos os cavalos precisam de ferraduras novas? [S/N]: ')).upper()[0]

    if resp not in 'SN':
        print('Erro! Favor informar S ou N para a resposta.')
        print()
    else:
        break

if resp == 'S':
    total = qtde * 4

    print(f'Serão necessárias {total} ferraduras para os {qtde} cavalos.')

else:
    for f in range(0, 4):
        qtde = int(input(f'Quantos cavalos precisam de {f+1} ferradura(s)? '))
        total += qtde

    print(f'O total de ferraduras a comprar é {total}.')
