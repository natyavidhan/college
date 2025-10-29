#include <iostream>

using namespace std;

int product(int m, int n) {
    if (n == 0) {
        return 0;
    }
    return m + product(m, n - 1);
}

int main() {
    int a, b;
    cin >> a;
    cin >> b;
    cout << product(a, b);
    return 0;
}