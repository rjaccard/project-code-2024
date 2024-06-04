## Electronic structure of molecules and atoms

### 6.1 Introduction

In this chapter we will discuss the arguably most important quantum many body problem - the electronic structure problem - relevant to predict almost all properties of matter at human scale. With $\mathrm{O}\left(10^{23}\right)$ atoms in a typical piece of matter, the exponential scaling of the Hilbert space dimension with the number of particles is a nightmare, and the exact diagonalization schemes discussed previously cannot be applied. In this Chapter we will set aside for a moment exact solutions, and introduce instead approximate methods that reduce the problem to a polynomial one, typically scaling like $\mathcal{O}\left(N^{4}\right)$ and even $\mathrm{O}(N)$ in modern codes that aim for a sparse matrix structure. These methods map the problem to a single-particle problem and work only as long as correlations between electrons are weak. This enormous reduction in complexity is however paid for by a crude approximation of electron correlation effects. This is acceptable for normal metals, band insulators and semi-conductors but fails in materials with strong electron correlations, such as almost all transition metal compounds. Being able to numerically implement approximate methods is however extremely important, since it is often the case that a fast, qualitatively (but not quantitatively) accurate prediction is desirable.

### 6.1.1 The electronic structure problem

For many atoms (with the notable exception of Hydrogen and Helium which are so light that quantum effects are important in daily life), the nuclei of atoms are so much heavier than the electrons that we can view them as classical particles and can consider them as stationary for the purpose of calculating the properties of the electrons. This assumption, that neglects the kinetic energy of the nuclei, is known as the Born-Oppenheimer approximation, leading to the following Hamiltonian operator for the electrons

$$
\begin{equation*}
\hat{H}=\sum_{i=1}^{N}\left(-\frac{\hbar^{2}}{2 m} \nabla_{\mathbf{r}_{i}}^{2}+V_{\mathrm{en}}\left(\mathbf{r}_{i}\right)\right)+\sum_{i<j} \frac{e^{2}}{\left|\mathbf{r}_{i}-\mathbf{r}_{j}\right|} \tag{6.1}
\end{equation*}
$$

where the potential of the $M$ atomic nuclei with charges $Z_{i} e$ at the locations $\mathbf{R}_{i}$ is given by

$$
\begin{equation*}
V_{\mathrm{en}}(\mathbf{r})=-e^{2} \sum_{i=1}^{M} \frac{Z_{i}}{\left|\mathbf{R}_{i}-\mathbf{r}\right|} \tag{6.2}
\end{equation*}
$$

In the following we will also adopt the following notation for the one-body and two-body parts entering the Hamiltonian:

$$
\begin{align*}
\hat{v}_{1}(\mathbf{r}) & =-\frac{\hbar^{2}}{2 m} \nabla_{\mathbf{r}}^{2}+V_{\mathrm{en}}(\mathbf{r})  \tag{6.3}\\
\hat{v}_{2}\left(\mathbf{r}, \mathbf{r}^{\prime}\right) & =\frac{e^{2}}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|} \tag{6.4}
\end{align*}
$$

### 6.2 Hamiltonian in second quantization

We have seen in the previous lecture that the natural space for treating identical particles (like the electrons) is the Fock space. In order to operate efficiently in this space, we need to be able to write the Hamiltonian operator (6.1) in terms of creation and annihilation operators. Using a basis set of $L$ orbital wave functions $\left\{\phi_{i}\right\}$, the matrix elements of the Hamiltonian are

$$
\begin{align*}
t_{i j} & =\int d \mathbf{r} \phi_{i}^{*}(\mathbf{r}) \hat{v}_{1}(\mathbf{r}) \phi_{j}(\mathbf{r})  \tag{6.5}\\
V_{i j k l} & =\int d \mathbf{r} \int d \mathbf{r}^{\prime} \phi_{i}^{*}(\mathbf{r}) \phi_{j}^{\star}\left(\mathbf{r}^{\prime}\right) \hat{v}_{2}\left(\mathbf{r}, \mathbf{r}^{\prime}\right) \phi_{k}(\mathbf{r}) \phi_{l}\left(\mathbf{r}^{\prime}\right) \tag{6.6}
\end{align*}
$$

In second quantized notation, the Hamiltonian then reads

$$
\begin{equation*}
\hat{H}=\sum_{i j \sigma} t_{i j} \hat{c}_{i \sigma}^{\dagger} \hat{c}_{j \sigma}+\frac{1}{2} \sum_{i j k l \sigma \sigma^{\prime}} V_{i j k l} \hat{c}_{i \sigma}^{\dagger} \hat{c}_{j \sigma^{\prime}}^{\dagger}, \hat{c}_{l \sigma^{\prime}} \hat{c}_{k \sigma} \tag{6.7}
\end{equation*}
$$

Notice that, mostly as a matter of convention (we like to write interactions with a + sign in front) the order of the indices in the interaction terms $(i, j, l, k)$ does not follow the same order of the indices of interaction matrix $(i, j, k, l)$. The explicit derivation of the form (6.5) is straightforward yet rather tedious. We have omitted here, but the interested reader can find it in full detail in any many-body theory book.

### 6.3 Basis functions

Before attempting to solve the many body problem we will discuss suitable basis sets for single particle wave functions. In realistic applications, using the naive discretization of space introduced in the first lectures will not be an efficient solution, thus we need some physical or chemical intuition to guide us in the best choice for the basis sets. This is also why the basis functions are so tightly connected to the notion of orbital in chemistry, since a correct choice of the single particle basis directly affects (at least in simple molecules) the understanding of the electronic structure.

### 6.3.1 The electron gas

For the free electron gas $\left(V_{\text {en }}=0\right)$ with Hamilton operator

$$
\begin{equation*}
\hat{H}=-\sum_{i=1}^{N} \frac{\hbar^{2}}{2 m} \nabla^{2}+\sum_{i<j} \frac{e^{2}}{\left|\mathbf{r}_{i}-\mathbf{r}_{j}\right|} \tag{6.8}
\end{equation*}
$$

one of the most commonly adopted basis functions are plane waves

$$
\begin{equation*}
\psi_{\mathbf{k}}(\mathbf{r})=\exp (-i \mathbf{k} \cdot \mathbf{r}) \tag{6.9}
\end{equation*}
$$

Such plane wave basis functions are also commonly used for band structure calculations of periodic crystals.

At low temperatures the electron gas forms a Wigner crystal. Then a better choice of basis functions are eigenfunctions of harmonic oscillators centered around the classical equilibrium positions.

### 6.3.2 Atoms and molecules

Which functions should be used as basis functions for atoms and molecules? We can let ourselves be guided by the exact solution of the Hydrogen atom and use the so-called Slater-Type-Orbitals (STO):

$$
\begin{equation*}
f_{\text {inlm }}(r, \theta, \phi) \propto r^{n-1} e^{-\zeta_{i} r} Y_{l m}(\theta, \phi) \tag{6.10}
\end{equation*}
$$

These wave functions have the correct asymptotic radial dependence and the correct angular dependence. The values $\zeta_{i}$ are optimized so that the eigenstates of isolated atoms are reproduced as accurately as possible.

The main disadvantage of the STOs becomes apparent when trying to evaluate the matrix elements in equation (6.6) for basis functions centered around two different nuclei at position $\mathbf{R}_{A}$ and $\mathbf{R}_{B}$. There we have to evaluate integrals containing terms like

$$
\begin{equation*}
\frac{1}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|} e^{-\zeta_{i}\left|\mathbf{r}-\mathbf{R}_{A}\right|} e^{-\zeta_{j}\left|\mathbf{r}-\mathbf{R}_{B}\right|} \tag{6.11}
\end{equation*}
$$

which cannot be solved in any closed form.

The Gauss-Type-Orbitals (GTO)

$$
\begin{equation*}
f_{i l m n}(\mathbf{r}) \propto x^{l} y^{m} z^{n} e^{-\zeta_{i} r^{2}} \tag{6.12}
\end{equation*}
$$

simplify the evaluation of matrix elements, as Gaussian functions can be integrated easily and the product of Gaussian functions centered at two different nuclei is again a single Gaussian function:

$$
\begin{equation*}
e^{-\zeta_{i}\left|\mathbf{r}-\mathbf{R}_{A}\right|^{2}} e^{-\zeta_{j}\left|\mathbf{r}-\mathbf{R}_{B}\right|^{2}}=K e^{-\zeta|\mathbf{r}-\mathbf{R}|^{2}} \tag{6.13}
\end{equation*}
$$

with

$$
\begin{align*}
K & =e^{-\frac{\zeta_{i} \zeta_{j}}{\zeta_{i}+\zeta_{j}}\left|\mathbf{R}_{A}-\mathbf{R}_{B}\right|^{2}}  \tag{6.14}\\
\zeta & =\zeta_{i}+\zeta_{j}  \tag{6.15}\\
\mathbf{R} & =\frac{\zeta_{i} \mathbf{R}_{A}+\zeta_{j} \mathbf{R}_{B}}{\zeta_{i}+\zeta_{j}} \tag{6.16}
\end{align*}
$$

Also the term $\frac{1}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|}$ can be rewritten as an integral over a Gaussian function

$$
\begin{equation*}
\frac{1}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|}=\frac{2}{\sqrt{\pi}} \int_{0}^{\infty} d t e^{-t^{2}\left(\mathbf{r}-\mathbf{r}^{\prime}\right)^{2}} \tag{6.17}
\end{equation*}
$$

and thus all the integrals (6.6) reduce to purely Gaussian integrals which can be performed analytically.

Independent of whether one chooses STOs or GTOs, extra care must be taken to account for the non-orthogonality of these basis functions.

### 6.3.3 Electrons in solids

Neither plane waves nor localized functions are ideal for electrons in solids. The core electrons are mostly localized and would best be described by localized basis functions as discussed in Sec. 6.3.2. The valence orbitals, on the other hand, overlap to form delocalized bands and are better described by a plane wave basis as in Sec. 6.3.1. More complicated bases sets, like linear augmented plane waves (LAPW), which smoothly cross over from localized wave function behavior near the nuclei to plane waves in the region between the atoms are used for such simulations. It is easy to imagine that a full featured electronic structure code with such basis functions gets very complicated to code.

### 6.3.3.1 Pseudo-potentials

The electrons in inner, fully occupied shells do not contribute in the chemical bindings. To simplify the calculations they can be replaced by pseudo-potentials, modeling the inner shells. Only the outer shells (including the valence shells) are then modeled using basis functions. The pseudo-potentials are chosen such that calculations for isolated atoms are as accurate as possible.

### 6.3.4 Other basis sets

There is ongoing development of new basis sets, such as finite element or wavelet based approaches. One key problem for the simulation of large molecules is that since there are $\mathcal{O}\left(L^{4}\right)$ integrals of the type (6.6), quantum chemistry calculations typically scale as $\mathcal{O}\left(N^{4}\right)$. A big goal is thus to find smart basis sets and truncation schemes to reduce the effort to an approximately $\mathcal{O}(N)$ method, since the overlap of basis functions at large distances becomes negligibly small.

### 6.4 The Hartree Fock method

### 6.4.1 The Hartree-Fock approximation

The Hartree-Fock approximation is based on the assumption of independent electrons. It starts from an ansatz for the $N$-particle wave function as a Slater determinant of $N$ single-particle wave functions:

$$
\Phi\left(\mathbf{r}_{1}, \sigma_{1} ; \ldots ; \mathbf{r}_{N}, \sigma_{N}\right)=\frac{1}{\sqrt{N}}\left|\begin{array}{ccc}
\phi_{1}\left(\mathbf{r}_{1}, \sigma_{1}\right) & \cdots & \phi_{N}\left(\mathbf{r}_{1}, \sigma_{1}\right)  \tag{6.18}\\
\vdots & & \vdots \\
\phi_{1}\left(\mathbf{r}_{N}, \sigma_{N}\right) & \cdots & \phi_{N}\left(\mathbf{r}_{N}, \sigma_{N}\right)
\end{array}\right|
$$

The orthogonal single particle wave functions $\phi_{\mu}$ are chosen so that the energy of the state is minimized.

### 6.4.2 Spinless case

To derive the Hartree-Fock equations it will be easiest to work in a second quantized notation. Also, for simplicity we will consider at first the spinless case, i.e.

$$
\Phi\left(\mathbf{r}_{1} ; \ldots ; \mathbf{r}_{N}\right)=\frac{1}{\sqrt{N}}\left|\begin{array}{ccc}
\phi_{1}\left(\mathbf{r}_{1}\right) & \cdots & \phi_{N}\left(\mathbf{r}_{1}\right)  \tag{6.19}\\
\vdots & & \vdots \\
\phi_{1}\left(\mathbf{r}_{N}\right) & \cdots & \phi_{N}\left(\mathbf{r}_{N}\right)
\end{array}\right|
$$

and then the spinful one.

### 6.4.2.1 Expectation value of the energy

The first goal is to compute the expectation value of the Hamiltonian operator over the Slater determinant (6.19):

$$
\begin{equation*}
E=\langle\Phi|\hat{H}| \Phi\rangle \tag{6.20}
\end{equation*}
$$

using the fact that the state has the simple expression

$$
\begin{equation*}
|\Phi\rangle=\hat{c}_{a_{1}}^{\dagger} \hat{c}_{a_{2}}^{\dagger} \ldots \hat{c}_{a_{N}}^{\dagger}|0\rangle \tag{6.21}
\end{equation*}
$$

where in analogy with the previous lecture, the set $a_{1}<a_{2} \cdots<a_{N}$ refer to the indexes of the occupied orbitals, i.e. such that $n_{a_{i}} \neq 0$.

The second-quantized Hamiltonian (6.7) contains the one-body term:

$$
\begin{equation*}
\hat{H}_{1}=\sum_{i j} t_{i j} \hat{c}_{i}^{\dagger} \hat{c}_{j} \tag{6.22}
\end{equation*}
$$

whose expectation value is

$$
\begin{equation*}
\left\langle\Phi\left|\hat{H}_{1}\right| \Phi\right\rangle=\sum_{i j} t_{i j}\left\langle 0\left|\hat{c}_{a_{N}} \ldots \hat{c}_{a_{1}} \hat{c}_{i}^{\dagger} \hat{c}_{j} \hat{c}_{a_{1}}^{\dagger} \ldots \hat{c}_{a_{N}}^{\dagger}\right| 0\right\rangle \tag{6.23}
\end{equation*}
$$

from which we immediately see that we must have $i=j=a_{f}$, where $a_{f}$ is one of the occupied orbitals. Therefore

$$
\begin{equation*}
\left\langle\Phi\left|\hat{H}_{1}\right| \Phi\right\rangle=\sum_{f} t_{a_{f} a_{f}} \tag{6.24}
\end{equation*}
$$

The two-body interaction term is:

$$
\begin{equation*}
\hat{H}_{2}=\frac{1}{2} \sum_{i j k l} V_{i j k l} \hat{c}_{i}^{\dagger} \hat{c}_{j}^{\dagger} \hat{c}_{l} \hat{c}_{k} \tag{6.25}
\end{equation*}
$$

and the expectation value over the Slater determinant reads :

$$
\begin{equation*}
\left\langle\Phi\left|\hat{H}_{2}\right| \Phi\right\rangle=\frac{1}{2} \sum_{i j k l} V_{i j k l}\left\langle 0\left|\hat{c}_{a_{N}} \ldots \hat{c}_{a_{1}} \hat{c}_{i}^{\dagger} \hat{c}_{j}^{\dagger} \hat{c}_{l} \hat{c}_{k} \hat{c}_{a_{1}}^{\dagger} \ldots \hat{c}_{a_{N}}^{\dagger}\right| 0\right\rangle \tag{6.26}
\end{equation*}
$$

In this expression, we see again that we must have $(l, k)=\left(a_{f}, a_{g}\right)$, where $a_{f}$ and $a_{g}$ are two occupied orbitals with $f \neq g$. There are now two possibilities:

1. $i=k=a_{f}, j=l=a_{g}$. This gives rise to the so-called direct term :

$$
\begin{align*}
& \frac{1}{2} \sum_{f g} V_{a_{f} a_{g} a_{f} a_{g}}\left\langle 0\left|\hat{c}_{a_{N}} \ldots \hat{c}_{a_{1}} \hat{c}_{a_{f}}^{\dagger} \hat{c}_{a_{g}}^{\dagger} \hat{c}_{a_{g}} \hat{c}_{a_{f}} \hat{c}_{a_{1}}^{\dagger} \ldots \hat{c}_{a_{N}}^{\dagger}\right| 0\right\rangle= \\
&=-\frac{1}{2} \sum_{f \neq g} V_{a_{f} a_{g} a_{f} a_{g}}\left\langle 0\left|\hat{c}_{a_{N}} \ldots \hat{c}_{a_{1}} \hat{c}_{a_{f}}^{\dagger} \hat{c}_{a_{g}}^{\dagger} \hat{c}_{a_{f}} \hat{c}_{a_{g}} \hat{c}_{a_{1}}^{\dagger} \ldots \hat{c}_{a_{N}}^{\dagger}\right| 0\right\rangle= \\
&=\frac{1}{2} \sum_{f \neq g} V_{a_{f} a_{g} a_{f} a_{g}} \tag{6.27}
\end{align*}
$$

2. $i=l=a_{f}$ and $j=k=a_{g}$. This gives rise to the so-called exchange term :

$$
\begin{equation*}
-\frac{1}{2} \sum_{f \neq g} V_{a_{f} a_{g} a_{g} a_{f}} \tag{6.28}
\end{equation*}
$$

where we have used the fact that $\hat{c}_{i}^{\dagger} \hat{c}_{j}^{\dagger} \hat{c}_{i} \hat{c}_{j}=-\hat{c}_{i}^{\dagger} \hat{c}_{i} \hat{c}_{j}^{\dagger} \hat{c}_{j}=-\hat{n}_{i} \hat{n}_{j}$.

The total energy therefore simply reads :

$$
\begin{equation*}
E=\sum_{f} t_{a_{f} a_{f}}+\frac{1}{2} \sum_{f g}\left(V_{a_{f} a_{g} a_{f} a_{g}}-V_{a_{f} a_{g} a_{g} a_{f}}\right) \tag{6.29}
\end{equation*}
$$

where we have also eliminated the restriction $f \neq g$, since in that case the direct and exchange terms sum to zero. Notice that the second quantization formalism has allowed us to compute in a rather straightforward way this expectation value, without the painful complications that would emerge if we had attacked the wave-function starting from the definition of the determinant.

We can also try to grasp the physical meaning of the terms entering (6.29). Apart from the trivial kinetic energy term $\sum_{f} t_{a_{f} a_{f}}$, we have that the interactions lead to the direct (Hartree) term:

$$
\begin{align*}
E_{H} & =\frac{1}{2} \sum_{f g} V_{a_{f} a_{g} a_{f} a_{g}}  \tag{6.30}\\
& =\frac{1}{2} \sum_{f g} \int d \mathbf{r} d \mathbf{r}^{\prime}\left|\phi_{a_{f}}(\mathbf{r})\right|^{2} \frac{e^{2}}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|}\left|\phi_{a_{g}}\left(\mathbf{r}^{\prime}\right)\right|^{2}  \tag{6.31}\\
& =\frac{1}{2} \int d \mathbf{r} d \mathbf{r}^{\prime} \rho(\mathbf{r}) \frac{e^{2}}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|} \rho\left(\mathbf{r}^{\prime}\right) \tag{6.32}
\end{align*}
$$

where $\rho(\mathbf{r})$ is the total electron density in a given point $\mathbf{r}$. This term is just the classical electrostatic repulsion energy for the charge distribution $\rho(\mathbf{r})$. On the other hand, the exchange term leads to a purely quantum term, which does not have a classical analogy, and it is exclusively due to the anti-symmetrization properties of the fermionic wave-function.

### 6.4.3 Spin: Restricted Hartree Fock

We now relax the assumption that we have only spinless fermions. To simplify the discussion we assume the so-called "closed-shell" conditions, where each orbital is occupied by both an electron with spin $\uparrow$ and one with spin $\downarrow$ as well as the restricted Hartree Fock form for the spin-orbitals:

$$
\phi_{k}(\mathbf{r}, \sigma)=\phi_{k}(\mathbf{r}) \times\left\{\begin{array}{l}
\alpha(\uparrow)  \tag{6.33}\\
\beta(\downarrow)
\end{array}\right.
$$

i.e. the radial part of the orbital is independent of the spin value. The closed-shell condition also implies that each radial orbital $\phi_{k}(\mathbf{r})$ is occupied exactly by one spin up and one spin down. These conditions allow to enormously simplify the expression for the energy, which becomes:

$$
E_{\mathrm{RHF}}=\sum_{f} 2 t_{a_{f} a_{f}}+\frac{1}{2} \sum_{f g}\left(2 V_{a_{f} a_{g} a_{f} a_{g}}-V_{a_{f} a_{g} a_{g} a_{f}}\right)
$$

The main difference with respect to the spinless case is that the both the kinetic term and direct term have an extra factor of 2 . This can be understood from the fact that in the expectation value of the interaction energy:

$$
\begin{align*}
& \left\langle\Phi\left|\hat{H}_{2}\right| \Phi\right\rangle= \\
& \quad \frac{1}{2} \sum_{i j k l \sigma \sigma^{\prime}} V_{i j k l}\left\langle 0\left|\hat{c}_{a_{N} \downarrow} \hat{c}_{a_{N} \uparrow} \ldots \hat{c}_{a_{1} \downarrow} \hat{c}_{a_{1} \uparrow} \hat{c}_{i \sigma}^{\dagger} \hat{c}_{j \sigma}^{\dagger} \hat{c}_{c_{\sigma^{\prime}}} \hat{c}_{k \sigma} \hat{c}_{a_{1} \uparrow}^{\dagger} \hat{\hat{c}}_{a_{1} \downarrow}^{\dagger} \ldots \hat{c}_{a_{N} \uparrow}^{\dagger} \hat{\hat{c}}_{a_{N} \downarrow}^{\dagger}\right| 0\right\rangle \tag{6.34}
\end{align*}
$$

the exchange term is obtained setting the restriction $\sigma=\sigma^{\prime}$, whereas the direct term does not have this restriction and thus pick an extra factor of 2 .

### 6.4.4 The Roothaan-Hall Equations

We have now found a general expression for the HF energy. However, in order to concretely solve this equation on a computer, we need to express the orbitals in terms of some known (and fixed) basis set. In particular we concentrate again on the Restricted Hartree Fock case with closed shells, for which the only unknowns are the spatial parts of the orbitals. We write those as linear combinations of some other basis orbitals we have chosen:

$$
\begin{equation*}
\left|\phi_{k}\right\rangle=\sum_{\beta} C_{\beta k}\left|f_{\beta}\right\rangle \tag{6.35}
\end{equation*}
$$

We can then express the total energy in terms of the given orbitals $\left|f_{\beta}\right\rangle$, for example the one-body term reads :

$$
\begin{align*}
2 \sum_{i} t_{i i} & =2 \sum_{i}\left\langle\phi_{i}\left|\hat{v}_{1}\right| \phi_{i}\right\rangle  \tag{6.36}\\
& =2 \sum_{i} \sum_{\alpha \beta} C_{\alpha i}^{\star} C_{\beta i}\left\langle f_{\alpha}\left|\hat{v}_{1}\right| f_{\beta}\right\rangle  \tag{6.37}\\
& =\sum_{\alpha \beta} P_{\alpha \beta} \bar{t}_{\alpha \beta} \tag{6.38}
\end{align*}
$$

where we have introduced the so-called "density matrix"

$$
\begin{equation*}
P_{\alpha \beta}=2 \sum_{i} C_{\alpha i}^{*} C_{\beta i} \tag{6.39}
\end{equation*}
$$

and the matrix elements of the one-body term in the chosen fixed basis $\bar{t}_{\alpha \beta}=\left\langle f_{\alpha}\left|\hat{v}_{1}\right| f_{\beta}\right\rangle$.

A similar calculation for the direct and exchange terms can be carried out (left as an Exercise) and the energy reads

$$
\begin{align*}
E_{0} & =\sum_{\alpha \beta} P_{\alpha \beta} \bar{t}_{\alpha \beta}+\frac{1}{2} \sum_{\alpha \beta \gamma \delta} P_{\alpha \beta} P_{\gamma \delta}\left(\bar{V}_{\alpha \gamma \beta \delta}-\frac{1}{2} \bar{V}_{\alpha \gamma \delta \beta}\right)  \tag{6.40}\\
& =\frac{1}{2} \sum_{\alpha \beta}\left(\bar{t}_{\alpha \beta}+F_{\alpha \beta}\right) P_{\alpha \beta} . \tag{6.41}
\end{align*}
$$

Where we have introduced the so-called Fock matrix:

$$
\begin{equation*}
F_{\alpha \beta}=\bar{t}_{\alpha \beta}+\sum_{\gamma \delta} P_{\gamma \delta}\left(\bar{V}_{\alpha \gamma \beta \delta}-\frac{1}{2} \bar{V}_{\alpha \gamma \delta \beta}\right) \tag{6.42}
\end{equation*}
$$

Since the energy is now an explicit function of the coefficients $C_{\alpha \beta}$ we can minimize it in order to find the best possible variational approximation to the ground state wave function. The only complication here is that we also need to impose that resulting orbitals are orthonormal

$$
\begin{align*}
\left\langle\phi_{k} \mid \phi_{l}\right\rangle & =\sum_{\alpha \beta} C_{\alpha k}^{\star} C_{\beta l}\left\langle f_{\alpha} \mid f_{\beta}\right\rangle  \tag{6.43}\\
& =\delta_{k l}, \tag{6.44}
\end{align*}
$$

thus the energy needs to be minimized by imposing such constraints using a Lagrange multiplier approach. By performing the minimization explicitly (a straightforward yet tedious exercise) one finds that the matrix of coefficients have to satisfy the Equation

$$
\begin{equation*}
\sum_{\beta}\left(F_{\alpha \beta}-\epsilon_{k} S_{\alpha \beta}\right) C_{\beta k}=0 \tag{6.45}
\end{equation*}
$$

first derived by Roothaan and Hall in the 1950s. In this Equation we have introduced

$$
\begin{align*}
S_{\alpha \beta} & \equiv\left\langle f_{\alpha} \mid f_{\beta}\right\rangle  \tag{6.46}\\
& =\int d \mathbf{r} f_{\alpha}^{\star}(\mathbf{r}) f_{\beta}(\mathbf{r}) \tag{6.47}
\end{align*}
$$

the positive-definite overlap (or Gramian) matrix, which for an orthogonal basis would simply be the identity, as well as the coefficients $\epsilon_{k}$, which are the Lagrange multipliers resulting from imposing the orthogonality condition. A full derivation of this Equation can be found in quantum chemistry textbooks. Here we just notice that this equation takes the form of a generalized eigenvalue problem: $\hat{A}|x\rangle=\lambda_{x} \hat{B}|x\rangle$.

Since the matrix $F_{\alpha, \beta}$ depends itself on the coefficients $C$ (the generalized eigenvectors), this equation is however intrinsically nonlinear, and cannot be solved "in one shot". The equation is instead typically solved iteratively, using the previous value of the coefficients $C$ in defining the matrix $F$, solving the generalized eigenvalue problem for new values of $C$ etc, until convergence to a fixed point is achieved.

### 6.4.5 Configuration-Interaction

The approximations used in Hartree-Fock and density functional methods are based on non-interacting electron pictures. They do not treat correlations and interactions between electrons correctly. To improve these methods, and to allow the calculation of excited states, often the "configuration-interaction" (CI) method is used.

Starting from the Hartree-Fock ground state

$$
\begin{equation*}
|\Phi\rangle=\prod_{\mu=1}^{N} \hat{c}_{\mu}^{\dagger}|0\rangle \tag{6.48}
\end{equation*}
$$

one or two of the $\hat{c}_{\mu}^{\dagger}$ are replaced by other (unoccupied) orbitals $\hat{c}_{i}^{\dagger}$ :

$$
\begin{equation*}
\left|\psi_{0}\right\rangle=\left(1+\sum_{i, \mu} \alpha_{\mu}^{i} \hat{c}_{i}^{\dagger} \hat{c}_{\mu}+\sum_{i<j, \mu<\nu} \alpha_{\mu \nu}^{i j} \hat{c}_{i}^{\dagger} \hat{c}_{j}^{\dagger} \hat{c}_{\mu} \hat{c}_{\nu}\right)|\Phi\rangle \tag{6.49}
\end{equation*}
$$

The energies are then minimized using this variational ansatz. In a problem with $N$ occupied and $M$ empty orbitals this leads to a matrix eigenvalue problem with dimension $1+N M+N^{2} M^{2}$. Using the Lanczos algorithm the low lying eigenstates can then be calculated in $\mathrm{O}\left((N+M)^{2}\right)$ steps.

Further improvements are possible by allowing more than only double-substitutions. The optimal method treats the full quantum problem of dimension $(N+M)!/ N!M!$. Quantum chemists call this method "full-CI". Physicists simplify the Hamilton operator slightly to obtain simpler models with fewer matrix elements, and call that method "exact diagonalization". This method will be discussed later in the course.

