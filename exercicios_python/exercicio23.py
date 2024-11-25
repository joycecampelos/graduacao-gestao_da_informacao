"""
EXERCÍCIO 23 - Escreva um programa para ler os valores das coordenadas cartesianas de um ponto e imprimir os valores lidos, seguidos do número (1 a 4) do quadrante em que o ponto está situado. Se o ponto estiver situado sobre um dos eixos, fornecer o valor -1. Se estiver sobre a origem, fornecer o valor 0.
_2_|_1_
 3 | 4
"""

x = float(input("Digite o valor de X: "))
y = float(input("Digite o valor de Y: "))

if x > 0 and y > 0:
    print(f"\nO ponto P({x:.1f},{y:.1f}) pertence ao 1º Quadrante.")

elif x < 0 and y > 0:
    print(f"\nO ponto P({x:.1f},{y:.1f}) pertence ao 2º Quadrante.")

elif x < 0 and y < 0:
    print(f"\nO ponto P({x:.1f},{y:.1f}) pertence ao 3º Quadrante.")

elif x > 0 and y < 0:
    print(f"\nO ponto P({x:.1f},{y:.1f}) pertence ao 4º Quadrante.")

elif x == 0 and (y > 0 or y < 0):
    print(f"\nO ponto P({x},{y:.1f}) está localizado no eixo Y.")

elif (x > 0 or x < 0) and y == 0:
    print(f"\nO ponto P({x:.1f},{y}) está localizado no eixo X.")

elif x == 0 and y == 0:
    print(f"\nO ponto P({x},{y}) está localizado na Origem.")
