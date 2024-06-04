# Lecture 4: Optimal Coding And More About Entropy

In this lecture, we will spend a little more time on the problem of minimising the average codelength after which we will dive more deeply into the notion of entropy, its relations and its implications.

## 1 Minimising The Expected Codeword Length

## 1.1 General Idea: Two Letters With The Same Length

Suppose that by some means, we have learned that in the best code, the letters $u_{0}$ and $u_{1}$ have the same length, i.e. are such that $l(u_{0})=l(u_{1})$. Can we use this hypothesis to make our life easier? The answer is yes! In this case, the above problem becomes $\min p(u_{0})l_{0}+p(u_{1})l_{0}+\sum_{i=2}^{m}p(u_{i})l(u_{i})$ subject to $2\cdot2^{-l_{0}}+\sum_{i=2}^{m}2^{-l_{i}}\leq1\implies2^{-(l_{0}-1)}+\sum_{i=2}^{m}2^{-l_{i}}\leq1$. We can then rewrite the above as follows:

$$\min\left[p(u_{0})+p(u_{1})\right]\left((l_{0}-1)+1\right)+\sum_{i=2}^{m}p(u_{i})l(u_{i})\text{subject to}2^{-l_{0}}+\ldots+2^{-l_{m}}\leq1,$$
which is equivalent to writing

$$\min\left((p(u_{0})+p(u_{1}))(l_{0}-1)+\sum_{i=2}^{m}p(u_{i})l(u_{i})\right)+p(u_{0})+p(u_{1})\text{subject to}2^{-l_{1}}+\ldots+2^{-l_{m}}\leq1,$$
on an alphabet of now, size m.

To conclude, we see that if we can identify two letters of U that have the same length on the best code, we can reduce BCL(U, p) to *BCL*( ˜U, ˜p) where | ˜U|= *|U|−*1.

## 1.2 Properties Of Optimal Codes

1. If p(u) > p(v) then l(u) ≤ l(v). To prove this property, we use a contradiction. Suppose for
instance that l(u) > l(v). Swap them. Then, . . .+p(u)l(u)+p(v)l(u)+ . . . < . . . +p(u)l(u)+p(v)l(v) + . . . which contradicts our initial claim.
2. **There are at least two letters which have the longest length**. We prove this property
again using contradiction. Suppose that ∃u0 with l(u0) > l(u) ∀u ̸= u0. By prefixfreeness,
we can shorten it by at least one level of height (i.e. removing the last digit of the code), therefore there will have to exist a second letter with the same assigned codeword length.
To moreover formalise the above properties, we can express the following lemma: 

Lemma 1 : If u and v are letters with the two smallest probabilities, it must be that l(u) = l(v).

This lemma is the bridge to the Huffman algorithm.

## 1.3 Huffman Algorithm

Let U be the alphabet having respective probabilities determined by the distribution p. The idea of the algorithm is to group the probabilities by two starting by the two lowest ones and create a new letter with frequency corresponding to the sum of the two previous probabilities. Continue this procedure until we arrive at a probability of 1. Then, we simply assign a 0 or a 1 regarding how we travel the binary tree. The multiple codes that we can obtain when having run instances of the Huffman algorithm are all optimal.

## 2 More About Entropy

Entropy is one of the most important notions in information theory, so it is important for us to understand it a little more at this point. Recall the definition of entropy:

$$H(U)=\sum_{u\in{\mathcal{U}}}p(u)\log_{2}{\frac{1}{p(u)}},$$
where p(u) = Pr(U = u). In case of a joint distribution, we define the joint entropy as follows:

$$H(U V)=\sum_{u\in{\mathcal{U}},v\in{\mathcal{V}}}p_{U V}(u,v)\log_{2}{\frac{1}{p_{U V}(u,v)}},$$
where p_{UV}(u, v) = Pr(U = u, V = v).

When recalling from probability theory, we note that the entropy is simply the negative expected value of the log of the probability. In other words, H(U) = −E[log2 p(U)] or E[log2(1/p(U))] and similarly, H(UV ) = −E[log2 p(U,V)] or E[log2(1/p(U, V))].

## 2.1 Conditional Entropy

Before introducing the notion of conditional entropy, let us first recall the chain rule in probability otherwise known as Bayes rule. This rule states the following:

$$Pr(U_{1},\ldots,U_{n}=u_{1},\ldots,u_{n})=Pr(U_{1}=u_{1})Pr(U_{2}=u_{2}|U_{1}=u_{1})Pr(U_{3}=u_{3}|U_{1}=u_{1},U_{2}=u_{2})\ldots$$ $$\cdot\,Pr(U_{n}=u_{n}|U_{1}=u_{1},\ldots,U_{n-1}=u_{n-1})$$ $$=Pr(U_{1}=u_{1})\prod_{i=2}^{n}Pr(U_{i}=u_{i}|r_{j<i}U_{j}=u_{j}).$$

By taking the log on both sides, we have

$\log Pr(U_{1},\ldots,U_{n}=u_{1},\ldots,u_{n})=\log Pr(U_{1}=u_{1})+\sum_{i=2}^{n}\log Pr(U_{i}=u_{i}|\cap_{j<i}U_{j}=u_{j})$.

Let us now take the expected value of the log of the inverse probabilities. We have the following:

$$E\left[\log\frac{1}{p(U_{1},\ldots,U_{n})}\right]=E\left[\log\frac{1}{p(U_{1})}\right]+\sum_{i=2}^{n}E\left[\log\frac{1}{p(U_{i}|\cap_{j<i}U_{j}=u_{j})}\right].$$
Using the above, we can now define what conditional entropy is.

Definition 2 (Conditional entropy):

$$H(U|V)=\sum_{u\in\mathcal{U},v\in\mathcal{V}}p_{UV}(u,v)\log_{2}\frac{1}{p_{U|V}(u|v)}=E\left[\log\frac{1}{p_{U|V}(u|v)}\right].$$

Theorem 3:

$H(U_{1},\ldots,U_{n})=H(U_{1})+H(U_{2}|U_{1})+H(U_{3}|U_{1},U_{2})+\ldots+H(U_{n}|U_{1},\ldots,U_{n-1})$
The proof of this theorem has actually already been done. 

Theorem 4 : $$H(U|V)\leq H(U)$$

Corollary 5 : $$H(UV)\leq H(U)+H(V)$$.

The proof of this corollary is the same as the last theorem when adding H(V ) on both sides.

## 2.2 Mutual Information

Mutual information essentially measures the dependency of random variables between themselves. We define it as follows:

Definition 6 (Mutual information):

$$I(U;V)\triangleq H(U)+H(V)-H(U V)$$

Note that we can also express it as I(U; V ) = H(U) − H(U|V ) which by symmetry gives us H(V )−H(V |U) also known as I(V ; U). We can easily deduce from previous results that I(U; V ) ≥ 0. Note that for all above theorems and definitions concerning entropy, there are equalities if and only if U and V are independent.