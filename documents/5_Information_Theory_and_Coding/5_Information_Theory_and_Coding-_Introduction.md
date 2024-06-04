
## Lecture 1: Introduction And Representation Of Information

## 1 Introduction

Information theory is the mathematical representation of everything that concerns transmission and processing of information. Everything began in 1948, following a paper written by Claude Shannon *(the mathematical theory of communication)*, one of the pionners of information theory.

The overall goal of this course is to, given a party A that wants to send a message to a party B over a noisy communication medium, design efficient encoders and decoders in order for the message to be received in its entirety whilst diminishing the number of unsuccessful bits transfered.

## 2 Efficient Representation Of Data And Information

This section introduces a more in depth sense of what information is, how we represent it and how we can model information sources.

## 2.1 Injective, Uniquely Decodable And Prefix-Free Codes

We are given an alphabet U (i.e. a finite set of cardinality *|U|*). A binary source code c is a simple function c : *U → {*0, 1}∗ that maps every element of the alphabet to a binary number. Note that the set we are talking about is simply a union of all possible combinations of zeroes and ones.

**Definition 1** : 

A code c *is called* injective or **non-singular** if ∀u ̸= v =⇒ c(u) ̸= c(v).

Given $\mathcal{U}$ and $\mathcal{V}$, $c:\mathcal{U}\to\{0,1\}^{*}$, $d:\mathcal{V}\to\{0,1\}^{*}$, we define $(c\times d):\mathcal{U}\times\mathcal{V}\to\{0,1\}^{*}$ such that $(c\times d)(u,v)=c(u)d(v)$. Additionally,

$$c^{n}=\underbrace{c\times c\times\cdots\times c}_{n\text{times}}\text{and}c^{*}:\mathcal{U}^{*}\to\{0,1\}^{*},$$

such that $c^{*}(u_{1}\ldots u_{n})=c^{n}(u_{1}\ldots u_{n})$.

**Definition 2** :

A code c *is called* **uniquely decodable** if c∗ is injective.

As an example of a non-injective code, let U = {*a, b, c, d*} and the corresponding codes being c = 0, 00, 1, 01. As we can see, c∗(ac) = c∗(d) so c is injective but c∗ isn't.

**Definition 3** :

A code c *is said to be* **prefix-free** if u ̸= v =⇒ c(u) is not a prefix of c(v), ∀u, v.

If c(u) is a prefix of c(v), then c(u) will represent all combinations of the n first digits of c(v), that is, including c(v) itself.

For example, let U = {*a, b, c, d*} and c = 0, 10, 110, 111 respectively. We can easily see that the code is prefix-free. For instance, except for the letter d, a zero indicates the end of a code.

**Theorem 4** : If a code c is prefix-free, it must be uniquely decodable.

As another example, let U = {*a, b, c, d*} and c = 0, 01, 011, 111 respectively. This code is constructed by reversing the one from the previous example. It is thus uniquely decodable as we can read it backwards. However, it is possible to have a uniquely decodable code that is not instantaneous. For instance, if we have 0111111111111111, we unfortunately have to read all the word before determining if the string starts with an a, a b or a c.

**Theorem 5** : If c is a uniquely decodable code, there exists a c′ that is prefix-free such that length(c(u)) = length(c′(u)), ∀u.

The above theorem means that c′ is exactly as efficient as the original code c. Note that "prefixfree"ness has no efficiency penalty with respect to uniquely decodable codes.

## 2.2 Kraft Sum

**Definition 6**: _Given a code $c:\mathcal{U}\rightarrow\{0,1\}^{*}$, we define the Kraft Sum of $c$ as_

$$KS(c)=\sum_{u\in\mathcal{U}}2^{-length(c(u))}.$$
Lemma 7 KS(c × d) = KS(c) · KS(d).

**Proof**:

$$KS(c\times d)=\sum_{\begin{subarray}{c}u\in\mathcal{U},\\ v\in\mathcal{V}\end{subarray}}2^{-length((c\times d)(u,v))}$$ $$=\sum_{\begin{subarray}{c}u\in\mathcal{U},\\ v\in\mathcal{V}\end{subarray}}2^{-length(c(u))-length(d(v))}$$ $$=\sum_{\begin{subarray}{c}u\in\mathcal{U},\\ v\in\mathcal{V}\end{subarray}}2^{-length(c(u))}2^{-length(d(v))}$$ $$=\sum_{\begin{subarray}{c}v\in\mathcal{V}\\ u\in\mathcal{U}\end{subarray}}2^{-length(c(u))}\sum_{v\in\mathcal{V}}2^{-length(d(v))}=KS(u)\cdot KS(v).$$
As a corollary for the above lemma, we have that KS(cn) = (KS(c))n ∀n ≥ 0.

**Theorem 8** : c is prefix-free =⇒ KS(c) ≤ 1.

**Proof** : Consider a binary tree that grows upside down from the root. If we go left, we append a 0 and if we go right, we append a 1. Start by labeling the tree and mark the c(u)'s. Note that as the code is prefix-free, there is no ancester relationship between c(u) and c(v) for all u and v.

Then start the following experiment: imagine a monkey that climbs the tree from the root and goes left or right at random with equal probability. He stops climbing when reaching a marked node. We observe that Pr(monkey stops at a particular c(u)) = 2−*length*(c(u)). Therefore:

$1\geq Pr(\text{monkey stops})=\sum_{u\in\mathcal{U}}Pr(\text{monkey stops at a particular}c(u))=\sum_{u\in\mathcal{U}}2^{-length(c(u))}=KS(c)$,
which concludes the proof.