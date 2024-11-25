/*
EXERCÍCIO 04 - Escreva um programa em C que entre com 3 números e imprima e quadrado de cada número.
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    float A, B, C;
    printf("Digite o primeiro valor: ");
    scanf("%f", &A);
    printf("Digite o segundo valor: ");
    scanf("%f", &B);
    printf("Digite o terceiro valor: ");
    scanf("%f", &C);

    printf("\nOs resultados de todos esses valores elevado ao quadrado eh");

    printf("\nPrimeiro: %.2f", (A * A));
    printf("\nSegundo: %.2f", (B * B));
    printf("\nTerceiro: %.2f", (C * C));

    return 0;
}
