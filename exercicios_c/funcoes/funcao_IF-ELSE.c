#include <stdio.h>

int main()
{
    int idade;

    printf("Favor informar idade: ");
    scanf("%i", &idade);

    if (idade < 18)
    {
        printf("\nBebidas alcoolicas nao estao liberadas.\n");
    }
    else
    {
        printf("\nBebidas alcoolicas liberadas.\n");
    }

    return 0;
}
