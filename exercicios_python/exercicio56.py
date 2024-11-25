"""
EXERCÍCIO 56 - Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que receba dados de vendedores de uma empresa (quantidade indeterminada de entrada de dados) e apresente quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie uma estratégia para obter a posição da lista a partir do salário, sem fazer vários ifs​ aninhados.
"""

salariofixo = 200
salarios = [0, 0, 0, 0, 0, 0, 0, 0, 0]
while True:
    valorvendas = float(input("Informe o valor das vendas do vendedor: "))
    salario = valorvendas * 0.09 + salariofixo
    indice = int(salario / 100) - 1
    if indice > 9:
        indice = 9
    elif indice < 1:
        indice = 1
    salarios[indice - 1] += 1
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N] ")).upper()
    if continuar == "N":
        break
    print()
print()
for c in range(0, 9):
    print(f"R${c * 100 + 200}", end="")
    print(" em diante" if c == 8 else f" - R${(c + 1) * 100 + 199}", end="")
    print(f": {salarios[c]} vendedor(es).")
