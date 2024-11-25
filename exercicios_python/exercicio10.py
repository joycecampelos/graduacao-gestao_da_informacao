"""
EXERCÍCIO 10 - Faça um programa que peça um número inteiro e determine se ele é par ou ímpar.
"""

num = int(input("Informe um número: "))

if (num % 2) == 0:
    print(f"\n{num} é par!")
else:
    print(f"\n{num} é ímpar!")
