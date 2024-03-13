all: distrib/greet server/greet

distrib/greet: src/main.cpp
	g++ src/main.cpp -o distrib/greet -static
	strip -s distrib/greet

server/greet: src/main.cpp
	g++ src/main.cpp -o server/greet -static
	strip -s server/greet
