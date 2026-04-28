#include <bits/stdc++.h>
using namespace std;

void countSort(vector<int>& arr) {
    if (arr.empty()) return;
    
    int maxVal = *max_element(arr.begin(), arr.end());
    int minVal = *min_element(arr.begin(), arr.end());
    
    int range = maxVal - minVal + 1;
    vector<int> count(range, 0);
    
    for (int num : arr) {
        count[num - minVal]++;
    }
    
    for (int i = 1; i < range; i++) {
        count[i] += count[i - 1];
    }
    
    vector<int> output(arr.size());
    for (int i = arr.size() - 1; i >= 0; i--) {
        output[count[arr[i] - minVal] - 1] = arr[i];
        count[arr[i] - minVal]--;
    }
    
    arr = output;
}

int main() {
    vector<int> testCases[] = {
        {64, 34, 25, 12, 22, 11, 90},
        {5, 2, 8, 1, 9},
        {100, 50, 75, 25, 10}
    };
    
    cout << "=== COUNT SORT ===" << endl << endl;
    
    for (int t = 0; t < 3; t++) {
        vector<int> arr = testCases[t];
        cout << "Test Case " << (t + 1) << ":" << endl;
        cout << "Input: ";
        for (int x : arr) cout << x << " ";
        cout << endl;
        
        countSort(arr);
        
        cout << "Output: ";
        for (int x : arr) cout << x << " ";
        cout << endl << endl;
    }
    
    // Large input test
    cout << "Test Case 4: Large Random Array (50 elements)" << endl;
    vector<int> largeArr(50);
    for (int i = 0; i < 50; i++) {
        largeArr[i] = rand() % 200;
    }
    
    cout << "Input (first 20): ";
    for (int i = 0; i < 20; i++) cout << largeArr[i] << " ";
    cout << "..." << endl;
    
    countSort(largeArr);
    
    cout << "Output (first 20): ";
    for (int i = 0; i < 20; i++) cout << largeArr[i] << " ";
    cout << "..." << endl;
    
    return 0;
}
