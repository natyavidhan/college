#include <bits/stdc++.h>
using namespace std;

class Graph {
public:
    int V;
    vector<vector<int>> adj;
    
    Graph(int V) {
        this->V = V;
        adj.resize(V);
    }
    
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    
    void BFS(int start) {
        vector<bool> visited(V, false);
        queue<int> q;
        
        visited[start] = true;
        q.push(start);
        
        cout << "BFS Traversal starting from vertex " << start << ": ";
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            cout << u << " ";
            
            for (int v : adj[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    q.push(v);
                }
            }
        }
        cout << endl;
    }
};

int main() {
    cout << "=== BREADTH-FIRST SEARCH (BFS) ===" << endl << endl;
    
    // Test Case 1
    cout << "Test Case 1:" << endl;
    cout << "Graph with 6 vertices and edges:" << endl;
    cout << "0-1, 0-2, 1-3, 1-4, 2-5" << endl << endl;
    
    Graph g1(6);
    g1.addEdge(0, 1);
    g1.addEdge(0, 2);
    g1.addEdge(1, 3);
    g1.addEdge(1, 4);
    g1.addEdge(2, 5);
    
    g1.BFS(0);
    cout << endl;
    
    // Test Case 2
    cout << "Test Case 2:" << endl;
    cout << "Graph with 7 vertices and edges:" << endl;
    cout << "0-1, 0-2, 1-3, 1-4, 2-5, 2-6" << endl << endl;
    
    Graph g2(7);
    g2.addEdge(0, 1);
    g2.addEdge(0, 2);
    g2.addEdge(1, 3);
    g2.addEdge(1, 4);
    g2.addEdge(2, 5);
    g2.addEdge(2, 6);
    
    g2.BFS(0);
    cout << endl;
    
    // Test Case 3
    cout << "Test Case 3:" << endl;
    cout << "Graph with 5 vertices (complete graph):" << endl;
    cout << "All pairs connected" << endl << endl;
    
    Graph g3(5);
    for (int i = 0; i < 5; i++) {
        for (int j = i + 1; j < 5; j++) {
            g3.addEdge(i, j);
        }
    }
    
    g3.BFS(0);
    
    return 0;
}
