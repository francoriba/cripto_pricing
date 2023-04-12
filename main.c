#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Declaramos la función convert_to, que se definirá en assembler
//float PRE_CDECL convert_to( float, float) POST_CDECL; 
extern float convert_to(float , float);

//Prototipo de funcion
float somecripto_somerate(float crypto_usd, float rate);

int main(int argc, char *argv[]){

    printf("%f",somecripto_somerate(30364.108274487993, 387.075));
    return 0;
}

float somecripto_somerate(float crypto_usd, float rate){
    double somecripto_somerate = convert_to(crypto_usd, rate); // calcula el precio de btc en ars
    return somecripto_somerate;}
