"""
EXERCÍCIO 31 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares.
"""

contpares = contimpares = 0
for c in range(10):
    nums = int(input("Informe um número: "))
    if nums % 2 == 0:
        contpares += 1
    else:
        contimpares += 1
print(
    f"""Quantidade de números pares: {contpares}.
Quantidade de números ímpares: {contimpares}."""
)
