#define RAND_MAX ULLONG_MAX

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

volatile const char* USEME = "cat ./flag.txt";

void IO() {
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);
}

unsigned long long encrypt(unsigned long long x) {
    srand(time(NULL) / 10);
    for (int i=0; i<5; ++i)
        rand();
    
    return (x ^ ((unsigned long long) rand()));
}

int main(int argc, char** argv) {
    IO();
    printf("Hint: %p\n", encrypt((unsigned long long) exit));

    char notes[100];
    puts("Enter your notes:");
    scanf("%s", notes);

    return 0;
}