/*
EXERCÍCIO 01 - Escreva um programa em C em que sejam declaradas variáveis dos tipos Inteiro (int), Decimal (float), Caractere (char), Cadeia (vetor de char). Posteriormente, deve-se atribuir valor a cada uma delas por meio da função scanf e imprimir seus valores.
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int inteiro;
    float decimal;
    char caractere, cadeia[50];

    printf("Digite sua idade: ");
    scanf("%d", &inteiro);
    printf("Digite seu peso: ");
    scanf("%f", &decimal);
    printf("Digite a inicial do seu nome: ");
    scanf(" %c", &caractere);
    printf("Digite seu nome: ");
    scanf("%s", &cadeia);

    printf("\nSeu nome eh %s.", cadeia);
    printf("\nVoce tem %d anos.", inteiro);
    printf("\nPesa %.2f kilogramas.", decimal);
    printf("\nLetra inicial do seu nome e %c.", caractere);

    return 0;
}
