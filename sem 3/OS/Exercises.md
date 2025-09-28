### Chapter 3: Processes

(Topics: 3.1 Process Concept, 3.2 Process Scheduling, 3.3 Operations on Processes, excluding process creation using Windows API figure 3.11)

| Question | Type     | Summary                                                                                                                                           |
| :------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| **3.1**  | Practice | Using the program shown in Figure 3.30 (involving `fork()`), explain what the output will be at LINE A.                                           |
| **3.2**  | Practice | Including the initial parent process, how many processes are created by the program shown in Figure 3.31?.                                        |
| **3.3**  | Practice | Discuss three major complications that concurrent processing adds to an operating system.                                                         |
| **3.4**  | Practice | Describe what happens when a context switch occurs if the new context is already loaded into one of the register sets (Sun UltraSPARC).           |
| **3.5**  | Practice | When a process creates a new process using the `fork()` operation, which of the following states is shared: Stack, Heap, Shared memory segments?. |
| **3.8**  | Exercise | Describe the differences among short-term, medium-term, and long-term scheduling.                                                                 |
| **3.9**  | Exercise | Describe the actions taken by a kernel to context-switch between processes.                                                                       |
| **3.10** | Exercise | Construct a process tree similar to Figure 3.8.                                                                                                   |
| **3.11** | Exercise | Explain the role of the `init` process on UNIX and Linux systems in regard to process termination.                                                |
| **3.12** | Exercise | Including the initial parent process, how many processes are created by the program shown in Figure 3.32?.                                        |
| **3.13** | Exercise | Explain the circumstances under which the line of code marked `printf("LINE J")` in Figure 3.33 will be reached.                                  |
| **3.14** | Exercise | Using the program in Figure 3.34, identify the values of `pid` at lines A, B, C, and D.                                                           |
| **3.17** | Exercise | Using the program shown in Figure 3.35, explain what the output will be at lines X and Y.                                                         |

_**Note:**_ _Programming Problem 3.20 (PID manager), 3.21 (Collatz conjecture), and related exercises 3.22, 3.26, and 3.27, while related to process operations and creation, are programming assignments/problems and are listed here for completeness if required, but the primary request focuses on analytical questions from the back exercises._

### Chapter 4: Threads

(Topics: 4.1 Overview, 4.2 Multicore Programming, 4.3 Multithreading Models, 4.4 Thread Libraries, 4.4.1 Pthreads)

| Question | Type     | Summary                                                                                                                                                                                     |
| :------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **4.6**  | Exercise | Provide two programming examples in which multithreading does not provide better performance than a single-threaded solution.                                                               |
| **4.7**  | Exercise | Under what circumstances does a multithreaded solution using multiple kernel threads provide better performance than a single-threaded solution on a single-processor system?.              |
| **4.8**  | Exercise | Which components of program state are shared across threads in a multithreaded process? (Register values, Heap memory, Global variables, Stack memory).                                     |
| **4.9**  | Exercise | Can a multithreaded solution using multiple user-level threads achieve better performance on a multiprocessor system than on a single-processor system?.                                    |
| **4.11** | Exercise | Is it possible to have concurrency but not parallelism? Explain.                                                                                                                            |
| **4.12** | Exercise | Using Amdahl’s Law, calculate the speedup gain of an application that has a 60 percent parallel component for (a) two processing cores and (b) four processing cores.                       |
| **4.13** | Exercise | Determine if the following problems exhibit task or data parallelism: the multithreaded statistical program (Exercise 4.21), Sudoku validator (Project 1), and sorting program (Project 2). |
| **4.14** | Exercise | Discuss thread creation strategies for a computationally and I/O-intensive application.                                                                                                     |
| **4.15** | Exercise | Consider a code segment involving `fork()` and `thread_create()`. How many unique processes and how many unique threads are created?.                                                       |

### Chapter 5: Process Synchronization

(Topics: 5.1 Background, 5.2 The Critical-Section Problem, 5.3 Peterson’s Solution)

| Question | Type     | Summary                                                                                                                                                                    |
| :------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **5.3**  | Practice | What is the meaning of the term busy waiting? What other kinds of waiting are there? Can busy waiting be avoided altogether?.                                              |
| **5.7**  | Exercise | Describe how a race condition is possible in a banking system with concurrent `deposit()` and `withdraw()` functions, and what might be done to prevent it.                |
| **5.8**  | Exercise | Dekker’s algorithm: Prove that the algorithm satisfies all three requirements for the critical-section problem.                                                            |
| **5.10** | Exercise | Explain why implementing synchronization primitives by disabling interrupts is not appropriate in a single-processor system if they are to be used in user-level programs. |
| **5.13** | Exercise | Describe two kernel data structures in which race conditions are possible.                                                                                                 |
| **5.15** | Exercise | Implement the `acquire()` and `release()` functions for a mutex lock using the `test_and_set()` and `compare_and_swap()` instructions.                                     |

### Chapter 6: CPU Scheduling

(Topics: 6.1 Basic Concepts, 6.2 Scheduling Criteria, 6.3 Scheduling Algorithms)

| Question | Type     | Summary                                                                                                                                                                                           |
| :------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **6.1**  | Practice | Given $n$ processes to be scheduled on one processor, how many different schedules are possible?.                                                                                                 |
| **6.2**  | Practice | Explain the difference between preemptive and nonpreemptive scheduling.                                                                                                                           |
| **6.3**  | Practice | Scheduling problem: determine Gantt charts and average waiting time for FCFS, nonpreemptive SJF, and nonpreemptive priority algorithms.                                                           |
| **6.4**  | Practice | What advantage is there in having different time-quantum sizes at different levels of a multilevel queueing system?.                                                                              |
| **6.5**  | Practice | What relation holds between the following pairs of algorithm sets: Priority and SJF; Multilevel feedback queues and FCFS; Priority and FCFS; RR and SJF?                                          |
| **6.6**  | Practice | Explain why a scheduler favoring processes that have used the least processor time favors I/O-bound programs but not permanently starve CPU-bound programs.                                       |
| **6.10** | Exercise | Why is it important for the scheduler to distinguish I/O-bound programs from CPU-bound programs?.                                                                                                 |
| **6.11** | Exercise | Discuss how the following pairs of scheduling criteria conflict: CPU utilization and response time; Average turnaround time and maximum waiting time; I/O device utilization and CPU utilization. |
| **6.14** | Exercise | What are the implications of assigning different values to the parameters used by the exponential average formula for predicting the length of the next CPU burst?.                               |
| **6.16** | Exercise | Scheduling problem: draw Gantt charts, find turnaround time, waiting time, and minimum average waiting time for FCFS, SJF (NP), nonpreemptive priority, and RR (quantum = 2).                     |
| **6.19** | Exercise | Which of the following scheduling algorithms could result in starvation: FCFS, SJF, Round robin, Priority?                                                                                        |
| **6.20** | Exercise | Consider a variant of the RR scheduling algorithm where entries are pointers to PCBs. Discuss the effects, advantages, disadvantages, and alternative implementation.                             |
| **6.21** | Exercise | Describe the CPU utilization for a round-robin scheduler given I/O-bound and CPU-bound tasks, context switching overhead, and time quanta of 1ms and 10ms.                                        |
| **6.22** | Exercise | Consider a system implementing multilevel queue scheduling. What strategy can a computer user employ to maximize the amount of CPU time allocated to the user’s process?.                         |
| **6.24** | Exercise | Explain the differences in how much FCFS, RR, and Multilevel Feedback Queues discriminate in favor of short processes.                                                                            |

### Chapter 7: Deadlocks

(Topics: 7.1 System Model, 7.2 Deadlock Characterization, 7.3 Methods for Handling Deadlocks)

| Question | Type     | Summary                                                                                                                                                                     |
| :------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **7.1**  | Practice | List three examples of deadlocks that are not related to a computer-system environment.                                                                                     |
| **7.4**  | Practice | Compare the containment deadlock prevention scheme (using a single high-order lock) with the circular-wait scheme of Section 7.4.4.                                         |
| **7.5**  | Practice | What are the arguments for and against installing the deadlock-avoidance algorithm?.                                                                                        |
| **7.10** | Exercise | Is it possible to have a deadlock involving only one single-threaded process?.                                                                                              |
| **7.11** | Exercise | Show that the four necessary conditions for deadlock hold in the traffic deadlock depicted in Figure 7.10, and state a simple avoidance rule.                               |
| **7.12** | Exercise | Assume a multithreaded application uses only reader–writer locks for synchronization. Is deadlock still possible if multiple reader–writer locks are used?.                 |
| **7.15** | Exercise | Compare the circular-wait scheme with the various deadlock-avoidance schemes with respect to the following issues: Runtime overhead, System throughput, Programming effort. |
| **7.17** | Exercise | Show that a system consisting of four resources of the same type shared by three processes, each needing at most two resources, is deadlock free.                           |