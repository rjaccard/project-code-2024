## Variational Quantum Algorithms

### 15.1 Variational State Preparation

Here we describe approaches that aim at preparing a quantum state with a variational approach on a quantum computer. This general family of algorithms is based on variational principles and intrinsically demands a hybrid classical-quantum approach, as we will see in the following.

Generally speaking, the idea of these methods is to reformulate the task of preparing a certain quantum state as a carefully chosen optimization problem.

In the general setting we have three main ingredients:

1. A parameterized quantum circuit (sometimes also improperly called quantum neural networks), consisting of a sequence of unitaries parameterize by some $\theta=\left(\theta_{1} \ldots \theta_{l}\right)$. In the following we assume the form

$$
\begin{equation*}
\hat{U}(\theta)=\hat{U}_{l}\left(\theta_{l}\right) \ldots \hat{U}_{2}\left(\theta_{2}\right) \hat{U}_{1}\left(\theta_{1}\right) \tag{15.1}
\end{equation*}
$$

thus preparing a family of variational states

$$
\begin{equation*}
|\Psi(\theta)\rangle=\hat{U}(\theta)|0\rangle \tag{15.2}
\end{equation*}
$$

2. A "loss function" that is representative of the task one wants to solve. The choice of the loss function is problem dependent, however in several applications it takes the form of an expectation value of an Hermitean operator $B$

$$
\begin{equation*}
\mathcal{L}(\theta)=\left\langle 0\left|\hat{U}^{\dagger}(\theta) \hat{B} \hat{U}(\theta)\right| 0\right\rangle \tag{15.3}
\end{equation*}
$$

and the best variational approximations coincides with the set of parameters that minimize the loss function.

3. A classical optimizer, that uses suitable measurements from the quantum computer in order to find a good approximation for the minimum of the loss function, i.e.

$$
\begin{equation*}
\bar{\theta}=\operatorname{argmin}_{\theta} \mathcal{L}(\theta) \tag{15.4}
\end{equation*}
$$

### 15.2 Loss Functions

We now present several interesting problems in physics, chemistry, and mathematics that can be formulated through a variational approach. The main conceptual requirement in this phase is rewriting the specific problem at hand as a suitable optimization problem, for which it is therefore important to:

1. Identity a suitable loss function $\mathcal{L}(\theta)$ such that, in the ideal case, the state $|\Psi(\bar{\theta})\rangle$ prepares the given target quantum state;
2. Make sure that the loss function is efficiently measurable on quantum hardware;
3. Make sure that sufficient progress is made in optimizing the loss.

### 15.2.1 Ground-State Preparation

In the context of quantum simulation, a very important task is preparing the ground state of a given hamiltonian, $\hat{\mathcal{H}}$. In this case, the most natural loss function for state preparation is the total energy of the quantum system:

$$
\begin{equation*}
E(\theta)=\left\langle 0\left|\hat{U}^{\dagger}(\theta) \hat{\mathcal{H}} \hat{U}(\theta)\right| 0\right\rangle \tag{15.5}
\end{equation*}
$$

From the variational principle of quantum mechanics we know that

$$
\begin{equation*}
E(\theta) \geq E_{0} \tag{15.6}
\end{equation*}
$$

where $E_{0}$ is the exact ground state energy. Thus by minimizing $E(\theta)$ we seek to approximate the ground state of a given Hamiltonian using a fixed-depth quantum circuit. This algorithm is known as the Variational Quantum Eigensolver (VQE).

In practical applications, one is interested in Hamiltonians that are sum of local operators, most prominently taking the form of sum of "Pauli strings" :

$$
\begin{equation*}
\hat{\mathcal{H}}=\sum_{k} c_{k} \hat{A}_{k, 1} \hat{A}_{k, 2} \ldots \hat{A}_{k, N} \tag{15.7}
\end{equation*}
$$

with the coefficients $c_{k} \in \mathbb{R}$ and $A_{k, i} \in[I, X, Y, Z]$. To measure the total energy $E(\theta)$ then a simple approach is to measure the Pauli strings

$$
\begin{equation*}
\hat{P}_{k}=\hat{A}_{k, 1} \hat{A}_{k, 2} \ldots \hat{A}_{k, N} \tag{15.8}
\end{equation*}
$$

in the $\sigma^{z}$ computational basis, after a suitable basis rotation.

To give a concrete example, imagine that we would like to find the ground state of our best friend, the Transverse Field Ising Model (TFIM) :

$$
\begin{equation*}
\hat{\mathcal{H}}=-\Gamma \sum_{i} \hat{X}_{i}+\sum_{\langle i, j\rangle} J_{i j} \hat{Z}_{i} \hat{Z}_{j} \tag{15.9}
\end{equation*}
$$

In this case, to estimate the expectation value of the energy we need to measure for example $P_{k}=\hat{X}_{k}$. This can be done noticing that

$$
\begin{equation*}
\left\langle\hat{X}_{k}\right\rangle=\left\langle 0\left|\hat{U}^{\dagger}(\theta) \hat{H}_{k} \hat{Z}_{k} \hat{H}_{k} \hat{U}(\theta)\right| 0\right\rangle \tag{15.10}
\end{equation*}
$$

where we do a simple basis rotation through the Hadamard gate:

$$
\hat{H}=\frac{1}{\sqrt{2}}\left(\begin{array}{cc}
1 & 1 \\
1 & -1
\end{array}\right)
$$

In conclusion, all the terms of the energy that include the transverse field parts can be simply measured by collecting the output of the circuit depicted in Fig. 15.1.

![](https://cdn.mathpix.com/cropped/2024_05_17_e75ce80bb96efbd36cd0g-03.jpg?height=346&width=494&top_left_y=661&top_left_x=764)

Figure 15.1: Example of circuit to measure $\sum_{k}\left\langle\hat{X}_{k}\right\rangle$ on the variational state.

The accuracy of this estimate will depend on the number of measurements (or shots) taken, $N_{s}$, with a statistical error decreasing like $1 / \sqrt{N_{s}}$.

### 15.2.2 Excited States

There have been a few proposals of cost functions to find excited states of a given Hamiltonian. It is fair to say that this is still a matter of research activity, thus we sketch here only the conceptually simplest approach (albeit not necessarily a very efficient one). The idea is to first prepare an approximation of the ground state, such that $\left|\Psi\left(\bar{\theta}_{0}\right)\right\rangle \simeq\left|\Psi_{0}\right\rangle$, then one considers the cost function

$$
\begin{equation*}
E_{1}(\theta, \lambda)=\left\langle 0\left|\hat{U}^{\dagger}(\theta) \hat{\mathcal{H}} \hat{U}(\theta)\right| 0\right\rangle+\lambda\left|\left\langle\Psi\left(\overline{\theta_{0}}\right)|\hat{U}(\theta)| 0\right\rangle\right|^{2} \tag{15.11}
\end{equation*}
$$

where we have introduced a Lagrange multiplier $\lambda$, such that the resulting state $\left|\Psi\left(\theta_{1}^{\star}\right)\right\rangle=$ $\hat{U}\left(\theta_{1}^{\star}\right)|0\rangle$ will be state of lowest energy that is also orthogonal to the given approximation of the ground state, i.e. $\left\langle\Psi\left(\bar{\theta}_{0}\right) \mid \Psi\left(\overline{\theta_{1}}\right)\right\rangle=0$. The first term in this cost function can be estimated as much as in standard VQE, whereas the second term can be estimated noticing that

$$
\begin{equation*}
\left|\left\langle\Psi\left(\overline{\theta_{0}}\right)|\hat{U}(\theta)| 0\right\rangle\right|^{2}=\left|\left\langle 0\left|\hat{U}^{\dagger}\left(\overline{\theta_{0}}\right) \hat{U}(\theta)\right| 0\right\rangle\right|^{2} \tag{15.12}
\end{equation*}
$$

is the probability of measuring $|0\rangle$ after having prepared the state

$$
\begin{equation*}
|\Phi\rangle=\hat{U}^{\dagger}\left(\overline{\theta_{0}}\right) \hat{U}(\theta)|0\rangle \tag{15.13}
\end{equation*}
$$

thus requiring a doubling of the circuit depth, as shown in Figure 15.2.

![](https://cdn.mathpix.com/cropped/2024_05_17_e75ce80bb96efbd36cd0g-04.jpg?height=361&width=864&top_left_y=245&top_left_x=653)

Figure 15.2: Example circuit to measure the overlap between two parameterized circuits.

### 15.3 Parameterized Quantum Circuits

Here we give a few example of the specific form that parameterized quantum circuits can take, especially in the context of ground state problems. In order to get some insight, it is useful first to recall how, at least in principle, one can prepare the ground state of a given Hamiltonian using purely unitary time evolution.

### 15.3.1 Ground states through adiabatic state preparation

Adiabatic state preparation is based on the quantum adiabatic theorem. We assume that at $t=0$ we start in the ground state $\left|\psi_{0}(t)\right\rangle$ of some time-dependent Hamiltonian $\hat{\mathcal{H}}(t)$. If we change the Hamiltonian $\hat{\mathcal{H}}(t)$ adiabatically slowly we will remain in the ground state $\left|\psi_{0}(t)\right\rangle$ of $\hat{\mathcal{H}}(t)$ for all times $t>0$. This opens a way to prepare the ground state of a quantum system. Let us start at time $t=0$ in a Hamiltonian $\hat{\mathcal{H}}_{0}$ of which we can easily compute the ground state. In order to find the ground state of an unknown Hamiltonian $\hat{\mathcal{H}}{ }_{f}$ we adiabatically interpolate between $\hat{\mathcal{H}}$ and $\hat{\mathcal{H}}_{f}$ to arrive at the desired Hamiltonian at time $t_{f}$ :

$$
\begin{equation*}
\hat{\mathcal{H}}(t)=\left(1-\frac{t}{t_{f}}\right) \hat{\mathcal{H}}_{0}+\frac{t}{t_{f}} \hat{\mathcal{H}}_{f} . \tag{15.14}
\end{equation*}
$$

Instead of this linear interpolation any other function can be chosen as long as $\hat{\mathcal{H}}(0)=$ $\hat{\mathcal{H}}_{0}$ and $\hat{\mathcal{H}}\left(t_{f}\right)=\hat{\mathcal{H}}_{f}$. If we choose $t_{f}$ long enough we are guaranteed to end up in the ground state with only exponentially small errors.

What is meant by "long enough"? The quantum adiabatic theorem states that this time should be much longer than a scale set by the minimum gap:

$$
\begin{equation*}
t_{f} \gg \mathcal{O}\left(\min _{t} \Delta(t)^{-2}\right) \tag{15.15}
\end{equation*}
$$

where the gap

$$
\begin{equation*}
\Delta(t)=E_{1}(t)-E_{0}(t) \tag{15.16}
\end{equation*}
$$

is the difference between the ground state energy $E_{0}(t)$ and the energy of the first excited state $E_{1}(t)$. Since in practice we know neither the minimum gap of the unknown quantum system, nor the constants that go into this inequality, we will have to perform numerical experiments on our (quantum) computer to determine when the results start to converge as a function of $t_{f}$. It is important to remark that for generic physical
hamiltonians we expect the time $t_{f} \sim \exp (N)$, as a result of exponentially closing gap during the adiabatic state preparation. There is no known classical or quantum algorithm that can efficiently prepare the ground state of a generic physical hamiltonian in polynomial time, and the adiabatic algorithm is no exception.

### 15.3.2 Quantum alternating operator

The adiabatic state preparation gives a hint at what kind of ansatz we can take to study ground state problems. Let us consider the case in which the time-dependent Hamiltonian takes the generic form

$$
\begin{equation*}
\hat{\mathcal{H}}(t)=\sum_{s}^{M} \hat{\mathcal{H}}_{s}(t) \tag{15.17}
\end{equation*}
$$

where the terms $\left[\hat{\mathcal{H}}_{s}, \hat{\mathcal{H}}_{s^{\prime}}\right] \neq 0$ in general but are chosen in a way that each $\mathcal{H}_{s}$ contains all terms mutually commuting. In general each term can contain both parts of $\hat{\mathcal{H}}_{0}$ and $\hat{\mathcal{H}}_{f}$.

In order to implement the adiabatic preparation algorithm on a quantum computer, we need to write the time evolution induced by the Hamiltonian in terms of gates. A simple approach would be to consider a small time step $\delta_{t}$ such that

$$
\begin{equation*}
|\Psi(t)\rangle \simeq \Pi_{p}^{\left[t / \delta_{t}\right]} e^{-i \delta_{t} \hat{\mathcal{H}}\left(p \delta_{t}\right)}|\Psi(0)\rangle \tag{15.18}
\end{equation*}
$$

Then the small time-step propagators are written in terms of a Trotter decomposition, such that

$$
\begin{equation*}
|\Psi(t)\rangle \simeq \Pi_{p}^{\left[t / \delta_{t}\right]} e^{-i \delta_{t} \hat{\mathcal{H}}_{1}\left(p \delta_{t}\right)} e^{-i \delta_{t} \hat{\mathcal{H}}_{2}\left(p \delta_{t}\right)} \ldots e^{-i \delta_{t} \hat{\mathcal{H}}_{M}\left(p \delta_{t}\right)}|\Psi(0)\rangle \tag{15.19}
\end{equation*}
$$

To give a concrete example, imagine that we would like to find the ground state of the Transverse Field Ising Model :

$$
\begin{equation*}
\hat{\mathcal{H}}_{f}=\sum_{\langle i, j\rangle} J_{i j} \hat{Z}_{i} \hat{Z}_{j}+\Gamma \sum_{i} \hat{X}_{i} \tag{15.20}
\end{equation*}
$$

In this case, we can define $\hat{\mathcal{H}}_{0}=\Gamma \sum_{i} \hat{X}_{i}$, such that the ground state of this part, $\left|\psi_{0}(0)\right\rangle$, is easily prepared as a product state.

We split the Hamiltonian into $M=2$ non-commuting terms, the classical Ising interaction

$$
\begin{equation*}
\hat{\mathcal{H}}_{z z}=\sum_{\langle i, j\rangle} J_{i j} \hat{Z}_{i} \hat{Z}_{j} \tag{15.21}
\end{equation*}
$$

and the transverse field term

$$
\begin{equation*}
\hat{\mathcal{H}}_{x}=\Gamma \sum_{i} \hat{X}_{i} \tag{15.22}
\end{equation*}
$$

such that

$$
\begin{align*}
\hat{\mathcal{H}}(t) & =\left(1-\frac{t}{t_{f}}\right) \hat{\mathcal{H}}_{x}+\frac{t}{t_{f}}\left(\hat{\mathcal{H}}_{x}+\hat{\mathcal{H}}_{z z}\right)  \tag{15.23}\\
& =\hat{\mathcal{H}}_{x}+\frac{t}{t_{f}} \hat{\mathcal{H}}_{z z}  \tag{15.24}\\
& =\hat{\mathcal{H}}_{1}(t)+\hat{\mathcal{H}}_{2}(t) . \tag{15.25}
\end{align*}
$$

Each of these terms, when exponentiated, correspond to local unitaries. Since the Ising term gives a product of two-local unitaries that are diagonal in the computational basis

$$
\begin{equation*}
e^{-i \hat{\mathcal{H}}_{2}(t) \delta_{t}}=e^{-i \delta_{t} \frac{t}{t_{f}} \sum_{\langle i, j\rangle} J_{i j} \hat{\mathcal{Z}}_{i} \hat{Z}_{j}}=\prod_{\langle i, j\rangle} e^{-i\left(\delta_{t} \frac{t}{t_{f}}\right) J_{i j} \hat{\bar{Z}}_{i} \hat{Z}_{j}} \tag{15.26}
\end{equation*}
$$

The transverse field term splits into $N$ commuting terms for each of the spins:

$$
\begin{equation*}
e^{-i \hat{\mathcal{H}}_{1}(t) \delta_{t}}=e^{-i \delta_{t} \Gamma \sum_{i} \hat{X}_{i}}=\prod_{i} e^{-i \delta_{t} \Gamma \hat{X}_{i}} \tag{15.27}
\end{equation*}
$$

The time evolution under the transverse field term $e^{-i \delta_{t} \Gamma \hat{X}_{i}}$ is trivial to implement, since it is just a rotation around the $x$ axis, implemented by an RX gate, depicted in Fig. 15.3 .

$$
-\mathrm{Rx}\left(2 \delta_{t} \Gamma\right)
$$

Figure 15.3: Simple rotation gate realizing $e^{-i \delta_{t} \Gamma \hat{X}_{i}}$

The Ising term is a 2 -spin coupling and thus requires a 2 -qubit gate. To implement $e^{-i\left(\delta_{t} \frac{t}{t_{f}}\right) J_{i j} \hat{Z}_{i} \hat{Z}_{j}}$ one needs to rotate by an angle $\Phi_{i j}(t)=-\delta_{t} J_{i j} t / t_{f}$ if the two spin values are the same and $-\Phi_{i j}(t)$ if they differ. The circuit in Fig. 15.4 can realize this operation.

![](https://cdn.mathpix.com/cropped/2024_05_17_e75ce80bb96efbd36cd0g-06.jpg?height=174&width=625&top_left_y=1532&top_left_x=770)

Figure 15.4: Circuit realizing $\mathrm{RZZ}=e^{-i\left(\delta_{t} \frac{t}{t_{f}}\right) J_{i j} \hat{\mathcal{Z}}_{i} \hat{\mathcal{Z}}_{j}}$.

The resulting unitary preparing $|\psi(t)\rangle$ is then schematically shown in Figure 15.5.

![](https://cdn.mathpix.com/cropped/2024_05_17_e75ce80bb96efbd36cd0g-06.jpg?height=414&width=777&top_left_y=1975&top_left_x=705)

Figure 15.5: Circuit realizing the first Trotter step of adiabatic time evolution for the Transverse-Field Ising model.

It can be noticed that this circuit is not parametric, since all the gates are fixed. The main idea of QAOA/Hamiltonian Variational ansatz is to make these gates parametric:

$$
\begin{equation*}
|\Psi(\theta)\rangle=\Pi_{s, p} e^{-i \hat{\mathcal{H}}_{p} \theta_{s p}}\left|\Psi_{0}\right\rangle \tag{15.28}
\end{equation*}
$$

A nice way of interpreting this is in terms of a time evolution that can possibly break the adiabatic condition but that can in principle prepare the state faster (i.e. with a short circuit, as compared with the adiabatic state preparation that would take very deep circuits).

### 15.3.3 Hardware Efficient Ansatz

In addition to ansatz wave functions inspired by the adiabatic state preparation, another possible (and popular) choice is to to take parameterized circuits that are not necessarily physically motivated but that at least can be implemented efficiently on existing quantum hardware. Typically, this family of states takes the form

$$
\begin{equation*}
|\Psi(\theta)\rangle=\Pi_{k} \hat{U}_{k}\left(\theta_{k}\right) \hat{W}_{k}|0\rangle \tag{15.29}
\end{equation*}
$$

where the gates $\hat{W}_{k}$ are fixed and do not carry a variational parameter to be optimized. In several applications, for example, only single-qubit gates are parameterized and a fixed set of two-qubit gates, $\hat{W}_{k}$, are positioned on qubit edges that are consistent with the physical connectivity of the devices.

### 15.4 Optimization Algorithms

Here we discuss optimization strategies based on gradients. To make our discussion more concrete, we focus again on parameterized states

$$
\begin{equation*}
|\Psi(\theta)\rangle=\hat{U}_{l}\left(\theta_{l}\right) \ldots \hat{U}_{2}\left(\theta_{2}\right) \hat{U}_{1}\left(\theta_{1}\right)|0\rangle \tag{15.30}
\end{equation*}
$$

and loss functions of the form

$$
\begin{equation*}
\mathcal{L}(\theta)=\langle\Psi(\theta)|\hat{B}| \Psi(\theta)\rangle \tag{15.31}
\end{equation*}
$$

where $B$ is some hermitean operator. We have seen in the previous discussion that several of the loss functions of interest can be written in this form.

In their simplest setting, gradient-based hybrid optimization algorithms do the following iterative procedure do minimize the loss function:

1. At iteration $i$, use the quantum computer to estimate $\mathcal{L}\left(\theta^{(i)}\right)$ with the current set of variational parameters $\theta^{(i)}$ and the components of the gradient, $G_{k}\left(\theta^{(i)}\right)=$ $\partial_{\theta_{k}} \mathcal{L}\left(\theta^{(i)}\right)$
2. Update the variational parameters according, for example, to a gradient descent step $\theta_{k}^{(i+1)}=\theta_{k}^{(i)}-\eta G_{k}\left(\theta^{(i)}\right)$, where $\eta$ is a small constant, known as the "learning rate", following standard machine learning terminology
3. Quit when converged to a minimum of the loss function.

### 15.4.1 Parameter Shift Rule

For specific applications, we have already seen how to compute the loss function efficiently, using measurements in the computational basis. We now describe also an efficient strategy, known in literature as the parameter shift rule, to estimate the gradient of the loss function. More details can be bound in Ref. [2].

For simplicity, we restrict ourselves to unitaries of the form

$$
\begin{equation*}
\hat{U}_{k}\left(\theta_{k}\right)=e^{-i \hat{S}_{k} \frac{\theta_{k}}{2}} \tag{15.32}
\end{equation*}
$$

where the operator $S_{k}$ is taken to be involutory, i.e. satisfying $S_{k}^{2}=\mathbb{I}$. Notice that this family of gates is quite general and encompasses for example all single qubit rotations generated by pauli operators, i.e. $S_{k} \in(X, Y, Z)$ as well as several two-qubit gates acting on qubits $i$ and $j$ such that $S_{k} \in\left(X_{i} X_{j}, Y_{i} Y_{j}, \ldots\right)$. Because of the involutory property, it is easy to verify that

$$
\begin{align*}
\hat{U}_{k}\left(\theta_{k}\right)= & \hat{I}-i \hat{S}_{k} \frac{\theta_{k}}{2}-\frac{1}{2!} \hat{S}_{k}^{2}\left(\frac{\theta_{k}}{2}\right)^{2}+\frac{i}{3!} \hat{S}_{k}^{3}\left(\frac{\theta_{k}}{2}\right)^{3}+\ldots  \tag{15.33}\\
= & {\left[1-\frac{1}{2!}\left(\frac{\theta_{k}}{2}\right)^{2}+\frac{1}{4!}\left(\frac{\theta_{k}}{2}\right)^{4}+\ldots\right] \hat{I}+}  \tag{15.34}\\
& -i \hat{S}_{k}\left[\frac{\theta_{k}}{2}-\frac{1}{3!}\left(\frac{\theta_{k}}{2}\right)^{3}+\frac{1}{5!}\left(\frac{\theta_{k}}{2}\right)^{5}+\ldots\right]  \tag{15.35}\\
= & \cos \left(\frac{\theta_{k}}{2}\right) \hat{I}-i \sin \left(\frac{\theta_{k}}{2}\right) \hat{S}_{k} \tag{15.36}
\end{align*}
$$

we also notice that the unitary conjugation of an arbitrary operator can be written as

$$
\begin{align*}
\hat{K}\left(\theta_{k}\right) & =\hat{U}_{k}^{\dagger}\left(\theta_{k}\right) \hat{K} \hat{U}_{k}\left(\theta_{k}\right)  \tag{15.37}\\
& =\hat{A}+\hat{B} \cos \left(\theta_{k}\right)+\hat{C} \sin \left(\theta_{k}\right) \tag{15.38}
\end{align*}
$$

where the operators $\hat{A}, \hat{B}, \hat{C}$ do not depend on the parameter. This last property is especially interesting for us, since the derivative is now easily found:

$$
\begin{align*}
\partial_{\theta_{k}} \hat{K}\left(\theta_{k}\right) & =-\hat{B} \sin \left(\theta_{k}\right)+\hat{C} \cos \left(\theta_{k}\right)  \tag{15.39}\\
& =\frac{\hat{K}\left(\theta_{k}+\pi / 2\right)-\hat{K}\left(\theta_{k}-\pi / 2\right)}{2} \tag{15.40}
\end{align*}
$$

Now, let us define $\hat{U}(\theta)=\hat{V}_{k} \hat{U}_{k}(\theta) \hat{W}_{k}$, where the operators $\hat{V}_{k}$ and $\hat{W}_{k}$ do not depend explicitly on the parameter $\theta_{k}$ but can depend on all the other parameters. With this
definition, we can write the derivative of the loss explicitly

$$
\begin{align*}
\partial_{\theta_{k}} \mathcal{L}\left(\theta_{1}, \ldots, \theta_{k}, \ldots \theta_{l}\right)= & \partial_{\theta_{k}}\left\langle 0\left|\hat{W}_{k}^{\dagger} \hat{U}_{k}^{\dagger}\left(\theta_{k}\right) \hat{V}_{k}^{\dagger} \hat{B} \hat{V}_{k} \hat{U}_{k}\left(\theta_{k}\right) \hat{W}_{k}\right| 0\right\rangle  \tag{15.41}\\
= & \partial_{\theta_{k}}\left\langle\Psi_{k}\left|\hat{U}_{k}^{\dagger}\left(\theta_{k}\right) \hat{Q}_{k} \hat{U}_{k}\left(\theta_{k}\right)\right| \Psi_{k}\right\rangle  \tag{15.42}\\
= & \partial_{\theta_{k}}\left\langle\Psi_{k}\left|\hat{Q}_{k}\left(\theta_{k}\right)\right| \Psi_{k}\right\rangle  \tag{15.43}\\
= & \frac{1}{2}\left\{\left\langle\Psi_{k}\left|\hat{U}_{k}\left(\theta_{k}+\frac{\pi}{2}\right)^{\dagger} \hat{Q}_{k} \hat{U}_{k}\left(\theta_{k}+\frac{\pi}{2}\right)\right| \Psi_{k}\right\rangle+\right.  \tag{15.44}\\
& \left.-\left\langle\Psi_{k}\left|\hat{U}_{k}\left(\theta_{k}-\frac{\pi}{2}\right)^{\dagger} \hat{Q}_{k} \hat{U}_{k}\left(\theta_{k}-\frac{\pi}{2}\right)\right| \Psi_{k}\right\rangle\right\}  \tag{15.45}\\
= & \frac{\mathcal{L}\left(\theta_{1}, \ldots, \theta_{k}+\frac{\pi}{2}, \ldots \theta_{l}\right)-\mathcal{L}\left(\theta_{1}, \ldots, \theta_{k}-\frac{\pi}{2}, \ldots \theta_{l}\right)}{2}
\end{align*}
$$

This formula is very interesting because it tells us that the gradient can be computed just as the difference of two loss functions, thus it can be estimated just as done for the loss function itself.

### 15.5 Qubits Encodings

### 15.5.1 Fermions

Quantum computers intrinsically operate with spin degrees of freedom, since in the standard model of quantum computation basis states are eigenstates $|\uparrow\rangle,|\downarrow\rangle$ of the $\sigma^{z}$ operator,

$$
\begin{align*}
& |\uparrow\rangle \equiv|0\rangle  \tag{15.47}\\
& |\downarrow\rangle \equiv|1\rangle \tag{15.48}
\end{align*}
$$

In Nature however particles can obey to different statistics, most notably interacting fermionic matter plays a crucial role in the determination of chemical and physical properties of materials, molecules and much more.

When studying electronic problems with variational quantum algorithms, it is then necessary to map these fermionic degrees of freedom into qubits. When doing exact diagonalization of fermions, we have faced exactly the same problem, when me mapped fermions onto spins. In general, we consider electronic Hamiltonians defined in terms of the usual fermionic operators $\hat{c}_{i}^{\dagger}$ and $\hat{c}_{i}$ satisfying the anti-commutation relations

$$
\begin{equation*}
\left\{\hat{c}_{l}^{\dagger}, \hat{c}_{m}\right\}=\delta_{l m} \hat{I} \tag{15.49}
\end{equation*}
$$

The Jordan-Wigner mapping is one of the main (and the oldest) strategies to "convert" these fermionic operators into spins. This is achieved through the following transformation

$$
\begin{align*}
\hat{c}_{l} & =\left(\Pi_{j=1}^{l-1} \hat{Z}_{j}\right) \hat{\sigma}_{l}^{-}  \tag{15.50}\\
\hat{c}_{l}^{\dagger} & =\left(\Pi_{j=1}^{l-1} \hat{Z}_{j}\right) \hat{\sigma}_{l}^{+} \tag{15.51}
\end{align*}
$$

with the usual raising and lowering spin operators

$$
\begin{align*}
& \hat{\sigma}_{l}^{+}=\frac{\hat{X}_{l}+i \hat{Y}_{l}}{2}  \tag{15.52}\\
& \hat{\sigma}_{l}^{-}=\frac{\hat{X}_{l}-i \hat{Y}_{l}}{2} \tag{15.53}
\end{align*}
$$

that satisfy

$$
\begin{equation*}
\left\{\hat{\sigma}_{l}^{+}, \hat{\sigma}_{l}\right\}=\hat{I} \tag{15.54}
\end{equation*}
$$

It can be verified that the fermionic operators defined through the mapping satisfy the required commutation relations, for example

$$
\begin{align*}
\left\{c_{l}^{\dagger}, c_{l}\right\} & =\left\{\left(\Pi_{j=1}^{l-1} \hat{Z}_{j}\right) \hat{\sigma}_{l}^{+},\left(\Pi_{j=1}^{l-1} \hat{Z}_{j}\right) \hat{\sigma}_{l}^{-}\right\}  \tag{15.55}\\
& =\left(\Pi_{j=1}^{l-1} \hat{Z}_{j}\right)^{2}\left\{\hat{\sigma}_{l}^{+}, \hat{\sigma}_{l}\right\}  \tag{15.56}\\
& =\left(\Pi_{j=1}^{l-1} \hat{Z}_{j}\right)^{2} \tag{15.57}
\end{align*}
$$

and the last term is nothing but the identity, since Pauli matrices square to one, thus $\left(\Pi_{j=1}^{l-1} \hat{Z}_{j}\right)^{2}=\Pi_{j=1}^{l-1}\left(\hat{Z}_{j}\right)^{2}=\hat{I}$.

With this mapping at hand, it is clear that we can write arbitrary fermionic hamiltonians in the form of sum of Pauli strings, and we can use all the techniques discussed above for spin/qubits hamiltonians.

