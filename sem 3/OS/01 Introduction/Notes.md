### Unit 1: Introduction (Chapter 1.1, 1.4, 1.5, 1.6, 1.7, 1.8)

#### 1.1 What Operating Systems Do

- **Definition and Role**: An **operating system (OS)** is a program that **manages a computer's hardware**, provides a **basis for application programs**, and acts as an **intermediary between the user and the hardware**. It controls the hardware and coordinates its use among various application programs and users. The OS also functions as a **control program**, managing the execution of user programs to prevent errors and improper use, with a particular focus on I/O devices.
- **Components of a Computer System**: A computer system is broadly divided into four components: the **hardware**, the **operating system**, **application programs**, and **users**.
- **Diversity of Operating Systems**: OS designs vary widely depending on their purpose. For instance, mainframe operating systems prioritize hardware utilization, while personal computer (PC) operating systems support diverse applications, and mobile operating systems focus on user-computer interaction.
- **The Kernel**: The **kernel** is often considered the core of the operating system, defined as **"the one program running at all times on the computer"**. Other programs are either system programs (associated with the OS but not part of the kernel) or application programs.

#### 1.4 Operating-System Structure

- **Modular Design**: Due to their large and complex nature, modern operating systems are carefully engineered and often partitioned into **small, well-defined components or modules**. Each module has clearly defined inputs, outputs, and functions.
- **Monolithic Structure**: Traditional UNIX, Linux, and Windows operating systems often follow a **monolithic structure**, where the entire kernel code and data structures reside in a **single address space**. This design prioritizes performance by minimizing context switches and enabling direct C function calls between subsystems. Key functions like the file system, CPU scheduling, and memory management are provided through system calls within this kernel.
- **Hybrid Systems**: In practice, most operating systems are **hybrid systems**, combining different structures to balance performance, security, and usability. For example, Linux and Solaris are monolithic for efficiency but modular to allow dynamic addition of new functionality. Windows also largely monolithic, incorporates features of microkernel systems, and supports dynamically loadable kernel modules.
- **Loadable Kernel Modules**: This methodology allows the kernel to **load and unload arbitrary sections of code on demand** during runtime or boot time. These modules run in privileged kernel mode and have full access to hardware. They are used to implement device drivers, file systems, and networking protocols, offering flexibility by avoiding kernel recompilation for every change. Linux maintains an internal symbol table of explicitly exported symbols, which modules can reference to interact with the kernel.

#### 1.5 Operating-System Operations

- **Interrupt-Driven Nature**: Modern operating systems are primarily **interrupt-driven**, meaning they wait for events to occur. These events are almost always signaled by an **interrupt (from hardware)** or a **trap (software-generated interrupt/exception)**.
- **Traps (Exceptions)**: These are software interrupts caused by errors (e.g., division by zero) or by user programs requesting operating system services through a **system call**.
- **Mode Bit**: A hardware feature called the **mode bit** distinguishes between **user mode (1)**, where user applications execute, and **kernel mode (0)** (also known as supervisor or privileged mode), where the operating system executes. When a user application requests OS service via a system call, the system transitions from user to kernel mode.
- **System Calls**: These provide the **interface to services made available by the operating system**. When a system call is executed, it's typically treated as a software interrupt, transferring control to a kernel service routine in kernel mode. The kernel verifies parameters, executes the request, and returns control to the user program. Programmers often use Application Programming Interfaces (APIs) like Windows API or POSIX API, which provide library functions that in turn invoke the necessary system calls.
- **Timer**: To ensure the operating system maintains control over the CPU and prevents user programs from monopolizing it (e.g., in an infinite loop), a **timer** is used. It can be set to interrupt the computer after a specified period, typically implemented using a fixed-rate clock and a counter.

#### 1.6 Process Management

- **Process Concept**: A **process is a program in execution**. It is an **active entity**, unlike a program, which is a passive entity stored on disk. A process requires resources such as CPU time, memory, files, and I/O devices to accomplish its task.
- **Multithreading**: Modern operating systems have extended the process concept to allow a process to have **multiple threads of execution**, enabling it to perform more than one task concurrently. This is especially beneficial on multicore systems where threads can run in parallel. A single-threaded process has one program counter, while a multithreaded process has multiple program counters, one for each thread.
- **OS Activities in Process Management**: The operating system is responsible for:
    - **Creating and deleting processes**.
    - **Suspending and resuming processes**.
    - **Providing mechanisms for process synchronization** (coordination).
    - **Providing mechanisms for process communication**.

#### 1.7 Memory Management

- **Main Memory**: Main memory is crucial to computer system operation. It is a **large array of bytes**, each with its own address, and serves as a repository for quickly accessible data shared by the CPU and I/O devices. The CPU directly accesses instructions and data from main memory.
- **Importance of Management**: To improve **CPU utilization and response time**, general-purpose computers keep several programs in memory simultaneously, necessitating robust memory management.
- **Memory Management Schemes**: Various schemes exist, and their effectiveness depends on the situation and the **hardware design** of the system, as each algorithm often requires specific hardware support.
- **OS Activities in Memory Management**: The operating system is responsible for:
    - **Keeping track of memory usage**: which parts are used and by whom.
    - **Deciding which processes/data to move into and out of memory**.
    - **Allocating and deallocating memory space** as needed.

#### 1.8 Storage Management

- **File System Concept**: The operating system provides a **uniform, logical view of information storage** by abstracting physical storage devices into a **file**. Files are then mapped onto physical media.
- **File-System Management**: The OS manages files and directories. This includes:
    - **Creating and deleting files and directories**.
    - **Supporting primitives for manipulating files and directories**.
    - **Mapping files onto secondary storage**.
    - **Backing up files on stable (nonvolatile) storage media**.
- **Mass-Storage Management**: As main memory is volatile and limited, **secondary storage (primarily disks)** is essential for permanent storage of programs and data. The operating system is responsible for managing disk storage, including free space management, storage allocation, and disk scheduling. SSDs (Solid-State Disks) are also becoming increasingly important in this context.
- **Caching**: Caching is a fundamental principle where frequently used information is **copied into a faster storage system (cache)** for temporary, quicker access. Cache management, including size selection and replacement policies, is vital for performance. Main memory acts as a fast cache for secondary storage.
- **I/O Systems**: The **I/O subsystem** is a critical component of the OS that abstracts and hides the peculiarities of specific hardware devices from the user and the rest of the OS. It comprises buffering, caching, spooling, a general device-driver interface, and drivers for specific hardware.