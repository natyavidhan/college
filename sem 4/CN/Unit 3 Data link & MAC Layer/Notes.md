### **1. Data Link Layer Services**

The data link layer is responsible for the node-to-node delivery of data across a single communication link. To achieve this, it provides several core services to the network layer:

- **Framing**: The data link layer takes packets (datagrams) received from the network layer and encapsulates them into frames. A frame is constructed by adding a header (containing the source and destination link-layer MAC addresses) and a trailer (containing error detection information) to the packet. Common framing techniques include byte count, byte stuffing (adding escape characters to distinguish data from flags), and bit stuffing (inserting artificial bits to prevent accidental flag patterns in the payload).
- **Error Control**: Ensures the integrity of the data being transmitted over a physical link. Due to noise and interference, frames can be corrupted or lost. Error control involves detecting these errors (usually via a checksum or CRC in the trailer) and requesting retransmission of damaged frames.
- **Flow Control**: Regulates the pace of data transmission. It ensures that a fast-sending node does not transmit frames faster than a slow-receiving node can process them, which prevents buffer overflows at the receiver.
- **Connection Services**: The data link layer can provide varying levels of reliability, ranging from _unacknowledged connectionless service_ (like standard Ethernet, where no connection is established and lost frames are not recovered at this layer) to _acknowledged connection-oriented service_ (where a logical connection is made and delivery is strictly guaranteed).

### **2. Error Detection and Correction Techniques**

Transmission errors are inevitable over physical channels due to noise, signal attenuation, and interference. Errors can be classified as **Single-Bit Errors** (only one bit changes), **Multiple-Bit Errors**, or **Burst Errors** (where multiple consecutive bits are corrupted). To manage this, redundant bits are added to the data.

- **Error-Correcting Codes (Forward Error Correction - FEC)**: These codes include enough redundant information to allow the receiver to pinpoint the exact location of an error and correct it without needing a retransmission.
    - **Hamming Code**: A prominent linear block error-correcting code. Redundant check bits are inserted into the data at positions that are powers of 2 (bits 1, 2, 4, 8, etc.). Each check bit calculates the parity (even or odd) for a specific sequence of bits. If a single-bit error occurs, the combination of incorrect check results (called the syndrome) mathematically points to the exact index of the corrupted bit, allowing the receiver to flip it back.
- **Error-Detecting Codes**: These codes include just enough redundancy for the receiver to realize an error occurred. The receiver then discards the frame and requests a retransmission.
    - **Parity Bit**: A single bit appended to a data block so that the total number of 1s becomes even (or odd). It easily detects isolated single-bit errors. By interleaving parity bits across columns of data, burst errors can also be detected.
    - **Checksum**: The sender divides the data into fixed-size segments, adds them together, and appends the complement of the sum to the message. The receiver performs the same addition; if the final result is zero, the data is accepted.
    - **Cyclic Redundancy Check (CRC)**: A highly robust polynomial code used heavily in data link protocols. The sender and receiver agree on a generator polynomial $G(x)$. The sender appends a specific sequence of bits to the data so that the resulting string is perfectly divisible by $G(x)$ using binary division. The receiver divides the incoming frame by $G(x)$; any non-zero remainder definitively indicates a transmission error.

### **3. Error Recovery Protocols (Flow and Error Control)**

To provide reliable, sequential delivery, the data link layer uses Automatic Repeat reQuest (ARQ) protocols. These rely on sequence numbers, acknowledgements (ACKs), and timers.

- **Stop-and-Wait Protocol**: The simplest ARQ protocol. The sender transmits a single frame and starts a timer. It must wait for an ACK from the receiver before sending the next frame. If the frame is lost, or the ACK is lost, the timer expires and the sender retransmits the frame. To prevent the receiver from processing a delayed duplicate frame as a new one, frames and ACKs are tagged with alternating sequence numbers (0 and 1).
- **Go-Back-N (GBN) Protocol**: To improve the bandwidth efficiency over long distances, GBN uses a "sliding window" that allows the sender to transmit multiple frames (pipelining) before requiring an ACK. The receiver's window size is exactly 1, meaning it will _only_ accept frames in strictly correct order. If a frame is corrupted or lost, the receiver discards all subsequent frames. When the sender's timer for the lost frame expires, it "goes back" and retransmits the lost frame along with every frame sent after it.
- **Selective Repeat Protocol**: Designed to save bandwidth wasted by GBN's aggressive retransmissions. Both the sender and receiver maintain a sliding window of equal size. The receiver is capable of accepting and buffering out-of-order frames as long as they fall within its window. If a frame is lost, the sender's timeout will trigger the retransmission of _only_ that specific lost frame, rather than the entire pipeline.

### **4. Multiple Access Protocols with Collision Detection**

In broadcast networks (like local area networks), multiple devices share a single communication link. If two nodes transmit at exactly the same time, their signals collide and the data is garbled. MAC protocols establish the rules for channel access.

- **Carrier Sense Multiple Access (CSMA)**: To reduce collisions, a station "listens" (senses the carrier) to the medium before it attempts to send data. If the channel is busy, it defers. However, collisions can still occur if two distant stations sense an idle channel and transmit simultaneously due to propagation delay.
- **CSMA/CD (Carrier Sense Multiple Access with Collision Detection)**: Used in classic Ethernet. Stations do not just listen before transmitting; they monitor the energy level of the channel _while_ they are transmitting. If the hardware detects an abnormal energy level (a collision), the station immediately aborts transmission, sends a short "jam signal" to ensure all other stations are aware of the collision, and then waits a random amount of time (using a binary exponential backoff algorithm) before trying again.

### **5. MAC Addressing and Ethernet**

- **MAC Addressing**: To deliver frames to the correct node on a shared physical link, the data link layer uses link-layer addresses, commonly called MAC addresses.
    - An Ethernet MAC address is 48 bits (6 bytes) long, represented as 12 hexadecimal digits separated by colons (e.g., 47:20:1B:2E:08:EE).
    - Addresses are categorized into three types: **Unicast** (sent to a specific node, indicated by a 0 in the least significant bit of the first byte), **Multicast** (sent to a designated group of nodes, indicated by a 1), and **Broadcast** (sent to all nodes on the network, represented by all 1s: FF:FF:FF:FF:FF:FF).
- **Ethernet (IEEE 802.3)**: The dominant wired LAN technology.
    - **Frame Format**: A standard Ethernet frame begins with an 8-byte Preamble to allow receivers to synchronize their clocks. This is followed by a 6-byte Destination MAC Address, a 6-byte Source MAC Address, a 2-byte Type/Length field (to identify the encapsulated network-layer protocol, like IPv4), the Data payload (which must be between 46 and 1500 bytes), and a 4-byte CRC checksum for error detection.
    - **Frame Constraints**: Ethernet mandates a minimum frame length of 64 bytes (512 bits). If the actual data is smaller than 46 bytes, artificial "padding" is added. This minimum size restriction is critical; it ensures that a transmitting station is still sending data by the time a potential collision signal propagates back to it, allowing the CSMA/CD mechanism to function properly.