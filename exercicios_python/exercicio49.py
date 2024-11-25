"""
EXERCÍCIO 49 - Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
"""

cont = maisalto = maisbaixo = numeroalto = numerobaixo = 0
while True:
    numeroaluno = input("Número do aluno: ")
    alturaaluno = int(input("Altura em cm: "))
    if cont == 0 or alturaaluno > maisalto:
        maisalto = alturaaluno
        numeroalto = numeroaluno
    if cont == 0 or alturaaluno < maisbaixo:
        maisbaixo = alturaaluno
        numerobaixo = numeroaluno
    cont += 1
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if continuar == "N":
        break
    print()

print(f"O número do aluno mais alto é {numeroalto}, com altura de {maisalto}cm.")
print(f"O número do aluno mais baixo é {numerobaixo}, com altura de {maisbaixo}cm.")
