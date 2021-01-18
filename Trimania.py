# Projeto Trimania
# [x] Salvar cartela
# [ ] Realizar 4 jogos
# [x] Calcular chance de vencer
# [ ] Colorir em verde os números que estão na cartela
# [x] Exibir os números sorteados
# [x] Informar que o jogador venceu/perdeu

cartela = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
sorteados = list()
num = cont = percentual = 0

for li in range(0, 4):
    for col in range(0, 5):
        cartela[li][col] = int(input(f'Informe o {col + 1}º número da {li + 1}º linha: '))

print('Sua cartela:')

for li in range(0, 4):
    for col in range(0, 5):
        print(f'[{cartela[li][col]:^5}]', end='')
    print()

while True:
    num = int(input('Bolinha sorteada: '))

    if num > 60:
        break

    if (cont + 1) == 20:
        print('PARABÉNS! VOCÊ GANHOU NA TRIMANIA!')
        break

    if num not in cartela[0] \
            and num not in cartela[1] \
            and num not in cartela[2] \
            and num not in cartela[3]:
        sorteados.append(num)
    else:
        sorteados.append(num)
        cont += 1

    percentual = (cont / len(sorteados)) * 100

    print(f'Números sorteados: {sorteados}')
    print(f'Chance de ganhar: {percentual}')

if (cont + 1) <= 20:
    print(f'Que pena, você perdeu. Ficou por {20-cont} bolinha(s). :(')
