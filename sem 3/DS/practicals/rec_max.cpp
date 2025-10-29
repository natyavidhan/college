#include <iostream>

using namespace std;

int rec_max(const int arr[], int n) {
    if (n == 1) return arr[0];
    int next = rec_max(arr + 1, n - 1);
    return arr[0] > next ? arr[0] : next;
}

int main() {
    int nums[5] = {5, 6, 7, 8, 9};
    cout << rec_max(nums, 5);
}