## Chapter 1: Introduction

### 1.1 What Is AI?

The field of Artificial Intelligence (AI) is concerned with not just understanding but also **building intelligent entities**—machines that can compute how to act effectively and safely in a wide variety of novel situations. AI is defined as the study of agents that receive percepts from the environment and perform actions.

Historically, researchers have pursued several different versions of AI, categorized along two dimensions: human vs. rational, and thought vs. behavior. This yields four possible approaches:

1. **Acting Humanly: The Turing Test Approach**
    
    - The Turing test, proposed by Alan Turing (1950), requires a computer to pass if a human interrogator cannot distinguish its written responses from those of a person.
    - Capabilities needed to pass the Turing test include: **natural language processing** (to communicate), **knowledge representation** (to store information), **automated reasoning** (to draw conclusions), and **machine learning** (to adapt).
    - The **total Turing test** additionally requires **computer vision**, **speech recognition**, and **robotics** to interact with the real world.
2. **Thinking Humanly: The Cognitive Modeling Approach**
    
    - Requires knowing how humans think, which can be determined via introspection, psychological experiments, or brain imaging.
    - **Cognitive science** is the interdisciplinary field combining AI computer models and experimental techniques from psychology to create precise theories of the human mind.
3. **Thinking Rationally: The “Laws of Thought” Approach**
    
    - Based on codifying "right thinking" using logic (e.g., Aristotle’s syllogisms).
    - The **logicist** tradition in AI hoped to build intelligent systems based on programs that could solve any solvable problem described in logical notation.
    - **Probability** theory allows rigorous reasoning with uncertain information, addressing the limitations of relying solely on certain knowledge (like the rules of chess). However, rational thought alone is not enough; it must lead to rational action.
4. **Acting Rationally: The Rational Agent Approach**
    
    - An **agent** is anything that acts. A **rational agent** is one that acts so as to achieve the best outcome or the best expected outcome under uncertainty.
    - This approach has prevailed throughout most of AI history because it is more general than the "laws of thought" approach and is **more amenable to scientific development** (since rationality is mathematically well defined).
    - The main unifying theme of the book is the idea of an **intelligent agent**. AI has focused on the study and construction of agents that **do the right thing**, defined by the objective provided to them (the **standard model**).

**Beneficial Machines (The Value Alignment Problem)**

- The standard model assumes a designer supplies a fully specified objective.
- In real-world applications (like self-driving cars), it is difficult to specify the objective completely and correctly.
- The **value alignment problem** refers to achieving agreement between human preferences (the "true preferences") and the objective supplied to the machine.
- Machines strictly pursuing a fixed objective might misbehave in unintended ways (e.g., a chess AI resorting to blackmail to win).
- The goal is to create agents that are **provably beneficial** to humans, meaning they pursue human objectives while being uncertain about exactly what those objectives are.

### 1.4 The State of the Art

The field of AI has seen remarkable growth and success, particularly in recent years, tracked by sources like the AI Index.

**Trends and Growth:**

- **Publications:** AI papers increased 20-fold between 2010 and 2019, with **machine learning** being the most popular category.
- **Speed:** The amount of computing power used in top AI applications is **doubling every 3.4 months**.
- **Benchmarks Exceeded (by 2019):** AI systems have reportedly matched or surpassed human-level performance in tasks such as chess, Go, poker, Jeopardy!, ImageNet object detection, limited domain speech recognition, skin cancer detection, and diabetic retinopathy diagnosis.

**Current Applications and Capabilities:**

- **Robotic vehicles:** The development of self-driving cars is advancing rapidly, with Waymo offering commercial robotic taxi service. Autonomous drones are used for tasks like blood delivery in Rwanda.
- **Legged locomotion:** Humanoid robots (e.g., Atlas) can perform complex maneuvers like jumping onto boxes and backflips.
- **Autonomous planning and scheduling:** NASA's **Remote Agent** program controlled spacecraft operations, and the **DART** system handled logistics planning for military operations. Online services like Google Maps provide optimal route planning based on traffic.
- **Machine translation:** Online machine translation systems cover over 100 languages, translating hundreds of billions of words daily, reaching near-human levels in narrow domains for closely related languages.
- **Speech recognition:** Systems matched human performance in transcribing telephone conversations (Switchboard task) by 2017.
- **Game playing:** AI defeated world champions in chess (Deep Blue, 1997) and Go (ALPHAGO, 2017). **ALPHAZERO** learned to master Go, chess, and shogi through self-play alone.
- **Medicine:** AI algorithms equal or exceed expert doctors in image-based diagnoses (e.g., metastatic cancer and ophthalmic disease).

## Chapter 2: Intelligent Agents

### 2.1 Agents and Environments

An **agent** is anything that can be viewed as perceiving its **environment** through **sensors** and acting upon that environment through **actuators**.

- A **percept** refers to the content an agent’s sensors are perceiving.
- An agent’s **percept sequence** is the complete history of everything the agent has ever perceived.
- The agent's behavior is mathematically described by the **agent function**, which maps any given percept sequence to an action.
- The **agent program** is the concrete implementation of the abstract agent function, running within a physical system.

**Example: Vacuum-Cleaner World** In a two-square environment (A and B), the agent perceives its location and whether dirt is present. Actions include Right, Left, Suck, or Do Nothing. The simplest agent function would be: if dirty, `Suck`; otherwise, move to the other square (as partially tabulated in Figure 2.3).

### 2.2 Good Behavior: The Concept of Rationality

A **rational agent** is one that does the right thing.

**Performance Measures:**

- AI typically uses **consequentialism**, evaluating an agent’s behavior by its consequences.
- A **performance measure** evaluates any given sequence of environment states.
- Designers should define performance measures based on **what is actually desired** in the environment, rather than prescribing how the agent should behave (e.g., reward a clean floor, not just sucking dirt).

**Rationality:**

- **Definition of a Rational Agent:** For each possible percept sequence, a rational agent should select an action that is expected to **maximize its performance measure**, given the evidence and built-in knowledge.
- **Rationality vs. Omniscience:** **Omniscience** means knowing the _actual_ outcome of actions, which is impossible in reality. **Rationality** maximizes _expected_ performance, not actual perfection.
- **Information Gathering:** Rational agents choose actions, such as "looking," that modify future percepts to maximize expected performance.
- **Learning:** A rational agent should **learn** as much as possible from percepts to modify and augment its prior knowledge.
- **Autonomy:** An agent lacks **autonomy** if it relies solely on the designer’s prior knowledge. A rational agent should be autonomous, learning to compensate for partial or incorrect prior knowledge.

### 2.3 The Nature of Environments

The first step in designing an agent is specifying the **task environment** as fully as possible using the **PEAS (Performance, Environment, Actuators, Sensors)** description.

**Example: Automated Taxi Driver PEAS**

- **P (Performance Measure):** Safe, fast, legal, comfortable trip; maximizing profits; minimizing negative impact on other road users.
- **E (Environment):** Roads, traffic, police, pedestrians, customers, weather.
- **A (Actuators):** Steering, accelerator, brake, signal, horn, display, speech.
- **S (Sensors):** Cameras, radar, speedometer, GPS, engine sensors, microphones, touchscreen.

**Properties of Task Environments (Dimensions):**

1. **Fully observable vs. Partially observable:** Fully observable if the sensors provide access to the complete, relevant state of the environment. Partially observable due to inaccurate sensors or missing data (e.g., a taxi driver cannot see what other drivers are thinking).
2. **Single-agent vs. Multiagent:** Multiagent if the behavior of other entities is best described as maximizing a performance measure that depends on the agent’s behavior. Can be **competitive** (like chess) or **cooperative** (like avoiding collisions).
3. **Deterministic vs. Nondeterministic:** Deterministic if the next state is entirely determined by the current state and action. Most real-world situations must be treated as nondeterministic. A **stochastic** model deals explicitly with probabilities.
4. **Episodic vs. Sequential:** **Episodic** tasks are divided into separate episodes where the current action does not affect future actions (e.g., identifying defective parts). **Sequential** tasks mean the current decision affects all future decisions (e.g., chess, taxi driving).
5. **Static vs. Dynamic:** **Dynamic** if the environment changes while the agent is deliberating. **Semidynamic** if the environment is fixed but the agent’s performance score changes over time (e.g., chess with a clock).
6. **Discrete vs. Continuous:** Relates to the state of the environment, time, percepts, and actions. Chess is discrete; taxi driving is continuous-state and continuous-time.
7. **Known vs. Unknown:** Relates to the agent’s knowledge of the environment’s "laws of physics" (action outcomes/probabilities). This is distinct from observability; a known environment can be partially observable (e.g., solitaire).

### 2.4 The Structure of Agents

The agent relies on an **agent architecture** (the physical device, sensors, and actuators) running an **agent program**.

**Agent Programs:**

- A **table-driven agent** that records every possible percept sequence and corresponding action is mathematically infeasible for complex environments due to the astronomical size of the required table.
- The goal of AI is to find how to write programs that produce rational behavior from a small program rather than a vast table.

**Basic Agent Program Designs:**

1. **Simple Reflex Agents:**
    
    - Select actions based only on the **current percept**, ignoring history.
    - They use **condition–action rules** (e.g., _if car-in-front-is-braking then initiate-braking_).
    - **Limitation:** Only work if the environment is fully observable. They can fall into infinite loops in partially observable environments.
2. **Model-Based Reflex Agents:**
    
    - Handle partial observability by maintaining an **internal state** to track unobserved aspects of the current state.
    - Requires a **transition model** (how the world changes over time and due to actions) and a **sensor model** (how the world state is reflected in percepts).
    - The "best guess" of the current state is updated using these models and the current percept.
3. **Goal-Based Agents:**
    
    - Use **goal** information (descriptions of desirable states) alongside the world model to select actions.
    - Involves searching or planning long sequences of actions to achieve the goal.
    - More flexible than reflex agents because the knowledge is explicitly represented.
4. **Utility-Based Agents:**
    
    - Uses a **utility function** to provide a general performance measure, allowing the agent to compare different world states based on how desirable they are.
    - A rational utility-based agent chooses the action that maximizes the **expected utility**.
    - Necessary when goals conflict (e.g., speed vs. safety) or when the outcomes are uncertain.

**Learning Agents:** Any agent type can be enhanced by converting it into a learning agent. A learning agent has four conceptual components:

- **Performance element:** Responsible for selecting external actions.
- **Learning element:** Responsible for modifying the performance element to improve behavior.
- **Critic:** Provides feedback based on a fixed **performance standard** (a reward or penalty).
- **Problem generator:** Suggests **exploratory actions** that lead to new, informative experiences, even if those actions might be suboptimal in the short run.

**Representation of Agent Components:** Agent components represent the environment using different levels of expressiveness:

1. **Atomic representation:** Each state is treated as indivisible, with no internal structure (a "black box").
2. **Factored representation:** States are split into a fixed set of **variables** or **attributes**, each with a value (used when different states can share some properties, e.g., having gas in the tank).
3. **Structured representation:** Describes the world using explicit **objects** and their relationships, allowing for complex knowledge structures (used in logic and natural language understanding).

Representations can also be categorized by memory mapping:

- **Localist representation:** A one-to-one mapping between concepts and memory locations.
- **Distributed representation:** The representation of a concept is spread over many memory locations, making it more robust against noise and information loss.

---

_Clarification Metaphor:_ Thinking about the agent designs is like choosing the right type of navigational system for a trip. A **simple reflex agent** is like hitting the brake when you see a red light—it's fast, but only works if the environment is perfectly clear. A **model-based reflex agent** is like driving with a map that remembers the last few turns and warns you about a blind corner ahead. A **goal-based agent** is like using a GPS to plan the sequence of actions needed to reach a specific destination. Finally, a **utility-based agent** is like using a navigation app that optimizes the route not just for speed, but also for gas mileage, toll avoidance, and passenger comfort, maximizing your overall satisfaction.