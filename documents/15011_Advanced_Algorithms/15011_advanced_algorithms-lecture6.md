##  Hungarian Method and Weighted Vertex Cover

## 1 Recall: Linear Programming Duality

In the last lecture, we saw that if we have a linear progam with $n$ variables $x_{1}, x_{2}, \ldots, x_{n}$ and $m$ constraints of the following form:

$$
\begin{aligned}
\text { Minimize } & \sum_{i=1}^{n} c_{i} x_{i} \\
\text { Subject to: } & \sum_{i=1}^{n} A_{j i} x_{i} \geq b_{j} \quad \forall j=1, \ldots, m \\
& x \geq 0
\end{aligned}
$$

Then, the dual program with $m$ variables $y_{1}, y_{2}, \ldots, y_{m}$ and $n$ constraints is as follows:

$$
\begin{aligned}
\text { Maximize } & \sum_{j=1}^{m} b_{j} y_{j} \\
\text { Subject to: } & \sum_{j=1}^{m} A_{j i} y_{j} \leq c_{i} \quad \forall i=1, \ldots, n \\
& y \geq 0
\end{aligned}
$$

In other words, if the primal program is written as $\min \left\{c^{\top} x: A x \geq b, x \geq 0\right\}$, then the dual can be written as $\max \left\{b^{\top} y: A^{\top} y \leq c, y \geq 0\right\}$. Here $A \in \mathbb{R}^{m \times n}, x \in \mathbb{R}^{n}, y \in \mathbb{R}^{m}, b \in \mathbb{R}^{m}, c \in \mathbb{R}^{n}$.

Remark Any linear program can be written in the above form and thus we can use the above recipe to take the dual of any linear program.

Basically by definition, we have weak duality:

Theorem 1 (Weak Duality) If $x$ is primal-feasible (meaning that $x$ is a feasible solution to the primal problem) and $y$ is dual-feasible, then

$$
\sum_{i=1}^{n} c_{i} x_{i} \geq \sum_{j=1}^{m} b_{j} y_{j}
$$[^0]

Perhaps more surprisingly, it turns out that the optimal solutions to the primal and dual have the same value:

Theorem 2 (Strong Duality) If $x$ is an optimal primal solution and $y$ is an optimal dual solution, then

$$
\sum_{i=1}^{n} c_{i} x_{i}=\sum_{j=1}^{m} b_{j} y_{j}
$$

Furthermore, if the primal problem is unbounded, then the dual problem is infeasible and analogously if the dual is unbounded, then the primal is infeasible.

Strong duality gives an important relationship between primal and dual optimal solutions.

Theorem 3 (complementarity slackness) Let $x \in \mathbb{R}^{n}$ be a feasible solution to the primal and let $y \in \mathbb{R}^{m}$ be a feasible solution to the dual. Then

$$
x, y \text { are both optimal solutions } \Longleftrightarrow \begin{cases}x_{i}>0 \Rightarrow c_{i}=\sum_{j=1}^{m} A_{j i} y_{j} & \forall i=1, \ldots, n \\ y_{j}>0 \Rightarrow b_{j}=\sum_{i=1}^{n} A_{j i} x_{i} & \forall j=1, \ldots, m\end{cases}
$$

## 2 Duality and Complementarity Slackness of Min-Cost Perfect Matching

Let $G=(A \cup B, E)$ be a bipartite weighted graph with edge-costs $c: E \rightarrow \mathbb{R}$. We wish to find a perfect matching $M$ of minimum cost $\sum_{e \in M} c(e)$.

To write down the linear program for this problem, we have a variable $x_{e}$ for every edge $e$, with the intended meaning that $x_{e}$ takes value 1 if $e$ is in the matching and 0 otherwise. In a perfect matching, every vertex is adjacent to exactly one edge of the matching. This leads to the following linear program:

$$
\begin{aligned}
\text { Minimize } & \sum_{e \in E} c(e) x_{e} \\
\text { Subject to: } \sum_{b \in B:(a, b) \in E} x_{a b}=1 & \forall a \in A \\
\sum_{a \in A:(a, b) \in E} x_{a b}=1 & \forall b \in B \\
x_{e} \geq 0 & \forall e \in E
\end{aligned}
$$

In a previous lecture, we saw that any extreme point of the above linear program is integral. Hence, we could solve the min-cost perfect matching problem by simply solving the above linear program, finding an extreme-point solution. However, this may be unnecessarily inefficient. Instead, we will see how to use LP duality to, basically, reduce this (weighted) problem to that of finding a perfect matching in an unweighted graph. (A problem that we already saw how to solve using augmenting paths.)

Obtaining the dual. To take the dual of the above program, let us first write it in the same form as the linear program in Section 1. We can do this by replacing each equality by two inequalities. This gives us the following equivalent linear program:

$$
\begin{array}{rlr}
\text { Minimize } & \sum_{e \in E} c(e) x_{e} & \\
\text { Subject to: } \sum_{b \in B:(a, b) \in E} x_{a b} \geq 1 \quad & \forall a \in A \\
& -\sum_{b \in B:(a, b) \in E} x_{a b} \geq-1 & \forall a \in A \\
& \sum_{a \in A:(a, b) \in E} x_{a b} \geq 1 & \forall b \in B \\
& -\sum_{a \in A:(a, b) \in E} x_{a b} \geq-1 & \forall b \in B \\
& x_{e} \geq 0 & \forall e \in E
\end{array}
$$

For each $a \in A$, we then associate a variable $u_{a}^{+}$to the first constraint for $a\left(\sum_{b \in B:(a, b) \in E} x_{a b} \geq 1\right)$ and $u_{a}^{-}$to the second constraint for $a\left(-\sum_{b \in B:(a, b) \in E} x_{a b} \geq-1\right)$. Similarly, we have variables $v_{b}^{+}$and $v_{b}^{-}$ for each $b \in B$. These variables take the same role as the $y$-variables in Section 1: the dual has a variable for each constraint in the primal. We now have that the dual equals

$$
\begin{array}{rll}
\text { Maximize } & \sum_{a \in A}\left(u_{a}^{+}-u_{a}^{-}\right)+\sum_{b \in B}\left(v_{b}^{+}-v_{b}^{-}\right) & \\
\text {Subject to: } & \left(u_{a}^{+}-u_{a}^{-}\right)+\left(v_{b}^{+}-v_{b}^{-}\right) \leq c(e) \\
& u_{a}^{+}, u_{a}^{-}, v_{b}^{+}, v_{b}^{-} \geq 0 \quad \forall a \in A, b \in B & \forall e=(a, b) \in E \\
& \forall 0
\end{array}
$$

Complementarity Slackness. Complementarity slackness tells us that if $x,\left(u^{+}, u^{-}, v^{+}, v^{-}\right)$are feasible, then they are both optimal if and only if the following holds:

$$
\begin{aligned}
x_{e}>0 \Rightarrow\left(u_{a}^{+}-u_{a}^{-}\right)+\left(v_{b}^{+}-v_{b}^{-}\right)=c(e) & \forall e=(a, b) \in E, \\
u_{a}^{+}>0 \Rightarrow \sum_{b \in B:(a, b) \in E} x_{a b}=1 & \forall a \in A \\
u_{a}^{-}>0 \Rightarrow-\sum_{b \in B:(a, b) \in E} x_{a b}=-1 & \forall a \in A, \\
v_{b}^{+}>0 \Rightarrow \sum_{a \in A:(a, b) \in E} x_{a b}=1 & \forall b \in B \\
v_{b}^{-}>0 \Rightarrow-\sum_{a \in A:(a, b) \in E} x_{a b}=1 & \forall b \in B .
\end{aligned}
$$

We have thus obtained the dual and the complementarity slackness conditions in an "automatic" way.

Simplifying the notation. Before continuing, we would like to make an observation that will simplify our description and notation. Namely, in the dual that we obtained, the variables $u_{a}^{+}$and $u_{a}^{-}$always appear only as part of the expression $\left(u_{a}^{+}-u_{a}^{-}\right)$. Although we have $u_{a}^{+}, u_{a}^{-} \geq 0$, this expression can take any value (positive and negative). We can thus for every $a \in A$ replace $\left(u_{a}^{+}-u_{a}^{-}\right)$by a new variable $u_{a} \in \mathbb{R}$ whose value is not constrained to be nonnegative (it can take both positive and negative values). We do the same for each $b \in B$ and replace $\left(v_{b}^{+}-v_{b}^{-}\right)$by $v_{b} .{ }^{2}$ We can thus write the primal and the dual as follows:[^1]

$$
\begin{aligned}
\text { Minimize } & \sum_{e \in E} c(e) x_{e} \\
\text { Subject to: } \sum_{b \in B:(a, b) \in E} x_{a b}=1 & \forall a \in A \\
\sum_{a \in A:(a, b) \in E} x_{a b}=1 & \forall b \in B \\
x_{e} \geq 0 & \forall e \in E
\end{aligned}
$$

and

$$
\begin{aligned}
\text { Maximize } & \sum_{a \in A} u_{a}+\sum_{b \in B} v_{b} \\
\text { Subject to: } & u_{a}+v_{b} \leq c(e) \quad \forall e=(a, b) \in E
\end{aligned}
$$

With this simplified notation, complementarity slackness gives us that if $x,(u, v)$ are feasible, then they are both optimal if and only if the following holds:

$$
\begin{array}{ll}
x_{e}>0 \Rightarrow u_{a}+v_{b}=c(e) & \forall e=(a, b) \in E \\
u_{a} \neq 0 \Rightarrow \sum_{b \in B:(a, b) \in E} x_{a b}=1 & \forall a \in A \\
v_{b} \neq 0 \Rightarrow \sum_{a \in A:(a, b) \in E} x_{a b}=1 & \forall b \in B
\end{array}
$$

As a final simplification, observe that the last two conditions always hold since they follow immediately from the fact that $x$ is primal-feasible (this is because in this LP we have equalities instead of inequalities).

We can thus summarize the above with the following:

Lemma $4 A$ perfect matching $M$ is of minimum cost iff there is a feasible dual solution $u, v$ such that

$$
u_{a}+v_{b}=c(e) \quad \text { for every } e=(a, b) \in M
$$

We will now use this fact to develop an algorithm for finding a minimum-cost perfect matching.

## 3 The Hungarian Algorithm

We start with some intuition before we give the formal description of the algorithm.[^2]

### 3.1 Intuition

Consider the following instance of the min-cost perfect matching problem:

The thin edges have cost 1 , whereas the thick edge has cost 2. The Hungarian algorithm will use Lemma 4 in the following way: we will maintain a dual solution $u, v$ that is feasible at all times. Then, for a fixed dual solution, the lemma tells us that our perfect matching is only allowed to contain edges that are tight, i.e., edges $e=(a, b)$ for which $u_{a}+v_{b}=c(e)$. This reduces our problem to finding any perfect matching in the subgraph consisting only of tight edges, i.e., in the graph $\left(V, E^{\prime}\right)$ where $E^{\prime}=\left\{e=(a, b) \in E: u_{a}+v_{b}=c(e)\right\}$. Intuitively, we have thus reduced our weighted problem to an unweighted one!

Let us return to our example. We initialize our procedure with the trivial dual solution

$$
v_{b}=0, \quad u_{a}=\min _{b \in B} c_{a b}
$$

(We could have also started from $u=v=0$.) So in the example, $v_{4}=v_{5}=v_{6}=0$ and $u_{1}=u_{2}=u_{3}=1$. The set $E^{\prime}$ of tight edges is thus:

We then try to find a perfect matching in this graph using e.g. the augmenting path algorithm we saw in Lecture 3. However, the considered graph has no perfect matching! This is because we started with a poor lower bound (dual solution). So we will use the fact that there is no perfect matching to improve our dual solution. We make use of Hall's condition, which you will prove in the exercise session:

Theorem 5 (Hall's Theorem) An $n$-by-n bipartite graph $G=\left(A \cup B, E^{\prime}\right)$ has a perfect matching if and only if $|S| \leq|N(S)|$ for all $S \subseteq A$.

Here $N(S)=\left\{b \in B\right.$ : there is an $a \in S$ such that $\left.(a, b) \in E^{\prime}\right\}$ denotes the neighborhood of the vertices in $S$.

In the above example, we have $S=\{1,2\}$ and $N(S)=\{4\}$, which violates Hall's condition (and thus there is no perfect matching). We now use the set $S$ to improve our dual lower bound.

We gradually increase $u_{a}$ for every $a \in S$ and at the same time decrease $v_{b}$ for $b \in N(S)$ at the same rate. Let us see what happens to all edges in $E^{\prime}$. Notice that the tight edges between $S$ and $N(S)$ will remain tight. Similarly, the tight edges between $A \backslash S$ and $B \backslash N(S)$ will remain tight. Any tight edges between $A \backslash S$ and $N(S)$ will stop being tight. Finally, by definition, there are no edges from $S$ to $B \backslash N(S)$ initially. We continue to gradually change the dual solution until some such edge becomes tight.

In the above example, this will result in updating $u_{1}=u_{2}=2$ and $v_{4}=-1$. We have thus increased two variables by one unit and decreased one variable by one unit. In total, the dual lower bound was thus increased by one. The set $E^{\prime}$ of tight edges with respect to the new dual solution is now

Our (augmenting-path) algorithm will now find a perfect matching in this graph, which is optimal by Lemma 4 (since it only uses tight edges). In summary, our algorithm always maintains a dual feasible solution. We then solve the unweighted perfect matching problem on the edges allowed by Lemma 4. In the case of failure, we update the dual lower bound to a strictly better lower bound and repeat.

### 3.2 Formal description

Idea: Maintain a feasible dual solution $(u, v)$. Try to construct a feasible primal solution that satisfies complementarity slackness (Lemma 4) and is thus optimal.

## Algorithm:

## - Initialization:

$$
v_{b}=0, \quad u_{a}=\min _{b \in B} c_{a b}
$$

## - Iterative step:

- consider $G^{\prime}=\left(A \cup B, E^{\prime}\right)$ where $E^{\prime}=\left\{e=(a, b) \in E: u_{a}+v_{b}=c(e)\right\}\left(E^{\prime}\right.$ is the set of all tight edges);
- find a maximum-cardinality matching in $G^{\prime}$ :
* if it is a perfect matching, then we are done (this is a primal feasible solution and it satisfies complementarity slackness, because we consider only the edges in $E^{\prime}$ and all of them satisfy slackness by construction),
* otherwise the algorithm finds a set $S \subseteq A$ s.t. $|S|>|N(S)|$ (which is guaranteed to exist by Hall's theorem)
- we can choose a small $\varepsilon>0$ and improve the dual solution:

$$
\begin{aligned}
u_{a}^{\prime} & = \begin{cases}u_{a}+\epsilon & \text { if } a \in S \\
u_{a} & \text { if } a \notin S\end{cases} \\
v_{b}^{\prime} & = \begin{cases}v_{b}-\epsilon & \text { if } b \in N(S) \\
v_{b} & \text { if } b \notin N(S)\end{cases}
\end{aligned}
$$

which remains dual feasible because:

* edges in $S \times N(S)$ are unchanged $(+\varepsilon-\varepsilon)$,
* edges in $(A \backslash S) \times(B \backslash N(S))$ are unchanged,
* edges in $(A \backslash S) \times N(S)$ are decreased by $\varepsilon$,
* edges in $S \times(B \backslash N(S))$ are increased by $\varepsilon$ but they were not tight (they were not in $E^{\prime}$ ),
- the dual value increases by $(|S|-|N(S)|) \varepsilon$;
- to make as much progress as possible (and to get a new tight edge), we should choose $\varepsilon$ as large as possible for which the dual remains feasible, that is

$$
\varepsilon=\min _{e=(a, b) \in S \times(B \backslash N(S))} c(e)-u_{a}-v_{b}>0
$$

The above algorithm can be implemented to run in time $O\left(n^{3}\right)$. (This is quite non-trivial to see. It is somewhat easier to implement in $O\left(n^{4}\right)$.)

### 3.3 An alternative proof that the bipartite perfect matching polytope is integral

We have shown that for any cost function $c$ we can obtain a minimum-cost perfect matching and it will be integral. By carefully choosing the cost function, one can make any extreme point of the polytope to be the unique optimum solution to the minimum-cost perfect matching problem. This shows that all extreme points are integral, i.e., it is an integral polytope. See Figure 1 for an example.

## 4 When Relaxing Integrality is Not for Free: Approximation Algorithms

Thousands (or millions :)) of optimization problems have been proved to be NP-hard, which means that finding optimal solutions for them is very likely to be intractable. More specifically, unless $\mathrm{P}=\mathrm{NP}$, there is no algorithm for an NP-hard optimization problem that satisfies all of the following three desiderata:

1. The algorithm is efficient (runs in polynomial time).
2. The algorithm is reliable (works for any input instance).
3. The algorithm finds an optimal solution (optimality).

Therefore, when confronted which such problems, we need to relax one of the above conditions when dealing with NP-hard optimization problems. If we relax reliability, then we get heuristics that are designed to work well on instances that commonly appear in practice. If we relax the third condition, we obtain approximation algorithms. The notion of approximation algorithms allows us to obtain a more fine-grained picture of the difficulty of NP-hard optimization problems: some problems turn out to have very good approximations, whereas others resist such attempts.

The formal definition of approximation algorithms is as follows.

Definition 6 An $\alpha$-approximation algorithm for a given optimization problem is an algorithm that runs in polynomial time and outputs a solution $S$ such that:

- $\frac{\operatorname{cost}(S)}{\operatorname{cost}(\text { Optimal solution })} \leq \alpha$ if the problem is a minimization problem,
- $\frac{p \text { proft }(S)}{\text { profit( Optimal solution })} \geq \alpha$ if the problem is a maximization problem.

It is clear that we will have $\alpha \geq 1$ for minimization problems and $\alpha \leq 1$ for maximization problems. Moreover, if $\alpha=1$, then we have an efficient exact algorithm (and the problem is in $\mathrm{P}$ ). The goal when designing approximation algorithms is to achieve a guarantee $\alpha$ that is as close to 1 as possible. We now introduce a general framework for using linear programming in the design of approximation algorithms followed by an application: vertex cover.

## 5 Using Linear Programming to Design Approximation Algorithms

Consider a minimization problem. When considering the definition of approximation algorithms, it seems very hard, even for a specific instance of the problem, to analyze the approximation guarantee $\frac{\operatorname{cost}(S)}{\operatorname{cost}(\text { Optimal solution })}$ of the algorithm on the instance, as we are comparing ourselves with an optimal solution (that is most likely very hard to compute and does not possess any nice structure). The solution to this is to compare ourselves with a lower bound on the optimum. Indeed, we then have that

$$
\frac{\operatorname{cost}(S)}{\operatorname{cost}(\text { Optimal solution })} \leq \frac{\operatorname{cost}(S)}{\text { lower bound on opt }} \leq \alpha
$$

From the above, it is clear that we need a good lower bound to be able to claim a good guarantee $\alpha$. To obtain such a lower bound (and to design the approximation algorithm), linear programming is super handy. A popular framework is as follows:

1. Give an exact formulation of the problem as Integer LP - usually with binary variables $\left(x_{i} \in\{0,1\}\right)$.
2. Relax to $\mathrm{LP}-x_{i} \in[0,1]$
3. Solve LP to get a optimal solution $x^{*}$ to the LP which is a lower (upper) bound on the optimal solution to Integer LP and thus the original problem. Then somehow round $x^{*}$ to an integral solution "without losing too much" (which will determine the guarantee $\alpha$ ).

We now use the above framework for the vertex cover problem, and then introduce the concept of integrality gap.

### 5.1 Vertex Cover

Here, we apply the framework to get an approximation algorithm for the Vertex Cover problem. First recall the definition:

Definition 7 (Vertex Cover (VC) Problem) Given a graph $G=(V, E)$ and a weight function on the vertices $w: V \rightarrow \mathbb{R}_{+}$, output a set $C \subseteq V$ of minimum weight such that for all $\{u, v\} \in E, u \in C$ or $v \in C$.

First, we define an ILP solving VC: For all $v \in V$, we introduce a variable $x_{v}$, which is 1 if $v \in C$, and 0 otherwise. The objective function is

$$
\min \sum_{v \in V} w(v) x_{v}
$$

and for each $\{u, v\} \in E$ we introduce the constraint $x_{u}+x_{v} \geq 1$. This ensures that for each edge, at least one endpoint is in $C$. Additionally, we require that for each $v \in V$ we have $x_{v} \in\{0,1\}$. Note that at this point our Integer LP formulation is exactly equivalent to the original problem.

Second, we relax the ILP to an LP by allowing that $x_{v} \in[0,1]$. Actually, it's sufficient to require that $x_{v} \geq 0$, because having an $x_{v}$ greater than 1 will not satisfy any additional constraint, but only increase the value of the objective function, so this will not happen in an optimal solution.

Third, we have to do the rounding: Suppose we've solved the LP and got an optimal solution $x^{*}$. We will return $C=\left\{v \in V: x_{v}^{*} \geq \frac{1}{2}\right\}$ as our solution to VC.

Claim $8 C$ is a feasible solution.

Proof Consider any edge $\{u, v\}$ and its constraint. Since $x_{u}^{*}+x_{v}^{*} \geq 1$, at least one of $x_{u}^{*}, x_{v}^{*}$ is $\geq \frac{1}{2}$ and thus in $C$.

Claim 9 The weight of $C$ is at most twice the value of the optimal solution of VC.

Proof We have

$$
\sum_{v \in C} w(v)=\sum_{v \in V: x_{v}^{*} \geq \frac{1}{2}} w(v) \leq \sum_{v \in V: x_{v}^{*} \geq \frac{1}{2}} 2 x_{v}^{*} w(v) \leq \sum_{v \in V} 2 x_{v}^{*} w(v)=2 \sum_{v \in V} x_{v}^{*} w(v)=2 L P_{O P T} \leq 2 V C_{O P T}
$$

where the first inequality holds because $2 x_{v}^{*} \geq 1$.

So, we have designed a 2-approximation algorithm for Vertex Cover. This is a simple algorithm using linear programming. To appreciate the power of the framework, I challenge you to find a 2approximation algorithm for Vertex Cover (with node-weights) without the use of LPs. (It is possible but quite difficult.)

### 5.2 Integrality Gap

The notion of the integrality gap allows us to bound the power of our linear programming relaxation. Let $\mathcal{I}$ be the set of all instances of a given problem. In the case of a minimization problem, the integrality gap $g$ is defined as

$$
g=\max _{I \in \mathcal{I}} \frac{O P T(I)}{O P T_{L P}(I)}
$$

As an example, suppose $g=2$, and that LP found that $O P T_{L P}=70$. Then, since our problem instance might be the one which maximizes the expression for $g$, all we can guarantee is that $O P T(I) \leq$ $2 \cdot O P T_{L P}(I)=140$, so it's not possible to find an approximation algorithm (using only this linear programming relaxation) that approximates better than within a factor of $g=2$.

### 5.2.1 Integrality Gap for Vertex Cover

Claim 10 The integrality gap for vertex cover is at least $2-\frac{2}{n}$.

Proof Consider the complete graph on $n$ vertices. We have $O P T=n-1$, because if there are 2 vertices that we don't choose, the edge between them is not covered. However, $L P_{O P T} \leq \frac{n}{2}$, because assigning $\frac{1}{2}$ to each vertex is a feasible solution of cost $\frac{n}{2}$, so the optimum can only be smaller. Now,

$$
g \geq \frac{n-1}{\frac{n}{2}}=2-\frac{2}{n}
$$

We remark that our 2 -approximation algorithm for vertex cover implies that the integrality gap is at most 2 .


[^0]:    ${ }^{1}$ Disclaimer: These notes were written as notes for the lecturer. They have not been peer-reviewed and may contain inconsistent notation, typos, and omit citations of relevant works.

[^1]:    ${ }^{2}$ Note that our new LP is in fact equivalent to the old one. Given a feasible solution to the old LP, we can obtain a feasible solution to the new LP by setting the values for the new variables as $u_{a}:=u_{a}^{+}-u_{a}^{-}$(and similarly for $v$ ). Since we

[^2]:    do the same in the objective function, the objective value remains unchanged. We can also go back and obtain a solution of the old LP from a solution of the new LP as follows: if $u_{a} \geq 0$, set $u_{a}^{+}=u_{a}$ and $u_{a}^{-}=0$; otherwise set $u_{a}^{+}=0$ and $u_{a}^{-}=-u_{a}$ (and similarly for $v$ ).

    Also note that the new LP is what we would have obtained if we had multiplied each equality constraint $\sum_{b \in B:(u, v) \in E} x_{a b}=1$ by an unconstrained dual variable $u_{a} \in \mathbb{R}$, rather than rewriting this equality constraint as two inequality constraints and then multiplying each by a nonnegative dual variable $\left(u_{a}^{+}\right.$or $\left.u_{a}^{-}\right)$. (And similarly for $v$.)

