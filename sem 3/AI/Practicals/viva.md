## I. Fundamental AI Concepts

**1) What is AI? Difference between weak vs strong ai. What is super ai.**

- **What is AI?**
    
    - AI is a branch of computer science concerned with the study and creation of computer systems that exhibit some form of intelligence.
    - The rational agent approach to AI, which has generally prevailed, focuses on the study and construction of agents that "do the right thing".
    - AI systems are designed to perform tasks that require high levels of human-like intelligence, but the programs are not necessarily meant to imitate human senses or thought processes.
- **Weak vs. Strong AI**
    
    - The sources describe **weak methods** (or general algorithms) as those used by early general-purpose problem solvers that relied on a limited number of laws or axioms. These methods proved too weak to be effective for complex problems.
    - In machine learning, **weak methods** are general-purpose methods with little or no initial knowledge, often relying on heuristic search. These are contrasted with **knowledge-rich methods**.
    - _(Note: The sources do not explicitly define the philosophical concepts of "Weak AI" or "Strong AI.")_
- **Super AI (Artificial Superintelligence - ASI)**
    
    - The goal of creating intelligence comparable to or more capable than human intelligence is a long-standing one in AI.
    - **Artificial Superintelligence (ASI)** is a term associated with the concerns raised regarding the creation of superhuman AI.

**2) Define learning, autonomous systems.**

- **Learning / Machine Learning**
    
    - An agent is learning if it improves its performance after making observations about the world.
    - Machine learning is a subfield of AI.
    - Machine learning is defined as the autonomous acquisition of knowledge through computer programs.
- **Autonomous Systems / Agents**
    
    - An **agent** is simply something that acts.
    - Computer agents are expected to operate **autonomously**, perceive their environment, persist over a prolonged time period, adapt to change, and create and pursue goals.
    - A **rational agent** is one that acts so as to achieve the best outcome or the best expected outcome under uncertainty.

**9) Difference between AI and learning or machine learning.**

- AI is the overall field focused on studying and creating intelligent computer systems.
- Machine learning is a specialized **subfield** or branch of AI.
- While AI encompasses many techniques (including search, reasoning, and knowledge representation), machine learning specifically concerns the ability to improve performance based on experience and the autonomous acquisition of knowledge.

---

## II. PROLOG and Logic Programming

**7) On which model prolog is working and how?**

- PROLOG (PROgramming in LOGic) is a logic programming language that uses the syntax of predicate logic to perform symbolic, logical computations.
- It is based on the **resolution principle**.
- The specific refutation proof strategy used in PROLOG is **SLD resolution** (selective linear with definite clauses), which is a form of linear input resolution using definite Horn clauses.
- PROLOG programs are executed through **depth-first backward chaining**.
- PROLOG also uses **database semantics**, which includes the unique names assumption and the closed world assumption, distinguishing it from general first-order logic.

**8) facts, rules and queries.**

- **Facts:** Declared using predicates and constants, typically written in lowercase letters. Arguments are enclosed in parentheses and separated by commas.
    - _Example:_ `parent(ann,sam)`.
- **Rules:** Composed of a conclusion ("then" part) and a condition ("if" part), separated by the symbol `:-` (read as "if"). Rules represent general relations. Conditions in the "if" part are separated by commas, which act as conjunctions ("and"). Variables must begin with uppercase letters.
    - _Example:_ `grandfather(X,Z) :- parent(X,Y), parent(Y,Z), male(X)`.
- **Queries:** Statements typed after the query symbol `?-`. Responses return variable values that satisfy the query, or simply `yes` (true) or `no` (false).

**3) How to define list in prolog? Data types available in prolog. Usage of different operators and their precedence.**

- **List Definition:** A PROLOG list is written as a sequence of items separated by commas and enclosed in square brackets.
    - _Example:_ `[tom,sue,joe,mary,bill]`.
    - A nonempty list has a **head** and a **tail**, similar to LISP's `car` and `cdr`.
    - The notation `[Head|Tail]` separates the head item(s) from the remaining list.
- **Data Types:** PROLOG includes predicates, constants, and variables in its language. It also has numeric functions and relations. _(The sources do not detail the standard data types like integer or float.)_
- **Operators:** The `:-` symbol is used to separate the conclusion from the condition in a rule (read as "if"). Commas act as conjunctions (AND statements) within a rule's conditions. _(The sources do not discuss operator precedence in detail.)_

**4) What is backtracking in prolog? How it works?**

- **Backtracking (Implicit Search):** PROLOG uses resolution, implemented via **depth-first backward chaining** search, to find a proof for a query.
- **How it Works:**
    1. The query sets up a sequence of goals to be satisfied.
    2. PROLOG searches the database to find matching predicates and attempts to make consistent substitutions of constants and variables for the arguments.
    3. If a consistent set of substitutions is found (i.e., a goal logically follows from the facts and rules), the query succeeds.
    4. If a potential match fails or if all required substitutions cannot be found, failure is reported (`no`).

**5) Difference between cut and fail predicate.**

- _(The provided source material does not contain information regarding the PROLOG predicates "cut" or "fail.")_

**6) Explanation of each program with possible outputs.**

Here are two PROLOG examples presented in the sources:

|Program/Rule Set|Explanation|Query & Output|
|:--|:--|:--|
|**A. Grandfather Rule**|X is the grandfather of Z if X is the parent of Y, and Y is the parent of Z, and X is male.|`?-grandfather(X,Y)` `X=joe, Y=sam`|
|**B. Member Function**|Defines when an item X is a member of a list L. The first clause (`member(X,[X|Tail]).`) states X is a member if it is the head. The second clause states X is a member if it is a member of the remaining tail.|
|||`?- rnember(b,[a,[b,c],d])` `no` (because `b` is not the first element, and is not a member of the tail `[[b,c],d]`)|

## Part 1: Intelligent Agents (Russell/Norvig)

### 1) Four Categories of AI Definitions

AI goals can be categorized based on whether they focus on **thought** (internal process) or **behavior** (external action), and whether they aim for **human** performance or abstract **rationality** (doing the right thing).

|Approach|Focus|Description|Example|
|:--|:--|:--|:--|
|**Acting Humanly**|Behavior (Fidelity to human performance)|A machine passes the Turing test if a human interrogator cannot distinguish its written responses from a person’s.|Requires capabilities like natural language processing, automated reasoning, and robotics.|
|**Thinking Humanly**|Thought (Cognitive Modeling)|Requires having a precise theory of the human mind, often involving comparison of the sequence and timing of reasoning steps to human subjects.|General Problem Solver (GPS).|
|**Thinking Rationally**|Thought (Laws of Thought)|Uses formal logic to generate conclusions mechanically from premises, emphasizing correct inferences.|The logicist tradition in AI.|
|**Acting Rationally**|Behavior (Rational Agent)|Focuses on studying and constructing agents that "do the right thing", maximizing the expected outcome. This is the prevailing approach in the field.|Any agent that achieves the best expected outcome.|

### 2) Components of an Intelligent Machine

To pass the rigorous **Total Turing Test**, a system (robot) would require:

- **Natural Language Processing:** To communicate successfully.
- **Knowledge Representation:** To store what it knows or hears.
- **Automated Reasoning:** To answer questions and draw new conclusions.
- **Machine Learning:** To adapt to new circumstances and extrapolate patterns.
- **Computer Vision and Speech Recognition:** To perceive the world.
- **Robotics:** To manipulate objects and move about.

### 3) Agents and Rational Agents. Agent Function vs. Agent Program

- **Agent:** Something that acts. It perceives its environment through sensors and acts upon it through actuators.
- **Rational Agent:** An agent that acts so as to achieve the best outcome or, when uncertain, the best expected outcome.
- **Agent Function:** The abstract mathematical description that maps the entire sequence of percepts received by the agent to an action. It is an external characterization of the agent.
- **Agent Program:** A concrete implementation of the agent function, running within some physical system. It takes the **current percept** as input.

### 4) PEAS and Types of Environmental Properties

The **PEAS** scheme describes the environment (E), actuators (A), and sensors (S) necessary to achieve the performance measure (P).

|Environmental Properties (Dimensions)|Definition|
|:--|:--|
|**Fully Observable/Partially Observable/Unobservable**|Whether the agent's sensors give it access to the complete state of the environment.|
|**Deterministic/Stochastic**|Whether the next state of the environment is completely determined by the current state and the action executed.|
|**Episodic/Sequential**|Whether the agent's experience is divided into atomic episodes where the choice of action in one episode does not affect later episodes.|
|**Static/Dynamic**|Whether the environment changes while the agent is deliberating.|
|**Discrete/Continuous**|Whether the state of the world, time, and percepts/actions are discrete or continuous.|
|**Single-agent/Multiagent**|Whether other agents are present and affect the environment.|
|**Known/Unknown**|Whether the agent knows the rules (transition model) of the environment.|

### 5) Model in AI and Types of AI (Agent Architectures)

- **Model (Transition Model):** Information encoded in the agent program about how the world changes over time. This includes the effects of the agent's actions and how the world evolves independently.
- **Four Basic Types of Agent Programs/Architectures**:
    1. Simple reflex agents
    2. Model-based reflex agents
    3. Goal-based agents
    4. Utility-based agents

### 6) Learning Agents

An agent is learning if it improves its performance after making observations about the world. Learning is crucial because designers cannot anticipate all future situations and often do not know how to program a solution themselves.

A learning agent is conceptually divided into four components:

1. **Performance Element:** What we previously considered the whole agent program; it selects external actions.
2. **Learning Element:** Responsible for making improvements by modifying components of the performance element.
3. **Critic:** Tells the learning element how well the agent is doing with respect to a fixed performance standard.
4. **Problem Generator:** Suggests actions that might lead to new, informative experiences.

---

## Part 2: Knowledge Representation (Patterson/Logic)

### 1) Why KR is required? PL and Syntax/Semantics of PL

- **Why KR is Required:** Knowledge is the food for intelligence. Knowledge is essential for intelligent behavior, and its representation is one of AI's top research priorities. KR is needed to handle knowledge acquisition, organization, manipulation, and representation.
- **Propositional Logic (PL):** A special case of First Order Predicate Logic (FOPL).
- **PL Syntax:** Governs the combination of basic building blocks, which are elementary atomic sentences (propositions) and logical connectives.
- **PL Semantics:** Defines the rules for determining the truth of a sentence with respect to a particular model. In PL, a model is an assignment of a truth value (true or false) for every proposition symbol. Truth tables are used to compute the truth value of sentences formed with connectives.

### 2) Problems with PL. How FOPL overcome these problems

- **Problems with PL:** It is too "coarse" to easily describe the properties of objects. It lacks the structure to express relations that exist among two or more entities. It does not permit generalized statements about classes of similar objects.
- **FOPL Overcomes Problems:** FOPL is expressive enough to allow for the use of symbols for predicates, functions, variables, constants, and quantifiers, which permits the accurate representation of natural language concepts.

### 3) Components of FOPL and Well-Formed Formula (WFF)

- **FOPL Components:** Statements in FOPL are translated into symbolic structures composed of predicates, functions, variables, constants, quantifiers, and logical connectives.
- **Well-Formed Formula (WFF):** This term is often used interchangeably with "valid statements or sentences" in logic. Valid FOPL structures are formed by combining its components according to the formal syntax rules of FOPL.

### 4) Checking Meaning and Conversion to Clausal Form

- **Checking Meaning in PL:** The truth value of any sentence is determined with respect to a model using truth tables.
- **Checking Meaning in FOPL:** The semantics define the truth of each sentence in each possible world or model.
- **Conversion to FOPL:** Involves translating natural language statements into symbolic structures using predicates, functions, variables, etc..
- **Conversion to Clausal Form (CNF):** Resolution requires all statements to be converted into a normalized **clausal form**. A clause is defined as the disjunction of a number of literals.

### 5) CNF, DNF and Resolution Principle

- **Conjunctive Normal Form (CNF):** A complex set of formulas can be converted into CNF. A clause (the component of CNF) is the disjunction of literals.
- **Disjunctive Normal Form (DNF):** This form is implied by the text, which includes exercises requiring transformation into DNF.
- **Resolution Principle:** A syntactic inference procedure that, when applied to a set of clauses, determines if the set is unsatisfiable. It is similar to obtaining a proof by contradiction (refutation), where the goal is to deduce the empty clause (contradiction). PROLOG is based on the resolution principle.

### 6) Problems with FOPL and Benefits of Semantic Network

- **Problems with FOPL:** When modeling the real world, FOPL struggles with inconsistent, uncertain, incomplete, or vague knowledge. Additionally, FOPL systems tend to be monotonic (only growing with added knowledge), which clashes with real-world common sense reasoning where facts may need to be retracted.
- **Semantic Network Benefits:** Also called associative networks, they cluster and bind related information using linked nodes (concepts) and arcs (relations). This structure is appealing because the knowledge needed for a task is typically localized in a narrow domain or "semantic vicinity," which aids retrieval efficiency and resembles how humans store knowledge.

### 7) Frames and their Structure and Application

- **Frames:** Structured sets of closely related knowledge, useful for grouping and linking related chunks of knowledge.
- **Structure:** Frames use **slots** and **facets** to store information. These slots contain the object name, its main attributes and values, and potentially attached procedures (e.g., if-needed, if-added, if-removed).
- **Application:** Frames support **property inheritance** and **default reasoning**. They have been used in the architecture of several expert systems.

### 8) Conceptual Dependency (CD) Creation

Conceptual dependency theory provides primitive building blocks for actions and states. Building CD structures typically follows three simple steps:

1. Obtain the next lexical item (a word or phrase).
2. Access the lexical entry for the item to obtain the associated tests and actions.
3. Perform the actions specified with the entry.

### 9) Script and their application in relation world

- **Scripts:** Special frame-like structures that represent stereotypical patterns for commonly occurring events. They contain actors, roles, props, and scenes, much like a play.
- **Application:** Scripts are used to fill in missing details about a current scenario based on prestored descriptions. They have been used in programs that read and "understand" language in the form of stories.

## I. Natural Language Processing (NLP)

### 1. Role of NLP and its Processing

- **Role of NLP:** Developing programs to understand natural language is important because a natural form of communication with systems is essential for user acceptance. The ability to communicate effectively is one of the most critical tests for intelligent behavior (the Turing test).
- **Understanding:** A program understands a natural language if it behaves by taking a predictably correct or acceptable action in response to the input.
- **Processing:** NLP requires transforming sentences into data structures which convey the intended meaning to a reasoning program. The whole process is a series of transformations from basic speech sounds to a complete set of internal representation structures.
- **Knowledge Levels:** Successful systems require knowledge of language structure, word meanings (semantics), context (pragmatics), and general world knowledge.

### 2. Parser, Types of Parsers

- **Parser Function:** Parsing is the analysis of a sentence to determine its structure (syntax) and grammatical correctness. It can be thought of as a search for a valid parse tree whose leaves are the words of the string.
- **Top-Down vs. Bottom-Up:** Parsing can start with the structure (Top-Down, beginning with the S symbol) or with the words (Bottom-Up). Both pure strategies can be inefficient.
- **Deterministic vs. Nondeterministic:**
    - **Deterministic Parsers** permit only one choice (arc) for each word category. If an incorrect choice is accepted, the parse fails, as the parser cannot backtrack.
    - **Nondeterministic Parsers** allow multiple choices at a given state.
- **Chart Parsers:** Use dynamic programming to avoid repeating effort by storing the results of analyzing substrings in a data structure called a chart. The **CYK algorithm** is a probabilistic bottom-up chart parser, running in $O(n^3m)$ time for context-free grammars.

### 3. Transition Network and RTN

- **Transition Networks (TNs):** Simple transition networks are basic parsing techniques.
- **Recursive Transition Networks (RTNs):** Similar to simple TNs, but are defined recursively. An RTN parser uses a stack (RLIST) to PUSH a return node onto the list when a subnetwork is called and POP the node when the traversal is complete.
- **Augmented Transition Networks (ATNs):** An extension of the RTN that includes tests and actions as part of the arc components. ATNs use special registers to help build syntactic structures and enable extensive semantic analysis. The LUNAR system used an ATN parser.

## II. Game Playing

### 1. Minimax Algorithm, Utility Function, and Alpha-Beta Pruning

- **Minimax Algorithm:** A slightly more general search algorithm than AND–OR search, used for games with multiple outcome scores. It assumes that the agent (MAX) will choose the move that maximizes its score, given that the opponent (MIN) will choose the move that minimizes MAX's score.
- **Utility Function:** A function that applies to **terminal states** to define the final score or outcome. The goal of MAX is to maximize this utility.
- **Look-Ahead Process (Search Cutoff):** Minimax search is often cut off at a fixed depth limit, $d$, chosen to ensure a move is selected within the allocated time.
- **Plausible Move Generator/Evaluation:** When the search is cut off, a heuristic **EVAL function** is called to evaluate the nonterminal state. Early game programs relied on human expertise to craft these evaluation functions.
- **Alpha-Beta Pruning:** A technique that generates the game tree incrementally and prunes branches that cannot possibly affect the final optimal decision. This is achieved by maintaining bounds ($\alpha$ for MAX's best choice so far, $\beta$ for MIN's best choice so far).

## III. Problem and Search Space

### 1. What is problem and how to define it properly

- **Problem Definition:** A problem is characterized as a space consisting of a set of **states** (which may not be finite) and a set of **operators** (actions) that map from one state to other states.
- **State Types:** Problems distinguish between one or more **initial states**, intermediate states, and one or more **goal states**.
- **Solution:** A solution to a problem is defined as a sequence of operators that maps an initial state to a goal state.

### 2. State space, study about famous problems like water jug, 8-queen etc

- **State Space:** The graph where the nodes are states and the edges are actions.
- **8-Puzzle:** Consists of eight numbered, movable square tiles in a $3\times3$ frame with one empty space. The objective is to find a sequence of tile movements from a start configuration to a goal configuration. The states are the different permutations of the tiles.
- **8-Queens Problem:** The goal is to find a valid final configuration of 8 queens on a chessboard where none attacks another. This problem is noted for being trivially easy for **local search** methods, such as min-conflicts, because solutions are densely distributed.

### 3. Searching, Informed Search vs Uninformed Search

- **Searching:** A search procedure is a strategy for selecting the order in which nodes are generated and a given path is selected. It is required in almost all AI programs.
- **Uninformed (Blind) Search:** An algorithm that uses no information other than the initial state, the search operators, and a test for a solution. It explores nodes in some predetermined order.
- **Informed (Heuristic) Search:** Utilizes additional problem-specific knowledge (heuristics) to select the most promising node for expansion.

### 4. BFS, DFS, Best-First Search

- **Breadth-First Search (BFS):** Explores all nodes at a given depth before proceeding to the next level.
    - **Properties:** It is complete if the branching factor $b$ is finite and a solution exists. It is guaranteed to find a minimal path length solution and is cost-optimal if all action costs are identical.
    - **Complexity:** Time and space complexity are $O(b^d)$, where $d$ is the depth of the shallowest solution.
- **Depth-First Search (DFS):** Explores paths to the maximum depth $m$ before backtracking.
    - **Properties:** It is not complete or cost-optimal in the general case.
    - **Complexity:** It has low memory complexity, only $O(bm)$.
- **Best-First Search:** A general search algorithm that uses an evaluation function $f$ (often a heuristic) to determine the order in which nodes are expanded from the frontier.

### 5. Hill Climbing Algorithm and its working, problems, and wayout

- **Hill Climbing:** A **local search** method applied to optimization problems. It keeps only a small number of states in memory.
- **Working:** It modifies one variable at a time in the space of complete assignments, moving only to a neighboring state that improves the evaluation score (e.g., reduces the number of unsatisfied constraints in SAT problems).
- **Problems (Limitations):** Hill climbing frequently gets stuck in **local minima**.
- **Wayout (Stochastic Methods):** **Simulated Annealing** is a stochastic local search algorithm that introduces randomness to escape local minima and can return optimal solutions if given an appropriate cooling schedule.

### 6. A* Algo, Underestimation and Overestimation

- __A_ Algorithm (A_ Search):** The most widely known form of best-first search, it is an optimal search algorithm. It evaluates nodes $n$ using the cost function $f(n) = g(n) + h(n)$.
    - $g(n)$: The cost of the path from the initial state to $n$.
    - $h(n)$: The estimated cost of the cheapest path from $n$ to a goal state.
- **Underestimation (Admissible Heuristic):** A heuristic $h(n)$ is **admissible** if it never overestimates the cost to reach the goal. If $h(n)$ is admissible, A* is guaranteed to be cost-optimal.
- **Overestimation:** If $h(n)$ overestimates the true cost, A* may expand fewer nodes, but it sacrifices optimality.