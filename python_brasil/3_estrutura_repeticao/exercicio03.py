"""
EXERCÍCIO 03 - Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
"""

nome = str(input("Digite seu nome: "))
while len(nome) <= 3:
    nome = str(input("Nome inválido! Por favor, digite um nome válido: "))
idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Idade inválida! Por favor, digite uma idade válida: "))
salário = float(input("Digite o valor do seu salário: R$"))
while salário <= 0:
    salário = float(input("Salário inválido! Por favor, digite um valor válido: R$"))
sexo = str(input("Digite a letra correspondente ao seu sexo (F/M): "))
while sexo not in "FfMm":
    sexo = str(input("Sexo inválido! Por favor, digite uma letra válida: "))
estadocivil = str(input("Digite a letra que corresponde ao seu estado civil: "))
while estadocivil not in "SsCcVvDd":
    estadocivil = str(
        input("Estado civil inválido! Por favor, digite uma letra válida: ")
    )
