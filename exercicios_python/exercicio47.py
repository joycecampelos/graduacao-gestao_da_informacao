"""
EXERCÍCIO 47 - Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
"""

códigoalto = códigobaixo = maisalto = maisbaixo = somaaltura = cont = 0
códigogordo = códigomagro = maisgordo = maismagro = somapeso = 0
while True:
    código = int(input("Código: "))
    if código == 0:
        break
    altura = float(input("Altura: "))
    peso = float(input("Peso: "))
    somaaltura += altura
    somapeso += peso
    if cont == 0 or altura > maisalto:
        maisalto = altura
        códigoalto = código
    if cont == 0 or altura < maisbaixo:
        maisbaixo = altura
        códigobaixo = código
    if cont == 0 or peso > maisgordo:
        maisgordo = peso
        códigogordo = código
    if cont == 0 or peso < maismagro:
        maismagro = peso
        códigomagro = código
    cont += 1
    print()
mediaaltura = somaaltura / cont
mediapeso = somapeso / cont
print(f"O cliente com o código {códigoalto}, é o mais alto com {maisalto}m de altura.")
print(
    f"O cliente com o código {códigobaixo}, é o mais baixo com {maisbaixo}m de altura."
)
print(f"O cliente com o código {códigogordo}, é o mais gordo com {maisgordo}Kg.")
print(f"O cliente com o código {códigomagro}, é o mais magro com {maismagro}Kg.")
print(
    f"A média de altura e peso dos cliente, respectivamente, é {mediaaltura:.1f}m e {mediapeso:.1f}Kg."
)
