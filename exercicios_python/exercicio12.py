"""
EXERCÍCIO 12 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:
• Álcool:
 - até 20 litros, desconto de 3% por litro
 - acima de 20 litros, desconto de 5% por litro
• Gasolina:
 - até 20 litros, desconto de 4% por litro
 - acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 e o preço do litro do álcool é R$ 1,90.
"""

litros = float(input("Informe a quantidade de litros vendidos: "))
tipocombustivel = input("Informe o tipo de combustível: ").upper()

if tipocombustivel == "A":
    if litros <= 20:
        preco = litros * 1.90
        precofinal = preco - (preco * (3 / 100))
        print(f"\nPreço a ser pago R${precofinal:.2f}.")
    else:
        preco = litros * 1.90
        precofinal = preco - (preco * (5 / 100))
        print(f"\nPreço a ser pago R${precofinal:.2f}.")

elif tipocombustivel == "G":
    if litros <= 20:
        preco = litros * 2.50
        precofinal = preco - (preco * (4 / 100))
        print(f"\nPreço a ser pago R${precofinal:.2f}.")
    else:
        preco = litros * 2.50
        precofinal = preco - (preco * (6 / 100))
        print(f"\nPreço a ser pago R${precofinal:.2f}.")

else:
    print("Tipo de combustível não identificado.")
