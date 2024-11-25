"""
EXERCÍCIO 03 - Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
Onde: h = altura em metros
Peça o peso da pessoa e informe se ela está acima ou abaixo do peso.
"""

altura = float(input("Informe sua altura (em metros): "))
sexo = input("Informe seu sexo (F/M): ").upper()

if sexo == "F":
    pesoideal = (62.1 * altura) - 44.7
    peso = float(input("Informe seu peso: "))
    if peso > pesoideal:
        print("Você está acima do peso ideal!")
    elif peso == pesoideal:
        print("Você está com o peso ideal!")
    else:
        print("Você está abaixo do peso ideal!")
elif sexo == "M":
    pesoideal = (72.7 * altura) - 58
    peso = float(input("Informe seu peso: "))
    if peso > pesoideal:
        print("Você está acima do peso ideal!")
    elif peso == pesoideal:
        print("Você está com o peso ideal!")
    else:
        print("Você está abaixo do peso ideal!")
else:
    print("\nDados incorretos! Digite novamente.")
