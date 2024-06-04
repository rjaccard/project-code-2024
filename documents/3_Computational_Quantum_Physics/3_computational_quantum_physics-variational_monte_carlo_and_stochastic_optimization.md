## Variational Monte Carlo and Stochastic Optimization

In the previous lectures we have extensively made use of the variational principle. This principle states that

$$
\begin{equation*}
E\left(\theta_{1}, \ldots \theta_{M}\right)=\left\langle\Psi\left(\theta_{1}, \ldots \theta_{M}\right)|\hat{H}| \Psi\left(\theta_{1}, \ldots \theta_{M}\right)\right\rangle \geq E_{0} \tag{8.1}
\end{equation*}
$$

where $\Psi\left(\theta_{1} \ldots \theta_{M}\right)$ is some ansatz $z$ wave-function depending on a set of $M$ parameters, and $E_{0}$ is the exact ground-state energy of the Hamiltonian $\hat{H}$.

Apart from the very special case of mean-field-like ansatz wave-functions (like the single determinant used in the Hartree-Fock method), it is seldom possible to compute analytically $E\left(\theta_{1}, \ldots \theta_{M}\right)$ for a generic variational state $\Psi$. The goal of this lecture is to introduce a series of stochastic techniques that allow to obtain accurate estimates of the variational energies for a given set of parameters $\mathbf{p}$, as well as approaches to optimize those parameters in order to obtain the best possible ground-state energy within the given ansatz form. Albeit this approach is principle approximate (since the chosen form of $\Psi$ might not contain the exact ground-state wave-function) however modern optimization techniques, in conjunction with modern many-body variational states encompassing thousands or more variational parameters, effectively allow to solve for the ground-state properties with very high accuracy.

### 8.1 Variational Monte Carlo

The Variational Monte Carlo method is rooted into the observation that expectation values like (8.1) can be written as statistical averages over a suitable probability distribution. Let us assume that our Hilbert space is spanned by the many-body kets $|\mathbf{x}\rangle$. These in practice depend on the system in exam. For example in the case of spins $1 / 2$ we have seen that one would typically have $|\mathbf{x}\rangle=\left|s_{1} s_{2} \ldots s_{N}\right\rangle$, whereas for second-quantized fermions $|\mathbf{x}\rangle=\left|n_{1} n_{2} \ldots n_{N}\right\rangle$, for particles in continuous space $|\mathbf{x}\rangle=\left|\mathbf{r}_{1} \mathbf{r}_{2} \ldots \mathbf{r}_{N}\right\rangle$, etc. The only difference is of course that in the first two cases one has a discrete set of quantum numbers, whereas in the latter case the degrees of freedom are continuos. In all cases we will denote sums over the Hilbert space with discrete sums, although one
should always bear in mind that in the case of continuous variables these sums must be interpreted as integrals. In particular we will use the closure relation $\sum_{\mathbf{x}}|\mathbf{x}\rangle\langle\mathbf{x}|=\hat{I}$.

### 8.1.1 Stochastic Estimates of Properties

Using the closure relation, we can rewrite a generic quantum expectation value of some operator $\hat{O}$ as

$$
\begin{align*}
\frac{\langle\Psi|\hat{O}| \Psi\rangle}{\langle\Psi \mid \Psi\rangle} & =\frac{\sum_{\mathbf{x}, \mathbf{x}^{\prime}}\langle\Psi \mid \mathbf{x}\rangle\left\langle\mathbf{x}|\hat{O}| \mathbf{x}^{\prime}\right\rangle\left\langle\mathbf{x}^{\prime} \mid \Psi\right\rangle}{\sum_{\mathbf{x}}\langle\Psi \mid \mathbf{x}\rangle\langle\mathbf{x} \mid \Psi\rangle}  \tag{8.2}\\
& =\frac{\sum_{\mathbf{x}, \mathbf{x}^{\prime}} \Psi^{\star}(\mathbf{x}) O_{\mathbf{x} \mathbf{x}^{\prime}} \Psi\left(\mathbf{x}^{\prime}\right)}{\sum_{\mathbf{x}}|\Psi(\mathbf{x})|^{2}} \tag{8.3}
\end{align*}
$$

There can be, in general, two cases:

1. The operator $\hat{O}$ is diagonal in the computational basis, i.e. $O_{\mathbf{x x}^{\prime}}=\delta_{\mathbf{x x}^{\prime}} O(\mathbf{x})$. Then

$$
\begin{align*}
\frac{\langle\Psi|\hat{O}| \Psi\rangle}{\langle\Psi \mid \Psi\rangle} & =\frac{\sum_{\mathbf{x}}|\Psi(\mathbf{x})|^{2} O(\mathbf{x})}{\sum_{\mathbf{x}}|\Psi(\mathbf{x})|^{2}}  \tag{8.4}\\
& \equiv \mathbb{E}_{\Pi}[O(\mathbf{x})] \tag{8.5}
\end{align*}
$$

where $\mathbb{E}_{\Pi}[\ldots]$ denote statistical expectation values over the probability distribution $\Pi(\mathbf{x})=|\Psi(\mathbf{x})|^{2} / \sum_{\mathbf{x}^{\prime}}\left|\Psi\left(\mathbf{x}^{\prime}\right)\right|^{2}$. In other words, in this case quantum expectation values are completely equivalent to averaging over Hilbert-space states sampled according to the square-modulus of the wave-function.

2. The operator $\hat{O}$ is off-diagonal in the computational basis. Then, we can define an auxiliary diagonal operator (often called, in a somehow misleading fashion, local operator or estimator)

$$
\begin{equation*}
O_{\mathrm{loc}}(\mathbf{x})=\sum_{\mathbf{x}^{\prime}} O_{\mathbf{x x}^{\prime}} \frac{\Psi\left(\mathbf{x}^{\prime}\right)}{\Psi(\mathbf{x})} \tag{8.6}
\end{equation*}
$$

such that it is easily seen that

$$
\begin{align*}
\frac{\langle\Psi|\hat{O}| \Psi\rangle}{\langle\Psi \mid \Psi\rangle} & =\frac{\sum_{\mathbf{x}}|\Psi(\mathbf{x})|^{2} O_{\mathrm{loc}}(\mathbf{x})}{\sum_{\mathbf{x}}|\Psi(\mathbf{x})|^{2}}  \tag{8.7}\\
& \equiv \mathbb{E}_{\Pi}\left[O_{\mathrm{loc}}(\mathbf{x})\right] \tag{8.8}
\end{align*}
$$

For any observable, then, we can always compute expectation values over arbitrary wave-functions as statistical averages. In the case of off-diagonal operators, it should be noticed that the sum $\sum_{\mathbf{x}^{\prime}} O_{\mathbf{x x}^{\prime}} \frac{\Psi\left(\mathbf{x}^{\prime}\right)}{\Psi(\mathbf{x})}$, is extended to the tiny portion of the Hilbert space for which $\mathbf{x}^{\prime}$ is such that $\left|O_{\mathbf{x x}^{\prime}}\right| \neq 0$. As we have already seen when performing exact diagonalization, matrix elements of physical operators are typically such that they are row/column sparse, meaning that for fixed $\mathbf{x}$, the number of elements $\mathbf{x}^{\prime}$ such that $\left|O_{\mathbf{x x}^{\prime}}\right| \neq 0$ is polynomial in the system size. In turn this implies that, for given $\mathbf{x}$, the
local estimator $O_{\text {loc }}(\mathbf{x})$ can always be computed in polynomial time, provided also that computing the amplitudes $\langle\mathbf{x} \mid \Psi\rangle$ can be done in polynomial time. In the rest of this and of the following lectures, we will always restrict our attentions to variational wave functions that have this property.

While the local estimator can be computed efficiently, however the summations in $\sum_{\mathbf{x}}|\Psi(\mathbf{x})|^{2}$ are typically not exactly doable, since one has an exponentially large number of possible values of $\mathbf{x}$ on which to perform the summation, and therefore cannot be done by brute-force. Think for example to the case in which you have $|\mathbf{x}\rangle=\left|s_{1} s_{2} \ldots s_{N}\right\rangle$, a system of $N$ spins $1 / 2$. In that case, the summation over $\mathbf{x}$ implies summing over $2^{N}$ possible values, which soon becomes unfeasible as $N$ grows. Similarly, this exponential grows applies to all the other many-body systems of interest.

The powerful idea of the Variational Monte Carlo (VMC) is exactly to replace these sums over exponentially many states, with a statistical average over a large but finite set of states sampled according to the probability distribution $\Pi(\mathbf{x})$. We therefore have a way to compute, stochastically, the expectation value of all the properties of interest, provided we have a way to perform statistical averages efficiently. For example, this strategy will allow us to compute the expectation value of $\hat{\sigma}_{i}^{x}$ for a spin system, the expectation value of $\hat{c}_{i}^{\dagger} \hat{c}_{j}$ for fermions, or even the expectation value of the interaction energy $W_{e e}\left(\vec{r}_{1} \ldots \vec{r}_{N}\right)$ for our electronic structure problems.

### 8.1.1.1 Energy

An immediate corollary of the previously presented scheme, is that also the expectation value of the Hamiltonian $\hat{H}$ (which is itself a generic off-diagonal operator) can be computed using the estimator (8.8). Historically, the local estimator associated to the Hamiltonian is called "local energy":

$$
\begin{equation*}
E_{\mathrm{loc}}(\mathbf{x})=\sum_{\mathbf{x}^{\prime}} H_{\mathbf{x x}^{\prime}} \frac{\Psi\left(\mathbf{x}^{\prime}\right)}{\Psi(\mathbf{x})} \tag{8.9}
\end{equation*}
$$

Notice that this expression (and the equivalent above for local estimators) is strictly valid only for discrete Hilbert spaces. A more general form valid also for continuous Hilbert spaces is

$$
\begin{equation*}
E_{\mathrm{loc}}(\mathbf{x})=\frac{\langle\mathbf{x}|\hat{H}| \Psi\rangle}{\langle\mathbf{x} \mid \Psi\rangle} \tag{8.10}
\end{equation*}
$$

### 8.2 Stochastic Variational Optimization

The final goal we want to achieve here is to optimize the variational energy with respect to the parameters $\boldsymbol{\theta}=\theta_{1}, \ldots \theta_{M}$. We have seen that the expectation value of the energy can be written as a statistical average of the form

$$
\begin{equation*}
\langle\hat{H}\rangle \simeq \mathbb{E}_{\Pi}\left[E_{\mathrm{loc}}(\mathbf{x})\right] \tag{8.11}
\end{equation*}
$$

It is easy to show that also the gradient of the energy can be written under to form of the expectation value of some stochastic variable. In particular, define

$$
\begin{equation*}
D_{k}(\mathbf{x})=\frac{\partial_{\theta_{k}} \Psi(\mathbf{x})}{\Psi(\mathbf{x})} \tag{8.12}
\end{equation*}
$$

then

$$
\begin{align*}
& \partial_{\theta_{k}}\langle\hat{H}\rangle=\partial_{\theta_{k}} \frac{\sum_{\mathbf{x}, \mathbf{x}^{\prime}} \Psi^{\star}(\mathbf{x}) H_{\mathbf{x x}^{\prime}} \Psi\left(\mathbf{x}^{\prime}\right)}{\sum_{\mathbf{x}}|\Psi(\mathbf{x})|^{2}} \\
& =\frac{\sum_{\mathbf{x}, \mathbf{x}^{\prime}} \Psi^{\star}(\mathbf{x}) H_{\mathbf{x x}^{\prime}} D_{k}\left(\mathbf{x}^{\prime}\right) \Psi\left(\mathbf{x}^{\prime}\right)}{\sum_{\mathbf{x}}|\Psi(\mathbf{x})|^{2}}+\frac{\sum_{\mathbf{x}, \mathbf{x}^{\prime}} \Psi^{\star}(\mathbf{x}) D_{k}^{\star}(\mathbf{x}) H_{\mathbf{x x}^{\prime}} \Psi\left(\mathbf{x}^{\prime}\right)}{\sum_{\mathbf{x}}|\Psi(\mathbf{x})|^{2}} \\
& -\frac{\sum_{\mathbf{x}, \mathbf{x}^{\prime}} \Psi^{\star}(\mathbf{x}) H_{\mathbf{x x}} \Psi\left(\mathbf{x}^{\prime}\right)}{\sum_{\mathbf{x}}|\Psi(\mathbf{x})|^{2}} \frac{\sum_{\mathbf{x}}|\Psi(\mathbf{x})|^{2}\left(D_{k}(\mathbf{x})+D_{k}^{\star}(\mathbf{x})\right)}{\sum_{\mathbf{x}}|\Psi(\mathbf{x})|^{2}} \\
& =\frac{\sum_{\mathbf{x}, \mathbf{x}^{\prime}} \frac{\Psi^{\star} \star(\mathbf{x})}{\left.\mathbf{x}^{\prime}\right)} H_{\mathbf{x x}} D_{k}\left(\mathbf{x}^{\prime}\right)\left|\Psi\left(\mathbf{x}^{\prime}\right)\right|^{2}+\sum_{\mathbf{x}, \mathbf{x}^{\prime}}|\Psi(\mathbf{x})|^{2} H_{\mathbf{x x}} D_{k}^{\star}\left(\mathbf{x}^{\prime}\right) \frac{\Psi\left(\mathbf{x}^{\prime}\right)}{\Psi(\mathbf{x})}}{\sum_{\mathbf{x}}|\Psi(\mathbf{x})|^{2}}+ \\
& -\langle H\rangle \frac{\sum_{\mathbf{x}}|\Psi(\mathbf{x})|^{2}\left(D_{k}(\mathbf{x})+D_{k}^{\star}(\mathbf{x})\right)}{\sum_{\mathbf{x}}|\Psi(\mathbf{x})|^{2}} \\
& =\mathbb{E}_{\Pi}\left[E_{\mathrm{loc}}(\mathbf{x}) D_{k}^{\star}(\mathbf{x})\right]-\mathbb{E}_{\Pi}\left[E_{\mathrm{loc}}(\mathbf{x})\right] \mathbb{E}_{\Pi}\left[D_{k}^{\star}(\mathbf{x})\right]+\mathrm{cc} \tag{8.13}
\end{align*}
$$

We can therefore compactly write $\partial_{\theta_{k}}\langle\hat{H}\rangle=\mathbb{E}_{\Pi}\left[G_{k}(\mathbf{x})\right]$, with the gradient estimator being

$$
\begin{equation*}
G_{k}(\mathbf{x})=2 \operatorname{Re}\left[\left(E_{\mathrm{loc}}(\mathbf{x})-\mathbb{E}_{\Pi}\left[E_{\mathrm{loc}}(\mathbf{x})\right]\right) D_{k}^{\star}(\mathbf{x})\right] \tag{8.14}
\end{equation*}
$$

### 8.2.1 Zero-Variance Property

One of the most interesting feature of the energy and energy-gradient estimators sofar presented is that they have the so-called zero-variance property: their statistical fluctuations are exactly zero when sampling from the exact ground-state wave-function. Let us consider for example

$$
\begin{align*}
\operatorname{Var}_{\Pi}\left[E_{\mathrm{loc}}(\mathbf{x})\right] & =\mathbb{E}_{\Pi}\left[E_{\mathrm{loc}}(\mathbf{x})^{2}\right]-\mathbb{E}_{\Pi}\left[E_{\mathrm{loc}}(\mathbf{x})\right]^{2} \\
& =\sum_{\mathbf{x}} \Psi(\mathbf{x})^{2} E_{\mathrm{loc}}(\mathbf{x})^{2}-\langle H\rangle^{2} \\
& =\sum_{\mathbf{x}} \sum_{\mathbf{x}_{1}} H_{\mathbf{x}, \mathbf{x}_{1}} \Psi\left(\mathbf{x}_{1}\right) \sum_{\mathbf{x}_{2}} H_{\mathbf{x}, \mathbf{x}_{2}} \Psi\left(\mathbf{x}_{2}\right)-\langle H\rangle^{2} \\
& =\sum_{\mathbf{x}_{1}} \Psi\left(\mathbf{x}_{1}\right) \sum_{\mathbf{x}} H_{\mathbf{x}_{\mathbf{x}} \mathbf{x}_{1}} \sum_{\mathbf{x}_{2}} H_{\mathbf{x}, \mathbf{x}_{2}} \Psi\left(\mathbf{x}_{2}\right)-\langle H\rangle^{2} \\
& =\left\langle\hat{H}^{2}\right\rangle-\langle\hat{H}\rangle^{2} \tag{8.15}
\end{align*}
$$

where we have assumed for simplicity that the wave-function is real. Therefore the variance of the local energy is an important physical quantity: the energy variance. It is easy to see that if $\Psi$ is an eigenstate of $H$ then $\left\langle\hat{H}^{2}\right\rangle=\langle\hat{H}\rangle^{2}=E_{0}^{2}$, and $\operatorname{Var}_{\Pi}\left[E_{\text {loc }}(\mathbf{x})\right]=$ 0 , i.e. the statistical fluctuations completely vanish. This property is very important since it also implies that, in a sense to be specified below, the closer we get to the ground-state, the less fluctuations we have on the quantity we want to minimize, the energy.

### 8.2.2 Stochastic Gradient Descent

The gradient descent method is the simplest optimization scheme, where at each iteration $i$ the variational parameters are modified according to

$$
\begin{equation*}
\theta_{k}^{i+1}=\theta_{k}^{i}-\eta \partial_{\theta_{k}}\langle\hat{H}\rangle \tag{8.16}
\end{equation*}
$$

where $\eta$ is a (small) parameter called the "learning rate" in the machine learning community. An important difference with respect to the non-stochastic (deterministic) gradient descent approach, is that now we only have stochastic averages of the gradient which is therefore subjected to noise. Let us assume for simplicity that all the components of the gradient are subjected to the same amount of gaussian noise with standard deviation $\sigma$, i.e.

$$
\begin{equation*}
\partial_{\theta_{k}}\langle\hat{H}\rangle=\mathbb{E}_{\Pi}\left[G_{k}(\mathbf{x})\right]+\operatorname{Normal}(0, \sigma) \tag{8.17}
\end{equation*}
$$

where the variance is due to the fact that we are estimating the gradient using a finite number of samples, thus for the central limit theorem it will be equal to

$$
\begin{equation*}
\sigma^{2}=\frac{\operatorname{Var}_{\Pi}\left[G_{k}(\mathbf{x})\right]}{N_{s}} \tag{8.18}
\end{equation*}
$$

We can then compare Eq. 67 to the discretized Langevin equation (for example as found in Brownian motion):

$$
\begin{equation*}
r_{k}^{i+1}=r_{k}^{i}-\delta_{t} \partial_{r_{k}} E(\mathbf{r})+\operatorname{Normal}\left(0, \sqrt{2 \delta_{t} T}\right) \tag{8.19}
\end{equation*}
$$

where $\delta_{t}$ is a small time step, such that the particle positions $\mathbf{r}\left(t=\delta_{t} i\right) \equiv \mathbf{r}^{i}$ evolve in time under the action of a conservative force (the first term) and a stochastic force, the second term. It can be shown that the stationary distribution of the Langevin process is the Boltzmann distribution

$$
\begin{equation*}
\Pi_{B}(\mathbf{r})=\frac{e^{-\frac{E(\mathbf{r})}{T}}}{Z(T)} \tag{8.20}
\end{equation*}
$$

which in the limit $T \rightarrow 0$ would converge to the ground-state of the energy potential, i.e. to $\min _{\mathbf{r}} E(\mathbf{r})$.

To complete the analogy between stochastic gradient descend and Langevin dynamics, we can identify the parameters and the particle positions, such that

$$
\begin{align*}
E(\mathbf{r}) & \rightarrow E(\theta)  \tag{8.21}\\
\partial_{r_{k}} E(\mathbf{r}) & \rightarrow \mathbb{E}_{\Pi}\left[G_{k}(\mathbf{x})\right]  \tag{8.22}\\
\delta_{t} & \rightarrow \eta  \tag{8.23}\\
\sqrt{2 \delta_{t} T} & \rightarrow \eta \sqrt{\frac{\operatorname{Var}_{\Pi}\left[G_{k}(\mathbf{x})\right]}{N_{s}}} \tag{8.24}
\end{align*}
$$

We therefore see that the variance of the gradient corresponds to the effective temperature

$$
\begin{equation*}
T_{\mathrm{eff}} \propto \frac{\eta \operatorname{Var}_{\Pi}\left[G_{k}(\mathbf{x})\right]}{N_{\mathrm{s}}} \tag{8.25}
\end{equation*}
$$

Since we want to find the variational ground state (that corresponds to the state with $T_{\text {eff }}=0$ in this analogy), we should have a scheme in which the effective temperature is gradually decreased at each optimization step, i.e. $T_{1}>T_{2}>T_{3} \ldots$, as in the simulated annealing optimization protocol. Given the form of the effective temperature, convenient ways to reduce the temperature are either to reduce the learning rate: $\eta(i)=$ $\eta_{0} / \sqrt{i+1}$ or to increase the number of samples $N_{s}$ with the iteration count.

During the optimization however it often happens that if we are close enough to the ground-state solution $\operatorname{Var}_{\Pi}\left[G_{k}(\mathbf{x})\right] \rightarrow 0$. Indeed, we have shown before that for an exact eigenstate the statistical fluctuations of the gradient are exactly vanishing, i.e. $\operatorname{Var}_{\Pi}\left[G_{k}\right]=0$. In practice then, even a constant number of samples and a fixed (small) $\eta$ are sufficient to converge to the ground-state, provided that one checks during the optimization that the value of the effective temperature (8.25) is actually going to zero as expected.

### 8.3 Sampling Methods

Once established this fundamental connection between variational methods, optimization of wave functions and statistical sampling, we need an efficient way of sampling from the probability distribution $\Pi(\mathbf{x})=|\Psi(\mathbf{x})|^{2}$, and compute the required expectation values. In particular the goal is to generate $N_{s}$ samples $\mathbf{x}^{(1)}, \mathbf{x}^{(2)}, \ldots \mathbf{x}^{\left(N_{s}\right)}$ such that we can estimate expectation values as averages over those samples, for example for the local energy:

$$
\begin{equation*}
\mathbb{E}_{\Pi}\left[O_{\mathrm{loc}}(\mathbf{x})\right] \simeq \frac{1}{N_{s}} \sum_{i}^{N_{s}} O_{\mathrm{loc}}\left(\mathbf{x}^{(i)}\right) \tag{8.26}
\end{equation*}
$$

### 8.3.1 Markov Chain and Detailed Balance

Devising strategies to sample from a given probability distribution is, in general, a complex computational task. This task can be simplified if the probability to be sampled from has a special structure, however in general there is a family of sampling techniques that are rather universal, and known as Markov-Chain Monte Carlo (MCMC). Here we review these algorithms, that you have already covered in previous courses.

A Markov chain is completely specified by the transition probability $\mathcal{T}\left(\mathbf{x}^{(i)} \rightarrow\right.$ $\mathbf{x}^{(i+1)}$ ), i.e. given a sample $\mathbf{x}^{(i)}$, we transition to the next element of the chain with probability $T$. The transition probability (as all well-defined probabilities) must always be normalized: $\sum_{\mathbf{x}^{\prime}} \mathcal{T}\left(\mathrm{x} \rightarrow \mathbf{x}^{\prime}\right)=1$. We would like to devise a Markov chain process such that $\Pi^{\mathrm{mc}}(\mathbf{x})=\Pi(\mathbf{x})$, i.e. that the probability with which a given state $\mathbf{x}$ appears in the chain is equal to desired probability we want to sample from.

An important condition for this to happen is that the probability distribution $\Pi^{\mathrm{mc}}(\mathbf{x})$ is stationary, i.e. all states along the chain should be distributed according to the same probability, and this should not change along the chain. A sufficient condition for this to happen is that

$$
\begin{equation*}
\Pi(\mathrm{x}) \mathcal{T}\left(\mathrm{x} \rightarrow \mathrm{x}^{\prime}\right)=\Pi\left(\mathrm{x}^{\prime}\right) \mathcal{T}\left(\mathrm{x}^{\prime} \rightarrow \mathbf{x}\right) \tag{8.27}
\end{equation*}
$$

which is called detailed balance equation. This condition basically enforces stationarity (also called micro-reversibility) in the chain: the probability of being in a given state $\mathrm{x}$ and of doing a transition to another state $\mathbf{x}^{\prime}$ must be equal to the reverse process, starting from $\mathbf{x}^{\prime}$ and transitioning to $\mathbf{x}$.

### 8.3.2 The Metropolis-Hastings Algorithm

There exist many possible transition probabilities that satisfy the detailed balance condition (8.27), however the most famous choice is certainly the Metropolis-Hastings prescription. In this case, we separate the transition process into two steps:

$$
\begin{equation*}
\mathcal{T}\left(\mathbf{x} \rightarrow \mathbf{x}^{\prime}\right)=T\left(\mathbf{x} \rightarrow \mathbf{x}^{\prime}\right) A\left(\mathbf{x} \rightarrow \mathbf{x}^{\prime}\right) \tag{8.28}
\end{equation*}
$$

i.e. we first propose a state with some (simple) probability distribution $T\left(\mathbf{x} \rightarrow \mathbf{x}^{\prime}\right)$ we can easily sample from, and then accept or reject the new state $\mathbf{x}^{\prime}$ as the next element of the chain with probability $A\left(\mathbf{x} \rightarrow \mathbf{x}^{\prime}\right)$.

Using the detailed balance condition, we see that the acceptance probability must satisfy:

$$
\begin{equation*}
\frac{A\left(\mathbf{x} \rightarrow \mathbf{x}^{\prime}\right)}{A\left(\mathbf{x}^{\prime} \rightarrow \mathbf{x}\right)}=\frac{\Pi\left(\mathbf{x}^{\prime}\right)}{\Pi(\mathbf{x})} \times \frac{T\left(\mathbf{x}^{\prime} \rightarrow \mathbf{x}\right)}{T\left(\mathbf{x} \rightarrow \mathbf{x}^{\prime}\right)} \tag{8.29}
\end{equation*}
$$

A possible acceptance that satisfies this condition is:

$$
\begin{equation*}
A\left(\mathbf{x} \rightarrow \mathbf{x}^{\prime}\right)=\min \left(1, \frac{\Pi\left(\mathbf{x}^{\prime}\right)}{\Pi(\mathbf{x})} \times \frac{T\left(\mathbf{x}^{\prime} \rightarrow \mathbf{x}\right)}{T\left(\mathbf{x} \rightarrow \mathbf{x}^{\prime}\right)}\right) \tag{8.30}
\end{equation*}
$$

Notice that this acceptance probability satisfies (8.29), since if $\frac{\Pi\left(\mathbf{x}^{\prime}\right)}{\Pi(\mathbf{x})} \times \frac{T\left(\mathbf{x}^{\prime} \rightarrow \mathbf{x}\right)}{T\left(\mathbf{x} \rightarrow \mathbf{x}^{\prime}\right)}<1$ then $\frac{\Pi(\mathbf{x})}{\Pi\left(\mathbf{x}^{\prime}\right)} \times \frac{T\left(\mathbf{x} \rightarrow \mathbf{x}^{\prime}\right)}{T\left(\mathbf{x}^{\prime} \rightarrow \mathbf{x}\right)}>1, A\left(\mathbf{x}^{\prime} \rightarrow \mathbf{x}\right)=1$ and (8.29) is trivially verified. The same reasoning can be applied for the case $\frac{\Pi\left(\mathbf{x}^{\prime}\right)}{\Pi(\mathbf{x})} \times \frac{T\left(\mathbf{x}^{\prime} \rightarrow \mathbf{x}\right)}{T\left(\mathbf{x} \rightarrow \mathbf{x}^{\prime}\right)}>1$.

The Metropolis-Hasting Algorithm can be then summarized in the following steps:

1. Generate a random state $\mathbf{x}^{\prime}$ drawing from the (simple) transition probability $T\left(\mathbf{x}^{(i)} \rightarrow \mathbf{x}^{\prime}\right)$.
2. Compute the quantity

$$
\begin{equation*}
R=\frac{\Pi\left(\mathbf{x}^{\prime}\right)}{\Pi\left(\mathbf{x}^{(i)}\right)} \times \frac{T\left(\mathbf{x}^{\prime} \rightarrow \mathbf{x}^{(i)}\right)}{T\left(\mathbf{x}^{(i)} \rightarrow \mathbf{x}^{\prime}\right)} \tag{8.31}
\end{equation*}
$$

3. Draw a uniformly distributed random number $\xi \in[0,1)$.
4. If $R>\xi$, accept the new states, i.e. $\mathbf{x}^{(i+1)}=\mathbf{x}^{\prime}$. Otherwise, the following state in the chain stays the current one: $\mathbf{x}^{(i+1)}=\mathbf{x}^{(i)}$.

Notice that steps 2-4 are necessary to decide whether to accept or reject the proposed state according to the Metropolis probability (8.30).

### 8.3.3 Estimating Errors and Auto-Correlation Times

Since Markov chains are generated transitioning from a state to the next one, it is natural to expect that adjacent points in the chain will be statistically correlated. To quantify this notion of correlation more precisely, let us first consider the Markov chain estimate for the expectation value of a given function:

$$
\begin{equation*}
\bar{g}_{N_{s}}=\frac{1}{N_{s}} \sum_{i}^{N_{s}} g_{i} \tag{8.32}
\end{equation*}
$$

where we have used the short-hand $g_{i} \equiv g\left(\mathbf{x}^{(i)}\right)$. The law of large numbers states that

$$
\begin{equation*}
\lim _{N_{s} \rightarrow \infty} \bar{g}_{N_{s}}=\sum_{\mathbf{x}} \Pi(\mathbf{x}) g(\mathbf{x}) \tag{8.33}
\end{equation*}
$$

and the central limit theorem says that $\bar{g}_{N s}$ is a random variable normally distributed,

$$
\begin{equation*}
\operatorname{Prob}\left(\bar{g}_{N_{s}}\right)=\operatorname{Normal}\left(\bar{g}_{\infty}, \sigma\right), \tag{8.34}
\end{equation*}
$$

with expected value $\bar{g}_{\infty}$ and variance $\sigma^{2}=\operatorname{Var}_{\mathrm{c}}\left[\bar{g}_{N_{s}}\right]$, where the variance is computed over different realizations of the Markov chain. It explicitly reads

$$
\begin{align*}
\operatorname{Var}_{\mathrm{c}}\left[\bar{g}_{N_{s}}\right] & =\operatorname{Var}_{\mathrm{c}}\left[\frac{1}{N_{s}} \sum_{i}^{N_{s}} g_{i}\right] \\
& =\frac{1}{N_{s}^{2}} \sum_{i j} \mathbb{E}_{\mathrm{c}}\left[g_{i} g_{j}\right]-\frac{1}{N_{s}^{2}} \sum_{i j} \mathbb{E}_{\mathrm{c}}\left[g_{i}\right] \mathbb{E}_{\mathrm{c}}\left[g_{j}\right] \\
& =\frac{1}{N_{s}}\left(\frac{1}{N_{s}} \sum_{i}^{N_{s}}\left(\mathbb{E}_{\mathrm{c}}\left[g_{i}^{2}\right]-\mathbb{E}_{\mathrm{c}}\left[g_{i}\right]^{2}\right)+\frac{2}{N_{s}} \sum_{i}^{N_{s}} \sum_{j=i+1}^{N_{s}}\left(\mathbb{E}_{\mathrm{c}}\left[g_{i} g_{j}\right]-\mathbb{E}_{\mathrm{c}}\left[g_{i}\right] \mathbb{E}_{\mathrm{c}}\left[g_{j}\right]\right)\right) \\
& =\frac{1}{N_{s}} \operatorname{Var}_{\mathrm{c}}\left(g_{0}\right)+2 \sum_{j=1}^{N_{s}}\left(\mathbb{E}_{\mathrm{c}}\left[g_{0} g_{j}\right]-\mathbb{E}_{\mathrm{c}}\left[g_{0}\right] \mathbb{E}_{\mathrm{c}}\left[g_{j}\right]\right)\left(1-\frac{j}{N_{s}}\right) \tag{8.35}
\end{align*}
$$

where we assumed that the Markov chain is stationary, thus the variance is independent on the index $i$, i.e. $\operatorname{Var}_{\mathrm{c}}\left(g_{i}\right)=\operatorname{Var}_{\mathrm{c}}\left(g_{0}\right)$, and the same for the covariance. Now, since all Markov chains we are averaging over generate samples from $\Pi(\mathbf{x})$, computing the variance over the chains is equivalent to computing the variance over $\Pi(\mathbf{x})$, thus $\operatorname{Var}_{\mathrm{c}}\left(g_{0}\right)=\operatorname{Var}_{\Pi}[g(\mathbf{x})]$ and

$$
\begin{equation*}
\operatorname{Var}_{\mathrm{c}}\left(\bar{g}_{n_{s}}\right)=\frac{1}{N_{s}} \operatorname{Var}_{\Pi}[g(\mathbf{x})] 2 \tau_{\mathrm{int}}, \tag{8.36}
\end{equation*}
$$

having defined the integrated auto-correlation time as

$$
\begin{equation*}
\tau_{\text {int }}=\frac{1}{2}+\frac{1}{\operatorname{Var}_{\Pi}[g(\mathbf{x})]} \sum_{j=1}^{N_{s}}\left(\mathbb{E}_{\mathrm{c}}\left[g_{0} g_{j}\right]-\mathbb{E}_{\mathrm{c}}\left[g_{0}\right] \mathbb{E}_{\mathrm{c}}\left[g_{j}\right]\right)\left(1-\frac{j}{N_{s}}\right) \tag{8.37}
\end{equation*}
$$

We therefore see that unless the Markov chain samples are completely uncorrelated (i.e. $\mathbb{E}_{c}\left[g_{s} g_{j}\right]-\mathbb{E}_{c}\left[g_{s}\right] \mathbb{E}_{c}\left[g_{j}\right]=0$ ) the statistical error on the estimator $\bar{g}_{n_{s}}$ is increased by the positive factor $\tau_{\text {int }}$.

A way to correctly estimate the integrated autocorrelation time is through the correlation function

$$
\begin{equation*}
\rho(j)=\frac{\left\langle g_{0} g_{j}\right\rangle-\langle g\rangle^{2}}{\left\langle g^{2}\right\rangle-\langle g\rangle^{2}} \tag{8.38}
\end{equation*}
$$

where $\langle\ldots\rangle$ here denote averages over the Markov Chain. A numerically stable estimate of the correlation time is given by

$$
\begin{equation*}
\tau_{\mathrm{int}} \simeq \frac{1}{2}+\sum_{j=1}^{j_{\mathrm{cut}}} \rho(j) \tag{8.39}
\end{equation*}
$$

where $j_{\text {cut }}$ is chosen for numerical stability as the first $j$ such that $\rho\left(j_{\max }\right)<0$. In practice, given a sequence of estimates $g_{1}, \ldots g_{n_{s}}=\mathbf{g}$, then the correlation function can be efficiently estimated with a sequence of Fast Fourier Transforms and its inverses:

$$
\begin{align*}
A & =F F T(\mathbf{g}-\bar{g})  \tag{8.40}\\
B & =A A^{\star}  \tag{8.41}\\
\rho & =\frac{F F T^{-1}(B)}{\left\langle g^{2}\right\rangle-\langle g\rangle^{2}} \tag{8.42}
\end{align*}
$$

### 8.4 Examples of spin wave functions

In the following we give two simple examples of variational wave functions for many spins, specifically considering the Tranverse-Field Ising model, as also introduced earlier in these lectures. Specifically, we can consider the 1-dimensional hamiltonian

$$
\begin{equation*}
\hat{H}=-J \sum_{i=1}^{N} \hat{\sigma}_{i}^{z} \hat{\sigma}_{i+1}^{z}-\Gamma \sum_{i=1}^{N} \hat{\sigma}_{i}^{x} \tag{8.43}
\end{equation*}
$$

### 8.4.1 Mean-Field Ansatz

We start considering a simple "mean-field" ansatz, that corresponds to taking a wave function that factorizes:

$$
\begin{equation*}
|\Psi\rangle=\left|\Phi_{1}\right\rangle \otimes\left|\Phi_{2}\right\rangle \ldots\left|\Phi_{N}\right\rangle \tag{8.44}
\end{equation*}
$$

where

$$
\begin{equation*}
\left\langle s_{1} s_{2} \ldots s_{N} \mid \Psi\right\rangle=\Pi_{i=1}^{N} \Phi_{i}\left(s_{i}\right) \tag{8.45}
\end{equation*}
$$

In this case, there are $M=2 N$ variational parameters, corresponding to the amplitudes of the single-spin wave functions: $\theta_{2 i}=\Phi_{i}(\uparrow)$ and $\theta_{2 i+1}=\Phi_{i}(\downarrow)$. Without loss of generality, since in this case the Hamiltonian is real, we can take the variational parameters to be real valued.

Since this wave function is very simple, sampling from it can be done even without MCMC, by direct sampling. Most notably, we have that the probability density $\Pi(\mathbf{s})=$ $|\Psi(\mathbf{s})|^{2}$ factorizes:

$$
\begin{equation*}
\Pi(\mathbf{s})=\Pi_{i=1}^{N} \Phi_{i}\left(s_{i}\right)^{2} \tag{8.46}
\end{equation*}
$$

thus a simple strategy to sample from it is to generate each spin $s_{i}=(\uparrow, \downarrow)$ according to the probability:

$$
\begin{equation*}
p_{i}(s)=\frac{\Phi_{i}(s)^{2}}{\Phi(\uparrow)^{2}+\Phi_{i}(\downarrow)^{2}} \tag{8.47}
\end{equation*}
$$

This is nothing but a Bernoulli distribution for the variable $s$, and a simple algorithm to sample from it is the following:

1. Draw a uniformly distributed random number $\xi \in[0,1)$
2. Compute the quantity

$$
\begin{equation*}
p_{i}(\uparrow)=\frac{\left|\Phi_{i}(\uparrow)\right|^{2}}{\left|\Phi_{i}(\uparrow)\right|^{2}+\left|\Phi_{i}(\downarrow)\right|^{2}} \tag{8.48}
\end{equation*}
$$

3. If $p_{i}>\xi$ then $s_{i}=\uparrow$, otherwise $s_{i}=\downarrow$.

By repeating this algorithm for all spins $s_{i}$, and for all samples $N_{s}$, we will generate samples $\mathbf{s}^{k}=\left(s_{1}^{k}, s_{2}^{k} \ldots s_{N}^{k}\right)$. Notice that these are all independent samples, at variance with MCMC approaches that instead carry a correlation.

The $\log$ derivatives are also easily computed, for example

$$
\begin{align*}
D_{2 i}(\mathbf{s}) & =\delta_{s_{i}, \uparrow} \frac{\partial_{\theta_{2 i}} \Phi_{i}(\uparrow)}{\Phi_{i}(\uparrow)}  \tag{8.49}\\
& =\frac{\delta_{s_{i}, \uparrow}}{\Phi_{i}(\uparrow)} \tag{8.50}
\end{align*}
$$

### 8.4.2 Jastrow Ansatz

The mean field ansatz is nice and simple, however it does capture any of the correlations among spins, because of its factorized nature. A systematic way to improve on it is to consider an ansatz of the Jastrow-Feenberg form

$$
\begin{align*}
\left\langle s_{1} s_{2} \ldots s_{N} \mid \Psi\right\rangle= & \exp \left[\sum_{i} J_{i}^{(1)}\left(s_{i}\right)+\sum_{i<j} J_{i j}^{(2)}\left(s_{i}, s_{j}\right)+\right. \\
& \left.+\ldots \frac{1}{p!} \sum_{i_{1} \neq i_{2} \neq \ldots i_{p}} J_{i_{1} \ldots i_{p}}^{(p)}\left(s_{i_{1}}, s_{i_{2}} \ldots s_{i_{p}}\right)\right] \tag{8.51}
\end{align*}
$$

where the variational parameters are the functions $J_{i}^{(1)}\left(s_{i}\right), J_{i j}^{(2)}\left(s_{i}, s_{j}\right), \ldots J_{i_{1} \ldots i_{p}}^{(p)}\left(s_{i_{1}}, s_{i_{2}} \ldots s_{i_{p}}\right)$. This expansion coincides with the mean field ansatz when $p=1$ (prove it for yourself,
assuming the $J$ parameters are not necessarily real-valued), and it is clearly an exact description of the many-body state when $p=N$. The main limitation however is that the number of variational parameters also scales exponentially with $p$. Nonetheless, in practice one observes convergence to the exact ground-state much sooner, and it is often the case that two-body correlations only are enough to very accurately describe the ground state properties.

For this kind of wave functions, exact sampling is not possible in general, however a good strategy is to perform MCMC. For the TFIM it is commonly chosen a symmetric transition probability :

$$
\begin{equation*}
T\left(\mathbf{s} \rightarrow \mathbf{s}^{\prime}\right)=T\left(\mathbf{s}^{\prime} \rightarrow \mathbf{s}\right) \tag{8.52}
\end{equation*}
$$

such that the Metropolis Hastings ratio simply becomes

$$
\begin{equation*}
R=\frac{\Pi\left(\mathbf{s}^{\prime}\right)}{\Pi(\mathbf{s})} \tag{8.53}
\end{equation*}
$$

For example a common symmetric transition probability consists in picking a random spin $i$ with uniform probability in $[1, N]$ and then flip it, such that

$$
\begin{equation*}
\mathbf{s}^{\prime}=s_{1} \cdots-s_{i} \ldots s_{N} \tag{8.54}
\end{equation*}
$$

