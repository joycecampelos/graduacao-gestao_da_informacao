"""
EXERCÍCIO 46 - Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
"""

primos = []
numdousuario = int(input("Informe um número: "))
for numero in range(1, numdousuario + 1):
    qtd = 0
    for c in range(1, numero + 1):
        if numero % c == 0:
            qtd += 1
    if qtd == 2:
        primos.append(numero)
print(
    f"""Entre 1 e {numdousuario} tem os seguintes números primos:
{primos}."""
)
