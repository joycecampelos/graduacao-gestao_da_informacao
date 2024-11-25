"""
EXERCÍCIO 03 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

sexo = input("Digite a letra correspondente ao seu sexo (F/M): ").upper()
if sexo == "F":
    print("F - Feminino")
elif sexo == "M":
    print("M - Masculino")
else:
    print("Sexo Inválido")
