### 10.1 Overview of Mass-Storage Structure

Mass-storage structure primarily describes secondary and tertiary storage devices. Modern computer systems rely on disks as the **primary online storage medium** for programs and data. The file system mechanism provides **online storage of and access** to data and programs residing on these disks.

#### 10.1.1 Magnetic Disks (Contextual Information)

**Magnetic disks** provide the bulk of secondary storage for modern computer systems.

- A disk platter is circular and covered with magnetic material for recording information.
- A **read-write head** moves above the surface, attached to a disk arm.
- The surface is logically divided into **circular tracks**, which are further subdivided into **sectors**.
- A **cylinder** is the set of tracks found at one specific arm position across all platters.
- Disks are attached to a computer via an **I/O bus** (e.g., ATA, SATA, USB, fibre channel).
- Data transfers are managed by **controllers**; the **host controller** is at the computer end, and a **disk controller** is built into the drive. Disk controllers usually include a built-in cache.
- **Solid-state disks (SSDs)** are magnetic disk alternatives that use flash memory and are growing in importance. In the storage hierarchy, the levels above the solid-state disk are volatile, whereas the SSD and below are nonvolatile.

#### 10.1.2 Magnetic Tapes and Other Storage

Although not explicitly numbered in the detailed TOC snippet, magnetic tapes are discussed immediately following disk structure:

- **Magnetic tapes** are used mainly for **backup**, storage of infrequently accessed information, and transferring data between systems.
- Accessing the correct spot on a tape can take minutes, but once positioned, tape drives can write data at speeds comparable to disk drives.
- Tape capacities can exceed several terabytes.
- Tapes and optical platters are typical **tertiary storage** devices, providing storage that is slower and lower in cost than secondary storage.

### 10.2 Disk Structure

- Magnetic disk drives are addressed as **large one-dimensional arrays of logical blocks**.
- The **logical block** is the smallest unit of transfer, typically 512 bytes, although some disks can be formatted for 1,024 bytes.
- Logical blocks are mapped sequentially onto the physical sectors of the disk.
- **Sector 0** is the first sector of the first track on the outermost cylinder.
- The mapping proceeds inward: through all sectors on a track, then through the rest of the tracks in that cylinder, and then moving to the next cylinder (from outermost to innermost).

### 10.3 Disk Attachment

Computers access disk storage in two primary ways:

1. **Host-Attached Storage:** Accessed through local I/O ports, common on small systems. Technologies include IDE, ATA, and SATA.
2. **Network-Attached Storage (NAS):** Accessed via a remote host in a distributed file system.

#### Network-Attached Storage (NAS)

- **NAS** provides a convenient mechanism for all computers on a Local Area Network (LAN) to share a pool of storage easily.
- It generally offers lower performance compared to direct-attached options.
- **iSCSI** is a network-attached storage protocol that uses the IP protocol to carry the SCSI protocol, enabling hosts to treat distant storage as if it were directly attached.

#### (Related to 10.3.6) Storage-Area Networks (SANs)

- A **SAN** is a private network connecting storage devices and servers.
- SANs are utilized to achieve low **access time** and large **disk bandwidth**.
- **Access time** components include **seek time** (arm movement to the cylinder) and **rotational latency** (rotation for the desired sector to reach the head).
- **Disk bandwidth** is the total bytes transferred divided by the total time from the first request to the completion of the last transfer.

### 12.1 File-System Structure

File systems are highly structured, often implemented in a **layered design**.

|Layer Name|Functionality|Key Components|
|:--|:--|:--|
|**Application Programs**|User-level interaction.||
|**Logical File System**|Manages **metadata** and directory structure; provides a symbolic name interface. Responsible for **protection**. Maintains files via **File-Control Blocks (FCBs)** (or _inodes_ in UNIX).|Directory structure, FCBs (metadata), Protection.|
|**File-Organization Module**|Translates logical block addresses (0 through N) to **physical block addresses**. Manages allocation type and tracks locations. Includes the **free-space manager**.|Logical-to-Physical Block Mapping, Free-space Manager.|
|**Basic File System**|Issues generic commands (read/write physical blocks) to device drivers using numeric disk addresses (e.g., cylinder, track, sector). Manages memory buffers and caches.|Physical block transfer, Buffer/Cache management.|
|**I/O Control Level**|Transfers information between main memory and the disk system. **Device drivers** translate high-level commands into hardware-specific instructions.|Device drivers, Interrupt handlers.|
|**Devices**|Physical hardware.||

- **FCB/Inode:** A File-Control Block contains critical file information, including ownership, permissions, file size, timestamps, and pointers to file data blocks.
- **File System Types:** Operating systems support multiple file system types (e.g., Linux uses **ext3/ext4**; Windows uses **FAT, FAT32, and NTFS**; UNIX uses **UFS**).
- **In-Memory Structures**: The system uses several in-memory structures for management and performance:
    - **In-memory mount table** (for each mounted volume).
    - **System-wide open-file table** (contains copies of FCBs for open files).
    - **Per-process open-file table** (contains a pointer to the system-wide entry and tracking information like the current location/offset and access mode).
    - **Buffers** (hold file-system blocks read from or written to disk).
- **Virtual File System (VFS):** This layer abstracts file-system operations from specific implementations, allowing transparent access to different mounted file systems.

### 12.4 Allocation Methods

Three main methods are used to allocate disk space to files:

#### 12.4.1 Contiguous Allocation

- **Mechanism:** Each file occupies a **single, physically contiguous set of blocks**.
- **Directory Entry:** Stores the starting disk address and the length of the allocation.
- **Advantages:** Supports **both sequential and direct (random) access efficiently**. Requires minimal disk head movement for sequential access.
- **Disadvantages:** Suffers from **external fragmentation** (wasted space between allocations). Finding space for new files can be difficult.

#### 12.4.2 Linked Allocation

- **Mechanism:** Each file is a **linked list of disk blocks**, which can be scattered anywhere. Each block contains a pointer to the next block.
- **Directory Entry:** Stores the pointer to the first and last blocks.
- **Advantages:** Solves the external fragmentation problem.
- **Disadvantages:** Direct access is **inefficient** because finding the $i$th block requires reading $i$ blocks by following pointers. Space is lost to pointers within each block (internal fragmentation).
- **File-Allocation Table (FAT) Variation:** This improves efficiency by collecting all the pointers into a **FAT** located at the beginning of the volume. The directory entry points to the first block, and the FAT entries chain the blocks together. The FAT method simplifies free-block accounting.

#### 12.4.3 Indexed Allocation

- **Mechanism:** All pointers for a file are consolidated into an **index block**.
- **Directory Entry:** Stores the address of the index block.
- To access block $i$, the system reads the index block and uses the $i$th entry to find the corresponding physical block.
- **Advantages:** Supports **direct access** efficiently and prevents external fragmentation.
- **Disadvantages:** Requires overhead for the index block itself.

**Addressing Large Files in Indexed Allocation:**

- **Linked Scheme:** Multiple index blocks are linked together if one block is insufficient.
- **Multilevel Index:** A hierarchy of index blocks is created. A first-level index points to second-level index blocks, which in turn point to data blocks (e.g., two levels allows files up to 4 GB with 4 KB blocks).
- **Combined Scheme (UNIX Inode):** Used in UNIX-based systems, the file's **inode** (FCB) holds several pointers directly to data blocks (**direct blocks**) for small files. If the file is larger, it uses **single, double, and triple indirect blocks** to hold pointers to increasingly large amounts of data.