# Lecture 7: Typicality, Typical Sets, Entropy And Divergence

Last time, we shortly introduced the notion of typicality. Today, we will dive deeper into the notion of ϵ-typicality and determine its uses in information theory.

## 1 Useful Probability Bounds

Before diving into notions concerning typicality and typical sets, it is important to recall some basic but useful probability bounds that we will use all along this course.

1. First of all, if X ≥ 0, its expected value E[X] is also ≥ 0 as expectation is linear operator.
2. Consider now X+ = max{X, 0}, i.e. only the positive part of X. Then, if X+ − 1_{X≥1} ≥ 0, we have Pr(X ≥ 1) ≤ E[X+].
3. The preceding bound brings us to Markov's inequality which states that for any *a >* 0,
$$Pr(X\geq a)\leq{\frac{E[X]}{a}}.$$
4. From Markov, we can derive Chebyshev's inequality by letting Y be such that *Var*(X) = Y .
This gives us
$$Pr(|X-E[X]\geq a^{2})\leq\frac{Var(X)}{a^{2}}.$$
5. Let now $X_{1},X_{2},\ldots,X_{n}$ be i.i.d random variables. Applying Chebyshev's inequality to the sum $\frac{1}{n}\sum_{i}X_{i}$ gives us 
$$Pr\left(\left|\frac{1}{n}\sum_{i=1}^{n}X_{i}-E[X_{i}]\right|\geq a\right)\leq\frac{Var(X_{1})}{na^{2}}.$$
6. The last fundamental bound is what is called the Weak Law of Large Numbers (WLLN), obtained by taking a limit of the above probability when $n\rightarrow\infty$ (only in the equality case), i.e. $$\lim_{n\rightarrow\infty}Pr\left(\left|\frac{1}{n}\sum_{i=1}^{n}X_{i}-E[X_{i}]\right|=a\right)=0.$$

## 2 Typicality and typical sets

## 2.1 Formal Definition

Last time, we introduced the notion of typicality. Recall:

Definition 1 : Given an alphabet U, a probability distribution p on U, a positive integer n and an
ϵ > 0, we call

$$T(n,p,\epsilon)=\{u^{n}\in\mathcal{U}^{n}:\forall u\in\mathcal{U},\,\frac{1}{n}\sum_{i}\mathds{1}_{\{U_{i}=u\}}\in[(1-\epsilon)p(u),(1+\epsilon)p(u)]\},$$

to be the set of ϵ-typical sequences of length n w.r.t. p. 

Some examples could be the following:
1. Let U = {*a, b*}, p(a) = 0.6, p(b) = 0.4, n = 5 and ϵ = 1/10. Then, T is made of the total number of permutations of strings of length 5 containing exactly 3 a's and 2 b's, i.e. T = {*aaabb, ababa, . . . , bbaaa*}.

## 2.2 Limiting Values Of Typicality

Theorem 2 : Fix U, p_U and ϵ > 0. Also, suppose U1, U2, . . . , Un are i.i.d ∼ p_U. Then
lim_{n→∞} Pr(U^n ̸∈ T(n, p_U, ϵ)) = 0.

## 2.3 Typicality With Entropy And Divergence

Proposition 3 : Fix U, a distribution p on U and let ϵ > 0. Let U1, U2, . . . , Un be i.i.d ∼ q where q can for instance be the distribution of a biased coin. Then, for any u^n ∈ T(n, p, ϵ), Pr(U^n = u^n) = 2^{−n(1+ϵ)[H(p)+D(p||q)]}.

Proof : We start with Pr(U^n = u^n) = q(u1)q(u2) *. . . q*(un). Taking the log on both sides gives us an easier expression:

$\log Pr(U^{n}=u^{n})=\sum_{i}\log q(u_{i})$

$=\sum_{\alpha\in\mathcal{U}}np(\alpha)(1\pm\epsilon)\log q(\alpha)$.

To write the bound in a more formal way, we have

$n(1+\epsilon)\sum_{\alpha}p(\alpha)\log q(\alpha)\leq\log Pr(U^{n}=u^{n})\leq n(1-\epsilon)\sum_{\alpha}p(\alpha)\log q(\alpha)$.

Note the reversed inequality signs, due to the fact that log q(α) is a negative quantity as q is a probability distribution. From there, we can split the log into a sum of two logs as follows:

$$\sum_{\alpha}p(\alpha)\log q(\alpha)=\sum_{\alpha}p(\alpha)\log p(\alpha)+\sum_{\alpha}p(\alpha)\log\frac{q(\alpha)}{p(\alpha)}=-H(p)+D(p||q).$$
This concludes the proof.

Corollary 4 : If U1, U2, . . . , Un are i.i.d ∼ p and un ∈ T(n, p, ϵ), then
$2^{−n(1+ϵ)H(p)} ≤ Pr(U^n = u^n) ≤ 2^{−n(1+ϵ)H(p)}$.

To prove the above corollary, we simply set p = q in the previous theorem and the bounds become trivial.

Corollary 5 : $$|T(n,p,\epsilon)\leq2^{n(1+\epsilon)H(p)}.$$

Proof : To prove this bound, first note that the number of elements in the set cannot be bigger than the reciprocal of the above bound. From there, we have

$$1\geq Pr(U^{n}\in T)=\sum_{u^{n}\in T}Pr(U^{n}=u^{n})\geq\sum_{u^{n}\in T}2^{-n(1+\epsilon)H(p)}=|T|2^{-n(1+\epsilon)H(p)},$$
which proves the bound.

Corollary 6 : For any ϵ > 0 and for n > n0(ϵ),

$$|T(n,p,\epsilon)\geq(1-\epsilon)2^{n(1-\epsilon)H(p)}$$

**Proof** : We know that $\lim_{n\to\infty}Pr(U^{n}\in T(n,p,\epsilon))=1$ as $U^{n}$ are i.i.d $\sim p$. From there, we know that there exists an $n(\epsilon)$ where $\forall n\geq n(\epsilon)$, $Pr(U^{n}\in T(n,p,\epsilon))\geq1-\epsilon$. So

$$(1-\epsilon)\leq Pr(U^{n}\in T(n,p,\epsilon))=\sum_{u^{n}\in T}Pr(U^{n}=u^{n})\leq\sum_{u^{n}\in T}2^{-n(1-\epsilon)H(p)}=|T|2^{-n(1-\epsilon)H(p)},$$
which again proves the desired bound.