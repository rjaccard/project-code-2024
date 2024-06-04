# Streaming Algorithms (AMS $F_{2}$ estimator)  

In this lecture we start by stating the streaming algorithm for distinct elements and then provide the analysis (last lecture notes). We then see a classic streaming algorithm by Alon, Matias, and Szegedy $[\mathbf{A M S}]$ for estimating the $\ell_{2}$ norm of the frequency vector. Recall the streaming setting that we consider:

- The input is a long stream $\sigma=\left\langle a_{1}, a_{2}, \ldots, a_{m}\right\rangle$ consisting of $m$ elements where each element takes a value from the universe $[n]=\{1, \ldots, n\}$.
- Our central goal is to process the input stream (going from left to right) using a small amount of space $s$, i.e., to use $s$ bits of random-access memory while calculating (approximately) some interesting function/statistics $\phi(\sigma)$.

In this lecture, we are again interested in calculating statistics based on the frequency vector vector $\mathbf{f}=\left(f_{1}, \ldots, f_{n}\right)$ of the stream, where $f_{i}=\left|\left\{j: a_{j}=i\right\}\right|$ is the number of elements of value $i$. Note that $f_{1}+f_{2}+\cdots+f_{m}=m$. In particular, we want to estimate the second moment

$$
F_{2}=\sum_{i=1}^{n} f_{i}^{2}
$$

## 1 Naive attempt: downsampling

Since we are dealing with a "big data" problem, we may first downsample the input into a smaller length, then we calculate the second moment of the down sample and we use it to estimate the second moment of the original input. Consider the following set of two inputs.

$$
\begin{aligned}
& 1,2,3,4, \ldots, n \\
& \underbrace{1,1, \ldots, 1}_{m \text { times }}, \underbrace{2,2, \ldots, 2}_{m \text { times }}, \ldots, \underbrace{n / m, n / m, \ldots, n / m}_{m \text { times }}
\end{aligned}
$$

where $m=\Omega(\sqrt{n})$. Observe that any downsample of the first sequence gives completely distinct numbers, and any downsample of the second sequence of size $O(\sqrt{n})$ also gives almost distinct numbers with a high probability. So, any streaming algorithm that is based on downsampling sees almost the same thing, i.e., completely distinct elements, in both cases. However, the second moment of the first sequence is $n$ and the second moment of the second one is $O\left(n^{3 / 2}\right)$, so we don't expect a streaming algorithm based on downsampling to size at most $O(\sqrt{n})$ obtain an estimate better than $\sqrt{n}$ of the true second moment.

## 2 AMS Sketch

Let us first define $k$-wise independent family of hash functions.

Definition 1 A family of hash functions $H=\{h:[n] \rightarrow U\}$ is a $k$-wise independent if for any $k$ distinct elements $\left(x_{1}, \cdots, x_{k}\right) \in U^{k}$ and any numbers $\left(u_{1}, \cdots, u_{k}\right)$, we have:

$$
\operatorname{Pr}_{h \in H}\left[h\left(x_{1}\right)=u_{1} \wedge \cdots \wedge h\left(x_{k}\right)=u_{k}\right]=\left(\frac{1}{|U|}\right)^{k}
$$[^0]

## Initialization:

```
(1) Pick a 4-wise independent hash function: $h:[n] \rightarrow\{-1,+1\}$

(2) Let $\sigma_{i}=h(i)$ so $\sigma \in\{-1,1\}^{n}$

(3) Let $Z=0$.

Process element of value $i: Z=Z+\sigma_{i}$

Output: $Z^{2}$
```

Note that at the end of the algorithm we have that $Z=\sum_{i=1}^{n} f_{i} \sigma_{i}$. As for distinct elements, it is crucial to bound the expected value and variance of $Z^{2}$ in the above algorithm. We start by proving that it is an unbiased estimator.

## Claim 2

$$
\mathbb{E}\left[Z^{2}\right]=\|f\|_{2}^{2}
$$

Proof

$$
\begin{aligned}
\mathbb{E}\left[Z^{2}\right] & =\mathbb{E}\left[\left(\sum_{i \in[n]} \sigma_{i} f_{i}\right)^{2}\right] \\
& =\mathbb{E}\left[\sum_{i, j \in[n]} \sigma_{i} \sigma_{j} f_{i} f_{j}\right] \\
& =\mathbb{E}\left[\sum_{i \in[n]} \sigma_{i}^{2} f_{i}^{2}\right]+\mathbb{E}\left[\sum_{i \neq j \in[n]} \sigma_{i} \sigma_{j} f_{i} f_{j}\right] \\
& =\mathbb{E}\left[\sum_{i \in[n]} f_{i}^{2}\right]+\sum_{i \neq j \in[n]} \mathbb{E}\left[\sigma_{i}\right] \mathbb{E}\left[\sigma_{j}\right] f_{i} f_{j} \\
& =\|\mathbf{f}\|_{2}^{2}
\end{aligned}
$$

Next we bound the variance of the output (to later be apply to apply Chebychev's Inequality).

## Claim 3

$$
\operatorname{Var}\left[Z^{2}\right] \leq 2\|\boldsymbol{f}\|_{2}^{4}
$$

Proof Recall that, one can compute the variance of a random variable using the following formula:

$$
\operatorname{Var}\left[Z^{2}\right]=\mathbb{E}\left[Z^{4}\right]-\left(\mathbb{E}\left[Z^{2}\right]\right)^{2}
$$

Therefore, let us first compute $\mathbb{E}\left[Z^{4}\right]$.

$$
Z^{4}=\left(\sum_{i \in[n]} \sigma_{i} f_{i}\right)\left(\sum_{j \in[n]} \sigma_{j} f_{j}\right)\left(\sum_{k \in[n]} \sigma_{k} f_{k}\right)\left(\sum_{l \in[n]} \sigma_{l} f_{l}\right)
$$

Let us consider several types of terms:

- all the indexes are equal $i=j=k=l$ : $\sum_{i \in[n]} \sigma_{i}^{4} f_{i}^{4}=\sum_{i \in[n]} f_{i}^{4}$
- the indexes are matched 2 by 2 :

$\binom{4}{2} \sum_{i<j}\left(\sigma_{i} \sigma_{j} f_{i} f_{j}\right)^{2}=6 \sum_{i<j} f_{i}^{2} f_{j}^{2}$

- terms with a single (unmatched) multiplier: in this case, since the value $\mathbb{E}\left[\sigma_{i}\right]=0$ for any $1 \leq$ $i \leq n$, then the coefficient of such terms are zero. (Here we use that our hash function is 4 -wise independent.)

Therefore, $\mathbb{E}\left[Z^{4}\right]=\sum_{i \in[n]} f_{i}^{4}+6 \sum_{i<j} f_{i}^{2} f_{j}^{2}$. So the variance of $Z^{2}$ is :

$$
\begin{aligned}
\operatorname{Var}\left[Z^{2}\right] & =\mathbb{E}\left[Z^{4}\right]-\left(\mathbb{E}\left[Z^{2}\right]\right)^{2} \\
& =\sum_{i \in[n]} f_{i}^{4}+6 \sum_{i<j} f_{i}^{2} f_{j}^{2}-\left(\sum_{i} f_{i}^{2}\right)^{2} \\
& =\sum_{i} f_{i}^{4}+6 \sum_{i<j} f_{i}^{2} f_{j}^{2}-\sum_{i} f_{i}^{4}-2 \sum_{i<j} f_{i}^{2} f_{j}^{2} \\
& =4 \sum_{i<j} f_{i}^{2} f_{j}^{2} \\
& \leq 2\left(\sum^{2} f_{i}^{2}\right)^{2} \\
& =2\|\mathbf{f}\|_{2}^{4}
\end{aligned}
$$

We have $\mathbb{E}\left[Z^{2}\right]=\|\mathbf{f}\|_{2}^{2}$ and $\operatorname{Var}\left[Z^{2}\right] \leq 2\|\mathbf{f}\|_{2}^{4}$. Now we improve the precision of the estimate by repeating the algorithm for a sufficient number of times (independently) and using the average as an estimate.

(1) For $t=\frac{6}{\epsilon^{2}}$, maintain $t$ i.i.d copies of the above algorithm. Let $Z_{1}^{2}, Z_{2}^{2} \cdots Z_{t}^{2}$ be the output of these copies.

(2) Let $\tilde{Z}^{2}=\frac{1}{t} \sum_{i=1}^{t} Z_{i}^{2}$.

(3) Output $\tilde{Z}^{2}$.

By linearity of expectation, we have $\mathbb{E}\left[\tilde{Z}^{2}\right]=\|\mathbf{f}\|_{2}^{2}$. However, the variance becomes smaller. In particular, the variance of the estimate is now $\frac{\operatorname{Var}\left(Z^{2}\right)}{t} \leq \frac{2}{t}\|\mathbf{f}\|_{2}^{4}$. By Chebyshev's inequality we get

$$
\begin{aligned}
\operatorname{Pr}\left[\left|\tilde{Z}^{2}-\|\mathbf{f}\|_{2}^{2}\right|>\epsilon \mid \mathbf{f} \|_{2}^{2}\right] & \leq \frac{\left(\frac{2}{t}\right) \cdot\|\mathbf{f}\|_{2}^{4}}{\epsilon^{2}\|\mid \mathbf{f}\|_{2}^{4}} \\
& \leq \frac{2}{t \epsilon^{2}} \\
& \leq \frac{1}{3}
\end{aligned}
$$

## 3 AMS sketch and the Johnson-Lindenstrauss lemma

We just constructed an algorithm for approximating the $L_{2}$ norm of a vector $x \in \mathbf{R}^{n}$ using the AMS sketch, given a stream of updates to entries of $x$. We generated a random matrix $A \in \mathbf{R}^{m \times n}$ by independently and uniformly sampling each entry $A_{i j}$ from $\{1,-1\}$. We then proved that $\forall \epsilon>0$, if the dimension $m=O\left(\frac{1}{\epsilon^{2}}\right)$, then $\forall x \in \mathbf{R}^{n}$ :

$$
\operatorname{Pr}\left|\|A x\|_{2}^{2}-m\|x\|_{2}^{2}\right|>\epsilon m\|x\|_{2}^{2}<\frac{1}{3}
$$

This implies that with probability at least $\frac{2}{3},(1-\epsilon)\|x\|_{2} \leq\left\|\frac{1}{\sqrt{m}} A x\right\|_{2} \leq(1+\epsilon)\|x\|_{2}-$ this follows because for any $0<\epsilon<1, \sqrt{1+\epsilon}<1+\epsilon$ and $\sqrt{1-\epsilon}>1-\epsilon$.

### 3.1 Sketch using a Gaussian distribution

We consider another sketch $A \in \mathbf{R}^{m \times n}$, where $\forall 1 \leq i, j \leq n, A_{i j} \sim \mathcal{N}(0,1)$. Examining the conditions imposed on the $A$ 's coefficients in the last lecture, we notice that both still hold:

1. $E\left[A_{k i} A_{k j}\right]=0, \forall i \neq j, 1 \leq k \leq m$ because the variables are independent.
2. $E\left[A_{i k}^{2}\right]=1, \forall 1 \leq i \leq m, 1 \leq k \leq n$ by definition.

The new sketch has an additional property: $1 \leq i \leq n,(A x)_{i}=\sum_{j=1}^{n} A_{i j} x_{j} \sim \mathcal{N}\left(0,\|x\|_{2}^{2}\right)$. This is known as the 2-stability of the Gaussian distribution.

Most importantly, it is possible to prove a strong Chernoff-type concentration inequality for $\|A x\|_{2}$. Specifically, $\|A x\|_{2}^{2}=\sum_{i=1}^{m}(A x)_{i}^{2}=\sum_{i=1}^{m} y_{i}^{2}, y_{i} \sim \mathcal{N}\left(0,\|x\|_{2}^{2}\right)$ follows a $\chi^{2}$ with $m$ degrees of freedom. The following bound holds for this distribution:

$$
\operatorname{Pr}\left|\|A x\|_{2}^{2}-m\|x\|_{2}^{2}\right|>\epsilon m\|x\|_{2}^{2}<e^{-C \epsilon^{2} m} \text { for a constant } C>0
$$

### 3.2 Johnson - Lindenstrauss lemma

Lemma 4 For any $\epsilon \in\left(0, \frac{1}{2}\right), \forall x_{1}, \cdots, x_{n} \in \mathbf{R}^{d}$, there exists $M \in \mathbf{R}^{m \times d}$ with $m=O\left(\frac{1}{\epsilon^{2}} \log n\right)$ such that for all $1 \leq i, j \leq n$ :

$$
(1-\epsilon)\left\|x_{i}-x_{j}\right\|_{2} \leq\left\|M x_{i}-M x_{j}\right\|_{2} \leq(1+\epsilon)\left\|x_{i}-x_{j}\right\|_{2}
$$

Remark This is a statement about dimensionality reduction. The dimension to which the $\mathbf{R}^{d}$ vectors are reduced, $m$, does not depend on $d$, only on the number of vectors.

Proof Fix two indices $i \neq j$ and let $y^{i j}=x_{i}-x_{j}$ and $M=\frac{1}{\sqrt{m}} A$, where $A \in \mathbf{R}^{m \times n}$ has i.i.d. elements sampled from $\mathcal{N}(0,1)$. By the previous result and setting $m=\frac{4}{C \epsilon^{2}} \log n$ :

$$
\operatorname{Pr}\left|\left\|M y^{i j}\right\|_{2}^{2}-\left\|y^{i j}\right\|_{2}^{2}\right|>\epsilon\left\|y^{i j}\right\|_{2}^{2}<e^{-C \epsilon^{2} m}=e^{-C \epsilon^{2} \frac{4}{C \epsilon^{2}} \log n}=\frac{1}{n^{4}}
$$

Next, by taking the union bound:

$$
\begin{aligned}
\operatorname{Pr} \exists i \neq j,\left|\left\|M y^{i j}\right\|_{2}^{2}-\left\|y^{i j}\right\|_{2}^{2}\right|>\epsilon\left\|y^{i j}\right\|_{2}^{2} & \leq \sum_{i \neq j} \operatorname{Pr}\left|\left\|M y^{i j}\right\|_{2}^{2}-\left\|y^{i j}\right\|_{2}^{2}\right|>\epsilon\left\|y^{i j}\right\|_{2}^{2} \\
& <\binom{n}{2} \frac{1}{n^{4}} \\
& <\frac{1}{n^{2}}
\end{aligned}
$$

Therefore $\operatorname{Pr} \forall i \neq j,\left|\left\|M x_{i}-M x_{j}\right\|_{2}^{2}-\left\|x_{i}-x_{j}\right\|_{2}^{2}\right| \leq \epsilon\left\|x_{i}-x_{j}\right\|_{2}^{2}>1-\frac{1}{n^{2}}$. The probability is taken w.r.t the law of $M$, which allows us to conclude the existence of at least one matrix $M$ satisfying the desired inequality.

Remark The bound for $m$ is optimal, as proved by a very recent result Larsen-Nelson'16.


[^0]:    ${ }^{1}$ Disclaimer: These notes were written as notes for the lecturer. They have not been peer-reviewed and may contain inconsistent notation, typos, and omit citations of relevant works.

