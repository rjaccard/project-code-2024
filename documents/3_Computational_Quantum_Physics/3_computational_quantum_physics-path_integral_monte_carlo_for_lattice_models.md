## Path-Integral Monte Carlo for Lattice Models

In the previous Lecture we have introduced the finite-temperature path-integral Monte Carlo, and applied it to particles in continuous space. We now want to see how the path-integral formulation is applied to lattice (spin) models, and how we can devise a Monte Carlo algorithm to obtain finite-temperature properties.

### 13.1 Transverse-Field Ising model

The finite-temperature path-integral representation we have derived in the previous Lecture is completely general, and can be readily generalized to the case of spin systems. Let us consider once more as an example the transverse-field Ising model in one dimension:

$$
\begin{equation*}
\hat{H}=-\Gamma \sum_{i=0}^{N-1} \hat{\sigma}_{i}^{x}-J \sum_{i=0}^{N-1} \hat{\sigma}_{i}^{z} \hat{\sigma}_{i+1}^{z} \tag{13.1}
\end{equation*}
$$

for a system of $N$ spins and with periodic boundary conditions $\hat{\sigma}_{N}^{z} \equiv \hat{\sigma}_{0}^{z}$.

As a state vector, we will use the value of the spin projections along the $z$ direction, i.e. $|\mathbf{x}\rangle=\left|\sigma_{1}^{z} \sigma_{2}^{z} \ldots \sigma_{N}^{z}\right\rangle$, exactly as we have previously done with other techniques applied to spin models.

### 13.1.1 Short-Time propagator

The first thing we need to derive a useful path-integral formulation is then the propagator

$$
\begin{equation*}
G^{\Delta_{\tau}}(\mathbf{x}, \mathbf{y}) \equiv\left\langle\mathbf{x}\left|e^{-\Delta_{\tau} \hat{H}}\right| \mathbf{y}\right\rangle \tag{13.2}
\end{equation*}
$$

for which we invoke again the second-order Trotter decomposition:

$$
\begin{equation*}
G^{\Delta_{\tau}}(\mathbf{x}, \mathbf{y})=e^{-\Delta_{\tau} \frac{H_{0}(\mathbf{x})}{2}} G_{1}^{\Delta_{\tau}}(\mathbf{x}, \mathbf{y}) e^{-\Delta_{\tau} \frac{H_{0}(\mathbf{y})}{2}}+\mathcal{O}\left(\Delta_{t}^{2}\right) \tag{13.3}
\end{equation*}
$$

In this expression we identify the diagonal part: $H_{0}(\mathbf{x})=-\sum_{i} \hat{\sigma}_{i}^{z} \hat{\sigma}_{i+1}^{z}$ the classical energy, and

$$
\begin{align*}
G_{1}^{\Delta_{\tau}}(\mathbf{x}, \mathbf{y}) & =\left\langle\mathbf{x}\left|e^{\Delta_{\tau} \Gamma \sum_{i} \hat{\theta}_{i}^{x}}\right| \mathbf{y}\right\rangle \\
& =\Pi_{i}\left\langle\mathbf{x}\left|e^{\Delta_{\tau} \Gamma \hat{\sigma}_{i}^{x}}\right| \mathbf{y}\right\rangle \\
& =\Pi_{i} g_{1}^{\Delta_{\tau}}\left(\sigma_{i}^{z}(\mathbf{x}), \sigma_{i}^{z}(\mathbf{y})\right) \tag{13.4}
\end{align*}
$$

where we have first used the fact that all the different $\hat{\sigma}_{i}^{x}$ commute (thus the $\mathrm{N}$ spin propagator can be factorized, in the second line) and then introduced the single-spin propagators

$$
\begin{align*}
g_{1}^{\Delta_{\tau}}\left(\sigma^{z}, \sigma^{z^{\prime}}\right) & =\left\langle\sigma^{z}\left|\exp \left[\Delta_{\tau} \Gamma \hat{\sigma}^{x}\right]\right| \sigma^{z^{\prime}}\right\rangle \\
& =\left\langle\sigma^{z}\left|\left(\begin{array}{cc}
\cosh \Gamma \Delta_{\tau} & \sinh \Gamma \Delta_{\tau} \\
\sinh \Gamma \Delta_{\tau} & \cosh \Gamma \Delta_{\tau}
\end{array}\right)\right| \sigma^{z^{\prime}}\right\rangle \\
& =\delta_{\sigma^{z}, \sigma^{z^{\prime}}} \cosh \Gamma \Delta_{\tau}+\left(1-\delta_{\sigma^{z}, \sigma^{z^{\prime}}}\right) \sinh \Gamma \Delta_{\tau} \tag{13.5}
\end{align*}
$$

### 13.1.2 Path-Integral expression

We then consider the thermal density matrix of the system $\hat{\rho}^{\beta}=\exp (-\beta \hat{H}) / Z$, where $\beta=1 / k_{B} T$, with $k_{B}$ the Boltzmann's constant, and $T$ the temperature of the system and the partition function:

$$
\begin{equation*}
Z=\sum_{\mathbf{x}_{0}} \rho^{\beta}\left(\mathbf{x}_{0}, \mathbf{x}_{0}\right) \tag{13.6}
\end{equation*}
$$

The path-integral expression for the partition function has been derived in the previous Lecture and reads:

$$
\begin{equation*}
Z=\sum_{\mathbf{x}_{0} \ldots \mathbf{x}_{P-1}} \Pi_{j=0}^{P-1} G_{1}^{\Delta_{\tau}}\left(\mathbf{x}_{j}, \mathbf{x}_{j+1}\right) e^{-\Delta_{\tau} H_{0}\left(\mathbf{x}_{j}\right)} \tag{13.7}
\end{equation*}
$$

with periodic boundaries in imaginary time, i.e. $\mathbf{x}_{\mathbf{p}}=\mathbf{x}_{\mathbf{0}}$. In this case the path-integral configurations are completely determined by the value of the $i$-th spin at each imaginary time $j=0, \ldots P$. We call these values $\sigma_{i j}^{z}$, such that the full many-body configuration at given imaginary-time is given by $\mathbf{x}_{j}=\sigma_{N j}^{z}, \sigma_{2 j}^{z} \ldots, \sigma_{N j}^{z}$. The path-integral formulation then maps the 1D quantum model for $N$ spins onto the 2D classical model for $N \times P$ effective spins.

### 13.1.3 Classical 2D Ising Model

We can actually do more than that and show that the 2D classical system is a simple classical Ising model, with some specific couplings. In order to do so, we start noticing that the single-spin propagator can be written as the exponential of an effective
interaction between the spins $\sigma^{z}$ and $\sigma^{z^{\prime}}$ :

$$
\begin{align*}
g_{1}^{\Delta_{\tau}}\left(\sigma^{z}, \sigma^{z^{\prime}}\right)= & \exp \left[\frac{1}{2}\left(1+\sigma^{z} \sigma^{z^{\prime}}\right) \log \left(\cosh \Gamma \Delta_{\tau}\right)+\right. \\
& \left.+\frac{1}{2}\left(1-\sigma^{z} \sigma^{z^{\prime}}\right) \log \left(\sinh \Gamma \Delta_{\tau}\right)\right]  \tag{13.8}\\
= & \exp \left[\sigma^{z} \sigma^{z^{\prime}} \frac{1}{2}\left[\log \left(\cosh \Gamma \Delta_{\tau}\right)-\log \left(\sinh \Gamma \Delta_{\tau}\right)\right]\right] \times \\
& \times \exp \left[\frac{1}{2}\left[\log \left(\cosh \Gamma \Delta_{\tau}\right)+\log \left(\sinh \Gamma \Delta_{\tau}\right)\right]\right]  \tag{13.9}\\
= & e^{-\sigma^{z} \sigma^{z^{\prime}} \cdot \text { jeff }} \times \text { const } \tag{13.10}
\end{align*}
$$

with $J^{\text {eff }}=\frac{1}{2} \log \left(\tanh \Gamma \Delta_{\tau}\right)$. From this expression, it is then easy to realize that that the quantum partition function is completely equivalent to the classical partition function:

$$
\begin{align*}
Z & =\sum_{\left\{\sigma_{i, j}^{z}\right\}} e^{-\beta^{\mathrm{eff}} E^{\mathrm{eff}}\left(\sigma_{i, j}^{z}\right)}  \tag{13.11}\\
& =\sum_{\left\{\sigma_{i, j}^{z}\right\}} \exp \left[-\sum_{i} \sum_{j}\left(-\Delta_{\tau} J \sigma_{i, j}^{z} \sigma_{i+1, j}^{z}+J^{\text {eff }} \sigma_{i, j}^{z} \sigma_{i, j+1}^{z}\right)\right] \tag{13.12}
\end{align*}
$$

The classical energy is therefore simply that of a classical Ising model in 2 dimensions:

$$
\begin{equation*}
E^{\text {eff }}\left(\sigma_{i, j}^{z}\right)=\sum_{i=0}^{N-1} \sum_{j=0}^{P-1}\left(-\Delta_{\tau} J \sigma_{i, j}^{z} \sigma_{i+1, j}^{z}+J^{\text {eff }} \sigma_{i, j}^{z} \sigma_{i, j+1}^{z}\right) \tag{13.13}
\end{equation*}
$$

where we have periodic boundary conditions both in the spatial axis $\left(\sigma_{N}^{z} \equiv \sigma_{0}^{z}\right)$ and in the imaginary-time axis $\left(\sigma_{P}^{z} \equiv \sigma_{0}^{z}\right)$, and the effective classical inverse temperature is just $\beta^{\text {eff }}=1$. An example of configuration is shown in Figure 13.1.

![](https://cdn.mathpix.com/cropped/2024_05_17_9c01516965c9153c9dbag-4.jpg?height=745&width=1511&top_left_y=267&top_left_x=318)

Figure 13.1: Example of path-integral configurations for the transverse-field Ising model in one dimension. The quantum partition function is equivalent to the classical partition function of a two-dimensional Ising model with couplings $\Delta_{\tau} J$ along the spatial direction (vertical axis in the Figure) and $J^{\text {eff }}=-\frac{1}{2} \log \left(\tanh \Gamma \Delta_{\tau}\right)$ along the imaginary-time direction (horizontal axis in the Figure). In the Figure, there are $N=3$ spins and $P=4$ imaginary-time slices, with periodic boundary conditions along both directions.

### 13.1.4 Monte Carlo Sampling

Once established the equivalent classical partition function, Eq. (13.11), we can readily devise a Markov-Chain Monte Carlo sampling strategy to generate path-integral configurations. In particular, any classical Monte Carlo algorithm used to sample the partition function of the Ising model can be used. One of the simplest approach (albeit ineffective in the ferromagnetic phase) is to use single spin flip moves.

We can just pick uniformly both a spatial and a time index, respectively $i \in[0, N)$ and $j \in[0, P)$ and propose a spin flip for the $\sigma_{i j}^{z}$ spin. In the new configuration we would then have $\sigma_{i j}^{z \prime}=-\sigma_{i j}^{z}$, and the acceptance probability is readily computed to be:

$$
\begin{align*}
& A_{S}\left(\sigma_{i j}^{z} \rightarrow \sigma_{i j}^{z \prime}\right)= \\
& \quad=\min \left[1, \frac{\exp \left[-\Delta_{\tau} J\left(\sigma_{i-1, j}^{z} \sigma_{i, j}^{z \prime}+\sigma_{i, j}^{z \prime} \sigma_{i+1, j}^{z}\right)-J^{\text {eff }}\left(\sigma_{i, j-1}^{z} \sigma_{i, j}^{z \prime}+\sigma_{i, j}^{z^{\prime}} \sigma_{i, j+1}^{z}\right)\right]}{\exp \left[-\Delta_{\tau} J\left(\sigma_{i-1, j}^{z} \sigma_{i, j}^{z}+\sigma_{i, j}^{z} \sigma_{i+1, j}^{z}\right)-J^{\text {eff }}\left(\sigma_{i, j-1}^{z} \sigma_{i, j}^{z}+\sigma_{i, j}^{z} \sigma_{i, j+1}^{z}\right)\right]}\right] \\
& =\min \left[1, \exp \left[2 \Delta_{\tau} J\left(\sigma_{i-1, j}^{z} \sigma_{i, j}^{z}+\sigma_{i, j}^{z} \sigma_{i+1, j}^{z}\right)+2 J^{\text {eff }}\left(\sigma_{i, j-1}^{z} \sigma_{i, j}^{z}+\sigma_{i, j}^{z} \sigma_{i, j+1}^{z}\right)\right]\right] \tag{13.14}
\end{align*}
$$

### 13.1.5 Energy Estimator

An estimator for the expectation value of the energy can be immediately found using again the thermodynamics relation $\langle H\rangle_{T}=-\partial_{\beta} \log Z$. I leave as an exercise to derive it in this case.

### 13.2 Continuous-Time path integrals

The most remarkable difference between lattice and continuous-space systems is that for lattice models we can efficiently (and exactly) take the continuous-time limit $\Delta_{\tau} \rightarrow 0$, whereas for systems in continuous space this is not the case. To see how we can eventually get rid of the Trotter error, we need to introduce a different representation of the partition function, based on a perturbative expansion.

The starting point is the Dyson series for the exponential of a matrix:

$$
e^{-\beta\left(\hat{H}_{0}+\hat{H}_{1}\right)}=e^{-\beta \hat{H}_{0}} \sum_{n=0}^{\infty}(-1)^{n} \underbrace{\int d \tau_{1} \ldots d \tau_{n}}_{0<\tau_{1} \leq \cdots \leq \tau_{n}<\beta} \hat{H}_{1}\left(\tau_{n}\right) \ldots \hat{H}_{1}\left(\tau_{1}\right)
$$

where $\hat{H}_{1}(\tau)=e^{\tau \hat{H}_{0}} \hat{H}_{1} e^{-\tau \hat{H}_{0}}$ is the time-evolved $\hat{H}_{1}$ in the so-called "interaction representation". The Dyson series is basically the exact summation of all the contributions in perturbation theory, of order $\hat{H}_{1}^{n}$ with $n=0,1 \ldots \infty$. Notice that the imaginary times arising in the integrals are t-ordered, i.e. $0<\tau_{1} \leq \cdots \leq \tau_{n}<\beta .{ }^{1}$

As much as we have done for the path-integral representation of the exponential, we can derive now an expression we can sample from using Monte Carlo. In particular, we will need now not only to sample over the spin configurations at different imaginary times, but also over all the possible orders in perturbation theory $n$, and over all the possible values of the times. Let us start by considering the first few terms, and inserting completeness in the middle:

$$
\begin{align*}
Z= & \sum_{\mathbf{x}_{0}}\left\langle\mathbf{x}_{0}\left|e^{-\beta \hat{H}_{0}}\right| \mathbf{x}_{0}\right\rangle-\sum_{\mathbf{x}_{1}} e^{-\beta H_{0}\left(\mathbf{x}_{1}\right)} \int_{0}^{\beta} d \tau_{1}\left\langle\mathbf{x}_{1}\left|\hat{H}_{1}\right| \mathbf{x}_{1}\right\rangle+ \\
& +\sum_{\mathbf{x}_{1}, \mathbf{x}_{2}} e^{-\beta H_{0}\left(\mathbf{x}_{2}\right)} \int_{0}^{\beta} d \tau_{2} \int_{0}^{\tau_{2}} d \tau_{1} e^{\left(\tau_{2}-\tau_{1}\right) H_{0}\left(\mathbf{x}_{2}\right)}\left\langle\mathbf{x}_{2}\left|\hat{H}_{1}\right| \mathbf{x}_{1}\right\rangle e^{\left(\tau_{1}-\tau_{2}\right) H_{0}\left(\mathbf{x}_{1}\right)}\left\langle\mathbf{x}_{1}\left|\hat{H}_{1}\right| \mathbf{x}_{2}\right\rangle+ \\
& +\ldots \tag{13.15}
\end{align*}
$$

The goal of our Monte Carlo sampling will be now to sample from the probability distribution

$$
\begin{align*}
& \Pi_{\mathrm{ct}}\left(\mathbf{x}_{1} \ldots \mathbf{x}_{n}, \tau_{1} \ldots \tau_{n}, n\right)= \\
& \quad=\frac{1}{Z} e^{-\beta H_{0}\left(\mathbf{x}_{n}\right)}(-1)^{n} \hat{H}_{1}\left(\mathbf{x}_{n}, \mathbf{x}_{n-1}, \tau_{n}\right) \ldots \hat{H}_{1}\left(\mathbf{x}_{2}, \mathbf{x}_{1}, \tau_{2}\right) \hat{H}_{1}\left(\mathbf{x}_{1}, \mathbf{x}_{n}, \tau_{1}\right) \tag{13.16}
\end{align*}
$$

where we have introduced the matrix elements $H_{1}\left(\mathbf{x}, \mathbf{x}^{\prime}, \tau\right)=e^{\tau H_{0}(\mathbf{x})}\left\langle\mathbf{x}\left|\hat{H}_{1}\right| \mathbf{x}^{\prime}\right\rangle e^{-\tau H_{0}\left(\mathbf{x}^{\prime}\right)}$.

In general, in order to sample from this probability distribution we have not include a set of Markov-Chain moves that:

1. Change the spin configurations, $\mathbf{x}_{j}$
2. Change the perturbation order, $n$[^0]
3. Move the imaginary times, according to the time-ordering constraint

As a result of this extended sampling space (with respect to the standard path-integral configurations, comprising only the set 1 in the previous list), we will have that our simulation will not carry any time-step error!

I will now discuss an example where these moves can be seen explicitly at work.

![](https://cdn.mathpix.com/cropped/2024_05_17_9c01516965c9153c9dbag-6.jpg?height=663&width=923&top_left_y=571&top_left_x=612)

Figure 13.2: Example of allowed configurations for the continuous-time path-integral for a single spin. Different perturbative order are shown (notice that they are all even), and vertical dashed lines denote periodic boundaries in imaginary time. In each configuration (but for the special case $n=0$ ) the total number of up spins must match the total number of down spins, and each spin is followed in imaginary time by a spin of opposite sign.

### 13.2.1 Example: single spin Hamiltonian

To give a concrete example, let us now examine the expressions above in the case of a simple single-spin Hamiltonian: $\hat{H}=-\Gamma \hat{\sigma}_{x}+\Gamma_{z} \hat{\sigma}_{z}$, and take $\hat{H}_{0}=\Gamma_{z} \hat{\sigma}_{z}, \hat{H}_{1}=-\Gamma \hat{\sigma}_{x}$. We therefore have that $H_{1}\left(\sigma^{z}, \sigma^{z^{\prime}}, \tau\right)=\left\langle\sigma^{z}\left|H_{1}(\tau)\right| \sigma^{z \prime}\right\rangle=-\Gamma e^{\Gamma_{z} \tau\left(\sigma_{z}-\sigma_{z}^{\prime}\right)}\left(1-\delta_{\sigma_{z}, \sigma_{z}^{\prime}}\right)=$ $-\left(1-\delta_{\sigma_{z}, \sigma_{z}^{\prime}}\right) \Gamma e^{2 \Gamma_{z} \tau \sigma^{z}}$, where in the last equality we have used the fact that we need $\sigma_{z}^{\prime}=-\sigma_{z}$ for the matrix element to be non-vanishing. In this case the probability to be sampled is therefore:

$$
\begin{align*}
\Pi_{\mathrm{ct}}\left(\sigma_{1}^{z} \ldots \sigma_{n}^{z}, \tau_{1} \ldots \tau_{n}, n\right) & = \\
= & \frac{1}{Z} \Gamma^{n} e^{-\beta \sigma_{n}^{z}} e^{2 \Gamma_{z} \sum_{j=1}^{n} \tau_{j} \sigma_{j}^{z}} C(\sigma, n, \tau) \tag{13.17}
\end{align*}
$$

where we have introduced a constraint on the allowed configurations:

$$
\begin{equation*}
C(\sigma, n, \tau)=\delta\left(\sigma_{j}^{z} \neq \sigma_{(j+1)}^{z} \bmod n\right) \times \delta_{n, 2 k} \times \delta\left(0<\tau_{1} \leq \tau_{2} \leq \ldots \tau_{n}<\beta\right) \tag{13.18}
\end{equation*}
$$

The first constraint comes from the fact that the matrix elements of $\hat{H}_{1}$ are purely off-diagonal, and we must flip a spin every time we introduce a term $\hat{H}_{1}$ in the path.

The second constraint implies that we must have only an even number of terms $\hat{H}_{1}$, since because of the periodic boundary conditions in time this is the only way to have a non-vanishing total weight. The third constraint comes from the t-ordered product in the Dyson series.

Examples of allowed configurations corresponding to the continuous-time path integral are those represented in Fig. 13.2.

Let us now discuss in detail how to devise a set of moves for all the previously listed quantities.

![](https://cdn.mathpix.com/cropped/2024_05_17_9c01516965c9153c9dbag-7.jpg?height=1139&width=1105&top_left_y=701&top_left_x=447)

Figure 13.3: Example of moves in the continuos-time path-integral Monte Carlo. The left Figure shows the insertion of two spins at two random times $\tau_{a}<\tau_{b}$, followed (if necessary) by flipping the intermediate spins to satisfy the constraint. The right Figure shows the inverse move, in which two random spins at times $\tau_{a}$ and $\tau_{b}$ are randomly picked and deleted. This move is again followed by flipping any intermediate spin to satisfy the constraint in the final configuration.

### 13.2.1.1 Inserting and erasing pair of vertexes

Since the perturbation order can change only in multiples of 2, in our Monte Carlo sampling we should have a move that inserts/deletes pairs of terms $H_{1}\left(\tau_{a}\right) H_{1}\left(\tau_{b}\right)$. To this end, we generate two random times $\tau_{a} \in[0, \beta)$ and $\tau_{b} \in[0, \beta)$. Let us assume that $\tau_{a}<\tau_{b}$ (if it is not the case, just exchange the labels $a \leftrightarrow b$. Now, call $\tau_{\text {left }}<\tau_{a}$ the first time already existing in the path on the left of $\tau_{a}$, and call $\tau_{\text {right }}>\tau_{b}$ the first time
already existing in the path on the right of $\tau_{b}$. In all the discussion we always assume periodic boundary conditions along the time direction, which also of course reflect on the correct ordering of the times.

When inserting a spin flip at $\tau_{a}$ we must set $\sigma_{a}^{z}=-\sigma_{\text {left }}^{z}$ and equally $\sigma_{b}^{z}=-\sigma_{\text {right }}^{z}$. If in the existing path we had intermediate times between $\tau_{a}$ and $\tau_{b}$, say $\tau_{a}<\tau_{j}<$ $\tau_{j+1} \cdots<\tau_{b}$ then we must flip all the intermediate spins in order to satisfy the constraint that consecutive spins in imaginary times have opposite signs. An example of this operation is shown in Fig. 13.3.

### 13.3 Stochastic Series Expansion

The continuous-time formulation is not the only way of getting rid of the time-step error. An alternative approach is baed on the Taylor series for the matrix exponential:

$$
\begin{equation*}
e^{-\beta \hat{H}}=\sum_{n=0}^{\infty} \frac{(-\beta \hat{H})^{n}}{n!} \tag{13.19}
\end{equation*}
$$

and is dubbed "Stochastic Series Expansion" 2 . Using this expansion, we then just insert completeness at each order $n$, in a way that the partition function becomes:

$$
\begin{align*}
Z= & \sum_{\mathbf{x}_{1}}\left\langle\mathbf{x}_{1}|\hat{I}| \mathbf{x}_{1}\right\rangle+\sum_{\mathbf{x}_{1}}\left\langle\mathbf{x}_{1}|-\beta \hat{H}| \mathbf{x}_{1}\right\rangle+ \\
& +\sum_{\mathbf{x}_{1}, \mathbf{x}_{2}} \frac{\left\langle\mathbf{x}_{1}|-\beta \hat{H}| \mathbf{x}_{2}\right\rangle\left\langle\mathbf{x}_{2}|-\beta \hat{H}| \mathbf{x}_{1}\right\rangle}{2}+ \\
& +\ldots \tag{13.20}
\end{align*}
$$

The probability distribution to be sampled then depends on the perturbation order and on the path configurations:

$$
\begin{align*}
& \Pi_{\mathrm{sse}}\left(\mathbf{x}_{1} \ldots \mathbf{x}_{n}, n\right) \propto \\
& \quad=\frac{\beta^{n}}{n!}\left\langle\mathbf{x}_{1}|-\hat{H}| \mathbf{x}_{2}\right\rangle \ldots\left\langle\mathbf{x}_{-1}|-\hat{H}| \mathbf{x}_{n}\right\rangle\left\langle\mathbf{x}_{n}|-\hat{H}| \mathbf{x}_{1}\right\rangle \tag{13.21}
\end{align*}
$$

A Monte Carlo procedure in this case must then be able to propose changes in the perturbation order and in the configurations at different points in the SSE path.

For the previously considered example of the single-spin Hamiltonian, the SSE paths would not need to obey the constraint of alternating opposite spins $\sigma_{j}^{z} \neq \sigma_{(j+1) \bmod n}^{z}$, since the matrix elements entering the SSE weight are those of the full Hamiltonian and not only of the off-diagonal part $\hat{H}_{1}$. I leave as an exercise to think about possible ways of updating the SSE paths.

A point to be remarked here is that, albeit the sum over $n$ in principle goes to infinity, in practice the number of orders that need to be sampled is finite, and can be done efficiently using Monte Carlo moves. A way to think about this is when sampling from the probability distribution of a Normal variable Normal(x), for which in principle we[^1]should generate values in the interval $x \in(-\infty,+\infty)$, however the probability of having very large (in modulus) values of $x$ is exponentially suppressed, and typical samples will lie in a finite interval. The same thing happens for the discrete variable $n \in[0, \infty)$, which in fact has a finite average value $|\langle n\rangle|=\beta\langle H\rangle \propto N \beta$ and a finite variance $\left\langle n^{2}\right\rangle-\langle n\rangle^{2} \propto N \beta$. These two last relations can be easily derived directly considering the definition of the expectation values, for example we have the very elegant relation:

$$
\begin{align*}
\langle\hat{H}\rangle= & \frac{1}{Z} \sum_{n=0}^{\infty} \sum_{\mathbf{x}_{1}} \frac{\beta^{n}}{n!}\left\langle\mathbf{x}_{1}\left|(-\hat{H})^{n} \hat{H}\right| \mathbf{x}_{1}\right\rangle  \tag{13.22}\\
= & -\frac{1}{Z} \sum_{n=0}^{\infty} \sum_{\mathbf{x}_{1}} \frac{\beta^{n}}{n!}\left\langle\mathbf{x}_{1}\left|(-\hat{H})^{n+1}\right| \mathbf{x}_{1}\right\rangle  \tag{13.23}\\
& -\frac{1}{Z} \sum_{n=1}^{\infty} \sum_{\mathbf{x}_{1}} \frac{\beta^{n-1}}{n-1!}\left\langle\mathbf{x}_{1}\left|(-\hat{H})^{n}\right| \mathbf{x}_{1}\right\rangle  \tag{13.24}\\
= & -\frac{1}{Z \beta} \sum_{n=1}^{\infty} \sum_{\mathbf{x}_{1}} \frac{\beta^{n} n}{n!}\left\langle\mathbf{x}_{1}\left|(-\hat{H})^{n}\right| \mathbf{x}_{1}\right\rangle  \tag{13.25}\\
= & -\frac{\langle n\rangle}{\beta} \tag{13.26}
\end{align*}
$$


[^0]:    ${ }^{1} \mathrm{~A}$ good and self-contained derivation of the Dyson series can be found at https://en.wikipedia. org/wiki/Dyson_series.

[^1]:    ${ }^{2}$ Anders W. Sandvik, Phys. Rev. E 68,056701 (2003)

