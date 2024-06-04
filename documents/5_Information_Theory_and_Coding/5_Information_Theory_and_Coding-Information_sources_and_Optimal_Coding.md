
## Lecture 3: Information Sources And Optimal Coding

Today's lecture's aim is to convince ourselves that the preceding bounds we have given for the expected code length are correct and start mentioning the importance of optimising codes.

## 1 More On Information Sources 1.1 Kl-Divergence

Recall the last inequality we introduced in the previous lecture, namely

$$\sum_{u\in\mathcal{U}}p(u)\log_{2}\frac{q(u)}{p(u)}\leq H(U)-\log_{2}\sum_{u\in\mathcal{U}}q(u).$$

Notice that if both $p$ and $q$ are valid distributions, then the term on the right becomes $0$ as $\log_{2}(1)=0$. We have $\sum_{u\in\mathcal{U}}p(u)\log_{2}\frac{q(u)}{p(u)}\leq0$, which we can rewrite as

$$\sum_{u\in\mathcal{U}}p(u)\log_{2}\frac{p(u)}{q(u)}\geq0\triangleq D(p||q),$$
which gives us what is commonly called the **KL divergence** (or relative entropy).

This new quantity (where we simply swapped the numerator and the denominator in the log) essentially represents how close two probability distributions are to each other. Note that this inequality becomes an equality iff both probabilites are equal, i.e. p = q.

## 1.2 Meaning Of Code Lengths

Given a prefix-free code with Kraft Sum less than 1, we can always try to find shorter codewords
(if possible) by getting closer to the root of the tree. Note that a well designed prefix-free code will have a Kraft Sum equal to 1. Then

$$E[length(c(U))]-H(U)=\sum_{u\in\mathcal{U}}p(u)\left(length(c(u))-\log_{2}\frac{1}{p(u}$$ $$=\sum_{u\in\mathcal{U}}p(u)\log_{2}\frac{p(u)}{q(u)}=D(p||q)\geq0.$$

Suppose now that $q(u)=2^{-length(c(u))}$ sums to less than $1$. It is a good idea to invent a fictitious letter $u_{0}\not\in\mathcal{U}$ such that $q(u_{0})=1-\sum_{u\in\mathcal{U}}q(u)$ (i.e. it makes it a valid distribution) and $p(u_{0})=0$. The quantity we computed before will remain the same.

To clarify,

$$D(p||q)=\sum_{u}p(u)\log_{2}\frac{p(u)}{q(u)}=\begin{cases}0&\text{if}p(u)=0\\ +\infty&\text{if}p(u)>0,q(u)=0,\\ \text{some other value}&\text{otherwise.}\end{cases}$$

## 1.2 Selecting valid distributions

The discussion so far suggests that, to design a good code c, we should choose a q_c(u) ≈ p(u).

When comparing the logarithms, we want − log2 qc(u) ≈ − log2 p(u). But how can we ensure that
− log2 qc(u) ∈ Z and − log2 p(u) is close to the distribution of q ? One may suggest the idea of rounding up q to the upper nearest integer. In that way, we would have

$1-\log_{2}p(u)>-\log_{2}q_{c}(u)=\lceil-\log_{2}p(u)\rceil\geq-\log_{2}p(u)+1$.

This actually guarantees that qc(u) is of the form 2−k with k ∈ Z and q_c(u) ≤ p(u). We would also have l(u) = ⌈− log2 p(u)⌉ satisfying Kraft's inequality and we would be sure that there exists a prefix free code with *length*(c(u)) = ⌈− log2 p(u)⌉ < − log2 p(u) + 1 and such that E[*length*(c(U))] ≤ H(U) + 1. It is also very important to remember that **any code, no matter how it is designed, lies within the interval** [H(U), H(U) + 1]. Let us formalise this last statement into a theorem:

Theorem 1 : Given a random variable U, there exists a prefix-free code c : U → {0, 1}∗ such that H(U) ≤ E[*length*(c(U))] ≤ H(U) + 1.

Corollary 2 : For every integer n, there exists a prefix-free code c_n : U^n → {0, 1}∗ such that H(U1 . . . Un) ≤ E[length(c_n(U1 *. . . U*n))] ≤ H(U1 *. . . U*n) + 1.

To illustrate the above, let U = {a, b, c} with respective probabilites 0.6, 0.2 and 0.2 and let U1, U2*, . . . , U*n be i.i.d random variables. c_2(aa) will be a binary sequence of length ⌈log_ \frac{1}{(0.6)^2} ⌉.

Similarly, c_2(ab) will be a binary sequence of length ⌈log_2 \frac{1}{(0.6)(0.2)}⌉ etc... Note that the above corollary gives us the actual number of bits used for the entire sequence. If we are only interested in the number of bits per symbol, we can add a 1/n normalisation factor on both sides of the inequality. This would give us

$${\frac{1}{n}}H(U_{1}\ldots U_{n})\leq{\frac{1}{n}}E[l e n g t h(c_{n}(U_{1}\ldots U_{n}))]\leq{\frac{1}{n}}H(U_{1}\ldots U_{n})+{\frac{1}{n}}.$$

Theorem 3 : Suppose U1, . . . , Un is an information source with alphabet U (i.e. U1, . . . , Un are random variables that take values in U).

Any injective sequence of codes c_n : U^n → {0, 1}∗ satisfies :

$$\frac{1}{n}E[length(c_{n}(U_{1},\ldots,U_{n}))]\geq\frac{1}{n}\left(H(U_{1},\ldots,U_{n})-\log_{2}\log_{2}(1+|{\cal U}|^{n})\right),$$
and there exists a sequence of prefix-free codes ˜c1, . . . , ˜cn such that

$\frac{1}{n}E[length(\tilde{c_{n}}(U_{1},\ldots,U_{n}))]\leq\frac{1}{n}H(U_{1},\ldots,U_{n})+\frac{1}{n}$.

For simplicity, one could consider the double logarithm as a very small value, say ϵn, as the first log cancels the power, and the normalisation by n cancels the logarithmic growth created by the second log. In other words, (log log(1 + |U|^n))/n → 0 as n *→ ∞*.

## 2 An Introduction To Optimal Codes

The goal of this part of the course is to, given an alphabet U and a probability distribution
{p(u) : u *∈ U}*, design a prefix-free code c so as to minimise the expected length of the code via the use of convex constraints. The minimisation problem will be written as follows:

$$\operatorname*{min}_{l:\sum_{u}2^{-l(u)}\leq1}\sum_{u}p(u)l(u).$$