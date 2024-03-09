CC = g++
CFLAGS = -fPIE

distrib/decrypt distrib/decrypt-syms: src/source.cpp
	$(CC) -o distrib/decrypt-syms $(CFLAGS) $^
	strip -s -o distrib/decrypt distrib/decrypt-syms

clean:
	rm distrib/*