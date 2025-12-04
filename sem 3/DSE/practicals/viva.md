#### What is data mining

Data mining is the process of **automatically discovering useful information in large data repositories**. It combines traditional data analysis methods with sophisticated algorithms designed specifically for processing **large volumes of data**.

The motivation for data mining stems from the rapid advances in data collection and storage, leading to the accumulation of vast amounts of data. Data mining provides the necessary new techniques to answer complex questions that cannot be addressed by existing traditional analysis methods.

#### Relationship between AI, ML, and DM (Visualized conceptually)
- **AI** is the overall concept of intelligent machines.
- **ML** is one way to achieve AI by learning from data.
- **Data Mining** is a process of discovering patterns in data—many ML algorithms are used to achieve this.
 **AI is the goal, ML is the method, and Data Mining is the process of finding useful patterns that ML can learn from.**

#### Core data mining tasks

Data mining tasks are broadly categorized into **predictive** and **descriptive** tasks:

|Category|Task|Objective/Target|
|:--|:--|:--|
|**Predictive**|**Classification**|Predict a **discrete** target variable (e.g., loan default status).|
|**Predictive**|**Regression**|Predict a **continuous** target variable (e.g., stock price forecasting).|
|**Descriptive**|**Cluster Analysis**|Find groups of highly similar objects (unsupervised classification).|
|**Descriptive**|**Association Analysis**|Discover patterns representing frequently co-occurring items or relationships (e.g., market basket rules).|
|**Descriptive**|**Anomaly Detection**|Discover observations (outliers) whose characteristics differ significantly from the rest of the data (e.g., fraud detection).|

#### KDD

**KDD** stands for **Knowledge Discovery in Databases**. Data mining is an **integral part** of the overall KDD process, which aims to **convert raw data into useful information**. This process involves a series of transformation steps, including data preprocessing and postprocessing of data mining results.

---

### Data Preprocessing

#### Why Preprocessing

Preprocessing is necessary to transform the raw input data into an **appropriate format for subsequent analysis**. Since data used for mining is often collected for other purposes, quality issues must be actively detected and corrected (data cleaning).

Key objectives of preprocessing include:

- Improving **data quality**, addressing issues like **noise, outliers, missing values, inconsistent values, and duplicate data**.
- Modifying the data so that it **better fits a specified data mining technique or tool** (e.g., discretizing continuous attributes for classification algorithms).
- Increasing **efficiency** and **performance** by reducing dimensionality or eliminating irrelevant features.

#### Methods to preprocess data

Important preprocessing steps include:

- **Aggregation**
- **Sampling**
- **Dimensionality Reduction**
- **Feature Subset Selection**
- **Feature Creation**
- **Discretization and Binarization**
- **Variable Transformation (Normalization/Standardization)**

#### Dimensionality reduction

Dimensionality reduction refers to techniques that **create new attributes** that are combinations of the old ones, projecting the data from a high-dimensional space into a lower-dimensional space (e.g., Principal Components Analysis, PCA).

**Benefits** of reducing dimensionality include:

1. **Improved Algorithm Performance:** Elimination of irrelevant features and noise, mitigating the _curse of dimensionality_.
2. **More Understandable Models:** Easier visualization or interpretation involving fewer attributes.
3. **Efficiency:** Decreases time and memory required by the algorithm.

When reduction is achieved by selecting a subset of existing attributes, it is known as **feature subset selection**.

#### Aggregation

Aggregation involves summarizing data, which often results in collecting and combining multiple objects into a single object. While aggregation can reduce the data set size and complexity, its main disadvantage is the **loss of interesting details**. Conceptually, aggregation can be viewed as a form of dimensionality reduction (e.g., summing over dimensions in OLAP).

#### Sampling

**Sampling** involves **selecting a subset of the data objects to be analyzed**. Data miners use sampling primarily because **processing the entire dataset is often too time-consuming or expensive**. Using sampling can reduce data size enough to enable the use of better, but more expensive algorithms.

#### Types of sampling

1. **Simple Random Sampling:** Every item has an **equal probability** of being selected.
    - **Sampling without replacement:** Selected item is removed from the population.
    - **Sampling with replacement:** The same object can be selected multiple times.
2. **Stratified Sampling:** Used when the population consists of different types of objects, especially when some types are infrequent (e.g., rare classes). Samples are drawn either equally or proportionally based on the size of predefined groups (strata).

#### How to deal with missing values

Missing values occur when information is uncollected, unavailable, or ignored. The overall goal of preprocessing is to detect and correct data quality issues, which includes addressing missing values. _(The sources define missing values as a quality issue but do not detail specific handling methodologies like mean imputation or specialized data mining techniques for handling them.)_

#### Outliers vs noise

- **Noise:** Refers to **random errors** in a measured variable. Noise often has a spatial or temporal component. Eliminating noise is challenging, and data mining often focuses on robust algorithms to tolerate it.
- **Outliers (Anomalies):** Data objects or attribute values that are **unusual compared to typical values**. Unlike noise, outliers **can be legitimate data objects** and are sometimes the primary focus of the analysis (e.g., fraud detection). Outliers can distort data models like the mean or standard deviation.

#### Boxplot

The box plot is a visualization technique. In the context of data exploration, a box plot can give information about whether the value of an attribute is symmetrically distributed.

---

### Classification

#### Classification vs clustering

|Feature|Classification|Clustering|
|:--|:--|:--|
|**Task Type**|Predictive|Descriptive|
|**Goal**|Assign objects to **predefined categories**|Find **groups (clusters)** based on inherent similarity in the data|
|**Supervised/Unsupervised**|Supervised (requires known labels)|Often Unsupervised (no prior labels needed)|
|**Target Variable**|Must be **discrete**|No predefined target variable|

#### Supervised vs unsupervised

- **Supervised Techniques:** Rely on **known outcomes or labels** to train a model. They learn a function that maps an attribute set $\mathbf{x}$ to a known discrete class label $y$ (Classification) or a continuous value (Regression).
- **Unsupervised Techniques:** Aim to discover patterns and structure in the data **without prior knowledge** of classes or labels. Cluster Analysis is often referred to as unsupervised classification.

#### Methods of implementing classification

Classification methods discussed in the sources include:

- **Decision Tree Classifiers:** Organizes attribute tests into a hierarchical structure to partition the data space.
- **Rule-Based Classifiers:** Use a collection of "**if...then...**" rules to classify records.
- **Nearest Neighbor (k-NN) Classifiers:** A lazy learner that assigns a test example to the majority class of its $k$ closest neighbors in the training data.
- **Naive Bayes Classifiers:** Bayesian methods that model probabilistic relationships, relying on the crucial assumption of **conditional independence** between attributes given the class label.
- **Support Vector Machines (SVM):** A technique that finds a **maximal margin hyperplane** to separate classes, often working well with high-dimensional data.

#### Entropy vs gini

Both **Entropy** and the **Gini Index** are measures used in decision tree induction algorithms (like Hunt's algorithm) to evaluate the **goodness of a split**. They are defined in terms of the class distribution before and after splitting.

- **Entropy** intuitively measures the **purity** of an interval or node.
- Both measures reach their **maximum value when the class distribution is uniform** (e.g., 50/50 mix) and their minimum value (zero) when all records belong to the same class.
- Studies show that the **choice between entropy and Gini index has little effect** on the overall performance of decision tree algorithms, as they are often highly consistent.

#### Significance of entropy

Entropy is a fundamental measure of **purity**. It is used in decision tree induction to choose split points that maximize the resulting purity of the child nodes. An interval or group containing only one class has **zero entropy**, while a perfectly mixed group has maximum entropy. Entropy is also used as a supervised measure to evaluate the quality of clustering results (e.g., how well a cluster aligns with a known class).

#### Confusion matrix

A **confusion matrix** is a table used to tabulate the **counts of test records correctly and incorrectly predicted** by a classification model. For a binary problem (Class 1 is Positive, Class 0 is Negative), the key entries are:

- $f_{11}$: True Positives (Correctly predicted class 1)
- $f_{00}$: True Negatives (Correctly predicted class 0)
- $f_{10}$: False Negatives (Class 1 incorrectly predicted as 0)
- $f_{01}$: False Positives (Class 0 incorrectly predicted as 1)

#### Recall vs precision

These are metrics derived from the confusion matrix, particularly important when dealing with imbalanced classes. They are usually focused on the positive class:

- **Precision:** The fraction of predictions belonging to a specified class that are **correct**.
- **Recall:** The fraction of objects truly belonging to a specified class that are **correctly identified**.

#### F1 score (F-measure)

The **F-measure** is a metric that **combines precision and recall**. It is used to assess how well a cluster or classification result contains only objects of a particular class and simultaneously contains all objects of that class.

#### Why accuracy not sufficient alone

While accuracy (or error rate) is the most common metric, it can be **misleading** when the data set is **imbalanced**. When the rare class is the primary focus (e.g., fraud detection), a high accuracy can be achieved simply by classifying everything as the majority class. Therefore, alternative metrics derived from the confusion matrix, like precision and recall, are necessary to properly evaluate performance.

#### Hold out vs cross validation

- **Holdout Method:** The original labeled data is partitioned into two **disjoint sets**: a **training set** (used for model induction) and a **test set** (used for performance evaluation). Ratios like 50-50 or 2/3 training and 1/3 testing are common.
- **Cross-Validation (k-fold):** The data is segmented into $k$ equal-sized partitions. The procedure is repeated $k$ times, ensuring that each partition is used for testing exactly once. Crucially, **each record is used the same number of times for training and exactly once for testing**.

#### Overfitting

**Overfitting** occurs when a classification model is **too complex** for the training data. An overfit model achieves a low training error (or resubstitution error) but exhibits a high **generalization error** (error on unseen records) because it has essentially memorized the noise in the training set. Techniques like **tree pruning** are used to reduce model size and avoid overfitting.

#### Underfitting

**Underfitting** is a pathology related to model complexity that is mentioned in contrast to overfitting. _(The sources do not provide a detailed definition of underfitting.)_

---

### Association Analysis

#### Association analysis

**Association analysis** is a methodology for **discovering interesting relationships, or patterns**, that are hidden in large data sets. These relationships are typically represented as **association rules**. The task is generally decomposed into two steps: Frequent Itemset Generation and Rule Generation. Association patterns are valuable for business intelligence, such as recommending products or managing inventory.

#### Apriori

The Apriori algorithm is a pioneering method for **Frequent Itemset Generation** that uses **support-based pruning** to control the search space. It is a **level-wise algorithm** that traverses the itemset lattice one size ($k$) at a time (e.g., finding all frequent 1-itemsets before 2-itemsets) using a **generate-and-test strategy**. The key pruning step eliminates candidate $k$-itemsets if any of their proper subsets are known to be infrequent.

#### Support and confidence

These are the two primary metrics used to define strong association rules:

- **Support:** Measures the occurrence frequency of an itemset. An itemset is considered **frequent** if its support meets or exceeds the user-specified **minimum support ($\text{minsup}$)** threshold.
- **Confidence:** Measures the reliability of an inference made by a rule (e.g., in rule $X \rightarrow Y$). Rules must satisfy a minimum confidence threshold ($\text{minconf}$) to be considered **strong**.

#### Frequent itemsets

A **frequent itemset** is a collection of zero or more items whose occurrence frequency meets or exceeds the user-specified minimum support ($\text{minsup}$) threshold. **Finding all frequent itemsets** is the first major subtask of association rule mining.

#### Rules and their significance

Rules represent derived patterns summarizing underlying relationships. The rules are extracted from frequent itemsets and must meet the minimum confidence threshold to be classified as **strong rules**. These rules provide insights, such as finding items that are frequently bought together (e.g., {Diapers} $\rightarrow$ {Milk}).

---

### Clustering

#### Methods of clustering

The three primary clustering techniques discussed in detail are:

1. **K-means:** A **prototype-based, partitional** technique that finds $K$ clusters represented by their centroids.
2. **Agglomerative Hierarchical Clustering:** A collection of techniques that produce a **nested (hierarchical)** structure by repeatedly merging the two closest clusters.
3. **DBSCAN (Density-Based Spatial Clustering of Applications with Noise):** A **density-based, partitional** technique that finds regions of high density and identifies noise points.

Other methods include **Fuzzy Clustering** (e.g., Fuzzy c-means) which assigns membership weights to objects, and **Mixture Model Clustering** (using the EM algorithm) which models clusters as arising from a mixture of distributions.

#### Types of clustering

A collection of clusters is a **clustering**. Types include:

- **Partitional (Unnested):** Divides data objects into non-overlapping subsets, where each object belongs to exactly one subset (e.g., K-means, DBSCAN).
- **Hierarchical (Nested):** A set of nested clusters organized in a tree structure (dendrogram).
- **Exclusive:** Each object is assigned to a single cluster (e.g., standard K-means).
- **Fuzzy:** Each object belongs to every cluster with a membership **weight** (or probability) between 0 and 1.
- **Complete:** Every object in the dataset is assigned to a cluster.
- **Partial:** Some objects (often noise or outliers) are not assigned to a cluster (e.g., DBSCAN).

#### Why normalisation

Normalization or standardization is used to ensure the entire set of values for a variable possesses a specific property. The purpose is **crucial when combining different variables** (e.g., age and income) to **prevent the variable with the largest absolute values from mathematically dominating the results** of a calculation.

#### Need of normalisation in kmeans

K-means relies on calculating distances (often Euclidean $L_2$ distance) between points and cluster centroids. If attributes have widely different numerical scales, the clustering solution will be dominated by the variable with the largest absolute values, leading to biased results. Normalization ensures that all variables contribute equally to the distance computation.

#### Normalisation vs Standardization

The terms **standardization and normalization are often used interchangeably** in the data mining community. A common example of standardization produces a new variable with a **mean of 0 and a standard deviation of 1** using the formula $x' = (x - \bar{x}) / s_x$.

#### Kmeans vs hierarchical vs dbscan

|Feature|K-means (Prototype-based)|Hierarchical (Agglomerative)|DBSCAN (Density-based)|
|:--|:--|:--|:--|
|**Cluster Concept**|Globular/Spherical, based on prototype.|Nested structure (tree).|Arbitrary shapes, based on density.|
|**Output Type**|Complete Partitional clustering.|Hierarchical/Nested clustering.|Partial clustering (discards noise/outliers).|
|**Parameters**|Must specify $K$ (number of clusters).|Requires proximity measure/linkage method.|Requires $Eps$ and $MinPts$.|
|**Noise Handling**|Sensitive to outliers.|Varies greatly by technique (e.g., single link sensitive to noise).|Highly robust, identifies noise explicitly.|

#### Core point, border point, noise, minpts , eps (DBSCAN)

DBSCAN relies on two user-specified parameters: **$Eps$** (the radius of the neighborhood) and **$MinPts$** (the minimum number of points required in the neighborhood).

- **Core point:** A point whose $Eps$ neighborhood contains at least $MinPts$ points. Core points are in the interior of a dense region.
- **Border point:** A point that is within the $Eps$ neighborhood of a core point but does not satisfy the $MinPts$ condition itself.
- **Noise point:** Any point that is neither a core point nor a border point. Noise points are generally discarded.

#### What is SSE

**SSE** stands for the **Sum of the Squared Error**, sometimes known as scatter. It is the most common objective function optimized by the K-means algorithm. SSE is a measure of **cohesion** for prototype-based clusters, where a lower SSE indicates better cohesion (tighter clusters). Minimizing SSE is analogous to maximizing the separation between clusters (Between Group Sum of Squares, SSB).

_The term Mean Squared Error (MSE) is not explicitly defined or discussed in the provided sources, although it is functionally related to SSE in regression models._

#### Name of text book

The excerpts are drawn from the book **"Introduction to Data Mining"** by **Pang-Ning Tan, Michael Steinbach, and Vipin Kumar**.

#### Iris dataset, what all are it's attributes and class labels

The Iris data set is a well-known benchmark data set containing **150 data objects** (flowers).

- **Attributes:** There are four attributes (features): **sepal length, sepal width, petal length, and petal width**.
- **Class Labels:** The flowers belong to one of three species: **Setosa, Versicolour, or Virginica**.

#### Data mining vs machine learning vs deep learning

- **Data Mining (DM):** The core process of **automatically discovering useful information in large data repositories**. It is broader than ML, encompassing preprocessing, data visualization, managing large data, and applying predictive and descriptive tasks.
- **Machine Learning (ML):** A discipline from which DM draws methodology. ML provides the core algorithms (like classification, regression, and clustering algorithms) used in DM to build predictive models or discover descriptive patterns. ML techniques fall into supervised (requiring labels) and unsupervised (without labels) methods.
- **Deep Learning (DL):** _The provided sources reference the broader concept of Artificial Neural Networks (ANN), but do not define or discuss Deep Learning as a specific subset of Machine Learning._