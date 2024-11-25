"""
EXERCÍCIO 25 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

nota = 0

while nota <= 0 or nota >= 10:
    nota = float(input("Informe a nota: "))

    if nota <= 0 or nota >= 10:
        print("Valor inválido!\n")
print(f"\nNota digitada: {nota}.")
