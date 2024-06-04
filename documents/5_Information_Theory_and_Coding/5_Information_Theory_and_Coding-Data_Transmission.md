
## Lecture 11: More Data Transmission

Lecturer: E. Telatar Scribes: S. Ollquist1
In this lecture, we will provide more detail as to how we can construct efficient source channel encoders and decoders so that we maximise the chance of correctly receiving the input we originally tried to send. We will cite an important theorem and introduce some tools that we need in order to prove it.

## 2 Source Channel Encoding And Decoding 

## 2.1 A Complete Data Communication Diagram

Often in data transmission problems, a certain channel will not be able to correctly understand the input we give it. We need to encode our data. For the purpose, our job is to construct what we call a source channel encoder or *transmitter* that accepts a source and outputs something that the communication channel will be able to read or understand. Similarly, we shall construct a source channel decoder or *receiver* for the output. The fundamental problem is as follows:

The information source is a sequence U1, U2*, . . .* of random variables that are transformed by the encoder into a sequence X1, X2*, . . .* passed as input to the communication channel. The noisy channel then outputs a sequence Y1, Y2*, . . .* which has to go through a decoder that will output V1, V2*, . . .*. The main goal of an efficient communication system is that we ideally want the Vi's to be identical to the Ui's. This is of course pretty much impossible. So it is better to look at the problem in terms of probability. In a sense, we can make errors but not too many of them.

## 2.2 Problem Formalisation

Suppose V^k are produced after observing V^{n(k)}. Let lim_{k→∞} k/n(k) = ρ be the number of transmitted source symbols per channel use. Ideally, we would like the error rate ϵ to be smalle, and ρ to be large. Let us introduce some bad news (actually in form of a theorem).

Theorem 1: Given the entropy rate H of U1, U2, . . ., given Pr(y|x) that describes the channel and given ϵ, we have

$$\rho\leq\frac{C(P)}{\mathcal{H}-(h_{2}(\epsilon)+\epsilon\log_{2}(|\mathcal{U}-1))},$$

_where $C(P)$ is defined as $\max_{p_{X}}I(X;Y)$._
This rather complicated expression will make more sense once we introduce and understand some important tools that we shall use to prove it.

## 2.3 Fano'S Inequality

The first tool we need to introduce is Fano's inequality.

Lemma 2 : If U and V are random variables defined on the same alphabet U, then

$$H(U|V)\leq h_{2}(p)+p\log_{2}(|{\mathcal{U}}|-1),$$
where p = Pr(U ̸= V ) *and* h2(p) = p log 1/p + (1 − p) log 1/(1 − p) is the binary entropy function.

Proof : First note that if H(U|V ) is large, p cannot be too small and conversely, if H(U|V ) is small, then p also must be. Now, let W = 1{U̸=V } so that H(W) = h2(p). Then

$$H(U|V)=H(UW|V)=H(W|V)-H(U|V,W)\leq H(W)+H(U|V,W).$$

Notice that we can write $H(U|V,W)$ as

$$H(U|V,W)=\sum_{w\in\{0,1\}}\sum_{v\in\mathcal{U}}p_{WV}(w,v)H(U|WV=wv),$$
where

$H(U|WV=wv)\begin{cases}=0&\text{if}w=0\\ \leq\log_2(|\mathcal{U}|-1)&\text{otherwise.}\end{cases}$
Then, we have H(U|V ) ≤ Pr(W = 1) log2(*|U|−*1) = p log2(*|U|−*1) which concludes the proof.

## 2.4 Corollary To Fano'S Inequality

To have a more complete bound in the case of k random variables, let us introduce the following:

**Corollary 3**: _Let $U_{1},\ldots,U_{k},V_{1},\ldots,V_{k}$ be all defined on the same alphabet $\mathcal{U}$. Let $p_{i}=Pr(U_{i}\neq V_{i})$. Then_

$$\frac{1}{k}H(U^{k}|V^{k})\leq h_{2}(p)+p\log_{2}(|\mathcal{U}|-1),$$

## 2.5 Important Bound On Mutual Information

$I(X^{n};Y^{n})=H(Y^{n})-H(Y^{n}|X^{n})$

$\leq\sum(H(Y_{i})-H(Y_{i}|X_{i}))$
$=\sum I(X_{i};Y_{i})$
$\leq n\cdot C(P)$,

by definition of C(P) (see theorem 1).

## 2.6 Proof Of Theorem 1

We now have the tools to prove the main theorem. Suppose U k is passed as input to the encoder which outputs the sequence X∞ (by convention we write ∞ here as we are not sure of the sequence length the encoder can give us). X∞ is the input to the communication channel which outputs Y n(k). We then pass this as input to our decoder in order to obtain V k which we wish to be relatively close to U k. Notice that U k—Xn(k)—Y n(k)—V k form a Markov chain (so the right and left most variables are completely independent conditioned on the middle ones). By the data processing inequality I(U k; V k) ≤ I(Xn(k)Y n(k)) ≤ n(k)C(P) by the previous computation. So

$$\frac{1}{k}H(U^{k})-\frac{1}{k}H(U^{k}|V^{k})\leq\frac{n(k)}{k}C(P)$$
$$\Rightarrow\mathcal{H}-\frac{1}{k}H(U^{k}|V^{k})\leq\frac{n(k)}{k}C(P)$$
Notice that 1
kH(U k|V k) ≤ h2(p) + p log(*|U|−*1) ≤ h2(ϵ) + ϵ log(*|U|−*1) by Fano's inequality. Hence

$$\frac{k}{n(k)}\leq\frac{C(P)}{{\mathcal{H}}-(h_{2}(\epsilon)+\epsilon\log(|{\mathcal{U}}|-1))},$$
which proves the theorem.