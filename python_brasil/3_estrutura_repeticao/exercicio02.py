"""
EXERCÍCIO 02 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""

nome = str(input("Digite o nome de usuário: "))
senha = str(input("Digite a senha: "))
while nome == senha:
    print("\nDados inválidos! Digite as informações novamente.")
    nome = str(input("Digite o nome de usuário: "))
    senha = str(input("Digite a senha: "))
