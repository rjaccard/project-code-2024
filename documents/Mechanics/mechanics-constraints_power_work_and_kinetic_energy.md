# Constraints, power, work and kinetic energy 

In this section, we shall examine first the notion of geometric constraint that leads to the presence of constraint forces in the expression of the laws of motion. Then, we shall study the dynamics of the mathematical pendulum. Finally, we shall define the notions of power, work and kinetic energy.

### 6.1 Geometric constraints

The dynamical laws describe the motion of a material point in the presence of specific forces. In general, the material point is subjected to external constraints that determine the geometry of motion. These geometric constraints impose restrictions on motion. If the motion of the material point occurs on a sphere, its radius in spherical coordinates is constant. If the motion occurs on a horizontal surface, the vertical coordinates is constant. These geometric constraints can also be expressed in terms of forces applied on the material point. A material point suspended to a rod can be at equilibrium only if a constraint force is opposed to its weight. This force is the tension in the rod. The constraint forces prevent the acceleration of a material point in particular directions, which echoes the geometric constraints.

Now, we shall consider several concrete examples of geometric constraints that restrict the motion of the material point. The first example is a ball - that can be assimilated to a material point - that moves on the internal surface of a hollow hemisphere of radius $R$. To model the dynamics of the ball constrained to move on this surface, we use spherical coordinates. In spherical coordinates, the geometric constraint is that the radial coordinate $r$ is equal to the radius $R$ of the sphere,

$$
\begin{equation*}
r=R=\text { const } \tag{6.1}
\end{equation*}
$$

The second example is the ball that moves on the internal surface of a funnel. To model the dynamics of the ball constrained to move on this surface, we use cylindrical coordinates since the funnel has a cylindrical symmetry, i.e. it is invariant by rotation around the vertical axis. The intersection between the funnel and a vertical plane containing the vertical symmetry axis yields two hyperbolic arms. In cylindrical coordinates, the geometric constraint is that the opposite of the vertical coordinate $z$ is a hyperbolic function of the radial coordinate $\rho$, i.e.

$$
\begin{equation*}
z=-\frac{1}{\rho}=\text { const } \tag{6.2}
\end{equation*}
$$

The third example is a ball that moves on a slide with a looping. To model the dynamics of the ball constrained to move on this curve, we use Cartesian coordinates along the ramp and polar coordinates at the level of the circle (Fig. 6.1).

### 6.1.1 Constraint force

In the absence of a constraint force, the motion of the material point can occur a priori in the whole three dimensional space. To account for the geometric constraints in the expression of the law of motion (2.33), constraint forces that restrict the motion of the material point to a specific region of space have to be introduced. These forces are always normal to the physical surface on which the material point moves and they are orthogonal to the motion of the material point at all times. In the case of the material point laying on a horizontal surface like the ground, there is a constraint force $\boldsymbol{N}$ called the normal reaction of the ground on the material point that is of equal norm and opposite orientation to its weight. If this force would not be included in the law of motion, the material point would sink into the ground.

To link the notions of geometric constraints and force of constraint, we shall consider the specific example of a ball of mass $m$ sliding inside a vertical ring of radius $R$ rotating around its vertical symmetry axis at angular velocity $\omega=$ const (Fig. 5.5). To model the dynamics of a ball constrained to move on this rotating curve that defines a surface, we use spherical coordinates $(r, \theta, \phi)$. In spherical coordinates, the geometric constraints are that the radial coordinate $r$ is equal to the radius $R$ of the ring and that the time derivative of the azimuthal angle $\phi$ is the constant rotation angular velocity (Fig. 6.2),

$$
\begin{array}{lllll}
r=R=\text { const } & \text { thus } & \dot{r}=0 & \text { and } & \ddot{r}=0 \\
\omega=\dot{\phi}=\text { const } & \text { thus } & \dot{\omega}=0 & & \tag{6.3}
\end{array}
$$

The external forces acting on the material point are its weight $\boldsymbol{P}$ and the normal reaction force $\boldsymbol{N}$ of the ring on the material point. The weight $\boldsymbol{P}$ is oriented downwards. In the plane of the ring, the ball can move tangentially along the vector $\boldsymbol{e}_{\theta}$. Thus, in all generality, the normal reaction force $\boldsymbol{N}$ has two non-vanishing components that are orthogonal to the vector $\boldsymbol{e}_{\theta}$. Thus, the weight $\boldsymbol{P}$ and the normal reaction force $\boldsymbol{N}$ are written in spherical coordinates as,

$$
\begin{align*}
& \boldsymbol{P}=m \boldsymbol{g}=m g\left(\cos \alpha \boldsymbol{e}_{r}+\sin \alpha \boldsymbol{e}_{\theta}\right)=m g\left(-\cos \theta \boldsymbol{e}_{r}+\sin \theta \boldsymbol{e}_{\theta}\right)  \tag{6.4}\\
& \boldsymbol{N}=N_{r} \boldsymbol{e}_{r}+N_{\phi} \boldsymbol{e}_{\phi}
\end{align*}
$$

taking into account that $\alpha+\theta=\pi$, thus $\sin \alpha=\sin \theta$ and $\cos \alpha=-\cos \theta$. In order to obtain an explicit expression for the constraint force, we have to determine the dynamics of the ball given by the law of motion (2.33) that is written as,

$$
\begin{equation*}
\sum \boldsymbol{F}^{\mathrm{ext}}=\boldsymbol{P}+\boldsymbol{N}=m \boldsymbol{a} \tag{6.5}
\end{equation*}
$$

Taking into account the geometric constraints (6.3) the general expression (5.20) of the acceleration in spherical coordinates reduces here to,

$$
\begin{equation*}
\boldsymbol{a}=-R\left(\dot{\theta}^{2}+\omega^{2} \sin ^{2} \theta\right) \boldsymbol{e}_{r}+R\left(\ddot{\theta}-\omega^{2} \sin \theta \cos \theta\right) \boldsymbol{e}_{\theta}+2 R \omega \dot{\theta} \cos \theta \boldsymbol{e}_{\phi} \tag{6.6}
\end{equation*}
$$

Projecting the vectorial law of motion (6.5) along the three coordinates axes $\boldsymbol{e}_{r}, \boldsymbol{e}_{\theta}$ and $\boldsymbol{e}_{\phi}$ respectively, taking into account the expressions (6.4) for the external forces $\boldsymbol{P}$ and $\boldsymbol{N}$ as well as the expression (6.6) for the acceleration $\boldsymbol{a}$, we obtain three scalar equations,

$$
\begin{align*}
& -m g \cos \theta+N_{r}=-m R\left(\dot{\theta}^{2}+\omega^{2} \sin ^{2} \theta\right) \\
& m g \sin \theta=m R\left(\ddot{\theta}-\omega^{2} \sin \theta \cos \theta\right)  \tag{6.7}\\
& N_{\phi}=2 m R \omega \dot{\theta} \cos \theta
\end{align*}
$$

The first and the third equation yield the expression of the components $N_{r}$ and $N_{\phi}$ of the normal reaction force $\boldsymbol{N}$. The second equation is the motion equation of the ball in the ring that depends only on the angle $\theta$ since the other parameters are fixed. Taking into account equations (6.7), the normal reaction force $\boldsymbol{N}$ is written explicitly as,

$$
\begin{equation*}
\boldsymbol{N}=m\left(g \cos \theta-R \dot{\theta}^{2}-R \omega^{2} \sin ^{2} \theta\right) \boldsymbol{e}_{r}+2 m R \omega \dot{\theta} \cos \theta \boldsymbol{e}_{\phi} \tag{6.8}
\end{equation*}
$$

The normal reaction $\boldsymbol{N}$ is orthogonal to the unconstrained motion that occurs along $\boldsymbol{e}_{\theta}$ where the degree of freedom is the angle $\theta$.

### 6.2 Mathematical pendulum

There are several types of pendula. The simplest pendulum to describe is called the mathematical pendulum by opposition to a more realistic pendulum called the physical pendulum. In the model of the mathematical pendulum, we consider that the whole mass is located at a point suspended at the end of a massless rod whereas in the model of the physical pendulum the mass and inertia of the rod are not neglected. The mathematical pendulum is also sometimes called simple pendulum. Here, we shall use the term mathematical pendulum for reasons that shall become clearer in the end of the section.

### 6.2.1 Law and equation of motion

We consider a pendulum modelled as a material point constrained to move on a circle of constant radius $\ell$ in a vertical plane and subjected to the earth's gravitational field.

To make a mathematical model of this pendulum, we choose polar coordinates $(r, \phi)$ in a vertical plane, i.e. cylindrical coordinates $(r, \phi, z)$ with the geometric constraint $z=0$ where

$$
\begin{equation*}
\rho=\ell=\text { const } \quad \text { thus } \quad \dot{\rho}=0 \quad \text { and } \quad \ddot{\rho}=0 \tag{https://cdn.mathpix.com/cropped/2024_05_18_b84bd9b91e818ff3ebc0g-4.jpg?height=46&width=77&top_left_y=314&top_left_x=1796}
\end{equation*}
$$

The external forces acting on the material point are its weight $\boldsymbol{P}$ and the tension $\boldsymbol{T}$ in the rod. The weight $\boldsymbol{P}$ is oriented downwards. The pendulum oscillates in a vertical plane and the tension is orthogonal to the tangential motion of the mass. Thus, the tension $\boldsymbol{T}$ is radial and oriented towards the suspension point since it is opposed to the weight $\boldsymbol{P}$. Thus, the weight $\boldsymbol{P}$ and the tension $\boldsymbol{T}$ are written in polar coordinates in the vertical plane as (Fig. 6.4),

$$
\begin{equation*}
\boldsymbol{P}=m \boldsymbol{g}=m g\left(\cos \phi \boldsymbol{e}_{\rho}-\sin \phi \boldsymbol{e}_{\phi}\right) \quad \text { and } \quad \boldsymbol{T}=-T \boldsymbol{e}_{\rho} \tag{6.10}
\end{equation*}
$$

The dynamics of the mass is given by the law of motion (2.33) that is written as,

$$
\begin{equation*}
\sum \boldsymbol{F}^{\mathrm{ext}}=\boldsymbol{P}+\boldsymbol{T}=m \boldsymbol{a} \tag{6.11}
\end{equation*}
$$

Taking into account the geometric constraints (6.9) the general expression (5.10) of the acceleration in cylindrical coordinates reduces in the vertical plane $z=0$ to,

$$
\begin{equation*}
\boldsymbol{a}=-\ell \dot{\phi}^{2} \boldsymbol{e}_{\rho}+\ell \ddot{\phi} \boldsymbol{e}_{\phi} \tag{6.12}
\end{equation*}
$$

Projecting the vectorial law of motion (6.11) along the two coordinate axes $\boldsymbol{e}_{\rho}$ and $\boldsymbol{e}_{\phi}$
respectively, taking into account the expressions (6.10) for the external forces $\boldsymbol{P}$ and $\boldsymbol{T}$ as well as expression (6.12) for the acceleration $\boldsymbol{a}$, we obtain two scalar equations,

$$
\begin{align*}
& m g \cos \phi-T=-m \ell \dot{\phi}^{2} \\
& -m g \sin \phi=m \ell \ddot{\phi} \tag{6.13}
\end{align*}
$$

The first equation (6.13) yields the expression of the norm of the tension in the rod that depends on the angle $\phi$ and on the scalar angular velocity $\dot{\phi}$,

$$
\begin{equation*}
T=m\left(g \cos \phi+\ell \dot{\phi}^{2}\right) \tag{6.14}
\end{equation*}
$$

The second equation (6.13) is the tangential equation of motion for the mass $m$ that can be recast as,

$$
\begin{equation*}
\ddot{\phi}+\frac{g}{\ell} \sin \phi=0 \tag{6.15}
\end{equation*}
$$

which shows that the motion is independent of the mass $m$.

### 6.2.2 Small oscillations around the equilibrium

Before discussing the general solution of the motion equation (6.15), we will consider a particular case, the case of small oscillations around the equilibrium position when the rod is vertical, i.e. when $\phi=0$. In the small oscillation limit, using the formula (1.21) of the power series expansion to first-order of the function $\sin \phi$ around $\phi=0$, we obtain,

$$
\begin{equation*}
\sin \phi \simeq \sin 0+\left(\frac{d \sin \phi}{d \phi}(0)\right) \phi=0+\cos 0 \phi=\phi \tag{6.16}
\end{equation*}
$$

Taking into account the relation (6.16) in the small oscillation limit, the equation of motion reduces in good approximation to,

$$
\begin{equation*}
\ddot{\phi}+\frac{g}{\ell} \phi=0 \tag{6.17}
\end{equation*}
$$

which is the equation of a harmonic oscillator where the variable is the angle $\phi$. According to the definitions (4.6), (4.11) and (4.12), the pulsation $\omega$ and the oscillation period $T$ are expressed as,

$$
\begin{equation*}
\omega=\sqrt{\frac{g}{\ell}} \quad \text { and } \quad T=\frac{2 \pi}{\omega}=2 \pi \sqrt{\frac{\ell}{g}} \tag{6.18}
\end{equation*}
$$

Thus, for small oscillations around the equilibrium position, the pulsation $\omega$ and the oscillation period $T$ of the pendulum are independent of the initial angle $\phi_{0}$.

### 6.2.3 General oscillation period

For larger initial angles $\phi_{0}$, the expression of the oscillation period $T$ depends on the initial angle $\phi_{0}$. To determine the general expression of the oscillation period $T$, we multiply the motion equation $(6.15)$ by $\dot{\phi}$ which yields,

$$
\begin{equation*}
\dot{\phi} \ddot{\phi}+\frac{g}{\ell} \dot{\phi} \sin \phi=0 \tag{6.19}
\end{equation*}
$$

According to the definition (1.13) of the time derivative of a functional, equation (6.19) can be recast as a time derivative,

$$
\begin{equation*}
\frac{d}{d t}\left(\frac{1}{2} \dot{\phi}^{2}-\frac{g}{\ell} \cos \phi\right)=0 \tag{6.20}
\end{equation*}
$$

The indefinite integral of equation (6.20) over time is written as,

$$
\begin{equation*}
\frac{1}{2} \dot{\phi}^{2}-\frac{g}{\ell} \cos \phi=\text { const } \tag{6.21}
\end{equation*}
$$

To determine the integration constant, we substitute the initial conditions on the angle and the angular velocity,

$$
\begin{equation*}
\phi(0)=\phi_{0} \quad \text { and } \quad \dot{\phi}(0)=0 \tag{6.22}
\end{equation*}
$$

Motion independent of the mass
into equation (6.21) which implies that,

$$
\begin{equation*}
\frac{1}{2} \dot{\phi}^{2}-\frac{g}{\ell} \cos \phi=-\frac{g}{\ell} \cos \phi_{0} \tag{6.23}
\end{equation*}
$$

Since $\dot{\phi}=d \phi / d t$, we can now write the infinitesimal time interval $d t$ as a function of the infinitesimal angle variation $d \phi$

$$
\begin{equation*}
d t=\sqrt{\frac{\ell}{2 g}} \frac{d \phi}{\sqrt{\cos \phi-\cos \phi_{0}}} \tag{6.24}
\end{equation*}
$$

The expression of the time interval between the initial time $t=0$ and the time $t$ is obtained by integration of equation (6.24) over time,

$$
\begin{equation*}
t=\int_{0}^{t} d t^{\prime}=\sqrt{\frac{\ell}{2 g}} \int_{\phi_{0}}^{\phi(t)} \frac{d \phi^{\prime}}{\sqrt{\cos \phi^{\prime}-\cos \phi_{0}}} \tag{6.25}
\end{equation*}
$$

Initially, the angular position of the pendulum is $\phi_{0}$ and after a quarter oscillation period $T / 4$, the pendulum is at the minimum at $\phi=0$. The oscillation period $T$ is the sum of four identical quarter oscillation periods,

$$
\begin{equation*}
T=4 \sqrt{\frac{\ell}{2 g}} \int_{\phi_{0}}^{0} \frac{d \phi^{\prime}}{\sqrt{\cos \phi^{\prime}-\cos \phi_{0}}} \tag{6.26}
\end{equation*}
$$

Equation (6.26) is an elliptic integral of the first kind. The resolution of this integral is lengthy and complicated. It involves notably Legendre polynomials. Finally, the solution reads,

$$
\begin{equation*}
T=2 \pi \sqrt{\frac{\ell}{g}} \sum_{n=0}^{\infty}\left[\left(\frac{(2 n)!}{\left(2^{n} n!\right)^{2}}\right)^{2} \sin ^{2 n}\left(\frac{\phi_{0}}{2}\right)\right]=2 \pi \sqrt{\frac{\ell}{g}}\left(1+\frac{1}{16} \phi_{0}^{2}+\frac{11}{3072} \phi_{0}^{4}+\mathcal{O}(6)\right) \tag{6.27}
\end{equation*}
$$

The first term in brackets in the expression (6.27) of the period $T$ corresponds to the oscillation period in the small oscillation limit, i.e. $\phi_{0} \ll 1$ (Fig. 6.5). The following term is a $2^{\text {nd }}$ order correction term in $\phi_{0}^{2}$ and the last correction term is a $4^{\text {th }}$ order correction term in $\phi_{0}^{4}$ (Tab. 6.1). We neglect higher order correction terms.

| $\phi_{0}$ | $\frac{1}{16} \phi_{0}^{2}$ | $\frac{11}{3072} \phi_{0}^{4}$ |
| :---: | :---: | :---: |
| $10^{\circ}$ | $0.19 \%$ | $0.003 \%$ |
| $30^{\circ}$ | $1.7 \%$ | $0.027 \%$ |
| $60^{\circ}$ | $6.9 \%$ | $0.43 \%$ |
| $90^{\circ}$ | $15 \%$ | $2.2 \%$ |
| $120^{\circ}$ | $27 \%$ | $6.9 \%$ |

TABLE 6.1 Correction terms
Figure 6.5 The oscillation period $T$ of the pendulum depends on the initial angular position $\phi_{0}$.

### 6.3 Power, work and kinetic energy

In this section, we shall define key notions in mechanics and more generally in physics. These notions are the power exerted by a force on a material point, the work performed by this force and the kinetic energy of the material point with respect to a given frame of reference.

### 6.3.1 Power

The power $P$ of a force $\boldsymbol{F}$ exerted on a material point is an extensive scalar quantity that accounts for the ability of the force to accelerate or slow down the material point, i.e. to modify its state of motion. The motion of the material point is described by the velocity vector $\boldsymbol{v}$ that is collinear to the motion. Since the power is a scalar quantity, it can be defined as the scalar product between the force vector $\boldsymbol{F}$ and the velocity vector $\boldsymbol{v}$,

$$
\begin{equation*}
P=\boldsymbol{F} \cdot \boldsymbol{v} \tag{6.28}
\end{equation*}
$$

The unit of power in the International system of units is the Watt denoted $\left[\mathrm{W}=\mathrm{kg} \mathrm{m}^{2} / \mathrm{s}^{3}\right]$, in the honour of James Watt who played an important role in the development of steam engines.

When the force $\boldsymbol{F}$ is applied in the direction of motion, it accelerates the material point, thus its power is positive, i.e. $P>0$. When the force $\boldsymbol{F}$ is applied in the direction opposed to the motion, it slows down the material point, thus its power is negative, i.e. $P<0$. When the force is applied in a direction that is orthogonal to the motion, its power vanishes, i.e. $P=0$.

The notion of power is extremely useful in mechanics to compare quantitatively the operation of different engines. These engines are for instance mechanical engines (Fig. 6.6) or even human muscles.

### 6.3.2 Work

The work $W_{12}$ performed by a force $\boldsymbol{F}(t)$ exerted on a material point is an extensive scalar quantity corresponding to the integral of the power exerted by this force on the material point during the time interval $\left[t_{1}, t_{2}\right]$,

$$
\begin{equation*}
W_{12}=\int_{t_{1}}^{t_{2}} P(t) d t=\int_{t_{1}}^{t_{2}} \boldsymbol{F}(t) \cdot \boldsymbol{v} d t \tag{6.29}
\end{equation*}
$$

In all generality, we consider that the force can depend on the position $\boldsymbol{r}(t)$, i.e. $\boldsymbol{F}(t) \equiv$ $\boldsymbol{F}(\boldsymbol{r}(t)) \equiv \boldsymbol{F}(\boldsymbol{r})$. Given the infinitesimal displacement $d \boldsymbol{r}=\boldsymbol{v} d t$, taking into account the definition (6.29), the work $W_{12}$ performed by a force $\boldsymbol{F}$ along the trajectory $\mathcal{C}_{12}$ between an initial position $\boldsymbol{r}\left(t_{1}\right)$ and a final position $\boldsymbol{r}\left(t_{2}\right)$ is given by the following curvilinear integral (Fig.6.7)

$$
\begin{equation*}
W_{12}=\int_{\mathcal{C}_{12}} \boldsymbol{F}(\boldsymbol{r}) \cdot d \boldsymbol{r} \tag{6.30}
\end{equation*}
$$

The unit of work in the International system of units is the Joule denoted $\left[\mathrm{J}=\mathrm{kg} \mathrm{m}^{2} / \mathrm{s}^{2}\right]$, in honour of James Prescott Joule who showed the equivalence between work and heat. As an example, we can mention the work performed by the muscular forces of a backpacker while climbing the Mont-Blanc or the work performed by the kinetic friction force while a vehicle breaks.

The infinitesimal work $\delta W$ performed by the force $\boldsymbol{F}$ is the integrand of the curvilinear
integral (6.30). By definition of the scalar product (1.28), the infinitesimal work $\delta W$ is written explicitly as,

$$
\begin{equation*}
\delta W=\boldsymbol{F} \cdot d \boldsymbol{r}=\|\boldsymbol{F}\|\|d \boldsymbol{r}\| \cos \theta \tag{6.31}
\end{equation*}
$$

where $\theta$ is the angle between the force vector $\boldsymbol{F}$ and the infinitesimal displacement vector $d \boldsymbol{r}$ (Fig. 6.8).

### 6.3.3 Kinetic energy

The kinetic energy $T$ is an extensive scalar quantity associated to the motion of a material point. In the absence of a force, the kinetic energy is a conserved quantity, i.e. it does not change over time. The motion of a material point in the absence of a force is characterised entirely by its momentum $\boldsymbol{p}$ and its velocity $\boldsymbol{v}$. The kinetic energy is a scalar quantity defined as the integral of the scalar product of the velocity vector $\boldsymbol{v}$ and of the infinitesimal variation of momentum vector $d \boldsymbol{p}$. Taking into account the expression (2.30) for the momentum $\boldsymbol{p}$ of a material point of mass $m$, the kinetic energy $T$ is written,

$$
\begin{equation*}
T=\int_{0}^{T} d T^{\prime}=\int_{0}^{\boldsymbol{p}} \boldsymbol{v} \cdot d \boldsymbol{p}^{\prime}=\frac{1}{m} \int_{0}^{\boldsymbol{p}} \boldsymbol{p}^{\prime} \cdot d \boldsymbol{p}^{\prime}=\frac{\boldsymbol{p}^{2}}{2 m}=\frac{1}{2} m \boldsymbol{v}^{2} \tag{6.32}
\end{equation*}
$$

where the prime symbol has been added on the integration variable in order not to confuse it with the integration bound. The kinetic energy unit in the International system of units is the Joule denoted $\left[\mathrm{J}=\mathrm{kg} \mathrm{m}^{2} / \mathrm{s}^{2}\right]$.

The expression (6.32) for the kinetic energy $T$ is very interesting. The kinetic energy is expressed as the product between an extensive quantity and an intensive quantity. This is the case for all the kinds of energy that are studied in the framework of thermodynamics. Since the momentum is defined up to a constant, the kinetic energy is as well. Moreover, since kinetic energy is a quadratic function of the velocity $\boldsymbol{v}$, there has to be a minimal value of the energy. In special relativity, the kinetic energy is not a quadratic function of the velocity, but it can be expressed as a linear combination of even powers of the velocity which ensures the existence of a minimum.

Historically, the concept of "vis viva" (living force in Latin) expressed as $m \boldsymbol{v}^{2}$ has been introduced first by Gottfried Wilhelm Leibniz. It is only a century and a half later that the term kinetic energy appeared in the works of Gaspard-Gustave de Coriolis with the correct factor $1 / 2$.

### 6.3.4 Kinetic energy theorem

Theorem 6.1 The work $W_{12}$ performed by the net exterior force $\boldsymbol{F}^{\text {ext }}$ on a material point of mass $m$ from an initial position $\boldsymbol{r}\left(t_{1}\right)$ to a final position $\boldsymbol{r}\left(t_{2}\right)$ is equal to the kinetic energy variation between times $t_{1}$ and $t_{2}$,

$$
\begin{equation*}
W_{12}=T_{2}-T_{1} \tag{6.33}
\end{equation*}
$$

Demonstration The definition (6.30) of work, the law of motion (2.33) and the definition (2.2) of the acceleration imply that,

$$
\begin{equation*}
W_{12}=\int_{t_{1}}^{t_{2}} \boldsymbol{F}^{\mathrm{ext}} \cdot \boldsymbol{v} d t=\int_{t_{1}}^{t_{2}} m \boldsymbol{a} \cdot \boldsymbol{v} d t=\int_{t_{1}}^{t_{2}} m \frac{d \boldsymbol{v}}{d t} \cdot \boldsymbol{v} d t \tag{6.34}
\end{equation*}
$$

Taking into account the definition (6.32) of kinetic energy, the work (6.34) can be recast as,

$$
\begin{equation*}
W_{12}=\int_{t_{1}}^{t_{2}} \frac{d}{d t}\left(\frac{1}{2} m \boldsymbol{v}^{2}\right) d t=\left.\frac{1}{2} m \boldsymbol{v}^{2}\right|_{\boldsymbol{v}=\boldsymbol{v}_{1}} ^{\boldsymbol{v}=\boldsymbol{v}_{2}}=\frac{1}{2} m \boldsymbol{v}_{2}^{2}-\frac{1}{2} m \boldsymbol{v}_{1}^{2}=T_{2}-T_{1} \tag{6.35}
\end{equation*}
$$

To conclude this section, here is a table (Tab. 6.2) summarising the physical units of the main physical quantities occurring in mechanics expressed in the International system of units. After having established a physical result, I strongly advise you - especially during the exam - to proceed to a systematic dimensional analysis, i.e. to verify the coherence of the physical units of the quantity appearing in the analytical expression of the result. This will prevent you from making avoidable mistakes and will increase significantly your final grade!

TABLE 6.2 Physical units of main mechanical quantities (International system).

| Quantity | Unit (SI) | Abbreviation |
| :---: | :---: | :---: |
| Mass | kilogram | $[\mathrm{kg}]$ |
| Length | meter | $[\mathrm{m}]$ |
| Time | second | $[\mathrm{s}]$ |
| Velocity |  | $[\mathrm{m} / \mathrm{s}]$ |
| Acceleration |  | $\left[\mathrm{m} / \mathrm{s}^{2}\right]$ |
| Force | Newton | $\left[\mathrm{N}=\mathrm{kg} \mathrm{m} / \mathrm{s}^{2}\right]$ |
| Work, kinetic energy | Joule | $\left[\mathrm{J}=\mathrm{kg} \mathrm{m}^{2} / \mathrm{s}^{2}\right]$ |
| Power | Watt | $\left[\mathrm{W}=\mathrm{kg} \mathrm{m}^{2} / \mathrm{s}^{3}\right]$ |

