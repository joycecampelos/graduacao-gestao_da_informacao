/*
EXERCÍCIO 18 - Preencha um vetor A com todos os números pares de 1 até 50 e um vetor B com todos os números ímpares de 1 até 50. Em seguida, preencha o vetor C com a soma dos elementos presentes em A e B, em suas respectivas posições.

- Ex.: A[0] = 2; B[0] = 1; C[0] = 2 + 1 = 3;
*/

#include <stdio.h>

int main()
{
    int A[25], B[25], C[25], x, posVetor, num;

    for (x = 0; x < 50; x++)
    {
        posVetor = x / 2;
        if ((x + 1) % 2 == 0)
        {
            A[posVetor] = x + 1;
        }
        else
        {
            B[posVetor] = x + 1;
        }
    }
    for (x = 0; x < 25; x++)
    {
        C[x] = A[x] + B[x];
    }
    printf("Vetor A: \n");
    for (x = 0; x < 25; x++)
    {
        printf("%d, ", A[x]);
    }
    printf("\n\nVetor B: \n");
    for (x = 0; x < 25; x++)
    {
        printf("%d, ", B[x]);
    }
    printf("\n\nVetor C: \n");
    for (x = 0; x < 25; x++)
    {
        printf("%d, ", C[x]);
    }
    return 0;
}
