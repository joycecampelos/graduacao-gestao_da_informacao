/*
EXERCÍCIO 17 - Preencher um vetor com 8 números inteiros; solicitar um número do teclado. Pesquisar se esse número existe no vetor. Se existir, imprimir em qual posição do vetor. Se não existir, imprimir que não existe.
*/

#include <stdio.h>

int main()
{
    int x, vet[8], num, achei = 0;

    for (x = 0; x < 8; x++)
    {
        printf("\nDigite um numero [%d]: ", x);
        scanf("%d", &vet[x]);
    }
    printf("\n\n");
    printf("Digite um valor a ser pesquisado: ");
    scanf("%d", &num);

    for (x = 0; x < 8; x++)
    {
        if (vet[x] == num)
        {
            printf("\nO numero %d esta na posicao: %d", num, x);
            achei = 1;
        }
    }
    if (achei != 1)
    {
        printf("\nEste numero nao existe.");
    }
    return 0;
}
