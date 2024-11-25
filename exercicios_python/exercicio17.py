"""
EXERCÍCIO 17 - Faça um programa que lê três valores. Se todos forem positivos, calcule e imprima a área do trapézio que tem A e B por bases, e C por altura.	
"""

a = float(input("\nDigite o valor da BASE MAIOR: "))
b = float(input("Digite o valor da BASE MENOR: "))
c = float(input("Digite o valor da ALTURA: "))

if a > 0 and b > 0 and c > 0:
    area = ((a + b) * c) / 2
    print(f"\nA área do Trapézio é {area:.2f}cm².")

else:
    print("\nCom esses valores, não é possível calcular a área do trapézio!")
