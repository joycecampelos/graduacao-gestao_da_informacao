"""
EXERCÍCIO 05 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

metrosquadrados = float(
    input("Informe o tamanho (em metros quadrados) da área a ser pintada: ")
)

litros = metrosquadrados / 3
latas = int(round(litros / 18, 0))
precototal = 80 * latas

print(
    f"\nSerão necessárias {latas} latas de tintas que ficarão num preço total de R${precototal:.2f}."
)
