## Density functional theory

In the previous lecture we have introduced the Electronic Structure problem, and discussed the Hartree-Fock approximation to solve it.

Another commonly used method, for which the Nobel prize in chemistry was awarded to Walter Kohn, is the density functional theory. In density functional theory (DFT) the many-body wave function living in $\mathbb{R}^{3 N}$ is replaced by the electron density, which lives just in $\mathbb{R}^{3}$. Density functional theory again reduces the many body problem to a one-dimensional problem. In contrast to Hartree-Fock theory it has the advantage that it could - in principle - be exact if there were not the small problem of the unknown exchange-correlation functional.

The starting point of our analysis is again the "standard Model" in Condensed Matter Physics, namely the Hamiltonian

$$
\begin{equation*}
\hat{H}=\sum_{i=1}^{N}\left(-\frac{\hbar^{2}}{2 m} \nabla_{\mathbf{r}_{i}}^{2}+V_{e n}\left(\mathbf{r}_{i}\right)\right)+\sum_{i<j} \frac{e^{2}}{\left|\mathbf{r}_{i}-\mathbf{r}_{j}\right|} \tag{7.1}
\end{equation*}
$$

where we have once more made use of the Born-Oppenheimer approximation, and considered the interaction with the nuclei as an external potential seen by the electrons, and depending parametrically on the nuclei positions,

$$
\begin{equation*}
V_{e n}(\mathbf{r})=-e^{2} \sum_{i=1}^{M} \frac{Z_{i}}{\left|\mathbf{R}_{i}-\mathbf{r}\right|} \tag{7.2}
\end{equation*}
$$

This external potential is what determines basically all the chemical and physical properties of molecules and materials, and it can be seen as a "non-universal" addition to the electron gas Hamiltonian

$$
\begin{align*}
\hat{H}_{e g} & =-\frac{\hbar^{2}}{2 m} \sum_{i=1}^{N} \nabla_{\mathbf{r}_{i}}^{2}+\sum_{i<j} \frac{e^{2}}{\left|\mathbf{r}_{i}-\mathbf{r}_{j}\right|}  \tag{7.3}\\
& =\hat{T}_{e}+\hat{W}_{e e}
\end{align*}
$$

Goal of the DFT is, in a nutshell, to use some universal features of the electron gas in order to solve the full Electronic Structure problem.

### 7.1 The electron density

DFT is heavily based on the electron density, defined as the expectation value of the density operator

$$
\hat{\rho}(\mathbf{r})=\sum_{i=1}^{N} \delta\left(\mathbf{r}-\mathbf{r}_{i}\right)
$$

over a given fermionic state $\Psi$ :

$$
\begin{aligned}
\hat{\rho}(\mathbf{r}) & =\int d \mathbf{r}_{1} d \mathbf{r}_{2} \ldots d \mathbf{r}_{N}\left|\Psi\left(\mathbf{r}_{1}, \mathbf{r}_{2}, \ldots, \mathbf{r}_{N}\right)\right|^{2} \sum_{i=1}^{N} \delta\left(\mathbf{r}-\mathbf{r}_{i}\right) \\
& =N \int d \mathbf{r}_{2} \ldots d \mathbf{r}_{N}\left|\Psi\left(\mathbf{r}, \mathbf{r}_{2}, \ldots, \mathbf{r}_{N}\right)\right|^{2}
\end{aligned}
$$

where we have used the permutation symmetry of the wave-function, and ignored the spin degrees of freedom (as for the Hartree-Fock, for simplicity we will derive all the necessary equations in the spinless case). Notice also that these expressions are in first quantization, and that the density is normalized such that $\int d \mathbf{r} \rho(\mathbf{r})=N$.

### 7.2 Variational principle for the density

The standard variational principle states that given some state $\Psi$ and a Hamiltonian $\hat{H}$,

$$
\langle\Psi|\hat{H}| \Psi\rangle \geq E_{0}
$$

where $E_{0}$ is the exact ground-state energy of $H$, and the equal sign is obtained whenever $\Psi=\Psi_{0}$, the exact ground-state wave function. We can also state then that the wavefunction satisfies the following minimization problem:

$$
E_{0}=\min _{\Psi}\langle\Psi|\hat{H}| \Psi\rangle
$$

where we search for the optimal $\Psi$ that minimizes the functional $E[\Psi]=\langle\Psi|\hat{H}| \Psi\rangle$ among the (huge) space of all possible $N$-body normalized wave-functions. Kohn first realized that the variational principle can be written in terms of an optimization procedure for the density itself, instead of the wave-function. This idea can be formulated following Levy's constrained-search approach.

We start writing

$$
\begin{aligned}
E_{0} & =\min _{\Psi}\langle\Psi|\hat{H}| \Psi\rangle \\
& =\min _{\rho} \min _{\Psi[\rho]}\left[\left\langle\Psi\left|\hat{T}_{e}+\hat{W}_{e e}+\sum_{i} V_{e n}\left(\mathbf{r}_{i}\right)\right| \Psi\right\rangle\right]
\end{aligned}
$$

where we have separated the minimization over $\Psi$ in a two-step process: first we fix the density $\rho(\mathbf{r})$, and minimize over all possible $N$-body states $\Psi[\rho]$ which have the density
$\rho$. Then, we do a further minimization over the density. It is clear that this procedure is completely equivalent to the original formulation of the optimization procedure. Then, we notice that

$$
\begin{align*}
\left\langle\Psi\left|\sum_{i} V_{e n}\left(\mathbf{r}_{i}\right)\right| \Psi\right\rangle & =\int d \mathbf{r} \rho(\mathbf{r}) V_{e n}(\mathbf{r})  \tag{7.4}\\
& \equiv \bar{V}_{e n}[\rho] \tag{7.5}
\end{align*}
$$

which follows directly from the previous definition of the density operator, and in the last line we have made explicit that the expectation value of the one-body potential is a functional of the density. This term indeed does not depend explicitly on $\Psi[\rho]$ (since all wave-functions $\Psi[\rho]$ give the same density) and we are left only with the minimization over the density. Putting the terms together we have

$$
\begin{equation*}
E_{0}=\min _{\rho}\left[F[\rho]+\bar{V}_{e n}[\rho]\right] \tag{7.6}
\end{equation*}
$$

where we have introduced the density functional

$$
F[\rho]=\min _{\Psi[\rho]}\left\langle\Psi[\rho]\left|\hat{T}_{e}+\hat{W}_{e e}\right| \Psi[\rho]\right\rangle
$$

This is the central object of DFT, and it is an universal quantity in the sense that it does not depend on the external potential $V_{e n}(\mathbf{r})$.

The formulation of the variational principle (7.6) makes our life very easy: instead of minimizing with respect to the many-body wave functions, we only have to minimize with respect to the density (a function of just 3 spatial variables) and we obtain both the ground state energy and the electron density in the ground state - and everything is exact. This is a tremendous simplification with respect to the original problem of solving for the ground-state wave-function, which lives in a much higher dimensional space.

However, the problem is that, while the functional $F$ is universal, it is also unknown! Thus for the DFT to be useful, we need to find good approximations for this universal functional.

### 7.3 The Kohn-Sham scheme

Kohn and Sham proposed to decompose the density functional as

$$
\begin{equation*}
F[\rho]=E_{k}[\rho]+E_{h}[\rho]+E_{x c}[\rho] \tag{7.7}
\end{equation*}
$$

The first term reads:

$$
E_{k}[\rho]=\min _{\Phi[\rho]}\left\langle\Phi[\rho]\left|\hat{T}_{e}\right| \Phi[\rho]\right\rangle
$$

where the minimization is done not all over possible many-body states $\Psi[\rho]$ at the given density, but instead on the smaller set of single-particle (Slater determinants)
wave-functions $\Phi[\rho]$ at given density. The Hartree-term $E_{h}[\rho]$ has an explicit expression and it is given by the Coulomb repulsion between two electrons:

$$
\begin{equation*}
E_{h}[\rho]=\frac{1}{2} \int d \mathbf{r} d \mathbf{r}^{\prime} \rho(\mathbf{r}) \frac{e^{2}}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|} \rho\left(\mathbf{r}^{\prime}\right) \tag{7.8}
\end{equation*}
$$

as we have also seen in the previous lecture. The exchange- and correlation term $E_{x c}[\rho]$ contains instead the remaining unknown contribution, and it is implicitly defined by Equation (7.7). We will discuss how to approximate it a bit later.

A consequence of this decomposition of the density functional is that we can write the variational minimization as:

$$
\begin{align*}
E_{0} & =\min _{\rho}\left[F[\rho]+\bar{V}_{e n}[\rho]\right] \\
& =\min _{\rho}\left[\min _{\Phi[\rho]}\left\langle\Phi\left|\hat{T}_{e}\right| \Phi\right\rangle+\bar{V}_{e n}[\rho]+E_{h}[\rho]+E_{x c}[\rho]\right] \\
& =\min _{\rho}\left[\min _{\Phi[\rho]}\left[\left\langle\Phi\left|\hat{T}_{e}\right| \Phi\right\rangle+\bar{V}_{e n}\left[\rho_{\Phi}\right]+E_{h}\left[\rho_{\Phi}\right]+E_{x c}\left[\rho_{\Phi}\right]\right]\right] \tag{7.9}
\end{align*}
$$

in other words the minimization is done now on all the single-particle wave-functions which have some density $\rho_{\Phi}$. Notice that here we have implicitly assumed that singleparticle wave-functions are able to represent all possible ground-state densities profiles $\rho(\mathbf{r})$ generated by the many-body wave-functions. This assumption is reasonable but hard to prove rigorously.

To calculate the ground state energy (and other properties) we have to minimize the energy functional in (7.9) with respect to the density, solving the variational problem

$$
\begin{equation*}
0=\delta E[\rho]=\int d \mathbf{r} \delta \rho(\mathbf{r})\left(V_{e n}(\mathbf{r})+e^{2} \int d \mathbf{r}^{\prime} \frac{\rho\left(\mathbf{r}^{\prime}\right)}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|}+\frac{\delta E_{k}[\rho]}{\delta \rho(\mathbf{r})}+\frac{\delta E_{x c}[\rho]}{\delta \rho(\mathbf{r})}\right) \tag{7.10}
\end{equation*}
$$

subject to the constraint that the total electron number to be conserved

$$
\begin{equation*}
\int d \mathbf{r} \delta \rho(\mathbf{r})=0 \tag{7.11}
\end{equation*}
$$

Since the minimization is carried over densities coming from single-particle Slater determinant wave-functions, this variational problem is equivalent to solving the Schroedinger equation for a non-interacting system in an external potential:

$$
\begin{equation*}
\left(-\frac{1}{2 m} \nabla^{2}+V_{\mathrm{KS}}(\mathbf{r})\right) \phi_{\mu}(\mathbf{r})=\epsilon_{\mu} \phi_{\mu}(\mathbf{r}) \tag{7.12}
\end{equation*}
$$

where the Kohn-Sham potential of the non-interacting system is

$$
\begin{equation*}
V_{\mathrm{KS}}(\mathbf{r})=V_{e n}(\mathbf{r})+e^{2} \int d \mathbf{r}^{\prime} \frac{\rho\left(\mathbf{r}^{\prime}\right)}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|}+V_{\mathrm{xc}}(\mathbf{r}) \tag{7.13}
\end{equation*}
$$

and the exchange-correlation potential is defined by

$$
\begin{equation*}
V_{\mathrm{xc}}(\mathbf{r})=\frac{\delta E_{\mathrm{xc}}[\rho]}{\delta \rho(\mathbf{r})} \tag{7.14}
\end{equation*}
$$

The Equations (7.12) are know as Kohn-Sham equations, and effectively reduce the many-body problem to the solution of a much simpler one-body problem with an effective potential $V_{\mathrm{KS}}(\mathbf{r})=V_{\mathrm{en}}(\mathbf{r})+\mathcal{J}(\mathbf{r})+V_{\mathrm{xc}}(\mathbf{r})$. This should be contrasted with the Hartree-Fock approximation, which we have seen gives rise as well to a one-body problem but with an effective potential $V_{H F}(\mathbf{r})=V_{e n}(\mathbf{r})+\mathcal{J}(\mathbf{r})-\mathcal{K}(\mathbf{r})$. Comparing the two expressions we therefore see that $V_{x c}(\mathbf{r})$ contains both the exchange part (as per the term $\mathcal{K}(\mathbf{r})$ ), but also all the other corrections due to the correlations between the electrons, which are not captured by the Hartree Fock mean-field treatment.

For some given $V_{x c}(\mathbf{r})$, the non-linear equations (7.12) are solved in the same way we solved the Hartree-Fock equations. In particular, they are solved iteratively, using some finite basis to express the unknown Kohn-Sham orbitals $\phi_{\mu}(\mathbf{r})$.

### 7.4 Local Density Approximation

The Kohn-Sham equations discussed so-far are in principle exact. However, the functional $E_{x c}[\rho]$ and thus the potential $V_{x c}(\mathbf{r})$ is not known, and it was dubbed the stupidity functional by Richard Feynman, in the sense that we are just moving our original ignorance of the many-body system to the ignorance of this functional. To proceed further we need to introduce approximations for this functional.

The simplest approximation is the "local density approximation" (LDA), which replaces $V_{x c}$ by that of a uniform electron gas with the same density. Instead of taking a functional $E[\rho](\mathbf{r})$ which could be a function of $\rho(\mathbf{r}), \nabla \rho(\mathbf{r}), \nabla \nabla \rho(\mathbf{r}), \ldots$ we ignore all the gradients and just take the local density

$$
\begin{equation*}
E_{x c}^{L D A}[\rho]=\int d \mathbf{r} \rho(\mathbf{r}) E_{x c}^{\mathrm{eg}}(\rho(\mathbf{r})) \tag{7.15}
\end{equation*}
$$

where $E_{x c}^{\mathrm{eg}}(\rho)$ is the exact exchange-correlation energy per particle of the homogeneous electron gas, (7.3). This approximation is clearly exact for the uniform electron gas (i.e. in the absence of any external potential) for which the density is constant, since the total Hamiltonian is translational invariant. In the case in which we have an external potential, this approximation is expected to work well when the electron density does not have strong spatial variations (i.e. corrections coming from the gradients of the density can be neglected).

To proceed further, we need an expression for the exchange-correlation energy $E_{x c}^{\mathrm{eg}}(\rho)$ in the uniform electron gas. Recalling the definition (7.7), we immediately see that

$$
\begin{aligned}
E^{\mathrm{eg}}[\rho] & =F^{\mathrm{eg}}[\rho] \\
& =E_{k}[\rho]+E_{h}^{\mathrm{eg}}[\rho]+E_{x c}^{\mathrm{eg}}[\rho]
\end{aligned}
$$

therefore if the exact energy of the electron gas is known, $E^{\text {eg }}(\rho), E_{x c}^{\text {eg }}(\rho)$ can be found just subtracting the (known) Hartree term and the kinetic energy of the non-interacting electrons. In practice, very accurate energies $E^{\operatorname{eg}}(\rho)$ (at various values of the density $\rho$ ) can be obtained from quantum Monte Carlo calculations, and explicit expressions for $E_{x c}^{\text {eg }}(\rho)$ are available.

The exchange correlation potential is then found doing the functional derivative of $(7.15)$

$$
\begin{aligned}
V_{x c}^{L D A}(\mathbf{r}) & =\frac{\delta E_{x c}[\rho]}{\delta \rho(\mathbf{r})} \\
& =E_{x c}^{\mathrm{eg}}(\rho(\mathbf{r}))+\rho(\mathbf{r}) \nabla_{\rho} E_{x c}^{\mathrm{eg}}(\rho(\mathbf{r}))
\end{aligned}
$$

Putting all together, one arrives at the following explicit expression for the LDA exchange and correlation potential:

$$
\begin{gather*}
r_{s}^{-1}=a_{B}\left(\frac{4 \pi}{3} \rho\right)^{1 / 3}  \tag{7.16}\\
V_{x c}^{L D A}=-\frac{e^{2}}{a_{B}}\left(\frac{3}{2 \pi}\right)^{2 / 3} \frac{1}{r_{s}}\left[1+0.0545 r_{s} \ln \left(1+11.4 / r_{s}\right)\right] \tag{7.17}
\end{gather*}
$$

where the numerical factors come from fitting the quantum Monte Carlo data for $E^{\mathrm{eg}}(\rho)$ to a semi-empirical expression based on many-body perturbation theory.

### 7.5 Improved approximations

Improvements over the LDA have been an intense field of research in quantum chemistry. I will just mention two improvements. The "local spin density approximation" (LSDA) uses separate densities for electrons with spin $\uparrow$ and $\downarrow$. The "generalized gradient approximation" (GGA) and its variants use functionals depending not only on the density, but also on its derivatives.

### 7.6 Program packages

As the model Hamiltonian and the types of basis sets are essentially the same for all quantum chemistry applications flexible program packages have been written. There is thus usually no need to write your own programs - unless you want to implement a new algorithm.

