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

![](https://github.com/francoriba/lab2_cripto_pricing/blob/master/img/mapa%20conceptual.png)

1. Ejecución de ``make`` y si todo sale bien, nos avisa que ya se hizo el build  
![](https://github.com/francoriba/lab2_cripto_pricing/blob/master/img/execution.png)  
2. Ejecutamos el script de python y vemos que nos va a pedir ingresar una crypto y una moneda. Si ingresamos valores válidos, realizará la conversión:  
![](https://github.com/francoriba/lab2_cripto_pricing/blob/master/img/execution2.png)  
3. El programa nos pregunta si queremos realizar otra conversión. Si decimos que no, finalizará, sino vuelve al paso 2.  
![](https://github.com/francoriba/lab2_cripto_pricing/blob/master/img/execution3.png)  
4. En el caso de que se haya ingresado un valor incorrecto, se le avisa al usuario y se vuelve a pedir el valor  
![](https://github.com/francoriba/lab2_cripto_pricing/blob/master/img/execution4.png)  

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

![](https://github.com/francoriba/lab2_cripto_pricing/blob/master/img/stack_x86.png)

El ```stackframe``` contiene dos parametros del tipo float (ocupando 4Bytes c/u) que ocupan las posiciones ```EBP+12``` (precio en USD de alguna criptomoneda) y ```EBP+8``` (precio de un USD expresado en unidades de alguna moneda fiduciaria). 
<br>

## Dump del Stack
A continuación se muestra el área de memoria donde se encuentra alojado el stack haciendo uso de la función dump_stack que ya se encontraba implementada en los ejemplos propuestos por Paul Carter:<br>

![](https://github.com/francoriba/lab2_cripto_pricing/blob/master/img/dump_stack.png)
<br>

Para verificar usamos la calculadora online que utiliza el Estándar IEEE 754 para convertir un valor de punto flotante a su equivalente decimal. 

![](https://github.com/francoriba/lab2_cripto_pricing/blob/master/img/rate.png)
<br>
Comparando ambas imágenes podemos ver como la posición del stack referenciada por [EBP+12] = FFF9E834 efectivamente contiene el valor 43C1899A que se corresponde con el primer parámetro pusheado (rate de conversión).

![](https://github.com/francoriba/lab2_cripto_pricing/blob/master/img/price.png)
<br>
Del mismo modo podemos ver como la posición del stack referenciada por [EBP+8] = FFF9E830  efectivamente contiene el valor 46ED3833  que se corresponde con el segundo parámetro pusheado (precio de la cripto en USD).

También podemos observar que la posición de la pila referenciada por [EBP + 4] = FFF9E82C contiene el valor 5658E293 que se corresponde con la dirección de retorno de la función mul1 (es decir el respaldo del valor que tenía el registro IP antes de el llamado a la función mul1).

## GDB
Compilando con la flag -g, podemos depurar el código utilizando gdb.  
En primera instancia, establecemos el break point en el main y vamos mostrando los registros en cada step realizado con el comando ``info register``<br>
![](https://github.com/francoriba/lab2_cripto_pricing/blob/master/img/image.png)
![](https://github.com/francoriba/lab2_cripto_pricing/blob/master/img/image2.png)
![](https://github.com/francoriba/lab2_cripto_pricing/blob/master/img/image3.png)
