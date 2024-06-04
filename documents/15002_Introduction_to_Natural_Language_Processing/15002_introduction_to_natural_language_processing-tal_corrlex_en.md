# Out of Vocabulary forms

- Out of Vocabulary ( $\mathrm{OoV}$ ) forms matter: they occur quite frequently (e.g. $\simeq 10 \%$ in newspapers)

What do they consist of?

- spelling errors: foget, summmary, usqge, ...
- neologisms: Internetization, Tacherism, ...
- borrowings: gestalt, rendez-vous, ...
- forms difficult to exhaustively lexicalize: (numbers,) proper names, abbreviations, ...
- identification based on patterns is not well-adapted for all OoV forms

We will focus here on spelling errors, neologisms and borrowings

## Spelling errors and neologisms

- for spelling errors (resp. neologisms), distortions (resp. derivations) are modelled by transformations, i.e. rewriting rules (sometimes weighted)


## Example:

- Transposition (distortion): $\mathrm{XY} \rightarrow \mathrm{YX}[1.0]$

where $X$ and $Y$ stands for variables

- tripling (distortion): $\mathrm{XX} \rightarrow \mathrm{XXX} \quad[1.0]$
- name derivation: ize:INF $\rightarrow$ ization:N [1.0]
- a given lexicon (regular language) and a set of transformations define the edit space to be explored

The aim is to find the position of the OoV forms in the edit space with respect to known (lexicalized) forms (neighbourhoods, similarity, distance)

- if the transformation set is simple enough: automatic (or semi-automatic) learning of the transformation set is possible


## Borrowings

For borrowings, identification of the source language when no large coverage lexica are avalaible for the other languages, but only representative texts.

Decomposition into $n$-grams of characters.
Example: for trigrams

$$
\text { dribble } \rightarrow \text { (dri,rib,ibb,bbl,ble) }
$$

- From reference corpora, computation of a frequency matrix ( $n$-gram $\times$ language)
- Approximation of likelihood of a word to belong to a given language

Example for trigrams:

$$
P(\text { dribble } \mid L)=P(\text { dri } \mid L) \cdot \frac{P(\text { rib } \mid L)}{P(\text { ri } \mid L)} \cdot \ldots \cdot \frac{P(\mathrm{ble} \mid L)}{P(\mathrm{~b}|| L)}
$$

## Likelihood verus posterior probability

Why the likelihood $P(w \mid L)$ rather than the posterior probability $P(L \mid w)$ ?

- They are both hard to accurately model without further assumptions ( $w$ belongs to a huge set!)

but no further simplification can be made on $P(L \mid w): w$ is fixed (and there is nothing to gain "simplifying" $L$ !

$P(w \mid L)$ can be further simplified making assumptions on $w$

- Using the Bayes' rule:

$$
\underset{L}{\operatorname{Argmax}} P(L \mid w)=\underset{L}{\operatorname{Argmax}} P(w \mid L) \cdot P(L)
$$

- If you can accurately estimate $P(L)$, sure, make use of it!
- Otherwise, the least biaised hypothesis (maximum entropy) is to a priori assume that all languages are all equally possible: maximizing posterior probability is then the same as maximizing likelihood


## Probabilistic approach summarized 

Make (one more time!) use of $n$-grams

w: OoV token to be corrected

$c$ : candidate correction, out of $\mathcal{C}(w)$, set of possible candidates for $w$

$$
\underset{c \in \mathcal{C}(w)}{\operatorname{Argmax}} P(c \mid w)=\underset{c \in \mathcal{C}(w)}{\operatorname{Argmax}} P(c) \cdot P(w \mid c)
$$

$P(c)$ : language model ( $n$-grams of words/tokens; $n=1$ here, but could easily be extended to neighboring tokens ( $n>1$ then))

$P(w \mid c)$ : error model: edit distance and/or $m$-grams of characters

A usual (unexplicit?) assumption is that $P(w \mid c)$ is many orders of magnitude higher for smaller edit distance (than for higher): thus closer candidate are considereds first, leading to this simple algorithm:

- if $\mathcal{C}_{1}(w)$ is not empty, return $\operatorname{Argmax} P(c)$; $c \in \mathcal{C}_{1}(w)$
- (else) if $\mathcal{C}_{2}(w)$ is not empty, return $\operatorname{Argmax} P(c)$;

$$
c \in \mathcal{C}_{2}(w)
$$

- etc...

where $\mathcal{C}_{d}(w)$ is the set of candidates at distance $d$ from $w$

## Edit distance, also called Levenshtein distance

Distance between 2 forms $=$ minimal number of transformations to change one into the other

Example of transformations:

- insertion: exmple $\rightarrow$ example
- deletion: example $\rightarrow$ exmple
- substitution: exemple $\rightarrow$ example
- transposition: exmaple $\rightarrow$ example


## Computation of edit distance

Notations:

$X_{i}$ : $i$ th char of string $X$

$X_{i}^{j}:$ if $i \leq j$ : substring $X_{i}, \ldots, X_{j}$; empty string otherwise

Example: $X=$ castle

$$
X_{3}=\mathrm{s} \quad X_{4}^{6}=\mathrm{tle} \quad X_{1}^{4}=\mathrm{cast} \quad X_{1}^{0}=\varepsilon
$$

Computation of the distance $D(X, Y)$ by dynamic programming:

step by step in a chart $m$ where each cell $m_{i j}$ contains the distance between the two substrings $X_{1}^{i}$ and $Y_{1}^{j}$ :

$$
m_{i j}=D\left(X_{1}^{i}, Y_{1}^{j}\right)
$$

$$
\begin{array}{rlrl}
D\left(X_{1}^{0} ; Y_{1}^{j}\right)= & \mathrm{j} & & \text { initialization } \\
D\left(X_{1}^{i} ; Y_{1}^{0}\right)= & \mathrm{i} & \\
\hline D\left(X_{1}^{i} ; Y_{1}^{j}\right)= & D\left(X_{1}^{i-1} ; Y_{1}^{j-1}\right) & & \text { if } X_{i}=Y_{j} \text { (equality) } \\
= & 1+\min \left\{D\left(X_{1}^{i-2} ; Y_{1}^{j-2}\right),\right. & & \text { else if } i \geq 2 \text { and } j \geq 2 \\
& \left.D\left(X_{1}^{i-1} ; Y_{1}^{j}\right), D\left(X_{1}^{i} ; Y_{1}^{j-1}\right)\right\} \begin{array}{l}
\text { and } X_{i-1}=Y_{j} \text { and } X_{i}= \\
Y_{j-1} \quad \text { (transposition, dele- } \\
\text { tion, insertion) }
\end{array} \\
= & & \text { else (substitution, deletion, } \\
& & &
\end{array}
$$

Example, columnwise:

for all $i$ from 0 to $|X|$ (size of $X$ ) do

$$
m_{i 0}=i
$$

for all $j$ from 1 to $|Y|$ do

$$
m_{0 j}=j
$$

for all $i$ from 1 to $|X|$ do

if $X_{i}=Y_{j}$ then

$$
m_{i j}=m_{i-1, j-1}
$$

else if $i \geq 2$ and $j \geq 2$ and $X_{i-1}=Y_{j}$ and $X_{i}=Y_{j-1}$ then

$$
m_{i j}=1+\min \left\{m_{i-2, j-2} ; m_{i, j-1} ; m_{i-1, j}\right\}
$$

else

$$
m_{i j}=1+\min \left\{m_{i-1, j-1} ; m_{i, j-1} ; m_{i-1, j}\right\}
$$

Return $m_{|X|,|Y|}$
$\mathrm{D}$ (exmple;exemple)

|  |  | $\mathrm{e}$ | $\mathrm{x}$ | $\mathrm{e}$ | $\mathrm{m}$ | $\mathrm{p}$ | $\mathrm{I}$ | $\mathrm{e}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| $\mathrm{e}$ | 1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| $\mathrm{x}$ | 2 | 1 | 0 | 1 | 2 | 3 | 4 | 5 |
| $\mathrm{m}$ | 3 | 2 | 1 | 1 | 1 | 2 | 3 | 4 |
| $\mathrm{p}$ | 4 | 3 | 2 | 2 | 2 | 1 | 2 | 3 |
| $\mathrm{l}$ | 5 | 4 | 3 | 3 | 3 | 2 | 1 | 2 |
| $\mathrm{e}$ | 6 | 5 | 4 | 3 | 4 | 3 | 2 | 1 |

$\mathrm{D}$ (exmaple;example)

|  |  | $\mathrm{e}$ | $\mathrm{x}$ | $\mathrm{a}$ | $\mathrm{m}$ | $\mathrm{p}$ | $\mathrm{l}$ | $\mathrm{e}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| $\mathrm{e}$ | 1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| $\mathrm{x}$ | 2 | 1 | 0 | 1 | 2 | 3 | 4 | 5 |
| $\mathrm{m}$ | 3 | 2 | 1 | 1 | 1 | 2 | 3 | 4 |
| $\mathrm{a}$ | 4 | 3 | 2 | 1 | 1 | 2 | 3 | 4 |
| $\mathrm{p}$ | 5 | 4 | 3 | 2 | 2 | 1 | 2 | 3 |
| $\mathrm{l}$ | 6 | 5 | 4 | 3 | 3 | 2 | 1 | 2 |
| $\mathrm{e}$ | 7 | 6 | 5 | 4 | 4 | 3 | 2 | 1 |

## Spelling error correction using a FSA

Problem: approximative search of lexicalized (surface) forms $=$ within a max. distance range

i.e. Fault-tolerant recognition (within a regular language):

Find all ending paths such that the corresponding string is within a distance range less than $\underline{\theta}$ of the given input string.

## Finite-State Automata (FSA)

Formally:

- $Q:($ finite) set of states
- $\Sigma:$ (finite) alphabet
- $\delta$ : arcs (mapping from $Q \times \Sigma$ to $Q$ )
- $q_{0} \in Q:$ inital state
- $F \subset Q:$ final states

Interface:

- initialState(): provides $q_{0}$
- $(q, a)=$ nextAfter $(p, c)$ : returns next state and character

Formally: returns $\operatorname{Argmin}_{\alpha}\{(q, \alpha) \in Q \times \Sigma$ such that $\alpha>c$ and $\delta(p, \alpha)=q\}$

- isFinal $(p)$ : are we done with $p$ ? Checks whether $p \in F$ or not.


## Pruning criteria: cut-off edit distance

$$
\begin{gathered}
D_{c}\left(X_{1}^{n}, Y_{1}^{m}\right)=\min _{I(m) \leq i \leq J(m)} D\left(X_{1}^{i} ; Y_{1}^{m}\right) \\
I(m)=\min (n, \max (1, m-\theta)) \quad J(m)=\min (n, \max (1, m+\theta))
\end{gathered}
$$

Important property:

$$
D_{c}(X, Y)>\theta \Longrightarrow \forall Z D(X, Y+Z)>\theta
$$

## Prefix-compatible Depth-first version

Input: a string to be corrected $(X)$, a lexicon in the form of a FSA and a maximal error

threshold $(\theta)$

$$
\operatorname{Push}\left(\varepsilon, \varepsilon, q_{0}\right)
$$

while Stack is not empty do

$$
\begin{aligned}
& \operatorname{Pop}(Z, c, p) \\
& (q, a)=\text { nextAfter }(p, c) \\
& \text { if }(q, a) \neq \emptyset \text { then } \\
& \quad \text { Push }(Z, a, p) \\
& \quad Y \leftarrow Z+a \\
& \quad \text { if } D_{c}(X, Y) \leq \theta \text { then }
\end{aligned}
$$

$$
\operatorname{Push}(Y, \varepsilon, q)
$$

$$
\text { if isFinal }(q) \text { and } D(X, Y) \leq \theta \text { then }
$$

