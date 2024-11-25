"""
EXERCÍCIO 08 - Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

soma = 0
for c in range(1, 6):
    num = int(input(f"Informe {c}º número: "))
    soma += num
média = soma / 5
print(f"A soma dos números digitados é {soma} e a média é {média:.1f}.")
