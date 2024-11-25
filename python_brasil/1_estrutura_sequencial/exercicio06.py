"""
EXERCÍCIO 06 - Faça um programa que peça o raio de um círculo, calcule e mostre sua área.
"""

raio = float(input("Informe o valor do raio do círculo: "))
a = 3.14 * pow(raio, 2)
print(f"A área do círculo é {a:.1f} cm².")
