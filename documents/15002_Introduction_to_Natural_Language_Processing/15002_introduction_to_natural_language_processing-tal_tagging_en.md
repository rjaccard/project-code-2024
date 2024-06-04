# Part of Speech Tagging 

## Morpho-lexical level

Aims:

- resolution of some ambiguities (e.g. can:V .vs. can:N)
- suppression of some lexical variability which is not necessarily meaningful for certain applications

(e.g. difference between "cat" and "cats"in Information Retrieval).

Tools:

- Part-of-Speech tagging
- Stemming / Lemmatization


## Lemmatization

- Automatically reduce word form to their canonical form, within context canonical form: infinitive for verbs, singular for nouns, (masculin) singular for adjectives, $\ldots$

Example:

$$
\begin{aligned}
& \text { executes } \longrightarrow \text { execute } \\
& \text { bought } \longrightarrow \text { buy }
\end{aligned}
$$

. Lemmatization is easy if PoS tagging has been performed (and lemma information is available in the lexicon)

Otherwise: "stemming" (mostly known for English: Porter's stemmer): basically, encoding most significative morphological rules

## Part-of-Speech Tagging (definition) 

Automatically assign Part-of-Speech (PoS) Tags to words in context.
Non trivial task because of lexical ambiguities:

$$
\begin{aligned}
& \text { process } \longrightarrow \vee \text { or } \mathrm{N} \text { ? } \\
& \text { programs } \longrightarrow \mathrm{N} \text { or } \mathrm{V} \text { ? }
\end{aligned}
$$

and of $\mathrm{OoV}$ forms (neologisms, proper nouns mainly).

$\Longrightarrow$ Two main components:

- guesser: assign PoS tag list to OoV
- chooser/disambiguator


## PoS tagging (formalisation)

Given a text and a set of possible (word, tag) couples (a.k.a. the vobulary/lexicon), choose among the possible tags for each word (known or unknown) the right one according to the context.

Implies that the assertion "the right one according to the context" is properly defined $(\rightarrow$ goldstandard), e.g. means "as given by a human expert" (!! inter-annotator agreement).

Several approaches:

- (old) Rule-based: Brill's tagger
- Probabilistic: Hidden Markov Models (HMM), Conditionnal Random Fields (CRF), Maximum entropy cyclic dependency network (MaxEnt)
- "Neural" (also probabilistic, but less clearly): averaged perceptrons, Support-Vector Machines (SVM), Long Short-Term Memory (LSTM)


## PoS tagging (example)

Tags explained (from original Brown Corpus documentation):

| Tag | Description | Examples |
| :--- | :--- | :--- |
| AT | article | the, an, no, a, every $[\ldots]$ |
| NN | noun, singular, common | failure, burden, court, fire [...] |
| VBZ | verb, present tense, 3rd <br> person singular | deserves, believes, receives, takes, [...] |
| JJ | adjective | recent, over-all, possible, hard-fought [...] |
| IN | preposition | of, in, for, by, considering [...] |
| QL | qualifier, pre | well, less, very, most $[\ldots]$ |
| . | sentence terminator | .$? ;!:$ |

## Tag sets

Complexity/Grain of tag set can vary a lot (even for the same language).

Original Brown Corpus tagset contains 87 PoS tags (!)

For instance, it contains 4 kind of adjectives:

| JJ | adjective | recent, over-all, possible, hard-fought [...] |
| :--- | :--- | :--- |
| JJR | comparative adjective | greater, older, further, earlier [...] |
| JJS | semantically superlative <br> adjective | top, chief, principal, northernmost [...] |
| JJT | morphologically superla- <br> tive adjective | best, largest, coolest, calmest [...] |
|  |  |  |

## Tag sets (2/2)

NLTK "universal" tagset is much shorter : 12 tags (from NLTK documentation):

| Tag | Meaning | Examples |
| :--- | :--- | :--- |
| ADJ | adjective | new, good, high, special, big, local |
| ADP | adposition | on, of, at, with, by, into, under |
| ADV | adverb | really, already, still, early, now |
| CONJ | conjunction | and, or, but, if, while, although |
| DET | determiner, article | the, a, some, most, every, no, which |
| NOUN | noun | year, home, costs, time, Africa |
| NUM | numeral | twenty-four, fourth, 1991, 14:24 |
| PRT | particle | at, on, out, over per, that, up, with |
| PRON | pronoun | he, their, her, its, my, l, us |
| VERB | verb | is, say, told, given, playing, would |
| . | punctuation marks | ., ; ! |
| X | other | ersatz, esprit, dunno, gr8, univeristy |

## Probabilistic PoS tagging

Let $w_{1}^{n}=w_{1} \ldots w_{n}$ be a sequence of $n$ words.

Tagging $w_{1}^{n}$ consists in looking a corresponding sequence of Part-of-Speech (PoS) tags $T_{1}^{n}=T_{1} \ldots T_{n}$ such that the conditionnal probability $P\left(T_{1}, \ldots, T_{n} \mid w_{1}, \ldots, w_{n}\right)$ is maximal

## Example:

Sentence to tag: Time flies like an arrow

Set of possible PoS tags: $\mathscr{T}=\{$ Adj, Adv, Det, $\mathrm{N}, \mathrm{v}, \ldots, \mathrm{WRB}\}$

Probabilities to be compared (find the maximum):

$P($ Adj Adj Adj Adj Adj|time flies like an arrow)

$P(\operatorname{Adj} A d j$ Adj Adj Adv|time flies like an arrow)

$\vdots$

$P($ Adj $\mathrm{N} V$ Det $\mathrm{N} \mid$ time flies like an arrow)

$P(\mathrm{~N}$ V Adv Det N|time flies like an arrow)

$P$ (WRB WRB WRB WRB WRB|time flies like an arrow)

## Probabilistic PoS tagging

Let $w_{1}^{n}=w_{1} \ldots w_{n}$ be a sequence of $n$ words.

Tagging $w_{1}^{n}$ consists in looking a corresponding sequence of Part-of-Speech (PoS) tags $T_{1}^{n}=T_{1} \ldots T_{n}$ such that the conditionnal probability $P\left(T_{1}, \ldots, T_{n} \mid w_{1}, \ldots, w_{n}\right)$ is maximal

How to find $\widetilde{T_{1}^{n}}=\underset{\operatorname{argmax}^{2}}{ } P\left(T_{1}^{n} \mid w_{1}^{n}\right)$ ?

Bayes Rule:

$$
P\left(T_{1}^{n} \mid w_{1}^{n}\right)=\frac{P\left(w_{1}^{n} \mid T_{1}^{n}\right) \cdot P\left(T_{1}^{n}\right)}{P\left(w_{1}^{n}\right)}
$$

As maximization is performed for a given $w_{1}^{n}$,

$$
\underset{T_{1}^{n}}{\operatorname{argmax}} P\left(T_{1}^{n} \mid w_{1}^{n}\right)=\underset{T_{1}^{n}}{\operatorname{argmax}}\left(P\left(w_{1}^{n} \mid T_{1}^{n}\right) \cdot P\left(T_{1}^{n}\right)\right)
$$

Furthermore (chain-rule):

$$
\begin{aligned}
P\left(w_{1}^{n} \mid T_{1}^{n}\right) & =P\left(w_{1} \mid T_{1}^{n}\right) \cdot P\left(w_{2} \mid w_{1}, T_{1}^{n}\right) \cdot \ldots \cdot P\left(w_{n} \mid w_{1}^{n-1}, T_{1}^{n}\right) \\
P\left(T_{1}^{n}\right) & =P\left(T_{1}\right) \cdot P\left(T_{2} \mid T_{1}\right) \cdot \ldots \cdot P\left(T_{n} \mid T_{1}^{n-1}\right)
\end{aligned}
$$

## Hypotheses:

- limited lexical conditioning

$$
P\left(w_{i} \mid w_{1}, \ldots, w_{i-1}, T_{1}, \ldots, T_{i}, \ldots, T_{n}\right)=P\left(w_{i} \mid T_{i}\right)
$$

- limited scope for syntactic dependencies: $k$ neighbors

$$
P\left(T_{i} \mid T_{1}, \ldots, T_{i-1}\right)=P\left(T_{i} \mid T_{i-k}, \ldots, T_{i-1}\right)
$$

Therefore:

$$
\begin{gathered}
P\left(w_{1}^{n} \mid T_{1}^{n}\right)=P\left(w_{1} \mid T_{1}\right) \cdot \ldots \cdot P\left(w_{n} \mid T_{n}\right) \\
P\left(T_{1}^{n}\right)=P\left(T_{1}^{k}\right) \cdot P\left(T_{k+1} \mid T_{1}, \ldots, T_{k}\right) \cdot \ldots \cdot P\left(T_{n} \mid T_{n-k}, \ldots, T_{n-1}\right)
\end{gathered}
$$

and eventually:

$$
P\left(w_{1}^{n} \mid T_{1}^{n}\right) \cdot P\left(T_{1}^{n}\right)=P\left(w_{1}^{k} \mid T_{1}^{k}\right) \cdot P\left(T_{1}^{k}\right) \cdot \prod_{i=k+1}^{i=n}\left(P\left(w_{i} \mid T_{i}\right) \cdot P\left(T_{i} \mid T_{i-k}^{i-1}\right)\right)
$$

This model corresponds to a $k$-order Hidden Markov Model (HMM)

## (order 1) Hidden Markov Models (HMM)

A order-1 HMM is, for PoS-tagging:

- a set of states $\mathscr{C}=\left\{C_{1}, \ldots, C_{m}\right\}$
- PoS tags $\mathscr{T}=\left\{t^{(1)}, \ldots, t^{(m)}\right\}$
- a transition probabilities matrix $\mathbf{A}$ :

$$
a_{i j}=P\left(Y_{t+1}=C_{j} \mid Y_{t}=C_{i}\right) \text {, shorten } P\left(C_{j} \mid C_{i}\right) \quad P\left(T_{i+1} \mid T_{i}\right)
$$

- an initial probabilities vector $I$ :

$$
\begin{equation*}
I_{i}=P\left(Y_{1}=C_{i}\right) \text { or } P\left(Y_{t}=C_{i} \mid \text { "start"), shorten } P_{/}\left(C_{i}\right)\right. \tag{1}
\end{equation*}
$$

- s a set of "observables" $\Sigma$ (not necessarily discreate, in general)

$$
\mathscr{L}=\left\{a^{(1)}, \ldots, a^{(L)}\right\}
$$

- $m$ probability densities on $\Sigma$, one for each state (emission probabilities): $B_{i}(0)=P\left(X_{t}=o \mid Y_{t}=C_{i}\right)$ (for $\left.o \in \Sigma\right)$, shorten $P\left(o \mid C_{i}\right)$


## Example: PoS tagging with HMM

Example: Time flies like an arrow

Example of HMM model:

- PoS tags: $\mathscr{T}=\{A d j, A d v, D e t, N, V, \ldots\}$
- Transition probabilities:

$$
\begin{aligned}
& P(\mathrm{~N} \mid \text { Adj })=0.1, P(\mathrm{~V} \mid \mathrm{N})=0.3, P(\operatorname{Adv} \mid \mathrm{N})=0.01, P(\operatorname{Adv} \mid \mathrm{V})=0.005, \\
& P(\text { Det } \mid \text { Adv })=0.1, P(\text { Det } \mid \mathrm{V})=0.3, P(\mathrm{~N} \mid \text { Det })=0.5
\end{aligned}
$$

(plus all the others, such that stochastic constraints are fullfilled)

- Initial probabilities:

$$
\begin{align*}
& P_{l}(\mathrm{Adj})=0.01, P_{l}(\mathrm{Adv})=0.001, P_{l}(\mathrm{Det})=0.1, \\
& P_{l}(\mathrm{~N})=0.2, P_{l}(\mathrm{~V})=0.003
\end{align*}
$$

- Words: $\mathscr{L}=\{$ an, arrow, flies, like, time,$\ldots\}$
- Emission probabilities:

$$
\begin{align*}
& P(\text { time } \mid \mathrm{N})=0.1, P(\text { time } \mid \text { Adj })=0.01, P(\text { time } \mid \mathrm{v})=0.05, P(\text { flies } \mid \mathrm{N})=0.1, \\
& P(\text { flies } \mid \mathrm{V})=0.01, P(\text { like } \mid \text { Adv })=0.005, P(\text { like } \mid \mathrm{V})=0.1, P(\text { an } \mid \text { Det })=0.3, \\
& P(\text { arrow } \mid \mathrm{N})=0.5
\end{align*}
$$

## Example: PoS tagging with HMM (cont.)

In this example, $12=3 \cdot 2 \cdot 2 \cdot 1 \cdot 1$ analyzes are possible, for example:

$P($ time $/ \mathrm{N}$ flies $/ \mathrm{v}$ like/Adv an/Det arrow $/ \mathrm{N})=1.13 \cdot 10^{-11}$

$P($ time/Adj flies $/ \mathrm{N}$ like $/ \mathrm{v}$ an/Det arrow $/ \mathrm{N})=6.75 \cdot 10^{-10}$

Details of one of such computation:

$$
\begin{aligned}
& P(\text { time } / \mathrm{N} \text { flies } / \mathrm{v} \text { like/Adv an/Det arrow } / \mathrm{N}) \\
&= P_{/}(\mathrm{N}) \cdot P(\text { time } \mid \mathrm{N}) \cdot P(\mathrm{v} \mid \mathrm{N}) \cdot P(\text { flies } \mid \mathrm{V}) \cdot P(\text { Adv } \mid \mathrm{v}) \cdot P(\text { like } \mid \text { Adv }) \\
& \cdot P(\text { Det } \mid \text { Adv }) \cdot P(\text { an } / \text { Det }) \cdot P(\mathrm{~N} \mid \text { Det }) \cdot P(\operatorname{arrow} / \mathrm{N}) \\
&= 2 \mathrm{e}-1 \cdot 1 \mathrm{e}-1 \cdot 3 \mathrm{e}-1 \cdot 1 \mathrm{e}-2 \cdot 5 \mathrm{e}-3 \cdot 5 \mathrm{e}-3 \cdot 1 \mathrm{e}-1 \cdot 3 \mathrm{e}-1 \cdot 5 \mathrm{e}-1 \cdot 5 \mathrm{e}-1 \\
&= 1.13 \cdot 10^{-11}
\end{aligned}
$$

The aim is to choose the most probable tagging among the possible ones (e.g. as provided by the lexicon)

HMM advantage: well formalized framework, efficient algorithms

* Viterbi: linear algorithm $(\mathscr{O}(n))$ that computes the sequence $T_{1}^{n}$ maximizing $P\left(T_{1}^{n} \mid w_{1}^{n}\right)$ (provided the former hypotheses)
- Baum-Welch : iterative algorithm for estimating parameters from unsupervised data (words only, not the corresponding tag sequences) (parameters $\left.=P\left(w \mid T_{i}\right), P\left(T_{j} \mid T_{j-k}^{j-1}\right), P_{l}\left(T_{1} \ldots T_{k}\right)\right)$
$\rightarrow$ supervised (i.e. manually tagged text corpus)


## HMM

$$
\begin{aligned}
& P\left(T_{1}^{n}, w_{1}^{n}\right)=P\left(T_{1}\right) P\left(w_{1} \mid T_{1}\right) \\
& \quad \prod_{i=2}^{n} P\left(w_{i} \mid T_{i}\right) P\left(T_{i} \mid T_{i-1}\right)
\end{aligned}
$$

## CRF

$$
P\left(T_{1}^{n} \mid w_{1}^{n}\right)=\prod_{i=2}^{n} P\left(T_{i-1}, T_{i} \mid w_{1}^{n}\right),
$$

with

$$
P\left(T_{i-1}, T_{i} \mid w_{1}^{n}\right) \propto \exp \left(\sum_{j} \lambda_{j} f_{j}\left(T_{i-1}, T_{i}, w_{1}^{n}, i\right)\right)
$$

## Other Models and Performances

| On the "WallStreet Journal" corpus: |  |  |  |
| :---: | :---: | :---: | :---: |
| name | technique | publication | accuracy (\%) |
| TnT | $\mathrm{HMM}$ | Brants $(2000)$ | 96.5 |
| GENiA Tagger | MaxEnt | Tsuruoka, et al. (2005) | 97.0 |
| Averaged Perceptron |  | Collins (2002) | 97.1 |
| SVMTool | SVM | Giménez and Márquez (2004) | 97.2 |
| Stanford Tagger 2.0 | MaxEnt | Manning (2011) | 97.3 |
| structReg | CRF | Sun (2014) | 97.4 |
| Flair | LSTM-CRF | Akbik et al. (2018) | 97.8 |

## Keypoints

- The aim of PoS tagging is to choose among the possible tags for each word of the text the right tag according to the context

$\rightarrow$ Different efficient techniques exist allowing for both supervised and unsupervised learning

$\rightarrow$ Performances: $95-98 \% \quad$ (random $\rightarrow \simeq 75-90 \%)$

$\rightarrow$ Be familiar with the principles of HMM tagging

$\rightarrow$ Word normalization (a.k.a. "lematization") is easy once PoS tagging has been done

