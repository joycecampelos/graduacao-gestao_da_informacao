"""
EXERCÍCIO 01 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

condição = float(input("Informe uma nota: "))
while condição < 0 or condição > 10:
    condição = float(input("Valor inválido! Digite uma nota entre zero e dez: "))
