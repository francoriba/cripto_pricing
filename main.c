#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// prototype of "mul" functions, implemented in "mul32.asm"
extern float mul1(float , float);
extern float mul2(float , float);
//function prototype
float convert(float crypto_usd, float rate);

int main(){

    printf("%f",convert(30364.10f, 387.075f));
    return 0;
}

float convert(float crypto_usd, float rate){
    float convertion = mul2(crypto_usd, rate); // calcula el precio de btc en ars
    return convertion;}