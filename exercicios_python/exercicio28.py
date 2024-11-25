"""
EXERCÍCIO 28 - Faça um programa que leia 5 números e informe o maior número, a soma e a média dos números.
"""

maior = soma = 0
for c in range(0, 5):
    numero = int(input("Digite um número: "))
    if c == 0 or numero > maior:
        maior = numero
    soma += numero
media = soma / 5

print(
    f"""O maior número é {maior}.
A soma dos números digitados é {soma}.
E a média dos números digitados é {media:.2f}."""
)
