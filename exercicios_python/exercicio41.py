"""
EXERCÍCIO 41 - Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
"""

soma = cont = 0
while True:
    idade = int(input("Informe a idade: "))
    if idade < 0 or idade > 100:
        print("Idade inválida! Tente novamente.")
    else:
        soma += idade
        cont += 1
        continuar = " "
        while continuar not in "SN":
            continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
        if continuar == "N":
            break
media = soma / cont
if media > 0 and media <= 25:
    print(f"A média da turma é {media:.2f}, então pode ser considerada JOVEM.")
elif media >= 26 and media <= 60:
    print(f"A média da turma é {media:.2f}, então pode ser considerada ADULTA.")
else:
    print(f"A média da turma é {media:.2f}, então pode ser considerada IDOSA.")
