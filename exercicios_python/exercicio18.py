"""
EXERCÍCIO 18 - Faça um programa que calcule as seguintes conversões entre sistemas de medida:
(a) dada uma temperatura na escala Celcius, fornecer a temperatura equivalente em graus	Farenheit e vice-versa (Fórmula de conversão: F = (9/5) * C + 32.
(b) dada uma medida em polegadas, fornecer a equivalente em milímetros e vice-versa (Fórmula de conversão: 1 pol = 25,4 mm).
O programa deve mostrar uma tela com as quatro conversões de sistema de medida possíveis, perguntando qual deverá ser realizada. Em seguida, deve ler um valor e informá-lo após a conversão como resposta.
"""

print("1 - CELSIUS para FARENHEIT.")
print("2 - FARENHEIT para CELSIUS.")
print("3 - POLEGADAS para MILÍMETROS.")
print("4 - MILÍMETROS para POLEGADAS.")

opcao = int(input("\nDigite a opção corresponde a conversão que deseja realizar: "))

if opcao == 1:
    print("\n-----CELSIUS para FARENHEIT-----")
    c = float(input("Informe a temperatura em ºC: "))
    print(f"A temperatura de {c:.1f}ºC corresponde a {((9 * c) / 5) + 32:.1f}ºF.")
elif opcao == 2:
    print("\n-----FARENHEIT para CELSIUS-----")
    f = float(input("Informe a temperatura em ºF: "))
    print(f"A temperatura de {f:.1f}ºF corresponde a {((f - 32) * 5) / 9:.1f}ºC.")
elif opcao == 3:
    print("\n-----POLEGADAS para MILÍMETROS-----")
    p = float(input("Informe a medida em polegadas: "))
    print(f"A medida de {p:.1f} polegadas corresponde a {p * 25.4:.1f}mm.")
elif opcao == 4:
    print("\n-----MILÍMETROS para POLEGADAS-----")
    mm = float(input("Informe a medida em milímetros: "))
    print(f"A medida de {mm:.1f}mm corresponde a {mm / 25.4:.1f} polegadas.")
else:
    print("")
    print("=" * 15)
    print("Opção inválida!")
    print("=" * 15)
