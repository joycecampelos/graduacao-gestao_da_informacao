"""
EXERCÍCIO 65 - Faça um programa que simula uma calculadora que aceita as seguintes operações: soma, subtração, divisão e multiplicação. O programa inicia pedindo para o usuário escolher uma opção do menu:
1. Somar
2. Subtrair
3. Dividir
4. Multiplicar
5. Sair	
Ao escolher a opção, o programa solicita os dois números a serem operados (exceto se a opção escolhida for a 5), efetua a operação mostra o resultado na tela e volta para o menu para que o usuário escolha outra opção.
"""

while True:
    print("1 - SOMA")
    print("2 - SUBTRAÇÃO")
    print("3 - DIVISÃO")
    print("4 - MULTIPLICAÇÃO")
    print("5 - SAIR")

    opcao = int(input("\nEscolha uma opção corresponde com o que deseja fazer: "))
    if opcao >= 1 and opcao <= 5:
        if opcao >= 1 and opcao <= 4:
            n1 = float(input("\nDigite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            if opcao == 1:
                resultado = n1 + n2
                print(f"\nResultado = {resultado:.1f}.\n")
            elif opcao == 2:
                resultado = n1 - n2
                print(f"\nResultado = {resultado:.1f}\n")
            elif opcao == 3:
                resultado = n1 / n2
                print(f"\nResultado = {resultado:.1f}\n")
            else:
                resultado = n1 * n2
                print(f"\nResultado = {resultado:.1f}\n")

            input("Pressione <enter> para realizar outra operação.\n")
        else:
            print("\nAção finalizada!")
            break
    else:
        print("\nOpção inválida! Digite novamente.\n")
