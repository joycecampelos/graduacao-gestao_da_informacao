/*
EXERCÍCIO 08 - Escreva um programa que leia uma estação do ano e informe ao usuário qual o período que aquela estação ocorre.
(P) - Primavera: Setembro a Dezembro.
(V) - Verão: Dezembro a Março.
(O) - Outono: Março a Junho.
(I) - Inverno: Junho a Setembro.
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    char estacao;
    printf ("Estacoes: \n Primavera - P \n Verao - V \n Outono - O \n Inverno - I");
    printf ("\n\n Digite a letra indicada para saber a duracao da estacao desejada:");
    scanf ("%c", &estacao);

    switch(estacao)
    {
    case 'P':
    case 'p':
        printf ("\n Estacao Primavera: De Setembro a Dezembro \n");
        break;
    case 'V':
    case 'v':
        printf ("\n Estacao Verao: De Dezembro a Marco \n");
        break;
    case 'O':
    case 'o':
        printf ("\n Estacao Outono: De Marco a Junho \n");
        break;
    case 'I':
    case 'i':
        printf ("\n Estacao Inverno: De Junho a Setembro \n");
        break;
        default:
            printf ("\n Estacao nao encontrada \n");
    }
    return 0;
}
