# Lecture 15: Channel Coding Theorem And Channels With Costs

In this lecture we will conclude the proof of the channel coding theorem and introduce a related concept which involves adding cost contraints to a communication system.

## 1 Proof Of The Channel Coding Theorem

Recall that we are given p_{Y |X}, *ϵ >* 0 and *R < C*. We pick a distribution p_X such that it maximises the mutual information, i.e. p_X is s.t. I(X; Y ) = C. We also pick an n large enough, that will be defined later in the proof. We design an encoder in the following way:

$\begin{array}{l}\mbox{\rm{\it enc}}(1)=X_{1,1},\cdot\cdot\cdot\cdot\,,X_{1,n}\\ \mbox{\rm{\it enc}}(2)=X_{2,1},\cdot\cdot\cdot\cdot\,,X_{2,n}\\ \mbox{\rm{\it enc}}(L)=X_{L,1},\cdot\cdot\cdot\cdot\,,X_{L,n}\\ \end{array}$

Here, L = 2⌈2^{nR}⌉ and {X_{mj} : 1 ≤ m ≤ L, 1 ≤ j ≤ *n, i.i.d.* ∼ p_X}. We design a decoder such that if there exists a unique l s.t. (enc(l), Y^n) ∈ T(n, p_{XY} *, δ*) where δ is to be chosen later, set dec(Y^n) = l. Otherwise, let *dec*(Y^n) be defined by a uniformly random guess in {1, . . . , L}. Recall that we defined the average error given a random input as

$${\frac{1}{L}}\sum_{m=1}^{L}P r{\bigl(}D e c{\bigl(}Y^{n}{\bigr)}\neq m{\bigr|}X^{n}=e n c{\bigl(}m{\bigr)}{\bigr)}.$$

Since the above is a random variable, we compute its expectation over the choice of the Xi's. We have:

$$E\left[\frac{1}{L}\sum_{m=1}^{L}P r(D e c(Y^{n})\neq m|X^{n}=e n c(m))\right]=E\left[\mathbbm{1}_{\{d e c(Y^{n})\neq1\}}|m=1\text{is sent}\right],$$
over the choice of both the Xi's and the Yi's. Note that

$\mathbbm{1}\left\{\mathit{dec}(Y^{n})\neq1\right\}\leq\mathbbm{1}\left\{(\mathit{enc}(1),Y^{n})\notin T\right\}+\sum_{2\leq j\leq L}\mathbbm{1}\left\{(\mathit{enc}(j),Y^{n})\in T\right\}$.

From there,

$E\left[\mathds{1}_{\{\,dec(Y^{n})\neq1|m=1\text{is sent}\}}\right]\leq E\left[\mathds{1}_{\{(enc(1),Y^{n})\not\in T\}}|m=1\text{is sent}\right]$

$$+\sum_{j=2}^{L}E\left[\mathds{1}_{\{(enc(j),Y^{n})\in T\}}|m=1\text{is sent}\right]$$ $$=Pr((enc(1),Y^{n})\not\in T|m=1\text{is sent})$$ $$+\sum_{j=2}^{L}Pr((enc(j),Y^{n})\in T|m=1\text{is sent}).$$

Note that (enc(1), Y^n) are iid ∼ p_{XY} since the output will depend on both p_X and p_{Y |X}. However for *j >* 1, (enc(j), Y^n) will be iid ∼ p_Xp_Y since X and Y are this time completely independent
(as the Yi's are generated with the first encoder). From the above, we see that Pr((enc(1), Y^n) ̸∈
T) → 0 when n *→ ∞* and from the properties of typical sets, Pr((enc(j), Y^n) ∈ T) ≤ 2−n[D(p_{XY} ||p_Xp_Y )(1−δ)−o(δ)], for *j >* 1. Hence

$E\left[\mathds{1}_{\{\,d\in\langle Y^{n}\rangle\neq1|m=1\text{is sent}\}}\right]\leq Pr\big{(}(enc(1),Y^{n})\not\in T\big{)}+(L-1)2^{-n\left[(1-\delta)I(X;Y)-\phi(\delta)\right]}$, that $L-1\leq(2\cdot2^{nR})+1$. Then, since $R<I(X;Y)$, we can choose a $\delta>0$ such that $L-1\leq(2\cdot2^{nR})+1$.

Notice that L − 1 ≤ (2 · 2^{nR}) + 1. Then, since *R < I*(X; Y ), we can choose a *δ >* 0 such that
(1 − δ)I(X; Y ) − o(δ) *> R* + δ. Using this choice, we can upper bound Pr(dec(Y n) ̸= m|m is sent)
by Pr((enc(1), Y n) ̸∈ T) + (2 · 2^{nR} + 1)2−n(R+δ). Both the former and the latter go to 0 as n gets large, hence we can find an n such that E [Pr(dec(Y^n) ̸= m|m is sent)] *< ϵ/*2. Summing over all possible m's implies that

$$E\left[{\frac{1}{L}}\sum_{l=1}^{L}P r(d e c(Y^{n})\neq l|l{\mathrm{~is~sent}})\right]<\epsilon/2,$$
which in turn implies that there exists an encoder and decoder such that

$$\frac{1}{L}\sum_{l=1}^{L}P r(d e c(Y^{n}\neq l|l{\mathrm{~is~sent}}))<\epsilon/2.$$
Now, we elimintate from {1*, . . . , L*} all l's where Pr(dec(Y n) ̸= l|l is sent) ≥ ϵ. Note that the number of eliminated l's is at most L/2. After elimination, we are left with at least L/2 = 2^{nR} indices, for each of which Pr(dec(Y n) ̸= l|l is sent) *< ϵ*. This concludes the proof.

## 2 Channels With Costs

In order to move to the next chapter where we will introduce channels that accept a continuous input, we must define the notion of cost function for communication systems. Let us suppose we have the same scenario as before where this time we introduce a cost function b : *X →* R which maps a real integer cost for each of the alphabet letters. Our system will take as input a message m of nR bits and try to output the closest message possible ˆm. Let as before R be the rate of communication in bits/channel use, Pe = maxm Pr( ^m ̸= m|m) be the probability that the message is not detected correctly, i.e. the error probability and define a new bound value

$$\beta=\operatorname*{max}_{m}{\frac{1}{n}}\sum_{i=1}^{n}b(e n c(m)_{i}),$$
as the worst case time average cost. In a similar way to what we did before, we define the following theorem:

**Theorem 1** : Given pY |X, a cost function b, ϵ > 0 and β, define

$R<C(p_{Y|X},\beta)=\max\limits_{p_{X}:E[b(X)]\leq\beta}I(X;Y)$.

Then, there exists an encoder and decoder with rate ≥ R, max error probability ϵ and worst case time average cost < β + ϵ.

**Proof**: Following the previous computations, the proof is trivial and is left as an exercise to whoever decides to read this.

More seriously, this theorem can be proved following the same computations done for the previously introduced good news theorem.
