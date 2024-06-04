# Lecture 19: Rate-Distortion Theory

In this lecture, we will continue our discussion on the relation between rate and distortion. We will alongside theoretical constructions provide useful examples in order to better understand what is going on.

## 1 Relation Between Rate And Distortion

Theorem 1 : The mutual information I(U; V ) viewed as a function of the distributions pU and pV |U is concave in pU and convex in pV |U.

**Proof** Fix $p_{U}$, two different $p_{V|U}$'s and $\lambda\in[0,1]$. Write $p_{V|U}=\lambda p_{V|U}^{1}+(1-\lambda)p_{V|U}^{2}$ where $1$ and $2$ are just indices. Let $W=1$ w.p. $\lambda$ and $2$ otherwise be independent of $U$. We aim to show that $I(U;V)$ w.r.t the distribution $p_{V|U}$ is not $\lambda I(U;V)+(1-\lambda)I(U;V)$ where both mutual informations are w.r.t $p_{V|U}^{1}$ and $p_{V|U}^{2}$, respectively. Consider

$$p(u,w,v)=p(w)p(u)\cdot\begin{cases}p^{\lambda}(v|u)\text{if}W=1\text{(w.p.}\lambda)\\ p^{\lambda}(v|u)\text{if}W=2\text{(w.p.}1-\lambda).\end{cases}$$
Now, p(*u, v*) = λp(u)p1(vu) + (1 − λ)p(u)p2(v|u) = p(u)p(v|u) and

$I(U;V)\leq I(U;VW)$

$I(U;W)+I(U;V|W)$

$I(U;V|W)$,
since U and W are independent. This concludes the proof.

## 2 Examples 


## 2.2 Asymmetric Bernoulli

Let there be the exact same setup as in our last example except that U is now asymmetric, namely, Pr(U = 0) = 1 − p and Pr(U = 1) = p. Assume w.l.o.g that p ≤ 1/2. Let Z = 1{u̸=v}. We have

$$\begin{array}{r l}{I(U;V)=h_{2}(p)-H(U|V)}\\ {=h_{2}(p)-H(Z|V)}\\ {\geq h_{2}(p)-H(Z)}\\ {=h_{2}(p)-h_{2}(D).}\end{array}$$
Here, min I(U; V ) = h2(p) − h2(D). Note that there is equality above if and only if Z ⊥⊥ V and V ∼ U. For this, we need 1−p to be equal to pv(0)(1−D)+pv(1)D s.t. pv(0)+pv(1) = 1. Solving for pv(1) gives us

$$(1-p_{v}(1))(1-D)+p_{v}(1)D=(1-D)+p_{v}(1)(2D-1)\implies p_{v}(1)=\frac{p-D}{1-2D}.$$

The above is indeed a valid probability since $(p-D)/(1-2D)\geq0$ and $(p-D)\leq(1-2D)$ since $p+D\leq1$. With this, we obtain

$$p_{v}(0)=1-\frac{p-D}{1-2D}=\frac{1-D-p}{1-2D}.$$

## 2.3 Gaussian Random Variable

As a final example, let U = V = R. Let d(*u, v*) = (u − v)^2 and U ∼ N(0, σ2). We now wish to minimise the mutual information I(U; V ) subject to a density function f_{V |U} being such that E[(U − V )^2] = D. Assume again w.l.o.g that D ≤ σ2. We have

$$I(U;V)=h(U)-h(U|V)$$ $$=h(U)-h(U-V|V)$$ $$\geq h(U)-h(U-V)\text{with equality iff}(U-V)\perp\!\!\!\perp V.$$ $$\geq\frac{1}{2}\log2\pi e\sigma^{2}-\frac{1}{2}\log2\pi eD\text{with equality iff}(U-V)\sim\mathcal{N}(0,D).$$ $$=\frac{1}{2}\log\frac{\sigma^{2}}{D}.$$

Hence,
$$\operatorname*{min}_{P V\mid U:E[(U-V)^{2}]=D}I(U;V)={\frac{1}{2}}\log{\frac{\sigma^{2}}{D}}.$$

## 3 Some Good News

**Theorem 2**: _Given $p_{U}$ and $p_{V|U}$ (i.e. given $p_{U,V}$) and given $R>I(U;V)$, $\epsilon>0$ and $d:\mathcal{U}\times\mathcal{V}\rightarrow\mathbb{R}$, there exists an encoder/decoder pair such that_

$$\left|E\left[\frac{1}{n}\sum_{i}d(U_{i},V_{i})\right]-E\left[d(U,V)\right]\right|<\epsilon.$$


To give a hindsight about how the proof is going to work, we will use a random construction. Let $dec(i)=V_{i,1}\ldots V_{i,n}$ for $1\leq i\leq2^{n_{i}}$, assuming $2^{nR}$ is an integer. Assume that all $V_{i,j}$ are iid $\prec\,p_{V_{i,j}}$. We search the rows of the decoder to find one row $m$ such that $(u_{1},\ldots,u_{n},dec(m))\in T(p_{V,1},n,s)$ where $n$ and $s$ are to be defined later. We set $enc(u^{n})$ to be $m$ if one such row is found, and a random one between $1$ and $2^{nR}$ otherwise. By reason of time, the proof is to be completed in the next lecture.

