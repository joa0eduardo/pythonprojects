# 5. Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o preço do
# litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque.

valorpago = float(input('Informe o valor que deseja colocar de gasolina: '))
resposta = ' '

while resposta not in ('SsNn'):
    resposta = str(input('O valor da Gasolina é R$ 4,94? [S/N]: '))

if resposta in ('Ss'):
    litros = valorpago / 4.94

else:
    precogasolina = float(input('Informe o valor atualizado: R$ '))
    litros = valorpago / precogasolina

print(f'Você abastecerá \033[1;33m{litros:.3f}\033[0;0m litros.')
