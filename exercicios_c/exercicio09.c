/*
EXERCÍCIO 09 - Elabore um algoritmo que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
- Infantil: 5 a 10 anos;
- Juvenil: 11 a 17 anos;
- Sênior: 18 anos ou mais.
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("Qual categoria voce se encaixa?");
    int idade;
    printf("\nDigite sua idade: ");
    scanf("%i", &idade);

    if (idade >= 5 && idade <= 10)  {
        printf("\nVoce se encaixa na categoria infantil!");
        printf("\n");
    }
    if (idade >= 11 && idade <= 17) {
        printf("\nVoce se encaixa na categoria juvenil!");
        printf("\n");
    }
    if (idade >=18) {
        printf("\nVoce se encaixa na categoria senior!");
        printf("\n");
    }
    if (idade <5) {
        printf("\nVoce nao tem idade pra ser nadador!");
        printf("\n");
    }
    return 0;
}
