#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> nums = {5, 3, 6, 7, 2, 9, 10, 14, 4};
    for (int i = 0; i<nums.size(); i++) {
        int shortest = i;
        for (int j = i+1; j < nums.size(); j++ ) {
            if (nums[j] < nums[shortest]) {
                shortest = j;
            }
        }
        swap(nums[shortest], nums[i]);
    }

    for (int i=0; i<nums.size(); i++) {
        cout << nums[i] << " ";
    }
    cout << endl; 
    return 0;
}