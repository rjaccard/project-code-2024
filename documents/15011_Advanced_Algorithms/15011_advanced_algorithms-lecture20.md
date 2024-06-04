# Streaming Algorithms (CountSkETCH)  

In this lecture we start by stating the streaming algorithm for distinct elements and then provide the analysis (last lecture notes). We then see a classic streaming algorithm by Alon, Matias, and Szegedy $[\mathbf{A M S}]$ for estimating the $\ell_{2}$ norm of the frequency vector. Recall the streaming setting that we consider:

- The input is a long stream $\sigma=\left\langle a_{1}, a_{2}, \ldots, a_{m}\right\rangle$ consisting of $m$ elements where each element takes a value from the universe $[n]=\{1, \ldots, n\}$.
- Our central goal is to process the input stream (going from left to right) using a small amount of space $s$, i.e., to use $s$ bits of random-access memory while calculating (approximately) some interesting function/statistics $\phi(\sigma)$.

The stream $\sigma$ implicitly defined the frequency vector $f \in \mathbb{R}^{n}$ : for every $i \in[n]$ we let $f_{i}$ denote the number of occurrences of $i$ in the stream $\sigma$.

## 1 AMS sketch and the Johnson-Lindenstrauss lemma

### 1.1 Reminder from the last lecture

Last time, we constructed an algorithm for approximating the $L_{2}$ norm of a vector $x \in \mathbb{R}^{n}$ using the AMS sketch, given a stream of updates to entries of $x$. We generated a random matrix $A \in \mathbb{R}^{m \times n}$ by independently and uniformly sampling each entry $A_{i j}$ from $\{1,-1\}$. We then proved that $\forall \epsilon>0$, if the dimension $m=O\left(\frac{1}{\epsilon^{2}}\right)$, then $\forall x \in \mathbb{R}^{n}$ :

$$
\operatorname{Pr}\left[\left|\|A x\|_{2}^{2}-m\|x\|_{2}^{2}\right|>\epsilon m\|x\|_{2}^{2}\right]<\frac{1}{3}
$$

This implies that with probability at least $\frac{2}{3},(1-\epsilon)\|x\|_{2} \leq\left\|\frac{1}{\sqrt{m}} A x\right\|_{2} \leq(1+\epsilon)\|x\|_{2}-$ this follows because for any $0<\epsilon<1, \sqrt{1+\epsilon}<1+\epsilon$ and $\sqrt{1-\epsilon}>1-\epsilon$.

### 1.2 Sketch using a Gaussian distribution

We consider another sketch $A \in \mathbb{R}^{m \times n}$, where $\forall 1 \leq i, j \leq n, A_{i j} \sim \mathcal{N}(0,1)$. Examining the conditions imposed on the $A$ 's coefficients in the last lecture, we notice that both still hold:

1. $E\left[A_{k i} A_{k j}\right]=0, \forall i \neq j, 1 \leq k \leq m$ because the variables are independent.
2. $E\left[A_{i k}^{2}\right]=1, \forall 1 \leq i \leq m, 1 \leq k \leq n$ by definition.

The new sketch has an additional property: $1 \leq i \leq n,(A x)_{i}=\sum_{j=1}^{n} A_{i j} x_{j} \sim \mathcal{N}\left(0,\|x\|_{2}^{2}\right)$. This is known as the 2-stability of the Gaussian distribution.

Most importantly, it is possible to prove a strong Chernoff-type concentration inequality for $\|A x\|_{2}$. Specifically, $\|A x\|_{2}^{2}=\sum_{i=1}^{m}(A x)_{i}^{2}=\sum_{i=1}^{m} y_{i}^{2}, y_{i} \sim \mathcal{N}\left(0,\|x\|_{2}^{2}\right)$ follows a $\chi^{2}$ with $m$ degrees of freedom. The following bound holds for this distribution:

$$
\operatorname{Pr}\left[\left|\|A x\|_{2}^{2}-m\|x\|_{2}^{2}\right|>\epsilon m\|x\|_{2}^{2}\right]<e^{-C \epsilon^{2} m} \text { for a constant } C>0
$$[^0]

### 1.3 Johnson - Lindenstrauss lemma

Lemma 1 For any $\epsilon \in\left(0, \frac{1}{2}\right), \forall x_{1}, \cdots, x_{n} \in \mathbb{R}^{d}$, there exists $M \in \mathbb{R}^{m \times n}$ with $m=O\left(\frac{1}{\epsilon^{2}} \log n\right)$ such that for all $1 \leq i, j \leq n$ :

$$
(1-\epsilon)\left\|x_{i}-x_{j}\right\|_{2} \leq\left\|M x_{i}-M x_{j}\right\|_{2} \leq(1+\epsilon)\left\|x_{i}-x_{j}\right\|_{2}
$$

Remark This is a statement about dimensionality reduction. The dimension to which the $\mathbb{R}^{d}$ vectors are reduced, $m$, does not depend on $d$, only on the number of vectors.

Proof Fix two indices $i \neq j$ and let $y^{i j}=x_{i}-x_{j}$ and $M=\frac{1}{\sqrt{m}} A$, where $A \in \mathbb{R}^{m \times n}$ has i.i.d. elements sampled from $\mathcal{N}(0,1)$. By the previous result and setting $m=\frac{4}{C \epsilon^{2}} \log n$ :

$$
\operatorname{Pr}\left[\left|\left\|M y^{i j}\right\|_{2}^{2}-\left\|y^{i j}\right\|_{2}^{2}\right|>\epsilon\left\|y^{i j}\right\|_{2}^{2}\right]<e^{-C \epsilon^{2} m}=e^{-C \epsilon^{2} \frac{4}{C \epsilon^{2}} \log n}=\frac{1}{n^{4}}
$$

Next, by taking the union bound:

$$
\begin{aligned}
\operatorname{Pr}\left[\exists i \neq j,\left|\left\|M y^{i j}\right\|_{2}^{2}-\left\|y^{i j}\right\|_{2}^{2}\right|>\epsilon\left\|y^{i j}\right\|_{2}^{2}\right] & \leq \sum_{i \neq j} \operatorname{Pr}\left[\left|\left\|M y^{i j}\right\|_{2}^{2}-\left\|y^{i j}\right\|_{2}^{2}\right|>\epsilon\left\|y^{i j}\right\|_{2}^{2}\right] \\
& <\binom{n}{2} \frac{1}{n^{4}} \\
& <\frac{1}{n^{2}}
\end{aligned}
$$

Therefore $\operatorname{Pr}\left[\forall i \neq j,\left|\left\|M x_{i}-M x_{j}\right\|_{2}^{2}-\left\|x_{i}-x_{j}\right\|_{2}^{2}\right| \leq \epsilon\left\|x_{i}-x_{j}\right\|_{2}^{2}\right]>1-\frac{1}{n^{2}}$. The probability is taken w.r.t the law of $M$, which allows us to conclude the existence of at least one matrix $M$ satisfying the desired inequality.

Remark The bound for $m$ is optimal, as proved by a very recent result Larsen-Nelson'16.

## 2 CountSketch ( $\ell_{2}$-heavy hitters)

We now use ideas from the AMS sketch to design a small space algorithm for outputting (approximately) the top few elements of a data stream using a small amount of space. Specifically, we will be able to recover elements with 'large' frequencies - such elements are known as heavy-hitters. The formal definition is

Definition 2 ( $\ell_{\mathbf{2}}$ Heavy Hitter) We call $i \in[n]$ a $\phi$ - heavy hitter if $\left|x_{i}\right| \geq \phi\|x\|_{2}$ for $\phi \in(0,1)$.

Goal: Design a small space algorithm that,

1. Approximates $x_{i}$ up to $(\phi / 4)\|x\|_{2}$ error, for every $i \in[n]$.
2. Outputs a list $L \subseteq[n]$ that contains all $\phi$ - heavy hitters and does not contain any element that is not a $\phi / 2$-heavy hitter.

Remark Note that $\ell_{2}$-heavy hitters for constant $\phi$ is a more powerful primitive than $\ell_{1}$-heavy hitters (the elements found by the Misra-Gries estimator that we discussed two lectures ago). For example, consider a stream of length $n$ where one item occurs $\sqrt{n}$ times, and the remaining $n-\sqrt{n}$ items are distinct. Note that the 'heavy' item is heavy in $\ell_{2}$ sense, but not in $\ell_{1}$ sense. In particular, if one samples a random location in the stream, the probability of hitting the 'heavy' item is only $1 / \sqrt{n}$. In particular,
the Misra-Gries estimator will not be able to find the 'heavy' item using $O(\log n)$ space. Nevertheless, the CountSketch algorithm recovers this 'heavy' item using $O(\log n)$ space.

The CountSketch algorithm of Charikar, Chen and Farach-Colton proceeds as follows. Choose $R$ pairwise independent hash functions

$$
h_{r}:[n] \rightarrow[B], \quad r=1,2, \ldots, R
$$

mapping the universe $[n]$ to $B$ buckets. Also choose a sequence of $R$ sign functions

$$
s_{r}:[n] \rightarrow\{ \pm 1\}, \quad r=1,2, \ldots, R
$$

from a pairwise independent family. The CountSKetch algorithm maintains, for each bucket $b \in[B]$ and repetition $r \in R$

$$
y_{r, b}=\sum_{j \in[n] \text { s.t. } h_{r}(j)=b} s_{r}(j) x_{j}
$$

where $x \in \mathbb{R}^{n}$ is the frequency vector of the data stream. Frequency estimation is performed as follows. First, for $i \in[n]$ and $r \in[R]$ define

$$
\widehat{x}_{i}^{r}=s_{r}(i) y_{r, h_{r}(i)}
$$

Our estimate for $i \in[n]$ is then given by

$$
\operatorname{median}_{r \in[R]}\left\{\widehat{x}_{i}^{r}\right\}
$$

We now give the analysis of CountSketch. For convenience relabel elements of the universe $[n]=$ $\{0,1,2, \ldots, n-1\}$ so that $x_{0} \geq x_{1} \geq x_{2} \ldots \geq x_{n}$. We then define the head and tail of $x$ as follows. Define the head of the signal as $H=\{0,1,2, \ldots k-1\}$ (top $\mathrm{k}$ frequencies) and the tail as $T=\{k, \ldots n-1\}$.

### 2.1 Bounding estimation error for fixed $r \in[R]$

We now analyze the estimation error. It is convenient to consider the contribution of the head and the tail of the signal separately to the estimation error:

$$
\begin{align*}
& \widehat{x}_{i}^{r}-x_{i}=s_{r}(i) y_{r, h_{r}(i)}-x_{i} \\
& =\sum_{j \in[n] \backslash\{i\} \text { s.t. } h_{r}(j)=h_{r}(i)} s_{r}(i) s_{r}(j) x_{j} \tag{1}
\end{align*}
$$

![](https://cdn.mathpix.com/cropped/2024_05_17_a9bd3f8397dc722db490g-3.jpg?height=222&width=778&top_left_y=1862&top_left_x=760)

Note that if $i$ does not collide with any of the head elements of the signal in its bucket by $\mathcal{E}_{\text {no-collisions }}(i, r)$. Note that this event is quite likely if the number of buckets is much larger than $k$. Formally, we have for every $r \in[R]$ and $i, j \in[n], i \neq i$

$$
\operatorname{Pr}\left[h_{r}(j)=h_{r}(i)\right]=\frac{1}{B}
$$

We thus have that the probability that $i$ does not collide with any of the head elements in its bucket is upper bounded by

$$
\operatorname{Pr}\left[\exists j \in H \backslash\{i\}: h_{r}(i)=h_{r}(j)\right] \leq \frac{k}{B}
$$

where we used the union bound over at most $k$ elements of $H$. Choosing $B \geq 10 k$, we get that this probability is at most $\frac{1}{10}$, giving that $\operatorname{Pr}\left[\mathcal{E}_{\text {no-collisions }}(i, r)\right] \geq 9 / 10$, and thus the first term in 11 is zero with probability at least $9 / 10$.

We next show that the second term, namely $\Delta(i, r)$, is small in absolute value with high probability. We first show that the expectation of the second term is zero, and then bound the variance. For the expectation we have

$$
\begin{aligned}
\mathbf{E}[\Delta(i, r)] & =\mathbf{E}\left[\sum_{\substack{j \in T \backslash\{i\} \\
h_{r}(i)=h_{r}(j)}} s_{r}(i) s_{r}(j) x_{j}\right] \\
& =\sum_{\substack{j \in T \backslash\{i\} \\
h_{r}(i)=h_{r}(j)}} \mathbf{E}\left[s_{r}(i) s_{r}(j)\right] x_{j} \\
& =0
\end{aligned}
$$

We now bound the variance, conditioned on a specific choice of $h_{r}$ :

$$
\begin{aligned}
\mathbf{E}_{s}\left[\Delta(i, r)^{2}\right] & =\mathbf{E}\left[\Delta(i, r)^{2}\right]-(\mathbf{E}[\Delta(i, r)])^{2} \\
& =\mathbf{E}_{s}\left[\left(\sum_{\substack{j \in T \backslash\{i\} \\
h_{r}(j)=h_{r}(i)}} s_{r}(i) s_{r}(j) x_{j}\right)^{2}\right] \quad(\text { since } \mathbf{E}[\Delta(i, r)]=0) \\
& =\mathbf{E}_{s}\left[\sum_{\substack{j \in T \backslash\{i\}}} \sum_{\substack{j^{\prime} \in T \backslash\{i\} \\
h_{r}(i)=h_{r}(j) \\
h_{r}(i)=h_{r}\left(j^{\prime}\right)}} s_{r}(i)^{2} s_{r}(j) s_{r}\left(j^{\prime}\right) x_{j} x_{j^{\prime}}\right] \\
& =\sum_{j, j^{\prime}} \mathbf{E}_{s}\left[s_{r}(j) s_{r}\left(j^{\prime}\right)\right] x_{j} x_{j^{\prime}} \quad\left(\text { since } s_{r}(i)^{2}\right. \text { is always 1) } \\
& =\sum_{j \in T \backslash\{i\}} x_{j}^{2} \quad\left(\text { since } \mathbf{E}_{s}\left[s_{r}(j) s_{r}\left(j^{\prime}\right)\right]=0 \text { if } j \neq j^{\prime} \text { and } 1 \text { if } j=j^{\prime}\right)
\end{aligned}
$$

We thus have

$$
\operatorname{Pr}\left[\Delta(i, r)^{2} \geq 10 \sum_{\substack{j \in T \backslash\{i\} \\ h_{r}(i)=h_{r}(j)}} x_{j}^{2}\right] \leq \frac{1}{10}
$$

where the probability is over $s$, conditioned on a fixed choice of $h_{r}$. Define the event $\mathcal{E}_{\text {small-noise }}(i, r)$ by

$$
\mathcal{E}_{\text {small-noise }}(i, r):=\left\{\Delta(i, r)^{2} \leq 10 \sum_{\substack{j \in T \backslash\{i\} \\ h_{r}(i)=h_{r}(j)}} x_{j}^{2}\right\}
$$

How small is $\sum_{\substack{j \in T \backslash\{i\} \\ h_{r}(i)=h_{r}(j)}} x_{j}^{2}$ typically? Taking the expectation over the hash function $h$, we get

$$
\begin{aligned}
\mathbf{E}_{h}\left[\sum_{\substack{j \in T \backslash\{i\} \\
h_{r}(i)=h_{r}(j)}} x_{j}^{2}\right] & =\mathbf{E}\left[\sum_{j \in T \backslash\{i\}} x_{j}^{2} \cdot \mathbf{1}_{\left[h_{r}(j)=h_{r}(i)\right]}\right] \\
& =\sum_{j \in T \backslash\{i\}} x_{j}^{2} \cdot \operatorname{Pr}\left[h_{r}(j)=h_{r}(i)\right] \\
& \leq \frac{1}{B} \sum_{j \in T} x_{j}^{2}
\end{aligned}
$$

where the probability is over the choice of $h_{r}$. Now using Markov's Inequality, we get

$$
\operatorname{Pr}\left[\sum_{\substack{j \in T \backslash\{i\} \\ h_{r}(i)=h_{r}(j)}} x_{j}^{2}>\frac{10}{B} \sum_{j \in T} x_{j}^{2}\right] \leq \frac{1}{10}
$$

We define $\mathcal{E}_{\text {small-var }}(i, r)$ by

$$
\mathcal{E}_{\text {small-var }}(i):=\left\{\sum_{\substack{j \in T \backslash\{i\} \\ h_{r}(i)=h_{r}(j)}} x_{j}^{2}<\frac{10}{B} \sum_{j \in T} x_{j}^{2}\right\}
$$

Letting $x_{T}$ denote the restriction of $x$ onto coordinates in $T$, we get $\sum_{j \in T} x_{j}^{2}=\left\|x_{T}\right\|_{2}^{2}$. Using this notation, we get by a union bound over $\mathcal{E}_{\text {no-collisions }}(i, r), \mathcal{E}_{\text {small-noise }}(i, r)$ and $\mathcal{E}_{\text {small-var }}(i, r)$ that

$$
\operatorname{Pr}\left[\left|\widehat{x}_{i}^{r}-x_{i}\right|^{2} \leq \frac{100\left\|x_{T}\right\|_{2}^{2}}{B}\right] \geq 1-\frac{1}{10}-\frac{1}{10}-\frac{1}{10} \geq 7 / 10
$$

### 2.2 Putting it together

We repeat this process $R=C_{1} \log n$ times for a sufficiently large constant $C>0$ to get $\widehat{x}_{i}^{1}, \widehat{x}_{i}^{2}, \ldots, \widehat{x}_{i}^{R}$. Recall that our final estimate is

$$
\widehat{x}_{i}=\operatorname{median}_{r \in[R]}\left\{\widehat{x}_{i}^{r}\right\}
$$

By standard median trick analysis we have $\left|\widehat{x}_{i}-x_{i}\right| \leq \frac{100\left\|x_{T}\right\|_{2}}{\sqrt{B}}$ with probability at least $1-1 / n^{2}$ for every fixed $i \in[n]$. By a union bound over all $i \in[n]$ we thus have

$$
\|\widehat{x}-x\|_{\infty} \leq \frac{10\left\|x_{T}\right\|_{2}}{\sqrt{B}}
$$

with probability at least $1-1 / n$.

To solve the original problem, just let $B=C_{2} k / \phi^{2}$ for a sufficiently large $C_{2}$ to ensure that $\frac{10\left\|x_{T}\right\|_{2}}{\sqrt{B}}<$ $(\phi / 4)\left\|x_{T}\right\|_{2} \leq(\phi / 4)\|x\|_{2}$, and let the output list be defined as

$$
L=\left\{i \in[n]:\left|\widehat{x}_{i}\right|>(3 \phi / 4)\|x\|_{2}\right\}
$$

Remark Note that we proved stronger upper bounds on the quality of estimation provided by CountSketch than are needed for the application to heavy hitters. Specifically, we showed that our estimate errs by at most $\frac{10\left\|x_{T}\right\|_{2}}{\sqrt{B}}$, i.e. the error depends on the $\ell_{2}$ mass in the tail of the signal only. This in particular shows that vectors $x$ with at most $k$ nonzero entries can recovered exactly from our sketch.


[^0]:    ${ }^{1}$ Disclaimer: These notes were written as notes for the lecturer. They have not been peer-reviewed and may contain inconsistent notation, typos, and omit citations of relevant works.

