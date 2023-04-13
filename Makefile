# Compilador
CC = 			gcc
CFLAGS 	= 		-Wall -Werror -pedantic -Wextra -Wconversion -std=gnu11 -m64 -g
LDFLAGS = 		-shared
NASM = 			nasm
NASMFLAGS=		-f elf64

# Source files
SRCS = main.c mul64.asm

# Object files
OBJS= main.o mul64.o

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

# Create shared library from object files
currencyconverterlib.so: mul64.o main.o
	$(CC) $(LDFLAGS) -o $@ $^
	@echo "\n"Build Donde!"\n"

# Eliminar todos los objetos, dependencias y ejecutables  -f los ignora si no existen
clean:
	rm -f *.o
	rm -f $(TARGETS)
	@echo "\n"All clean now!