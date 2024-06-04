Short intermezzo on pigeonhole principle: a constructive example. Many examples of applications of the pigeonhole principle ("if more than $B$ items are distributed over $B$ buckets, then there must be a bucket containing two or more items"; see also the footnote on the next page) are non-constructive in the sense that the existence of something is shown (you know there is a bucket that contains at least two items) without giving an actual way to construct it (you don't know which of the buckets contains two or more item). The present example is somewhat more constructive in the sense that the pigeonhole principle is proved to show the optimality of a certain construction.

We consider the following problem, from the pre-wireless printing era. Assume that a desktop can only use a printer if the desktop is directly connected, via a cable, to that printer. The question is how many cables are necessary and sufficient to connect $d$ desktops to $p$ printers in such a way that the desktops can always optimally use all $p$ available printers: thus, any subset of $p$ desktops (from the set of $d$ desktops) must be able to simultaneously use all $p$ available printers, i.e., such that no two desktops in the subset have to print on the same printer (and wait for each other). We may assume that $d>p$, because for $d<p$ the question does not make sense and because for $d=p$ the solution is trivial (just use $d=p$ cables, each desktop connected to its own printer). A sufficient solution would be to run a cable from each desktop to each printer, using in total $d p$ cables (product rule). But, as shown below, we can do better if $p>1$.

The argument consists of two parts: a construction where it is shown that a certain way of cabling satisfies the requirement that the set of $p$ printers can always be optimally used, followed by a separate argument (using the pigeonhole principle) proving that if fewer cables are used than used in the construction (and completely irrespective of how that construction works), then there must be a subset of $p$ desktops that is directly connected (via a cable) to at most $p-1$ of the $p$ available printers, thus violating our requirement (again due to the pigeonhole principle: at least two of those $p$ desktops will have to compete for one among the only $p-1$ printers).

Assuming both desktops and printers are ordered, the construction works by connecting the first desktop and the first printer using a single cable, doing the same for the second desktop and the second printer, etc., upto the $p$ th desktop and the $p$ th printer (for a total of $p$ cables so far), and by then connecting each of the
$d-p$ remaining desktops to all $p$ printers (for a total of $p$ cables per desktop, thus requiring an additional $(d-p) p$ cables (product rule again)). Overall we have used $p+(d-p) p$ cables.

We prove that the above construction works by showing that for any subset $S$ of $p$ desktops $p$ cables can be found leading from the $p$ desktops in $S$ to the $p$ printers (obviously in such a way that no two cables lead to the same printer - so the mapping is a bijection and "uses just the cables" as defined by the construction). Take a subset $S$ of $p$ desktops. If $S$ does not contain any of the first $p$ desktops, then all desktops in $S$ can "find their own" printer, because they are all connected to all printers: just make the assignment in a random but collision-free manner. If the subset $S$ contains $k$ of the first desktops, for some $k$ with $1 \leq k \leq p$, then let those $k$ desktops use the only printer they are connected to. That leaves $p-k$ unused printers each of which is wired to all $p-k$ remaining desktops in $S$ (i.e., not among the first $p$ ), so $p-k$ disjoint connections can be found (as above). That finishes the description of feasible solution that uses $p+(d-p) p$ cables.

It remains to prove that it is impossible to use fewer than $p+(d-p) p$ cables while still meeting the requirements. Thus we have to prove that if we use at most $p+(d-p) p-1$ cables, then we can find a subset of $p$ desktops that is directly connected to at most $p-1$ of the $p$ available printers. Assuming that we have at most $p+(d-p) p-1$ cables, and thus that on average a printer is connected to $\frac{p+(d-p) p-1}{p}$ cables, there must be a printer, call it $P$, with at most $\left\lfloor\frac{p+(d-p) p-1}{p}\right\rfloor=d-p$ cables connected to it: otherwise, each printers would have at least $d-p+1$ cables connected to it, for a total of at least $p(d-p+1)$ cables, which is one more cable than we assume we have (this argument is a version of the pigeonhole principle ${ }^{1}$ ).

Taking the printer $P$ that has at most $d-p$ cables connected to it, that printer $P$ is, via those at most $d-p$ cables, connected to at most $d-p$ desktops. What about the other desktops, of which there are at least $d-(d-p)=p$ ? We do not know to which printers those other at least $p$ desktops are connected, but we know for sure that they are not connected to printer $P$ : therefore they can be connected to at most the $p-1$ remaining printers. This implies the existence of a subset of $p$ desktops that is directly connected to at most $p-1$ of the $p$ available printers, which means that using $p+(d-p) p-1$ cables is not sufficient and that thus at least $p+(d-p) p$ cables are necessary. Because $p+(d-p) p$ cables was already shown to be sufficient it follows that $p+(d-p) p$ cables are necessary and sufficient. Note that this saves $p^{2}-p$ cables over the trivial approach to simply use $d p$ cables to connect all desktops to all printers.

Returning to identities involving binomial coefficients. Returning to where we left off at the end of the previous lecture, we were considering the scenario where we are given two disjoint sets $A$ and $B$ with $|A|=|B|=n$ (thus $A \cup B=2 n$ ) and counted the number of ways an $r$-combination (thus order irrelevant) can be selected without replacement from $A \cup B$ for positive integers $r$. Throughout we[^0]assume that $n \geq r$. We already know that this can be done in $\binom{2 n}{r}$ ways, but we are going to count it in a different way as well.

- We had excluded the case $r=0$. When incorrectly argued ("selecting zero items from $A \cup B$ can be done in one way, or it can be done by selecting zero items from $A$ (in one way) or zero items from $B$ (in one way)"), it leads to the incorrect identity $1=1+1$. After fixing the argument using the principle of inclusion and exclusion ("selecting zero items from $A$ or from $B$ are not disjoint events, so we have to subtract the number of ways in which zero items can be selected from $A \cap B$ : there is one way to do so"), corrected to $1=1+1-1$.
- Considering the case $r=1$, selecting a 1-combination (repetition or not and with or without replacement are both irrelevant for a 1-combination) from $A \cup B$ can, obviously, be done in $\binom{2 n}{1}=2 n$ ways (note that $A$ and $B$ were assumed to be disjoint, so $|A \cup B|=2 n$ ), or it can be done by selecting the element either from $A$ (in $\binom{n}{1}=n$ ways) or from $B$ (again in $\binom{n}{1}=n$ ways). Because the latter two possibilities are disjoint there is no need for the principle of inclusion and exclusion and we find that $\binom{2 n}{1}=\binom{n}{1}+\binom{n}{1}$, i.e., that $2 n=n+n$, which was argued to be a result of potential interest only because of the way it was derived.
- Last time we got stuck while considering the case $r=2$. Literally repeating the argument that was given: with $A$ and $B$ as above (thus disjoint and of cardinality $n$ ) and assuming that $n \geq 2$, if a 2-combination from $A \cup B$ is selected without replacement (which can be done in $\binom{2 n}{2}$ ways because $|A \cup B|=2 n$ ), then either the two elements belong to $A$ (thus $\binom{n}{2}$ ways they could have been selected), or to $B$ (again $\binom{n}{2}$ ways this could have been done), or one element comes from $A$ and the other from $B$ (due to the product rule there are $n^{2}$ ways this could have been done). Overall, and noting that selecting the two items just from $A$ is disjoint from selecting the two items just from $B$, this led to $\binom{2 n}{2}=2\binom{n}{2}+n^{2}$ which we then checked algebraically:

$\binom{2 n}{2}=\frac{2 n(2 n-1)}{2}=n(2 n-1)=n(n-1)+n^{2}=2 \frac{n(n-1)}{2}+n^{2}=2\binom{n}{2}+n^{2}$.

During the previous lecture, at this point a sensible question was raised, namely why the underlined part is correct: why does this $n^{2}$ not have to be divided by two, or something of that sort? After all, it was argued, we are interested in a 2-combination, so the order of our selection does not count and here it seems we took the order into account: an element from $A$ in $n$ ways, then an element from $B$ in $n$ ways, so a total of $n^{2}$ ways, but we $\operatorname{did} A$ first and then $B$ - the same $n^{2}$ that we got when deriving the number of length two passwords from an $n$-character alphabet. For passwords however the order is relevant (here it is not: therefore the suspicion that we must do some correction here) and we may use replacement (here we do not use replacement, so our current situation is apparently quite different).

To sort out this confusion, note that here we are considering an entirely different scenario from what we considered before: here we select an element from set $A$ $(|A|=n$ ways to do so) and an element from the set $B$ that is disjoint from $A$ (thus, $|B|=n$ ways to do so which are all disjoint from the choice made from $A$ ), thus a total of $|A||B|=n^{2}$ ways to select a 2-combination, where the order does not matter (if the order would have mattered, first $A$ then $B$ would have been different from first $B$ then $A$, and the overall count would have been $2 n^{2}$ ). If on the other hand $A$ and $B$ are not disjoint but, for instance, $A=B$ then the number of 2-permutations with replacement is $n^{2}$, the number of 2-combinations with replacement is $\binom{n+1}{2}$, the number of 2-permutations without replacement is $n(n-1)$, and the number of 2-combinations without replacement is $\binom{n}{2}$.

- In the same way the case $r=3$ leads to $\binom{2 n}{3}=\binom{n}{3}+\binom{n}{1}\binom{n}{2}+\binom{n}{2}\binom{n}{1}+\binom{n}{3}=$ $2\binom{n}{3}+2 n\binom{n}{2}$. The combinatorial proof of the latter identity is immediate given the
previous paragraph, and the algebraic proof is similarly straightforward: the left hand side evaluates to

$$
\binom{2 n}{3}=\frac{2 n(2 n-1)(2 n-2)}{3!}=\frac{4 n^{3}-6 n^{2}+2 n}{3}
$$

and the right hand side to

$$
2\binom{n}{3}+2 n\binom{n}{2}=\frac{2 n(n-1)(n-2)}{3!}+n^{2}(n-1)=\frac{n^{3}-3 n^{2}+2 n+3 n^{3}-3 n^{2}}{3}
$$

so the two sides can be seen to be the same.

- Generalizing the above combinatorial argument to arbitrary $r$-values (while assuming that $n \geq r)$, it is found that it "must be the case that"

$$
\begin{equation*}
\binom{2 n}{r}=\sum_{i=0}^{r}\binom{n}{r-i}\binom{n}{i} \tag{1}
\end{equation*}
$$

which already looks more interesting. This identity can also be seen to be true based on Pascal's triangle and the analogy with optimal walks in a rectangular grid.
Binomial theorem. Let $n \in \mathbf{Z}_{\geq 0}$ and let $X$ and $Y$ be variables, then

$$
(X+Y)^{n}=\sum_{r=0}^{n}\binom{n}{r} X^{n-r} Y^{r}
$$

The polynomial $(X+Y)$ has two terms and is therefore called a binomial. The binomial theorem thus states that the coefficients of the $n$-th power of a binomial
are the values $\binom{n}{r}$; these coefficients, i.e., the values $\binom{n}{r}$, are therefore called the binomial coefficients. The binomial theorem follows from the simple combinatorial argument that when evaluating the product

$$
\underbrace{(X+Y)(X+Y) \ldots(X+Y)}_{n \text { factors }(X+Y)}
$$

the coefficient of the term $X^{n-r} Y^{r}$ is the same as the number of distinct ways of selecting the term $Y$ a total number of $r$ times (so that the other $n-r$ terms selected will all have to be $X$-terms) from the $n$ available binomials $X+Y$. Because the order does not matter in this selection, this number of distinct ways (of selecting the term $Y$ a total number of $r$ times) is $\binom{n}{r}$.

The formal (non-combinatorial) proof uses induction and is a bit tedious but instructive. The propositional function $P(n)$ is the statement that $(X+Y)^{n}=$ $\sum_{r=0}^{n}\binom{n}{r} X^{n-r} Y^{r}$ and the domain for $n$ consists of the non-negative integers. The basis of the induction consists of proving $P(0)$, i.e., proving the statement of the theorem for $n=0$ : the left hand side evaluates to $(X+Y)^{0}=1$, and the right hand side evaluates to 1 as well because $\sum_{r=0}^{0}\binom{0}{r} X^{0-r} Y^{0}=\binom{0}{0} X^{0} Y^{0}=1$; it follows that the basis step is correct. (On an independent note: please remember that $0^{0}=1$.)

For the inductive step, take an arbitrary $k \in \mathbf{Z}_{\geq 0}$ and assume that $P(k)$ is correct, i.e., assume that $(X+Y)^{k}=\sum_{r=0}^{k}\binom{k}{r} X^{k-r} Y^{r}$; this is the induction hypothesis. We have to prove that $P(k+1)$ is correct, i.e., that

$$
\begin{equation*}
(X+Y)^{k+1}=\sum_{r=0}^{k+1}\binom{k+1}{r} X^{k+1-r} Y^{r} \tag{3}
\end{equation*}
$$

To prove this, consider $(X+Y)^{k+1}$ and write it as $(X+Y)(X+Y)^{k}$. Based on the induction hypothesis, thus that $P(k)$ is true, i.e., that $(X+Y)^{k}=\sum_{r=0}^{k}\binom{k}{r} X^{k-r} Y^{r}$, it follows from $(X+Y)^{k+1}=(X+Y)(X+Y)^{k}$ that

$$
\begin{aligned}
(X+Y)^{k+1} & =(X+Y) \sum_{r=0}^{k}\binom{k}{r} X^{k-r} Y^{r} \\
& =\left(X \sum_{r=0}^{k}\binom{k}{r} X^{k-r} Y^{r}\right)+\left(Y \sum_{r=0}^{k}\binom{k}{r} X^{k-r} Y^{r}\right) \\
& =\left(\sum_{r=0}^{k}\binom{k}{r} X^{k+1-r} Y^{r}\right)+\left(\sum_{r=0}^{k}\binom{k}{r} X^{k-r} Y^{r+1}\right) \\
\text { (use } r+1=\ell) & =\left(\sum_{r=0}^{k}\binom{k}{r} X^{k+1-r} Y^{r}\right)+\left(\sum_{\ell=1}^{k+1}\binom{k}{\ell-1} X^{k-\ell+1} Y^{\ell}\right) \\
& =\left(\sum_{r=0}^{k}\binom{k}{r} X^{k+1-r} Y^{r}\right)+\left(\sum_{r=1}^{k+1}\binom{k}{r-1} X^{k+1-r} Y^{r}\right)
\end{aligned}
$$

where for the last step we simply switched back from $\ell$ to $r$ again.

Continuing, and treating separately the green and the red terms from the first and the second summation, respectively, we get

$$
(X+Y)^{k+1}=\binom{k}{0} X^{k+1}+[\sum_{r=1}^{k}(\underbrace{\binom{k}{r}+\binom{k}{r-1}}_{\text {(use Pascal's identity) }}) X^{k+1-r} Y^{r}]+\binom{k}{(k+1)-1} Y^{k+1}
$$

and thus (with $\binom{k}{0}=1$, Pascal's identity, and $\binom{k}{k}=1$ )

$$
\begin{aligned}
(X+Y)^{k+1} & =X^{k+1}+\left(\sum_{r=1}^{k}\binom{k+1}{r} X^{k+1-r} Y^{r}\right)+Y^{k+1} \\
& =\underbrace{\binom{k+1}{0}}_{=1} X^{k+1}+\left(\sum_{r=1}^{k}\binom{k+1}{r} X^{k+1-r} Y^{r}\right)+\underbrace{\binom{k+1}{k+1}}_{=1} Y^{k+1} \\
& =\sum_{r=0}^{k+1}\binom{k+1}{r} X^{k+1-r} Y^{r} .
\end{aligned}
$$

This proves the inductive step because the final line shows that Equation (3) holds and thereby that $P(k+1)$ is correct under the assumption that $P(k)$ is correct. The statement of the binomial theorem now follows from the correctness of the basis step and the inductive step.

Proof of Vandermonde's identity. From the binomial theorem with $n$ replaced by $m+n$ and $X=1$ it follows that

$$
(1+Y)^{m+n}=\sum_{r=0}^{m+n}\binom{m+n}{r} Y^{r}
$$

and therefore that the coefficient of $Y^{r}$ in $(1+Y)^{m+n}$ equals $\binom{m+n}{r}$. But we can also write $(1+Y)^{m \overline{+n}}=(1+Y)^{m} \cdot(1+Y)^{n}$ and thus

$$
\begin{aligned}
(1+Y)^{m+n} & =\left(\sum_{r=0}^{m}\binom{m}{r} Y^{r}\right) \cdot\left(\sum_{r=0}^{n}\binom{n}{r} Y^{r}\right) \\
& =\sum_{r=0}^{m+n}\left(\sum_{i=0}^{r}\binom{m}{r-i}\binom{n}{i}\right) Y^{r}
\end{aligned}
$$

where for ease of notation we use the convention that $\binom{\ell}{j}=0$ if $j>\ell$. How this " $=$ " works, i.e., turning the product of two summations into a nested double summation, is a standard method that is referred to as "convolution"; if convolutions are new to you, this step is described further below (after we have wrapped up the proof of Vandermonde's identity).

From this last equation we find that the coefficient of $Y^{r}$ in $(1+Y)^{m+n}$ equals $\sum_{i=0}^{r}\binom{m}{r-i}\binom{n}{i}$. The earlier underlined part states that the coefficient of $Y^{r}$ in $(1+Y)^{m+n}$ equals $\binom{m+n}{r}$. Combining the two, we find that

$$
\binom{m+n}{r}=\sum_{i=0}^{r}\binom{m}{r-i}\binom{n}{i}
$$

which is Vandermonde's identity. Identity (1) now follows by taking $m=n$.

The convolution used for "=" may be explained in the following manner:

- because $Y^{0}$ can only be obtained from $Y^{0}+Y^{1}+Y^{2}+\ldots+Y^{m-1}+Y^{m}$ times $Y^{0}+Y^{1}+Y^{2}+\ldots+Y^{n-1}+Y^{n}$ by multiplying the $Y^{0}$ term and the $Y^{0}$ term to get $Y^{0} Y^{0}=Y^{0}$, the coefficient of the term $Y^{0}$ in the product of $\sum_{r=0}^{m}\binom{m}{r} Y^{r}$ and $\sum_{r=0}^{n}\binom{n}{r} Y^{r}$ is obtained by multiplying the coefficients $\binom{m}{0}$ and $\binom{n}{0}$ of the two " $r=0$ " terms in the sums and thus equals the inner-sum coefficient $\sum_{i=0}^{0}\binom{m}{0-i}\binom{n}{i}=\binom{m}{0}\binom{n}{0}$ of $Y^{0}$, i.e., for $r=0$;
- because $Y^{1}$ can only be obtained as $Y^{1} Y^{0}+Y^{0} Y^{1}$, the coefficient of the term $Y^{1}$ in the product of $\sum_{r=0}^{m}\binom{m}{r} Y^{r}$ and $\sum_{r=0}^{n}\binom{n}{r} Y^{r}$ is obtained by multiplying the " $r=1$ " coefficient $\binom{m}{1}$ in the first sum and the " $r=0$ " coefficient $\binom{n}{0}$ in the second sum and adding this to the product of the " $r=0$ " coefficient $\binom{m}{0}$ in the first sum by the " $r=1$ " coefficient $\binom{n}{1}$ in the second sum and thus equals the inner-sum coefficient $\sum_{i=0}^{1}\binom{m}{1-i}\binom{n}{i}$ of $Y^{1}$, i.e., for $r=1$;
- because $Y^{2}$ can only be obtained as $Y^{2} Y^{0}+Y^{1} Y^{1}+Y^{0} Y^{2}$, the coefficient of the term $Y^{2}$ in the product of $\sum_{r=0}^{m}\binom{m}{r} Y^{r}$ and $\sum_{r=0}^{n}\binom{n}{r} Y^{r}$ is obtained by multiplying the " $r=2$ " coefficient $\binom{m}{2}$ in the first sum and the " $r=$ 0 " coefficient $\binom{n}{0}$ in the second sum, adding this to the product of the coefficients $\binom{m}{1}$ and $\binom{n}{1}$ of the two " $r=1$ " terms in the sums, and adding the result to the product of the " $r=0$ " coefficient $\binom{m}{0}$ in the first sum by the " $r=2$ " coefficient $\binom{n}{2}$ in the second sum and thus equals the inner-sum coefficient $\sum_{i=0}^{2}\binom{m}{2-i}\binom{n}{i}$ of $Y^{2}$, i.e., for $r=2$;
- similarly, the term $Y^{r}$ can only be obtained as $Y^{r} Y^{0}+Y^{r-1} Y^{1}+Y^{r-2} Y^{2}+$ $\ldots+Y^{1} Y^{r-1}+Y^{0} Y^{r}=\sum_{i=0}^{r} Y^{r-i} Y^{i}$, from which the general term above follows in the same manner as described above.

Next class. Read sections 7.1, 7.2, 7.3 .


[^0]:    ${ }^{1}$ The generalized pigeonhole principle states that if $N$ items are placed in $k$ buckets, then there is at least one bucket containing at least $\lceil N / k\rceil$ items. Namely, if not, then all buckets contain at most $\lceil N / k\rceil-1$ items, for a total of at most $k(\lceil N / k\rceil-1)$ items; because $\lceil N / k\rceil<(N / k)+1$ it follows that there are at most $k(\lceil N / k\rceil-1)<k(((N / k)+1)-1)=N$ items, thus at most $N-1$ items, a contradiction.

    The variation that we use here states that if $N$ items are placed in $k$ buckets, then there is at least one bucket containing at most $\lfloor N / k\rfloor$ items. Namely, if not, then all buckets contain at least $\lfloor N / k\rfloor+1$ items, for a total of at least $k(\lfloor N / k\rfloor+1)$ items; because $\lfloor N / k\rfloor>(N / k)-1$ it follows that there are at least $k(\lfloor N / k\rfloor+1)>k(((N / k)-1)+1)=N$ items, thus at least $N+1$ items, a contradiction.

