
## Lecture 2: Codes And Information Sources

In this lecture, we will dive more deeply into more theorems and claims regarding prefix-free and uniquely decodable codes as well as introducing the notion of information sources and entropy.

## 1 More On Prefix-Free Codes

**Theorem 1 :** Suppose l : U → {0, 1, . . .} *satisfies Kraft's inequality.

Then, there exists a prefix-free code c : U → {0, 1}∗ such that for all u, *length*(c(u)) = l(u).

**Proof** : Let *|U|*= m and order the alphabet letters U = {u1*, . . . , u*m} such that l(u1) ≤ l(u2) ≤
. . . ≤ l(um). Consider now the following procedure to construct c:

- Step 0: consider an infinite labeled binary tree that we construct the same way we did in the
last lecture (i.e. add a 0 if we go left and add a 1 if we go right) and mark every node as available.
- Step 1: for i = 1*, . . . , m*, pick an available node at height l(ui), set c(ui) as the label of this
node and mark it along with all its decendents as unavailable.
- Step 2: done.

The question is: **how can we certify that this procedure will terminate** ? First of all, we clearly see that if we reach step 2, the constructed code is prefix-free and *length*(c(u)) ≤ l(u) ∀u.

We are left to prove that there is indeed an available node at each iteration.

At iteration i, the number of available nodes at height h = l(ui) is

$$2^{h}-\sum_{j=1}^{i-1}2^{h-l(u_{j})}=2^{h}\left(1-\sum_{j=1}^{i-1}2^{-l(u_{j})}\right).$$

By Kraft, the above simplified sum is strictly less than $1$. This implies that the term in the parenthesis is strictly positive and hence, the overall quantity is more than $1$ which concludes the proof.

## 2 Kraft'S Sum For Injective Codes

We will now study codes that are relatively longer than prefix-free codes.

For instance, consider the infinite binary combinations {0, 1}∗ = ∅, 0, 1, 00, 01, 10, 11, 000*, . . .* to which we associate its list of corresponding lengths 0, 1, 1, 2, 2, 2, 2, 4*, . . .* and the associated frequencies 2−l =
1, 1/2, 1/2, 1/4, 1/4, 1/4, 1/4, 1/8*, . . .* It is here very easy to select elements that give us a Kraft Sum greater than one.

**Theorem 2** : c : U → {0, 1}^∗ *injective* =⇒ KS(c) ≤ log_2(1 + |U|).

**Proof** : Suppose *|U|*= m. Write m as 1 + 2 + 4 + *. . .* + 2^{k−1} + r where 0 ≤ r ≤ 2k is called the remainder and k is the closest power of two greater than m. Then: KS(c) ≤ k + r2^{−k}. We thus want to show that if m = 2^k − 1 + r with 0 ≤ r ≤ 2^k, then k + r2^{−k} ≤ log_2(1 + m). By taking the log on both sides and rearranging the terms we get:

$1+m=2^{k}+r\implies\log_{2}(1+m)=\log_{2}(2^{k}+r)=k+\log_{2}(1+r2^{-k})$.

We are now left with showing that r2^{−k} ≤ log2(1 + r2^{−k}). For the purpose, let x = r2^{−k}. Clearly,
0 ≤ x ≤ 1. Also (as seen in the picture below), recall that log(x) is strictly increasing and greater than x in [0, 1].

Therefore, KS(c) ≤ log2(1 + *|U|*) and this concludes the proof.

**Theorem 3**: If c : U → {0, 1}^∗ is uniquely decodable, then KS(c) ≤ 1.

**Proof**: Recall that c u.d. ≡ c∗ injective. This implies that for all n, cn : Un → {0, 1}^∗ is injective.

Additionally, writing KS(cn) ≤ log2(1 + |Un|) is equivalent to writing (KS(c))n ≤ log2(1 + *|U|*n).

The term on the left is exponential if the Kraft Sum is greater than 1. The one on the right is in fact linear as the logarithm cancels out the exponential growth. Hence, the term on the left cannot grow exponentially and consequently, KS(c) is upper bounded by 1 which concludes the proof.

**Corollary 4**:  c : U → {0, 1}∗ u.d. =⇒ ∃ a prefix-free code ˜c : U → {0, 1}∗ where *length*(˜c(u)) =
length(c(u)) ∀u ∈ U.

What is important to remember with all of this is that the class of prefix-free codes is as efficient as the one of uniquely decodable ones.

## 3 Information Sources

Suppose we have an information source that produces letters u1, u2*, . . .* from an alphabet U following some probabilistic model (i.e. Ui is a random variable). Suppode we have a code c : *U → {*0, 1}∗.

Trivially, c(U1) is a random binary sequence and l(c(U1)) a random integer. We are interested in knowing what the expected length of one of these codes is.

## 3.1 Entropy

To have an idea of what this expected value is, we must first introduce the very important concept of entropy. This nonnegative quantity essential to information theory deals with the statistics of the information sources we have. More formally, it represents the level of randomness in the characters that figure in a particular string. An entropy of 0 means that all characters either have probability of 0 or 1 of appearing and a very high entropy means that all characters are equally likely to appear.

Let $U$ be a random variable. Let also $p(u)$ be the probability that $U$ takes the value $u$. We define the entropy as follows:

$$H(U)=\sum_{u\in U}p(u)\log_{2}\frac{1}{p(u)}.$$
For example, suppose that U = {*a, b, c, d*} and that the associated probability distribution for each character is {1/2, 1/4, 1/4, 1/8}. The entropy is then:

$$H(U)=\frac{1}{2}\log_{2}(2)+\frac{1}{4}\log_{2}(4)+2\frac{1}{8}\log_{2}(8)=\frac{1}{2}+\frac{1}{2}+\frac{3}{4}=7/4.$$

## 3.2 Expected Length Of A Code

Now that we have the definition of entropy, we can start to think about the expected length of a code given a probability distribution. We introduce the following claim:

## Claim 5

$$E[length(c(U))]\geq H(U)-\log_{2}(KS(c))$$

**Proof** Let $q(u)\triangleq2^{-length(c(u))}$. Rearranging the terms give us that $length(c(u))=\log_{2}\frac{1}{q(u)}$
q(u).

Using log rules and some more rewriting, we have

$$\sum_{u\in\mathcal{U}}p(u)\log_{2}\frac{1}{q(u)}\geq\sum_{u\in\mathcal{U}}p(u)\log_{2}\frac{1}{p(u)}-\log_{2}\sum_{u\in\mathcal{U}}q(u),$$ $$\Rightarrow\sum_{u\in\mathcal{U}}p(u)\log_{2}\frac{q(u)}{p(u)}\leq\log_{2}\sum_{u\in\mathcal{U}}q(u),$$

where the last inequality is also equivalent (to a constant factor) when removing the base of the log. To prove the last inequality, consider a simpler claim: suppose X is a positive r.v., then E[log(X)] ≤ log(E[X]) (from Jensen's inequality). To prove this claim, let f(z) = ln z −(z −1). If z > 0, then ln z ≤ z − 1. We see that this inequality is maximised when z = 1. Using this simpler claim, we can prove the main one.

Let µX = E[X]. Then ln(X/µX) ≤ *X/µ*X − 1 by the simler claim. Hence, the expected value is negative or zero. That is:

$$E[\ln X-\ln\mu_{X}]\leq0\implies E[\ln X]\leq\ln\mu_{X}=\ln E[X].$$

To complete the proof, define $X(u)=q(u)/p(u)$. Now: $\sum_{n}p(u)\log\frac{q(u)}{p(u)}=E[\log X]$ and $\sum_{n}q(u)=E[X]$. So by the claim,

$$\sum_{u\in\mathcal{U}}p(u)\log\frac{q(u)}{p(u)}\leq\log\sum_{u\in\mathcal{U}}q(u),$$
which concludes the proof.