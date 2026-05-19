#include <bits/stdc++.h>
using namespace std;

long long comparisons;

int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    
    for (int j = low; j < high; j++) {
        comparisons++;
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main() {
    vector<int> testCases[] = {
        {64, 34, 25, 12, 22, 11, 90},
        {5, 2, 8, 1, 9},
        {1, 2, 3, 4, 5}
    };
    
    cout << "=== QUICK SORT ===" << endl << endl;
    
    for (int t = 0; t < 3; t++) {
        vector<int> arr = testCases[t];
        cout << "Test Case " << (t + 1) << ":" << endl;
        cout << "Input: ";
        for (int x : arr) cout << x << " ";
        cout << endl;
        
        comparisons = 0;
        quickSort(arr, 0, arr.size() - 1);
        
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
            
            comparisons = 0;
            quickSort(arr, 0, arr.size() - 1);
            totalComparisons += comparisons;
        }
        
        long long avgComparisons = totalComparisons / 10;
        cout << size << "\t" << avgComparisons << endl;
    }
    
    return 0;
}
