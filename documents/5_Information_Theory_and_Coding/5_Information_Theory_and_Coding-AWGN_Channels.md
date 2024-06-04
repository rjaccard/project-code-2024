
## Lecture 18: Awgn Channels

In this lecture, we will use our previous tools to investigate Additive White Gaussian Noise (AWGN) channels and their properties.

## 1 Simple Awgn Channel

Suppose we are given an input variable $X$ that we wish to transmit through a channel of probability distribution $p_{Y|X}$ such that it outputs $Y=X+Z$ where $Z\sim\mathcal{N}(0,\sigma^{2})$. Let $b(X)=X^{2}$ be the cost function for this scheme. Let us compute the capacity of this channel. Recall that for some $\beta$, the capacity is defined by

$$C(\beta)=\max_{X,\,\|X^{2}\|\leq\beta}I(X;Y).$$
We have:

$C=\max h(Y)-h(Y|X)$

$=\max h(X+Z)-h(X+Z|X)$ by definition of $Y$

$=\max h(X+Z)-h(Z|X)$ since $X$ is supposedly known

$=\max h(X+Z)-h(Z)$ by independence of $X$ and $Z$

$=\max h(X+Z)-\frac{1}{2}\log(2\pi e\sigma^{2})$ since $Z$ is Gaussian.

Now, we know that E[(X +Z)^2] = E[X^2 +Z^2 +2XZ] ≤ β +σ^2 by our constraints, the definition of Z and the indepencence of X and Z, respectively. This directly implies that *Var*(X +Z) ≤ β +σ^2 and hence h(X + Z) ≤ log(2πe(β + σ2))/2 with equality iff X + Z is a zero-mean Gaussian with variance β +σ2. Since a sum of Gaussians is Gaussian with variance equal to the sum of variances, choosing X ∼ N(0, β) yields the maximum possible mutual information I(X; Y ). For this choice,

$$C={\frac{1}{2}}\log{\frac{2\pi e(\beta+\sigma^{2})}{2\pi e\sigma^{2}}}={\frac{1}{2}}\log\left(1+{\frac{\beta}{\sigma^{2}}}\right),$$
where *β/σ*2 is often referred to as the Signal to Noise Ratio (or SNR in short). Note that for large
β/σ2, the +1 term becomes negligible so that C = log(β/σ^2)/2.

## 2 Parallel Awgn Channels

Let $X\in\mathbb{R}^{k}$ be the input to a channel and $Y\in\mathbb{R}^{k}$ be its output, where $Y_{i}=X_{i}+Z_{i}\,\forall i$ in which the $Z_{i}$'s are independent zero-mean Gaussians each of respective variance $\sigma_{i}^{2}$. In this scenario, we order the variances such that $\sigma_{i}^{2}\leq\sigma_{i}^{2}\leq\ldots\leq\sigma_{i}^{2}$. Let $b(X_{1},\ldots,X_{k})=X_{1}^{2}+\ldots+X_{k}^{2}$ be our cost function. We wish to compute the maximum mutual information $C(\beta)$ subject to the $X^{k}$ being such that $\sum_{k}E[X_{k}^{2}]\leq\beta$. In other words, we want to compute

$$C(\beta)=\max_{X^{k}\cdot\sum_{k}E[X_{k}^{2}]\leq\beta}I(X^{k};Y^{k}).$$

This problem essentially translates to maximising a concave function on the simplex scaled by β.

We establish the necessary and sufficient conditions for the βi's to be maximisers: there must exist a µ such that


$$\frac{∂}{∂βi} \sum_{i=1}^{k}\frac{1}{2}\log\left(1+\frac{\beta_{i}}{\sigma_{i}^{2}}\right)\leq\mu\,\forall i,$$

with equality only for the $i$'s such that $\beta_{i}>0$. Note that when computing the derivative, the above term becomes $1/(\beta_{i}+\sigma_{i}^{2})$. Hence, there must exist a $\mu$ such that $1/(\beta_{i}+\sigma_{i}^{2})\leq\mu\,\forall i$ and $=\mu$ for only the $i$'s such that $\beta_{i}>0$. We can let $\beta_{i}$ be the positive part of $(1/\mu-\sigma_{i}^{2})$, i.e. $\beta_{i}=(1/\mu-\sigma_{i}^{2})^{+}$ with $\mu$ chosen so that $\beta_{i}=\sum\beta_{i}=\sum(1/\mu-\sigma_{i}^{2})^{+}$. This is called the **water filling solution**.