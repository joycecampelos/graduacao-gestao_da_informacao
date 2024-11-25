"""
EXERCÍCIO 08 -Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

produto1 = float(input("Digite o preço do 1º produto: R$"))
produto2 = float(input("Digite o preço do 2º  produto: R$"))
produto3 = float(input("Digite o preço do 3º produto: R$"))

if produto1 < produto2 and produto1 < produto3:
    print(f"O 1º produto é o mais barato. Com preço de R${produto1:.2f}.")
elif produto2 < produto1 and produto2 < produto3:
    print(f"O 2º produto é o mais barato. Com preço de R${produto2:.2f}.")
else:
    print(f"O 3º produto é o mais barato. Com preço de R${produto3:.2f}.")
