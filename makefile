# Compilador
CC = 			gcc
CFLAGS 	= 		-Wall -Werror -pedantic -Wextra -Wconversion -std=gnu11 -m32 -g
LDFLAGS = 		-shared
NASM = 			nasm
NASMFLAGS=		-f elf32

# Source files
SRCS = main.c mul32.asm

# Object files
OBJS= main.o mul32.o asm_io.o

# Target
TARGETS = main currencyconverterlib.so #Name for final target

# Tell make these are not real targets (won't create an output file)
.PHONY: all clean 

# Targets to build when writing only make command
all: $(TARGETS)

###### Objects and librearies ######

# Link object files to create the final executable
main: $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^

# Compile C source files
%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

# Compile NASM assembly files
%.o: %.asm 
	$(NASM) $(NASMFLAGS) -o $@ $<

asm_io.o: asm_io.asm
	nasm -f elf32 -d ELF_TYPE -o $@ $^

# Create shared library from object files
currencyconverterlib.so: mul32.o main.o
	$(CC) $(LDFLAGS) -m32 -o $@ $^
	@echo "\n"Build Donde!"\n"

# Eliminar todos los objetos, dependencias y ejecutables  -f los ignora si no existen
clean:
	rm -f *.o
	rm -f $(TARGETS)
	@echo "\n"All clean now!