"""
EXERCÍCIO 21 - Escreva um programa que recebe como entrada a data de nascimento do usuário, e informa qual o seu signo.
"""

dia = int(input("Informe o dia que você nasceu: "))
mes = int(input("Informe o mês que você nasceu: "))

if dia >= 21 and dia <= 31 and mes == 3 or dia >= 1 and dia <= 20 and mes == 4:
    print("\nVocê é do signo de Áries!♈")
elif dia >= 21 and dia <= 30 and mes == 4 or dia >= 1 and dia <= 20 and mes == 5:
    print("\nVocê é do signo de Touro!♉")
elif dia >= 21 and dia <= 31 and mes == 5 or dia >= 1 and dia <= 20 and mes == 6:
    print("\nVocê é do signo de Gêmeos!♊")
elif dia >= 21 and dia <= 30 and mes == 6 or dia >= 1 and dia <= 21 and mes == 7:
    print("\nVocê é do signo de Câncer!♋")
elif dia >= 22 and dia <= 31 and mes == 7 or dia >= 1 and dia <= 22 and mes == 8:
    print("\nVocê é do signo de Leão!♌")
elif dia >= 23 and dia <= 31 and mes == 8 or dia >= 1 and dia <= 22 and mes == 9:
    print("\nVocê é do signo de Virgem!♍")
elif dia >= 23 and dia <= 30 and mes == 9 or dia >= 1 and dia <= 22 and mes == 10:
    print("\nVocê é do signo de Libra!♎")
elif dia >= 23 and dia <= 31 and mes == 10 or dia >= 1 and dia <= 21 and mes == 11:
    print("\nVocê é do signo de Escorpião!♏")
elif dia >= 22 and dia <= 30 and mes == 11 or dia >= 1 and dia <= 21 and mes == 12:
    print("\nVocê é do signo de Sagitário!♐")
elif dia >= 22 and dia <= 31 and mes == 12 or dia >= 1 and dia <= 20 and mes == 1:
    print("\nVocê é do signo de Capricórnio!♑")
elif dia >= 21 and dia <= 31 and mes == 1 or dia >= 1 and dia <= 19 and mes == 2:
    print("\nVocê é do signo de Aquário!♒")
elif dia >= 20 and dia <= 29 and mes == 2 or dia >= 1 and dia <= 20 and mes == 3:
    print("\nVocê é do signo de Peixes!♓")
else:
    print("\nData inválida!")
