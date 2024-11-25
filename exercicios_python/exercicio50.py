"""
EXERCÍCIO 50 - Foi realizada uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
- Código da cidade;
- Número de veículos de passeio (em 1999);
- Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
- Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
- Qual a média de veículos nas cinco cidades juntas;
- Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos
de passeio.
"""

maior = menor = codigomaior = codigomenor = somaveiculos = somaacidentes = cont = 0
for c in range(0, 5):
    código = input("Código da cidade: ")
    numveículos = int(input("Número de veículos de passeio (em 1999): "))
    numacidentes = int(input("Número de acidentes de trânsito com vítimas (em 1999): "))

    if c == 0 or numacidentes > maior:
        maior = numacidentes
        codigomaior = código
    if c == 0 or numacidentes < menor:
        menor = numacidentes
        codigomenor = código

    somaveiculos += numveículos

    if numveículos < 2000:
        somaacidentes += numacidentes
        cont += 1
    print()
mediaveiculos = somaveiculos / 5
mediaacidentes = somaacidentes / cont
print(
    f"""A cidade {codigomaior} tem maior índice de acidentes de trânsito, de {maior}.
A cidade {codigomenor} tem menor índice de acidentes de trânsito, de {menor}.
A média de veículos das cidades é {mediaveiculos:.1f}.
E a média de acidentes de trânsito nas cidades com menos de 2000 veículos é {mediaacidentes:.1f}."""
)
