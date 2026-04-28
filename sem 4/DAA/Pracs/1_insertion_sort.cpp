#include <bits/stdc++.h>
using namespace std;

long long comparisons;

void insertionSort(vector<int>& arr) {
    comparisons = 0;
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && (comparisons++, arr[j] > key)) {
            arr[j + 1] = arr[j];
            j--;
        }
    }
}

int main() {
    vector<int> testCases[] = {
        {64, 34, 25, 12, 22, 11, 90},
        {5, 2, 8, 1, 9},
        {1, 2, 3, 4, 5}
    };
    
    cout << "=== INSERTION SORT ===" << endl << endl;
    
    for (int t = 0; t < 3; t++) {
        vector<int> arr = testCases[t];
        cout << "Test Case " << (t + 1) << ":" << endl;
        cout << "Input: ";
        for (int x : arr) cout << x << " ";
        cout << endl;
        
        insertionSort(arr);
        
        cout << "Output: ";
        for (int x : arr) cout << x << " ";
        cout << endl;
        cout << "Comparisons: " << comparisons << endl << endl;
    }
    
    // Performance analysis
    cout << "\nPerformance Analysis (Sizes 30-1000, step 100):" << endl;
    cout << "Size\tAvg Comparisons" << endl;
    
    for (int size = 30; size <= 1000; size += 100) {
        long long totalComparisons = 0;
        
        for (int instance = 0; instance < 10; instance++) {
            vector<int> arr(size);
            for (int i = 0; i < size; i++) {
                arr[i] = rand() % 10000;
            }
            
            insertionSort(arr);
            totalComparisons += comparisons;
        }
        
        long long avgComparisons = totalComparisons / 10;
        cout << size << "\t" << avgComparisons << endl;
    }
    
    return 0;
}
