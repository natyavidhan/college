### Chapter 3: Solving Problems by Searching (Russell and Norvig)

#### 3.1 Problem-Solving Agents

1. **The Nature of Search and Planning:**
    
    - When the correct action is not immediately obvious, an agent may need to **plan ahead** by considering a sequence of actions that form a path to a goal state.
    - Such an agent is known as a **problem-solving agent**, and the required computational process is called **search**.
    - Problem-solving agents utilize **atomic representations**, meaning states of the world are considered as whole, indivisible units without internal structure visible to the search algorithms.
2. **Components of a Search Problem:** A search problem consists of five key components:
    
    - **Initial state:** The starting point for the agent.
    - **Actions:** The set of actions available to the agent (sometimes called _operators_).
    - **Transition model** ($RESULT(s, a)$): This describes the state that results from performing an action $a$ in state $s$.
    - **Goal test:** A way to determine if a given state is the goal state.
    - **Path cost:** A function that assigns a numerical cost to an action sequence, typically calculated as the sum of the costs of the individual actions. Actions are generally assumed to have positive costs.
    - A **solution** is defined as an action sequence that maps the initial state to a goal state.
3. **State Space Representation:**
    
    - The overall state space can be modeled as a **graph**, where states are vertices and the directed edges connecting them represent actions.

#### 3.2 Example Problems

- Example problems are frequently used in AI because they are concisely described and easily manipulated.
- **Grid Worlds (e.g., Vacuum World):**
    - The state definition includes which objects are in which cells (like the agent and any dirt).
    - In the simple **two-cell vacuum world**, there are 8 distinct states: the agent can be in one of two cells, and each cell can either contain dirt or not ($2 \cdot 2 \cdot 2 = 8$ states).
    - The actions defined for this simple world are **Suck**, move **Left**, and move **Right**.
    - For a general vacuum environment with $n$ cells, there are $n \cdot 2^n$ possible states.
    - The goal is to have no dirt in any cell, and the standard path cost is 1 per action.

---

### Chapter 5: Constraint Satisfaction Problems (Russell and Norvig)

#### 5.1 Defining Constraint Satisfaction Problems

- **Factored Representation:** CSPs break away from the atomic state model by using a **factored representation**, where the state is defined by a set of **variables**, each having a specific **value**.
- A **Constraint Satisfaction Problem (CSP)** is solved when all constraints are satisfied by the values assigned to the variables.
- **Formal Definition:** A CSP is defined by three components:
    1. A set of **variables** $X$.
    2. A set of **domains** $D$, where $D_i$ is the set of possible values for variable $X_i$.
    3. A set of **constraints** $C$.
- **Assignments and Solutions:**
    - A **state** is an assignment of values to some or all variables.
    - An assignment is **complete** if every variable has a value.
    - A **solution** is a complete and consistent assignment.
- **Constraints:** Constraints specify the acceptable combinations of values for a subset of variables. They can be defined either by listing the allowed pairs (or tuples) or by an algebraic relationship.
    - Constraints can be classified by the number of variables involved (e.g., unary, binary, or high-order constraints).

---

### Chapter 6: Adversarial Search and Games (Russell and Norvig)

#### 6.1 Game Theory

- **Adversarial Search:** This type of search deals with **competitive environments** where two or more agents have conflicting goals.
- AI research typically focuses on **games** because they are simplified: states are easy to represent, and actions are precisely regulated.
- Games are categorized based on factors such as whether they are deterministic or stochastic, whether they are zero-sum (constant sum of payoffs, often zero), and whether they involve perfect or imperfect information.

#### 6.2 Optimal Decisions in Games

- **Zero-Sum Games with Perfect Information:** For deterministic, two-player, perfect-information, zero-sum games (like Chess or Checkers), the utility outcomes are typically defined as 1 (win for MAX), 0 (draw), or $-1$ (loss for MAX).
- **Optimal Strategy:** The goal is for the maximizing agent (MAX) to choose a move that achieves the best possible outcome, assuming the minimizing opponent (MIN) also plays optimally.
- **Minimax Algorithm:** This algorithm is used to compute the optimal move under the assumption of perfect adversarial play.
    - The **Minimax value** of a state is the maximum utility that the agent can guarantee itself starting from that state.
    - The game tree search alternates: MAX chooses the move to maximize utility, and MIN chooses the move to minimize utility.
    - The time complexity of Minimax is **$O(b^m)$**, where $b$ is the branching factor (legal moves) and $m$ is the depth.

---

### Chapter 9: Search and Control Strategies (Patterson)

#### 9.1 Introduction

- **Central Role of Search:** **Search** is a core operational task in AI programs; nearly every AI application relies on a search procedure to execute its intended function.
- Problems are formulated using **states**, and solutions are found by searching through the sequence of states until one or more **goal states** are reached.
- Search is vital for solving complex problems such as understanding natural language, where a program must search dictionaries, grammatical structures, and contexts. It is also essential for pattern recognition in vision systems and for finding clauses in theorem proving.
- The objective is to find methods that limit search and matching to avoid the "combinatorial explosion" common in search problems.

#### 9.2 Preliminary Concepts

- **Problem Space Definition:** A problem is characterized by a **space** consisting of a set of states (potentially infinite) and a set of **operators** (actions) that facilitate transitions between states.
- **States and Solutions:** The states include one or more **initial states**, **intermediate states**, and one or more **goal states**.
- A **solution** is defined as a sequence of operators that leads from an initial state to a goal state.
- Performance is evaluated based on the amount of **time and memory space** required for solution completion.
- **Graph/Tree Representation:** The problem space can be represented as a directed graph or a tree structure.
- **Search Process:** Search involves finding a path by successively expanding nodes.
    - **Node generation** is computing the representation code of child nodes from a parent.
    - **Expanding the node** is the process of generating all children of a parent.
    - A **search procedure** determines the strategy for ordering node generation and selecting a path.
- **And-Or Graphs:** Used for problems that can be decomposed into subproblems where _all_ subproblems must be solved. An **And node** represents this requirement with a curved line connecting the emanating arcs. **Or nodes** permit choosing any single emanating path.

#### 9.3 Examples of Search Problems

- The structure of search problems can be exemplified by systems like the **General Problem Solver (GPS)**, which utilizes the problem-solving technique known as **means-end analysis (MEA)**.
- GPS works by comparing an initial state/object ($L_x$) to a goal object ($L_g$), determining the difference, and systematically applying operations to reduce that difference until the goal is achieved.

#### 9.4 Uninformed or Blind Search (Excluding Depth-First Iterative Deepening Search and Bidirectional Search)

- A **blind or uninformed search** algorithm uses _only_ the initial state, the search operators, and the goal test; no domain-specific knowledge is used to guide the path selection.

1. **Depth-First Search (DFS):**
    
    - DFS explores the search space by proceeding as far down a path as possible before backing up.
    - It operates by always generating a successor node (if possible) and continuing the search from that successor. If a path terminates (no successors found), the search backs up to the nearest unexplored branch.
    - DFS is commonly implemented using a **LIFO queue (stack)**.
    - Time and space complexities are generally $O(b^m)$, where $b$ is the branching factor and $m$ is the maximum depth.
    - DFS is typically **incomplete** and **not optimal**.
2. **Breadth-First Search (BFS):**
    
    - BFS explores nodes level by level, examining all nodes at depth $d$ before moving to depth $d+1$.
    - It finds the shortest solution path based on the number of steps (transitions).
    - BFS is implemented using a **FIFO queue**.
    - BFS is **complete** and **optimal** when all action costs are equal.
    - Time and space complexities are $O(b^d)$, where $d$ is the depth of the solution. The exponential space requirement can make it intractable for deep problems.

#### 9.5 Informed Search (Excluding Branch-and-Bound and Iterative Deepening A*)

- **Informed Search** methods utilize knowledge (heuristics) to restrict the number of states visited, preventing the search space from becoming intractable.

1. **General Best-First Search:**
    
    - This strategy employs an evaluation function $f(n)$ to rate the relative promise of nodes on the _open_ list (or frontier).
    - The **open list** holds nodes generated but not yet expanded; the **closed list** holds nodes already expanded.
    - The node with the best $f(n)$ score is selected for expansion.
2. **Hill Climbing:**
    
    - A local search approach that looks only at the current node and its immediate successors.
    - It selects the successor node that yields the greatest improvement in relation to a heuristic measure of distance to the goal, $h(n)$.
    - If no successor provides an improvement, the search terminates at a **local optimum**.
    - While often finding _a_ solution, it does not guarantee finding the optimal one.
3. **A\* Algorithm (Optimal Heuristic Search):**
    
    - A* is a standard method for finding the least-cost path.
    - It uses the evaluation function $f^*(n) = g^*(n) + h^*(n)$.
        - $g^*(n)$ is the actual lowest cost from the start node $n_0$ to $n$.
        - $h^*(n)$ is the lowest cost from $n$ to the goal $n_g$.
    - A* relies on an **admissible heuristic**, $h(n)$, which must always be less than or equal to the actual cost $h^*(n)$.
    - If the heuristic is admissible, **A* guarantees finding an optimal path** to the goal.