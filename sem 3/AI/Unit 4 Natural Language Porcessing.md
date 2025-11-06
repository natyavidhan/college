[ChatGPT Explaination](https://chatgpt.com/g/g-p-68f9481143b4819190a80421f345fa52-college/c/6903e704-77a4-8321-adc9-005e17801165)
### 12.1 Introduction

The ability to **understand natural language** is crucial for Artificial Intelligence (AI) because a natural form of communication is essential for user acceptance. Effective communication is regarded as one of the most critical tests for intelligent behavior, a concept highlighted by the Turing test.

A program is said to **understand a natural language** if it responds by taking a predictably correct or acceptable action in response to the input. This action may be an external response, such as providing an answer to a question, or simply the creation of **meaningful internal data structures** (as in learning new facts).

Developing programs to handle natural language is difficult because:

1. Natural languages are vast, containing an **infinity of different sentences**. New sentences can always be produced, regardless of how many a person has encountered.
2. Natural languages contain much **ambiguity**. Many words possess multiple meanings (e.g., _can, bear, fly, orange_), and sentences can take on different meanings depending on the context.

### 12.2 Overview of Linguistics

Linguistics provides the foundation for designing successful language understanding systems.

- **Sentence Structure:** The basic element of language is the **sentence**, which expresses a complete thought. A sentence must contain both a subject (what the sentence is about) and a predicate (what is said about the subject).
- **Word Types:** Words are categorized by their function, including nouns, pronouns, verbs, adjectives, adverbs, prepositions, conjunctions, and interjections.
- **Phrases:** Groups of words that act as a single unit within a sentence; these function as the building blocks for syntactic structures.

**Levels of Knowledge Used in Language Understanding**

A language understanding program requires considerable knowledge across multiple levels to function effectively:

1. **Phonological:** Knowledge relating sounds to the words recognized; the **phoneme** is the smallest unit of sound.
2. **Morphological:** Lexical knowledge concerning word constructions from **morphemes** (the smallest unit of meaning, e.g., constructing _friendly_ from _friend_ and _-ly_).
3. **Syntactic:** Knowledge of how words are structured to form grammatically correct sentences.
4. **Semantic:** Knowledge focused on the meanings of words and phrases and how they combine to create sentence meanings.
5. **Pragmatic:** High-level knowledge related to the use of sentences in specific contexts and how context influences meaning.
6. **World:** General knowledge a user needs to understand and maintain a conversation, including knowledge of the other person's beliefs and goals.

The overall process of understanding language is a series of transformations, from basic speech sounds to a complete set of internal representation structures. Understanding written language (textual input) is simpler than understanding speech, as speech processing requires additional facilities to handle noisy input signals.

**General Approaches to Natural Language Understanding** Historically, three main approaches have been used to develop NLP programs:

1. **Keyword and Pattern Matching:** The simplest approach, relying on sentence templates containing key words or phrases (e.g., used in early programs like ELIZA).
2. **Syntactic and Semantic Directed Analysis:** A popular approach where knowledge structures are built during a syntactical and semantic analysis of input sentences. Parsers analyze individual sentences to build structures that are then translated into knowledge formats.
3. **Scenario Representations (Scripts/Frames):** Relies on mapping input to prescribed primitives used to build larger knowledge structures based on constraints imposed by context and world knowledge. This approach bypasses much of the computational requirements of syntactical analysis.

### 12.3 Grammars and Languages

A **language L** is defined as a set of strings, finite or infinite, constructed by concatenating basic atomic elements called symbols. The finite set of these symbols is the **alphabet or vocabulary ($v$)**. Well-formed sentences are created using a set of rules known as a **grammar (G)**.

A grammar $G$ is formally specified as $G = (v_n, v_t, s, p)$, where:

- $v_n$ is the set of **nonterminal symbols** (symbols that can be decomposed, such as Noun Phrase (NP) or Verb Phrase (VP)).
- $v_t$ is the set of **terminal symbols** (symbols that cannot be decomposed further, such as nouns or verbs).
- $s$ is the **starting symbol**.
- $p$ is a finite set of **productions or rewrite rules**.

A **Phrase Marker (Parse Tree)** represents the structure of how a sentence is generated from a grammar.

**The Chomsky Hierarchy of Generative Grammars** Noam Chomsky defined four types of grammars:

|Type|Name|Characteristics|
|:--|:--|:--|
|**Type 0**|Most General|$\chi \nu \psi \rightarrow \chi \omega \psi$, where $\nu$ cannot be the empty string. Requires the computational power of a Turing machine to recognize.|
|**Type 1**|Context-Sensitive|Rules $X \rightarrow Y$ are permitted only if the length of $X$ is less than or equal to the length of $Y$.|
|**Type 2**|**Context-Free**|The left-hand side of a rule must be a single nonterminal symbol ($A \rightarrow \chi \nu \psi$). Formal programming languages are commonly based on these.|
|**Type 3**|Finite State or Regular|Most restrictive, rules are limited to forms such as $A \rightarrow aB$ or $A \rightarrow a$.|

**Extended Grammars**

- **Transformational Grammars:** Extensions of generative grammars used to address the issue of sentences with the same semantic content yielding different phrase marker structures (e.g., active vs. passive voice). These grammars use transformation rules (tree manipulation rules) to map the surface structure to a **deeper semantic structure**.
- **Case Grammars:** Focus on the **semantic role (case)** that a noun phrase plays relative to verbs and adjectives. A sentence is defined as $S \rightarrow M + P$, where $P$ is a proposition and $M$ is a modality constituent. **Case frames** are associated with verbs to define the required and optional cases.
- **Systemic Grammars:** Emphasize the **function and purpose** of language, incorporating context and pragmatics. Language is classified by ideational (content), interpersonal (purpose/mood), and textual (coherence) functions.
- **Semantic Grammars:** Encode semantic information directly into the grammar rules, replacing traditional nonterminals (NP, VP) with **semantic constituents** (e.g., _,_ ). This approach restricts the generated sentences, making it suitable for limited applications.

### 12.4 Basic Parsing Techniques

**Parsing** is the process of taking a sentence apart word-by-word to determine its structure from its constituent parts, essentially performing the inverse of the sentence generation process.

**The Lexicon** A **lexicon** is a dictionary containing syntactic, semantic, and potentially pragmatic information for words (usually root words or morphemes). This information is crucial for the parser to determine a word's function and meaning.

- Lexicon entries typically contain the root word (head), derivatives, and the roles (part of speech, sense) it can play in a sentence.
- The organization (alphabetical, frequency-based, or partitioned) is designed to facilitate searching and access.

**Transition Networks** Transition networks use directed graphs (digraphs) and finite state automata to represent formal and natural language structures.

- **Nodes** represent states in traversing a sentence, and **arcs** represent the necessary rules or test conditions for transition.
- A complete path through the network corresponds to the successful recognition of a permissible sentence structure. Simple transition networks, however, are severely limited in the variety of sentences they can recognize.

**Parsing Strategy**

- **Top-Down Parsing:** Starts by hypothesizing the sentence symbol ($S$) and successively predicting lower-level constituents until they match the input words. This approach is prediction-driven.
- **Bottom-Up Parsing:** Starts with the actual input words, replacing them with their syntactic categories, and then combining these categories into larger units until the starting symbol ($S$) is generated. This approach is data-driven.
- **Deterministic Parsers:** Allow only one choice of arc for each word category, often relying on look-ahead features to ensure a correct selection, as backtracking is not permitted.
- **Nondeterministic Parsers:** Permit multiple choices (same test on different arcs) from a given state, requiring the parser to guess and potentially backtrack if the choice leads to failure.

**Prolog Parsers** The similarity between rewrite rules and Horn clauses makes **PROLOG** a suitable language for writing basic parsers. For example, the grammar rule $S \rightarrow NP \ VP$ can be written in PROLOG as: `sentence(A,C) :- nounPhrase(A,B), verbPhrase(B,C)`. The arguments $A, B,$ and $C$ represent lists of words, tracking which words have been consumed during the parse.

**Recursive Transition Networks (RTNs)** RTNs extend simple transition networks by permitting arc labels to refer to **other networks** (or even the network's own name), leading to recursion.

- RTNs enable the parsing of complex sentences containing embedded phrases using relatively simple networks.
- When traversing an RTN, a record (a triple like POS CND RLIST) must be maintained to track the current word position, current node, and **return nodes** (stored on a stack RLIST).
- The **POP arc** is a dummy arc signaling the successful completion of a subnetwork and directing the interpreter to return control to the previously noted node.