segment .data
; no usamos segmento de datos

segment .bss
; no usamos variables sin inicializar

segment .text
    global  convert_to

;declaramos macros para la dirección de los bytes mas altos de los dos parametros
%define p1 [rbp+24] 
%define p2 [rbp+16]

convert_to: 
    enter 0, 0 ;no se reserva espacio para variables locales
    fld     qword p1 ;ST0 = p1
    fld     qword p2 ;ST1 = p2
    fmulp   st1, st0 ;multiplicamos la cotización de la mondea fiduciaria por el valor de la cripto
    leave ;liberamos la pila
    ret ;retornamos a la función de c
