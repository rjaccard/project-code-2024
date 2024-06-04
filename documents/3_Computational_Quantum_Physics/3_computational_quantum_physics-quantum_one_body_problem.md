## The quantum one-body problem

### 3.1 The time-independent 1D Schrödinger equation

We start the numerical solution of quantum problems with the time-independent onedimensional Schrödinger equation for a particle with mass $m$ in a Potential $V(x)$. In one dimension the Schrödinger equation is just an ordinary differential equation

$$
\begin{equation*}
-\frac{1}{2} \frac{\partial^{2} \psi(x)}{\partial x^{2}}+V(x) \psi(x)=E \psi(x) \tag{3.1}
\end{equation*}
$$

where we have taken units in which $\hbar=m=1$.

In order to efficiently solve this problem on a computer, in the great majority of numerical approaches it is necessary to introduce some discretization of the problem. The simplest discretization we can perform consists in discretizing the space. We then consider $x \in\left[x_{0}, x_{p}\right]$ living in a finite interval, and a discretization of the space into a mesh of uniform spacing $\delta$. The points on the mesh are such that

$$
\begin{equation*}
x_{n}=n \delta+x_{0} \tag{3.2}
\end{equation*}
$$

where $x_{0}$ is the starting point of the interval and the wave function at these points is denoted by

$$
\begin{equation*}
\psi_{n}=\psi\left(x_{n}\right) \tag{3.3}
\end{equation*}
$$

In the following we will assume that the mesh contains a total of $p+1$ points, thus implying that the last point in the interval is

$$
\begin{equation*}
x_{p}=p \delta+x_{0} \tag{3.4}
\end{equation*}
$$

### 3.1.1 Discretizing the Hamiltonian

The previous discussion has introduced a simple strategy to represent the wave function as a finite-size vector of components $\psi_{n}$. In order to solve Schroedinger's equation, it is now necessary also to have finite-sized description of the Hamiltonian. This must be a matrix acting on the same vector space of the discretized state $\psi_{n}$. The potential energy
term in the hamiltonian is diagonal in the position basis and it is easily discretized into a diagonal matrix with diagonal entries $V_{n}$ :

$$
\begin{equation*}
V(x) \rightarrow V_{n} \equiv V\left(x_{n}\right) \tag{3.5}
\end{equation*}
$$

The kinetic energy term is off-diagonal in the position basis and we can also expect that its matrix representation is off diagonal. In order to find an explicit representation, we can use a finite-difference approximation of the derivative:

$$
\begin{equation*}
\frac{\partial^{2}}{\partial x^{2}} f\left(x_{n}\right) \simeq \frac{1}{\delta^{2}}\left(f\left(x_{n-1}\right)-2 f\left(x_{n}\right)+f\left(x_{n+1}\right)\right)+\mathcal{O}\left(\delta^{2}\right) \tag{3.6}
\end{equation*}
$$

Using this discretization, the action of the hamiltonian on the wave function is written as

$$
\begin{equation*}
\left\langle x_{n}|\hat{H}| \psi\right\rangle=-\frac{1}{2 \delta^{2}}\left(\psi_{n-1}-2 \psi_{n}+\psi_{n+1}\right)+V_{n} \psi_{n}+\mathcal{O}\left(\delta^{2}\right) \tag{3.7}
\end{equation*}
$$

The right-hand side of this equation contains only linear combinations of the vector $\psi_{n}$ and it is thus linear operator that corresponds to the discretization of the original Hamiltonian. It is easy to see that this linear operator is a matrix :

$$
\hat{H}_{\delta}=\left(\begin{array}{ccccc}
\cdots & -\frac{1}{2 \delta^{2}} & 0 & 0 & \cdots  \tag{3.8}\\
-\frac{1}{2 \delta^{2}} & V_{n-1}+\frac{1}{\delta^{2}} & -\frac{1}{2 \delta^{2}} & 0 & \cdots \\
0 & -\frac{1}{2 \delta^{2}} & V_{n}+\frac{1}{\delta^{2}} & -\frac{1}{2 \frac{1}{2 \delta^{2}}} & \cdots \\
0 & 0 & -\frac{1}{2 \delta^{2}} & V_{n+1}+\frac{1}{\delta^{2}} & \cdots \\
\cdots & 0 & 0 & \cdots & \cdots
\end{array}\right)
$$

Notice that we explicitly omitted, for the moment, the value of the matrix on the boundary. This is because the second-order finite difference scheme we have chosen would act also on $\psi\left(x_{0}-\delta\right) \equiv \psi_{-1}$ and on $\psi\left(x_{p}+\delta\right) \equiv \psi_{p+1}$, but these are beyond the discretized region we have chosen for the vector $\psi_{n}$.

In the following we will concentrate on the conceptually easy (and practically relevant) case in which we have a bound state, thus the wave-function goes to zero at infinity. In this case, we can always choose an interval $\left[x_{0}, x_{p}\right]$ large enough such that, to good approximation $\psi_{-1}=\psi_{p+1}=0$. In this case then the matrix above is exactly tridiagonal, since it is safe to just ignore the extra-boundary points $\psi_{-1}, \psi_{p+1}$.

For bound states then, finding solutions to the time-independent Schroedinger equation is a simple as diagonalizing the finite-dimensional matrix $\hat{H}_{\delta}$, and find the eigenvectors and eigen-energies

$$
\hat{H}_{\delta}\left|\psi_{k}\right\rangle=E_{k}\left|\psi_{k}\right\rangle
$$

An interesting property of the matrix $\hat{H}_{\delta}$ is that it is tridiagonal, and it can be very efficiently diagonalized, as you will see more in detail in the exercises.

### 3.2 The time-independent Schrödinger equation in higher dimensions

In higher dimensions, in most common cases it is possible to reduce the problem to a onedimensional problem. This happens if the problem, because of symmetries, factorizes.

### 3.2.1 Factorization along coordinate axis

A first example is a three-dimensional Schrödinger equation in a cubic box with potential $V(\vec{r})=V(x)+V(y)+V(z)$ with $\vec{r}=(x, y, z)$. Using the product ansatz

$$
\begin{equation*}
\psi(\vec{r})=\psi_{x}(x) \psi_{y}(y) \psi_{z}(z) \tag{3.9}
\end{equation*}
$$

the Schroedinger's equation factorizes into three one-dimensional equations which can be solved as above.

### 3.2.2 Potential with spherical symmetry

Another famous trick is possible for spherically symmetric potentials with $V(\vec{r})=V(|\vec{r}|)$ where an ansatz using spherical harmonics

$$
\begin{equation*}
\psi_{l, m}(\vec{r})=\psi_{l, m}(r, \theta, \phi)=\frac{u(r)}{r} Y_{l m}(\theta, \phi) \tag{3.10}
\end{equation*}
$$

can be used to reduce the three-dimensional Schrödinger equation to a one-dimensional one for the radial wave function $u(r)$ :

$$
\begin{equation*}
\left[-\frac{\hbar^{2}}{2 \mu} \frac{d^{2}}{d r^{2}}+\frac{\hbar^{2} l(l+1)}{2 \mu r^{2}}+V(r)\right] u(r)=E u(r) \tag{3.11}
\end{equation*}
$$

where we have called the particle mass $\mu$ (to avoid confusion with magnetic quantum number $m$ in the spherical harmonics). This is again a one-dimensional Schrödinger equation, with a modified effective potential

$$
\begin{equation*}
V_{l}(r)=V(r)+\frac{\hbar^{2}}{2 \mu} \frac{l(l+1)}{r^{2}} \tag{3.12}
\end{equation*}
$$

and with the radial wave-function defined in the interval $[0, \infty[$. In practice, for regular potentials we always have $u(0)=u\left(x_{i}\right)=0$ and it is always possible to find a point $x_{p} \gg 1$ such that, with good approximation, $u\left(x_{p}\right)=0$.

### 3.2.3 Finite difference methods in higher dimension

In higher dimension we can still discretize the space on a regular grid (for example, on a square grid in two dimensions). By doing so, we obtain once more a matrix representation of the kinetic energy. The Laplacian in two dimensions for example takes this form

$$
\begin{align*}
\nabla^{2} \psi\left(x_{n}, y_{n}\right)= & \frac{1}{\delta^{2}}\left[\psi\left(x_{n+1}, y_{n}\right)-2 \psi\left(x_{n}, y_{n}\right)+\psi\left(x_{n-1}, y_{n}\right)\right]+ \\
& +\frac{1}{\delta^{2}}\left[\psi\left(x_{n}, y_{n+1}\right)-2 \psi\left(x_{n}, y_{n}\right)+\psi\left(x_{n}, y_{n-1}\right)\right] \tag{3.13}
\end{align*}
$$

While the resulting discretized Hamiltonian in general will not be of tridiagonal form as in the $1 \mathrm{~d}$ case, it is essential to realize that the matrices produced by the discretization of the Schrödinger equation are still very sparse, meaning that only a small fraction of
the matrix entries are non zero. For these sparse systems of equations, optimized iterative numerical algorithms exist ${ }^{1}$ and are implemented in numerical libraries such as in the EIGEN library $(\mathrm{C}++)^{2}$ or in SciPy (Python) ${ }^{3}$. To calculate bound states, an eigenvalue problem has to be solved. For small problems, where the full matrix can be stored in memory, Mathematica or the dsyev eigensolver in the LAPACK library can be used. For bigger systems, sparse solvers such as the Lanczos algorithm (which will be discussed in detail in the following lectures) are best. Again there exist efficient implementations of iterative algorithms for sparse matrices.

### 3.3 The time-dependent Schrödinger equation

We now move to the problem of solving the time-dependent Schrödinger equation

$$
\begin{equation*}
i \frac{\partial}{\partial t} \psi(x, t)=-\frac{1}{2} \frac{\partial^{2} \psi(x, t)}{\partial x^{2}}+V(x) \psi(x, t) \tag{3.14}
\end{equation*}
$$

with given initial condition $\psi\left(x, t_{0}\right)$.

### 3.3.1 Spectral methods

By introducing a basis and solving for the complete spectrum of energy eigenstates we can directly solve the time-dependent problem in the case of a stationary (timeindependent) Hamiltonian. This is a consequence of the linearity of the Schrödinger equation.

To calculate the time evolution of a state $\left|\psi\left(t_{0}\right)\right\rangle$ from time $t_{0}$ to $t$ we first solve the stationary eigenvalue problem $\hat{H}|\phi\rangle=E|\phi\rangle$ and calculate the eigenvectors $\left|\phi_{n}\right\rangle$ and eigenvalues $\epsilon_{n}$. Next we represent the initial wave function $|\psi\rangle$ by a spectral decomposition

$$
\begin{equation*}
\left|\psi\left(t_{0}\right)\right\rangle=\sum_{n} c_{n}\left|\phi_{n}\right\rangle \tag{3.15}
\end{equation*}
$$

Since each of the $\left|\phi_{n}\right\rangle$ is an eigenvector of $\hat{H}$, the time evolution $e^{-i \hat{H}\left(t-t_{0}\right)}$ is trivial and we obtain at time $t$ :

$$
\begin{equation*}
|\psi(t)\rangle=\sum_{n} c_{n} e^{-i \epsilon_{n}\left(t-t_{0}\right)}\left|\phi_{n}\right\rangle \tag{3.16}
\end{equation*}
$$

This approach is, however, only useful for very small problems since the effort of diagonalizing the matrix is huge. A better method is direct numerical integration, discussed in the next subsections.[^0]

### 3.3.2 Direct numerical integration

If the number of basis states is too large to perform a complete diagonalization of the Hamiltonian, or if the Hamiltonian changes over time, instead of the spectral method it is more convenient to perform a direct integration of the Schrödinger equation. Like other initial value problems of partial differential equations the Schrödinger equation can be solved by the method of lines. After choosing a set of basis functions or discretizing the spatial derivatives we obtain a set of coupled ordinary differential equations which can be evolved for each point along the time line (hence the name) by standard ODE solvers.

In the remainder of this chapter we use the symbol $\hat{H}_{\delta}$ to refer the representation of the Hamiltonian in the chosen finite basis. A simple ODE integration scheme is the forward Euler scheme

$$
\begin{equation*}
\left|\psi\left(t_{n+1}\right)\right\rangle=\left|\psi\left(t_{n}\right)\right\rangle-i \delta_{t} \hat{H}_{\delta}\left|\psi\left(t_{n}\right)\right\rangle \tag{3.17}
\end{equation*}
$$

However, this method is not only numerically unstable, but it also violates the conservation of the norm of the wave function $\langle\psi(t) \mid \psi(t)\rangle=1$, since

$$
\left(1-i \delta_{t} \hat{H}_{\delta}\right)\left(1-i \delta_{t} \hat{H}_{\delta}\right)^{\dagger}=1+\delta_{t}^{2} \hat{H}^{2} \neq 1
$$

The exact quantum evolution

$$
\begin{equation*}
\left|\psi\left(t+\delta_{t}\right)\right\rangle=e^{-i \hat{H}_{\delta} \delta_{t}}|\psi(t)\rangle \tag{3.18}
\end{equation*}
$$

is however clearly unitary and thus conserves the norm, we therefore want to look for a unitary approximation as integrator. Instead of using the forward Euler method (3.17) which is just a first order Taylor expansion of the exact time evolution

$$
\begin{equation*}
e^{-i H \delta_{t}}=1-i \delta_{t} \hat{H}_{\delta}+\mathrm{O}\left(\delta_{t}^{2}\right) \tag{3.19}
\end{equation*}
$$

we reformulate the time evolution operator as

$$
\begin{equation*}
e^{-i H \delta_{t}}=\left(e^{i H \delta_{t} / 2}\right)^{-1} e^{-i H \delta_{t} / 2}=\left(1+\frac{i \delta_{t}}{2} \hat{H}_{\delta}\right)^{-1}\left(1-\frac{i \delta_{t}}{2} \hat{H}_{\delta}\right)+\mathrm{O}\left(\delta_{t}^{3}\right) \tag{3.20}
\end{equation*}
$$

therefore

$$
\begin{equation*}
\left|\psi\left(t+\delta_{t}\right)\right\rangle=\left(1+\frac{i \delta_{t}}{2} \hat{H}_{\delta}\right)^{-1}\left(1-\frac{i \delta_{t}}{2} \hat{H}_{\delta}\right)|\psi(t)\rangle \tag{3.21}
\end{equation*}
$$

It is possible to check that the propagation scheme defined above is unitary (for example, showing that the two terms appearing commute with one another), thus we have a small time-step approach that is both unitary and second-order in $\delta_{t}$. Equivalently, we can write it as

$$
\begin{equation*}
\left(1+\frac{i \delta_{t}}{2} \hat{H}_{\delta}\right)\left|\psi\left(t+\delta_{t}\right)\right\rangle=\left(1-\frac{i \delta_{t}}{2} \hat{H}_{\delta}\right)|\psi(t)\rangle \tag{3.22}
\end{equation*}
$$

which shows more explicitly that, unfortunately this is an implicit integrator, since the value of $\left|\psi\left(t+\delta_{t}\right)\right\rangle$ is not a simple linear combination of the wave-function values at the previous time-steps.

### 3.3.2.1 Practical implementations of the implicit scheme

Despite its implicit nature, this integrator can be still be used efficiently. Concentrating again on the $1 \mathrm{~d}$ case, we have seen previously that if we discretize our problem on a mesh $x_{n}=n \delta+x_{0}$, that the Hamiltonian becomes a simple tridiagonal matrix. The implicit equation 3.22 then becomes a linear system of the form $\hat{A} y=b$, where the matrix $\hat{A}=\left(1+\frac{i \delta_{t}}{2} \hat{H}_{\delta}\right)$, the right hand side is $b_{n}=\left(1-\frac{i \delta_{t}}{2}\right) \psi_{n}(t)$ and the unknown vector $y_{n}=\psi_{n}\left(t+\delta_{t}\right)$.

At each time step, one can therefore solve this linear system of equations and find explicitly $\psi_{n}\left(t+\delta_{t}\right)$. Because of the tridiagonal structure, very efficient tridiagonal solver can be used.

In higher dimensions the matrix $H$ will no longer be simply tridiagonal but still very sparse and we can use iterative algorithms, similar to the Lanczos algorithm for the eigenvalue problem. For details about these algorithms we refer to the nice summary at http://mathworld.wolfram.com/topics/Templates.html and especially the biconjugate gradient $(\mathrm{BiCG})$ algorithm. Implementations of this algorithm are available, e.g. in the EIGEN Library C++, or in SciPy, for a Python version.

### 3.4 Appendix: The split operator method

An alternative to the unitary, implicit method described in the main text exists, and we discuss it as an optional argument for the interested reader. An explicit and unitary method is possible for a quantum particle in the real space picture with the "standard" Schrödinger equation for non-relativistic particles in continuous space. Writing the Hamiltonian operator as

$$
\begin{equation*}
H=\hat{T}+\hat{V} \tag{3.23}
\end{equation*}
$$

with

$$
\begin{align*}
\hat{T} & =\frac{1}{2 m} \hat{p}^{2}  \tag{3.24}\\
\hat{V} & =V(\vec{x}) \tag{3.25}
\end{align*}
$$

it is easy to see that $\hat{V}$ is diagonal in position space while $\hat{T}$ is diagonal in momentum space.

Indeed if we consider a $d$-dimensional particle, its wave-function in momentum space is obtained through the Fourier transform:

$$
\begin{equation*}
\tilde{\psi}(\vec{k})=\left(\frac{1}{\sqrt{2 \pi}}\right)^{d} \int_{-\infty}^{\infty} \psi(\vec{x}) e^{-i \vec{k} \cdot x} d \vec{x} \tag{3.26}
\end{equation*}
$$

and the inverse Fourier transform yields

$$
\begin{equation*}
\psi(\vec{x})=\left(\frac{1}{\sqrt{2 \pi}}\right)^{d} \int_{-\infty}^{\infty} \tilde{\psi}(\vec{k}) e^{i \vec{k} \cdot x} d \vec{k} \tag{3.27}
\end{equation*}
$$

It is then easy to check that $\tilde{\psi}(\vec{k})$ is an eigenstate of the kinetic operator $T$, and that $T \tilde{\psi}(\vec{k})=\|\vec{k}\|^{2} \tilde{\psi}(\vec{k}) / 2$.

If we split the time evolution as

$$
\begin{equation*}
e^{-i \Delta_{t} H / \hbar}=e^{-i \Delta_{t} \hat{V} / 2 \hbar} e^{-i \Delta_{t} \hat{T} / \hbar} e^{-i \Delta_{t} \hat{V} / 2 \hbar}+\mathrm{O}\left(\Delta_{t}^{3}\right) \tag{3.28}
\end{equation*}
$$

we can perform the individual time evolutions $e^{-i \Delta_{t} \hat{V} / 2 \hbar}$ and $e^{-i \Delta_{t} \hat{T} / \hbar}$ exactly:

$$
\begin{align*}
{\left[e^{-i \Delta_{t} \hat{V} / 2 \hbar}|\psi\rangle\right](\vec{x}) } & =e^{-i \Delta_{t} V(\vec{x}) / 2 \hbar} \psi(\vec{x})  \tag{3.29}\\
{\left[e^{-i \Delta_{t} \hat{T} / \hbar}|\psi\rangle\right](\vec{k}) } & =e^{-i \Delta_{t} \hbar\|\vec{k}\|^{2} / 2 m} \psi(\vec{k}) \tag{3.30}
\end{align*}
$$

in real space for the first term and momentum space for the second term.

Propagating for a time $t=N \Delta_{t}$, two consecutive applications of $e^{-i \Delta_{t} \hat{V} / 2 \hbar}$ can easily be combined into a propagation by a full time step $e^{-i \Delta_{t} \hat{V} / \hbar}$, resulting in the propagation:

$$
\begin{align*}
e^{-i H t / \hbar} & =\left(e^{-i \Delta_{t} \hat{V} / 2 \hbar} e^{-i \Delta_{t} \hat{T} / \hbar} e^{-i \Delta_{t} \hat{V} / 2 \hbar}\right)^{N}+\mathrm{O}\left(\Delta_{t}^{2}\right) \\
& =e^{-i \Delta_{t} \hat{V} / 2 \hbar}\left[e^{-i \Delta_{t} \hat{T} / \hbar} e^{-i \Delta_{t} \hat{V} / \hbar}\right]^{N-1} e^{-i \Delta_{t} \hat{T} / \hbar} e^{-i \Delta_{t} \hat{V} / 2 \hbar} \tag{3.31}
\end{align*}
$$

In practice, in order to obtain efficient representations of the wave-functions both in real and momentum space we still need to discretize the real space with a suitable mesh of size $\Delta x$, for a total of $P$ points per spatial direction. As a consequence of this discretization, the continuous Fourier transform becomes a discrete Fourier transform defined on the discrete set of wave-vectors $k_{n}=\frac{2 \pi}{n} P$, for each spatial direction, with $n=0,1, \ldots P-1$. Changing from real space to momentum space then requires the application of the discrete Fourier transform and of its inverse when going back from momentum space to real space. This can be efficiently accomplished numerically thanks to the Fast Fourier Transform (FFT) algorithm, which performs the discrete Fourier transform in only $\mathcal{O}(P \log (P))$ operations.

The discretized algorithm then starts as

$$
\begin{align*}
& \psi_{1}(\vec{x})=e^{-i \Delta_{t} V(\vec{x}) / 2 \hbar} \psi_{0}(\vec{x})  \tag{3.32}\\
& \psi_{1}(\vec{k})=\mathcal{F} \psi_{1}(\vec{x}) \tag{3.33}
\end{align*}
$$

where $\mathcal{F}$ denotes the Fourier transform and $\mathcal{F}^{-1}$ will denote the inverse Fourier transform. Next we propagate in time using full time steps:

$$
\begin{align*}
\psi_{2 n}(\vec{k}) & =e^{-i \Delta_{t} t \mid \vec{k} \|^{2} / 2 m} \psi_{2 n-1}(\vec{k})  \tag{3.34}\\
\psi_{2 n}(\vec{x}) & =\mathcal{F}^{-1} \psi_{2 n}(\vec{k})  \tag{3.35}\\
\psi_{2 n+1}(\vec{x}) & =e^{-i \Delta_{t} V(\vec{x}) / \hbar} \psi_{2 n}(\vec{x})  \tag{3.36}\\
\psi_{2 n+1}(\vec{k}) & =\mathcal{F} \psi_{2 n+1}(\vec{x}) \tag{3.37}
\end{align*}
$$

except that in the last step we finish with another half time step in real space:

$$
\begin{equation*}
\psi_{2 N+1}(\vec{x})=e^{-i \Delta_{t} V(\vec{x}) / 2 \hbar} \psi_{2 N}(\vec{x}) \tag{3.38}
\end{equation*}
$$

This is a fast and unitary integrator for the Schrödinger equation in real space. It could be improved by replacing the locally third order splitting (3.28) by a fifth-order version involving five instead of three terms.


[^0]:    ${ }^{1}$ R. Barret, M. Berry, T.F. Chan, J. Demmel, J. Donato, J. Dongarra, V. Eijkhout, R. Pozo, C. Romine, and H. van der Vorst, Templates for the Solution of Linear Systems: Building Blocks for Iterative Methods (SIAM, 1993)

    ${ }^{2}$ https://eigen.tuxfamily.org/

    ${ }^{3}$ https://docs.scipy.org/, the relevant routines are contained in scipy.sparse.linalg

