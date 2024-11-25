"""
EXERCÍCIO 26 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""

nome = input("Nome de usuário: ").upper()
senha = input("Senha: ").upper()

while nome == senha:
    print("A senha não pode ser igual ao nome de usuário!\n")
    senha = input("Digite uma nova senha: ")

print(f"\nUsuário: {nome} || Senha: {senha}")
