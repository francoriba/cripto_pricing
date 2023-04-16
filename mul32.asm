%include "asm_io.inc"
; Using Linux and gcc:
;nasm -f elf32 -o mul32.o mul32.asm
;gcc -o main mul32.o -m32 main.c -g
;gcc -m32 -shared -o currencyconverterlib.so main.c mul32.o

segment .data
; no usamos segmento de datos
segment .bss
; no usamos variables sin inicializar
segment .text
    global  mul1
    global  mul2

;declaramos macros para la dirección de los bytes mas altos de los dos parametros
%define p1 [ebp+12] 
%define p2 [ebp+8]

;probamos realizar la operación de multiplicación de dos formas distintas

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