"""
EXERCÍCIO 48 - Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
- Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
- Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
- A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
"""

from datetime import date

ano = date.today().year
percentual = 1.5
salárioinicial = float(input("Informe o salário inicial: "))

for c in range(1995, ano + 1):
    saláriocomaumento = salárioinicial + (salárioinicial * percentual / 100)
    # print(f'Ano {c} - R$ {saláriocomaumento:.2f}')
    percentual = percentual * 2
print(f"Salário atual: R$ {saláriocomaumento:.2f}")
