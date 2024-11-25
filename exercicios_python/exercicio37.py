"""
EXERCÍCIO 37 - Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
"""

while True:
    n = int(input("Digite um número para calcular seu fatorial: "))
    if n < 0 or n > 16:
        print("Valor inválido! Por favor, digite números entre 0 e 16.")
    else:
        f = 1
        print(f"Calculando {n}! = ", end="")
        for c in range(n, 0, -1):
            print(f"{c}", end="")
            print(" x " if c > 1 else " = ", end="")
            f *= c
        print(f"{f}.")

        continuar = " "
        while continuar not in "SN":
            continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
        if continuar == "N":
            break
