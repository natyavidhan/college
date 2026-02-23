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

### 8. Network Features

1. **Connectivity** Connectivity is the fundamental ability of computers and devices to exchange information. It allows users to connect to remote computers, access information, and communicate with other people, effectively ending the "tyranny of geography" by allowing users to access data as though it were local regardless of distance.

2. **Scalability** A network is scalable if its design continues to work well even as the network grows large. Scalability ensures that the network can handle an increasing number of nodes, users, and traffic without a complete redesign, though some topologies (like a bus topology) have limited scalability compared to others.

3. **Reliability - Fault Tolerance** Reliability measures a network's ability to operate correctly even when components (like routers or links) are unreliable or fail. It is measured by the frequency of failure, the time it takes to recover from a failure, and its robustness in a catastrophe. Fault tolerance ensures that the network can dynamically reconfigure itself to find alternative paths if a line or switch goes down.

4. **Performance: Throughput & Delay** Performance can be evaluated by two main metrics: **throughput** (how fast data can actually be sent through the network) and **delay/latency**. As noted in your specific course materials, performance is often measured by _transit time_ (the amount of time required for a message to travel from one device to another) and _response time_ (the elapsed time between an inquiry and a response).

5. **Security** Security involves protecting the network and data against various threats. It includes maintaining confidentiality (preventing eavesdropping), authentication (preventing impersonation), and data integrity (protecting data from unauthorized modification or damage).

6. **Interoperability** Interoperability ensures that devices manufactured by different companies or running different software can communicate effectively. This is made possible by adhering to standardized protocols that define the rules and conventions for data exchange.

7. **Manageability** Manageability refers to the ease with which a network can be monitored, configured, and maintained. For example, some network topologies, like a star topology, provide centralized control for easier management and fault isolation, whereas others can become complex to manage as they grow.

8. **QoS (Quality of Service)** QoS involves mechanisms that reconcile competing demands for network resources to guarantee specific performance levels. It is essential for ensuring the timeliness of delivery required by real-time applications, such as live video or IP telephony, where late data is useless.

9. **Flexibility** Flexibility is the network's ability to be customized and adapted to meet specific or changing requirements. For example, a hybrid topology combines different topologies to provide a flexible and robust infrastructure, and flexible network architectures (like TCP/IP) are designed to handle divergent applications ranging from simple file transfers to real-time speech transmission.

10. **Distributed Processing** Modern computer networks have replaced the old model of a single, centralized "computer center." Instead, they rely on distributed processing, where a large number of separate but interconnected computers share the computational workload to get the job done.

11. **Resource Sharing** This is the primary goal of setting up a network in many companies: making all programs, equipment, and data available to anyone on the network. A common example is sharing a single high-volume network printer among many office workers rather than buying everyone a private printer.

12. **Accessibility** Accessibility refers to the network's ability to make resources available to users across wide geographic areas. A salesperson thousands of miles away can instantly access a product inventory database just as easily as someone sitting in the same building.

13. **Cost-Effectiveness** Networks inherently save money. Beyond sharing physical hardware like printers, networks reduce phone bills through Voice over IP (VoIP), decrease travel costs via video conferencing, and reduce the need for large physical inventories by allowing automated, electronic ordering between manufacturers and suppliers.

14. **Adaptability** Adaptability is the network's ability to adjust to internal changes, such as fluctuating traffic loads or hardware failures. For example, dynamic routing algorithms allow the network to automatically update routes to avoid failed components and reflect current network loads.

15. **Standardization** Standardization is the agreement on network protocols and interfaces (like those set by IEEE, ITU, or IETF). Good standards not only ensure that different computers can communicate, but they also create a larger market for products, which leads to mass production, economies of scale, and decreased prices.

### 9. Protocols

A protocol is a set of rules and conventions that govern how data is exchanged between devices in a network. These rules define the format, timing, sequencing, and error control of the communication. Here is an elaboration of the five key elements of a protocol:

**1. Message Encoding** Before a message can be sent across a network, it must be converted into a format suitable for the physical medium. This process involves a chain of events: a message source passes information to an **encoder**, which translates it into a signal. A transmitter then sends this signal across the transmission medium. At the other end, a receiver captures the signal, a **decoder** translates it back into the original format, and it is delivered to the message destination.

**2. Message Formatting and Encapsulation** For devices to communicate, they must use an **agreed format** for the data. When a message is passed down through the network layers, it undergoes **encapsulation**, which means control information (such as headers and trailers) is added to the data. A critical part of this formatting and encapsulation is identifying the sender and the receiver by including the **source and destination addresses**.

**3. Message Timing** Timing rules coordinate the flow and reliability of data. This element generally includes:

- **Flow Control:** This mechanism regulates the rate of data transmission to ensure that a high-speed sender does not swamp a slow receiver with more messages than it can handle.
- **Response Timeout:** Senders use timers to dictate how long they should wait for a response or acknowledgement. If the response timeout expires, the sender typically assumes the message was lost and takes corrective action, such as retransmitting the data.

**4. Message Size** Networks impose strict limits on the maximum size of a message that can be transmitted at one time. Because of these limitations, **long messages must be broken into smaller pieces** (such as packets or frames) before they are sent. At the destination, these smaller pieces are reassembled back into the original message.

**5. Message Delivery Options** Protocols define how a message is addressed and delivered to its intended audience. There are three primary delivery options:

- **Unicast:** A one-to-one transmission where a message is sent from one sender to exactly one specific receiver.
- **Multicast:** A one-to-many transmission where a message is sent to a specific subset or group of connected machines.
- **Broadcast:** A one-to-all transmission where a message is sent to every machine on the network.