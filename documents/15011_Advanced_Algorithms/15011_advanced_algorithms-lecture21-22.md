# Submodularity and Minimization 

In these notes, we introduce submodular functions, give examples, and explain how they can be minimized in polynomial time via Lovász extension.

## 1 Introduction to Set Functions and Submodularity

In this lecture we want to start our discussion on set functions with the focus on submodular functions. Let us begin with defining what a set function is.

Definition $1 A$ set function $f: 2^{N} \rightarrow \mathbb{R}$ is a function assigning a real value to every subset $S \subseteq N$ of a given ground set $N$.

Many examples of set functions can be interpreted as a measure of the value we think a collection of items has. We have already seen some examples of set functions "in disguise," when considering weighted optimization problems. For example, in the maximum weight matching problem we have a graph $G=(V, E)$, and a non-negative weight $w_{e}$ for each edge $e \in E$ and want to find a maximum weight set $M$ of edges from $E$ that form a matching in $G$. We can think of this as the problem of maximizing the set function:

$$
f(M)=\sum_{e \in M} w_{e}
$$

subject to the constraint that $M$ is a matching of $G$. Here, the value of a collection $M$ is simply the sum of the individual value of each of its elements. That is, each element $e$ has some inherent value $w_{e}$ that does not depend on the other elements we choose in $M$. In many settings, however, the value of an item may depend on whether we have already selected some other item(s). For example: consider a pair of shoes. The amount you would pay for the left shoe alone is not very large compared to the amount you would pay for both shoes together. In the other direction, suppose you are building a coin (or stamp, or Pokémon) collection. Once you have a coin of a particular type, the value of adding another coin of the same type is not so large anymore. In the rest of the lecture, we consider these types of item interactions in more detail. In particular, submodularity is a generalization of the sort of item dependencies captured in the second example above. Formally, we have the following.

Definition $2 A$ set function $f$ is submodular if

$$
f(A)+f(B) \geq f(A \cup B)+f(A \cap B)
$$

holds for all $A, B \subseteq N$.

In order to get more intuition about submodularity, let's think about the value of a single item may change.

Definition 3 Given a set function $f$, a set $S \subseteq N$ and an element $u \in N$ the marginal contribution of u to $S$ w.r.t. $f$ is defined as

$$
f(u \mid S)=f(S \cup\{u\})-f(S)
$$

If we interpret $f$ as assigning a value to collections of items, then $f(u \mid S)$ is precisely how much extra value we would gain by taking element $u$ when we had already taken all elements in $S$. Using this definition, we can give an alternative definition of submodular functions.

Lemma $4 A$ set function $f$ is submodular if and only if for all $A \subseteq B \subseteq N$ and each $u \in N \backslash B$ the following holds:

$$
f(u \mid A) \geq f(u \mid B)
$$

Proof First suppose that $f$ is submodular and consider two sets $A \subseteq B$. We will show that $f(u \mid A) \geq$ $f(u \mid B)$. Consider the sets $A \cup\{u\}$ and $B$. According to submodularity we have:

$$
\begin{aligned}
f(A \cup\{u\})+f(B) & \geq f(A \cup\{u\} \cup B)+f((A \cup\{u\}) \cap B) \\
f(A \cup\{u\})+f(B) & \geq f(\{u\} \cup B)+f(A) \\
f(A \cup\{u\})-f(A) & \geq f(\{u\} \cup B)-f(B) \\
f(u \mid A) & \geq f(u \mid B)
\end{aligned}
$$

where in the second line, we have used that $A \subseteq B$.

Now, let us assume $f(u \mid A) \geq f(u \mid B)$ for all $u$ and all $A \subseteq B$. We will show that $f$ must be submodular. Consider any two sets $C, D \subseteq N$. Let $h$ be the number of elements in $D \backslash C=\left\{d_{1}, d_{2}, \ldots, d_{h}\right\}$. Also let $D_{i}=\left\{d_{j}: 1 \leq j \leq i\right\}$. Then,

$$
\begin{aligned}
f(D)-f(C \cap D) & =\sum_{i=1}^{h} f\left((C \cap D) \cup D_{i}\right)-f\left((C \cap D) \cup D_{i-1}\right) \\
& =\sum_{i=1}^{h} f\left(d_{i} \mid(C \cap D) \cup D_{i-1}\right) \\
& \geq \sum_{i=1}^{h} f\left(d_{i} \mid\left(C \cup D_{i-1}\right)\right) \\
& =\sum_{i=1}^{h} f\left(D_{i} \cup C\right)-f\left(D_{i-1} \cup C\right) \\
& =f(C \cup D)-f(C)
\end{aligned}
$$

Note that $D_{0}=\emptyset, D_{h}=D \backslash C$ and that the first and last sums are telescopic. Hence, the first and last equalities hold. The other equalities follow by the definition of the marginal contribution. The inequality holds by assumption, since $(C \cap D) \cup D_{i-1} \subseteq C \cup D_{i-1}$. Rearranging, we get $f(C)+f(D) \geq$ $f(C \cup D)+f(C \cap D)$, as desired.

The alternative characterization given by Lemma 4 gives us some better intuition about submodularity. It says that a set function $f$ is submodular if and only if the marginal value of an element $u$ with respect to some set $S$ can only decrease (or stay the same) as more elements are chosen in $S$. That is, submodularity captures the common economic notion of diminishing returns. In some sense, submodularity can be thought of as a discrete analogue of concavity, since it implies that the "discrete derivative" $f(e \mid S)$ is non-increasing in $S$.

### 1.1 Examples of submodular functions

There are plentiful examples of useful and interesting submodular functions. Here we give some of our favorites. For the first three, we prove submodularity. For the remaining, we leave that as an exercise.

- Our first example is the function measuring the size of a cut in a graph $G=(V, E)$ induced by $(S, V \backslash S)$. Formally, we consider the ground set $V$ and the define the function $\delta: 2^{V} \rightarrow \mathbb{R}$ by

$$
\delta(S)=|\{(u, v): u \in S, v \in V \backslash S\}|
$$

for every subset of nodes $S \subseteq V$. To see that $\delta$ is submodular we want to measure the marginal contribution. Let $E(v, T)$ be the number of edges between some node $v$ and a set of nodes $T$.

$$
\delta(v \mid S)=E(v, V \backslash(S \cup\{v\}))-E(v, S)
$$

Observe that the first term on the right is decreasing in $S$ while the second term is increasing in $S$. Thus, the entire right hand side is decreasing in $S$. This proves the submodularity (via the "diminishing returns" definition given by Lemma 4).

- Consider a finite collection of sets $T_{1}, T_{2} \ldots, T_{n}$, where each $T_{i} \subseteq \mathbb{N}$ is a finite set. We consider the ground set $N=\{1,2, \ldots, n\}$ and set function $c: 2^{N} \rightarrow \mathbb{R}$ by:

$$
c(S)=\left|\bigcup_{i \in S} T_{i}\right|
$$

for every $S \subseteq N$. Intuitively $c$ measures the number of elements from $\mathbb{N}$ contained in the union of the sets specified by (indices from) $S$. This kind of function is often referred to as a coverage function. To show that $c$ is submodular we (again) analyze the marginal contribution of a set $T_{i}$ :

$$
c(i \mid S)=\left|T_{i} \cup \bigcup_{j \in S} T_{j}\right|-\left|\bigcup_{j \in S} T_{j}\right|=\left|T_{i} \backslash \bigcup_{j \in S} T_{j}\right|
$$

The last term is decreasing in $S$ which, as in the previous case, proves submodularity.

- Let $\mathcal{M}=(\mathcal{I}, X)$ be a matroid on ground set $X$. The rank function $r: 2^{X} \rightarrow \mathbb{R}$ of the matroid is defined by $r(A)=\max _{I \in \mathcal{I} \cap A}|I|$ for every $A \subseteq X$. That is, $r(A)$ is the size of a maximal independent containing only the elements in $A$. We will show that $r$ is submodular. Consider any two subsets $A$ and $B$ of $X$. Let $C$ be any maximal independent set of $\mathcal{M}$ contained in $A \cap B$. By the matroid augmentation axiom, we can extend $C$ to a maximal independent set $D$ contained in $A \cup B$. Then:

$r(A \cup B)+r(A \cap B)=|D|+|C| \leq|D \cap(A \cup B)|+|D \cap(A \cap B)|=|D \cap B|+|D \cap A| \leq r(B)+r(A)$.

the penultimate equality follows from the inclusion-exclusion principle, and the last inequality follows since both $D \cap B$ and $D \cap A$ must be independent (as they are subsets of an independent set $D$ ) and are contained in $B$ and $A$, respectively.

- When summarizing data the utility function is often submodular. This is for the same reason as in the previous coin collection example. Suppose e.g. you wish to summarize all the photos of animals in Switzerland. It is better to select one goat and one horse than two horses or two goats. This is exactly the diminishing returns property.
- Another example is influence maximization: suppose you wish to select $k$ persons to give free samples to in order to launch your product. You wish to select $k$ persons that have the maximum influence: they tell the most people about the product. As you will see in the exercise session, this can again be modeled as the problem of maximizing a submodular function subject to a cardinality constraint.
- Our final example is from information theory. Let $x_{1}, x_{2}, \ldots, x_{n}$ be discrete random variables. For any $A \subseteq[n]$, let $H(A)$ be the joint entropy of the variables $\left\{x_{i}\right\}_{i \in A}$. In other words, $H(A)=$ $-\sum_{a} \mathbb{P}\left[\left\{x_{i}\right\}_{i \in A}=a\right] \log \left(\mathbb{P}\left[\left\{x_{i}\right\}_{i \in A}=a\right]\right)$. One can see that $H$ is a submodular function.


## 2 Submodular function minimization

Next, we will start concerning ourselves with some algorithmic problems concerning submodular functions. Since we will want that our algorithms are efficient, a first issue is how the examined submodular function is given to us as part of the input. Clearly, providing the value of such a function for every possible subset of the ground set $N$ might require a lot of space (exponential in $|N|$ ), while nearly every interesting problem concerning submodular functions suddenly becomes trivial, as we can go over all subsets of $N$ in linear time and find the one that satisfies the requirements of the examined problem (e.g. if we are interested in minimizing a submodular function, we can find the subset of $N$ with the minimum value). Also the space requirement $2^{|N|}$ is unreasonable in most settings.

Therefore, from now on we will assume that $f$ is given in the form of access to an oracle, i.e., for every $S \subseteq N$ we can in constant time query the value $f(S)$. That is, the encoding of $f$ is not considered part of the input.

We have already developed some intuition that submodularity is like a discrete form of concavity. Strangely enough, we now show that it is also connected to convexity. The first problem we will examine is called unconstrained submodular function minimization, which is the problem of finding some $S \subseteq N$ on which $f$ takes its minimum value:

$$
f(S)=\min _{S^{\prime} \subseteq N} f\left(S^{\prime}\right)
$$

As we will see, this is a quite rare case of a problem of substantial interest that we can solve exactly in polynomial time. The way we will do this is by showing that it is equivalent to finding the global minimum of a certain convex continuous function, a problem we can solve using the so-called ellipsoid method in polynomial time. To be more precise, in order to minimize a (bounded) convex function $g$ with the ellipsoid method ${ }^{1}$, it is sufficient to solve the following problem: given an input $x$, either decide that $x$ is an optimal solution or, if not, compute a (sub)gradient $\nabla g(x)$ in polynomial time. To use this framework, we need to extend $f$ from a discrete function to a continuous function.

### 2.1 Lovász Extension

We want to use the general framework for minimizing a convex function to solve the problem of minimizing a submodular function $f: 2^{N} \rightarrow \mathbb{R}$. To do this, we will define an extension $\hat{f}$ of $f$. The definition itself makes sense for an arbitrary set function $f: 2^{N} \rightarrow \mathbb{R}$. However, $\hat{f}$ will be convex if and only if $f$ is submodular.

First, we think of $f: 2^{N} \rightarrow \mathbb{R}$ as $f:\{0,1\}^{n} \rightarrow \mathbb{R}$ by associating a set $S$ with its $0-1$ indicator from $\{0,1\}^{n}$ where $n=|N|$. We shall also let $N=[n]=\{1,2, \ldots, n\}$ and interchangeably use $[n]$ and $N$ for the ground set.

Definition 5 Let $f:\{0,1\}^{n} \rightarrow \mathbb{R}$. Define $\hat{f}:[0,1]^{n} \rightarrow \mathbb{R}$, the Lovász extension of $f$, by

$$
\hat{f}(z)=\underset{\lambda \sim[0,1]}{\mathbb{E}}\left[f\left(\left\{i: z_{i} \geq \lambda\right\}\right)\right] \quad \text { for every } z \in[0,1]^{n}
$$

where $\lambda \sim[0,1]$ denotes a uniformly random sample from the interval $[0,1]$.

Why is $\hat{f}$ an extension of $f$ ? Let $z \in\{0,1\}^{n}$. Then notice that for any $\lambda \in(0,1],\left\{i \mid z_{i} \geq \lambda\right\}=S$ where $S=\left\{i \mid z_{i}=1\right\}$. Thus $\hat{f}$ agrees with $f$ over the hypercube (all 0-1 points) and is some kind of average of $f$ at fractional points.[^0]

We can in fact explicitly find out this averaging representation of $\hat{f}(z)$. To do this, we define a "chain" of sets associated with any $z \in[0,1]^{n}$. For simplicity of notation, assume that $z_{0}=1 \geq z_{1} \geq z_{2} \geq \ldots \geq$ $z_{n} \geq 0=z_{n+1}$. Let $S_{i}$ for any $i \in[n] \cup\{0\}$ equal $\{1,2, \ldots, i\}$. Then, $S_{0}=\emptyset \subseteq S_{1} \subseteq S_{2} \subseteq \cdots \subseteq S_{n}=[n]$.

Further notice that if $\lambda \in\left[z_{i}, z_{i+1}\right.$ ) (the probability of which is equal to $z_{i}-z_{i+1}$ ) for any $i \in[n] \cup\{0\}$, then $\left\{j \mid z_{j} \geq \lambda\right\}=S_{i}$. Thus,

$$
\begin{equation*}
\hat{f}(z)=\sum_{i=0}^{n}\left(z_{i}-z_{i+1}\right) f\left(S_{i}\right) \tag{1}
\end{equation*}
$$

In particular, we can evaluate $\hat{f}$ at any $z$ efficiently and we only need $n+1$ calls to the evaluation oracle.

### 2.2 Lovàsz Extension is Convex iff $f$ is Submodular

The key result that allow us to minimize submodular functions in polynomial time is the following:

Theorem 6 Let $\hat{f}$ be the Lovàsz extension of $f:\{0,1\}^{n} \rightarrow \mathbb{R}$. Then, $\hat{f}$ is convex iff $f$ is submodular.

Proof We will only show the "if" part - that is, if $f$ is submodular then $\hat{f}$ is convex. This is what is needed for our minimization algorithm. The proof is a neat application of LP Duality and is a reminder that duality is not only useful in algorithm design but also a powerful method of arguing structural properties especially in situations where one can define the quantity of interest as the optimum value of a linear program.

We will assume that $f(\emptyset)=0$. This is without loss of generality as otherwise we can define a new function $f^{\prime}=f-f(\emptyset)$ which satisfies $f^{\prime}(\emptyset)=0$ and is just a shifted version of $f$.

In Definition 5, we have a definition of the Lovász extension via an explicit formula. We now give a second definition of the same function as an optimum of a linear program. Specifically, for $z \in[0,1]^{n}$ and $f$, the submodular function above, consider the following linear program (with exponentially many constraints):

$$
\begin{aligned}
g(z)=\max _{x} & z^{\top} x \\
\text { subject to: } & \sum_{i \in S} x_{i} \leq f(S) \quad \forall S \subseteq N \\
& \sum_{i \in N} x_{i}=f(N)
\end{aligned}
$$

We will call it the primal (P) program. Our main claim is that $g(z)=\hat{f}(z)$ for every $z \in[0,1]^{n}$. In other words, the LP optimum above is an alternate definition of $\hat{f}(z)$.

To see why this helps, we observe that $g$ is convex. The idea is simple and general, the maximum of a linear function over a convex set is always convex. Concretely, for $0 \leq \lambda \leq 1$ and $z_{1}, z_{2} \in[0,1]^{n}$, observe that $g\left(\lambda z_{1}+(1-\lambda) z_{2}\right)=\max _{x}\left(\lambda z_{1}^{\top} x+(1-\lambda) z_{2}^{\top} x\right) \leq \lambda \max _{x} z_{1}^{\top} x+(1-\lambda) \max _{x} z_{2}^{\top} x=$ $\lambda g\left(z_{1}\right)+(1-\lambda) g\left(z_{2}\right)$, where the maximum is taken over the $x$ 's that are feasible to the above linear program $(\mathrm{P})$.

Thus, proving $\hat{f}=g$ completes the proof. To show this, we will use weak duality. Verify that the dual linear program $(\mathrm{D})$ to $(\mathrm{P})$ is given by:

$$
\begin{aligned}
& \min \sum_{S \subseteq N} y_{S} f(S) \\
& \text { subject to: } \quad \sum_{S \ni i} y_{S}=z_{i} \quad \forall i \in N \\
& y_{S} \geq 0 \quad \forall S \subsetneq N
\end{aligned}
$$

How does this help us? For a fixed $z \in[0,1]^{n}$, we want to prove that the optimum value of (P) is $\hat{f}(z)$. We will do this by "guessing" the optimal solutions to (P) and (D) (you'll see why it's intuitive to guess these solutions, especially when you know what we want to prove). Given such a guess, how do we verify that they are indeed optimal?

By weak duality, for any $x$ feasible for (P) and $y$ feasible for (D), $z^{\top} x \leq \sum_{S \subseteq N} y_{S} f(S)$. So if our guesses $x^{*}$ for $(\mathrm{P})$ and $y^{*}$ for (D) it so happens that $z^{\top} x=\sum_{S \subset N} y_{S} f(S)$, then $x^{*}$ and $y^{*}$ have to be optimal solutions for the respective linear programs as any better solution will violate weak duality!

For notational convenience, assume (without loss of generality by relabeling coordinates) that $z_{0}=$ $1 \geq z_{1} \geq z_{2} \geq \ldots \geq z_{n} \geq 0=z_{n+1}$. Further, let $S_{i}$ for any $i \in[n] \cup\{0\}$ equal $\{1,2, \ldots, i\}$. We define $x^{*}$ by: $x_{i}^{*}=f\left(S_{i}\right)-f\left(S_{i-1}\right)$ for every $i \in[n]$ and $y^{*}$ by:

$$
y_{S}^{*}= \begin{cases}z_{i}-z_{i+1} & \text { for } S=S_{i} \text { with } i \in[n] \\ 0 & \text { otherwise }\end{cases}
$$

We now make four claims about $x^{*}$ and $y^{*}$ which will complete the proof. First, we establish that $z^{\top} x^{*}=\hat{f}(z)$

CLAIM 1: $z^{\top} x^{*}=\hat{f}(z)$.

Next, we claim that the weak duality condition is satisfied by equality for $x^{*}$ and $y^{*}$.

CLAIM 2: $z^{\top} x^{*}=\sum_{S \subseteq N} y_{S} f(S)$.

And finally,

CLAIM 3: $y^{*}$ is feasible for $(D)$.

CLAIM 4: $x^{*}$ is feasible for $(\mathrm{P})$.

Using our discussion from above, the above claims complete the proof. Let us now verify them one by one. First,

$$
\begin{align*}
z^{\top} x^{*} & =\sum_{i=1}^{n} z_{i} \cdot\left(f\left(S_{i}\right)-f\left(S_{i-1}\right)\right)  \tag{2}\\
& =\sum_{i=0}^{n}\left(z_{i}-z_{i+1}\right) f\left(S_{i}\right)  \tag{3}\\
& =\sum_{S \subseteq N} y_{S}^{*} f(S) \tag{4}
\end{align*}
$$

(3) along with (1) establishes Claim 1. (4) establishes Claim 2. Let us now proceed to Claims 3 and 4. Observe that $y^{*}$ has all non-negative entries because $z_{i} \geq z_{i+1}$ for every $i$. Further, for any $i$,

$$
\sum_{S: S \ni i} y_{S}^{*}=\sum_{j \geq i} y_{S_{j}}^{*}=\left(z_{i}-z_{i+1}\right)+\left(z_{i+1}-z_{i+2}\right)+\cdots+\left(z_{n-1}-z_{n}\right)+\left(z_{n}-z_{n+1}\right)=z_{i}-z_{n+1}=z_{i}
$$

as required. This establishes that $y^{*}$ is feasible for (D).

Let us now finally come to Claim 4. Observe that $\sum_{i \in[n]} x_{i}^{*}=\sum_{i \leq n}\left(f\left(S_{i}\right)-f\left(S_{i-1}\right)\right)=f([n])-$ $f(\emptyset)=f([n])$ using that $f(\emptyset)=0$. Let $S \subsetneq[n]$. Then, we must show that $\sum_{i \in S} x_{i}^{*} \leq f(S)$. We will argue this by induction on the size of the set $S$. The base case trivially holds as $f(\emptyset)=0 \geq \sum_{i \in \emptyset} x_{i}^{*}$. Let us now prove the inductive case (observe that so far we haven't used the submodularity of $f-$ this is the part of the argument it comes in).

Let $i$ be the largest index in $S$. By definition of submodularity, $f(S)+f\left(S_{i-1}\right) \geq f\left(S \cup S_{i-1}\right)+f(S \cap$ $\left.S_{i-1}\right)=f\left(S_{i}\right)+f(S \backslash\{i\})$ which can be rearranged to

$$
f(S) \geq f\left(S_{i}\right)-f\left(S_{i-1}\right)+f(S \backslash\{i\})=x_{i}^{*}+f(S \backslash\{i\}) \geq \sum_{i \in S} x_{i}^{*}
$$

where we used the inductive hypothesis in the final inequality. This completes the proof of Claim 4.

### 2.3 Some remarks

- The arguments presented in these notes present the "core" of why we can minimize submodular functions efficiently. To obtain faster algorithms than that given by the Ellipsoid method is a very active research area.
- Using the Ellipsoid method, one can in fact show that we can in polynomial time minimize the Lovász extension subject to (polynomially) many inequalities.
- In contrast, maximizing a submodular function generalizes the max cut problem and is thus NPhard.
- In the proof of Theorem 6 , we showed that the Lovász extension equals the optimum value to the linear program (P). By strong duality, we also have that it equals the optimum value of the dual (D). One can see that implies that the Lovász extension is the convex closure of $f$. The convex closure $f^{-}$of $f$ is a function $f^{-}:[0,1]^{n} \rightarrow \mathbb{R}$ such that, if $D^{-}(z)$ for $z \in[0,1]^{n}$ is a distribution on subsets of $N$ with marginal probabilities given by $z$ (i.e. $\operatorname{Pr}_{S \sim D^{-}(z)}[u \in S]=z_{u}$ ) which minimizes

$$
\underset{S \sim D^{-}(z)}{\mathbb{E}}[f(S)]
$$

then $f^{-}(z)=\mathbb{E}_{S \sim D^{-}(z)}[f(S)]$.


[^0]:    ${ }^{1}$ Recall that a function $g$ is convex if $\left.g(\lambda x+(1-\lambda) y)\right) \leq \lambda g(x)+(1-\lambda) g(y)$ for all $\lambda \in[0,1]$ and inputs $x$ and $y$.

