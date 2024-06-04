
## Lecture 16: Continuous Information Measures

In this lecture, we will conclude our discussion on communication channels that accept discrete inputs and will move to a little more realistic and applicative scenario in which the input is continuous.

## 1 Differential Entropy

So far, we have studied communication channels that accept a countable (i.e. discrete) alphabet X *∈ X* with associated probability distribution pX(x) s.t. $\sum_x P_X(x) = 1$. From now on, we will assume a continuous input, that is, a random variable X ∈ R with associated probability density function f_X(x). Note that, compared to a discrete probability mass function, the pdf can be more than 1, but it must however remain positive at all times. 

**Definition 1 (Differential Entropy)**: Similarly to the discrete entropy, the continuous one is defined using an integral instead of a sum. Namely,

$$h(X)=\int f_{X}(x)\log{\frac{1}{f_{X}(x)}}\,d x=E\left[\log{\frac{1}{f_{X}(X)}}\right]$$

Note that the differential entropy shares some properties with its discrete relative, however not all of them apply. For instance, differential entropy can be negative ! 

**Definition 2 (Chain rule for densities)**: If X and Y are two random variables, then

$f_{XY}(x,y)=f_{X}(x)f_{Y|X}(y|x)=f_{Y}(y)f_{X|Y}(x|y)$.

Similarly, for n random variables X1, . . . , Xn, we define

$f_{X^{n}}(x^{n})=f_{X_{1}\ldots X_{n}}(x_{1},\ldots,x_{n})=f_{X_{1}}(x_{1})f_{X_{2}|X_{1}}(x_{2}|x_{1})\ldots f_{X_{n}|X_{1}\ldots X_{n-1}}(x_{n}|x_{1},\ldots,x_{n-1})$.

**Definition 3 (Joint differential entropy)** : Suppose X1, . . . , Xn are n real valued random variables with joint pdf fXn(xn). Their joint differential entropy is defined as

$$h(X^{n})=\int_{\mathbb{R}^{n}}f_{X^{n}}(x^{n})\log\frac{1}{f_{X^{n}}(x^{n})}\,dx^{n}=E\left[\log\frac{1}{f_{X^{n}}(x^{n})}\right].$$

Note that we can express the joint differential entropy in terms of the conditional one using the chain rule. We obtain

$$h(X^{n})=\sum_{i}E\left[\log\frac{1}{f_{X_{i}|X^{i-1}}(x_{i}|x^{i-1})}\right]=\sum_{i}h(X_{i}|X^{i-1}).$$
Note that the "conditioning reduces entropy" property is still valid here, i.e. h(X|Y ) ≤ h(X).

## 2 Continuous KL Divergence

Compared to the differential entropy, the continuous KL divergence keeps the exact same properties as the discrete one. Note that using the ideas of the fundamental theorem of calculus, we can approximate the continuous KL divergence in terms of the discrete one. This can be done by seeing an integral as an infinite addition of small volumes. 

## 3 Continuous Mutual Information

**Definition 5** : For X and Y being real valued random variables, we define

$$I(X;Y)=h(X)-h(X|Y)=h(Y)-h(Y|X)$$ 
$$=h(X)+h(Y)-h(XY)\text{by the chain rule}$$ 
$$=D(f_{XY}||f_{X}f_{Y})\geq0,$$
with equality iff X ⊥ Y .

We also define joint and conditional mutual information in the exact same way as we defined it for discrete distributions.

## 4 Relation Between Discrete And Continuous Domains

In this section, we wish to express the continuous mutual information in terms of the discrete one by performing a similar computation to what we did for the KL divergence. Namely, we would like to express it as a limit of the discrete one and for this, we will use what is called *quantization*.

## 4.1 General Idea

Let X be a r.v. with density f and ˜X be one with density g and consider the quantization of x. For the purpose, we pick a partitioning of R made of disjoint intervals {Ii}i≥1 and let *Quant*(x) = i if x ∈ Ii. Furthermore, we let U = *Quant*(X) and ˜U = *Quant*( ˜X) such that each has pmf p and q, respectively. When computing the limit of D(p||q) as max_i *vol*(Ii) → 0, we obtain D(f||g).

Because of this, I(X; Y ) is the limit of I(Quant(X)*, Quant*′( ˜X)) as both quantizations get finer and finer. That is, we quantize to more and more precise values. Note that for any *Quant*(·) and Quant′(·), Quant(X)—X—Y —*Quant*′(Y ) form a Markov chain. This limit can in fact be seen as a supremum since we have a finite quantization of decreasing values.

## 4.2 Quantization Applied To Differential Entropy

What happens now if we decide to quantize $h(\cdot)$? Suppose for instance that $X\in\mathbb{R}$ and $Q(\cdot)$ is the uniform scalar quantizer, i.e. we divide the real axis into many small intervals of equal size $\Delta$. $Q(x)=i$ s.t. $i\Delta\leq x\leq(i+1)\Delta$, i.e. we find the interval $x$ falls into. Let $U=Q(X)$ and let us now see the relation between $H(U)$ and $h(X)$. Similarly to previous computations, for a partitioning of $\mathbb{R}$ into disjoint intervals $I_{i}$ where $x_{i}\in I_{i}$ in which $I_{i}=[i\Delta,(i+1)\Delta]$, we have

$$h(X)\approx\sum_{i}f(x_{i})vol(I_{i})\log\frac{1}{f(x_{i})}$$ $$\approx\sum_{i}Pr(U=i)\log\frac{\Delta}{Pr(U=i)}\text{given that}f(x_{i})\approx Pr(U=i)/vol(I_{i})$$ $$=H(U)+\log\Delta.$$

This brings us to the following theorem. Theorem 6 Given a real valued r.v. X,

$$\operatorname*{lim}_{\Delta\to0}H(Q u a n t_{\Delta}(X))+\log\Delta=h(X).$$

Hence, discrete and continuous entropies are related by a log ∆ factor, that decreases as ∆ *→ ∞*.

In a sense, from analysis courses, we recall that given a function f, the approximation of the value of the area under its curve can be computed using sums instead of integrals, the approximation getting more and more precise the smaller the quantization.

## 4.3 Examples

1. If X ∼ *Unif*(−1/2, 1/2), it's entropy is simply 0.
2. If X ∼ Unif(−a/2*, a/*2),
$$h(X)=\int{\frac{1}{a}}\log{\frac{1}{1/a}}=\log\!|a|.$$
3. Now, suppose that X ∼ *Unif*(−1/2, 1/2) and ˜X = aX. Clearly, ˜X ∼ Unif(−a/2*, a/*2) and
as before h(X) = 0 and h( ˜X) = log|a|. Note that ˜X is one-to-one but entropies are different.
This shows that the behaviour of continuous entropy is completely different than that of the discrete one.
We conclude the lecture with two, now trivial theorems: 

**Theorem 7:** If a *is a constant,* h(a + X) = h(X).

**Theorem 8**: h(aX) = h(x) + log|a|.