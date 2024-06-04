The class $\mathbf{P}$ of polynomial time solvable problems. We continued with our discussion of computational complexity. Last time we saw examples of problems that can be solved in time $O\left(n^{d}\right)$, i.e., for which there exists an algorithm and a fixed constant $d$ such that for any problem instance of size $n$ (i.e., the length of the input to the algorithm ${ }^{1}$ ), the algorithm will produce a solution in a number of operations that is $O\left(n^{d}\right)$. In the early 1970s it became customary to use the term polynomial time for such algorithms. If a problem can be solved by a polynomial time algorithm, the problem is polynomial time solvable (has polynomial complexity), and the problem is said to belong to the class $\mathbf{P}$ of polynomial time solvable problems: a problem $X$ can be solved in polynomial time if there is an algorithm $A$ and a fixed constant $d$ such that for all $n$ any instance of size $n$ of problem $X$ can be solved by $A$ in $O\left(n^{d}\right)$ operations:

$\exists A \exists d \forall n \forall$ instances $I_{n}$ of size $n$ of $X, A$ solves $I_{n}$ in time $O\left(n^{d}\right)$.

Note the importance of the order of the quantified variables $A, d, n$ and $I_{n}$ : reversing the order of the existentially quantified $d$ and the universally quantified $n$ and $I_{n}$ turns it into a useless property (it would always hold because it would become possible to choose $d$ depending on $n$ or $I_{n}$ ).

The existence of a polynomial time algorithm for a problem does not imply that each algorithm to solve the problem runs in polynomial time: there are always plenty of ways to do things in a less clever manner that may take many more operations. But, once a polynomial time algorithm for a problem has been found, the problem is, more or less and at least from a theoretical point of view, considered to be solved, because it means that the number of operations required to find a solution can be nicely controlled by a "decent" polynomial function: of course solutions require more operations when larger problem instances are solved, but the growth of the number of operations is limited by a polynomial function and therefore thought to be reasonably well under control.[^0]

Everything that is purple in the "big- $O$ hierarchy" in the October 26 lecture notes is polynomial time, assuming that the input length is $n$. Problems in the class $\mathbf{P}$ are traditionally referred to as tractable problems. But notice that the fixed exponent $d$ in the expression that upper bounds the number of operations (up to a constant) may be any nonnegative constant: one may wonder how "tractable" a polynomial time solution is for which $d=12$.

These nicely behaving polynomial time solvable problems are very much unlike nasty problems for which polynomial time solutions are not known to exist and for which the best algorithms known require at least exponential time: the blue bulleted expressions in the "big- $O$ hierarchy" represent exponential time and worse (see below) run times, again assuming that the input length is $n$.

Problems not known to be in P. A simple example of a problem for which no polynomial time solution is known to exist is the knapsack problem: given a set $S$ of $n$ items, each item in $S$ with a value and a weight, the "best" subset of items in $S$ must be found that satisfies a maximal weight restriction:

let $S=\left\{s_{1}, s_{2}, \ldots, s_{n}\right\}$ be some set of items, let $v, w: S \rightarrow \mathbf{R}_{\geq 0}$ be value $(v)$ and weight $(w)$ functions, and let $W \in \mathbf{R}_{\geq 0}$ be a maximal weight restriction. Find a subset $T \subseteq S$ such that

$$
\left(\sum_{t \in T} v(t)\right) \text { is maximized, while }\left(\sum_{t \in T} w(t)\right) \leq W
$$

A solution would be to try all $2^{n}$ possible subsets $T$ of $S$ (while verifying the maximal weight $W$ restriction) and selecting the one of highest value, but $2^{n}$ is exponential time. It is often more convenient to replace the above optimization problem by the - mostly equivalent ${ }^{2}$ - decision problem of deciding if for some specified value $V \in \mathbf{R}_{\geq 0}$ there exists a subset $T \subseteq S$ such that $\left(\sum_{t \in T} v(t)\right) \geq V$ and $\left(\sum_{t \in T} w(t)\right) \leq W$ (and, if so, to provide such a subset $T$ ). Note that it can easily (i.e., in polynomial time, even in linear time) be checked if any proposed solution (i.e., some subset $T$ ) to the latter decision problem is correct (i.e., satisfies the two conditions). How to efficiently construct such a solution, however, is unclear. In particular it is not known if exponential time is required.

Another example is the traveling salesman problem, where a bounded length tour must be found among $n$ cities: again a proposed solution can easily be checked, but finding one still escapes us, despite decades of intensive research. Note that a solution can be found in $O(n!)$ operations by trying all possible tours. Finding the chromatic index of a graph (the smallest number of colors required to color all vertices in the graph in a such a way that two neighbouring vertices have different colors) is - for the moment at least - not doable in polynomial time either; but checking if a given coloring satisfies a given bound is easily done (i.e., in polynomial time). These examples should be contrasted with problem such as "minimal spanning tree" or "shortest path" which are both easily solvable in polynomial time: minimal spanning tree even by a greedy algorithm that consistently selects a new edge of lowest weight without closing a cycle.

The class NP, and P versus NP. Occasionally a polynomial time solution is found for one of the nasty problems, but after a promising start in the 1970s this soon happened less and less frequently (once the low-hanging fruit was gone) and occurs only very rarely these days (this should not be interpreted as a reason to stop looking!). The separation between the polynomial time solvable problems and[^1]those for which a polynomial time solution is not known to exist (yet?) persists to the present day. A particular question that is found to be of interest (and that will earn you a one million US\$ prize if you solve it) is the $\mathbf{P}$ versus NP problem, namely if $\mathbf{P}$ is properly contained in NP or if $\mathbf{P}$ and NP are the same. But, what is NP? Probably not what you think it is, as explained in the next paragraph.

The class NP consists of those problems for which the correctness of a proposed solution can be verified in polynomial time: for instance, the decision versions of the knapsack and traveling salesman problems belong to NP. Note that NP does not stand for "not-P": it refers to the class of algorithms that can be solved in nondeterministic polynomial time. Here "nondeterminism" refers to the unspecified way in which a proposed solution is found: it may have been found by guesswork or any other way one sees fit (for instance, a "nondeterministic" one).

The difference between $\mathbf{P}$ and $\mathbf{N P}$ is the same as the difference between finding a solution to a problem (namely in polynomial time) and verifying (in polynomial time) that a given solution is correct - without worrying at all in the latter case how the solution was found. It is clear that all problems that belong to $\mathbf{P}$ also belong to NP. It has not been proved yet that there are problems that belong to NP but for which no polynomial time solution can exist (which would prove that $\mathbf{P} \neq \mathbf{N P}$ and thus that $\mathbf{P}$ is properly contained in NP) and neither has it been proved that all problems in NP allow a polynomial time solution (which would prove that $\mathbf{P}$ $=\mathbf{N P})$. Some argue that based on our failure to prove that $\mathbf{P}=\mathbf{N P}$, despite the aforementioned decades of indeed intensive research, $\mathbf{P} \neq \mathbf{N P}$ is a safer bet than $\mathbf{P}=\mathbf{N P}$

NP-complete problems. The above statement "neither has it been proved that all problems in NP allow a polynomial time solution" sounds like a hopeless exercise, but this is what makes this field interesting: it has been shown that there are problems in NP, the so-called NP-complete problems, that have the following intriguing property: if a polynomial time solution is constructed for just a single NP-complete problem (not for a single problem instance, of course...), then all problems in NP are polynomial time solvable. The first problem shown ${ }^{3}$ to be NPcomplete was the satisfiability problem (finding an assignment of values to logical values such that a conjunction of disjunctions of the logical values (or their negations) evaluates to true), by showing that any problem $X$ in NP can be reduced in polynomial time to the satisfiability problem (this means that solving $X$ can be done in polynomial time, assuming the operations spent on solving one or more (but at most polynomially many) satisfiability problems are not counted).

Much more can be said about this subject, and many more intriguing notions can be introduced or considered (such as: what is there, if anything, beyond NP?), but that is unfortunately outside the scope of this course. If interested, and to prepare yourself for later classes (such as the 4th semester bachelor's course "Theory of computation" by Prof. Ola Svensson) on Theoretical Computer Science, read Garey and Johnson's "Computers and Intractability": from the late 1970s, but an unbeatable classic.

Beyond exponential time. Let $n$ be the (variable) input size and let $d$ and $b>1$ be fixed constants (and logs are natural ${ }^{4}$, unless indicated otherwise such as in " $\log _{b}$ "). We have seen that run times that are $O\left(n^{d}\right)$ are called polynomial time, and that run times $\Theta\left(b^{n}\right)$ are called exponential time. Worse than exponential[^2]time is factorial time $\Theta(n!)$ (which equals $\Theta\left(e^{n \log (n)-n+O(\log (n))}\right)$ (use Stirling's formula), making it easier to see why $n$ ! dominates $\left.b^{n}\right)$ and even worse is $\Theta\left(n^{n}\right)$ (which equals $\Theta\left(e^{n \log (n)}\right)$, making is easy to see why $n^{n}$ really dominates $n!$ ).

Note that by writing the $\Theta$ estimates for $n!$ and $n^{n}$ as powers of $e$, it immediately follows that $n \log (n)$ and $\log (n!)$ are of the same order (i.e., "are each other's $\Theta$ "). During the previous lecture we proved this using elementary means (i.e., not using Stirling's formula).

The gray area between polynomial and exponential time. Given that polynomial time $n^{d}$ is $O\left(b^{n}\right)$ but exponential time $b^{n}$ is not $O\left(n^{d}\right)$, there is a "gap" between polynomial and exponential time. One may wonder if this "gap" is good for anything. Indeed it is: there are algorithms for which the number of operations is more than polynomial but less than exponential and that thus fall right in the gap (they are much less common, though, than polynomial time or exponential time algorithms, which is why this gray area is hardly discussed). Below we highlight two classes of algorithms that fall in this gap: subexponential time and quasi-polynomial time.

What type of expressions fit in the gap between $n^{d}$ and $b^{n}$ ? To find "something" between $n^{d}$ and $b^{n}$ rewrite $n^{d}$ in such a way that it looks a bit more like $b^{n}$ :

$$
n^{d}=\left(b^{\log _{b}(n)}\right)^{d}=b^{d \log _{b}(n)}
$$

Now both functions are exponential functions of $b$, with exponents $d \log _{b}(n)$ and $n$, respectively, so any exponent $y$ that is between $d \log _{b}(n)$ and $n$ will result in an expression $b^{y}$ between $n^{d}=b^{d \log _{b}(n)}$ and $b^{n}$. Consider the two exponents involved, $d \log _{b}(n)$ and $n$, and rewrite them as follows:

$$
d \log _{b}(n)=d \cdot n^{0}\left(\log _{b}(n)\right)^{1} \quad \text { and } \quad n=n^{1}\left(\log _{b}(n)\right)^{0}
$$

Writing $y(r)=n^{r}\left(\log _{b}(n)\right)^{1-r}$ to obtain a more general expression that captures both exponents, we find that the two exponents $d \log _{b}(n)$ and $n$ satisfy

$$
d \cdot y(0)=d \log _{b}(n) \quad \text { and } \quad y(1)=n
$$

With $d$ just a constant it is seen that by letting $r$ slide from 0 to 1 , the expression $b^{y(r)}$ changes from polynomial time $\left(n^{d}=b^{d \log _{b}(n)}\right)$ to exponential time $\left(b^{n}\right)$. Any value $r$ strictly between 0 and 1, i.e., $0<r<1$, results in a function $b^{y(r)}$ that is strictly somewhere between polynomial and exponential time, with $r$-values closer to zero resulting in a $b^{y(r)}$ closer to polynomial time and $r$-values closer to one resulting in a $b^{y(r)}$ closer to exponential time. Run times of this sort, with $0<r<1$, are referred to as subexponential time.

The resulting general expression for subexponential time

$$
b^{d \cdot n^{r}\left(\log _{b}(n)\right)^{1-r}}
$$

(for some constant $d$ ) may look crazy, but indeed there are classes of subexponential algorithms that have precisely these runtimes for $r=\frac{1}{2}$ and for $r=\frac{1}{3}$ (note that the latter is "better" than the former because $r$ is closer to zero and thus $b^{y(r)}$ is closer to polynomial time). For instance, currently the fastest general purpose algorithm to find a factor of a composite integer $N$ (thus with input length $n$ of order $\log (N)$ ) has the following run time expression:

$$
e^{(c+o(1))(\log (N))^{1 / 3}(\log (\log (N)))^{2 / 3}}
$$

where $e=2.718281828 \ldots$ is the basis of the natural logarithm (and of the log used here!) and $c=\left(\frac{64}{9}\right)^{1 / 3}$. Note that changing the base of the logarithm from $e$ (which
is the correct value here) to 2 (which would be the incorrect value here ${ }^{5}$ ) changes the constant $c$ - by approximately how much? More on this subject is outside the scope of this course.

Another way to find run time expressions between $n^{d}=b^{d \log _{b}(n)}$ and $b^{n}$ is by considering for any nonnegative constant $c$ the expression $b^{O\left(\left(\log _{b}(n)\right)^{c}\right)}$. For $c=1$ we get $b^{O\left(\left(\log _{b}(n)\right)^{1}\right)}=b^{O\left(\log _{b}(n)\right)}$ which is $O\left(n^{C}\right)$ for some constant $C$, where the $C$ is borrowed from the definition of the big- $O$ (in the exponent), and thus equivalent to polynomial time. For any value of the constant $c$, expressions of the form $b^{O\left(\left(\log _{b}(n)\right)^{c}\right)}$ are dominated by any subexponential run time as above of the form $b^{d \cdot n^{r}\left(\log _{b}(n)\right)^{1-r}}$ for $r>0$ : no matter how small $r>0$ is chosen, $n^{r}$ dominates $(\log (n))^{c}$ irrespective of how large (but constant) $c$ is chosen. Expressions of the form $b^{O\left(\left(\log _{b}(n)\right)^{c}\right)}$ do not fill the entire gap between $b^{d \log _{b}(n)}$ and $b^{n}$ (as the $r$-values above do when $r$ ranges from 0 to 1). They are referred to as quasi-polynomial time. Note that for $c=2$ one gets $n^{\log _{b}(n)}$, which is obviously worse than polynomial time (as the exponent $\log _{b}(n)$ grows with $n$ and is unbounded), but the growth is "only logarithmic", which explains the name "quasi-polynomial". For instance, it was recently found that computing discrete logarithms in multiplicative groups of finite fields with finite characteristic can be done in quasipolynomial time with $c=2$; to an outsider this may sound irrelevant; for crypto-practitioners it means that such fields can no longer be used in widely deployed - most likely also on your computer - digital signature schemes. Three years ago also the graph isomorphism problem was found to be solvable in quasi-polynomial time, but apparently there is still some uncertainty surrounding this claim.

Mathematical induction. Let $\mathbf{N}=\{0,1,2, \ldots\}$, the set of natural integers, be our domain, and let $P(n)$ be a propositional function of $n \in \mathbf{N}$. Mathematical induction is a convenient way to prove that

$$
\forall n P(n)
$$

(i.e., that $P(n)$ is true for all $n$ in the domain) using the "intuitively obvious" approach of showing that $P(0)$ is true (the basis step), followed by showing for all $k \in \mathbf{N}$ that $P(k+1)$ follows from $P(k)$ (the inductive step). Formulated as a rule of inference, mathematical induction thus looks like

$$
\begin{equation*}
(P(0) \wedge \forall k(P(k) \rightarrow P(k+1))) \rightarrow \forall n P(n) \tag{1}
\end{equation*}
$$

or, if you prefer, in rules of inference notation:
$P(0)$
(the basis step)
$\frac{\forall k(P(k) \rightarrow P(k+1))}{\forall n P(n) .}$
(the inductive step)

It is important to remember that the inductive step must be shown to hold for all $k$ in the domain under consideration, which, in the present case, is the set of natural integers $\mathbf{N}=\{0,1,2, \ldots\}$.

To most, this new rule of inference sounds perfectly reasonable. But one may wonder why this is a valid rule of inference (i.e., why it is a tautology), and if it follows, or not, from the rules that we have already seen. As shown in the (gray) paragraphs below - included just for your background information, but not part of either test - a new assumption is needed, namely either the assumption that indeed the above is a tautology or - equivalently - the so-called "well-ordering principle". If this well-ordering principle is deemed unacceptable, then so is the principle of[^3]mathematical induction, because the two (i.e., the well-ordering principle and the principle of mathematical induction) are equivalent: assuming either one, the other one follows (using our existing rules of inference).

Strong induction works in precisely the same way as mathematical induction, except that while proving $P(k+1)$ one assumes that $P(\ell)$ holds for all values $\ell$ in the domain that are at most $k$ - as opposed to just $\ell=k$ as in mathemetical induction. The rule of inference corresponding to strong induction thus looks like

$$
\begin{equation*}
(P(0) \wedge \forall k[(\forall \ell \leq k P(\ell)) \rightarrow P(k+1)]) \rightarrow \forall n P(n) \tag{2}
\end{equation*}
$$

Although strong induction looks like a more powerful tool than mathematical induction - after all, assuming $P(0), P(1), \ldots, P(k)$ is quite a bit more than just assuming $P(k)$ - the two notions are equivalent: what can be proved using mathematical induction can be proved using strong induction (trivially), and vice versa: if " $\forall n P(n)$ " can be proved using strong induction then observe that a strong induction proof of " $\forall n P(n)$ " implies a mathematical induction proof of " $\forall n Q(n)$ " where $Q(n)=\bigwedge_{i=0}^{n} P(i)$ and that " $\forall n P(n) \equiv \forall n Q(n)$ ".

On the validity of mathematical induction: why it is reasonable to add mathematical induction to our set of rules of inference, and why it does not follow from our existing set of rules of inference? Before we start using mathematical induction (by doing many examples) the question must be addressed why statement (1) above is indeed a rule of inference, i.e., a tautology. We try to prove this using a proof by contradiction.

Suppose that

$$
(P(0) \wedge \forall k(P(k) \rightarrow P(k+1))) \rightarrow \forall n P(n)
$$

is not true. Then the following must be true:

$$
\neg((P(0) \wedge \forall k(P(k) \rightarrow P(k+1))) \rightarrow \forall n P(n)) .
$$

As usual, we want to blindly follow the rules to get something we may be able to get a handle on. The obvious thing to do would be to pull the " $\neg$ " inside the parentheses. That means we first have to rewrite the (second) " $\rightarrow$ ", which results in the following equivalent formulation:

$$
\neg(\neg(P(0) \wedge \forall k(P(k) \rightarrow P(k+1))) \vee(\forall n P(n)))
$$

(note that we are using the equivalence " $(p \rightarrow q) \equiv(\neg p \vee q)$ "). Now we can conveniently pull the " $\neg$ " inside the parentheses and we get (due to "De Morgan"):

$$
(P(0) \wedge \forall k(P(k) \rightarrow P(k+1))) \wedge \neg(\forall n P(n))
$$

and therefore

$$
\begin{equation*}
(P(0) \wedge \forall k(P(k) \rightarrow P(k+1))) \wedge(\exists n \neg P(n)) \tag{3}
\end{equation*}
$$

This is indeed a rather obvious conclusion, but at least we did not derive it in a suspect "intuitive" manner, but by following the formal rules: the negation of the mathematical induction rule of inference is the statement that the basis step $P(0)$ holds and that the inductive step holds (because for all $k \in \mathbf{N}$ it is the case that $P(k+1)$ follows from $P(k))$, but that nevertheless there exists a value $n$ for which $P(n)$ is false. To show the validity of mathematical induction it must be shown that such an $n$ cannot exist, thus showing that (3) is incorrect. It is instructive to see how far we can get proving that this is indeed a false statement when using our rules of inference.


[^0]:    ${ }^{1}$ In our input length estimates we disregard the sizes of the numbers involved. For the problems and algorithms considered in this course that will be adequate. For more complex problems a more precise approach must be used.

[^1]:    ${ }^{2}$ Because the optimization problem can be solved by solving polynomially many decision problems (using binary search on potential $V$-values). The same comment applies to other optimization problems (such as traveling salesman or chromatic index).

[^2]:    ${ }^{3}$ Independently by two researchers in the very early 1970s: Stephen Cook and Leonard Levin.

    ${ }^{4}$ If the basis of a logarithm is not indicated you may assume that it equals $e=2.718281828 \ldots$ in a "mathematics" context and that it equals 2 in a "computer science" context; in our present context you can select either one if you feel uncomfortable without an explicit choice.

[^3]:    ${ }^{5}$ The wrong choice has been used in practice. This led to incorrect security estimates for cryptographic schemes, and resulted in information protection methods that turned out to be ineffective.

