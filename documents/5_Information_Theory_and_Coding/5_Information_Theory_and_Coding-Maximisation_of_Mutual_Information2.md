# Lecture 13: More On Mutual Information Maximisation

In this lecture, as the title suggests, we will dive further into maximising mutual information over some probability distribution and working with the Karush-Kuhn-Tucker (KKT) conditions defined previously. We will this time find an exact value for µ which will include citing a few important theorems.

## 1 Reminders From Analysis 1.1 Convexity And Concavity

Definition 1 (Convex set) : A set S ⊆ R∗ is said to be convex if ∀x, y ∈ S and ∀λ ∈ [0, 1] we have z = λx + (1 − λ)y ∈ S.

Definition 2 (Convex function) : A function f : S → R is said to be convex if ∀x, y ∈ S and
∀λ ∈ [0, 1], f(λx + (1 − λ)y) ≤ λf(x) + (1 − λ)f(y).

Note that we obtain a concave function by flipping the sign of the inequality above, i.e. if −f is convex. We can also say that a function f : [*a, b*] → R is convex iff it is smooth, i.e. if d2f(x)

$${\frac{J^{(4)}}{d x^{2}}}\geq0.$$
f thus has to be twice differentiable. This brings us to our next reminder.

## 1.2 Partial Derivatives

From analysis, we recall that for some small ∆x and ∆y, we have

$$f(x+\Delta x,y+\Delta y)-f(x,y)=\Delta x{\frac{\partial f}{\partial x}}+\Delta y{\frac{\partial f}{\partial y}}.$$
Here, if we replace the ∆'s by a common small term, multiplied by a constant factor, we have

$$f(x+\epsilon a,y+\epsilon b)=\epsilon\left(a\frac{\partial f}{\partial x}+b\frac{\partial f}{\partial y}\right)+o(\epsilon^{2}).$$

## 2 Usage Of KKT Conditions

Recall that in last lecture, we defined the KKT conditions. Namely, for a smooth $f:k$-simplex $\to\mathbb{R}$ and some $p\in k$-simplex such that it maximizes $f$,

$$\exists\mu\text{s.t.}\frac{\partial f}{\partial p_{i}}\begin{cases}=\mu&\text{\text{\textasciitif}}\text{s.t.}p_{i}>0\\ \leq\mu&\text{\textasciitif}\text{s.t.}p_{i}=0.\end{cases}$$
Note that the k-simplex is convex.

## 2.1 Sufficient Condition For Maximisation

Theorem 3 :Suppose f : k-simplex → R is concave and let p ∈ k-simplex such that it satisfies the KKT conditions. Then, ∀q ∈ k-simplex, f(q) ≤ f(p) (i.e. p is the maximiser).

## 2.2 Examples

1. Let us try to maximise the 3-simplex (p1, p2, p3) 7→ p1p2p3 = f(p1, p2, p3). Here the partial
derivatives are trivial:
$${\frac{\partial f}{\partial p_{1}}}=p_{2}p_{3},\quad{\frac{\partial f}{\partial p_{2}}}=p_{1}p_{3},{\mathrm{~and~}}{\frac{\partial f}{\partial p_{3}}}=p_{1}p_{2}.$$
We see that each pi is equal so the triplet (1/3, 1/3, 1/3) satisfies the KKT conditions with f(.) = (1/3)^3.

Note that maximising p1p2p3 is equivalent to maximising log(p1p2p3) =
log p1 +log p2 +log p3. By KKT, we can find a µ such that 1/p1 ≤ µ, 1/p2 ≤ µ and 1/p3 ≤ µ.

Since each pi is equal and so non zero, we have equality and deduce that µ = 3.

2. Suppose now f(p1, p2, p3) = (1 + p1)p2p3. Consider F = log f and let us maximise it. The
derivatives are respectively 1/(1 + p1), 1/p2 and 1/p3. We have 1/p2 = 1/p3 = µ since p2 or
p3 cannot be 0. Then, we see that setting p1 = 0 satisfies the KKT conditions. From there,
we deduce that p2 = p3 = 1/2 and so µ = 2.

## 2.3 Application Of The Previous Theorem To The Problem Of Mutual Information

**Theorem 4**: _Given the joint distribution $p_{Y|X}(y|x)$, a probability $p_{X}$ maximises $I(X;Y)$ iff $\exists\mu\ s.t.$_

$$\sum_{y}p_{Y|X}(y|x_{0})\ln\frac{p_{Y|X}(y|x_{0})}{p_{Y}(y)}\begin{cases}=\mu+1=\mu&\forall x_{0}\ s.t.\ p_{X}(x_{0})>0\\ \leq\mu+1=\mu&\forall x_{0}\ s.t.\ p_{X}(x_{0})=0.\end{cases}$$

Moreover, µ = max_{pX} I(X; Y ).
