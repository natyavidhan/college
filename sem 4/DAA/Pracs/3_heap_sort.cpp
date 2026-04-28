#include <bits/stdc++.h>
using namespace std;

long long comparisons;

void heapify(vector<int>& arr, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    
    if (left < n && (comparisons++, arr[left] > arr[largest]))
        largest = left;
    
    if (right < n && (comparisons++, arr[right] > arr[largest]))
        largest = right;
    
    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(vector<int>& arr) {
    comparisons = 0;
    int n = arr.size();
    
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
    
    for (int i = n - 1; i > 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

int main() {
    vector<int> testCases[] = {
        {64, 34, 25, 12, 22, 11, 90},
        {5, 2, 8, 1, 9},
        {1, 2, 3, 4, 5}
    };
    
    cout << "=== HEAP SORT ===" << endl << endl;
    
    for (int t = 0; t < 3; t++) {
        vector<int> arr = testCases[t];
        cout << "Test Case " << (t + 1) << ":" << endl;
        cout << "Input: ";
        for (int x : arr) cout << x << " ";
        cout << endl;
        
        heapSort(arr);
        
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
            
            heapSort(arr);
            totalComparisons += comparisons;
        }
        
        long long avgComparisons = totalComparisons / 10;
        cout << size << "\t" << avgComparisons << endl;
    }
    
    return 0;
}
