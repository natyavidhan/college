Based on the required syllabus topics—Chapter 3 (3.1, 3.2), Chapter 5 (5.1), Chapter 6 (6.1, 6.2), and Chapter 9 (excluding specific variants of search and pruning)—here are the relevant questions extracted from the provided question papers:

### Chapter 3: Problem Formulation, State Space Search, and Agents (3.1, 3.2)

These sections cover Agent definitions, environments, problem solving steps, and state space problems (like the Water Jug Problem).

|Question Paper|Question Number|Relevant Question Text|Source(s)|
|:-:|:-:|:--|:--|
|1108|8(c)|Define the **PEAS for vacuum cleaner agent**.||
|2211|1(d)(ii)|Describe the following terms: **Software Agent**.||
|2211|1(h)|Define the **PEAS for taxi Driver Agent**.||
|2926|1(g)|**Differentiate between Model based agent and Utility based agent**.||
|2926|4(c)|Differentiate between a **static and dynamic environment of an agent**.||
|4506|2(a)|Describe the **water-jug problem**. Also give a suitable **state space representation** for this problem?||
|4506|4(c)|Give **PEAS description for Taxi Driver Agent**?||
|6515|1(a)(i)|Describe the following: **Agent Function**.||
|6515|1(k)|Differentiate between a **fully observable and partially observable environment**.||
|6515|7(c)|You are given two jugs of capacity 4-gallon and 3-gallon respectively... How can you get exactly 2 gallons of water into the 4-gallon jug? Write down solution by showing all intermediate states.||
|6632|5(a)|Describe and give the **state space representation for the water-jug problem**.||
|798|1(c)|List out various steps for solving a problem using search **state space strategy**.||
|798|1(g)(i)|Define the following terms: **State Space Search**.||
|798|2(a)|Compare and contrast "**Fully observable environment**" and "**Partially observable environment**".||

---

### Chapter 5: Uninformed Search (5.1)

This section primarily covers basic search strategies like Breadth-First Search (BFS) and Depth-First Search (DFS).

|Question Paper|Question Number|Relevant Question Text|Source(s)|
|:-:|:-:|:--|:--|
|4506|1(f)|**Compare and contrast Depth first search and Breadth first search**?||
|6515|1(d)|**Differentiate between breadth first search and best first search**.||
|6632|1(b)|**Compare and contrast Depth first search and Breadth first search**?||
|6632|9(i)|Write short note on the following: **Uninformed Search**.||

---

### Chapter 6: Informed (Heuristic) Search (6.1, 6.2)

This section covers Best-First Search, A* Algorithm, and the definition/properties of Heuristic Functions.

|Question Paper|Question Number|Relevant Question Text|Source(s)|
|:-:|:-:|:--|:--|
|1108|1(a)(i)|Describe the following terms: **Heuristic Function**.||
|1108|1(l)|Why should the **heuristic function of A* algorithm always underestimate**? Give reason, example.||
|1108|6|**Compare and contrast Best-first search and Hill Climbing search**. You can use example.||
|2211|1(i)|Define **Heuristic Search Technique**. What is the role of a **heuristic function**?||
|2211|6(c)|Explain, why should the **heuristic function of A* underestimate**?||
|2926|4(a)|Give the **similarities and differences between Best First Search and A* algorithm**. Under what conditions A* algorithm provide an optimal solution?||
|4506|5(a)|When do we say that the search is admissible? You can take the example of **A***.||
|6515|1(c)|Let h' denote the estimate of h (the actual cost of getting from the current node to a final state node). Explain in what way the efficiency of **A* algorithm** and reaching of a goal state is affected if h' always **overestimates h**.||
|6632|9(ii)|Write short note on the following: **Heuristic search**.||
|798|1(a)|Write a short note on **heuristic search**.||

---

### Chapter 9: Adversarial Search (Game Playing) and Local Search (9.1, 9.2, 9.3, 9.4, 9.5)

This section includes Minimax, Alpha-Beta Pruning, and Hill-Climbing, while excluding Depth-First Iterative Deepening Search, Bidirectional Search, Branch-and-Bound, and Iterative Deepening A*.

| Question Paper | Question Number | Relevant Question Text                                                                                                                                                                                               | Source(s) |
| :------------: | :-------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------- |
|      1108      |      2(c)       | In the following two-ply game tree, the terminal nodes show the utility values computed by the utility function. Use the **Minimax algorithm** to compute the utility values for other nodes in the given game tree. |           |
|      1108      |      5(b)       | What are **alpha and beta cutoffs**? How **alpha-beta pruning** is used to improve the efficiency of **Minimax procedure**?                                                                                          |           |
|      1108      |      8(b)       | Describe the **limitations of Hill Climbing Methods**.                                                                                                                                                               |           |
|      2211      |      1(g)       | Describe the **limitations of Hill climbing search**.                                                                                                                                                                |           |
|      2211      |      4(c)       | Consider the following game tree with ply depth 2... in which the indicated scores are from the MAX player's point of view. What move should MAX choose, and why? (**Minimax**)                                      |           |
|      2211      |      6(b)       | What do you understand by **alpha-beta cutoffs**. Describe the method of **alpha-beta pruning** using these cutoffs with the help of an example.                                                                     |           |
|      2926      |      7(a)       | Consider the following game tree... What move should be chosen and why? Which nodes will be pruned according to the **alpha-beta pruning procedure**? Give justification of each.                                    |           |
|      4506      |      1(j)       | In the following two-ply game tree, the terminal nodes show the utility function. Use the **Minimax algorithm** to compute the utility values for other nodes in the given game tree.                                |           |
|      4506      |      1(k)       | Write about the **limitations of Hill Climbing search**?                                                                                                                                                             |           |
|      6515      |      1(h)       | Consider the following game tree with ply depth 2... indicated scores are from the **MIN player's point of view**. What move should MIN choose, and why? (**Minimax**)                                               |           |
|      6515      |      4(b)       | Discuss, based on the alpha value of a MAX player and beta value of a MIN player, when the search is discontinued in the **MINIMAX procedure using alpha-beta pruning**. Explain using an example.                   |           |
|      6632      |      1(d)       | Describe the various problems associated with **Hill climbing methods** and explain them.                                                                                                                            |           |
|      798       |      4(a)       | What are the **limitations of Hill Climbing search technique**? Explain.                                                                                                                                             |           |
|      798       |      4(b)       | Explain the utility of **alpha and beta cuts in Minimax problem**.                                                                                                                                                   |           |
|      798       |      4(c)       | In the following two-ply game tree, the terminal nodes show the utility values computed by the utility function. Use the **Minimax algorithm** to compute the utility values for other nodes in the given game tree. |           |