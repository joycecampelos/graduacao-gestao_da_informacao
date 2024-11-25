/*
EXERCÍCIO 10 - Sabendo que A=5, B=4 e C=3 e D=6, construa um código em C para verificar se as expressões abaixo são verdadeiras ou falsas:
a) (A > C) E (C <= D) ( )
b) (A+B) > 10 OU ((A+B) = (D-C)) ( )
c) (A>=C) E (D >= C) ( )
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int A = 5, B = 4, C = 3, D = 6;

    printf((A > C) && (C <= D) ? "Verdadeiro" : "Falso");
    printf("\n");
    printf(((A + B) > 10) || ((A + B) == (D - C)) ? "Verdadeiro" : "Falso");
    printf("\n");
    printf((A >= C) && (D >= C) ? "Verdadeiro" : "Falso");

    return 0;
}
