"""
EXERCÍCIO 22 - Faça um programa que converta um número inteiro positivo para a notação de números romanos, considerando os seguintes símbolos romanos: I, V, X, L, C, D, M.
"""

e = int(input("Digite um número entre 1 e 3999: "))

if e > 0 and e <= 3999:
    a = int(e / 1000) * 1000
    b = (int(e / 100) % 10) * 100
    c = (int(e / 10) % 10) * 10
    d = int(e / 1) % 10

    print(f"\nO número {e} é representado em números romanos como ", end="")

    if a == 1000:
        print("M", end="")
    elif a == 2000:
        print("MM", end="")
    elif a == 3000:
        print("MMM", end="")

    if b == 100:
        print("C", end="")
    elif b == 200:
        print("CC", end="")
    elif b == 300:
        print("CCC", end="")
    elif b == 400:
        print("CD", end="")
    elif b == 500:
        print("D", end="")
    elif b == 600:
        print("DC", end="")
    elif b == 700:
        print("DCC", end="")
    elif b == 800:
        print("DCCC", end="")
    elif b == 900:
        print("CM", end="")

    if c == 10:
        print("X", end="")
    elif c == 20:
        print("XX", end="")
    elif c == 30:
        print("XXX", end="")
    elif c == 40:
        print("XL", end="")
    elif c == 50:
        print("L", end="")
    elif c == 60:
        print("LX", end="")
    elif c == 70:
        print("LXX", end="")
    elif c == 80:
        print("LXXX", end="")
    elif c == 90:
        print("XC", end="")

    if d == 1:
        print("I", end="")
    elif d == 2:
        print("II", end="")
    elif d == 3:
        print("III", end="")
    elif d == 4:
        print("IV", end="")
    elif d == 5:
        print("V", end="")
    elif d == 6:
        print("VI", end="")
    elif d == 7:
        print("VII", end="")
    elif d == 8:
        print("VIII", end="")
    elif d == 9:
        print("IX", end="")
    print(".")
else:
    print("\nNúmero inválido!")
