##  Linear Programming: Extreme Points

## 1 Recall LPs, Extreme Points, and Bipartite Matching

Recall that a linear program is the problem of optimizing a linear objective subject to linear constraints (inequalities and equalities):

Definition 1 A linear program (LP) is the problem of finding values for $n$ variables $x_{1}, x_{2}, \ldots, x_{n} \in \mathbb{R}$ that minimize (or equivalently, maximize) a given linear objective function, subject to $m$ linear constraints

$$
\begin{array}{rlr}
\text { minimize: } & \sum_{i=1}^{n} c_{i} x_{i} & \\
\text { Subject to: } & \sum_{i} e_{i, j} x_{i}=b_{j} & \\
& \sum_{i} d_{i, k} x_{i} \geq g_{k} & \text { for } j=1, \ldots, m_{1} \\
& \sum_{i} f_{i, p} x_{i} \leq l_{p} & \text { for } k=1, \ldots, m_{2} \\
& \text { for } p=1, \ldots, m_{3}
\end{array}
$$

where $m_{1}+m_{2}+m_{3}=m$.

An example of a linear program is as follows:

$$
\begin{aligned}
\text { Maximize } & x+y \\
\text { Subject to } & x+y \leq 2 \\
& y \leq 1 \\
& x, y \geq 0
\end{aligned}
$$

When solving discrete optimization problems (such as matchings, vertex cover, spanning tree, etc.) it will be important that optimal solutions have certain structure. That is where we use extreme points and their structure (which is also important for the simplex algorithm).

### 1.1 Extreme Points

Let us first define an extreme point:

Definition $2 A$ feasible solution is an extreme point if it cannot be written as a convex combination of other feasible solutions.

Just to recall:

Definition $3 A$ convex combination of points $x_{1}, x_{2}, \ldots, x_{n}$ is a point of the form $\sum_{i=1}^{n} \lambda_{i} x_{i}$ where the real numbers $\lambda_{i}$ satisfy $\sum_{i=1}^{n} \lambda_{i}=1$ and $\lambda_{i} \in[0,1]$ for all $i$.

Now, we state a theorem about extreme points. Extreme points are important because sometimes they have useful structural properties, which we can exploit to design algorithms. We see two such examples in this lecture.

Theorem 4 If the feasible region is bounded, there always exists an optimum which is an extreme point.

Proof As the feasible region is bounded, there is an optimal solution $x^{\star}$ and any feasible point can be written as a convex combination of the extreme points. In particular, we have $x^{\star}=\sum_{i} \lambda_{i} x^{(i)}$ where $x^{(i)}$ 's are feasible extreme points and $\lambda^{\prime} s$ are non-negative real numbers satisfying $\sum_{i} \lambda_{i}=1$. Now let $c$ be the vector defining the objective that we wish to maximize (the proof is the same if we minimize). Then we have

$$
c^{T} x^{\star}=c^{T}\left(\sum_{i} \lambda_{i} x^{(i)}\right)=\sum_{i} \lambda_{i} c^{T} x^{(i)}
$$

which implies that there is an extreme point $x^{(i)}$ such that $c^{T} x^{(i)} \geq c^{T} x^{\star}$, i.e., it is an optimal solution.

If the feasible region is not bounded, then we might not have any extreme points. For example, the following LP does not contain any extreme points.

$$
\begin{aligned}
\text { Maximize } & y \\
\text { Subject to } & y \leq 1 \\
& y \geq 0
\end{aligned}
$$

## 2 Maximum Weight Bipartite Perfect Matching

In this section we are going to concentrate on maximum weight/profit bipartite perfect matching. Given a bipartite graph $G=(V, E)$ with $V$ partitioned into $A$ and $B$ and edge-weights $w \rightarrow \mathbb{R}$, this is the problem where we wish to find a perfect matching $M$ that maximizes $w(M)=\sum_{e \in M} w(e)$. Recall that a matching is perfect if every vertex is incident to exactly one edge in the matching, i.e., every vertex is matched. The LP for the maximum weight bipartite perfect matching problem can be formulated as

$$
\begin{array}{rll}
\text { Maximize } & \sum_{e \in E} x_{e} w_{e} \\
\text { Subject to } & \sum_{e=(a, b) \in E} x_{e}=1 \quad \forall a \in A \\
& \sum_{e=(a, b) \in E} x_{e}=1 \quad \forall b \in B \\
& x_{e} \geq 0 \quad \forall e \in E &
\end{array}
$$

In the linear program, we have a variable $x_{e}$ for each edge $e$ with the intended meaning that it should take value 1 if that edge is picked by the matching. The constraints say that each vertex should have exactly one incident edge in the matching.

Note that in a feasible solution the variables $x_{e}$ may take values strictly between 0 and 1 , which does not really correspond to a matching. However, we have the following key structural result:

Claim 5 For bipartite graphs, any extreme point solution to the LP is integral.

Proof Let $x^{*}$ be an extreme point for the graph $G=\left(V_{1}, V_{2}, E\right)$ and let $E_{f}=\left\{e \in E: 0<x_{e}^{*}<1\right\}$. Suppose towards contradiction that $E_{f} \neq \emptyset$. Note that $E_{f}$ must then contain a cycle: indeed any vertex incident to an edge in $E_{f}$ is incident to at least two edges in $E_{f}$. All these edges are fractional and we want to define $y$ and $z$ so that they are feasible solutions and $x^{*}=\frac{1}{2}(y+z)$ which will contradict the
fact that $x^{*}$ is an extreme point. Let $e_{1}, e_{2}, \ldots, e_{2 k}$ be the edges of the cycle. Let $y, z$ be

$$
\begin{aligned}
& y_{e}= \begin{cases}x_{e}^{*}+\epsilon & \text { if } e \in\left\{e_{1}, e_{3}, e_{5}, \ldots, e_{2 k-1}\right\} \\
x_{e}^{*}-\epsilon & \text { if } e \in\left\{e_{2}, e_{4}, e_{6}, \ldots, e_{2 k}\right\} \\
x_{e}^{*} & \text { otherwise }\end{cases} \\
& z_{e}= \begin{cases}x_{e}^{*}-\epsilon & \text { if } e \in\left\{e_{1}, e_{3}, e_{5}, \ldots, e_{2 k-1}\right\} \\
x_{e}^{*}+\epsilon & \text { if } e \in\left\{e_{2}, e_{4}, e_{6}, \ldots, e_{2 k}\right\} \\
x_{e}^{*} & \text { otherwise }\end{cases}
\end{aligned}
$$

Notice that the degree constraints are still satisfied by $y$ and $z$ as we are alternating between increasing and decreasing the edge values in a cycle of even length. Hence, to ensure feasibility, we need to choose such a small $\epsilon$ so as to guarantee that all $y_{e}$ and $z_{e}$ are in $[0,1]$. For example $\epsilon=\min \left\{x_{e}^{*},\left(1-x_{e}^{*}\right): e \in E_{f}\right\}$ gives that both $y$ and $z$ are feasible. Now one can easily see that $x^{*}=\frac{1}{2}(y+z)$ which contradicts the assumption that $x^{*}$ is an extreme point.

Because of the above claim, the polytope

$$
\begin{aligned}
& P=\left\{x: \sum_{b:(a, b) \in E} x_{(a, b)}=1 \quad a \in A\right. \\
& \sum_{a:(a, b) \in E} x_{(a, b)}=1 \quad b \in B \\
& \left.x_{(a, b)} \geq 0 \quad(a, b) \in E\right\}
\end{aligned}
$$

is called the bipartite perfect matching polytope. Also, it says that we can solve the maximum weight bipartite matching problem by simply solving the above linear program.

## 3 Vertex Cover

Here, we consider minimum weight vertex cover on bipartite graphs. The definition of the vertex cover problem is:

Definition 6 Given a graph $G=(V, E)$ with node-weights $w: V \rightarrow \mathbb{R}$ find a vertex cover $C$ (i.e., $e \cap C \neq \emptyset$ for all $e \in E)$ that minimizes $w(C)=\sum_{v \in C} w(v)$.

Similarly to the case of maximum weight bipartite perfect matching, we formulate a linear program for the vertex cover problem. Here, we have a variable $x_{v}$ for each vertex $v$ with the intended meaning that it takes value 1 if that vertex is in the vertex cover. The constraints say that each edge needs to be covered. The LP can be formulated as follows:

$$
\begin{array}{rll}
\text { Minimize } & \sum_{v \in V} x_{v} w(v) & \\
\text { Subject to to } & x_{u}+x_{v} \geq 1 & \forall\{u, v\} \in E \\
& 0 \leq x_{v} \leq 1 \quad \forall v \in V
\end{array}
$$

We have the following structural result for bipartite graphs:

Claim 7 For bipartite graphs, any extreme point to the vertex cover LP is integral.

Proof Consider an extreme point $x^{*}$ and let $V_{f}=\left\{v: 0<x_{v}^{*}<1\right\}$ be those vertices with fractional values in $x^{*}$. Suppose toward contradiction that $V_{f} \neq \emptyset$. Further, let $A, B$ be the bipartition of $V$ and let $A_{f}=V_{f} \cap A$ and $B_{f} \cap V_{f}$ be the fractional vertices in $A$ and $B$, respectively. As for bipartite matchings, we reach a contradiction by defining feasible solutions $y$ and $z$ so that $x^{*}=\frac{1}{2}(y+z)$ which contradicts that $x^{*}$ is an extreme point. Let $\epsilon=\min \left\{x_{v},\left(1-x_{v}\right): v \in A_{f} \cup B_{f}\right\}$ and define $y$ and $z$ by

$$
\begin{aligned}
& y_{v}= \begin{cases}x_{v}^{*}+\epsilon & \text { if } v \in A_{f} \\
x_{v}^{*}-\epsilon & \text { if } v \in B_{f} \\
x_{v}^{*} & \text { otherwise }\end{cases} \\
& z_{v}= \begin{cases}x_{v}^{*}-\epsilon & \text { if } v \in A_{f} \\
x_{v}^{*}+\epsilon & \text { if } e \in B_{f} \\
x_{v}^{*} & \text { otherwise }\end{cases}
\end{aligned}
$$

Clearly, we have that $x^{*}=\frac{1}{2}(y+z)$. It remains to verify that $y$ and $z$ are feasible solutions. Let us verify $y$ (the argument that $z$ is feasible is the same). By the selection of $\epsilon$, we have that $0 \leq y_{v} \leq 1$ for all $v \in V$. We now need to verify that the constraint for every edge is satisfied. Consider an edge $\{a, b\} \in E$ in the bipartite graph. We need to verify that $y_{a}+y_{b} \geq 1$. If $x_{a}=1$ (or $x_{b}=1$ ), then we have that $y_{a}=1$ (or $y_{b}=1$ ) and so the constraint holds. Otherwise $0<x_{a}, x_{b}<1$ and so $a \in A_{f}$ and $b \in B_{f}$. This in turn implies that $y$ is feasible since

$$
y_{a}+y_{b}=\left(x_{a}+\epsilon\right)+\left(x_{b}-\epsilon\right)=x_{a}+x_{b} \geq 1
$$

where the last inequality holds because $x^{*}$ is a feasible solution.

The above structural result says that we can solve minimum weighted vertex cover on bipartite graphs by simply solving the above linear program to find an optimal extreme point. It does not work for general graphs which can be seen by considering the triangle (as for matchings). In contrast to matchings, the vertex cover problem on general graphs is an NP-hard problem and we do not expect to have efficient algorithms for it.

