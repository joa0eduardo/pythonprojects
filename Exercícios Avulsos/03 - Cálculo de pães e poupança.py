# A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia.
# Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. Ao final do dia, o dono quer saber quanto arrecadou com a
# venda dos pães e broas (juntos), e quanto deve guardar numa conta de poupança (10% do total arrecadado). Você
# foi contratado para fazer os cálculos para o dono. Com base nestes fatos, faça um algoritmo para ler as quantidades
# de pães e de broas, e depois calcular os dados solicitados.

precobroa = 1.2
precopao = 0.12
opcao = 0

print('-' * 10)
print(' PADARIA HOTPÃO  ')
print('-' * 10)

while True:

    opcao = int(input('''O que você deseja fazer?
    [ 1 ] Atualizar preço dos produtos
    [ 2 ] Calcular venda de hoje
    [ 3 ] Sair do sistema
    Resposta: '''))

    if opcao == 1:
        precobroa = float(input(f'Broa - Valor atual é: R$ {precobroa}. Informe o novo valor: '))
        precopao = float(input(f'Pão - Valor atual é: R$ {precopao}. Informe novo valor: '))

    elif opcao == 2:

        print('Informe a quantidade vendida hoje: ')
        vendabroa = int(input(' - Broas: '))
        vendapao = int(input(' - Pães: '))
        totalvenda = (vendabroa * precobroa) + (vendapao * precopao)
        print()

        print(f'Total de Broas vendidas: R$ {vendabroa * precobroa:.2f}')
        print(f'Total de Pães vendidos: R$ {vendapao * precopao:.2f}')
        print(f'Total de vendas: R$ {totalvenda}')
        print(f'Valor sugerido para poupança: R$ {totalvenda * 0.10:.2f}')

    elif opcao == 3:
        print('Volte sempre!')
        break

    else:
        print('Escolha entre umas das opções.')