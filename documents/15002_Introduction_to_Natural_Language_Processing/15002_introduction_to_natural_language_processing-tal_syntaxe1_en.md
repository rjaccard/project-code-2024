# Syntactic Parsing: <br> Introduction, CYK Algorithm 

## Syntactic level

Analysis of the sentence structure i.e. "grammatical" analysis (in the linguistic sense)

In automatic natural language processing, formal grammars and parsing theory two separated/complementary aspects:

| procedural <br> generic algorithms | declarative <br> data |
| :--- | :--- |
| parsing algorithm | formal grammar |

## Parsing

Parsing can be seen as:

- RECOGNIZING a sequence of words

$\Rightarrow$ Is a given sentence correct or not?

or as

- ANALYZING a sequence of words

$\Rightarrow$ For a syntactically correct sentence, give the set of all its possible interpretations.

(Returns the empty set for incorrect sentences)

## What is acceptable and what is not?

A sequence of words can be rejected for several different reasons:

- the words are not in the "right" order: cat the on sat the couch nice
- the rules defining what are the acceptable word orders in a given language are called "positional constraints"
    - related word pairs are not matching "right": cats eats mice
    - the rules defining what are the acceptable word pairs in a given language are called "selectional constraints" (e.g. "agreement rules")

It is not enough for a sequence of words to satisfy all positional and selectional constraints to be acceptable, see Chomsky's famous example: Colorless green ideas sleep furiously.

But the reason is different: the sequence is rejected because it is meaningless; indeed, how can something colorless be green ? or a sleep to be furious ?

As this type of problem is related to meaning, it will not be considered here; we will consider any sequence satisfying all positional and selectional constraints as acceptable; to avoid potential confusion, we will refer to such sequences as "syntactically acceptable".

## Where is the border?

- Syntactic acceptability is not as clear cut as one may think!
- The underlying hypothesis is that any syntactically acceptable sequence may possibly be given a meaning, even if this may require some context to guarantee that a large enough fraction of speakers indeed understand it as intended (which is crucial for any linguistic entity to be truly useful, but, maybe, in pure poetry)
- For example: What do you understand if one talks about a "small giant"?...


## Positional constraints

As already mentioned, positional constraints govern the word order in a language:

- the more such constraints, the more the language tends to be fixed order (e.g. French, German),
- the less, the more it tends to be free order (e.g. Latin, Italian)

For example: in English "girls like roses" is acceptable, while "girls roses like" or "like girls roses" are not.

## How to deal with selectional constraints?

As already mentioned, selectional constraints are taking into account constraints such as agreement rules that are further restricting the word sequences to be considered as (syntactically) acceptable

For example, in English "cats eat mice" is acceptable, while "cats eats mice" is not, because the number agreement between "cats" (plural) and "eats" (singular) is violated.

Agreement rules can be taken into account by preserving the required morpho-syntactic features in the PoS tags assigned to words (e.g. a number agreement will require to use PoS tags such as NOUNs (noun singular), NOUNp (noun plural), vERBs (verb singular), and VERBp (verb plural).

## What formalism?

- symbolic grammars / statistical grammars
- symbolic grammars:
- phrase-structure grammars (a.k.a constituency grammars, syntagmatic grammars) recursively decompose sentences into constituants, the atomic parts of which are words ("terminals").

Well suited for ordered languages, not adapted to free-order languages.

Better expresses structural dependencies.

- dependency grammars focus on words and their relations (not necessarly in sequence): functional role of words (rather than categories, e.g. "agent"/"actor" rather than "noun").

Dependency grammars provide simpler structures (with less nodes, 1 for each word, and less deep), but are less rich than phrase-structure grammars

Modern approach: combine both

## Formal phrase-structure grammars

A formal phrase-structure grammar $\mathcal{G}$ is defined by:

- A finite set $\mathcal{C}$ of "non-terminal" symbols
- A finite set $\mathcal{L}$ of "terminal" symbols
- The upper level symbol $S \in \mathcal{C}$
- A finite set $\mathcal{R}$ of rewriting rules syntactic categories words the "sentence" syntactic rules

$$
\mathcal{R} \subset \mathcal{C}^{+} \times(\mathcal{C} \cup \mathcal{L})^{*}
$$

In the NLP field, the following concepts are also introduced:

- lexical rules
- pre-terminal symbols or Part of Speech tags


## What kind of grammar for NLP?

Reminder: Chomsky's Hierarchy: complexity is related to the shape of the rules

| embeddings <br> crossings | language <br> class | grammar type | recognizer | complexity <br> $\mathcal{O}(n)$ |
| :---: | :---: | :---: | :---: | :---: |
|  | regular | $X \rightarrow w$ or <br> $X \rightarrow w Y$  <br> $($ type 3$)$  | FSA |  |
|  | context-free | $\underset{\text { (type 2) }}{X} \rightarrow Y_{1} \ldots Y_{n}$ | PDA | $\mathcal{O}\left(n^{3}\right)$ |
|  | context- <br> dependent | $\alpha \rightarrow \beta\|\alpha\| \leq\|\beta\|$ <br> (type 1) | ![](https://cdn.mathpix.com/cropped/2024_05_17_96f92d7bf392744fa3d9g-15.jpg?height=96&width=224&top_left_y=536&top_left_x=936) | exp. |
|  | recursively <br> enumerable | $\alpha \rightarrow \beta$ (type 0) | under | idable |

embedding: "The bear the dog belonging to the hunter my wife was a friend of bites howls"

crossing: "Diamonds, emeralds, amethysts are respectively white, green and purple"

real-life NLP constraints $\Rightarrow$ important limitations on complexity algorithms at most polynomial time complex

$\Rightarrow$ models actually used: context-free grammars (or midly context-sentive grammars)

Notice that in practice, higher level description formalisms might be used for developing the grammars, which are afterwards translated into CFG for practical use ("CF backbone").

## Context Free Grammars

A Context Free Grammar (CFG) $\mathcal{G}$ is (in the NLP framework) defined by:

- a set $\mathcal{C}$ of syntactic categories (called "non-terminals")
- a set $\mathcal{L}$ of words (called "terminals")
- an element $S$ of $\mathcal{C}$, called the top level category, corresponding to the category identifying complete sentences
- a proper subset $\mathcal{T}$ of $\mathcal{C}$, which defines the morpho-syntactic categories or "Part-of-Speech tags"
- a set $\mathcal{R}$ of rewriting rules, called the syntactic rules, of the form:

$$
X \rightarrow X_{1} X_{2} \ldots X_{n}
$$

where $X \in \mathcal{C} \backslash \mathcal{T}$ and $X_{1} \ldots X_{n} \in \mathcal{C}$

- a set $\mathcal{L}$ of rewriting rules, called the lexical rules, of the form:

$$
x \rightarrow w
$$

where $X \in \mathcal{T}$ and $w$ is a word of the language described by $\mathcal{G}$.

$\mathcal{L}$ is indeed the lexicon

## A simplified example of a Context Free Grammar 

- terminals: a, cat, ate, mouse, the
- PoS tags: N, V, Det
- non-terminals: S, NP, VP, N, V, Det
- rules:

$$
R_{1}: \quad S \rightarrow N P V P
$$

$$
\begin{array}{ll}
R_{2}: & \mathrm{VP} \rightarrow \mathrm{V} \\
R_{3}: & \mathrm{VP} \rightarrow \mathrm{V} \text { NP } \\
R_{4}: & \mathrm{NP} \rightarrow \operatorname{Det} \mathrm{N}
\end{array}
$$

## Syntactically Correct

A word sequence is syntactically correct (according to $\mathcal{G}$ ) $\Longleftrightarrow$ it can be derived from the upper symbol $S$ of $\mathcal{G}$ in a finite number of rewriting steps corresponding to the application of rules in $\mathcal{G}$.

Notation: $S \Rightarrow{ }^{*} w_{1} \ldots w_{n}$

Any sequence of rules corresponding to a possible way of deriving a given sentence $W=w_{1} \ldots w_{n}$ is called a derivation of $W$.

The set (not necessary finite) of syntactically correct sequences (according to $\mathcal{G}$ ) is by definition the language recognized by $\mathcal{G}$

A elementary rewriting step is noted: $\alpha \Rightarrow \beta$; several consecutive rewriting steps: $\alpha \Rightarrow^{*} \beta$ with $\alpha$ and $\beta \in(\mathcal{C} \cup \mathcal{L})^{*}$

Example: if as rules we have $X \rightarrow a, Y \rightarrow b$ and $Z \rightarrow c$, then for instance:

$$
\begin{array}{lll}
X Y Z \Rightarrow a Y Z & \text { and } & X Y Z \Rightarrow{ }^{*} a b c
\end{array}
$$

## Example

The sequence "the cat ate a mouse" is syntactically correct (according to the former example grammar)

|  | $S$ |
| :--- | :--- |
| $\overrightarrow{R_{3}}$ | $N P V P$ |
| $\overrightarrow{R_{4}}$ | Det $N V P$ |
| $\overrightarrow{L_{2}}$ | the $N V P$ |
| $\overrightarrow{L_{1}}$ | the cat $V P$ |
| $\overrightarrow{R_{3}}$ | the cat $V N P$ |
| $\overrightarrow{L_{5}}$ | the cat ate $N P$ |
| $\overrightarrow{R_{4}}$ | the cat ate $D e t$ |
| $\xrightarrow{L_{3}}$ | the cat ate a $N$ |
| $\xrightarrow{L_{4}}$ | the cat ate a mouse |

Its derivation is $\left(R_{1}, R_{4}, L_{2}, L_{1}, R_{3}, L_{5}, R_{4}, L_{3}, L_{4}\right)$

## Example (2)

The sequence "ate a mouse the cat" is syntactically wrong (according to the former example grammar)

|  | $S$ |
| :--- | :--- |
| $\xrightarrow{R 1}$ | $N P V P$ |
| $\xrightarrow{R 4}$ | $\operatorname{Det} N \mathrm{VP}$ |
| $\xrightarrow{x}$ | ate/Det $N \mathrm{VP}$ |

Exercise : Some colorless green ideas sleep furiously

Syntactically correct $\neq$ Semantically correct

## Syntactic tree(s) associated with a sentence

Each derivation of a sentence $W$ can be represented graphically in the form of a tree in which each rewriting rule is represented as a sub-tree of depth 1 : the root (resp. the leaves) corresponds (resp. correspond) to the left-hand side (resp. the right-hand side) of the rule.

Such a tree will be called a syntactic tree (or parse tree, or syntactic structure) associated to $W$ by $\mathcal{G}$.

## Mapping between trees and derivations

A priori, several derivations can correspond to the same tree

Example ("the cat ate a mouse"): $R_{1}, R_{4}, L_{2}, L_{1}, R_{3}, L_{5}, R_{4}, L_{3}, L_{4}$ (where the $N P$ is derived before the VP) and $R_{1}, R_{3}, L_{5}, R_{4}, L_{3}, L_{4}, R_{4}, L_{2}, L_{1}$ (where the VP is derived before the $N P$ ) correspond to the same tree

However, if, by convention, derivations are restricted to left-most derivations (i.e. derivations where rewriting rules are exclusively applied to the left-most non-terminal), there is a one-to-one mapping between derivations and parse trees.

Warning ! This is not true in general for grammars more complex than context-free grammars.

This property is one of the important properties of the CF grammars and will be used for their probabilization.

## Syntactic ambiguity

One of the major characteristics of natural languages (in opposition to formal languages) is that they are inherently ambiguous at every level of analysis.

For example, at the syntactic level:

- words are often associated with several parts-of-speech (for example "time" can be a verb or a noun).

This can lead to multiple syntactic interpretations corresponding to global structural ambiguities

Example: time flies like an arrow

- word attachments are often not completely constrained at syntactic level. This can lead to multiple syntactic interpretations corresponding to local structural ambiguities

Example: She ate a fish with a fork

## Syntactic parsing

One of the main advantages of the CFG formalism is that there exist several generic parsing algorithms that can recognize/analyze sentences in a computationally very efficient way (low polynomial worst case complexity).

efficient $==\mathcal{O}\left(n^{3}\right)$ worst case complexity

The two most famous of such algorithms are:

- the CYK (Cocke-Younger-Kasami) algorithm (first proposed in the early 60's)
- and the Earley parser (late 60's)


## The CYK algorithm

CYK is a bottom-up chart parsing algorithm characterized by 3 interesting features:

- its worst case parsing complexity is $\mathcal{O}\left(n^{3}\right)$ (where $n$ is the number of words of the sentence to be analyzed);
- a very simple algorithm that is easy to implement;
- it can provided partial analysis of syntactically correct subsequences of syntactically incorrect sequences.

However, its standard implementation suffers from two important drawbacks:

- the CF grammar used by the parser has to be in a predefined format (the Chomsky normal form) and therefore the grammar usually needs to be first converted into this predefined format;
- the complexity is always $\mathcal{O}\left(n^{3}\right)$ even when the grammer is in fact regular.


## CYK algorithm: basic principles

As it is usual for chart parsing algorithms, the CYK algorithm will compute in an efficient way all the possible syntactic interpretations of all the sub-sequences of the sequence to be analyzed.

Subsequences of the sentences are combined in a bottom-up fashion, using the rules present in the grammar.

How to prevent the space of possible combinations of subsequences from exploding?

$\Rightarrow$ Restrict the types of CFG's allowed.

## Chomsky Normal Form

Any context-free grammar can be converted into an equivalent Chomsky Normal Form (CNF) grammar

A CFG is in CNF if all its syntactic rules are of the form:

$$
X \rightarrow X_{1} X_{2}
$$

where $X \in \mathcal{C} \backslash \mathcal{T}$ and $X_{1}, X_{2} \in \mathcal{C}$

A context free grammar is in extended Chomsky Normal Form (eCNF) if all its syntactic rules are of the form:

$$
X \rightarrow X_{1} \text { or } X \rightarrow X_{1} X_{2}
$$

where $X \in \mathcal{C} \backslash \mathcal{T}$ and $X_{1}, X_{2} \in \mathcal{C}$

## Chomsky normal form: example

| R1: | $S$ | $\rightarrow$ | $N P V P$ | R1: | $S$ | $\rightarrow$ | $N P V P$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| R2: | $N P$ | $\rightarrow$ | $\operatorname{Det} N$ | R2: | $N P$ | $\rightarrow$ | $\operatorname{Det} N$ |
| R3: | $N P$ | $\rightarrow$ | Det N PNP | R3.1: | $N P$ | $\rightarrow$ | $X_{1} P N P$ |
|  |  |  |  | R3.2: | $X_{1}$ | $\rightarrow$ | Det $N$ |
| R4: | $P N P$ | $\rightarrow$ | Prep NP | R4: | $P N P$ | $\rightarrow$ | Prep NP |
| R5: | $V P$ | $\rightarrow$ | $V$ |  |  |  |  |
| R6: | $V P$ | $\rightarrow$ | $V N P$ | R6: | $V P$ | $\rightarrow$ | $V N P$ |
| R7: | $V P$ | $\rightarrow$ | $V N P P N P$ | R7.1: | $V P$ | $\rightarrow$ | $X_{2} P N P$ |
|  |  |  |  | R7.2: | $x_{2}$ | $\rightarrow$ | $V N P$ |
| L5: | $V$ | $\rightarrow$ | ate | L5.1: | $V$ | $\rightarrow$ | ate |
|  |  |  |  | L5.2: | VP | $\rightarrow$ | ate |

increases the number of non-terminals and the number of rules

## CYK algorithm: basic principles (2)

The algorithmically efficient organization of the computation is based on the following property:

if the grammar is in CNF (or in eCNF) the computation of the syntactic interpretations of a sequence $W$ of length / only requires the exploration of all the decompositions of $W$ into exactly two sub-subsequences, each of them corresponding to a cell in a chart. The number of pairs of sub-sequences to explore to compute the interpretations of $W$ is therefore $n-1$.

Idea: put all the analyses of sub-sequences in a chart

## CYK algorithm: basic principles (3)

The syntactic analysis of an $n$-word sequence $W=w_{1} \ldots w_{n}$ is organized into a half-pyramidal table (or chart) of cells $C_{i, j}(1 \leq i \leq n, 1 \leq j \leq n)$, where the cell $C_{i, j}$ contains all the possible syntactic interpretations of the sub-sequence $w_{j} \ldots w_{j+i-1}$ of $i$ words starting with the $j$-th word in $W$.

The computation of the syntactic interpretations proceeds row-wise upwards (i.e. with increasing values of $i$ ).

## Formal algorithm

1) Initialisation: fill first row with corresponding Part-of-Speech
2) Fill chart:
```
for all 2\leqi\leqn (row) do
    for all 1\leqj\leqn-i+1 (column) do
        for all 1\leqk\leqi-1 (decomposition) do
        for all X\inchart [i-k][j] do
            for all Y\in chart [k][i+j-k] do
                Add Z to chart[i][j]
```


## Analyzer or recognizer?

- The preceeding algorithm does not store the parse trees.

$\Rightarrow$ Recognizer (check wheter $S$ is in top cell or not) or, for an analyser, need to reconstruct the parse trees.

- For an analyzer, it's definitely better to store the parse trees in the chart while parsing:


## CYK algorithm: worst case complexity

As the computation of the syntactic interpretations of a cell $C_{i, j}$ requires $(i-1)$ explorations of pairs of cells $(1 \leq k \leq i-1)$, the total number of explorations is therefore

$$
\sum_{i=2}^{n} \sum_{j=1}^{n-i+1}(i-1)=\sum_{i=2}^{n}(n-i+1) \cdot(i-1) \in \mathcal{O}\left(n^{3}\right)
$$

A cell contains at most as many interpretations as the number $|\mathcal{C}|$ of syntactic categories contained in the grammar, the worst case cost of an exploration of a pair of cells corresponds therefore to $|\mathcal{C}|^{2}$ accesses to the grammar.

As cost of the access to the rules in the grammar can be made constant if efficient access techniques (based on hash-tables for example) are used, the worst case computational complexity of the analysis of a sequence of length $n$ is:

$$
\mathcal{O}\left(n^{3}\right) \text { and } \mathcal{O}\left(|\mathcal{C}|^{2}\right)
$$

We can here see one drawback of the CNF: $\mathcal{C}$ is increased.

There are modified versions of the CYK algorithm where CNF is no longer required $\mathcal{C}$ is then smaller): bottom-up chart parsing

Notice: Once the chart has been filled ( $O\left(n^{3}\right)$ complex), one parse tree of the input sentence can be extracted in $O(n)$.

PITFALL!! It is easy to implement this algorithm in such a way that the complexity becomes $\mathcal{O}(\exp n)!$

If indeed the non-terminals produced in a cell are duplicated (instead of factorizing their interpretations), their number can become exponential!

## Beyond CNF: bottom-up chart parting

Idea: get rid of (e)CNF constraint

How to? on-line binarization, when needed, during bottom-up analysis

Mainly:

- factorize (with respect to $\alpha$ ) all the partial derivations $X \rightarrow \alpha \bullet \beta \quad \alpha \bullet \ldots$ This is possible because processing bottom-up.

[ $\alpha$ and $\beta$ are (non-empty) sequences of non-terminals. ]

## Bottom-up Chart Parsing

More formally, a CYK algorithm in which:

- cells contain two kind of objects: $[\alpha \bullet \ldots, i, j]$ and $[X, i, j]$ respectively
- initialization consists in adding $[X, i, j]$ for all $X \rightarrow w_{i j} \in \mathcal{R}$ ( $w_{i j}$ is a sequence of tokens of the input sentence; see "Dealing with compounds" later slide)
- and the completion phase becomes: (association of two cells)

$$
[\alpha \bullet \ldots, i, j] \oplus[X, k, j+i] \Rightarrow \begin{cases}{[\alpha X \bullet \ldots, i+k, j]} & \text { if } Y \rightarrow \alpha X \beta \in \mathcal{R} \\ {[Y, i+k, j]} & \text { if } Y \rightarrow \alpha X \in \mathcal{R}\end{cases}
$$

("self-filling")

$$
[X, i, j] \Rightarrow \begin{cases}{[X \bullet \ldots, i, j]} & \text { if } Y \rightarrow X \beta \in \mathcal{R} \\ {[Y, i, j]} & \text { if } Y \rightarrow X \in \mathcal{R}\end{cases}
$$

