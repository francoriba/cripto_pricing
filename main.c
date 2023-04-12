#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Declaramos la función convert_to, que se definirá en assembler
extern float mul(float , float);

//Prototipo de funcion
float somecripto_somerate(float btc_usd, float rate_ars);

int main(){

    printf("%f",somecripto_somerate(30364.108274487993, 387.075));
    return 0;
}
float somecripto_somerate(float btc_usd, float rate_ars){
    double btc_ars = mul(btc_usd, rate_ars); // calcula el precio de btc en ars
    return btc_ars;
}