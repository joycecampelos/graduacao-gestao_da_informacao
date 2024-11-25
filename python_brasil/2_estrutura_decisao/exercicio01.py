"""
EXERCÍCIO 01 - Faça um programa que peça dois números e imprima o maior deles.
"""

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
if num1 > num2:
    print(f"O número {num1} é maior que o número {num2}.")
elif num2 > num1:
    print(f"O número {num2} é maior que o número {num1}.")
else:
    print("Os dois números tem valores iguais!")
