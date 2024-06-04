
## Lecture 25: Polar Codes (2)

This lecture is the follow up from last lecture about polar codes. We continue our discussion on the construction of such codes and try to prove why they are useful in information theory.

## 1 Polar Coding On A *Bec*(P) 

## 1.1 Worked Example

Recall the basic polar construction we introduced last time. In the example of the Binary Erasure Channel of erasure probability p, we have the following:

$Y_{1}Y_{2}=\begin{cases}U_{1}+U_{2},U_{2}&\text{w.p.}(1-p)^{2}\\ U_{1}+U_{2},e&\text{w.p.}p(1-p)\\ e,U_{2}&\text{w.p.}p(1-p)\\ e,e&\text{w.p.}p^{2}.\end{cases}$

When performing the construction, we obtain that W^− is a *BEC*(2p(1−p)) and W^+ is a *BEC*(p2).

This comes from the fact that for W^−, only the first case above provides useful information on the output which implies that Y1Y2 = U1 with probability (1 − p)^2 and thus equals e with probability 1 − (1 − p)^2. For W^+, it is the last case alone that provides no information on the output such that Y1Y2U1 = U2 w.p. 1 − p^2 and therefore equals e w.p. p^2.

## 1.2 Numerical Experiment

We refer the reader to the following video https://www.youtube.com/watch?v=VhyoZSB9g0w&t=
2180s of Professor Telatar's conference on polar coding. This above numerical experiment gives us the following general recursion formula: for s ∈ {+, −}^∗, W^s = *BEC*(p(s)) where p(s^+) = p(s)^2 and $p(s^{-})=p(s)(2-p(s))$. We note that for any $0<\epsilon<1/2$,

$$\frac{1}{2^{t}}\sum_{s\in\{+,-\}^{t}}\mathds{1}_{\{p(s)\in(\epsilon,1-\epsilon)\}}\to0\text{as}t\to\infty,$$

$$\frac{1}{2^{t}}\sum_{s\in\{+,-\}^{t}}\mathds{1}_{\{p(s)<\epsilon\}}\to1-p\text{as}t\to\infty,$$

and

$$\frac{1}{2^{t}}\sum_{s\in\{+,-\}^{t}}\mathds{1}_{\{p(s)\geq1-\epsilon\}}\to p\text{as}t\to\infty.$$

Moreover, we can partition $\{+,-\}^{t}$ into $A\cup A^{c}$ s.t. $\sum$ formally, for any $\epsilon>0$ and any $R<1-p$ letting $t$ big e $\sum_{s\in A}p(s)\leq\epsilon$. This essentially means that there are a $\cdot$
s∈A p(s) ≤ ϵ. This essentially means that there are a lot of very good channels, i.e. that have small p's such that their sum also is small.

Moreover, we can partition $\{+,-\}^{\mathfrak{t}}$ into $A\cup A^{\mathfrak{c}}$ s.t. $\sum_{s\in A}p(s)\approx0$ and $|A|/2^{\mathfrak{t}}\approx1-p$. More formally, for any $\epsilon>0$ and any $R<1-p$ letting $t$ big enough, $\exists A\subset\{+,-\}^{\mathfrak{t}}$ with $|A|\geq R2^{\mathfrak{t}}$ and $\sum_{s\in A}p(s)\leq\epsilon$. This essentially means that there are a lot of very good channels, i.e. that have small $p$'s such that their sum also is small.