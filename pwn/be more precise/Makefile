CC=g++
CFLAGS=-mavx -funroll-loops -ftemplate-depth=10000 -Os -static
FLAG=$(shell cat flag.txt)

distrib/precise: src/float.cpp
	mkdir -p distrib
	$(CC) $^ -o $@ $(CFLAGS) '-DFLAG="FAKE_FLAG"'
	strip -s $@

server/precise: src/float.cpp
	mkdir -p server
	$(CC) $^ -o $@ $(CFLAGS) '-DFLAG="${FLAG}"'
	strip -s $@
