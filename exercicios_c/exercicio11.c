/*
EXERCÍCIO 11 - Escreva um algoritmo que leia três valores (A, B e C) correspondentes aos lados de um triângulo. Verificar se os lados fornecidos formam realmente um triângulo e, caso sim, qual tipo de triângulo:
- Eqüilátero
- Isósceles
- Escaleno
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int A, B, C;

    printf("Digite o valor A: ");
    scanf("%d", &A);
    printf("Digite o valor B: ");
    scanf("%d", &B);
    printf("Digite o valor C: ");
    scanf("%d", &C);

    if (A + B >= C && A + C >= B && B + C >= A)
    {
        if (A == B && B == C && C == A)
        {
            printf("\nCom esses valores formamos um Triangulo Equilatero.");
            printf("\n");
        }
        else if (A == B || B == C || C == A)
        {
            printf("\nCom esses valores formamos um Triangulo Isosceles.");
            printf("\n");
        }
        else if (A != B && B != C && C != A)
        {
            printf("\nCom esses valores formamos um Triangulo Escaleno.");
            printf("\n");
        }
    }
    else
        printf("Nao pode ser formado um triangulo com esses valores");

    return 0;
}
