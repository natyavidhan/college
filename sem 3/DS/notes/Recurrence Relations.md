### 4.3 The Substitution Method for Solving Recurrences

The substitution method is generally the **most robust method** for solving recurrences. It requires you to make a good guess for the solution and then formally verify it using mathematical induction.

#### Steps of the Method

The substitution method involves two steps:

1. **Guess the form of the solution** using symbolic constants.
2. **Use mathematical induction to show that the solution works**, and determine the necessary constants. To apply the inductive hypothesis, you substitute the guessed solution for the function on smaller arguments.

#### Usage and Bounding

- This method can be used to establish either an asymptotic **upper bound (O-bound)** or a **lower bound (Ω-bound)**.
- It is generally recommended to prove the upper and lower bounds separately rather than attempting to prove a tight **Θ-bound** directly.

#### Importance of Precise Induction

- It is crucial to **avoid using asymptotic notation** (like $O(n \lg n)$) within the inductive hypothesis itself, as this can lead to erroneous proofs where the hidden constant implicitly changes.
- The inductive hypothesis must be stated with explicit constants (e.g., $T(n) \le cn \lg n$). You must explicitly prove the exact statement of the inductive hypothesis.

#### Technique: Subtracting Lower-Order Terms

- A "trick of the trade" addresses situations where a correct asymptotic guess fails to satisfy the inductive hypothesis. If the inequality does not hold, it may be necessary to **strengthen the inductive hypothesis by subtracting a lower-order term**.
- For example, if you guess $T(n) = O(n)$ for $T(n) = 2T(n/2) + \Theta(1)$, but the proof yields $T(n) \le cn + \Theta(1)$ (which doesn't guarantee $T(n) \le cn$), you should try $T(n) \le cn - d$ instead.
- Subtracting the term $d$ works because, if the coefficient of the recursive call is $a$, the subtraction results in $-a \cdot d$, which helps absorb the $\Theta(1)$ term.

#### Handling Base Cases (Algorithmic Recurrences)

- For most algorithmic recurrences (those describing the running time of correct divide-and-conquer algorithms), the base cases $T(n) = \Theta(1)$ for small $n$ are handled by choosing the leading constant $c$ large enough to satisfy the bound for the base values.
- By convention, when a recurrence is stated without an explicit base case, it is assumed to be **algorithmic**.

---

### 4.4 The Recursion-Tree Method for Solving Recurrences

The recursion-tree method is a visual technique that helps convert a recurrence into a summation, providing a mechanism to **generate a good guess** for the solution, which is then verified using the substitution method.

#### Mechanism and Structure

- **Modeling Cost:** Each node in the tree represents the cost of a single subproblem within the set of recursive function invocations.
- **Calculation:** To find the total cost, you typically sum the costs at each level of the tree to find the per-level costs, and then sum all the per-level costs.
- **Height:** The height of the tree depends on how rapidly the subproblem size decreases.

#### Illustrative Example: $T(n) = 3T(n/4) + cn^2$

1. **Root Cost:** The top level (depth 0) costs $cn^2$.
2. **Subproblem Sizes:** At depth $i$, the subproblem size is $n/4^i$.
3. **Nodes per Level:** At depth $i$, the number of nodes is $3^i$.
4. **Cost per Node:** Each node at depth $i$ costs $c(n/4^i)^2$.
5. **Total Cost per Level:** The cost at depth $i$ is $3^i \cdot c(n/4^i)^2 = (3/16)^i cn^2$.
6. **Total Cost:** The total cost is the sum $\sum_{i=0}^{\log_4 n - 1} (\frac{3}{16})^i cn^2 + \Theta(n^{\log_4 3})$.
7. **Result:** Since the series is a geometrically decreasing series dominated by the first term (root cost $cn^2$), the guess is $T(n) = O(n^2)$.

#### Irregular Example: Unbalanced Recursion

- The method can model **unbalanced recursion trees**, such as $T(n) = T(n/3) + T(2n/3) + cn$.
- **Height:** The tree's height is determined by the longest path, which follows the larger fraction ($2n/3$). The height is $h = \log_{3/2} n = \Theta(\lg n)$.
- **Cost per Level:** The sum of costs across any full level is $cn$.
- **Result:** Since there are $\Theta(\lg n)$ levels, the total cost is $\Theta(cn \lg n)$, leading to the solution $T(n) = \Theta(n \lg n)$.

---

### 4.5 The Master Method for Solving Recurrences

The master method is a straightforward "cookbook" approach used to solve a specific class of algorithmic recurrences, known as **master recurrences**.

#### Master Recurrence Form

The method applies to recurrences of the form: $$T(n) = aT(n/b) + f(n)$$ Where:

- $a \ge 1$ (the number of subproblems) and $b > 1$ (the factor by which input size is reduced) are constants.
- $f(n)$ is the **driving function** representing the time cost for the divide and combine steps.

A crucial element for applying the master theorem is the **watershed function**, $n^{\log_b a}$. The asymptotic solution depends on comparing the driving function $f(n)$ to this watershed function.

#### Master Theorem (Theorem 4.1)

The theorem categorizes the solution into three cases based on the comparison between $f(n)$ and $n^{\log_b a}$:

|Case|Condition (Comparison)|Result (Solution $T(n)$)|Intuition (Recursion Tree)|
|:--|:--|:--|:--|
|**1**|$f(n)$ is polynomially smaller than $n^{\log_b a}$. (Requires $f(n) = O(n^{\log_b a - \epsilon})$ for some $\epsilon > 0$).|$T(n) = \Theta(n^{\log_b a})$.|**Leaves dominate.** Cost grows geometrically from root to leaves.|
|**2**|$f(n)$ is polylogarithmically similar to $n^{\log_b a}$. (Requires $f(n) = \Theta(n^{\log_b a} \lg^k n)$ for some $k \ge 0$).|$T(n) = \Theta(n^{\log_b a} \lg^{k+1} n)$. (If $k=0$, $T(n) = \Theta(n^{\log_b a} \lg n)$).|**Costs are equal per level.** All levels contribute approximately the same cost.|
|**3**|$f(n)$ is polynomially larger than $n^{\log_b a}$. (Requires $f(n) = \Omega(n^{\log_b a + \epsilon})$ for some $\epsilon > 0$) **AND** satisfies the **regularity condition** ($af(n/b) \le cf(n)$ for some $c < 1$ and sufficiently large $n$).|$T(n) = \Theta(f(n))$.|**Root dominates.** Cost drops geometrically from root to leaves.|

#### Practical Examples Using the Master Method

1. **Merge Sort** (Recurrence: $T(n) = 2T(n/2) + \Theta(n)$)
    
    - $a=2, b=2$. Watershed function: $n^{\log_2 2} = n$.
    - $f(n) = \Theta(n)$. This matches the watershed function (Case 2, $k=0$).
    - Solution: $T(n) = \Theta(n \lg n)$.
2. **Simple Recursive Matrix Multiplication** (Recurrence: $T(n) = 8T(n/2) + \Theta(1)$)
    
    - $a=8, b=2$. Watershed function: $n^{\log_2 8} = n^3$.
    - $f(n) = \Theta(1)$. This is polynomially smaller than $n^3$ (Case 1, $\epsilon=3$).
    - Solution: $T(n) = \Theta(n^3)$.
3. **Strassen's Algorithm** (Recurrence: $T(n) = 7T(n/2) + \Theta(n^2)$)
    
    - $a=7, b=2$. Watershed function: $n^{\log_2 7} \approx n^{2.81}$.
    - $f(n) = \Theta(n^2)$. Since $2 < \log_2 7$, $f(n)$ is polynomially smaller (Case 1).
    - Solution: $T(n) = \Theta(n^{\lg 7})$.

#### When the Master Method Doesn't Apply

The master method does not cover all recurrences. It fails if:

- The driving function $f(n)$ and the watershed function $n^{\log_b a}$ cannot be asymptotically compared.
- $f(n)$ falls into gaps between the three cases (e.g., growing slower than polynomially, or faster than polylogarithmically but not polynomially).
- The regularity condition in Case 3 fails.

For example, $T(n) = 2T(n/2) + n/\lg n$ cannot be solved by the master method because $f(n)$ is asymptotically smaller than the watershed function $n$, but not polynomially smaller, thus failing Case 1. In these situations, the Substitution Method (Section 4.3) or the Akra-Bazzi method (Section 4.7) must be used.

---

The three methods function like different tools in a kit: the **master method** is the specialized power tool for common cases; the **recursion tree** is the sketchpad for generating initial blueprints; and the **substitution method** is the rigorous construction method used to finalize and verify the foundation.