"""
EXERCÍCIO 61 - Elabore um programa que leia n valores e	mostre a soma de seus quadrados.
"""

n = 1
soma = 0

while n != 0:
    n = int(input("\nDigite um número ou <0> para sair: "))
    if n != 0:
        quad = n * n
        print(f"O quadrado de {n} = {quad}.")
        soma += quad
print(f"\nA somatória do quadrado de todos os valores digitados é {soma}.")
