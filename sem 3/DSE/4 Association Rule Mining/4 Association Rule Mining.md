**Association Analysis** is a methodology useful for discovering interesting relationships, often referred to as patterns, hidden in large data sets. These discovered relationships are typically represented as **association rules**.

The overall task of **Association Rule Mining** is generally decomposed into two major subtasks:

1. **Frequent Itemset Generation:** Finding all itemsets that satisfy the minimum support threshold ($\ge minsup$).
2. **Rule Generation:** Extracting all high-confidence rules (called **strong rules**) from the frequent itemsets found in the first step.

### 1. Transaction Data-set and Itemset

The input data for association analysis is often **market basket transactions**. This data typically consists of records collected at the checkout counters of stores.

- **Definition:** Let $I = {i_1, i_2, \dots, i_d}$ be the set of all items (products) in the market basket data, and $T = {t_1, t_2, \dots, t_N}$ be the set of all transactions.
- **Representation:** Market basket data can be represented in a **binary format** where columns correspond to items (an item is a binary variable: 1 if present in a transaction, 0 otherwise).
- **Itemset:** A collection of zero or more items is an **itemset**. If an itemset contains $k$ items, it is called a $\mathbf{k}$-itemset.
- **Transaction Containment:** A transaction $t_j$ is said to **contain** an itemset $X$ if $X$ is a subset of $t_j$ ($X \subseteq t_j$).
- **Frequent Itemset:** An itemset is considered **frequent** if its occurrence frequency meets or exceeds a user-specified threshold called **minimum support** ($minsup$).

### 2. Support Measure

Support is an objective measure used both to define frequent itemsets and to evaluate association rules.

- **Support Count ($\sigma(X)$):** The number of transactions that contain a particular itemset $X$. $$\sigma(X) = \left|{t_i | X \subseteq t_i, t_i \in T}\right| \quad$$
- **Support ($s(X \rightarrow Y)$):** The support of an association rule $X \rightarrow Y$ is the fraction of total transactions ($N$) that contain both $X$ and $Y$ (i.e., contain the itemset $X \cup Y$). $$s(X \rightarrow Y) = \frac{\sigma(X \cup Y)}{N} \quad$$
- **Role of Support:** Support is crucial for eliminating uninteresting rules that may occur simply by chance or are not profitable to promote (due to low volume).

### 3. Association Rule and Confidence of Association Rule

An association rule expresses an implication relationship between two itemsets.

- **Definition:** An association rule is an expression of the form $\mathbf{X} \rightarrow \mathbf{Y}$, where $X$ and $Y$ are non-empty and disjoint itemsets ($X \cap Y = \emptyset$).
- **Confidence ($c(X \rightarrow Y)$):** Confidence measures the reliability of the inference made by a rule; specifically, it is the conditional probability that a transaction contains $Y$, given that it already contains $X$. $$c(X \rightarrow Y) = \frac{\sigma(X \cup Y)}{\sigma(X)} \quad$$
- **Strong Rule:** A rule is considered a strong rule if it satisfies both the minimum support ($\ge minsup$) and the minimum confidence ($\ge minconf$) thresholds.

### 4. Apriori Principle

The Apriori principle is a fundamental property used to efficiently prune the vast search space of potential itemsets during the Frequent Itemset Generation stage.

- **Theorem 6.1 (Apriori Principle): If an itemset is frequent, then all of its subsets must also be frequent**.
- **Anti-monotone Property:** The Apriori principle relies on the **anti-monotone property of the support measure**, meaning that the support for an itemset never exceeds the support for any of its subsets. If $X \subseteq Y$, then $s(Y) \leq s(X)$.
- **Pruning Strategy:** Conversely, if an itemset is found to be infrequent, all of its supersets must also be infrequent and can be immediately pruned from consideration. This is known as **support-based pruning**.

### 5. Apriori Algorithm (Frequent Itemset Generation)

The Apriori algorithm was a pioneering approach that systematically used support-based pruning to control the exponential search space.

- **Approach:** Apriori is a **level-wise algorithm**; it traverses the itemset lattice one level (size $k$) at a time. It uses a **generate-and-test strategy** where candidate itemsets are generated, tested against the transactions (for support counting), and then pruned.
    
- **High-Level Steps (Algorithm 6.1):**
    
    1. **Initialization (k=1):** Scan the data once to find the support of each item and determine the set of **frequent 1-itemsets** ($F_1$).
    2. **Iteration (k > 1):** Repeatedly generate new candidate $k$-itemsets ($C_k$) from $F_{k-1}$ using the `apriori-gen` function.
    3. **Support Counting:** Perform an additional pass over the dataset ($T$) to calculate the support count ($\sigma$) for each candidate itemset $c \in C_k$. The `subset` function identifies all candidates in $C_k$ contained within a transaction $t$.
    4. **Extraction:** Extract the **frequent $k$-itemsets** ($F_k$) by eliminating candidates whose support counts are less than $minsup$.
    5. **Termination:** The process repeats until no new frequent itemsets are generated ($F_k = \emptyset$).
- **Candidate Generation and Pruning (apriori-gen):** The `apriori-gen` function performs two steps:
    
    1. **Candidate Generation:** Generates new candidate $k$-itemsets, typically by merging pairs of frequent $(k-1)$-itemsets. (The specific method used by Apriori is the $F_{k-1} \times F_{k-1}$ method, which merges pairs only if their first $k-2$ items are identical).
    2. **Candidate Pruning:** Eliminates candidate $k$-itemsets $X$ if any of their proper subsets ($X - {i_j}$) are known to be infrequent (based on the Apriori principle). This drastically reduces the number of candidates that need full support counting.

### 6. Rule Generation (Confidence-Based Pruning)

Once all frequent itemsets are found, the next step is to generate high-confidence rules from these itemsets.

- **Support is Satisfied:** Every rule $X \rightarrow Y$ derived from a frequent itemset $X \cup Y$ must inherently satisfy the minimum support threshold, as the support of the rule is identical to the support of its originating frequent itemset.
- **Confidence Check:** Computing the confidence of a rule does not require additional scans of the transaction data, as the necessary support counts ($\sigma(X \cup Y)$ and $\sigma(X)$) were already computed during the frequent itemset generation stage.
- **Confidence-Based Pruning (Theorem 6.2):** When examining rules derived from the same frequent itemset $Y$, the confidence measure exhibits a useful property: **If a rule $X \rightarrow Y - X$ does not satisfy the confidence threshold, then any rule $X' \rightarrow Y - X'$ where $X'$ is a subset of $X$ must also fail the confidence threshold**.
- **Implication:** Because of this property, rule generation can proceed level-wise (based on the size of the rule consequent). If a rule fails the confidence test, rules with larger antecedents (and smaller consequents) that are subsets of the original rule's antecedent can be pruned immediately. For instance, if ${bcd} \rightarrow {a}$ has low confidence, all rules with consequent ${a}$ derived from subsets of ${bcd}$ (e.g., ${cd} \rightarrow {ab}$) can be discarded.

---

**Analogy:** The Apriori algorithm is like using a **sieve to refine flour**. The frequent itemset generation process repeatedly uses the **Apriori Principle** (the property that all subsets of frequent items must also be frequent) as the sifting mechanism. In the first pass, you sieve coarse material (1-itemsets). In subsequent passes, you use the previously collected frequent material to predict which larger chunks (k-itemsets) might pass through the next, finer sieve. If a large chunk (supersets) contains too much unusable material (infrequent subsets), you don't even bother putting it through the sieve, thereby saving a lot of unnecessary work.