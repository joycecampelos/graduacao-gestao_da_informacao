"""
EXERCÍCIO 06 - Faça um programa que peça dois números e imprima o maior deles.
"""

n1 = int(input("Informe um número: "))
n2 = int(input("Informe outro número: "))

if n1 > n2:
    print(f"\n{n1} é maior!")
elif n1 == n2:
    print(f"\nOs dois números são iguais!")
else:
    print(f"\n{n2} é maior!")
