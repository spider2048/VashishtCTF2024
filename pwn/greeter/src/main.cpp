#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <string>
#include <iostream>

int show = 0;

[[nodiscard]] void win() {
    std::ifstream flag("flag.txt");
    std::string buf;
    std::getline(flag, buf);
    std::cout << "You win! " << buf << std::endl;
}

void IO() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);
}

int main() {
    IO();

    int* p_show = &show;
    std::string buf(100, '\x00');
    std::cout << "Enter your name> ";
    std::getline(std::cin, buf);
    std::cout << "Hello, ";
    printf(buf.c_str());
    std::cout << std::endl;

    if (show == 0) {
        std::cout << "You may not have the flag" << std::endl;
    } else {
        win();
    }
}