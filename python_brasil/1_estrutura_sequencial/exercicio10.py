"""
EXERCÍCIOS 10 - Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
"""

c = float(input("Digite uma temperatura em graus Celsius: "))
f = ((c * 9) / 5) + 32
print(f"A temperatura {c}ºC equivale a {f:.1f}ºF.")
