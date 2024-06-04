# Lecture 5: Mutual Information And Its Implications

In today's lecture, we will discuss more about mutual information and study its different implications. We will understand the theory behind it and provide illustrative examples.

## 1 Why Mutual Information ?

We have introduced in the previous lecture the notion of mutual information, a quantity that essentially tells us the level of dependency random variables have between each other. Let us elaborate a little more on the subject.

## 1.1 Back On Source Coding

The general scheme of source coding is as follows: Given an alphabet $\mathcal{U}$, generate a code of approximatively $H(U)$ bits per letter. If the code goes through a source decoder, we can easily reconstruct $\mathcal{U}$. Let us name this trivial scenario $\lambda$. In a second scenario $\mathfrak{g}$, we suppose that we know a random variable $V$ that can take values in a set. We can design $|V|$ source codes for $\mathcal{U}$, one for each value of $v\in\mathcal{V}$. The probabilities for the values of $U$ we are interested in are computed with respect to the values of $v$, for instance, if we sum over all possible values of $v\in\mathcal{V}$, we get

$$H(|U|V=v)=\sum_{v\in\mathcal{V}}p_{V}(v)H(U|V=v)$$ $$=\sum_{u\in\mathcal{U},v\in\mathcal{V}}\frac{p_{V}(v)p_{U|V}(u|v)}{=_{p(u,v)}}\log\frac{1}{p(u|v)}$$ $$=H(U|V)\text{bits per letter.}$$

The improvement from scenario a to scenario b is what we call mutual information, i.e. I(U; V )
represents the values of U obtained given the knowledge of V.

## 1.2 Conditional Mutual Information

Definition 1 : Conditional mutual information: let U, V and W be three random variables. Then

I(U; V |W) = H(U|W) + H(V |W) − H(UV |W) = H(UW) + H(V W) − H(UV W) − H(W).

How can we better understand what conditional mutual information is ? Let us for the purpose elaborate the two preceding scenarios into two new scenarios a' and b' which will both now consider three random variables U, V and W. Scenario a' will use the knowledge of W whereas scenario b' will use the knowledge of both W and V . Each scenario will use a different number of bits per letter. It is the difference between these two numbers that will be called the conditional mutual information.

Detailing the above definition gives us

$$I(U;V|W)=E\left[\log{\frac{p(U|V W)}{p(U|W)}}\right]=E\left[\log{\frac{p(U V|W)}{p(U|W)p(V|W)}}\right]=E\left[\log{\frac{p(U V W)p(W)}{p(U W)p(V W)}}\right].$$

The second equality above will constitute the base of the proof for the following theorem: 

Theorem 2 : $$I(U;V|W)\geq0.$$

Proof : If we expand the definition of conditional mutual information following the definition of expectation, we obtain

$$I(U;V|W)=E\left[\log\frac{p(UV|W)}{p(U|W)p(V|W)}\right]$$ $$=\sum_{u,v,w}p(uvw)\log\frac{p(uv|w)}{p(u|w)p(v|w)}$$ $$=\sum_{w}p(w)\sum_{u,v}p(uv|w)\log\frac{p(uv|w)}{p(u|w)p(v|w)}.$$

Now, let q(uv|w) = p(u|w)p(v|w). The inner sum is actually D(p(uv|w)||q(uv|w)) which is as we know, always positive. Therefore, the sum of positive elements must be positive and hence we get that I(U; V |W) ≥ 0 which concludes the proof.

Note that there is equality if and only if either the main probability is 0 or the denominator of the log's argument is 1, i.e. the value of the logarithm is 0. This means that we must have that p(uv|w) = p(u|w)p(v|w). In other words, U and V must be independent conditionned on W, i.e.
they must form a Markov chain of the form U—W—V . More formally,

$I(U;V|W)=0 \Leftrightarrow \forall u,v,w,$ we have $p(uv|w)=q(uv|w)=p(u|w)p(v|w)$
$\Leftrightarrow U$ and $V$ are independent conditioned on $W$.

## 1.3 Chain Rule For Mutual Information

Recall the definition of the chain rule for entropy. By letting U^n = U_1 . . . U_n , we have

$$H(U^{n})=H(U_{1})+\sum_{i=2}^{n}H(U_{i}|U^{i-1}).$$

We also have

$$H(U^{n}|V)=H(U_{1}|V)+\sum_{i=2}^{n}H(U_{i}|VU^{i-1}),$$

in the case of joint probabilities. To prove the above definition, write $H(VU^{n})$ as $H(V)+H(U^{n}|V)$ and as $H(V)+H(U|V)+H(U_{2}|VU_{1})+\ldots+H(U_{n}|VU^{n-1})$. When equating both expressions, we see that $H(U^{n}|V)$ and the long sum must be equal which concludes the proof.

Definition 3 (Chain rule for mutual information):

$$I(U;V^{n})=I(U;V_{1})+I(U;V_{2}|V_{1})+I(U;V_{3}|V_{1}V_{2})+\ldots+I(U;V_{n}|V^{n-1}),$$

_and_

$$I(U;V^{n}|W)=I(U;V_{1}|W)+I(U;V_{2}|WV_{1})+\ldots+I(U;V_{n}|WV^{n-1}).$$

**Proof** To prove the above definitions, we can simply express $I(U;V_{i}|V_{i-1})$ as $H(V_{i}|V^{i-1})=H(V_{i}|U^{i-1})$ and use the chain rule for entropies to arrive at the desired result.

## 2 Bounds For Entropy And Mutual Information 2.1 A Lower Bound For Entropy

Theorem 4 : $$p\leq H(U|V)\leq H(U)$$
H(U) is zero if all probabilities are either 0 or 1. This means that U is deterministic, i.e. ∃u_0
such that Pr(U = u_0) = 1. Similarly, H(U|V ) is zero if and only if forall v where p(v) is strictly positive, ∃u(v) such that Pr(U = u(v)|V = v) = 1.

## 2.2 An Upper Bound For Entropy

Theorem 5 : $$H(U)\leq\log_{2}|{\mathcal{U}}|$$

Proof : Let q(u) = 1/|U, i.e. q assigns equal probability to all letters meaning each letter has a uniform distribution. Consider the difference between those two quantities:

$\log|\mathcal{U}|-H(U)=\log|\mathcal{U}|-E[\log(1/p(U))]$

$$=E\left[\log|\mathcal{U}|-\log\frac{1}{p(U)}\right]$$ $$=E\left[\log\frac{p(U)}{q(U)}\right]=D(p||q)\geq0.$$
This concludes the proof.

## 2.3 Bounds On Mutual Information

As we have stated before, I(U; V ) and I(U; V |W) are both non-negative quantities.

We now express upper bounds on mutual information as the following theorem: 

Theorem 6 :

$$I(U;V)\leq H(U),\,I(U;V)\leq H(V),$$

_and_

$$I(U;V|W)\leq H(U|W),\,I(U;V|W)\leq H(V|W).$$

Important note: conditioning reduces the entropy values, but does not necessarily affect mutual information. Conversely, **adding more random variables increases the entropy**.

## 3 Binary Entropy Function

In this last section, we rapidly introduce the notion of binary entropy function, which is quite commonly encountered in the world of information theory.

For a p ∈ [0, 1], let h2(p) be the entropy of a Bernoulli random variable that equals 0 w.p. 1 − p and 1 with probability p. h2(p) is called the Binary entropy function. We define it as follows:

$$h_{2}(p)=p\log{\frac{1}{p}}+(1-p)\log{\frac{1}{1-p}}.$$
