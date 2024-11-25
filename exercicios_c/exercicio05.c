/*
EXERCÍCIO 05 - Escreva um programa em C que calcule e imprima o valor de x elevado a n. O valor de n deverá ser maior do que 1 e inteiro, e o valor de x maior ou igual a 2 e inteiro.
*/

#include <stdio.h>
#include <math.h>

int main()
{
    int x, n, resultado;

    printf("Digite um numero inteiro para a base: ");
    scanf("%i", &x);
    printf("Digite um numero inteiro para o exponente: ");
    scanf("%i", &n);

    if (n > 1 && x >= 2)
    {
        resultado = pow(x, n);
        printf("O valor de x elevado a n eh %i", resultado);
    }
    else
        printf("Com esses valores nao eh possivel realizar a operacao");

    return 0;
}
