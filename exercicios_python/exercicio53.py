"""
EXERCÍCIO 53 - Faça um programa que mostre os n termos da série a seguir:
S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
​Imprima no final a soma da série.
"""

m = 1
total = 0
n = int(input("Informe a quantidade de termos: "))
print("S = ", end="")
for c in range(1, n + 1):
    print(f"{c}/{m}", end="")
    print(" = " if c == n else " + ", end="")
    total += c / m
    m += 2
print(f"{total:.2f}.")
