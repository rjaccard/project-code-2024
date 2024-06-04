# Lecture 8: Approximation Algorithms using LPs 

In this lecture we do the following:

- We give a randomized approximation algorithm for the Set Cover problem
- We show that the integrality gap of the set cover LP is $\Omega(\log n)$


## 1 Set Cover via Randomized Rounding

Let us now apply the framework to the Set Cover problem. It can be seen as a generalization of the vertex cover problem and its definition is as follows:

Definition 1 (Set Cover Problem) Given a universe $\mathcal{U}=\left\{e_{1}, e_{2}, \ldots e_{n}\right\}$, and a family of subsets $\mathcal{T}=\left\{S_{1}, S_{2}, \ldots S_{m}\right\}$ and a cost function $c: \mathcal{T} \rightarrow \mathbb{R}_{+}$, find a collection $C$ of subsets of minimum cost that cover all elements.

As for vertex cover, we start by giving an exact Integer LP formulation. For each $i \in\{1, \ldots m\}$, define $x_{i}$, which is 1 if $S_{i} \in C$, and 0 otherwise. The objective function is

$$
\min \sum_{i=1}^{m} x_{i} \cdot c\left(S_{i}\right)
$$

and for each element $e \in \mathcal{U}$, we add the constraint $\sum_{S_{i}: e \in S_{i}} x_{i} \geq 1$. This ensures that each element is covered by at least one set in $C$. And for each $x_{i}$, we require that $x_{i} \in\{0,1\}$ in the ILP. The LP relaxation is then obtained by replacing the boolean constraints $x_{i} \in\{0,1\}$ by $x_{i} \in[0,1]$.

Now suppose that each element belongs to at most $f$ sets. Then, as in your exercise on vertex cover on $k$-uniform hypergraphs, we can do the following rounding: $C=\left\{S_{i}: x_{i}^{*} \geq \frac{1}{f}\right\}$. In each constraint, there's at least one $x_{i}^{*}$ which is at least $\frac{1}{f}$, so each constraint is satisfied. Using the same reasoning as in the analysis of the vertex cover rounding, we can show that this approximation is within a factor of $f$.

### 1.1 A better approximation for Set Cover

If we introduce randomness and allow our algorithm to output non-feasible solutions with some small probability, we can get much better results (in expectation).

We use the same LP as in the previous section, and will run the following algorithm:

1. Solve the LP to get an optimal solution $x^{*}$.
2. Choose some positive integer constant $d$ (we will see later how $d$ affects the guarantees we get). Start with an empty result set $C$, and repeat step $3 d \cdot \ln (n)$ times.
3. For $i=1, \ldots m$, add set $S_{i}$ to the solution $C$ with probability $x_{i}^{*}$, choosing independently for each set.

Now let us analyze what guarantees we can get:[^0]

Claim 2 The expected cost of all sets added in one execution of Step 3 is

$$
\sum_{i=1}^{m} x_{i}^{*} c\left(S_{i}\right)=L P_{O P T}
$$

Proof

$$
\mathbb{E}[\text { rounded cost }]=\sum_{i=1}^{m} c\left(S_{i}\right) \operatorname{Pr}\left[S_{i} \text { is added }\right]=\sum_{i=1}^{m} c\left(S_{i}\right) x_{i}^{*}=L P_{O P T}
$$

From this, we can immediately derive

Corollary 3 The expected cost of $C$ after $d \cdot \ln (n)$ executions of Step 3 is at most

$$
d \cdot \ln (n) \cdot \sum_{i=1}^{m} c\left(S_{i}\right) x^{*} \leq d \cdot \ln (n) \cdot L P_{O P T} \leq d \cdot \ln (n) \cdot O P T
$$

Note that we have $L P_{O P T} \leq O P T$ because $L P$ is a relaxation of the original problem, so its optimum can only be better.

That sounds good, but we should also worry about feasibility:

Claim 4 The probability that a constraint remains unsatisfied after a single execution of Step 3 is at most $\frac{1}{e}$.

Proof Suppose our constraint contains $k$ variables, and let us write it as $x_{1}+x_{2}+\cdots+x_{k} \geq 1$. Then,

$$
\begin{align*}
\operatorname{Pr}[\text { constraint unsat. }] & =\operatorname{Pr}\left[S_{1} \text { not taken }\right] \ldots \operatorname{Pr}\left[S_{k} \text { not taken }\right] \\
& =\left(1-x_{1}^{*}\right) \ldots\left(1-x_{k}^{*}\right) \\
& \leq e^{-x_{1}^{*}} \cdot \ldots \cdot e^{-x_{k}^{*}}  \tag{1}\\
& =e^{-\sum_{i=1}^{k} x_{i}^{*}} \\
& \leq e^{-1} \tag{2}
\end{align*}
$$

where (1) follows from the inequality $1-x \leq e^{-x}$ and (2) from the fact that $\sum_{i} x_{i}^{*} \geq 1$.

Claim 5 The output $C$ is a feasible solution with probability at least $1-\frac{1}{n^{d-1}}$.

Proof Using claim 4, we find that the probability that a given constraint is unsatisfied after $d \cdot \ln (n)$ executions of step 3 is at most

$$
\left(\frac{1}{e}\right)^{d \cdot \ln (n)}=\frac{1}{n^{d}}
$$

and by union-bound, the probability that there exists any unsatisfied constraint is at most

$$
n \cdot \frac{1}{n^{d}}=\frac{1}{n^{d-1}}
$$

Now we have an expected value for the cost, and also a bound on the probability that an infeasible solution is output, but we still might have a bad correlation between the two: It could be that all feasible outputs have a very high cost, and all infeasible outputs have a very low cost.

The following claim deals with that worry.

Claim 6 The algorithm outputs a feasible solution of cost at most $4 d \ln (n) O P T$ with probability greater than $\frac{1}{2}$.

Proof Let $\mu$ be the expected cost, which is $d \ln (n) \cdot O P T$ by corollary 3 . We can upper-bound the bad event that the actual cost is very high: By Markov's inequality, we have $\operatorname{Pr}[$ cost $>4 \mu] \leq \frac{1}{4}$. The other bad event that we have to upper bound is that the output is infeasible, and by claim 5 , we know that this happens with probability at most $\frac{1}{n^{(d-1)}} \leq \frac{1}{n}$. Now in the worst case, these two bad events are completely disjoint, so the probability that no bad event happens is at least $1-\frac{1}{4}-\frac{1}{n}$, and if we suppose that $n$ is greater than 4 , this probability is indeed greater than $\frac{1}{2}$.

We have thus designed a randomized $O(\log n)$-approximation algorithm for the set cover problem.

We remark that the used framework has the following general advantage (compared to worst-case guarantees): we can often get better per-instance guarantee than the general approximation factor: Suppose we have an instance where $L P_{O P T}=100$, and our algorithm found a solution of cost 110. Since we know that $L P_{O P T} \leq O P T$, we can say that our solution on this instance is at most $10 \%$ away from the optimal solution for this instance.

## 2 Integrality gap of the set cover LP

Consider the following instance of the Set Cover problem. For an even integer $d \geq 1$ let

$$
U=\left\{x \in\{0,1\}^{d}: \sum_{i=1}^{d} x_{i}=d / 2\right\}
$$

i.e., the universe consists of all binary vectors of length $d$ that have $d / 2$ nonzeros. Let the collection $\mathcal{F}$ contain $m=d$ sets $S_{1}, \ldots, S_{m}$, defined by

$$
S_{i}=\left\{x \in U: x_{i}=1\right\}
$$

for every $i=1, \ldots, m$. All costs are 1 .

We first give a feasible solution to the LP relaxation of Set Cover on the instance above with value bounded by 2 . The LP relaxation of the set cover problem is the following:

$$
\begin{aligned}
& \quad \min _{z} \sum_{i=1}^{d} z_{i}, \text { st.: } \\
& \forall i \in[d]: z_{i} \in[0,1] \\
& \forall x \in U: \sum_{i: x \in S_{i}} z_{i} \geq 1
\end{aligned}
$$

A solution to this with value 2 is to set every variable $z_{i}$ to $2 / d$. That way $\sum_{i} z_{i}=2$ and all constraints are satisfied:

$$
\sum_{i: x \in S_{i}} z_{i}=\sum_{i: x_{i}=1} z_{i}=\sum_{i: x_{i}=1} 2 / d=\sum_{i=1}^{n} 2 / d \cdot x_{i}=1
$$

Suppose we have any collection of $d / 2$ sets $\mathcal{F}^{\prime} \subseteq \mathcal{F}$. We can characterise $\mathcal{F}^{\prime}$ as $\left\{S_{i}: i \in \mathcal{I}\right\}$ for some $\mathcal{I} \subseteq\{1, \ldots, d\}$ with $|\mathcal{I}|=d / 2$. Let us then define the vector $x^{*}$ such that $x_{i}^{*}=0$ for $i \in \mathcal{I}$ and $x_{i}^{*}=1$ for $i \notin \mathcal{I}$. Then $x^{*} \in U$ but $x^{*} \notin \cup \mathcal{F}$, thus proving that $\mathcal{F}$ does not cover $U$. In this set cover problem the optimal integral solution is at least $d / 2+1$, but the optimal fractional solution is at most 2 . This is an $\Omega(d)$ integrality gap. Since the size of the universe, $|U|=\binom{d}{d / 2} \leq 2^{d}$, this translates to an $\Omega(\log |U|)$ integrality gap.

## 3 The Multiplicative Weights Algorithm

Multiplicative weights is a retronym for the simple iterative rule that underlies modular, iterative algorithms for solving LPs and SDPs (semidefinite programs) ${ }^{3}$. The Multiplicative Weights Algorithm is known by diferent names in the various fields where it was (re)discovered. Check out the survey by Arora, Hazan and Kale [3]; our discussion will be based on their treatment. Due to its broad appeal, we will consider multiplicative weights in more generality than is needed for solving LPs and SDPs. In this lecture, we'll introduce some strategies for playing a prediction game.

### 3.1 Warmup: Prediction with Expert Advice

The following sequential game is played between an omniscient Adversary and an Aggregator who is advised by $N$ experts. Special cases of this game include predicting if it will rain tomorrow, or if the stock market will go up or down.

```
Strategy 1 Prediction with Expert Advice
    for $t=1 \ldots T$ do
        Each expert $i \in[N]$ advises either YES or NO
        Aggregator predicts either YES or NO
        Adversary, with knowledge of the expert advice and Aggregator's prediction, decides the YES/NO
    outcome
            Aggregator observes the outcome and suffers if his prediction was incorrect.
    end for
```

Naturally, Aggregator wants to make as few mistakes as possible. Since the experts may be unhelpful and the outcomes may be capricious, Aggregator can hope only for a relative performance guarantee. In particular, Aggregator hopes to do as well as the best single expert in hindsight ${ }^{4}$. In order to do so, Aggregator must track which experts are helpful. We will consider a few tracking strategies. Almost every other aspect of the game - that advise is aggregated into a single value, that this value is binary, and even that the game is sequential - is not relevant; we will generalize or eliminate these aspects.

If there is a perfect expert, then an obvious strategy is to dismiss experts who are not perfect. With the remaining experts, take a majority vote. Whenever the Aggregator makes a mistake, at least half of the remaining experts are dismissed, so Aggregator makes at most $\log N$ mistakes ${ }^{5}$. We can use the same strategy even when there isn't a perfect expert, if we restart after every expert has been eliminated. If the best expert has made $M$ mistakes by time $T$, then Aggregator has restarted at most $M+1$ times, so it has made at most $(M+1) \cdot \log N$ mistakes. This bound is rather poor since it depends multiplicatively on $M$.

### 3.2 Fewer Mistakes with Weighted Majority

We may obtain an additive mistake bound by softening our strategy: instead of dismissing experts who erred, discount their advice. This leads to the Weighted Majority Algorithm of Littlestone and Warmuth [4]. Assign each expert $i$ a weight $w_{i}^{(1)}$ initialized to 1 . Then for every $t$, predict YES/NO based on the weighted majority vote and halve the mistaken experts' weights after observing the outcome. The game strategy then becomes:[^1]

```
Strategy 2 Prediction with Weighted Majority

Initialize $\mathbf{w}^{(1)}=\left(w_{1}^{(1)}, \ldots, w_{N}^{(1)}\right)$ to be a vector of 1 's

for $t=1 \ldots T$ do

    Each expert $i \in[N]$ advises either YES or NO

    Aggregator predicts either YES or NO based on a weighted majority vote using $\mathbf{w}^{(t)}$

    Adversary, with knowledge of the expert advice and Aggregator's prediction, decides the YES/NO outcome.

    Aggregator observes the outcome and for every mistaken expert $i$, set $w_{i}^{(t+1)} \leftarrow w_{i}^{(t)} / 2$

end for
```

Claim 7 For any sequence of outcomes, duration $T$, let $M_{W M}$ be the number of mistakes that the Weighted Majority strategy makes, and $M_{i}$ be the number of mistakes that expert $i$ makes. Then

$$
M_{W M} \leq 2.41 \cdot\left(M_{i}+\log N\right)
$$

Proof Let

$$
\Phi^{(t)}=\sum_{i \in[N]} w_{i}^{(t)}
$$

be a 'potential' function. Observe that:

- By definition, we have $\Phi^{(1)}=N$
- Also by definition, $\left(\frac{1}{2}\right)^{M_{i}} \leq \Phi^{(T+1)}$
- At any time $\tau$ when WM errs, at least half of the weight gets halved:

$$
\Phi^{(\tau+1)} \leq \frac{3}{4} \Phi^{(\tau)}
$$

This implies

$$
\Phi^{(T+1)} \leq\left(\frac{3}{4}\right)^{M_{W M}} \Phi^{(1)}
$$

Combining these facts yields

$$
\left(\frac{1}{2}\right)^{M_{i}} \leq\left(\frac{3}{4}\right)^{M_{W M}} N
$$

Taking the base-2 logarithm of both sides,

$$
-M_{i} \leq \log N+\log \left(\frac{3}{4}\right) M_{W M}
$$

so

$$
M_{W M} \leq \underbrace{\frac{1}{\log (4 / 3)}}_{\approx 2.41}\left(M_{i}+\log N\right)
$$

The leading constant is a consequence of our arbitrary choice to halve the weights. We can optimize $\epsilon$ in the update rule

$$
w_{i}^{(t+1)} \leftarrow w_{i}^{(t)} /(1+\epsilon)
$$

then using the WM strategy we may achieve

$$
M_{W M} \leq 2(1+\epsilon)\left(M_{i}+O(\log N / \epsilon)\right)
$$


[^0]:    ${ }^{1}$ Disclaimer: These notes were written as notes for the lecturer. They have not been peer-reviewed and may contain inconsistent notation, typos, and omit citations of relevant works.

[^1]:    ${ }^{2}$ This section corresponds to Lecture 16 in the course, which was scribed by Shiva Kaul

    ${ }^{3}$ See Lecture 17 in the course linked earlier

    ${ }^{4}$ The excess number of mistakes is called (external) regret

    ${ }^{5}$ We will use log to denote the binary logarithm

