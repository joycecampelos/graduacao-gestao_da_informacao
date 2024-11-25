"""
EXERCÍCIO 40 - Faça um programa que calcule o mostre a média aritmética de N notas.
"""

soma = cont = 0
while True:
    nota = float(input("Informe a nota: "))
    soma += nota
    cont += 1
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
media = soma / cont
print(f"A média aritmética das notas digitadas é {media:.2f}.")
