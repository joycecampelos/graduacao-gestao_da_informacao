"""
EXERCÍCIO 38 - Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
"""

numero = int(input("Digite um número: "))
qtd = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        qtd += 1
        print(numero)
if qtd == 2:
    print(f"O número {numero} É PRIMO!")
else:
    print(f"O número {numero} NÃO É PRIMO!")
