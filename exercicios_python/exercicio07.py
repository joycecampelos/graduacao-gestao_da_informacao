"""
EXERCÍCIO 07 - Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo
"""

valor = int(input("Digite um valor: "))

if valor > 0:
    print("Esse valor é positivo!")
elif valor < 0:
    print("Esse valor é negativo!")
else:
    print("Não é positivo e nem negativo.")
