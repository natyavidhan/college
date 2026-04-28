#include <bits/stdc++.h>
using namespace std;

long long comparisons;

void merge(vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    vector<int> L(n1), R(n2);
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];
    
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        comparisons++;
        if (L[i] <= R[j]) {
            arr[k++] = L[i++];
        } else {
            arr[k++] = R[j++];
        }
    }
    
    while (i < n1)
        arr[k++] = L[i++];
    while (j < n2)
        arr[k++] = R[j++];
}

void mergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

int main() {
    vector<int> testCases[] = {
        {64, 34, 25, 12, 22, 11, 90},
        {5, 2, 8, 1, 9},
        {1, 2, 3, 4, 5}
    };
    
    cout << "=== MERGE SORT ===" << endl << endl;
    
    for (int t = 0; t < 3; t++) {
        vector<int> arr = testCases[t];
        cout << "Test Case " << (t + 1) << ":" << endl;
        cout << "Input: ";
        for (int x : arr) cout << x << " ";
        cout << endl;
        
        comparisons = 0;
        mergeSort(arr, 0, arr.size() - 1);
        
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
            mergeSort(arr, 0, arr.size() - 1);
            totalComparisons += comparisons;
        }
        
        long long avgComparisons = totalComparisons / 10;
        cout << size << "\t" << avgComparisons << endl;
    }
    
    return 0;
}
