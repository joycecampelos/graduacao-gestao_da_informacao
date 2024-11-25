"""
EXERCÍCIO 09 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
• Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve pedir os demais valores, sendo encerrado.
• Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa.
• Se o delta calculado for igual a zero a equação possui apenas uma raiz real. Informe-a ao usuário.
• Se o delta for positivo, a equação possui duas raizes reais. Informe-as ao usuário.
"""

a = int(input("Informe o valor de A: "))

if a == 0:
    print(
        "O valor de A é igual a zero, o que faz com que a equação não seja mais de segundo grau."
    )
else:
    b = int(input("Informe o valor de B: "))
    c = int(input("Informe o valor de C: "))

    delta = (b**2) - (4 * a * c)

    if delta < 0:
        print("\nA equação não possui raízes reais.")
    elif delta == 0:
        x = (b * (-1)) / (2 * a)
        print(f"\nA equação possui apenas uma raiz real, que é {x:.0f}.")
    else:
        x1 = ((b * (-1)) + (delta**0.5)) / (2 * a)
        x2 = ((b * (-1)) - (delta**0.5)) / (2 * a)
        print(f"\nA equação possui duas raízes reais, que são {x1:.0f} e {x2:.0f}.")
