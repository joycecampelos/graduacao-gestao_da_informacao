"""
EXERCÍCIO 34 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5! = 5.4.3.2.1 = 120
"""

n = int(input("Digite um número para calcular seu fatorial: "))
f = 1
print(f"Calculando {n}! = ", end="")
for c in range(n, 0, -1):
    print(f"{c}", end="")
    print(" x " if c > 1 else " = ", end="")
    f *= c
print(f"{f}.")
