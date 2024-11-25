#include <stdio.h>

int main()
{
    int idade;
    float peso, altura;
    char nome[20];

    printf("Preencha sua ficha corretamente:\n\n");

    printf("Seu nome: ");
    gets(nome);

    printf("Sua idade: ");
    scanf("%i", &idade);

    printf("Sua altura: ");
    scanf("%f", &altura);

    printf("Seu peso: ");
    scanf("%f", &peso);

    printf("\nParabens! %s voce foi cadrastada com sucesso.\n", nome);

    return 0;
}
