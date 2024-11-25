#include <stdio.h>

int main()
{
    int idade;

    printf("Informar idade: ");
    scanf("%i", &idade);

    if (idade <= 5)
    {
        printf("\nBebe\n");
    }
    else if (idade > 5 && idade <= 10)
    {
        printf("\nCrianca\n");
    }
    else if (idade > 10 && idade <= 18)
    {
        printf("\nAdolescente\n");
    }
    else if (idade > 18 && idade <= 50)
    {
        printf("\nAdulto\n");
    }
    else
    {
        printf("\nIdoso\n");
    }
    return 0;
}
