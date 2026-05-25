# Unit 1: Searching, Sorting, Selection

## Topic: Sorting Algorithms & Analysis

1. Arrange the following sorting techniques in the increasing order of the number of comparisons that they would do in order to sort the data : {7, 3, 9, 12, 11}. Justify your answer. Insertion sort, Merge sort, Improved Bubble Sort **Source:**

- 4057 / 2024 / Semester IV / Q1(a)

2. Which of the following algorithms are stable: Insertion sort, Quicksort? Justify with the help of an example. **Source:**

- 1143 / 2022 / Semester IV / Q1(c)

3. For each of the following sorting algorithms, merge sort and insertion sort, discuss whether or not it is (i) stable (ii) in-place **Source:**

- 4523 / 2023 / Semester IV / Q2(b)

4. “Counting sort is a comparison sort algorithm.” Yes or No. Justify your answer using the input A = < 4, 3, 2, 4, 1, 5, 2, 4, 3 > **Source:**

- 1143 / 2022 / Semester IV / Q1(g)

5. Can Insertion Sort be used as an intermediate sort for Radix sort? Explain why or why not. **Source:**

- 2208 / 2019 / Semester IV / Q1(c)

6. Comment on the correctness of the following implementation of radix sort : `for i = 1 to d` `use heap sort to sort array A on digit i` **(d is the number of digits in each element)** **Source:**

- 2944 / 2024 / Semester IV / Q1(c)

7. An implementation of radix sort uses heap sort instead of count sort as the intermediate sorting technique. Is radix sort still stable? Justify your answer with an example. **Source:**

- 4057 / 2024 / Semester IV / Q4(b)[ii]

8. Consider an algorithm A with run time O(n). What is the condition on A for it to be usable as the inter-mediate sort in Radix sort ? Explain. **Source:**

- 6512 / 2018 / Semester IV / Q1(f)

9. Give an algorithm to sort n integers in the range 0 to $n^3 - 1$ in O(n) time. Justify it's time complexity. **Source:**

- 1143 / 2022 / Semester IV / Q4(a)

10. Suppose an input to the bucket sort algorithm is not uniformly distributed. What will be the effect of this condition on the running time of the algorithm? Justify. **Source:**

- 1143 / 2022 / Semester IV / Q4(c)

11. Suppose an input to the bucket sort algorithm is not uniformly distributed. Then: (i) will the sort still give correct output? (ii) what will be the impact of relaxing this condition on the running time ? Justify. **Source:**

- 2796 / 2017 / Semester IV / Q1(f)

12. Why is the worst-case running time for bucket sort O(n²)? What changes would you make to the algorithm so that its worst-case running time becomes O(n lg n)? **Source:**

- 4523 / 2023 / Semester IV / Q1(g)

13. Why is Bucket sort considered a non-comparison based sorting algorithm (where no comparison of keys is performed for sorting the list) despite the fact that insertion sort, which is used to sort individual buckets, is comparison based ? **Source:**

- 6512 / 2018 / Semester IV / Q6(b)

14. Professor William claims that the $\Omega(n \lg n)$ lower bound for sorting n numbers does not apply to his machine. The control flow of a program on his machine can split three ways after a single comparison of two elements of the array $a_i : a_j$. The three ways are $a_i < a_j$, $a_i = a_j$, or $a_i > a_j$. Show that the professor is wrong by proving that the number of three-way comparisons required to sort n elements is $\Omega(n \lg n)$. **Source:**

- 1143 / 2022 / Semester IV / Q2(a)

15. Prove that any comparison based sorting algorithm requires $\Omega(n \log n)$ comparisons in the worst case. **Source:**

- 2944 / 2024 / Semester IV / Q1(f)

16. (i) What is the smallest possible depth of a leaf in a decision tree for a comparison sort? Name a sorting technique to which this smallest depth would correspond. (ii) What is the minimum number of leaves in the decision tree for a comparison sort? Use this observation to derive a lower bound on the number of comparisons performed by a comparison sort in the worst case. **Source:**

- 4523 / 2023 / Semester IV / Q6(a)

17. Can an input that leads to the best-case behaviour for one sorting algorithm lead to the worst-case behaviour for another algorithm? Explain with a suitable example. **Source:**

- 2944 / 2024 / Semester IV / Q1(a)

18. What will be the time complexity of the following sorting algorithms on an almost-sorted input? (i) Heap Sort (ii) Insertion Sort **Source:**

- 2944 / 2024 / Semester IV / Q3(a)

19. Write an algorithm to sort 4 keys in 5 comparisons in the worst case. **Source:**

- 2944 / 2024 / Semester IV / Q1(j)

20. A student was asked to sort a list of n numbers in decreasing order. The student writes an algorithm which works iteratively as follows. In every iteration, the following two steps are done : (i) Linear search is used to find the maximum element in the portion of the array which is not yet sorted. (ii) The maximum element found in step 1 is placed at the beginning of the not-yet-sorted portion of the array. This algorithm is given as input a list already sorted in decreasing order. What would be the time complexity of the algorithm on this input? Explain. **Source:**

- 4523 / 2023 / Semester IV / Q5(b)

21. Observe that selection sort and heap sort function in a similar fashion - in any iteration both the sorting techniques find the maximum amongst the elements yet to be processed and place it appropriately. However, they have different running times. Give the asymptotic time complexity of both and comment on what makes their running times different. **Source:**

- 6512 / 2018 / Semester IV / Q5(b)

22. What kind of inputs will lead to (i) best case (ii) worst case performance for insertion sort algorithm ? Give the running time for both the cases. **Source:**

- 6512 / 2018 / Semester IV / Q6(c)

23. Consider a department of the university with 60 teachers and 20 courses. The 8 administration department maintains the records such that each record contains the name of a teacher and the course he/she is teaching. A teacher name can be maximum 32 characters long and courses are coded as BCS101, MCS101, MCA101, etc. Each teacher may be teaching more than one course and one course may be taught by more than one teacher. Give a linear time algorithm to sort the teachers course wise, in alphabetical order. Courses should also be reported in chronological order. **Source:**

- 4057 / 2024 / Semester IV / Q7(b)

24. Suppose there are n bottles and each bottle i has some capacity $c_i$. Write the most efficient algorithm to arrange the bottles in the order of their capacities. Also, explain the running time of your algorithm. Next, consider that every bottle has an expiry date before which its content should be consumed. Each bottle is assigned a priority such that a higher value indicates a higher priority. The bottle having a closer expiry date has a higher priority assigned to it. Give an efficient algorithm to arrange the bottles in non-increasing order of their priorities. Does your algorithm involve any comparisons? If yes, count them. Explain the running time of your algorithm. **Source:**

- 32341401 / 2021 / Semester IV / Q3

25. A chemical laboratory has n chemicals stored in it. There is a risk that some chemicals may react with some others. For safety purpose, the lab assistant decides that for each pair of reactive chemicals, one is kept in a yellow-coloured bottle and the other is kept in a green-coloured bottle. Give an efficient algorithm that he can use to find out whether such a colouring is possible or not. If yes, the algorithm should determine the bottle colour for each of the n chemicals. If not, the algorithm should report it. Give an instance having at least 6 chemicals in which there are a minimum of 7 reactive pairs for which such a colouring is possible. **Source:**

- 32341401 / 2021 / Semester IV / Q6 (Note: Maps to Bipartite Graph Checking / Sorting logic)

### Frequency Analysis

- **Most repeated questions:** Lower bounds on comparison-based sorting ($\Omega(n \log n)$); bucket sort's behavior with non-uniform distributions; stability and in-place nature of algorithms like Radix, Quick, and Insertion sort.
- **Frequently asked concepts:** Replacing Count Sort with Heap/Insertion sort inside Radix Sort; Time complexities of various algorithms (Heap vs. Insertion vs. Selection) on best-case/worst-case/almost-sorted inputs.
- **Trend analysis across years:** Consistently tests the conceptual understanding of linear-time sorting algorithms (Radix, Bucket, Counting) and their properties, shifting slightly towards application-based problems (e.g., sorting bottles, sorting teachers) in newer iterations.

## Topic: Priority Queues, Heaps & Selection

1. What are the minimum and maximum number of elements in a binary heap of height h? **Source:**

- 1143 / 2022 / Semester IV / Q1(b)

2. Give an efficient algorithm to find the minimum element in a max-heap. Give the exact running time of the algorithm. **Source:**

- 2796 / 2017 / Semester IV / Q1(i)

3. Give an efficient algorithm to find the maximum element in a min-heap. Give the exact running time of the algorithm. **Source:**

- 6512 / 2018 / Semester IV / Q1(j)

4. Show that in any subtree of a max-heap, root of the subtree contains the largest value occurring anywhere in that subtree. **Source:**

- 4523 / 2023 / Semester IV / Q1(j)

5. Show that for an n-element max heap (having distinct elements) represented through an array, the leaves are the nodes indexed by floor (n/2 + 1), floor (n/2 + 2),........., n. What would be the location of the minimum element in the above heap? **Source:**

- 4523 / 2023 / Semester IV / Q4(a)

6. A d-ary heap is like a binary heap, except that nodes may have d children instead of two children. Consider a 3-ary heap represented using an array, how would the indices of the three children of a node be computed? **Source:**

- 2208 / 2019 / Semester IV / Q7(a)

7. A priority queue can be implemented in two different ways using min-heap and using singly linked list in which elements are stored in sorted order (Smaller values indicates higher priority). Compare the time complexity of following operations when performed on two different implementations of priority queue. (1) Finding the highest priority element (2) Deleting the highest priority element (3) Increase the priority of a certain element **Source:**

- 1143 / 2022 / Semester IV / Q1(h)

8. A priority queue is implemented in two different ways using a max heap and an array sorted in decreasing order of key values (higher key value indicates higher priority). Compare the time complexity of the following operations when performed on the two different implementations of the priority queue. (i) Finding the maximum element (ii) Deleting the maximum element (iii) Increase the priority of a certain element **Source:**

- 2796 / 2017 / Semester IV / Q3(a)

9. What is an in-place sorting algorithm? Is heap sort an in-place sorting algo-rithm? Sort the following data using heap sort. 4, 3, 7, 1, 8, 5, 9 **Source:**

- 4057 / 2024 / Semester IV / Q3(a)

10. Consider the Heapsort Algorithm. Fill in the missing details correctly. `Assume A[1....length] be the array to be sorted` `MaxHeapify(A,i)` `l=2*i` `r=2*i+1` `if l<= A.heapsize and A[l]>A[r]` `largest = l` `else largest = i` `if r<=A.heapsize and A[r] >A[largest]` `largest = r` `if largest != i` `exchange A[i] and A[largest]` `Maxheapify(A, ____ )` `BuildMaxHeap(A)` `A.heapsize = A.length` `for i = _________________` `MaxHeapify (A,i)` `Heapsort(A)` `BuildMaxHeap (A)` `for i = A.length downto 2` `exchange A[ __ ] with A[i]` `A.heapsize = A.heapsize -1` `MaxHeapify ( A, __ )` **Source:**

- 2208 / 2019 / Semester IV / Q4(a)

11. Illustrate the operation of BUILD -MAX -HEAP on the array A <4, 3, 17, 10, 28, 19, 6, 12, 7>. Write down the total number of comparisons done by BUILD -MAX -HEAP. **Source:**

- 1143 / 2022 / Semester IV / Q3(a)

12. Suppose we use randomized select to select the minimum element of the array A = <4, 2, 1, 7, 8, 12, 3, 0, 9, 5, 10>. Describe a sequence of partitions that result in a worst case performance of randomized select. **Source:**

- 1143 / 2022 / Semester IV / Q4(b)

13. We use Randomized-Select to select the minimum element of the array A = <3, 2, 9, 0, 7>. Describe a sequence of partitions that would result in the worst case performance of the algorithm. **Source:**

- 2796 / 2017 / Semester IV / Q5(c)

14. In randomized-select algorithm randomized partition subroutine is used. If we replace the randomized partition by a partition subroutine which chooses the last element of the list as pivot and call the modified algorithm as the select algorithm. What affect does it have on the running time of the select algorithm? **Source:**

- 2208 / 2019 / Semester IV / Q6(a)

1. Using the Median of Medians method, find the 5th smallest element in the following array : **Source:**

- 2944 / 2024 / Semester IV / Q2(b)

16. Consider the following algorithm that takes as input an array of n integers and an integer T. It finds whether there exist two elements in the array that sum up to T and returns 1 on success and 0 on failure. `TargetSum (A, n, T)` `Heapsort(A, 1, n)` `for i = 1 to n` `flag = BinarySearch(A, i+1, n, |T-A[i]|)` `if (flag)` `return 1` `endif` `endfor` `return 0` Analyze the worst case running time of TargetSum. **Source:**

- 2796 / 2017 / Semester IV / Q7(c)
- 6512 / 2018 / Semester IV / Q3(a) (Similar TargetSum via Quicksort and BinarySearch asking to analyze worst case running time)

17. Suppose there exists an O(n) time algorithm to find the 5th smallest element in an array of size n. Sort the following data using quick sort assuming 5th smallest element as the pivot. 7, 3, 5, 1, 2, 4, 6 Also, determine the time complexity of the algorithm. **Source:**

- 4057 / 2024 / Semester IV / Q3(b)

### Frequency Analysis

- **Most repeated questions:** Finding the min/max element in a max/min heap and calculating exact running time; worst-case partition sequence for Randomized Select.
- **Frequently asked concepts:** Implementations of Priority Queues (Heap vs Sorted Array/Linked List) and comparison of their base operations (Insert, Extract, Increase Key).
- **Trend analysis across years:** Earlier years (2017, 2018) focused on identifying max/min elements in heaps and Priority Queue comparisons. Recent years (2022, 2024) included Median-of-Medians simulation and detailed tracking of Heapsort algorithms.

## Topic: Red-Black Trees & Binary Search Trees

_(Note: Red-black trees appear consistently in the exams as part of advanced data structures/sorting)._

1. Compare the worst case running times of the following operations with respect to red-black trees and binary search trees. (i) Searching a given key (ii) Inserting a given key **Source:**

- 2208 / 2019 / Semester IV / Q1(d)

2. For each of the following operations does a Red Black Tree work faster than a Binary Search Tree ? Elaborate your answer. (i) Search (ii) Postorder traversal **Source:**

- 2796 / 2017 / Semester IV / Q2(b)

3. For each of the following operations does a Red Black Tree work faster than a Binary Search Tree ? Elaborate your answer. (i) Insertion (ii) Preorder traversal. **Source:**

- 6512 / 2018 / Semester IV / Q2(b)

4. Can a red-black tree have: (i) a black node without any sibling ? Justify. (ii) a red node without any sibling ? Justify. **Source:**

- 6512 / 2018 / Semester IV / Q1(e)

5. Which red-black tree properties may be violated when a node is deleted ? **Source:**

- 2796 / 2017 / Semester IV / Q6(a)

6. For the elements 6, 2, 8, 3, 10; give a valid Red Black tree. **Source:**

- 2208 / 2019 / Semester IV / Q6(c)

7. Create a Red-black tree with successive insertions for the following sequence of numbers: 10,8,14,12,13. **Source:**

- 6512 / 2018 / Semester IV / Q5(c)

8. Consider a set of jobs to be scheduled on a processor... The scheduler has a fixed maximum execution time... Construct the red-black tree corresponding to the given input and then schedule the jobs showing the red-black tree after every step. Assume the maximum execution time is 20 nanoseconds. **Source:**

- 32341401 / 2021 / Semester IV / Q4

### Frequency Analysis

- **Most repeated questions:** Comparison of Big-O time complexity between Red-Black Trees and naive Binary Search Trees for searching, insertion, and traversals.
- **Frequently asked concepts:** RB-Tree properties; step-by-step insertions to create an RB-Tree.
- **Trend analysis across years:** Standard RB-tree mechanics are a staple. The 2021 paper tied the RB-Tree directly to a practical Processor Scheduling problem.

---

# Unit 2: Graphs

## Topic: Graph Representations & Traversals (BFS/DFS)

1. Give space requirements of adjacency matrix and adjacency list representation having m edges and n vertices. **Source:**

- 1143 / 2022 / Semester IV / Q5(c)
- 2796 / 2017 / Semester IV / Q1(h)

2. In a certain application it is required to find the nodes adjacent to a given node in a sparse graph. Which of the two representations, namely adjacency list and adjacency matrix, is more suitable? Justify. **Source:**

- 2208 / 2019 / Semester IV / Q1(h)

3. Consider an adjacency list representation of a directed graph wherein an array of the outgoing edges (and not the incoming edges) for each vertex is maintained. Give an algorithm to compute the indegree for each vertex and discuss the time complexity of the algorithm. **Source:**

- 6512 / 2018 / Semester IV / Q2(a)

4. Let G be a graph with n vertices and m edges. What is the upper bound on the running time of Depth First Search on G, where G is represented as an adjacency matrix? **Source:**

- 1143 / 2022 / Semester IV / Q6(c)

5. Would you use BFS to find the shortest path between two nodes in a weighted graph with arbitrary edge weights? Justify your answer with the help of a graph having at least 5 Vertices and at least 7 edges. **Source:**

- 1143 / 2022 / Semester IV / Q1(f)
- 2796 / 2017 / Semester IV / Q1(j) (Similar phrasing without graph size constraints)

6. Can Depth First Search algorithm be used to determine a shortest path from a source node to a destination node in an unweighted graph? Justify. **Source:**

- 2208 / 2019 / Semester IV / Q1(i)

7. Would you use DFS to find the shortest-path distance between two nodes in a graph ? Justify your answer. **Source:**

- 6512 / 2018 / Semester IV / Q1(k)

8. Let G = (V,E) be a directed unweighted graph. Given two vertices s and t in V, what is the time required to determine if there exists at least one s-t path in G? Can we use the DFS algorithm to find the shortest-path distance from the s to t? If yes, justify, otherwise give a counter example. **Source:**

- 4523 / 2023 / Semester IV / Q3(a)
- 6512 / 2018 / Semester IV / Q1(i) (Similar: Name algorithm to find s-t path and its running time).

9. Let G be a tree-graph. Further, let $T_B$ and $T_D$ be the trees produced by performing BFS and DFS respectively on G. Can $T_B$ and $T_D$ be different trees? Why or why not? **Source:**

- 4523 / 2023 / Semester IV / Q1(f)

10. The BFS algorithm has been used to produce the shortest paths from a node s to all other nodes in a graph G. Can the Dijkstra's algorithm be used in place of BFS? In a different scenario, the Dijkstra's algorithm has been used to produce the shortest paths from a node s to all other nodes in a graph G'. Can BFS be used in place of the Dijkstra's algorithm? Explain your answers for both the scenarios. **Source:**

- 4523 / 2023 / Semester IV / Q7(a)

11. Consider a directed graph G with one component. Can a vertex u of G end up in a depth-first tree containing only u, even though u has both incoming and out-going edges in G? Justify your answer with an example. **Source:**

- 4057 / 2024 / Semester IV / Q1(d)

## Topic: Cyclic Graphs, Bipartite Graphs & Topological Sorting

1. Give an efficient algorithm to check if a given undirected graph has a cycle. Discuss the time complexity of your algorithm. **Source:**

- 2796 / 2017 / Semester IV / Q2(a)
- 2944 / 2024 / Semester IV / Q1(h)
- 4057 / 2024 / Semester IV / Q5(b)

2. Design a O(|V|+|E|) time algorithm to find whether a given undirected graph is bipartite (where V is the set of vertices, E is the set of edges of the graph). **Source:**

- 1143 / 2022 / Semester IV / Q5(b)

3. Consider the following graphs: G1 and G2 [Graphs shown in paper]. For each of the graphs, specify whether the graph is bipartite or not. If it is bipartite then give the two partitions else justify. **Source:**

- 2208 / 2019 / Semester IV / Q3(a)

4. Consider the following graph: [Graph shown in paper]. Specify whether the above graph is bipartite or not. If yes, give the partition, else justify. **Source:**

- 4523 / 2023 / Semester IV / Q1(h)

5. Let G=(V,E) be a graph where V is the set of vertices and E is the set of edges. BFS is performed starting at node s, which produces layers $L_1, L_2, ...L_m$. There is an edge e = (u, v) in E such that $u \in L_i$ and $v \in L_i$ for some i. Show that G is not a bipartite graph. **Source:**

- 2944 / 2024 / Semester IV / Q6(a)

6. For what values of n are cycle graphs $C_n$ bipartite? Justify. **Source:**

- 2944 / 2024 / Semester IV / Q6(b)

7. Find possible Topological sorts of the given directed acyclic graph. Give any four : [Graph with nodes a,b,c,d,f] **Source:**

- 1143 / 2022 / Semester IV / Q1(i)

8. For the given directed acyclic graph, determine the topological ordering. [Graph Image] **Source:**

- 4057 / 2024 / Semester IV / Q5(a)

9. How many topological orderings does the following graph have? Specify all of them. [Graph Image] **Source:**

- 4523 / 2023 / Semester IV / Q5(a)

10. Give an example graph having four nodes that does not have a topological ordering. **Source:**

- 2796 / 2017 / Semester IV / Q5(a)

11. Give an example graph having five nodes that has two different topological orderings. Also, show the topological orderings. **Source:**

- 6512 / 2018 / Semester IV / Q5(a)

12. Show that any directed graph having a topological ordering must be acyclic. **Source:**

- 2208 / 2019 / Semester IV / Q6(b)

13. Consider two vertices x and y in a directed graph G(V, E). Let $G_x$ and $G_y$ be the strongly connected components containing x and y respectively such that there exists a node $u \in G_x \cap G_y$. Show that $G_x$ and $G_y$ are identical. **Source:**

- 2944 / 2024 / Semester IV / Q1(g)

### Frequency Analysis

- **Most repeated questions:** Checking if a graph has a cycle; verifying if a graph is Bipartite; determining all Topological Orderings for a given DAG.
- **Frequently asked concepts:** The inadequacy of BFS for shortest path in arbitrarily weighted graphs; the inadequacy of DFS for shortest paths in unweighted graphs; the connection between cycles and bipartite graphs (odd cycles).
- **Trend analysis across years:** Bipartite property testing and topological sorting have appeared almost every year. The 2024 papers show a strong emphasis on cycle detection algorithms and strongly connected components logic.

---

# Unit 3: Divide and Conquer

## Topic: Recurrence Relations & Master Theorem

1. Use the Master's Theorem to give tight asymptotic bounds for the recurrence T(n) = 8T(n/2) + O(n²). **Source:**

- 4523 / 2023 / Semester IV / Q1(a)

2. Give a recurrence for the running time of the following algorithms to sort n elements. (i) Maxheapify (ii) Quicksort **Source:**

- 2208 / 2019 / Semester IV / Q1(b)

3. Consider a variation of the merge sort algorithm that solves a problem of size n by dividing it into two subproblems of sizes 2n/3 and n/3, and then merging the solutions. Find the recurrence for the running time of the above algorithm and solve it. **Source:**

- 6512 / 2018 / Semester IV / Q1(b)

4. Consider the ternary search algorithm for searching an element in a given array: divide the array into three equal parts by taking two mid points... Write the recurrence relation for the running time of the algorithm and solve it. **Source:**

- 2796 / 2017 / Semester IV / Q1(b)

5. Consider the following algorithm for finding an element t in a sorted array A of size n : `ter_search(Array A, Index first, Index last, Element t)` `Array A is divided into 3 equal parts.` `Let p and q be the index of the elements that divide A such that p < q` `if t = A[p] return p` `else if t < A[p] then ter_search(A, first, p-1, t).` `else if t = A[q] return q` `else if t < A[q] then ter_search(A, p+1, q-1, t).` `else ter_search(A, q+1, last, t)` Write a recurrence equation for computing the time complexity of the above algorithm and Justify the equation obtained by you and also solve it. **Source:**

- 2944 / 2024 / Semester IV / Q2(a)
- 4057 / 2024 / Semester IV / Q4(b)

6. Suppose divide and conquer approach is used by an algorithm to solve a problem on the input of size n. The algorithm divides the problem into k number of smaller instances, each of which is 1/b the size of the original problem... Let G(n) denotes the cost of dividing the problem into smaller instances and F(n) denotes the cost of combining the solutions. Write the recurrence relation to find the running time of the algorithm. Give G(n) and F(n) for Both Quicksort and Mergesort algorithm. **Source:**

- 1143 / 2022 / Semester IV / Q6(b)

7. Consider the recursive version of Insertion sort algorithm as follows : In order to sort A[1 : n], we recursively sort A[1 : n-1] and then insert A[n] into the sorted array A[1 : n-1]. Write a recurrence for the running time of this algorithm. **Source:**

- 1143 / 2022 / Semester IV / Q1(a)

## Topic: Divide & Conquer Sorting & Applications

1. Consider an input of n numbers that are all equal. What would be the running time of the following algorithms for the input : (i) Merge Sort (ii) Heap Sort **Source:**

- 2208 / 2019 / Semester IV / Q1(a)

2. Give the worst case for the merge algorithm to merge two sorted arrays A[1 ... k], B[1...m] (where n = k + m) and give the total number of comparisons in the worst case (in terms of n). Merge the two sorted arrays A = and B = using merge algorithm. How many number of comparisons are done by the algorithm in the above example? **Source:**

- 1143 / 2022 / Semester IV / Q1(j)

3. Discuss the time complexity of the following steps in the Merge sort algorithm : (i) Divide (ii) Combine **Source:**

- 2944 / 2024 / Semester IV / Q1(d)

4. A certain input to the merge sort algorithm is such that the merging step always depicts the worst case behaviour. Determine the running time of the merge sort algorithm for this instance. **Source:**

- 2796 / 2017 / Semester IV / Q7(b)

5. Is Merge sort (i) in place (ii) stable ? Explain. **Source:**

- 6512 / 2018 / Semester IV / Q3(c)

6. For each of the following sorting algorithms give an input of size five for which it shows worst case behaviour: (i) Merge sort (ii) Quick sort. **Source:**

- 6512 / 2018 / Semester IV / Q4(b)

7. Is it possible for the randomized version of Quick sort to show its worst-case behaviour on the following list of numbers? If yes, indicate a sequence of pivots that may cause such behaviour. And if not, justify. **Source:**

- 2944 / 2024 / Semester IV / Q3(b)

8. If quick sort is run on an n sized array such that the array is always divided into 2 equal halves. How many times is the partition algorithm called? Explain briefly. **Source:**

- 2208 / 2019 / Semester IV / Q5(b)

9. Recall that the usual implementation of quicksort makes two recursive calls. Consider a variant that optimizes on stack space as follows. It recurses on the smaller subarray as usual, but whenever it needs to recurse on the larger subarray, it uses an iterative module instead. What would be the depth of recursion for this variant? Compare it to the depth of recursion for usual implementation of quicksort. **Source:**

- 2208 / 2019 / Semester IV / Q1(e)

10. Suppose you have an algorithm to find median of n elements of an unsorted array in O(n) time in the worst case. Now consider an implementation of Quicksort where you first find median using the above algorithm, then use median as pivot. What will be the time complexity of this modified Quicksort? Write down the recurrence relation to justify your time complexity. **Source:**

- 1143 / 2022 / Semester IV / Q2(b)

11. Use Strassen's algorithm to compute the product of the following matrices: $$ \begin{pmatrix} 1 & 3 \ 5 & 7 \end{pmatrix} \begin{pmatrix} 8 & 4 \ 6 & 2 \end{pmatrix} $$ **Source:**

- 4057 / 2024 / Semester IV / Q1(e)

12. Show that at most $3 * \lfloor n/2 \rfloor$ comparisons are sufficient to find both the minimum and maximum in a given array of size n. **Source:**

- 4523 / 2023 / Semester IV / Q6(b)
- 6512 / 2018 / Semester IV / Q7(a)

13. Given a set of n numbers, write an algorithm to find the maximum and minimum element using divide and conquer strategy. Also, determine the time complexity. **Source:**

- 4057 / 2024 / Semester IV / Q7(a)

### Frequency Analysis

- **Most repeated questions:** Time complexity recurrences for D&C algorithms (Merge Sort variations, Quicksort, Ternary Search); finding Min/Max simultaneously using optimal $3\lfloor n/2 \rfloor$ comparisons.
- **Frequently asked concepts:** Behavior of standard algorithms (Merge Sort, Quick Sort) on structured input (all elements identical, worst-case arrangements); Master's theorem calculation.
- **Trend analysis across years:** Consistently heavy emphasis on generating recurrences for specific algorithm modifications (e.g., Ternary search in 2017/2024, recursive Insertion sort in 2022).

---

# Unit 4: Greedy algorithms

## Topic: Minimum Spanning Trees (Prim's & Kruskal's)

1. “Prim's algorithm only include an edge in the Minimum Spanning tree when it is justified by the Cut property.” State the Cut Property. Justify the above statement on the given graph showing cuts in all the intermediate steps. [Graph shown in source] **Source:**

- 1143 / 2022 / Semester IV / Q6(a)

2. Give an example graph with 5 nodes that gives two different Minimum Spanning Trees when computed with Prim's algorithm and Kruskal's algorithm. **Source:**

- 2208 / 2019 / Semester IV / Q1(f)
- 2944 / 2024 / Semester IV / Q5(b)

3. “The minimum spanning tree in a graph is not always unique.” Justify. Give a graph with 5 nodes that has two different minimum spanning trees. **Source:**

- 1143 / 2022 / Semester IV / Q1(e)

4. Can a graph G in which edge weights are not necessarily distinct, have more than one minimum spanning trees (MST). If yes, give an example; if no, justify. **Source:**

- 4523 / 2023 / Semester IV / Q1(i)
- 6512 / 2018 / Semester IV / Q3(b)

5. Let G(V, E) be a graph where V is the set of vertices and E is the set of edges. Let c(e) be the cost of edge $e \in E$ and T be a Minimum Spanning Tree (MST) of G, with cost $C_T$. Will the MST of the graph G change if the cost of every edge is modified as follows : (i) $1 - c(e)$ (ii) $c(e)^2$ Explain your answer. **Source:**

- 2944 / 2024 / Semester IV / Q5(a)
- 4057 / 2024 / Semester IV / Q6(b) (Similar format, asks if T and C will change)

6. Suppose a graph G has two edge-disjoint spanning trees (two spanning trees have no edges in common). Argue that in this graph G, every pair of nodes forms part of a cycle. **Source:**

- 2796 / 2017 / Semester IV / Q4(b)

## Topic: Shortest Path & Knapsack/Scheduling (Greedy)

1. Does the Dijkstra's algorithm for the shortest path problem work for graphs with negative edge weights? Justify your claim. **Source:**

- 2944 / 2024 / Semester IV / Q1(i)
- 2796 / 2017 / Semester IV / Q1(h) (Asks if Dijkstra will give shortest path for negative edges. Justify.)

2. Suppose we are given an instance of the Shortest s-t path problem on a directed graph G. We assume all the edge costs are positive and distinct. Let P be a minimum cost s-t path for this instance. Now suppose we replace each edge cost $c_e$ by its square, $c_e^2$, thereby creating a new instance of the problem with the same graph but different costs. Is it necessary for P to still be a minimum cost s-t path for this new instance ? Explain. **Source:**

- 6512 / 2018 / Semester IV / Q6(a)

3. The following graph represents network of airports that are connected to each other... Run an efficient algorithm to find the route taken by the flight to each to its destinations in minimum possible time. Show all the intermediate steps taken by the algorithm. Also derive its time complexity. **Source:**

- 1143 / 2022 / Semester IV / Q8(a)

4. A person named Albert starts a food delivery service... Compute the minimum time to reach them all individually. Now, suppose all Scooters need to be serviced and are unavailable. The amount of time taken to reach the destination using a bicycle is the square of the time taken... using a Scooter. Does this imply all such routes will never change...? **Source:**

- 32341401 / 2021 / Semester IV / Q2

5. What is (i) greedy-choice property? (ii) optimal substructure property? **Source:**

- 4057 / 2024 / Semester IV / Q1(b)

6. A Shopkeeper has n empty boxes and M number of balls. Let {$K_1, K_2 ......... K_n$} denote the number of balls that each box can store. Given M and {$K_1, K_2 ......... K_n$}, describe a greedy algorithm which determines the minimum number of boxes needed to store the balls. Give time complexity of the algorithm. **Source:**

- 1143 / 2022 / Semester IV / Q5(a)

7. A team of explorers is visiting the Sahara desert. As the weather is very hot, they are having n bottles of different sizes to carry water and keep them hydrated... They want to fill L litres of water in minimum number of bottles. Describe a greedy algorithm to help them fill U litres of water in minimum number of bottles. **Source:**

- 4523 / 2023 / Semester IV / Q1(c)

8. A Shopkeeper has W marbles and n empty bottles. Let $c_1, c_2,....... c_n$ respectively denote the number of marbles the bottles can contain. The shopkeeper wants to store the marbles in the bottles. (i) Describe a greedy algorithm which minimizes the number of bottles used. (ii) How would you modify your algorithm if bottle i also has an associated cost price $p_i$ and the goal is to minimize the total cost of the bottles used. **Source:**

- 2796 / 2017 / Semester IV / Q1(c)

9. A thief wants to steal all the gold dust from a store having W kg of it. The thief has n sacks having different capacities. Give an efficient algorithm for the thief to fill his sacks with dust so that the number of sacks used is minimized. **Source:**

- 2208 / 2019 / Semester IV / Q7(b)
- 6512 / 2018 / Semester IV / Q1(c)

10. Can 0-1 knapsack problem be solved optimally using greedy strategy? Justify your answer. **Source:**

- 4057 / 2024 / Semester IV / Q2(a)
- 4523 / 2023 / Semester IV / Q1(d) (Similar: "Will greedy strategy with parameter value per unit weight yield optimal for 0-1 knapsack?")

11. Consider the Interval Scheduling problem wherein we are given a resource and a set of requests each having a start time and a finish time. The goal is to maximize the number of requests scheduled. Show that the following greedy strategy does not give an optimal solution for the above problem. Greedy strategy: Select the request with fewest number of incompatible requests. **Source:**

- 1143 / 2022 / Semester IV / Q1(k)
- 2208 / 2019 / Semester IV / Q1(j)

12. Consider the weighted interval scheduling problem. Will the following greedy strategy work? Justify. While requests remain, Choose and add a request to solution that has the largest starting time and delete all non-compatible requests. **Source:**

- 2208 / 2019 / Semester IV / Q5(c)

13. For the Interval Scheduling Problem, consider the greedy strategy of selecting first the request that starts last, i.e., the request for which s(i) is as large as possible. Prove that this greedy approach always finds an optimal solution to the problem. **Source:**

- 2944 / 2024 / Semester IV / Q7(a)

14. Recall the scheduling problem wherein we are given a single resource and a set of requests having deadlines. A request is said to be late if it misses the deadline. Our goal is to minimize the maximum lateness... Argue that all schedules with no idle time and no inversions have the same maximum lateness. **Source:**

- 2208 / 2019 / Semester IV / Q3(b)
- 4523 / 2023 / Semester IV / Q2(a)

15. For the variant of interval scheduling problem that minimizes lateness, give an instance with two different optimal solutions, neither of which has any inversions or idle time. **Source:**

- 6512 / 2018 / Semester IV / Q4(c)

16. Let G = (V,E) be an undirected path graph with n nodes. We call a graph a 'path' if its nodes can be written as $v_1, v_2, ....... v_n$ with an edge between $v_i$ and $v_j$ if and only if the numbers i and j differ by exactly 1... Consider the following greedy algorithm for finding an independent set of maximum total weight in a path graph: `Start with S empty set. While some node remains in G, Pick a node v_i of maximum weight, Add v_i to S, Delete v_i and its neighbors from G. Endwhile. Return S`. Give an example to show that the above algorithm does not always find an optimal solution. **Source:**

- 6512 / 2018 / Semester IV / Q1(g)

### Frequency Analysis

- **Most repeated questions:** Impact of squaring/linear transformation of edge weights on Dijkstra and MST algorithms; checking if greedy algorithms (fractional vs 0-1 knapsack, interval scheduling counter-examples) guarantee optimality.
- **Frequently asked concepts:** Cut property (Prim's); Kruskal vs Prim difference leading to different MSTs on the same graph; greedy choice property logic for scheduling (earliest finish vs fewest incompatibilities).
- **Trend analysis across years:** The concept of evaluating a "flawed" greedy strategy by asking for a counter-example is extremely prevalent in the syllabus exams (especially in 2018, 2019, 2022).

---

# Unit 5: Dynamic Programming

## Topic: Knapsack & Subset Sum

1. Write the recurrence equation for solving 0 1 knapsack problem using dynamic programming. How is memoization technique used in solving the problem? **Source:**

- 4057 / 2024 / Semester IV / Q1(c)

2. Is the following recurrence for the Knapsack problem correct? If not, give the correct recurrence. Justify your answer in either case. If $w < w_i$ then $OPT(i,w) = OPT(i-1, w)$ Otherwise, $OPT(i,w) = \max(OPT(i-1), w), v_i + OPT(i-1, w)$ **Source:**

- 2208 / 2019 / Semester IV / Q4(b)

3. Consider the following recursive relation for 0-1 knapsack problem. If $w < w_i$, then $OPT(i, w) = OPT(i-1, w)$ else $OPT(i, w) = \max(OPT(i-1, w), v_i + OPT(i-1, ____))$ where $OPT(i, w)$ denote the value of the optimal solution... $v_i$ is the cost of ith item. Fill the missing value. What is the running time of the recursive implementation of the above recurrence? Justify. Give memoized recursive algorithm for the above problem. Explain how does it improve the running time? **Source:**

- 1143 / 2022 / Semester IV / Q3(b)

4. A boat has a capacity C to carry load. There are n number of items each having certain weight Wi associated with it. The goal is to select the set of items that the boat should carry so that it could carry maximum load(i.e. sum of the weights of selected items should be maximum) within its capacity C. Design a Polynomial time Dynamic Programming algorithm for the problem. Derive the time complexity of the above algorithm. Run this algorithm on the sample instance given below to find the optimal solution. Capacity of the boat = 4kg. Items: [Item1: 3kg, Item2: 2kg, Item3: 1kg]. **Source:**

- 1143 / 2022 / Semester IV / Q7(a)

5. Give the condition(s) under which the 0-1 Knapsack problem becomes equivalent to the subset sum problem. How would you modify the recursive formula for the subset sum problem to solve 0-1 knapsack problem? **Source:**

- 2944 / 2024 / Semester IV / Q4(b)

6. Give a recurrence relation for solving the subset sum problem. **Source:**

- 2208 / 2019 / Semester IV / Q2(c)

7. Solve the Subset Sum Problem using dynamic programming with W = 17, and 4 items with weights $w_1 = 4, w_2 = 2, w_3 = 9, w_4 = 6$. Also, give the recursive formula. **Source:**

- 2944 / 2024 / Semester IV / Q4(a)
- 4057 / 2024 / Semester IV / Q6(a) (Subset sum for {4, 2, 9, 6} and sum 17).

8. Consider the following recursive algorithm to find an optimal solution to the subset sum problem : `Compute_opt(i,w)` ... (i) Explain why does this algorithm take exponential time to run in the worst case. (ii) What changes should be made to the above algorithm to make it run in polynomial time. (iii) Consider an optimal solution to the above problem. Is it possible for this solution to contain a sub-optimal solution to a subproblem ? Explain. **Source:**

- 6512 / 2018 / Semester IV / Q6(b)

## Topic: Interval Scheduling & Subarrays

1. What are the two key factors that decide whether Dynamic Programming is applicable for an optimization problem or not? **Source:**

- 1143 / 2022 / Semester IV / Q1(d)
- 2944 / 2024 / Semester IV / Q1(e) ("What are the two principles of Dynamic Programming?")

2. Can dynamic programming be applied to all optimization problems? Why or why not? **Source:**

- 4523 / 2023 / Semester IV / Q1(e)

3. Consider the following recursive algorithm to find an optimal schedule for weighted interval scheduling problem : `Compute_opt(j)` ... (i) Explain why does this algorithm take exponential time to run in the worst case. (ii) What changes should be made to the above algorithm to make it run in polynomial time. **Source:**

- 2796 / 2017 / Semester IV / Q4(a)

4. Consider an instance of the weighted interval scheduling problem with 6 intervals as specified below : ... With the help of the above example argue that the memorized recursive algorithm solves lesser number of subproblems than the corresponding iterative algorithm. **Source:**

- 6512 / 2018 / Semester IV / Q1(d)
- 2796 / 2017 / Semester IV / Q1(c) (Subset sum variant of the same question: memorized vs iterative).

5. There are n Jobs where each job starts at time $s_i$ and finishes at time $f_i$. There is a profit associated with each job. The goal is to find a subset of non-overlapping jobs such that the sum of their profits is maximum. Given below is the instance of the problem : [Job1: 0-6 Profit 60, Job2: 1-4 Profit 30, Job3: 3-5 Profit 10, Job4: 5-7 Profit 30, Job5: 5-9 Profit 50, Job6: 7-8 Profit 10]. Give a Dynamic programming iterative solution for the above problem. Explain the recurrence relation used in the solution. Show that the “Optimal solution to the above problem contains within it optimal solution to its subproblems.” With reference to the above example. **Source:**

- 1143 / 2022 / Semester IV / Q8(b)

6. Given an array A of n integers, you need to find the maximum sum of any contiguous subarray. For instance, the maximum sum of any contiguous subarray in the array `-1, 2, 3, -2, 5, -6, 7, -8` is 9 (which is the sum of the subarray `2, 3, -2, 5, 6, 7`). Complete the following Dynamic Programming solution for the above problem : `DP = A` `For i = 1 to n` `DP[i] = max(A[i], _____ )` **Source:**

- 4523 / 2023 / Semester IV / Q4(b)

7. Consider the following recurrence relation for computing the sum of n natural numbers. F(n) = F(n-1)+n, n>1; F(1) = 1. What is the running time of the recursive implementation of the above recurrence? Would memoizing the recursive solution improve the running time? Explain. **Source:**

- 2208 / 2019 / Semester IV / Q1(g)

8. Write a pseudocode for the memorized recursive algorithm to compute the nth Fibonacci number. What would be its time complexity? **Source:**

- 4523 / 2023 / Semester IV / Q7(b)

### Frequency Analysis

- **Most repeated questions:** Filling in missing recurrence logic for 0-1 Knapsack and Subarray/Fibonacci DP problems; calculating DP matrix step-by-step for small W knapsack or subset sum.
- **Frequently asked concepts:** Memoization vs. Iteration (Top-down vs Bottom-up) subproblem trees; overlapping subproblems & optimal substructure definitions.
- **Trend analysis across years:** Standard applications (Subset Sum, Weighted Interval Scheduling) run steadily throughout the years, requiring not just code but detailed step-by-step table resolutions.

---

# Unit 6: Intractability

## Topic: P, NP, NP-Completeness & Reductions

1. “Suppose $Y \le_p X$. If X can be solved in polynomial time, then Y can be solved in polynomial time.” Based on the above statement, which of the following statements are correct? If any statement is incorrect, write its correct version. (i) If Y cannot be solved in polynomial time, then X cannot be solved in polynomial time. (ii) Y is at least as hard as X. (iii) If X belongs to NP, then X is NP-complete problem. **Source:**

- 4057 / 2024 / Semester IV / Q2(b)

### Frequency Analysis

- **Most repeated questions:** Very few questions appear exactly targeting intractability in the provided dataset, besides theoretical implications of polynomial-time reductions.
- **Frequently asked concepts:** Poly-time reduction definitions ($Y \le_p X$ implications).
- **Trend analysis across years:** The concept is primarily foundational, mainly appearing as 1-2 mark questions on whether a problem in NP equates to NP-completeness.

---

# Unit 7: Advanced Analysis of Algorithms

## Topic: Amortized Analysis

1. A sequence of n operations is performed on a data structure. The ith operation costs i if i is an exact power of 2, and 1 otherwise. Use aggregate analysis to determine the amortized cost per operation. **Source:**

- 4057 / 2024 / Semester IV / Q1(f)
- 1143 / 2022 / Semester IV / Q7(b)

2. Consider a k bit binary counter implemented using an array A such that A stores the lowest order bit and A[k-1] stores the highest order bit. The only operation that can be performed on the counter is 'increment'. Using the aggregate method of analysis, determine the amortised cost per increment operation when a sequence of n increments is performed. **Source:**

- 2796 / 2017 / Semester IV / Q7(a)
- 2944 / 2024 / Semester IV / Q8(b) (Identical phrasing: "Suppose we implement a k-bit binary counter...")

3. Consider a stack S that supports the following operations : `Push(S, x) : push element x onto stack S` `Pop(S) : pop the top element from stack S and return it` `Multipop(S, k) : remove top k elements of stack S` Using the aggregate method of analysis, determine the amortised cost per operation when a sequence of n operations is performed on an empty stack. **Source:**

- 6512 / 2018 / Semester IV / Q4(a)
- 2208 / 2019 / Semester IV / Q5(a) (Similar conceptual question asking if amortized cost is O(1) and to explain).

4. Suppose we perform a sequence of stack operations on a stack whose size never exceeds k. After every k operations, we make a copy of the entire stack for backup purposes. Show that the cost of n stack operations, including copying the stack, is O(n) by assigning suitable amortized costs to the various stack operations. **Source:**

- 4523 / 2023 / Semester IV / Q3(b)

5. A party is going on in a hotel. When the dinner starts, a waiter is assigned the task of distributing plates to the guests. He creates a pile of plates on a table by adding one plate at a time. The waiter can pick up one or more plates at a time from the pile to distribute... Analyse the average cost per operation over a sequence of n operations. **Source:**

- 32341401 / 2021 / Semester IV / Q5

### Frequency Analysis

- **Most repeated questions:** Aggregate analysis of a binary counter; Stack multi-pop/backup operations amortized cost mapping; Dynamic array/Power of 2 operation cost.
- **Frequently asked concepts:** The Aggregate Method is explicitly tested almost universally when addressing amortized analysis.
- **Trend analysis across years:** Appears exactly once in every paper examined in the dataset, highly consistent.

---

# Miscellaneous (Fundamentals & Growth of Functions)

1. Arrange the following functions in the increasing order of their rate of growth : $2^{2^n}$, $2^{n^2}$, $n^2\log(n)$, $n^{2^n}$ **Source:**

- 2796 / 2017 / Semester IV / Q1(a)

2. Arrange the following functions in the increasing order of their rate of growth : $n^2\log(n)$, $2^n$, $2^{2^n}$, $n^{\log(n)}$. **Source:**

- 6512 / 2018 / Semester IV / Q1(a)

3. How many times will the print statement in the following code snippet be executed? `i = 1` `while i*i <= n` `print("Hello")` `i += 1` **Source:**

- 2944 / 2024 / Semester IV / Q1(b)

4. Discuss the running time of the following snippet of code : `count = 0` `for (i=1, i<=n, i++)` `for (j = 1, j<=n, j = 2 * j)` `count++` **Source:**

- 4523 / 2023 / Semester IV / Q1(b)

5. Discuss the run time complexity of the naive string matching algorithm. / Give a scenario in which the naive string matching algorithm demonstrates its worst case behaviour. **Source:**

- 2796 / 2017 / Semester IV / Q1(g)
- 6512 / 2018 / Semester IV / Q1(h)
- 2208 / 2019 / Semester IV / Q2(b)

### Frequency Analysis

- **Most repeated questions:** Loop analysis for Big-O notation (`O(\sqrt{n})` or `O(n \log n)` equivalent structures); sorting functional rates of growth.
- **Frequently asked concepts:** Asymptotic behavior comparisons.