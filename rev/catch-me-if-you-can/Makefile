distrib/catch-me: src/main.py
	mkdir -p distrib
	cython --embed -3 src/main.py -o src/main.c
	gcc -I /usr/include/python3.11 src/main.c -o distrib/catch-me -lpython3.11 -L /usr/lib/x86_64-linux-gnu
	strip -s distrib/catch-me
