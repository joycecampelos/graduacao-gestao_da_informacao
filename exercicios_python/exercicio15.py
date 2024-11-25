"""
EXERCÍCIO 15 - Faça um programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
"""

A = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
soma = 0
for x in A:
    quadrado = x**2
    soma += quadrado
print("Soma:", soma)
