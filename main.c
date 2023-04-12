#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Declaramos la función convert_to, que se definirá en assembler
extern float convert_to(float , float);

//Prototipos de funciones
float btc_ars(float btc_usd, float rate_ars);
float btc_eur(float btc_usd,float rate_eur);
float eth_ars(float eth_usd, float rate_ars);
float eth_eur(float eth_usd, float rate_eur);
float ltc_ars(float ltc_usd, float rate_ars);
float ltc_eur(float ltc_usd, float rate_eur);

int main(int argc, char *argv[]){

    printf("%f",btc_ars(30364.108274487993, 387.075));
    return 0;
}

float btc_ars(float btc_usd, float rate_ars){
    double btc_ars = convert_to(btc_usd, rate_ars); // calcula el precio de btc en ars
    return btc_ars;
}

float btc_eur(float btc_usd,float rate_eur){
    float btc_eur = convert_to(btc_usd, rate_eur); //calcula el precio de btc en eur
    return btc_eur;
}

float ltc_ars(float ltc_usd, float rate_ars){
    float ltc_ars = convert_to(ltc_usd, rate_ars); //calcula el precio de ltc en ars
    return ltc_ars;
}

float ltc_eur(float ltc_usd, float rate_eur){
    float ltc_eur = convert_to(ltc_usd, rate_eur); //calcula el precio de ltc en eur
    return ltc_eur;
}

float eth_ars(float eth_usd, float rate_ars){
    float eth_ars = convert_to(eth_usd, rate_ars); //calcula el precio de eth en ars
    return eth_ars;
}

float eth_eur(float eth_usd, float rate_eur){
    float eth_eur = convert_to(eth_usd, rate_eur); //calcula el precio de eth en eur
    return eth_eur;
} 