# PROBABILISTIC PARSING 

## Parsing: probabilisitic approach

- Linguistic resources needed for semantic/pragmatic models, even for more sophisiticated syntactic models, are hard to obtain/create
- Extension of (simple) standard syntactic models
- to be able to make choices among sentences/structures (in case of ambiguity)
- Automatic Learning of models from corpora


### What does it mean to "probabilize"?

- Implicitly represent the linguistic constraints that we do not want to or do not know how to integrate into the models:
- Set of linguistic phenomena that cannot or are hard to express in operational terms but that still are possible to evaluate (on corpora)
- The probability is then a measure of the quality of the adequation between the sentence/structure and the underlying model


## WHAT is "probabilized"?

The point of view is different depending on whether the syntactic model is used as a recognizer or as an analyzer

- A recognizer in only able to tell whether the input sentence is correct or not
- An analyzer is more complex and produces additional information for the correct sentences: a structure representing the syntactic organization of the words.

Notice: Although in principle probabilities have no reason to depend on the formal description of the language they are associated with, their operational definition in practice can hardly be build independently of the generative model defining the language (i.e. the grammar)

### General scheme of realization of probabilistic model:

- Identify the probability to estimate: $P\left(W_{1} \ldots W_{n}\right)$ or $P\left(A \mid W_{1} \ldots W_{n}\right)$ on the basis of linguistic hypotheses, express this probability by restricted number of parameters: $P=f\left(p_{1} \ldots p_{k}\right)$
- On the basis of a well defined corpora, estimate retained parameters in order to be able to compute probabilities
- One possible probabilization of a language: estimate probabilities of sequences of words by their occurrence frequencies in a reference corpus
- For an accurate estimation, huge amounts of data are required
- Reducing the number of parameters: estimate probabilities of fixed-size sequences ( $N$-grams) and then approximate the probabilities of a longer sequence on the basis of these parameters:

$$
P\left(w_{1}, \ldots, w_{n}\right)=P\left(w_{1}, \ldots, w_{N-1}\right) \cdot \prod_{i=N}^{n} P\left(w_{i} \mid w_{i-N+1}, \ldots, w_{i-1}\right)
$$

Example: $(N=2)$ - the cat ate a mouse
-> (the cat) (cat ate) (ate a) (a mouse) (ate mouse) (mouse a) (a cat) (cat the)

## SCFG: Summary

A Stochastic Context-Free Grammar is

- a CFG for which
- each rule $R$ is associated with a stochastic coefficient $p(R)$ such that
    - $-0 \leq p(R) \leq 1$
    - $-\sum_{R^{\prime}: \operatorname{left}\left(R^{\prime}\right)=\operatorname{left}(R)} p\left(R^{\prime}\right)=1$
    - $P\left(T=R_{0} \circ \ldots \circ R_{n}\right)=\prod_{i=0}^{n} p\left(R_{i}\right)$


## Notations

For a context-free grammar $\mathcal{G}$ we will use the following notations:

$\mathcal{L}(\mathcal{G})$ the language recognized by $\mathcal{G}$

$\mathcal{R}(\mathcal{G})$ the set of rules of $\mathcal{G}$

$\mathcal{A}(\mathcal{G})$ the set of partial trees of $\mathcal{G}$ (with root $\mathrm{S}$ )

$\mathcal{T}(\mathcal{G})$ the set of complete trees of $\mathcal{G}$

For a tree $T$ of $\mathcal{A}(\mathcal{G}), r(T)$ will denote its root, $F(T)$ the ordered sequences of its leaves and $\operatorname{lmnt}(T)$ the lest-most non-terminal leave of $T$. If $T$ does not have any non-terminal leave, $\operatorname{lmnt}(T)=\varepsilon$

$$
\begin{aligned}
& F(T)=\{\text { the, cat, } \mathrm{V}, \mathrm{PNP}\} \\
& \text { and } \operatorname{Imnt}(T)=\mathrm{V}
\end{aligned}
$$

Furthermore, the same notation $R$ will be used for both the rule and the corresponding elementary tree:

$$
N P \rightarrow \text { Det N }
$$

The symbol o denotes the internal composition rule on $\mathcal{A}(\mathcal{G})$ that returns the tree resulting from the substitution of the left-most non-terminal leave of the left tree by the right tree when it is possible, and $\varepsilon$ if not.

For a rule $R$ of $\mathcal{R}(\mathcal{G})$, left $(R)$ denotes the left-hand side of $R$

## SCFG

Desambiguation: Let $\mathcal{G}$ be a Stochastic CFG and $W=w_{1}^{n}$ a sentence with several interpretations $T_{1}, \ldots, T_{k}$ according to $\mathcal{G}$. The goal is to choose among the $T_{i} \mathrm{~s}$. In a standard approach, such a choice is made on semantic/pragmatic criteria In the probabilistic approach, the choice is made according to the probabilities of the $T_{i}$ trees. In other terms, we are looking for:

$$
T=\underset{T_{i} \supset W}{\operatorname{Argmax}} P\left(T_{i} \mid W\right)
$$

But $P\left(T_{i} \mid W\right)=\frac{P\left(T_{i}, W\right)}{P(W)}=\frac{P\left(T_{i}\right)}{P(W)}$ since $T_{i}$ precisely is a tree that analyses $W$

We are therefore looking for $T=\operatorname{Argmax} P\left(T_{i}\right)$

$$
T_{i} \supset W
$$

## SCFG: formalization

$T_{i}$ is interpreted as the result of a given (unknown) stochastic process $\xi$

because of the one-to-one mapping that exists in CFG between trees and derivations (sequences of rules), $\xi$ is supposed to be a stochastic process on rules, i.e a random sequence in $\mathcal{R}(\mathcal{G})$

We will therefore characterize $P(T)$ using $P\left(\xi=R_{0}, \ldots, R_{n}\right)$

$$
P\left(\xi=R_{0}, \ldots, R_{n}\right)=P\left(R_{0}\right) \cdot \prod_{i=1}^{n} P\left(R_{i} \mid R_{1}, \ldots, R_{i-1}\right)
$$

## Definition of $\xi$

To fully define $\xi$ we need the definition of $P\left(R_{0}\right)$ and $P\left(R_{i} \mid R_{1}, \ldots, R_{i-1}\right)$ :

- $R_{0}$ is the constant "random" variable $\mathrm{S}$ (null-depth tree with root $\mathrm{S}$, the start-symbol) Therefore $P\left(R_{0}=\mathrm{S}\right)=1$
- $P\left(R_{i} \mid R_{0}, \ldots, R_{i-1}\right)$ is null if left $\left(R_{i}\right) \neq \operatorname{Imnt}\left(R_{0} \circ \ldots \circ R_{i-1}\right)$

What value for the probability when it is not zero?

## Value for $P\left(R_{i} \mid R_{0}, \ldots, R_{i-1}\right)$

As up to now, this probability is conditioned by left $\left(R_{i}\right)=\operatorname{mnt}\left(R_{0} \circ \ldots \circ R_{i-1}\right)$ If we make the assumption that it is conditioned ONLY by this, then

$$
P\left(R_{i} \mid R_{0}, \ldots, R_{i-1}\right)=P\left(R_{i} \mid \operatorname{mnt}\left(R_{0} \circ \ldots \circ R_{i-1}\right)\right)=P\left(R_{i} \mid \operatorname{left}\left(R_{i}\right)\right)
$$

which therefore only depends on $R_{i}$ and will be denoted by $p\left(R_{i}\right)$. It is called the "stochastic coefficient" of the rule $R_{i}$

$p\left(R_{i}\right)$ is a parameter of the processus $\xi$ and, by construction, we have:

$\forall R \in \mathcal{R}(\mathcal{G}) \quad \sum_{R^{\prime} \in \mathcal{R}(\mathcal{G}): \operatorname{left}\left(R^{\prime}\right)=\operatorname{left}(R)} p\left(R^{\prime}\right)=1$

Notice that limiting $P\left(R_{i} \mid R_{0} \ldots R_{i-1}\right)$ to the conditioning by $P\left(R_{i} \mid \operatorname{mnt}\left(R_{0} \circ \ldots \circ R_{i-1}\right)\right)$ only is a strongly restrictive hypothesis on the processus

## Probability of a tree?

Finaly, the probability of a (valid) sequence of rules is:

$$
P\left(R_{0}, \ldots, R_{n}\right)=\prod_{i=1}^{n} p\left(R_{i}\right)
$$

Each $T$ in $\mathcal{T}(\mathcal{G})$ corresponds to a unique (valid) sequence of rules, therefore

$$
P(T)=P\left(R_{0}, R_{1}, \ldots, R_{k}\right)=\prod_{i=1}^{k} p\left(R_{i}\right)
$$

In short: For SCFGs, the probability of a tree is the product of the stochastic coefficient associated to its rules

BUT... is it really a probabilty on $T(\mathcal{G}) ? \ldots$

What is $\sum_{T \in T(\mathcal{G})} P(T)$ ?

- It converges
- towards a limit lower or equal to 1
- But that can be $<1$
Example:
$S \rightarrow S S(p)$
$S \rightarrow a(1-p)$

Therefore the correct probabilization is:

$$
\widehat{P}(T)=\frac{P(T)}{\sum_{T \in T(\mathcal{G})} P(T)}
$$

In the case where the grammar is consistent (i.e. $\sum P(A)=1$ ) (or in the case where only the maximum probability is considered), the two approches are equivalent. The only problematic case here is when one deals simultaneously with several not consistent grammars.

## Probability of a sentence $P(W)$

The probability of a sentence is defined by:

$$
P(W)=\sum_{\substack{T \in T(\mathcal{G}): \\ F(T)=W}} \widehat{P}(T)
$$

Notice that $P(T, W)=\widehat{P}(T) \cdot \delta(W=F(T))$ (Kronecker notation) which justifies the formulas used at the beginning of the course

## SCFG: Implementation

It is possible to compute $\operatorname{Argmax} P\left(T_{i}\right)$ and/or $P(W)=\sum P\left(T_{i}\right)$ during the bottom-up phase of the CYK analysis, using dynamic programming

For a given element in a cell, a value $v_{i}$ representing the maximum (or the sum) of the probabilities of its interpretations is stored

Notice:

$$
\begin{aligned}
P(X) & =\prod p\left(R_{i}\right) \\
& =p(R) \cdot P_{1} \cdots P_{n}
\end{aligned}
$$

When a new interpretation of element $i$ is build (by composition of elements $j$ and $k$ ), the value $v_{i}$ is updated according to:

$$
\begin{aligned}
v_{i} & =\max \left(v_{i}, v_{j} v_{k} \rho_{i}\right) \\
\text { (or) } \quad v_{i} & =v_{i}+v_{j} v_{k} \rho_{i}
\end{aligned}
$$

with $\rho_{i}=1 \quad$ if element $i$ is a item $[\alpha \bullet \ldots]$

and $\rho_{i}=p\left(R_{k}\right)$ if element $i$ is a non-terminal obtained by applying rule $R_{k}$

The initial value for the $v_{i} s$ is 0

## Grammar extraction from a treebank

Let us consider that a treebank made of the following parse trees is available:

From the trees present in the corpus, we can extract the context-free grammar $G$, made of the following 15 rules:

| rule | $p_{i}$ |
| :---: | :---: |
| $r_{1}: \mathrm{S}->\mathrm{NP} \mathrm{VP}$ | $p_{1}$ |
| $r_{2}: \mathrm{S}$-> NP NP PNP | $p_{2}$ |
| $r_{3}$ : PNP -> Prep NP | $p_{3}$ |
| $r_{4}: \mathrm{VP}->\mathrm{V} \mathrm{NP}$ | $p_{4}$ |
| $r_{5}:$ NP $->$ NP0 | $p_{5}$ |
| $r_{6}:$ NP $->$ NPO PNP | $p_{6}$ |
| $r_{7}:$ NPO $->$ Det N | $p_{7}$ |


| rule | $p_{i}$ |
| :--- | ---: |
| $r_{8}:$ Det -> the | $p_{8}$ |
| $r_{9}:$ Det -> a | $p_{9}$ |
| $r_{10}: \mathrm{N}->$ boy | $p_{10}$ |
| $r_{11}: \mathrm{N}->$ barrel | $p_{11}$ |
| $r_{12}: \mathrm{N}->$ truck | $p_{12}$ |
| $r_{13}: \mathrm{N}->$ cap | $p_{13}$ |
| $r_{14}:$ V -> delivers | $p_{14}$ |
| $r_{15}:$ Prep -> with | $p_{15}$ |

where the $p_{i}$ denote the probabilities associated with each of the rules

## Estimating the probabilities

supervised learning: When a tree-bank (annotated corpus) is available, stochastic coefficients are estimated by the relative frequencies (maximum likelihood estimation):

$$
p(R)=\frac{\text { nb. occurrences of } R}{R^{\prime} \text { such that left }\left(R^{\prime}\right)=\operatorname{left}(R)}
$$

unsupervised learning: When only text is available (and also a grammar) : EM estimation of the coefficients : inside-outside algorithm

- iterative algorithm
- converges towards a local minimum
- highly sensitive to initial values

hybrid approaches: using a (small) tree-bank and a (large) corpus of text

## Keypoints

- Probabilities of SCFGs are implicit linguistic constraints serving as measures of the adequation between the sentence and the model
- $\rightarrow$ The role of probabilities is to identify the correctness of the sentence and eventually to choose one interpretation among several
- $\rightarrow$ Calculation of probabilities of syntactic interpretations of sentences
- $\rightarrow$ Estimation of probabilities of SCFGs from training corpora

