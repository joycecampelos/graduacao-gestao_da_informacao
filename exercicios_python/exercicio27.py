"""
EXERCÍCIO 27 - Faça um programa que leia e valide as seguintes informações:
- Idade: entre 0 e 150
- Salário: maior que zero
- Sexo: 'f' ou 'm'
- Estado Civil: 's', 'c', 'v', 'd'
"""

idade = salario = 0
sexo = estadocivil = ""

while idade <= 0 or idade >= 150:
    idade = int(input("Informe sua idade: "))
    if idade <= 0 or idade >= 150:
        print("Idade incorreta!\n")

while salario <= 0:
    salario = float(input("Informe seu salário: R$"))
    if salario <= 0:
        print("Salário incorreto!\n")

while sexo != "F" and sexo != "M":
    sexo = input("Informe seu sexo (F/M): ").upper()
    if sexo != "F" and sexo != "M":
        print("Sexo incorreto!\n")

while (
    estadocivil != "S"
    and estadocivil != "C"
    and estadocivil != "V"
    and estadocivil != "D"
):
    estadocivil = input("Informe seu estado civil (S/C/V/D): ").upper()
    if (
        estadocivil != "S"
        and estadocivil != "C"
        and estadocivil != "V"
        and estadocivil != "D"
    ):
        print("Estado civil incorreto!\n")

print("\nFIM")
