## Graph Sparsification <br> Notes by Michael Kapralov ${ }^{1}$

In this lecture we show how to construct cut sparsifiers of general graphs. More formally, we show how given an unweighted graph $G=(V, E)$, one can construct a weighted graph $G^{\prime}=(V, E, w)$ with $O\left(\frac{1}{\epsilon^{2}} n \log n\right)$ edges such that for every $S \subseteq V$ one has

$$
(1-\epsilon) E(S, V \backslash S) \leq E^{\prime}(S, V \backslash S) \leq(1+\epsilon) E(S, V \backslash S)
$$

with high probability. Here $E(S, V \backslash S)$ stands for the number of edges going from $S$ to $V \backslash S$ in $G$, and $E^{\prime}(S, V \backslash S)$ stands for the total weight of edges going from $S$ to $V \backslash S$ in $G^{\prime}$.

We will construct a graph $G^{\prime}$ such that for every $S \subseteq V$ one has

$$
\begin{equation*}
(1-\epsilon) E(S, V \backslash S) \leq E^{\prime}(S, V \backslash S) \leq(1+\epsilon) E(S, V \backslash S) \tag{*}
\end{equation*}
$$

with high probability.

## 1 Uniform sampling

The argument from previous lecture only applies to the clique, as it is easy to get a good upper bound on the number of cuts of a given size in a clique. A seminal result of Karger [2] shows how to generalize this argument to graphs with a large min-cut. Suppose that $G$ has min-cut $k$ (think of $k$ as large). We now upper bound the number of cuts of size $\alpha k$ for $\alpha \geq 1$ such that $2 \alpha$ is an integer. Run Karger's randomized contraction process for $n-2 \alpha$ steps, and then choose a uniformly random subset of the remaining $2 \alpha$ vertices that contains vertex 1 . The probability that a given cut of size $\alpha k$ survives the contraction process is

$$
\left(1-\frac{2 \alpha}{n}\right) \cdot\left(1-\frac{2 \alpha}{n-1}\right) \cdots\left(1-\frac{2 \alpha}{2 \alpha+1}\right)=\binom{n}{2 \alpha}^{-1}
$$

and the probability that the cut is output conditioned on having survived the contraction process is exactly equal to $2^{1-2 \alpha}$. Thus, the number of cuts of size bounded by $\alpha k$ is at most

$$
\binom{n}{2 \alpha} 2^{2 \alpha-1}
$$

Now to construct a sparsifier of $G$ we include every edge $e \in E$ into $E^{\prime}$ independently with probability $p=\frac{C \log n}{\epsilon^{2} k}$ for a sufficiently large constant $C>0$. We can now take a union bound over cuts of all sizes,[^0]getting

$\operatorname{Pr}[\exists S \subseteq V:(*)$ fails for $(S, V \backslash S)] \leq \sum_{\alpha=2}^{\infty} \operatorname{Pr}[$ a fixed cut of size $\geq(\alpha-1) k$ fails $] \cdot \#($ cuts of size $\leq \alpha k)$

$$
\begin{aligned}
& \leq \sum_{\alpha=2}^{\infty} 2 e^{-\epsilon^{2}(\alpha-1) k p / 3} \cdot\binom{n}{2 \alpha} 2^{2 \alpha-1} \\
& \leq 2 \sum_{\alpha=2}^{\infty} e^{-\epsilon^{2}(\alpha-1) k p / 3} \cdot(2 n)^{2 \alpha} \\
& \leq 2 \sum_{\alpha=2}^{\infty} n^{-(C / 3)(\alpha-1)} \cdot(2 n)^{2 \alpha} \\
& \leq 2 \sum_{\alpha=2}^{\infty} n^{-(C / 6) \alpha} \cdot(2 n)^{2 \alpha} \\
& \leq 1 / n
\end{aligned}
$$

as long as $C$ is a sufficiently large absolute constant.

Exercise 1 Prove that if $G$ is a bipartite clique and $p=o\left(\frac{\log n}{n}\right)$, then $G^{\prime}$ is not a sparsifier of the clique on $n$ vertices with $\epsilon=1 / 2$ with high probability.

## 2 Non-uniform sampling

In the previous section we showed that uniform sampling can be used to obtain a sparsifier with few edges when the min-cut in the graph is large. If the min-cut is small, uniform sampling will not succeed. Indeed, suppose that the input graph $G$ is a union of two disjoint cliques of size $n / 2$ joined by a single edge: any sparsifier must include that edge, but uniform sampling will either lose it or not reduce the number of edges in the cliques. The right approach here is to keep the edge connecting the cliques and sampled edges induced by the cliques, giving sampled edges appropriately large weight, as we did in the previous section. To generalize this idea, we need a convenience definition of 'well-connected' parts of the graph. This is provided by

Definition 1 (Strong connectivity) A k-strongly connected component of a graph $G=(V, E)$ is a maximal induced subgraph that is $k$-edge connected (i.e., with min-cut at least $k$ ). For every edge $e \in E$ the strong connectivity of $k_{e}$ of $e$ is the maximum $k$ such that both endpoints of $e$ belong to a $k$-strongly connected component.

Exercise 2 Prove that for every $k_{1} \leq k_{2}$ and every graph $G=(V, E)$ the collection of $k_{2}$-strongly connected components in $G$ is a refinement of the collection of $k_{1}$-strongly connected components in $G$.

We will let $p_{e}=\min \left\{\frac{r}{k_{e}}, 1\right\}$, where $r=\frac{C \log n}{\epsilon^{2}}$ for a sufficiently large constant $C>0$. Thus, the expected number of edges in the sparsifier will be bounded by

$$
\sum_{e \in E} p_{e}=\sum_{e \in E} \min \left\{\frac{r}{k_{e}}, 1\right\} \leq \sum_{e \in E} \frac{r}{k_{e}}=r \sum_{e \in E} 1 / k_{e}
$$

To bound its size, we prove

Lemma $2 \sum_{e \in E} 1 / k_{e} \leq n-1$.

Proof The proof is by induction. The base case corresponds to $n=1$, in which case the claim trivially holds. Now consider a graph $G$ and a minimum cut $(S, V \backslash S)$ in $G$. Let $k$ denote the number of edges in the min cut. The strong connectivity of every edge in the min-cut is at least $k$, since $G$ is $k$-connected. Thus, the total contribution of edges crossing the cut to the sum is at most $\sum_{e \in \delta(S)} 1 / k_{e} \leq$ $\sum_{e \in \delta(S)} 1 / k=k \cdot 1 / k=1$. On the other hand, we have by the inductive hypothesis

$$
\sum_{e \in E, e \text { induced by } S} 1 / k_{e}^{S} \leq|S|-1 \text { and } \sum_{e \in E, e \text { induced by } V \backslash S} 1 / k_{e}^{V \backslash S} \leq|V \backslash S|-1
$$

where $k_{e}^{S}$ and $k_{e}^{V \backslash S}$ denote strong connectivities in the subgraphs induced by $S$ and $V \backslash S$ respectively. It remains to note that for all $e$ induced by $S$ one has $k_{e}^{S} \leq k_{e}$, and similarly for all $e$ induced by $V \backslash S$ one has $k_{e}^{V \backslash S} \leq k_{e}$, so the above imply

$$
\sum_{e \in E, e \text { induced by } S} 1 / k_{e} \leq|S|-1 \text { and } \sum_{e \in E, e \text { induced by } V \backslash S} 1 / k_{e} \leq|V \backslash S|-1
$$

Putting everything together, we get

$$
\sum_{e \in E} 1 / k_{e} \leq(|S|-1)+(|V \backslash S|-1)+1 \leq|V|-1
$$

as required

We now prove that if $G^{\prime}$ is obtained by including every edge $e \in E$ independently with probability $p_{e}$ (with weight $1 / p_{e}$ if included), then $G^{\prime}$ is a sparsifier of $G$ with high probability, proving the result of [1]. The main challenge is that some edges in $G^{\prime}$ will have very large weights. This means that the random variables corresponding to cut sizes have large variance, and therefore the analysis of the uniform sampling scheme from the previous lecture does not go through. As we will shortly see, this difficulty can be circumvented by a nice decomposition of the graph into layers corresponding to components of different connectivity.

Consider a reweighted graph $G_{w}$, where edges are given weight $k_{e}$ (assume for simplicity that all edges have $\left.p_{e}<1\right)$. Thus, our sampling process is simply the process of including every edge in $G_{w}$ independently with probability $p_{e}$ with its own weight. Let $k_{1}<k_{2}<\ldots<k_{T}$ denote distinct values of edge strengths in $G$ (note that $T \leq m$, where $m$ is the number of edges). For every $t=1, \ldots, T$ let $F_{\geq t}$ denote the set of edges in $G$ whose strength is at least $k_{t}$, and note that

$$
G_{w}=\sum_{t=1}^{T}\left(k_{t}-k_{t-1}\right) F_{\geq t}
$$

where $k_{0}=0$ by convention. To see that the above equality holds, note that the weight of $e$ on the lhs is $k_{e}$, and its weight on the rhs is $\sum_{t=1}^{t^{\prime}}\left(k_{t}-k_{t-1}\right)=k_{e}$, where $t^{\prime}$ is the largest such that $e \in F_{\geq t^{\prime}}$. Now consider a sampling process where if an edge $e \in E$ is included in $G$ (with probability $p_{e}$ ), then it is included in all $F_{\geq t}$ that it belongs to, namely in all $F_{\geq t}$ for $t \geq k_{e}$. The sampling processes in $F_{\geq t}$ are correlated, but the sampling within any given $F_{\geq t}$ is independent, so it is enough to prove that all cuts in all $F_{\geq t}$ 's concentrate around their expectation. In order to show that, we use the following stronger version of the uniform sampling claim proved in the previous section:

Theorem 3 [3] For a graph $G=(V, E)$, if every edge $e \in E$ is included independently with probability $p_{e}$, and the expected number of edges crossing every cut is at least $(C \log n) / \epsilon^{2}$ for a sufficiently large constant $C>0$, then in the resulting graph all cuts are within a $1 \pm \epsilon$ factor of their expectation with probability at least $1-1 / n$.

Its proof is an exercise, given the analysis of our uniform sampling scheme from the previous section. Note that we will be applying Theorem 3 to the $F_{\geq t}$ 's, which is exactly what lets us circumvent the issue of large weights. Now it remains to note that expected sizes of cuts in $F_{\geq t}$ are at least $r$. To verify that, consider any connected component in $F_{\geq t}$, and any cut in this component. Suppose that the number of edges of $G$ crossing this cut is $k^{\prime}$. Then the strong connectivity of all of those edges is at most $k^{\prime}$, so the probability of sampling those edges is at least $r / k^{\prime}$, and therefore the expected number of edges in the cut is at least $r=(C \log n) / \epsilon^{2}$. Thus, the preconditions of Theorem 3 are satisfied, and we get that $G^{\prime}$ is a sparsifier of $G$ with high probability.


[^0]:    ${ }^{1}$ Disclaimer: These notes were written as notes for the lecturer. They have not been peer-reviewed and may contain inconsistent notation, typos, and omit citations of relevant works.

