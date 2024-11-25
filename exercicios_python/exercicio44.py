"""
EXERCÍCIO 44 - O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
"""

while True:
    print("Lojas Tabajara")
    cont = 1
    soma = 0
    while True:
        preço = float(input(f"Produto {cont}: R$ "))
        if preço == 0:
            break
        else:
            cont += 1
            soma += preço
    print(f"Total: R$ {soma:.2f}")
    dinheirocliente = float(input("Dinheiro: R$ "))
    print(f"Troco: R$ {dinheirocliente - soma:.2f}")

    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer registrar outra compra? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
    print()
print("PROGRAMA FINALIZADO!")
