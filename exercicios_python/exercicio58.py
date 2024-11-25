"""
EXERCÍCIO 58 - Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"
As possíveis respostas são:
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

Sistema Operacional | Votos  |  %
-------------------   ------  -----
Windows Server      |  1500  | 17%
Unix                |  3500  | 40%
Linux               |  3000  | 34%
Netware             |  500   | 5%
Mac OS              |  150   | 2%
Outro               |  150   | 2%
-------------------   ------  -----
Total                  8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""

sistemaoperacionais = [
    ["Windows Server", 0],
    ["Unix", 0],
    ["Linux", 0],
    ["Netware", 0],
    ["Mac OS", 0],
    ["Outro", 0],
]
opcao = -1
totaldevotos = 0
print("Qual o melhor Sistema Operacional para uso em servidores?")
print("As possíveis respostas são:")
i = 0
for s in sistemaoperacionais:
    print(f"{i + 1} - {s[0]}")
    i += 1
while opcao != 0:
    opcao = int(input("Sistema escolhido (0 para finalizar): "))
    if opcao < 0 or opcao > 6:
        print("Informe um valor entre 1 e 6 ou 0 para finalizar.")
    elif opcao != 0:
        sistemaoperacionais[opcao - 1][1] += 1
        totaldevotos += 1
print()
print("-" * 41)
print(f'{"Sistema Operacional":<21}{"Votos":^13}{"%":^5}')
print("-" * 41)
i = 0
maiorvoto = 0
maiorvotonome = ""
for s in sistemaoperacionais:
    print(f"{s[0]:<21}{s[1]:^13}{(s[1] * 100) / totaldevotos:>5.1f}")
    if i == 0 or s[1] > maiorvoto:
        maiorvoto = s[1]
        maiorvotonome = s[0]
    i += 1
print("-" * 41)
print(f'{"Total":<21}{totaldevotos:^13}')
print(
    f"\nO Sistema Operacional mais votado foi o {maiorvotonome}, com {maiorvoto} votos, correspondendo a {(maiorvoto * 100) / totaldevotos:.1f}% dos votos."
)
