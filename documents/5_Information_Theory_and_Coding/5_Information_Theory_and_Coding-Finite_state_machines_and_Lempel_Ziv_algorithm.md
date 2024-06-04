# Lecture 9: Finite State Machines And Lempel-Ziv Algorithm

In this lecture, we will start by finding a lower bound to the length of the sequence y1 *. . . y*n in terms of (i) the number of the set of states S of a machine, (ii) the sequence (u1 *. . . u*n) valid for every information lossless machine with *|S|* states and finish by introducing the Lempel-Ziv algorithm.

## 1 Lower Bound To The Length Of The Output Sequence

Recall that m∗(un) is the largest m such that u1 . . . un = v1 . . . vn, vi ∈ U* and vi ̸= vj for i ̸= j.

Let us state the following lemma: 

Lemma 1 : $$\operatorname*{lim}_{n\to\infty}{\frac{1}{n}}m^{*}(u^{n})=0$$

Proof : Let (v1 *. . . v*m∗) = (u1 *. . . u*n). Note that there is one sequence ∅ of length 0, there are U|
sequences of length 1, *|U|*2 sequences of length 2,..., and *|U|*k−1 sequences of length k − 1. Now, for any k, we have:

$$n=\sum_{i=1}^{m^{*}}length(v_{i})\geq\sum_{\begin{subarray}{c}1\leq i\leq m^{*}:\\ length(v_{i})\geq k\end{subarray}}length(v_{i})$$ $$\geq k|\{i:length(v_{i})\geq k\}|$$ $$=k(m^{*}-|\{i:length(v_{i})<k\}|)$$ $$\geq k(m^{*}-|\mathcal{U}|^{k}),$$
where the last inequality comes from the fact that

$\{i:length(v_{i})<k\}|<1+|\mathcal{U}|+\ldots+|\mathcal{U}|^{k-1}$

$$=\frac{|\mathcal{U}|^{k}-1}{|\mathcal{U}|-1}\leq|\mathcal{U}|^{k}.$$

Therefore, we have a lower bound for n which allows us to write:

$$0\leq{\frac{1}{n}}m^{*}(u^{n})\leq{\frac{1}{k}}+{\frac{|{\cal U}|^{k}}{n}},$$

which goes to 1/k as n *→ ∞*. 

The above lemma states that we cannot find a distinct parsing for which m∗ increases linearly with n (m∗ actually grows sublinearly in the size of the input).

Corollary 3 : Using the same assumptions as the previous lemma,

$$length(y_{1}\ldots y_{m})\geq m\log_{2}\frac{m}{8k}.$$

**k-distinct sequences** : Recall that we have the following scenario: we have a sequence u1 . . . un that we pass to input to an IL machine M containing s states and the machine outputs us a sequence y1 *. . . y*n. We write u1 . . . un = v1 *. . . v*n. It is a distinct parsing. Suppose z1 *. . . z*m is the set of states and let t1 *. . . t*m be the set of outputs. We now introduce the following claim:

**Claim 4** : The collection of binary sequences t1, . . . , tm is s^2-distinct.

Proof : To prove this claim, we use a contradiction. Suppose that there exists a binary sequence t among t1*, . . . , t*m that appeared more than s2 times.

Note that there are only s^2 values for
(zi, zi+1) so by the pigeonhole principle, ∃i ̸= j s.t. (zi, zi+1) = (zj, zj+1) and ti = tj. Now by definition, g(zi, vi) = zi+1 = zj+1 = g(zj, vj) and similarly f(zi, vi) = ti = tj = f(zj, vj). So, by letting z = zi = zj, we have f(*z, v*i) = f(*z, v*j) and g(*z, v*i) = g(*z, v*j) but vi ̸= vj. So the machine takes two different input sequences that lead to the same output state which contradicts the information lossless property. As we reach a contradiction, we can conclude the proof.

**Theorem 5** : For any information lossless machine with s states,

$length(y_{1}\cdot\cdot\cdot y_{n})\geq m^{*}(u^{n})\log_{2}\frac{m^{*}(u^{n})}{8s^{2}}$

**Corollary 6** :

$\rho_{IL}(u_{1}u_{2}\ldots)\geq\lim\inf\limits_{n\to\infty}\frac{1}{n}m^{*}(u^{n})\log m^{*}(u^{n})$
Proof For any s and any IL machine with at most s states,

$$\frac{1}{n}l e n g t h(y_{1}\ldots y_{n})\geq\frac{1}{n}m^{*}(u^{n})\log m^{*}(u^{n})-\frac{1}{n}m^{*}(u^{n})\log8s^{2},$$
from the previous theorem. By taking the limit on both sides, we get

$$\liminf_{n\to\infty}\frac{1}{n}length(y_{1}\ldots y_{n})\geq\liminf_{n\to\infty}\frac{1}{n}m^{*}(u^{n})\log m^{*}(u^{n}).$$
Since this quantity is independent of s, we have what we need.

## 2 Lempel-Ziv Universal Compression

In this section, our aim is to describe a procedure that accepts a sequence u1u2 . . . and produces a
binary output (from which u can be recovered) for which the previous quantity becomes an upper
bound.

## 2.1 Lempel-Ziv Algorithm

We are given a universe U.

We will be fed a sequence one letter at a time.

We start with a dictionary D = *∅ ∪ U*. Set i (the number of letters sent from the input so far) to 0. We then construct the following procedure: For example, suppose U = {*a, b, c*}. Our dictionary D is initially set to {∅*, a, b, c*}. and the binary representation of each character must be of length 2 as there are four elements in D. Hence, ∅ will be represented by 00, a by 01, b by 10 and c by 11. Suppose u1u2 . . . = *ababc . . .* We start with a so we output 01. We then add the sequences aa, ab and ac to D which will enforce us to change our binary representation to three characters. Hence ∅ will be encoded by 000, a with 001, etc... Now, we read b so we add the representation of b to the output (010) and update D so that it contains ba, bb and bc. The output now becomes 01010.

As there are now ten elements in D, we have to add one more digit to represent our elements. When continuing to read the input, we notice that ab is an element of D, so we can add its binary representation to the output and add aba, *abb* and *abc* to D. Notice that now, the number of digits used in the binary representation of each element of D is sufficient enough for the next iteration so each character will keep the same code. Reading a c adds 0011 to the output. This procedure will continue for as long as there are remaining letters in our input. 

At the decoder, we know the initial value of $\mathcal{D}$ along with the initial binary representation assigned to each element of $\mathcal{D}$. This easily allows us to reverse engineer the above procedure so that we can find the input text given a particular output. Hence, Lempel-Ziv procedure is "reversible".

