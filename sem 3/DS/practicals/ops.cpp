#include <iostream>
using namespace std;

int sum(int n) {
    int sum = 0;
    while (n) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int reverse(int n) {
    int rev = 0;
    while (n) {
        rev = rev * 10 + n % 10;
        n /= 10;
    }
    return rev;
}

int factorial(int n) {
    int fact = 1;
    for (int i = 2; i <= n; i++)
        fact *= i;
    return fact;
}

void fibonacci(int n) {
    int a = 0, b = 1, c;
    cout << "Fibonacci series: " << a << " " << b << " ";
    for (int i = 2; i < n; i++) {
        c = a + b;
        cout << c << " ";
        a = b;
        b = c;
    }
    cout << endl;
}

bool is_prime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

void print_primes(int n) {
    cout << "Primes up to " << n << ": ";
    for (int i = 2; i <= n; i++) {
        if (is_prime(i))
            cout << i << " ";
    }
    cout << endl;
}

int main() {
    int choice, n;
    while (true) {
        cout << "\n1. Sum of digits\n2. Reverse integer\n3. Factorial\n4. Fibonacci series\n5. Prime numbers\n6. Exit\nEnter choice: ";
        cin >> choice;
        if (choice == 6) break;
        cout << "Enter an integer: ";
        cin >> n;
        if (choice == 1) {
            cout << "Sum of digits = " << sum(n) << endl;
        } else if (choice == 2) {
            cout << "Reversed number = " << reverse(n) << endl;
        } else if (choice == 3) {
            cout << "Factorial = " << factorial(n) << endl;
        } else if (choice == 4) {
            fibonacci(n);
        } else if (choice == 5) {
            print_primes(n);
        } else {
            cout << "Invalid choice\n";
        }
    }
    return 0;
}
