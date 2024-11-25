"""
EXERCÍCIO 09 - Faça um programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).
"""

f = float(input("Digite uma temperatura em graus Farenheit: "))
c = 5 * (f - 32) / 9
print(f"A temperatura {f}ºF equivale a {c:.1f}ºC.")
