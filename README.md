# lab2_cripto_pricing
Repositorio para el laboratorio n°2 de la asignatura "Sistemas de Computación" de la FCEFyN , Universidad Naconal de Córdoba, Argentina. <br>
Grupo de trabajo: Internautas  <br>
Abril, 2023 <br>
Integrantes: 
 * Careggio, Camila
 * Casanueva, María Constanza
 * Riba, Franco <br>
 
 Profesores:
 * Jorge, Javier Alejandro 
 * Solinas, Miguel

## Como ejecutar el script de Python
Para poder ejecutar el script "api.py" es necesario previamente crear la libreria "currencyconverterlib.so", puede hacer esto manualmente mediante los comandos comentados en el archivo "mul64.asm" o bien haciendo uso del Makefile mediante el comando "make" (que creará además el archivo ejecutable apto para ser debugeado mediante gdb y los archivos objeto asociados). Con el comando "make clean" puede eliminar los archivos de salida del Makefile. 

![](https://github.com/francoriba/lab2_cripto_pricing/blob/x86-64-mejoras/img/mapa%20conceptual%20.png)


## Funcionamiento 
Nuestro programa esta pensando en rasgos generales en 3 capas donde la primera utilizamos ```python``` donde hacemos el desarrollo de la API,para el desarrollo usamos  la API https://www.coinapi.io/ <br>
Esta API nos permite hacer la cotizacion de las criptomonedas como tambien de las monedas USD EUR ARS en tiempo real. <br>
En nuestra capa de ```C```esta el desarrollo de la conversion y tambien es la capa que conecta la otras dos
```
float convert(float crypto_usd, float rate){
    float convertion = mul(crypto_usd, rate); // calcula el precio de btc en ars
    return convertion;}

```
Donde nuestro archivo mul es con ```assembler```, nosotros utilizamos una arquitectura de assemble de x64 bits 
```
segment .text
        global  mul
    mul:
        push	rbp
        mov	    rbp, rsp
        push	rbx
        
	    mulss	xmm0, xmm1

        pop		rbx		
        mov		rsp, rbp
        pop		rbp            
        ret
```
Los registros que usamos no son parametros si no que son registros del procesador. <br>
Como vemos hacemos el uso de una pila donde realizamos la multiplicacion de dos puntos flotantes ```mulss	xmm0, xmm1```
<br>
Podemos visualizar como se genera nuestra ```stackframe``` quedando  visualmente de esta manera

![](https://github.com/francoriba/lab2_cripto_pricing/blob/x86-64-mejoras/img/stack.png)

Donde podemos ver como nuetra ```stackframe``` esta conformada por el valor de la criptomoneda en dolares ```RBP+24``` , de la moneda que se haya elegido a su conversion en dolares```RBP+16```, la direccion de retorno```RBP+8``` y el valor original de el ```RBP```. <rb>
