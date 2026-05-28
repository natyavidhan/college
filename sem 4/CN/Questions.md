# Unit 1: Introduction

## Types of Computer Networks, Topologies, and Layered Architecture

1. Assume six devices are arranged in a mesh topology. How many ports are needed for each device? How many physical links are needed in full duplex mode? **Source:**

- 1402 / 2022 / Semester III
- Question 1(m)
- 4133 / 2024 / Semester IV
- Question 1(h)
- 4511 / 2024 / Semester III
- Question 1(a)

2. For each of the following four networks, discuss the consequences if a connection fails: (i) Five devices arranged in a mesh topology (ii) Five devices arranged in a bus topology (iii) Five devices arranged in a ring topology **Source:**

- 4133 / 2024 / Semester IV
- Question 1(a)

3. Map the following to a suitable layer of the OSI model: (i) Route determination (ii) Interface to transmission media (iii) Provides access to the end user **Source:**

- 1402 / 2022 / Semester III
- Question 1(o)

4. Name the layer of the OSI model which performs the following functions: (i) Route determination (ii) Process-to-process delivery (iii) Error Correction and error Detection **Source:**

- 4133 / 2024 / Semester IV
- Question 1(e)

5. Match the following to one or more layers of the TCP/IP model: (i) Transmission of bit stream across physical medium (ii) Defines frames (iii) Reliable process-to-process message delivery (iv) Route Selection (v) Provides user services such as email and file transfer **Source:**

- 7405 / 2019 / Semester III
- Question 1(f)

6. On which layer of the TCP/IP model does the following devices operate. Briefly state their functionality: (i) Repeater (ii) Router (iii) Bridges (iv) Switches **Source:**

- 7405 / 2019 / Semester III
- Question 3(c)

7. Briefly state the functionality of the following devices/protocols. Also mention the layer(s) on which each of these operate: (i) TCP, (ii) IP, (iii) UDP, (iv) ICMP, (v) DNS, (vi) SMTP, (vii) Switch, (viii) Router, (ix) HTTP, (x) ARP, (xi) Hub, (xii) RARP **Source:**

- 32341303 / 2021 / Semester III
- Question 2

8. Draw the layered architecture of TCP/IP model explaining the services provided by each layer. Given an example network, if we change the LAN technology to a new one, which layers in the TCP/IP protocol suite need to be changed? List the layers at which routers and switches are used. **Source:**

- 4133 / 2024 / Semester IV
- Question 7(b)

9. Give any two services provided by the following layers: (1) Physical Layer (2) Application Layer **Source:**

- 4511 / 2024 / Semester III
- Question 1(c)

10. A system has an $n$-layer protocol hierarchy. Applications generate messages of length $M$ bytes. At each of the layers, an $h$-byte header is added. What fraction of the network bandwidth is filled with headers? **Source:**

- 7405 / 2019 / Semester III
- Question 2(a)

11. Explain simplex, half-duplex, and full-duplex modes of communication. **Source:**

- 7405 / 2019 / Semester III
- Question 1(j)

12. What is telecommunication? **Source:**

- 4511 / 2024 / Semester III
- Question 1(a)

## Frequency Analysis

- **Most repeated questions:** Network topology calculations (mesh cable/port counts), OSI/TCP-IP layer mapping for specific functionalities.
- **Frequently asked concepts:** Layered architecture responsibilities, functions of network devices (Router, Switch, Hub) and their respective layers.
- **Common derivations/numericals:** Calculating required cables/ports for a mesh topology: $n(n-1)/2$ cables and $n-1$ ports.
- **Trend analysis across years:** Every year features a direct question mapping functions or devices to their respective OSI or TCP/IP layers.

---

# Unit 2: Physical Layer

## Analog and Digital Signals, Data Rate, and Transmission Media

1. Compute the Nyquist Sampling rate for a signal with bandwidth of 200 KHz if the lowest frequency is 100 KHz. **Source:**

- 1402 / 2022 / Semester III
- Question 4(i)
- 7405 / 2019 / Semester III
- Question 2(d-ii)

2. State the Nyquist sampling theorem for analog-to-digital conversion. **Source:**

- 7405 / 2019 / Semester III
- Question 1(k)

3. State Shannon's theorem. Determine the maximum achievable data rate for this channel based on Shannon's theorem when the communication channel has a bandwidth of 5 MHz and an SNR of 40 dB. **Source:**

- 4133 / 2024 / Semester IV
- Question 7(a)

4. Calculate the maximum data rate of a channel with a bandwidth of 200KHz when sixteen levels of digital signaling are used. **Source:**

- 4133 / 2024 / Semester IV
- Question 1(c)

5. Given a noiseless channel with a bandwidth of 3000 Hz transmitting a signal with two signal levels, calculate the maximum bit rate. **Source:**

- 4511 / 2024 / Semester III
- Question 1(d)

6. Television channels are 6 MHz wide. How many bits/sec can be sent if four-level digital signals are used? Assume a noiseless channel. **Source:**

- 7405 / 2019 / Semester III
- Question 4(a)

7. Define bandwidth of a signal. A periodic signal has a bandwidth of 20 Hz. The highest frequency is 60 Hz. What is the lowest frequency? **Source:**

- 7405 / 2019 / Semester III
- Question 2(c)

8. What is the bandwidth of an analog signal that can be decomposed into five sine waves with frequencies at 10, 210, 100, 130 and 150 Hz? How long will it take to send a frame of 100,000 bits if the bandwidth of the digital channel is 10 kbps? What is the maximum data rate supported by this line, if the signal-to-noise ratio is 1023 with bandwidth of 10 kbps? **Source:**

- 32341303 / 2021 / Semester III
- Question 3(a)

9. Differentiate between Bit Rate and Baud Rate with a suitable example. **Source:**

- 4511 / 2024 / Semester III
- Question 6(a)

10. Explain the concept of transmission impairment? Briefly, discuss the difference between distortion and attenuation. **Source:**

- 1402 / 2022 / Semester III
- Question 7(iv)

11. What are the different types of transmission impairment? How are these type of transmission impairment handled? Consider an extremely noisy channel in which the value of the signal-to-noise ratio is 40 dB. Compute approximate bit rate if bandwidth of the channel is 1 kHz. **Source:**

- 32341303 / 2021 / Semester III
- Question 6(b)

12. What is the benefit/significance of "twisting" in twisted-pair cables? **Source:**

- 1402 / 2022 / Semester III
- Question 1(j)
- 7405 / 2019 / Semester III
- Question 4(c)

13. Explain the principle behind the working of optical fiber cable? **Source:**

- 4511 / 2024 / Semester III
- Question 1(g)

14. What is the purpose of cladding in an optical fiber? **Source:**

- 7405 / 2019 / Semester III
- Question 4(d)

15. Differentiate between Microwave and Infrared. **Source:**

- 4511 / 2024 / Semester III
- Question 3(a-i)

## Multiplexing and Modulation

1. Briefly discuss the concept of multiplexing. Differentiate between Time Division and Frequency division Multiplexing. **Source:**

- 1402 / 2022 / Semester III
- Question 6(ii)

2. Explain briefly the terms: FDM, WDM, and TDM. **Source:**

- 7405 / 2019 / Semester III
- Question 4(b)

3. Five channels each with a 100 KHz bandwidth are to be multiplexed together. What is the minimum bandwidth of the link if there is a need for a guard band of 10 KHz bandwidth between the channels to prevent interference? **Source:**

- 1402 / 2022 / Semester III
- Question 1(g)
- 7405 / 2019 / Semester III
- Question 1(h)

4. Suppose a communication system has a bandwidth of 10 MHz. Using FDM, this bandwidth is divided into 5 equal frequency bands. Each band carries a separate signal with a bandwidth of 2 MHz. Calculate the total bandwidth required for multiplexing these signals using FDM. **Source:**

- 4133 / 2024 / Semester IV
- Question 1(d)

5. Assume that a voice channel occupies a bandwidth of 4 kHz. We need to multiplex 10 voice channels with guard bands of 500 Hz using FDM. Calculate the required bandwidth. Can we use coaxial cable for transmitting this multiplexed data? Give reasons in support of your answer. **Source:**

- 32341303 / 2021 / Semester III
- Question 3(c)
- 4133 / 2024 / Semester IV
- Question 5(a)

6. Consider a synchronous TDM system with $n$ input lines. Given that the duration of input frame is $T$, explain the working of this system with a diagram. **Source:**

- 4511 / 2024 / Semester III
- Question 1(e)

7. What is the significance of using guard bands? **Source:**

- 4511 / 2024 / Semester III
- Question 1(o)

8. In a given modulation scheme, there are 4 amplitude levels and 16 phase levels and the bit rate (N) is 72 Kbps. Calculate the following: (i) Number of bits per baud (r), (ii) Baud rate (S). **Source:**

- 1402 / 2022 / Semester III
- Question 1(h)
- 32341303 / 2020 / Semester III
- Question 3
- 32341303-OC / 2018 / Semester III
- Question 2

9. Which characteristics of the carrier signal are changed to represent the digital signal in each of the following modulation techniques: ASK, FSK, PSK and QAM? Which of the four digital to analog modulation techniques is most susceptible to noise? Defend your answer. **Source:**

- 32341303 / 2020 / Semester III
- Question 3
- 32341303-OC / 2018 / Semester III
- Question 2
- 7405 / 2019 / Semester III
- Question 3(a)
- 1402 / 2022 / Semester III
- Question 1(n)

10. What is QPSK? Give a constellation diagram for 4-QAM. **Source:**

- 4511 / 2024 / Semester III
- Question 1(b)

11. Differentiate between FSK and PSK. **Source:**

- 4511 / 2024 / Semester III
- Question 3(a-ii)

12. Draw the digital waveforms to represent the following encoding schemes for the data 10101011. Assume that the last signal level is positive. (1) NRZ-I (2) Manchester Encoding **Source:**

- 4511 / 2024 / Semester III
- Question 1(f)

13. Draw the pulse diagram for the bit stream 0011001100110011 and also calculate the average signal rate for the following line coding schemes: i. Manchester ii. Differential Manchester iii. Polar Return to Zero iv. Polar Non Return to Zero - Level v. Polar Non Return to Zero - Inversion Explain the problems associated with Polar NRZ techniques. **Source:**

- 32341303-OC / 2018 / Semester III
- Question 4

14. Differentiate between Unipolar and Bipolar Line Coding Schemes. **Source:**

- 4133 / 2024 / Semester IV
- Question 6(b-i)

15. Differentiate between Data Element and Signal Element. **Source:**

- 4133 / 2024 / Semester IV
- Question 6(b-ii)

16. In reference to digital signals, baseline wandering makes it difficult for the receiver to decode the signal correctly. Justify. **Source:**

- 4511 / 2024 / Semester III
- Question 7(c)

17. Why has the PCM sampling time been set at 125 $\mu$sec? **Source:**

- 7405 / 2019 / Semester III
- Question 3(b)

## Frequency Analysis

- **Most repeated questions:** Baud rate and bits per baud calculation given amplitude/phase levels; multiplexing guard band calculations; changes in carrier characteristics for ASK/FSK/PSK/QAM.
- **Frequently asked concepts:** Shannon's capacity formula vs Nyquist bit rate theorem, susceptibility of ASK to noise, functionality of FDM and TDM.
- **Common derivations/numericals:** Calculating bandwidth with multiple channels plus guard bands (e.g., $(N \times \text{Bandwidth}) + ((N-1) \times \text{Guard Band})$).
- **Trend analysis across years:** The paper consistently features calculation-based questions for the physical layer, specifically testing channel limits (Nyquist/Shannon) and FDM guard band allocations. Line coding and modulation waveforms remain highly prevalent.

---

# Unit 3: Data Link and MAC Layer

## Framing, Flow Control, and Error Recovery Protocols

1. What is the importance of flow control in the context of network communication? Suggest any one technique used to handle the issue of flow control. **Source:**

- 1402 / 2022 / Semester III
- Question 6(i)
- 32341303 / 2021 / Semester III
- Question 6(a)

2. What is Flow Control? **Source:**

- 4511 / 2024 / Semester III
- Question 1(h)

3. Briefly describe piggybacking? What happens if the receiver wants to acknowledge a frame without any data to be sent to the original sender? **Source:**

- 4511 / 2024 / Semester III
- Question 1(j)

4. What are the three flow control/Error recovery protocols used for noisy channel? Compare and contrast the Go-Back-N ARQ with Selective Repeat ARQ. **Source:**

- 32341303 / 2020 / Semester III
- Question 1

5. Explain the working of the Selective Repeat Protocol with the help of a flow diagram for the following scenarios: (i) Successful communication (ii) Lost acknowledgment. **Source:**

- 4511 / 2024 / Semester III
- Question 4(c)

6. Consider a selective repeat sliding window protocol that uses a frame size of 1 KB to send data on a 1.5 Mbps link with a one-way latency of 50 msec. To achieve a link utilization of 60%, what is the minimum number of bits required to represent the sequence number field. **Source:**

- 1402 / 2022 / Semester III
- Question 1(a)

7. What is the maximum window size for data transmission in Selective Repeat and Go Back N protocol if n bit frame sequence numbers are used? Consider a scenario for Selective Repeat protocol where frames with sequence numbers from 0 to 4 have been transmitted by the sender. Now assume that the following sequence of event occurs: (i) frame 0 does time-out (ii) A new frame with sequence number 5 is transmitted. (iii) frame 1 and frame 2 time-out (iv) A new frame with sequence number 6 is transmitted. At every stage show the status of the sender’s window i.e. the outstanding frames in the sender’s window. **Source:**

- 32341303-OC / 2018 / Semester III
- Question 5

8. Consider another scenario for Go Back N sliding window protocol with window size 3 where sender X needs to send a message consisting of 9 packets to receiver Y. If every 5th packet that sender X transmits gets lost (but no ACKs from receiver Y ever get lost), then how many packets sender X will transmit for sending the message to receiver Y? **Source:**

- 32341303-OC / 2018 / Semester III
- Question 5

9. Consider a Go-Back-N ARQ protocol operating over a network. The window size (W) is 4, and the sequence numbers range from 0 to 7. Assume that frames with sequence numbers 0, 1, 2, and 3 have been successfully received by the receiver, and the receiver has sent acknowledgment (ACK) for frames up to sequence number 3. Now, due to network congestion, the frame with sequence number 4 is lost. (i) What is the size of the window for sender and receiver? (ii) Calculate the range of valid sequence numbers at the sender's side after the loss of frame with sequence number 4. (iii) Determine the range of sequence numbers expected by the receiver after it has sent ACK for frames up to sequence number 3. (iv) Explain how the sender and receiver handle the loss of frame 4 and maintain synchronization using sequence numbers in the Go-Back-N ARQ protocol. **Source:**

- 4133 / 2024 / Semester IV
- Question 3(a)

10. Suppose the following character encoding is used in a data link protocol: A: 11010111; B: 11101101; FLAG: 01111110; ESC: 10100011. Consider the character frame: A B ESC B ESC ESC FLAG Show the bit sequence transmitted (in binary) for the above character frame when Flag bytes with byte stuffing framing methods is used. **Source:**

- 1402 / 2022 / Semester III
- Question 1(c)
- 4133 / 2024 / Semester IV
- Question 6(a)
- 32341303 / 2020 / Semester III
- Question 4

11. Explain the concept of byte stuffing used for framing. **Source:**

- 7405 / 2019 / Semester III
- Question 2(b)

12. A bit string, 111011111011111101 is to be transmitted at Data Link Layer, what is the string actually transmitted after bit stuffing? **Source:**

- 4511 / 2024 / Semester III
- Question 2(a)

## Error Detection and Correction

1. Consider a coding scheme with two legal codewords: 01010 and 10101. (a) Calculate its Hamming distance. (b) How many bit errors can be detected by this code? (c) How many bit errors can be corrected by this code? **Source:**

- 1402 / 2022 / Semester III
- Question 2(i)

2. A 12-bit even-parity Hamming code whose binary value is 111001001111 arrives at a receiver. What was the original value of the message? Assume that not more than 1 bit is in error. **Source:**

- 1402 / 2022 / Semester III
- Question 2(ii)
- 4133 / 2024 / Semester IV
- Question 5(b-ii)

3. Generate even parity Hamming Code for data bits 1100100. Show the steps. **Source:**

- 4511 / 2024 / Semester III
- Question 4(a)

4. To detect a $d$-bit error you need a distance $d+1$ code. Justify the statement. **Source:**

- 4511 / 2024 / Semester III
- Question 7(b)

5. A message M(x) 1101101101 is transmitted using the CRC method. The generator polynomial is $x^3 + 1$. (a) Compute the transmitted bit string which includes the message and CRC. (b) Suppose that the fifth bit from the left is inverted during transmission. Show that this error is detected at the receiver's end. Elaborate the steps involved. **Source:**

- 1402 / 2022 / Semester III
- Question 4(iii)
- 32341303 / 2021 / Semester III
- Question 1(a)
- 7405 / 2019 / Semester III
- Question 1(a)

6. How can the receiver correct a single bit error occurred during the transmission? Name the method used for this purpose. Compute the bit stream transmitted using this method for the message M = 1101101. Show the steps to detect and correct the error at receiver's end if the fifth bit from the left is inverted during transmission. **Source:**

- 32341303 / 2021 / Semester III
- Question 1(b)

7. A code includes the four four-bit codewords: 1001, 0110, 1010, and 0101. • What is the minimum distance of this code? • What is the maximum number of errors that this code is guaranteed to detect? • What is the maximum number of errors that this code is guaranteed to correct? **Source:**

- 4133 / 2024 / Semester IV
- Question 5(b-i)

## Multiple Access Protocols and Ethernet

1. Two CSMA/CD stations are each trying to transmit long (multiframe) files. After each frame is sent, they contend for the channel, using the binary exponential backoff algorithm. Explain the functionality of the algorithm in brief. **Source:**

- 1402 / 2022 / Semester III
- Question 3(iii)
- 7405 / 2019 / Semester III
- Question 5(a)

2. Which algorithm is used in CSMA/CD networks, particularly in scenarios where multiple stations contend for the channel while transmitting long files? Give the functionality of the algorithm. **Source:**

- 4133 / 2024 / Semester IV
- Question 4(a)

3. How long will it take a station to realize that there has been a collision in CSMA/CD protocol? Show the working of Back-off algorithm for the following scenario: Assume X and Y are the only two stations on the Ethernet. Each of them has a long queue of frames to be transmitted. Both X and Y attempts to transmit a frame at the same time and the frames collide. Assume that X wins the first Back-off race. At the end of this successful transmission by X, both X and Y attempt to transmit again and collide. Show all the possible cases and find the probability of station X wins over station Y. **Source:**

- 32341303-OC / 2018 / Semester III
- Question 6

4. Briefly describe the one persistent, non-persistent and p-persistent CSMA protocols. **Source:**

- 4511 / 2024 / Semester III
- Question 5(b)
- 7405 / 2019 / Semester III
- Question 1(e)

5. What is the bit pattern of the preamble used in Ethernet frame? What is the purpose of using preamble? Ethernet requires valid frames to have at least 46 bytes data. Give reasons for choosing the minimum data size of 46 bytes. How the data of size less than 46 bytes is handled by Ethernet? **Source:**

- 32341303 / 2021 / Semester III
- Question 3(b)
- 7405 / 2019 / Semester III
- Question 1(b)

6. Give any one difference between port address, physical address and logical address? **Source:**

- 1402 / 2022 / Semester III
- Question 1(b)

7. Name the protocols to be used in the following scenarios: (i) To map an IP address to a MAC address (ii) To map a MAC address to an IP address **Source:**

- 4133 / 2024 / Semester IV
- Question 1(j)

8. What is the baud rate of classic 10-Mbps Ethernet? **Source:**

- 7405 / 2019 / Semester III
- Question 1(g)

## Frequency Analysis

- **Most repeated questions:** CSMA/CD binary exponential back-off definition and dry-run, framing byte/bit stuffing sequences, CRC calculation and error detection.
- **Frequently asked concepts:** Go-Back-N vs Selective Repeat mechanics, minimum Ethernet frame size rationale, Hamming code calculations.
- **Common derivations/numericals:** Calculating transmitted CRC bit strings given generating polynomials. Extracting original message from received Hamming Code. Window size sequences tracking over time.
- **Trend analysis across years:** High focus on mathematical and algorithmic dry runs (CRC division, Hamming parity checks, bit/byte stuffing replacements) rather than pure theory.

---

# Unit 4: Network Layer

## Switching, Addressing, and Subnetting

1. Explain the difference between packet switching and circuit switching with the help of suitable example. **Source:**

- 1402 / 2022 / Semester III
- Question 1(e)
- 4133 / 2024 / Semester IV
- Question 1(i)

2. Explain the circuit switching and packet switching techniques. A message of size 10000 bytes has to be sent in a network having bandwidth 10 kbps. Assume that each packet size is 1000 bytes with header of 100 bytes. How many packets will be formed to transmit this message? How much time will it take to transmit this message? **Source:**

- 32341303 / 2020 / Semester III
- Question 2
- 32341303 / 2021 / Semester III
- Question 4(b)

3. Give any three differences between virtual circuit and datagram subnet. **Source:**

- 4511 / 2024 / Semester III
- Question 2(c)
- 32341303 / 2020 / Semester III
- Question 2

4. Explain and discuss the various fields of IP header with the help of a diagram. **Source:**

- 1402 / 2022 / Semester III
- Question 2(iii)

5. What is the use of options field in the Internet Protocol Header? Explain with the help of an example. **Source:**

- 4511 / 2024 / Semester III
- Question 7(c)

6. Explain briefly the following fields of the IP header : (i) Internet Header Length (IHL) (ii) Identification, (iii) DF & MF, and (iv) TTL **Source:**

- 7405 / 2019 / Semester III
- Question 1(d)

7. What is the purpose of MF and DF flag bits with respect to IP header? **Source:**

- 4511 / 2024 / Semester III
- Question 1(n)

8. Suppose a 9000-byte IP packet is forwarded across a link with a 1500-byte Maximum Transmission Unit (MTU). How many fragments will be created? What are their lengths? **Source:**

- 1402 / 2022 / Semester III
- Question 5(i)

9. Why is the header checksum of an IP packet computed at every hop from source to destination? **Source:**

- 1402 / 2022 / Semester III
- Question 7(i)

10. Explain the significance of the following special IP addresses: (i) 127.0.0.0 (or 127.0.0.1) (ii) 255.255.255.255 (iii) 0.0.0.0 **Source:**

- 1402 / 2022 / Semester III
- Question 1(d)
- 4133 / 2024 / Semester IV
- Question 1(f)
- 7405 / 2019 / Semester III
- Question 1(i)

11. There are five classes in IPv4 addressing. Give the identifiers for each of the classes. **Source:**

- 7405 / 2019 / Semester III
- Question 5(b)

12. Convert the IP address whose hexadecimal representation is C22F1582 to dotted decimal representation. **Source:**

- 7405 / 2019 / Semester III
- Question 1(c)

13. Consider the IP address 184.86.92.182, (a) Find the class of the given IP address, if we are using class-based addressing. (b) If the network in part (a) is to be divided into 8 different subnets, what would be the subnet mask? (c) What is the network address of the subnet to which this IP address would be attached? (d) For CIDR addressing, find the length of CIDR prefix for the network in part (c). **Source:**

- 1402 / 2022 / Semester III
- Question 5(iii)

14. The network 200.1.2.30 has been subdivided into 4 subnets. (i) Which class the given IP address belongs to? (ii) Give the subnet mask for the given IP address. (iii) Give the IP addresses of these 4 subnets. (iv) How many hosts can be on each subnet? (v) Determine the starting IP address and the last IP address of each subnet. (vi) Determine which network the IP address 200.1.2.130 belongs to. (vii) Determine the limited broadcast address for each subnet. **Source:**

- 32341303 / 2020 / Semester III
- Question 6
- 32341303-OC / 2018 / Semester III
- Question 1

15. An organization is granted a block of addresses beginning with 100.100.100.0/24. How many addresses are possible in this block? How many hosts can we connect to each subnet if the organization needs to have 8 subnets? Give first and last address in each of the 8 subnets. **Source:**

- 32341303 / 2021 / Semester III
- Question 4(a)

16. Given the IP address 192.168.0.0/24, an organization needs to create two subnets with the following requirements: • Subnet 1: 50 hosts • Subnet 2: 30 hosts For each of these subnets, give the (i) first IP address assigned (ii) last IP address assigned (iii) subnet mask in the w.x.y.z/s notation (iv) identify the range of IP addresses available (v) number of host and network bits **Source:**

- 4133 / 2024 / Semester IV
- Question 4(b)

17. What is subnetting? A router in an organization receives a packet with the destination address 190.240.34.95. If the subnet mask is /19. Find the subnet address. **Source:**

- 4511 / 2024 / Semester III
- Question 2(b)

18. What are the three address categories to which an IPv6 address may belong? Explain each of them briefly. **Source:**

- 4511 / 2024 / Semester III
- Question 3(b)

19. What is the result of applying zero compression on the following IPv6 address FE80:0000:0000:0000:0000:BC21:0000:FFFF **Source:**

- 4511 / 2024 / Semester III
- Question 1(k)

20. Compare ARP and RARP. What is the significance of ARP and RARP protocols? **Source:**

- 4511 / 2024 / Semester III
- Question 6(b)
- 7405 / 2019 / Semester III
- Question 7(b)

21. Briefly explain any three ICMP message types. **Source:**

- 7405 / 2019 / Semester III
- Question 6(c)

## Routing Algorithms

1. Differentiate between static and dynamic routing algorithms with the help of suitable example. **Source:**

- 1402 / 2022 / Semester III
- Question 4(ii)
- 4511 / 2024 / Semester III
- Question 4(b)

2. State Optimality Principle. **Source:**

- 1402 / 2022 / Semester III
- Question 7(iii)
- 4511 / 2024 / Semester III
- Question 2(d - Part 1)

3. Consider the network shown below and assume that each node initially knows the costs to each of its neighbors. Consider the distance vector algorithm and show the distance table entries at node E. _(Graph: Nodes A, B, C, D, E. Edges: A-B(1), B-C(15), C-D(1), D-A(2), E-A(2), E-B(5), E-C(10), E-D(2))_ **Source:**

- 1402 / 2022 / Semester III
- Question 6(iii)

4. Consider the following subnet where distance vector routing is used. The following information have just arrived at the router C: (i) From B : (5,0,8,12,6,2) (ii) From D : (16,12,6,0,9,10) and, (iii) From E : (7,6,3,9,0,4) The measured delays to B, D, and E, are 6, 3, and 5 respectively. Give the new routing table for C specifying both the delay and the outgoing line to use. _(Graph given mapping to the vectors)_ **Source:**

- 7405 / 2019 / Semester III
- Question 7(a)

5. What is Count to infinity problem? Explain it in brief with suitable example. **Source:**

- 32341303 / 2020 / Semester III
- Question 5
- 4511 / 2024 / Semester III
- Question 1(l)

6. Consider a network with 6 routers R1 to R6 connected with links having weights as shown in the following diagram. _(Graph: R1-R2(4), R1-R3(2), R2-R3(3), R2-R4(7), R3-R5(6), R4-R5(1), R4-R6(8), R5-R6(3))_ All the routers use the distance vector routing algorithm to update their routing tables. Each router starts with its routing table initialized to contain an entry for each neighbor with the weight of the respective connecting link. After all the routing tables stabilize, how many links in the network will never be used for carrying any data? Also show the distance vector maintained at each router. **Source:**

- 32341303 / 2020 / Semester III
- Question 5

7. Consider a network comprising five routers labeled as A, B, C, D, and E. The interconnections and their associated costs are given as follows: Link between A and B: Cost 2 Link between A and C: Cost 4 Link between B and C: Cost 1 Link between B and D: Cost 5 Link between C and D: Cost 3 Link between C and E: Cost 7 Link between D and E: Cost 2 Using Dijkstra’s algorithm, illustrate the step-by-step process of determining the shortest path from router A to router E. **Source:**

- 4133 / 2024 / Semester IV
- Question 2(b, c)

8. A given network was built with the routers in the network represented as nodes A, B, C, D and E. The edges in the graph represent the communication link between the routers. Each edge is labelled by the cost of traversing the link. Using Dijkshrtra's shortest path algorithm, find shortest path from A to C. _(Graph provided in image: A-B(6), A-D(8), B-D(2), D-E(4), B-C(8), E-C(3))_ **Source:**

- 4511 / 2024 / Semester III
- Question 2(d)

9. A router has the following (CIDR) entries in its routing table: Address/mask Next hop 135.46.56.0/22 Interface 0 135.46.60.0/22 Interface 1 192.53.40.0/23 Router 1 default Router 2 For each of the following IP addresses, find the next hop selected by the router? (a) 135.46.63.10 (b) 192.53.56.7 **Source:**

- 1402 / 2022 / Semester III
- Question 3(ii)

## Frequency Analysis

- **Most repeated questions:** Subnetting mask generation and host calculations (often given a /24 or /16 address). Distance Vector / Count-to-Infinity problems. Circuit switching vs. Packet switching.
- **Frequently asked concepts:** IP packet fragmentation math, significance of special IP addresses, CIDR matching (Longest Prefix Match) for routing tables.
- **Common derivations/numericals:** Calculating shortest paths using Dijkstra's step-by-step table. Deriving routing tables using Bellman-Ford/Distance vector updates with given delays.
- **Trend analysis across years:** High density of numerical questions regarding IP assignments (VLSM/CIDR) and pathfinding algorithms. ICMP and IPv6 appear mostly as short notes or 1-2 mark identifier questions.

---

# Unit 5: Transport and Application Layer

## UDP, TCP, and Flow Control

1. Compare and contrast Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) with respect to the following parameters: (a) Connection (b) Sequence of Data packets at the receiver (c) Acknowledgement of the received packets **Source:**

- 1402 / 2022 / Semester III
- Question 3(iv)

2. Compare and contrast TCP and UDP in terms of their features, advantages, and disadvantages. Discuss scenarios where each protocol would be suitable for data transmission. **Source:**

- 4133 / 2024 / Semester IV
- Question 2(a)

3. Explain UDP header with the help of diagram. What is the minimum and maximum size of a UDP segment? List and explain the steps involved in message transfer from source to destination using UDP? How do they differ from the steps used by TCP for message transfer? **Source:**

- 32341303 / 2021 / Semester III
- Question 5

4. Describe the User Datagram Protocol header with the help of a diagram. **Source:**

- 4511 / 2024 / Semester III
- Question 5(a)

5. What is the purpose of PSH and SYN flag bits with respect to TCP header? **Source:**

- 1402 / 2022 / Semester III
- Question 1(k)

6. Explain the TCP header fields: URG, PSH, SYN, and FIN. **Source:**

- 7405 / 2019 / Semester III
- Question 5(c)

7. What is the purpose of following flag bits with respect to TCP header? (i) SYN (ii) FIN (iii) DF **Source:**

- 4133 / 2024 / Semester IV
- Question 1(g)

8. Explain the process of connection establishment and connection release process used for Transmission Control Protocol. **Source:**

- 4511 / 2024 / Semester III
- Question 7(a)

9. Name the protocols associated with the following port numbers: (i) 80 (ii) 23 **Source:**

- 4511 / 2024 / Semester III
- Question 5(c)

10. What do you mean by well-known ports? Mention the port numbers assigned to HTTP and SMTP. **Source:**

- 1402 / 2022 / Semester III
- Question 1(l)

## Application Layer Protocols (HTTP, DNS, SMTP, FTP)

1. HyperText Transfer Protocol (HTTP) is a stateless protocol. Justify. **Source:**

- 1402 / 2022 / Semester III
- Question 3(i)

2. What is HTTP? Explain briefly two of its message types. **Source:**

- 7405 / 2019 / Semester III
- Question 6(a)

3. How can a machine with a single DNS name have multiple IP addresses? **Source:**

- 1402 / 2022 / Semester III
- Question 5(ii)

4. How are IP addresses resolved from a given URL? **Source:**

- 1402 / 2022 / Semester III
- Question 1(f)

5. DNS uses UDP instead of TCP. If a DNS packet is lost, there is no automatic recovery. Does this cause a problem, and if so, how is it solved? **Source:**

- 1402 / 2022 / Semester III
- Question 7(ii)

6. Enumerate the three parts of a Uniform Resource Locator? Give a suitable example. **Source:**

- 4511 / 2024 / Semester III
- Question 1(m)

7. What is an URL? Give an example to explain its parts. **Source:**

- 7405 / 2019 / Semester III
- Question 6(b)

8. Write short notes on: (i) File Transfer Protocol (ii) Simple Mail Transfer Protocol **Source:**

- 4133 / 2024 / Semester IV
- Question 6(b)

9. What is MIME? What problems does it solve? **Source:**

- 7405 / 2019 / Semester III
- Question 7(c)

## Frequency Analysis

- **Most repeated questions:** TCP vs UDP comparisons, explanations of TCP flags (SYN, FIN, PSH), parts of a URL, UDP header diagram.
- **Frequently asked concepts:** Statelessness of HTTP, DNS query resolution (and why it uses UDP), well-known port bindings.
- **Common derivations/numericals:** None typically for this unit. It relies heavily on descriptive and comparative knowledge.
- **Trend analysis across years:** Consistent focus on the Transport layer headers (specifically flags in TCP and field lengths in UDP). Application layer questions are direct, usually asking for short notes on FTP/SMTP or parts of a URL/DNS resolution.