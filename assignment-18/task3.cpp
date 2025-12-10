#include <iostream>

int factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n - 1);
}

int main() {
    std::cout << "Input: 5 → Output: Factorial = " << factorial(5) << std::endl;
    std::cout << "Input: 0 → Output: Factorial = " << factorial(0) << std::endl;
    return 0;
}
