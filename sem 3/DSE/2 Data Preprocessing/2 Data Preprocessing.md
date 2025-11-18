### 2.3.1 Aggregation

**Aggregation** is the process of **combining two or more objects into a single object**.

**Methods and Examples:**

- For **quantitative attributes** (e.g., price), aggregation is typically done by calculating a sum or an average.
- For **qualitative attributes** (e.g., item type), the aggregation might involve omitting the attribute or summarizing it as the set of all values that were present.
- An example of aggregation is replacing all daily transactions of a product at a specific store location with a single store-wide transaction, thereby reducing the number of data objects.

**Motivations for Aggregation:**

1. **Reduced Data Size:** Smaller datasets require less memory and processing time, which may permit the use of more expensive data mining algorithms.
2. **Change of Scope/Scale:** Aggregation provides a **high-level view** of the data instead of a low-level view, acting as a change of scope or scale (e.g., switching from a daily, per-item view to a monthly, per-store view).
3. **Increased Stability:** Aggregate quantities, such as averages or totals, tend to be **more stable** and have less variability than the individual objects being aggregated.

**Disadvantage:** Aggregation can result in the loss of interesting details.

### 2.3.2 Sampling

**Sampling** involves **selecting a subset of the data objects to be analyzed**. Data miners frequently employ sampling because processing the entire dataset is often too time-consuming or expensive.

**Types of Sampling:**

- **Simple Random Sampling:** Every item has an **equal probability** of being selected.
    - **Sampling without replacement:** Once an item is selected, it is removed from the population.
    - **Sampling with replacement:** Objects are not removed, meaning the same object can be selected more than once.
- **Stratified Sampling:** This method is used when the population consists of different types of objects, especially when some types are infrequent (e.g., rare classes in classification). Stratified sampling starts with prespecified groups, and samples can be drawn either equally from each group or proportionally to the size of that group.

**Sample Size Consideration:** Choosing the sample size requires a methodical approach. While larger sample sizes increase the probability that the sample is representative, they reduce the efficiency advantage of sampling. Conversely, very small samples risk missing important patterns or detecting erroneous ones.

### 2.3.3 Dimensionality Reduction (Introduction)

**Dimensionality reduction** addresses the challenge posed by datasets having a very large number of features (e.g., hundreds or thousands of attributes).

**Benefits of Reduction:**

1. **Improved Algorithm Performance:** Many data mining algorithms perform better when dimensionality is lower, as reduction can eliminate irrelevant features and reduce noise.
2. **More Understandable Models:** A reduction in dimensionality can result in a more easily visualized or more understandable model involving fewer attributes.
3. **Efficiency:** Decreases the amount of time and memory required by the data mining algorithm.

**Terminology:** The term "dimensionality reduction" is often reserved for techniques that create **new attributes** that are combinations of the old ones. When the reduction is achieved by selecting a subset of the old attributes, it is known as **feature subset selection** or **feature selection**.

**The Curse of Dimensionality:** This phenomenon refers to the difficulty many data analysis types encounter as dimensionality increases, primarily because the data becomes increasingly sparse in the space it occupies. This sparsity makes concepts like density and distance less meaningful, potentially leading to poor classification accuracy and low-quality clusters.

**Linear Algebra Techniques:** For continuous data, common approaches include **Principal Components Analysis (PCA)** and **Singular Value Decomposition (SVD)**. These project the data from a high-dimensional space into a lower-dimensional space. PCA finds orthogonal new attributes (principal components) that capture the maximum amount of data variation.

### 2.3.4 Feature Subset Selection (Introduction)

**Feature subset selection** is a method for **reducing dimensionality by using only a subset of the available features**. This approach is effective if redundant and irrelevant features are present.

**Types of Unnecessary Features:**

- **Redundant features** duplicate information already contained in one or more other attributes (e.g., sales tax and purchase price).
- **Irrelevant features** provide almost no useful information for the given data mining task (e.g., student ID numbers for predicting GPA).

The presence of these features can degrade classification accuracy and cluster quality.

**Strategies for Selection (Alternatives to Exhaustive Search):** Since trying all $2^n$ subsets of features is usually impractical, systematic alternatives are necessary:

1. **Embedded approaches:** The data mining algorithm itself determines which attributes to use or ignore during its operation.
2. **Filter approaches:** Features are selected **before** the data mining algorithm runs, based on an approach independent of the final data mining task (e.g., selecting attributes with minimal pairwise correlation).
3. **Wrapper approaches:** These methods use the target data mining algorithm as a "black box" to evaluate and find the best subset of attributes.

### 2.3.5 Feature Creation (Introduction)

**Feature creation** involves generating a **new set of attributes** from the original attributes that more effectively captures the essential information in the dataset. This can result in a reduction of attributes and provide the same benefits as dimensionality reduction.

Three related methodologies for feature creation are:

1. **Feature Extraction:** The construction of new features from the raw input data. For instance, in image analysis, processing pixels to determine the presence of high-level features like edges or areas correlated with human faces makes the data suitable for broader classification techniques.
2. **Mapping the Data to a New Space:** This method reveals important features by viewing the data differently. For example, applying a **Fourier transform** to time series data makes frequency information explicit, helping to detect complex periodic patterns otherwise buried in noise. The **wavelet transform** is also useful for time series and other data types.
3. **Feature Construction:** Creating new features by combining existing ones when the necessary information is present but unsuitable for the algorithm in its original form. Often achieved using **domain expertise**; for example, constructing a density feature (mass/volume) to classify historical artifacts based on material composition.

### 2.3.6 Binarization and Discretization of Continuous Attributes

These transformations are often necessary because certain data mining algorithms (e.g., some classification and association algorithms) require data to be in the form of categorical or binary attributes.

#### Discretization of Continuous Attributes

**Discretization** is the process of transforming a continuous attribute into a categorical attribute. The process involves two steps:

1. **Determining the split points:** The sorted continuous attribute values are divided into $n$ intervals using $n-1$ split points.
2. **Mapping:** All values within one interval are mapped to the same categorical value.

**Unsupervised Discretization** (does not use class labels):

- **Equal Width:** Divides the range into a user-specified number of intervals of the same width (sensitive to outliers).
- **Equal Frequency (Equal Depth):** Attempts to place the same number of objects into each interval (often preferred over equal width).
- **Clustering:** Methods like K-means can be used to determine split points.

**Supervised Discretization** (uses class labels):

- These methods aim to place splits to maximize the **purity** of the resulting intervals, as they often produce better results.
- **Entropy-based approaches** are among the most promising. Entropy intuitively measures the purity of an interval; an interval containing only one class has zero entropy, while one with an equal mix of classes has maximum entropy. A simple approach involves iteratively bisecting intervals to achieve minimum overall entropy.

#### Binarization

Binarization converts attributes (continuous or discrete) into one or more binary attributes.

- For **association analysis**, which relies on the presence of items, it often requires **asymmetric binary attributes**.
- **Asymmetric Binary Conversion:** If a categorical attribute has $m$ values, it is often necessary to introduce **one binary attribute for each categorical value** for association problems.
- **Symmetric Binary Conversion (General):** A simple technique for categorical attributes involves mapping $m$ values to integers $[0, m-1]$ and then converting these integers into $n = \lceil \log_2(m) \rceil$ binary attributes. This conversion method, however, can introduce unintended relationships among the transformed attributes.

### 2.3.7 Variable Transformation

A **variable transformation** is a transformation applied consistently to all values of a variable (attribute).

**Simple Functional Transformations:** These involve applying a single mathematical function to each value individually. Examples include $x^k$, $\log x$, $e^x$, $\sqrt{x}$, $1/x$, $\sin x$, or $|x|$.

- In statistics, functions like $\sqrt{x}$, $\log x$, and $1/x$ are commonly used to convert data that lacks a Gaussian (normal) distribution into data that does.
- Transformations must be applied cautiously, as they change the nature of the data (e.g., $1/x$ reverses the order of values between 1 or larger, and also between 0 and 1).

**Normalization or Standardization:** The goal is to ensure the entire set of values for a variable possesses a specific property. The terms standardization and normalization are often used interchangeably in the data mining community.

- **Standardization Example:** $x' = (x - \bar{x}) / s_x$ (where $\bar{x}$ is the mean and $s_x$ is the standard deviation) produces a new variable with a mean of 0 and a standard deviation of 1.
- **Purpose:** This process is crucial when combining different variables (e.g., age and income) to prevent the variable with the largest absolute values (income) from mathematically dominating the results of a calculation.

### 2.4.2 Similarity and Dissimilarity between Simple Attributes

**Proximity** is the collective term referring to either similarity or dissimilarity. Similarity measures can be converted into dissimilarities, and vice versa, generally using any **monotonic decreasing function**.

|Attribute Type|Dissimilarity $d(x, y)$|Similarity $s(x, y)$|
|:--|:--|:--|
|**Nominal**|$d=0$ if $x=y$, $d=1$ if $x \ne y$|$s=1$ if $x=y$, $s=0$ if $x \ne y$|
|**Ordinal**|$d =|x-y|
|**Interval or Ratio**|$d =|x-y|

For interval or ratio attributes, the natural measure of dissimilarity is the absolute difference, with values typically ranging from 0 to $\infty$.

### 2.4.3 Dissimilarities between Data Objects (excluding properties)

This section discusses ways to measure dissimilarity between data objects that have multiple attributes, beginning with distances.

**Distances:**

- **Euclidean Distance ($L_2$):** The standard straight-line distance, defined for one, two, three, or higher-dimensional space.
- **Minkowski Distance ($L_r$):** A general formulation where $r$ specifies how differences across attributes are combined into an overall distance.
    - **Manhattan Distance ($L_1$):** Used for calculating distances (e.g., taxicab distance).
    - **Supremum Distance ($L_\infty$):** Also defined for all dimensions.

Distance matrices produced using $L_1$ or $L_\infty$ distances, for instance, are symmetric (the distance from $x$ to $y$ is the same as the distance from $y$ to $x$).