Chapter 4, titled "Divide-and-Conquer," introduces mathematical methods necessary to solve recurrence relations, which are used to characterize the running times of recursive algorithms. A recurrence describes an overall running time $T(n)$ in terms of the running time of the same algorithm on smaller inputs.

The guidelines specify focusing on the three primary techniques for solving recurrences:

### 4.3 The Substitution Method for Solving Recurrences

The substitution method is considered the most general and robust technique for solving recurrences.

#### Core Steps:

1. **Guess the form** of the solution using symbolic constants.
2. **Use mathematical induction** to prove the guess correct and solve for the appropriate constants.

To apply the inductive hypothesis, the guessed solution is substituted back into the recurrence for smaller arguments, which is why the method is named the "substitution method".

#### Proving Bounds ($\Theta, O, \Omega$):

It is generally best practice to establish asymptotic bounds separately: first prove an $O$-bound (upper bound), and then an $\Omega$-bound (lower bound). Together, these establish a $\Theta$-bound (asymptotically tight bound).

#### Handling Difficult Inductive Steps:

Sometimes a straight guess fails to satisfy the inductive step, but a slightly modified guess can succeed. If $T(n) \le c \cdot (\text{guessed solution})$ fails, trying to **subtract a lower-order term** (e.g., guessing $T(n) \le c n \lg n - d$) can sometimes make the math work out, especially when the recurrence involves multiple recursive invocations.

#### Avoiding Pitfalls:

When using the substitution method, **avoid using asymptotic notation** (such as $O$ or $\Theta$) within the inductive hypothesis, as the hidden constants might change, leading to erroneous proofs.

### 4.4 The Recursion-Tree Method for Solving Recurrences

The recursion-tree method is a visual technique primarily used to **generate intuition for a good guess** that can then be formally verified using the substitution method. If applied meticulously, it can also serve as a direct proof.

#### Procedure:

1. **Model the recurrence as a tree**, where each node represents the cost of a single subproblem.
2. **Sum the costs horizontally** across all nodes at each level to determine the per-level cost.
3. **Sum all the per-level costs** to find the total cost of the recursion.

The method also involves determining the **height of the tree** and the **number of leaves**. For a standard divide-and-conquer recurrence where the problem size decreases by a factor of $b$ each level, the height is related to $\log_b n$.

#### Analyzing Costs:

The total cost typically depends on whether the costs per level:

- **Decrease geometrically** from the root to the leaves (root dominates total cost).
- **Are approximately equal** at every level.
- **Increase geometrically** from the root to the leaves (leaves dominate total cost).

The method can handle complex cases, such as **unbalanced recursion trees** where different root-to-leaf paths have different lengths (e.g., $T(n) = T(n/3) + T(2n/3) + \Theta(n)$).

### 4.5 The Master Method for Solving Recurrences

The master method provides a "cookbook" solution for a specific type of algorithmic recurrence, making it the easiest method when applicable.

#### The Master Recurrence Form:

The method solves recurrences of the form: $$T(n) = aT(n/b) + f(n)$$

Where:

- $a \ge 1$: The number of subproblems created recursively.
- $b > 1$: The factor by which the input size is reduced in each subproblem.
- $f(n)$: The "driving function," representing the cost of dividing the problem and combining the subproblem results.

This form typically arises from divide-and-conquer algorithms. Importantly, floors and ceilings in the arguments (e.g., $T(\lfloor n/b \rfloor)$) can be ignored, as they do not affect the asymptotic bounds.

#### The Master Theorem (Theorem 4.1):

The solution depends on comparing the driving function $f(n)$ with the **watershed function** $\Theta(n^{\log_b a})$:

|Case|Condition|Solution|Interpretation (Recursion Tree)|
|:--|:--|:--|:--|
|**Case 1**|$f(n) = O(n^{\log_b a - \epsilon})$ for some constant $\epsilon > 0$.|$T(n) = \Theta(n^{\log_b a})$|The watershed function dominates $f(n)$ polynomially. The cost is dominated by the **leaves**.|
|**Case 2**|$f(n) = \Theta(n^{\log_b a} \lg^k n)$ for some constant $k \ge 0$. (Most commonly $k=0$, so $f(n) = \Theta(n^{\log_b a})$)|$T(n) = \Theta(n^{\log_b a} \lg^{k+1} n)$|$f(n)$ and the watershed function grow at nearly the same rate. The cost is **equal** across all $\Theta(\lg n)$ levels.|
|**Case 3**|$f(n) = \Omega(n^{\log_b a + \epsilon})$ for some constant $\epsilon > 0$. **AND** the regularity condition holds: $af(n/b) \le cf(n)$ for some constant $c < 1$ and sufficiently large $n$.|$T(n) = \Theta(f(n))$|$f(n)$ dominates the watershed function polynomially. The cost is dominated by the **root** (divide and combine steps).|

#### Limitations (The Gaps):

The master theorem requires a polynomial separation between $f(n)$ and the watershed function in cases 1 and 3. If $f(n)$ falls into one of the gaps—for instance, growing only logarithmically slower than $n^{\log_b a}$ (not polynomially slower, thus failing Case 1) or if the regularity condition in Case 3 fails—the master method cannot be used, and alternative methods (like substitution or the Akra-Bazzi method) must be applied.

---

_Analogy:_ Think of solving recurrences like finding a hidden treasure. The **Substitution Method** is like an archaeologist who guesses the location based on historical clues, then meticulously digs (induction) to prove the spot correct. The **Recursion-Tree Method** is like mapping the site, visually seeing how the land (the cost) is distributed, which helps the archaeologist make a good guess. The **Master Method** is a modern, specialized tool—a metal detector—that works only on certain standardized sites, providing the answer instantly if the spot fits one of its predefined search modes.