"""
EXERCÍCIO 08 - Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

valordahora = float(input("Quanto ganha por hora: R$"))
horastrabalhadas = int(input("Quantas horas trabalhou esse mês: "))
saláriototal = valordahora * horastrabalhadas
print(
    f"Calculando o valor pelas horas trabalhadas, seu salário esse mês é de R${saláriototal:.2f}."
)
