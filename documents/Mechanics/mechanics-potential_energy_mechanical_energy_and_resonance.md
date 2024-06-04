## Potential energy, mechanical energy and resonance

In chapter 6, we defined the kinetic energy of a material point. In the first section, we will show that we can define potential energies related to conservative forces. The sum of the kinetic and potential energies is the mechanical energy. In the second section, we will discuss the power dissipated by the non-conservative forces and we will study the notion of stability of an equilibrium position. In chapter 4, we studied the dynamics of a free harmonic oscillator and of a damped harmonic oscillator. In the third section of this chapter, we will examine the dynamics of a driven harmonic oscillator coupled to a periodic external force. We will see that the amplitude of motion depends critically on the oscillation frequency. This behaviour is at the root of the resonance phenomenon.

### 7.1 Potential energy and mechanical energy

In chapter 6 , we defined the work $W_{12}$ performed by a force $\boldsymbol{F}$ on a material point, when it moves from an initial position $\boldsymbol{r}_{1}$ to a final position $\boldsymbol{r}_{2}$, as the integral of the product of the force $\boldsymbol{F}$ and the displacement $d \boldsymbol{r}$ along the trajectory of the material point. This curvilinear integral (6.30) depends in general on the path followed. However, there are forces called conservative forces - term that will be justified later - for which the integral is independent of the path followed. It depends only on the initial position $\boldsymbol{r}_{1}$ and the final position $\boldsymbol{r}_{2}$. The work performed by a conservative force $\boldsymbol{F}_{c}$ to move a material point from an initial position $\boldsymbol{r}_{1}$ to a final position $\boldsymbol{r}_{2}$ is thus written as,

$$
\begin{equation*}
W_{12}=\int_{\boldsymbol{r}_{1}}^{\boldsymbol{r}_{2}} \boldsymbol{F}_{c}\left(\boldsymbol{r}^{\prime}\right) \cdot d \boldsymbol{r}^{\prime}=\int_{\boldsymbol{r}_{1}}^{\boldsymbol{r}_{s}} \boldsymbol{F}_{c}\left(\boldsymbol{r}^{\prime}\right) \cdot d \boldsymbol{r}^{\prime}+\int_{\boldsymbol{r}_{s}}^{\boldsymbol{r}_{2}} \boldsymbol{F}_{c}\left(\boldsymbol{r}^{\prime}\right) \cdot d \boldsymbol{r}^{\prime} \tag{7.1}
\end{equation*}
$$

### 7.1.1 Potential energy

Now we can define the potential associated to the conservative force $\boldsymbol{F}_{c}$, that is a function of the position $\boldsymbol{r}$ and corresponds to the potential energy,

$$
\begin{equation*}
V(\boldsymbol{r})=-\int_{\boldsymbol{r}_{s}}^{\boldsymbol{r}} \boldsymbol{F}_{c} \cdot d \boldsymbol{r}^{\prime} \tag{7.2}
\end{equation*}
$$

where $\boldsymbol{r}_{s}$ is a position of reference called the reference of potential that can be chosen appropriately. The potential or the potential energy is thus defined up to a constant like the kinetic energy. Taking into account the definition (7.2), the work (7.1) of the conservative force $\boldsymbol{F}_{c}$ can be expressed now as the opposite of the variation of potential energy,

$$
\begin{equation*}
W_{12}=-\int_{\boldsymbol{r}_{s}}^{\boldsymbol{r}_{1}} \boldsymbol{F}_{c} \cdot d \boldsymbol{r}^{\prime}+\int_{\boldsymbol{r}_{s}}^{\boldsymbol{r}_{2}} \boldsymbol{F}_{c} \cdot d \boldsymbol{r}^{\prime}=V\left(\boldsymbol{r}_{1}\right)-V\left(\boldsymbol{r}_{2}\right) \equiv-\left(V_{2}-V_{1}\right) \tag{7.3}
\end{equation*}
$$

The unit of potential energy in the international system of units is the Joule denoted $[\mathrm{J}=$ $\left.\mathrm{kg} \mathrm{m}^{2} / \mathrm{s}^{2}\right]$. It is of course the same unit as the work and the kinetic energy.

Theorem 7.1 The necessary and sufficient condition for the existence of a potential or a potential energy $V(\boldsymbol{r})$ associated to a force $\boldsymbol{F}$, i.e. for the force to be conservative, is that
the curvilinear integral of the infinitesimal work $\boldsymbol{F} \cdot d \boldsymbol{r}$ vanishes along every closed path,

$$
\begin{equation*}
\oint \boldsymbol{F} \cdot d \boldsymbol{r}^{\prime}=0 \tag{7.4}
\end{equation*}
$$

Demonstration Since the curvilinear integral of the force has to vanish along every closed path, it has to be independent of the path and depends only on the initial position $\boldsymbol{r}_{1}$ and on the final position $\boldsymbol{r}_{2}$. For a closed path, the initial position is identical to the final position, i.e. $\boldsymbol{r}_{1} \equiv \boldsymbol{r}_{2}$. Thus,

$$
\begin{equation*}
\oint \boldsymbol{F} \cdot d \boldsymbol{r}^{\prime}=\int_{\boldsymbol{r}_{1}}^{\boldsymbol{r}_{1}} \boldsymbol{F} \cdot d \boldsymbol{r}^{\prime}=0 \tag{7.5}
\end{equation*}
$$

Historically, it is William John Macquorn Rankine who introduced the extremely useful notion of potential energy.

### 7.1.2 Mechanical energy

The mechanical energy $E$ is an extensive scalar quantity that is the sum of the kinetic energy $T$ and of the total potential energy $V$ associated to all the conservative forces,

$$
\begin{equation*}
E=T+V \tag{7.6}
\end{equation*}
$$

It is of course the same unit as the kinetic and potential energies.

Theorem 7.2 If all the forces acting on the material point are conservative forces, then the mechanical energy $E$ is conserved, which implies that the mechanical energy $E_{1}$ at the initial time $t_{1}$ is equal to the mechanical energy $E_{2}$ at the final time $t_{2}$,

$$
\begin{equation*}
E_{1}=E_{2}=\text { const } \tag{7.7}
\end{equation*}
$$

Demonstration Identifying expressions (6.33) and (7.3) of the work $W_{12}$, we obtain the relation

$$
\begin{equation*}
T_{2}-T_{1}=-\left(V_{2}-V_{1}\right) \quad \text { thus } \quad E_{1}=T_{1}+V_{1}=T_{2}+V_{2}=E_{2}=\text { const } \tag{7.8}
\end{equation*}
$$

### 7.1.3 Conservative force

We would like now to express a conservative force $\boldsymbol{F}_{c}$ in terms of the potential $V$ asso-

Vertical and radial gradients ciated to this force. In order to do so, we compute the infinitesimal work performed by the conservative force $\boldsymbol{F}_{c}$ during an infinitesimal displacement $d \boldsymbol{r}$ from an initial position $\boldsymbol{r}$ to a final position $\boldsymbol{r}+d \boldsymbol{r}$. In a Cartesian frame, the position vector and the displacement vector are written as,

$$
\begin{equation*}
\boldsymbol{r}=\sum_{i=1}^{3} x_{i} \boldsymbol{e}_{i} \quad \text { thus } \quad d \boldsymbol{r}=\sum_{i=1}^{3} d x_{i} \boldsymbol{e}_{i} \tag{7.9}
\end{equation*}
$$

and therefore the infinitesimal work of the conservative force $\boldsymbol{F}_{c}$ is expressed as,

$$
\begin{align*}
\boldsymbol{F}_{c} \cdot d \boldsymbol{r} & =-(V(\boldsymbol{r}+d \boldsymbol{r})-V(\boldsymbol{r}))=-\sum_{i=1}^{3}\left(\frac{V\left(\boldsymbol{r}+d x_{i} \boldsymbol{e}_{i}\right)-V(\boldsymbol{r})}{d x_{i}}\right) d x_{i} \\
& =-\sum_{i=1}^{3} \frac{\partial V}{\partial x_{i}} d x_{i}=-\left(\sum_{i=1}^{3} \frac{\partial V}{\partial x_{i}} \boldsymbol{e}_{i}\right) \cdot d \boldsymbol{r} \equiv-\frac{d V}{d \boldsymbol{r}} \cdot d \boldsymbol{r} \tag{7.10}
\end{align*}
$$

where the term $\partial V / \partial x_{i}$ means partial derivative of the potential $V$ with respect to the coordinate $x_{i}$ that is computed by keeping the other coordinates constant in the expression of the potential $V$.

The potential gradient $\nabla V$ is a vector whose coordinates are obtained by taking the partial derivative of the potential $V$ with respect to the corresponding coordinates,

$$
\begin{equation*}
\boldsymbol{\nabla} V \equiv \frac{d V}{d \boldsymbol{r}}=\sum_{i=1}^{3} \frac{\partial V}{\partial x_{i}} \boldsymbol{e}_{i} \quad \text { where } \quad \boldsymbol{\nabla}=\left(\frac{\partial}{\partial x_{1}}, \frac{\partial}{\partial x_{2}}, \frac{\partial}{\partial x_{3}}\right) \tag{7.11}
\end{equation*}
$$

The potential gradient is the vectorial derivative of the potential. At a given point, it is oriented in the direction of the largest variation of the potential and its norm corresponds to the value of the slope. The curves of constant potential are called equipotentials. At every point of an equipotential, the gradient vector is orthogonal to the equipotential. Substituting the definition (7.10) into equation (7.11), we can express the conservative force $\boldsymbol{F}_{c}$ as the opposite of the associated potential gradient,

$$
\begin{equation*}
\boldsymbol{F}_{c}=-\nabla V \tag{7.12}
\end{equation*}
$$

### 7.1.4 Gravitational potential energy

The gravitational potential energy $V_{g}(\boldsymbol{r})$ is the potential energy associated to the weight $\boldsymbol{P}=m \boldsymbol{g}$ of a material point of mass $m$. It is a conservative force. According to the definition (7.2), the gravitational potential energy is written as,

$$
\begin{equation*}
V_{g}(\boldsymbol{r})=-\int_{\boldsymbol{r}_{s}}^{\boldsymbol{r}} \boldsymbol{P} \cdot d \boldsymbol{r}^{\prime}=-\int_{\boldsymbol{r}_{s}}^{\boldsymbol{r}} m \boldsymbol{g} \cdot d \boldsymbol{r}^{\prime} \tag{7.13}
\end{equation*}
$$

Since the gravitational field $\boldsymbol{g}$ is vertical, we choose a vertical axis $O z$ with an origin at the level of the ground. We take as a reference of gravitational potential the horizontal plane that goes through the origin $O$, i.e. $\boldsymbol{r}_{s}=\mathbf{0}$. The position vector $\boldsymbol{r}$, the infinitesimal displacement vector $d \boldsymbol{r}$ and the gravitational field $\boldsymbol{g}$ along the vertical axis are written as,

$$
\begin{equation*}
\boldsymbol{r}=z \boldsymbol{e}_{z} \quad d \boldsymbol{r}=d z \boldsymbol{e}_{z} \quad \boldsymbol{g}=-g \boldsymbol{e}_{z} \tag{7.14}
\end{equation*}
$$

Taking into account the vectorial expressions (7.14), the potential energy (7.13) is recast as,

$$
\begin{equation*}
V_{g}(z)=-\int_{0}^{\boldsymbol{r}} m \boldsymbol{g} \cdot d \boldsymbol{r}^{\prime}=m g \int_{0}^{z} d z^{\prime}=m g z \tag{7.15}
\end{equation*}
$$

According to expression (7.12), the weight $\boldsymbol{P}$ of the material point is obtained by differentiation of the gravitational potential energy,

$$
\begin{equation*}
\boldsymbol{P}=-\boldsymbol{\nabla} V_{g}=-\frac{d V_{g}}{d \boldsymbol{r}}=-\frac{d V_{g}}{d z} \boldsymbol{e}_{z}=-m g \boldsymbol{e}_{z}=m \boldsymbol{g} \tag{7.16}
\end{equation*}
$$

As an example, let us mention the yo-yo that transforms gravitational potential energy into kinetic energy and vice versa, conserving the mechanical energy.

### 7.1.5 Elastic potential energy

The elastic potential energy $V_{e}(\boldsymbol{r})$ is the potential energy associated to the elastic force $\boldsymbol{F}_{e}=-k \boldsymbol{r}$ exerted on a material by a spring of elastic constant $k$. It is a conservative force. According to the definition (7.2), the elastic potential energy is written as,

$$
\begin{equation*}
V_{e}(\boldsymbol{r})=-\int_{\boldsymbol{r}_{s}}^{\boldsymbol{r}} \boldsymbol{F}_{e} \cdot d \boldsymbol{r}^{\prime}=\int_{\boldsymbol{r}_{s}}^{\boldsymbol{r}} k \boldsymbol{r}^{\prime} \cdot d \boldsymbol{r}^{\prime} \tag{7.17}
\end{equation*}
$$

We choose a horizontal axis $O x$ along the spring with an origin at the level of the suspension point of the material point at rest. We take as a reference of elastic potential the vertical plane that goes through the origin $O$, i.e. $\boldsymbol{r}_{s}=\mathbf{0}$. The position vector $\boldsymbol{r}$ and the infinitesimal displacement vector $d \boldsymbol{r}$ along the horizontal axis are written as,

$$
\begin{equation*}
\boldsymbol{r}=x \boldsymbol{e}_{x} \quad d \boldsymbol{r}=d x \boldsymbol{e}_{x} \tag{7.18}
\end{equation*}
$$

Taking into account the vectorial expressions (7.18), the potential energy (7.17) is recast as,

$$
\begin{equation*}
V_{e}(x)=\int_{\mathbf{0}}^{\boldsymbol{r}} k \boldsymbol{r}^{\prime} \cdot d \boldsymbol{r}^{\prime}=k \int_{0}^{x} x^{\prime} d x^{\prime}=\frac{1}{2} k x^{2} \tag{7.19}
\end{equation*}
$$

According to expression (7.12), the elastic force $\boldsymbol{F}_{e}$ exerted on the material point is obtained by differentiation of the elastic potential energy,

$$
\begin{equation*}
\boldsymbol{F}_{e}=-\boldsymbol{\nabla} V_{e}=-\frac{d V_{e}}{d \boldsymbol{r}}=-\frac{d V_{e}}{d x} \boldsymbol{e}_{x}=-k x \boldsymbol{e}_{x}=-k \boldsymbol{r} \tag{7.20}
\end{equation*}
$$

As an example, let us mention the Wilberforce pendulum that transforms translational elastic potential energy into rotational elastic potential energy and kinetic energy, conserving the mechanical energy.

### 7.2 Power dissipation, equilibrium and stability

In this section, we will show first that the non-conservative forces, called dissipative forces, dissipate mechanical energy. Then, we will show that the expression of the equilibrium positions can be determined analytically by differentiating the expression of the total potential energy. We will also study their stability.

### 7.2.1 Mechanical power dissipation

We consider a conservative external force $\boldsymbol{F}_{c}^{\text {ext }}(t)$ and a non-conservative or dissipative external forces $\boldsymbol{F}_{n c}^{\text {ext }}(t)$ exerted on a material point of mass $m$. The sum of the external forces is written as,

$$
\begin{equation*}
\sum \boldsymbol{F}^{\text {ext }}(t)=\boldsymbol{F}_{c}^{\text {ext }}(t)+\boldsymbol{F}_{n c}^{\text {ext }}(t) \tag{7.21}
\end{equation*}
$$

The conservative force is obtained by differentiating the associated potential,

$$
\begin{equation*}
\boldsymbol{F}_{c}^{\mathrm{ext}}(t)=-\boldsymbol{\nabla} V(\boldsymbol{r}(t)) \tag{7.22}
\end{equation*}
$$

The potential energy is written as,

$$
\begin{equation*}
V(t) \equiv V(\boldsymbol{r}(t))=\sum_{i=1}^{N} V_{i}(\boldsymbol{r}(t)) \tag{7.23}
\end{equation*}
$$

The mechanical power dissipated $P_{n c}(t)$ is defined as the time derivative of the mechanical energy $E(t)$,

$$
\begin{equation*}
P_{n c}(t)=\frac{d E(t)}{d t} \tag{7.24}
\end{equation*}
$$

Taking into account the definition (7.6) of the mechanical energy $E(t)$, the expression (6.32) of the kinetic energy $T(t)$, the expression (7.23) of the total potential energy $V(t)$, the definition (2.1) of the velocity, the definition (2.2) of the acceleration and the definition of the potential gradient (7.11), the mechanical power dissipated (7.24) can be recast as,

$$
\begin{align*}
P_{n c}(t) & =\frac{d E(t)}{d t}=\frac{d}{d t}(T(t)+V(t))=\frac{d}{d t}\left(\frac{1}{2} m \boldsymbol{v}^{2}(t)+V(\boldsymbol{r}(t))\right) \\
& =m \boldsymbol{v}(t) \cdot \frac{d \boldsymbol{v}(t)}{d t}+\frac{d V(\boldsymbol{r}(t))}{d \boldsymbol{r}(t)} \cdot \frac{d \boldsymbol{r}(t)}{d t}=(m \boldsymbol{a}(t)+\boldsymbol{\nabla} V(\boldsymbol{r}(t))) \cdot \boldsymbol{v}(t) \tag{7.25}
\end{align*}
$$

The law of motion (2.33) of the material point is written as,

$$
\begin{equation*}
\sum \boldsymbol{F}^{e x t}(t)=m \boldsymbol{a}(t) \tag{7.26}
\end{equation*}
$$

Taking into account the expression (7.22) of the conservative forces and the law of motion (7.26), the mechanical power dissipated (7.25) reduces to,

$$
\begin{equation*}
P_{n c}(t)=\left(\sum \boldsymbol{F}^{\mathrm{ext}}(t)-\boldsymbol{F}_{c}^{\mathrm{ext}}(t)\right) \cdot \boldsymbol{v}(t)=\boldsymbol{F}_{n c}^{\mathrm{ext}}(t) \cdot \boldsymbol{v}(t) \tag{7.27}
\end{equation*}
$$

which shows that the mechanical energy dissipation is due only to the non-conservative or dissipative force.

As an example, let us consider the mechanical power dissipated due to a viscous friction

Antoine Laurent de Lavoisier
force $\boldsymbol{F}_{f}(t)=-b \boldsymbol{v}(t)$ where $b>0$ in a laminar flow regime. According to equation (7.27), the mechanical power dissipated is then written as,

$$
\begin{equation*}
P_{n c}(t)=\boldsymbol{F}_{f}(t) \cdot \boldsymbol{v}(t)=-b \boldsymbol{v}^{2}(t)<0 \tag{7.28}
\end{equation*}
$$

The mechanical power dissipated is negative which means that the material point looses mechanical energy. However, Antoine Laurent de Lavoisier rightly stated : "Nothing is lost, nothing is created, everything is transformed". Actually, the mechanical energy dissipated by the friction force transforms into another form of energy called thermal energy as you will discover during the second semester in the thermodynamics course, that is an extension of mechanics allowing to include other kinds of energy.

### 7.2.2 Equilibrium position and stability

We consider the motion of a material point in the absence of a non-conservative, which implies that the mechanical energy $E$ is conserved. At equilibrium, the kinetic energy (6.32) vanishes. Taking into account the mechanical energy (7.6),

$$
\begin{equation*}
T=0 \quad \text { thus } \quad E=V=\text { const } \quad \text { (equilibrium) } \tag{7.29}
\end{equation*}
$$

The material point dynamics is characterised by only one variable that corresponds to a degree of freedom. This variable called generalised coordinate and denoted $q$ can be either a position or an angle, i.e. $q \in\{x, y, z, \theta, \phi\}$. At equilibrium, when $q=q_{0}$, the condition (7.29) on the potential energy $V(q)$ associated to the conservative force $\boldsymbol{F}_{c}$ is written as,

$$
\begin{equation*}
\left.\frac{d V}{d q}\right|_{q=q_{0}}=0 \quad(\text { equilibrium) } \tag{7.30}
\end{equation*}
$$

which means that the equilibrium state corresponds to an extremum of the potential energy. To study the stability of the equilibrium position $q_{0}$, the dynamics of the material point in the neighbourhood of the equilibrium position has to be considered. The power series expansion to $2^{\text {nd }}$ order of the potential energy $V(q)$ around the equilibrium position $q_{0}$ is written as,

$$
\begin{equation*}
V(q)=V\left(q_{0}\right)+\left.\frac{d V}{d q}\right|_{q=q_{0}}\left(q-q_{0}\right)+\left.\frac{1}{2} \frac{d^{2} V}{d q^{2}}\right|_{q=q_{0}}\left(q-q_{0}\right)^{2}+\mathcal{O}\left(q^{3}\right) \tag{7.31}
\end{equation*}
$$

Taking into account the condition (7.30), the power series expansion (7.31) in the neighbourhood of the equilibrium reduces to,

$$
\begin{equation*}
V(q)=V\left(q_{0}\right)+\left.\frac{1}{2} \frac{d^{2} V}{d q^{2}}\right|_{q=q_{0}}\left(q-q_{0}\right)^{2}+\mathcal{O}\left(q^{3}\right) \tag{7.32}
\end{equation*}
$$

Taking into account expressions (7.11) and (7.12), the conservative force $\boldsymbol{F}_{c}$ is given by,

$$
\begin{equation*}
\boldsymbol{F}_{c}=-\boldsymbol{\nabla} V=-\frac{d V}{d q} \boldsymbol{e}_{q} \tag{7.33}
\end{equation*}
$$

where $\boldsymbol{e}_{q}$ is the unit vector tangent to the line of coordinates $q$. The equilibrium position $q_{0}$ is stable if the sign of the second order derivative of the potential energy is positive because the conservative force brings the material point back to the equilibrium position in its neighbourhood. The equilibrium position $q_{0}$ is unstable if the sign of the second order derivative of the potential energy is negative because the conservative force $\boldsymbol{F}_{c}$ drives the material point away from the equilibrium position in its neighbourhood (Fig. 7.1).

### 7.2.3 Stability of the mathematical pendulum

As an example, let us determine the stability of the equilibrium positions of a mathematical pendulum consisting of a material point of mass $m$ suspended at the extremity of a rod of length $\ell$ oscillating in a vertical plane. The degree of freedom is the inclination angle of the rod of the pendulum $q=\phi$. We take a as reference of potential the horizontal surface that goes through the material point when the rod is vertical and the material point is at
its lowest position. The vertical coordinate is then written $z=\ell(1-\cos \phi)$. Taking into account the definition (7.15), the gravitational potential energy is given by,

$$
\begin{equation*}
V_{g}(\phi)=m g \ell(1-\cos \phi) \tag{7.34}
\end{equation*}
$$

According to the condition (7.30), at equilibrium the pendulum satisfies the condition,

$$
\begin{equation*}
\left.\frac{d V_{g}}{d \phi}\right|_{\phi=\phi_{0}}=m g \ell \sin \phi_{0}=0 \quad \text { thus } \quad \phi_{0} \in\{0, \pi\} \tag{7.35}
\end{equation*}
$$

To determine the stability of the equilibrium positions $\phi_{0}=0$ and $\phi_{0}=\pi$, we compute the second-order derivative of the gravitational potential energy $V_{g}(\phi)$,

$$
\begin{equation*}
\left.\frac{d^{2} V_{g}}{d \phi^{2}}\right|_{\phi=\phi_{0}}=m g \ell \cos \phi_{0} \tag{7.36}
\end{equation*}
$$

we conclude that the lower equilibrium position $\phi_{0}=0$ is stable because,

$$
\begin{equation*}
\left.\frac{d^{2} V_{g}}{d \phi^{2}}\right|_{\phi=\phi_{0}=0}=m g \ell>0 \quad \text { (stable position) } \tag{7.37}
\end{equation*}
$$

and that the superior equilibrium position $\phi_{0}=\pi$ is unstable because,

$$
\begin{equation*}
\left.\frac{d^{2} V_{g}}{d \phi^{2}}\right|_{\phi=\phi_{0}=\pi}=-m g \ell<0 \quad \text { (unstable position) } \tag{7.38}
\end{equation*}
$$

### 7.3 Resonance

The resonance of a physical system subjected to a periodic external force gives rise to an amplification of its oscillation amplitude for a precise frequency called the resonance frequency and for multiples of this frequency called harmonics. This resonance can be of acoustic or mechanical nature, as in the case of an air tube or of vibrating rods (Fig. 7.2). It can also be of electric or magnetic nature, as in the case of an $R L C$ circuit or of magnetic resonance imaging.

### 7.3.1 Driven harmonic oscillator

To study this very common resonance phenomenon in physics, we will consider the simplest mechanical model, namely a driven harmonic oscillator. Such an an oscillator is damped by viscous friction and driven by an periodic external force. In this model, a material point of mass $m$ is suspended to a spring of elastic constant $k$ and of natural length $l_{0}$. The spring is attached to a vibrator that exerts a tuneable periodic force on the spring.

The external forces $\boldsymbol{F}^{\text {ext }}$ are the weight $\boldsymbol{P}=m \boldsymbol{g}$ of the material point, the elastic force $\boldsymbol{F}_{e}=-k \boldsymbol{r}$, the viscous friction force $\boldsymbol{F}_{f}=-b \boldsymbol{v}$ and the periodic driving force $\boldsymbol{F}(t)=F_{0} \cos (\omega t) \boldsymbol{e}_{X}$ of amplitude $F_{0}$ and of pulsation $\omega$ generated by the vibrator where $\boldsymbol{e}_{X}$ is the unit vector oriented downwards. Thus, the law of motion of a driven harmonic oscillator $(2.33)$ reads,

$$
\begin{equation*}
m \boldsymbol{g}-b \boldsymbol{v}-k \boldsymbol{r}+F_{0} \cos (\omega t) \boldsymbol{e}_{X}=m \boldsymbol{a} \tag{7.39}
\end{equation*}
$$

We choose the origin $O$ of the vertical axis $O X$ - oriented positively downwards - at the
level of the suspension point of the spring to the vibrator when the vibrator is not vibrating (Fig. 7.3). The projections of the vectors $\boldsymbol{r}, \boldsymbol{v}, \boldsymbol{a}$ and $\boldsymbol{g}$ along the axis $O X$ are written as,

$$
\begin{equation*}
\boldsymbol{r}=\left(X-l_{0}\right) \boldsymbol{e}_{X} \quad \boldsymbol{v}=\dot{X} \boldsymbol{e}_{X} \quad \boldsymbol{a}=\ddot{X} \boldsymbol{e}_{X} \quad \boldsymbol{g}=g \boldsymbol{e}_{X} \tag{7.40}
\end{equation*}
$$

Taking into account the expressions (7.40), the projection of the law of motion along the axis $O X$ is written as,

$$
\begin{equation*}
m g-b \dot{X}-k\left(X-l_{0}\right)+F_{0} \cos (\omega t)=m \ddot{X} \tag{7.41}
\end{equation*}
$$

Using the following change of variables,

$$
\begin{equation*}
x=X-l_{0}-\frac{m g}{k} \quad \text { thus } \quad \dot{x}=\dot{X} \quad \text { and } \quad \ddot{x}=\ddot{X} \tag{7.42}
\end{equation*}
$$

the equation of motion (7.41) can be recast as,

$$
\begin{equation*}
m \ddot{x}+b \dot{x}+k x=F_{0} \cos (\omega t) \tag{7.43}
\end{equation*}
$$

Using the expression (3.22) of the damping time $\tau$ and the expression (4.26) of the pulsation $\omega_{0}$, and introducing the intensity of the driving acceleration $a_{0}$ expressed as,

$$
\begin{equation*}
a_{0}=\frac{F_{0}}{m} \tag{7.44}
\end{equation*}
$$

the equation of motion of the driven oscillator (7.43) can be recast as,

$$
\begin{equation*}
\ddot{x}+\frac{1}{\tau} \dot{x}+\omega_{0}^{2} x=a_{0} \cos (\omega t) \tag{7.45}
\end{equation*}
$$

### 7.3.2 Transient and stationary regimes

The general solution of the differential equation (7.45) corresponds to a linear combinational of two types of motions. Before switching on the vibrator, when the intensity $a_{0}$ of the driving acceleration vanishes, i.e. $a_{0}=0$, the motion equation (7.45) is that of a harmonic oscillator damped by the viscous friction of the surrounding fluid - generally air or water. If we wait long enough, the eigenmotion of the harmonic oscillator is entirely damped by the viscous friction. Then, the motion of the harmonic oscillator is entirely determined by the driving force $\boldsymbol{F}(t)$, i.e. it acquires the same pulsation $\omega$ as the driving force. The mathematical solution $x(t)$ of the equation of motion (7.45) is the sum of the solution of the homogeneous equation $x_{h}(t)$, defined by $a_{0}=0$, and of a specific solution $x_{p}(t)$ towards which the system tends at large times,

$$
\begin{equation*}
x(t)=x_{h}(t)+x_{p}(t) \tag{7.46}
\end{equation*}
$$

In chapter 4, we established that for a damped harmonic oscillator, the oscillation amplitude decreases exponentially over time,

$$
\begin{equation*}
x_{h}(t)=C e^{-t / \tau} \cos \left(\omega_{h} t+\varphi_{h}\right) \tag{https://cdn.mathpix.com/cropped/2024_05_18_d76a9ee6ab899d07a9a8g-08.jpg?height=49&width=91&top_left_y=905&top_left_x=1779}
\end{equation*}
$$

where $\omega_{h}$ is the pulsation of the damped harmonic oscillator in the absence of excitation and $\varphi_{h}$ is the dephasing angle. The specific solution $x_{p}(t)$ of pulsation $\omega$, that is independent of $\omega_{h}$, is given by,

$$
\begin{equation*}
x_{p}(t)=\rho \cos (\omega t+\varphi) \tag{7.48}
\end{equation*}
$$

where $\rho$ is the oscillation amplitude and $\varphi$ is the dephasing angle due to the viscous friction that generates a delay of the response of the system with respect to the excitation generated by the vibrator.

In the presence of a periodic driving force, there are two regimes that can be distinguished qualitatively and quantitatively. When the vibrator is switched on at the initial time, i.e. $t=0$, until a time that is of the order of magnitude of the damping time, i.e. $t \sim \tau$, there is coexistence between the eigenoscillations of the system and oscillations due to the driving force. It is the transient regime characterised qualitatively by the inference between oscillations of different pulsations that have amplitudes of the same order of magnitude and generate thus perceptible beats (Fig. 7.4).

$$
\begin{equation*}
x_{h}(t) \sim x_{p}(t) \quad \text { (transient regime) } \tag{https://cdn.mathpix.com/cropped/2024_05_18_d76a9ee6ab899d07a9a8g-08.jpg?height=49&width=91&top_left_y=1649&top_left_x=1779}
\end{equation*}
$$

For a time that is much larger than the damping time, i.e. $t \gg \tau$, the amplitude of the eigenoscillations becomes negligible compared to the amplitude of the oscillations generated by the periodic driving force. The motion of the harmonic oscillator is then entirely determined by the periodic driving force. It is the stationary regime.

$$
\begin{equation*}
x(t) \simeq x_{p}(t) \quad \text { because } \quad x_{h}(t) \ll x_{p}(t) \quad \text { (stationary regime) } \tag{https://cdn.mathpix.com/cropped/2024_05_18_d76a9ee6ab899d07a9a8g-08.jpg?height=46&width=91&top_left_y=2558&top_left_x=1779}
\end{equation*}
$$

The response of the system to the excitation force in a stationary regime is called the harmonic response. We will now examine this response.

### 7.3.3 Harmonic response

In a stationary regime, the solution of the equation of motion (7.45) is thus,

$$
\begin{equation*}
x(t)=\rho \cos (\omega t+\varphi) \tag{7.51}
\end{equation*}
$$

To determine the expression of the amplitude $\rho$ and the dephasing $\varphi$ of the harmonic response, we introduce a stationary solution of the equation of motion (7.45) dephased by a angle $\pi / 2$, which means that we perform the transformation $\omega t \rightarrow \omega t-\pi / 2$ in the expression $(7.51)$ for $x(t)$ to obtain,

$$
\begin{equation*}
y(t)=\rho \sin (\omega t+\varphi) \tag{7.52}
\end{equation*}
$$

The equation of motion (7.45) is written in terms of the variable $y$ and its time derivatives as,

$$
\begin{equation*}
\ddot{y}+\frac{1}{\tau} \dot{y}+\omega_{0}^{2} y=a_{0} \sin (\omega t) \tag{7.53}
\end{equation*}
$$

Taking the sum of equation (7.45) and of equation (7.53) multiplied by $i$ and expressing this sum in terms of the variable $z=x+i y$, taking into account Euler's formula (4.7), we obtain,

$$
\begin{equation*}
\ddot{z}+\frac{1}{\tau} \dot{z}+\omega_{0}^{2} z=a_{0} e^{i \omega t} \tag{7.54}
\end{equation*}
$$

Taking into account Euler's formula (4.7), the stationary solution of the equation of motion (7.54) is written as,

$$
\begin{equation*}
z(t)=z_{0} e^{i \omega t} \quad \text { where } \quad z_{0}=\rho e^{i \varphi} \tag{7.55}
\end{equation*}
$$

Substituting the stationary solution (7.55) into the equation of motion (7.54), we obtain the following condition,

$$
\begin{equation*}
\left(-\omega^{2}+i \frac{\omega}{\tau}+\omega_{0}^{2}\right) z_{0} e^{i \omega t}=a_{0} e^{i \omega t} \tag{7.56}
\end{equation*}
$$

Thus, the complex amplitude $z_{0}$ is written as,

$$
\begin{equation*}
z_{0}=\frac{a_{0}}{\omega_{0}^{2}-\omega^{2}+i(\omega / \tau)}=a_{0} \frac{\omega_{0}^{2}-\omega^{2}-i(\omega / \tau)}{\left(\omega_{0}^{2}-\omega^{2}\right)^{2}+(\omega / \tau)^{2}} \tag{7.57}
\end{equation*}
$$

According to the definition (7.55), the real amplitude $\rho$ is given by the modulus of $z_{0}$,

$$
\begin{equation*}
\rho=\left|z_{0}\right|=\frac{a_{0}}{\sqrt{\left(\omega_{0}^{2}-\omega^{2}\right)^{2}+(\omega / \tau)^{2}}} \tag{7.58}
\end{equation*}
$$

and the tangent of the dephasing angle $\varphi$ is given by the ratio of the imaginary and real parts of $z_{0}$,

$$
\begin{equation*}
\tan \varphi=\frac{\rho \sin \varphi}{\rho \cos \varphi}=\frac{\operatorname{Im}\left(\rho e^{i \varphi}\right)}{\operatorname{Re}\left(\rho e^{i \varphi}\right)}=\frac{\operatorname{Im}\left(z_{0}\right)}{\operatorname{Re}\left(z_{0}\right)}=-\frac{\omega / \tau}{\omega_{0}^{2}-\omega^{2}} \tag{7.59}
\end{equation*}
$$

By definition, the real amplitude $\rho$ is maximal at resonance. This is the case when the denominator of the fraction in the expression (7.58) is minimal. Thus, the system reaches the resonance frequency - in fact the resonance pulsation - when,

$$
\begin{equation*}
\omega=\omega_{0} \quad(\text { resonance frequency) } \tag{7.60}
\end{equation*}
$$

According to expression (7.59), the dephasing angle is maximal at resonance,

$$
\begin{equation*}
\varphi=-\frac{\pi}{2} \quad(\text { dephasing at resonance }) \tag{7.61}
\end{equation*}
$$

The ratio between the amplitudes at null frequency and at resonance frequency is given by (Fig 7.5),

$$
\begin{equation*}
\frac{\rho\left(\omega_{0}\right)}{\rho(0)}=\omega_{0} \tau \tag{7.62}
\end{equation*}
$$

In chapter 3, we showed that the smaller the fluid viscosity is the larger the damping time $\tau$ will be. Thus, since the ratio of the amplitudes at the resonance frequency (7.62)
is proportional to $\tau$, the smaller the viscosity of the surrounding medium is the larger the amplitude at the resonance frequency will be for a given excitation. For instance, the amplitude at the resonance frequency will be larger in air than in water, which seems quite intuitive.

The most famous historic example of resonance is probably the one of the destruction of the Tacoma bridge in 1940 due to the wind (Fig. 7.6). The Tacoma bridge collapsed when a strong wind generated a resonance whose amplitude became so large that the structure of the bridge could not resist.

A second example of mechanical resonance is the oscillation of pendula disposed on a rope. Letting the first pendulum oscillate, the other pendula begin to oscillate also : it is the transient regime. After a certain time, only the first and the fourth are still oscillating and the other stop oscillating : it's the stationary regime (Fig. 7.7). The first pendulum in

Destruction of a glass at resonance red has the same length as the fourth and thus the same pulsation because the pulsation $\omega=\sqrt{g / \ell}$ of a pendulum depends on its length.

A third example is the synchronisation of metronomes laid on a single wooden plate. When the plate rests on two cylinders and can thus oscillate laterally, the metronomes get synchronised by resonance through the plate. When the plate is not free to oscillate, the metronomes loose their synchronisation (Fig. 7.8).

A fourth example is the destruction of a glass at an acoustic resonance using ultrasounds generated by a loudspeaker (Fig. 1.1).

