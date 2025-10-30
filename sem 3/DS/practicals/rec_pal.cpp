#include <iostream>
#include <string>

using namespace std;

bool palindrome(string s) {
    int len = s.length();
    if (len <= 1) return true;
    if (s[0] != s[len-1]) return false;
    return palindrome(s.substr(1, len-2));
}

int main() {
    bool isit = palindrome("gohangasalamiimalasagnahog");
    if (isit) {
        cout << "Palindrome" << endl;
    } else {
        cout << "Not Palindrome" << endl;
    }
    return 0;
}