#include <iostream>
#include <string>

using namespace std;

string reverse(string s) {
    if (s.length() == 0) {
        return "";
    }
    return reverse(s.substr(1)) + s[0];
}

int main() {
    string str = "snap&stop";
    string rev_str = reverse(str);
    cout << rev_str << endl;
    return 0;
}