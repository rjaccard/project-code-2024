## Indistinguishable particles: fermions and bosons

### 5.1 Introduction

We have seen at the beginning of this course that the complete quanto-mechanical description of a single particle is given by its wave function $\langle\vec{q} \mid \psi\rangle \equiv \psi(\vec{q})$, where $\vec{q}$ is a chosen coordinate (say the position or the momentum of the particle, for example). Single-particle wave functions live in the function space $L^{2}$, which, among others, ensures that wave-functions are normalizable. Without loss of generality, we can pick from this space a set of orthonormal functions $\phi_{a}(\vec{q})$, satisfying

$$
\begin{align*}
\int d \vec{q} \phi_{a}^{\star}(\vec{q}) \phi_{b}(\vec{q}) & =\delta_{a b}  \tag{5.1}\\
\sum_{a} \phi_{a}^{\star}(\vec{q}) \phi_{a}\left(\vec{q}^{\prime}\right) & =\delta\left(\vec{q}-\vec{q}^{\prime}\right) \tag{5.2}
\end{align*}
$$

and such that any $\psi(\vec{q})$ can be written as a linear combination of those basis functions.

What happens now if we want to describe a many-particle system? We have seen in the case of many-spins systems that we should start by considering the tensor product of the individual Hilbert spaces. For example, a two-particle system would live in the space $L^{2} \otimes L^{2}$, and its wave function

$$
\begin{equation*}
\psi\left(\vec{q}_{1}, \vec{q}_{2}\right) \tag{5.3}
\end{equation*}
$$

can be written as a linear combination of an (infinite) set of basis functions of the form

$$
\begin{align*}
\phi_{1}^{(2)}\left(\vec{q}_{1}, \vec{q}_{2}\right) & =\phi_{1}\left(\vec{q}_{1}\right) \phi_{1}\left(\vec{q}_{2}\right)  \tag{5.4}\\
\phi_{2}^{(2)}\left(\vec{q}_{1}, \vec{q}_{2}\right) & =\phi_{1}\left(\vec{q}_{1}\right) \phi_{2}\left(\vec{q}_{2}\right) \\
\phi_{3}^{(2)}\left(\vec{q}_{1}, \vec{q}_{2}\right) & =\phi_{2}\left(\vec{q}_{1}\right) \phi_{1}\left(\vec{q}_{2}\right) \\
\ldots & =\ldots
\end{align*}
$$

This basis set, albeit completely acceptable, is not the most practical one to describe physical systems of many-particles. The reason is that in most situations we deal with
an indistinguishable set of particles ${ }^{1}$. For example, electrons or photons are indistinguishable: there is no serial number painted on the electrons that would allow us to distinguish two electrons. As a consequence, the only physical basis states are only those that have the correct particle-exchange symmetries. If we exchange the label of two particles, the system must be the same as before.

For our two-body wave-function example, this means that

$$
\begin{equation*}
\psi\left(\vec{q}_{2}, \vec{q}_{1}\right)=e^{i \phi} \psi\left(\vec{q}_{1}, \vec{q}_{2}\right) \tag{5.5}
\end{equation*}
$$

since upon exchanging the two particles the wave function needs to be identical, up to a phase factor $e^{i \phi}$. In three dimensions the first homotopy group is trivial and after doing two exchanges we need to be back at the original wave function ${ }^{2}$

$$
\begin{equation*}
\psi\left(\vec{q}_{1}, \vec{q}_{2}\right)=e^{i \phi} \psi\left(\vec{q}_{2}, \vec{q}_{1}\right)=e^{2 i \phi} \psi\left(\vec{q}_{1}, \vec{q}_{2}\right) \tag{5.6}
\end{equation*}
$$

and hence $e^{i \phi}= \pm 1$ :

$$
\begin{equation*}
\psi\left(\vec{q}_{2}, \vec{q}_{1}\right)= \pm \psi\left(\vec{q}_{1}, \vec{q}_{2}\right) \tag{5.7}
\end{equation*}
$$

The many-body Hilbert space can thus be split into orthogonal subspaces, one in which particles pick up a - sign and are called fermions, and the other where particles pick up a + sign and are called bosons.

One of the major consequences of the exchange symmetry is that no two fermions can be in the same state as a wave function. Consider for example the state

$$
\begin{equation*}
\phi_{1}^{(2)}\left(\vec{q}_{1}, \vec{q}_{2}\right)=\phi_{1}\left(\vec{q}_{1}\right) \phi_{1}\left(\vec{q}_{2}\right) \tag{5.8}
\end{equation*}
$$

which is completely symmetric with respect to particle exchange $\vec{q}_{1} \leftrightarrow \vec{q}_{2}$, therefore any attempt to anti-symmetrize leads to a vanishing state:

$$
\begin{equation*}
\operatorname{Antisymm}\left[\phi_{1}^{(2)}\left(\vec{q}_{1}, \vec{q}_{2}\right)\right]=\phi_{1}\left(\vec{q}_{1}\right) \phi_{1}\left(\vec{q}_{2}\right)-\phi_{1}\left(\vec{q}_{2}\right) \phi_{1}\left(\vec{q}_{1}\right)=0 \tag{5.9}
\end{equation*}
$$

This is known as Pauli principle.

### 5.2 The Fock space

Generic elements in the tensor-product space spanned by the functions in (5.4) do not satisfy the physical requirements of exchange symmetry. For example, the state

$$
\begin{equation*}
\phi_{2}^{(2)}\left(\vec{q}_{1}, \vec{q}_{2}\right) \neq \pm \phi_{2}^{(2)}\left(\vec{q}_{2}, \vec{q}_{1}\right) \tag{5.10}
\end{equation*}
$$

and it is not physically allowed.[^0]

It is therefore more convenient to work in a space where symmetrization properties are taken into account from the very beginning. The Hilbert space describing a quantum many-body system with $N=0,1, \ldots, \infty$ identical particles is called the Fock space. It is the direct sum of the appropriately symmetrized $N$-particle Hilbert spaces (made up from single-particle Hilbert spaces) $\mathcal{H}$ :

$$
\begin{equation*}
\bigoplus_{N=0}^{\infty} S_{ \pm} \mathcal{H}^{\otimes N} \tag{5.11}
\end{equation*}
$$

where $S_{+}$is the symmetrization operator used for bosons and $S_{-}$is the anti-symmetrization operator used for fermions.

### 5.2.1 Fermions

For Fermions the basis wave functions have to be antisymmetric under exchange of any two particles. If we have $N$ fermions and $L$ states, a basis state for the Fock space is fully specified by the ket of occupation numbers $\left|n_{1} \ldots n_{L}\right\rangle$ of the single-particle states. Since no two fermions cannot occupy the same state the occupation numbers are restricted to $n_{i}=0$ or 1 . Moreover, since the total number of particles is conserved we must have $\sum_{i}^{L} n_{i}=N$.

The wave function of the state $\left|n_{1}, \ldots, n_{L}\right\rangle$ is given by the appropriately antisymmetrized and normalized product of the single particle wave functions.

For example, the two-particle basis state $|1,1\rangle$ has wave function

$$
\begin{equation*}
\left\langle\vec{q}_{1}, \vec{q}_{2} \mid 1,1\right\rangle=\frac{1}{\sqrt{2}}\left[\phi_{1}\left(\vec{q}_{1}\right) \phi_{2}\left(\vec{q}_{2}\right)-\phi_{1}\left(\vec{q}_{2}\right) \phi_{2}\left(\vec{q}_{1}\right)\right] \tag{5.12}
\end{equation*}
$$

In general, a Fermionic basis state in Fock space takes the form of a Slater determinant

$$
\left\langle\vec{q}_{1}, \ldots \vec{q}_{N} \mid n_{1}, \ldots n_{L}\right\rangle=\frac{1}{\sqrt{N!}}\left|\begin{array}{ccc}
\phi_{a_{1}}\left(\vec{q}_{1}\right) & \ldots & \phi_{a_{1}}\left(\vec{q}_{N}\right)  \tag{5.13}\\
\phi_{a_{2}}\left(\vec{q}_{1}\right) & \ldots & \phi_{a_{2}}\left(\vec{q}_{N}\right) \\
\vdots & \vdots \vdots & \vdots \\
\phi_{a_{N}}\left(\vec{q}_{1}\right) & \ldots & \phi_{a_{N}}\left(\vec{q}_{N}\right)
\end{array}\right|
$$

where the occupied single-particle states (also called orbitals) are $1 \leq a_{1}<a_{2}<\cdots<$ $a_{N} \leq L$, such that $n_{a_{i}} \neq 0$. The states $\left|n_{1}, \ldots n_{L}\right\rangle$ are trivially anti-symmetric under exchange of two particles, because of the property of the determinant (i.e., exchanging two columns of the matrix leads to a factor -1 ).

### 5.2.2 Spinful fermions

Fermions, such as electrons, usually have a spin- $1 / 2$ degree of freedom in addition to their orbital wave function. The full wave function as a function of a generalized coordinate $\vec{q}=(\vec{x}, \sigma)$ including both position $\vec{x}$ and $\operatorname{spin} \sigma$.

### 5.2.3 Bosons

For Bosons instead a general basis function in Fock space needs to be symmetric under permutations. If we have $N$ Bosons and $L$ states, a basis state for the Fock space is again fully specified by the ket of occupation numbers $\left|n_{1} \ldots n_{L}\right\rangle$ of the single-particle states. At variance with Fermions, however, the occupation numbers can take any arbitrary value $n_{i}=0, \ldots N$, provided that the total number of particles is conserved, i.e. $\sum_{i}^{L} n_{i}=N$.

The wave function of the state $\left|n_{1}, \ldots, n_{L}\right\rangle$ is given by the appropriately symmetrized and normalized product of the single particle wave functions.

For example, the two-particle basis state $|1,1\rangle$ has wave function

$$
\begin{equation*}
\left\langle\vec{q}_{1}, \vec{q}_{2} \mid 1,1\right\rangle=\frac{1}{\sqrt{2}}\left[\phi_{1}\left(\vec{q}_{1}\right) \phi_{2}\left(\vec{q}_{2}\right)+\phi_{1}\left(\vec{q}_{2}\right) \phi_{2}\left(\vec{q}_{1}\right)\right] . \tag{5.14}
\end{equation*}
$$

In general, a Fermionic basis state in Fock space takes the form of a matrix permanent

$$
\left\langle\vec{q}_{1}, \ldots \vec{q}_{N} \mid n_{1}, \ldots n_{L}\right\rangle=\sqrt{\frac{\prod_{j} n_{j}}{N!}} \operatorname{perm}\left(\begin{array}{ccc}
\phi_{a_{1}}\left(\vec{q}_{1}\right) & \ldots & \phi_{a_{1}}\left(\vec{q}_{N}\right)  \tag{5.15}\\
\phi_{a_{2}}\left(\vec{q}_{1}\right) & \ldots & \phi_{a_{2}}\left(\bar{q}_{N}\right) \\
\vdots & \vdots: & \vdots \\
\phi_{a_{N}}\left(\vec{q}_{1}\right) & \ldots & \phi_{a_{N}}\left(\vec{q}_{N}\right)
\end{array}\right)
$$

where the occupied single-particle states are $1 \leq a_{1} \leq a_{2} \leq \cdots \leq a_{N} \leq L$, such that $n_{a_{i}} \neq 0$ and the same state can be occupied by more than a particle.

### 5.3 Creation and annihilation operators

Since it is very cumbersome to work with appropriately symmetrized many body wave functions, we will mainly use the formalism of second quantization and work with creation and annihilation operators which directly operate in Fock space.

### 5.3.1 Fermionic operators

Let us start introducing the creation, $\hat{c}_{i}^{\dagger}$, and annihilation, $\hat{c}_{i}$, operators which add or remove, respectively, a fermion in state $i$.

The hermitian operator $\hat{c}_{i}^{\dagger} \hat{c}_{i}$ first annihilates then creates a particle in state $i$, and, analogously to the harmonic oscillator case we have already seen, it counts how many fermions occupy a given state, i.e.

$$
\begin{equation*}
\hat{c}_{i}^{\dagger} \hat{c}_{i}\left|n_{i}\right\rangle=n_{i}\left|n_{i}\right\rangle \tag{5.16}
\end{equation*}
$$

We therefore have

$$
\begin{align*}
\hat{c}_{i}^{\dagger} \hat{c}_{i}\left|n_{i}=0\right\rangle & =0  \tag{5.17}\\
\hat{c}_{i}^{\dagger} \hat{c}_{i}\left|n_{i}=1\right\rangle & =|1\rangle . \tag{5.18}
\end{align*}
$$

On the other hand, the operator $\hat{c}_{i} \hat{c}_{i}^{\dagger}$ first creates than destroys a particle in state $i$, and we have

$$
\begin{align*}
& \hat{c}_{i} \hat{c}_{i}^{\dagger}\left|n_{i}=0\right\rangle=\left|n_{i}=0\right\rangle  \tag{5.19}\\
& \hat{c}_{i} \hat{c}_{i}^{\dagger}\left|n_{i}=1\right\rangle=0 \tag{5.20}
\end{align*}
$$

where the last relation comes from the Pauli principle. Summing the two cases, we obtain

$$
\begin{equation*}
\left(\hat{c}_{i} \hat{c}_{i}^{\dagger}+\hat{c}_{i}^{\dagger} \hat{c}_{i}\right)\left|n_{i}=0,1\right\rangle=\left|n_{i}=0,1\right\rangle \tag{5.21}
\end{equation*}
$$

which leads to the identity

$$
\begin{equation*}
\left\{\hat{c}_{i}, \hat{c}_{i}^{\dagger}\right\}=1 \tag{5.22}
\end{equation*}
$$

where $\{\hat{a}, \hat{b}\} \equiv \hat{a} \hat{b}+\hat{b} \hat{a}$, denotes the anti-commutator. We have thus found that the fermionic operators anti-commute. In addition, since we cannot create nor destroy two fermions in the same state, we have

$$
\begin{align*}
\left\{\hat{c}_{i}, \hat{c}_{i}\right\} & =0  \tag{5.23}\\
\left\{\hat{c}_{i}^{\dagger}, \hat{c}_{i}^{\dagger}\right\} & =0 \tag{5.24}
\end{align*}
$$

When acting on a Fock state, say of two fermions, we have

$$
\begin{align*}
\hat{c}_{i}^{\dagger} c_{j}^{\dagger}|0\rangle & =\left|n_{i}=1, n_{j}=1\right\rangle  \tag{5.25}\\
c_{j}^{\dagger} c_{i}^{\dagger}|0\rangle & =\left|n_{j}=1, n_{i}=1\right\rangle \tag{5.26}
\end{align*}
$$

however we know that if we exchange labels to the orbitals in the Slater determinant the state picks a minus sign, therefore

$$
\begin{equation*}
\left|n_{j}=1, n_{i}=1\right\rangle=-\left|n_{i}=1, n_{j}=1\right\rangle \tag{5.27}
\end{equation*}
$$

and we can conclude that it must be

$$
\begin{equation*}
\hat{c}_{i}^{\dagger} \hat{c}_{j}^{\dagger}=-\hat{c}_{j}^{\dagger} \hat{c}_{i}^{\dagger} \tag{5.28}
\end{equation*}
$$

or equivalently

$$
\begin{equation*}
\left\{\hat{c}_{i}^{\dagger}, \hat{c}_{j}^{\dagger}\right\}=0 \tag{5.29}
\end{equation*}
$$

Moreover,

$$
\begin{align*}
\hat{c}_{i} \hat{c}_{j}^{\dagger}\left|n_{i}=1\right\rangle & =\hat{c}_{i}\left|n_{j}=1, n_{i}=1\right\rangle  \tag{5.30}\\
& =-\hat{c}_{i}\left|n_{i}=1, n_{j}=1\right\rangle  \tag{5.31}\\
& =-\left|n_{j}=1\right\rangle \tag{5.32}
\end{align*}
$$

and

$$
\begin{align*}
\hat{c}_{j}^{\dagger} \hat{c}_{i}\left|n_{i}=1\right\rangle & =\hat{c}_{j}^{\dagger}|0\rangle  \tag{5.33}\\
& =\left|n_{j}=1\right\rangle \tag{5.34}
\end{align*}
$$

which again summing up the two equations leads to

$$
\begin{equation*}
\left\{\hat{c}_{i}, \hat{c}_{j}^{\dagger}\right\}=0 \tag{5.35}
\end{equation*}
$$

All these commutation relations can be recast in the compact form

$$
\begin{align*}
\left\{\hat{c}_{i}, \hat{c}_{j}^{\dagger}\right\} & =\delta_{i, j}  \tag{5.36}\\
\left\{\hat{c}_{i}, \hat{c}_{j}\right\} & =0  \tag{5.37}\\
\left\{\hat{c}_{i}^{\dagger}, \hat{c}_{j}^{\dagger}\right\} & =0 \tag{5.38}
\end{align*}
$$

### 5.3.1.1 Normal ordering

The basis state $\left|n_{1}, \ldots, n_{L}\right\rangle$ in the occupation number basis can easily be expressed in terms of creation operators:

$$
\begin{equation*}
\left|n_{1}, \ldots, n_{L}\right\rangle=\prod_{i=1}^{L}\left(\hat{c}_{i}^{\dagger}\right)^{n_{i}}|0\rangle=\left(\hat{c}_{1}^{\dagger}\right)^{n_{1}}\left(\hat{c}_{2}^{\dagger}\right)^{n_{2}} \cdots\left(\hat{c}_{L}^{\dagger}\right)^{n_{L}}|0\rangle \tag{5.39}
\end{equation*}
$$

The order in which we apply the creation operators is extremely important, since the fermionic creation operators anti-commute and, for example, $\hat{c}_{1}^{\dagger} \hat{c}_{2}^{\dagger}|0\rangle=-{\hat{c_{2}}}^{\dagger} \hat{c}_{1}^{\dagger}|0\rangle$. We thus need to agree on a specific ordering of the creation operators to define what we mean by the state $\left|n_{1}, \ldots, n_{L}\right\rangle$. The choice of ordering does not matter but we have to stay consistent and use e.g. the convention in equation (5.39).

Once the normal ordering is defined, we can derive the expressions for the matrix elements of the creation and annihilation operators in that basis. Using above normal ordering the matrix elements are

$$
\begin{align*}
\hat{c}_{i}\left|n_{1}, \ldots, n_{i}, \ldots, n_{L}\right\rangle & =\delta_{n_{i}, 1}(-1)^{\sum_{j=1}^{i-1} n_{j}}\left|n_{1}, \ldots, n_{i}-1, \ldots, n_{L}\right\rangle  \tag{5.40}\\
\hat{c}_{i}^{\dagger}\left|n_{1}, \ldots, n_{i}, \ldots, n_{L}\right\rangle & =\delta_{n_{i}, 0}(-1)^{\sum_{j=1}^{i-1} n_{j}}\left|n_{1}, \ldots, n_{i}+1, \ldots, n_{L}\right\rangle \tag{5.41}
\end{align*}
$$

where the minus signs come from commuting the annihilation and creation operator to the correct position in the normal ordered product.

### 5.3.2 Bosonic operators

The same procedure can be carried on for Bosons, introducing creation $\hat{b}_{i}^{\dagger}$ and annihilation operators $\hat{b}_{i}$. The most notable difference is that in this case the Pauli principle does not hold, and different commutation relations are found. In particular, one can show that

$$
\begin{align*}
& {\left[\hat{b}_{i}, \hat{b}_{j}^{\dagger}\right]=\delta_{i j}}  \tag{5.42}\\
& {\left[\hat{b}_{i}, \hat{b}_{j}\right]=0}  \tag{5.43}\\
& {\left[\hat{b}_{i}^{\dagger}, \hat{b}_{j}^{\dagger}\right]=0} \tag{5.44}
\end{align*}
$$

and that the bosonic operators act on Fock states as

$$
\begin{align*}
\hat{b_{i}}\left|n_{1}, \ldots n_{i}, \ldots n_{L}\right\rangle & =\sqrt{n_{i}}\left|n_{1}, \ldots n_{i}-1, \ldots n_{L}\right\rangle  \tag{5.45}\\
\hat{b}_{i}^{\dagger}\left|n_{1}, \ldots n_{i}, \ldots n_{L}\right\rangle & =\sqrt{n_{i}+1}\left|n_{1}, \ldots n_{i}+1, \ldots n_{L}\right\rangle . \tag{5.46}
\end{align*}
$$

Notice that at variance with fermions in the previous expression we have extra factors to take into account, to guarantee the normalization of the Fock states.

A generic Fock state can be then written as

$$
\begin{equation*}
\left|n_{1}, \ldots, n_{L}\right\rangle=\prod_{i=1}^{L} \frac{\left(\hat{b}_{i}^{\dagger}\right)^{n_{i}}}{\sqrt{n_{i}!}}|0\rangle=\frac{\left(\hat{b}_{1}^{\dagger}\right)^{n_{1}}}{\sqrt{n_{1}!}} \frac{\left(\hat{b}_{2}^{\dagger}\right)^{n_{2}}}{\sqrt{n_{2}!}} \cdots \frac{\left(\hat{b}_{L}^{\dagger}\right)^{n_{L}}}{\sqrt{n_{L}!}}|0\rangle \tag{5.47}
\end{equation*}
$$

and since creation operators on different states commute, in this case we do not need to stick to any specific normal ordering.

### 5.4 Exact diagonalization

Exact diagonalization for identical particles is very similar to what we have already done for spins. In the following we will see specific examples for fermions, which however already contains all the necessary ingredients.

### 5.4.1 Bosons

Bosons are conceptually identical to spins, in the sense that in practical applications we can think of truncating the local Hilbert space and set up a maximum occupation number, $d$ such that $0 \leq n_{i}<d$. Then, in this representation the bosonic operators have a very simple explicit form, for example:

$$
\begin{equation*}
\hat{b}_{i}=\underbrace{\hat{I}(d) \otimes \ldots \hat{I}(d)}_{i-1 \text { terms }} \otimes \hat{b} \otimes \underbrace{\hat{I}(d) \otimes \ldots \hat{I}(d)}_{L-i \text { terms }} \tag{5.48}
\end{equation*}
$$

with, for example, the destruction operator a $d \times d$ matrix:

$$
\hat{b}=\left(\begin{array}{ccccc}
0 & \sqrt{1} & 0 & \cdots & 0  \tag{5.49}\\
0 & 0 & \sqrt{2} & \cdots & 0 \\
0 & 0 & 0 & \ddots & 0 \\
\vdots & \vdots & \vdots & \ddots & \sqrt{d} \\
0 & 0 & 0 & 0 & 0
\end{array}\right)
$$

and $\hat{b}_{i}^{\dagger}$ is instead just the transpose of $\hat{b}_{i}$.

With this explicit writing of bosonic operators in terms of Kronecker products, we can then write any bosonic Hamiltonian using the same strategy adopted for spins in the previous Chapter.

### 5.4.2 Fermions

For Fermions, the situation is slightly more complicated, because we have to take into account the normal ordering of the operators, as discussed previously. However, Jordan and Wigner realized that fermionic operators can be mapped onto spin operators, with a relatively simple trick. The main idea of these mappings is to identify the local occupation numbers $n_{i}=(0,1)$ with the local spin numbers $s_{i}=(1,-1)$ in such a way that the number operator maps onto the $\hat{\sigma}^{z}$ operator:

$$
\begin{equation*}
\hat{n}_{i}\left|n_{1}, \ldots, n_{i}, \ldots, n_{L}\right\rangle \rightarrow \frac{\left(\hat{I}-\hat{\sigma}_{i}^{z}\right)}{2}\left|s_{1}, \ldots, s_{i}, \ldots, s_{L}\right\rangle \tag{5.50}
\end{equation*}
$$

then we have that

$$
\begin{align*}
& \hat{c}_{i}\left|n_{1}, \ldots, n_{i}, \ldots, n_{L}\right\rangle=\delta_{n_{i}, 1}(-1)^{n_{1}} \ldots(-1)^{n_{i-1}}\left|n_{1}, \ldots, n_{i}-1, \ldots, n_{L}\right\rangle  \tag{5.51}\\
& \rightarrow \underbrace{\hat{\sigma}^{z} \otimes \ldots \hat{\sigma}^{z}}_{i-1 \text { terms }} \otimes \hat{\sigma}^{+} \otimes \underbrace{\hat{I} \otimes \cdots \otimes \hat{I}}_{L-i \text { terms }}\left|s_{1}, \ldots, s_{i}, \ldots, s_{L}\right\rangle \tag{5.52}
\end{align*}
$$

where we have introduced the usual raising and lowering spin operators:

$$
\begin{equation*}
\hat{\sigma}^{ \pm}=\frac{\hat{\sigma}^{x} \pm i \hat{\sigma}^{y}}{2} \tag{5.53}
\end{equation*}
$$

With the prescription

$$
\begin{equation*}
\hat{c}_{i}=\underbrace{\hat{\sigma}^{z} \otimes \hat{\sigma}^{z} \cdots \hat{\sigma}^{z}}_{i-1 \text { terms }} \otimes \hat{\sigma}^{+} \otimes \underbrace{\hat{I} \otimes \hat{I} \cdots \otimes \hat{I}}_{L-i \text { terms }} \tag{5.54}
\end{equation*}
$$

and analogously for its conjugate operator $\hat{c}_{i}^{\dagger}$, we can therefore write an arbitrary fermionic Hamiltonian just using Kronecker products of spin operators, and again we can use all the techniques for sparse matrices described in the previous Chapter.

The mapping derived above is for spinless fermions, however we can also readily generalize the discussion to the case when spin degrees of freedom are present, most notably for operators obeying the commutation relations

$$
\begin{equation*}
\left\{\hat{c}_{i, \sigma}^{\dagger}, \hat{c}_{j, \sigma^{\prime}}\right\}=\delta_{i, j} \delta_{\sigma, \sigma^{\prime}} \tag{5.55}
\end{equation*}
$$

We can readily use the Kronecker product expressions found for the spinless case just increasing the total number of local states:

$$
\begin{equation*}
n_{i, \sigma} \rightarrow n_{k}^{\prime}, \tag{5.56}
\end{equation*}
$$

with $k \in[1, L \times d]$, with the $d$ the dimension of the local spin space. For example in the case of spin $1 / 2$ fermions we have $\sigma=\uparrow, \downarrow, d=2$ and we can work with the following occupation numbers as a basis:

$$
\begin{equation*}
\left|n_{1 \uparrow}, n_{1 \downarrow} \ldots, n_{L, \uparrow}, n_{L, \downarrow}\right\rangle \rightarrow\left|n_{1}^{\prime}, n_{2}^{\prime} \ldots, n_{2 L-1}^{\prime}, n_{2 L}^{\prime}\right\rangle \tag{5.57}
\end{equation*}
$$

and

$$
\begin{align*}
& \hat{c}_{i, \uparrow} \rightarrow \hat{c}_{2 i}^{\prime}  \tag{5.58}\\
& \hat{c}_{i, \downarrow} \rightarrow \hat{c}_{2 i+1}^{\prime} \tag{5.59}
\end{align*}
$$

### 5.4.3 Fixing the number of particles

In most cases of interest the Hamiltonians we work with commute with the total particle number operator,

$$
\begin{equation*}
\hat{N}=\sum_{i} \hat{n}_{i} \tag{5.60}
\end{equation*}
$$

this means that $\hat{H}$ is block-diagonal in the sectors with fixed number of particles. We can for example exploit this symmetry of the problem to reduce the dimensionality of the Hilbert space and diagonalize a smaller matrix. We will not describe in detail strategies to do that in this course. A simple strategy to diagonalize the Hamiltonian in a fixed symmetry sector consists instead in wisely choosing the initial states for our iterative diagonalization approaches. For example, in the power method we can choose
an initial state $\left|u_{0}\right\rangle$ such that it is an eigenket of $\hat{N}$ with the desired number of particles. For example, we could take any simple product state:

$$
\begin{equation*}
\left|u_{0}\right\rangle=\left|n_{1}\right\rangle \otimes\left|n_{2}\right\rangle \otimes \ldots\left|n_{L}\right\rangle, \tag{5.61}
\end{equation*}
$$

with random $n_{i}$ and such that $\sum_{i} n_{i}=N$. Then, the power method will yield the lowest eigenstate of $\hat{H}$ non-orthogonal to $\left|u_{0}\right\rangle$ (remember that we asked the condition $\left.\left|\left\langle E_{0} \mid u_{0}\right\rangle\right| \neq 0\right)$. Since $\left|u_{0}\right\rangle$ however is orthogonal to all eigenstates of the Hamiltonian that have number of particles different from $N$, it follows that we will converge to the ground state with the given fixed number of particles.

### 5.5 Example Fermionic models

Here we give a few examples of model fermionic Hamiltonian. The simplest case is certainly the "tight binding" model for spinless fermions

$$
\begin{equation*}
\hat{H}=\sum_{i, j} t_{i j} \hat{c}_{i}^{\dagger} \hat{c}_{j} \tag{5.62}
\end{equation*}
$$

where $\hat{c_{i}}$ obey Fermi statistics and $t_{i j}$ are some arbitrary coefficients describing transitions between state $i$ and state $j$. Notice that for the Hamiltonian to be hermitian, we must have $t_{i j}=t_{j i}^{\star}$, which in particular implies that the diagonal term $t_{i i}$ is real. This model is easily solvable by Fourier transforming it, as there are no interactions.

### 5.5.1 The Hubbard model

To include effects of electron correlations, the Hubbard model includes only the often dominant on-site repulsion:

$$
\begin{equation*}
H=\sum_{\langle i, j\rangle, \sigma}\left(t_{i j} \hat{c}_{i, \sigma}^{\dagger} \hat{c}_{j, \sigma}+\text { H.c. }\right)+\sum_{i} U_{i} \hat{n}_{i, \uparrow} \hat{n}_{i, \downarrow} \tag{5.63}
\end{equation*}
$$

The Hubbard model is a long-studied, but except for the 1D case still not completely understood model for correlated electron systems.

In contrast to band insulators, which are insulators because all bands are either completely filled or empty, the Hubbard model at large $U$ is insulating at half filling, when there is one electron per orbital. The reason is the strong Coulomb repulsion $U$ between the electrons, which prohibit any electron movement in the half filled case at low temperatures.

### 5.5.2 The $t-J$ model

The $t-J$ model is the effective model for large $U$ at low temperatures away from halffilling. Its Hamiltonian is

$$
\begin{equation*}
H=\sum_{\langle i, j\rangle, \sigma}\left[\left(1-\hat{n}_{i,-\sigma}\right) t_{i j} \hat{c}_{i, \sigma}^{\dagger} \hat{c}_{j, \sigma}\left(1-\hat{n}_{j,-\sigma}\right)+\text { H.c. }\right]+\sum_{\langle i, j\rangle} J_{i j}\left(\vec{S}_{i} \vec{S}_{j}-\hat{n}_{i} \hat{n}_{j} / 4\right) \tag{5.64}
\end{equation*}
$$

As double-occupancy is prohibited in the $t-J$ model there are only three instead of four states per orbital, greatly reducing the Hilbert space size.


[^0]:    ${ }^{1}$ There are fundamental reasons why classical and quantum particles are taken to be indistinguishable. One of the most striking arguments comes from the Gibbs paradox in thermodynamics: the entropy of an ideal gas would not be extensive if particles were distinguishable.

    ${ }^{2}$ As a side remark we want to mention that in two dimensions the first homotopy group is $\mathbb{Z}$ and nontrivial: it matters whether we move the particles clock-wise or anti-clock wise when exchanging them, and two clock-wise exchanges are not the identity anymore. Then more general, anyonic, statistics are possible.

