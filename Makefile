# Compilador
CC = 			gcc
CFLAGS 	= 		-Wall -Werror -pedantic -Wextra -Wconversion -std=gnu11

# Target
default: currencyconverterlib

all: clean default

###### Objects and librearies ######
mul64.o: 
	nasm -f elf64 mul64.asm

main.c: $(SRC)/main.c mul.o
	$(CC) -c -g  main.c $(CFLAGS) -o main.o

# currencyconverterlib
currencyconverterlib.so: main.c mul64.o
	$(CC)  -shared -W mul64.o main.o -o libconverter.so
	@echo "\n"Build Donde!"\n"

#########################################################################################################
# Eliminar todos los objetos, dependencias y ejecutables
clean:
	rm $/*.o
	rm $/*.so
	@echo "\n"All clean now!