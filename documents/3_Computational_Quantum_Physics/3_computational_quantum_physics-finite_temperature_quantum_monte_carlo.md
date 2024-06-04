## Finite-Temperature Quantum Monte Carlo

In the previous Lecture we have introduced our first path-integral methods. We have seen that one can obtain an exact representation of the imaginary time evolution, and then sample from the ground-state wave-function using Monte Carlo techniques. During this Lecture we will see how similar ideas can be applied to study finite-temperature properties.

### 12.1 Thermal Density Matrix

All the static properties of a quantum many-body system in thermal equilibrium are obtainable from the thermal density matrix $\rho^{\beta}=\exp (-\beta \hat{H})$, where $\beta=1 / k_{B} T$, with $k_{B}$ the Boltzmann's constant, and $T$ the temperature of the system. The expectation value of an observable operator $O$ is:

$$
\begin{equation*}
\langle\hat{O}\rangle=\frac{\operatorname{Tr}\left(\hat{O} e^{-\beta \hat{H}}\right)}{Z} \tag{12.1}
\end{equation*}
$$

where the partition function $Z$ is the trace of the density matrix:

$$
\begin{equation*}
Z=\operatorname{Tr}(\exp (-\beta \hat{H})) \tag{12.2}
\end{equation*}
$$

We denote the matrix elements of the unnormalized density matrix in some many-body basis $|\mathbf{x}\rangle$ as:

$$
\begin{equation*}
\rho^{\beta}(\mathbf{x}, \mathbf{y}) \equiv\langle\mathbf{x}|\exp (-\beta \hat{H})| \mathbf{y}\rangle \tag{12.3}
\end{equation*}
$$

The partition function is the integral of the diagonal matrix elements over all possible configurations:

$$
\begin{equation*}
Z(N, T, V)=\sum_{\mathbf{x}} \rho^{\beta}(\mathbf{x}, \mathbf{x}) \tag{12.4}
\end{equation*}
$$

and we have made explicit that in general this quantity depends on the number of particles, the temperature, and the volume $V$ in which we assume the particles are confined.

Comparing Equation (12.3) with the expression for the imaginary-time propagator, introduced in the previous lecture, we immediately see that the density matrix elements coincides with the propagator of total imaginary-time $\beta$ :

$$
\begin{equation*}
\rho^{\beta}(\mathbf{x}, \mathbf{y})=G^{\beta}(\mathbf{x}, \mathbf{y}) \tag{12.5}
\end{equation*}
$$

The inverse temperature then plays here the role of an effective imaginary time. This important connection allows us to immediately use all the path-integral machinery we have introduced in the previous Lecture.

In particular, we introduce again a small time step $\Delta_{\tau}$, such that $\beta=P \times \Delta_{\tau}$, and write the density matrix in the path-integral form:

$$
\begin{equation*}
\rho^{\beta}(\mathbf{x}, \mathbf{y})=\sum_{\mathbf{x}_{1} \ldots \mathbf{x}_{P-1}} \underbrace{G^{\Delta_{\tau}}\left(\mathbf{x}_{0}, \mathbf{x}_{1}\right) \ldots G^{\Delta_{\tau}}\left(\mathbf{x}_{P-1}, \mathbf{x}_{P}\right)}_{P \text { times }}, \tag{12.6}
\end{equation*}
$$

where we have identified $\mathbf{x}_{0} \equiv \mathbf{x}$ and $\mathbf{x}_{P} \equiv \mathbf{y}$. As explained in the previous lecture, the representation (12.6) is useful because we typically know how to compute controlled numerical approximations of the short-time propagators $G^{\Delta_{\tau}}\left(\mathbf{x}_{0}, \mathbf{x}_{1}\right)$. In particular, we have seen that in several interesting applications the Hamiltonian is the sum of two non-commuting terms, $\hat{H}=\hat{H}_{0}+\hat{H}_{1}$, where the first term is diagonal in the chosen basis $|\mathbf{x}\rangle$. In that case we then use the second-order Trotter approximation:

$$
\begin{equation*}
G^{\Delta_{\tau}}(\mathbf{x}, \mathbf{y})=e^{-\Delta_{\tau} \frac{H_{0}(\mathbf{x})}{2}} G_{1}^{\Delta_{\tau}}(\mathbf{x}, \mathbf{y}) e^{-\Delta_{\tau} \frac{H_{0}(\mathbf{y})}{2}}+\mathcal{O}\left(\Delta_{t}^{2}\right) \tag{12.7}
\end{equation*}
$$

Using this decomposition, we see that the trace of the density matrix (12.4) takes the form:

$$
\begin{align*}
\sum_{\mathbf{x}_{0}} \rho^{\beta}\left(\mathbf{x}_{0}, \mathbf{x}_{0}\right) & =\sum_{\mathbf{x}_{0}, \mathbf{x}_{1} \ldots \mathbf{x}_{P-1}} G^{\Delta_{\tau}}\left(\mathbf{x}_{0}, \mathbf{x}_{1}\right) \ldots G^{\Delta_{\tau}}\left(\mathbf{x}_{P-1}, \mathbf{x}_{0}\right) \\
& =\sum_{\mathbf{x}_{0}, \mathbf{x}_{1} \ldots \mathbf{x}_{P-1}} G_{1}^{\Delta_{\tau}}\left(\mathbf{x}_{0}, \mathbf{x}_{1}\right) e^{-\Delta_{\tau} H_{0}\left(\mathbf{x}_{0}\right)} \ldots G_{1}^{\Delta_{\tau}}\left(\mathbf{x}_{P-1}, \mathbf{x}_{0}\right) e^{-\Delta_{\tau} H_{0}\left(\mathbf{x}_{P-1}\right)} \\
& =\sum_{\mathbf{x}_{0}, \mathbf{x}_{1} \ldots \mathbf{x}_{P-1}} \Pi_{i=0}^{P-1} G_{1}^{\Delta_{\tau}}\left(\mathbf{x}_{i}, \mathbf{x}_{i+1}\right) e^{-\Delta_{\tau} H_{0}\left(\mathbf{x}_{i}\right)} \tag{12.8}
\end{align*}
$$

Since we have periodic boundaries in imaginary time, i.e. $\mathbf{x}_{\mathrm{p}}=\mathbf{x}_{\mathbf{0}}$, then all points in the path are equivalent. In this case we can imagine that the paths are closed rings, whereas in the zero-temperature, ground-state Path-Integral, the paths have open ends (reptiles with heads and tails).

### 12.1.1 Computing Properties

Having found an explicit path-integral expression for the thermal density matrix, we can also express the expectation values of observables in terms of this representation. For example, the expectation value of a diagonal operator:

$$
\begin{align*}
\langle\hat{O}\rangle & =\frac{\operatorname{Tr}\left(\hat{O} e^{-\beta \hat{H}}\right)}{Z} \\
& =\frac{\sum_{\mathbf{x}_{0}} \rho^{\beta}\left(\mathbf{x}_{0}, \mathbf{x}_{0}\right) O\left(\mathbf{x}_{0}\right)}{\sum_{\mathbf{x}_{0}} \rho^{\beta}\left(\mathbf{x}_{0}, \mathbf{x}_{0}\right)} \tag{12.9}
\end{align*}
$$

If we introduce

$$
\begin{equation*}
\Pi\left(\mathbf{x}_{0}, \mathbf{x}_{1}, \ldots \mathbf{x}_{P}\right) \equiv \Pi_{i=0}^{P-1} G_{1}^{\Delta_{\tau}}\left(\mathbf{x}_{i}, \mathbf{x}_{i+1}\right) e^{-\Delta_{\tau} H_{0}\left(\mathbf{x}_{i}\right)} \tag{12.10}
\end{equation*}
$$

we can immediately notice that the finite-temperature quantum expectation values, Eq. (12.9), can be interpreted as statistical expectation values over the distribution $\Pi$, if this is positive definite. In the absence of a sign problem, we can therefore write

$$
\begin{equation*}
\langle O\rangle=\mathbb{E}_{\Pi}\left[O\left(\mathbf{x}_{0}\right)\right] \tag{12.11}
\end{equation*}
$$

This estimator can be further improved using the periodic boundaries in the path, i.e. we can average the estimator over all the points:

$$
\begin{equation*}
\langle O\rangle=\frac{1}{P} \sum_{i} \mathbb{E}_{\Pi}\left[O\left(\mathbf{x}_{i}\right)\right] \tag{12.12}
\end{equation*}
$$

which ideally leads to a factor $1 / \sqrt{P}$ improvement in the statistical uncertainty.

### 12.2 Continuous-Space particles

We specialize now our discussion to the case of particles in continuous space. We consider again the Hamiltonian for a system of $N$ particles, of coordinates $\vec{r}_{1}, \vec{r}_{2} \ldots \vec{r}_{N}$, and subjected to both one and two-body interactions:

$$
\begin{equation*}
\hat{H}=-\frac{\hbar^{2}}{2 m} \sum_{i}^{N} \nabla_{\vec{r}_{i}}^{2}+\sum_{i} V_{1}\left(\vec{r}_{i}\right)+\sum_{i<j} V_{2}\left(\vec{r}_{i}, \vec{r}_{j}\right) \tag{12.13}
\end{equation*}
$$

We first assume that particles, although being identical, are distinguishable. Therefore, we do not need to impose the Bose or Fermi restriction to the Hilbert space. In section 12.2.1 we will describe the treatment of identical particles obeying Bose statistics.

In this case, the path-integral probability density reads:

$$
\begin{equation*}
\Pi\left(\mathbf{x}_{0}, \mathbf{x}_{1} \ldots \mathbf{x}_{P}\right) \propto \Pi_{i=0}^{P-1} \Pi_{j=1}^{N} \exp \left[-\frac{\left(\vec{r}_{j}(i)-\vec{r}_{j}(i+1)\right)^{2}}{2 \Delta_{\tau} \hbar^{2} / m}\right] e^{-\Delta_{\tau} H_{0}\left(\mathbf{x}_{i}\right)} \tag{12.14}
\end{equation*}
$$

where we denote $\vec{r}_{j}(i)$ the position of the $j$-th particle at discrete imaginary-time $i$, i.e. $\left|\mathbf{x}_{i}\right\rangle=\left|\vec{r}_{1}(i), \vec{r}_{2}(i), \ldots \vec{r}_{N}(i)\right\rangle$ and, again, $\mathbf{x}_{P}=\mathbf{x}_{0}$.

Note that eq. (12.14) represents the Boltzmann weight of a classical system of polymers. Every polymer is a necklace of beads (particles at a given imaginary-time) interacting as if they were connected by ideal springs. This harmonic interaction is due to the kinetic density matrix. In the Trotter approximation, beads with the same imaginary time index i, i.e., belonging to the same time-slice, interact with the inter-particle potential $H_{0}\left(\mathbf{x}_{i}\right)$. With higher order approximations one generally introduces effective inter-particle interactions. This is the famous mapping of quantum to classical systems introduced by Feynman to describe the properties of superfluid helium. Each quantum particle has been substituted by a classical polymer. The size of polymers is of order $\lambda_{T}=\sqrt{2 \pi \hbar^{2} \beta / m}$, the de Broglie thermal wave-length, and represents the indetermination on the position of the corresponding quantum particle. In the section 12.2.1 we will see how the indistinguishability of identical particles modifies the "polymer" description of the quantum many body system.

### 12.2.1 Bose symmetry

The expression (12.14) for the partition function is not symmetrical under particle exchange, so it holds for distinguishable particles only. The correct expression for identical particles obeying Bose (Fermi) statistics should be symmetrical (anti-symmetrical) under particle exchange. A convenient way to symmetrize the density matrix (12.6) is to sum over all possible permutations of the particle labels in one of the two arguments:

$$
\begin{equation*}
\rho_{\text {Bose }}^{\beta}\left(\mathbf{x}_{1}, \mathbf{x}_{2}\right)=\frac{1}{N!} \sum_{\mathcal{P}} \rho^{\beta}\left(\mathbf{x}_{1}, \mathcal{P}\left(\mathbf{x}_{2}\right)\right) \tag{12.15}
\end{equation*}
$$

where $\mathcal{P}$ denotes each of the $N$ ! permutations of the particle labels; this means that $\mathcal{P}(\mathbf{x})=\left(\vec{r}_{\mathcal{P}_{1}}, \vec{r}_{\mathcal{P}_{2}}, \ldots, \vec{r}_{\mathcal{P}_{N}}\right)$, where $\mathcal{P}_{i}$, with $i=1,2, \ldots, N$, is the particle label in permutation with the $i$-th particle. If we trace the symmetrized density matrix eq. (12.15) we obtain the partition function for identical Bose particles:

$$
\begin{equation*}
Z_{\text {Bose }}(N, V, T)=\frac{1}{N!} \sum_{\mathcal{P}} \int d \mathbf{x}_{0} \ldots d \mathbf{x}_{P} \Pi\left(\mathbf{x}_{0}, \mathbf{x}_{1} \ldots \mathbf{x}_{P}\right) \delta\left(\mathbf{x}_{P}-\mathcal{P}\left(\mathbf{x}_{0}\right)\right) \tag{12.16}
\end{equation*}
$$

with the new boundary condition $\mathbf{x}_{P}=\mathcal{P}\left(\mathbf{x}_{0}\right)$. As a consequence of symmetrization the necklaces constituting the polymers are not closed on themselves. The last bead of the $i$-th polymer is connected to the first bead of the $\mathcal{P}_{i}$-th world-line (see Fig. 12.1 for an example of path configuration).

At low temperatures, where the thermal wave-length $\lambda_{T}$ is comparable to the average inter-particle distance, large permutations cycles form. These are responsible for macroscopic quantum phenomena such as superfluidity and Bose-Einstein condensation.

An exact evaluation of the $N$ ! addends summed in eq.(12.16) becomes soon unfeasible by increasing $N$. Fortunately, all terms are positive definite, then we can still arrange a Monte Carlo procedure for the evaluation of eq. (12.16). If we considered Fermi particles, an additional '+' or '-' sign would appear in front of each term, the former for even permutations, the latter for odd permutations. A Monte Carlo evaluation of the Fermi partition function would lead to an exponentially small signal to noise ratio going to small $T$ and large $N$. As a consequence of this sign problem the path-integral calculation becomes unfeasible unless one introduces some systematic approximations.
![](https://cdn.mathpix.com/cropped/2024_05_17_976c09c0be3891ca9225g-5.jpg?height=496&width=1446&top_left_y=248&top_left_x=268)

Figure 12.1: Example of path-integral configurations for a two-particle systems. In the left path, we have two separate closed polymers (rings) one for particle 1 (red beads) and one for particle 2 (blue beads). In the right configuration we are sampling instead a particle exchange between particle 1 and 2 . In this case the two polymers become a single, larger one.

### 12.3 Path-Integral Monte Carlo

In this section we describe the Monte Carlo procedure to sample path-integrals.

The Path-Integral Monte Carlo method is again based on Markov Chain sampling, and therefore is fully specified by the transition probabilities $T\left(\mathbf{x} \rightarrow \mathbf{x}^{\prime}\right)$, of going from a given path configuration $\mathbf{x}=\mathbf{x}_{0} \ldots \mathbf{x}_{P}$ to a new one $\mathbf{x}^{\prime}=\mathbf{x}_{0}^{\prime} \ldots \mathbf{x}_{P}^{\prime}$.

In general, we will need both moves that change the particle positions at given imaginary times (beads), and Monte Carlo moves that sample the permutations. Here we discuss only the essential steps to build an elementary Path-Integral algorithm. More advanced moves can be found in Refs. $[1,2,3]$.

### 12.3.1 Moving a single bead

The simplest move we can imagine starts with randomly picking a discrete imaginary time $i$, which we sample uniformly in $i \in[0, P-1)$, and a random particle index $j \in$ $[1, N]$. Then we propose to randomly move the particle (at position $\vec{r}_{j}(i)$ ), to another point $\vec{r}_{j}(i)^{\prime}$. For simplicity we pick a Gaussian transition probability $T\left(\vec{r}_{j}(i), \vec{r}_{j}(i)^{\prime}\right)$, such that the new particle position is generated according to $\vec{r}_{j}(i)^{\prime}=\vec{r}_{j}(i)+\operatorname{Normal}(\sigma)$. Here $\operatorname{Normal}(\sigma)$ denotes the sum of 3 independent normal distributions, one per spatial direction. Since in this case the transition probability is symmetric, the acceptance ratio is just given by the ratio of the two probabilities distribution : $\Pi\left(\mathrm{x}^{\prime}\right) / \Pi(\mathrm{x})$, with $\mathbf{x}^{\prime}=\mathbf{x}_{0} \ldots \mathbf{x}_{i}^{\prime} \ldots \mathbf{x}_{P-1}$, and $\mathbf{x}_{i}^{\prime}=\vec{r}_{1}(i), \ldots \vec{r}_{j}(i)^{\prime}, \ldots \vec{r}_{N}(i)$. The probability to accept the move is then:

$$
\begin{equation*}
A_{s}=\min \left[1, \frac{\exp \left[-\frac{\left(\vec{r}_{j}(i-1)-\vec{r}_{j}(i)^{\prime}\right)^{2}+\left(\vec{r}_{j}(i)^{\prime}-\vec{r}_{j}(i+1)\right)^{2}}{2 \Delta_{\tau}}\right]}{\exp \left[-\frac{\left(\vec{r}_{j}(i-1)-\vec{r}_{j}(i)\right)^{2}+\left(\vec{r}_{j}(i)-\vec{r}_{j}(i+1)\right)^{2}}{2 \Delta_{\tau}}\right]} \exp \left[-\Delta_{\tau}\left(H_{0}\left(\mathbf{x}_{j}^{\prime}\right)-H_{0}\left(\mathbf{x}_{j}\right)\right)\right]\right] \tag{12.17}
\end{equation*}
$$

![](https://cdn.mathpix.com/cropped/2024_05_17_976c09c0be3891ca9225g-6.jpg?height=672&width=1464&top_left_y=247&top_left_x=338)

Figure 12.2: Example of a single-bead move in the Path-Integral Quantum Monte Carlo. One random bead is picked (in this case bead 1) and it is displaced to a random configuration with a normal distribution.

### 12.3.2 Moving multiple beads

The previously describe 'single bead' move becomes extremely inefficient when the number of time-slices $P$ increases (critical slowing down), so one faces ergodicity problems. A better approach is to reconstruct a larger segment of the path, involving a certain number of $m$ adjacent (in time) beads. An example of such multi-bead move is depicted in Figure 12.3.

The most commonly adopted strategy to sample a piece of path is to fix the two ends (in the example, $\mathbf{x}_{0}$ and $\mathbf{x}_{4}$ ) and generate the missing beads in the middle with a probability proportional to the free propagator. In the example shown in Figure 12.3, the transition probability would then correspond to:

$$
\begin{equation*}
T_{\mathrm{mb}}\left(\mathbf{x} \rightarrow \mathbf{x}^{\prime}\right)=G_{1}^{\Delta_{\tau}}\left(\mathbf{x}_{0}, \mathbf{x}_{1}^{\prime}\right) G_{1}^{\Delta_{\tau}}\left(\mathbf{x}_{1}^{\prime}, \mathbf{x}_{2}^{\prime}\right) G_{1}^{\Delta_{\tau}}\left(\mathbf{x}_{2}^{\prime}, \mathbf{x}_{3}^{\prime}\right) G_{1}^{\Delta_{\tau}}\left(\mathbf{x}_{3}^{\prime}, \mathbf{x}_{4}\right) \tag{12.18}
\end{equation*}
$$

This process effectively corresponds to bridging the two ends with a sequence of Gaussians. Since the transition probability samples exactly the free-particle part of the path-integral weight, it is easy to see that the acceptance probability for this move depends only on the potential/interaction energy:

$$
\begin{equation*}
A_{\mathrm{mb}}=\min \left[1, \exp \left[-\Delta_{\tau}\left(\sum_{j}^{m} H_{0}\left(\mathbf{x}_{j_{0}+j}^{\prime}\right)-H_{0}\left(\mathbf{x}_{j_{0}+j}\right)\right)\right]\right] \tag{12.19}
\end{equation*}
$$

where $j_{0}$ is the initial bead for the bridge, and $m$ is the number of beads that are being changed by this move (in the example, we would have $j_{0}=0$ and $m=3$. The remaining point to be addressed is then just how to to sample points distributed according to the general transition probability:

$$
\begin{equation*}
T_{\mathrm{mb}}\left(\mathrm{x} \rightarrow \mathbf{x}^{\prime}\right)=\Pi_{j=0}^{m} G_{1}^{\Delta_{\tau}}\left(\mathbf{x}_{j_{0}+j}^{\prime}, \mathbf{x}_{j_{0}+j+1}^{\prime}\right) \tag{12.20}
\end{equation*}
$$

where we have set $\mathbf{x}_{j_{0}}^{\prime} \equiv \mathbf{x}_{j_{0}}$ and $\mathbf{x}_{j_{0}+m+1}^{\prime} \equiv \mathbf{x}_{j_{0}+m+1}$.

In order to solve this problem, let us for simplicity concentrate on the one-dimensional case, and address the issue of sampling from a single point $x^{\prime}$, from the probability $G_{1}^{\Delta_{r}^{1}}\left(x_{A}, x^{\prime}\right) G_{1}^{\Delta_{\tau}^{2}}\left(x^{\prime}, x_{B}\right)$, where we take fixed end points $x_{A}$ and $x_{B}$, bridged by a free propagator of time step $\Delta_{\tau}^{1}$ on the left and a free propagator of time step $\Delta_{\tau}^{2}$ on the right. Considering the explicit expressions for the free propagators, we have:

$$
\begin{align*}
G_{1}^{\Delta_{\tau}^{1}}\left(x_{A}, x^{\prime}\right) G_{1}^{\Delta_{\tau}^{2}}\left(x^{\prime}, x_{B}\right) & \propto \exp \left[-\frac{x_{A}^{2}-2 x^{\prime} x_{A}+x^{\prime 2}}{2 \Delta_{\tau}^{1}}-\frac{x^{\prime 2}-2 x^{\prime} x_{B}+x_{B}^{2}}{2 \Delta_{\tau}^{2}}\right] \\
& \propto \exp \left[-\frac{\left(x^{\prime}-x_{A B}\right)^{2}}{2 \sigma^{2}}\right] \tag{12.21}
\end{align*}
$$

where

$$
\begin{equation*}
\sigma^{2}=\left(1 / \Delta_{\tau}^{1}+1 / \Delta_{\tau}^{2}\right)^{-1} \tag{12.22}
\end{equation*}
$$

and

$$
\begin{equation*}
x_{A B}=\frac{\Delta_{\tau}^{2} x_{A}+\Delta_{\tau}^{1} x_{B}}{\Delta_{\tau}^{1}+\Delta_{\tau}^{2}} \tag{12.23}
\end{equation*}
$$

Equation (12.21) therefore tells us that to sample a point bridging two fixed ends $x_{A}$ and $x_{B}$, we just need to consider a modified Gaussian, whose variance is given Eq. (12.22) and whose mean value is given by Eq. (12.23). This procedure can be easily used to reconstruct the full bridge. One starts from the left end (say $x_{A} \equiv x_{j_{0}}$ and $x_{B} \equiv$ $\left.x_{j_{0}+m+1}\right)$, samples a point $x_{j_{0+1}^{\prime}}^{\prime}$ at imaginary time $j_{0}+1$ using the previously introduced modified Gaussian, with $\Delta_{\tau}^{1+1}=\Delta_{\tau}$ and $\Delta_{\tau}^{2}=m \Delta_{\tau}$. Then, one advances the left end of the bridge, fixing now $x_{A} \equiv x_{j_{0}+1}^{\prime}$ and sampling $x_{j_{0}+2}^{\prime}$, with $\Delta_{\tau}^{2}=(m-1) \Delta_{\tau}$. We end this procedure when all the points have been generated. For a complete discussion of the algorithm we suggest to read Ref. [2] (page 152).
![](https://cdn.mathpix.com/cropped/2024_05_17_976c09c0be3891ca9225g-7.jpg?height=534&width=1450&top_left_y=1829&top_left_x=264)

Figure 12.3: Example of a multi-bead move in the Path-Integral Quantum Monte Carlo. A path segment is randomly picked (in this case from bead 1 to bead 3) and it is reconstructed using a Gaussian bridge.

### 12.3.3 Displacing entire polymers

Even if we allow for the construction of large segments of paths, one can still face critical slowing down in the sampling. The reason is that if the number of beads is large, then it takes many moves to significantly displace entire polymers. Let us consider for simplicity the case in which we ignore particle exchanges. In this case, what we can do is to pick a random closed polymer $j \in[1, N]$, consider all the particles in that ring: $\vec{r}_{j}(i)$ with $i=1, \ldots P$ and displace them according to $\vec{r}_{j}^{\prime}(i)=\vec{r}_{j}(i)+\Delta R_{j}$, where $\Delta R_{j}=\operatorname{Normal}(\sigma)$ is a random variable which is identical for all the beads at different imaginary-time (i.e. we do a rigid translation of all the polymer corresponding to particle $j$ ). We immediately see that this move does not affect the kinetic part of the propagator (since it depends only on position differences), but only the part containing the potential energy. Therefore the acceptance is

$$
\begin{equation*}
A_{d}=\min \left[1, \exp \left[-\Delta_{\tau} \sum_{i}\left(H_{0}\left(\vec{r}_{j}(i)+\Delta R_{j}\right)-H_{0}\left(\vec{r}_{j}(i)\right)\right)\right]\right] \tag{12.24}
\end{equation*}
$$

### 12.3.4 Sampling permutations

Apart from the moves previously described, one has also to sample all the possible particle permutations $\mathbf{x}_{P}=\mathcal{P} \mathbf{x}_{0}$. Any path-integral Monte Carlo methods for bosons should therefore provide a move which exchanges particles. For example this can be done cutting two independent polymers, and then connecting them. Sampling permutations with ergodic moves can be rather challenging, and only relatively recently a powerful algorithm has introduced which efficiently samples permutations for thousands of particles. This method is the Worm algorithm of Reference [3]. During this Lecture we will not have the time to discuss in detail how to implement exchange moves, but the interested student can read the paper [3], where all the several steps to implement the Worm algorithm are described in detail. Notice that implementing the algorithm from scratch is a nontrivial task for a beginner in the field, and might require several weeks of coding and debugging.

### 12.3.5 Energy expectation value

In 12.1.1 we have seen how to recast thermal expectation values of diagonal observables in terms of statistical expectation values over the path distribution $\Pi\left(\mathbf{x}_{0}, \ldots \mathbf{x}_{P}\right)$. The energy per particle, $E / N$, can be found through its thermodynamic definition. In particular, $E / N$ is just the $\beta$-derivative of the partition function $Z$ :

$$
\frac{E(N, V, \beta)}{N}=-\frac{1}{N Z} \frac{\partial Z(N, V, \beta)}{\partial \beta}
$$

If we apply this derivative to the partition function defined through the path-integral representation of Eq. (13.7), we obtain the following estimator for the energy per particle (called thermodynamic estimator):

$$
\begin{equation*}
\frac{E_{\mathrm{th}}}{N}=\mathbb{E}_{\Pi}\left[\frac{d}{2 \Delta_{\tau}}-\frac{1}{2\left(\Delta_{\tau}\right)^{2} P N} \sum_{i=0}^{P-1} \sum_{j}^{N}\left(\vec{r}_{j}(i)-\vec{r}_{j}(i+1)\right)^{2}+\frac{1}{P N} \sum_{i}^{P-1} H_{0}\left(\mathbf{x}_{i}\right)\right] \tag{12.25}
\end{equation*}
$$

where $d$ is the system dimensionality. More details, and other energy estimators based on the Virial theorem can be found in Ref. [1].

