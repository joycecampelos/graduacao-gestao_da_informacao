"""
EXERCÍCIO 59 - As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:

a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; 
Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades.
Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
- O salário de cada funcionário, juntamente com o valor do abono;
- O número total de funcionário processados;
- O valor total a ser gasto com o pagamento do abono;
- O número de funcionário que receberá o valor mínimo de 100 reais;
- O maior valor pago como abono;
"""

print("      Projeção de Gastos com Abono")
print("==" * 20)
salarioscomabono = []
totalabono = abonominimo = maiorabono = cont = 0
salario = -1
while salario != 0:
    salario = float(input("Salário: "))
    if salario < 0:
        print("Informe um valor maior que 0 ou 0 para sair.")
    elif salario != 0:
        abono = salario * 0.2
        if abono <= 100:
            abono = 100
            abonominimo += 1
        totalabono += abono
        salarioscomabono.append([salario, abono])
print(f'\n{"Salário":^10} - {"Abono":^11}')
for s in salarioscomabono:
    print(f"R${s[0]:>8.2f} - R${s[1]:>8.2f}")
    if cont == 0 or s[1] > maiorabono:
        maiorabono = s[1]
    cont += 1
print(f"\nForam processados {len(salarioscomabono)} colaboradores.")
print(f"Total gasto com abonos: R$ {totalabono:.2f}.")
print(f"Valor mínimo pago a {abonominimo} colaborador(es).")
print(f"Maior valor de abono pago: R$ {maiorabono:.2f}")
