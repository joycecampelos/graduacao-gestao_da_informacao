"""
EXERCÍCIO 04 - Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o imposto de renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
◦ salário bruto.
◦ quanto pagou ao INSS.
◦ quanto pagou ao sindicato.
◦ o salário líquido.
Calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário líquido : R$
Obs.: salário bruto - descontos = salário líquido.
"""

valorporhora = float(input("Informe o valor que ganha por hora: R$"))
horastrabalhadas = int(input("Informe as horas trabalhadas no mês: "))

salariobruto = valorporhora * horastrabalhadas
impostorenda = salariobruto * (11 / 100)
inss = salariobruto * (8 / 100)
sindicato = salariobruto * (5 / 100)
salarioliquido = salariobruto - impostorenda - inss - sindicato

print(f"\nSalário Bruto: R${salariobruto:.2f}.")
print(f"IR (11%): R${impostorenda:.2f}.")
print(f"INSS (8%): R${inss:.2f}.")
print(f"Sindicato (5%): R${sindicato:.2f}.")
print(f"Salário Líquido: R${salarioliquido:.2f}")
