## Linear Programming: Duality

### 1.1 Intuition

Consider the following linear program:

$$
\begin{array}{rlr}
\text { Minimize } & 7 x_{1}+3 x_{2} \\
\text { Subject to: } & x_{1}+x_{2} \geq 2, \quad / \cdot y_{1} \\
& 3 x_{1}+x_{2} \geq 4, \quad / \cdot y_{2} \\
& x_{1}, x_{2} \geq 0
\end{array}
$$

We are looking for the optimal solution OPT to this LP. To find the solution we may ask two types of questions (to find the upper and lower bound on OPT). Is there a solution of cost $\leq 10$ ? (Is OPT $\leq 10$ )? An answer to this type of questions is quite simple; we just find a feasible solution to the LP with objective function $\leq 10$ e.g. $x_{1}=x_{2}=1$. Is there no better solution? (Is OPT $\geq 10$ )? Observe that we can bound the objective function value using constraints that every feasible solution satisfies. From the first constraint we get

$$
7 x_{1}+3 x_{2} \geq x_{1}+x_{2} \geq 2
$$

Thus $\mathrm{OPT} \geq 2$. Similarly from the second constraint we get $\mathrm{OPT} \geq 4$. To make a better lower bound we will need to be more clever. Let's take a linear combination of the constraints with coefficients $y_{1}, y_{2}$ correspondingly. $y_{1}, y_{2}$ should be non-negative because multiplying a constraint by negative number would flip the inequality. By taking $y_{1}=1, y_{2}=2$ we obtain

$$
7 x_{1}+3 x_{2} \geq\left(x_{1}+x_{2}\right)+2\left(3 x_{1}+x_{2}\right) \geq 2+2 \cdot 4=10
$$

For each constraint of the given LP we associate a dual variable $y_{i}$ denoting the weight of the $i$-th constraint. What kind of variables can we take to get a valid lower bound? How should we pick coefficients to maximize lower bound for OPT? First of all we are interested in lower-bounding the objective function. Thus linear combination of primal constraints cannot exceed primal objective function. As mentioned earlier $y_{i} \geq 0$. In this way we get the following (dual) linear program for $y_{1}, y_{2}$ :

Maximize $2 y_{1}+4 y_{2} \quad$ (lower bound as tight as possible)

Subject to: $y_{1}+3 y_{2} \leq 7, \quad\left(\right.$ coefficient of $\left.x_{1}\right)$

$y_{1}+y_{2} \leq 3, \quad\left(\right.$ coefficient of $\left.x_{2}\right)$

$y_{1}, y_{2} \geq 0$.

Let's try now to formalize this approach.[^0]

### 1.2 General case

Consider the following linear program with $n$ variables $x_{i}$ for $i \in[1, n]$ and $m$ constraints:

$$
\begin{aligned}
\text { Minimize } & \sum_{i=1}^{n} c_{i} x_{i} \\
\text { Subject to: } & \sum_{i=1}^{n} A_{j i} x_{i} \geq b_{j} \quad \forall j=1, \ldots, m \\
& x \geq 0
\end{aligned}
$$

Then, the dual program has $m$ variables $y_{j}$ for $j \in[1, m]$ and $n$ constraints:

$$
\begin{aligned}
\text { Maximize } & \sum_{j=1}^{m} b_{j} y_{j} \\
\text { Subject to: } & \sum_{j=1}^{m} A_{j i} y_{j} \leq c_{i} \quad \forall i=1, \ldots, n \\
& y \geq 0
\end{aligned}
$$

Each variable $y_{j}$ in the dual program corresponds to the weight of one of constraints from the primal LP. We have $n$ constraints in the dual, one for every primal variable $x_{i}$.

Remark We showed how to produce dual program for minimization problem. Similar approach works also for maximization problems. Also every maximization problem can be reduced to a minimization one. We replace $x_{i}$ with $-x_{i}$ in constraints and objective function obtaining minimization problem.

Remark One can verify that if we take the dual of the dual problem, we get back to the primal problem, as we should expect. Finding the dual linear program is an automatic procedure.

### 1.3 Duality Theorems

Let's focus now on the solutions of both LPs. In our example optimal solutions to primal and dual problems coincided. We now present two theorems that connect primal and dual solutions.

Theorem 1 (Weak Duality) If $x$ is primal-feasible (meaning that $x$ is a feasible solution to the primal problem) and $y$ is dual-feasible, then

$$
\sum_{i=1}^{n} c_{i} x_{i} \geq \sum_{j=1}^{m} b_{j} y_{j}
$$

Proof Let's rewrite the right hand side

$$
\sum_{j=1}^{m} b_{j} y_{j} \leq \sum_{j=1}^{m} \sum_{i=1}^{n} A_{j i} x_{i} y_{j}=\sum_{i=1}^{n}\left(\sum_{j=1}^{m} A_{j i} y_{j}\right) x_{i} \leq \sum_{i=1}^{n} c_{i} x_{i}
$$

Here we used the fact that $x, y \geq 0$ for the inqualities.

This theorem tells us that every dual-feasible solution is a lower bound to any primal solution. This is intuitive: every primal feasible solution satisfies primal constraints, dual feasible solution gives us a way of lower bounding primal solution using primal constraints. Moreover from Weak Duality we can conclude that optimal solution to primal program is lower bounded by optimal solution to dual program. In fact optimal solutions to primal and duals linear programs coincide, leading to the following theorem.

Theorem 2 (Strong Duality) If $x$ is an optimal primal solution and $y$ is an optimal dual solution, then

$$
\sum_{i=1}^{n} c_{i} x_{i}=\sum_{j=1}^{m} b_{j} y_{j}
$$

Furthermore, if the primal problem is unbounded, then the dual problem is infeasible and analogously if the dual is unbounded, the primal is infeasible.

We omit the proof of strong duality for now but I encourage you to understand one of the many proofs!

### 1.4 Example: Maximum cardinality matching and Vertex Cover on Bipartite Graphs

Let $G=(A \cup B, E)$ be a bipartite graph and let $M$ be a matching. Let $x_{e}$ be a variable corresponding to taking edge $e \in M$. We want to maximize the cardinality of $M$ while assuring that every vertex has at most one neighboring edge belonging to $M$. Writing those conditions in a form of LP gives us:

$$
\begin{aligned}
\text { Maximize } & \sum_{e \in E} x_{e} \\
\text { Subject to: } & \sum_{e=(a, b) \in E} x_{e} \leq 1 \quad \forall a \in A, \\
& \sum_{e=(a, b) \in E} x_{e} \leq 1 \quad \forall b \in B, \\
& x_{e} \geq 0 .
\end{aligned}
$$

Thus the dual program looks like this:

$$
\begin{aligned}
\text { Minimize } & \sum_{v \in A \cup B} y_{v} \\
\text { Subject to: } & y_{a}+y_{b} \geq 1 \quad \text { for }(a, b) \in E, \\
& y_{v} \geq 0
\end{aligned}
$$

One can easily notice that this LP is vertex cover relaxation. By weak-duality, we have that $|M| \leq|C|$ for any matching $M$ and vertex cover $C$. Moreover, since both the primal and the dual are integral for bipartite graphs, strong LP-duality implies König's theorem:

Theorem 3 (König 1931) Let $M^{\star}$ be a maximum cardinality matching and $C^{\star}$ be a minimum vertex cover of a bipartite graph. Then

$$
\left|M^{\star}\right|=\left|C^{\star}\right| .
$$

Another well-known duality that is also a special case of LP-duality is the max-flow= min-cut theorem.

### 1.5 Complementarity Slackness

Strong duality gives an important relationship between primal and dual optimal solutions.

Theorem 4 Let $x \in \mathbb{R}^{n}$ be a feasible solution to the primal and let $y \in \mathbb{R}^{m}$ be a feasible solution to the dual. Then

$$
x, y \text { are both optimal solutions } \Longleftrightarrow \begin{cases}x_{i}>0 \Rightarrow c_{i}=\sum_{j=1}^{m} A_{j i} y_{j} & \forall i=1, \ldots, n \\ y_{j}>0 \Rightarrow b_{j}=\sum_{i=1}^{n} A_{j i} x_{i} & \forall j=1, \ldots, m\end{cases}
$$

Proof We will apply the strong duality theorem to the weak duality theorem proof.

$\Rightarrow$ Let $x$ be the optimal primal solution. From the weak duality theorem proof, we have that

$$
\begin{equation*}
\sum_{j=1}^{m} b_{j} y_{j} \leq \sum_{j=1}^{m} \sum_{i=1}^{n} A_{j i} x_{i} y_{j}=\sum_{i=1}^{n}\left(\sum_{j=1}^{m} A_{j i} y_{j}\right) x_{i} \leq \sum_{i=1}^{n} c_{i} x_{i} \tag{1}
\end{equation*}
$$

Here we used the fact that $x, y \geq 0$. On the other hand by the strong duality theorem

$$
\sum_{j=1}^{m} b_{j} y_{j}=\sum_{i=1}^{n} c_{i} x_{i}
$$

So in (1) there are equalities everywhere. Thus

$$
\sum_{i=1}^{n} c_{i} x_{i}=\sum_{i=1}^{n}\left(\sum_{j=1}^{m} A_{j i} y_{j}\right) x_{i} \Rightarrow c_{i} x_{i}=\left(\sum_{j=1}^{m} A_{j i} y_{j}\right) x_{i} \text { for } i=1, \ldots n
$$

And finally for every $x_{i}, i=1, \ldots n$ :

$$
x_{i} \neq 0 \quad c_{i} x_{i}=\left(\sum_{j=1}^{m} A_{j i} y_{j}\right) x_{i} \Rightarrow c_{i}=\left(\sum_{j=1}^{m} A_{j i} y_{j}\right)
$$

$\Leftarrow$ Similarly to the previous part we know that:

$$
\begin{array}{ll}
x_{i} c_{i}=\left(\sum_{j=1}^{m} A_{j i} y_{j}\right) x_{i} & \forall i=1, \ldots, n \\
y_{j} b_{j}=\left(\sum_{i=1}^{n} A_{j i} x_{i}\right) y_{j} & \forall j=1, \ldots, m
\end{array}
$$

Thus

$$
\sum_{j=1}^{m} b_{j} y_{j}=\sum_{j=1}^{m} \sum_{i=1}^{n} A_{j i} x_{i} y_{j}=\sum_{i=1}^{n}\left(\sum_{j=1}^{m} A_{j i} y_{j}\right) x_{i}=\sum_{i=1}^{n} c_{i} x_{i}
$$

The above equality is equivalent to $x, y$ being optimal solutions to the primal and the dual linear programs, respectively. Indeed for feasible solution $x^{\star}$ to the primal we have by weak duality

$$
\sum_{i=1}^{n} c_{i} x_{i}^{\star} \geq \sum_{j=1}^{m} b_{j} y_{j}=\sum_{i=1}^{n} c_{i} x_{i}
$$

Thus $x$ is an optimal solution to the primal program and similarly $y$ is an optimal solution to the dual.


[^0]:    ${ }^{1}$ Disclaimer: These notes were written as notes for the lecturer. They have not been peer-reviewed and may contain inconsistent notation, typos, and omit citations of relevant works.

