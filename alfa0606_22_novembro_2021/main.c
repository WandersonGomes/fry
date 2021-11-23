/*
Autor: Wanderson Gomes da Costa
E-mail: wanderson.gomes.costa05@aluno.ifce.edu.br
Data da Ultima Modificacao: 22 de Novembro 2021

Problema:

*/
#include <stdio.h>

int main() {
    //dados
    double altura_bambu = 0.00;
    double distancia_ponta_bambu = 0.00;
    double altura_quebra = 0.00;

    //leitura
    do {
        printf("Informe a altura do bambu: ");
        scanf("%lf", &altura_bambu);
        //error
        if (altura_bambu <= 0.00)
            printf("Error: altura invalida! Tente novamente.\n");
    } while (altura_bambu <= 0.00);

    do {
        printf("Informe a distancia da ponta do bambu ate sua base: ");
        scanf("%lf", &distancia_ponta_bambu);
        //error
        if ((distancia_ponta_bambu <= 0.00) || (distancia_ponta_bambu > altura_bambu))
            printf("Error: distancia invalida! Tente novamente.\n");
    } while ((distancia_ponta_bambu <= 0.00) || (distancia_ponta_bambu > altura_bambu));

    //processamento
    altura_quebra = (-(distancia_ponta_bambu * distancia_ponta_bambu) + (altura_bambu * altura_bambu))/(2 * altura_bambu);

    //apresentacao dos resultados
    printf("A altura que ocorreu a quebra foi de: %g\n", altura_quebra);

    return 0;
}