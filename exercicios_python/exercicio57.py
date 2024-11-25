"""
EXERCÍCIO 57 - Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""

ficha = []
saltos = []
saltosnome = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]
cont = 0
while True:
    nome = str(input("Atleta: "))
    if nome == "":
        break
    for c in range(0, 5):
        saltos.append(float(input(f"{saltosnome[c]} Salto: ")))
    soma = sum(saltos)
    media = soma / 5
    ficha.append([nome, saltos[:], media])
    saltos.clear()
    print("\nDados digitados:")
    print(f"Atleta: {ficha[cont][0]}")
    cont1 = 0
    for s in saltosnome:
        print(f"{s} Salto: {ficha[cont][1][cont1]} m")
        cont1 += 1
    cont += 1
    print()
print("\n>>> RESULTADOS FINAIS <<<")
for p in ficha:
    print(f"Atleta: {p[0]}")
    print(f"Saltos: {p[1][0]} - {p[1][1]} - {p[1][2]} - {p[1][3]} - {p[1][4]}")
    print(f"Média dos saltos: {p[2]}\n")
