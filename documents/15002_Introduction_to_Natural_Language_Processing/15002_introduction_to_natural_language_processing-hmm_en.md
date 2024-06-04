# A Primer on Hidden Markov Models 

## Example: PoS tagging with HMM

## Sentence to tag: $\quad$ Time flies like an arrow

## Example of HMM model:

- PoS tags: $\mathscr{T}=\{$ Adj, Adv, Det $, \mathrm{N}, \mathrm{v}, \ldots\}$
- Transition probabilities:

$$
\begin{aligned}
& P(\mathrm{~N} \mid \text { Adj })=0.1, P(\mathrm{~V} \mid \mathrm{N})=0.3, P(\text { Adv } \mid \mathrm{N})=0.01, P(\text { Adv } \mid \mathrm{V})=0.005, \\
& P(\text { Det } \mid \text { Adv })=0.1, P(\text { Det } \mid \mathrm{V})=0.3, P(\mathrm{~N} \mid \text { Det })=0.5
\end{aligned}
$$

- Initial probabilities:

$$
P_{l}(\mathrm{Adj})=0.01, P_{l}(\mathrm{Adv})=0.001, P_{l}(\mathrm{Det})=0.1, P_{l}(\mathrm{~N})=0.2, P_{l}(\mathrm{v})=0.003 \quad(+\ldots)
$$

- Words: $\mathscr{L}=\{$ an, arrow, flies, like, time,$\ldots\}$
- Emission probabilities:

$$
\begin{align*}
& P(\text { time } \mid \mathrm{N})=0.1, P(\text { time } \mid \text { Adj })=0.01, P(\text { time } \mid \mathrm{V})=0.05, \\
& P(\text { flies } \mid \mathrm{N})=0.1, P(\text { flies } \mid \mathrm{V})=0.01, \quad P(\text { like } \mid \text { Adv })=0.005, P(\text { like } \mid \mathrm{V})=0.1, \quad(+\ldots) \\
& P(\text { an } \mid \text { Det })=0.3, \quad P(\text { arrow } \mid \mathrm{N})=0.5
\end{align*}
$$

## Example: PoS tagging with HMM (cont.)

In this example, $12=3 \cdot 2 \cdot 2 \cdot 1 \cdot 1$ analyzes are possible, for example:

$P($ time $/ \mathrm{N}$ flies $/ \mathrm{v}$ like $/$ Adv an/Det arrow $/ \mathrm{N})=1.13 \cdot 10^{-11}$

$P($ time/Adj flies $/ \mathrm{N}$ like $/ \mathrm{v}$ an/Det arrow $/ \mathrm{N})=6.75 \cdot 10^{-10}$

Details of one of such computation:

$$
\begin{aligned}
& P(\text { time } / \mathrm{N} \text { flies } / \mathrm{v} \text { like } / \text { Adv an } / \text { Det arrow } / \mathrm{N}) \\
&= P_{/}(\mathrm{N}) \cdot P(\text { time } \mid \mathrm{N}) \cdot P(\mathrm{v} \mid \mathrm{N}) \cdot P(\text { flies } \mid \mathrm{v}) \cdot P(A d v \mid \mathrm{v}) \cdot P(\text { like } \mid \text { Adv }) \\
& \cdot P(\text { Det } \mid \text { Adv }) \cdot P(\text { an } / \text { Det }) \cdot P(\mathrm{~N} \mid \text { Det }) \cdot P(\operatorname{arrow} \mid \mathrm{N}) \\
&= 2 \mathrm{e}-1 \cdot 1 \mathrm{e}-1 \cdot 3 \mathrm{e}-1 \cdot 1 \mathrm{e}-2 \cdot 5 \mathrm{e}-3 \cdot 5 \mathrm{e}-3 \cdot 1 \mathrm{e}-1 \cdot 3 \mathrm{e}-1 \cdot 5 \mathrm{e}-1 \cdot 5 \mathrm{e}-1 \\
&= 1.13 \cdot 10^{-11}
\end{aligned}
$$

The aim is to choose the most probable tagging among the possible ones (e.g. as provided by the lexicon)

## Markov Models

Markov model: a discrete-time stochastic process $\mathbf{T}$ on $\mathscr{T}=\left\{t^{(1)}, \ldots, t^{(m)}\right\}$ satisfying the Markov property (limited conditioning):

$$
P\left(T_{i} \mid T_{1}, \ldots, T_{i-1}\right)=P\left(T_{i} \mid T_{t-k}, \ldots, T_{i-1}\right)
$$

$k$ : order of the Markov model

In practice $k=1$ (bigrams) or 2 (trigrams) rarely 3 or $4 \quad(\rightarrow$ learning difficulties)

From a theoretical point of view: every Markov model of order $k$ can be represented as another Markov model of order 1 (introduce $Y_{i}=\left(T_{i-k+1}, \ldots, T_{i}\right)$ ).

Vocable:

$$
P\left(T_{1}, \ldots, T_{i}\right)=P\left(T_{1}\right) \cdot P\left(T_{2} \mid T_{1}\right) \cdot \ldots \cdot P\left(T_{i} \mid T_{i-1}\right)
$$

initial probabilities transition probabilities

## Hidden Markov Models (HMM)

## What is hidden?

The model itself (i.e. the state sequence)

## What do we see then?

An observation $w$ related to the state (but not the state itself)

Formally:

- a set of states $\mathscr{C}=\left\{C_{1}, \ldots, C_{m}\right\}$
- a transition probabilities matrix $\mathbf{A}$ :
$a_{i j}=P\left(Y_{t+1}=C_{j} \mid Y_{t}=C_{i}\right)$, shorten $P\left(C_{j} \mid C_{i}\right)$

Example for PoS-tagging:

- PoS tags $\left\{t^{(1)}, \ldots, t^{(m)}\right\}$

$$
P\left(T_{i+1} \mid T_{i}\right)
$$

- an initial probabilities vector $I$ :

$$
\begin{equation*}
l_{i}=P\left(Y_{1}=C_{i}\right) \text { or } P\left(Y_{t}=C_{i} \mid \text { "start"), shorten } P_{/}\left(C_{i}\right)\right. \tag{1}
\end{equation*}
$$

- s a set of "observables" $\Sigma$ (not necessarily discreate, in general)
- $m$ probability densities on $\Sigma$, one for each state (emission probabilities): $B_{i}(o)=P\left(X_{t}=o \mid Y_{t}=C_{i}\right)$ (for $\left.o \in \Sigma\right)$, shorten $P\left(o \mid C_{i}\right)$


## Simple example of HMM

Example: a cheater tossing from two hidden (unfair) coins

- States: coin 1 and coin 2: $\mathscr{C}=\{1,2\}$ transition matrix $\mathbf{A}=\left[\begin{array}{ll}0.4 & 0.6 \\ 0.9 & 0.1\end{array}\right]$ observed: $\Sigma=\{\mathrm{H}, \mathrm{T}\}$
- emission probabilities:
$\mathbf{B}_{1}=(0.49,0.51)$ and $\mathbf{B}_{\mathbf{2}}=(0.85,0.15)$
- initial probabilities : $\mathbf{I}=(0.5,0.5)$
- 5 free parameters: $l_{1}, A_{11}, A_{21}, B_{1}(\mathrm{H}), B_{2}(\mathrm{H})$
- Observation: HTTHTTHHTTHTTTHHTHHTTHTTTTHTHHTHTHHTTTH
- (Hidden) sequence of states: 211211211121112112111211112121121211112


## HMM example for PoS tagging

Problems: Given an HMM and an observation sequence $\mathbf{w}=w_{1} \ldots w_{n}$

$\Rightarrow$ given the parameters $\boldsymbol{\theta}$ of the HMM, what is the probability of the observation sequence: $\quad P(\mathbf{w} \mid \boldsymbol{\theta})$

$$
\begin{aligned}
\boldsymbol{\theta}=(\mathbf{I}, \mathbf{A}, \mathbf{B})
= & \left(l_{1}, \ldots, l_{m}, A_{11}, \ldots, A_{1 m}, \ldots, A_{m 1}, \ldots, A_{m m}, B_{1}\left(w_{1}\right), B_{1}\left(w_{2}\right), \ldots, B_{1}\left(w_{L}\right),\right. \\
& \left.B_{2}\left(w_{1}\right), \ldots, B_{2}\left(w_{L}\right), \ldots, B_{m}\left(w_{1}\right), \ldots, B_{m}\left(w_{L}\right)\right)
\end{aligned}
$$

Application - Language Identification : given the parameters $\boldsymbol{\theta}$ of the HMM, find the most likely state sequence $\mathbf{T}=T_{1} \ldots T_{n}$ that produces $\mathbf{w}$ :

Application - PoS Tagging, Speech recognition : find the parameters that maximize the probability of producing w: $\operatorname{argmax} P(\boldsymbol{\theta} \mid \mathbf{w})$

## Computation of $P(\mathbf{w} \mid \boldsymbol{\theta})$

Computation of $P(\mathbf{w} \mid \boldsymbol{\theta})$ is mathematically trivial:

$$
P(\mathbf{w} \mid \boldsymbol{\theta})=\sum_{\mathbf{T}} P(\mathbf{w}, \mathbf{T} \mid \boldsymbol{\theta})=\sum_{\mathbf{T}} P(\mathbf{w} \mid \mathbf{T}, \boldsymbol{\theta}) \cdot P(\mathbf{T} \mid \boldsymbol{\theta})
$$

Practical limitation: complexity is $\mathscr{O}\left(n m^{n}\right)$

$\rightsquigarrow$ exponential!

Practical computation: forward/backward algorithms $\longrightarrow$ complexity is $\mathscr{O}\left(n m^{2}\right)$

## Forward-Backward algorithms

"forward" variable : $\alpha_{i}(t)=P\left(w_{1}, \ldots, w_{i}, T_{i}=t \mid \boldsymbol{\theta}\right)$

$$
t \in \mathscr{T}
$$

iterative computation: $\alpha_{i+1}\left(t^{\prime}\right)=B_{t^{\prime}}\left(w_{i+1}\right) \cdot \sum_{t \in \mathscr{T}}\left(\alpha_{i}(t) \cdot A_{t t^{\prime}}\right)$

$\alpha_{1}(t)=B_{t}\left(w_{1}\right) \cdot I_{t}$

"backward" variable : $\beta_{i}(t)=P\left(w_{i+1}, \ldots, w_{n} \mid T_{i}=t, \boldsymbol{\theta}\right)$

iterative computation: $\beta_{i-1}\left(t^{\prime}\right)=\sum_{t \in \mathscr{T}}\left(\beta_{i}(t) \cdot A_{t^{\prime} t^{\prime}} \cdot B_{t}\left(w_{i}\right)\right)$

$\beta_{n}(t)=1$ (by convention, practical considerations)

Computation in $\mathscr{O}\left(\mathrm{nm}^{2}\right) \rightarrow$ efficient solutions to "first problem":

$$
\begin{array}{ll}
P(\mathbf{w} \mid \boldsymbol{\theta})=\sum_{t \in \mathscr{T}} P\left(\mathbf{w}, T_{n}=t \mid \boldsymbol{\theta}\right)=\sum_{t \in \mathscr{F}} \alpha_{n}(t) & \\
P(\mathbf{w} \mid \boldsymbol{\theta})=\sum_{t \in \mathscr{T}} \alpha_{i}(t) \cdot \beta_{i}(t) & \forall i: 1 \leq i \leq n
\end{array}
$$

There exist also

"forward-backward" variable : $\gamma_{i}(t)=P\left(T_{i}=t \mid \mathbf{w}, \boldsymbol{\theta}\right)$

$$
\gamma_{i}(t)=\frac{P\left(\mathbf{w}, T_{i}=t \mid \boldsymbol{\theta}\right)}{P(\mathbf{w} \mid \boldsymbol{\theta})}=\frac{\alpha_{i}(t) \cdot \beta_{i}(t)}{\sum_{t^{\prime} \in \mathscr{T}} \alpha_{i}\left(t^{\prime}\right) \cdot \beta_{i}\left(t^{\prime}\right)}
$$

usefull later for other algorithms

## Viterbi algorithm

Efficient solution to the "second problem": find the most likely sequence of states $\mathbf{T}$ (knowing $\mathbf{w}$ and the parameters $\boldsymbol{\theta}): \underset{\mathbf{T}}{\operatorname{argmax}} P(\mathbf{T} \mid \mathbf{w}, \boldsymbol{\theta})$

$\Rightarrow$ maximize (in $\mathbf{T}) P(\mathbf{T}, \mathbf{w} \mid \boldsymbol{\theta})$.

"The" lattice temporal unfolding of all possible walks through the Markov chain

Let $\rho_{i}(t)=\max _{T_{1}, \ldots, T_{i-1}} P\left(T_{1}, \ldots, T_{i-1}, T_{i}=t, w_{1}, \ldots, w_{i} \mid \boldsymbol{\theta}\right)$

We are looking for $\max _{t \in \mathscr{T}} \rho_{n}(t)$

It's easy (exercise) to show that $\rho_{i}(t)=\max _{t^{\prime}}\left[P\left(t \mid t^{\prime}, \boldsymbol{\theta}\right) P\left(w_{i} \mid t, \boldsymbol{\theta}\right) \rho_{i-1}\left(t^{\prime}\right)\right]$

from which the following algorithm comes:

$$
\begin{aligned}
& \text { for all } t \in \mathscr{T} \text { do } \\
& \quad \rho_{1}(t)=I_{t} \cdot B_{t}\left(w_{1}\right)
\end{aligned}
$$

for $\mathrm{i}$ from 2 to $n$ do for all $t \in \mathscr{T}$ do

- $\rho_{i}(t)=B_{t}\left(w_{i}\right) \cdot \max _{t^{\prime}}\left(A_{t^{\prime} t} \cdot \rho_{i-1}\left(t^{\prime}\right)\right)$
- mark one of the transitions from $t^{\prime}$ to $t$ where the maximum is reached reconstruct backwards (from $T_{n}$ ) the best path following the marked transitions


## Expectation-Maximization

Our goal: maximize $P(\boldsymbol{\theta} \mid \mathbf{w})$

Maximum-likelihood estimation of $\theta$

$\rightarrow$ maximization of $P(\mathbf{w} \mid \boldsymbol{\theta})$

To achieve it: Expectation-Maximization (EM) algorithm

General formulation of EM: given observed data $\mathbf{w}=w_{1} \ldots w_{n}$

- a parameterized probability distribution $P(T, \mathbf{w} \mid \boldsymbol{\theta})$ where
- $\mathbf{T}=T_{1} \ldots T_{n}$ are unobserved data
- $\boldsymbol{\theta}$ are the parameters of the model

determine $\boldsymbol{\theta}$ that maximizes $P(\mathbf{w} \mid \boldsymbol{\theta})$ by convergence of iterative computation of the series $\boldsymbol{\theta}^{(i)}$ that maximizes (in $\left.\boldsymbol{\theta}\right) \quad \mathbf{E}_{\mathbf{T}}\left[\log P(\mathbf{T}, \mathbf{w} \mid \boldsymbol{\theta}) \mid \mathbf{w}, \boldsymbol{\theta}^{(i-1)}\right]$

To do so, define the auxilary function

$$
Q\left(\boldsymbol{\theta}, \boldsymbol{\theta}^{\prime}\right)=\mathbf{E}_{\mathbf{T}}\left[\log P(\mathbf{T}, \mathbf{w} \mid \boldsymbol{\theta}) \mid \mathbf{w}, \boldsymbol{\theta}^{\prime}\right]=\sum_{\mathbf{T}} P\left(\mathbf{T} \mid \mathbf{w}, \boldsymbol{\theta}^{\prime}\right) \log P(\mathbf{T}, \mathbf{w} \mid \boldsymbol{\theta})
$$

as it can be shown (with Jensen inequality) that

$$
Q\left(\boldsymbol{\theta}, \boldsymbol{\theta}^{\prime}\right)>Q\left(\boldsymbol{\theta}^{\prime}, \boldsymbol{\theta}^{\prime}\right) \Rightarrow P(\mathbf{w} \mid \boldsymbol{\theta})>P\left(\mathbf{w} \mid \boldsymbol{\theta}^{\prime}\right)
$$

This is the fundamental principle of EM: if we already have an estimation $\boldsymbol{\theta}^{\prime}$ of the parameters and we find another parameter configuration $\theta$ for which the first inequality (on $Q$ ) holds, then $\mathbf{w}$ is most probable with model $\boldsymbol{\theta}$ rather than with model $\boldsymbol{\theta}^{\prime}$.

## EM algorithm:

- Estimation Step: Compute $Q\left(\boldsymbol{\theta}, \boldsymbol{\theta}^{(i)}\right)$
- Maximization Step: Compute $\boldsymbol{\theta}^{(i+1)}=\underset{\boldsymbol{\theta}}{\operatorname{argmax}} Q\left(\boldsymbol{\theta}, \boldsymbol{\theta}^{(i)}\right)$

in other words:

1. Choose $\boldsymbol{\theta}^{(0)}$ (and set $i=0$ )
2. Find $\boldsymbol{\theta}^{(i+1)}$ which maximizes $\sum_{\mathbf{T}} P\left(\mathbf{T} \mid \mathbf{w}, \boldsymbol{\theta}^{(i)}\right) \log P\left(\mathbf{T}, \mathbf{w} \mid \boldsymbol{\theta}^{(i+1)}\right)$
3. Set $i \leftarrow i+1$ and go back to (2) unless some convergence test is fulfilled

## Baum-Welch Algorithm

The Baum-Welch Algorithm is an EM algorithm for estimating HMM parameters.

It's an answer to the "third problem".

The goal is therefore to find

$$
\underset{\boldsymbol{\theta}}{\operatorname{argmax}} \sum_{\mathbf{T}} P\left(\mathbf{T} \mid \mathbf{w}, \boldsymbol{\theta}^{\prime}\right) \log P(\mathbf{T}, \mathbf{w} \mid \boldsymbol{\theta})=\underset{\boldsymbol{\theta}}{\operatorname{argmax}} \underbrace{\sum_{\mathbf{T}} P\left(\mathbf{T}, \mathbf{w} \mid \boldsymbol{\theta}^{\prime}\right) \log P(\mathbf{T}, \mathbf{w} \mid \boldsymbol{\theta})}_{\operatorname{def} \widehat{Q}\left(\boldsymbol{\theta}, \boldsymbol{\theta}^{\prime}\right)}
$$

since $P\left(\mathbf{w} \mid \boldsymbol{\theta}^{\prime}\right)$ does not depend on $\boldsymbol{\theta}$.

What is $\log P(\mathbf{T}, \mathbf{w} \mid \boldsymbol{\theta})$ ?

$$
\log P(\mathbf{T}, \mathbf{w} \mid \boldsymbol{\theta})=\log P_{l}\left(T_{1}\right)+\sum_{i=2}^{n} \log P\left(T_{i} \mid T_{i-1}\right)+\sum_{i=1}^{n} \log P\left(w_{i} \mid T_{i}\right)
$$

$\widehat{Q}\left(\boldsymbol{\theta}, \boldsymbol{\theta}^{\prime}\right)$ consists therefore of 3 terms:

$$
\widehat{Q}\left((\mathbf{I}, \mathbf{A}, \mathbf{B}), \boldsymbol{\theta}^{\prime}\right)=Q_{l}\left(\mathbf{I}, \boldsymbol{\theta}^{\prime}\right)+Q_{A}\left(\mathbf{A}, \boldsymbol{\theta}^{\prime}\right)+Q_{B}\left(\mathbf{B}, \boldsymbol{\theta}^{\prime}\right)
$$

Let's compute one of these:

$$
\begin{aligned}
Q_{l}\left(\mathbf{I}, \boldsymbol{\theta}^{\prime}\right) & =\sum_{\mathbf{T}} P\left(\mathbf{T}, \mathbf{w} \mid \boldsymbol{\theta}^{\prime}\right) \log P_{l}\left(T_{1}\right) \\
& =\sum_{T_{1}} \sum_{2} \sum_{2, \ldots, T_{n}} P\left(T_{1}, \mathbf{w} \mid \boldsymbol{\theta}^{\prime}\right) \cdot P\left(T_{2}, \ldots T_{n} \mid T_{1}, \mathbf{w}, \boldsymbol{\theta}^{\prime}\right) \cdot \log P_{l}\left(T_{1}\right) \\
& =\sum_{t \in \mathscr{T}} P\left(T_{1}=t, \mathbf{w} \mid \boldsymbol{\theta}^{\prime}\right) \cdot \log P_{l}(t) \underbrace{\sum_{T_{2}, \ldots, T_{n}} P\left(T_{2}, \ldots, T_{n} \mid T_{1}, \mathbf{w}, \boldsymbol{\theta}^{\prime}\right)}_{=1} \\
& =\sum_{t \in \mathscr{T}} P\left(T_{1}=t, \mathbf{w} \mid \boldsymbol{\theta}^{\prime}\right) \cdot \log I_{t}
\end{aligned}
$$

Similarly we have:

$$
\begin{gathered}
Q_{A}\left(\mathbf{A}, \boldsymbol{\theta}^{\prime}\right)=\sum_{i=2}^{n} \sum_{t \in \mathscr{T}} \sum_{t^{\prime} \in \mathscr{T}} P\left(T_{i-1}=t, T_{i}=t^{\prime}, \mathbf{w} \mid \boldsymbol{\theta}^{\prime}\right) \log A_{t t^{\prime}} \\
Q_{B}\left(\mathbf{B}, \boldsymbol{\theta}^{\prime}\right)=\sum_{i=2}^{n} \sum_{t \in \mathscr{T}} P\left(T_{i}=t, \mathbf{w} \mid \boldsymbol{\theta}^{\prime}\right) \log B_{t}\left(w_{i}\right)
\end{gathered}
$$

Therefore $\widehat{Q}$ is a sum of three independent terms (e.g. $Q_{\text {l }}$ does not depend on $\mathbf{A}$ nor on B)

therefore the maximisation over $\boldsymbol{\theta}$ is achieved by the three terms separately, i.e. maximizing $Q_{l}\left(\mathbf{I}, \boldsymbol{\theta}^{\prime}\right)$ over $\mathbf{I}, Q_{A}\left(\mathbf{A}, \boldsymbol{\theta}^{\prime}\right)$ over $\mathbf{A}$ and $Q_{B}\left(\mathbf{B}, \boldsymbol{\theta}^{\prime}\right)$ over $\mathbf{B}$ separately.

Notice that all these three functions are sums (over $i$ ) of functions of the form:

$$
f(\mathbf{x})=\sum_{j=1}^{m} y_{j} \log x_{j}
$$

and all the above three functions have to be maximized under the constraint $\sum_{j=1}^{m} x_{j}=1 .{ }^{1}$[^0]

Maximizing

$$
f(\mathbf{x})=\sum_{j=1}^{m} y_{j} \log x_{j}
$$

under the constraint

$$
\sum_{j=1}^{m} x_{j}=1
$$

can be achieved using Lagrange multipliers, i.e. looking at

$$
g(\mathbf{x})=f(\mathbf{x})-\lambda \cdot \sum_{j=1}^{m} x_{j}=\sum_{j=1}^{m}\left(y_{j} \log x_{j}-\lambda \cdot x_{j}\right)
$$

Solving this by $\frac{\partial}{\partial x} g(x)=0$, we find that $\lambda=\frac{y_{j}}{x_{j}}$.

Putting this back in the constraint we find:

$$
x_{j}=\frac{y_{j}}{\sum_{j=1}^{m} y_{j}}
$$

Summarizing the obtained results, we have the following reestimation formulas (where the max. is reached):

$$
\begin{aligned}
\widehat{t_{t}} & =\frac{P\left(T_{1}=t, \mathbf{w} \mid \boldsymbol{\theta}^{\prime}\right)}{\sum_{t^{\prime} \in \mathscr{T}} P\left(T_{1}=t^{\prime}, \mathbf{w} \mid \boldsymbol{\theta}^{\prime}\right)}=\frac{P\left(T_{1}=t, \mathbf{w} \mid \boldsymbol{\theta}^{\prime}\right)}{P\left(\mathbf{w} \mid \boldsymbol{\theta}^{\prime}\right)} \\
\widehat{A_{t t^{\prime}}} & =\frac{\sum_{i=2}^{n} P\left(T_{i-1}=t, T_{i}=t^{\prime}, \mathbf{w} \mid \boldsymbol{\theta}^{\prime}\right)}{\sum_{i=2}^{n} \sum_{\tau \in \mathscr{T}} P\left(T_{i-1}=t, T_{i}=\tau, \mathbf{w} \mid \boldsymbol{\theta}^{\prime}\right)} \\
& =\frac{\sum_{i=2}^{n} P\left(T_{i-1}=t, T_{i}=t^{\prime}, \mathbf{w} \mid \boldsymbol{\theta}^{\prime}\right)}{\sum_{i=2}^{n} P\left(T_{i-1}=t, \mathbf{w} \mid \boldsymbol{\theta}^{\prime}\right)}
\end{aligned}
$$

and:

$$
\widehat{B_{t}(w)}=\frac{\sum_{\substack{i=1 \text { s.t. } \\ w i=w}}^{n} P\left(T_{i}=t, \mathbf{w} \mid \boldsymbol{\theta}^{\prime}\right)}{\sum_{i=2}^{n} P\left(T_{i}=t, \mathbf{w} \mid \boldsymbol{\theta}^{\prime}\right)}=\frac{\sum_{i=2}^{n} P\left(T_{i}=t, \mathbf{w} \mid \boldsymbol{\theta}^{\prime}\right) \delta_{w_{i}, w}}{\sum_{i=2}^{n} P\left(T_{i}=t, \mathbf{w} \mid \boldsymbol{\theta}^{\prime}\right)}
$$

with $\delta_{w, w^{\prime}}=1$ if $w=w^{\prime}$ and 0 otherwise.

## Baum-Welch Algorithm: effective computation

How do we compute these reestimation formulas?

$$
\text { Let } \chi_{i}\left(t, t^{\prime}\right)=P\left(T_{i}=t, T_{i+1}=t^{\prime} \mid \mathbf{w}\right)
$$

$\chi_{i}$ is easy to compute with "forward" and "backward" variables:

$$
\chi_{i}\left(t, t^{\prime}\right)=\frac{\alpha_{i}(t) \cdot A_{t t^{\prime}} \cdot B_{t^{\prime}}\left(w_{i+1}\right) \cdot \beta_{i+1}\left(t^{\prime}\right)}{\sum_{\tau \in \mathscr{T}} \sum_{\tau^{\prime} \in \mathscr{T}} \alpha_{i}(\tau) \cdot A_{\tau \tau^{\prime}} \cdot B_{\tau^{\prime}}\left(w_{i+1}\right) \cdot \beta_{i+1}\left(\tau^{\prime}\right)}
$$

Notice: $\gamma_{i}(t)=\sum_{t^{\prime} \in \mathscr{T}} \chi_{i}\left(t, t^{\prime}\right)$
for all $1 \leq i<n$

## Effective reestimation formulas

$$
\widehat{I}_{t}=\gamma_{1}(t)
$$

$$
\widehat{A_{t t^{\prime}}}=\frac{\sum_{i=1}^{n-1} \chi_{i}\left(t, t^{\prime}\right)}{\sum_{i=1}^{n-1} \gamma_{i}(t)}
$$

$$
\widehat{B_{t}(w)}=\frac{\sum_{\substack{i=1 \text { s.t. } \\ w_{i}=w}}^{n} \gamma_{i}(t)}{\sum_{i=1}^{n} \gamma_{i}(t)}=\frac{\sum_{i=1}^{n} \gamma_{i}(t) \delta_{w_{i}, w}}{\sum_{i=1}^{n} \gamma_{i}(t)}
$$

with $\delta_{w, w^{\prime}}=1$ if $w=w^{\prime}$ and 0 otherwise.

## Baum-Welch Algorithm

1. Let $\boldsymbol{\theta}^{(0)}$ be an initial parameter set
2. Compute iteratively $\alpha, \beta$ and then $\gamma$ and $\chi$
3. Compute $\boldsymbol{\theta}^{(t+1)}$ with reestimation formulas
4. If $\boldsymbol{\theta}^{(t+1)} \neq \boldsymbol{\theta}^{(t)}$, go to ( 2 )

## WARNING!

The algorithm converges but only towards a local maximum of $\mathbf{E}[\log P(\mathbf{T}, \mathbf{w} \mid \boldsymbol{\theta})]$

## Other models

Beyond HMMs, what's next?

- Conditional Random Fields (CRF)
- Bayesian Networks
- Graphical Models

However, the main three important aspects remains:

1. efficient computations using dynamic programming
2. Viterbi-like search algorithm ("belief propagation")
3. Unsupervised learning with Expectation-Maximization

## CRF versus HMM

(linear) Conditional Random Fields (CRF) are a discriminative generalization of the HMMs where "features" no longer needs to be state-conditionnal probabilities (less constraint features).

For instance (order 1, i.e. bigrams of tags):

## HMM

$$
P(\mathbf{t}, \mathbf{w})=P\left(t_{1}\right) P\left(w_{1} \mid t_{1}\right)
$$

$$
\prod_{i=2}^{n} P\left(w_{i} \mid t_{i}\right) P\left(t_{i} \mid t_{i-1}\right)
$$

## CRF

$$
P(\mathbf{t} \mid \mathbf{w})=\prod_{i=2}^{n} P\left(t_{i-1}, t_{i} \mid \mathbf{w}\right)
$$

$$
\left(\text { with } P\left(t_{i-1}, t_{i} \mid \mathbf{w}\right) \propto \exp \left(\Sigma_{j} \lambda_{j} f_{j}\left(t_{i-1}, t_{i}, \mathbf{w}, i\right)\right)\right.
$$


[^0]:    ${ }^{1}$ To be accurate: for $\mathbf{B}_{\mathbf{t}}$ the constraint is $\sum_{w \in \mathscr{L}} B_{t}(w)=1$. This changes the formulas a bit, but not the

