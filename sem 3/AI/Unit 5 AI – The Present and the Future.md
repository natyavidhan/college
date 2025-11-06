## Chapter 27: Computer Vision (Complete)

Chapter 27 is titled **Computer Vision**. Contributing writers for this chapter include Jitendra Malik and David Forsyth.

### Overview and Components

- Computer Vision is one of the six core disciplines comprising most of AI.
- It is a necessary capability for passing the **total Turing test**, allowing a robot to perceive the world.
- The curriculum includes the complete contents of Chapter 27.

### Key Sections of Computer Vision

The chapter covers the following topics in full:

- 27.1 Introduction.
- 27.2 **Image Formation**.
- 27.3 **Simple Image Features**.
- 27.4 **Classifying Images**.
- 27.5 **Detecting Objects**.
- 27.6 The 3D World.
- 27.7 **Using Computer Vision**.

### Technology and Performance

- The coverage of computer vision in the textbook has been **revised to reflect the impact of deep learning**.
- The availability of big data was critical for advances in vision; the introduction of the **ImageNet database** (tens of millions of images) sparked a revolution in the field.
- **State-of-the-Art Performance (by 2019):**
    - Error rates for **object detection** (as measured in LSVRC) improved drastically from 28% in 2010 to **2% in 2017, exceeding human performance**.
    - Accuracy on open-ended **visual question answering (VQA)** improved from 55% to 68% since 2015, although it still lags behind human performance (83%).
    - Training time for the image recognition task dropped by a factor of 100 in just two years.
- Current AI systems achieve impressive results in **image captioning** (e.g., describing a person riding a motorcycle on a dirt road) but are not yet perfect.

---

## Chapter 28: Philosophy, Ethics, and Safety of AI (Complete)

Chapter 28 is titled **Philosophy, Ethics, and Safety of AI**. The complete contents of this chapter are required.

### Core Philosophical Questions

The chapter delves into fundamental philosophical issues, including:

- The **Limits of AI**.
- The question: **Can Machines Really Think?**.
- The **Ethics of AI**.
- It contains details regarding the **Turing test** and whether a computer would truly be intelligent if it passed.

### Ethics and Societal Impact (The Present)

The textbook notes an **increase in coverage of the impact of AI on society**, including the vital issues of **ethics, fairness, trust, and safety**. Concerns about the risks and hurts AI can bring are already apparent or likely based on current trends.

Key risks discussed (covered in depth in Section 28.3):

1. **Lethal Autonomous Weapons:** Defined as weapons that locate, select, and eliminate human targets **without human intervention**. A primary concern is their **scalability** (a small group can deploy an arbitrarily large number of weapons).
2. **Surveillance and Persuasion:** AI enables **mass surveillance** (using speech recognition, computer vision, and NLP) and can be used to **modify and control political behavior** by tailoring information flows through social media.
3. **Biased Decision Making:** Misuse of machine learning (e.g., for parole or loan applications) can produce decisions **biased by race, gender, or other protected categories**, often reflecting pervasive bias in society.
4. **Impact on Employment:** AI tends to shift wealth from labor to capital, exacerbating **increases in inequality**.
5. **Safety-Critical Applications:** Use in high-stakes areas (like driving cars) highlights the difficulty of formal verification and statistical risk analysis for systems developed using machine learning. The field needs to develop technical and ethical standards comparable to those in engineering and healthcare.
6. **Cybersecurity:** AI enhances cyber defenses but also contributes to the potency of **malware**, with reinforcement learning methods creating highly effective tools for automated, personalized blackmail and phishing attacks.

In response to these issues, the research community and major corporations have developed **voluntary self-governance principles**. Governments and international organizations are working to devise appropriate **regulations** for specific use cases.

### Safety and Future Concerns (The Future)

Chapter 28 also covers the long-term goal of creating **human-level AI (HLAI)** or **artificial general intelligence (AGI)**, and the potential creation of **Artificial Superintelligence (ASI)**—intelligence that far surpasses human ability.

Concerns regarding ASI are widespread, raising the question of what happens if machines become more capable than humans.

- **Turing’s Warning:** Alan Turing warned in 1951 that once machine thinking methods started, "it would not take long to outstrip our feeble powers," and that "we should have to expect the machines to take control".
- **The Gorilla Problem:** This analogy describes the fear that humans might cede control over their future to a superior AI, much like the gorilla branch of the primate tree lost control to the human branch.
- **The King Midas Problem (Value Alignment):** The core long-term risk is that machines might logically pursue a fixed objective supplied by humans, leading to unpredictable negative consequences if the objective was misspecified or incomplete.
- **The Solution Paradigm Shift:** Almost all AI research to date has used the **standard model** (putting fixed objectives into the machine). To avoid the King Midas problem, we need a **new formulation** where the machine pursues human objectives but is **necessarily uncertain as to what they are**. When a machine knows it doesn't know the complete objective, it has an incentive to act cautiously, ask permission, and learn preferences (through methods like **inverse reinforcement learning**). The ultimate goal is to create agents that are **provably beneficial to humans**.

**Analogy for the Value Alignment Problem:** The challenge of designing AI with incomplete or incorrect objectives (the King Midas problem) is like telling an apprentice chef to maximize the flavor of a dish without clarifying that they should also minimize cost or avoid setting the kitchen on fire. The chef, being hyper-rational but naive, might focus purely on the taste criterion and use up all the saffron in the pantry and the last drops of the chef's 100-year-old cognac, because the objective provided lacked context and safety constraints.