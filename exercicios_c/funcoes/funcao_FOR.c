#include <stdio.h>

int main()
{
    int clientes;
    char nome[30];

    for (clientes = 1; clientes <= 5; clientes = clientes + 1)
    {
        printf("Digite o nome do cliente: ");
        gets(nome);
    }
    return 0;
}
