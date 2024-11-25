/*
EXERCÍCIO 02 - Escreva um programa em C em que seja lido um valor decimal e seja impresso esse valor com reajuste de 10%.
*/

#include <stdio.h>

int main()
{
    float decimal, resultado;

    printf("Digite um valor: ");
    scanf("%f", &decimal);

    resultado = (90 * decimal) / 100;

    printf("%.2f", resultado);

    return 0;
}
