## Time-Dependent Variational Principle

### 10.1 Time-Dependent Variational States

The main goal of time-dependent variational methods is to find the optimal (in a sense to be clarified in the following) description of the time evolution of a state, in terms of a variational state. In practice, we consider a variational state whose parameters, $\boldsymbol{\theta}(t)$, explicitly depend on time $t$, and such that

$$
\begin{equation*}
|\psi[\boldsymbol{\theta}(t)]\rangle \simeq|\phi(t)\rangle \tag{10.1}
\end{equation*}
$$

where the state $|\phi(t)\rangle$ is the exact solution to the time-dependent Schrödinger's equation:

$$
\begin{equation*}
i \frac{\partial}{\partial t}|\phi(t)\rangle=\hat{H}|\phi(t)\rangle \tag{10.2}
\end{equation*}
$$

Notice that here we are taking the case of a time-independent Hamiltonian for simplicity, but the discussion of this Chapter can be readily generalized to time-dependent Hamiltonians as well.

In order to make progress in this problem, we can imagine that we start our exact dynamics at time $t$, from the current variational state, and consider a small time step:

$$
\begin{align*}
\left|\phi\left(t+\delta_{t}\right)\right\rangle & =|\phi(t)\rangle-i \hat{H} \delta_{t}|\phi(t)\rangle+\mathcal{O}\left(\delta_{t}^{2}\right)  \tag{10.3}\\
& =|\psi[\boldsymbol{\theta}(t)]\rangle-i \hat{H} \delta_{t}|\psi[\boldsymbol{\theta}(t)]\rangle+\mathcal{O}\left(\delta_{t}^{2}\right) \tag{10.4}
\end{align*}
$$

On the other hand, since we have assumed that the variational parameters have a time dependence, we have that

$$
\begin{equation*}
\left|\psi\left(\left[\boldsymbol{\theta}\left(t+\delta_{t}\right)\right]\right)\right\rangle=|\psi[\boldsymbol{\theta}(t)]\rangle+\delta_{t} \sum_{k} \dot{\theta}_{k}(t) \partial_{\theta_{k}}|\psi[\boldsymbol{\theta}(t)]\rangle \tag{10.5}
\end{equation*}
$$

In order for the variational state to be as close as possible to the exact dynamics, we then need that

$$
\begin{equation*}
\left|\psi\left[\boldsymbol{\theta}\left(t+\delta_{t}\right)\right]\right\rangle \simeq\left|\phi\left(t+\delta_{t}\right)\right\rangle \tag{10.6}
\end{equation*}
$$

There several ways to impose that Equation (10.6) is approximately verified, giving rise to different time-dependent variational principles. In this Lecture, we consider the variational principle due to McLachlan, that amounts to maximize the distance between the two states appearing on the left and on the right hand side in the equation above.

We can start by considering the distance between the vector changes to the original quantum state:

$$
\begin{equation*}
\left.\Delta^{2}=\left|\delta_{t} \sum_{k} \dot{\theta}_{k}(t) \partial_{\theta_{k}}\right| \psi[\boldsymbol{\theta}(t)]\right\rangle+\left.i \delta_{t} \hat{H}|\psi(\boldsymbol{\theta})\rangle\right|^{2} \tag{10.7}
\end{equation*}
$$

This quantity is exactly zero if the time-dependent Schroedinger equation is satisfied exactly by the variational state. In general this is not exactly satisfied, but we can minimize $\Delta^{2}$ to obtain the best possible variational state that most closely matches the exact dynamics. Since $\Delta^{2}$ is an explicit function of $\dot{\theta}_{k}(t)$, we can proceed to minimizing it by computing its gradient:

$$
\begin{align*}
\frac{\Delta^{2}}{\delta_{t}^{2}}= & \left.\left|\sum_{k} \dot{\theta}_{k}\right| \partial_{\theta_{k}} \psi\right\rangle+\left.i \hat{H}|\psi\rangle\right|^{2}  \tag{10.8}\\
= & \sum_{k, k^{\prime}} \dot{\theta}_{k} \dot{\theta}_{\hat{k}^{\prime}}\left\langle\partial_{\theta_{k^{\prime}}} \psi \mid \partial_{\theta_{k}} \psi\right\rangle-i \sum_{k} \dot{\theta}_{k}\left\langle\psi|H| \partial_{\theta_{k}} \psi\right\rangle+i \sum_{k} \dot{\theta}_{k}\left\langle\partial_{\theta_{k}} \psi|H| \psi\right\rangle+ \\
& +\left\langle\psi\left|\hat{H}^{2}\right| \psi\right\rangle \tag{10.9}
\end{align*}
$$

thus

$$
\begin{equation*}
\frac{\partial}{\partial \theta_{k}} \frac{\Delta^{2}}{\delta_{t}^{2}}=\sum_{k^{\prime}} \dot{\theta}_{k^{\prime}}\left\langle\partial_{\theta_{k^{\prime}}} \psi \mid \partial_{\theta_{k}} \psi\right\rangle-i\left\langle\psi|H| \partial_{\theta_{k}} \psi\right\rangle+\text { c.c. } \tag{10.10}
\end{equation*}
$$

with the stationary point given by

$$
\begin{align*}
\left.\sum_{k^{\prime}} \dot{\theta}_{k^{\prime}} \operatorname{Re}\left[\left\langle\partial_{\theta_{k}} \psi \mid \partial_{\theta_{k^{\prime}}}\right\rangle\right\rangle\right] & =-\operatorname{Re}\left[i\left\langle\partial_{\theta_{k}} \psi|H| \psi\right\rangle\right]  \tag{10.11}\\
& =\operatorname{Im}\left\langle\partial_{\theta_{k}} \psi|H| \psi\right\rangle \tag{10.12}
\end{align*}
$$

In addition to minimizing this distance, we should also enforce that the resulting state conserves the normalization, since the dynamics is unitary. In practice, this can be either done by adding a suitable Lagrange multiplier, or by considering a variational parameter that takes into account the normalization of the state:

$$
\begin{equation*}
|\bar{\psi}(t)\rangle=e^{\theta_{0}(t)}|\psi(t)\rangle \tag{10.13}
\end{equation*}
$$

I leave as an exercise to shown that this leads to

$$
\begin{equation*}
\sum_{k^{\prime}} S_{k k^{\prime}}^{R} \dot{\theta}_{k^{\prime}}(t)=C_{k}^{I} \tag{10.14}
\end{equation*}
$$

with the superscript $R$ and $I$ denoting the real and imaginary part, respectively, of the following quantities:

$$
\begin{align*}
C_{k} & =\frac{\left\langle\partial_{\theta_{k}} \psi|\hat{H}| \psi\right\rangle}{\langle\psi \mid \psi\rangle}-\frac{\left\langle\partial_{\theta_{k}} \psi \mid \psi\right\rangle}{\langle\psi \mid \psi\rangle} \frac{\langle\psi|\hat{H}| \psi\rangle}{\langle\psi \mid \psi\rangle}  \tag{10.15}\\
S_{k k^{\prime}} & =\frac{\left.\left\langle\partial_{\theta_{k}} \psi \mid \partial_{\theta_{k^{\prime}}},\right\rangle\right\rangle}{\langle\psi \mid \psi\rangle}-\frac{\left.\left\langle\partial_{\theta_{k}} \psi \mid \psi\right\rangle\left\langle\psi \mid \partial_{\theta_{k^{\prime}}},\right\rangle\right\rangle}{\langle\psi \mid \psi\rangle^{2}} \tag{10.16}
\end{align*}
$$

The latter quantity is also known in literature as the "quantum geometric tensor" and plays a fundamental role in setting the metric of associated with variational states.

### 10.2 Imaginary-time evolution

Up to now, we have considered solutions to the "standard" time-dependent Schrödinger equation, for the evolution of a quantum state in the physical time $t$. A rather important tool in computational quantum physics is found solving the Schrödinger equation in the so-called imaginary-time $\tau=i t$. Let us consider again the case of static Hamiltonian, then in this case the imaginary-time evolved quantum state reads:

$$
\begin{equation*}
|\Psi(\tau)\rangle=e^{-\hat{H} \tau}|\Psi(0)\rangle \tag{10.17}
\end{equation*}
$$

We can immediately notice an important difference with respect to the real (or physical)time evolution: in the imaginary-time case, the evolution is no longer unitary and it can, for example, systematically change the norm of our initial state. One of the reasons why imaginary-time evolution is important, is that it can be used as an alternative scheme to find the ground-state of a given hamiltonian $\mathrm{H}$. To show this, we use the spectral decomposition of the initial state in terms of the eigenstates of the Hamiltonian, $\left|\phi_{k}\right\rangle$ of energy $E_{k}:$

$$
\begin{equation*}
|\Psi(\tau)\rangle=\sum_{k} e^{-E_{k} \tau} c_{k}\left|\phi_{k}\right\rangle \tag{10.18}
\end{equation*}
$$

We also imagine that we have sorted the eigenstates in ascending order with respect to the energy, such as that $E_{0}<E_{1}<E_{2} \ldots$, and define the energy differences $\Delta E_{k}=$ $E_{k}-E_{0} \geq 0$. We then rewrite

$$
\begin{equation*}
|\Psi(\tau)\rangle=e^{-E_{0} \tau}\left[c_{0}\left|\phi_{0}\right\rangle+\sum_{k>0} e^{-\Delta E_{k} \tau} c_{k}\left|\phi_{k}\right\rangle\right] \tag{10.19}
\end{equation*}
$$

When the initial state is non-orthogonal to the exact ground-state (i.e. when $\left|c_{0}\right| \neq 0$ ), the imaginary-time evolution converges to the exact ground state. This can be derived immediately from the last expression, since in the limit $\tau \gg \Delta E_{0}$ the right-hand-side vanished exponentially. Therefore, apart from an arbitrary normalization, we converge to the exact ground-state of the system, namely : $|\Psi(\tau)\rangle \simeq\left|\phi_{0}\right\rangle$. Imaginary-time evolution can be then used as an alternative approach to find the exact ground-state of the system, and can be implemented using the same methods presented before for the real-time evolution.

### 10.2.1 Variational Imaginary Time evolution

The discussion on the time dependent variational principle can be extended also to the case of imaginary time dynamics, and offers an alternative approach to find the variational ground state of a given Hamiltonian. The main difference is that the variational parameters are now taken to be dependent on the imaginary time $\tau$ and we aim at finding optimal variational parameters derivatives, such that

$$
\begin{equation*}
\left|\psi\left[\boldsymbol{\theta}\left(\tau+\delta_{\tau}\right)\right]\right\rangle \simeq\left|\phi\left(t+\delta_{\tau}\right)\right\rangle \tag{10.20}
\end{equation*}
$$

The optimal equation of the solved in this case is found by minimizing the distance between these two states:

$$
\begin{align*}
|I\rangle & =|\psi(\boldsymbol{\theta})\rangle-\delta_{\tau} \hat{H}|\psi(\boldsymbol{\theta})\rangle  \tag{10.21}\\
|I I\rangle & =|\psi(\boldsymbol{\theta})\rangle+\delta_{\tau} \sum_{k} \dot{\theta}_{k}(\tau) \partial_{\theta_{k}}|\psi(\boldsymbol{\theta})\rangle \tag{10.22}
\end{align*}
$$

which yields a very similar equation of motion:

$$
\begin{equation*}
\sum_{k^{\prime}} S_{k k^{\prime}}^{R} \dot{\theta}_{k^{\prime}}(\tau)=-C_{k}^{R} \tag{10.23}
\end{equation*}
$$

the main difference being that the right hand side now contains the real part of $C_{k}$.

### 10.3 The Dirac-Frenkel variational principle

The time-dependent variational principle derived before (due to McLachlan) is valid for arbitrary states containing real-valued parameters, $\theta(t)$. In the special case in which the parameters are complex valued instead, we can still solve the equations of motions as written before, just considering twice as many variational parameters, corresponding to the real and imaginary part of each complex-valued parameter $\theta(t)=\theta^{R}+i \theta^{I}$. In this sense, the McLachlan variational principle is very general. However, there is an important family of variational states that depend on complex parameters and that are holomorphic (complex differentiable). In this context, this implies that the following Cauchy-Riemann conditions for the wave functions amplitudes derivatives are verified:

$$
\begin{align*}
& \frac{\partial \psi^{R}(\mathbf{x} ; \theta)}{\partial \theta_{k}^{R}}=\frac{\partial \psi^{I}(\mathbf{x} ; \theta)}{\partial \theta_{k}^{I}}  \tag{10.24}\\
& \frac{\partial \psi^{R}(\mathbf{x} ; \theta)}{\partial \theta_{k}^{I}}=-\frac{\partial \psi^{I}(\mathbf{x} ; \theta)}{\partial \theta_{k}^{R}} \tag{10.25}
\end{align*}
$$

Famous examples of holomorphic functions are polynomials, exponentials etc. In this case, instead of considering the McLachlan equations of motion with twice as many (realvalued) variational parameters, we can exploit holomorphicity to reduce the equations of motion to the following form (in the real time evolution case):

$$
\begin{equation*}
\sum_{k^{\prime}} S_{k k^{\prime}} \dot{\theta}_{k^{\prime}}(t)=-i C_{k} \tag{10.26}
\end{equation*}
$$

Notice that in this case both the LHS matrix $S$ and the vector $C$ are complex valued, as well as the variational parameters derivatives. This version of the time dependent variational principle was actually discovered significantly before than the (more general) McLachlan case, and is traditionally attributed to Dirac and Frenkel.

### 10.4 Time-Dependent Variational Monte Carlo

In order to implement the time-dependent variational principle (both in real and imaginary time) with generic variational states, we can use an extension of Variational Monte Carlo. To simplify the equations, we start noticing that we can write the variational derivatives in terms of $D_{k}(\mathbf{x} ; \boldsymbol{\theta})=\frac{\partial_{\theta_{k}} \Psi(\mathbf{x} ; \boldsymbol{\theta})}{\Psi(\mathbf{x} ; \boldsymbol{\theta})}$ and its associated diagonal operator $\hat{D}_{k}$, such that:

$$
\begin{align*}
\partial_{\theta_{k}} \Psi(\mathbf{x} ; \boldsymbol{\theta}) & =\frac{\partial_{\theta_{k}} \Psi(\mathbf{x} ; \boldsymbol{\theta})}{\Psi(\mathbf{x} ; \boldsymbol{\theta})} \Psi(\mathbf{x} ; \boldsymbol{\theta})  \tag{10.27}\\
& =D_{k}(\mathbf{x} ; \boldsymbol{\theta}) \Psi(\mathbf{x} ; \boldsymbol{\theta}) \tag{10.28}
\end{align*}
$$

and

$$
\begin{equation*}
\left|\partial_{\theta_{k}} \psi(\boldsymbol{\theta})\right\rangle=\hat{D}_{k}|\psi(\boldsymbol{\theta})\rangle \tag{10.29}
\end{equation*}
$$

We therefore have that the metric tensor can be estimated as an average of operators, and estimated as the covariance of the logarithmic derivatives over the Born distribution:

$$
\begin{align*}
S_{k k^{\prime}} & =\frac{\left\langle\psi\left|\hat{D}_{k}^{\dagger} \hat{D}_{k^{\prime}}\right| \psi\right\rangle}{\langle\psi \mid \psi\rangle}-\frac{\left.\left\langle\psi\left|\hat{D}_{k}^{\dagger}\right| \psi\right\rangle\right\rangle}{\langle\psi \mid \psi\rangle} \frac{\left\langle\psi\left|\hat{D}_{k^{\prime}}\right| \psi\right\rangle}{\langle\psi \mid \psi\rangle}  \tag{10.30}\\
& =\mathbb{E}_{\Pi}\left[D_{k}^{\star}(\mathbf{x}) D_{k^{\prime}}(\mathbf{x})\right]-\mathbb{E}_{\Pi}\left[D_{k}^{\star}(\mathbf{x})\right] \mathbb{E}_{\Pi}\left[D_{k^{\prime}}(\mathbf{x})\right] \tag{10.31}
\end{align*}
$$

On the other hand the vector $C$ can be estimated noticing that

$$
\begin{align*}
\frac{\left\langle\partial_{\theta_{k}} \psi|\hat{H}| \psi\right\rangle}{\langle\psi \mid \psi\rangle} & =\frac{\sum_{\mathbf{x}}\left\langle\psi\left|\hat{D}_{k}^{\dagger}\right| \mathbf{x}\right\rangle\langle\mathbf{x}|\hat{H}| \psi\rangle}{\langle\psi \mid \psi\rangle}  \tag{10.32}\\
& =\frac{\sum_{\mathbf{x}}|\psi(\mathbf{x})|^{2} D_{k}^{\star}(\mathbf{x}) \frac{\langle\mathbf{x}|\hat{H}| \psi\rangle}{\langle\mathbf{x} \mid \psi\rangle}}{\langle\psi \mid \psi\rangle}  \tag{10.33}\\
& =\mathbb{E}_{\Pi}\left[D_{k}^{\star}(\mathbf{x}) E_{\mathrm{loc}}(\mathbf{x})\right] \tag{10.34}
\end{align*}
$$

thus it also takes the form of a statistical covariance:

$$
\begin{equation*}
C_{k}=\mathbb{E}_{\Pi}\left[D_{k}^{\star}(\mathbf{x}) E_{\mathrm{loc}}(\mathbf{x})\right]-\mathbb{E}_{\Pi}\left[D_{k}^{\star}(\mathbf{x})\right] \mathbb{E}_{\Pi}\left[E_{\mathrm{loc}}(\mathbf{x})\right] \tag{10.35}
\end{equation*}
$$

By comparing this with the results in the previous Lectures, we also notice that the real part of this vector is proportional to the energy gradient:

$$
\begin{equation*}
\frac{\partial}{\partial \theta_{k}} E(\boldsymbol{\theta})=\frac{1}{2} C_{k}^{R} \tag{10.36}
\end{equation*}
$$

### 10.4.1 Overall Algorithm

We summarize now the time-dependent Variational Monte Carlo in the general case of McLachlan variational principle. First off, we decided wether we want to simulate real or imaginary time dynamics. Then, the choice made, we go through the following steps:

0. Start the time evolution by initializing the variational parameters at some given values $\boldsymbol{\theta}(0)$. For example, these could random values, or could be parameters corresponding to a given state.

Then, at each time step:

1. Generate random samples $\mathbf{x}^{(1)} \ldots \mathbf{x}^{\left(N_{s}\right)}$ drawing from the probability density $\Pi(\mathbf{x}) \propto$ $|\psi(\mathbf{x} ; \boldsymbol{\theta}(t))|^{2}$.
2. Compute the quantities $S_{k k^{\prime}}$ and $C_{k}$ as averages over this samples using the expressions above
3. If doing real time evolution, solve the linear system:

$$
\begin{equation*}
\sum_{k^{\prime}} S_{k k^{\prime}}^{R} \dot{\theta}_{k^{\prime}}(t)=C_{k}^{I} \tag{10.37}
\end{equation*}
$$

for the vector of unknowns $\dot{\theta}_{k}(t)$. If doing imaginary time evolution, solve instead the linear system:

$$
\begin{equation*}
\sum_{k^{\prime}} S_{k k^{\prime}}^{R} \dot{\theta}_{k^{\prime}}(\tau)=-C_{k}^{R} \tag{10.38}
\end{equation*}
$$

for the vector of unknowns $\dot{\theta}_{k}(\tau)$.

4. Use the time derivatives to update the parameters, for example with a simple Euler scheme:

$$
\begin{equation*}
\theta_{k}\left(t+\delta_{t}\right)=\theta_{k}(t)+\delta_{t} \dot{\theta}_{k}(t) \tag{10.39}
\end{equation*}
$$

In practice, in the last step one rarely uses the simple Euler scheme, because it would require very small time steps in order to get a stable trajectory. More often, higher-order integration schemes such as Runge-Kutta are employed. A noticeable exception is the case of imaginary time evolution, where it is often the case that the simple Euler scheme is preferred, giving rise to a method known as "Stochastic reconfiguration", that is commonly adopted as an alternative to stochastic gradient descent to find the variational ground state of a given Hamiltonian.

### 10.5 Example: dynamics of a mean-field variational state

As a relatively simple example of the formalism developed above, let us consider the case of 2 spins $1 / 2$ on a lattice evolving according to the usual transverse-field Ising hamiltonian:

$$
\hat{H}=-\Gamma\left(\hat{\sigma}_{1}^{x}+\hat{\sigma}_{2}^{x}\right)-V \hat{\sigma}_{1}^{z} \hat{\sigma}_{z}^{z}
$$

and we consider as an initial state

$$
\begin{equation*}
|\phi(0)\rangle=|\downarrow\rangle_{1} \otimes|\downarrow\rangle_{2} \tag{10.41}
\end{equation*}
$$

This problem is small enough that it can be solved exactly, however it is instructive to look at how variational dynamics works. We will consider a time-dependent variational ansatz of the form

$$
\begin{equation*}
|\psi(t)\rangle=e^{\theta(t)\left(\hat{\sigma}_{1}^{x}+\hat{\sigma}_{2}^{x}\right)}|\phi(0)\rangle \tag{10.42}
\end{equation*}
$$

where the variational parameter $\theta(t)$ is taken complex valued and it is to be determined by solving the corresponding equations of motion. The explicit form of the variational state is by construction factorized

$$
\begin{equation*}
|\psi(t)\rangle=|\Phi(t)\rangle_{1} \otimes|\Phi(t)\rangle_{2} \tag{10.43}
\end{equation*}
$$

with

$$
\begin{equation*}
|\Phi(t)\rangle_{k}=\cosh (\theta(t))|\downarrow\rangle_{k}+\sinh (\theta(t))|\uparrow\rangle_{k} \tag{10.44}
\end{equation*}
$$

Because of the simple variational form, we can also determine the variational derivatives easily.

$$
\begin{equation*}
\left|\partial_{\theta} \psi(t)\right\rangle=\left(\hat{\sigma}_{1}^{x}+\hat{\sigma}_{2}^{x}\right)|\psi(t)\rangle \tag{10.45}
\end{equation*}
$$

Since the ansatz contains a complex parameter, $\theta(t)$, and its amplitudes are holomorphic (prove it!), we can solve the Dirac-Frenkel equations of motion, Eq. (10.26). The matrix $S$ in this case is then just a scalar and reads:

$$
\begin{align*}
\left\langle\partial_{\theta} \psi(t) \mid \partial_{\theta} \psi(t)\right\rangle-\left|\left\langle\psi(t) \mid \partial_{\theta} \psi(t)\right\rangle\right|^{2} & =2+2\left\langle\hat{\sigma}_{1}^{x}\right\rangle\left\langle\hat{\sigma}_{2}^{x}\right\rangle-\left|\left\langle\hat{\sigma}_{1}^{x}\right\rangle+\left\langle\hat{\sigma}_{2}^{x}\right\rangle\right|^{2}  \tag{10.46}\\
& =2-2\left\langle\hat{\sigma}_{1}^{x}\right\rangle^{2} \tag{10.47}
\end{align*}
$$

Analogous equations can be derived for the vector $C$ (which is again just a scalar in this case). We leave as an exercise the task of solving the equations of motion and comparing the variational dynamics to the exact one.

In general, one can already expect that if the interactions are small, the variational dynamics with this simple mean-field ansatz should be accurate.

