/*
EXERCÍCIO 14 - Escreva um programa que leia um conjunto de números e determine se este número é par ou ímpar. O programa deverá ser encerrado se o usuário digitar 0 (zero).
*/

#include <stdio.h>

int main()
{
    int n;
    do
    {
        printf("\nDigite um numero: ");
        scanf("%d", &n);

        if (n == 0)
            printf("Saindo...");
        else if (n % 2 == 0)
            printf("%d eh PAR!", n);
        else
            printf("%d eh IMPAR!", n);
    } while (n != 0);
}
