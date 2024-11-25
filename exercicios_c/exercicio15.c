/*
EXERCÍCIO 15 - Faça um programa que, para um número indeterminado de pessoas: leia a idade de cada pessoa, sendo que a leitura da idade zero indica o fim dos dados e não deve ser contabilizada. Calcule e escreva:

- o número de pessoas
- a idade média do grupo
- a menor idade e a maior idade
*/

#include <stdio.h>

int main()
{
    int idade, qntPessoa, somaIdade, maiorIdade, menorIdade;
    float mediaIdades;

    qntPessoa = 0;
    somaIdade = 0;
    maiorIdade = 0;
    menorIdade = 150;

    do
    {
        printf("\nInforme a idade: ");
        scanf("%d", &idade);
        if (idade != 0)
        {
            somaIdade = somaIdade + idade;
            if (idade > maiorIdade)
            {
                maiorIdade = idade;
            }
            if (idade < menorIdade)
            {
                menorIdade = idade;
            }
            qntPessoa++;
        }
        else
        {
            printf("\nFIM da coleta de idades...");
        }
    } while (idade != 0);

    mediaIdades = somaIdade / qntPessoa;
    printf("\n\nRELATORIO DA COLETA DE IDADES: ");
    printf("\nQuantidade de pessoas: %d", qntPessoa);
    printf("\nIdade media do grupo: %2.f", mediaIdades);
    printf("\nMaior idade do grupo: %d", maiorIdade);
    printf("\nMenor idade do grupo: %d", menorIdade);
}
