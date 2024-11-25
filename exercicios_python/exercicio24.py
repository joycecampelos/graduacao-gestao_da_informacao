"""
EXERCÍCIO 24 - Faça um programa que simule uma calculadora. Devem ser efetuadas apenas operações de soma, subtração, multiplicação e divisão. O programa deve ler dois valores (operandos) e a operação a ser efetuada. Após o cálculo, o programa apresenta a resposta na tela.
"""

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

print(
    "\nOperações possíveis: \nSOMA (+) \nSUBTRAÇÃO (-) \nMULTIPLICAÇÃO (*) \nDIVISÃO (/)"
)

operacao = input(
    "\nDigite o símbolo correspondente a operação que se deseja realizar: "
)

if operacao == "+":
    resultado = valor1 + valor2
    print(f"\nO resultado dessa soma é {resultado:.2f}.")
elif operacao == "-":
    resultado = valor1 - valor2
    print(f"\nO resultado dessa subtração é {resultado:.2f}.")
elif operacao == "*":
    resultado = valor1 * valor2
    print(f"\nO resultado dessa multiplicação é {resultado:.2f}.")
elif operacao == "/":
    resultado = valor1 / valor2
    print(f"\nO resultado dessa divisão é {resultado:.2f}.")
else:
    print("\nNão é possível realizar essa operação!")
