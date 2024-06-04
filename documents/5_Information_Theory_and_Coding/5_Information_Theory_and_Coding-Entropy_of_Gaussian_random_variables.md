# Lecture 17: Entropy Of Gaussian Random Variables

In this lecture, we will continue our discussion on differential entropy whilst this time introducing the Gaussian random variable and its various interesting applications in information theory.

## 1 Entropy Of A Function Of Random Variables 1.1 Proof Of The Previous Theorems

Last time, we introduced two small theorems that we shall prove today.

To do so, we must introduce the Cumulative Distribution Function (CDF). Recall that last time we defined what differential entropy is for which we used the notion of probability density function. We can obtain it by differentiating the so called CDF. We write

$$f_{X}(x)=\lim_{\epsilon\searrow0}\frac{Pr(X\in(x-\epsilon,x])}{\epsilon}$$ $$=\lim_{\epsilon\searrow0}\frac{Pr(X\leq x)-Pr(X\leq x-\epsilon)}{\epsilon}$$ $$=\lim_{\epsilon\searrow0}\frac{F_{X}(x)-F_{X}(x-\epsilon)}{\epsilon}$$ $$=\frac{dF_{X}(x)}{dx}.$$

Theorem 1 : If a *is a constant,* h(a + X) = h(X).

Proof : Let Y = a + X. Then, note that F_Y (y) = Pr(Y ≤ y) = Pr(X ≤ y − a) = F_X(y − a).

When differentiating, we obtain f_Y (y) = f_X(y − a) and hence h(Y ) = h(X) which proves the theorem.

Theorem 2 : h(aX) = h(x) + log|a|.

Proof : Let Y = aX. We have

$F_{Y}(y)=Pr(Y\leq y)=\begin{cases}Pr(X\leq y/a)=F_{X}(y/a)&\text{if}a>0\\ Pr(X\geq y/a)=1-Pr(X\leq y/a)=1-F_{X}(y/a)&\text{if}a<0.\end{cases}$
Then,

$$f_{Y}(y)=\begin{cases}1/af_{X}(y/a)&\text{if}a>0\\ -1/af_{X}(y/a)&\text{if}a<0.\end{cases}=\frac{1}{|a|}f_{X}(y/a),$$
which is where the log constant comes from in the computation of the entropy. Hence

$$h(aX)=h(Y)=\int_{-\infty}^{+\infty}f_{Y}(y)\log\frac{1}{f_{Y}(y)}\,dy$$ $$=\int_{-\infty}^{+\infty}f_{Y}(y)\log\frac{|a|}{f_{X}(y/a)}\,dy$$ $$=\log|a|+\frac{1}{|a|}\int_{-\infty}^{+\infty}f_{X}(y/a)\log\frac{1}{f_{X}(y/a)}\,dy$$ $$=\log|a|+\int_{-\infty}^{+\infty}f_{X}(x)\log\frac{1}{f_{X}(x)}\,dx\text{by letting}x=y/a$$ $$=\log|a|+h(X),$$
which concludes the proof.

## 1.2 Functions Of Random Variables

It is often the case in probability to find random variables that are functions of random variables. Let for instance $X_{1}$ and $X_{2}$ be two random variables and define

$$\begin{pmatrix}Y_{1}\\ Y_{2}\end{pmatrix}=\begin{pmatrix}2X_{1}+X_{2}\\ X_{1}+2X_{2}\end{pmatrix}.$$
Then

$$h(Y_{1}Y_{2})=h(Y_{1})+h(Y_{2}|Y_{1})$$ $$=h(2X_{1}+X_{2})+h(X_{1}+2X_{2}|2X_{1}+X_{2})$$ $$=h(2X_{1}+X_{2})+h(X_{1}+2X_{2}+c(2X_{1}+X_{2})|2X_{1}+X_{2})\text{for some constant}c$$ $$=h(2X_{1}+X_{2})+h(3/2X_{2}|2X_{1}+X_{2})\text{by letting}c=1/2\text{such that}X_{1}\text{vanishes.}$$

$h(\tilde{Y}^{n})=h(Y^{n})$ but $h(\tilde{Y}^{n})=\sum_{i}^{n}\log[k_{ii}]+h(X^{n})=\sum_{i}^{n}\log[\tilde{a}_{ii}]+h(X^{n})=\log[det(\tilde{A})]+h(X^{n})=\log[det(A)]+h(X^{n})$.

From there, we can define two new random variables ˜Y1 and ˜Y2 with ˜Y1 = Y1 = 2X1 + X2 and
˜Y2 = 3/2X2. Note, Y1 and Y2 have the same entropy as ˜Y1 and ˜Y2 respectively since functions of random variables are not independent. Hence, for vectors of size n, we can in general write Y = AX implying that ˜Y = ˜
AX where ˜
A is obtained by the composition matrix A via some row operation, i.e. by subtracting a multiple of some row from some of another row. Via these operations, we can bring our equation to the form of ˜Y = BX where B is the diagonal matrix AI_n where I_n is the identity matrix of size n (so non-zero values on the diagonal only).

## 2 Application To Gaussian Random Variables

Let X ∼ N(*µ, σ*2). Note that w.l.o.g., we can safely assume that µ = 0. Since the entropy doesn't depend on µ, it can be treated as a constant.

## 2.1 Single Random Variable

Let $Y=(X-\mu)/\sigma$ be such that the entropy is changed by a $\log\sigma$ factor. $Y$ is called the standard normal, i.e. $Y\sim{\cal N}(0,1)$. Let us compute the entropy of $X$. Recall that if $Y$ is a normalised Gaussian,

$$f_{Y}(y)=\frac{1}{2\pi}e^{-y^{2}/2}.$$ We have

$$-\log f_{Y}(y)=\frac{1}{2}\log2\pi+\frac{1}{2}y^{2}\log e.$$
Now, by treating y as a random variable, we have

$$E\left[-\log f_{Y}(Y)\right]=\frac{1}{2}\log2\pi+\frac{1}{2}E\left[Y^{2}\log e\right]=\frac{1}{2}\log(2\pi e),$$

since $E[Y^{2}]=1$. Consequently, if $X\sim\mathcal{N}(\mu,\sigma^{2})$, then $h(X)=\frac{1}{2}\log(2\pi e\sigma^{2})$.

## 2.2 Generalisation To Gaussian Vectors

Introduction : Suppose we wish to generalise the above computations to higher dimensions. Let for instance Xn ∼ N(µ, Σ), where µ is the vector of means of each Xi and Σ is the covariance matrix.

To find h(Xn), we assume again w.l.o.g that µ = 0. Then Σ = E[XX^T ] (since µµ^T = 0). Observe that for any a ∈ Rn, a^T Σa = aT E[XX^T]a = E[(a^T X)(X^T a)] = E[(a^T X)^2] ≥ 0. This shows that our covariance matrix Σ is positive semi-definite. In particular, Σ = AA^T . This provides a good factorisation of our covariance matrix. In fact, Σ = UΛU^T where U is orthogonal (such that UU^T = In) and Λ ≥ 0 is diagonal.

Problem formalisation : Consider now Y = A^{−1}X (note that Y ∼ N(0, In)). Each Yi are iid unit variance and zero mean Gaussian random variables ! From there, we have that h(Y^n) = n/2 log(2πe) so that

$$h(X^{n})=\log\!\left|d e t(A)\right|+\frac{n}{2}\log(2\pi e)=\frac{1}{2}\log d e t\mathbf{\Sigma}+\frac{n}{2}\log(2\pi e)=\frac{1}{2}\log d e t(2\pi e\mathbf{\Sigma}).$$

So, given Xn ∼ N(0, Σ) we have that

$$h(X^{n})={\frac{1}{2}}\log d e t(2\pi e\Sigma).$$

Generalising this to a single random variable gives us the following important theorem.

**Theorem 3**: _(Gaussian r.v's have the highest entropy) Suppose $X$ is a r.v. with variance $\sigma^{2}$. Then,_

$$h(X)\leq\frac{1}{2}\log(2\pi e\sigma^{2})$$
with equality if and only if X ∼ N(µ, σ2).

Therefore, among all random variables, the normal one has the largest entropy. Proof Again w.l.o.g, assume that X has 0 mean. such that E[X2] = σ2. Let

$$g_{X}(x)={\frac{1}{\sigma{\sqrt{2\pi}}}}e^{-x^{2}/2\sigma^{2}}$$ be the pdf of a zero mean Gaussian r.v. of variance $\sigma^{2}$. We have that $\log1/g_{X}(x)$ can be rewritten as $C+Dx$ where $C$ and $D$ are two constant values. Then:

$$\int f_{X}(x)\log\frac{1}{g_{X}(x)}\,dx=\int g_{X}(x)\log\frac{g_{X}(x)}{g_{X}(x)f_{X}(x)}\,dx=\frac{1}{2}\log(2\pi\sigma^{2}).$$
Now, note

$$h(X)=\int f_{X}(x)\log\frac{1}{f_{X}(x)}\,dx$$ $$=\int f_{X}(x)\log\frac{g_{X}(x)}{g_{X}(x)f_{X}(x)}\,dx$$ $$=\int f_{X}(x)\log\frac{1}{g_{X}(x)}\,dx-\int f_{X}(x)\log\frac{f_{X}(x)}{g_{X}(x)}\,dx$$ $$=\int f_{X}(x)\log\frac{1}{g_{X}(x)}-D(f||g)$$ $$=\frac{1}{2}\log(2\pi\sigma^{2})-D(f||g)$$ $$\leq\frac{1}{2}\log(2\pi\sigma^{2}),$$
since D(f||g) is always non-negative. This concludes the proof.

Similarly

**Theorem 4**: _(Generalisation of the previous thm to $n$ dimensions) If $X^{n}$ is a random vector with covariance matrix $\mathbf{\Sigma}$, then_

$$h(X^{n})\leq\frac{1}{2}\log\det(2\pi e\mathbf{\Sigma})$$
with equality iff X is normal. In words, Gaussians are entropy maximisers under covariance constraints.

Theorem 5 If X ≥ 0 *with* E[X] = 1, h(X) ≤ h(Y ) when Y ∼ *Exp*(1).

The proof of the above theorem follows from the above computations.