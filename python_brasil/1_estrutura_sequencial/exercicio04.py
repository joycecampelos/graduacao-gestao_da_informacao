"""
EXERCÍCIO 04 - Faça um programa que peça as 4 notas bimestrais e mostre a média.
"""

soma = 0
for c in range(1, 5):
    nota = float(input(f"Digite a {c}º nota: "))
    soma += nota
print(f"A média das notas: {soma / 4:.2f}.")
