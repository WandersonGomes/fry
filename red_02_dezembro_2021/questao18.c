/*
Autor: Wanderson Gomes da Costa
E-mail: wanderson.gomes.costa05@aluno.ifce.edu.br
Data da Ultima Modificacao: 02 de Dezembro de 2021

Problema:
18 - Escreva um programa que solicite ao usuario a altura
e o raio de um cilindro circular e imprima o volume do 
cilindro. O volume de um cilindro circular e calculado por
meio da seguinte formula:

Vol = 3.141592 * raio * raio * altura
*/
#include <stdio.h>

int main() {
    //dados
    double raio = 0.00;
    double altura = 0.00;

    double volume = 0.00;

    //leitura
    do {
        printf("Informe o raio do cilindro: ");
        scanf("%lf", &raio);
        //error
        if (raio <= 0)
            printf("ERROR: valor do raio invalido! Tente novamente.\n");
    } while (raio <= 0);

    do {
        printf("Informe a altura do cilindro: ");
        scanf("%lf", &altura);
        //error
        if (altura <= 0)
            printf("ERROR: valor da altura e invalido! Tente novamente.\n");
    } while (altura <= 0);

    //processsamento
    volume = 3.141592 * raio * raio * altura;

    //apresentacao dos resultados (saida)
    printf("\nO volume do cilindro informado e: %.2lf\n", volume);

    return 0;
}