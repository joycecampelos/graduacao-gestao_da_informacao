"""
EXERCÍCIO 13 - Faça um programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números ímpares no vetor ÍMPAR. Imprima os dois vetores.
"""

numero = []
par = []
impar = []

for i in range(20):
    digito = int(input("Digite um número: "))

    numero.append(digito)

    if (digito % 2) == 0:
        par.append(digito)
    else:
        impar.append(digito)

print(f"\nPAR: {par}.")
print(f"ÍMPAR: {impar}.")
