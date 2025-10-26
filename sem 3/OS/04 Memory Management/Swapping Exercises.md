### 8.1.3 Logical Versus Physical Address Space

- **Practice Exercise 8.1:** Name two differences between logical and physical addresses.

### 8.2 Swapping

- **Exercise 8.15:** Explain why mobile operating systems such as iOS and Android do not support swapping.
- **Exercise 8.16:** Although Android does not support swapping on its boot disk, it is possible to set up a swap space using a separate SD nonvolatile memory card. Why would Android disallow swapping on its boot disk yet allow it on a secondary disk?.

### 8.3 Contiguous Memory Allocation

- **Exercise 8.9:** Explain the difference between internal and external fragmentation.
- **Exercise 8.11:** Given six memory partitions of 300 KB, 600 KB, 350 KB, 200 KB, 750 KB, and 125 KB (in order), how would the first-fit, best-fit, and worst-fit algorithms place processes of size 115 KB, 500 KB, 358 KB, 200 KB, and 375 KB (in order)? Rank the algorithms in terms of how efficiently they use memory.
- **Exercise 8.12a:** What is required to support dynamic memory allocation in Contiguous memory allocation?
- **Exercise 8.13:** Compare the memory organization schemes of contiguous memory allocation, pure segmentation, and pure paging with respect to the following issues: a. External fragmentation b. Internal fragmentation c. Ability to share code across processes.

### 8.4 Segmentation

- **Practice Exercise 8.6:** Describe a mechanism by which one segment could belong to the address space of two different processes.
- **Practice Exercise 8.7a:** Define a system that allows static linking and sharing of segments without requiring that the segment numbers be the same.
- **Exercise 8.12b:** What is required to support dynamic memory allocation in Pure segmentation?
- **Exercise 8.13:** Compare the memory organization schemes of contiguous memory allocation, pure segmentation, and pure paging with respect to the following issues: a. External fragmentation b. Internal fragmentation c. Ability to share code across processes.
- **Exercise 8.27:** Explain why sharing a reentrant module is easier when segmentation is used than when pure paging is used.
- **Exercise 8.28:** Consider the following segment table: [Segment table entries] What are the physical addresses for the following logical addresses? a. 0,430 b. 1,10 c. 2,500 d. 3,400 e. 4,112.

### 8.5–8.5.2 Paging (Basic Method and Hardware Support)

- **Practice Exercise 8.3:** Why are page sizes always powers of 2?.
- **Practice Exercise 8.4:** Consider a logical address space of 64 pages of 1,024 words each, mapped onto a physical memory of 32 frames. a. How many bits are there in the logical address? b. How many bits are there in the physical address?.
- **Practice Exercise 8.5:** What is the effect of allowing two entries in a page table to point to the same page frame in memory? Explain how this effect could be used to decrease the amount of time needed to copy a large amount of memory from one place to another. What effect would updating some byte on the one page have on the other page?.
- **Practice Exercise 8.7b:** Describe a paging scheme that allows pages to be shared without requiring that the page numbers be the same.
- **Exercise 8.12c:** What is required to support dynamic memory allocation in Pure paging?
- **Exercise 8.13:** Compare the memory organization schemes of contiguous memory allocation, pure segmentation, and pure paging with respect to the following issues: a. External fragmentation b. Internal fragmentation c. Ability to share code across processes.
- **Exercise 8.14:** On a system with paging, a process cannot access memory that it does not own. Why? How could the operating system allow access to other memory? Why should it or should it not?.
- **Exercise 8.18:** Explain why address space identifiers (ASIDs) are used.
- **Exercise 8.20:** Assuming a 1-KB page size, what are the page numbers and offsets for the following address references (provided as decimal numbers): a. 3085 b. 42095 c. 215201 d. 650000 e. 2000001.
- **Exercise 8.21:** The BTV operating system has a 21-bit virtual address, yet on certain embedded devices, it has only a 16-bit physical address. It also has a 2-KB page size. How many entries are there in each of the following? a. A conventional, single-level page table b. An inverted page table.
- **Exercise 8.23:** Consider a logical address space of 256 pages with a 4-KB page size, mapped onto a physical memory of 64 frames. a. How many bits are required in the logical address? b. How many bits are required in the physical address?.
- **Exercise 8.25a:** If a memory reference takes 50 nanoseconds, how long does a paged memory reference take?.
- **Exercise 8.25b:** If we add TLBs, and 75 percent of all page-table references are found in the TLBs, what is the effective memory reference time? (Assume that finding a page-table entry in the TLBs takes 2 nanoseconds, if the entry is present.).