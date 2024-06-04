Heapsort. A far more entertaining sorting method than either of the ones discussed during the previous lecture is heapsort: like merge sort, it always run in time $O(n \log (n))$ and never suffers from deteriorating performance such as quick sort in the worst case; like quick sort and unlike merge sort, it does not require additional memory on top of the array containing the list to be sorted.

Heap sort is easiest (i.e., least hard) to understand if the array is depicted as a binary tree, with parent $\ell_{i}$ having children $\ell_{2 i}, \ell_{2 i+1}$ (unless either index is larger than $n$ ).
The first element $\ell_{1}$ of the array could be referred to as both the root or the top of the tree, the nodes in the tree without children could be referred to as the leaves of the tree, and the array element with the largest index as the last leaf of the tree (in the tree above that would be $\ell_{16}$ ).

A tree is a heap if each parent is at least equal to each of its children (if any) ${ }^{1}$. It simply follows (but we will not formally prove) that if a tree is a heap, then its top is the largest element of the corresponding array. To sort the array, it would thus suffice to

- first transform the initial tree into a heap;
- then for $i=n, n-1, n-2, \ldots, 2,1$ in succession:
- swap the values of nodes $\ell_{1}$ (the top of the tree) and $\ell_{i}$ (the last leaf of the tree corresponding to $\left.\ell_{1}, \ell_{2}, \ldots, \ell_{i}\right)$;
- restore the heap property of the tree $\ell_{1}, \ell_{2}, \ldots, \ell_{i-1}$ (note that this is a smaller tree because the last leaf of the previous tree is gone: from now on we disregard tree node $\ell_{i}$ ).

More on big- $O$. More properties of big-O were discussed. As a reminder, if $f$ and $g$ are two functions from $\mathbf{R}$ to $\mathbf{R}$ then we say that " $f(x)$ is big-oh of $g(x)$ " (and write " $f(x)$ is $O(g(x))$ " or " $f$ is $O(g)$ ") if

$$
\exists C, k \forall x>k|f(x)| \leq C|g(x)|
$$

where for convenience we take the domain for $C, k$, and $x$ as $\mathbf{R}_{>0}$. Thus, if we can find constants $C$ and $k$ such that $|f(x)| \leq C|g(x)|$ for any $x>k$, then $f(x)$ is $O(g(x))$. Finding explicit expressions for the witnesses $C$ and $k$ is usually omitted in practice (because it is hardly informative), but you should know how to proceed to prove that witnesses indeed exist (in order to be able to prove that some $f$ is
$O(g)$ for some $g)$. Note that the existence of $C$ and $k$ follows by proving that

$$
\limsup _{x \rightarrow \infty} \frac{|f(x)|}{|g(x)|}<\infty
$$

because the latter statement is equivalent to " $f$ is $O(g)$ ".

Below we list a whole bunch of examples and properties of big- $O$ that you should be familiar with (and many of which were not done in class and some of which were part of this week's exercises).

Example of finding witnesses. Given the polynomial $f(x)=75 x^{5}+642 x^{4}-$ $118 x+563661$, for $x \geq 1$ the value $|f(x)|$ is upper bounded by $\mid 75 x^{5}+642 x^{4}+$ 563661|, which itself is upper bounded by $563661\left(x^{5}+x^{4}+1\right)$ and thus, with $x^{5}+x^{4}+1 \leq 3 x^{5}$ for $x \geq 1$, by $3 * 563661 x^{5}$. Therefore, with witness $C=3 * 563661$ and $k=1$ we have shown that $f(x)$ is $O\left(x^{5}\right)$ (some write $f(x)=O\left(x^{5}\right)$, others get chemically unbalanced when seeing this because of the asymmetry of the equality: writing $O\left(x^{5}\right)=f(x)$ would be odd). It follows that $f(x)$ is $O\left(x^{d}\right)$ for any value $d \geq 5$ (but for any $\ell<5$ it is no longer the case that $f(x)$ is $O\left(x^{\ell}\right)$, but $x^{\ell}$ is $O(f(x)))$ : see next paragraph. Note that no attempt was made to find the "smallest possible" witnesses $C$ and $k$ (where no claim is made that "smallest possible" is even well-defined).

Fixed powers. For all positive constants $d, \ell$ with $d \geq \ell$ it is the case that $n^{\ell}$ is $O\left(n^{d}\right)$ and if $d>\ell$ then $n^{d}$ is not $O\left(n^{\ell}\right)$ : the statements easily follow by observing that $\lim \sup _{n \rightarrow \infty} \frac{n^{d}}{n^{\ell}}=\lim \sup _{n \rightarrow \infty} n^{d-\ell}=\infty$.

Big- $O$ of a polynomial of degree $d$ versus big- $O$ of sum of $d$-th powers. (This was part of the exercises and we did not get to it during the lecture; if this still needs clarification, do not hesitate to ask for it in class!) For any fixed nonnegative integer $d$ and constants $a_{i}$ for $i \in \mathbf{Z}$ with, say, $\max _{i \in \mathbf{Z}}\left(\left|a_{i}\right|\right)=B$ for some constant bound $B$, any polynomial

$$
f(x)=\sum_{i=0}^{d} a_{i} x^{i}
$$

satisfies $|f(x)| \leq(d+1) B x^{d}$ for $x \geq 1$, so $f(x)$ is $O\left(x^{d}\right)$ (with witnesses $C=(d+1) B$ and $k=1)$.

Similarly and yet quite differently, let

$$
S(n)=\sum_{i=0}^{n} a_{i} i^{d}
$$

(note that without the $a_{i}$-values this is just a sum of $d$-th powers). Because $S(n)$ consists of at most $n$ non-zero terms, and each term is upper bounded by $B n^{d}$ (because the largest $i$-value equals $n$ ), the value $|S(n)|$ is upper bounded by $n B n^{d}=$ $B n^{d+1}$ so that $S(n)$ is $O\left(n^{d+1}\right)$.

If the various constants involved are strictly positive, both these upper bounds $\left(f(x)\right.$ is $O\left(x^{d}\right)$ and $S(n)$ is $\left.O\left(n^{d+1}\right)\right)$ are lower bounds as well $\left(f(x)\right.$ is $\Omega\left(x^{d}\right)$ and $S(n)$ is $\left.\Omega\left(n^{d+1}\right)\right)$ and we say that " $f(x)$ is of order $x^{d "}$ and " $S(n)$ is of order $n^{d+1}$ " or $f(x)$ is $\Theta\left(x^{d}\right)$ and $S(n)$ is $\Theta\left(n^{d+1}\right)$ (with $\Omega$ and $\Theta$ as defined in the October 19 lecture and lecture notes).

Two further simple summations that you should keep in mind (and assuming a fixed integer $d>0): \sum_{i=0}^{n} d=(n+1) d$ which is $O(n)$, whereas $\sum_{i=0}^{d} d=d(d+1)$ which is $O(1)$, both because $d$ is constant.

Powers of $\log (n)$ versus powers of $n$. Any fixed power of $\log (n)$ (for any fixed basis $>1$ of the logarithm; below we stick to the basis 2 ) is upper bounded
("dominated") by even the tiniest fixed positive power of $n$ :

$$
\forall \epsilon>0, t>0\left(\log _{2}(n)\right)^{t} \text { is } O\left(n^{\epsilon}\right)
$$

To prove this, note that $n<2^{n}$ for all $n$ (this is obvious, but later we will prove it "par récurrence"), so that $\log _{2}(n)<n$ (because the logarithm function is strictly increasing). We assume $n \geq 2$. Now let $n=x^{\epsilon / t}$ from some $\epsilon>0$ and $t>0$. Then $x \geq 2^{t / \epsilon}$ (which may be a pretty big number for large $t$ and tiny $\epsilon>0$ ) and because $\log _{2}(n)<n$

$$
\log _{2}\left(x^{\epsilon / t}\right)<x^{\epsilon / t}
$$

It follows that $(\epsilon / t) \log _{2}(x)<x^{\epsilon / t}$ and thus $\log _{2}(x)<(t / \epsilon) x^{\epsilon / t}$ and $\left(\log _{2}(x)\right)^{t}<$ $(t / \epsilon)^{t} x^{\epsilon}$, showing that indeed $\left(\log _{2}(x)\right)^{t}$ is $O\left(x^{\epsilon}\right)$. The desired witnesses are thus $C=(t / \epsilon)^{t}$ and $k=2^{t / \epsilon}$; though these values may be big, they are constants.

More on logarithms. For any constant $\sigma$ it is the case that $\log \left(n^{\sigma}\right)$ is $O(\log n)$. Note that without the logarithms this is far from true if $\sigma>1$ (see also the above paragraph "Fixed powers"), implying also that $(\log (n))^{\sigma}$ is not $O(\log (n))$ if $\sigma>1$.

For all constants $a, b, \sigma, \tau$ with $a>b>1$ it is the case that $\log _{b}\left(n^{\tau}\right)$ is $O\left(\log _{a}\left(n^{\sigma}\right)\right)$, that $\log _{a}\left(n^{\sigma}\right)$ is $O\left(\log _{b}\left(n^{\tau}\right)\right)$, and that both $\log _{a}\left(n^{\sigma}\right)$ and $\log _{b}\left(n^{\tau}\right)$ are $O(\log (n))$.

These obvious properties may suggest that the base of the logarithm is irrelevant. Often this is indeed the case, and the reason that the base of the logarithm does not play a prominent role in general. But the base of the logarithm may be relevant, for instance if the logarithm appears in the exponent: with constants $a$ and $b$ as above (thus $a>b>1$ ) and constant $c>1$ it is the case that $c^{\log _{a}(n)}$ is $O\left(c^{\log _{b}(n)}\right)$ but $c^{\log _{b}(n)}$ is not $O\left(c^{\log _{a}(n)}\right)$.

Properties and non-properties of big- $O$. Let $f_{i}$ and $g_{i}$ be functions such that $f_{i}$ is $O\left(g_{i}\right)$ for $i=1,2$. It is often assumed that if some standard operation (such as addition (where $\left.\left(f_{1}+f_{2}\right)(x)=f_{1}(x)+f_{2}(x)\right)$, multiplication (where $\left(f_{1} f_{2}\right)(x)=$ $\left.f_{1}(x) f_{2}(x)\right)$, powering (where $\left.2^{f_{i}}(x)=2^{f_{i}(x)}\right)$, logarithm (where $\left(\log \left(f_{i}\right)\right)(x)=$ $\left.\log \left(f_{i}(x)\right)\right)$ is applied to the $f_{i}$-functions, that then the resulting composed function is again the big- $O$ of the same composition of the $g_{i}$-functions. Unfortunately, in general this assumption is most often wrong, as summarized below:

Addition (wrong): In general it is not the case that the function $f_{1}+f_{2}$ is $O\left(g_{1}+g_{2}\right)$ : take for instance $g_{2}=-g_{1}$. It is not hard to prove, however, that $\left(f_{1}+f_{2}\right)(x)$ is $O\left(\max \left(\left|g_{1}(x)\right|,\left|g_{2}(x)\right|\right)\right.$ (use the triangle inequality $|x+y| \leq$ $|x|+|y|$. For a proof of the triangle inequality refer to the Appendix at the end of these notes, as an example of a proof using a "case-by-case analysis".

Multiplication (exceptionally correct): It is true (and it is not hard to prove) that the function $f_{1} f_{2}$ is $O\left(g_{1} g_{2}\right)$.

Powering (wrong): In general it is not the case that $2^{f_{1}}$ is $O\left(2^{g_{1}}\right)$ : take for instance $f_{1}(x)=2 x$ and $g_{1}(x)=x$, then $f_{1}$ is $O\left(g_{1}\right)$ (witness $C=2$ ), but

$$
\frac{2^{f_{1}}(x)}{2^{g_{1}}(x)}=\frac{2^{f_{1}(x)}}{2^{g_{1}(x)}}=\frac{2^{2 x}}{2^{x}}=2^{x}
$$

and $2^{x}$ can obviously not be bounded by any constant (for $x$ going to infinity) as would be required by $2^{f_{1}}$ being $O\left(2^{g_{1}}\right)$ (remember the equivalence of " $f$ is $O(g)$ " and lim $\sup _{x \rightarrow \infty} \frac{|f(x)|}{|g(x)|}<\infty$ : because $\lim \sup _{x \rightarrow \infty} \frac{\left|2^{f_{1}}(x)\right|}{\left|2^{g_{1}}(x)\right|}=\infty$ it is not the case that $2^{f_{1}}$ is $\left.O\left(2^{g_{1}}\right)\right)$. Note that an incorrect answer is given to exercise 29 of Section 3.2 of the seventh edition of the book. In the eighth edition it is exercise 42 in Section 3.2.

Logarithm (wrong): In general $\log \left(f_{1}\right)$ is not $O\left(\log \left(g_{1}\right)\right)$. All we know about $f_{1}$ and $g_{1}$ is that there is a positive constant $C$ (say $C>2$ ) such that for all large enough $x$ it is the case that $\left|f_{1}(x)\right| \leq C\left|g_{1}(x)\right|$. It follows that $\log \left(\left|f_{1}(x)\right|\right) \leq \log (C)+\log \left(\left|g_{1}(x)\right|\right)$, but that does not imply $\left|\log \left(f_{1}(x)\right)\right|<\tilde{C}\left|\log \left(g_{1}(x)\right)\right|$ for some constant $\tilde{C}$ and large enough $x$, as required for $\log \left(f_{1}\right)$ being $O\left(\log \left(g_{1}\right)\right)$. If $f_{1}$ and $g_{1}$ are increasing and unbounded it follows that $f_{1}(x)>1$ and $g_{1}(x)>1$ for all $x>y$ for some $y$, so that logarithm-accidents involving huge negative values are avoided and we have $\log \left(f_{1}(x)\right) \leq \log (C)+\log \left(g_{1}(x)\right)=\log (C) \frac{\log \left(g_{1}(x)\right)}{\log \left(g_{1}(x)\right)}+\log \left(g_{1}(x)\right)$ and thus, using again that $g_{1}$ is increasing, that $\log \left(f_{1}(x)\right) \leq \log (C) \frac{\log \left(g_{1}(x)\right)}{\log \left(g_{1}(y)\right)}+$ $\log \left(g_{1}(x)\right) \leq \tilde{C} \log \left(g_{1}(x)\right)$, where $\tilde{C}=\frac{\log (C)}{\log \left(g_{1}(y)\right)}+1$.

Symmetries and lack thereof. It is obvious that $f$ is $O(f)$ (but see $f$ and $o(f)$ below). Generally speaking " $f$ is not $O(g)$ " does not imply " $g$ is $O(f)$ ": indeed, functions $f$ and $g$ can be constructed such that it is not the case that $f$ is $O(g)$ and it is not the case that $g$ is $O(f)$. A dull example is $f(x)=\sin (x)$ and $g(x)=\cos (x)$; more interesting examples would be where both $f$ and $g$ are strictly increasing functions (cf. this week's exercises).

Note that if $f$ is $O(g)$ it may be the case that $g$ is $O(f)$ as well or it may be the case that $g$ is not $O(f)$. The negation of $f$ is $O(g)$, i.e., "it is not the case that $f$ is $O(g)$ " or equivalently " $f$ is not $O(g)$ ", immediately follows from the above definition of big- $O$ :

" $f$ is not $O(g)$ " is equivalent to: $\quad \forall C, k \exists x>k|f(x)|>C|g(x)|$.

Thus, an "occasional $x$ " (i.e., not necessarily all $x$ ) that breaks the " $\leq$ " as required by big- $O$ suffices to negate $f$ is $O(g)$. It follows that to prove that $f$ is not $O(g)$ it suffices to find, for any constants $C>0$ and $k$, some $x>k$ (not necessarily all $x>k)$ for which $|f(x) / g(x)|>C$.

The big- $O$ hierarchy. You should be familiar with the following underlined (and strictly increasing) hierarchy of big-Os (and with the proofs: look at the ratios and consider the behavior for $n$ going to infinity, cf. $\lim$ sup-equivalence), where $b>1$, $\epsilon$ with $0<\epsilon<1, k>0$, and $d>1$ are fixed constants:

- any constant is $O(1)$
- 1 is $O(\log (\log (n)))$

but $\log (\log (n))$ is not $O(1)$

- $\log (\log (n))$ is $\quad \overline{O(\log (n))}$
- $(\log (n))^{k}$ is

but $\log (n)$ is not $O(\log (\log (n)))$

$O\left(n^{\epsilon}\right)$

- $n^{\epsilon}$ is

but $n^{\epsilon}$ is not $O\left((\log (n))^{k}\right)$

$\overline{O(n)}$

- $n$ is

but $n$ is not $O\left(n^{\epsilon}\right)$

$\overline{O(n \log (\log (n)))}$ but $n \log (\log (n))$ is not $O(n)$

- $n \log (\log (n))$ is
- $n(\log (n))^{k}$ is

$\frac{O(n \log (n))}{O\left(n^{d}\right)}$

but $n \log (n)$ is not $O(n \log (\log (n)))$

but $n^{d}$ is not $O\left(n(\log (n))^{k}\right)$

- $n^{d}$ is

$\overline{O\left(b^{n}\right)} \quad$ but $b^{n}$ is not $O\left(n^{d}\right)$

- $b^{n}$ is

$O(n!)$ but $n!$ is not $O\left(b^{n}\right)$

- $n!$ is $\overline{O\left(n^{n}\right)} \quad$ but $n^{n}$ is not $O(n!)$, whereas $n^{n}$ is $O\left((n!)^{2}\right)$
- $\log (n!)$ is $\quad \overline{O\left(\log \left(n^{n}\right)\right)}$

and $\log \left(n^{n}\right)$ is $O(\log (n!))$

To prove the statements about $n^{d}$ versus $b^{n}$ use $n^{d}=b^{d \log _{b}(n)}$ and observe that the latter's logarithmic in $n$ exponent $d \log _{b}(n)$ grows much slower than the exponent $n$ of $b^{n}$.

From $n!$ is $O\left(n^{n}\right)$ (and the earlier discussion on logarithms) it follows that $\log (n!)$ is $O\left(\log \left(n^{n}\right)\right)=O(n \log (n))$. Conversely, from the fact that $n^{n}$ is $O\left((n!)^{2}\right)$ (this follows from $n^{n} \leq(n!)^{2}$, which is easily seen to be the case ${ }^{2}$ ) it follows that $\log \left(n^{n}\right)=n \log (n)$ is $O\left(\log \left((n!)^{2}\right)\right)=O(\log (n!))$. We conclude that $n \log (n)$ is $\Theta(\log (n!))$. Here everything in purple is called polynomial time - traditionally "good" - and blue is exponential time or worse - traditionally "bad".

Big-O related definitions Except for big-Omega and big-Theta you may also (but probably less frequently) encounter the little-o or small-o notation (as seen in this week's exercises): " $f(x)$ is little-oh of $g(x)$ " (written as " $f(x)$ is $o(g(x))$ " or " $f$ is $o(g) ")$ if

$$
\forall C>0 \quad \exists k \forall x>k|f(x)|<C|g(x)|
$$

The usage here of the universal quantifier for $C$ (" $\forall C$ ") as opposed to the existential quantifier for $C$ (" $\exists C$ ") in big- $O$ is what makes the big difference between little-o and big- $O$ (the difference between usage of " $<C$ " here and " $\leq C$ " there is almost immaterial). The above definition of "little-o" is equivalent to:

$$
\lim _{x \rightarrow \infty} \frac{f(x)}{g(x)}=0
$$

For the little-o it is the case that not only does $f$ is $o(g)$ not imply $2^{f}$ is $o\left(2^{g}\right)$ (example: take $f(x)=\frac{1}{x^{2}}$ and $g(x)=\frac{1}{x}$ ) but neither does it imply that $\log (f)$ is $o(\log (g))$ (example: take $f(x)=x, g(x)=x^{2}$ ). Addition and multiplication properties are maintained though.

Note that $f$ is $O(f)$ but $f$ is not $o(f)$. So, in general, $f$ is $O(g)$ does not imply $f$ is $o(g)$; but $f$ is $o(g)$ implies $f$ is $O(g)$. Indeed: existence does not imply universal existence, but universal existence (over a non-empty domain) implies existence.

Computational complexity. As we have seen during the lectures, the big- $O$ notation is a succinct way to catch the essence of the number of operations to be carried out by an algorithm to solve a certain problem. Here it is assumed that a "problem" is interpreted as an infinite set of problem instances, where each problem instance has a certain well defined size. For instance: "sorting integers" is a problem, and any integer sequence of length $n$ may be regarded as an instance of length $n$ of the sorting integers problem; "integer addition" and "integer multiplication" are problems and any pair of $n$-bit integers may be regarded as an instance of length $n$ of the integer addition or of the integer multiplication problem. Any instance of length $n$ of the sorting problem can be solved in time $O(n \log (n))$, any instance of length $n$ of the integer addition problem can be solved in time $O(n)$, any instance of length $n$ of the integer multiplication problem can be solved in time $O\left(n^{2}\right)$ using schoolbook multiplication, in time $O\left(n^{\log _{2}(3)}\right)$ using Karatsuba multiplication, and in time $O(n \log (n) \log (\log (n)))$ using "fast multiplication". It can be done even faster using "Fürer's algorithm" (which runs in time $O\left(n \log (n) 2^{O\left(\log ^{*}(n)\right)}\right)$ time, where $\log ^{*}(n)$ is the number of times the logarithm function must be applied until the result is at most 1, cf. Exercise 42 (seventh edition) or 62 (eighth edition) of Section 5.3 in the book), but no one knows yet if an $O(n)$ or even an $O(n \log (n))$ solution is possible.

We refer to the expressions in the big- $O$ 's as the "complexity" (or "time complexity", or "computational complexity") of the problem at hand, or we say that[^0]the problem belongs to the "complexity class" $O(\ldots)$ for whatever ... is applicable: "the complexity of sorting is $n \log (n)$ ", "the complexity of addition is linear, but no one knows yet what the complexity is of multiplication"3. Below a few common complexity classes are listed (where the $O \mathrm{~s}$ may be replaced by $\Theta \mathrm{s}$, except it is more common to use $O \mathrm{~s}$ ), along with common problems that belong to that complexity class:
- $O(1)$ ("constant") to retrieve the largest item in a sorted list of any size, or to compute the parity of a number given in its binary representation;
- $O(\log (n))$ ("logarithmic") for binary search in a sorted list of $n$ items (if the list allows random access, for whatever that is worth);
- $O(n)$ ("linear") for linear search in a list of $n$ items that is not necessarily sorted (requiring only sequential access);
- $O(n \log (n))$ (" $n \log n$ ") to sort a list of $n$ items using merge sort or heapsort ${ }^{4}$ but
- $O\left(n^{2}\right)$ ("quadratic") to do it using bubble sort or in the worst case of quick sort;
- $O\left(n^{3}\right)$ ("cubic") to multiply two $n \times n$ matrices (note that the input length in that case is $n^{2}$, so as a function of the input length it is "only" a degree 1.5 algorithm and calling it cubic is a bit misleading - but traditional) and, a rather extreme example:
- $O\left(n^{12}\right)$ ("exponent twelve") for the original 2002 AKS primality-proving method ("the three Indians method" - Indian indians, not American indians) to establish if an $n$-bit integer is prime or composite (this has in the meantime been improved to $O\left(n^{6}\right)$ ("exponent six")).

Next class. We will wrap up the discussion of computational complexity and then move to proofs by mathematical and strong induction: read sections 5.1 and 5.2.

Appendix: proof of the triangle inequality. The absolute value $|x|$ of a real value $x$ is defined as follows:

$$
|x|=\left\{\begin{array}{rll}
x & \text { if } & x \geq 0  \tag{1}\\
-x & \text { if } & x<0
\end{array}\right.
$$

For real values $x$ and $y$ the triangle inequality is the statement

$$
|x+y| \leq|x|+|y| \text {. }
$$

To prove the triangle inequality we distinguish four cases; the proof is thus a nice example of a proof that uses a case-by-case analysis.

(1) Case $x \geq 0, y \geq 0$ : With (1) it follows from $x \geq 0$ and $y \geq 0$ that $|x|=x$ and $|y|=y$. It also follows from $x \geq 0$ and $y \geq 0$ that $x+y>0$, so that, again with (1), it is the case that $|x+y|=x+y$. Using $|x+y|=x+y$, $x=|x|$, and $y=|y|$, we find that

$$
|x+y|=x+y=|x|+|y|
$$

(2) Case $x<0, y<0$ : With (1) it follows from $x<0$ and $y<0$ that $|x|=-x$ and $|y|=-y$. It also follows from $x<0$ and $y<0$ that $x+y<0$, so that, again with (1), it is the case that $|x+y|=-(x+y)$ and therefore[^1]$|x+y|=-x+(-y)$. Using $|x+y|=-x+(-y),-x=|x|$, and $-y=|y|$, we find that

$$
|x+y|=-x+(-y)=|x|+|y| \text {. }
$$

(3) Case $x \geq 0, y<0$ : With (1) it follows from $x \geq 0$ and $y<0$ that $|x|=x$ and $|y|=-y$.

Distinguish two subcases:

(a) Subcase $x \geq-y$ : If $x \geq-y$ then $x+y \geq 0$ so that with (1) it follows that $|x+y|=x+y$. From $y<0$ it follows that $-y>0$, thus $0<-y$ from which, by combining $y<0$ and $0<-y$ it follows that $y<-y$. With $|x+y|=x+y$ it then follows that $|x+y|=x+y<x+(-y)$, which with $x=|x|$ and $-y=|y|$ leads to

$$
|x+y|<x+(-y)=|x|+|y| \text {. }
$$

(b) Subcase $x<-y$ : If $x<-y$ then $x+y<0$ so that with (1) it follows that $|x+y|=-(x+y)=-x+(-y)$. From $x \geq 0$ it follows that $-x \leq 0$ and $0 \leq x$, from which it follows that $-x \leq x$. With $|x+y|=-x+(-y)$ it then follows that $|x+y|=-x+(-y) \leq x+(-y)$, which with $x=|x|$ and $-y=|y|$ leads to

$$
|x+y| \leq x+(-y)=|x|+|y| .
$$

Either way, it may be concluded that

$$
|x+y| \leq|x|+|y| \text {. }
$$

(4) Case $x<0, y \geq 0$ : Let $\tilde{x}=y$ and $\tilde{y}=x$, then $\tilde{x} \geq 0$ and $\tilde{y}<0$. Case (3) thus applies to $\tilde{x}$ and $\tilde{y}$ and we find that

$$
|\tilde{x}+\tilde{y}| \leq|\tilde{x}|+|\tilde{y}|
$$

so that

$$
|y+x| \leq|y|+|x|
$$

from which

$$
|x+y| \leq|x|+|y|
$$

follows, as desired.


[^0]:    ${ }^{2}$ Because $(n!)^{2}=\prod_{i=1}^{n} i(n-i+1)$, to prove that $n^{n} \leq(n!)^{2}$ it suffices to prove that $n \leq$ $i(n-i+1)$ for $1 \leq i \leq n$. This follows from the fact that the parabola $-i^{2}+i(n+1)-n$ is zero for $i=1, n$ and positive on the interval $1<i<n$.

[^1]:    ${ }^{3}$ Observe, as noted in class, that each $\delta>0$ and each $k>0$ gives rise to unique complexity classes $O\left(n^{\delta}\right), O\left((\log (n))^{k}\right)$, and $O\left(n^{\delta}(\log (n))^{k}\right)$ and thus that there are uncountably many different complexity classes.

    ${ }^{4}$ During the lecture it was briefly argued why, if we can only make "binary decisions" such as comparing items, we need at least $\log (n!)$ steps to be able to distinguish between all $n$ ! possible distinct outcomes of the problem of sorting a list of $n$ items. Because $\log (n!)$ is of the same order as $n \log (n)$ sorting cannot be done faster than order $n \log (n)$.

