# Submodularity and Maximization 

In this lecture, we consider the problem of maximizing a submodular function. We use the same notation as last lecture. We assume that all functions $f: 2^{N} \rightarrow \mathbb{R}$ we deal with in this lecture are

- non-negative: $f(S) \geq 0$ for all $S \subseteq N$,
- and normalized: $f(\emptyset)=0$.

Suppose also that $f: 2^{N} \rightarrow \mathbb{R}$ is monotone: $f(S) \leq f(T)$ for all $S \subseteq T \subseteq N$. Then, we must have $f(N) \geq f(S)$ for any other $S \subseteq N$, so unconstrained maximization is trivial in this case. However, the following constrained problem arises naturally in many settings: we are given a parameter $k$, and must find a set $S \subseteq N$ of size at most $k$ that maximizes $f$. Natural applications of this setting is e.g. data summarization and influence maximization.

## 1 Cardinality Constrained Monotone Maximization

Recall that for weighted maximization problems with linear objective, this problem is solved optimally by the greedy algorithm. This result in fact holds even if we replace the constraint that $|S| \leq k$ by a general matroid constraint. The natural generalization of the greedy algorithm to submodular functions is as follows: at each step, we choose the element $u \notin S$ with maximal marginal gain $f(u \mid S)$ and add $u$ to $S$.

Input: Ground set $N$, value oracle for monotone submodular $f: 2^{N} \rightarrow \mathbb{R}$, parameter

$$
0 \leq k \leq|N| .
$$

Output: $S \subseteq N$ with $|S| \leq k$

$S \leftarrow \emptyset$;

for $i=1$ to $k$ do

Let $u_{i}=\arg \max _{u \in N \backslash S} f(u \mid S)$

$S \leftarrow S \cup\left\{u_{i}\right\} ;$

return $S$

Notice that if $f(S)=\sum_{e \in S} w_{e}$ for some set of weights $w$, this is indeed exactly the standard greedy algorithm. Here, however, we find that the algorithm can produce a suboptimal solution. Consider a coverage function with sets:

$$
\begin{aligned}
& T_{1}=\{1,2,3,4\} \\
& T_{2}=\{1,2,5\} \\
& T_{3}=\{3,4,6\}
\end{aligned}
$$

Suppose $k=2$. Then, the greedy algorithm first selects $T_{1}$ and then takes either $T_{2}$ or $T_{3}$. This covers 5 total elements. However, taking $T_{2}$ and $T_{3}$ covers 6 elements!

Despite this, we can show that the greedy algorithm gives a constant factor approximation. Let's start by proving a simple claim that holds for any submodular function:

Lemma 1 Let $f: 2^{N} \rightarrow \mathbb{R}$ be a submodular function and let $S, T \subseteq N$. Then, $\sum_{e \in T \backslash S} f(e \mid S) \geq$ $f(T \cup S)-f(S)$.

Proof Order the elements of $T \backslash S$ as $e_{1}, e_{2}, \ldots, e_{|T \backslash S|}$ and let $T_{i}$ be the set containing the first $i$ elements in this ordering. Observe that $T_{0}=\emptyset$ and $T_{|T \backslash S|}=T \backslash S$. Then,

$$
\begin{aligned}
\sum_{e \in T \backslash S} f(e \mid S) & =\sum_{i=1}^{|T \backslash S|} f\left(e_{i} \mid S\right) \\
& \geq \sum_{i=1}^{|T \backslash S|} f\left(e_{i} \mid S \cup T_{i-1}\right) \\
& =\sum_{i=1}^{|T \backslash S|} f\left(T_{i} \cup S\right)-f\left(T_{i-1} \cup S\right) \\
& =f\left(T_{|T \backslash S|} \cup S\right)-f\left(T_{0} \cup S\right) \\
& =f(T \cup S)-f(S)
\end{aligned}
$$

Here, we have used submodularity for the inequality, and then noted that the sum is telescoping.

We can now prove the following result:

Theorem 2 Let $S$ be the set produced by the greedy algorithm for maximizing a monotone submodular function $f$ subject to a cardinality constraint $k$. Let $O$ be any set of at most $k$ elements. Then, $f(S) \geq$ $(1-1 / e) f(O) \approx 0.632 f(O)$.

Proof Notice that since $f$ is monotone, we can assume that $|O|=k$, since we can always add elements to it if this is not the case without decreasing its value.

Let $u_{i}$ be the $i$ th element selected by the greedy algorithm and let $S_{i}$ be the set $\left\{u_{j}: j \leq i\right\}$ containing the first $i$ elements selected. Note that $S_{0}=\emptyset$ and $S_{k}=S$. Consider an iteration $i$ and let $e$ be any element in $O \backslash S_{i-1}$. Then, by our greedy choice we have:

$$
f\left(u_{i} \mid S_{i-1}\right) \geq f\left(e \mid S_{i-1}\right)
$$

We have one such inequality for each $e \in O \backslash S_{i-1}$. Adding them all together and applying Lemma 1, we get:

$$
\left|O \backslash S_{i-1}\right| \cdot f\left(u_{i} \mid S_{i-1}\right) \geq \sum_{e \in O \backslash S_{i-1}} f\left(e \mid S_{i-1}\right) \geq f\left(S_{i-1} \cup O\right)-f\left(S_{i-1}\right) \geq f(O)-f\left(S_{i-1}\right)
$$

where the last inequality follows from the fact that $f$ is monotone. Now, note that $\left|O \backslash S_{i-1}\right| \leq k$ and also $f\left(u_{i} \mid S_{i-1}\right) \geq 0$ since $f$ is monotone. Thus,

$$
k \cdot f\left(u_{i} \mid S_{i-1}\right) \geq\left|O \backslash S_{i-1}\right| \cdot f\left(u_{i} \mid S_{i-1}\right) \geq f(O)-f\left(S_{i-1}\right)
$$

Dividing by $k$, and recalling the definition of $S_{i-1}$ and $S_{i}$, we get:

$$
f\left(S_{i}\right)-f\left(S_{i-1}\right)=f\left(u_{i} \mid S_{i-1}\right) \geq \frac{1}{k} f(O)-\frac{1}{k} f\left(S_{i-1}\right)
$$

Let's rearrange this to:

$$
\begin{equation*}
f\left(S_{i}\right) \geq\left(1-\frac{1}{k}\right) f\left(S_{i-1}\right)+\frac{1}{k} f(O) \tag{1}
\end{equation*}
$$

Notice that this gives a recurrence for $f\left(S_{i}\right)$. We now show by induction on $i$.

$$
\begin{equation*}
f\left(S_{i}\right) \geq\left(1-\left(1-\frac{1}{k}\right)^{i}\right) f(O) \tag{2}
\end{equation*}
$$

For $i=0$, we have $f\left(S_{0}\right)=f(\emptyset)=0=\left(1-\left(1-\frac{1}{k}\right)^{0}\right) f(O)$. For $i>0$, we have:

$$
\begin{aligned}
f\left(S_{i}\right) & \geq\left(1-\frac{1}{k}\right) f\left(S_{i-1}\right)+\frac{1}{k} f(O) \\
& \geq\left(1-\frac{1}{k}\right)\left(1-\left(1-\frac{1}{k}\right)^{i-1}\right) f(O)+\frac{1}{k} f(O) \\
& =\left(1-\left(1-\frac{1}{k}\right)^{i}\right) f(O)
\end{aligned}
$$

where we used (1) and the induction hypothesis in the first and second lines, respectively.

To complete the proof, it suffices to plug in $i=k$ in (2) and then note that $\left(1-\frac{1}{k}\right)^{k} \leq e^{-1}$ (since $1+x \leq e^{x}$, as is seen by considering Taylor series expansion of the exponential function).

We briefly remark that the approximation ratio of $(1-1 / e)$ is in fact the best possible for the general problem. If $f$ is somehow given to us explicitly, it is NP-hard to do better. Similarly, if $f$ is given as a value oracle (and so the only way to get information about it is to query values) then one can show that it is impossible to do better without making a super-polynomial number of value queries. This latter result is information-theoretic and holds even if $P=N P$.

## 2 Unconstrained Submodular Maximization

Now, suppose that $f$ is not monotone. Then, even without constraints, it makes sense to ask what set $S$ maximizes $f(S)$. One idea is to just run the greedy algorithm, and stop when no element gives any positive marginal gain (i.e. when $f(e \mid S) \leq 0$ for all $e \in N \backslash S$.

However, this algorithm performs very badly on the following example function. Let $N=\left\{u_{1}, u_{2}, \ldots u_{n}, v\right\}$. Then, define:

$$
f(S)= \begin{cases}2 & \text { if } v \in S \\ |S| & \text { if } v \notin S\end{cases}
$$

One can verify that $f$ is indeed submodular. The optimal solution chooses $S=\left\{u_{1}, u_{2}, \ldots u_{n}\right\}$ and has value $n$, but the greedy algorithm would choose $\{v\}$, and of value 2 .

### 2.1 A greedy deterministic $\frac{1}{3}$-approximation algorithm

So we need a better algorithm. We still use a greedy approach, but one which is "greedy from two sides" (one side being $\emptyset$ and the other being $N$ ):

```
Input: ground set $N$, value oracle for submodular function $f: 2^{N} \rightarrow \mathbb{R}$ Choose an arbitrary order $u_{1}, u_{2}, \ldots u_{n}$ on the elements.;

$X_{0} \leftarrow \emptyset ;$

$Y_{0} \leftarrow N ;$

for $i=1$ to $n$ do

Let $a_{i}=f\left(X_{i-1} \cup\left\{u_{i}\right\}\right)-f\left(X_{i-1}\right)$;

Let $b_{i}=f\left(Y_{i-1} \backslash\left\{u_{i}\right\}\right)-f\left(Y_{i-1}\right)$

if $a_{i} \geq b_{i}$ then

$X_{i} \leftarrow X_{i-1} \cup\left\{u_{i}\right\}$ and $Y_{i} \leftarrow Y_{i-1}$

else

$X_{i} \leftarrow X_{i-1}$ and $Y_{i} \leftarrow Y_{i-1} \backslash\left\{u_{i}\right\}$

return $X_{n}$ (which is equal to $Y_{n}$ ).
```

Theorem 3 The above algorithm is a $\frac{1}{3}$-approximation for unconstrained submodular maximization.

Before proving the theorem, we need some lemmas:

Lemma 4 For every $1 \leq i \leq n, a_{i}+b_{i} \geq 0$

Proof Notice that for all $i$, we have $X_{i-1} \subseteq Y_{i-1}$ and also $u_{i} \in Y_{i-1}$. Thus, we have:

$$
\begin{aligned}
& \left(X_{i-1} \cup\left\{u_{i}\right\}\right) \cap\left(Y_{i-1} \backslash\left\{u_{i}\right\}\right)=X_{i-1} \\
& \left(X_{i-1} \cup\left\{u_{i}\right\}\right) \cup\left(Y_{i-1} \backslash\left\{u_{i}\right\}\right)=Y_{i-1}
\end{aligned}
$$

We now apply submodularity:

$$
\begin{aligned}
a_{i}+b_{i} & =f\left(X_{i-1} \cup\left\{u_{i}\right\}\right)-f\left(X_{i-1}\right)+f\left(Y_{i-1} \backslash\left\{u_{i}\right\}\right)-f\left(Y_{i-1}\right) \\
& =f\left(X_{i-1} \cup\left\{u_{i}\right\}\right)+f\left(Y_{i-1} \backslash\left\{u_{i}\right\}\right)-\left[f\left(X_{i-1}\right)+f\left(Y_{i-1}\right)\right] \\
& \geq 0
\end{aligned}
$$

Let $O P T$ be the optimal solution of the problem, and define:

$$
O P T_{i}=\left(O P T \cup X_{i}\right) \cap Y_{i}
$$

Then, note that $O P T_{i}$ is obtained from $O P T$ by adding all of the elements added to $X_{i}$ by the algorithm and removing all of the elements removed from $Y_{i}$ by the algorithm. The idea of this definition is that we transform OPT into a set that agrees with what the algorithm has already done. We show the following.

Lemma 5 At each step $i$ :

$$
\left[f\left(X_{i}\right)+f\left(Y_{i}\right)\right]-\left[f\left(X_{i-1}\right)+f\left(Y_{i-1}\right)\right] \geq f\left(O P T_{i-1}\right)-f\left(O P T_{i}\right)
$$

Proof We prove the lemma in the case that $a_{i} \geq b_{i}$. The other case is similar. In this case, by Lemma 4 we must have $a_{i} \geq 0$. The algorithm sets $X_{i}=X_{i-1} \cup\left\{u_{i}\right\}$, and $Y_{i}=Y_{i-1}$, so the left-hand side of the inequality is just $f\left(u_{i} \mid X_{i-1}\right)=a_{i} \geq 0$. We also have $O P T_{i}=O P T_{i-1} \cup\left\{u_{i}\right\}$. If $u_{i} \in O P T$, then we have $O P T_{i}=O P T_{i-1}$, so the right-hand side is 0 and we are done. Suppose that $u_{i} \notin O P T$. Then, note that $O P T_{i-1} \subseteq Y_{i-1} \backslash\left\{u_{i}\right\}$. Thus, by submodularity:

$$
\begin{aligned}
f\left(O P T_{i}\right)-f\left(O P T_{i-1}\right)=f\left(u_{i} \mid O P T_{i-1}\right) & \geq f\left(u_{i} \mid\left(Y_{i-1} \backslash\left\{u_{i}\right\}\right)\right) \\
& =f\left(Y_{i-1}\right)-f\left(Y_{i-1} \backslash\left\{u_{i}\right\}\right)=-b_{i} \geq-a_{i}
\end{aligned}
$$

multiplying by -1 then gives

$$
f\left(O P T_{i-1}\right)-f\left(O P T_{i}\right) \leq a_{i}
$$

as required.

Now we have everything we need to prove Theorem 3. Initially we have $O P T_{0}=O P T$ and at the end we have $O P T_{n}=X_{n}=Y_{n}$. Intuitively Lemma 5 shows that each step our version $O P T_{i}$ of $O P T$ decrease in value, but this decrease is always matched by an increase in the value of either $X_{i}$ or $Y_{i}$, which should contribute the value of the solution we return. To make this formal, we sum the inequality of Lemma 5 over $i=1$ to $n$ :

$$
\sum_{i=1}^{n}\left[f\left(O P T_{i-1}\right)-f\left(O P T_{i}\right)\right] \leq \sum_{i=1}^{n}\left[f\left(X_{i}\right)+f\left(Y_{i}\right)-f\left(X_{i-1}\right)-f\left(Y_{i-1}\right)\right]
$$

Simplifying, and using that $f$ is non-negative we get:

$$
f\left(O P T_{0}\right)-f\left(O P T_{n}\right) \leq f\left(X_{n}\right)+f\left(Y_{n}\right)-f\left(X_{0}\right)-f\left(Y_{0}\right) \leq f\left(X_{n}\right)+f\left(Y_{n}\right)
$$

Finally, since $O P T_{0}=O P T$ and $O P T_{n}=X_{n}=Y_{n}$ we get:

$$
f(O P T) \leq 3 \cdot f\left(X_{n}\right)
$$

