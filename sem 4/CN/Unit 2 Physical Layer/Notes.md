### **1. Data and Signals (Analog and Digital)**

Data must be transformed into electromagnetic signals to be transmitted across a network.

- **Analog vs. Digital:** Analog data and signals are continuous and can take on an infinite number of values within a range. Digital data and signals have discrete states and can take on only a limited number of defined values.
- **Periodic vs. Nonperiodic Signals:** Both analog and digital signals can be periodic or nonperiodic. A periodic signal completes a pattern within a measurable time frame (called a period) and repeats that pattern, while a nonperiodic signal changes without exhibiting a repeating cycle.
- **Signal Attributes:** The **period** refers to the amount of time (in seconds) a signal needs to complete one cycle, while **frequency** refers to the number of periods in one second. For digital signals, we measure the **bit rate** (number of bits sent per second) and the **bit length** (the physical distance one bit occupies on the transmission medium).

### **2. Transmission Impairments**

As signals travel through a medium, they can degrade. Understanding these impairments is crucial for determining maximum data rates.

- **Attenuation:** This means a loss of energy. As a signal travels through a medium, it loses some of its energy in overcoming the medium's resistance, often converting to heat. This loss is typically measured in decibels (dB).
- **Distortion:** This means that the signal changes its form or shape as it travels, which commonly occurs in composite signals made of different frequencies.
- **Noise:** Unwanted signals (such as thermal noise, induced noise, crosstalk, and impulse noise) corrupt the intended message. The quality of the signal is heavily dependent on the **Signal-to-Noise Ratio (SNR)**, which compares the average signal power to the average noise power.

### **3. The Maximum Data Rate of a Channel**

The speed at which data can be accurately transmitted over a channel depends on the available bandwidth, the number of signal levels we use, and the noise level.

- **Noiseless Channel (Nyquist Bit Rate):** For a theoretical channel with no noise, the Nyquist theorem dictates the maximum bit rate. The formula is $Bit Rate = 2 \times Bandwidth \times \log_2(L)$, where $L$ is the number of signal levels used to represent data.
- **Noisy Channel (Shannon Capacity):** In reality, channels have random thermal noise. Claude Shannon introduced a formula to find the theoretical highest data rate for a noisy channel: $Capacity = Bandwidth \times \log_2(1 + SNR)$.
- **Using Both Limits:** In practice, both limits are used together. The Shannon capacity gives the absolute upper limit of the channel, while the Nyquist formula tells us how many signal levels ($L$) we need to achieve that capacity.

### **4. Multiplexing**

Multiplexing is a set of techniques that allows the simultaneous transmission of multiple signals across a single data link, maximizing the efficiency of the available bandwidth.

- **Frequency-Division Multiplexing (FDM):** An analog multiplexing technique applied when the bandwidth of a link is greater than the combined bandwidths of the signals to be transmitted. It divides the available bandwidth into distinct frequency bands, assigning each band to a different source.
- **Wavelength-Division Multiplexing (WDM):** An analog multiplexing technique designed specifically to combine several optical signals (different wavelengths of light) into a single beam transmitted over a fiber-optic cable.
- **Time-Division Multiplexing (TDM):** A digital multiplexing process that allows several connections to share the high bandwidth of a link by dividing the channel into time slots. In synchronous TDM, these time slots are grouped into frames, with one slot in each frame strictly dedicated to a specific input line.

### **5. Transmission Media**

The transmission medium is the physical path by which a message travels from the sender to the receiver. They are categorized into guided and unguided media.

**Guided Media (Wired):**

- **Twisted-Pair Cable:** Consists of two insulated conductors (normally copper) twisted together. The twisting helps cancel out electromagnetic interference and crosstalk from neighboring pairs.
- **Coaxial Cable:** Features a central core conductor enclosed in an insulating sheath, which is in turn surrounded by an outer conducting foil or braid. It can carry signals of higher frequency ranges than twisted-pair cable.
- **Fiber-Optic Cable:** Uses glass or plastic to transmit signals in the form of light. It works on the principle of refraction and reflection; the light is guided down the core of the fiber because the surrounding material (cladding) has a lower density/refractive index.

**Unguided Media (Wireless):** Unguided media transport electromagnetic waves without using a physical conductor.

- **Radio Waves:** These are omnidirectional, meaning they propagate in all directions from the transmitting antenna. Because they can easily penetrate walls, they are widely used for AM radio, television, and general indoor/outdoor communications.
- **Microwaves:** These are unidirectional waves that travel in a line of sight. Because the sending and receiving antennas must be carefully aligned, they are strictly used for point-to-point communication links like cellular phones, satellite networks, and wireless LANs.
- **Infrared:** High-frequency waves used for short-range, line-of-sight communication. Unlike radio waves, infrared cannot penetrate solid objects (like walls), making it secure and ideal for closed-area applications such as TV remote controls.

**Satellite Communication:** Satellite networks rely on space-based equipment to relay microwave signals over vast global distances. Depending on their altitude and orbital mechanics, satellite systems are categorized into **Geostationary Earth Orbit (GEO)**, **Medium-Earth Orbit (MEO)**, and **Low-Earth Orbit (LEO)** satellites.