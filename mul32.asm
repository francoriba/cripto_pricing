; file: mul32.asm

; Using Linux and gcc:
;nasm -f elf32 -o mul32.o mul32.asm
;gcc -o main mul32.o -m32 main.c -g
;gcc -m32 -shared -o currencyconverterlib.so main.c mul32.o

segment .data
; no usamos segmento de datos

segment .bss
; no usamos variables sin inicializar

segment .text
    global  mul

;declaramos macros para la dirección de los bytes mas altos de los dos parametros
%define p1 [ebp+12] 
%define p2 [ebp+8]

mul: 
    enter 0, 0 ;no se reserva espacio para variables locales
    fld     dword p1 ;ST0 = p1
    fld     dword p2 ;ST1 = p2
    fmulp   st1, st0 ;multiplicamos la cotización de la mondea fiduciaria por el valor de la cripto
    leave ;liberamos la pila
    ret ;retornamos a la función de c