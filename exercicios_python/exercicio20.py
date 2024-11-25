"""
EXERCÍCIO 20 - Escreva um programa que leia o salário fixo de um vendedor de uma loja e o valor total de vendas efetuadas por ele no mês. Acrescente ao salário um prêmio, conforme a tabela a seguir:
Total de Vendas no Mês (v)  | Prêmio
  1000 < v ≤ 5000           |  500,00
  5000 < v ≤ 7500           |  700,00
  v > 7500                  |  1000,00
O programa deve calcular e informar o salário final do vendedor e qual foi o prêmio recebido.
"""

salariofixo = float(input("Informe o valor do sálario fixo do vendedor: R$"))
valorvendas = float(input("Informe o valor das vendas realizadas pelo vendedor: R$"))

if valorvendas > 1000 and valorvendas <= 5000:
    salariototal = salariofixo + 500
    print(
        f"\nO salário final do vendedor será de R${salariototal:.2f}, pois obteve um total de vendas de R${valorvendas:.2f} e ganhou o prêmio de R$500,00!"
    )
elif valorvendas > 5000 and valorvendas <= 7500:
    salariototal = salariofixo + 700
    print(
        f"\nO salário final do vendedor será de R${salariototal:.2f}, pois obteve um total de vendas de R${valorvendas:.2f} e ganhou o prêmio de R$700,00!"
    )
elif valorvendas > 7500:
    salariototal = salariofixo + 1000
    print(
        f"\nO salário final do vendedor será de R${salariototal:.2f}, pois obteve um total de vendas de R${valorvendas:.2f} e ganhou o prêmio de R$1000,00!"
    )
else:
    print(
        f"\nO vendedor teve um total de vendas muito baixo, não ganhará prêmio, somente o salário fixo de R${salariofixo:.2f}"
    )
