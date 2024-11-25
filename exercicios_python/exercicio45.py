"""
EXERCÍCIO 45 - O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
"""

cont = maior = menor = soma = 0
while True:
    temperatura = float(input("Informe a temperatura: "))
    soma += temperatura
    if cont == 0 or temperatura > maior:
        maior = temperatura
    if cont == 0 or temperatura < menor:
        menor = temperatura
    cont += 1

    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if continuar == "N":
        break
media = soma / cont
print(
    f"""A menor temperatura informada foi {menor:.2f}.
A maior temperatura informada foi {maior:.2f}.
A média das temperaturas informadas é {media:.2f}."""
)
