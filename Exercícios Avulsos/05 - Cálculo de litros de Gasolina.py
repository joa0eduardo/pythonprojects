# 5. Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o preço do
# litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque.

from Functions import Colors

valorpago = float(input('Informe o valor que deseja colocar de gasolina: '))
resposta = ' '

while resposta not in 'SN':
    resposta = str(input('O valor da Gasolina é R$ 4,94? [S/N]: ')).upper()[0]

if resposta in 'S':
    litros = valorpago / 4.94

else:
    precogasolina = float(input('Informe o valor atualizado: R$ '))
    litros = valorpago / precogasolina

print(f'Você abastecerá {Colors.destaca_amarelo(litros)} litros.')
