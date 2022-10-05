#include <iostream>

int main() {
    int a,b,c;
    std::cin >>a>>b>>c;
    if (a > b) {
        if (a > c) {
            std::cout << a <<" is largest";
        }
        else std::cout << c <<" is largest";
    }
    else if (b > c){
        std::cout << b <<" is largest";
    }
    else std::cout << c <<" is largest";
    return 0;
}