"""
EXERCÍCIO 39 - Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, quantos e quais são os seus divisores.
"""

numero = int(input("Digite um número: "))
divisores = []
for c in range(1, numero + 1):
    if numero % c == 0:
        divisores.append(c)
if len(divisores) == 2:
    print(f"O número {numero} É PRIMO!")
else:
    print(f"O número {numero} NÃO É PRIMO!")
    print(f"Com {len(divisores)} divisores, sendo eles: {divisores}.")
