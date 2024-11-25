#include <stdio.h>

int main()
{
    int base;
    int altura;
    int area;

    printf("\t\t\tCalcule o valor da area\n\n");

    printf("Digite o valor da base: ");
    scanf("%i", &base);

    printf("Digite o valor da altura: ");
    scanf("%i", &altura);

    area = base * altura;
    printf("\nO valor da area e' = %i\n", area);

    return 0;
}
