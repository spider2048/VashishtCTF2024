all: server/notes distrib/notes

server/notes: src/notes.c
	mkdir -p server
	gcc src/notes.c -o server/notes -fno-stack-protector -fPIC
	strip -s server/notes


distrib/notes: src/notes.c
	mkdir -p distrib
	gcc src/notes.c -o distrib/notes -fno-stack-protector -fPIC
	strip -s distrib/notes