"""
EXERCÍCIO 33 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
"""

t1 = 1
t2 = 1
print(f"{t1}")
print(f"{t2}")
cont = 3

while True:
    t3 = t1 + t2
    if t3 > 500:
        print(f"{t3}")
        break
    else:
        print(f"{t3}")
        t1 = t2
        t2 = t3
        cont += 1
