
; file: mul64.asm

; Using Linux and gcc:
;nasm -f elf64 -o mul64.o mul64.asm
;gcc -o main mul64.o -m64 main.c -g
;gcc -m64 -shared -o currencyconverterlib.so main.c mul64.o

;Parameters:
;	float a  [rbp + 16]
; 	float b [rbp + 24]

segment .text          ;definimos la sección de codigo
        global  mul    ;permitimos la visibilidad de la función para otros modulos
    mul:
        push	rbp        ;pusheamos el valor actual de base pointer
        mov	    rbp, rsp   ;copiamos el valor del stack pointer en el base pointer
        push	rbx        ;guardamos el valor actual del registro rbx en la pila
        
	    mulss	xmm0, xmm1 ; multiplicamos los dos operandos de punto flotante de precisión simple en los registros xmm0 y xmm1

        pop		rbx	;  restauramos el valor previo de rbx desde la pila
        mov		rsp, rbp ; restauramos el puntero de pila a su valor anterior al inicio de la función
        pop		rbp          ; restauramos el valor previo de rbp desde la pila
        ret     ; retorna al programa de c