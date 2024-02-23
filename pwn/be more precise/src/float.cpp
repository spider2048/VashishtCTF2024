#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <unistd.h>

#ifndef FLAG
#error "Compiling without flag"
#endif

// -1.8895833333333336146

template<unsigned N>
struct unroll {
    template <typename F>
    volatile static void call(const F& func) {
        func();
        unroll<N-1>::call(func);
    }
};

template<>
struct unroll<0> {
    template <typename F>
    volatile static void call(const F& func) {}
};

int main() {
    srand(10000);
    alarm(5);

    double f = 0.1f + 0.7f;
    double f3 = f * 0.87f;

    double f4 = f3 / 0.3f;
    double f5 = f * f4 * f3;

    double fq = 1.0f, fi=0.1;

    unroll<500>::call([&]() {
        if (fi < 5) {
            fq *= fi;
            fi += 1.3 + 1.1;
            return;
        } else {
            return;
        }
    });

    double f2 = 0;  
    // std::cout << std::setprecision(20) << fq << std::endl;
    std::cin >> f2;

    f2 += (1.1 + 1.3);

    volatile double v = 1.0f;

    unroll<100>::call([&] () { 
        v += rand() % 14;
    });

    unroll<100>::call([&] () { 
        v += rand() % 7;
    });

    f2 *= (1.1 + 1.3);

    unroll<50>::call([&] {
        v += rand() % 100;
    });

    if (f2 == fq) {
        std::cout << "Equal! " << f2 << std::endl;
        std::cout << "Flag is: " << FLAG << std::endl;
    } else {
        std::cout << "Not equal!" << std::endl;
        // std::cout << "Delta: " << fq  - f2 << std::endl;
        // std::cout << "fq: " << fq << std::endl;
        // std::cout << "f2: " << f2 << std::endl;
    }
}