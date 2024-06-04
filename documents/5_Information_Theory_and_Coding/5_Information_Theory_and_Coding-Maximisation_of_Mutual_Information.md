
## Lecture 12: Maximisation Of Mutual Information

In this lecture, we will investigate more one of the important tools we introduced last lecture, namely, the maximal mutual information needed for channel communication.

## 1 Maximal Mutual Information

Recall that last time, we defined the quantity C(P) = max_{pX} I(X; Y ) for a stationary memoryless channel P. In order to better understand the meaning of this quantity, let us study two examples.

## 1.1 Binary Symmetric Channel

When trying to compute C(P) we notice an important point: if we write I(X; Y ) as H(Y ) −
H(Y |X), we notice that H(Y |X = 0) = h2(p) = H(Y |X = 1).

From there, we have that H(Y |X) = H(Y |X = 0)Pr(X = 0) + H(Y |X = 1)Pr(X = 1) = h2(p) hence,

$max_{p_{X}}I(X;Y)=\max_{p_{X}}H(Y)-h_{2}(p)=1-h_{2}(p)$,
by symmetry of the channel since, if X is uniform in {0, 1}, Y also is. Note that if p = 1/2, C(p) = 0. This is due to the fact that X and Y become independent Bernoullis of probability 1/2.

The plot is symmetric. In fact, when *p >* 1/2, we can flip the output values of y which results in the same scenario as when using the unflipped values when *p <* 1/2. Also note that in this scenario, a 10% failure probability will result in an approximate 50% loss when communicating accross the channel.

## 1.2 Binary Erasure Channel

Our second example is the binary erasure channel. 
It is important here to see the e as an error term that stops us from knowing which bit we actually sent accross the channel. Intuitively, it can be seen as *loss of information*. Let us now compute the maximum capacity. This time, write max_{pX} I(X; Y ) = max_{pX} H(X) − H(X|Y ). Individually, H(X|Y = 0) = H(X|Y = 1) = 0 and to obtain H(X|Y = e), we use Bayes theorem:

$$Pr(X=0|Y=e)=\frac{Pr(X=0,Y=e)}{Pr(Y=e)}=\frac{Pr(Y=e|X=0)Pr(X=0)}{Pr(Y=e)}$$ $$=\frac{pPr(X=0)}{p}=Pr(X=0),$$
and hence H(X|Y= e) = H(X).

From there, we deduce that H(X|Y ) = pH(X) and so max_{pX} I(X; Y ) = max_{pX} H(X)(1 − p) = 1 − p as max_{pX} H(X) = 1.

## 2 Properties Of The Optimisation Of C(P)

Once we fix P, I(X; Y ) is just a function of p_X. Recall that P = {p(y|x) : x ∈ X, y ∈ Y}. Here, if
|X|= k, p_X is just an element of the k-simplex {(p1*, . . . , p*k) : pi ≥ 0 and \sum pi = 1}. Notice that k-simplex only means that we deal with a k'th dimensional vector of probabilities. Our problem is essentially to maximise some function f : k-simplex → R, where f is I(X; Y ) as a function of pX.

## 2.2 Properties Of Concave Function Maximisation On A K-Simplex Structure

**Theorem 2**: _Suppose $f:k$-simplex $\rightarrow\mathbb{R}$ is smooth and suppose $\vec{p}\in k$-simplex maximises $f$. Then $\exists\mu$ such that_

$$\frac{\partial f}{\partial p_{i}}(p)\begin{cases}=\mu&\text{\text{\textasciitif.}}s.t.\ p_{i}>0\\ \leq\mu&\text{\textasciitif.}}s.t.\ p_{i}=0.\end{cases}$$

**Proof** If $p$ is a maximiser, then for any $i,j\text{\textasciitif.}}s.t.\ p_{j}>0$, we consider a vector $p^{\prime}=(p_{1},\ldots,p_{k})$ with

$$p_{i}=\begin{cases}p_{i}&\text{\textasciitif}\neq i\text{\textasciitif}}i\text{\textasciitif}\\ p_{i+\leftarrow}&\text{\textasciitif}t=i\\ p_{i\leftarrow}&\text{\textasciitif}t=j,\end{cases}$$
where *ϵ >* 0 is considered small. Then

$f(p^{\prime})=f(p)+\epsilon\left(\frac{\partial f}{\partial p_{i}}(p)-\frac{\partial f}{\partial p_{j}}(p)\right)+o(\epsilon^{2})$.

As we want the term in the parenthesis to be ≤ 0, this concludes the proof of p being a maximiser.

Otherwise, we would reach a contradiction and hence such µ exists.