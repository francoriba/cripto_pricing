# Cripto pricing calculator
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
Para poder ejecutar el script "api.py" es necesario previamente crear la libreria "currencyconverterlib.so", puede hacer esto manualmente mediante los comandos comentados en el archivo "mul32.asm" o bien haciendo uso del Makefile mediante el comando "make" (que creará además el archivo ejecutable apto para ser debugeado mediante gdb y los archivos objeto asociados). Con el comando "make clean" puede eliminar los archivos de salida del Makefile. 

![](https://github.com/francoriba/lab2_cripto_pricing/blob/master/img/mapa%20conceptual%20.png)


## Funcionamiento 
Este proyecto se divide en 3 capas. La primer capa utiliza un lenguaje de alto nivel como los es **python** para interactuar con una [API REST](https://www.coinapi.io/) con la que, mediante un esquema HTTP request-response, se obtiene la información correspondiente a:<br>
* Cotización en USD de alguna criptomoneda (BTC, ETH o LTC)<br>
* Cotización en relacion a USD de alguna moneda fiduciaria (USD, ARS, EUR) <br>   

Esta capa interactúa con la capa inferior proporcionandole la información (parametros) tomada de la API REST, esto se logra con ayuda de la libreria ```ctypes``` de Python que permite utlizar las funciones disponibles en una **shared library de c**. Además esta capa implementa las funcionalidades requeridas para que el usuario pueda interactuar con el programa.<br>

La siguiente capa consiste de un **programa de lenguaje c** donde se implementa la función:<br>

```float convert(float crypto_usd, float rate)```<br>

Esta invoca a la subrutina ```mult```, que conforma la capa más baja y se encuentra escrita en **lenguaje ensamblador**, en este caso compatible con arquitecturas x86. El interfaceo de estas dos capas se hace posible gracias a la **call convention de c**. La subrutina se encarga de realizar la multiplicación de los valores en el stack frame que fueron traidos como parametros desde las capas superiores y permite obtener el precio de una criptomoneda expresado en unidades de alguna de las monedas fiduciarias. 

```
segment .text
    global  mul1
    global  mul2

;declaramos macros para la dirección de los bytes mas altos de los dos parametros
%define p1 [ebp+12] 
%define p2 [ebp+8]

;probamos realizar la operación de multiplicación de dos formas distintas, mul2 nos permite comprender mejor lo que sucede a la hora de dubuggear con gdb

mul1: 
    enter 0, 0 ;no se reserva espacio para variables locales
    fld     dword p1 ;ST0 = p1
    fld     dword p2 ;ST1 = p2
    fmulp   st1, st0 ;multiplicamos la cotización de la mondea fiduciaria por el valor de la cripto
    leave ;liberamos la pila
    ret ;retornamos a la función de c

mul2:
        enter           4,0 ; varibales locales definidas solo para inspección del stack frame
        
        mov             dword [ebp-4], 0
        mov             eax, p1
        mov             ebx, p2
        imul            ebx, eax
        mov             [ebp-4], ebx
        mov             eax, ebx
        dump_stack      1, 1, 3

        leave        
        ret
```
<br>

El ```stackframe``` contiene dos parametros del tipo float (ocupando 4Bytes c/u) que ocupan las posiciones ```EBP+12``` (precio en USD de alguna criptomoneda) y ```EBP+8``` (precio de un USD expresado en unidades de alguna moneda fiduciaria). 