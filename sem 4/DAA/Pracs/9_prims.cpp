#include <bits/stdc++.h>
using namespace std;

class Graph {
public:
    int V;
    vector<vector<pair<int, int>>> adj; // {vertex, weight}
    
    Graph(int V) {
        this->V = V;
        adj.resize(V);
    }
    
    void addEdge(int u, int v, int weight) {
        adj[u].push_back({v, weight});
        adj[v].push_back({u, weight});
    }
    
    void primMST() {
        vector<int> key(V, INT_MAX);
        vector<bool> inMST(V, false);
        vector<int> parent(V, -1);
        
        key[0] = 0;
        int totalWeight = 0;
        
        cout << "Minimum Spanning Tree using Prim's Algorithm:" << endl;
        cout << "Edge\tWeight" << endl;
        
        for (int count = 0; count < V - 1; count++) {
            int u = -1;
            for (int v = 0; v < V; v++) {
                if (!inMST[v] && (u == -1 || key[v] < key[u]))
                    u = v;
            }
            
            inMST[u] = true;
            
            if (parent[u] != -1) {
                cout << parent[u] << "-" << u << "\t" << key[u] << endl;
                totalWeight += key[u];
            }
            
            for (auto [v, weight] : adj[u]) {
                if (!inMST[v] && weight < key[v]) {
                    key[v] = weight;
                    parent[v] = u;
                }
            }
        }
        
        cout << "Total Weight of MST: " << totalWeight << endl;
    }
};

int main() {
    cout << "=== PRIM'S ALGORITHM FOR MINIMUM SPANNING TREE ===" << endl << endl;
    
    // Test Case 1: Small graph
    cout << "Test Case 1: 5 vertices" << endl;
    Graph g1(5);
    g1.addEdge(0, 1, 2);
    g1.addEdge(0, 3, 6);
    g1.addEdge(1, 2, 3);
    g1.addEdge(1, 3, 8);
    g1.addEdge(1, 4, 5);
    g1.addEdge(2, 4, 7);
    g1.addEdge(3, 4, 1);
    
    g1.primMST();
    cout << endl;
    
    // Test Case 2: 6 vertices
    cout << "Test Case 2: 6 vertices" << endl;
    Graph g2(6);
    g2.addEdge(0, 1, 4);
    g2.addEdge(0, 2, 2);
    g2.addEdge(1, 2, 1);
    g2.addEdge(1, 3, 5);
    g2.addEdge(2, 3, 8);
    g2.addEdge(2, 4, 10);
    g2.addEdge(3, 4, 2);
    g2.addEdge(3, 5, 6);
    g2.addEdge(4, 5, 3);
    
    g2.primMST();
    cout << endl;
    
    // Test Case 3: 4 vertices (simple square)
    cout << "Test Case 3: 4 vertices (square graph)" << endl;
    Graph g3(4);
    g3.addEdge(0, 1, 1);
    g3.addEdge(1, 2, 3);
    g3.addEdge(2, 3, 2);
    g3.addEdge(3, 0, 4);
    g3.addEdge(0, 2, 5);
    g3.addEdge(1, 3, 6);
    
    g3.primMST();
    
    return 0;
}
