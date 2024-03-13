all: distrib/jump

distrib/jump: src/main.cpp
	mkdir -p distrib
	g++ src/main.cpp -o distrib/jump -Oz
	strip -s distrib/jump
