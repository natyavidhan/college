#include <iostream>
using namespace std;

void findFloorCeil(int arr[], int n, int d, int &ceilVal, int &floorVal) {
    int low = 0, high = n - 1;
    floorVal = -1;
    ceilVal = -1;

    while (low <= high) {
        int mid = (low + high) / 2;

        if (arr[mid] == d) {
            ceilVal = floorVal = d;
            return;
        } else if (arr[mid] < d) {
            floorVal = arr[mid]; 
            low = mid + 1;
        } else {
            ceilVal = arr[mid]; 
            high = mid - 1;
        }
    }
}

int main() {
    int n;
    cin >> n;

    int* arr = new int[n];
    for (int i = 0; i < n; i++) cin >> arr[i];

    int d;
    cin >> d;

    int ceilVal, floorVal;
    findFloorCeil(arr, n, d, ceilVal, floorVal);

    cout << "Ceil = " << ceilVal << endl;
    cout << "Floor = " << floorVal << endl;

    delete[] arr;
    return 0;
}
