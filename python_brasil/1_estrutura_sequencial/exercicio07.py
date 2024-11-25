"""
EXERCÍCIO 07 - Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""

lados = int(input("Digite o valor de um dos lados do quadrado: "))
area = pow(lados, 2)
print(
    f"""A área do quadrado é {area} cm².
E o dobro da área é {area * 2} cm²."""
)
