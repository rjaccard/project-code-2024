
## Appendix B The Shannon Entropy

Given a discrete random variable $X$, we define the _Shannon entropy_ of $X$, that we denote by $H(X)$, the value

$$H(X)=-\sum_{x}\Pr[X=x]\log_{2}\Pr[X=x]$$

Intuitively, $H(X)$ is the minimal number of bits of information that we need to encode $X$.

By extension, the _joint entropy_ of a pair of random variables $X$ and $Y$ is the entropy or the variable $(X,Y)$, i.e.

$$H(X,Y)=-\sum_{x,y}\Pr[X=x,Y=y]\log_{2}\Pr[X=x,Y=y]$$
The *conditional entropy* H(X|Y ) is by definition

$$H(X|Y)=H(X,Y)-H(Y)$$
By manipulating the previous equations, we obtain

$H(X|Y)=-\sum_{x,y}\Pr[X=x,Y=y]\log_{2}\Pr[X=x|Y=y]$
s∈S px = 1 (that is a *weight function*), and every function t from S to [*a, b*], we have

Intuitively, this is the number of bits to represent $X$ once $Y$ is already represented.

Lots of inequalities about the Shannon entropy come from the theory of convex functions. A real function $f$ on the segment $[a,b]$ is said to be convex if and only if for every discrete set $S$, every function $p$ from $S$ to $[0,1]$ such that $\sum_{x\in S}p_{x}=1$ (that is a _weight function_), and every function $t$ from $S$ to $[a,b]$, we have

$$\sum_{x\in S}p_{x}f(t_{x})\geq f\left(\sum_{x\in S}p_{x}t_{x}\right)$$
(px resp. tx denote the image of x by the function p resp. t.) I.e., the weight sum of the f(tx)'s is not smaller that the image of the weight sum of the tx's. A function is further strictly convex if making the inequality an equality would always imply that all tx's are equal. We know that for a function f which has a second derivative on ]*a, b*[, f is strictly convex if and only if f ′′(t) > 0 for all t ∈]*a, b*[.

Lemma B.1. H(X) ≥ 0 with equality if and only if X is constant.

Proof.: We define $f(t)=-\log_{2}t$. Clearly, $f$ is strictly convex on $[0,1]$. We let $S$ be the set of all $x$ for which $\Pr[X=x]\neq0$. By taking $t_{x}=p_{x}=\Pr[X=x]$, the definition of convexity gives that

$$H(X)\geq-\log_{2}\left(\sum_{x\in S}p_{x}^{2}\right)$$
Since P
x p2
x = 1 so all px must be equal to 1 so there must be a single term in the sum. I.e., S has a single point x.

⊓⊔
x p2
x ≤ 1, we obtain H(X) ≥ 0.

Assuming equality, we must have P
Lemma B.2. H(X, Y ) ≥ H(X) with equality if and only if there exists some function f such that Y = f(X) with probability 1. Proof. We first write

$$H(X,Y)-H(X)=H(Y|X)=\sum_{x}\Pr[X=x]\sum_{y}\Pr[Y=y|X=x]\log_{2}\Pr[Y=y|X=x]$$
We look at the inner term in the sum over x. Given x fixed, due to Lemma B.1, the inner sum over y is non-negative. So, H(*X, Y* ) ≥ H(X).

Now, if we have equality, all the sums over y must be null. Due to Lemma B.1, this implies that there exists a unique y (depending on x) for which Pr[Y = y|X = x] > 0. We write it y = f(x).

Clearly, Pr[Y = f(x)|X = x] = 1 for all x. So, we have Pr[Y = f(X)] = 1.

⊓⊔
Lemma B.3. H(*X, Y* ) ≤ H(X) + H(Y ) with equality if, and only if X and Y are independent.

Proof. The function t 7→ t ln t has second derivative 1
t . So, it is convex. By using the weights Pr[Y = y], we have

$$-\sum_{y}\Pr[Y=y|t_{y}\log_{2}t_{y}\leq-\left(\sum_{y}\Pr[Y=y]t_{y}\right)\log_{2}\left(\sum_{y}\Pr[Y=y]t_{y}\right)$$

with equality if and only if all $t_{y}$'s for $\Pr[Y=y]\neq0$ are equal. Applying this to $t_{y}=\Pr[X=x|Y=y]$ with $x$ fixed yields

$$-\sum_{y}\Pr[X=x,Y=y]\log_{2}\Pr[X=x|Y=y]\leq-\Pr[X=x]\log_{2}\Pr[X=x]$$
with equality if and only if Pr[X = x|Y = y] does not depend on y. By summing over all x, we obtain H(X|Y ) ≤ H(X) with equality if and only if X and Y are independent.

⊓⊔
Lemma B.4. If Pr[X = x] ̸= 0 for n values of x *then* H(X) ≤ log2 n with equality if, and only if all non-zero Pr[X = x] *are equal to* 1
n.

Proof.: The function $t\mapsto-\ln t$ has second derivative $\frac{1}{P}$. So, it is convex. By using the weights $\Pr[X=x]$, we have

$$\sum_{x}\Pr[X=x]\log_{2}t_{x}\leq\log_{2}\left(\sum_{x}\Pr[X=x]t_{x}\right)$$

with equality if and only if all $t_{x}$'s for $\Pr[X=x]\neq0$ are equal. By applying this to $t_{x}=1/\Pr[X=x]$, we obtain

$$H(X)\leq\log_{2}n$$

with equality if and only if all nonzero $\Pr[X=x]$ are equal.

