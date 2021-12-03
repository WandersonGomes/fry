/*
Autor: Wanderson Gomes da Costa
E-mail: wanderson.gomes.costa05@aluno.ifce.edu.br
Data da Ultima Modificacao: 02 de Dezembro de 2021

Problema:
16 - Escreva uma expressao logica que resulte 1 se o ano for
bissexto e 0 se nao for. Um ano e bissexto se for divi-
sivel por 4, mas nao por 100. Um ano tambem e bissexto
se for divisivel por 400.

17 - Desenvolva um programa que solicite ao usuario o ano e 
imprima "Ano Bissexto" ou "Ano Nao Bissexto", conforme o valor
da expressao do exercicio 16. Utilize o operador condicional.
*/
#include <stdio.h>

int main() {
    //dados
    int ano = 0;
    int resultado = 0;    

    //leitura
    printf("Informe o ano: ");
    scanf("%d", &ano);

    //processamento
    //um ano e bissexto se for divisivel por 4, mas nao por 100
    //Um ano tambem e bissexto se for divisivel por 400
    resultado =  ((ano % 4 == 0) && (ano % 100 != 0)) || (ano % 400 == 0); //questao 16
    //2000 (0 || 1)
    //1900 (0 || 0) 

    //apresentacao dos resultados (saida)
    if (resultado == 1) 
        printf("\nO ano e bissexto!\n");
    if (resultado == 0)
        printf("\nO ano nao e bissexto!\n");

    return 0;
}