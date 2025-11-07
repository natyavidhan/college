#### 1.1 What Operating Systems Do

- **Practice Exercise 1.1**: What are the three main purposes of an operating system?
- **Practice Exercise 1.2**: We have stressed the need for an operating system to make efficient use of the computing hardware. When is it appropriate for the operating system to forsake this principle and to “waste” resources? Why is such a system not really wasteful?
- **Practice Exercise 1.4**: Keeping in mind the various definitions of operating system, consider whether the operating system should include applications such as web browsers and mail programs. Argue both that it should and that it should not, and support your answers.
- **Exercise 1.13**: The issue of resource utilization shows up in different forms in different types of operating systems. List what resources must be managed carefully in the following settings: a. Mainframe or minicomputer systems b. Workstations connected to servers c. Mobile computers.
- **Exercise 1.14**: Under what circumstances would a user be better off using a time-sharing system than a PC or a single-user workstation?
- **Exercise 1.15**: Describe the differences between symmetric and asymmetric multiprocessing. What are three advantages and one disadvantage of multiprocessor systems?

#### 1.4 Operating-System Structure

- There are no specific exercise questions that exclusively or primarily address "Operating-System Structure" (Chapter 1, Section 1.4) without significantly overlapping with other management or operational topics from Chapter 1. The syllabus mentions "Loadable Kernel Modules" under this section, but related programming exercises are found in Chapter 2, not Chapter 1.

#### 1.5 Operating-System Operations

- **Practice Exercise 1.5**: How does the distinction between kernel mode and user mode function as a rudimentary form of protection (security) system?
- **Practice Exercise 1.6**: Which of the following instructions should be privileged? a. Set value of timer. b. Read the clock. c. Clear memory. d. Issue a trap instruction. e. Turn off interrupts. f. Modify entries in device-status table. g. Switch from user to kernel mode. h. Access I/O device.
- **Practice Exercise 1.8**: Some CPUs provide for more than two modes of operation. What are two possible uses of these multiple modes?
- **Practice Exercise 1.9**: Timers could be used to compute the current time. Provide a short description of how this could be accomplished.
- **Exercise 1.12**: In a multiprogramming and time-sharing environment, several users share the system simultaneously. This situation can result in various security problems. a. What are two such problems? b. Can we ensure the same degree of security in a time-shared machine as in a dedicated machine? Explain your answer.
- **Exercise 1.19**: What is the purpose of interrupts? How does an interrupt differ from a trap? Can traps be generated intentionally by a user program? If so, for what purpose?
- **Exercise 1.21**: Some computer systems do not provide a privileged mode of operation in hardware. Is it possible to construct a secure operating system for these computer systems? Give arguments both that it is and that it is not possible.

#### 1.6 Process Management

- There are no specific exercise questions from Chapter 1 that solely focus on "Process Management" (Chapter 1, Section 1.6). The overview of process management in Chapter 1 is foundational, with detailed discussions and specific exercises typically found in Chapter 3.

#### 1.7 Memory Management

- **Practice Exercise 1.7**: Some early computers protected the operating system by placing it in a memory partition that could not be modified by either the user job or the operating system itself. Describe two difficulties that you think could arise with such a scheme.
- **Exercise 1.25**: Describe a mechanism for enforcing memory protection in order to prevent a program from modifying the memory associated with other programs.

#### 1.8 Storage Management

- **Practice Exercise 1.10**: Give two reasons why caches are useful. What problems do they solve? What problems do they cause? If a cache can be made as large as the device for which it is caching (for instance, a cache as large as a disk), why not make it that large and eliminate the device?
- **Exercise 1.20**: Direct memory access is used for high-speed I/O devices in order to avoid increasing the CPU’s execution load. a. How does the CPU interface with the device to coordinate the transfer? b. How does the CPU know when the memory operations are com-plete? c. The CPU is allowed to execute other programs while the DMA controller is transferring data. Does this process interfere with the execution of the user programs? If so, describe what forms of interference are caused.
- **Exercise 1.22**: Many SMP systems have different levels of caches; one level is local to each processing core, and another level is shared among all processing cores. Why are caching systems designed this way?
- **Exercise 1.23**: Consider an SMP system similar to the one shown in Figure 1.6. Illustrate with an example how data residing in memory could in fact have a different value in each of the local caches.
- **Exercise 1.24**: Discuss, with examples, how the problem of maintaining coherence of cached data manifests itself in the following processing environments: a. Single-processor systems b. Multiprocessor systems c. Distributed systems.