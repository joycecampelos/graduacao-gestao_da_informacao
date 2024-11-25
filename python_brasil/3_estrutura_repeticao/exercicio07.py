"""
EXERCÍCIO 07 - Faça um programa que leia 5 números e informe o maior número.
"""

for c in range(1, 6):
    num = int(input(f"Informe {c}º número: "))
    if c == 1 or num > maior:
        maior = num
print(f"O maior valor dos números informados é {maior}.")
