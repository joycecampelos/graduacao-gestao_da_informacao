"""
EXERCÍCIO 02 - Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

valorporhora = float(input("Informe o valor que ganha por hora: R$"))
horastrabalhadas = int(input("Informe as horas trabalhadas no mês: "))

salario = valorporhora * horastrabalhadas

print(f"\nSeu salário total desse mês é de R${salario:.2f}.")
