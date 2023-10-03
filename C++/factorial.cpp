#include <iostream>

unsigned long long factorial(int n) {
    if (n < 0) {
        std::cout << "Factorial is not defined for negative numbers";
        return 0; // Return an error value
    } else if (n == 0 || n == 1) {
        return 1;
    } else {
        unsigned long long result = 1;
        for (int i = 2; i <= n; ++i) {
            result *= i;
        }
        return result;
    }
}

int main() {
    int number;
    std::cout << "Enter a non-negative integer: ";
    std::cin >> number;
    std::cout << "Factorial of " << number << " is " << factorial(number) << std::endl;
    return 0;
}
