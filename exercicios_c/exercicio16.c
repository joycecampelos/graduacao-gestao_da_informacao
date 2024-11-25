/*
EXERCÍCIO 16 - Um número inteiro x é perfeito se a soma de seus fatores (divisores, exceto ele mesmo, é igual a x. Por exemplo, 6 é perfeito visto que 1 + 2 +3 = 6. Escreva um programa para informar se x é um número perfeito.
*/

#include <stdio.h>

int main()
{
    int x, i, soma;

    soma = 0;

    printf("Informe o numero: ");
    scanf("%d", &x);

    for (i = 1; i <= x / 2; i++)
    {
        if (x % i == 0)
        {
            soma = soma + i;
        }
    }
    if (soma == x)
    {
        printf("\n%d eh um numero PERFEITO!", x);
    }
    else
    {
        printf("\n%d NAO eh numero PERFEITO!", x);
    }
    return 0;
}
