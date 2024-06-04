## Quantum computing

### 14.1 Quantum bits and quantum gates

In 1982 Feynman suggested that the problem of exponential complexity of simulating a quantum system can be solved by using quantum mechanics itself for computing, thus laying the foundation for the field of quantum computing [1]. Just as there are many ways to build a classical computer and lots of different conventions, also quantum computers could be designed in many different ways. Since we don't have any large scale quantum computer yet we are free to choose a design that is simple from a theoretical point of view.

### 14.1.1 Quantum bits

The basic memory element is typically chosen as the quantum bit, or qubit for short a two-level system like a spin- $1 / 2$, where we associate the up spin state with the 0 bit and the down spin state with the 1 bit:

$$
\begin{align*}
& |0\rangle=|\uparrow\rangle=\binom{1}{0}  \tag{14.1}\\
& |1\rangle=|\downarrow\rangle=\binom{0}{1} \tag{14.2}
\end{align*}
$$

Just like for quantum spin-1/2s the quantum bit can exist in an arbitrary superposition of these two states:

$$
\begin{equation*}
|\Psi\rangle=\alpha|0\rangle+\beta|1\rangle \tag{14.3}
\end{equation*}
$$

where the normalization condition requires that $|\alpha|^{2}+|\beta|^{2}=1$. While such a state needs an infinite number of classical bits to be described accurately (think of the binary representation of $\alpha$ and $\beta$ ), a measurement will only give a single bit of information, either 0 or 1 . A register of $N$ qubits can store the wave function of $N$ spin-1/2s. This gives an exponential advantage in memory use. However, since we can only do one measurement on each qubit only $N$ bits of information can ever be read out. This is the first restriction we have to face when devising quantum algorithms, for which a clever use of these quantum bits needs to be devised.

| Gate Name | Symbol | Matrix Form |
| :--- | :---: | :---: |
| Pauli-X (NOT) | $-\boxed{X}$ | $\left(\begin{array}{cc}0 & 1 \\ 1 & 0\end{array}\right)$ |
| Pauli-Y | $-Y$ | $\left(\begin{array}{cc}0 & -i \\ i & 0\end{array}\right)$ |
| Pauli-Z | $-Y$ | $\left(\begin{array}{cc}1 & 0 \\ 0 & -1\end{array}\right)$ |
| Hadamard gate | $-\boxed{Z}$ | $\frac{1}{\sqrt{2}}\left(\begin{array}{cc}1 & 1 \\ 1 & -1\end{array}\right)$ |
| Phase gate | $-\boxed{S}$ | $\left(\begin{array}{cc}1 & 0 \\ 0 & i\end{array}\right)$ |
| T gate or $\pi / 8$ gate | $-\boxed{T}$ | $\left(\begin{array}{cc}1 & 0 \\ 0 & e^{i \pi 4}\end{array}\right)$ |
| Rz $(\theta)$ gate | $-\mathrm{Rz}(\theta)$ | $\left(\begin{array}{cc}e^{-i \theta / 2} & 0 \\ 0 & e^{i \theta / 2}\end{array}\right)$ |

Table 14.1: List of commonly used single-qubit gates

### 14.1.2 Quantum gates

Since quantum mechanical time evolution is unitary (apart from measurements that collapse the wave function), we can only perform unitary operations on quantum bits and measurements. This is the second big restriction.

Just as for classical computers it is convenient to build a quantum circuit from a set of quantum gates that act on a limited set of qubits. Classical circuits are typically built from a set of gates that include OR, AND, NOT, XOR and more. However, in principle only the NAND (not-AND) gate is necessary since all other gates can be built from it. The NAND gate is thus called universal: any classical computation can be done purely with NAND gates, and any boolean function can be written in terms of NAND gates. It still makes sense however to consider more types of gates when building circuits, to make the design of circuits easier.

For quantum circuits one similarly often uses a larger set of gates than is strictly necessary. In the following we will discuss a set of typically used one and two qubit gates and will then discuss which ones are strictly necessary.

### 14.1.2.1 Single qubit gates

A few remarks may be useful. The $X$ gate is the quantum analog of a classical NOT gate. The Hadamard gate $(H)$ squares to the identity and is essentially a ninety degree rotation around the $y$ axis, rotating a state aligned with $z$ to $x$. The $T$ gate is also called $\pi / 8$ gate since it can - up to an irrelevant global phase - be written as

$$
T=e^{i \pi / 8}\left(\begin{array}{cc}
e^{-i \pi / 8} & 0  \tag{14.4}\\
0 & e^{i \pi / 8}
\end{array}\right)
$$

The $R z$ gate performs a rotation around the $z$ axis in spin space. Similar rotations around the $x$ and $y$ axis are performed by the $R x$ and $R y$ gates. For example, a
rotation around the $x$ axis can be performed by swapping $z$ and $x$ by a Hadamard gate, performing a rotation around the $z$ axis, and then rotating back:

$$
\begin{equation*}
-\sqrt{\operatorname{Rx}(\theta)}-\sqrt{\mathrm{Rz}(\theta)}-\mathrm{H} \tag{14.5}
\end{equation*}
$$

### 14.1.2.2 Two-qubit gates

A set of common two-qubit gates are controlled gates, consisting of a control qubit and a target qubit. The controlled version CU of a single qubit gate U (any of the list above) performs the single qubit operation $\mathrm{U}$ on the target qubit only if the control qubit is set to 1 .

The quantum circuit for such a gate is:

![](https://cdn.mathpix.com/cropped/2024_05_17_2e07d6383b5b33be2a66g-3.jpg?height=156&width=192&top_left_y=913&top_left_x=886)

Denoting the matrix representation of the gate $\mathrm{U}$ as $\mathcal{U}$, the matrix representation of $\mathrm{CU}$ in a basis $|00\rangle,|01\rangle,|10\rangle,|11\rangle$ is

$$
\left(\begin{array}{cc|cc}
1 & 0 & 0 & 0  \tag{14.7}\\
0 & 1 & 0 & 0 \\
\hline 0 & 0 & \mathcal{U} \\
0 & 0 &
\end{array}\right)
$$

Maybe the most important two-qubit gate is the controlled-NOT-gate (CNOT), which is the same as a controlled-X gate. It is typically drawn as:

![](https://cdn.mathpix.com/cropped/2024_05_17_2e07d6383b5b33be2a66g-3.jpg?height=111&width=162&top_left_y=1555&top_left_x=907)

its matrix representation is

$$
\mathrm{CNOT} \doteq\left(\begin{array}{cccc}
1 & 0 & 0 & 0  \tag{14.9}\\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{array}\right)
$$

Other two-qubit gates can be built from single qubit gates and the CNOT gate. For example, the SWAP gate, which swaps the states of two qubits, can be built from three CNOT gates as:

![](https://cdn.mathpix.com/cropped/2024_05_17_2e07d6383b5b33be2a66g-3.jpg?height=146&width=626&top_left_y=2140&top_left_x=675)

In matrix representation the previous circuit corresponds to:

$$
\left(\begin{array}{llll}
1 & 0 & 0 & 0  \tag{14.11}\\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{array}\right)\left(\begin{array}{llll}
1 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0 \\
0 & 1 & 0 & 0
\end{array}\right)\left(\begin{array}{llll}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{array}\right)=\left(\begin{array}{llll}
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1
\end{array}\right) .
$$

The last gate corresponds to the SWAP operation, indeed one can immediately verify that its action corresponds to

$$
\left(\begin{array}{llll}
1 & 0 & 0 & 0  \tag{14.12}\\
0 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1
\end{array}\right)\left(\begin{array}{l}
c_{00} \\
c_{01} \\
c_{10} \\
c_{11}
\end{array}\right)=\left(\begin{array}{l}
c_{00} \\
c_{10} \\
c_{01} \\
c_{11}
\end{array}\right)
$$

### 14.1.2.3 Universal gate sets

Of the above gates just the Hadamard, $\pi / 8$ and CNOT gates are sufficient to implement any quantum circuit. All the other gates can be built from these gates, similar to the NAND gate being universal for classical computing.

The tricky part is how to represent arbitrary rotations using a discrete gate set. The Solovay-Kitaev algorithm allows to approximate arbitrary rotations to within any desired accuracy $\epsilon$, with just poly $\left(\log (1 / \epsilon)\right.$ gates. ${ }^{1}$ Better algorithms for approximation of rotations have recently been invented and this is still an interesting field of research.

### 14.1.3 Measurements

Measurements in quantum circuits can be done on an arbitrary number of qubits, and the conventional setting of quantum computing is to consider measurements of qubits in the computational basis, thus corresponding to measuring the spin in the $\mathrm{Z}$ direction. Diagrammatically, measurements are indicated as in the figure below, that shows a measurement of the uppermost qubit:

![](https://cdn.mathpix.com/cropped/2024_05_17_2e07d6383b5b33be2a66g-4.jpg?height=197&width=329&top_left_y=1575&top_left_x=909)

with a probability of observing one of the two possible outcomes $(+1$ or -1$)$ given in this case by

$$
\begin{equation*}
P\left(s_{1}= \pm 1\right)=\sum_{s_{2}= \pm 1}\left|\left\langle s_{1}, s_{2}|\hat{U}| 0,0\right\rangle\right|^{2} \tag{14.14}
\end{equation*}
$$

Measurements in other directions are possible after applying suitable rotations of the spin, for example measuring in the $\mathrm{X}$ direction can be done by performing a rotation through the Hadamard gate. The circuit below shows a measurement of this type:

![](https://cdn.mathpix.com/cropped/2024_05_17_2e07d6383b5b33be2a66g-4.jpg?height=195&width=454&top_left_y=2304&top_left_x=847)[^0]

### 14.1.4 Example: Creating entangled quantum states

As a first simple quantum algorithm that can be constructed using the build blocks discussed above, we will consider the task of creating entangled quantum states. Those can be very useful, for instance, in quantum communication tasks. One of the most prototypical entangled states are Bell states, also called EPR pairs after the EinsteinPodolsky-Rosen paper. These are produced by the following circuit:

![](https://cdn.mathpix.com/cropped/2024_05_17_2e07d6383b5b33be2a66g-5.jpg?height=168&width=694&top_left_y=630&top_left_x=612)

Starting from an initial state $\left|\psi_{0}\right\rangle=|x\rangle|y\rangle$, where $x$ and $y$ are either 0 or 1 and not in superposition, the circuit produces a final state

$$
\begin{equation*}
\left|\beta_{x y}\right\rangle \equiv \frac{|0, y\rangle+(-1)^{x}|1, \bar{y}\rangle}{\sqrt{2}} \tag{14.17}
\end{equation*}
$$

For pure initial states $|00\rangle,|01\rangle,|10\rangle$ and $|11\rangle$ we obtain the four Bell states called $\left|\beta_{00}\right\rangle,\left|\beta_{01}\right\rangle,\left|\beta_{10}\right\rangle$ and $\left|\beta_{11}\right\rangle$. The four possible outcomes are summarized in the Table below:

| In | Out |
| :---: | :---: |
| $\|00\rangle$ | $\frac{\|00\rangle+\|11\rangle}{\sqrt{2}}$ |
| $\|01\rangle$ | $\frac{\|01\rangle+110\rangle}{\sqrt{2}}$ |
| $\|10\rangle$ | $\frac{\|00\rangle-111}{\sqrt{2}}$ |
| $\|11\rangle$ | $\frac{\|01\rangle-10\rangle}{\sqrt{2}}$ |

Table 14.2: Input-Output table for the circuit creating Bell states.

### 14.2 Simulating the dynamics of quantum systems

### 14.2.1 Time evolution of a quantum spin model

Exponential speedup over classical computers can be obtained for the simulation of the dynamics of quantum systems. As an example, we will consider once more the transverse field Ising model. Notation-wise, we will adopt a calligraphic notation for the Hamiltonian to avoid confusion with the Hadamard gate and we will also use the notation for Pauli matrices normally adopted in quantum computing: $\hat{Z}_{i}=\hat{\sigma}_{i}^{z}, \hat{X}_{i}=\hat{\sigma}_{i}^{x}$, $\hat{Y}_{i}=\hat{\sigma}_{i}^{y}$, thus our Hamiltonian is

$$
\begin{equation*}
\hat{\mathcal{H}}=-\Gamma \sum_{i} \hat{X}_{i}+\sum_{\langle i, j\rangle} J_{i j} \hat{Z}_{i} \hat{Z}_{j} \tag{14.18}
\end{equation*}
$$

In order to simulate the time evolution on a quantum computer we have to use a Trotter decomposition just like in the classical case, and again have the choice between simpler low-order approximations or more accurate high-order ones that are more complex but also more accurate.

In this sense, the situation is entirely analogous to what we have seen when doing exact time evolution of quantum systems in the first lectures. The big advantage of quantum computers shows in the implementation of the individual terms of the Trotterized time evolution, which is now much easier. First, we need just $N$ qubits instead of $2^{N}$ complex numbers in a classical code and requires only $\mathcal{O}(N)$ instead of $\mathcal{O}\left(2^{N}\right)$ operations.

The time evolution under the transverse field term $e^{i \Delta_{t} \Gamma \sigma_{i}^{x}}$ is trivial to implement, since it is just a rotation around the $x$ axis, implemented by an $\operatorname{RX}(\theta)$ gate with an angle $\theta=-2 \Delta_{t} \Gamma$ :

$$
\begin{equation*}
-\mathrm{RX}\left(-2 \Delta_{t} \Gamma\right) \tag{14.19}
\end{equation*}
$$

If we the quantum hardware does not offer an RX gate, but only (for example) arbitrary rotations around the $\mathrm{z}$ directions through the $\mathrm{RZ}(\theta)$, then a basis transformation will be needed. It is easy to convince oneself that the Hadamard gate is the unitary matrix that transforms from the $\mathrm{Z}$ basis to the $\mathrm{X}$ basis, thus the Trotter step associated to the dynamics a single spin under the transverse field can be written as :

$$
\begin{equation*}
-H-\mathrm{RZ}\left(-2 \Delta_{t} \Gamma\right)-H \tag{14.20}
\end{equation*}
$$

The Ising term is a 2 -spin coupling and requires a 2 -qubit gate. To implement $e^{-i \Delta_{t} J_{i j} \hat{\sigma}_{i} \hat{\sigma}_{j}^{z}}$ one needs to rotate by an angle $-\Delta_{t} J_{i j}$ if the two spin values are the same and $+\Delta_{t} J_{i j}$ if they differ. The following simple circuit can realize this operation:

![](https://cdn.mathpix.com/cropped/2024_05_17_2e07d6383b5b33be2a66g-6.jpg?height=165&width=554&top_left_y=2276&top_left_x=794)

Similar circuits can be designed for other quantum models, as we will do in the exercises for a quantum Heisenberg model.

### 14.3 Quantum Phase Estimation

### 14.3.1 Measuring energies from phases

We now discuss an algorithm to estimate the energy of a given quantum state. The most straightforward way of measuring the energy of a quantum state $|\psi\rangle$ is to measure all the terms that make up the Hamiltonian $\hat{\mathcal{H}}$ and thus evaluate $\langle\psi|\hat{\mathcal{H}}| \psi\rangle$. However, this approach has several disadvantages. The wave function $|\psi\rangle$ gets destroyed with every measurement and we get only $N$ bits of information. As this approach is similar to Monte Carlo sampling, we need $\mathcal{O}\left(\epsilon^{-2}\right)$ measurements and thus $\mathcal{O}\left(\epsilon^{-2}\right)$ preparations of the wave function $|\psi\rangle$ to measure the energy to an accuracy $\epsilon$.

An alternative is to measure the phase which a state $|\psi\rangle$ picks up under time evolution with $\hat{\mathcal{H}}$. Let us first assume that $|\psi\rangle=\left|E_{n}\right\rangle$ be an eigenstate $\left|E_{n}\right\rangle$ of $\hat{\mathcal{H}}$ with eigenvalue $E_{n}$. Under time evolution $e^{-i \hat{\mathcal{H} t}}|\psi\rangle=e^{-i E_{n} t}\left|E_{n}\right\rangle$ the state picks up a phase $E_{n} t$. Measuring this phase would thus allow to measure the energy.

### 14.3.2 Quantum phase estimation algorithm

But, how do we measure the phase under time evolution? At first sight the phase is not an observable quantity. However, we can set up an "interference experiment" to determine the phase. We add an auxiliary qubit and perform the evolution under $\hat{U}=e^{-i \hat{\mathcal{H}} t}$ only if the auxiliary qubit is on:

![](https://cdn.mathpix.com/cropped/2024_05_17_2e07d6383b5b33be2a66g-7.jpg?height=192&width=574&top_left_y=1383&top_left_x=707)

Let us analyze step by the step what this circuit does. First, we start from $|0\rangle|\psi\rangle$ and apply a Hadamard gate to the auxiliary qubit, giving

$$
\begin{equation*}
\frac{1}{\sqrt{2}}(|0\rangle|\psi\rangle+|1\rangle|\psi\rangle) \tag{14.23}
\end{equation*}
$$

We then apply the evolution controlled by the auxiliary qubit:

$$
\begin{equation*}
\frac{1}{\sqrt{2}}(|0\rangle|\psi\rangle+|1\rangle \hat{U}|\psi\rangle) \tag{14.24}
\end{equation*}
$$

If $|\psi\rangle$ is an eigenstate $\left|E_{n}\right\rangle$ we pick up the corresponding phase $\phi=E_{n} t$

$$
\begin{equation*}
\frac{1}{\sqrt{2}}\left(|0\rangle|\psi\rangle+e^{-i \phi}|1\rangle|\psi\rangle\right) \tag{14.25}
\end{equation*}
$$

Measuring now would not give us any information since the phase cannot be determined from a direct measurement. However, we can interfere the two cases by another Hadamard transform on the auxiliary qubit, obtaining

$$
\begin{equation*}
\frac{1}{2}\left[\left(1+e^{-i \phi}\right)|0\rangle|\psi\rangle+\left(1-e^{-i \phi}\right)|1\rangle|\psi\rangle\right] \tag{14.26}
\end{equation*}
$$

Now we measure the auxiliary qubit and we notice that the probability of measuring 0 is $(1+\cos \phi) / 2=\cos (\phi / 2)^{2}$. By repeating then this experiment many times we can experimentally reconstruct (just counting how many times we measure 0 ) the probability of measuring 0 , and consequently reconstruct $\phi$. Using the histogram method, this probability can be determined to an accuracy of $1 / \sqrt{M}$, if $M$ measurements are realized. Thus, one needs to go through at least $M \sim 2^{2 m}$ independent rounds of measurements to obtain $m$ accurate binary digits of $\phi$.

A more efficient version of this algorithm is due to Kitaev. We only sketch here the idea of this improved approach, that performs time evolutions with times $2^{k} t(k=$ $1, \ldots, n)$, that are powers of 2 , by adding $n$ auxiliary qubits rather than one as in the simpler approach discussed previously. One starts by preparing the state as given by the circuit below:

![](https://cdn.mathpix.com/cropped/2024_05_17_2e07d6383b5b33be2a66g-8.jpg?height=506&width=734&top_left_y=855&top_left_x=707)

This is a generalization of the case with a single auxiliary qubit, and we can readily see that the output state of the circuit above is

$$
\begin{equation*}
\frac{1}{\sqrt{2^{n}}}\left(|0\rangle+e^{-i \phi}|1\rangle\right) \otimes\left(|0\rangle+e^{-i 2 \phi}|1\rangle\right) \otimes \cdots \otimes\left(|0\rangle+e^{-i 2^{n-1} \phi}|1\rangle\right) \otimes|\psi\rangle . \tag{14.28}
\end{equation*}
$$

We therefore end up with a register containing the Fourier transform of the phase:

$$
\begin{equation*}
\frac{1}{\sqrt{2^{n}}} \sum_{k=0}^{2^{n}-1} e^{-i \phi k}|k\rangle|\psi\rangle \tag{14.29}
\end{equation*}
$$

Employing an inverse quantum Fourier transform $F^{-1}$ (which is a unitary operation and can be implemented efficiently on a quantum computer) we measure a binary representation $\pi x / 2^{n}$ of the phase $\phi$.

The resulting algorithm is written in diagrammatic form below:

![](https://cdn.mathpix.com/cropped/2024_05_17_2e07d6383b5b33be2a66g-8.jpg?height=502&width=1002&top_left_y=2076&top_left_x=570)

The main advantage of Kitaev's phase estimation approach is that it allows to reconstruct the phase much more accurately than using a single auxiliary qubit, since we can determine its value "digit-by-digit" in binary form through the inverse Fourier transform.

### 14.3.3 Quantum phase estimation to find the exact eigenvalues

It is especially interesting to use the quantum phase estimation algorithm in the case when $|\psi\rangle$ is not an exact eigenstate of the Hamiltonian, but rather a generic state. We can then expand it in the the eigenbasis of $\hat{\mathcal{H}}$ :

$$
\begin{equation*}
|\psi\rangle=\sum_{l=0}^{2^{N}-1} c_{l}\left|E_{l}\right\rangle \tag{14.31}
\end{equation*}
$$

Since all the operations we have carried on in the quantum phase estimation are linear, it is not hard to convince one-self that if we apply the controlled time evolutions to an approximate state we get

$$
\begin{array}{r}
\frac{1}{\sqrt{2^{n}}} \sum_{l=0}^{2^{N}-1} c_{l}\left(|0\rangle+e^{-i E_{l} t}|1\rangle\right) \otimes\left(|0\rangle+e^{-i 2 E_{l} t}|1\rangle\right) \otimes \cdots \otimes\left(|0\rangle+e^{-i 2^{n-1} E_{l} t}|1\rangle\right) \otimes\left|E_{l}\right\rangle= \\
=\frac{1}{\sqrt{2^{n}}} \sum_{l=0}^{2^{N}-1} \sum_{k=0}^{2^{n}-1} c_{l} e^{-i\left(E_{l} t\right) k}|k\rangle\left|E_{l}\right\rangle . \tag{14.32}
\end{array}
$$

Further applying the inverse Fourier transform to this state then will return frequencies that correspond to the exact eigen-energies of the Hamiltonian! The intensity of these peaks will be proportional to the coefficients $\left|c_{l}\right|^{2}$. We therefore see that if we have access to a reasonable approximation of the ground state $|\psi\rangle$ such that its overlap with the exact ground state is not exponentially small, then by performing quantum phase estimation over such state will give us the exact energies of the system. In this sense, $\mathrm{QPE}$ is a very powerful technique. The important caveat, however, is that in general it is not easy to prepare a simple state $|\psi\rangle$ that has a sizable overlap with the exact ground state. In general, finding such an initial state is an exponentially hard task, however we will analyze strategies to do so in the next lecture.


[^0]:    ${ }^{1}$ The notation poly $(x)$ indicates an effort that is polynomial in $x$.

