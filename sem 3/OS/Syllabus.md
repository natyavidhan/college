### Chapter 3: Processes

#### 3.1 Process Concept

A process is informally defined as a program in execution. It is the unit of work in a modern time-sharing system. A system consists of a collection of concurrently executing processes, which include operating-system processes (executing system code) and user processes (executing user code).

A program is a passive entity, such as a file stored on disk, whereas a process is an active entity. A process includes:

- **Text section:** The program code.
- **Current activity:** Represented by the program counter and processor registers.
- **Process stack:** Contains temporary data like function parameters, return addresses, and local variables.
- **Data section:** Contains global variables.
- **Heap:** Memory dynamically allocated during run time.

A process changes state as it executes. The five primary states are:

1. **New:** The process is being created.
2. **Running:** Instructions are being executed.
3. **Waiting:** The process is waiting for an event (e.g., I/O completion or signal reception).
4. **Ready:** The process is waiting to be assigned to a processor.
5. **Terminated:** The process has finished execution. It is important to note that only one process can be running on any single processor at any instant.

Each process is represented in the operating system by a **Process Control Block (PCB)**. The PCB serves as a repository for process-specific information, including:

- Process state.
- Program counter.
- CPU registers.
- CPU-scheduling information (e.g., process priority, pointers to scheduling queues).
- Memory-management information (e.g., base/limit registers, page tables).
- Accounting information (e.g., CPU time used, job numbers).
- I/O status information (e.g., list of open files, allocated I/O devices).

Most modern operating systems extend the process concept to allow for **multiple threads of execution**, enabling a process to perform more than one task at a time.

#### 3.2 Process Scheduling

The goal of multiprogramming is to maximize CPU utilization by having some process running at all times. The goal of time sharing is to switch the CPU among processes so frequently that users can interact with each running program. The **process scheduler** selects an available process for execution on the CPU.

Processes are organized into several **scheduling queues** throughout their lifetime:

- **Job queue:** Consists of all processes in the system.
- **Ready queue:** Contains processes residing in main memory that are ready and waiting to execute.
- **Device queues:** Lists of processes waiting for a specific I/O device.

Processes move through the system by transitioning between these queues. For example, a new process goes to the ready queue; once dispatched, it might issue an I/O request (moving to an I/O queue), create a child process (and wait for termination), or be forcibly removed by an interrupt (returning to the ready queue).

Three types of schedulers manage these queues:

- **Long-term scheduler (Job scheduler):** Selects processes from the job pool and loads them into memory. Infrequent execution.
- **Short-term scheduler (CPU scheduler):** Selects processes ready to execute in memory and allocates the CPU to one of them. Must be fast due to frequent execution (often every 100 milliseconds or less).
- **Medium-term scheduler:** Used in time-sharing systems for swapping (removing a process from memory to reduce the degree of multiprogramming, and later swapping it back in to continue execution).

A **context switch** occurs when the CPU is interrupted (or a system call is made), requiring the operating system to save the current context of the running process (state save) into its PCB and restore the saved context (state restore) of the process to be resumed.

#### 3.3 Operations on Processes (Excluding Figure 3.11)

Processes can be created and deleted dynamically. The creating process is the **parent process**, and the new processes are its **children**, forming a tree structure. Processes are identified by a unique **process identifier (pid)**, typically an integer. The initial parent process in UNIX/Linux systems is the `init` process (pid = 1), which serves as the root for all user processes.

When a process creates a new one, two possibilities exist for execution:

1. **Concurrent execution:** The parent continues to execute concurrently with its children.
2. **Waiting:** The parent waits until some or all of its children have terminated.

Two address-space possibilities exist for the new process:

1. The child process is a **duplicate** of the parent process (same program and data).
2. The child process has a **new program loaded** into it.

**Process Creation in UNIX:** The `fork()` system call creates a new process that is a copy of the parent's address space. Both parent and child execute starting from the instruction immediately following the `fork()` call. The return value of `fork()` is 0 for the child process and the non-zero pid of the child for the parent process. The `exec()` system call is typically used after `fork()` to replace the process's memory space with a new program. `exec()` loads a binary file and starts its execution, destroying the original memory image. The `exec()` call does not return control unless an error occurs. The parent process can use the `wait()` system call to block itself until the child terminates.

**Process Termination:** A process terminates by executing the `exit()` system call, releasing all its resources (memory, open files, I/O buffers) to the operating system. The process may return a status value to its parent via `wait()`. A parent can terminate a child using a system call (e.g., `TerminateProcess()` in Windows). Reasons for termination include the child exceeding allocated resources, the task no longer being required, or the parent exiting. **Cascading termination** occurs when a process terminates, and the operating system automatically terminates all its children. If a parent process terminates without invoking `wait()`, the children become **orphan processes**. In Linux and UNIX, the `init` process is assigned as the new parent for orphans and periodically invokes `wait()` to collect their exit status and deallocate their resources.

### Chapter 4: Threads

#### 4.1 Overview

A thread is the **basic unit of CPU utilization**. It consists of a thread ID, a program counter, a register set, and a stack. Threads belonging to the same process share the process’s code section, data section, and operating-system resources like open files and signals. A traditional (heavyweight) process has only a single thread of control.

Benefits of multithreading include:

- **Responsiveness:** Allows a program to continue running even if part of it is blocked or performing a lengthy operation.
- **Resource sharing:** Threads share memory and resources by default, which is easier and more efficient than using explicit interprocess communication mechanisms like shared memory or message passing.
- **Economy:** Creating and context-switching threads is generally significantly less time consuming and resource intensive than doing the same for processes (e.g., in Solaris, creating a process is about thirty times slower than creating a thread).
- **Scalability:** Threads can run in parallel on different processing cores in a multiprocessor architecture.

#### 4.2 Multicore Programming

Multicore or multiprocessor systems place multiple computing cores on a single chip or across CPU chips. Multithreaded programming is key to utilizing these multiple cores efficiently.

A distinction exists between **parallelism** and **concurrency**:

- **Concurrency:** Supports more than one task by allowing all tasks to make progress (e.g., interleaving execution on a single-core system).
- **Parallelism:** The ability to perform more than one task _simultaneously_ (e.g., assigning a separate thread to each core on a multicore system).

Challenges in designing multithreaded programs for multicore systems include:

- Identifying tasks suitable for concurrent execution.
- Ensuring balance, where tasks perform equal work of equal value.
- Splitting data accessed and manipulated by tasks.
- Managing data dependency between tasks, ensuring synchronized execution.
- Increased difficulty in testing and debugging concurrent programs due to many possible execution paths.

#### 4.3 Multithreading Models

Thread support can be provided at the user level (**user threads**) or by the kernel (**kernel threads**). Most contemporary operating systems (Windows, Linux, Mac OS X, Solaris) support kernel threads.

There are three common models establishing the relationship between user and kernel threads:

1. **Many-to-One Model:** Maps many user-level threads to a single kernel thread. Thread management is efficient because it occurs in user space. However, if one thread makes a blocking system call, the entire process blocks, and multiple threads cannot run in parallel on multicore systems.
2. **One-to-One Model:** Maps each user thread to a separate kernel thread. This provides more concurrency and allows threads to run in parallel on multiprocessors. Its drawback is the overhead associated with creating a kernel thread for every user thread, which can limit the number of threads supported. (Linux and Windows systems implement this model).
3. **Many-to-Many Model:** Multiplexes many user-level threads to a smaller or equal number of kernel threads. Developers can create as many user threads as needed, and the kernel threads can run in parallel. A blocking system call by one thread does not block the entire process.
    - A variation is the **Two-Level Model**, which allows binding a user-level thread to a kernel thread while retaining the multiplexing capabilities.

#### 4.4 Thread Libraries

A thread library provides programmers with an **API for creating and managing threads**. Thread libraries can be implemented in two ways:

1. **User space:** All code and data structures exist in user space, meaning function invocation results in a local function call, not a system call.
2. **Kernel level:** Code and data structures exist in kernel space, and function invocation typically results in a system call.

The three main thread libraries are POSIX Pthreads, Windows, and Java. Global data is shared among all threads in a process (in Pthreads and Windows), while local data (on the stack) is unique to each thread.

Thread creation strategies include:

- **Asynchronous threading:** The parent creates the child thread and immediately resumes execution; the parent and child execute concurrently and independently.
- **Synchronous threading:** The parent creates the child thread but waits for the child's termination (often using a `join()` operation).

#### 4.4.1 Pthreads

**Pthreads** refers to the POSIX standard (IEEE 1003.1c) defining an API for thread creation and synchronization. It is a specification, not an implementation, typically implemented on UNIX-type systems such as Linux, Mac OS X, and Solaris.

In Pthreads, thread creation is done using the `pthread_create()` function. The parent thread can wait for the child thread to complete execution by using the `pthread_join()` function.

### Chapter 5: Process Synchronization

#### 5.1 Background

Cooperating processes are those that can affect or be affected by other processes in the system. This cooperation often involves sharing a logical address space (threads) or sharing data via files or messages. **Concurrent access to shared data may lead to data inconsistency**. Process synchronization and coordination are necessary to ensure orderly execution and maintain data consistency.

#### 5.2 The Critical-Section Problem

A **critical section** is a segment of code where a process may be changing common variables, updating a table, or writing a file. The fundamental requirement is that **when one process is executing in its critical section, no other process is allowed to execute in its critical section**.

The critical-section problem requires a protocol involving an **entry section** (requesting permission to enter the CS) and an **exit section** (following the CS).

A solution to the critical-section problem must satisfy three requirements:

1. **Mutual exclusion:** If process $P_i$ is executing in its critical section, then no other processes can be executing in their critical sections.
2. **Progress:** If no process is executing in its CS and some processes want to enter, the selection of which process enters next cannot be postponed indefinitely.
3. **Bounded waiting:** There exists a limit on the number of times other processes can enter their CS after a process $P_i$ has requested entry and before that request is granted.

Kernel code is subject to race conditions on shared data structures (like lists of open files or memory allocation structures). Operating systems use two general approaches to handle critical sections:

- **Nonpreemptive kernels:** Do not allow a process running in kernel mode to be preempted. This approach is essentially free from race conditions on kernel data structures.
- **Preemptive kernels:** Allow a process to be preempted while running in kernel mode. These kernels must be carefully designed to ensure shared kernel data structures are free from race conditions.

#### 5.3 Peterson’s Solution

Peterson’s solution is a **software solution** to the critical-section problem, restricted to two processes ($P_0$ and $P_1$). It uses two shared variables: a boolean array `flag` (to indicate if a process is ready to enter the critical section) and an integer `turn` (to indicate whose turn it is to enter).

The structure of process $P_i$ (where $j$ is the other process, $1-i$) is: it sets `flag[i] = true` and sets `turn = j`. It then waits in a `while` loop until both `flag[j]` is false AND `turn != j`. Peterson's solution is proven to satisfy all three requirements for the critical-section problem: mutual exclusion, progress, and bounded waiting.

#### 5.8.4 Resuming Processes within a Monitor (Interpreting 5.3.4 as 5.8.4)

When multiple processes are suspended (waiting) on a **condition** ($x$) inside a monitor, and an $x.signal()$ operation is executed, the process that is resumed must be determined. A simple method is to use **First-Come, First-Served (FCFS) ordering**.

Alternatively, the **conditional-wait construct** can be used, having the form $x.wait(c)$, where $c$ is an integer priority number. This priority number is stored with the suspended process. When $x.signal()$ is executed, the process with the **smallest priority number** is resumed next.

### Chapter 6: CPU Scheduling

#### 6.1 Basic Concepts

CPU scheduling is central to operating-system design. Process execution is characterized by the **CPU–I/O Burst Cycle**, consisting of alternating periods of CPU execution (**CPU bursts**) and I/O wait (**I/O bursts**).

CPU-scheduling decisions can occur under four circumstances:

1. Process switches from _running_ to _waiting_ state (e.g., I/O request).
2. Process switches from _running_ to _ready_ state (e.g., interrupt occurs).
3. Process switches from _waiting_ to _ready_ state (e.g., I/O completion).
4. Process _terminates_.

**Nonpreemptive (Cooperative) scheduling** occurs only in circumstances 1 and 4: once the CPU is allocated, the process keeps it until it terminates or switches to the waiting state. **Preemptive scheduling** occurs when scheduling decisions happen in circumstances 2 or 3, allowing a running process to be interrupted.

#### 6.2 Scheduling Criteria

In evaluating scheduling algorithms, two key criteria are based on time spent by a process:

- **Turnaround time:** The total interval from process submission to completion. This includes time spent waiting to get into memory, waiting in the ready queue, executing on the CPU, and doing I/O.
- **Waiting time:** The cumulative time a process spends waiting specifically in the ready queue. The scheduling algorithm primarily affects this metric.

#### 6.3 Scheduling Algorithms

The CPU scheduler decides which process in the ready queue is allocated the CPU.

1. **First-Come, First-Served (FCFS) Scheduling:**
    
    - The simplest algorithm; the process requesting the CPU first is allocated the CPU first.
    - Implemented using a FIFO queue.
    - It is **nonpreemptive**.
    - Average waiting time is generally not minimal and can vary substantially if CPU burst times differ greatly.
2. **Shortest-Job-First (SJF) Scheduling:**
    
    - This algorithm is provably **optimal**, providing the minimum average waiting time.
    - Implementation is difficult because predicting the length of the next CPU burst is required.
    - Can be implemented as either preemptive (often called Shortest-Remaining-Time-First) or nonpreemptive.
3. **Priority Scheduling:**
    
    - The CPU is allocated to the process with the highest priority.
    - Priorities can be defined internally (e.g., based on time limits or memory requirements) or externally (e.g., based on system importance).
    - Can be preemptive (preempting the running process if a higher priority process arrives) or nonpreemptive.
    - Major problem: **indefinite blocking** or **starvation** (low-priority processes may wait indefinitely). **Aging** (gradually increasing the priority of processes that wait for a long time) is a technique to prevent starvation.
4. **Round-Robin (RR) Scheduling:**
    
    - Designed for time-sharing systems, adding preemption to FCFS.
    - Uses a small fixed unit of time called a **time quantum** (or time slice, typically 10 to 100 milliseconds).
    - The ready queue is treated as a circular FIFO queue.
    - If a process's CPU burst is longer than the quantum, it is preempted and put back at the tail of the ready queue; thus, RR is a **preemptive** algorithm.
5. **Multilevel Queue Scheduling:**
    
    - Partitions the ready queue into several separate queues, often based on process properties (e.g., foreground interactive processes vs. background batch processes).
    - Each queue typically has its own scheduling algorithm (e.g., RR for foreground, FCFS for background).
    - Scheduling between queues can use absolute priority or time-slicing (e.g., giving one queue a certain percentage of CPU time).
6. **Multilevel Feedback Queue Scheduling:**
    
    - Allows processes to **move between queues**, separating processes based on the characteristics of their CPU bursts.
    - If a process uses too much CPU time, it is moved to a lower-priority queue.
    - Aging (moving long-waiting processes to higher-priority queues) is used to prevent starvation.

### Chapter 7: Deadlocks

#### 7.1 System Model

A system manages a finite number of resources distributed among competing processes. Resources are grouped into **resource types** (or classes), each potentially having multiple identical instances (e.g., the resource type CPU may have two instances). Synchronization tools like mutex locks and semaphores are also considered system resources and are common sources of deadlock.

Under normal operation, a process must follow this sequence when utilizing a resource:

1. **Request:** The process requests the resource and waits if it is unavailable.
2. **Use:** The process operates on the resource.
3. **Release:** The process releases the resource.

System calls are typically used for resource requests and releases, such as `wait()` and `signal()` for semaphores or `acquire()` and `release()` for mutex locks.

#### 7.2 Deadlock Characterization

A **deadlock** occurs when a set of processes is in a state where every process in the set is waiting for an event (usually a resource acquisition or release) that can only be caused by another process in the set.

A deadlock can occur only if **all four** of the following necessary conditions hold simultaneously:

1. **Mutual Exclusion:** At least one resource must be nonsharable (cannot be simultaneously used by multiple processes).
2. **Hold and Wait:** A process must be holding at least one resource and simultaneously waiting to acquire additional resources held by other processes.
3. **No Preemption:** Resources cannot be preempted; a resource can be released only voluntarily by the process holding it, after that process has completed its task.
4. **Circular Wait:** A set of waiting processes must exist such that there is a circular dependency where $P_0$ waits for $P_1$, $P_1$ waits for $P_2$, ..., and $P_n$ waits for $P_0$.

The **Resource-Allocation Graph (RAG)** is a graphical tool used to characterize deadlocks. If a RAG contains **no cycle**, then the system is definitely not in a deadlocked state. If a RAG **contains a cycle**, the system _may or may not_ be in a deadlocked state.

#### 7.3 Methods for Handling Deadlocks

There are three principal strategies for dealing with the deadlock problem:

1. **Deadlock Prevention or Avoidance:** Use a protocol to ensure the system never enters a deadlocked state.
2. **Detection and Recovery:** Allow the system to enter a deadlocked state, detect it, and then recover from it.
3. **Ignoring the Problem:** Pretend that deadlocks never occur in the system. This is the approach used by most operating systems, including Linux and Windows.

**Deadlock prevention** provides methods to guarantee that at least one of the four necessary conditions cannot hold, typically by constraining how resource requests are made.

**Deadlock avoidance** requires providing the operating system with additional advance information about which resources a process will request during its lifetime. The system then dynamically examines the resource-allocation state to ensure a circular-wait condition can never exist.