"""
EXERCÍCIO 06 - Faça um programa que leia três números e mostre o maior deles.
"""

num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))
if num1 > num2 and num1 > num3:
    print(f"O número {num1} é o maior.")
elif num2 > num1 and num2 > num3:
    print(f"O número {num2} é o maior.")
else:
    print(f"O número {num3} é o maior.")
