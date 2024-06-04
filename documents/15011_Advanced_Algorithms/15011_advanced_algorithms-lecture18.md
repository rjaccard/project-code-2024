# Distinct elements, AMS sketch 

## 1 Estimating the Number of Distinct Elements

(This is the Facebook problem, i.e., the number of different cities on Facebook.)

DISTINCT-ELEMENTS problem Our goal is to output an approximation to then number $d(\sigma)=$

$\left|\left\{j: f_{j}>0\right\}\right|$ of distinct elements that appear in the stream $\sigma$.

It is provably impossible to solve this problem in sublinear space if one is restricted to either deterministic algorithms or exact algorithms. Thus we shall seek a randomized approximation algorithms. More specifically, we give a guarantee of the following type

$$
\operatorname{Pr}[d(\sigma) / 3 \leq A(\sigma) \leq 3 d(\sigma)] \geq 1-\delta
$$

i.e., with probability $1-\delta$ we have a 3 -approximate solution. (With more work the 3 can be improved to $1+\varepsilon$ for any $\varepsilon>0$.) The amount of space we use will be $O(\log (1 / \delta) \log n)$.

### 1.1 Ingredients

### 1.1.1 Pairwise independent hash family

A family $\mathcal{H}$ of functions of the type $[n] \rightarrow[n]$ is said to be a pairwise independent hash family if the following property holds, with $h \in \mathcal{H}$ picked uniformly at random:

for any $x \neq x^{\prime} \in[n]$ and $y, y^{\prime} \in[n]$ we have

$$
\underset{h \sim \mathcal{H}}{\operatorname{Pr}}\left[h(x)=y \wedge h\left(x^{\prime}\right)=y^{\prime}\right]=1 / n^{2}
$$

Note that this implies that $\operatorname{Pr}_{h}[h(x)=y]=1 / n$. For us the following fact will be important (which follows from the construction in last lecture):

Lemma 1 There exists a pairwise independent hash family so that $h$ can be sampled by picking $O(\log n)$ random bits. Moreover, $h(x)$ can be calculated in space $O(\log n)$.

### 1.1.2 The zero function

For an integer $p>0$ let $z \operatorname{eros}(p)$ denote the number of zeros that the binary representation of $p$ ends with. Formally,

$$
z \operatorname{eros}(p)=\max \left\{i: 2^{i} \text { divides } p\right\}
$$

Examples are $z \operatorname{eros}(2)=1, z \operatorname{eros}(3)=0, z \operatorname{eros}(4)=2, z \operatorname{eros}(6)=1, z \operatorname{eros}(7)=0$.[^0]

### 1.2 The Algorithm

The basic intuition of the algorithm is as follows:

- The probability that a random number $x$ has $z \operatorname{eros}(x) \geq \log d$ is $1 / d$.
- So if we have $d$ distinct numbers we would expect $\operatorname{zeros}(h(j)) \geq \log d$ for some element $j$.

The algorithm is now very simple:

Initialization: Choose a random hash function $h:[n] \rightarrow[n]$ from a pairwise independent family ${ }^{2}$. Let $z=0$.

Process $j:$ If $z \operatorname{eros}(h(j))>z$ then $z=z \operatorname{eros}(h(j))$.

Output: $2^{z+1 / 2}$.

We only use $O(\log n)$ space. Let's now analyze the quality of the output.

### 1.3 Analysis of Algorithm

- For each $j \in[n]$ and each integer $r \geq 0$, let $X_{r, j}$ be an indicator random variable for the event "zeros $(h(j)) \geq r, "$ and let $Y_{r}=\sum_{j: f_{j}>0} X_{r, j}$.
- Let $t$ denote the value of $z$ when algorithm terminates. By definition,

$$
\begin{equation*}
Y_{r}>0 \Longleftrightarrow t \geq r \tag{1}
\end{equation*}
$$

- It will be useful to restate this fact as follows:

$$
\begin{equation*}
Y_{r}=0 \Longleftrightarrow t \leq r-1 \tag{2}
\end{equation*}
$$

- Since $h(j)$ is uniformly distributed over $(\log n)$-bit strings, we have

$$
\mathbb{E}\left[X_{r, j}\right]=\operatorname{Pr}[\operatorname{zeros}(h(j)) \geq r]=\operatorname{Pr}\left[2^{r} \text { divides } h(j)\right]=\frac{1}{2^{r}}
$$

We now estimate the expectation and variance of $Y_{r}$. We have

$$
\mathbb{E}\left[Y_{r}\right]=\sum_{j: f_{j}>0} \mathbb{E}\left[X_{r, j}\right]=\frac{d}{2^{r}}
$$

and

$$
\begin{aligned}
\operatorname{Var}\left[Y_{r}\right] & =\mathbb{E}\left[Y_{r}^{2}\right]-\mathbb{E}\left[Y_{r}\right]^{2} \\
& =\mathbb{E}\left[\sum_{j, j^{\prime}: f_{j}, f_{j^{\prime}}>0} X_{r, j} X_{r, j^{\prime}}\right]-\sum_{j, j^{\prime}: f_{j}, f_{j^{\prime}}>0} \mathbb{E}\left[X_{r, j}\right] \mathbb{E}\left[X_{r, j^{\prime}}\right] \\
& =\sum_{j: f_{j}>0}\left(\mathbb{E}\left[X_{r, j}^{2}\right]-\mathbb{E}\left[X_{r, j}\right]^{2}\right) \\
& \leq \sum_{j: f_{j}>0} \mathbb{E}\left[X_{r, j}^{2}\right]=\sum_{j: f_{j}>0} \mathbb{E}\left[X_{r, j}\right]=\frac{d}{2^{r}}
\end{aligned}
$$[^1]

Here, we used the pairwise independence from the hash-functions in the third equality.

Then by using Markov's inequality, we have

$$
\begin{equation*}
\operatorname{Pr}\left[Y_{r}>0\right]=\operatorname{Pr}\left[Y_{r} \geq 1\right] \leq \frac{\mathbb{E}\left[Y_{r}\right]}{1}=\frac{d}{2^{r}} \tag{3}
\end{equation*}
$$

(Recall that Markov's inequality says that for a non-negative random variable, we have $\operatorname{Pr}[Z \geq k] \leq \frac{\mathbb{E}[Z]}{k}$.) Also by using Chebyshev's inequality, we have

$$
\begin{equation*}
\operatorname{Pr}\left[Y_{r}=0\right] \leq \operatorname{Pr}\left[\left|Y_{r}-\mathbb{E}\left[Y_{r}\right]\right| \geq \frac{d}{2^{r}}\right] \leq \frac{\operatorname{Var}\left[Y_{r}\right]}{\left(d / 2^{r}\right)^{2}} \leq \frac{2^{r}}{d} \tag{4}
\end{equation*}
$$

(Recall that Chebyshev's inequality says that for a random variable $Z, \operatorname{Pr}[|Z-\mathbb{E}[Z]| \geq k] \leq \frac{\operatorname{Var}[Z]}{k^{2}}$.)

- Let $\hat{d}$ be the estimate of $d$ that the algorithm outputs. Then $\hat{d}=2^{t+1 / 2}$.
- Let $a$ be the smallest integer such that $2^{a+1 / 2} \geq 3 d$. Using Equations (1) and (3),

$$
\operatorname{Pr}[\hat{d} \geq 3 d]=\operatorname{Pr}[t \geq a]=\operatorname{Pr}\left[Y_{a}>0\right] \leq \frac{d}{2^{a}} \leq \frac{\sqrt{2}}{3}
$$

- Similarly, let $b$ the largest integer such that $2^{b+1 / 2} \leq d / 3$. Using Equations (2) and (4),

$$
\operatorname{Pr}[\hat{d} \leq d / 3]=\operatorname{Pr}[t \leq b]=\operatorname{Pr}\left[Y_{b+1}=0\right] \leq \frac{2^{b+1}}{d} \leq \frac{\sqrt{2}}{3}
$$

These guarantees are pretty weak in two ways:

- First the estimate $\hat{d}$ is not arbitrarily close to $d$ (can be fixed but not today).
- Secondly, the failure bounds (on each side) are $\frac{\sqrt{2}}{3} \approx 47 \%$ which is high. How can we fix this problem? Clearly we could aim for a worse than 3 -approximation and therefore obtain better failure probabilities.
- But a better idea, that does not further degrade the quality of the estimate $\hat{d}$, is to use a standard "median trick" which is really useful to know and use.


### 1.4 The Median Trick

- Imagine running $k$ copies of this algorithm in parallel, using mutually independent random hash functions, outputting the median of the $k$ answers.

If this median exceeds $3 d$ then $k / 2$ of the individual answers must exceed $3 d$, whereas we only expect $\leq k \frac{\sqrt{2}}{3}$ of them to exceed $3 d$. By a standard Chernoff bound, this event has a probability $\leq 2^{-\Omega(k)}$.

Similarly, the probability that the median is below $d / 3$ is also $2^{-\Omega(k)}$.

Choosing $k=\Theta(\log (1 / \delta))$, we can make the sum of these two probabilities work out to at most $\delta$. This gives us a one-pass randomized streaming algorithm that computes an estimate $\hat{d}$ of $d$ such that

$$
\operatorname{Pr}[\hat{d} \notin[d / 3,3 d]] \leq \delta
$$

What about the space requirement? The original algorithm requires $O(\log n)$ bits to store (and compute) the hash function and $O(\log \log n)$ bits to store $z$. Therefore, the space used by the final algorithm is $O(\log (1 / \delta) \log n)$.

## 2 The AMS sketch ( $F_{2}$ estimator)

In this section we see a classic streaming algorithm by Alon, Matias, and Szegedy [AMS] for estimating the $\ell_{2}$ norm of the frequency vector. Recall the streaming setting that we consider:

- The input is a long stream $\sigma=\left\langle a_{1}, a_{2}, \ldots, a_{m}\right\rangle$ consisting of $m$ elements where each element takes a value from the universe $[n]=\{1, \ldots, n\}$.
- Our central goal is to process the input stream (going from left to right) using a small amount of space $s$, i.e., to use $s$ bits of random-access memory while calculating (approximately) some interesting function/statistics $\phi(\sigma)$.

In this lecture, we are again interested in calculating statistics based on the frequency vector vector $\mathbf{f}=\left(f_{1}, \ldots, f_{n}\right)$ of the stream, where $f_{i}=\left|\left\{j: a_{j}=i\right\}\right|$ is the number of elements of value $i$. Note that $f_{1}+f_{2}+\cdots+f_{m}=m$. In particular, we want to estimate the second moment

$$
F_{2}=\sum_{i=1}^{n} f_{i}^{2}
$$


[^0]:    ${ }^{1}$ Disclaimer: These notes were written as notes for the lecturer. They have not been peer-reviewed and may contain inconsistent notation, typos, and omit citations of relevant works.

[^1]:    ${ }^{2}$ To ease calculations we assume that $n$ is a power of two and so we hash a value $p$ to a uniformly at random binary string of length $\log _{2}(n)$.

