(1) Pairs. Let $S$ be an unordered collection of $n$ people, for a finite nonnegative integer $n$ (thus $n$ may be 0 , or 1 , or 2 , or 3 , or $\ldots$, which we write as " $n \in \mathbf{Z}_{\geq 0}$ "; this is different from saying that $n$ is a positive integer because that would exclude 0 and would be written as " $n \in \mathbf{Z}_{>0}$ "). Under the assumption that any two people are distinct, the collection $S$ can be regarded as a set (read about sets in the book) and the people belonging to $S$ may be referred to as elements of $S$. We refer to $n$ as the cardinality of $S$ which we write as $|S|=n$ (as done in the book) or $\# S=n$ (an alternative notation for the same).

Ordered pairs among elements of $S$ are defined as elements of the Cartesian product $S^{2}=S \times S$ : with $S \times S$ defined as the set $\{(x, y) \mid x \in S$ and $y \in S\}$ (cf. book) we find that for any distinct $x, y \in S$ the ordered pair $(x, y)$ is distinct from the ordered pair $(y, x)$, that $(x, x)$ is regarded as an ordered pair, and that in total there are $n^{2}$ distinct ordered pairs (because $|S \times S|=n^{2}$ ).

For example, if $T=\{a, b, c\}$ with $m=|T|=3$, then

$$
T^{2}=T \times T=\{(a, a),(a, b),(a, c),(b, a),(b, b),(b, c),(c, a),(c, b),(c, c)\}
$$

confirming that there are $\left|T^{2}\right|=9=m^{2}$ ordered pairs among the elements of $T$.

In this lecture, we prefer to consider only unordered pairs of distinct elements: "unordered" means that we do not distinguish between the two ordered pairs $(x, y)$ and $(y, x)$ and "of distinct elements" means that we exclude ordered pairs of the form $(x, x)$. In these notes, we refer to these "unordered pairs of distinct elements" as "pairs".

For the example set $T$, the set of pairs would be $\{(a, b),(a, c),(b, c)\}$ (or equivalently $\{(a, b),(a, c),(c, b)\}$; or equivalently $\{(a, b),(c, a),(b, c)\}$; or equivalently $\ldots)$, implying that even though there are 9 ordered pairs, there are just 3 pairs as we defined them (namely, "unordered pairs of distinct elements"). We can avoid all these ugly equivalent definitions of the set of pairs by denoting the elements of $T$ in such a way that an ordering is implied (even though the elements of a set are in principle not ordered) and by exploiting this ordering: in the present example, we could write $T=\left\{t_{1}, t_{2}, t_{3}\right\}$ and define the corresponding set of pairs at $\left\{\left(t_{i}, t_{j}\right) \mid 1 \leq i<j \leq 3\right\}$. In this notation, the original set of $3^{2}$ ordered pairs (the Cartesian product of $T$ by itself) could be written as $\left\{\left(t_{i}, t_{j}\right) \mid 1 \leq i \leq 3,1 \leq j \leq 3\right\}$ which is often more conveniently written as $\left\{\left(t_{i}, t_{j}\right) \mid 1 \leq i, j \leq 3\right\}$.

Can we find a general expression for the number of pairs as a function of $n$ (as we did for the number of distinct ordered pairs, which is $n^{2}$ )? More precisely: given a set $S$ of finite cardinality $n$ how many distinct pairs are there among the elements of $S$ ? We already know that there are $n^{2}$ distinct ordered pairs. To find the number of distinct pairs (i.e., the number of distinct unordered pairs of distinct elements) among those $n^{2}$ distinct ordered pairs, we first exclude all ordered pairs
of the form $(x, x)$ for $x \in S$ : because there are $n$ choices for $x$, this excludes $n$ ordered pairs from our set of $n^{2}$ ordered pairs: we find $n^{2}-n=n(n-1)$ remaining ordered pairs which are now all of the form $(v, w)$ for distinct $v, w \in$ $S$ (for the example this would exclude the ordered pairs $(a, a),(b, b)$, and $(c, c)$ from the Cartesian product $T^{2}$, resulting in $m(m-1)=3(3-1)=6$ remaining ordered pairs $\{(a, b),(a, c),(b, a),(b, c),(c, a),(c, b)\})$. Because in the remaining set of $n(n-1)$ ordered pairs each unordered pair of distinct elements (i.e., each pair) is counted twice (namely, for distinct $v \neq w \in S$ the ordered pairs $(v, w)$ and $(w, v)$ both occur) there are $\frac{n(n-1)}{2}$ distinct pairs among the elements of a set $S$ with $|S|=n$ (confirmed by the example where we found 3 pairs and now find that indeed $\left.\frac{m(m-1)}{2}=\frac{3(3-1)}{2}=3\right)$.

This was an example of a counting problem, of which we will see many other examples this semester. For counting problems it is always useful to check that a proposed solution is indeed correct by verifying the solution using one or more small examples, or to come up with a different counting argument that leads to the same solution (if it leads to another solution, then obviously something is wrong), or both. For the present solution (i.e., "there are $\frac{|S|(|S|-1)}{2}$ distinct pairs among elements of a set $S^{\prime \prime}$ ) our example showed that the formula is correct for $|S|=3$, easy inspection shows that it is correct for $|S|=0$ (no element, thus no pair, and indeed $\frac{0(0-1)}{2}=0$ ), for $|S|=1$ (a single element, so no pair with two distinct elements, thus no pair at all, and indeed $\frac{1(1-1)}{2}=0$ ), and for $|S|=2$ too (just two distinct elements, thus just a single pair, and indeed $\left.\frac{2(2-1)}{2}=1\right)$. For $S=\{a, b, c, d\}$ (with $|S|=4)$ the $\frac{4(4-1)}{2}=6$ pairs are given by $(a, b),(a, c),(a, d),(b, c),(b, d)$, and $(c, d)$. This may inspire you to find a different counting method that leads to the formula $\sum_{i=0}^{n-1} i=\frac{n(n-1)}{2}$, a formula that we will see - and prove - over and over again this semester.

(2a) Perfect matchings. Given a set $S$ of $n$ people, let $P$ be the set of pairs among the elements of $S$ (with pairs as defined above: unordered pairs of distinct elements). So, we have seen that $|P|=\frac{n(n-1)}{2}$. Let a pairing be an arbitrary subset of $P$, i.e., a pairing is a set of pairs. For instance, the empty set $\emptyset$ (cf. book) is a valid subset of $P$ and corresponds to the pairing that contains no pairs; the other extreme is the pairing that contains all pairs, corresponding to the subset $P$ of $P$. Regarding $S$ as the set of vertices of a graph and pairs as undirected edges between those vertices, the pairing consisting of the empty set of pairs would correspond to a graph on $n$ vertices without any edges, the pairing consisting of $P$ itself, i.e., containing all possible pairs, would correspond to a complete (simple, undirected) graph on $n$ vertices.

If you are familiar with power sets (cf. book), you know that there are $2 \frac{n(n-1)}{2}$ distinct pairings ${ }^{1}$, namely the number of different subsets of $P$, i.e., the cardinality of the power set of $P$. It follows that the number of distinct pairings grows very rapidly: $2^{0}=1$ for $n=1,2^{1}=2$ for $n=2,2^{3}=8$ for $n=3,2^{6}=64$ for $n=4$, $2^{10}=1024$ for $n=5,2^{15}=32768$ for $n=6$, as can easily (or painfully) be verified for the smaller (or larger) numbers.[^0]

Clearly, even for modest values of $n$ the set of pairings is already huge. Here, however, we are not interested in all pairings, but we are only interested in so-called matchings: a matching is a pairing that contains only disjoint pairs, where two pairs $(x, y)$ and $(v, w)$ are disjoint if $x, y \notin\{v, w\}$ - just a complicated way of saying that the elements in all pairs in a matching must be distinct or, equivalently, that any element may occur in at most one pair in the matching.

Not that we really need it, but one may be curious to know how many of the $2^{\frac{n(n-1)}{2}}$ distinct pairings are matchings. At this point we will not try to answer that question, but instead impose a further restriction on the type of pairings that we wish to consider: not only do we require that the pairs in a pairing are disjoint (i.e., the pairing is a matching) and thus that each element of $S$ occurs in at most one pair in the matching, but we also require that each element of $S$ occurs in at least one pair in the matching. From "in at most one pair" and "in at least one pair" it follows that each element of $S$ occurs in precisely one pair in the matching. Combined with the fact that each pair in the matching contains two distinct elements of $S$, it follows that the cardinality $|S|$ of $S$ must be twice the number of pairs in the matching and thus that the cardinality $|S|$ of $S$ must be even. A matching as just defined where each element of $S$ is contained in a pair in the matching is called a perfect matching. If a perfect matching consists of $k$ pairs (for an integer $k \in \mathbf{Z}_{\geq 0}$ ) then $|S|=2 k$.

To count the number of perfect matchings of the elements of a set $S$ with $|S|=$ $n=2 k$ (and to partially satisfy our curiosity in the first sentence of the previous paragraph because we will be counting perfect matchings only, excluding from our count the matchings that are not perfect), note that in a perfect matching an arbitrary element of $S$ can be matched (or "paired") in $n-1=2 k-1$ different ways, that with this first pair fixed an arbitrary element of the remaining set of $n-2$ elements can be matched in $(n-2)-1=2 k-3$ different ways, that with these first two pairs fixed an arbitrary element of the remaining set of $(n-2)-2=n-4$ elements can be matched in $(n-4)-1=2 k-5$ different ways, etc, so that (cf. book: product rule; this will be extensively discusses later) the overall number of perfect matchings becomes $\prod_{i=1}^{k}(2 i-1)$ : the product of all odd numbers $<n=2 k$.

The product of all odd numbers $<n=2 k$ can be written as the neat "closed form expression" $\frac{n!}{k!2^{k}}$ (where $\left.n=2 k\right)^{2}$. If this goes too fast, no worries, arguments of this sort will be discussed extensively this semester. But make sure that you understand that $\prod_{i=1}^{k}(2 i-1)=\frac{n!}{k!2^{k}}$. Checking the number of perfect matchings for small (even) values of $n$ we find for $n=0$ that (the empty product) $1=\frac{0!}{0!2^{0}}$ (corresponding to the single empty perfect matching on the empty set), for $n=2$ that (the product consisting of the first single odd number) $1=\frac{2!}{1!2^{1}}$ (corresponding to the single pair among the two elements of a set of cardinality two), for $n=4$ that (the product of the first two odd numbers) $3=\frac{4!}{2!2^{2}}$ (corresponding to the three possible perfect matchings on a set of cardinality four: with $T=\{$ Andrea, Bobbie, Charlie, Drew $\}$, the three perfect matchings are $\{($ Andrea, Bobbie), (Charlie, Drew) $\},\{($ Andrea, Charlie), (Bobbie, Drew) $\}$, and $\{($ Andrea, Drew),(Bobbie, Charlie)\}). Check for yourself that (the product of the first three odd numbers) $15=\frac{6!}{3!2^{3}}$ is indeed the number of perfect matchings on a set of cardinality $n=6$.[^1](2b) Stability. Consider the example $T=\{$ Andrea, Bobbie, Charlie, Drew $\}$ and the perfect matching $\{($ Andrea, Bobbie),(Charlie, Drew) $\}$. With everyone in $T$ paired up, there should be no reason for concern. But if Bobbie would prefer to be paired up with Charlie rather than with Andrea and if at the same time Charlie would prefer Bobbie to Drew, nothing prevents Bobbie and Charlie from running off together and forming a pair - leaving unpaired Andrea and unpaired Drew behind, who now have no other choice than to pair up with each other: thus if indeed Bobbie and Charlie feel this way, the perfect matching $\{($ Andrea, Bobbie), (Charlie, Drew) $\}$ is not perfect in the sense that it is not stable and will "naturally" evolve into the perfect matching $\{($ Andrea, Drew), (Bobbie, Charlie) $\}$. Thus we say that a perfect matching is unstable if there are $\mathbf{t w o}^{3}$ elements that are not paired to each other (Bobbie and Charlie in the example) that prefer each other to the elements that they are paired to: said differently, there are two pairs $(x, y),(v, w)$ in the perfect matching such that $y$ prefers $v$ to $x$ while at the same time $v$ prefers $y$ to $w$.

A stable perfect matching is a perfect matching that is not unstable. This definition requires a notion of "preference" that we have, so far, conveniently glossed over because it is intuitively clear what is meant: it can quite easily be formalized by assuming that each element $x$ of the underlying set $S$ (or $T$ in the example) has an ordered list $L_{x}$ containing all other elements of $S$ and by saying that $x \in S$ prefers $y$ to $z$ if $y$ comes before $z$ on $L_{x}$. Below these lists are referred to as preference lists.

The natural question that arises is whether or not, given $n$ preference lists (namely, a preference list for each of the $n$ elements of $S$ ), a stable perfect matching exists and, if so, how it can efficiently be found. To answer the first question, assume that in our example $T=\{$ Andrea, Bobbie, Charlie, Drew $\}$ we have the following preference lists:

$$
\begin{aligned}
L_{\text {Andrea }} & =(\text { Bobbie }, \text { Charlie }, \text { Drew }) \\
L_{\text {Bobbie }} & =(\text { Charlie }, \text { Andrea }, \text { Drew })
\end{aligned}
$$

and

$$
L_{\text {Charlie }}=(\text { Andrea, Bobbie }, \text { Drew })
$$

with $L_{\text {Drew }}$ left unspecified. We have already seen that the first perfect matching

$\{($ Andrea, Bobbie), (Charlie, Drew) $\}$

is unstable (because Charlie comes before Andrea on $L_{\text {Bobbie }}$ and Bobbie comes before Drew on $\left.L_{\text {Charlie }}\right)$ and gets replaced by a second perfect matching

$$
\{(\text { Andrea, Drew), (Bobbie, Charlie })\} \text {. }
$$

For this new perfect matching we find that Charlie prefers Andrea to its current partner Bobbie while Andrea prefers Charlie to its current partner Drew, so this second perfect matching $\{($ Andrea, Drew),(Bobbie, Charlie) $\}$ is unstable too and evolves into a third perfect matching

$$
\{(\text { Andrea, Charlie), (Bobbie, Drew) }\} \text {. }
$$

Now, however, the preference lists tell us that Andrea prefers Bobbie to Charlie and that Bobbie prefers Andrea to Drew, so that the third perfect matching gets replaced by $\{($ Andrea, Bobbie), (Charlie, Drew) $\}$, which is our first - and unstable - perfect matching again and thus brings us back to our starting point. Because there are only three perfect matchings for $n=4$, there is no other possibility, and all perfect matchings are unstable: Andrea, Bobbie, Charlie, and Drew will keep moving around.

It can be argued that there are situations where the lack of a stable perfect matching could be undesirable, and one may wonder if anything can be done to make[^2]sure that no matter what the preference lists look like, a stable perfect matching exists.

(3) Existence of stable perfect matching. To answer the above question, something can indeed be done. It turns out that allowing anyone to pair up with anyone else (as done in the example above) is too liberal: to guarantee the existence of a stable perfect matching it suffices to define - and enforce - a more stringent pairing rule. A stricter pairing rule that would work consists of first partitioning the set $S$ with $|S|=n=2 k$ into two disjoint subsets $S_{1}$ and $S_{2}$ with $S_{1} \cup S_{2}=S$ and $\left|S_{1}\right|=\left|S_{2}\right|$ (and thus $\left|S_{1}\right|=\left|S_{2}\right|=k$ ) and then to allow only pairs between members of $S_{1}$ and members of $S_{2}$ (cf. bipartite graphs in the book).

For $n=2$ this changes nothing (the single stable pair that already existed under the liberal ruling still exists under the stricter one). But for $n \geq 4$ it makes a considerable difference, which we show by considering all possible choices of $T_{1}$ and $T_{2}$ for our earlier example $T=\{$ Andrea, Bobbie, Charlie, Drew $\}$ where the preference lists

$$
\begin{gathered}
L_{\text {Andrea }}=(\text { Bobbie }, \text { Charlie }, \text { Drew }) \\
L_{\text {Bobbie }}=(\text { Charlie }, \text { Andrea, Drew }) \\
L_{\text {Charlie }}=(\text { Andrea }, \text { Bobbie }, \text { Drew })
\end{gathered}
$$

made it impossible to find a stable perfect matching. Note that we may assume that Andrea $\in T_{1}$. There are three possibilities for the other member of $T_{1}$ :

- $T_{1}=\{$ Andrea, Bobbie $\}$ : Given that Andrea and Bobbie can no longer be paired and that Charlie and Drew can no longer be paired, the preference lists have to be adapted and become

$$
L_{\text {Andrea }}=(\text { Charlie }, \text { Drew }), L_{\text {Bobbie }}=(\text { Charlie }, \text { Drew }), L_{\text {Charlie }}=(\text { Andrea, Bobbie })
$$

(with Drew's preferences still irrelevant). Andrea and Charlie are each others' top choice so $\{($ Andrea, Charlie), (Bobbie, Drew) $\}$ is a stable perfect matching.

- $T_{1}=\{$ Andrea, Charlie $\}:$ Given that Andrea and Charlie can no longer be paired and that Bobbie and Drew can no longer be paired, the adapted preference lists are

$$
L_{\text {Andrea }}=(\text { Bobbie }, \text { Drew }), L_{\text {Bobbie }}=(\text { Charlie }, \text { Andrea }), L_{\text {Charlie }}=(\text { Bobbie }, \text { Drew })
$$

This time Bobbie and Charlie are each others' top choice and the perfect matching $\{($ Andrea, Drew), (Bobbie, Charlie) $\}$ is stable.

- $T_{1}=\{$ Andrea, Drew $\}:$ Given that Andrea and Drew can no longer be paired and that Bobbie and Charlie can no longer be paired, the adapted preference lists are

$$
L_{\text {Andrea }}=(\text { Bobbie }, \text { Charlie }), L_{\text {Bobbie }}=(\text { Andrea, Drew }), L_{\text {Charlie }}=(\text { Andrea, Drew }) .
$$

Andrea and Bobbie are each others' top choice and the perfect matching $\{($ Andrea, Bobbie),(Charlie, Drew) $\}$ is stable.

For the example the stricter pairing rule defused the danger of instability. Convince yourself that for $S_{1}=\{a, b\}, S_{2}=\{d, c\}$ a stable perfect matching consists for all possible combinations of all possible preference lists $L_{a}, L_{b}, L_{c}, L_{d}$ (note that there are two possibilities for $L_{a}$, namely $L_{a}=(c, d)$ or $L_{a}=(d, c)$, etc.).

But does it work in general, i.e., does the stricter rule indeed guarantee that a stable perfect matching always exists? And if a stable perfect matching exists, trying all $k$ ! perfect matchings (why $k!$ ?) until a stable one is found is not an attractive prospect, so how can one be found in an efficient manner?

(4) Constructing a stable perfect matching: the Gale-Shapley algorithm. To answer the existence and efficient construction questions in the previous paragraph, we first show an efficient construction method of a particular perfect matching, and then prove that the perfect matching that was constructed is stable. The construction can be regarded as a "greedy algorithm" (cf. book), because the construction is based on making choices that intuitively look like the "best" ones; indeed it turns out that they are best (this is not true for all greedy algorithms!).

```
Let $M$ be the set of pairs under construction; initially $M=\emptyset$

Let $S_{1}$ and $S_{2}$ be as above with $\left|S_{1}\right|=\left|S_{2}\right|=k$

For any $z \in S_{1} \cup S_{2}$ let $L_{z}$ be the preference list of $z$

    As long as $|M|<k$ do the following:

        Let $x \in S_{1}$ be unpaired and let $x$ propose to the first element $y \in S_{2}$ on $L_{x}$ :

        If $y$ is unpaired then add the pair $(x, y)$ to $M$

        else (if $y$ is paired already)

        Let $(\tilde{x}, y) \in M$

        If $\tilde{x}$ comes before $x$ on $L_{y}$ then remove $y$ from $L_{x}$ else $\left(x\right.$ comes before $\tilde{x}$ on $\left.L_{y}\right)$

        Replace $(\tilde{x}, y) \in M$ by $(x, y)$ and remove $y$ from $L_{\tilde{x}}$
```

(5a) Sketch of termination proof. Because $|M|<k$ implies the existence of an unpaired $x \in S_{1}$, and the latter existence implies that there is a $y \in S_{2}$ that is unpaired, this $y$ cannot have been removed from $L_{x}$, so that "the first element on $L_{x}$ " indeed exists and the construction does not get stuck. Each time that the block after "As long as $|M|<k$ do the following:" is executed, $|M|$ is increased by one or $|M|$ remains the same (though $M$ may change) and a member is removed from a preference list of an element of $S_{1}$. The latter can overall be done fewer than $k^{2}$ times, the former at most $k$ times, so that the entire block is executed fewer than $k+k^{2}$ times. Because execution of a block consists of a small constant number of steps, the overall number of steps is at most on the order of a small constant times $k^{2}$ (which is considered to be "efficient"). Combined with the fact that the construction does not get stuck, it must terminate under the (only) termination condition, namely that $|M| \geq k$, which implies that $|M|=k$ so that $M$ is a perfect matching.

(5b) Sketch of stability proof. To prove that the resulting perfect matching $M$ is stable, assume that $M$ is not stable by assuming there exist $(x, y),(\tilde{x}, \tilde{y}) \in M$ with $x, \tilde{x} \in S_{1}$ and $y, \tilde{y} \in S_{2}$ such that

- $\tilde{x}$ preceeds $x$ on $L_{y}$ and
- $y$ preceeds $\tilde{y}$ on the original $L_{\tilde{x}}$.

From the latter it follows that $\tilde{x}$ proposes to $y$ before proposing to $\tilde{y}$. If $y$ was not paired (when $\tilde{x}$ proposed to $y$ ) then the pair $(\tilde{x}, y)$ would have been added to $M$ and would later never have been replaced by $(x, y)$ because $\tilde{x}$ preceeds $x$ on $L_{y}$. Thus $y$ must have been paired already (when $\tilde{x}$ proposed to $y$ ), say to $\widehat{x} \in S_{1}$, so $(\widehat{x}, y) \in M$. If $\widehat{x}$ preceeds $\tilde{x}$ and thus $x$ on $L_{y}$, then $(\widehat{x}, y) \in M$ would never have been replaced by $(x, y)$ because $\widehat{x}$ preceeds $x$ on $L_{y}$. But also if $\tilde{x}$ preceeds $\widehat{x}$ on $L_{y}$ so that, when $\tilde{x}$ proposes to $y$, the pair $(\hat{x}, y) \in M$ is replaced by the pair $(\tilde{x}, y)$, the new pair $(\tilde{x}, y) \in M$ would never have been replaced ultimately by $(x, y)$ (again because $\tilde{x}$ preceeds $x$ on $L_{y}$ ). All possible cases lead to a contradiction, so the original assumption of instability must be incorrect, and we conclude that $M$ is a stable perfect matching.

Thus it was shown that a stable perfect matching always exists by first constructing a perfect matching in a particular way and by using the specific properties of the construction method to show that the resulting perfect matching is stable.

(6) Additional properties of the construction. With a bit more effort (than in the gray part above) it can be shown that if $(x, y)$ with $x \in S_{1}$ and $y \in S_{2}$ is in the stable perfect matching as constructed using the above method, then there is no stable perfect matching that contains a pair $(x, \widehat{y})$ for which $\widehat{y}$ preceeds $y$ on the original $L_{x}$. Said differently: the resulting stable perfect matching is $S_{1}$ optimal, because no element of $S_{1}$ can "do better" for any other stable perfect matching (based on the same original preference lists). Similarly, the resulting stable matching is $S_{2}$-pessimal: no element of $S_{2}$ can "do worse" for any other stable perfect matching (based on the same original preference lists).

The construction is thus best possible for the part of $S$ that "actively" makes the proposals ( $S_{1}$ in the description above), whereas for the part of $S$ that "passively" waits for things to happen ( $S_{2}$ in the description above) the method is worst possible.

(7) Examples. Assume that $k=4$, that $S_{1}=\left\{x_{1}, x_{2}, x_{3}, x_{4}\right\}, S_{2}=\left\{y_{1}, y_{2}, y_{3}, y_{4}\right\}$, that all $x \in S_{1}$ have the same preference list $L_{x}=\left(y_{1}, y_{2}, y_{3}, y_{4}\right)$, and that $L_{y_{1}}=\left(x_{2}, x_{1}, x_{3}, x_{4}\right), L_{y_{2}}=\left(x_{4}, x_{3}, x_{2}, x_{1}\right), L_{y_{3}}=\left(x_{2}, x_{3}, x_{4}, x_{1}\right)$ and $L_{y_{4}}=$ $\left(x_{4}, x_{1}, x_{2}, x_{3}\right)$. Assume furthermore that the method always selects the unmatched $x \in S_{1}$ with the lowest index. During the construction the following steps are performed (the updates of the preference lists are not given but can easily be inferred):

$\mathrm{x} 1$ proposes y1: y1 accepts x1's proposal

x2 proposes y1: y1 dumps current x1 and accepts x2's proposal

$\mathrm{x} 1$ proposes y2: y2 accepts $\mathrm{x} 1$ 's proposal

x3 proposes y1 but y1 prefers current x2 to x3

x3 proposes y2: y2 dumps current x1 and accepts x3's proposal

x1 proposes y3: y3 accepts x1's proposal

x4 proposes y1 but y1 prefers current x2 to x4

x4 proposes y2: y2 dumps current x3 and accepts x4's proposal

x3 proposes y3: y3 dumps current x1 and accepts x3's proposal

x1 proposes y4: y4 accepts x1's proposal

resulting stable perfect matching: (x1,y4) (x2,y1) (x3,y3) (x4,y2)

This matching is $S_{1}$-optimal and $S_{2}$-pessimal. To find the stable perfect matching that is $S_{2}$-optimal and $S_{1}$-pessimal, we swap the roles of $S_{1}$ and $S_{2}$, and run the construction method again. As a result the following steps are performed:

y1 proposes x2: x2 accepts y1's proposal

y2 proposes x4: x4 accepts y2's proposal

y3 proposes x2 but x2 prefers current y1 to y3

y3 proposes x3: x3 accepts y3's proposal

y4 proposes x4 but x4 prefers current y2 to y4

y4 proposes x1: x1 accepts y4's proposal

resulting stable perfect matching: (y1,x2) (y2,x4) (y3,x3) (y4,x1)

This is the same matching as found before: apparently neither the elements of $S_{1}$ nor the elements of $S_{2}$ can do better or worse in another stable perfect matching, so the stable perfect matching is unique.

There will be more examples in this week's exercises.

Final remarks. With this beautiful result about the existence of stable perfect matchings, why does the application to marriages not seem to work?

Check the moodle page to see how to prepare yourself for Friday's lecture.


[^0]:    ${ }^{1}$ We quickly discussed why a set $L$ of $|L|$ elements has $2^{|L|}$ subsets: there are $2^{|L|}$ different bitstrings of length $|L|$ and there is a bijection between these bitstrings and the set of subsets of $L$ where the $i$-th bit in a bitstring is "on" if and only if the $i$-th element of $L$ is in the subset. Under this bijection the zero-bitstring thus corresponds to the empty subset and the "all-one" bitstring corresponds to the subset $L$ of $L$. If this is puzzling, nothing to worry about, it will be discussed again later.

[^1]:    ${ }^{2}$ Quickly: each of the $n$ ! permutations of $n$ elements specifies a perfect matching (by interpreting the list of $n$ elements as a list of $k$ pairs), but the orders among the $k$ pairs must be divided out (thus dividing by $k!$ ) and the order in each pair is insignificant (dividing by two for each pair, does overall dividing by $\left.2^{k}\right)$.

[^2]:    ${ }^{3}$ Note that a single person that is unhappy is not enough for instability.

