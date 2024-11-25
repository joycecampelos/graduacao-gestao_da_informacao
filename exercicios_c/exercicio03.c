/*
EXERCÍCIO 03 - Escreva um programa em C em que sejam declaradas duas variáveis A e B do tipo Inteiro (int). Em seguida, atribua valores a elas e imprima o resultado das seguintes operações: A+B; A-B; A*B, A/B e A%B.
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
   int A, B;

   printf("Digite o valor de A: ");
   scanf("%i", &A);
   printf("Digite o valor de B: ");
   scanf("%i", &B);

   printf("\nResultados das Operacoes");
   printf("\n\nSoma = %i", A + B);
   printf("\nSubtracao = %i", A - B);
   printf("\nMultiplicacao = %i", A * B);
   printf("\nDivisao = %i", A / B);
   printf("\nResto da Divisao = %i", A % B);

   return 0;
}
