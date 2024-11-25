"""
EXERCÍCIO 62 - Faça um programa que leia dois valores x e y, e calcula o valor de x dividido por y, além do resto da divisão. Não é permitido usar as operações de divisão e resto de divisão do Python (use apenas soma e subtração).
"""

x = int(input("Digite um valor para X: "))
y = int(input("Digite um valor para Y: "))
divisao = 0
resto = 0

for i in range(y, x + 1, y):
    divisao += 1
    resto += y

print(f"\nO resultado da divisão é {divisao} e o resto é {x - resto}.")
