#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// prototype of "mul" functions, implemented in "mul32.asm"
extern float mul1(float , float);
extern float mul2(float , float);
//function prototype
float convert(float crypto_usd, float rate);

int main(){

    printf("%f \n\n",convert(30364.10f, 387.075f));
    printf("El segundo parametro enviado (primero pusheado y mas alto en la pila es: %f \n", 387.075f);
    printf("El primer parametro enviado (segundo pusheado y mas bajo en la pila es: %f \n", 30364.10f);
    return 0;
}

float convert(float crypto_usd, float rate){ //mul2 puede remplazarse por mul1
    float convertion = mul1(crypto_usd, rate); // calcula el precio de btc en ars
    return convertion;}