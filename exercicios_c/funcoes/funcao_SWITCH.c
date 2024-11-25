#include <stdio.h>

int main()
{
    int i;

    printf("Insira um numero inteiro de 1 a 5: ");
    scanf("%i", &i);

    switch (i)
    {
    case 1:
        printf("\nPrimeiro");
        break;
    case 2:
        printf("\nSegundo");
        break;
    case 3:
        printf("\nTerceiro");
        break;
    case 4:
        printf("\nQuarto");
        break;
    case 5:
        printf("\nQuinto");
        break;
    default:
        printf("\nOpcao invalida");
        break;
    }
    return 0;
}
