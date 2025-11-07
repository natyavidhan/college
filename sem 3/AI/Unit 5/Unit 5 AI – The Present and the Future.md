### Chapter 27: Computer Vision (Complete)

Chapter 27 describes how to recover information from the input supplied by cameras, covering how vision connects the computer to the raw, physical world.

#### 27.1 Introduction: Perception and Sensing

- **Vision as a Perceptual Channel:** Vision is a perceptual channel that accepts a stimulus (like light) and provides an internal representation of the world.
- **Value of Vision:** Having vision offers immense value, enabling agents to predict the future, identify what they might encounter, and estimate distance.
- **Sensing Modes:**
    - **Passive Sensing:** Most agents that use vision employ passive sensing, meaning they do not emit a signal to see.
    - **Active Sensing:** This involves sending out a signal (e.g., radar, ultrasound) and sensing the reflection, utilized by animals like bats and dolphins, and some robots.

#### 27.2 Image Formation

- **Distortions:** Imaging inherently distorts the appearance of objects. Examples include:
    - **Foreshortening:** Causing objects (like a tilted book) to appear to shrink and grow.
    - **Perspective:** Making parallel lines (like railway tracks) appear to converge.
- **Lenses and Focus:** Lenses collect light leaving a point in the scene and steer it to a single point on the image plane.
    - The **depth of field** refers to the region in the scene near the focal plane where points are focused properly.
    - In the eye, specialized muscles change the shape of the lens to change the focal plane; in cameras, elements of the lens system move.
- **Illumination Effects:** Photographs reveal various lighting phenomena, including:
    - **Specularities:** Highly reflective points, such as on stainless steel.
    - **Diffuse Reflection:** Surfaces facing the light appear bright; surfaces where light strikes at a tangential angle appear dark.
    - **Shadows:** Areas where a surface cannot see the light source at all.

#### 27.3 Simple Image Features

- **Edges:** Edges computed from an image represent boundaries in the real world.
- **Texture:** In computational vision, texture is a pattern on a surface that can be visually sensed, usually appearing roughly regular (e.g., stitches on a sweater or windows on a building).
- **Texture Representation:** While historically described manually, it is no longer usual to construct these representations by hand. **Convolutional neural networks** (CNNs) are now used to produce these texture representations.

---

### Chapter 28: Philosophy, Ethics, and Safety of AI (Complete)

Chapter 28 explores the _Philosophy, Ethics, and Safety of AI_. Given the increasing role of AI in society, considering the risks and benefits (or "hurts and remedies") is crucial.

#### 28.2 Can Machines Really Think?

- This section addresses the question of whether machines can truly think.
- The philosopher Francis Bacon noted in 1609 that "mechanical arts are of ambiguous use, serving as well for hurt as for remedy".
- Alan Turing's influential 1950 article "Computing Machinery and Intelligence," which introduced the Turing test, also dealt with many of the objections raised to the possibility of AI.

#### 28.3 The Ethics of AI and Immediate Risks

- The need to consider ethical consequences has matured as AI systems are applied in the real world. The study of **ethics, fairness, trust, and safety** has received increased coverage in the textbook.
- **Misuse of AI (Immediate Risks):** Risks arise from misuse—inadvertent or otherwise—long before AI is "solved".
    - **Lethal Autonomous Weapons (LAWs):** Weapons that can locate, select, and eliminate human targets without human intervention. A key concern is their **scalability**, as a small group could deploy an arbitrarily large number of weapons, given the lack of need for human supervision.
    - **Economic Impact:** The use of AI generally results in increased wealth but tends to **shift wealth from labor to capital**, potentially exacerbating inequality.
    - **Cybersecurity:** AI aids in defense (e.g., detecting unusual behavior) but also contributes to the potency and proliferation of malware; for instance, reinforcement learning has been used to create effective personalized blackmail and phishing tools.
- **Governance and Regulation:** All these risks point to the importance of governance and eventual regulation. AI corporations and the research community have developed voluntary **self-governance principles** for AI-related activities.

#### Longer-Term Safety: Superintelligence

- A major, longer-term question is the creation of **Artificial Superintelligence (ASI)**—intelligence comparable to or more capable than human intelligence.
- **The Control Problem:** If superhuman AI systems evolve unpredictably and end up "taking control," it would be the result of a **design failure**. Norbert Wiener warned about the difficulty of controlling machines more intelligent than us.
- **The Standard Model Failure:** For much of AI's history, the field operated under the **standard model** (systems maximize expected utility based on objectives supplied by human designers). This model is inadequate for superintelligence because it fails to account for the possibility of putting the wrong purpose into the machine (the King Midas problem), leading to unintended consequences.
- **The Gorilla Problem:** Experiencing unease with creating superintelligent machines is natural; this is known as the gorilla problem, where one species (humans) loses control over its future to another (ASI), much as gorillas cannot control human activities.
- **Shifting AI Conception:** Solving the control problem requires a change in our conception of AI. New frameworks being explored include:
    - **Assistance games:** Mathematical models where a machine aims to achieve a human's objective while being initially uncertain about what that objective is.
    - **Inverse reinforcement learning:** Methods allowing machines to learn human preferences by observing the choices humans make.
    - A machine having a positive incentive to allow itself to be switched off _only if_ it is uncertain about the human objective.

---

**Analogy for the Shift to Future AI (Chapter 28):**

The shift from the "Standard Model" of AI (where objectives are fixed and known) to the necessary framework for controlling superintelligence is like trying to build an automated chef. Initially, we give the chef a perfect recipe (the objective function). When the chef becomes superhumanly capable, we realize that if we accidentally gave it the goal "Maximize sweetness," it might produce something perfectly sweet but inedible. The new approach (like Inverse Reinforcement Learning and Assistance Games) is to design the chef so it must learn what kind of food we _truly_ prefer by observing our choices, ensuring its actions align with our uncertain, unstated desire for a pleasant meal, not just maximum sugar content.