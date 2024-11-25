"""
EXERCÍCIO 55 - Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
- Mostre a quantidade de valores que foram lidos;
- Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
- Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
- Calcule e mostre a soma dos valores;
- Calcule e mostre a média dos valores;
- Calcule e mostre a quantidade de valores acima da média calculada;
- Calcule e mostre a quantidade de valores abaixo de sete;
- Encerre o programa com uma mensagem;
"""

lista = []
while True:
    num = float(input("Digite um número (ou [-1] para sair): "))
    if num == -1:
        break
    lista.append(num)
print(f"\nForam lidos {len(lista)} elementos.")
print(f"Valores digitados: ", end="")
for c in range(len(lista)):
    print(lista[c], end="")
    print("." if c == len(lista) - 1 else ", ", end="")
print()
for c in range(len(lista) - 1, -1, -1):
    print(lista[c])
soma = sum(lista)
media = sum(lista) / len(lista)
acimadamedia = abaixodesete = 0
for c, v in enumerate(lista):
    if v > media:
        acimadamedia += 1
    if v < 7:
        abaixodesete += 1
print(f"A soma dos valores é {soma:.2f}")
print(f"A média dos valores é {media:.2f}")
print(f"Tem {acimadamedia} número(s) acima da média.")
print(f"Tem {abaixodesete} número(s) abaixo de sete.")
print("FIM DO PROGRAMA!")
