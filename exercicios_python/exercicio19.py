"""
EXERCÍCIO 19 - Construa um programa que recebe o número de cadastro (inteiro) de três clientes de uma loja e o valor (em reais) que cada um desses clientes pagou por sua compra. O programa deverá informar:
(a) o valor total pago pelos três clientes
(b) o valor da compra média efetuada
(c) o número de cadastro dos clientes que efetuaram compras superiores a 100 reais
(d) quantos clientes efetuaram compras inferiores a 50 reais
"""

cliente1 = int(input("Informe o número de cadastro do primeiro cliente: "))
valor1 = float(input("Informe o valor pago por esse cliente: R$"))
cliente2 = int(input("\nInforme o número de cadastro do segundo cliente: "))
valor2 = float(input("Informe o valor pago por esse cliente: R$"))
cliente3 = int(input("\nInforme o número de cadastro do terceiro cliente: "))
valor3 = float(input("Informe o valor pago por esse cliente: R$"))

valortotal = valor1 + valor2 + valor3
print(f"\nO valor total pago pelos três clientes é R${valortotal:.2f}.")
valormedio = valortotal / 3
print(f"O valor médio das compras efetuadas é R${valormedio:.2f}.")

print("\nNúmero de cadastro dos clientes que realizaram compras acima de R$100,00:")
if valor1 > 100 or valor2 > 100 or valor3 > 100:
    if valor1 > 100:
        print("-", cliente1)
    if valor2 > 100:
        print("-", cliente2)
    if valor3 > 100:
        print("-", cliente3)
else:
    print("Nenhum cliente realizou compras acima de R$100,00.")

print("\nQuantidade de clientes que efetuaram compras inferiores a R$50,00: ", end="")
if valor1 < 50 or valor2 < 50 or valor3 < 50:
    inferior = 0
    if valor1 < 50:
        inferior += 1
    if valor2 < 50:
        inferior += 1
    if valor3 < 50:
        inferior += 1
    print(f"{inferior} cliente(s).")
else:
    print("\nNenhum cliente realizou compras abaixo de R$50,00.")
