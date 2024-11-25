"""
EXERCÍCIO 08 - Faça um programa que leia três números e mostre o maior deles.
"""

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

if num1 > num2 and num1 > num3:
    print(f"\nO primeiro número é o maior: {num1}.")
elif num2 > num1 and num2 > num3:
    print(f"\nO segundo número é o maior: {num2}.")
elif num3 > num1 and num3 > num2:
    print(f"\nO terceiro número é o maior: {num3}.")
else:
    print("\nOs números digitados tem o mesmo valor.")
