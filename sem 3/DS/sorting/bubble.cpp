#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> nums = {5, 3, 6, 7, 2, 9, 10, 14, 4};
    int end = nums.size() - 1;

    for (int end_ = end; end_ > 0; end_--) {
        for (int i=0; i < end_; i++) {
            if (nums[i] > nums[i+1]) {
                swap(nums[i], nums[i+1]);
            }
        }
    }

    for (int i=0; i<nums.size(); i++) {
        cout << nums[i] << " ";
    }
    cout << endl; 
    return 0;
}