"""
EXERCÍCIO 32 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo ( o valor de n deve ser informado pelo usuário)
"""

n = int(input("Quantos termos da série de Fibonacci você quer mostrar? "))
t1 = 1
t2 = 1
print(f"{t1}")
print(f"{t2}")
cont = 3

while cont <= n:
    t3 = t1 + t2
    print(f"{t3}")
    t1 = t2
    t2 = t3
    cont += 1
