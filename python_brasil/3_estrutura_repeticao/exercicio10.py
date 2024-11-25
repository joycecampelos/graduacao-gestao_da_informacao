"""
EXERCÍCIO 10 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
"""

num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
for c in range(num1 + 1, num2):
    print(c)
