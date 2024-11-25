"""
EXERCÍCIO 05 - Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""

cont = 0
while True:
    A = int(input("Quantidade de habitantes no país A: "))
    while A <= 0:
        A = int(input("Valor inválido! Digite a quantidade de habitantes: "))
    TA = float(input("Percentual de crescimento do país A: "))
    while TA <= 0:
        TA = float(input("Valor inválido! Digite o percentual de crescimento: "))
    B = int(input("Quantidade de habitantes no país B: "))
    while B <= A:
        B = int(
            input(
                """O nº de habitantes do país B deve ser maior que o do país A.
Digite a quantidade de habitantes do país B: """
            )
        )
    TB = float(input("Taxa de crescimento do país B: "))
    while TB > TA:
        TB = float(
            input(
                """O percentual de crescimento do país B deve ser menor que o do país A.
Digite o percentual de crescimento do país B: """
            )
        )
    while A < B:
        A = A + (A * (TA / 100))
        B = B + (B * (TB / 100))
        cont += 1
    print(
        f"Será necessário {cont} anos para o país A ultrapassar ou igualar sua população ao do país B."
    )
    print()
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer realizar outra operação? [S/N] ")).upper()
    if continuar == "N":
        break
    print()
