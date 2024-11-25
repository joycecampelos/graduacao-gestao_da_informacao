"""
EXERCÍCIO 52 - O cardápio de uma lanchonete é o seguinte:

| Especificação | Código | Preço
|Cachorro Quente|  100   |R$ 1,20
|Bauru Simples  |  101   |R$ 1,30
|Bauru com ovo  |  102   |R$ 1,50
|Hambúrguer     |  103   |R$ 1,20
|Cheeseburguer  |  104   |R$ 1,30
|Refrigerante   |  105   |R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""

total = 0
while True:
    código = int(input("Código do pedido (para finalizar digite [0]): "))
    if código == 0:
        break
    quantidade = int(input("Quantidade: "))

    if código == 100:
        cachorroquente = 1.20 * quantidade
        print(f"Cachorro Quente: R$ {cachorroquente:.2f}.")
        total += cachorroquente
    elif código == 101:
        baurusimples = 1.30 * quantidade
        print(f"Bauru Simples: R$ {baurusimples:.2f}.")
        total += baurusimples
    elif código == 102:
        baurucomovo = 1.50 * quantidade
        print(f"Bauru com Ovo: R$ {baurucomovo:.2f}.")
        total += baurucomovo
    elif código == 103:
        hamburguer = 1.20 * quantidade
        print(f"Hambúrguer: R$ {hamburguer:.2f}.")
        total += hamburguer
    elif código == 104:
        cheeseburguer = 1.30 * quantidade
        print(f"Cheeseburguer: R$ {cheeseburguer:.2f}.")
        total += cheeseburguer
    elif código == 105:
        refrigerante = 1 * quantidade
        print(f"Refrigerante: R$ {refrigerante:.2f}.")
        total += refrigerante
    else:
        print("Código inválido! Tente novamente.")

    print()
print(f"\nTotal dos pedidos: R$ {total:.2f}.")
