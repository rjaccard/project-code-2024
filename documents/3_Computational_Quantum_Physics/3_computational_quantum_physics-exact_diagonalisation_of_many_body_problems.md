## Exact diagonalization of many-body problems

### 4.1 Quantum spin models

After learning how to solve the 1-body Schrödinger equation, let us next generalize to more particles. If a single body quantum problem is described by a Hilbert space $\mathcal{H}$ of dimension $\operatorname{dim} \mathcal{H}=d$ then $N$ distinguishable quantum particles are described by the tensor product of $N$ Hilbert spaces

$$
\begin{equation*}
\mathcal{H}^{(N)} \equiv \mathcal{H}^{\otimes N} \equiv \bigotimes_{i=1}^{N} \mathcal{H} \tag{4.1}
\end{equation*}
$$

with dimension $d^{N}$.

In this Chapter we will specifically focus on quantum spin- $1 / 2$ particles. A single spin-1/2 has a Hilbert space $\mathcal{H}=\mathbb{C}^{2}$ of dimension 2, but $N$ spin-1/2 have a Hilbert space $\mathcal{H}^{(N)}=\mathbb{C}^{2^{N}}$ of dimension $2^{N}$. This exponential scaling of the Hilbert space dimension with the number of particles is a big challenge. The basis for $N=30$ spins is already of size $2^{30} \approx 10^{9}$. A single complex vector needs 16 GByte of memory and may just barely fit into the memory of your personal computer.

For small and moderately sized systems of up to about 30 spin- $1 / 2$ we can calculate exactly the ground state, low-lying spectrum, and time evolution by direct calculations. For more than 30 spins we cannot apply exact diagonalization techniques anymore, and this will be the subject of several methods we will study in the next chapters.

### 4.1.1 Hamiltonian Matrix

As we have seen already in the previous Chapter, to perform exact diagonalization to find eigenstates of a given Hamiltonian, $\hat{H}$, or study its dynamics, it is important to come up with a concrete representation of the Hamiltonian matrix that can be efficiently manipulated on a computer. One common feature of many-body quantum models is that the matrix representation of their hamiltonian is sparse. For example, taking again the case of quantum spins, one can see that the total number of non-zero elements in the matrix representation of the Hamiltonian is at most $k \times 2^{N}$, where $k$ is
typically a small value (in most cases, $k \sim N$ ). This is to be contrasted to a general, full matrix, that instead contains $\mathcal{O}\left(2^{N} \times 2^{N}\right)$ elements. Sparsity-a generalization of the simple pattern of non-zero elements seen in tridiagonal matrices in the previous Chapter- can be exploited by exact diagonalization methods in different ways, both to find eigenvalues and eigenvectors of the Hamiltonian and to study its dynamics. Before seeing how sparsity can be exploited, we will first analyze a few prototypical spin models, in order to better understand where the sparse nature of the Hamiltonian matrix comes from. In all cases we will analyze in this Chapter we will consider the simple, and widely adopted, basis of eigenstates of $\hat{\sigma}^{z}$. Specifically, each many-spin state is written as a linear combination of $2^{N}$ basis states:

$$
\begin{equation*}
|\Psi\rangle=\sum_{s_{1} s_{2} \ldots s_{N}} c_{s_{1} s_{2} \ldots s_{N}}\left|s_{1} s_{2} \ldots s_{N}\right\rangle \tag{4.2}
\end{equation*}
$$

where

$$
\begin{equation*}
\left|s_{1} s_{2} \ldots s_{N}\right\rangle=\left|s_{1}\right\rangle \otimes\left|s_{2}\right\rangle \otimes \ldots\left|s_{N}\right\rangle \tag{4.3}
\end{equation*}
$$

are eigen-kets of the $\hat{\sigma}^{z}$ Pauli matrix:

$$
\begin{equation*}
\hat{\sigma}_{i}^{z}\left|s_{1} s_{2} \ldots s_{N}\right\rangle=s_{i}\left|s_{1} s_{2} \ldots s_{N}\right\rangle \tag{4.4}
\end{equation*}
$$

for $s_{i}= \pm 1$.

### 4.1.2 Example: the transverse-field Ising model

The simplest quantum spin model is probably the quantum transverse field Ising model (TFIM), which adds a magnetic field in the $x$ direction to a lattice of spin- $1 / 2$ particles coupled by an Ising interaction:

$$
\begin{equation*}
\hat{H}=\sum_{\langle i, j\rangle} J_{i j} \hat{\sigma}_{i}^{z} \hat{\sigma}_{j}^{z}-\Gamma \sum_{i} \hat{\sigma}_{i}^{x} \tag{4.5}
\end{equation*}
$$

Here the symbol $\langle i, j\rangle$ denotes a sum over all bonds in the lattice. In the absence of the second term, the first term is nothing but a classical Ising model and can be solved by your favorite method of simulating the Ising model. The second term does not exist in classical Ising models, where the spins point only in the $z$ direction. Considering that the Pauli $\hat{\sigma}^{x}$ matrix is

$$
\hat{\sigma}^{x}=\left(\begin{array}{ll}
0 & 1  \tag{4.6}\\
1 & 0
\end{array}\right)
$$

we see that this term flips an $\uparrow$ spin to a $\downarrow$ spin, and thus introduces quantum fluctuations to the classical Ising model.

The way of writing the hamiltonian as above is nothing but a short-hand for the more laborious (but more precise) notation with tensor products, that in this case would imply for example that a spin operator in the direction $\alpha=(x, y, z)$ and acting on spin $i$ is in reality the following $2^{N} \times 2^{N}$ matrix:

$$
\begin{align*}
\hat{\sigma}_{i}^{\alpha} & \equiv \underbrace{\hat{I} \otimes \hat{I} \otimes \ldots \hat{I}}_{i-1 \text { times }} \otimes \hat{\sigma}^{\alpha} \otimes \underbrace{\hat{I} \otimes \cdots \otimes \hat{I}}_{N-i \text { times }}  \tag{4.7}\\
& =\hat{I}\left(2^{i-1}\right) \otimes \hat{\sigma}^{\alpha} \otimes \hat{I}\left(2^{N-i}\right) \tag{4.8}
\end{align*}
$$

where $\hat{I}(n)$ are identity matrices of dimension $n$, and the $\otimes$ product here denotes Kronecker product between matrices.

We can readily verify that this Hamiltonian is sparse. For example, let's start computing the diagonal matrix elements in the basis specified above:

$$
\begin{equation*}
\left\langle s_{1} s_{2} \ldots s_{N}|\hat{H}| s_{1} s_{2} \ldots s_{N}\right\rangle=\sum_{\langle i, j\rangle} J_{i j} s_{i} s_{j} \tag{4.9}
\end{equation*}
$$

which is the familiar classical Ising interaction term. Thus we have found the first $2^{N}$ (in general) non-zero matrix elements, corresponding to the diagonal of $\hat{H}$. The offdiagonal terms can be readily found noticing that the action of the $\hat{\sigma}_{i}^{x}$ operator is just to flip a spin:

$$
\begin{equation*}
\hat{\sigma}_{i}^{x}\left|s_{1} \ldots s_{i} \ldots s_{N}\right\rangle=\left|s_{1} \cdots-s_{i} \ldots s_{N}\right\rangle \tag{4.10}
\end{equation*}
$$

thus there is only one non-zero matrix element per $\hat{\sigma}_{i}^{x}$ term:

$$
\begin{equation*}
\left\langle s_{1}^{\prime} s_{2}^{\prime} \ldots s_{N}^{\prime}\left|\hat{\sigma}_{i}^{x}\right| s_{1} s_{2} \ldots s_{N}\right\rangle=\delta_{s_{1}^{\prime}, s_{1}} \ldots \delta_{s_{i}^{\prime}-s_{i}} \ldots \delta_{s_{N}^{\prime}, s_{N}} \tag{4.11}
\end{equation*}
$$

implying that, at fixed $\left|s_{1} s_{2} \ldots s_{N}\right\rangle$, there is a total of $N$ non zero matrix elements for the Hamiltonian. In total, therefore, we have that the TFI Hamiltonian contains "only" $(N+1) \times 2^{N}$ non-zero elements.

### 4.2 Finding Ground States

We start with the problem of finding the lowest eigenvector (and its energy) of the Hamiltonian, the so-called ground state. This task is realized by using an iterative matrix eigensolver. These solvers exploit the fact that computing the product of the Hamiltonian matrix with an arbitrary vector can be done efficiently. While for a generic matrix of size $M \times M$ a product $\hat{A}|v\rangle$ can be computed in $\mathcal{O}\left(M^{2}\right)$ time, for a matrix $M \times M$, in the case of Hamiltonians we are considering here this product is computable in only $\mathcal{O}(M)=\mathcal{O}\left(N^{\alpha} \times 2^{N}\right)$, where $\alpha$ is in general a small exponent ( $\alpha=1$, for the TFIM, as seen before).

### 4.2.1 Power Method

The power method is the simplest iterative solver we can use to find ground-states of many-body Hamiltonians that exploits sparseness. This method generates a sequence of $P$ vectors $k=1, \ldots P$ by repeated application of the Hamiltonian:

$$
\begin{equation*}
\left|u_{k+1}\right\rangle=(\Lambda \hat{I}-\hat{H})\left|u_{k}\right\rangle \tag{4.12}
\end{equation*}
$$

where $\Lambda$ is a suitable constant, and the initial state $\left|u_{0}\right\rangle$ is given as starting condition for the algorithm. This sequence of vectors converges to the ground-state of the Hamiltonian under reasonable assumptions. To see this, let us formally expand the initial vector in terms of the eigen-states of the Hamiltonian:

$$
\begin{equation*}
\left|u_{0}\right\rangle=\sum_{l} c_{l}\left|E_{l}\right\rangle \tag{4.13}
\end{equation*}
$$

with $E_{0} \leq E_{1} \leq \ldots E_{M}$, thus the last state is

$$
\begin{align*}
\left|u_{P}\right\rangle & =(\Lambda \hat{I}-\hat{H})^{P}\left|u_{0}\right\rangle  \tag{4.14}\\
& =\sum_{l}\left(\Lambda-E_{l}\right)^{P} c_{l}\left|E_{l}\right\rangle \tag{4.15}
\end{align*}
$$

and the overlap with the ground state is

$$
\begin{equation*}
\left\langle E_{0} \mid u_{P}\right\rangle=\left(\Lambda-E_{0}\right)^{P} c_{0} \tag{4.16}
\end{equation*}
$$

We notice however that the state $\left|u_{P}\right\rangle$ is not normalized in general, thus the probability amplitude of being in the ground-state after $\mathrm{k}$ iterations is

$$
\begin{align*}
\frac{\left|\left\langle E_{0} \mid u_{P}\right\rangle\right|^{2}}{\left\langle u_{P} \mid u_{P}\right\rangle} & =\frac{\left(\Lambda-E_{0}\right)^{2 P}\left|c_{0}\right|^{2}}{\left(\Lambda-E_{0}\right)^{2 P}\left|c_{0}\right|^{2}+\left(\Lambda-E_{1}\right)^{2 P}\left|c_{1}\right|^{2}+\ldots}  \tag{4.17}\\
& =\frac{1}{1+\frac{\left(\Lambda-E_{1}\right)^{2 P}}{\left(\Lambda-E_{0}\right)^{2 P}} \frac{\left|c_{1}\right|^{2}}{\left|c_{0}\right|^{2}}+\ldots} \tag{4.18}
\end{align*}
$$

From this expression we can see that a suitable choice of $\Lambda$ can force the state $\left|u_{P}\right\rangle$ have a probability amplitude of being in the ground state that is exponentially close to 1. Specifically, if we impose $\Lambda>E_{M}$, we have that

$$
\begin{equation*}
\lim _{P \rightarrow \infty} \frac{\left(\Lambda-E_{l}\right)^{2 P}}{\left(\Lambda-E_{0}\right)^{2 P}}=0 \tag{4.19}
\end{equation*}
$$

for any excited state $l$ such that $E_{l}>E_{0}$. In the limit of large $P$ we therefore have that

$$
\begin{equation*}
\frac{\left|\left\langle E_{0} \mid u_{P}\right\rangle\right|^{2}}{\left\langle u_{P} \mid u_{P}\right\rangle} \simeq 1-\frac{\left(\Lambda-E_{1}\right)^{2 P}}{\left(\Lambda-E_{0}\right)^{2 P}} \frac{\left|c_{1}\right|^{2}}{\left|c_{0}\right|^{2}} \tag{4.20}
\end{equation*}
$$

and the correction can be made arbitrarily (and exponentially) small by increasing the number of steps $P$. We also see that for the exponential convergence to be true we need to have that the initial state has some finite overlap with the exact ground state, namely $\left|c_{0}\right|^{2} \neq 0$. This can be achieved, for example, starting the iterations from a random vector.

The power method is therefore a very simple, yet exponentially converging method, to find the ground state of the Hamiltonian. If, for example, the Hamiltonian is stored in memory as a sparse matrix, then by simple iterative applications one can find the ground state. In practice, it is convenient to keep the state $\left|u_{k}\right\rangle$ normalized at each step, to avoid an exponential increase of the coefficients appearing in the vector $\left|u_{k}\right\rangle$.

### 4.2.2 The Lanczos Method

The Lanczos algorithm is an important improvement over the power method, that allows to reconstruct not only the ground state wave function, but also excited states. The Lanczos algorithm builds an orthogonal basis $\left\{v_{1}, v_{2}, \ldots, v_{P}\right\}$ for the Krylov-subspace
$K_{P}=\operatorname{span}\left\{u_{1}, u_{2}, \ldots, u_{P}\right\}$, which is constructed by $P$ iterations of the power method. This is achieved by the following iterations:

$$
\begin{equation*}
\beta_{n+1}\left|v_{n+1}\right\rangle=\hat{H}\left|v_{n}\right\rangle-\alpha_{n}\left|v_{n}\right\rangle-\beta_{n}\left|v_{n-1}\right\rangle \tag{4.21}
\end{equation*}
$$

where

$$
\begin{equation*}
\alpha_{n}=\left\langle v_{n}|\hat{H}| v_{n}\right\rangle, \quad \beta_{n}=\left|\left\langle v_{n}|\hat{H}| v_{n-1}\right\rangle\right| . \tag{4.22}
\end{equation*}
$$

Since the orthogonality condition

$$
\begin{equation*}
\left\langle v_{i} \mid v_{j}\right\rangle=\delta_{i j} \tag{4.23}
\end{equation*}
$$

does not determine the phases of the basis vectors, the $\beta_{i}$ can be chosen to be real and positive. It can be shown that we only need to keep three vectors of size $M$ in memory, which makes the Lanczos algorithm very efficient, when compared to dense matrix eigen-solvers which require storage of order $M^{2}$ (see Table 4.1 for a summary of the complexity of matrix operations).

In the Krylov basis the matrix $\hat{H}$ is approximated by the following tridiagonal matrix

$$
\hat{T}^{(n)} \doteq\left[\begin{array}{ccccc}
\alpha_{1} & \beta_{2} & 0 & \cdots & 0  \tag{4.24}\\
\beta_{2} & \alpha_{2} & \ddots & \ddots & \vdots \\
0 & \ddots & \ddots & \ddots & 0 \\
\vdots & \ddots & \ddots & \ddots & \beta_{n} \\
0 & \cdots & 0 & \beta_{n} & \alpha_{n}
\end{array}\right]
$$

and it can also been shown that the eigenvalues $\left\{\tau_{1}, \ldots, \tau_{M}\right\}$ of $\hat{T}$ are good approximations of the eigenvalues of $\hat{H}$. Moreover, the extreme eigenvalues converge very fast. Thus $P \ll M$ iterations are sufficient to obtain the extreme eigenvalues. Since the Lanczos matrix is tridiagonal, we can use all the efficient computational approaches discussed in the previous Chapter to find both its eigenvalues and eigenvectors.

In practice, the Lanczos method can be already found implemented in all linear algebra solvers for sparse matrices, for example in scipy. For Python users, we strongly suggest to use SciPy (in particular scipy.sparse.linalg) which performs Lanczos/Arnoldi calling an efficient, C-coded backend. These routines allow to diagonalize directly sparse matrices defined within scipy. Alternatively, and in order to avoid storing the sparse matrix, one can also define its own Matrix-Vector multiplication using scipy.sparse.linalg.LinearOperator, and then obtain the eigenvalues and eigenvectors with a call to scipy.sparse.linalg.eigsh.

A more detailed discussion of the Lanczos algorithm and the issue of ghost eigenvalues can be found in Appendix 4.5.

### 4.2.3 Implementation

From the practical implementation point of view, the main requirement to use the simple power method or the more refined Lanczos algorithm is to provide a function that computes the product of the Hamiltonian with an arbitrary vector $|v\rangle$ :

$$
\begin{equation*}
\hat{H}|v\rangle=\left|v^{\prime}\right\rangle \tag{4.25}
\end{equation*}
$$

There are two main approaches to implement this efficiently. One one hand, we can form and store the hamiltonian $\hat{H}$ as a sparse matrix. This approach is very elegant and can be readily implemented, for example, in Python with scipy. The only requirement, for spin hamiltonians, is to explicitly use and form the Kronecker products for spin operators, as seen before:

$$
\begin{equation*}
\hat{\sigma}_{i}^{\alpha}=\hat{I}\left(2^{i-1}\right) \otimes \hat{\sigma}^{\alpha} \otimes \hat{I}\left(2^{N-i}\right) \tag{4.26}
\end{equation*}
$$

and then construct interactions terms as simple products of these matrices. For example, spin-spin interaction terms $\hat{\sigma}_{i}^{\alpha} \hat{\sigma}_{j}^{\beta}$ can be readily obtained as a sparse matrix-matrix multiplication.

In addition of being very elegant and compactly implemented, this approach has also the advantage that computing products of sparse matrices with vectors is a typically highly optimized operation in dedicated software libraries, thus the resulting scheme will be automatically highly efficient. The main drawback however is the memory requirements, since we need to store all the non-zero matrix elements of the Hamiltonian, and there are at least as many as $N \times 2^{N}$ of them, as we have seen before. This memory requirement is added to the requirements due to the necessity of storing (at least) the vectors $|v\rangle$ and $\left|v^{\prime}\right\rangle$, yielding an additional $2 \times 2^{N}$ coefficients to be stored.

The main alternative approach is to never store the matrix $\hat{H}$ and provide instead a function that computes the matrix-vector product "on the fly". This allows to drastically reduce the memory consumption to the bare minimum, namely to $2 \times 2^{N}$, at the expenses of, typically, a larger computational time. The latter approach is especially suited for applications where reaching to the largest possible value of $N$ is crucial, and need specialized low-level implementations. In the exercises we will mostly focus on the first approach.

### 4.3 Quantum Dynamics

In the previous discussion we have seen how to explicitly construct sparse representations of the Hamiltonian of quantum spin systems, and how to use them to obtain the ground-state wave-function. We now focus on the problem of solving the timedependent Schrödinger equation for the many-spin system, a task which requires specific techniques. For simplicity, we will analyze here the specific case of time-independent Hamiltonians, and leave the straightforward extension to time-dependent Hamiltonians as an exercise.

### 4.3.1 Taylor Expansion

To implement the time evolution we have to devise an efficient way to numerically compute the matrix exponential $\exp (-i \hat{H} t)$, since for a static Hamiltonian the timeevolved state that satisfies Schrödinger equation reads :

$$
\begin{equation*}
|\Psi(t)\rangle=e^{-i \hat{H} t}|\Psi(0)\rangle \tag{4.27}
\end{equation*}
$$

The most straightforward way to do so is to take a small time step $\Delta_{t}$ and consider a truncated Taylor expansion of the exponential, such that

$$
\begin{equation*}
\left|\Psi\left(t+\Delta_{t}\right)\right\rangle=\left(1-i \Delta_{t} \hat{H}-\frac{\Delta_{t}^{2}}{2} \hat{H}^{2}-i \frac{\Delta_{t}^{3}}{6} \hat{H}^{3}+\ldots\right)|\Psi(t)\rangle \tag{4.28}
\end{equation*}
$$

Taking the first $s$ orders in the Taylor expansion guarantees a scheme locally of order $\mathcal{O}\left(\Delta_{t}^{s}\right)$. This scheme can be efficiently implemented recalling that the Hamiltonian $\hat{H}$ is sparse, and that we can efficiently compute products of $\hat{H}$ with a given vector:

$$
\begin{equation*}
\left|\Psi^{\prime}\right\rangle=\hat{H}|\Psi\rangle \tag{4.29}
\end{equation*}
$$

A simple iterative scheme that realizes the Taylor expansion numerically is given by the following recursion formula:

$$
\begin{align*}
\left|\Gamma_{k}\right\rangle & =\frac{-i \Delta_{t}}{k} \hat{H}\left|\Gamma_{k-1}\right\rangle  \tag{4.30}\\
\left|\Delta_{k}\right\rangle & =\left|\Delta_{k-1}\right\rangle+\left|\Gamma_{k}\right\rangle \tag{4.31}
\end{align*}
$$

for $k=1,2, \ldots s$, up to the maximum truncation order chosen, and with zero-order conditions $\left|\Gamma_{0}\right\rangle=\left|\Delta_{0}\right\rangle=|\Psi(t)\rangle$. Then we have

$$
\begin{equation*}
\left|\Psi\left(t+\Delta_{t}\right)\right\rangle=\left|\Delta_{s}\right\rangle \tag{4.32}
\end{equation*}
$$

This scheme is particularly memory friendly, because it needs to store at most two vectors: $\left|\Delta_{k}\right\rangle$ and $\left|\Gamma_{k}\right\rangle$.

### 4.4 The Trotter-Suzuki decomposition

We now present an alternative numerical scheme which, at variance with the previous Taylor series, explicitly preserves the unitary character of the Hamiltonian evolution. To derive this scheme, we introduce one of the most important tools in computational quantum physics: the Trotter-Suzuki decomposition. ${ }^{1}$

To do this we split the Hamiltonian into a sum of $K$ non-commuting terms $\hat{H}=$ $\sum_{k=1}^{K} \hat{h}_{k}$. The splitting is done in such a way that the exponential of the individual terms, $e^{-i \hat{h}_{k} \Delta_{t}}$, can be easily computed. The time evolution operator $\exp \left(-i \hat{H} \Delta_{t}\right)$ for a small time step $\Delta_{t}$ is then decomposed into multiple products of the non-commuting terms in the Hamiltonian. To first order, the Trotter-Suzuki decomposition for a small time step $\Delta_{t}$ is

$$
\begin{equation*}
\exp \left(-i \hat{H} \Delta_{t}\right)=e^{-i \hat{h}_{1} \Delta_{t}} \ldots e^{-i \hat{h}_{K} \Delta_{t}}+\mathcal{O}\left(\Delta_{t}^{2}\right) \tag{4.33}
\end{equation*}
$$

The second order version of this formula reads

$$
\begin{equation*}
\exp \left(-i \hat{H} \Delta_{t}\right)=e^{-i \hat{h}_{1} \frac{\Delta_{t}}{2}} \ldots e^{-i \hat{h}_{K} \frac{\Delta_{t}}{2}} e^{-i \hat{h}_{K} \frac{\Delta_{t}}{2}} \ldots e^{-i \hat{h}_{1} \frac{\Delta_{t}}{2}}+\mathcal{O}\left(\Delta_{t}^{3}\right) \tag{4.34}
\end{equation*}
$$

For the special case with $K=2$ terms this expression simplifies to

$$
\begin{equation*}
\exp \left(-i \hat{H} \Delta_{t}\right)=e^{-i \hat{h_{1}} \Delta_{t} / 2} e^{-i \hat{h_{2}} \Delta_{t}} e^{-i \hat{h}_{1} \Delta_{t} / 2} \tag{4.35}
\end{equation*}
$$[^0]by combining the two terms $e^{-i \hat{h}_{2} \Delta_{t} / 2} e^{-i \hat{h}_{2} \Delta_{t} / 2}$ into $e^{-i \hat{h}_{2} \Delta_{t}}$. By similarly combining the terms $e^{-i \hat{h}_{1} \Delta_{t} / 2} e^{-i \hat{h}_{1} \Delta_{t} / 2}$ arising from two adjacent time steps into $e^{-i \hat{h}_{1} \Delta_{t}}$ one ultimately needs only one single additional terms for the full time evolution, when compared to the first order approximation. At second order, the full time evolution for $K=2$ indeed reads

$$
\begin{align*}
\exp (-i \hat{H} t) & \simeq e^{-i \hat{h}_{1} \Delta_{t} / 2} e^{-i \hat{h}_{2} \Delta_{t}} e^{-i \hat{h}_{1} \Delta_{t} / 2} \times e^{-i \hat{h}_{1} \Delta_{t} / 2} e^{-i \hat{h_{2} \Delta_{t}}} e^{-i \hat{h}_{1} \Delta_{t} / 2} \ldots  \tag{4.36}\\
& \simeq e^{-i \hat{h}_{1} \Delta_{t} / 2} \ldots e^{-i \hat{h}_{2} \Delta_{t}} e^{-i \hat{h}_{1} \Delta_{t}} \ldots e^{-i \hat{h}_{2} \Delta_{t}} e^{-i \hat{h}_{1} \Delta_{t} / 2} \tag{4.37}
\end{align*}
$$

### 4.4.1 Time evolution for the transverse field Ising model

To implement time evolution in the transverse field Ising model we split the Hamiltonian into $K=2$ non-commuting terms. The first one is the the transverse field term

$$
\begin{equation*}
\hat{H}_{x}=-\Gamma \sum_{l} \hat{\sigma}_{l}^{x} \tag{4.38}
\end{equation*}
$$

and the second one is the Ising term

$$
\begin{equation*}
\hat{H}_{z}=\sum_{\langle l, m\rangle} J_{l m} \hat{\sigma}_{l}^{z} \hat{\sigma}_{m}^{z} \tag{4.39}
\end{equation*}
$$

We will now see that each of these terms can be easily exponentiated.

The transverse field term splits into $N$ commuting terms for each of the spins:

$$
\begin{equation*}
e^{-i \hat{H}_{x} \Delta_{t}}=e^{i \Delta_{t} \Gamma \sum_{l} \hat{\sigma}_{l}^{x}}=\prod_{l} e^{i \Delta_{t} \Gamma \hat{\sigma}_{l}^{x}} \tag{4.40}
\end{equation*}
$$

Each of the terms in the product above can be written explicitly in Kronecker product form:

$$
\begin{equation*}
e^{i \Delta_{t} \Gamma \hat{\sigma}_{l}^{x}}=\hat{I}\left(2^{l-1}\right) \otimes\left(\cos \left(\Delta_{t} \Gamma\right) \hat{I}(2)+i \sin \left(\Delta_{t} \Gamma\right) \hat{\sigma}^{x}\right) \otimes \hat{I}\left(2^{N-l}\right) \tag{4.41}
\end{equation*}
$$

The Ising term instead is diagonal, and the exponentiation is particularly simple, yielding a diagonal matrix:

$$
\begin{equation*}
e^{-i \hat{H}_{z} \Delta_{t}}\left|s_{1} s_{2} \ldots s_{N}\right\rangle=\prod_{\langle l, m\rangle} e^{-i \Delta_{t} J_{l m} s_{l} s_{m}}\left|s_{1} s_{2} \ldots s_{N}\right\rangle \tag{4.42}
\end{equation*}
$$

We can further write this as a sum of Kronecker products, noticing that (the proof is left as an exercise)

$$
\begin{equation*}
e^{-i \theta \hat{\sigma}_{\hat{\sigma}} \hat{\sigma}_{m}^{z}}=\cos \theta \hat{I}\left(2^{N}\right)-i \sin \theta \hat{\sigma}_{l}^{z} \hat{\sigma}_{m}^{z} \tag{4.43}
\end{equation*}
$$

thus each term in the product $\prod_{\{l, m\rangle} e^{-i \Delta_{t} J_{l m} s_{l} s_{m}}$ can be easily applied recalling the explicit Kronecker product form of $\hat{\sigma}_{l}^{z}$ and $\hat{\sigma}_{m}^{z}$.

Overall, then both the diagonal and the off diagonal terms can easily be applied to a wave function in a similar way as we did for the multiplication with the Hamiltonian $\hat{H}$. We will implement time evolution for the TFIM in the exercises.

Table 4.1: Time and memory complexity for operations on sparse and dense $M \times M$ matrices

| operation | time | memory |
| :--- | :---: | :---: |
| storage <br> dense matrix <br> sparse matrix | - | $M^{2}$ |
| matrix-vector multiplication <br> dense matrix <br> sparse matrix | - | $\mathrm{O}(M)$ |
| matrix-matrix multiplication <br> dense matrix <br> sparse matrix | $\mathrm{O}\left(M^{2}\right)$ | $\mathrm{O}\left(M^{2}\right)$ |
| all eigen values and vectors <br> dense matrix <br> sparse matrix (iterative) | $\mathrm{O}(M)$ | $\mathrm{O}(M)$ |
| some eigen values and vectors <br> dense matrix (iterative) <br> sparse matrix (iterative) | $\mathrm{O}(M) \ldots \mathrm{O}\left(M^{\ln 7 / \ln 2)}\right.$ | $\mathrm{O}(M) \ldots \mathrm{O}\left(M^{2}\right)$ |

### 4.5 Appendix: The Lanczos algorithm

Sparse matrices with only $\mathcal{O}(M)$ non-zero elements are very common in scientific simulations. We have seen in this Chapter that many-body quantum Hamiltonians belong to the class of sparse matrices, and that for typical spin models one has $M \sim 2^{N} N^{\alpha}$, for some small power $\alpha$.

The importance of sparsity becomes obvious when considering the cost of matrix operations as listed in table 4.1. For large $M$ the sparsity leads to memory and time savings of several orders of magnitude.

Here we will discuss the iterative calculation of a few of the extreme eigenvalues of a matrix by the Lanczos algorithm. Similar methods can be used to solve sparse linear systems of equations.

### 4.5.1 Finding eigenvectors

While finding the eigenvectors of the tridiagonal Lanczos matrix $\hat{T}$ is a relatively easy computational task, however these are not directly the eigenvectors of the original matrix $\hat{H}$, since they are given in the (much smaller) Krylov basis $\left\{v_{1}, v_{2}, \ldots, v_{P}\right\}$. To obtain the eigenvectors in the original basis we need to perform a basis transformation.

Due to memory constraints we usually do not store all the $v_{i}$, but only the last three vectors. To transform the eigenvector to the original basis we have to do the Lanczos iterations a second time. Starting from the same initial vector $v_{1}$ we construct the vectors $v_{i}$ iteratively and perform the basis transformation as we go along.

### 4.5.2 Roundoff errors and ghosts in the Lanczos algorithm

In exact arithmetic the vectors $\left\{v_{i}\right\}$ are orthogonal and the Lanczos iterations stop after at most $M-1$ steps. The eigenvalues of $\hat{T}$ are then the exact eigenvalues of $\hat{H}$.

Roundoff errors in finite precision however cause a loss of orthogonality. There are two ways to deal with that:

- Re-orthogonalization of the vectors after every step. This requires storing all of the vectors $\left\{v_{i}\right\}$ and is memory intensive.
- Control of the effects of roundoff.

We will discuss the second solution as it is faster and needs less memory. The main effect of roundoff errors is that the matrix $\hat{T}$ contains extra spurious eigenvalues, called "ghosts". These ghosts are not real eigenvalues of $\hat{A}$. However they converge towards real eigenvalues of $\hat{A}$ over time and increase their multiplicities.

A simple criterion distinguishes ghosts from real eigenvalues. Ghosts are caused by roundoff errors. Thus they do not depend on on the starting vector $v_{1}$. As a consequence these ghosts are also eigenvalues of the matrix $\hat{Q}^{(n)}$, which can be obtained from $\hat{T}$ by deleting the first row and column:

$$
\hat{Q}^{(n)}:=\left[\begin{array}{ccccc}
\alpha_{2} & \beta_{3} & 0 & \cdots & 0  \tag{4.44}\\
\beta_{3} & \alpha_{3} & \ddots & \ddots & \vdots \\
0 & \ddots & \ddots & \ddots & 0 \\
\vdots & \ddots & \ddots & \ddots & \beta_{n} \\
0 & \cdots & 0 & \beta_{n} & \alpha_{n}
\end{array}\right]
$$

From these arguments we derive the following heuristic criterion to distinguish ghosts from real eigenvalues:

- All multiple eigenvalues are real, but their multiplicities might be too large.
- All single eigenvalues of $T$ which are not eigenvalues of $\tilde{T}$ are also real.


### 4.5.3 Open-source implementations

Numerically stable and efficient implementations of the Lanczos algorithm can be obtained as part of open-source packages.

For Python users, we strongly suggest to use SciPy (in particular scipy.sparse.linalg) which performs Lanczos/Arnoldi calling an efficient, C-coded backend. These routines allow to diagonalize directly sparse matrices defined within scipy. Alternatively, and in order to avoid storing the sparse matrix, one can also define its own Matrix-Vector multiplication using scipy.sparse.linalg.LinearOperator, and then obtain the eigenvalues and eigenvectors with a call to scipy.sparse.linalg.eigsh.

For C++ users, we strongly suggest the use of the EIGEN library ${ }^{2}$ in conjunction with SPECTRA ${ }^{3}$. Both libraries are header-only, require almost no installation effort[^1](apart from downloading it), and are very efficient. SPECTRA handles the Lanczos/Arnoldi algorithm, and just needs the user to implement a function implementing the Matrix-Vector multiplication, with minor modifications with respect to the one previously discussed in the Lecture.


[^0]:    ${ }^{1}$ H. F. Trotter, On the product of semi-groups of operators, Proc. Amer. Math. Soc. 10, 545 (1959); M. Suzuki, Generalized Trotter's formula and systematic approximants of exponential operators and inner derivations with applications to many-body problems, Commun. Math. Phys. 51, 183 (1976).

[^1]:    ${ }^{2} \mathrm{http} / / /$ eigen.tuxfamily.org/

    ${ }^{3} \mathrm{http}: / /$ yixuan.cos.name/spectra/

