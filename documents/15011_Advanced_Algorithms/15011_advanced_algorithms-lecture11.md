# Randomized Algorithms (Karger's Min-Cut Algorithm)  

## 1 Introduction to Randomized Algorithms

Deterministic algorithms take input and produce output. In Randomized Algorithms, in addition to input algorithms take a source of random bits and makes random choices during execution - which leads behavior to vary even on a fixed input. For many problems a randomized algorithm is the simplest or fastest or both.

Let $p>0$ be the probability that a (randomized) algorithm generates the correct (optimal) solution. It turns out that, even if $p$ is much smaller than 1 we can obtain an algorithm with that succeeds with high probability just by executing the original algorithm independently many times. In particular, if we run the original algorithm $k$ times, the probability that at least one copy succeeds is at least $1-(1-p)^{k}$. For small values of $p$ one can always approximate $1-p$ with $e^{-p}$, and during this course we always use such an approximation. It follows that for $k=100 / p$, at least one copy finds the correct (optimal) solution with probability at least

$$
1-e^{-p k}=1-e^{-100}
$$

In other words, even if we have an algorithm with a small probability of success we can boost the success probability to a number very close to 1.

In this lecture, we describe a randomized algorithm for the minimum cut problem. Let us start with the definition of minimum cut problem. Let $G=(V, E)$ be a graph with $n=|V|$ vertices. Let

$$
E(S, \bar{S}):=\{(u, v): u \in S, v \notin S\}
$$

be the set of edges that have exactly one endpoint in $S$. In the minimum cut problem, we want to partition the into two subsets which are joined together with minimum number of edges, i.e.,

$$
\min _{\emptyset \subset S \subset V}|E(S, \bar{S})|
$$

## 2 Karger's Algorithm

In this lecture we will discuss Karger's $[$ Kar93] and Karger-Stein's $[\mathbf{K S 9 3}]$ algorithm for the minimum cut problem. We will show that the former finds the minimum cut in time $O\left(n^{4} \log n\right)$ and the latter finds it in time $O\left(n^{2}\right)$ with high probability.

Before describing these algorithms, let us define a contraction procedure. Contraction of an edge $(u, v)$ in $G$, merges the endpoints $u$ and $v$ to create a new (super) node $u v$. This reduces the total number of nodes in the graph by 1 . All other edges which were previously attached to $u$ or $v$ are attached to the new (super) node $u v$. Note that this might lead to multiple parallel edges; in particular, if a node $z$ has $a$ edges to $u$ and $b$ edges to $v$, after contraction it will have $a+b$ edges to $u v$.

When we contract $u, v$ we just remove the edge connecting $u$ to $v$ from the graph; in other words, we do not include the loops.[^0]

Let $k$ be the size of the minimum cut of $G$; fix a minimum cut $\left(S^{*}, \overline{S^{*}}\right)$. In this section we design an algorithm that finds $\left(S^{*}, \overline{S^{*}}\right)$ with probability at least $1 /\binom{n}{2}$.

Let us start by describing the main idea. Suppose we choose a uniformly random edge $e$ in $G$. What is the probability that $e \in E\left(S^{*}, \overline{S^{*}}\right)$ ?

Claim 1 The probability that a uniformly random edge is in $E\left(S^{*}, \overline{S^{*}}\right)$ is at most $2 / n$.

Proof Let $e$ be a uniformly random edge in $G$. Obviously,

$$
\mathbb{P}\left[e \in E\left(S^{*}, \overline{S^{*}}\right)\right]=\frac{\left|E\left(S^{*}, \overline{S^{*}}\right)\right|}{|E|}=\frac{k}{|E|}
$$

To give an upper bound we need to lower bound $|E|$. Here we use the hand-shake lemma. Let $d(v)$ be the degree of a vertex $v$. The hand-shake lemma says that in any graph $G$,

$$
\sum_{v \in V} d(v)=2|E|
$$

This is because in the LHS we count each edge twice. Now, we can lower bound $d(v)$ for any vertex $v$ by $k$. This is because, for any $v$,

$$
d(v)=|E(\{v\}, \overline{\{v\}})| \geq k
$$

In other words, the size of the cut separating $v$ from the rest of the graph is at least $k$. It follows from the above two equations that $|E| \geq n k / 2$. So,

$$
\mathbb{P}\left[e \in E\left(S^{*}, \overline{S^{*}}\right)\right]=\frac{k}{|E|} \leq \frac{k}{n k / 2}=\frac{2}{n}
$$

Using the above lemma if we choose $n / 4$ edges of $G$ uniformly at random with probability $1 / 2$ none of them is in the min-cut $\left(S^{*}, \overline{S^{*}}\right)$. Now, we can contract these $n / 4$ edges. The new graph will have at most $3 n / 4$ vertices and we can recurse. After $O(\log n)$ steps, we get to a graph with just two super nodes. With probability at least $(1 / 2)^{O(\log n)}$ we do not contract any of the edges of $\left(S^{*}, \overline{S^{*}}\right)$ throughout the process. So, the size of the cut separating the final two super-nodes is exactly $k$. In fact, one of these two super-nodes corresponds to $S^{*}$ being contracted and the other one corresponds to $\overline{S^{*}}$.

In above we described the gist of the idea of Karger's algorithm. There are several missing points in the above description. First of all, when we recursively call the algorithm, we are recursively using the above claim. So, we need to make sure the size of the min-cut of $G$ does not decrease when we contract an edge.

Fact 2 For any graph $G$, when we contract an edge $(u, v)$ the size of the minimum cut does not decrease.

We leave the proof of the above fact as an exercise.

Secondly, when we choose $n / 4$ edges uniformly at random many of them may be parallel, so after contraction the number of vertices of $G$ may go down only by 1 . To avoid running into these special cases, it suffices to contract edges one by one. That is, each time we choose a uniformly random edge of $G$ and we contract it.

Theorem 3 For any graph $G=(V, E)$ with $n$ nodes and any min-cut $\left(S^{*}, \overline{S^{*}}\right)$, Algorithm 1 returns $\left(S^{*}, \overline{S^{*}}\right)$ with probability at least $\frac{2}{n(n-1)}$.

Proof Let, $A_{i}$ be the event that the edge picked in step $i$ of the loop is not in $E\left(S^{*}, \overline{S^{*}}\right)$. Observe that the algorithm succeeds in finding $\left(S^{*}, \overline{S^{*}}\right)$ if $A_{1}, A_{2}, \ldots, A_{n-2}$ occur, i.e., if we never contract an edge of $E\left(S^{*}, \overline{S^{*}}\right)$. So, we just need to lower bound $\mathbb{P}\left[A_{1}, A_{2}, \ldots, A_{n-2}\right]$. By Bayes rule we have,

$$
\mathbb{P}\left[A_{1}, \ldots, A_{n-2}\right]=\mathbb{P}\left[A_{1}\right] \mathbb{P}\left[A_{2} \mid A_{1}\right] \mathbb{P}\left[A_{3} \mid A_{1}, A_{2}\right] \ldots \mathbb{P}\left[A_{n-2} \mid A_{1}, A_{2}, \ldots, A_{n-3}\right]
$$

```
Algorithm 1 Karger's Algorithm
    for $i=1 \rightarrow n-2$ do

        Choose a uniformly random edge $(u, v)$ and contract it, i.e., remove $u, v$, add a new node $u v$,
        connect all edges that go to $u$ or $v$ to the new node $u v$, also remove all loops.
end for
Return the number edges between the final two super-nodes as the size of the min-cut.
```

Now, by Theorem 1] and Theorem 2, for all $i$,

$$
\mathbb{P}\left[A_{i} \mid A_{1}, \ldots, A_{i-1}\right] \geq 1-\frac{2}{n-i+1}
$$

Therefore,

$$
\begin{aligned}
\mathbb{P}\left[A_{1}, \ldots, A_{n-2}\right] & \geq\left(1-\frac{2}{n}\right)\left(1-\frac{2}{n-1}\right) \ldots\left(1-\frac{2}{3}\right) \\
& =\frac{n-2}{n} \cdot \frac{n-3}{n-1} \cdot \frac{n-4}{n-2} \cdots \frac{3}{5} \cdot \frac{2}{4} \cdot \frac{1}{3} \\
& =\frac{2}{n(n-1)}=1 /\binom{n}{2} .
\end{aligned}
$$

The following corollary is immediate from the above theorem.

Corollary 4 Any graph has at most $\binom{n}{2}$ min-cuts.

Proof Suppose there is a graph $G$ that has more than $\binom{n}{2}$ min-cuts. Then, for one of those cuts, say $(S, \bar{S})$ the probability that Algorithm 1, finds $(S, \bar{S})$ is less than $1 /\binom{n}{2}$. But, this is a contradiction.

In fact, the above bound is tight: you will give an example showing that it is tight in the exercise session.

Runtime and Boosting Probability of Success. It is not hard to see that one can run Algorithm 1 in time $O\left(n^{2}\right)$, but as we proved above the success probability of each execution is just $O\left(1 / n^{2}\right)$. Using the boosting idea, we can boost the probability of success to $1-1 / n$ by running $O\left(n^{2} \log n\right)$ independent copies of the above algorithm and returning the best cut that any of the copies find.

Note that, running Karger's algorithm $n^{2} \log n$ times produces a min cut with high probability; but this way we have to spend time $O\left(n^{4} \log n\right)$ to find the min-cut. In the next section we describe a much faster algorithm due to Karger and Stein.

## 3 Karger-Stein Algorithm

Recall that Karger's algorithm only fails if it contracts an edge of the min-cut. Also, note that the probability that we contract an edge of the min-cut at the beginning is only $2 / n$ while towards the end of the algorithm this probability goes up to a constant. In particular, in the very last step there is a probability of $1 / 3$ that we contract an edge of the min-cut.

The idea of Karger-Stein algorithm is to run multiple independent copies of the Karger's algorithm when the size of the graphs gets smaller. The idea kind of resembles the idea fault tolerant systems where one stores multiple copies of the data to decrease the probability of failure.

Let us describe Karger-Stein's algorithm.

```
Algorithm 2 Min-cut $(G=(V, E))$
    Let $n=|V|$. If $n=2$ return the unique cut separating the two nodes of $G$.
    for $i=1 \rightarrow n-n / \sqrt{2}$ do
        Choose a uniformly random edge and contract it.
    end for
    Let $G^{\prime}$ be the contracted graph. Call Min-cut $\left(G^{\prime}\right)$ twice and return the best cut that any of these two
    copies find.
```

First, let us calculate the running time. Let $T(n)$ be the time it takes to compute the min-cut of a graph of size $n$. Then,

$$
T(n)=O\left(n^{2}\right)+2 T(n / \sqrt{2})
$$

We can use the master theorem to solve the above recurrence. But, usually it is easier to open it up a couple of times and see the pattern. We can write

$$
\begin{aligned}
T(n) & =O\left(n^{2}\right)+2 O\left(\left(n / 2^{1 / 2}\right)^{2}\right)+4 O\left(\left(n / 2^{1}\right)^{2}\right)+\ldots \\
& =O\left(n^{2}\right)+O\left(n^{2}\right)+O\left(n^{2}\right)+\cdots=O\left(n^{2} \log n\right)
\end{aligned}
$$

Let us divide the work of the algorithm into $O(\log n)$ phases; in the first phase the algorithm goes from $n$ to $n / \sqrt{2}$, in the second phase it goes from $n / \sqrt{2}$ to $n / \sqrt{2}^{2}$ and so on. The number of copies are chosen such that the algorithm spends exactly the same amount of work $O\left(n^{2}\right)$ in each phase.

It remains the calculate the probability of success. In the next theorem we show that the algorithm succeeds with probability $\Omega(1 / \log n)$. This shows that to boost the probability of success to $1-1 / n$ it is enough to run $\log ^{2} n$ independent copies of the above algorithm. Therefore, the algorithm finds a min-cut with probability $1-1 / n$ in time $O\left(n^{2} \log ^{3} n\right)$.

Theorem 5 Algorithm 2 finds a min-cut with probability at least $1 /(2 \log n)$.

Proof Suppose we call Min-cut function from some graph $H$ (which is a contracted $G$ ) with $r$ vertices and let $\left(S^{*}, \overline{S^{*}}\right)$ be a min-cut of $H$. By an analysis similar to Theorem 3 , the probability that the we do not contract any edge of $\left(S^{*}, \overline{S^{*}}\right)$ in the $r-r / \sqrt{2}$ steps of the loop is at least

$$
\frac{r-2}{r} \cdot \frac{r-3}{r-1} \ldots \frac{r / \sqrt{2}-2}{r / \sqrt{2}} \approx \frac{(r / \sqrt{2})^{2}}{r^{2}}=1 / 2
$$

The algorithm is guaranteed in finding a min-cut if Min-cut $(G)$ does not contract an edge of $\left(S^{*}, \overline{S^{*}}\right)$ in its for loop and at least one of the two copies succeeds in finding the cut. We prove inductively that for any graph with $n$ vertices the probability of success is at least $1 /(2 \log n)$. Assuming by induction hypothesis, that the algorithm succeeds on $G^{\prime}$ with probability at least $p \geq 1 /(2 \log (n / \sqrt{2}))$. Here the logs are all in base 2 .

The probability that the algorithm succeeds in $G$ is at least

$$
\frac{1}{2}\left(p+p-p^{2}\right)
$$

Note that $p+p-p^{2}$ is the probability that at least one of the two copies succeed in finding the cut. The term $p^{2}$ is the probability that both copies succeed (because they are independent); we need to subtract this quantity because it is counted twice. So, it is enough to show that

$$
\frac{1}{2}\left(p+p-p^{2}\right)=p-p^{2} / 2 \geq \frac{1}{2 \log n}
$$

In the worst case we have $p=1 /(2 \log (n / \sqrt{2}))$. So, we need to show

$$
\frac{1}{2 \log (n / \sqrt{2})}-\frac{1}{8 \log (n / \sqrt{2})^{2}} \geq \frac{1}{2 \log n}
$$

Equivalently, it is enough to show

$$
\frac{1}{\log (n / \sqrt{2})}-\frac{1}{\log n} \geq \frac{1}{4 \log (n / \sqrt{2})^{2}}
$$

But,

$$
\frac{1}{\log (n / \sqrt{2})}-\frac{1}{\log n}=\frac{\log n-\log (n / \sqrt{2})}{\log n \log (n / \sqrt{2})}=\frac{1 / 2}{\log n \log (n / \sqrt{2})} \geq \frac{1}{4 \log (n / \sqrt{2})^{2}}
$$

as desired.


[^0]:    ${ }^{1}$ Disclaimer: These notes were written as notes for the lecturer. They have not been peer-reviewed and may contain inconsistent notation, typos, and omit citations of relevant works.

