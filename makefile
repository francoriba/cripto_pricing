CC=gcc
CFLAGS=-Wall -Wextra -std=c11 -m32 -g -fno-pie
LDFLAGS=-lm

all: main

main: main.o mul32.o
	$(CC) $(CFLAGS) -fno-pic -o $@ $< -L. -currencyconverterlib $(LDFLAGS)

main.o: main.c
	$(CC) $(CFLAGS) -c $<

mul32.o: mul32.asm
	nasm -f elf32 -o $@ $<

currencyconverterlib.o:
	gcc -m32 -shared -o currencyconverterlib.so main.c mul32.o

clean:
	rm -f *.o main
