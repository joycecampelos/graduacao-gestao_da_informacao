/*
EXERCÍCIO 06 - Escreva um programa em C em que seja lida a temperatura em graus centígrados e ela seja convertida em graus Fahrenheit. A fórmula de conversão é: F = C * 1,8 + 32, onde F é a temperatura em Fahrenheit e C é a temperatura em centígrados.
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    double C, F;

    printf("Digite uma temperatura em centigrados: ");
    scanf("%lf", &C);

    F = C * 1.8 + 32;

    printf("\nO valor em centigrados digitado foi %.2f", C);
    printf("\nO valor convertido em graus Fahrenheit eh %.2f", F);

    return 0;
}
