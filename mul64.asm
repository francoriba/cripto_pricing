
; file: mul64.asm

; Using Linux and gcc:
;nasm -f elf64 -o mul64.o mul64.asm
;gcc -o main mul64.o -m64 main.c -g
;gcc -m64 -shared -o currencyconverterlib.so main.c mul64.o

;Parameters:
;	float a  [rbp + 16]
; 	float b [rbp + 24]

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