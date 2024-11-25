"""
EXERCÍCIO 09 - Faça um programa que leia três números e mostre-os em ordem decrescente.
"""

num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))
print("\nNúmeros digitados em ordem decrescente:")
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)
if num1 < num2 and num1 > num3:
    print(num1)
elif num2 < num1 and num2 > num3:
    print(num2)
else:
    print(num3)
if num1 < num2 and num1 < num3:
    print(num1)
elif num2 < num1 and num2 < num3:
    print(num2)
else:
    print(num3)
