/*
EXERCÍCIO 12 - Uma fábrica possui diversos tanques cilíndricos de alturas e raios diferentes. Sabemos que para calcular o volume de um cilindro, basta multiplicar a altura (h) pela área da sua base (π * r²). Faça um programa que leia a altura e o raio e calcule o volume de um tanque. Exemplo: Entradas: “5”, “3” | Saída: “A área do tanque é de 141.37 m³”
*/

#include <stdio.h>
#include <math.h>

int main()
{
    float altura, raio, pi, resultado;

    pi = 3.14;

    printf("Digite o valor da altura: ");
    scanf("%f", &altura);
    printf("Digite o valor do raio: ");
    scanf("%f", &raio);

    resultado = altura * (pi * pow(raio, 2));

    printf("O volume do tanque e de %.2fm^3", resultado);

    return 0;
}
