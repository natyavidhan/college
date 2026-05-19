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
    
    void DFSUtil(int u, vector<bool>& visited) {
        visited[u] = true;
        cout << u << " ";
        
        for (int v : adj[u]) {
            if (!visited[v]) {
                DFSUtil(v, visited);
            }
        }
    }
    
    void DFS(int start) {
        vector<bool> visited(V, false);
        cout << "DFS Traversal starting from vertex " << start << ": ";
        DFSUtil(start, visited);
        cout << endl;
    }
};

int main() {
    cout << "=== DEPTH-FIRST SEARCH (DFS) ===" << endl << endl;
    
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
    
    g1.DFS(0);
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
    
    g2.DFS(0);
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
    
    g3.DFS(0);
    cout << endl;
    
    // Test Case 4: DFS from different starting vertices
    cout << "Test Case 4: DFS from vertex 2 in Test Case 1 graph:" << endl;
    g1.DFS(2);
    
    return 0;
}
