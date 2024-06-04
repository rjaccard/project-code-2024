# Lecture 8: Universal Source Coding And Finite State Machines

In the previous lecture, we properly defined the notion of typicality and typical sets. However, we have yet to relate these notions to source coding. Today's lecture will fill in the blanks as well as introduce the notion of finite state machine source codes.

## 1 Typicality And Source Coding

Before adding the notion of source coding to typicality, let us first recall an important notion to remember from the previous lectures. Consider the entire universe of all possible values U^n, where |U^n|= 2^{n log|U|}. A subset of this universe will be T(n, p, ϵ) whose size is at most 2^{nH(p)(1+ϵ)}. It is important to note that the size of T is rather small. In fact, its size is exponentially small compared to the size of the universe. However, the entire subset T is big, probability wise, i.e. Pr(U^n ∈ T) ≈ 1.

## 1.1 Source Coding Via Typicality

Important property from last lecture : Recall that last time we have stated two important relations. Namely, 1 − ϵ ≤ Pr(U^n ∈ T(n, p, ϵ)) for n large and Pr(U^n = u^n) = 2^{−nH(p)(1+ϵ)}. The combination of those two properties gives us something that is called the Asymptotic Equi-partition Property (AEP in short). It essentially tells us that with probability almost 1, sequences are all equally probable.

**How to merge source coding and typicality** : We assign binary representations of length $k=\lceil nH(p)(1+\epsilon)\rceil$ bits to the elements of $T(n,p,\epsilon)$ (note that we can do this as the number of elements in $T$ is at most $2^{k}$). Write $\mathit{repr}(u^{n}):T(n,p,\epsilon)\rightarrow\{0,1\}^{k}$. The encoder can be defined as follows:

$$\mathit{enc}(U^{n})=\begin{cases}1\circ\mathit{repr}(u^{n})&\text{if}u^{n}\in T(n,p,\epsilon)\\ 0\circ\mathit{repr}(u^{n})&\text{otherwise,}\end{cases}$$
where ◦ denotes the concatenation operator and repr : Un → {0, 1}^k' where k' = ⌈n log|U|⌉. 

## 1.2 Universal Source Coding

In this section, we want to ideally address all the weaknesses of the previous coding methods we introduced thus far in the lecture.

Recap on KL Divergence : First recall that c : U → {0, 1}^∗ has length c(u) = log 1/q(u) and E[*length*(c(U))] − H(U) = D(p||q). Here, D can be seen as the regret, that is, the difference between the actual loss and the best loss we could have achieved by knowing, in hindsight, the best possible action. Intuitively, recall that the KL divergence is similar to a notion of distance with the properties that it is non-negative, 0 iff p = q and small if the distributions p and q are close. However, we cannot really consider it as a distance since it is not symmetric and hence does not satisfy the triangle inequality. Therefore, we can see it as our best way to determine the difference between the expected length of a code and its entropy. 

Problem formalisation : Suppose P is a set of probability distributions on U and that the r.v. U has a distribution in P. A possible code design strategy is the folowing:

$$\arg\operatorname*{min}_{q}\operatorname*{max}_{p\in{\mathcal{P}}}D(p||q),$$

that is, the smallest index that minimises the maximal regret. We let $*rich*(P) = min_q max_p D(p||q)$
(it often corresponds to the capacity of a communication channel).

**Side note** Note that if there are big differences in each of the distributions of ${\cal P}$, we could also try to minimise the average regret. We would have $\max_{p}D(p||q)=\max_{w}\sum_{p}w(p)D(p||q)$ where all the weights $w$ are positive and sum up to 1. The problem would then become
$$\min_{q}\max_{w}\sum_{p}w(p)D(p||q)\geq\max_{w}\min_{q}\sum_{p}w(p)D(p||q),$$

with equality if and only if the max and the min are swappable. This only happens when the argument of the max is convex and the one of the min is concave. Here, as w(p) and D(p||q) are both linear, the two are both convex and concave which satisfies the condition for equality. 

## 2 Finite State Machine Source Codes 

## 2.1 Some Intuition

We are given a finite set of states S. The starting state is z1 *∈ S*. We define the next-state function as g : U x δ → δ where both δ's are respectively the current and the next state. We also define the output function f : U × δ *→ {*0, 1}∗ which maps an input letter to a binary string. As a simple example, consider the following machine on the alphabet U = {*a, b, c*}:


We ideally want this machine to be somewhat reversible, that is, such that if one only reads the output, he can determine what the input was. The next section will allow us to better understand how we can do so.

## 2.2 Decodable And Information Lossless Machines

When reaching u1, u2, u3*, . . .* the machine visits the states z1, z2, z3*, . . .* with zi+1 = g(ui, zi) and produces the binary output Y1, Y2, Y3*, . . .* where Yi = f(ui, zi). We call a machine *decodable* if from observing only the Y 's, we can determine the u's. Assume that all members of S are reachable, namely if for z *∈ S*, there is an input u1 *. . . u*m s.t. z_{m+1} = z. This allows us to avoid trivialities.

We will write g(z, u1 *. . . u*m) to be the final state if we start from z and read the input u1 *. . . u*m.

Similarly, f(z, u1 *. . . u*m) will be the entire output Y1 *. . . Y*m, again if we start from z and read the input u1 *. . . u*m.

Definition 1 : *A machine is said to be "Information Lossless" (I.L.) if* ∀z, ∀u^m ̸= u^˜n, either f(z, u^m) ̸= f(z, u^˜n) or g(z, u^m) ̸= g(z, u^˜n).

The above definition essentially says that when the inputs are different, either the outputs are also different, or they are the same but the machine can remember that the inputs weren't. Clearly, decodability implies information losslessibility. Note that the converse of the above is not true. Here is an example of a information lossless machine that is not decodable:

## 2.3 A Better Machine ?

Let M be a finite state machine. Given a sequence u1u2 *. . .*, define

$$\rho_{M}(u_{1}\ldots u_{n})={\frac{1}{n}}\sum_{i}l e n g t h(y_{i}),$$
where each yi is an output of M and define

$\rho_{M}(u_{1}u_{2}\ldots)=\liminf_{n\to\infty}\frac{1}{n}\sum_{i}length(y_{i})=\liminf_{n\to\infty}\rho_{M}(u_{1}\ldots u_{n})$.

Let now S be an integer. Define

$\rho_{S}(u_{1}u_{2}\dots)=\min_{M:\text{M is decodable and has}\leq S\text{states}}\rho_{M}(u_{1}u_{2}\dots)$

$$\geq\min_{M:\text{M is LL and has}\leq S\text{states}}\rho_{M}(u_{1}u_{2}\dots)=\rho_{S,IL}(u_{1}u_{2}\dots).$$
Finally, define

$\rho(u_{1}u_{2}\ldots)=\lim_{s\nearrow\infty}\rho_{S}(u_{1}u_{2}\ldots)\geq\lim_{s\nearrow\infty}\rho_{S,IL}(u_{1}u_{2}\ldots)=\rho_{IL}(u_{1}u_{2}\ldots)$.

We can design a new machine (actually a Turing Machine) that is better than all the previous designs we mentionned, even though we do not have the knowledge of the input sequence.

Definition 2 (Distinct parsing) : (v1, . . . , vm) where vi ∈ U^∗ is called a distinct parsing of u^n ∈ U^n if v1, . . . , vn = u^n and vi ̸= vj for all i ̸= j. In other words, no word can appear twice.

Now define m∗(u1, . . . , un) to be the largest m for which u^n = v1 . . . vm is a distinct parsing. For example, m∗(000) = 3 as 000 = , 0, 00. In the next lecture, we will study a little more all the above definitions we have given.