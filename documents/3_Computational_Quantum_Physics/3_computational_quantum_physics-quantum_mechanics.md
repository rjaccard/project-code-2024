## Quantum mechanics in one hour

### 2.1 Introduction

The purpose of this chapter is to refresh your knowledge of quantum mechanics and to establish notation. Depending on your background you might not be familiar with all the material presented here. If that is the case, please ask the lecturers and we will expand the introduction. Those students who are familiar with advanced quantum mechanics are asked to glance over some omissions.

### 2.2 Basis of quantum mechanics

### 2.2.1 Wave functions and Hilbert spaces

Quantum mechanics is nothing but simple linear algebra, albeit in huge Hilbert spaces, which makes the problem hard. The foundations are pretty simple though.

A pure state of a quantum system is described by a "wave function" $|\Psi\rangle$, which is an element of a Hilbert space $\mathcal{H}$ :

$$
\begin{equation*}
|\Psi\rangle \in \mathcal{H} \tag{2.1}
\end{equation*}
$$

Usually the wave functions are normalized:

$$
\begin{equation*}
\||\Psi\rangle \|=\sqrt{\langle\Psi \mid \Psi\rangle}=1 \tag{2.2}
\end{equation*}
$$

Here the "bra-ket" notation

$$
\begin{equation*}
\langle\Phi \mid \Psi\rangle \tag{2.3}
\end{equation*}
$$

denotes the scalar product of the two wave functions $|\Phi\rangle$ and $|\Psi\rangle$.

The simplest example is the spin- $1 / 2$ system, describing e.g. the two spin states of an electron. Classically the spin $\vec{S}$ of the electron (which can be visualized as an internal angular momentum), can point in any direction. In quantum mechanics it is described by a two-dimensional complex Hilbert space $\mathcal{H}=\mathbb{C}^{2}$. A common choice of
basis vectors are the "up" and "down" spin states

$$
\begin{align*}
& |\uparrow\rangle=\binom{1}{0}  \tag{2.4}\\
& |\downarrow\rangle=\binom{0}{1} \tag{2.5}
\end{align*}
$$

This is similar to the classical Ising model, but in contrast to a classical Ising spin that can point only either up or down, the quantum spin can exist in any complex superposition

$$
\begin{equation*}
|\Psi\rangle=\alpha|\uparrow\rangle+\beta|\downarrow\rangle \tag{2.6}
\end{equation*}
$$

of the basis states, where the normalization condition (2.2) requires that $|\alpha|^{2}+|\beta|^{2}=1$.

For example, as we will see below the state

$$
\begin{equation*}
|\rightarrow\rangle=\frac{1}{\sqrt{2}}(|\uparrow\rangle+|\downarrow\rangle) \tag{2.7}
\end{equation*}
$$

is a superposition that describes the spin pointing in the positive $x$-direction.

### 2.2.2 Mixed states and density matrices

Unless specifically prepared in a pure state in an experiment, quantum systems in Nature rarely exist as pure states but instead as probabilistic superpositions. The most general state of a quantum system is then described as a density matrix $\hat{\rho}$,

$$
\begin{equation*}
\hat{\rho}=\sum_{i} P_{i}\left|\Psi_{i}\right\rangle\left\langle\Psi_{i}\right| \tag{2.8}
\end{equation*}
$$

describing a mixture of pure states $\left|\Psi_{i}\right\rangle$ each of which carrying a probability $P_{i}$. It is easy to check that the density matrix has unit trace:

$$
\begin{align*}
\operatorname{Tr} \hat{\rho} & =\sum_{x} \sum_{i} P_{i}\left\langle x \mid \Psi_{i}\right\rangle\left\langle\Psi_{i} \mid x\right\rangle  \tag{2.9}\\
& =\sum_{i} P_{i} \sum_{x}\left|\left\langle x \mid \Psi_{i}\right\rangle\right|^{2}  \tag{2.10}\\
& =\sum_{i} P_{i}  \tag{2.11}\\
& =1 \tag{2.12}
\end{align*}
$$

The density matrix of a pure state is just the projector onto that state

$$
\begin{equation*}
\hat{\rho}_{\text {pure }}=|\Psi\rangle\langle\Psi| \text {. } \tag{2.13}
\end{equation*}
$$

For example, the density matrix of a spin pointing in the positive $x$-direction is

$$
\hat{\rho}_{\rightarrow}=|\rightarrow\rangle\langle\rightarrow|=\left(\begin{array}{ll}
1 / 2 & 1 / 2  \tag{2.14}\\
1 / 2 & 1 / 2
\end{array}\right)
$$

Instead of being in a coherent superposition of up and down, the system could also be in a probabilistic mixed state, with a $50 \%$ probability of pointing up and a $50 \%$ probability of pointing down, which would be described by the density matrix

$$
\hat{\rho}_{\text {mixed }}=\left(\begin{array}{cc}
1 / 2 & 0  \tag{2.15}\\
0 & 1 / 2
\end{array}\right)
$$

### 2.2.3 Observables

Any physical observable is represented by a self-adjoint linear operator acting on the Hilbert space, which in a final dimensional Hilbert space can be represented by a Hermitian matrix. For our spin-1/2 system, using the basis introduced above, the components $\hat{S}_{x}, \hat{S}_{y}$ and $\hat{S}_{z}$ of the spin in the $x$-, $y$-, and $z$-directions are represented by the Pauli matrices

$$
\begin{align*}
& \hat{S}_{x}=\frac{\hbar}{2} \hat{\sigma}_{x}=\frac{\hbar}{2}\left(\begin{array}{ll}
0 & 1 \\
1 & 0
\end{array}\right)  \tag{2.16}\\
& \hat{S}_{y}=\frac{\hbar}{2} \hat{\sigma}_{y}=\frac{\hbar}{2}\left(\begin{array}{cc}
0 & -i \\
i & 0
\end{array}\right)  \tag{2.17}\\
& \hat{S}_{z}=\frac{\hbar}{2} \hat{\sigma}_{z}=\frac{\hbar}{2}\left(\begin{array}{cc}
1 & 0 \\
0 & -1
\end{array}\right) \tag{2.18}
\end{align*}
$$

The spin component along an arbitrary unit vector $\mathbf{e}$ is the linear superposition of the components, i.e.

$$
\mathbf{e} \cdot \hat{\mathbf{S}}=e_{x} \hat{S}_{x}+e_{y} \hat{S}_{y}+e_{z} \hat{S}_{z}=\frac{\hbar}{2}\left(\begin{array}{cc}
e_{x} & e_{x}-i e_{y}  \tag{2.19}\\
e_{x}+i e_{y} & -e_{z}
\end{array}\right)
$$

The fact that these observables do not commute but instead satisfy the non-trivial commutation relations

$$
\begin{align*}
& {\left[\hat{S}_{x}, \hat{S}_{y}\right]=\hat{S}_{x} \hat{S}_{y}-\hat{S}_{y} \hat{S}_{x}=i \hbar \hat{S}_{z}}  \tag{2.20}\\
& {\left[\hat{S}_{y}, \hat{S}_{z}\right]=i \hbar \hat{S}_{x}}  \tag{2.21}\\
& {\left[\hat{S}_{z}, \hat{S}_{x}\right]=i \hbar \hat{S}_{y}} \tag{2.22}
\end{align*}
$$

is the root of the differences between classical and quantum mechanics .

### 2.2.4 The measurement process

The outcome of a measurement in a quantum system is usually intrusive and not deterministic. After measuring an observable $A$, the new wave function of the system will be an eigenvector of the associated operator $\hat{A}$ and the outcome of the measurement the corresponding eigenvalue. The state of the system is thus changed by the measurement process!

For example, if we start with a spin pointing up with wave function

$$
\begin{equation*}
|\Psi\rangle=|\uparrow\rangle=\binom{1}{0} \tag{2.23}
\end{equation*}
$$

or alternatively density matrix

$$
\hat{\rho}_{\uparrow}=\left(\begin{array}{ll}
1 & 0  \tag{2.24}\\
0 & 0
\end{array}\right)
$$

and we measure the $x$-component of the spin $\hat{S}_{x}$, the resulting measurement will be either $+\hbar / 2$ or $-\hbar / 2$, depending on whether the spin after the measurement points in
the + or $-x$-direction, and the wave function after the measurement will be either of

$$
\begin{align*}
& |\rightarrow\rangle=\frac{1}{\sqrt{2}}(|\uparrow\rangle+|\downarrow\rangle)=\binom{1 / \sqrt{2}}{1 / \sqrt{2}}  \tag{2.25}\\
& |\leftarrow\rangle=\frac{1}{\sqrt{2}}(|\uparrow\rangle-|\downarrow\rangle)=\binom{1 / \sqrt{2}}{-1 / \sqrt{2}} \tag{2.26}
\end{align*}
$$

Either of these states will be picked with a probability given by the overlap of the initial wave function by the individual eigenstates:

$$
\begin{align*}
& p_{\rightarrow}=\|\langle\rightarrow \mid \Psi\rangle\|^{2}=1 / 2  \tag{2.27}\\
& p_{\leftarrow}=\|\langle\leftarrow \mid \Psi\rangle\|^{2}=1 / 2 \tag{2.28}
\end{align*}
$$

The final state is a probabilistic superposition of these two outcomes, described by the density matrix

$$
\hat{\rho}=p_{\rightarrow}|\rightarrow\rangle\left\langle\rightarrow\left|+p_{\leftarrow}\right| \leftarrow\right\rangle\langle\leftarrow|=\left(\begin{array}{cc}
1 / 2 & 0  \tag{2.29}\\
0 & 1 / 2
\end{array}\right) .
$$

which differs from the initial density matrix $\hat{\rho}_{\uparrow}$.

If we are not interested in the result of a particular outcome, but just in the average, the expectation value of the measurement can easily be calculated from a wave function $|\Psi\rangle$ as

$$
\begin{equation*}
\langle A\rangle=\langle\Psi|\hat{A}| \Psi\rangle \tag{2.30}
\end{equation*}
$$

or from a density matrix $\hat{\rho}$ as

$$
\begin{equation*}
\langle A\rangle=\operatorname{Tr}(\hat{\rho} \hat{A}) \tag{2.31}
\end{equation*}
$$

For pure states with density matrix $\hat{\rho}_{\Psi}=|\Psi\rangle\langle\Psi|$ the two formulations are identical:

$$
\begin{equation*}
\operatorname{Tr}\left(\hat{\rho}_{\Psi} \hat{A}\right)=\operatorname{Tr}(|\Psi\rangle\langle\Psi| \hat{A})=\langle\Psi|\hat{A}| \Psi\rangle \tag{2.32}
\end{equation*}
$$

### 2.2.5 The uncertainty relation

If two observables $A$ and $B$ do not commute $[\hat{A}, \hat{B}] \neq 0$, they cannot be measured simultaneously. If $A$ is measured first, the wave function is changed to an eigenstate of $A$, which changes the result of a subsequent measurement of $B$. As a consequence the values of $A$ and $B$ in a state $\Psi$ cannot be simultaneously known, which is quantified by the famous Heisenberg uncertainty relation which states that if two observables $A$ and $B$ do not commute but satisfy

$$
\begin{equation*}
[\hat{A}, \hat{B}]=i \hbar \tag{2.33}
\end{equation*}
$$

then the product of the root-mean-square deviations $\Delta A$ and $\Delta B$ of simultaneous measurements of $A$ and $B$ has to be larger than

$$
\begin{equation*}
\Delta A \Delta B \geq \hbar / 2 \tag{2.34}
\end{equation*}
$$

For more details about the uncertainty relation, the measurement process or the interpretation of quantum mechanics we refer interested students to an advanced quantum mechanics class or text book.

### 2.2.6 The Schrödinger equation

### 2.2.6.1 The time-dependent Schrödinger equation

After so much introduction the Schrödinger equation is very easy to present. The wave function $|\Psi\rangle$ of a quantum system evolves according to

$$
\begin{equation*}
i \hbar \frac{\partial}{\partial t}|\Psi(t)\rangle=\hat{H}|\Psi(t)\rangle \tag{2.35}
\end{equation*}
$$

where $\hat{H}$ is the Hamiltonian operator. This is just a first order linear differential equation.

### 2.2.6.2 The time-independent Schrödinger equation

The so-called time-independent Schrödinger equation is nothing but the eigenvalue problem for the Hamiltonian operator:

$$
\begin{equation*}
\hat{H}\left|\Psi_{k}\right\rangle=E_{k}\left|\Psi_{k}\right\rangle \tag{2.36}
\end{equation*}
$$

where $E_{k}$ is the energy associated with the $k$-th eigen-ket $\left|\Psi_{k}\right\rangle$. A great deal of this course will be spent solving "just" this simple eigenvalue problem!

Knowing the eigen-kets of the Hamiltonian is very useful, for example, to solve the time-dependent Schrödinger equation, since

$$
\begin{align*}
|\Psi(t)\rangle & =\exp (-i \hat{H} t / \hbar)|\Psi(0)\rangle  \tag{2.37}\\
& =\sum_{k} c_{k} \exp \left(-i E_{k} t / \hbar\right)\left|\Psi_{k}\right\rangle \tag{2.38}
\end{align*}
$$

where $c_{k}=\left\langle\Psi_{k} \mid \Psi(0)\right\rangle$ are the overlaps of the initial state with eigen-kets of the Hamiltonian.

### 2.2.6.3 The Schrödinger equation for the density matrix

The time evolution of a density matrix $\hat{\rho}(t)$ can be derived from the time evolution of pure states, and can be written as

$$
\begin{equation*}
i \hbar \frac{\partial}{\partial t} \hat{\rho}(t)=[\hat{H}, \hat{\rho}(t)] \tag{2.39}
\end{equation*}
$$

The proof is left as a simple exercise.

### 2.2.7 The thermal density matrix

Finally we want to describe a physical system not in the ground state but in thermal equilibrium at a given inverse temperature $\beta=1 / k_{B} T$. In a classical system each microstate $k$ of energy $E_{k}$ is occupied with a probability given by the Boltzmann distribution

$$
\begin{equation*}
p_{k}=\frac{1}{Z} \exp \left(-\beta E_{k}\right) \tag{2.40}
\end{equation*}
$$

where the partition function

$$
\begin{equation*}
Z=\sum_{k} \exp \left(-\beta E_{k}\right) \tag{2.41}
\end{equation*}
$$

normalizes the probabilities.

In a quantum system, if we use a basis of eigenstates $\left|\Psi_{k}\right\rangle$ with energy $E_{k}$, the density matrix can be written analogously as

$$
\begin{equation*}
\hat{\rho}_{\beta}=\frac{1}{Z} \sum_{k} \exp \left(-\beta E_{k}\right)\left|\Psi_{k}\right\rangle\left\langle\Psi_{k}\right| \tag{2.42}
\end{equation*}
$$

For a general basis, which is not necessarily an eigen-basis of the Hamiltonian $\hat{H}$, the density matrix can be obtained by diagonalizing the Hamiltonian, using the equation above, and transforming back to the original basis. The resulting density matrix is

$$
\begin{equation*}
\hat{\rho}_{\beta}=\frac{1}{Z} \exp (-\beta \hat{H}) \tag{2.43}
\end{equation*}
$$

where the partition function now is

$$
\begin{equation*}
Z=\operatorname{Tr} \exp (-\beta \hat{H}) \tag{2.44}
\end{equation*}
$$

Calculating the thermal average of an observable $A$ in a quantum system is hence formally very easy:

$$
\begin{equation*}
\langle A\rangle=\operatorname{Tr}\left(\hat{A} \hat{\rho}_{\beta}\right)=\frac{\operatorname{Tr} \hat{A} \exp (-\beta \hat{H})}{\operatorname{Tr} \exp (-\beta \hat{H})} \tag{2.45}
\end{equation*}
$$

but actually evaluating this expression is a hard problem, as we will see during this course.

### 2.3 The spin- $S$ problem

Before discussing solutions of the Schrödinger equation we will review two very simple systems: a localized particle with general spin $S$ and a free quantum particle.

In section 2.2.1 we have already seen the Hilbert space and the spin operators for the most common case of a spin- $1 / 2$ particle. The algebra of the spin operators given by the commutation relations (2.16)-(2.16) allows not only the two-dimensional representation shown there, but a series of $2 S+1$-dimensional representations in the Hilbert space $\mathbb{C}^{2 S+1}$ for all integer and half-integer values $S=0, \frac{1}{2}, 1, \frac{3}{2}, 2, \ldots$. The basis states $\{|s\rangle\}$ are usually chosen as eigenstates of the $\hat{S}_{z}$ operator

$$
\begin{equation*}
\hat{S}_{z}|s\rangle=\hbar s|s\rangle \tag{2.46}
\end{equation*}
$$

where $s$ can take any value in the range $-S,-S+1,-S+2, \ldots, S-1, S$. In this basis the $S_{z}$ operator is diagonal, and the $\hat{S}_{x}$ and $\hat{S}_{y}$ operators can be constructed from the "ladder operators"

$$
\begin{align*}
& \hat{S}_{+}|s\rangle=\sqrt{S(S+1)-s(s+1)}|s+1\rangle  \tag{2.47}\\
& \hat{S}_{-}|s\rangle=\sqrt{S(S+1)-s(s-1)}|s-1\rangle \tag{2.48}
\end{align*}
$$

which increment or decrement the $\hat{S}_{z}$ value by 1 through

$$
\begin{align*}
& \hat{S}_{x}=\frac{1}{2}\left(\hat{S}_{+}+\hat{S}_{-}\right)  \tag{2.49}\\
& \hat{S}_{y}=\frac{1}{2 i}\left(\hat{S}_{+}-\hat{S}_{-}\right) \tag{2.50}
\end{align*}
$$

The Hamiltonian of the spin coupled to a magnetic field $\vec{h}$ is

$$
\begin{equation*}
\hat{H}=-g \mu_{B} \mathbf{h} \cdot \hat{\mathbf{S}} \tag{2.51}
\end{equation*}
$$

which introduces nontrivial dynamics since the components of $\hat{\mathbf{S}}$ do not commute. As a consequence the spin precesses around the magnetic field direction.

Exercise: Derive the differential equation governing the rotation of a spin starting along the $+x$-direction rotating under a field in the $+z$-direction

### 2.4 A quantum particle in free space

Our second example is a single quantum particle in an $n$-dimensional free space. Its Hilbert space is given by all twice-continuously differentiable complex functions over the real space $\mathbb{R}^{n}$. The wave functions $|\Psi\rangle$ are complex-valued functions $\Psi(\mathbf{x})$ in $n$ dimensional space. In this representation the operator $\hat{\mathbf{x}}$, measuring the position of the particle is simple and diagonal

$$
\begin{equation*}
\hat{x}=x \tag{2.52}
\end{equation*}
$$

while the momentum operator $\hat{p}$ becomes a differential operator

$$
\begin{equation*}
\hat{p}_{\alpha}=-i \hbar \hat{\nabla}_{\alpha} \tag{2.53}
\end{equation*}
$$

These two operators do not commute but their commutator is

$$
\begin{equation*}
\left[\hat{x}_{\alpha}, \hat{p}_{\beta}\right]=i \hbar \delta_{\alpha, \beta} \tag{2.54}
\end{equation*}
$$

The Schrödinger equation of a quantum particle in an external potential $V(\mathbf{x})$ can be obtained from the classical Hamilton function by replacing the momentum and position variables by the operators above. Instead of the classical Hamilton function

$$
\begin{equation*}
H(\mathbf{x}, \mathbf{p})=\frac{|\mathbf{p}|^{2}}{2 m}+V(\mathbf{x}) \tag{2.55}
\end{equation*}
$$

we use the quantum mechanical Hamiltonian operator

$$
\begin{equation*}
\hat{H}=\frac{|\hat{\mathbf{p}}|^{2}}{2 m}+V(\hat{x})=-\frac{\hbar^{2}}{2 m} \nabla^{2}+V(\hat{x}) \tag{2.56}
\end{equation*}
$$

which gives the famous form

$$
\begin{equation*}
i \hbar \frac{\partial \psi(\mathbf{x}, t)}{\partial t}=-\frac{\hbar^{2}}{2 m} \nabla^{2} \psi(\mathbf{x}, t)+V(\mathbf{x}) \psi(\mathbf{x}, t) \tag{2.57}
\end{equation*}
$$

of the one-body Schrödinger equation.

### 2.4.1 The harmonic oscillator

As a special exactly solvable case let us consider the one-dimensional quantum harmonic oscillator with mass $m$ and potential $\frac{K}{2} x^{2}$. Defining momentum $\hat{p}$ and position operators $\hat{x}$ in units where $m=\hbar=K=1$, the time-independent Schrödinger equation is given by

$$
\begin{equation*}
\hat{H}|n\rangle=\frac{1}{2}\left(\hat{p}^{2}+\hat{x}^{2}\right)|n\rangle=E_{n}|n\rangle \tag{2.58}
\end{equation*}
$$

Inserting the definition of $\hat{p}$ we obtain an eigenvalue problem of an ordinary differential equation

$$
\begin{equation*}
-\frac{1}{2} \phi_{n}^{\prime \prime}(x)+\frac{1}{2} x^{2} \phi_{n}(x)=E_{n} \phi_{n}(x) \tag{2.59}
\end{equation*}
$$

whose eigenvalues $E_{n}=(n+1 / 2)$ and eigenfunctions

$$
\begin{equation*}
\phi_{n}(x)=\frac{1}{\sqrt{2^{n} n!\sqrt{\pi}}} \exp \left(-\frac{1}{2} x^{2}\right) H_{n}(x) \tag{2.60}
\end{equation*}
$$

are known analytically. Here the $H_{n}$ are the Hermite polynomials and $n=0,1, \ldots$.

Using these eigenstates as a basis sets we need to find the representation of $\hat{q}$ and $\hat{p}$. Performing the integrals

$$
\begin{equation*}
\langle m|\hat{x}| n\rangle \quad \text { and } \quad\langle m|\hat{p}| n\rangle \tag{2.61}
\end{equation*}
$$

it turns out that they are nonzero only for $m=n \pm 1$ and they can be written in terms of "ladder operators" $\hat{a}$ and $\hat{a}^{\dagger}$ :

$$
\begin{align*}
& \hat{x}=\frac{1}{\sqrt{2}}\left(\hat{a}^{\dagger}+\hat{a}\right)  \tag{2.62}\\
& \hat{p}=\frac{1}{i \sqrt{2}}\left(\hat{a}^{\dagger}-\hat{a}\right) \tag{2.63}
\end{align*}
$$

where the raising and lowering operators $\hat{a}^{\dagger}$ and $\hat{a}$ only have the following nonzero matrix elements:

$$
\begin{equation*}
\left\langle n+1\left|\hat{a}^{\dagger}\right| n\right\rangle=\langle n|\hat{a}| n+1\rangle=\sqrt{n+1} \tag{2.64}
\end{equation*}
$$

and commutation relations

$$
\begin{gather*}
{[\hat{a}, \hat{a}]=\left[\hat{a}^{\dagger}, \hat{a}^{\dagger}\right]=0}  \tag{2.65}\\
{\left[\hat{a}, \hat{a}^{\dagger}\right]=1} \tag{2.66}
\end{gather*}
$$

It will also be useful to introduce the number operator $\hat{n}=\hat{a}^{\dagger} \hat{a}$ which is diagonal with eigenvalue $n$ : elements

$$
\begin{equation*}
\left.\hat{n}|n\rangle=\hat{a}^{\dagger} \hat{a}|n\rangle=\sqrt{n} \hat{a}^{\dagger}|n-1\rangle=n \| n\right\rangle . \tag{2.67}
\end{equation*}
$$

To check this representation let us plug the definitions back into the Hamiltonian to obtain

$$
\begin{align*}
H & =\frac{1}{2}\left(\hat{p}^{2}+\hat{x}^{2}\right) \\
& =\frac{1}{4}\left[-\left(\hat{a}^{\dagger}-\hat{a}\right)^{2}+\left(\hat{a}^{\dagger}+\hat{a}\right)^{2}\right] \\
& =\frac{1}{2}\left(\hat{a}^{\dagger} \hat{a}+\hat{a} \hat{a}^{\dagger}\right) \\
& =\frac{1}{2}\left(2 \hat{a}^{\dagger} \hat{a}+1\right)=\hat{n}+\frac{1}{2} \tag{2.68}
\end{align*}
$$

which has the correct spectrum. In deriving the last lines we have used the commutation relation $(2.66)$.

