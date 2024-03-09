#include <iostream>
#include <cstdlib>
#include <cstring>
#include <unistd.h>
#include <sys/mman.h>

int main(int argc, char** argv) {
    std::string KEY = "cdd2e040cf21d70c4ad47a4b1a401445";
    unsigned char IV[] = {16, 175, 220, 185, 99, 140, 216, 91, 9, 82, 34, 154, 52, 216, 101, 77};
    std::string Cipher = "5655dd747a8397339705ef606dfd00f6000a3ead9219fced7bce02b6bd7c6345dd674e7a630c0bbcf51c3d6b0e27f9f2";

    std::cout << "Enter the key:";
    std::string key;
    std::cin >> key;

    if (std::size(key) != 1) {
        std::cout << "Invalid key length" << std::endl;
        std::exit(-1);
    }

    std::cout << "Testing key ..." << std::endl;
    sleep(5);

    void* addr = mmap(NULL, 1024, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (addr == MAP_FAILED) {
        std::cout << "Critical error" << std::endl;
        std::exit(-1);
    }

    memcpy(addr, key.c_str(), 1);
    void (*fn)() = (void (*)()) addr;

    fn();

    munmap(addr, 1024);

    std::cout << "Test passed!" << std::endl;
    
    char ch = key[0];
    for (int i=0; i<16; ++i) {
        IV[i] ^= ch;
    }

    std::cout << "Key --" << std::endl;
    std::cout << KEY << std::endl;

    std::cout << "IV --" << std::endl;
    for (int i=0; i<16; ++i) {
        std::cout << std::hex << (int)IV[i];
    }

    std::cout << std::endl;

    std::cout << "CIPHER --" << std::endl;
    std::cout << Cipher << std::endl;
}