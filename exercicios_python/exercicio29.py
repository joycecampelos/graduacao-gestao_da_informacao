"""
EXERCÍCIO 29 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
…
5 X 10 = 50
"""

numero = int(input("Informe um número entre 1 a 10 para ver sua tabuada: "))
while numero < 1 or numero > 10:
    numero = int(input("Número inválido. Digite um número entre 1 a 10: "))
print(f"Tabuada de {numero}:")
for c in range(1, 11):
    print(f"{numero} x {c:2} = {numero * c:2}")
