/*
A ideia do projeto é a execução de uma calculadora financeira, com o objetivo de fornecer ao usuário o rendimento total do capital investido em um determinado tempo e em diferentes formas e para isso, o programa pede o valor do capital, o tempo e o tipo de investimento desejado.
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h> /* Biblioteca para variáveis bool (lógicas) */
#include <math.h>    /*Biblioteca para funções matemáticas*/
#include <string.h>  /* Biblioteca para manipulação de strings*/

/*Função para calcular os juros*/
float jurosC(float montante, int ano, float taxa)
{
    montante = montante * pow(1 + taxa, ano);
    return montante;
}

/*Função para verificar o capital*/
float receberDados(float min, float max)
{
    int i;
    float capital = 0, dado;
    bool verifica = true, verifica2 = true;
    char aux[20];

    do
    {
        printf("\nDigite o capital inicial:\n R$ ");
        gets(aux);
        verifica2 = true;
        for (i = 0; i < aux[i]; i++)
        {
            if (aux[i] < 48 && aux[i] > 57)
                verifica2 = false;
        }
        if (verifica2)
            capital = atof(aux);
        else
            capital = 0;
        if (capital >= 1)
            verifica = false;
        else
            printf("\nPor favor, digitar um capital valido!\n\n");
    } while (verifica);
    return capital;
}

/*Função para verificar o tempo*/
float receberTempo(float min, float max)
{
    int tempo = 0, i, dado;
    bool verifica = true, verifica2 = true;
    char aux[20];

    do
    {
        printf("\nDigite o tempo em anos (Limite = 100):\n ");
        gets(aux);
        verifica2 = true;
        for (i = 0; aux[i] != 0; i++) // For no lugar de while
        {
            if (aux[i] < 48 && aux[i] > 57)
                verifica2 = false;
        }
        if (verifica2)
            tempo = atoi(aux);
        else
            tempo = 0;
        if (tempo >= 1 && tempo <= 100)
            verifica = false;
        else
            printf("\nPor favor, digitar um tempo valido!\n\n");
    } while (verifica);
    return tempo;
}

int main()
{
    /* Declaração das variáveis */
    int tempo = 0, i, cont; /* Variavel "cont" para validar continuação do programa no final */
    float capital = 0, taxas[5] = {0.085, 0.14, 0.17, 0.20, 0.144}, min, max;
    bool verifica = true, verifica2 = true;
    char aux[20], investimento;

    do
    {
        printf("Calculadora Finaceira\n");

        capital = receberDados(min, max);
        tempo = receberTempo(min, max);

        while (verifica) /* Esse verifica se o número do investimento está correto*/
        {
            /*Menu com os tipos de investimentos*/
            printf("\nTipos de investimentos:");
            printf("\n\n1 - Poupanca");
            printf("\n2 - Tesouro Direto");
            printf("\n3 - CDB");
            printf("\n4 - Bovespa");
            printf("\n5 - Titulo de Capital");

            printf("\n\nDigite o numero correspondente ao investimento desejado: ");
            scanf("%c", &investimento);

            switch (investimento)
            {
            case '1':
                printf("\nO rendimento final e de R$%.2f \n", jurosC(capital, tempo, taxas[0]));
                verifica = false;
                break;
            case '2':
                printf("\nO rendimento final e de R$%.2f \n", jurosC(capital, tempo, taxas[1]));
                verifica = false;
                break;
            case '3':
                printf("\nO rendimento final e de R$%.2f \n", jurosC(capital, tempo, taxas[2]));
                verifica = false;
                break;
            case '4':
                printf("\nO rendimento final e de R$%.2f \n", jurosC(capital, tempo, taxas[3]));
                verifica = false;
                break;
            case '5':
                printf("\nO rendimento final e de R$%.2f \n", jurosC(capital, tempo, taxas[4]));
                verifica = false;
                break;

            default:
                verifica = true;
                printf("\n\nPOR FAVOR DIGITE O NUMERO CORRESPONDENTE.\n");
                fflush(stdin); /*Limpa o buffer*/
            }
        }

        /*Opção para o usuário continuar usando a calculadora ou finalizar*/
        do
        {
            printf("\nDigite 1 para realizar outra operacao ou 0 para finalizar o programa: ");
            scanf("%i", &cont);
        } while (cont < 0 || cont > 1);
        if (cont == 1)
        {
            verifica = true;
            system("cls"); /* limpa a tela */
        }
        fflush(stdin); /*Limpa o buffer, para não dar erro na próxima execução (na primeira variavel entrada)*/
    } while (verifica);
    return 0;
}
