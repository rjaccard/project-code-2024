More ways to compute $\sum_{i=0}^{n} i$. Last time we briefly discussed a telescoping based method to calculate $T_{n}=\sum_{i=0}^{n} i$ that is particularly useful because it generalizes to a method to compute for any fixed postitive integer $k$ the sum $\sum_{i=0}^{n} i^{k}$ of the $k$-th powers up to $n$ (assuming $\sum_{i=0}^{n} i^{\ell}$ are known for $0<\ell<k$ ). This was already pointed out in the final paragraph of the October 12 lecture notes and is used in this week's exercise 4. Before the break we focussed on a number of less generally applicable methods to compute $T_{n}$ and a method to compute another useful summation, namely $\sum_{i=1}^{\infty} i r^{i-1}$.

First it was briefly mentioned that sums can be approximated (bounded from above or below or both) by integrating the corresponding real function. For instance $\sum_{i=0}^{n} i$ can be approximated by $\int_{0}^{n+1} x d x=\left[\frac{1}{2} x^{2}\right]_{0}^{n+1}=\frac{1}{2}(n+1)^{2}$, and more in general $\sum_{i=0}^{n} i^{k}$ can be approximated by $\int_{0}^{n+1} x^{k} d x=\left[\frac{1}{k+1} x^{k+1}\right]_{0}^{n+1}=\frac{1}{k+1}(n+$ $1)^{k+1}$ (where in class I simply wrote " $\approx(n+1)^{k+1}$ ", discarding the multiplicative factor $\frac{1}{k+1}$ as relatively unimportant - we will see later why that factor is not our main concern and why we focus on the $(n+1)^{k+1}$ (or, rather, $n^{k+1}$ ) part. Though such estimates are definitely useful, here we are more interested in precise expressions for the sums.

Summation of an arithmetic sequence: simple pictorial method. The first method was explained by making a staircase picture of the function $f(i)=i$ for $i=0,1,2,3,4$ (thus with $T_{4}$ squares under the staircase). The entire staircase was then "lifted from the blackboard", turned by $180^{\circ}$, and put back on the blackboard, right on top of (and not overlapping with) the staircase where it came from, thereby forming a perfect rectangle of twice the area of the original staircase picture. From this informal argument it then followed that $2 T_{n}=n(n+1)$, thus "suggesting" that $T_{n}=\frac{n(n+1)}{2}$. Actually, it was shown that this staircase lifting and turning operation can be done in two different ways, one leading to $n+1$ terms equal to $n$ (i.e., an $(n+1) \times n$-rectangle), the other leading to $n$ terms equal to $n+1$ (i.e., an $n \times(n+1)$-rectangle), but we only used the first one to show how precisely the same argument applies when using summation formulas (to show how index substitutions etc. work). This calculation is repeated below.

Given that $T_{n}=\sum_{i=0}^{n} i$ (which we want to compute), let $j$ be a new variable such that $i+j=n$ (and therefore $j=n-i$ and $i=n-j$ ): it follows that when $i=0$ then $j=n$ and if $i=n$ then $j=0$. Now we replace $i$ by $n-j$ as the term in the summation and change the first and last index-value in the summation in a corresponding manner: the starting point $i=0$ becomes $j=n$ and the final index
value $i=n$ becomes $j=0$. Unfortunately, the new summation index $j$ now starts at its highest value $n$ and goes to its lowest value 0 (the " $\sum$ " below), so we reverse the order of the summation (one may wonder if we can just do this: indeed, this needs a proof, and we will see later in the semester how this can indeed be proved to be correct; intuitively, it is not a problem, if the addition is commutative, which it is). Here is what we did:

$$
T_{n}=\sum_{i=0}^{n} i=\sum_{j=n}^{0}(n-j)=\sum_{j=0}^{n}(n-j)
$$

From $T_{n}=\sum_{j=0}^{n}(n-j)$ it follows that $T_{n}=\sum_{i=0}^{n}(n-i)$ where we simply replace $j$ by $i$ again, because after all the name of the summation variable is irrelevant. We now have that

$$
T_{n}=\sum_{i=0}^{n} i \text { and that } T_{n}=\sum_{i=0}^{n}(n-i)
$$

where the leftmost identity refers to the "original staircase picture" on the blackboard and the rightmost to the picture that was lifted, turned, and put back on the blackboard on top of the original staircase. We now add the two identities and get

$$
T_{n}+T_{n}=\left(\sum_{i=0}^{n} i\right)+\left(\sum_{i=0}^{n}(n-i)\right)
$$

Here we have two summations that both use $i$ as summation index and for both of them the index $i$ runs from zero to $n$, so we may simply combine the corresponding terms under a single summation sign " $\sum$ " that goes from zero to $n$. As a result we get that

$$
2 T_{n}=\sum_{i=0}^{n}(i+(n-i))
$$

Now finish the argument by simplifying $(i+(n-i))$ to $i+n-i=n$ so that we find

$$
2 T_{n}=\sum_{i=0}^{n} n
$$

from which it follows that (because the sum consists of $n+1$ terms each of which is equal to $n$ )

$$
2 T_{n}=(n+1) n \text { and thus that } T_{n}=\frac{n(n+1)}{2}
$$

This finishes yet another of our many calculations of $T_{n}$. Note that the entire argument is just a cleaner way of expressing the observation that $T_{n}=\sum_{i=0}^{n} i$ equals both

$$
\begin{aligned}
& 0+1+2+\ldots+(n-2)+(n-1)+n \\
& \text { and } \\
& n+(n-1)+(n-2)+\ldots+2+1+1
\end{aligned}
$$

that summing these expressions term-by-term thus results in $n+1$ terms that are all equal to $n$ : it follows that $2 T_{n}=(n+1) n$, which implies that $T_{n}=\frac{n(n+1)}{2}$.

To get $n$ terms that are all equal to $n+1$ instead, we would use the fact that $T_{n}=\sum_{i=0}^{n} i$ equals $\sum_{i=1}^{n} i$, which equals both and that summing these expressions term-by-term results in $n$ terms, each equal to $n+1$.

Summation of an arithmetic sequence: more involved pictorial method. Instead of putting the complete staircase, after rotation, on top of itself, we also mentioned that we can cut the staircase right in the middle, and put the rotated bigger part on top of the first part, resulting in $n / 2$ terms each equal to $n+1$ (for even $n$ ) or $(n+1) / 2$ terms each equal to $n$ (for odd $n$ ). The two cases result in the sum values $\frac{n(n+1)}{2}$ and $\frac{(n+1) n}{2}$, respectively, which are the same. The only reason to show this involved approach is that we can practice a bit more with index shifts and reversions. Below the corresponding calculations (which were not done in class).

$n$ even. We use that $n / 2$ is an integer, that $n=n / 2+n / 2$, that we may drop the term for $i=0$ from $\sum_{i=0}^{n} i$, because that term is zero, and that the ranges from 1 to $n / 2$ and from $(n / 2)+1$ to $n$ (both ranges including the lower and upper bound) both contain $n / 2$ terms.

$$
\begin{aligned}
\sum_{i=1}^{n} i= & \sum_{i=1}^{n / 2} i+\sum_{i=(n / 2)+1}^{n} i \quad(\text { replace } i \text { by } j=i-n / 2 \text { in second sum }) \\
= & \sum_{i=1}^{n / 2} i+\sum_{j=1}^{n / 2}(j+n / 2) \quad(\text { replace } j \text { by } 1+n / 2-k, \text { so } j+k=1+n / 2 \\
& \text { and } j+n / 2=n+1-k, \text { and note that } k=n / 2 \text { if } j=1 \\
& \text { and that } k=1 \text { if } j=n / 2, \text { so swap order of the second sum) } \\
= & \left.\sum_{i=1}^{n / 2} i+\sum_{k=1}^{n / 2}(n+1-k) \quad \text { (replace } k \text { by } i\right) \\
= & \sum_{i=1}^{n / 2} i+\sum_{i=1}^{n / 2}(n+1-i) \quad(\text { combine the two sums }) \\
= & \sum_{i=1}^{n / 2}(i+(n+1-i)) \\
= & \sum_{i=1}^{n / 2}(n+1) \\
= & \frac{n(n+1)}{2}
\end{aligned}
$$

$n$ odd. We use that $(n-1) / 2$ and $(n+1) / 2$ are both integers, that $n=(n-1) / 2+$ $(n+1) / 2$, and that the ranges from 0 to $(n-1) / 2$ and from $(n+1) / 2$ to $n$ (both ranges including the lower and upper bound) both contain $(n+1) / 2$ terms.

$$
\begin{aligned}
\sum_{i=0}^{n} i= & \sum_{i=0}^{(n-1) / 2} i+\sum_{i=(n+1) / 2}^{n} i \quad(\text { replace } i \text { by } j=i-(n+1) / 2 \text { in second sum }) \\
= & \sum_{i=0}^{(n-1) / 2} i+\sum_{j=0}^{(n-1) / 2}(j+(n+1) / 2) \quad(\text { replace } j \text { by }(n-1) / 2-k, \text { so } \\
& j+k=(n-1) / 2 \text { and } j+(n+1) / 2=n-k, \text { and note that } k=(n-1) / 2 \\
& \text { if } j=0 \text { and that } k=0 \text { if } j=(n-1) / 2, \text { so swap order of the second sum) }
\end{aligned}
$$

$$
\begin{aligned}
\sum_{i=0}^{n} i & =\sum_{i=0}^{(n-1) / 2} i+\sum_{k=0}^{(n-1) / 2}(n-k) \quad(\text { replace } k \text { by } i) \\
& =\sum_{i=0}^{(n-1) / 2} i+\sum_{i=0}^{(n-1) / 2}(n-i) \quad \text { (combine the two sums) } \\
& =\sum_{i=0}^{(n-1) / 2}(i+(n-i)) \\
& =\sum_{i=0}^{(n-1) / 2} n \\
& =\frac{(n+1) n}{2}
\end{aligned}
$$

The above two examples are not meant to advertise either of those two methods as the way to calculate $\sum_{i=0 \text { or } 1}^{n} i$ (quite on the contrary): they are only meant to show all the index etc. calculations involved to formally realize the proposed computation.

Summation of a useful non-arithmetic, non-geometric sequence (from Table 2, Section 2.4. Let $R=\sum_{i=0}^{\infty} i r^{i-1}$ where $|r|<1$. First we noted that $\sum_{i=0}^{\infty} i r^{i-1}$ is the term-by-term derivative of $\sum_{i=0}^{\infty} r^{i}$, so we may be willing to believe that $R$ is the derivative of $\frac{1}{1-r}$ (which, as seen last time, equals $\sum_{i=0}^{\infty} r^{i}$ ). The derivative of $\frac{1}{1-r}$ equals $\frac{1}{(1-r)^{2}}$, so we could conclude that $R=\frac{1}{(1-r)^{2}}{ }^{2}$. That is correct, but a bit fishy becasue derived in a not entirely satisfactory manner. Another approach would be as follows:

$$
\begin{aligned}
R & =\sum_{i=0}^{\infty} i r^{i-1}=\sum_{i=1}^{\infty} i r^{i-1} \\
& =\left(\sum_{i=1}^{\infty}(i-1) r^{i-1}\right)+\left(\sum_{i=1}^{\infty} r^{i-1}\right) \\
& =\left(\sum_{\ell=0}^{\infty} \ell r^{\ell}\right)+\left(\sum_{\ell=0}^{\infty} r^{\ell}\right) \\
& =r\left(\sum_{\ell=0}^{\infty} \ell r^{\ell-1}\right)+\frac{1}{1-r} \\
& =r\left(\sum_{i=0}^{\infty} i r^{i-1}\right)+\frac{1}{1-r} \\
& =r R+\frac{1}{1-r}
\end{aligned}
$$

It is found that $R(1-r)=\frac{1}{1-r}$ so that $R=\frac{1}{(1-r)^{2}}$, but this approach also has its problems: strictly speaking this needs to be done a bit more carefully by considering finite sums only, similar to what we saw in the October 12 lecture notes when computing $\sum_{i}=0^{\infty} r^{i}$ in a similar manner; the remark made there ("This can easily be fixed, at little additional effort") applies here too. We won't make this argument precise, but instead opt for a more "elementary" method, to give as some first exposure to double summations.

To compute $R=\sum_{i=0}^{\infty} i r^{i-1}$ (where $|r|<1$ ) we use that $i=\sum_{j=1}^{i} 1$ and switches the order of the two resulting summations:

$$
\begin{aligned}
\sum_{i=1}^{\infty} i r^{i-1} & =\sum_{i=1}^{\infty}\left(\left(\sum_{j=1}^{i} 1\right) r^{i-1}\right)=\sum_{i=1}^{\infty}\left(r^{i-1}\left(\sum_{j=1}^{i} 1\right)\right)=\sum_{i=1}^{\infty} \sum_{j=1}^{i} r^{i-1} \\
& =\sum_{j=1}^{\infty} \sum_{i=j}^{\infty} r^{i-1}
\end{aligned}
$$

(to understand this last step it may help to make a picture)

$$
\begin{aligned}
& =\sum_{j=1}^{\infty} \sum_{\ell=0}^{\infty} r^{\ell+j-1}(i-j=\ell \text { so } i=j, j+1, j+2, \ldots \rightarrow \ell=0,1,2, \ldots) \\
& =\sum_{j=1}^{\infty}\left(r^{j-1} \sum_{\ell=0}^{\infty} r^{\ell}\right) \\
& =\sum_{j=1}^{\infty}\left(r^{j-1} \frac{1}{1-r}\right) \\
& =\frac{1}{1-r} \sum_{j=1}^{\infty} r^{j-1} \\
& =\frac{1}{1-r} \sum_{j=0}^{\infty} r^{j} \text { (be more careful with the indices than we were in class!) } \\
& =\frac{1}{1-r} \frac{1}{1-r} \\
& =\frac{1}{(1-r)^{2}} .
\end{aligned}
$$

Later we will see (many) more summations and applications of the summations that we have seen so far.

After the break we wrapped up Chapter 3 with a brief discussion of the main results from Section 2.5 .

Countability. A set $A$ is countable if it is finite or if there is a bijection from the set $\mathbf{N}$ of natural numbers to $A$ (or, equivalently, vice versa). In the former case, all elements of $A$ can be enumerated, because there are finitely many of them. But also in the second case all elements of $A$ can be enumerated: if we denote by $a_{i} \in A$ the image of $i \in \mathbf{N}$ under the bijection (that exists if $A$ is countable), then we can enumerate $A$ as $a_{0}, a_{1}, a_{2}, \ldots$ which will, if we let the dots go to infinity, cover all of $A$ because the mapping used is a bijection. Said differently, for any $a \in A$, if we consecutively try all $i \in \mathbf{N}$ starting at $i=0$, then we will at a given point run into $^{1}$ the unique ${ }^{2}$ value $i$ for which $a_{i}=a$, i.e., the unique $i$ for which the image $a_{i}$ of $i$ under the bijection equals $a$. Thus it is reasonable to say that $A$ is countable. An infinite set $S$ that is countable is said to have cardinality aleph zero (or "aleph null"), indicated as $\aleph_{0}$; thus $|S|=\aleph_{0}$.

It follows that if $A$ and $B$ are countable, then so is $A \cup B$ : if at least one of the two, say $A$, is finite, then first enumerate $A$ entirely, and then proceed with $B$ (which is finite or infinite, doesn't matter, as long as $B$ is countable); and if both $A$ and $B$ are infinite, then let $a_{0}, a_{1}, a_{2}, \ldots$ be an enumeration of $A$ and let $b_{0}, b_{1}$,[^0]$b_{2}, \ldots$ be an enumeration of $B$, then $a_{0}, b_{0}, a_{1}, b_{1}, a_{2}, b_{2}, \ldots$ (alternatingly taking the next of $A$ or of $B$ ) is an enumeration of $A \cup B$. This is not a proof (but it is a clear enough argument that a proof can be constructed based on it).

The bijection from $\mathbf{N}$ to $\mathbf{Z}$ defined by $f(2 k)=k, f(2 k-1)=-k$ for $k \in \mathbf{N}$ is a proof of the countability of $\mathbf{Z}$ (make sure that you understand that this is indeed a bijection, and check that $f^{-1}$, the inverse of $f$ that is a bijection from $\mathbf{Z}$ to $\mathbf{N}$, satisfies $f^{-1}(k)=2 k$ for $k \geq 0$ and $f^{-1}(k)=-2 k-1$ for $\left.k<0\right)$.

It follows that the union of countably many countable sets is countable. This can be seen in the following manner. To keep things easy, assume that all countable sets are infinite, disjoint, and that there are infinitely many of those countable sets (but, as was given, "only" countably many countable sets). So, because we have countably many sets we can enumerate them (using the bijection that exists between $\mathbf{N}$ and our collection of countable sets) as "countable set $S_{0}$ ", "countable set $S_{1}$ ", "countable set $S_{2}$ ", $\ldots$, and by letting the dots go to infinity each set will at a given point be encountered in our countable collection of sets. But it is also given that each set $S_{i}$ is countable itself, so for any $i \geq 0$ all elements of $S_{i}$ can be enumerated as $S_{i, 0}, S_{i, 1}, S_{i, 2}, S_{i, 3}, \ldots$ This leads to the following situation:

$$
\begin{array}{cc}
S_{0}: & S_{0,0}, S_{0,1}, S_{0,2}, S_{0,3}, \ldots, S_{0, j}, \ldots \\
S_{1}: & S_{1,0}, S_{1,1}, S_{1,2}, S_{1,3}, \ldots, S_{1, j}, \ldots \\
S_{2}: & S_{2,0}, S_{2,1}, S_{2,2}, S_{2,3}, \ldots, S_{2, j}, \ldots \\
\cdot & \cdot \\
\cdot & \cdot \\
\cdot & \cdot \\
S_{i}: & S_{i, 0}, S_{i, 1}, S_{i, 2}, S_{i, 3}, \ldots, S_{i, j}, \ldots
\end{array}
$$

It is a simple matter to organize a walk that visits all elements $S_{u, v}$ in the above picture in such a manner that the walk does not occasionally go off into infinity (from which one can never return to catch up with the counting of the other elements) and such that no elements are overlooked. One could take the consecutive and finite "north-east to south-west diagonals" fixing the sum of the indices per diagonal, and looping over this sum from $0,1,2,3, \ldots$ while visiting the finitely many elements (namely sum +1 elements) per diagonal in a regular manner (thus one element $\left(S_{0,0}\right)$ on the "sum of the indices equals zero" diagonal; two elements $\left(S_{0,1}, S_{1,0}\right)$ on the "sum of the indices equals one" diagonal; three elements ( $S_{0,2}, S_{1,1}, S_{2,0}$ ) on the "sum of the indices equals two" diagonal; four elements ( $S_{0,3}, S_{1,2}, S_{2,1}, S_{3,0}$ ) on the "sum of the indices equals three" diagonal; $\ldots ; i+1$ elements $\left(S_{0, i}, S_{1, i-1}, \ldots, S_{i-1,1}, S_{i, 0}\right)$ on the "sum of the indices equals $i$ " diagonal; ...), or one could do the same while alternatingly going up and down over the diagonals (as in the book), or one could come up with other (such as rectangular) patterns. This description is not a proof, but can be turned into a proof with more work.

Below two pieces of pseudo-code are given that visit all elements. Make sure you understand in which order the visits occur.

```
1: for sum $=0,1,2,3, \ldots$ :

    for $i=0,1,2, \ldots$, sum:

        $\operatorname{visit}\left(S_{i, \text { sum-i }}\right)$

2: for $k=0,1,2,3, \ldots$ :

    $\operatorname{visit}\left(S_{k, k}\right)$

for $i=0,1,2, \ldots, k-1$ :

    $$
    \operatorname{visit}\left(S_{k, i}\right) \text { and then } \operatorname{visit}\left(S_{i, k}\right)
    $$
```

It follows from the above that the set $M$ of pairs $(i, j) \in \mathbf{N}^{2}$ with $j \neq 0$ is countable, because all those pairs are included in the indices of the points that are visited. Because there is an easy surjection from $M$ to the set $\mathbf{Q}$ of positive rational numbers, namely by mapping the pair of integers $(i, j) \in M$ to the rational number $\frac{i}{j}$ (for instance mapping the pair $(3,5)$ and the pair $(21,35)$ (and infinitely many other pairs of the form $\frac{3 k}{5 k}$ for non-zero integers $k$ ) all to the rational number $\frac{3}{5}$ ), the countability of $\mathbf{Q}$ follows from the countability of $M$. Note that a minor complication is caused by negatives in $\mathbf{Q}$ - can you resolve this?

Next it was argued that using computer programs (plus inputs) we can compute only countably many functions. Each program (plus input, which we will no longer mention from now on) uses a finite alphabet of characters. Say there are $N$ different characters that can be used, thus there are at most $N$ distinct programs of length one, at most $N^{2}$ distinct programs of length two, at most $N^{3}$ of length three, $\ldots$, at most $N^{k}$ of length $k$, etc. For each length the collection is finite, and the sequence of lengths is countable (namely, $1,2,3, \ldots$ ), so the collection of all programs that we could possibly write - including all their possible inputs - is countable. It follows that we can compute only countably many functions. It follows, as shown in the next paragraph, that there are far more functions than we can calculate.

Now let $B$ be the set $\{f: \mathbf{N} \rightarrow\{0,1\}\}$ of all binary functions. Thus each $f \in B$ maps each integer to a bit. We want to show that we cannot calculate all functions in $B$. Assume the contrary, namely that we can calculate all functions in $B$. Given that we can calculate only countably many functions (as shown in the previous paragraph), we therefore have to assume that $B$ is countable. The latter implies that all functions in $B$ can be enumerated as $f_{0}, f_{1}, f_{2}, \ldots$ If we define a function $\tilde{f}$ by saying that for any nonnegative integer $i$ it is the case that $\tilde{f}(i)=f_{i}(i)$, then $\tilde{f}$ is again a binary function, and thus in $B$. But if $f$ is a binary function, then its negation $g=1-\tilde{f}$ is also a binary function, thus also $g \in B$, and thus $g$ must be among our enumeration $f_{0}, f_{1}, f_{2}, \ldots$ of all binary functions. But from the definition $g=1-\tilde{f}$ it follows that $g(i)=1-\tilde{f}(i)$, so that with $\tilde{f}(i)=f_{i}(i)$ it follows that $g(i)=1-f_{i}(i)$ and in particular that for all nonnegative integers $i$ it is the case that $g(i) \neq f_{i}(i)$. From this it follows that for all $i$ it is the case that $g \neq f_{i}$ (because they are different when evaluated at $i$ ), so that $g$ cannot appear among the functions $f_{i}$ for $i=0,1,2,3, \ldots$. This is a contradiction with the assumption that $f_{i}$ for $i=0,1,2,3, \ldots$ enumerates all functions in $B$. It follows that the assumption that $B$ is countable is wrong. This is Cantor's diagonalization argument.

$\begin{array}{lllllll}f_{0}(0) \neq g(0) & f_{0}(1) & f_{0}(2) & f_{0}(3) & \cdot & \cdot & \cdot \\ f_{1}(0) & f_{1}(1) \neq g(1) & f_{1}(2) & f_{1}(3) & \cdot & \cdot & \cdot \\ f_{2}(0) & f_{2}(1) & f_{2}(2) \neq g(2) & f_{2}(3) & \cdot & \cdot & \cdot \\ f_{3}(0) & f_{3}(1) & f_{3}(2) & f_{3}(3) \neq g(3) & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot & \cdot & \\ \cdot & \cdot & \cdot & \cdot & & \cdot \\ . & \cdot & \cdot & . & & .\end{array}$.

As shown in the book Cantor's diagonalization argument can also be used to prove that the set $\mathbf{R}$ of real numbers is not countable. Two sets $A$ and $B$ are said to have the same cardinality if there is a bijection from $A$ to $B$. Note that this definition has the interesting consequence that a set $A$ and a proper subset $B \subset A$ of $A$ may have the same cardinality. For instance, $A=\mathbf{Z}$ has $B=\mathbf{N}$ as a proper subset and, as seen above, there is a bijection from $\mathbf{Z}$ to $\mathbf{N}$; both $\mathbf{N}$ to $\mathbf{Z}$ have cardinality $\aleph_{0}$.

Similarly, because the tangent function is a bijection from the open interval $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ to $\mathbf{R}$, the set of all real numbers has the same cardinality as the set of real numbers strictly between $-\frac{\pi}{2}$ and $\frac{\pi}{2}$ - which is, obviously, a proper subset of the set $\mathbf{R}$ of real numbers; both are said to have cardinality $\aleph_{1}$, which equals $2^{\aleph_{0}}$.

Halting problem (cf. section 3.1 in the book). The above only gives us a non-constructive existence proof that there are (infinitely) many problems for which we cannot write a computer program. But we can actually give an example of a problem for which we cannot write a computer program: here is a proof that we cannot write a program that decides if any program $P$ when working on some input $x$ will terminate or not. Assume, on the contrary that we would have such a program. So we have a program, say $A$, such that $A(P, x)$ (i.e., $A$ when getting as input a program $P$ and an input $x$ to $P$ ), returns "yes" if $P$ working on input $x$ terminates but such that $A(P, x)$ returns "no" if $P$ working on input $x$ does not terminate.

Given $A$, define another program $Q$ which working on input some program $P$ (thus when running $Q(P))$ makes a call to $A(P, P)$ and stops if $A(P, P)$ returns "no" but goes into an infinite loop if $A(P, P)$ returns "yes". So, if $P$ applied to $P$ does not stop (according to $A$ 's "no"), then $Q$ stops, but if $P$ applied to $P$ stops (according to $A$ 's "yes"), then $Q$ does not stop. Note that in this application of $A$, the program $P$ gets itself as input - that may sound odd, but there is nothing that tells us that a program cannot use itself as its own input: a program is just a concatenation of characters over some alphabet, an input is also just a concatenation of characters over some alphabet, and there is nothing that intrinsically distinguishes the two.

Now consider what happens when program $Q$ gets $Q$, i.e., itself, as input. According to the definition of $Q$, this implies that $Q$ makes a call to $A(Q, Q)$ and then stops if $A(Q, Q)$ returns "no": thus $Q$ with input $Q$ terminates if $A(Q, Q)$ returns "no", but $A(Q, Q)$ returning "no" means, according to the definition of $A$ that $Q$ with input $Q$ does not terminate, with is a contradiction. Therefore $A(Q, Q)$ cannot return "no", implying it must return "yes", so that $Q$ with input $Q$ (according to the definition of $Q$ ) will loop infinitely. But this contradicts the fact that $Q$ with input $Q$ terminates, because we had concluded that $A(Q, Q)$ returns "yes" and $A(Q, Q)$ returning "yes" means that $Q$ with input $Q$ does terminate. It follows that $A(Q, Q)$ cannot return "yes" either, which implies that we have reached a contradiction. It follows that the initial assumption, the existence of $A$, must be incorrect.

A counting-based proof for the $x^{y}$ example (which we did not do in class). An "easier" proof follows that there are irrational numbers $x$ and $y$ such that $x^{y}$ is rational: a "simple" counting argument suffices. Let $y$ range over the irrational numbers, thus $y \in \mathbf{R} \backslash \mathbf{Q}$. There are uncountably many choices for $y$, because only countable many elements (those in $\mathbf{Q}$ ) cannot be chosen from the uncountable set $\mathbf{R}$. Consider $\sqrt[y]{2}=x$; thus $x^{y}=2$. With $y$ ranging over uncountably many distinct irrationals, $x$ ranges over uncountably many distinct real values. Occasionally, $x$ may hit a rational value, but that can happen only countably often, because there exist only countably many rational values, so there are only countable many that can be hit: most of the time, i.e., uncountably often, our irrational $y$ will result in an irrational $x$, which we find "good". Why good? Because with $x^{y}=2=\frac{2}{1} \in \mathbf{Q}$ all these uncountably many "good" instances provide an example of our desired pair of irrationals $(x, y)$ for which $x^{y}$ is rational, which proves the result. To some extent, however, the situation is even worse than in our first proof - there we were left empty handed but at least we knew that either $(\sqrt{2}, \sqrt{2})$ or $\left(\sqrt{2}^{\sqrt{2}}, \sqrt{2}\right)$ would
be our desired pair. Here we have uncountably many pairs, but no clue whatsoever what even one of them may look like.

The rest of this course will be quite a bit more down to earth and constructive, less contradictory, and more useful.

Next class. We will discuss Chapter 3 on Algorithms: a bit on algorithms and their complexity (section 3.1 and 3.3) and a lot on "big-O" (section 3.2). But first a (brief?) introduction to "the reality of algorithms when implemented on a computer" (which will be illustrated with a matrix multiplication example: make sure that you know how to multiply two matrices).


[^0]:    ${ }^{1}$ The "we will at a given point run into" is due to the fact that a bijection is surjective.

    ${ }^{2}$ The uniqueness is due to the fact that a bijection is injective.

