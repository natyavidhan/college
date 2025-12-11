#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> nums = {5, 3, 6, 7, 2, 9, 10, 14, 4};
    
    for (int i = 1; i < nums.size(); i++) {
        for (int j = i; j > 0 && nums[j-1] > nums[j]; j--) {
            swap(nums[j], nums[j-1]);
        }
    }

    for (int i=0; i<nums.size(); i++) {
        cout << nums[i] << " ";
    }
    cout << endl; 
    return 0;
}
