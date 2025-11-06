### 2.1 Operating-System Services

An operating system provides an environment for program execution and offers certain services to programs and their users. These services are provided for the convenience of the programmer, making the programming task easier.

Operating system services can be viewed as falling into two main categories: functions helpful to the user and functions ensuring the efficient operation of the system itself.

#### Services Helpful to the User:

- **User Interface (UI):** Almost all operating systems have a UI. This interface can take several forms:
    - **Command-Line Interface (CLI):** Uses text commands and a method for entering them.
    - **Batch Interface:** Commands and directives are entered into files for execution.
    - **Graphical User Interface (GUI):** Most commonly used, featuring a window system, a pointing device, menus, and icons.
- **Program Execution:** The system must be able to load a program into memory and run it. The program must be able to end execution, either normally or abnormally (indicating an error).
- **I/O Operations:** Running programs often require I/O. Since users usually cannot directly control I/O devices (for efficiency and protection), the operating system must provide a means to perform I/O.
- **File-System Manipulation:** Programs require functionality to read and write files and directories, create and delete them by name, search for files, and list file information. Many OSs also include **permissions management** to control access based on file ownership.
- **Communications:** Processes often need to exchange information, either on the same computer or across networked systems. Communication can be implemented via:
    - **Shared memory:** Processes read and write to a shared memory section.
    - **Message passing:** Packets of information are moved between processes by the operating system.

#### Services Ensuring Efficient System Operation:

- **Resource Allocation:** When multiple users or jobs are running concurrently, resources must be allocated to each. The operating system manages allocation for resources such as CPU cycles, main memory, file storage, and I/O devices, often using CPU-scheduling routines.
- **Accounting:** Tracks resource usage (CPU time, mass storage used, etc.) to keep statistics or for billing purposes.
- **Error Detection:** The OS must constantly detect errors in the hardware (CPU, memory, I/O devices) and software (e.g., application errors, data inconsistency) and take appropriate action to ensure correct and consistent computing.
- **Protection and Security:** Ensuring that all access to system resources is controlled. This includes protecting the integrity of the system and defending external I/O devices (like network adapters) from invalid access attempts.

### 2.3 System Calls

System calls serve as the **interface to the services** made available by the operating system. They are generally available as routines written in C and C++, though some low-level tasks accessing hardware may use assembly language.

#### Application Programming Interface (API)

Most application developers design programs based on an **API**, which specifies a set of functions, the parameters passed to them, and the expected return values.

- Programmers access the API via a **library of code** provided by the operating system (e.g., `libc` for C programs on UNIX/Linux).
- The three most common APIs are the **Windows API**, the **POSIX API** (for UNIX, Linux, and Mac OS X systems), and the **Java API**.
- When a user application invokes a function in the API, the library routine handles the transition to **kernel mode** and executes the corresponding system call.
- The details of the system-call implementation are hidden from the programmer by the API and managed by the run-time support library.

#### Passing Parameters to the Operating System

Three general methods are used to pass parameters when a system call is invoked:

1. **Passing in Registers:** The simplest approach, but limited by the number of available registers.
2. **Passing as a Block/Table in Memory:** Parameters are stored in a block in memory, and the **address of the block** is passed in a register. This approach is used by Linux and Solaris.
3. **Pushing onto the Stack:** Parameters are placed onto the stack by the program and popped off by the OS. This method does not limit the number or length of parameters being passed.

### 2.4 Types of System Calls

System calls are roughly organized into six major categories:

1. **Process Control**
    - Includes calls to `end` or `abort` a program, or to `load` and `execute` another program.
    - Allows for process creation/termination, setting/getting process attributes, waiting for time/events, signaling events, and memory allocation/deallocation.
    - System calls like `acquire lock()` and `release lock()` are often provided to ensure data integrity when multiple processes share data.
2. **File Management**
    - Basic calls include `create()`, `delete()`, `open()`, `close()`, `read()`, `write()`, and `reposition()`.
    - Also includes methods to determine and reset file attributes using `get file attributes()` and `set file attributes()`. These operations are also typically available for directories.
3. **Device Management**
    - In systems with multiple users, a process may need to `request()` and `release()` a device for exclusive use.
    - Devices support `read()`, `write()`, and possibly `reposition()` operations.
    - Many OSs (like UNIX) integrate I/O devices and files into a single file–device structure.
4. **Information Maintenance**
    - Used for transferring information between the user program and the operating system, such as returning the current `time()` or date.
    - Can also return system-level statistics (e.g., OS version, free memory, user count).
    - Includes tools for debugging, such as system calls to `dump()` memory or trace program execution (e.g., single-step CPU mode).
5. **Communications**
    - Involves two common models:
        - **Message-Passing Model:** Processes exchange messages, requiring connection management (`open connection()`, `close connection()`), process identification (`get processid()`), and message transfer (`read message()`, `write message()`).
        - **Shared-Memory Model:** Processes use `shared memory create()` and `shared memory attach()` calls to gain access to regions of memory owned by other processes, thus bypassing memory protection restrictions. Processes must handle synchronization themselves.
6. **Protection**
    - Mechanisms for controlling access to system resources, ensuring integrity and authorization.

### 2.5 System Programs

System programs (or system utilities) reside above the operating system in the logical computer hierarchy and provide a convenient environment for program development and execution. Some act as simple user interfaces to system calls, while others are more complex.

Categories of System Programs include:

- **File Management:** Utilities for creating, deleting, copying, renaming, listing, and manipulating files and directories.
- **Status Information:** Programs that ask the system for status details (date, time, memory/disk space, etc.). Some use an internal database called a **registry** to store configuration information.
- **File Modification:** Text editors and commands to search or transform the contents of files.
- **Programming-Language Support:** Compilers, assemblers, debuggers, and interpreters.
- **Program Loading and Execution:** Programs like loaders, linkage editors, and debugging systems.
- **Communications:** Tools for remote login, file transfer, web browsing, and message sending.
- **Background Services (Daemons):** Processes that run continuously after booting until the system is halted, handling specialized tasks such as network connections or print spooling.

The **user's view** of the operating system is primarily shaped by these application and system programs, rather than the raw system calls.

### 2.7 Operating-System Structure

A modern operating system is a large and complex system that must be carefully engineered, often by partitioning the task into small components or **modules**.

#### Simple Structure (Monolithic)

- Many early systems (like the original **MS-DOS**) lacked a well-defined structure, often growing beyond their initial simple scope. In MS-DOS, interfaces were not well separated, and applications could directly access I/O routines, making the system vulnerable to crashes.
- **Traditional UNIX** also used a simple structure, consisting of the kernel and system programs. Everything below the system-call interface (file system, CPU scheduling, memory management) was part of the monolithic kernel. This structure offered performance advantages due to minimal overhead but was difficult to maintain.

#### Layered Approach

- The OS is broken into a hierarchy of layers (levels), where **Layer 0 is the hardware** and the **highest Layer N is the user interface**.
- A layer relies only on the functions and data of lower-level layers.
- _Advantage:_ Simplicity in construction and debugging, as components are isolated.
- _Disadvantage:_ Defining the layers can be difficult, as components sometimes rely mutually on each other (e.g., CPU scheduler and backing-store driver).

#### Microkernel Approach

- This approach removes all non-essential components from the kernel and implements them as system and user-level programs (e.g., **Mach** kernel, part of Mac OS X).
- The microkernel's primary role is to provide **communication** (via **message passing**) between client programs and user-space services.
- _Benefits:_ Easier to extend (new services added to user space), easier to port to new hardware, and enhanced security and reliability since service failures do not crash the smaller kernel.

#### Hybrid Systems

- In practice, few operating systems use a single, strict structure; instead, they combine different structures to address performance, security, and usability.
- **Linux and Solaris** are largely monolithic (for efficient performance) but are also modular (allowing dynamic addition of features).
- **Mac OS X** is a layered hybrid system. The kernel environment consists of the **Mach microkernel** (handling memory management, IPC, and thread scheduling) and the **BSD UNIX kernel** (providing the command-line interface, networking, file systems, and POSIX APIs).

### 2.7.4 Modules

The methodology involving **loadable kernel modules** is considered the best current approach for operating-system design.

- The kernel maintains a set of core components and links in additional services dynamically, either at boot time or during run time.
- This approach is common in modern operating systems, including Linux, Solaris, and Windows.
- Modules are dynamically linked, which is preferable to adding new features directly to the kernel, thus avoiding recompilation for every change.
- The result resembles a layered system due to defined, protected interfaces, but it is more flexible because any module can call any other module.
- It is also more efficient than the microkernel approach, as modules do not require message passing for communication.
- **Solaris** uses a core kernel structure supporting seven types of loadable modules, including scheduling classes, file systems, loadable system calls, and device drivers.
- **Linux** primarily uses loadable kernel modules to support device drivers and file systems.

|Structure Type|Core Concept|Example(s)|Key Feature(s)|
|:--|:--|:--|:--|
|**Simple/Monolithic**|Large kernel containing all functionality below the system-call interface.|MS-DOS, Traditional UNIX|High performance (low overhead); difficult maintenance/debugging.|
|**Layered**|OS divided into levels, with each layer using services only from lower layers.|Early research OSs|Simplified debugging; hard to define dependencies correctly.|
|**Microkernel**|Essential functions remain in kernel; non-essential services run as user-space processes.|Mach|Increased extensibility, portability, reliability; performance penalty due to message passing.|
|**Modules**|Core kernel links services dynamically during runtime.|Linux, Solaris, Windows|Flexibility (any module calls any other); efficient communication (no message passing).|