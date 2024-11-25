"""
EXERCÍCIO 01 - Faça um programa que peça o raio de um círculo, calcule e mostre sua área.
"""

raio = float(input("Digite o valor do raio: "))
pi = 3.14
area = pi * (raio**2)

print(f"\nA área do círculo é {area:.1f}cm².")
