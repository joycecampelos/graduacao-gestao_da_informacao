#include <stdio.h>

int main()
{
    char nome[20];
    char sobrenome[20];

    printf("Insira seu nome e sobrenome: ");
    scanf("%s%s", &nome, &sobrenome);

    printf("\nSeu nome e' %s %s\n", nome, sobrenome);

    return 0;
}
