# 6. O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição. Escreva um algoritmo que leia o
# peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar. Assuma que a balança já desconte o peso
# do prato.

from Functions import Math

kilo = float(input('Peso do prato (Kg): ').replace(",", "."))
kiloreal = kilo - 0.820
precokilo = 12
list = [kiloreal, precokilo]

print(f'Peso do prato: {kiloreal:.3f}:')
print(f'Tara do prato: 0,820 Kg')
print(f'Valor por Kg: R$ 12,00')
print(f'Total a pagar: R$ {Math.multiplicacao(list):.2f}')
