## Solving LPs using Multiplicative Weights

In this lecture we do the following:

- We describe the Multiplicative Weight Update (actually Hedge) method.
- We then use this method to solve covering LPs.
- This is a very fast and simple (i.e., very attractive) method for solving these LPs approximately.


## 1 Recall last lecture

In the previous lecture, we saw how to use the weighted majority method in order to fairly smartly follow the advice of experts. Recall that the general game-setting with $T$ days and $N$ experts was as follows:

For $t=1, \ldots, T$ :

1. Each expert $i \in[N]$ gives some advice: UP or DOWN
2. Aggregator (you) predicts, based on the advice of the expert, UP or DOWN.
3. Adversary, with knowledge of the expert advice and the aggregator's decision, decides the UP/DOWN outcome.
4. Aggregator observes the outcome and suffers if his prediction was incorrect.

The weighted majority algorithm, parameterized by $\epsilon>0$ (the "learning rate"), now works as follows:

- Assign each expert $i$ a weight $w_{i}^{(1)}$ initialized to 1 . (All experts are equally trustworthy in the beginning.)

At each time $t$ :

- Predict UP/DOWN based on a weighted majority vote per $\vec{w}^{(t)}=\left(w_{1}^{(t)}, \ldots, w_{N}^{(t)}\right)$.
- After observing the cost vector, set $w_{i}^{(t+1)}=w_{i}^{(t)} \cdot(1-\varepsilon)$ for every expert $i \in[N]$ whose prediction was wrong. (Discount the trustworthiness of erroneous experts.)

Last lecture we analyzed the case when $\epsilon=1 / 2$. The same proof gives the following

Theorem 1 For any sequence of outcomes, duration $T$, and expert $i \in[N]$,

$$
\text { \# of WM mistakes } \leq 2(1+\epsilon) \cdot(\# \text { of } i \text { 's mistakes })+O(\log (N) / \epsilon)
$$[^0]

Proof [Sketch] The proof was done by defining a potential function: for each $t=1, \ldots, T+1$, let

$$
\Phi^{(t)}=\sum_{i \in[N]} w_{i}^{(t)}
$$

We now lower bound the "final" potential $\Phi^{(T+1)}$ using the number of mistakes of $i$. We then upper bound it in terms of our number of mistakes.

Lower bound: The weight of expert $i$ goes down by a factor $(1-\epsilon)$ for each mistake $i$ does. As the initial weight of $i$ is 1 ,

$$
\Phi^{(T+1)}=\sum_{j \in[N]} w_{j}^{(T+1)} \geq w_{i}^{(T+1)}=(1-\epsilon)^{\# \text { of } i \text { 's mistakes }}
$$

Upper bound: Every time WM errs, at least half the weight of the experts was wrong (since weighted majority was wrong). These weights are then decreased by $(1-\epsilon)$. It follows that the potential goes down by at least a factor $(1-\epsilon / 2)$ every time WM errs. And so

$$
\Phi^{(T+1)} \leq \Phi(1) \cdot(1-\epsilon / 2)^{\#} \text { of WM mistakes }=N \cdot(1-\epsilon / 2)^{\# \text { of WM mistakes }}
$$

where for the equality we used that $\Phi(1)=N$ since each expert was initialized with a weight of 1 .

The above bounds give us

$$
(1-\epsilon)^{\# \text { of } i \text { 's mistakes }} \leq \Phi^{(T+1)} \leq N \cdot(1-\epsilon / 2)^{\#} \text { of WM mistakes }
$$

Taking logs on both sides, simplifying and rearranging then gives us the statement.

## 2 Changing the game: allowing for randomized strategies

In the exercises, you proved that there are instances for which weighted majority does twice as many mistakes as the best expert! This is undesirable. To overcome this limitation, we will allow the aggregator to play a random strategy instead of always making a deterministic prediction (that the adversary then uses to create bad instances). A side note is that this is often a general strategy: randomization is often very good to limit the effect of adversaries.

Allowing for randomized strategies leads to the following game with $T$ days and $N$ experts:

```
For $t=1, \ldots, T$ :

1. Each expert $i \in[N]$ gives some advice.

2. Allocator picks some distribution $\vec{p}^{(t)}=\left(p_{1}^{(t)}, \ldots, p_{N}^{(t)}\right)$ over the experts.

3. Adversary, with knowledge of the expert advice and $\vec{p}^{(t)}$, determines a cost vector $\vec{m}^{(t)}=$

$\left(m_{1}^{(t)}, \ldots, m_{N}^{(t)}\right) \in[-1,1]^{N}$.

4. Allocator observes the cost vector and suffers $\vec{p}^{(t)} \cdot \vec{m}^{(t)}=\sum_{i \in[N]} p_{i}^{(t)} m_{i}^{(t)}$.
```

Note that in the above game, we have abstracted away the given advice and in fact Step 1 is not important. At each day $t$, the goal is to find a distribution $\vec{p}^{(t)}$ over the experts so as to minimize the suffering (the cost). For each day $t$, the adversary decides that the cost of following the $i$ 'th expert's
advice is $m_{i}^{(t)}$. Here, we have generalized the cost to be anything in $[-1,1]$ instead of only counting the number of mistakes. (A negative number means that it was profitable to follow that expert's advice.) As we play a randomized strategy, the expected cost incurred at day $t$ is thus

$$
\sum_{i \in[N]} \operatorname{Pr}[\text { aggregator follows expert } i \text { at day } t] \cdot m_{i}^{(t)}=\sum_{i \in[N]} p_{i}^{(t)} m_{i}^{(t)}=: \vec{p}^{(t)} \cdot \vec{m}^{(t)}
$$

The ultimate goal is to design a strategy that does as well as the best expert. That is, we wish to to find a strategy such that for every $i \in[N]$

$$
\underbrace{\sum_{t=1}^{T} \vec{p}^{(t)} \cdot \vec{m}^{(t)}}_{\text {our loss }} \leq \underbrace{\sum_{t=1}^{T} \vec{m}_{i}^{(t)}}_{\text {loss of best expert }}+(\text { small error terms })
$$

The Hedge strategy that we explain in the next section accomplishes this.

Example 1 A natural example of the above situation is when you investment money. You have the option to choose between say 4 different funds provided by Postfinance, UBS, Credit Suisse, and Banque cantonal. The probability $\vec{p}^{(t)}$ vector that you choose at day $t$ then corresponds to what fraction of your investment goes to the different funds. The goal is to update these fractions so as to make as much money as the best of the 4 options over the long run. Here the penalties (cost or profit) $\vec{m}^{(t)}$ that you observe reflects the performance of the different investments.

It is quite remarkable that you can do (almost) as good as the best possible option by doing rebalancing. HOWEVER, the caveat "almost" assumes that you live a very long life. For a small T, the guarantees get slightly worse.

## 3 The Hedge strategy

We now explain and analyze the Hedge strategy for the setting introduced in the last section. It is parameterized by the "learning parameter" $\epsilon>0$ :

- Initially, assign each expert $i$ a weight $w_{i}^{(1)}$ of 1. (All experts are equally trustworthy in the beginning.)

At each time $t$ :

- Pick the distribution $p_{i}^{(t)}=w_{i}^{(t)} / \Phi^{(t)}$ where $\Phi^{(t)}=\sum_{i \in[N]} w_{i}^{(t)}$.
- After observing the cost vector, set $w_{i}^{(t+1)}=w_{i}^{(t)} \cdot e^{-\varepsilon \cdot m_{i}^{(t)}}$.

The difference between Hedge and the so-called Multiplicative Weight Update method is the weightupdate $w_{i}^{(t+1)}=w_{i}^{(t)} \cdot e^{-\varepsilon \cdot m_{i}^{(t)}}$ instead of $w_{i}^{(t+1)}=w_{i}^{(t)} \cdot\left(1-\varepsilon \cdot m_{i}^{(t)}\right)$. Both methods have similar guarantees:

Theorem 2 Suppose $\epsilon \leq 1$ and for $t \in[T], \vec{p}^{(t)}$ is picked by Hedge. Then for any expert $i$,

$$
\sum_{t=1}^{T} \vec{p}^{(t)} \cdot \vec{m}^{(t)} \leq \sum_{t=1}^{T} m_{i}^{(t)}+\frac{\ln N}{\epsilon}+\epsilon T
$$

Note that in the above theorem, $i$ can be chosen to be the best expert and thus Hedge does as well as the best expert plus some small error terms.

Proof Similar to the analysis of the weighted majority strategy, the proof goes by analyzing the potential $\Phi^{t}=\sum_{i \in[N]} w_{i}^{(t)}$.

Lower bound on $\Phi^{(T+1)}$ : We lower bound the final potential as a function of $i$ 's performance:

$$
\Phi^{(T+1)}=\sum_{j \in[N]} w_{j}^{(T+1)} \geq w_{i}^{(T+1)}=\exp \left(-\epsilon \sum_{t=1}^{T} m_{i}^{(t)}\right)
$$

where the last equality follows from that the initial weight of $i$ was one and every day $t$ his weight was updated by $e^{-\epsilon m_{i}^{(t)}}$.

Upper bound on $\Phi^{(T+1)}$ : We upper bound the final potential in terms of the total cost Hedge suffered. By definition,

$$
\Phi^{(t+1)}=\sum_{j \in[N]} w_{j}^{(t+1)}=\sum_{j \in[N]} w_{j}^{(t)} \cdot \exp \left(-\epsilon m_{j}^{(t)}\right)
$$

The exponentiated term is in $[-1,1]$. Since $e^{x} \leq 1+x+x^{2}$ for $x \in[-1,1]$ (do a Taylor expansion),

$$
\begin{aligned}
\sum_{j \in[N]} w_{j}^{(t)} \cdot \exp \left(-\epsilon m_{j}^{(t)}\right) & \leq \sum_{j \in[N]} w_{j}^{(t)}\left(\left(1-\epsilon m_{j}^{(t)}+\epsilon^{2}\left(m_{j}^{(t)}\right)^{2}\right)\right. \\
& \leq \sum_{j \in[N]} w_{j}^{(t)}\left(\left(1-\epsilon m_{j}^{(t)}+\epsilon^{2}\right) \quad\left(\text { since }\left(m_{j}^{(t)}\right)^{2} \leq 1\right)\right. \\
& =\sum_{j \in[N]} w_{j}^{(t)}\left(1+\epsilon^{2}\right)-\sum_{j \in[N]} \epsilon w_{j}^{(t)} m_{j}^{(t)} \\
& =\Phi^{(t)}\left(1+\epsilon^{2}\right)-\epsilon \sum_{j \in[N]} \Phi^{(t)} p_{j}^{(t)} m_{j}^{(t)} \quad\left(\text { since } \Phi^{(t)} p_{j}^{(t)}=w_{j}^{(t)}\right) \\
& =\Phi^{(t)}\left(1+\epsilon^{2}-\epsilon \vec{p}^{(t)} \vec{m}^{(t)}\right) \\
& \leq \Phi^{(t)} \cdot \exp \left(\epsilon^{2}-\epsilon \vec{p}^{(t)} \vec{m}^{(t)}\right) \quad\left(\text { since } 1+x \leq e^{x}\right)
\end{aligned}
$$

We therefore have

$$
\begin{aligned}
\Phi^{(T+1)} \leq & \Phi^{(T)} \cdot \exp \left(\epsilon^{2}-\epsilon \vec{p}^{(T)} \vec{m}^{(T)}\right) \\
\leq & \Phi^{(T-1)} \cdot \exp \left(\epsilon^{2}-\epsilon \vec{p}^{(T-1)} \vec{m}^{(T-1)}\right) \cdot \exp \left(\epsilon^{2}-\epsilon \vec{p}^{(T)} \vec{m}^{(T)}\right) \\
& \vdots \\
\leq & \Phi^{(1)} \cdot \exp \left(\epsilon^{2} T-\epsilon \sum_{t=1}^{T} \vec{p}^{(t)} \vec{m}^{(t)}\right) \\
= & N \cdot \exp \left(\epsilon^{2} T-\epsilon \sum_{t=1}^{T} \vec{p}^{(t)} \vec{m}^{(t)}\right)
\end{aligned}
$$

where for the equality we used that $\Phi(1)=N$ since each expert was initialized with a weight of 1 .

The above bounds give us

$$
\exp \left(-\epsilon \sum_{t=1}^{T} m_{i}^{(t)}\right) \leq \Phi^{(T+1)} \leq N \cdot \exp \left(\epsilon^{2} T-\epsilon \sum_{t=1}^{T} \vec{p}^{(t)} \vec{m}^{(t)}\right)
$$

Taking (natural) logarithms,

$$
-\epsilon \sum_{t=1}^{T} m_{i}^{(t)} \leq \ln (N)+\epsilon^{2} T-\epsilon \sum_{t=1}^{T} \vec{p}^{(t)} \vec{m}^{(t)}
$$

and the final result follows by dividing by $\epsilon$ and rearranging the terms.

Remark The above proof may seem messy with all the inequalities. However, it follows a standard "framework": upper and lower bound the potential function. These Multiplicative Weight Update type of algorithms are most often analyzed using this potential argument. Once you know that cool argument, the analysis is almost automatic modulo some rewriting.

For the application of solving covering LPs, it will be convenient to consider the average cost incurred per day. We also generalize so that the cost vector can take values in $[-\rho, \rho]^{N}$ where $\rho$ is called the "width". The proof is the same by scaling and we get the following corollary:

Corollary 3 Suppose $\epsilon \leq 1$ and for $t \in[T]$, $\vec{p}^{(t)}$ is picked by Hedge and cost vectors satisfy $\vec{m}^{(t)} \in$ $[-\rho, \rho]^{N}$. If $T \geq\left(4 \rho^{2} \ln N\right) / \epsilon^{2}$, then for any expert $i$ :

$$
\frac{1}{T} \sum_{t=1}^{T} \vec{p}^{(t)} \cdot \vec{m}^{(t)} \leq \frac{1}{T} \sum_{t=1}^{T} m_{i}^{(t)}+2 \epsilon
$$

## 4 Hedging for LPs

We now turn to a nice application of the Hedge method to that of solving covering LPs. We start by defining these LPs.

### 4.1 Covering LPs

Definition 4 A linear program of the form :

$$
\begin{array}{cl}
\text { minimize } & \sum_{j=1}^{n} c_{j} x_{j} \\
\text { subject to } & A x \geq b \\
& 1 \geq x_{j} \geq 0 \quad \forall j
\end{array}
$$

is a covering linear program if

$$
A \in \mathbb{R}_{+}^{m \times n}, b \in \mathbb{R}_{+}^{m} \text { and } c \in \mathbb{R}_{+}^{n}
$$

This definition simply ensures that all the coefficients of the constraints and of the objective function are non-negative. Notice that both the set cover relaxation and the vertex cover relaxation that we saw in class were covering LPs.

Let us now introduce an example of a covering LP that we will reuse later:

$$
\begin{align*}
\operatorname{minimize} & x_{1}+2 x_{2}  \tag{1}\\
\text { subject to } & x_{1}+3 x_{2} \geq 2 \\
& 2 x_{1}+x_{2} \geq 1 \\
& 1 \geq x_{1}, x_{2} \geq 0
\end{align*}
$$

### 4.2 General idea

The idea of using the Hedge method for linear programming is to associate an expert with each constraint of the LP. In other words, the Hedge method will maintain a weight distribution over the set of constraints of a linear problem to solve, and to iteratively update those weights in a multiplicative manner based on the cost function at each step/day. Of course we need to define the cost function in a smart way later but let us first define the notion of an oracle and then give a small instructive example.

Initially, the Hedge method will give a weight $w_{i}^{(1)}=1$ for every constraint/expert $i=1, \ldots, m$ (the number $m$ of constraints now equals the number of experts). And at each day $t$, it will maintain a convex combination $\vec{p}^{(t)}$ of the constraints (that is defined in terms of the weights). Using such a convex combination $\vec{p}$, a natural easier LP with a single constraint is obtained by summing up all the constraints according to $\vec{p}$. Any optimal solution of the original LP is also a solution of this reduced problem, so the new problem will have at most the same cost as the previous one. We define an oracle for solving this reduced problem:

Definition 5 An oracle that, given $\vec{p}=\left(p_{1}, \ldots, p_{m}\right) \geq \mathbf{0}$ such that $\sum_{i=1}^{m} p_{i}=1$, outputs an optimal solution $x^{*}$ to the following reduced linear problem:

$$
\begin{array}{cl}
\text { minimize } & \sum_{j=1}^{n} c_{j} x_{j} \\
\text { subject to } & \left(\sum_{i=1}^{m} p_{i} A_{i}\right) \cdot x \geq \sum_{i=1}^{m} p_{i} b_{i} \\
& 1 \geq x \geq 0
\end{array}
$$

This linear problem is in practice much easier to solve than the original one and we can design a simple greedy algorithm for the oracle.

For concreteness, let us consider a small example. If we apply the method we described to our example (1), we have two initials weights $w_{1}=w_{2}=1$ and thus $p_{1}=p_{2}=\frac{1}{2}$, and we sum all the constraints:

$$
\begin{gathered}
p_{1}\left(x_{1}+3 x_{2}\right)+p_{2}\left(2 x_{1}+x_{2}\right) \geq p_{1} \cdot 2+p_{2} \cdot 1 \Leftrightarrow \\
1.5 x_{1}+2 x_{2} \geq 1.5 \\
1 \geq x_{1}, x_{2} \geq 0
\end{gathered}
$$

By using the oracle, an optimal solution to this reduced problem is $x_{1}=1, x_{2}=0$ of cost 1 . But is this a feasible solution to our original problem? By checking the constraints of the original LP:

$$
\begin{array}{ll}
2 x_{1}+x_{2}=2 \geq 1 & \text { OK } \\
x_{1}+3 x_{2}=1<2 & \text { not OK }
\end{array}
$$

We will need to go back to the original problem and increase the weights of the unsatisfied constraints to give them more importance and decrease the weights of the satisfied constraint. We will perform these updates (as done by Hedge) multiplicatively that we describe in detail in Section 4.4. We first describe how to implement the oracle in general.

### 4.3 Implementation of the oracle

The oracle is given an objective function minimize $\sum_{i=1}^{n} c_{i} x_{i}$ and only one constraint that we can rewrite as $\sum_{i=1}^{n} d_{i} x_{i} \geq b$ (which is the weighted sum of all constraints). We also have $1 \geq x_{i} \geq 0 \forall i$ and $c_{i}, d_{i} \geq 0 \forall i$ since it is a covering problem.

The idea is to assign the maximum value (namely 1) to the variables that have the highest ratio constraint coefficient/objective coefficient. That way we will satisfy the constraint as fast as possible while maintaining a small objective function. Then assign zero to the other variables and possibly an intermediate value for the variable that is at the limit to make the constraint satisfied. This is very similar to the most "bang-for-the-buck" greedy and it is the solution to fractional knapsack. Formally:

- Sort and relabel all variables $x_{i}$ so that $d_{1} / c_{1} \geq d_{2} / c_{2} \geq \ldots d_{n} / c_{n}$.
- Let $k=\min \left\{j: \sum_{i=1}^{j} d_{i} \geq b\right\}$ and $\ell=b-\sum_{i=1}^{k-1} d_{i}$.
- Set $x_{i}:=1$ for $i=1, \ldots, k-1$.
- Set $x_{k}:=\ell / d_{k}$.
- Set $x_{i}:=0$ for $i=k+1, \ldots, n$.

We have,

$$
\sum_{i=1}^{n} d_{i} x_{i}=\sum_{i=1}^{n} d_{i} x_{i}=\sum_{i=1}^{k-1} d_{i} x_{i}+d_{k} x_{\sigma(k)}+\sum_{i=k+1}^{n} d_{i} x_{i}=\sum_{i=1}^{k-1} d_{i}+\ell=b
$$

Therefore the constraint is exactly satisfied. By the ordering of the variables, this ensures that we minimize the objective function as required. Having implemented the oracle, we proceed to formally define the Hedge algorithm for linear programming.

### 4.4 Hedge algorithm for covering LPs

As already explained, we associate an expert to each constraint of the covering LP. In addition, as hinted above, we wish to increase the weight of unsatisfied constraints and decrease the weight of satisfied constraints (in a smooth manner depending on the size of the violation or the slack). The Hedge algorithm for covering LPs thus becomes:

- Assign each constraint $i$ a weight $w_{i}^{(1)}$ initialized to 1.

At each time $t$ :

- Pick the distribution $p_{i}^{(t)}=w_{i}^{(t)} / \Phi^{(t)}$ where $\Phi^{(t)}=\sum_{i \in[N]} w_{i}^{(t)}$.
- Now we define the cost vector instead of the adversary as follows:
- Let $x^{(t)}$ be the solution returned by the oracle on the LP obtained by using the convex combination $\vec{p}^{(t)}$ of constraints. Notice that cost of $x^{(t)}$, i.e., $c^{\top} x^{(t)}$, is at most the cost of an optimal solution to the original LP.
- Define the cost of constraint $i$ as

$$
m_{i}^{(t)}=\sum_{j=1}^{n} A_{i j} x_{j}-b_{i}=A_{i} x-b_{i}
$$

Notice that we have a positive cost if the constraint is satisfied (so the weight will be decreased by Hedge) and a negative cost if it is violated (so the weight will be increased by Hedge).

- After observing the cost vector, set $w_{i}^{(t+1)}=w_{i}^{(t)} \cdot e^{-\varepsilon \cdot m_{i}^{(t)}}$.

Output: the average $\bar{x}=\frac{1}{T} \sum_{t=1}^{T} x^{(t)}$ of the constructed solutions.

Analysis. Since the analysis for the Hedge algorithm works with an adversarial construction of the cost vectors, it definitely holds for the cost vectors we constructed. Let

$$
\rho=\max _{1 \leq i \leq m}\left\{\max \left(b_{i}, A_{i} \mathbf{1}-b_{i}\right)\right\}
$$

be (an upper bound on) the width of our constructed cost vectors. By Corollary 3, we thus have for $\epsilon \in[0,1], T \geq\left(4 \rho^{2} \ln m\right) / \epsilon^{2}$ and any constraint $i$ that

$$
\begin{equation*}
\frac{1}{T} \sum_{t=1}^{T} \vec{p}^{(t)} \cdot \vec{m}^{(t)} \leq \frac{1}{T} \sum_{t=1}^{T} m_{i}^{(t)}+2 \epsilon \tag{2}
\end{equation*}
$$

Let us first consider the left-hand-side of the above expression. We have that

$$
\begin{aligned}
\sum_{t=1}^{T} \vec{p}^{(t)} \cdot \vec{m}^{(t)} & =\sum_{t=1}^{T}\left(\sum_{i} p_{i}^{(t)} \cdot m_{i}^{(t)}\right) \\
& =\sum_{t=1}^{T}(\underbrace{\sum_{i} p_{i}^{(t)} \cdot\left(A_{i} x^{(t)}-b_{i}\right)}_{(*)})
\end{aligned}
$$

which is non-negative because $(*)$ is non-negative for every $t$ since the oracle outputs a feasible solution. Using that the left-hand-side of (2) is non-negative, we get

$$
-2 \epsilon \leq \frac{1}{T} \sum_{t=1}^{T} m_{i}^{(t)}=\frac{1}{T} \sum_{t=1}^{T}\left(A_{i} x^{(t)}-b_{i}\right)=A_{i} \bar{x}-b_{i}
$$

which implies that

$$
A_{i} \bar{x} \geq b_{i}-2 \epsilon
$$

for every constraint $i$. So our solution $\bar{x}$ is almost feasible. Moreover the $\operatorname{cost} c^{\top} \bar{x}=c^{\top}\left(\frac{1}{T} \sum_{t \in[T]} x^{(t)}\right)$ is at most the cost of an optimal solution to the original LP since each $x^{(t)}$ has no higher cost than an optimal solution (by the properties of the oracle).

Setting the parameters for solving the set cover relaxation. For set cover we have that $\rho \leq n$ and therefore, it is sufficient to set $T=\left(4 n^{2} \ln m\right) / \epsilon^{2}$ (this can in fact be improved by a better analysis to $\left.\approx n \ln m / \epsilon^{2}\right)$. This gives a solution $\bar{x}$ that satisfies $\sum_{e \in S} x_{e} \geq 1-2 \epsilon$ for every set $S$ and the cost of $\bar{x}$ is at most that of an optimal LP solution. We can obtain a feasible (approximately optimal) solution by simply defining $x^{*}=\frac{1}{1-2 \epsilon} \bar{x}$.


[^0]:    ${ }^{1}$ Disclaimer: These notes were written as notes for the lecturer. They have not been peer-reviewed and may contain inconsistent notation, typos, and omit citations of relevant works.

