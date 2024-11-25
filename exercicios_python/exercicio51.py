"""
EXERCÍCIO 51 - Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo
"""

num = 1
cont1 = cont2 = cont3 = cont4 = 0
while num >= 0:
    num = float(input("Digite um número: "))
    if 0 <= num <= 25:
        cont1 += 1
    elif 26 <= num <= 50:
        cont2 += 1
    elif 51 <= num <= 75:
        cont3 += 1
    elif 76 <= num <= 100:
        cont4 += 1
print(f"No intervalo [ 0 - 25 ]: {cont1} número(s).")
print(f"No intervalo [ 26 - 50 ]: {cont2} número(s).")
print(f"No intervalo [ 51 - 75 ]: {cont3} número(s).")
print(f"No intervalo [ 76 - 100 ]: {cont4} número(s).")
