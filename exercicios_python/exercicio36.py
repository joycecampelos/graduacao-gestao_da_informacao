"""
EXERCÍCIO 36 - Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""

cont = maior = menor = soma = 0
while True:
    num = int(input("Digite um número: "))
    if num < 0 or num > 1000:
        print("Número inválido! Por favor, digite números entre 0 e 1000.")
    else:
        if cont == 0 or num > maior:
            maior = num
        if cont == 0 or num < menor:
            menor = num
        soma += num
        cont += 1

        continuar = " "
        while continuar not in "SN":
            continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
        if continuar == "N":
            break

print(
    f"""O maior valor digitado foi {maior}.
O menor valor digitado foi {menor}.
A soma dos valores digitados é {soma}."""
)
