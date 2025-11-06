## 1. Basic Concepts of Clustering

**Cluster analysis** is a fundamental task in data mining that divides data into **groups (clusters)** that are either meaningful or useful, or both. The primary objective is to group data objects such that the objects **within a group are highly similar (or related)** to one another and **different from (or unrelated to)** the objects in other groups.

Cluster analysis is often referred to as **unsupervised classification**, differentiating it from supervised classification where class labels are already known.

### Goals and Utility of Clustering

Cluster analysis serves various purposes, categorized primarily as **understanding** or **utility**:

- **Understanding (Finding Classes):** Clusters are potential classes used to capture the natural structure of the data. Examples include identifying different subcategories of an illness in medicine or grouping genes with similar functions in biology.
- **Utility (Abstraction and Efficiency):** Clustering provides an abstraction from individual data objects to the resulting cluster groups.
    - **Summarization:** Cluster prototypes can reduce large datasets, allowing complex analyses (like regression or PCA, typically $O(m^2)$ complexity) to be applied efficiently to the reduced set of prototypes.
    - **Compression:** Prototypes can be used for data compression, known as vector quantization, often applied to image, sound, and video data.
    - **Efficiently Finding Nearest Neighbors:** Clustering can reduce the number of pairwise distance computations required to find an object's nearest neighbors.

## 2. Measure of Similarity and Dissimilarity

The relationship between two objects is quantified by **proximity**, a term used to refer to either **similarity** or **dissimilarity**.

- **Similarity:** A numerical measure of the degree to which two objects are alike. Similarities are higher for more alike pairs and are typically non-negative, often ranging between 0 (no similarity) and 1 (complete similarity).
- **Dissimilarity (Distance):** A numerical measure of the degree to which two objects are different. Dissimilarities are lower for more similar pairs and often range from 0 to $\infty$.
- **Metrics:** Measures that satisfy specific properties—non-negativity, self-similarity, symmetry ($d(x,y) = d(y,x)$), and the **Triangle Inequality** ($d(x, z) \leq d(x,y) + d(y, z)$)—are known as metrics.

### Common Proximity Measures

The correct choice of proximity measure is crucial and depends on the type of data.

|Attribute Type|Dissimilarity Examples|Similarity Examples|
|:--|:--|:--|
|Interval or Ratio|Euclidean distance ($d$), Manhattan distance ($L_1$), Supremum distance ($L_{\infty}$)|Cosine similarity|
|Binary/Asymmetric|Jaccard coefficient (ignores 0-0 matches)|Cosine similarity (for sparse data)|

- **Euclidean Distance (L2 norm):** Defined for points in one, two, three, or higher-dimensional space.
- **Cosine Similarity:** Frequently used for **sparse data** such as documents, as it ignores 0-0 matches.

## 3. Types of Clusters and Clustering Methods

### Types of Clusterings

A collection of clusters is called a **clustering**.

1. **Partitional (Unnested):** A division of data objects into non-overlapping subsets such that each object belongs to exactly one subset. K-means and DBSCAN produce partitional clusterings.
2. **Hierarchical (Nested):** A set of nested clusters organized as a tree structure.
3. **Exclusive:** Each object is assigned to a single cluster (e.g., standard K-means).
4. **Fuzzy:** Clusters are treated as fuzzy sets; every object belongs to every cluster with a membership **weight** (or probability) between 0 and 1, usually constrained so that the weights sum to 1 for each object.
5. **Complete:** Every object in the dataset is assigned to a cluster.
6. **Partial:** Some objects, often representing noise or outliers, are not assigned to a cluster.

### Types of Clusters

The definition of what constitutes a "good" cluster varies:

- **Well-Separated Clusters:** A cluster where every object is closer (or more similar) to every other object within the cluster than to **any** object not in the cluster. They do not need to be globular and can have any shape.
- **Prototype-Based (Center-Based) Clusters:** A cluster where each object is closer (more similar) to the prototype (centroid or medoid) defining the cluster than to the prototype of any other cluster. These clusters typically tend to be **globular**.
- **Density-Based Clusters:** A cluster defined as a **dense region of objects that is surrounded by a region of low density**. This definition is effective when clusters are irregular or intertwined, especially when noise and outliers are present.

## 4. Distance-Based Method: K-means Algorithm

K-means is a **prototype-based, partitional clustering technique** that attempts to find $K$ clusters, where $K$ is specified by the user.

### The Basic K-means Algorithm (Algorithm 8.1)

The algorithm uses an iterative refinement approach:

1. **Select $K$ initial centroids**.
2. **Repeat:** a. **Form $K$ clusters** by assigning each point to its **closest centroid**. b. **Recompute the centroid** (mean) of each cluster.
3. **Until** the centroids do not change.

The centroid that minimizes the sum of squared error (SSE) for a cluster in Euclidean space is the **mean** of the points in that cluster.

### Objective Function

The goal of K-means is typically expressed by minimizing the **Sum of the Squared Error (SSE)**, also known as scatter.

$$SSE = \sum_{i=1}^{K} \sum_{x \in C_i} dist(c_i, x)^2$$

- The algorithm minimizes SSE by iteratively performing the assignment and update steps, but is only guaranteed to find a **local minimum**. Different initializations can lead to different clustering results and different SSE values.

### Strengths and Weaknesses of K-means (Section 8.2.5)

|Strengths|Weaknesses|
|:--|:--|
|Simple and widely applicable to various data types.|Cannot find clusters with **non-spherical shapes**.|
|Highly efficient, with modest time complexity $O(I \cdot K \cdot m \cdot n)$.|Has difficulty with clusters of **widely different sizes or densities**.|
||Sensitive to **outliers**.|
||Requires the number of clusters, $K$, to be specified.|
||Requires data for which a notion of a center (centroid) exists.|

## 5. Density-Based Method: DBSCAN Algorithm

DBSCAN (**D**ensity-**B**ased **S**patial **C**lustering of **A**pplications with **N**oise) locates regions of high density separated by regions of low density. It results in a partitional, non-exclusive, and partial clustering, as it identifies and discards noise points.

### Density Concepts

DBSCAN relies on two user-specified parameters, the radius **$Eps$** and the minimum number of points **$MinPts$**.

1. **Core points:** A point is a core point if its $Eps$ neighborhood contains at least $MinPts$ points. Core points are in the interior of a dense region.
2. **Border points:** A point that is _within the $Eps$ neighborhood of a core point_ but does not have $MinPts$ points in its own neighborhood.
3. **Noise points:** Any point that is neither a core point nor a border point. Noise points are generally discarded.

### The DBSCAN Algorithm (Algorithm 8.4 simplified)

1. Label all points as core, border, or noise points.
2. Eliminate noise points.
3. Put an edge between all core points that are within $Eps$ of each other.
4. Make each group of **connected core points** into a separate cluster.
5. Assign each border point to one of the clusters of its associated core points.

### Parameter Selection

The selection of $Eps$ and $MinPts$ can be done systematically by examining the **k-dist graph**. By calculating the distance from every point to its $k^{th}$ nearest neighbor (where $k$ is often chosen as $MinPts$), sorting these distances, and plotting them, a sharp change (or "knee") is expected. This knee indicates a suitable value for $Eps$.

### Strengths and Weaknesses of DBSCAN

|Strengths|Weaknesses|
|:--|:--|
|Can find clusters of **arbitrary (non-globular) shape**.|Has difficulty when clusters exhibit **widely varying densities**.|
|Highly robust to **noise and outliers** (as it explicitly labels and discards them).|Density definition can be meaningless in **high-dimensional data**.|
|Automatically determines the **number of clusters**.|Requires setting two parameters ($Eps$ and $MinPts$).|
|Non-deterministic: produces the same clusters in different runs.|Time complexity can be $O(m^2)$ in the worst case (though often better for low-dimensional data).|

## 6. Comparison of K-means and DBSCAN

|Feature|K-means|DBSCAN|
|:--|:--|:--|
|**Cluster Concept**|Prototype-based (globular/spherical).|Density-based (arbitrary shapes).|
|**Output**|Complete clustering (assigns all objects).|Partial clustering (discards noise/outliers).|
|**Cluster Shape/Size**|Struggles with arbitrary shapes and widely varying sizes/densities.|Handles arbitrary shapes well; generally robust against noise.|
|**Number of Clusters**|Must be specified ($K$ parameter).|Determined automatically (based on density parameters).|
|**Initialization**|Non-deterministic (results depend on initial centroid selection).|Deterministic (produces the same result given the same parameters).|
|**Computational Complexity**|Generally fast, linear time complexity $O(m)$.|Can be slow, $O(m^2)$ in worst case.|
|**Underlying Model**|Based on optimizing an objective function (SSE); analogous to Gaussian mixture models.|Not based on a formal optimization model.|

## 7. Cluster Validation Measures and Optimal K

**Cluster validation** (evaluation) is necessary because almost every clustering algorithm will find clusters in data, even if the underlying data structure is random.

### Unsupervised (Internal) Measures

These measures evaluate the clustering quality using only the data itself (internal information):

- **Cohesion Measures:** Determine how closely related objects within a cluster are. The **Sum of Squared Error (SSE)** is a classic measure of cohesion for prototype-based clusters; lower SSE indicates better cohesion.
- **Separation Measures:** Determine how distinct or well-separated clusters are from one another. The **Between Group Sum of Squares (SSB)** measures prototype separation, where maximizing SSB is equivalent to minimizing SSE (for Euclidean data).
- **Silhouette Coefficient:** Combines both cohesion and separation into a single metric for individual points, clusters, or the entire clustering.

### Determining the Optimal Number of Clusters (K)

Unsupervised measures can be used to approximate the optimal number of clusters:

1. **SSE Plot:** Plot the SSE against the number of clusters ($K$). The correct number of clusters is often indicated by a distinct **"knee"** in the plot, where adding more clusters yields diminishing returns in error reduction.
2. **Average Silhouette Coefficient Plot:** Plot the average silhouette coefficient against $K$. The optimal number of clusters is often indicated by a distinct **"peak"** in the plot.