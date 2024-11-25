"""
EXERCÍCIO 60 - Um número inteiro é considerado triangular se este for o produto de 3 números inteiros consecutivos como, por exemplo, 120 =	4 x	5 x	6. Elabore um programa que, após ler um número n do teclado, verifique se n	é triangular.
"""

n = int(input("Digite um número: "))
i = 1

while i * (i + 1) * (i + 2) < n:
    i += 1

if i * (i + 1) * (i + 2) == n:
    print(f"\nO {n} é um número triangular!")
else:
    print(f"\nO {n} não é um número triangular!")
