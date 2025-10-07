#include <iostream>
using namespace std;

// Function definitions

int sum(int *arr, int n) {
    int total = 0;
    for(int i = 0; i < n; i++)
        total += arr[i];
    return total;
}

double average(int *arr, int n) {
    return (double)sum(arr, n) / n;
}

void min_max(int *arr, int n, int &min, int &max) {
    min = max = arr[0];
    for(int i = 1; i < n; i++) {
        if(arr[i] < min) min = arr[i];
        if(arr[i] > max) max = arr[i];
    }
}

void selection_sort(int *arr, int n) {
    for(int i = 0; i < n-1; i++) {
        int minIdx = i;
        for(int j = i+1; j < n; j++)
            if(arr[j] < arr[minIdx])
                minIdx = j;
        swap(arr[i], arr[minIdx]);
    }
    cout << "Array sorted using Selection Sort\n";
}

void insertion_sort(int *arr, int n) {
    for(int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while(j >= 0 && arr[j] > key) {
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }
    cout << "Array sorted using Insertion Sort\n";
}

void search(int *arr, int n, int key) {
    for(int i = 0; i < n; i++) {
        if(arr[i] == key) {
            cout << "Element found at index " << i << endl;
            return;
        }
    }
    cout << "Element not found\n";
}

int* merge_arrays(int *arr1, int n1, int *arr2, int n2) {
    int *merged = new int[n1 + n2];
    for(int i = 0; i < n1; i++)
        merged[i] = arr1[i];
    for(int i = 0; i < n2; i++)
        merged[n1 + i] = arr2[i];
    return merged;
}

int* concatenate_arrays(int *arr1, int n1, int *arr2, int n2) {
    return merge_arrays(arr1, n1, arr2, n2);
}

void print_array(int *arr, int n) {
    for(int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}

// Main program

int main() {
    int choice, n;
    cout << "Enter size of array: ";
    cin >> n;
    int *arr = new int[n];
    cout << "Enter elements:\n";
    for(int i = 0; i < n; i++)
        cin >> arr[i];

    while (true) {
        cout << "\n1. Sum of elements\n2. Average of elements\n3. Minimum and Maximum\n4. Sort using Selection Sort\n";
        cout << "5. Sort using Insertion Sort\n6. Search an element\n7. Merge with another array\n";
        cout << "8. Concatenate with another array\n9. Display array\n10. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        if (choice == 10)
            break;

        if (choice == 1) {
            cout << "Sum = " << sum(arr, n) << endl;
        } else if (choice == 2) {
            cout << "Average = " << average(arr, n) << endl;
        } else if (choice == 3) {
            int minVal, maxVal;
            min_max(arr, n, minVal, maxVal);
            cout << "Minimum = " << minVal << ", Maximum = " << maxVal << endl;
        } else if (choice == 4) {
            selection_sort(arr, n);
            print_array(arr, n);
        } else if (choice == 5) {
            insertion_sort(arr, n);
            print_array(arr, n);
        } else if (choice == 6) {
            int key;
            cout << "Enter element to search: ";
            cin >> key;
            search(arr, n, key);
        } else if (choice == 7) {
            int n2;
            cout << "Enter size of second array: ";
            cin >> n2;
            int *arr2 = new int[n2];
            cout << "Enter elements of second array:\n";
            for(int i = 0; i < n2; i++)
                cin >> arr2[i];
            int *merged = merge_arrays(arr, n, arr2, n2);
            cout << "Merged array:\n";
            print_array(merged, n + n2);
            delete[] arr2;
            delete[] merged;
        } else if (choice == 8) {
            int n2;
            cout << "Enter size of second array: ";
            cin >> n2;
            int *arr2 = new int[n2];
            cout << "Enter elements of second array:\n";
            for(int i = 0; i < n2; i++)
                cin >> arr2[i];
            int *concat = concatenate_arrays(arr, n, arr2, n2);
            cout << "Concatenated array:\n";
            print_array(concat, n + n2);
            delete[] arr2;
            delete[] concat;
        } else if (choice == 9) {
            cout << "Array elements:\n";
            print_array(arr, n);
        } else {
            cout << "Invalid choice\n";
        }
    }

    delete[] arr;
    return 0;
}
