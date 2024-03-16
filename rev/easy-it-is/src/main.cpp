#include <iostream>


int main() {
    std::string flag = "SURGE{09e887182e38f8264b72e86947e29629}";
    std::cout << "Flag: " << std::endl;

    std::string in;
    std::cin >> in;

    if (flag == in) {
        std::cout << "Correct!" << std::endl;
    } else {
        std::cout << "Wrong!" << std::endl;
    }
}