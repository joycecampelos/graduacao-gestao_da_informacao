"""
EXERCÍCIO 14 - Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,imprima o número de alunos com média maior ou igual a 7.0.
"""

medias = []
for x in range(10):
    nota1 = float(input("Digite a sua primeira nota: "))
    nota2 = float(input("Digite a sua segunda nota: "))
    nota3 = float(input("Digite a sua terceira nota: "))
    nota4 = float(input("Digite a sua quarta nota: "))
    print("\n")
    media = (nota1 + nota2 + nota3 + nota4) / 4
    medias.append(media)

quant = 0
for x in medias:
    if x >= 7:
        quant += 1

print(f"Quantidade de médias maior ou igual a 7.0: {quant}.")
