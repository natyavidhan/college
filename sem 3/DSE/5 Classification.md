Classification is a predictive data mining task aimed at assigning objects to one of several predefined categories. It is distinct from regression, as it is used for discrete target variables. The goal of classification is to learn a target function $f$ that maps each attribute set $\mathbf{x}$ to one of the predefined class labels $y$.

The general approach involves:

1. **Induction:** A learning algorithm builds a classification model from a labeled **training set**.
2. **Deduction:** The model is applied to a **test set** (records with unknown class labels) to predict outcomes.
3. The resulting model should exhibit good **generalization capability**—accurately predicting the class labels of previously unknown records.

---

### Naive Bayes Classifier

The Naive Bayes classifier is a Bayesian classification method used to model probabilistic relationships between the attribute set ($\mathbf{X}$) and the class variable ($\mathbf{Y}$).

#### Core Mechanism and Conditional Independence

The classifier works by estimating the posterior probability $P(Y |X)$ using **Bayes theorem**: $$P (Y |X) = \frac{P (X|Y ) \times P (Y)}{P (X)} \text{}$$

The defining feature of the Naive Bayes classifier is the crucial assumption of **conditional independence**: that attributes are conditionally independent given the class label $y$. This assumption simplifies the computation of the class-conditional probability $P(X|Y)$ significantly: $$P (X|Y = y) = \prod_{i=1}^{d} P (X_i|Y = y) \text{}$$ where $\mathbf{X} = {X_1, X_2, \dots, X_d}$ is the set of attributes.

To classify a test record, the classifier calculates the posterior probability for each class $Y$ and chooses the class that maximizes the numerator term, $P (Y ) \prod_{i=1}^{d} P (X_i|Y )$.

#### Estimating Conditional Probabilities

1. **Categorical Attributes:** $P (X_i = x_i|Y = y)$ is estimated by calculating the fraction of training instances in class $y$ that possess the specific attribute value $x_i$.
2. **Continuous Attributes:** Two common methods exist:
    - **Discretization:** Converting continuous attributes into discrete intervals (ordinal attributes) and estimating $P (X_i|Y = y)$ based on the fraction of training records in class $y$ falling within that interval.
    - **Assuming a Distribution:** Assuming the values follow a standard distribution, such as the Gaussian (Normal) distribution. The sample mean ($\mu$) and sample variance ($\sigma^2$) are estimated from training records belonging to class $Y$.

#### Addressing Zero Probabilities

If the training data does not contain examples covering specific attribute values, the calculated conditional probability may be zero. This prevents classification for test records containing those values.

This problem can be addressed using the **m-estimate approach** for estimating conditional probabilities: $$P (x_i|y_j) = \frac{n_c + mp}{n + m} \text{}$$ where $n_c$ is the count of examples of class $y_j$ having value $x_i$, $n$ is the total count of instances from class $y_j$, $m$ is the equivalent sample size, and $p$ is a user-specified prior probability.

#### Characteristics

- **Robustness to Noise:** Naive Bayes classifiers are robust to isolated noise points because these points are averaged out when estimating conditional probabilities.
- **Irrelevant Attributes:** They are robust to irrelevant attributes because if $X_i$ is irrelevant, $P(X_i|Y)$ becomes nearly uniformly distributed, having minimal impact on the overall posterior probability calculation.

---

### Nearest Neighbor Classifier

The Nearest Neighbor classifier is an example of a **lazy learner** because it delays the construction of a classification model until a test example needs to be classified. It is part of **instance-based learning**, which uses specific training examples to make predictions without developing an abstraction or model derived from the data.

#### Core Mechanism

The principle is based on finding all training examples that are relatively similar (nearest neighbors) to the attributes of the test example.

1. A test example is represented as a data point in a $d$-dimensional space (where $d$ is the number of attributes).
2. Its proximity (similarity or distance, such as Euclidean distance or cosine similarity) is calculated to all training points.
3. The **$k$-nearest neighbors** are the $k$ points closest to the test example ($z$).
4. The test example is assigned to the **majority class** of its $k$ nearest neighbors.

#### Voting Schemes

- **Majority Voting:** Each neighbor has the same impact on classification. $$y' = \text{argmax}_v \sum_{(x_i, y_i) \in D_z} I(v = y_i) \text{}$$
- **Distance-Weighted Voting:** The influence of each neighbor ($x_i$) is weighted according to its distance ($w_i = 1/d(x', x_i)^2$). Examples far away have a weaker impact. $$y' = \text{argmax}_v \sum_{(x_i, y_i) \in D_z} w_i \times I(v = y_i) \text{}$$

#### Choosing $k$

Choosing the value of $k$ is important:

- If $k$ is too **small**, the classifier is susceptible to **overfitting** due to noise in the training data.
- If $k$ is too **large**, the nearest-neighbor list may include distant points, potentially leading to misclassification.

#### Characteristics

- **Model Complexity:** It does not require model building.
- **Computational Cost:** Classifying a test example can be expensive for large training sets because proximity must be computed individually between the test and training examples.
- **Robustness:** With small values of $k$, nearest-neighbor classifiers are susceptible to noise since decisions are made locally.

---

### Decision Tree

The Decision Tree classifier is a simple yet widely used classification technique introduced in Chapter 4. It organizes a series of questions about attribute values into a **hierarchical structure** consisting of nodes and directed edges.

#### Structure and Classification Process

A decision tree consists of three types of nodes:

1. **Root node:** Has no incoming edges and zero or more outgoing edges.
2. **Internal node:** Has one incoming edge and two or more outgoing edges.
3. **Leaf node:** Has one incoming edge and is labeled with a class label (e.g., Mammals or Non-mammals).

Classification of a test record starts at the root node, applying the test condition and following the appropriate branch until a leaf node is reached, which provides the predicted class label.

#### Decision Tree Induction (Hunt’s Algorithm)

Many existing decision tree algorithms (like ID3, C4.5, and CART) are based on Hunt's algorithm, which grows the tree recursively by partitioning the training records ($D_t$) into successively purer subsets:

- **Step 1 (Stopping Criterion):** If all records in $D_t$ belong to the same class $y_t$, then $t$ is a leaf node labeled $y_t$.
- **Step 2 (Splitting):** If $D_t$ contains records from more than one class, an attribute test condition is selected to partition the records. A child node is created for each outcome, and the algorithm is recursively applied.

#### Types of Test Conditions

Test conditions depend on the attribute type:

- **Nominal Attributes:** Can result in a multiway split (one child per distinct value) or binary splits (by grouping attribute values into two subsets).
- **Ordinal Attributes:** Similar to nominal, but grouping must preserve the order property.
- **Continuous Attributes:** Usually expressed as a comparison test ($A < v$ or $A \ge v$) with binary outcomes, or a range query ($v_i \le A < v_{i+1}$).

#### Characteristics of Decision Tree Induction

- **Nonparametric:** It does not require prior assumptions regarding the probability distributions satisfied by the class and other attributes.
- **Efficiency:** Techniques for constructing decision trees are computationally inexpensive, allowing quick model construction even with large training sets. Classification is extremely fast (worst-case complexity $O(w)$, where $w$ is the maximum depth).
- **Interpretability:** Smaller trees are relatively easy to interpret.
- **Robustness to Noise and Redundancy:** Decision trees are robust to noise, especially when methods for avoiding overfitting are used. The presence of redundant attributes does not adversely affect accuracy, as only one of the correlated attributes will typically be chosen for splitting.

---

### Overfitting

Overfitting is a pathological issue related to model complexity, affecting all classification techniques.

#### Definition and Impact

Classification errors are categorized into **training errors** (misclassification on training records) and **generalization errors** (expected error on previously unseen records).

**Overfitting** occurs when a classification model, particularly a large decision tree, models the training data too closely—sometimes capturing noise or random patterns unique to the training set. This results in the model performing well on the training data (low training error) but poorly on the test data (high generalization error).

#### Avoiding Overfitting

- **Tree Pruning:** A post-construction step for decision trees used to reduce the size of the tree and improve its generalization capability. Pruning involves trimming branches of the initial tree.
- **Generalization Error Estimation:** Since the learning algorithm only uses the training set, it must estimate the generalization error to guide pruning or model selection. Key methods for estimation include:
    - **Pessimistic Error Estimation:** The generalization error $e_g(T)$ is estimated by adding a penalty term $\Omega(t)$ (representing model complexity) to the observed training error $e(T)$.
    - **Minimum Description Length (MDL) Principle:** An information-theoretic approach where the goal is to find a model that minimizes the total description length, which includes the cost of encoding the tree itself ($Cost(tree)$) and the cost of encoding the data given the tree ($Cost(data|tree)$—often based on classification errors).

---

### Confusion Matrix

The confusion matrix is a fundamental tool for evaluating the performance of a classification model, tabulating the counts of test records that were correctly or incorrectly predicted.

#### Binary Classification Confusion Matrix

For a binary classification problem (e.g., predicting Class 1 vs. Class 0), the matrix entries $f_{ij}$ denote the number of records from actual class $i$ predicted as class $j$.

|Actual Class|Predicted Class = 1|Predicted Class = 0|
|:--|:--|:--|
|Class = 1|$f_{11}$|$f_{10}$|
|Class = 0|$f_{01}$|$f_{00}$|
||**(Table 4.2)**||

The totals are derived from this table:

- Total correct predictions: $(f_{11} + f_{00})$
- Total incorrect predictions: $(f_{10} + f_{01})$

#### Terminology for Metrics (Positive/Negative Classes)

When one class is designated as positive ($+$) and the other as negative ($-$), specific terminology applies, typically used when analyzing imbalanced data:

- **True Positive (TP or $f_{++}$):** Positive examples correctly predicted.
- **False Negative (FN or $f_{+-}$):** Positive examples wrongly predicted as negative.
- **False Positive (FP or $f_{-+}$):** Negative examples wrongly predicted as positive.
- **True Negative (TN or $f_{--}$):** Negative examples correctly predicted.

---

### Evaluation Metrics and Model Evaluation

Model evaluation is performed on the test set to provide an unbiased estimate of the model's generalization error and to compare the relative performance of different classifiers.

#### Basic Metrics: Accuracy and Error Rate

The most common metric is the error rate, or equivalently, accuracy.

- **Error Rate:** The ratio of the number of wrong predictions to the total number of predictions. $$Error\ rate = \frac{f_{10} + f_{01}}{f_{11} + f_{10} + f_{01} + f_{00}} \text{}$$
- **Accuracy:** $1 - \text{Error rate}$. Most algorithms aim to find models achieving the highest accuracy/lowest error rate on the test set.

#### Evaluation Procedures

1. **Holdout Method:** The original labeled data is partitioned into two disjoint sets: a training set (used for model induction) and a test set (used for performance evaluation). The ratio is often 50-50 or 2/3 training and 1/3 testing.
2. **Statistical Comparison:** Observed differences in accuracy between classifiers can be tested for statistical significance. The classification task can be modeled as a binomial experiment to establish confidence intervals for accuracy.

#### Alternative Metrics (For Imbalanced Classes)

When the data set is imbalanced (the rare class is the primary focus), accuracy may be misleading, necessitating alternative metrics derived from the confusion matrix.

|Metric|Definition (in binary terms, usually focused on the Positive class)|Source|
|:--|:--|:--|
|**Precision**|The fraction of predictions belonging to a specified class that are correct.||
|**Recall**|The fraction of objects belonging to a specified class that are correctly identified.||
|**F-measure**|A measure combining precision and recall, often used to assess how well a cluster contains only objects of a particular class and all objects of that class.||
|**Entropy & Purity**|Used in the supervised evaluation of clusterings, measuring the extent to which a cluster contains objects of a single class.||

#### ROC Analysis (Receiver Operating Characteristic)

ROC analysis is a graphical technique particularly suited for analyzing imbalanced data sets. An ROC curve plots the **True Positive Rate (TPR)** against the **False Positive Rate (FPR)**.

- An **ideal model** is located as close as possible to the upper left corner (TPR=1, FPR=0).
- A model making **random guesses** will reside along the main diagonal (where TPR=FPR).

The curve is generated by sorting test records based on their probability of belonging to the positive class and then varying the classification threshold, updating the TPR and FPR at each step.