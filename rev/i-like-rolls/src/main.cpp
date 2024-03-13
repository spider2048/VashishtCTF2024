#include <iostream>


template <unsigned N>
struct unroll {
    template <typename F>
    static void call(const F& func) {
        func();
        unroll<N-1>::call(func);
    };
};

template <>
struct unroll<0> {
    template <typename F>
    static void call(const F& func) {}
};

// SURGE{d786925da332ac45490e5bafa17e02f4}

std::string X = "^pXf_rJxHyvjif:x5n;p4b?d8didlf>e>n?tlenm9f8q9x4o=khm8fojlhkslt<n:khr=w?xkv9spw";

int main() {
    std::string flag;

    std::cout << "Enter flag: " << std::endl;
    std::cin >> flag;

    if (flag.size() != 39) {
        std::cout << "Incorrect!" << std::endl;
        exit(-1);
    }

    int j = 0;
    unroll<39>::call([&] () {
        flag[j++] ^= 13;
    });

    int i = 0;
    j = 0;
    unroll<39>::call([&] () {
        if (flag[i] != X[j]) {
            std::cout << "Incorrect!" << std::endl;
            exit(-1);
        }
        i++;
        j++;j++;
    });

    std::cout << "Correct!" << std::endl;
}