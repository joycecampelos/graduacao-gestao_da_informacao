/*
EXERCÍCIO 07 - Escreva um programa em C em que sejam lidas a base e altura de um retângulo e seja impressa a seguinte saída:
a) Perímetro
b) Área
c) Diagonal
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    float base, altura, perimetro, area, diagonal;

    printf("Digite o valor da base do retangulo: ");
    scanf("%f", &base);
    printf("Digite o valor da altura do retangulo: ");
    scanf("%f", &altura);

    perimetro = (2 * base) + (2 * altura);
    printf("\nO valor do perimetro do retangulo eh %f", perimetro);
    area = base * altura;
    printf("\nO valor da area do retangulo eh %f", area);
    diagonal = sqrt((pow(base, 2)) + (pow(altura, 2)));
    printf("\nO valor da diagonal do retangulo eh %f", diagonal);

    return 0;
}
