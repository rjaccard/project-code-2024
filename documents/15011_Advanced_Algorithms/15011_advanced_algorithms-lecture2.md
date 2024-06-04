## Matroid Intersection and Bipartite Matchings

## 1 Recall: Matroids and Greedy

We start by recalling the main points from last lecture: definition of matroids which is exactly the structures for which GREEDY works.

Definition 1: A matroid $\mathcal{M}=(E, \mathcal{I})^{2}$ is defined on a finite ground set $E$ and a family $\mathcal{I}$ of subsets of $E$ that are called independent sets satisfying two axioms:

(I $\left.I_{1}\right)$ if $X \subseteq Y$ and $Y \in \mathcal{I}$ then $X \in \mathcal{I}$.

(I $\left.I_{2}\right)$ if $X \in \mathcal{I}$ and $Y \in \mathcal{I}$ and $|Y|>|X|$ then $\exists e \in Y \backslash X: X \cup\{e\} \in \mathcal{I}$.

## Remarks:

- The family $\mathcal{I}$ may be exponential in the size of the ground set $E$ (as is the case for example for graphic matroids of complete graphs). One therefore often assumes that $\mathcal{I}$ is given implicitly by having a membership/independence oracle: an algorithm that given $I \subseteq E$ efficiently answers whether $I \in \mathcal{I}$.
- The second axiom implies that every maximal independent set is of maximum cardinality. In other words, all maximal independent sets have the same cardinality. A maximal cardinality set is called a base of the matroid.

With the more abstract notation of matroids, the basic greedy algorithm becomes

```
$\operatorname{Greedy}(\mathcal{M}, w)$ :
Input: A matroid $\mathcal{M}=(E, \mathcal{I})$ and weights $\left(w_{e}\right)_{e \in E}$.
Output: A maximum weight base $S$.
1. Sort and relabel the elements so that $w_{1} \geq w_{2} \geq \cdots \geq w_{|E|}$.
2. $S \leftarrow \emptyset$.
3. for $i=1$ to $|E|$ :
4. $\quad$ if $S+i \in \mathcal{I}$ then $S \leftarrow S+i$.
5. return $S$.
```

The concept of matroids was defined so as to enable the correctness analysis of the basic greedy algorithm. Perhaps more surprisingly, it is if and only if.[^0]

Theorem 2 : For any ground set $E=\{1,2, \ldots, n\}$, and a family of subsets $\mathcal{I}$, Greedy finds a maximum weight base for any set of weights $w: E \rightarrow \mathbb{R}$ if and only if $\mathcal{M}=(E, \mathcal{I})$ is a matroid.

In the last lecture, we saw some examples of matroids ( $k$-Uniform matroids, partition matroids, linear matroids) and you will see more in tomorrows exercise session.

## 2 Matroid Intersection

Although the concept of matroids forms a rich set of problems that can be solved by the greedy algorithm, there are many problems that have efficient algorithms but are not matroids. Consider for example the bipartite matching problem:

Definition 3 : Given a bipartite graph $G=(V, E)$, find a matching of maximum size.

Recall that a matching $M \subseteq E$ is a subset of edges so that every vertex is incident to at most one edge of $M$, i.e., $|\{e \in M: v \in e\}| \leq 1$ for all $v \in V$.

Example 1 : The edges $(1,4)$ and $(3,5)$ form a matching (of maximum cardinality).

Let's see if GREEDY works for maximum cardinality (or max weight) bipartite matching. To do this, we can verify if $(E, \mathcal{I})$ is a matroid where

$$
\mathcal{I}=\{M \subseteq E: M \text { is a matching }\}
$$

It is easy to see that $(E, \mathcal{I})$ satisfies the downward closed property $\left(I_{1}\right)$ of matroids since a subset of a matching is still a matching. However, the second axiom $\left(I_{2}\right)$ is not satisfied which can be seen by taking the two matchings $M_{1}=\{(1,4),(3,5)\}$ and $M_{2}=\{(3,4)\}$ : although $\left|M_{1}\right|>\left|M_{2}\right|$ there is no edge in $M_{1}$ that we can add to $M_{2}$ while maintaining that it is a matching.

This is kind of sad: matroids and simple Greedy have their limits. On the other hand, we know from our undergraduate algorithm course that there are efficient algorithms for the bipartite matching problem. That there are efficient algorithms for the bipartite matching problem is in fact part of a more general phenomena: it can be described as the intersection of two matroids and any such problem has an efficient algorithm!

Definition 4 : Given two matroids $\mathcal{M}_{1}=\left(E, \mathcal{I}_{1}\right)$ and $\mathcal{M}_{2}=\left(E, \mathcal{I}_{2}\right)$ on the same ground set $E$, their intersection is

$$
\mathcal{M}_{1} \cap \mathcal{M}_{2}=\left(E, \mathcal{I}_{1} \cap \mathcal{I}_{2}\right)
$$

Note that the intersection of two matroids satisfy $\left(I_{1}\right)$ but not typically $\left(I_{2}\right)$. The following adds a lot of power to the concepts of matroids:

Theorem 5 (Edmonds, Lawler, 70's): There is an efficient algorithm for finding a max-weight independent set in the intersection of two matroids. ${ }^{3}$[^1]

The algorithm that gives the above result is quite technical and notation heavy. Instead of describing it in its full generality, we first see how we can apply the above result to obtain several interesting algorithmic applications. We then develop an algorithm for the special case of the bipartite matching problem that share several similarities with the general algorithm.

### 2.1 Examples

### 2.1.1 Bipartite Matching

We already mentioned that the bipartite matching problem is an example of matroid intersection. To see this, consider a bipartite graph $G=(V, E)$ with bipartition $(A, B)$, i.e., the vertices $V$ are partitioned into two disjoint sets $A$ and $B$ such that every edge is between a vertex in $A$ and a vertex in $B$.

Let $\mathcal{M}_{A}$ be a partition matroid with ground set $E$ where the partition $E$ is given by $E=\bigcup\{\delta(v)$ : $v \in A\}$ where $\delta(v)$ denotes the edges incident to $v$. Notice that this is a partition since all edges have precisely one endpoint in $A$. We also define $k_{v}=1$ for every $v \in A$. Thus, the family of independent sets of $M_{A}$ is given by

$$
\mathcal{I}_{A}=\{F \subseteq E:|F \cap \delta(v)| \leq 1 \text { for all } v \in A\}
$$

In other words, a set of edges is independent for $\mathcal{M}_{A}$ if it has at most one edge incident to every vertex of $A$ (and any number of edges incident to every vertex of $B$ ). We can similarly define $\mathcal{M}_{B}=\left(E, \mathcal{I}_{B}\right)$ by

$$
\mathcal{I}_{B}=\{F \subseteq E:|F \cap \delta(v)| \leq 1 \text { for all } v \in B\}
$$

Now observe that any $F \in \mathcal{I}_{A} \cap \mathcal{I}_{B}$ corresponds to a matching in $G$, and vice versa. And the largest common independent set $\mathcal{I}_{A}$ and $\mathcal{I}_{B}$ corresponds to a maximum matching in $G$.

### 2.1.2 Colorful Spanning Trees

Suppose we have an undirected graph $G=(V, E)$ and every edge has a color. This is represented by a partition of $E$ into $E_{1} \cup E_{2} \cup \cdots \cup E_{k}$ where each $E_{i}$ represents a set of edges of the same color $i$. The problem of deciding whether this graph has a spanning tree in which all edges have a different color can be tackled through matroid intersection. Such a spanning tree is called colorful. Colorful spanning trees are bases of the graphic matroid $\mathcal{M}_{1}=\left(E, \mathcal{I}_{1}\right)$ of $G$ which are also independent in the partition matroid $\mathcal{M}_{2}=\left(E, \mathcal{I}_{2}\right)$ defined by $\mathcal{I}_{2}=\left\{F \subseteq E:\left|F \cap E_{i}\right| \leq 1\right.$ for all $\left.i\right\}$.

### 2.1.3 Arborescences

Given a directed graph $D=(V, A)$ and a special root vertex $r \in V$, an r-arborescence (or just arborescence) is a spanning tree (when viewed as an undirected graph) directed away from $r$. Thus, in a $r$-arborescence, every vertex is reachable from the root $r$. As an $r$-arborescence has no arc incoming to the root, we assume that $D$ has no such arc.

r-arborescences can be viewed as sets simultaneously independent in two matroids. Let $G$ denote the undirected counterpart of $D$ obtained by disregarding the directions of the arcs. Note that if we have both $\operatorname{arcs} a_{1}=(u, v)$ and $a_{2}=(v, u)$ in $D$ then we get two undirected edges also labeled $a_{1}$ and $a_{2}$ between $u$ and $v$ in $G$. Define $\mathcal{M}_{1}=\left(A, \mathcal{I}_{1}\right)$ the graphic matroid corresponding to $G$, and $\mathcal{M}_{2}=\left(A, \mathcal{I}_{2}\right)$ the partition matroid in which independent sets are those with at most one arc incoming to every vertex $v \neq r$. In other words, we let

$$
\mathcal{I}_{2}=\left\{F:\left|F \cap \delta^{-}(v)\right| \leq 1 \text { for all } v \in V \backslash\{r\}\right\}
$$

where $\delta^{-}(v)$ denotes the set $\{(u, v) \in A\}$ of arcs incoming to $v$. Thus, any $r$-arborescence is independent in both matroids $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$. Conversely, any set $T$ independent in both $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$ and of cardinality $|V|-1$ (so that it is a base in both matroids) is an $r$-arborescence. Indeed, such a $T$ being a spanning tree in $G$ has a unique path between $r$ and any vertex $v$; this path must be directed from the root $r$ since otherwise we would have either an arc incoming to $r$ or two arcs incoming to the same vertex.

## 3 Algorithm for Maximum Cardinality Bipartite Matching

### 3.1 Duality

Before giving an algorithm, perhaps an easier question is: how would you give a short proof that a given matching is optimal?

For this purpose, one would like to find upper bounds on the size of the largest matching and hope that the smallest of these upper bounds be equal to the size of the largest matching. This is a duality concept that will be very important in this subject. In this case, the dual problem will be a famous combinatorial optimization problem: vertex cover.

Vertex cover: A vertex cover is a set $C$ of vertices so that all edges $e$ of $E$ are incident to at least one edge in $C$. In other words, there is no edge completely contained in $V \backslash C$.

We clearly have the following:

$$
|M| \leq|C| \quad \text { for any matching } M \text { and vertex cover } C \text {. }
$$

This follows from the fact that, given any matching $M$, a vertex cover $C$ must contain at least one of the end points of each edge in $M$.

This is weak duality: The maximum size of a matching is at most the minimum size of a vertex cover. We shall in fact prove strong duality (that equality holds) for bipartite graphs:

Theorem 6 (König 1931) : For any bipartite graph, the maximum size of a matching is equal to the minimum size of a vertex cover.

The proof of this theorem will be algorithmic. It will give an efficient algorithm for both finding a maximum size matching and a minimum size vertex cover of a bipartite graph. Note that whenever one has min max statement as above, the problem lies in $N P \cap \operatorname{coNP}$ which may indicate that it has an efficient algorithm ${ }^{4}$.[^2]

### 3.2 Algorithm

Recall that a path is a collection of edges $\left(v_{0}, v_{1}\right),\left(v_{1}, v_{2}\right), \ldots,\left(v_{k-1}, v_{k}\right)$ where the $v_{i}$ 's are distinct vertices. We can simply represent a path as $v_{0}-v_{1}-v_{2}-\ldots-v_{k}$.

Definition 7 (Alternating path) An alternating path with respect to $M$ is a path that alternates between edges in $M$ and edges in $E \backslash M$.

Definition 8 (Augmenting path) An augmenting path with respect to $M$ is an alternating path in which the first and last vertices are unmatched.

The definition of an augmenting path motivates the following algorithm:

AUGMENTINGPATHALGORITHM $(G)$ :

Input: A bipartite graph $G=(V, E)$.

Output: A matching $M$ of maximum cardinality.

1. Initialize $M=\emptyset$.
2. while exists an augmenting path $P$
3. update $M=M \Delta P \equiv(M \backslash P) \cup(P \backslash M)$.
4. return $M$.

Exercise 1 Devise an efficient algorithm for finding an augmenting path $P$ (if one exists). What is the total running time of the AUGMENTingPAthAlgorithm?

We now prove that AugmentingPathAlgorithm indeed finds a maximum matching.

Theorem 9 A matching $M$ is maximum if and only if there are no augmenting paths with respect to $M$.

Proof (By contradiction)

$(\Rightarrow)$ Let $P$ be some augmenting path with respect to $M$. Then $M^{\prime}=M \Delta P$ is matching of greater cardinality than $M$. This contradicts the optimality of $M$.

$(\Leftarrow)$ If $M$ is not maximum, let $M^{*}$ be a maximum matching so that $\left|M^{*}\right|>|M|$. Let $Q=M \Delta M^{*}$. Then

- $Q$ has more edges from $M^{*}$ than from $M$ (since $\left|M^{*}\right|>|M|$ implies that $\left|M^{*} \backslash M\right|>\left|M \backslash M^{*}\right|$ ).
- Each vertex is incident to at most one edge in $M \cap Q$ and one edge in $M^{*} \cap Q$.
- Thus $Q$ is composed of cycles and paths that alternate between edges from $M$ and $M^{*}$.
- Therefore there must be some path with more edges from $M^{*}$ in it than from $M$. This path is an augmenting path with respect to $M$.

Hence, there must exist an augmenting path $P$ with respect to $M$, which is a contradiction.

### 3.3 Proof of König's Theorem

Consider a maximum matching $M^{*}$ of $G=(A \cup B, E)$. Let $L$ the vertices reachable from unmatched vertices in $A$ by alternating paths with respect to $M^{*}$. (So e.g. in the figure of Example $3 L=\{4,8,3\}$.) The following proves König's theorem.

Lemma 10 We have that $C^{*}=(A \backslash L) \cup(B \cap L)$ is a vertex cover. Moreover, $\left|C^{*}\right|=\left|M^{*}\right|$.

Proof We first show that $C^{*}$ is a vertex cover. Suppose toward contradiction that it is not. Then there is an edge $e=(a, b) \in E$ with $a \in A \cap L$ and $b \in B \backslash L$. The edge cannot belong to the matching. If it did then $b$ should be in $L$ because otherwise $a$ would not be in $L$. Hence $e \in E \backslash M$. This however, implies that there is an alternating path from an unmatched vertex to $b$ (namely go to $a$ and take the edge $(a, b))$ contradicting the fact that $b \notin L)$.

To show the second part of the proof, we show that $\left|C^{*}\right| \leq\left|M^{*}\right|$, since the reverse inequality is true for any matching and any vertex cover. The proof follows from the following observations:

1. No vertex in $A \backslash L$ is unmatched by the definition of $L$;
2. No vertex in $B \cap L$ is unmatched since this would imply the existence of an augmenting path (which contradicts that $M^{*}$ is optimal).
3. There is no edge of the matching between a vertex $a \in A \backslash L$ and a vertex $b \in B \cap L$. Otherwise $a$ would be in $L$.

These remarks imply that every vertex in $C^{*}$ is matched and moreover the corresponding edges of the matching are distinct. Hence, $\left|C^{*}\right| \leq\left|M^{*}\right|$


[^0]:    ${ }^{1}$ Disclaimer: These notes were written as notes for the lecturer. They have not been peer-reviewed and may contain inconsistent notation, typos, and omit citations of relevant works.

    ${ }^{2}$ In these notes, we use $\mathcal{M}$ (instead of $M$ ) for matroids to not confuse them with matchings.

[^1]:    ${ }^{3}$ It is efficient meaning that it is a polynomial-time algorithm if we can, in polynomial time, answer independence queries of the type " $I \in \mathcal{I}_{1}$ ?" and " $I \in \mathcal{I}_{2}$ ?" for the two matroids (which is the case for all examples of matroids seen in class).

[^2]:    ${ }^{4}$ This sentence is hard to understand if you haven't taken a computational complexity course.

