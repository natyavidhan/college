### **1. Introduction to Computer Networks & Classifications**

A computer network is a set of interconnected computers and devices that communicate with each other to share resources and exchange information.

- **Key Characteristics:** A network must deliver data to the correct destination, accurately, in a timely manner, and with minimal jitter (variation in packet delay),-.
- **Network Taxonomy by Scale:**
    - **Personal Area Network (PAN):** A network covering a very short range (up to 10m), typically revolving around a single person (e.g., connecting a wireless mouse or Bluetooth headset),.
    - **Local Area Network (LAN):** Confined to a single building or campus (1km to 10km). LANs are privately owned, offer high speeds, and are inexpensive to design and maintain,.
    - **Metropolitan Area Network (MAN):** Covers an entire city (10km to 100km), such as a cable TV network,.
    - **Wide Area Network (WAN):** Spans a large geographical area such as a country or continent. They are typically leased or public, more difficult to maintain, and operate at lower speeds with longer propagation delays,.

### **2. Internet and Intranet**

- **Internet:** An internetwork (or internet) is created when two or more distinct networks are connected together. The **Internet** (capital 'I') is the world's largest internetwork, composed of thousands of interconnected networks, including international backbones, provider networks (ISPs), and customer networks-.
- **Intranet:** An internal, privately-owned network used by a specific organization. It functions using the same protocols as the Internet but is typically restricted to company premises or authorized employees.

### **3. Transmission Modes**

Transmission modes describe the direction of data flow between two connected devices.

- **Simplex:** Communication is strictly one-way. One device only sends, and the other only receives. Examples include a keyboard (sender) and a monitor (receiver), or television broadcasting.
- **Half-Duplex:** Both devices can transmit and receive data, but **not at the same time**. When one device is sending, the other must wait. A walkie-talkie is a classic example.
- **Full-Duplex:** Both devices can transmit and receive data simultaneously. The channel capacity is divided between the two directions. The telephone network is a prime example,.

### **4. Network Topologies**

Physical topology refers to the geometric arrangement of links and nodes (devices) in a network.

- **Mesh Topology:** Every device has a dedicated point-to-point link to every other device. For $n$ nodes, it requires $n(n-1)/2$ physical links.
    - _Advantages:_ High reliability, fault tolerance, and privacy/security,.
    - _Disadvantages:_ High cost, sheer bulk of wiring, and complexity of installation,.
- **Star Topology:** Each device has a dedicated link to a central controller called a hub or switch. All traffic passes through the central device.
    - _Advantages:_ Easy to install, less expensive than mesh, and fault isolation (if one link fails, others remain active).
    - _Disadvantages:_ Single point of failure; if the central hub goes down, the entire network dies,.
- **Bus Topology:** A multipoint topology where one long cable acts as a backbone linking all devices via drop lines and taps.
    - _Advantages:_ Simplicity, cost-effectiveness, and ease of installation,.
    - _Disadvantages:_ Limited scalability, performance issues with heavy traffic, and a single point of failure (if the backbone breaks, the network drops),.
- **Ring Topology:** Each device is connected point-to-point only to its two immediate neighbors, forming a logical ring. Signals circulate in one direction.
    - _Advantages:_ Simplicity, equal access to resources, and easy fault isolation,.
    - _Disadvantages:_ Unidirectional traffic means a single broken link or disabled station can bring down the entire network (unless a dual-ring is used),.
- **Tree Topology:** A hierarchical structure where nodes are arranged like branches.
    - _Advantages:_ Easily scalable and offers fault isolation within specific branches-.
    - _Disadvantages:_ Dependent on the central root node; requires more cables and can become complex to manage.
- **Hybrid Topology:** A combination of two or more different topologies (e.g., star-bus) tailored to leverage their strengths and mitigate individual weaknesses.

### **5. Layered Architecture Approach**

To reduce design complexity, modern networks are organized as a stack of layers.

- **Protocols:** A protocol is a set of rules and conventions that govern how data is exchanged between devices,.
- **Principles of Layering:**
    1. Each layer must perform specific, opposite tasks at the sender and receiver (e.g., encryption at the sender, decryption at the receiver).
    2. The objects under each corresponding layer at both sites must be identical (peer-to-peer communication).
- **Logical vs. Physical Connection:** Except for the lowest physical layer where bits actually travel over a medium, communication at higher layers is _logical_ (virtual). Layer $n$ on one machine communicates conceptually with layer $n$ on another machine,.

### **6. OSI and TCP/IP Reference Models**

- **OSI Reference Model:** Created by ISO, it is a theoretical 7-layer framework: Physical, Data Link, Network, Transport, Session, Presentation, and Application-,. It never became widely deployed because the TCP/IP protocols were already in place, and the OSI model was viewed as overly complex,.
- **TCP/IP Reference Model:** The practical suite used by the Internet, typically modeled in 5 layers today-,:
    1. **Physical Layer:** Responsible for coordinating the transmission of raw bits as electrical, optical, or radio signals over a physical medium,,.
    2. **Data Link Layer:** Responsible for node-to-node (hop-by-hop) delivery of frames over a single link. It provides framing, MAC addressing, and error detection,-.
    3. **Network Layer:** Responsible for routing and host-to-host delivery of packets (datagrams) across multiple interconnected networks. _IP (Internet Protocol)_ is the dominant protocol here,-.
    4. **Transport Layer:** Responsible for process-to-process delivery of messages. It uses port numbers to separate applications. The main protocols are TCP (connection-oriented, reliable) and UDP (connectionless, unreliable),.
    5. **Application Layer:** Contains user-facing network applications and services, such as HTTP (Web), SMTP (Email), and DNS,-.

### **7. Network Devices and Their Roles**

Network equipment operates at different layers of the reference models to route and forward data:

- **Repeater / Hub (Physical Layer):** A repeater receives a weak signal, cleans it, amplifies it, and sends it out. A **hub** is simply a multiport repeater. It has no filtering capability and blindly broadcasts incoming bits out of all other ports,-.
- **Bridge / Link-Layer Switch (Data Link Layer):** A bridge connects LAN segments and uses MAC addresses to filter and forward frames intelligently,. A **switch** is a modern, faster, multi-port bridge that isolates collision domains and forwards frames only to the designated output port,-,.
- **Router (Network Layer):** An internetworking device that links completely different networks. It extracts packets from incoming frames, inspects their logical IP addresses, consults a routing table, and forwards the packet toward its ultimate destination,,-.
- **Gateway (Application / Transport Layer):** A high-level device or software process that connects dissimilar networks or protocols. An application gateway (like an email translator) understands data formats and translates messages entirely,.