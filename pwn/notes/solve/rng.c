#include <stdlib.h>
#include <stdio.h>

int main(int argc, char** argv) {
	srand(time(0) / 10);
	
	for (int i=0; i<5; ++i)
		rand();
	
	printf("%d\n", rand());
}