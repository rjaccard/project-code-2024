# Words? Tokens! 

## Word vs. tokens

- Word (also sometimes called "type"): an element of the vocabulary; i.e. we a priori define what words have to be.
- Token: ambiguously defined as (definition may vary):

1. either a (continuous) sequence of non-separator characters

- requires the definition of "separator"
- is a separator a token in itself? (may vary)

2. or either an instance of a type or a (continuous) sequence of non-separator characters

## Key points

1. The notion of words is (inherently?) ambiguous and depends on the application.
2. Tokens are more useful in practice but may also depend on the application

## Lexicon

- to recognize and classify "correct words" of the language (as we want to define them)
- List of records structured in fields, describing the correct forms, with all the related relevant information, e.g.:
    - surface form: boards
    - Part-of-Speech tag: Np (= Noun plural)
    - lemma: board\#Ns ( $\rightarrow$ a surface form and a PoS tag)
    - probability: $3.2144 \mathrm{e}-05$
    - pronunciation: $\mathrm{b}$ oa $r \mathrm{~d} z$
    -         - etc...


## Surface forms: implementation

Surface form field implementation:

Formally: list of strings...

Implementations:

- Lists/Tables
- Hash Tables
- Tries (= lexical trees)
- Finite-State Automata (FSA)
- Transducers (FST)


## List/Tables implementation

needs an order on the values (e.g. alphabetical order)

:-) easy and fast to implement

:-) efficient by-reference access function $(\mathscr{O}(1))$

$:-(\quad$ access in $\mathscr{O}(\log N)$, insertion in $\mathscr{O}(N) \quad(N=$ number of records)

:- ( large size (replication of all (sub-)strings)

## Hash Tables

:-) easy and fast to implement

:-| complexity of access and insertion difficult to predict (collisions)

$:-($ no by-reference access-function ( $\rightarrow$ extra inversion table)

:-( large size (replication of all (sub-)strings)

## Implementation of methods for lexica with FSA

Finite-State Automata:

- Equivalence between DFSA and NFSA (with and without $\varepsilon$ )
- Equivalence between regular expressions and DFSA
- For a given regular language, existence of a unique minimal DFSA
- Can be numbered so as to do monotone minimal perfect hashing (by-value and by-reference access functions)

:-)) regexp (e.g. numbers, dates, $\ldots$ )

:-) access in $\mathscr{O}(1)$

:-) optimal size (minimal number of states)

:-( Implementation

:-( Update (insertion or deletion of strings)

## Summary of surface-form field implementations

|  | existence test | by_value access | by_ref access |
| :--- | :---: | :---: | :---: |
| lists/tables | $\mathbf{x}$ | $\mathbf{x}$ | $\mathbf{x}$ |
| hash-tables | $\mathbf{x}$ | $\mathbf{x}$ | $(\mathbf{x})$ |
| Tries | $\mathbf{x}$ | - | - |
| Tries + labeled leaves | $\mathbf{x}$ | $\mathbf{x}$ | - |
| Tries with invertion ${ }^{1}$ | $\mathbf{x}$ | $\mathbf{x}$ | $\mathbf{x}$ |
| FSA | $\mathbf{x}$ | - | - |
| FSA + numeration | $\mathbf{x}$ | $\mathbf{x}$ | $\mathbf{x}$ |
| Transducers | $\mathbf{x}$ | $\mathbf{x}$ | $\mathbf{x}$ |

## Language models

- all modern neural NLP techniques actually focus on $n$-grams, estimating various kinds of related probabilities
- probabilization of $n$-grams of tokens a.k.a. "language model"


## n-gram approach

- Consider sequence of $x$ (characters, tokens, ...)
- make use of ( $n-1$ )-order Markov assumption: $P\left(x_{i} \mid x_{1} \cdots x_{i-1}\right)=P\left(x_{i} \mid x_{i-n+1} \cdots x_{i-1}\right)$
- to end up with:

$$
P\left(x_{1} \cdots x_{N}\right)=P\left(x_{1} \cdots x_{n}\right) \cdot \prod_{i=n+1}^{N} P\left(x_{i} \mid x_{i-n+1} \cdots x_{i-1}\right)
$$

Use this as a score to compare sequences $(n \geq 2)$ :

$$
\frac{\prod_{i=1}^{N-n+1} P\left(x_{i} \cdots x_{i+n-1}\right)}{\prod_{i=2}^{N-n+1} P\left(x_{i} \cdots x_{i+n-2}\right)} \quad P\left(x_{i} \cdots x_{i+n-1}\right): \text { paramaters estimated on some corpus }
$$

Reminder: $P\left(x_{i} \cdots x_{i+n-2}\right)=\sum_{x} P\left(x_{i} \cdots x_{i+n-2} x\right)$

## n-gram approach: example

Assume $n=3$ (trigrams):

$$
\begin{aligned}
P(\text { errro }) & =P(e r r) \cdot P(r \mid r r) \cdot P(o \mid r r) \\
& =P(e r r) \cdot \frac{P(r r r)}{P(r r)} \cdot \frac{P(r r o)}{P(r r)} \\
P(\text { error }) & =P(e r r) \cdot \frac{P(r r o)}{P(r r)} \cdot \frac{P(r o r)}{P(r o)}
\end{aligned}
$$

## Estimation (= model learning)

Where do the $P\left(x_{i} \cdots x_{i+n-1}\right)$ come from?

Simplest: maximum-likelihood estimate:

$$
\widehat{P}\left(x_{1} \cdots x_{n}\right)=\frac{\#\left(x_{1} \cdots x_{n}\right)}{N_{n}}
$$

where $\#(y)$ is the count of $y$ (= the number of times $y$ appears in the corpus) and $N_{n}$ is the size of the corpus $=$ the total number of $n$-grams:

$$
N_{n}=\sum_{x_{1}, \ldots, x_{n}} \#\left(x_{1} \cdots x_{n}\right)
$$

Maximum-likelihood estimates (MLE) are the simplest ones but suffer from unseen events:

- unseen rare events have a 0 frequency, thus a 0 probability MLE (overfitting)
- That could be OK in domains where the number of zeros isn't huge (e.g. maybe for categorization), but is not for language modeling.

Several approaches to better estimate unseen rare events (a.k.a smoothing methods):

- change prior (a.k.a. "additive smoothing")
- add a new word (e.g. "<UNKNOWN>") and estimate (held-out) probabilities accordingly
- backoff smoothing: fall-back on smaller $n$ : increase the chance to observe events by decreasing the context-size
- interpolation: mix $n$-grams with ( $n-1)$-grams, $(n-2)$-grams, etc. the mixing coefficients can be fixed or adaptative (learned on held-out data)
- Good-Turing smoothing: use the count of hapaxes (events seen only once) to improve estimates of probabilities of unseen events
- Kneser-Ney smoothing: considered as the most-effective for $n$-grams; it's a mixture of discounting and interpolation


## Additive smoothing

$n$-grams is a probabilistic model, the parameters $\theta$ of which are the probabilities of the various $n$-grams (i.e. $\theta$ is a constraint vector of dimension $D=|X|^{n}$, with $|X|$ the number of possible values for $X$ )

A (partially) Bayesian view on learning $\theta$ from a corpus $\mathscr{C}$ leads to estimating as:

$$
\widehat{\theta}=\underset{\theta}{\operatorname{argmax}} P(\theta \mid \mathscr{C})=\underset{\theta}{\operatorname{argmax}} P(\theta) P(\mathscr{C} \mid \theta)
$$

$P(\mathscr{C} \mid \theta)$ (the likelihood of a corpus, represented here as a "bag-of- $n$-grams", i.e. by its $n$-grams counts) follows a multinomial law (the parameters of which are $\theta$ ).

It's conjugate prior is the Dirichlet distribution; so let's model $P(\theta)$ by a Dirichlet distribution (it's thus a probability density on probabilities):

$$
P(\theta \mid \alpha)=\Gamma\left(\sum_{i=1}^{D} \alpha_{i}\right) \cdot \prod_{i=1}^{D} \frac{\theta_{i}^{\alpha_{i}-1}}{\Gamma\left(\alpha_{i}\right)} \quad\left(\alpha_{i}>0\right)
$$

where $\Gamma()$ represents the "gamma function".

Thus the posterior $P(\theta \mid \mathscr{C})$ is itself a Dirichlet distribution, which is maximized (MAP) for

$$
\widehat{P}\left(x_{1} \cdots x_{n}\right)=\frac{\#\left(x_{1} \cdots x_{n}\right)+\alpha_{x_{1}, \ldots, x_{n}}-1}{N_{n}+\left(\sum_{x_{1}, \ldots, x_{n}} \alpha_{x_{1}, \ldots, x_{n}}\right)-D}
$$

In a "more Bayesian view", however, the expected value of $\widehat{P}\left(x_{1} \cdots x_{n}\right)$ (under posterior Dirichlet distribution) is:

$$
\tilde{P}\left(x_{1} \cdots x_{n}\right)=\frac{\#\left(x_{1} \cdots x_{n}\right)+\alpha_{x_{1}, \ldots, x_{n}}}{N_{n}+\sum_{x_{1}, \ldots, x_{n}} \alpha_{x_{1}, \ldots, x_{n}}}
$$

and moreover (predictive distribution):

$$
P\left(x_{1} \cdots x_{n} \mid \mathscr{C}, \alpha\right)=\widetilde{P}\left(x_{1} \cdots x_{n}\right)=\frac{\#\left(x_{1} \cdots x_{n}\right)+\alpha_{x_{1}, \ldots, x_{n}}}{N_{n}+\sum_{x_{1}, \ldots, x_{n}} \alpha_{x_{1}, \ldots, x_{n}}}
$$

## Example (bigrams among two letters)

$$
\mathscr{C}=\text { ababaabababaabab }=\{(\mathrm{ab}, 7),(\mathrm{ba}, 6),(\mathrm{aa}, 2),(\mathrm{bb}, 0)\}
$$

MLE:

$$
P(\mathrm{ab})=\frac{7}{15} \quad P(\mathrm{ba})=\frac{6}{15} \quad P(\mathrm{aa})=\frac{2}{15} \quad P(\mathrm{ba})=0
$$

Predictive distribution with uniform Dirichlet prior $\alpha_{i}=0.5$ for all $i \in\{\mathrm{ab}, \mathrm{ba}, \mathrm{aa}, \mathrm{bb}\}$ :

$$
P(\mathrm{ab} \mid \mathscr{C}, \alpha)=\frac{7.5}{17} \quad P(\mathrm{ba} \mid \mathscr{C}, \alpha)=\frac{6.5}{17} \quad P(\mathrm{aa} \mid \mathscr{C}, \alpha)=\frac{2.5}{17} \quad P(\mathrm{ba} \mid \mathscr{C}, \alpha)=\frac{0.5}{17}
$$

## Additive smoothing = Dirichlet prior

So additive smoothing techniques

$$
P\left(x_{1} \cdots x_{n} \mid \mathscr{C}, \alpha\right)=\frac{\#\left(x_{1} \cdots x_{n}\right)+\alpha_{x_{1}, \ldots, x_{n}}}{N_{n}+\sum_{x_{1}, \ldots, x_{n}} \alpha_{x_{1}, \ldots, x_{n}}}
$$

result from a Bayesian predictive distribution with a Dirichlet-prior assumption:

- “ $\alpha_{i}=0$ ” (impossible): MLE
- $\alpha_{i}=1$ : "Laplace smoothing", a.k.a. "add-one smoothing"

don't use that for linguistic corpora (see next slides and reference [7])

- $\alpha_{i}<1$ : makes sense with power laws (a priori $\theta$ lies "close to the borders")

But what does $\alpha_{i}$ actually represent (intuitively)?

The components of $\alpha$ represent the relative importance of each component of $\theta$ For $\alpha_{i}$ smaller than 1 , the distribution tends to "sharply increase" (in other words, to discretize) to the maximum $\alpha_{i}$ values.

More details in appendix for those interested.

