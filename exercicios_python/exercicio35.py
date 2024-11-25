"""
EXERCÍCIO 35 - Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""

cont = maior = menor = soma = 0
while True:
    num = int(input("Digite um número: "))

    if cont == 0 or num > maior:
        maior = num
    if cont == 0 or num < menor:
        menor = num
    soma += num
    cont += 1

    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if continuar == "N":
        break

print(
    f"""O maior valor digitado foi {maior}.
O menor valor digitado foi {menor}.
A soma dos valores digitados é {soma}."""
)
