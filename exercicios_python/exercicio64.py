"""
EXERCÍCIO 64 - Generalize o exercício anterior, de forma que ele calcule e mostre na tela os quadrados de todos os números naturais menores que 1000, usando o método da soma de ímpares.
"""

somador = 1
quadrado = 0
num = 0
numero = 999

for c in range(0, numero, 1):
    quadrado += somador
    somador += 2
    num += 1
    print(f"O quadrado de {num} é {quadrado}.")
