"""
EXERCÍCIO 16 - Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
a. Mostre a quantidade de valores que foram lidos;
b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d. Calcule e mostre a soma dos valores;
e. Calcule e mostre a média dos valores;
f. Calcule e mostre a quantidade de valores acima da média calculada;
g. Calcule e mostre a quantidade de valores abaixo de sete;
h. Encerre o programa com uma mensagem;
"""

acimaDaMedia = 0
abaixoDeSete = 0
notas = []
nota = 1

while nota != (-1):
    nota = float(input("Digite a nota: "))
    if nota == (-1):
        break
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"Quantidade de valores lidos: {len(notas)}.")

for x in notas:
    print(x, end=" ")

print()

notas.reverse()
for x in notas:
    print(x)

print(f"Soma dos valores: {sum(notas):.1f}.")
print(f"Média dos valores: {media:.1f}.")

for x in notas:
    if x > media:
        acimaDaMedia += 1

print(f"Quantidade de valores acima da média: {acimaDaMedia}.")

for x in notas:
    if x < 7:
        abaixoDeSete += 1

print(f"Quantidade de valores abaixo de sete: {abaixoDeSete}.")
print("FIM")
