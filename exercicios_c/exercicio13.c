/*
EXERCÍCIO 13 - Crie um programa que some o tempo de duração (em minutos) das 3 voltas de um corredor e retorne o tempo total da prova, bem como qual das voltas foi a mais rápida. Exemplo: Entradas: “7”, “9”, “5”| Saída: “Total: 21m. Mais rápida: 3ª volta”.
*/

#include <stdio.h>

int main()
{
    float tempo1, tempo2, tempo3, soma;

    printf("Digite o tempo da primeira volta: ");
    scanf("%f", &tempo1);

    printf("Digite o tempo da segunda volta: ");
    scanf("%f", &tempo2);

    printf("Digite o tempo da terceira volta: ");
    scanf("%f", &tempo3);

    soma = tempo1 + tempo2 + tempo3;
    if (tempo1 < tempo2 && tempo1 < tempo3)
    {
        printf("Total: %.2f m. Mais rapida: Primeira volta.", soma);
    }
    else if (tempo2 < tempo1 && tempo2 < tempo3)
    {
        printf("Total: %.2f m. Mais rapida: Segunda volta.", soma);
    }
    else if (tempo3 < tempo1 && tempo3 < tempo2)
    {
        printf("Total: %.2f m. Mais rápida: Terceira volta.", soma);
    }
    else
        printf("Total: %.2f m. Nao eh possivel saber qual volta foi mais rapida.", soma);
    return 0;
}
