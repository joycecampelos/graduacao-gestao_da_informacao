"""
EXERCÍCIO 63 - O quadrado de um numero natural n é dado pela soma dos n primeiros números impares consecutivos. Por exemplo, 1²=1, 2²=1+3, 3²=1+3+5, 4²=1+3+5+7, etc. Escreva um programa que dado um número n, calcule seu quadrado usando a soma de ímpares ao invés de produto.
"""

somador = 1
quadrado = 0
numero = int(input("Digite um número: "))

# for c in range(0, numero):
#    quadrado += somador
#    somador +=2

cont = 0
while cont < numero:
    quadrado += somador
    somador += 2
    cont += 1

print(f"\nO quadrado de {numero} é {quadrado}.")
