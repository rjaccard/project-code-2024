##  Matchings, Intro to Linear Programming \$

## 1 Algorithm for Maximum Cardinality Bipartite Matching

Recall the (unweighted) bipartite matching problem:

Definition 1 Given a bipartite graph $G=(V, E)$, find a matching of maximum size.

Recall that a matching $M \subseteq E$ is a subset of edges so that every vertex is incident to at most one edge of $M$, i.e., $|\{e \in M: v \in \bar{e}\}| \leq 1$ for all $v \in V$.

Also recall that a path is a collection of edges $\left(v_{0}, v_{1}\right),\left(v_{1}, v_{2}\right), \ldots,\left(v_{k-1}, v_{k}\right)$ where the $v_{i}$ 's are distinct vertices. We can simply represent a path as $v_{0}-v_{1}-v_{2}-\ldots-v_{k}$.

Definition 2 (Alternating path) An alternating path with respect to $M$ is a path that alternates between edges in $M$ and edges in $E \backslash M$.

Definition 3 (Augmenting path) An augmenting path with respect to $M$ is an alternating path in which the first and last vertices are unmatched.

The definition of an augmenting path motivates the following algorithm:[^0]

```
AUGMENTINGPATHALGORIthm $(G)$ :
Input: A bipartite graph $G=(V, E)$.
Output: A matching $M$ of maximum cardinality.
1. Initialize $M=\emptyset$.
2. while exists an augmenting path $P$
3. $\quad$ update $M=M \Delta P \equiv(M \backslash P) \cup(P \backslash M)$.
4. return $M$.
```

We now prove that AugmentingPathAlgorithm indeed finds a maximum matching.

Theorem 4 A matching $M$ is maximum if and only if there are no augmenting paths with respect to $M$.

Proof (By contradiction)

$(\Rightarrow)$ Let $P$ be some augmenting path with respect to $M$. Then $M^{\prime}=M \Delta P$ is matching of greater cardinality than $M$. This contradicts the optimality of $M$.

$(\Leftarrow)$ If $M$ is not maximum, let $M^{*}$ be a maximum matching so that $\left|M^{*}\right|>|M|$. Let $Q=M \Delta M^{*}$. Then

- $Q$ has more edges from $M^{*}$ than from $M$ (since $\left|M^{*}\right|>|M|$ implies that $\left|M^{*} \backslash M\right|>\left|M \backslash M^{*}\right|$ ).
- Each vertex is incident to at most one edge in $M \cap Q$ and one edge in $M^{*} \cap Q$.
- Thus $Q$ is composed of cycles and paths that alternate between edges from $M$ and $M^{*}$.
- Therefore there must be some path with more edges from $M^{*}$ in it than from $M$. This path is an augmenting path with respect to $M$.

Hence, there must exist an augmenting path $P$ with respect to $M$, which is a contradiction.

The above finishes a rather simple algorithm for unweighted bipartite matching. To devise an algorithm for the weighted version, it will be convenient to introduce a powerful algorithmic tool: linear programming. The concept of duality (that we will see in upcoming lectures) will then allow us to use (an adapted) version of the above algorithm for weighted graphs!

## 2 Linear Programming

(Large parts of the following is taken from [1].)

A linear programing problem is the problem of finding values for variables that optimize a given linear objective function, subject to linear constraints.

Let us state an example of a linear program:

$$
\begin{aligned}
\text { Maximize } & x+y \\
\text { Subject to } & x+y \leq 2 \\
& y \leq 1 \\
& x, y \geq 0
\end{aligned}
$$

The following figure shows the feasible area.

Definition 5 A linear program (LP) is the problem of finding values for $n$ variables $x_{1}, x_{2}, \ldots, x_{n} \in \mathbb{R}$ that minimize (or equivalently, maximize) a given linear objective function, subject to $m$ linear constraints

$$
\begin{array}{rlr}
\text { minimize: } & \sum_{i=1}^{n} c_{i} x_{i} & \\
\text { Subject to: } & \sum_{i} e_{i, j} x_{i}=b_{j} & \text { for } j=1, \ldots, m_{1} \\
& \sum_{i} d_{i, k} x_{i} \geq g_{k} & \text { for } k=1, \ldots, m_{2} \\
& \sum_{i} f_{i, p} x_{i} \leq l_{p} & \text { for } p=1, \ldots, m_{3}
\end{array}
$$

where $m_{1}+m_{2}+m_{3}=m$.

### 2.1 Motivation

Linear Programming is a very powerful tool - it can be used in many applications, both industrial and theoretical such as:

- obtaining an optimal production plan to maximize a profit of a factory
- modeling network flow problems (what is maximum possible flow that doesn't exceed capacity of each connection)
- theory - many theoretical problems can be introduced as Integer Programs(LP in which $\left.x_{i} \in \mathbb{Z}\right)$ that can be relaxed to LP obtaining a good approximation of optimal result- we'll see such applications later in the course.


### 2.2 Some history

It was first formalized and applied to problems in economics in the 1930s by Leonid Kantorovich. Kantorivich's work was hidden behind the Iron Curtain (where it was largely ignored) and therefore unknown in the West. Linear programming was rediscovered and applied to shipping problems in the early 1940 s by Tjalling Koopmans.

Simplex Method was published by George Dantzig in 1947: it is the first complete algorithm to solve linear programming problems.

The principle is the following: we start from an extreme point and then we look at its neighbors. If one of these is better we move to it and continue in the same way, else we stop. Once we stop, we can be sure that we have an optimal solution, since we're in a convex polytope. Even if it's usually extremely
fast, we know some bad examples where this method visits an exponential number of extreme points before to reach a solution, so this method does not always run in polynomial time.

Ellipsoid Method was studied by Leonid Khachiyan in the seventies.

This method is guaranteed to run in poly time (exactly poly $(n, m, \log (u))$ where $u$ is the largest constant) but it is slow in practice.

We do a binary search for the optimal value of the objective function, so we can add the objective function as a constraint, and just need to decide if there exists a feasible point. We start by taking an ellipsoid surrounding the feasible area. We then check the center of the ellipsoid, if it's inside the area then we have our solution, else we identify a violated constraint, and cut our ellipsoid in two parts using this constraint, and construct a new ellipsoid around the part of the old ellipsoid in which the constraint is satisfied. We repeat this process until we find a feasible point or can be sure that the feasible area is empty.

Interior point Method developed by Narendra Karmarkar in 1984. In this method we move in the feasible region to find an OPT solution.


[^0]:    ${ }^{1}$ Disclaimer: These notes were written as notes for the lecturer. They have not been peer-reviewed and may contain inconsistent notation, typos, and omit citations of relevant works.

