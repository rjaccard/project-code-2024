## Ground-State Quantum Monte Carlo

In the previous lectures we have started our journey through Quantum Monte Carlo methods, introducing the basis concept of stochastic sampling, as well as the Variational Monte Carlo approach. Even though Variational Monte Carlo is a very powerful method, in principle it can recover the exact ground-state solution only if a sufficiently general enough wave-function ansatz is used.

During this Lecture we will see how we can find, in some notable cases, the exact ground-state solution using a different set of Quantum Monte Carlo techniques.

### 11.1 Imaginary-Time Evolution

In order to find an exact (and computationally useful) representation of the exact ground-state wave-function, we start from the imaginary-time evolution of a some given initial state:

$$
\begin{equation*}
\langle\mathbf{x} \mid \Psi(\tau)\rangle=\left\langle\mathbf{x}\left|e^{-\tau \hat{H}}\right| \Psi(0)\right\rangle \tag{11.1}
\end{equation*}
$$

where $\hat{H}$ is the Hamiltonian, $\tau$ is the imaginary-time, and $|\Psi(0)\rangle$ is some chosen initial state (for example it might be the best possible variational estimate we have for the ground-state of $\hat{H})$. We have seen already previously that imaginary-time evolution converges to the exact ground-state $\left\langle\mathbf{x} \mid \Psi_{0}\right\rangle$ in the limit $\tau \gg \Delta E_{0}=E_{1}-E_{0}$, provided that the initial state is non-orthogonal to the exact one i.e. if $\left|\left\langle\Psi_{0} \mid \Psi(0)\right\rangle\right|^{2} \neq 0$. A complete demonstration of this statement has been given in one of the previous chapters.

Goal of today's lecture is to devise a way to sample exactly, using Monte Carlo methods, from $|\langle\mathbf{x} \mid \Psi(\tau)\rangle|^{2}$. If we achieve this goal, then all the properties of interest can be measured using just statistical averages, as already discussed in the case of the Variational Monte Carlo approach.

### 11.1.1 Path-Integral Representation

In order to devise a practical sampling scheme, we need to write $\langle\mathbf{x} \mid \Psi(\tau)\rangle$ in a way that is more suitable for computations. The first step is to divide the total imaginary-time
$\tau$ into $P$ small time-steps, such that $\tau=P \times \Delta_{\tau}$, and use the fact that

$$
\begin{equation*}
e^{-\tau \hat{H}}=\underbrace{e^{-\Delta_{\tau} \hat{H}} \ldots e^{-\Delta_{\tau} \hat{H}}}_{P \text { times }} \tag{11.2}
\end{equation*}
$$

We then derive the path-integral representation of the imaginary time-evolved state as:

$$
\begin{align*}
\langle\mathbf{x} \mid \Psi(\tau)\rangle & =\left\langle\mathbf{x}\left|e^{-\Delta_{\tau} \hat{H}} \ldots e^{-\Delta_{\tau} \hat{H}}\right| \Psi(0)\right\rangle \\
& =\sum_{\mathbf{x}_{0}}\langle\mathbf{x}|\underbrace{e^{-\Delta_{\tau} \hat{H}} \ldots e^{-\Delta_{\tau} \hat{H}}}_{P \text { times }}| \mathbf{x}_{0}\rangle\left\langle\mathbf{x}_{0} \mid \Psi(0)\right\rangle \\
& =\sum_{\mathbf{x}_{0}} \sum_{\mathbf{x}_{1}}\langle\mathbf{x}|\underbrace{e^{-\Delta_{\tau} \hat{H}} \ldots e^{-\Delta_{\tau} \hat{H}}}_{P-1 \text { times }}| \mathbf{x}_{1}\rangle\left\langle\mathbf{x}_{1}\left|e^{-\Delta_{\tau} \hat{H}}\right| \mathbf{x}_{0}\right\rangle\left\langle\mathbf{x}_{0} \mid \Psi(0)\right\rangle \\
& =\sum_{\mathbf{x}_{0} \mathbf{x}_{1} \ldots \mathbf{x}_{P-1}}\left\langle\mathbf{x}\left|e^{-\Delta_{\tau} \hat{H}}\right| \mathbf{x}_{P-1}\right\rangle \ldots\left\langle\mathbf{x}_{1}\left|e^{-\Delta_{\tau} \hat{H}}\right| \mathbf{x}_{0}\right\rangle\left\langle\mathbf{x}_{0} \mid \Psi(0)\right\rangle \tag{11.3}
\end{align*}
$$

where we have inserted $P$ completeness relations $\sum_{\mathbf{x}_{j}}\left|\mathbf{x}_{j}\right\rangle\left\langle\mathbf{x}_{j}\right|=\hat{I}$, and thus introduced a set of $P$ imaginary-time dependent quantum numbers $\mathbf{x}_{1}, \mathbf{x}_{2}, \ldots \mathbf{x}_{P}$. We now also define the propagator:

$$
\begin{equation*}
G^{\Delta_{\tau}}(\mathbf{x}, \mathbf{y}) \equiv\left\langle\mathbf{x}\left|e^{-\Delta_{\tau} \hat{H}}\right| \mathbf{y}\right\rangle \tag{11.4}
\end{equation*}
$$

and use the naming conventions $\mathbf{x} \equiv \mathbf{x}_{P}$, and $\left\langle\mathbf{x}_{0} \mid \Psi(0)\right\rangle \equiv \Psi\left(\mathbf{x}_{0}\right)$, thus we have

$$
\begin{equation*}
\langle\mathbf{x} \mid \Psi(\tau)\rangle=\sum_{\mathbf{x}_{0} \mathbf{x}_{1} \ldots \mathbf{x}_{P-1}} \underbrace{G^{\Delta_{\tau}}\left(\mathbf{x}_{P}, \mathbf{x}_{P-1}\right) \ldots G^{\Delta_{\tau}}\left(\mathbf{x}_{1}, \mathbf{x}_{0}\right)}_{P \text { times }} \Psi\left(\mathbf{x}_{0}\right) \tag{11.5}
\end{equation*}
$$

The representation (11.5) is particularly useful because we typically know how to compute controlled numerical approximations of the short-time propagators (11.4).

For example, in most applications the Hamiltonian is the sum of two non-commuting terms $\hat{H}=\hat{H}_{0}+\hat{H}_{1}$, where the first term is diagonal in the chosen basis $|\mathbf{x}\rangle$. We can then use the Trotter decomposition to find:

$$
\begin{align*}
G^{\Delta_{\tau}}(\mathbf{x}, \mathbf{y}) & =\left\langle\mathbf{x}\left|e^{-\Delta_{\tau} \hat{H}_{0}} e^{-\Delta_{\tau} \hat{H}_{1}}\right| \mathbf{y}\right\rangle+\mathcal{O}\left(\Delta_{\tau}^{2}\right) \\
& =e^{-\Delta_{\tau} H_{0}(\mathbf{x})}\left\langle\mathbf{x}\left|e^{-\Delta_{\tau} \hat{H}_{1}}\right| \mathbf{y}\right\rangle+\mathcal{O}\left(\Delta_{\tau}^{2}\right) \\
& =e^{-\Delta_{\tau} H_{0}(\mathbf{x})} G_{1}^{\Delta_{\tau}}(\mathbf{x}, \mathbf{y})+\mathcal{O}\left(\Delta_{\tau}^{2}\right) \tag{11.6}
\end{align*}
$$

or the symmetric second-order approximation:

$$
\begin{equation*}
G^{\Delta_{\tau}}(\mathbf{x}, \mathbf{y})=e^{-\Delta_{\tau} \frac{H_{0}(\mathbf{x})}{2}} G_{1}^{\Delta_{\tau}}(\mathbf{x}, \mathbf{y}) e^{-\Delta_{\tau} \frac{H_{0}(\mathbf{y})}{2}}+\mathcal{O}\left(\Delta_{\tau}^{3}\right) \tag{11.7}
\end{equation*}
$$

The important aspect of these decomposition is that, in interesting applications, it is typically possible to compute $G_{1}^{\Delta_{\tau}}(\mathbf{x}, \mathbf{y})$ exactly, since the Hamiltonian $H_{1}$ can be efficiently diagonalized.

### 11.2 Particles in continuous space

Let us now give a specific example of the path-integral representation, and consider a system of interacting particles in continuous space, for which we consider again the general Hamiltonian:

$$
\begin{equation*}
\hat{H}=-\frac{\hbar^{2}}{2 m} \sum_{i}^{N} \nabla_{\vec{r}_{i}}^{2}+\sum_{i} V_{1}\left(\vec{r}_{i}\right)+\sum_{i<j} V_{2}\left(\vec{r}_{i}, \vec{r}_{j}\right) \tag{11.8}
\end{equation*}
$$

where $V_{1}$ and $V_{2}$ are generic one and two-body interaction potential. In this case, the computational basis denotes all the particle positions, i.e. $|\mathbf{x}\rangle=\left|\vec{r}_{1}, \vec{r}_{2}, \ldots \vec{r}_{N}\right\rangle$ and it is therefore a vector of $N 3$-dimensional coordinates. On top of that, we must consider the additional imaginary-time index, i.e. a full state in the path-integral is represented by all the quantum numbers $\left|\mathbf{x}_{j}\right\rangle=\left|\vec{r}_{j 1}, \vec{r}_{j 2}, \ldots \vec{r}_{j N}\right\rangle$, where for each particle we must specify its position in space at all the discrete times $j=0,1 \ldots P$. We therefore see that this representation corresponds to effectively having $N$ particles living in a 4-dimensional space (with the extra dimension coming from the imaginary time direction).

### 11.2.1 The Propagator

For the Hamiltonian (12.13), it is easy to derive a short-time propagator using the Trotter decomposition. In particular, call $H_{0}(\mathbf{X})=\sum_{i} V_{1}\left(\vec{r}_{i}\right)+\sum_{i<j} V_{2}\left(\vec{r}_{i}, \vec{r}_{j}\right)$, the part of the Hamiltonian diagonal in the computational basis, and $\hat{H}_{1}=-\frac{\hbar^{2}}{2 m} \sum_{i}^{N} \nabla_{\vec{r}_{i}}^{2}$, the non-commuting kinetic energy. We then have that the free-particle propagator is:

$$
\begin{aligned}
& G_{1}^{\Delta_{\tau}}(\mathbf{x}, \mathbf{y})=\left\langle\mathbf{x}\left|e^{-\Delta_{\tau} \sum_{i}^{N} \frac{\vec{P}_{1}^{2}}{2 m}}\right| \mathbf{y}\right\rangle \\
& =\Pi_{i=1}^{N}\left\langle\vec{r}_{i} \mid e^{-\Delta_{\tau} \vec{p}_{i}^{2}} 2 \vec{r}_{i}^{\prime}\right\rangle \\
& =\Pi_{i=1}^{N} \Pi_{\alpha}^{\{x, y, z\}}\left\langle r_{\alpha i}\left|e^{-\Delta_{\tau} \frac{\hat{P}_{\alpha i}^{2}}{2 m}}\right| r_{\alpha i}^{\prime}\right\rangle \\
& =\Pi_{i=1}^{N} \Pi_{\alpha}^{\{x, y, z\}} \sum_{n}\left\langle r_{\alpha i}\left|e^{-\Delta_{\tau} \frac{P_{i a i}^{2}}{2 m}}\right| P_{\alpha i}(n)\right\rangle\left\langle P_{\alpha i}(n) \mid r_{\alpha i}^{\prime}\right\rangle
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_05_17_d35cc01b6173225c8774g-03.jpg?height=128&width=856&top_left_y=1895&top_left_x=617)

$$
\begin{align*}
& =\left(\frac{m}{2 \pi \hbar^{2} \Delta_{\tau}}\right)^{3 N / 2} \Pi_{i=1}^{N} \Pi_{\alpha}^{\{x, y, z\}} \exp \left[-\frac{\left(r_{\alpha i}-r_{\alpha i}^{\prime}\right)^{2}}{2 \Delta_{\tau} \hbar^{2} / m}\right] \tag{11.9}
\end{align*}
$$

where $P_{\alpha}(n)=\hbar \frac{2 \pi}{L} n_{\alpha}$ are the eigenvalues of the momentum operator along the cartesian coordinate $\alpha,\left\langle r_{\alpha i} \mid P_{\alpha i}(n)\right\rangle=e^{i \frac{P_{\alpha i i}(n)}{h} r_{\alpha i}} / \sqrt{L}$ are the corresponding eigenfunctions. Notice that here we are assuming that we are dealing with a system having periodic boundary conditions in a 3 dimensional box of size $L \times L \times L$, thus yielding the quantization of the momentum $P_{\alpha}(n)$. The last line in the equation above is instead obtained approximating the discrete sum by a continuous integral, yielding the inverse Fourier transform of a gaussian function.

For a single, one-dimensional particle, the free propagator is the simple Gaussian:

$$
\begin{equation*}
G_{1}^{\Delta_{\tau}}(x, y)=\left(\frac{m}{2 \pi \hbar^{2} \Delta_{\tau}}\right)^{1 / 2} \exp \left[-\frac{(x-y)^{2}}{2 \Delta_{\tau} \hbar^{2} / m}\right] \tag{11.10}
\end{equation*}
$$

### 11.3 Path-Integral-Ground-State Monte Carlo

We have derived a representation of the wave-function in terms of sums over a path of configurations. Quantum Monte Carlo techniques based on this representation aim at sampling the exact ground-state wave-function, and in particular at sampling $|\langle\mathbf{x} \mid \Psi(\tau)\rangle|^{2}$, which can then be used to compute all the properties of the ground state, with an approach similar to the Variational method. We restrict now ourselves to real-valued wave-functions, for which we have:

$$
\begin{align*}
\langle\mathbf{x} \mid \Psi(\tau)\rangle^{2}=\sum_{\left\{\mathbf{x}_{j}, \mathbf{x}^{\prime} j\right\} \neq \mathbf{x}_{P}} \Psi\left(\mathbf{x}_{0}\right) G^{\Delta_{\tau}}\left(\mathbf{x}_{0},\right. & \left.\mathbf{x}_{1}\right) \ldots G^{\Delta_{\tau}}\left(\mathbf{x}_{P-1}, \mathbf{x}\right) \times \\
& \times G^{\Delta_{\tau}}\left(\mathbf{x}, \mathbf{x}_{P-1}^{\prime}\right) \ldots G^{\Delta_{\tau}}\left(\mathbf{x}_{1}^{\prime}, \mathbf{x}_{0}^{\prime}\right) \Psi\left(\mathbf{x}_{0}^{\prime}\right) \tag{11.11}
\end{align*}
$$

or, doubling the number of imaginary time slices:

$$
\begin{align*}
\langle\mathbf{x} \mid \Psi(\tau)\rangle^{2}=\sum_{\left\{\mathbf{x}_{j}\right\} \neq \mathbf{x}_{P}} \Psi\left(\mathbf{x}_{0}\right) G^{\Delta_{\tau}}( & \left.\mathbf{x}_{0}, \mathbf{x}_{1}\right) \ldots G^{\Delta_{\tau}}\left(\mathbf{x}_{P-1}, \mathbf{x}_{P}\right) \times \\
& \times G^{\Delta_{\tau}}\left(\mathbf{x}_{P}, \mathbf{x}_{P+1}\right) \ldots G^{\Delta_{\tau}}\left(\mathbf{x}_{2 P-1}, \mathbf{x}_{2 P}\right) \Psi\left(\mathbf{x}_{2 P}\right) \tag{11.12}
\end{align*}
$$

### 11.3.1 Statistical estimators of quantum expectation values

The expression (11.12) can be immediately used to estimate expectation values of some given observable. Let us concentrate for simplicity on diagonal observables, $O_{\mathbf{x x}^{\prime}}=$ $\delta_{\mathbf{x x}} O(\mathbf{x})$, for which we have

$$
\begin{align*}
\frac{\langle\Psi(\tau)|\hat{O}| \Psi(\tau)\rangle}{\langle\Psi(\tau) \mid \Psi(\tau)\rangle} & =\frac{\sum_{\mathbf{x}}\langle\mathbf{x} \mid \Psi(\tau)\rangle^{2} O(\mathbf{x})}{\sum_{\mathbf{x}}\langle\mathbf{x} \mid \Psi(\tau)\rangle^{2}} \\
& =\frac{\sum_{\left\{\mathbf{x}_{\mathrm{j}}\right\}} \Pi\left(\mathbf{x}_{0}, \ldots, \mathbf{x}_{2 P}\right) O\left(\mathbf{x}_{P}\right)}{\sum_{\left\{\mathbf{x}_{\mathbf{j}}\right\}} \Pi\left(\mathbf{x}_{0}, \ldots, \mathbf{x}_{2 P}\right)} \tag{11.13}
\end{align*}
$$

where we have defined

$$
\begin{align*}
\Pi\left(\mathbf{x}_{0}, \ldots, \mathbf{x}_{2 P}\right)=\Psi\left(\mathbf{x}_{0}\right) G^{\Delta_{\tau}}\left(\mathbf{x}_{0},\right. & \left.\mathbf{x}_{1}\right) \ldots G^{\Delta_{\tau}}\left(\mathbf{x}_{P-1}, \mathbf{x}_{P}\right) \times \\
& \times G^{\Delta_{\tau}}\left(\mathbf{x}_{P}, \mathbf{x}_{P+1}\right) \ldots G^{\Delta_{\tau}}\left(\mathbf{x}_{2 P-1}, \mathbf{x}_{2 P}\right) \Psi\left(\mathbf{x}_{2 P}\right) . \tag{11.14}
\end{align*}
$$

We immediately see that if we want to interpret the quantum expectation value (11.13), then the quantity $\Pi\left(\mathbf{x}_{0}, \ldots, \mathbf{x}_{2 P}\right)$ must have the meaning of a probability density, such that

$$
\begin{equation*}
\frac{\langle\Psi(\tau)|\hat{O}| \Psi(\tau)\rangle}{\langle\Psi(\tau) \mid \Psi(\tau)\rangle}=\mathbb{E}_{\Pi}\left[O\left(\mathbf{x}_{P}\right)\right] \tag{11.15}
\end{equation*}
$$

where $\mathbb{E}_{\Pi}[\ldots]$ denote statistical expectation values over the probability distribution $\Pi\left(\mathbf{x}_{0}, \ldots, \mathbf{x}_{2 P}\right)$ of the $2 P+1$ many-body particle coordinates.

An analogous expression can be derived for the estimator of the energy, using the fact that the Hamiltonian commutes with the imaginary-time evolution:

$$
\begin{align*}
\frac{\langle\Psi(\tau)|\hat{H}| \Psi(\tau)\rangle}{\langle\Psi(\tau) \mid \Psi(\tau)\rangle} & =\frac{\left\langle\Psi(\tau)\left|e^{-\tau \hat{H}} \hat{H}\right| \Psi(0)\right\rangle}{\langle\Psi(\tau) \mid \Psi(\tau)\rangle} \\
& =\frac{\sum_{\left\{\mathbf{x}_{\mathbf{j}}\right\}} \Pi\left(\mathbf{x}_{0}, \ldots, \mathbf{x}_{2 P}\right) \frac{\left\langle\mathbf{x}_{2 P}|\hat{H}| \Psi\right\rangle}{\left\langle\mathbf{x}_{2 P} \mid \Psi\right\rangle}}{\sum_{\left\{\mathbf{x}_{j}\right\}} \Pi\left(\mathbf{x}_{0}, \ldots, \mathbf{x}_{2 P}\right)} \\
& =\frac{\sum_{\left\{\mathbf{x}_{\mathbf{j}}\right\}} \Pi\left(\mathbf{x}_{0}, \ldots, \mathbf{x}_{2 P}\right) E_{\mathrm{loc}}\left(\mathbf{x}_{2 P}\right)}{\sum_{\left\{\mathbf{x}_{\mathbf{j}}\right\}} \Pi\left(\mathbf{x}_{0}, \ldots, \mathbf{x}_{2 P}\right)} \\
& =\mathbb{E}_{\Pi}\left[E_{\mathrm{loc}}\left(\mathbf{x}_{2 P}\right)\right] \tag{11.16}
\end{align*}
$$

where we have used the local energy, previously introduced when discussing the Variational Monte Carlo. Slightly reduced statistical fluctuations can be obtained taking the symmetrized estimator:

$$
\begin{align*}
\frac{\langle\Psi(\tau)|\hat{H}| \Psi(\tau)\rangle}{\langle\Psi(\tau) \mid \Psi(\tau)\rangle} & =\frac{1}{2}\left(\frac{\left\langle\Psi(\tau)\left|\hat{H} e^{-\tau \hat{H}}\right| \Psi(0)\right\rangle}{\langle\Psi(\tau) \mid \Psi(\tau)\rangle}+\frac{\left\langle\Psi(\tau)\left|e^{-\tau \hat{H}} \hat{H}\right| \Psi(0)\right\rangle}{\langle\Psi(\tau) \mid \Psi(\tau)\rangle}\right) \\
& =\frac{1}{2}\left(\mathbb{E}_{\Pi}\left[E_{\mathrm{loc}}\left(\mathbf{x}_{0}\right)+E_{\mathrm{loc}}\left(\mathbf{x}_{2 P}\right)\right]\right) \tag{11.17}
\end{align*}
$$

i.e. taking the averages of the local energies at the ends of the path, yielding a reduction in the statistical error on the average of about a factor of $1 / \sqrt{2}$.

### 11.3.1.1 Sign Problem

The exact ground-state properties (Eqs. 11.15,11.16) have the meaning of statistical averages over a probability distribution whenever $\Pi\left(\mathbf{x}_{0} \ldots \mathbf{x}_{2 P}\right) \geq 0$ for all the possible values of the path configurations. It is easy to show that for particles in continuous space the sign of $\Pi\left(\mathrm{x}_{0} \ldots \mathrm{x}_{2 P}\right)$ is given only by the sign of the product of the wave-function at the ends of the path: $\operatorname{sign}\left(\Pi\left(\mathbf{x}_{0} \ldots \mathbf{x}_{2 P}\right)\right)=\operatorname{sign}\left[\Psi\left(\mathbf{x}_{0}\right) \times \Psi\left(\mathbf{x}_{2 P}\right)\right]$.

For bosons, it can be shown that the exact ground state wave-function satisfies $\Psi_{0}(\mathrm{x}) \geq 0$. If we want that $\left|\left\langle\Psi_{0} \mid \Psi(0)\right\rangle\right|^{2} \neq 0$, this also implies that the wave function at $\tau=0$ is positive, thus $\operatorname{sign}\left(\Pi\left(\mathbf{x}_{0} \ldots \mathbf{x}_{2 P}\right)\right) \geq 0$. For bosons then we can find all the exact ground-properties just sampling from the path-integral distribution $\Pi\left(\mathbf{x}_{0} \ldots \mathbf{x}_{2 P}\right)$.

For fermions, instead, the wave-function $\Psi(0)$ must be antisymmetric with respect to particle permutations, if we want that $\left|\left\langle\Psi_{0} \mid \Psi(0)\right\rangle\right|^{2} \neq 0$. Therefore, $\Psi(0)$ obeys Fermi statistics and can take both negative and positive values. This means that we cannot interpret any longer $\Pi$ as a probability distribution, and we cannot find the exact ground-state properties (Eqs. 11.15,11.16) using statistical averages. This infamous situation is known as the sign problem in Quantum Monte Carlo methods.

### 11.4 Reptation Quantum Monte Carlo

If we are in the lucky situation that the path-integral density is positive definite, we can devise a Monte Carlo procedure that samples from $\Pi\left(\mathbf{x}_{0}, \ldots, \mathbf{x}_{2 P}\right)$. Here I describe a method known as "Reptation Quantum Monte Carlo" [1,2], which is one of the easiest strategies to sample from the path integral. The method is based on Markov Chain sampling, and therefore is fully specified by the transition probabilities $T\left(\mathbf{x} \rightarrow \mathbf{x}^{\prime}\right)$, of going from a given path configuration $\mathbf{x}=\mathbf{x}_{0} \ldots \mathbf{x}_{2 P}$ to a new one $\mathbf{x}^{\prime}=\mathbf{x}_{0}^{\prime} \ldots \mathbf{x}_{2 P}^{\prime}$

### 11.4.1 Monte Carlo moves

In the Reptation Quantum Monte Carlo we have two possible moves: one is called the "Right" move and the other one is called the "Left" move. The move then consists in the following: first pick at random (with uniform probability) wether to move Left or Right.

### 11.4.1.1 Move Right

If we pick the Right direction, the proposed configuration is $\mathbf{x}^{\prime}=\mathbf{x}_{1} \mathbf{x}_{2} \ldots \mathbf{x}_{2 P} \mathbf{x}_{T}$, where $\mathbf{x}_{0}$ is being discarded, and the new configuration $\mathbf{x}_{T}$ is added on the right. To generate $\mathbf{x}_{T}$ we use as a transition probability the free propagator:

$$
\begin{equation*}
T\left(\mathbf{x}_{2 P} \rightarrow \mathbf{x}_{T}\right)=G_{1}^{\Delta_{\tau}}\left(\mathbf{x}_{2 P}, \mathbf{x}_{T}\right) \tag{https://cdn.mathpix.com/cropped/2024_05_17_d35cc01b6173225c8774g-07.jpg?height=49&width=123&top_left_y=1299&top_left_x=1633}
\end{equation*}
$$

which is a Gaussian, and therefore we can easily generate random values for $\mathbf{x}_{T}$.

The acceptance probability for this move can be now computed to be:

$$
\begin{align*}
A_{R} & =\min \left[1, \frac{\Pi\left(\mathbf{x}_{1} \mathbf{x}_{2} \ldots \mathbf{x}_{2 P} \mathbf{x}_{T}\right)}{\Pi\left(\mathbf{x}_{0} \mathbf{x}_{1} \mathbf{x}_{2} \ldots \mathbf{x}_{2 P}\right)} \times \frac{T\left(\mathbf{x}_{1} \rightarrow \mathbf{x}_{0}\right)}{T\left(\mathbf{x}_{2 P} \rightarrow \mathbf{x}_{T}\right)}\right] \\
& =\min \left[1, \frac{\Psi\left(\mathbf{x}_{1}\right)}{\Psi\left(\mathbf{x}_{0}\right)} \frac{\Psi\left(\mathbf{x}_{T}\right)}{\Psi\left(\mathbf{x}_{2 P}\right)} \exp \left(-\frac{\Delta_{\tau}}{2} \Delta S_{R}\right)\right] \tag{11.19}
\end{align*}
$$

with

$$
\Delta S_{R}=H_{0}\left(\mathbf{x}_{T}\right)+H_{0}\left(\mathbf{x}_{2 P}\right)-H_{0}\left(\mathbf{x}_{0}\right)-H_{0}\left(\mathbf{x}_{1}\right) .
$$

This expression arises since most of the factors cancel out in the ratios, but for the ratio of factors at the ends of the path.

![](https://cdn.mathpix.com/cropped/2024_05_17_d35cc01b6173225c8774g-07.jpg?height=360&width=1037&top_left_y=1999&top_left_x=475)

Figure 11.1: Example of right move in the Reptation Quantum Monte Carlo. All configurations are shifted by one position in the path integral, with the leftmost being discarded and the rightmost being generated with the importance-sampled propagator.

### 11.4.1.2 Move Left

If we pick the Left direction, the proposed configuration is $\mathbf{x}^{\prime}=\mathbf{x}_{T} \mathbf{x}_{0} \ldots \mathbf{x}_{2 P-1}$, where $\mathbf{x}_{2 P}$ is being discarded, and the new configuration $\mathbf{x}_{T}$ is added on the left of the path. To generate $\mathbf{x}_{T}$ we use the transition probability $T\left(\mathbf{x}_{0} \rightarrow \mathbf{x}_{T}\right)=G_{1}^{\Delta_{\tau}}\left(\mathbf{x}_{0} \rightarrow \mathbf{x}_{T}\right)$, and the acceptance probability now reads:

$$
\begin{equation*}
A_{L}=\min \left[1, \frac{\Psi\left(\mathbf{x}_{T}\right)}{\Psi\left(\mathbf{x}_{0}\right)} \frac{\Psi\left(\mathbf{x}_{2 P-1}\right)}{\Psi\left(\mathbf{x}_{2 P}\right)} \exp \left(-\frac{\Delta_{\tau}}{2} \Delta S_{L}\right)\right] \tag{11.20}
\end{equation*}
$$

with

$$
\Delta S_{L}=H_{0}\left(\mathbf{x}_{T}\right)+H_{0}\left(\mathbf{x}_{0}\right)-H_{0}\left(\mathbf{x}_{2 P-1}\right)-H_{0}\left(\mathbf{x}_{2 P}\right)
$$

![](https://cdn.mathpix.com/cropped/2024_05_17_d35cc01b6173225c8774g-08.jpg?height=374&width=1022&top_left_y=864&top_left_x=563)

Figure 11.2: Example of left move in the Reptation Quantum Monte Carlo. All configurations are shifted by one position in the path integral, with the rightmost being discarded and the leftmost being generated with the importance-sampled propagator.

### 11.4.2 Practical aspects for the implementation

We now discuss some practical aspects useful for the implementation of the algorithm in the case of particles in continuous space.

In particular, a trial configuration is generated assigning positions to the $N$ particles, i.e. $\mathbf{x}_{T}=\vec{r}_{1}^{\prime}, \ldots \vec{r}_{N}^{\prime}$, with a probability $T\left(\mathbf{x} \rightarrow \mathbf{x}_{T}\right)$, as discussed previously.

To generate a trial configuration, starting from the configuration $\mathbf{x}=\vec{r}_{1}, \ldots \vec{r}_{N}$ (which in practice can be either the head or the tail of the path, depending on the chosen direction for the move), we do the following gaussian moves sampling from the free-particle propagator:

$$
\begin{equation*}
\vec{r}_{i}^{\prime}=\vec{r}_{i}+\sqrt{\Delta_{\tau}} \vec{\chi}_{i} \tag{11.21}
\end{equation*}
$$

where $\vec{\chi}_{i}$ is a vector containing $3 N$ independent, normally distributed random numbers.

### 11.4.2.1 Data Structure

As for almost any algorithm, first of all we have to specify a good data structure to hold the information we need. In particular, we want to store the path-integral configurations $\mathbf{x}_{0} \mathbf{x}_{1} \mathbf{x}_{2} \ldots \mathbf{x}_{2 P}$, where each $\left|\mathbf{x}_{i}\right\rangle=\left|\vec{r}_{i 1}, \vec{r}_{i 2}, \ldots \vec{r}_{i N}\right\rangle$. For example in python we might use a numpy ndarray with shape $(2 P+1, N, 3)$ such that $r_{i j \alpha}=\operatorname{conf}[i, \mathrm{j}, \alpha]$, where $i \in[0,2 P+1), j \in[0, N)$ and $\alpha \in[0,3)$ is the index corresponding to the spatial coordinate of the particle.

### 11.4.2.2 Putting everything together

At the beginning of our simulation, one typically does the following:

1. Pick the desired number of particles $N$
2. Pick a wave-function $\Psi(0)$ for which the local energy can be easily computed
3. Fix the total imaginary time $\tau$ and the number of time slices $P$.
4. Fix the total number of Monte Carlo moves to be done, $N_{s} \gg 1$.

A Monte Carlo move is then given by the following steps:

1. Generate the random direction $d$. To do so, take a uniform number $u \in[0,1)$, and if $u<0.5 d=$ LEFT, otherwise $d=$ RIGHT.
2. If $d=$ LEFT generate a trial configuration $\mathbf{x}_{T}$ with probability $T\left(\mathbf{x}_{2 P} \rightarrow \mathbf{x}_{T}\right)$, otherwise if $d=$ RIGHT with probability $T\left(\mathbf{x}_{2 P} \rightarrow \mathbf{x}_{T}\right)$.
3. Compute the ratios entering the acceptance factors: if moving left compute $R_{L}=$ $\frac{\Psi\left(\mathbf{x}_{T}\right)}{\Psi\left(\mathbf{x}_{0}\right)} \frac{\Psi\left(\mathbf{x}_{2 P-1}\right)}{\Psi\left(\mathbf{x}_{2 P}\right)} \exp \left(-\frac{\Delta_{T}}{2} \Delta S_{L}\right)$, otherwise $R_{R}=\frac{\Psi\left(\mathbf{x}_{1}\right)}{\Psi\left(\mathbf{x}_{0}\right)} \frac{\Psi\left(\mathbf{x}_{T}\right)}{\Psi\left(\mathbf{x}_{2 P}\right)} \exp \left(-\frac{\Delta_{T}}{2} \Delta S_{R}\right)$.
4. Generate a uniform random number $u \in[0,1)$, if $R_{d}>u$, then update the path configurations according to $\mathbf{x}^{(i+1)}=\mathbf{x}^{\prime}$, otherwise leave the path unchanged, and increase the Markov chain counter $i$ by one, i.e. $\mathbf{x}^{(i+1)}=\mathbf{x}^{(i)}$.
5. Measure the quantities of interest, for example compute the local energy on the end configuration of the path, or any other diagonal observable in the center of the path (Equations 11.15,11.16) and store these quantities in a vector $O^{(i)}$.

At the end of the simulation one then should:

1. Analyze the vector of observables, computing the average value $\mathbb{E}_{\Pi}[O(\mathbf{x})] \simeq$ $\frac{1}{N_{s}} \sum_{i} O\left(\mathbf{x}^{(i)}\right)$ and the variance (possibly corrected for correlations in the Markov chain, as explained in the previous lectures).

Further step to check the convergence to the ground-state wave-function and the effect of the Trotter splitting are:

1. Check that the time-step error is small enough, i.e. we can for example do another simulation with double the number of time slices (half the time step) and see if $\mathbb{E}_{\Pi}[O(\mathbf{x})]$ changes significantly beyond the statistical noise.
2. Check that the $\tau$ is large enough to have approached the ground-state energy. For example plot $\langle\hat{H}\rangle$ computed for values of increasing $\tau$ and see if you find convergence. This check should be done at parity of time-step, i.e. if for example we double the total imaginary time, we should equally double the value of $P$.

### 11.5 Importance Sampled Propagator in continuous space

In production codes, one rarely uses the simple form (11.18) for the transition probability. In particular, it is much more efficient to use the so-called importance-sampled propagator, which corresponds to taking a transition probability of the form:

$$
\begin{equation*}
\tilde{T}\left(\mathbf{x} \rightarrow \mathbf{x}_{T}\right)=\frac{1}{w(\mathbf{x})} G^{\Delta_{\tau}}\left(\mathbf{x}, \mathbf{x}_{T}\right) \frac{\Psi\left(\mathbf{x}_{T}\right)}{\Psi(\mathbf{x})} \tag{11.22}
\end{equation*}
$$

where $w(\mathbf{x})=\int d \mathbf{y} G^{\Delta_{\tau}}(\mathbf{x}, \mathbf{y}) \frac{\Psi(\mathbf{y})}{\Psi(\mathbf{x})}$ is a normalization factor. Considering again the case of particles in continuous space, it can be shown that for sufficiently small time step one can generate samples from the transition probability above $\tilde{T}\left(\mathbf{r} \rightarrow \mathbf{r}^{\prime}\right)$ by following the prescription:

$$
\begin{equation*}
\vec{r}_{i}^{\prime}=\vec{r}_{i}+\Delta_{\tau} \nabla_{r} \log \Psi\left(\vec{r}_{1}, \ldots \vec{r}_{N}\right)+\sqrt{\Delta_{\tau}} \vec{\chi}_{i} \tag{11.23}
\end{equation*}
$$

where $\vec{\chi}_{i}$ is a vector containing $3 N$ independent, normally distributed random numbers. When using the importance-sampled propagator, one has to change accordingly the acceptance probabilities, by taking into account the modified transition probability $\tilde{T}$. The resulting acceptance probabilities become:

$$
\begin{align*}
& \tilde{A}_{R}=\min \left[1, \exp \left(-\frac{\Delta_{\tau}}{2} \Delta \tilde{S}_{R}\right)\right]  \tag{11.24}\\
& \tilde{A}_{L}=\min \left[1, \exp \left(-\frac{\Delta_{\tau}}{2} \Delta \tilde{S}_{L}\right)\right] \tag{11.25}
\end{align*}
$$

with, respectively,

$$
\begin{align*}
& \Delta \tilde{S}_{R}=E_{\mathrm{loc}}\left(\mathbf{x}_{T}\right)+E_{\mathrm{loc}}\left(\mathbf{x}_{2 P}\right)-E_{\mathrm{loc}}\left(\mathbf{x}_{0}\right)-E_{\mathrm{loc}}\left(\mathbf{x}_{1}\right)  \tag{11.26}\\
& \Delta \tilde{S}_{L}=E_{\mathrm{loc}}\left(\mathbf{x}_{T}\right)+E_{\mathrm{loc}}\left(\mathbf{x}_{0}\right)-E_{\mathrm{loc}}\left(\mathbf{x}_{2 P-1}\right)-E_{\mathrm{loc}}\left(\mathbf{x}_{2 P}\right) \tag{11.27}
\end{align*}
$$

Notice that the effect of taking this specific transition probability is that we have introduced the local energy in the acceptance factors, instead of the diagonal Hamiltonian $H_{0}$. This allows to have much less fluctuations in the weights entering the acceptance factors, since typically $H_{0}$ contains diverging terms coming from the Coulomb interactions, that can result in rejecting most of the moves. On the contrary, if the initial state $\Psi$ is close to the exact ground state, then the fluctuations of the local energy are very small (see the discussion on the zero-variance principle in the previous lecture). Therefore, also the fluctuations of $\Delta \tilde{S}$ will be particularly small, and the acceptance probability very close to 1 . This algorithm therefore would sample efficiently groundstate configurations, without rejection, and correcting for the variational bias of the initial state.

### 11.6 Diffusion Quantum Monte Carlo

An alternative approach to implement imaginary-time evolution is the Diffusion Quantum Monte Carlo method (see Ref. [3] for a review). This method is one of the oldest

Quantum Monte Carlo methods, and it is not based on the Metropolis algorithm. I will not discuss it during my lecture, mostly because of time constraints. It should also be noticed that Metropolis-based schemes, like the one discussed at length in this lecture, are typically superior to the Diffusion Monte Carlo in terms of efficiency on large systems.

