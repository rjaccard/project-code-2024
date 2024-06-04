# Examples of syntactic ambiguities

## Syntactic ambiguity 

As the syntactic ambiguity of a given sentence $W$ will be expressed through the association to $W$ of several syntactic structures, grammars used to describe natural languages need to be ambiguous.

This corresponds to a major difference with the grammars that are usually used for formal languages (e.g. programming languages) and have fundamental consequences on the algorithmic complexity of the parsers (i.e. syntactic analyzers) that are designed for Natural Language Processing.

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

$$
w_{1} w_{2} \ldots w_{i} \ldots w_{p} w_{d r_{1}} \ldots . . w_{x}
$$

How to prevent the space of possible combinations of subsequences from exploding? $\Leftrightarrow$ Restrict the types of CFG's allowed.

## Chomsky Normal Form

$$
w_{n} w_{2} \ldots w_{n}
$$

Any context-free grammar can be converted into an equivalent Chomsky Normal Form (CNF) grammar-only.

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

## CYK algorithm: basic principles

The algorithmically efficient organization of the computation is based on the following property:

if the grammar is in CNF (or in eCNF) the computation of the syntactic interpretations of a sequence $W$ of length $n$ only requires the exploration of all the decompositions of $W$ into exactly two sub-subsequences, each of them corresponding to a cell in a chart. The number of pairs of sub-sequences to explore to compute the interpretations of $W$ is therefore $n-1$.

The syntactic analysis of an $n$-word sequence $W=w_{1} \ldots w_{n}$ is organized into a half-pyramidal table (or chart) of cells $C_{i, j}(1 \leq i \leq n, 1 \leq j \leq n)$, where the cell $C_{i, j}$ contains all the possible syntactic interpretations of the sub-sequence $w_{j} \ldots w_{i+i-1}$ of $i$ words starting with the $j$-th word in $W$.

$$
x \in c_{i j}: \sum_{w_{j}}^{\cdots} \sum_{w_{j+i-1}}^{x} \omega_{j, \cdots} w_{j \mu_{i-1}^{\prime}}
$$

The computation of the syntactic interpretations proceeds row-wise upwards (i.e. with increasing values of $i$ ).

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

There are modified versions of the CYK algorithm where CNF is no longer required ( $\mathcal{C}$ is then smaller): bottom-up chart parsing

Notice: Once the chart has been filled ( $O\left(n^{3}\right)$ complex), one parse tree of the input sentence can be extracted in $O(n)$.

PITFALL!! It is easy to implement this algorithm in such a way that the complexity becomes $\mathcal{O}(\exp n)!$

If indeed the non-terminals produced in a cell are duplicated (instead of factorizing their interpretations), their number can become exponential!

