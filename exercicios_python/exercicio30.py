"""
EXERCÍCIO 30 - Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
"""

n1 = int(input("Informe o valor da base: "))
n2 = int(input("Informe o valor do expoente: "))
potencia = 1
for c in range(n2):
    potencia *= n1

print(potencia)
