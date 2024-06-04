# Lecture 20: Proof Of The "Good News" For Rate-Distortion

In this lecture we will, as promised, provide a complete proof of the "good news" for rate-distortion.

## 1 "Good News" Theorem

Let us first recall the theorem:

**Theorem 1**: _Given $p_{U}$ and $p_{V|U}$ (i.e. given $p_{U,V}$) and given $R>I(U;V)$, $\epsilon>0$ and $d:\mathcal{U}\times\mathcal{V}\rightarrow\mathbb{R}$, there exists an encoder/decoder pair such that_

$$\left|E\left[\frac{1}{n}\sum_{i}d(U_{i},V_{i})\right]-E\left[d(U,V)\right]\right|<\epsilon.$$

To prove it, we proceed as follows: pick $n$ large and $\delta>0$. Generate $2^{nR}\ V^{n}$'s and let $dec(i)=V_{i,1}\ldots V_{i,n}$ for $1\leq i\leq2^{nR}$, assuming $2^{nR}$ is an integer where each $V_{i,j}$ is iid $\sim p_{V}$. We construct an encoder as follows: find an $m$ such that $(U^{n},dec(m))\in\mathcal{T}(n,p_{V},\delta)$. If there exists such an $m$, let $enc(u^{n})=dec(m)$. Otherwise, select a random $1\leq i\leq2^{nR}$ and let $enc(u^{n})=dec(i)$.

## 2 Analysis 

## 2.1 Success Scenario

If the above procedure succeeds, we know that (U^n, V^n) ∈ T(n, p_UV, δ). Then

$$\frac{1}{n}\sum_{i=1}^{n}d(U_{i},V_{i})=\frac{1}{n}\sum_{i=1}^{n}\sum_{u,v}\mathds{1}_{\{(U_{i},V_{i})=(u,v)\}}d(U_{i},V_{i})$$ $$=\frac{1}{n}\sum_{i=1}^{n}\sum_{u,v}\mathds{1}_{\{(U_{i},V_{i})=(u,v)\}}d(u,v)$$ $$=\sum_{u,v}d(u,v)\frac{1}{n}\sum_{i=1}^{n}\mathds{1}_{\{(U_{i},V_{i})=(u,v)\}}.$$


$$\frac{1}{n}\sum_{i=1}^{n}d(U_{i},V_{i})-E[d(U,V)]=\sum_{u,v}d(u,v)\left(\frac{1}{n}\sum_{i=1}^{n}\mathds{1}_{\{(U_{i},V_{i})=(u,v)\}}-p(u,v)\right)$$ $$=\sum_{u,v}d(u,v)\left(p(u,v)(1\pm\delta)-p(u,v)\right)\text{by}\epsilon\text{-typically}.$$ 

Taking the absolute value of the difference on both sides allows us to bound the expected distortion as follows:

$$\left|\frac{1}{n}\sum_{i=1}^{n}d(U_{i},V_{i})-E[d(U,V)]\right|\leq\sum_{u,v}d(u,v)\left|p(u,v)(1\pm\delta)-p(u,v)\right|$$ $$\leq\delta\sum_{u,v}p(u,v)|d(u,v)|$$ $$\leq\delta A\text{letting}A=\max_{u,v}|d(u,v)|,$$
which can be made arbitrarily small by choosing a small value for δ.

## 2.2 Failure Scenario

Now, let us study the case in which the above procedure does not succeed. The only bound we can give in this scenario is a bad one. Namely, we have

$$\left|\frac{1}{n}\sum_{i=1}^{n}d(U_{i},V_{i})-Ed(U,V)\right|\leq2A,$$

since each term in the difference will have possible values ranging between $-A$ and $+A$. We wish to understand the probability of the algorithm falling. We distinguish two different cases:
1. The first one is that the sequence of U n is not typical, i.e. U^n ̸∈ T(n, p_U, δ/3). This has
small probability so we are fixed.
2. The second and more interesting case is when the sequence of U^n is typical, but for each
i ∈ [2^{nR}], (U^n, dec(i)) ̸∈ T(n, p_UV, δ). For given U^n ∈ T(n, p_U, δ/3) and for all i,
$$Pr((U^{n},dec(i))\not\in T(n,p_{UV},\delta))=\prod_{i=1}^{2^{nR}}Pr((U^{n},dec(i))\not\in T)$$ $$=(1-Pr((U^{n},dec(i))\in T))^{2^{nR}}\text{by independence}$$ $$\leq e^{-2^{-n(l(U\cap V)(1+\delta))}2^{nR}}\text{since}1-x\leq e^{-x}$$ $$=e^{-2n(R-l(U;V)(1+\delta))}$$ $$=\alpha_{n},$$

that tends to 0 as n *→ ∞* by choosing *δ >* 0 s.t. R − I(U; V )(1 + δ) → 0 as n *→ ∞*.

Consequently:

$$E_{dec}\left[\left[E\left[\frac{1}{n}\sum_{i=1}^{n}d(U_{i},V_{i})\right]-E\left[d(U,V)\right]\right]\right]\leq\delta A+2A(\alpha_{n}+Pr(U^{n}\not\in T(n,p_{U},\delta/3)))<\epsilon,$$

by choosing $n$ large enough and $\delta>0$ small enough and hence, there exists an encoder/decoder pair with the desired property, i.e. where the average distribution is close to $E[d(U,V)]$. This concludes the analysis and thus, the proof.

