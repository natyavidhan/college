#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> nums = {1, 4, 6, 7, 8, 10, 11, 14, 20};
    int target = 11;
    int start = 0;
    int end = nums.size() - 1;

    while (start <= end) {
        int mid = (start + end) / 2;
        if (nums[mid] == target) {
            cout << mid << endl;
            break;
        } else if (nums[mid] < target) {
            start = mid + 1;
        } else if (nums[mid] > target) {
            end = mid - 1;
        }
    }
    
    return 0;
}