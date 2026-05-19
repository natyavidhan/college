#include <bits/stdc++.h>
using namespace std;

int knapsack01(vector<int>& weights, vector<int>& values, int capacity) {
    int n = weights.size();
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));
    
    for (int i = 1; i <= n; i++) {
        for (int w = 1; w <= capacity; w++) {
            if (weights[i - 1] <= w) {
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                );
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }
    
    return dp[n][capacity];
}

void printKnapsackDetails(vector<int>& weights, vector<int>& values, int capacity) {
    int n = weights.size();
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));
    
    for (int i = 1; i <= n; i++) {
        for (int w = 1; w <= capacity; w++) {
            if (weights[i - 1] <= w) {
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                );
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }
    
    // Backtrack to find which items are included
    vector<bool> included(n, false);
    int w = capacity;
    for (int i = n; i > 0 && w > 0; i--) {
        if (dp[i][w] != dp[i - 1][w]) {
            included[i - 1] = true;
            w -= weights[i - 1];
        }
    }
    
    cout << "Items included (0-indexed): ";
    for (int i = 0; i < n; i++) {
        if (included[i]) cout << i << " ";
    }
    cout << endl;
    
    cout << "Maximum value: " << dp[n][capacity] << endl;
}

int main() {
    cout << "=== 0-1 KNAPSACK PROBLEM ===" << endl << endl;
    
    // Test Case 1
    cout << "Test Case 1:" << endl;
    vector<int> weights1 = {2, 3, 4, 5};
    vector<int> values1 = {3, 4, 5, 6};
    int capacity1 = 5;
    
    cout << "Items: 4" << endl;
    cout << "Weights: ";
    for (int w : weights1) cout << w << " ";
    cout << endl;
    cout << "Values: ";
    for (int v : values1) cout << v << " ";
    cout << endl;
    cout << "Knapsack Capacity: " << capacity1 << endl;
    
    printKnapsackDetails(weights1, values1, capacity1);
    cout << endl;
    
    // Test Case 2
    cout << "Test Case 2:" << endl;
    vector<int> weights2 = {1, 2, 3, 4, 5};
    vector<int> values2 = {10, 40, 30, 50, 35};
    int capacity2 = 8;
    
    cout << "Items: 5" << endl;
    cout << "Weights: ";
    for (int w : weights2) cout << w << " ";
    cout << endl;
    cout << "Values: ";
    for (int v : values2) cout << v << " ";
    cout << endl;
    cout << "Knapsack Capacity: " << capacity2 << endl;
    
    printKnapsackDetails(weights2, values2, capacity2);
    cout << endl;
    
    // Test Case 3
    cout << "Test Case 3:" << endl;
    vector<int> weights3 = {6, 3, 4, 2};
    vector<int> values3 = {30, 14, 16, 9};
    int capacity3 = 10;
    
    cout << "Items: 4" << endl;
    cout << "Weights: ";
    for (int w : weights3) cout << w << " ";
    cout << endl;
    cout << "Values: ";
    for (int v : values3) cout << v << " ";
    cout << endl;
    cout << "Knapsack Capacity: " << capacity3 << endl;
    
    printKnapsackDetails(weights3, values3, capacity3);
    
    return 0;
}
