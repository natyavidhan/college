import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Iris Dataset Shape:", X.shape)
print("Features:", iris.feature_names)


class KMeans:
    """Simple K-Means implementation that tracks MSE per iteration"""
    
    def __init__(self, n_clusters=3, max_iter=100, random_state=42):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.random_state = random_state
        self.centroids = None
        self.labels = None
        self.mse_history = []  # Track MSE after each iteration
    
    def fit(self, X):
        np.random.seed(self.random_state)
        n_samples, n_features = X.shape
        
        # Initialize centroids randomly from the data points
        random_indices = np.random.choice(n_samples, self.n_clusters, replace=False)
        self.centroids = X[random_indices].copy()
        
        self.mse_history = []
        
        for iteration in range(self.max_iter):
            # Assign each point to the nearest centroid
            self.labels = self._assign_clusters(X)
            
            # Calculate MSE for this iteration
            mse = self._calculate_mse(X)
            self.mse_history.append(mse)
            
            # Update centroids
            new_centroids = np.zeros((self.n_clusters, n_features))
            for k in range(self.n_clusters):
                cluster_points = X[self.labels == k]
                if len(cluster_points) > 0:
                    new_centroids[k] = cluster_points.mean(axis=0)
                else:
                    new_centroids[k] = self.centroids[k]
            
            # Check for convergence
            if np.allclose(self.centroids, new_centroids):
                print(f"Converged at iteration {iteration + 1}")
                break
            
            self.centroids = new_centroids
        
        return self
    
    def _assign_clusters(self, X):
        distances = np.zeros((X.shape[0], self.n_clusters))
        for k in range(self.n_clusters):
            distances[:, k] = np.linalg.norm(X - self.centroids[k], axis=1)
        return np.argmin(distances, axis=1)
    
    def _calculate_mse(self, X):
        total_error = 0
        for k in range(self.n_clusters):
            cluster_points = X[self.labels == k]
            if len(cluster_points) > 0:
                total_error += np.sum((cluster_points - self.centroids[k]) ** 2)
        return total_error / X.shape[0]
    
    def predict(self, X):
        return self._assign_clusters(X)


# ============================================================
# Part 1: Apply K-Means and plot MSE per iteration
# ============================================================
print("\n" + "="*60)
print("Part 1: K-Means with k=3 (default for Iris)")
print("="*60)

kmeans = KMeans(n_clusters=3, max_iter=100, random_state=42)
kmeans.fit(X_scaled)

print(f"Final MSE: {kmeans.mse_history[-1]:.4f}")
print(f"Number of iterations: {len(kmeans.mse_history)}")

# Plot MSE vs Iteration
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(kmeans.mse_history) + 1), kmeans.mse_history, 'b-o', linewidth=2, markersize=8)
plt.xlabel('Iteration', fontsize=12)
plt.ylabel('Mean Squared Error (MSE)', fontsize=12)
plt.title('K-Means: MSE vs Iteration (k=3)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('kmeans_mse_iteration.png', dpi=150)
plt.show()


# ============================================================
# Part 2: Compare performance by varying number of clusters (k)
# ============================================================
print("\n" + "="*60)
print("Part 2: Comparing different values of k")
print("="*60)

k_values = [2, 3, 4, 5, 6, 7, 8]
final_mse_values = []
mse_histories = {}

for k in k_values:
    km = KMeans(n_clusters=k, max_iter=100, random_state=42)
    km.fit(X_scaled)
    final_mse_values.append(km.mse_history[-1])
    mse_histories[k] = km.mse_history
    print(f"k={k}: Final MSE = {km.mse_history[-1]:.4f}, Iterations = {len(km.mse_history)}")

# Plot Final MSE vs k (Elbow Method)
plt.figure(figsize=(10, 6))
plt.plot(k_values, final_mse_values, 'r-o', linewidth=2, markersize=10)
plt.xlabel('Number of Clusters (k)', fontsize=12)
plt.ylabel('Final MSE', fontsize=12)
plt.title('Elbow Method: Final MSE vs Number of Clusters', fontsize=14)
plt.xticks(k_values)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('kmeans_elbow.png', dpi=150)
plt.show()

# Plot MSE per iteration for different k values
plt.figure(figsize=(12, 6))
for k in [2, 3, 4, 5]:
    plt.plot(range(1, len(mse_histories[k]) + 1), mse_histories[k], '-o', label=f'k={k}', markersize=6)
plt.xlabel('Iteration', fontsize=12)
plt.ylabel('Mean Squared Error (MSE)', fontsize=12)
plt.title('MSE vs Iteration for Different k Values', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('kmeans_mse_comparison.png', dpi=150)
plt.show()


# ============================================================
# Part 3: Compare performance by varying random initialization
# ============================================================
print("\n" + "="*60)
print("Part 3: Comparing different random initializations (k=3)")
print("="*60)

random_states = [0, 10, 42, 100, 200]
init_mse_histories = {}

plt.figure(figsize=(12, 6))
for rs in random_states:
    km = KMeans(n_clusters=3, max_iter=100, random_state=rs)
    km.fit(X_scaled)
    init_mse_histories[rs] = km.mse_history
    print(f"Random State {rs}: Final MSE = {km.mse_history[-1]:.4f}, Iterations = {len(km.mse_history)}")
    plt.plot(range(1, len(km.mse_history) + 1), km.mse_history, '-o', label=f'seed={rs}', markersize=6)

plt.xlabel('Iteration', fontsize=12)
plt.ylabel('Mean Squared Error (MSE)', fontsize=12)
plt.title('MSE vs Iteration for Different Random Initializations (k=3)', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('kmeans_init_comparison.png', dpi=150)
plt.show()


# ============================================================
# Part 4: Visualize clustering results
# ============================================================
print("\n" + "="*60)
print("Part 4: Clustering Visualization")
print("="*60)

# Final clustering with k=3
kmeans_final = KMeans(n_clusters=3, max_iter=100, random_state=42)
kmeans_final.fit(X_scaled)

# Plot clusters using first two features (sepal length vs sepal width)
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
scatter = plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=kmeans_final.labels, cmap='viridis', alpha=0.7)
plt.scatter(kmeans_final.centroids[:, 0], kmeans_final.centroids[:, 1], 
            c='red', marker='X', s=200, edgecolors='black', linewidths=2, label='Centroids')
plt.xlabel('Sepal Length (scaled)', fontsize=12)
plt.ylabel('Sepal Width (scaled)', fontsize=12)
plt.title('K-Means Clustering (k=3)', fontsize=14)
plt.legend()
plt.colorbar(scatter, label='Cluster')

plt.subplot(1, 2, 2)
scatter = plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=y, cmap='viridis', alpha=0.7)
plt.xlabel('Sepal Length (scaled)', fontsize=12)
plt.ylabel('Sepal Width (scaled)', fontsize=12)
plt.title('Actual Iris Species', fontsize=14)
plt.colorbar(scatter, label='Species')

plt.tight_layout()
plt.savefig('kmeans_clusters.png', dpi=150)
plt.show()


# ============================================================
# Summary Table
# ============================================================
print("\n" + "="*60)
print("Summary: Performance Comparison")
print("="*60)

summary_data = {
    'k': k_values,
    'Final MSE': [f"{mse:.4f}" for mse in final_mse_values],
    'Iterations': [len(mse_histories[k]) for k in k_values]
}
summary_df = pd.DataFrame(summary_data)
print("\nPerformance by Number of Clusters:")
print(summary_df.to_string(index=False))

print("\nConclusion:")
print("- As k increases, MSE decreases (more clusters = less error)")
print("- The 'elbow' in the MSE curve suggests optimal k")
print("- Different initializations can lead to different final solutions")
print("- For Iris dataset, k=3 is optimal (matching 3 species)")
