### Chapter 3: Solving Problems by Searching (Russell and Norvig)

#### 3.1 Problem-Solving Agents

A **problem-solving agent** utilizes a process called **search** to plan ahead when the correct action is not immediately obvious, considering a sequence of actions that form a path to a goal state.

**Atomic Representation** Problem-solving agents use **atomic representations**, where states of the world are treated as indivisible wholes, having no internal structure visible to the problem-solving algorithms.

**Components of a Search Problem** A search problem is formally defined by five components:

1. **States:** A set of possible states the environment can be in, referred to as the **state space**.
2. **Initial state:** The state the agent begins in.
3. **Actions:** A set of actions possible in any state, combined with a **transition model** that describes the state resulting from taking a specific action in a specific state.
4. **Goal test:** A way to determine if a state is the goal state.
5. **Path cost:** A function that assigns a numeric cost to a path. For this type of problem, all action costs are assumed to be positive.

A **solution** is a sequence of actions from the initial state to a goal state, and a "good" solution is one with the lowest **path cost**. The state space can be represented as a **graph**, where vertices are states and directed edges are actions.

#### 3.2 Example Problems

Problems tackled by problem-solving agents are often categorized as **standardized problems** or **real-world problems**.

**Standardized Problems** Standardized problems are benchmarks with concise, exact descriptions used to test and compare problem-solving algorithms:

- **Grid world problem:** A two-dimensional array where agents move between cells. The **vacuum world** from Section 2.1 is an example. A simple two-cell vacuum world has 8 states. A vacuum environment with $n$ cells has $n \cdot 2^n$ states.
- **Infinite state spaces:** Problems involving the generation of mathematical expressions, circuits, proofs, or programs, where the state space is infinite.

**Real-World Problems** Real-world problems include applications whose solutions are actively used:

- **Route-finding problems:** Defined by specified locations and transitions along edges, used in applications like Web directions and military planning. Complications include varying costs due to traffic and rerouting.
- **Robot navigation:** A generalization of route-finding where a robot creates its own paths in a potentially continuous, multi-dimensional search space (one dimension for each joint angle).
- **Automatic assembly sequencing:** Determining the optimal order to assemble parts of an object. A key example is **protein design**.

---

### Chapter 5: Constraint Satisfaction Problems (Russell and Norvig)

#### 5.1 Defining Constraint Satisfaction Problems

A **Constraint Satisfaction Problem (CSP)** is defined by a set of variables, a domain for each variable, and a set of constraints.

A state in a CSP is determined by assigning values to some or all variables. An assignment that adheres to all constraints is called a **consistent** or **legal** assignment. A **solution** to a CSP is a complete and consistent assignment.

---

### Chapter 6: Adversarial Search and Games (Russell and Norvig)

#### 6.1 Game Theory

Game theory is essential for studying **multiagent systems** and decisions in **multiagent environments** where the actions of one agent significantly impact the utility of others.

For certain games, a rational agent should adopt policies that are or appear to be **randomized**. The study of rational decisions resulting from sequential actions was historically pursued in operations research, leading to fields like reinforcement learning.

#### 6.2 Optimal Decisions in Games

Optimal decision-making in adversarial search problems, such as games, is crucial. The simplest games studied are those that are deterministic, turn-taking, two-player, zero-sum, and fully observable.

---

### Chapter 9: Search and Control Strategies (Patterson)

#### 9.1 Introduction

**Search** is fundamental in almost all AI programs. Problem solutions are sought by moving through various **states** in a problem space until a **goal state** is found. Search is widespread in AI for tasks such as identifying model patterns in vision perception, solving planning problems, and identifying matching words in natural language understanding.

#### 9.2 Preliminary Concepts

A problem space consists of **states** and **operators** (transformations) that map states to other states. States include initial states, intermediate states, and **goal states**.

- A **solution** is the sequence of operators mapping the initial state to the goal state.
- The performance of a solution is judged by **time and space complexities**, often expressed using O notation (e.g., linear O(n), exponential O($b^k$)).
- The search space is graphically represented as a directed **graph** or a **tree**. Nodes represent states, and arcs represent transformations.
- Nodes below a parent are **children** (or successors); nodes above are **ancestors**.
- The number of successors is the **branching degree** ($b$).
- Search involves generating successive **child nodes** or **successors** from a parent node, a process known as **expanding the node**.

Search strategies are categorized based on information availability:

- **Blind (uninformed) search:** Gives no preference to the order of successor selection.
- **Informed (directed) search:** Uses information about the problem space to compute preference among successors.

#### 9.3 Examples of Search Problems

Key examples illustrating search concepts include:

- **The Eight Puzzle:** A classic problem involving moving numbered tiles in a 3x3 frame to reach a goal configuration.
- **General Problem Solver (GPS):** A system that separates task knowledge from problem-solving logic. GPS used a technique called **means-end analysis**, which repeatedly determined the difference between the current object (state) and the goal object, then applied appropriate rewrite rules (operators) to reduce that difference.
- **Traveling Salesman Problem:** Finding an optimal tour through a set of cities.

#### 9.4 Uninformed or Blind Search

Uninformed search algorithms use no information beyond the initial state, the operators, and the goal test.

- **Breadth-First Search:**
    
    - **Strategy:** Explores all nodes at a given depth level before moving deeper.
    - **Implementation:** Uses a FIFO queue.
    - **Completeness and Optimality:** Always finds a solution with a **minimal path length** if one exists.
    - **Complexity:** Time complexity is O($b^d$) and space complexity is O($b^d$). This exponential complexity (both time and space) is a primary drawback.
- **Depth-First Search:**
    
    - **Strategy:** Always expands the **deepest node** in the frontier first.
    - **Implementation:** Places newly generated children at the **head of the queue** (LIFO stack behavior).
    - **Process:** Proceeds down a single path until a goal or terminal node is met, then backtracks.
    - **Disadvantage (Memory/Completeness):** It is not systematic in infinite spaces and can get stuck going down an infinite path, making it **incomplete**.

#### 9.5 Informed Search

Informed search methods use knowledge, often in the form of **heuristics**, to constrain the search space and find solutions more efficiently.

- **Hill Climbing Methods:**
    
    - **Strategy:** At each point in the search path, the successor node that appears to lead most quickly to the goal ("the top of the hill") is selected for exploration.
    - **Drawbacks:** It discards previously expanded nodes and can get trapped in local optima, known as a **foothill**, a **ridge**, or a **plateau** (an area where all neighboring nodes have the same value).
- **Best-First Search:**
    
    - **Strategy:** Retains and evaluates all estimates computed for all previously generated nodes, selecting the best among them.
    - **Advantage:** Avoids the local traps encountered in hill climbing.
- **Optimal Search and A*:**
    
    - The **A* algorithm** is a specialization of best-first search that estimates the total cost from the start to the goal through a given successor node.
    - Nodes are categorized into an **open list** (generated but not expanded) and a **closed list** (expanded).
    - **Admissibility condition:** An algorithm that is guaranteed to return an optimal solution when one exists.
    - **Completeness condition:** An algorithm that always terminates with a solution when one exists.
    - **Dominance property:** An admissible algorithm $A_1$ is said to **dominate** another admissible algorithm $A_2$ if $A_1$ is "more informed" (i.e., its heuristic function consistently estimates the cost higher than $A_2$'s).