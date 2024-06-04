
## Lecture 21: Elements Of Coding Theory

In this lecture, we will attack the last part of the course which consists of studying the way to design efficient encoders and decoders such that we maximise the chance that we receive the message we sent in its entirety.

## 1 Coding For Binary Input Channels

We will here again consider the Binary Symmetric Channel $BSC(p)$. Recall that in this setting, the probability that we receive the bit we sent is $1-p$ and the probability that the bit flips is $p$. Assume w.l.o.g that $p\leq1/2$. In a sense, the output $Y$ can be viewed as $X\oplus Z$ where $Z=0$ w.p. $1-p$ and $1$ otherwise is the noise (i.e. the flip probability), independent of $X$. Note that the average number of flips is $p$. Therefore, the probability that $Z^{n}=1$ is $p\leq1$, $\ldots,\frac{p}{2^{n}}/p\neq p$ using the law of large numbers. Suppose that we measure $m=\{1,\ldots,2^{n}\}$ is the number that outputs $X^{n}/(m)$. This gives too our BSC and outputs $Y^{n}$ which is then passed as input to order that outputs an estimate $\hat{m}$ of our initial message. The error probability when each message is equally likely is

$$\frac{1}{2^{n}h}\sum_{m=1}^{2^{n}}Pr(dec(Y^{n})\neq m|m).$$

The decoding rule that minimises this probability is $\operatorname{dec}(y^{n})=\arg\max_{m}Pr(Y^{n}=y^{n}|m)=p^{q(y^{n},x^{n}(m))}(1-p)^{n-d(y^{n},x^{n}(m))}$, where $d(a^{n},b^{n})=\sum_{i}1_{\{a_{i},b_{i}\}}$ is the Hamming distance between $a$ and $b$. Maximizing $\operatorname{dec}(y^{n})$ involves finding the $x^{n}(m)$ among all possible ones for which the Hamming distance to $y$ is the smallest possible (i.e. finding the $x$ closest to $y$). We have

$$\widehat{\operatorname{dec}}(y^{n})=\arg\min_{m}d_{H}(y^{n},x^{n}(m)).$$

The above motivates the following "figure of merit" for an encoder:

$$d_{min}(enc)=\min_{m,m'\to np,m'}\operatorname{dec}(enc(m),enc(m'))\geq\operatorname{large}O(np).$$
Classical coding theory tries to design encoders with high R and high dmin (where one of them is fixed and the other is computed). Note that when m is equally likely in {1*, . . . , M*}, the probability of correctly decoding is

$$Pr(\text{correct decoding})=\sum_{y}\sum_{m}\frac{1}{M}Pr(y|x(m))\mathds{1}_{\{\text{desc}(y)=m\}}$$ $$=\sum_{y}p(y)\sum_{m}p(m|y)\mathds{1}_{\{\text{desc}(y)=m\}}$$ $$\leq\sum_{y}p(y)\frac{\max}{\max}p(m|y).$$

## 2 Sphere Packing Bound

Let us try to better understand the Hamming distance, which will be very useful in what is to follow.

## 2.1 Triangle Inequality For Hamming Distance

First of all, note that dH satisfies the triangle inequality. That is, we have d(a, b)+d(b, c) ≥ d(*a, c*).

To prove this, it suffices to show that 1{a̸=b} + 1{b̸=c} ≥ 1{a̸=c}. We have two cases: either a = c, which implies that d(*a, c*) = 0 and d(*a, b*) = −d(*b, c*) so that d(*a, b*) + d(*b, c*) = d(*a, c*) = 0, or a ̸= c in which the triangle inequality imposes that d(*a, c*) being positive, either b = a or b = c would be a contradiction to d(*a, b*) + d(*b, c*) being smaller than d(*a, c*) so the bound is proved.

Lemma 1: If enc has d_min = d, then B_m = {y^n : d(y^n, enc(m)) < d/2} are disjoint.

**Proof** : Suppose towards contradiction that $y^{n}\in B_{m}$ and $y^{n}\in B_{m^{\prime}}$. Then $d(enc(m),enc(m^{\prime}))\leq d(enc(m),enc(y^{n}))+d(enc(y^{n}),enc(m^{\prime}))$ by triangle inequality. But since both terms on the RHS are at most $d/2$, the LHS term is at most $d$ which contradicts the fact that the $B_{m}$ are disjoint. This concludes the proof.

Now, observe that

$$|\{y^{n}:d(y^{n},enc(m))=k\}|{=}\binom{n}{k}.$$

Consequently

$$|\{y^{n}:d(y^{n},enc(m))\leq r\}|{=}\sum_{i=0}^{r}{n\choose i}.$$

This leads us to the following theorem which is called the _Sphere Packing Bound_:

## 2.3 Example

We consider the (7, 4, 3)-Hamming code where 7 = n, 4 = log2 M and 3 = dmin. Note that

$$2^{7}=2^{4}2^{3}=2^{4}(1+7)=2^{4}\left(\binom{7}{0}+\binom{7}{1}\right),$$ from the sphere asking bound. The encoders for this code (there are 16 of them) are the $x$'s that satisfy

$$\mathbf{H}\mathbf{x}=\vec{0}\equiv\begin{pmatrix}1&0&0&1&1&0&1\\ 0&1&0&1&0&1&1\\ 0&0&1&0&1&1&1\end{pmatrix}\begin{pmatrix}x_{1}\\ \vdots\\ x_{7}\end{pmatrix}=\begin{pmatrix}0\\ 0\\ 0\end{pmatrix}.$$

The above matrix vector product corresponds to the following system of equations:

$$\begin{cases}x_{1}+x_{4}+x_{5}+x_{7}=0\\ x_{2}+x_{4}+x_{6}+x_{7}=0\\ x_{3}+x_{5}+x_{6}+x_{7}=0\end{cases}\Leftrightarrow\begin{cases}x_{1}=x_{4}+x_{5}+x_{7}\\ x_{2}=x_{4}+x_{6}+x_{7}\\ x_{3}=x_{5}+x_{6}+x_{7}\end{cases},$$
in which additions are performed modulo 2. The second system comes from the fact that in base
2, x = −x. By the third equation, we can choose {xi}i∈{4,5,6,7} freely and find the other xi's from there. Here, M = 24 since there are 24 possible choices for {xi}i∈{4,5,6,7}. We want to show that the distances 1 and 2 are not possible (i.e. show that the only valid dmin is 3). Suppose x and ˜x both satisfy Hx = H ˜x = 0, meaning that H(x − ˜x) = 0.

1. Suppose d(x, ˜x) = 1. Then x − ˜x = eJ where ei is the unit vector in direction i (i.e. the
vector containing a 1 in position i and 0 everywhere else) and J is uniformly random between
1 and the number of elements in x. Then, H(x − ˜x) will give us one of the columns of H
(in fact, the J'th column) which is ̸= ⃗0 so that we reach a contradiction.
2. The proof works the same way for d(x, ˜x) = 2 except that in this case, H(x − ˜x) will give
us the sum of two columns of H which also cannot be 0 since each column is distinct.

Hence, two codewords x and ˜x must have length at least 3. By the sphere packing bound, the length cannot be more than three and thus, the result is proved.