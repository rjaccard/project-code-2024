# Lecture 14: Channel Coding Theorem

In this lecture, we will finally introduce some good news, namely the channel coding theorem which essentially states that for every channel, there exists a constant capacity C such that for all rates that are smaller than C, we can reliably (with few errors) send information across this channel at that rate.

## 1 An Application Of The Maximal Mutual Information

Consider the Z-channel: Suppose pX(0) and pX(1) are I(X; Y )-maximising pX′. We have:

$$\mu=1\log\frac{1}{p_{Y}(0)}=p\log\frac{p}{p_{Y}(0)}+(1-p)\log\frac{1-p}{p_{Y}(1)}=-h_{2}(p)+p\log\frac{1}{p_{Y}(0)}+(1-p)\log\frac{1}{p_{Y}(1)}$$ $$\Rightarrow(1-p)\log\frac{1}{p_{Y}(0)}=-h_{2}(p)+(1-p)\log\frac{1}{p_{Y}(1)}$$ $$\Rightarrow(1-p)\log\frac{p_{Y}(1)}{p_{Y}(0)}=-h_{2}(p)$$ $$\Rightarrow\log\frac{p_{Y}(1)}{p_{Y}(0)}=\frac{-h_{2}(p)}{1-p}\Rightarrow\frac{p_{Y}(1)}{p_{Y}(0)}=2^{-h_{2}(p)/(1-p)}.$$
So for those two quantities to be equal (since they must sum up to one), we let

$$p_{Y}(0)={\frac{2^{-h_{2}(p)/(1-p)}}{1+2^{-h_{2}(p)/(1-p)}}}{\mathrm{~and~}}{\frac{1}{1+2^{-h_{2}(p)/(1-p)}}}.$$
Hence, we get µ = log(1 + 2−h2(p)/(1−p)) in this particular example.

## 2 Channel Coding Theorem 2.1 Recall The "Bad News" Theorem

So far, we have seen scenarios where in a communication system, we send values U1, U2*, . . .* across a channel and recover values V1, V2*, . . .* on the other end. We wish to have each Ui = Vi with high probability. More specifically, we want

$$\frac{1}{k}\sum_{i=1}^{k}Pr(U_{i}\neq V_{i})<\epsilon.$$

Note that the above sum can be seen if one of expectations of indicators of random variables, namely the indicators that $U_{i}\neq V_{i}$ for every $i$. It corresponds to the expected fraction of incorrectly delivered $U$'s across the channel, also called the _symbol error rate_. We can construct a more restrictive requirement which concerns all values at once, namely $Pr((U_{1}\dots U_{k})=(V_{1}\dots V_{k}))>1-\epsilon$. By a union bound, we get our initial requirement. Namely,

$$Pr((U_{1}\dots U_{k})=(V_{1}\dots V_{k}))>1-\epsilon\equiv(Pr(U_{1}\dots U_{k}\neq V_{1}\dots V_{k})<\epsilon)\leq\sum Pr(U_{i}\neq V_{i})\leq ke.$$

We now introduce the "good news" by basing ourselves on the more restrictive requirement.

## 2.2 Shannon'S Channel Coding Theorem

Theorem 1 Given p_{Y |X}, ϵ > 0, and a value *R < C* maxpX I(X; Y ), we can design a communication system that takes as input an integer m ∈ {1, . . . , ⌈2nR⌉} and outputs a value ˆm ∈ {1, . . . , ⌈2nR⌉} *such that* Pr( ˆM ̸= m|M = m) < ϵ for all m.

This theorem changed everything. The basic idea is that we can (for large n) reliably send information at any rate under a certain capacity. Let us provide an example:

**Application to the binary erasure channel** Suppose we have two possible messages: namely, if $m=1$, we send $000\dots$ and if $m=2$ we send $111\dots$ Each sent sequence is of length $n$. The probability of error will be

$${\bf Prob}(err)=\frac{1}{2}p^{n},$$
because a bit is "lost" w.p. p and there is no way to guess which ones were sent if we don't at least know one. The 1/2 factor comes from the fact that we guess by flipping a coin the original bit sent. If we augment n, the error probability decreases. In the generalised theorem, n will tend to 1/R. Note that the number of bits is roughly kH = nR. We now give an intuition on how to prove the theorem, proof that we shall complete in the next lecture.

## 2.3 Some Intuition On How To Prove The Good News Theorem

Given p_{Y |X}, *ϵ >* 0 and *R < C*, pick a distribution pX such that it maximises the mutual information, i.e. pX is s.t. I(X; Y ) = C. Pick an n large enough. We design an encoder in the following way:

$\begin{array}{l}\mbox{\rm{\it enc}}(1)=X_{1,1},\cdot\cdot\cdot\cdot\,,X_{1,n}\\ \mbox{\rm{\it enc}}(2)=X_{2,1},\cdot\cdot\cdot\cdot\,,X_{2,n}\\ \mbox{\rm{\it enc}}(L)=X_{L,1},\cdot\cdot\cdot\cdot\,,X_{L,n}\\ \end{array}$
Here, L = 2⌈2nR⌉ and {Xmj : 1 ≤ m ≤ L, 1 ≤ j ≤ *n, i.i.d.* ∼ pX}. The average error given a random input is given by the following expression:

$${\frac{1}{L}}\sum_{m=1}^{L}P r{\big(}D e c{\big(}Y^{n}{\big)}\neq m{\big|}X^{n}=e n c{\big(}m{\big)}{\big)}.$$
Note that the above is a random variable. We will compute its expectation over the choice of the Xi's. In fact, we will see that this quantity is quite small for large enough n, namely that

$$E\left[{\frac{1}{L}}\sum_{m=1}^{L}P r(D e c(Y^{n})\neq m|X^{n}=e n c(m))\right]<\epsilon/2,$$
which essentially means that there exists some encoder and decoder such that

$$\frac{1}{L}\sum_{m=1}^{L}P r(D e c(Y^{n})\neq m|X^{n}=e n c(m))<\epsilon/2,$$
also meaning that for at least L/2 of the m's,

$$P r(d e c(Y^{n})\neq m|X^{n}=e n c(m))<\epsilon.$$
Although, before we do this computation, we need to design a decoder. For this, we search the above table for a row l such that (Xn(l), Y n) ∈ T(n, pXY *, δ*) where δ is to be chosen. If we find exactly one such l, output it (so let *dec*(Y n) = *enc*(l)). Otherwise, we choose another random row. Note that E[Pr(dec(Y n) ̸= m|Xn = *enc*(m))] and E[Pr(dec(Y n) ̸= 1|Xn = *enc*(1))] are equivalent. From there, we can make the summation over all rows disappear which implies that the event *dec*(Y n) ̸= 1
happens if, exactly one of the conditions (X(1), Y n) ̸∈ T, (X(2), Y n) ∈ T, . . . , (X(L), Y n) ∈ T is verified. All but the first condition are what we call the *error event*.