## Angular momentum, torque and law of gravitation

In the first section of this chapter, we will define two extensive quantities that will enable us to characterise the rotational motion of a material point. These quantities are the angular momentum and the torque. In the second section, we will establish the law of universal gravitation from Kepler's laws of celestial mechanics.

### 9.1 Angular momentum and torque

In chapter 2, we defined the momentum, which is an extensive quantity that is conserved during a uniform linear motion. The quantity that is conserved during a uniform rotation motional is the angular momentum. The law of motion states that the external forces modify the state of uniform translation of a material point. The extensive quantity that modifies the state of uniform rotation of a material point is the torque.

### 9.1.1 Angular momentum

The angular momentum $\boldsymbol{L}_{O}$ is an extensive axial vector quantity, defined with respect to a point $O$ and associated to the rotational motion of a material point $P$ around $O$. The angular momentum is defined as the vectorial product of the position vector $\boldsymbol{r} \equiv \boldsymbol{O P}$ of the material point $P$ with respect to the point $O$ and of the momentum vector $\boldsymbol{p}$ (Fig. 9.1),

$$
\begin{equation*}
\boldsymbol{L}_{O}=\boldsymbol{O P} \times \boldsymbol{p}=\boldsymbol{r} \times \boldsymbol{p} \tag{9.1}
\end{equation*}
$$

The physical unit of the angular momentum in the international system of units is denoted

$\left[\mathrm{kg} \mathrm{m}^{2} / \mathrm{s}\right]$. Isaac Newton introduced the notion of areal velocity to describe a rotational motion. This velocity corresponds to the time derivative of the area swept by the position vector over time. Newton used this notion to model mathematically Kepler's $2^{\text {and }}$ law. However, the areal velocity is not an extensive quantity. It is Daniel Bernoulli who introduced an extensive quantity to characterise a rotational motion. He called this quantity a moment of rotational motion in a letter to Leonhard Euler.

### 9.1.2 Torque

The torque $\boldsymbol{\tau}_{O}$ is an extensive axial vector quantity, defined with respect to a point $O$ and associated to the action of a force $\boldsymbol{F}$ exerted on this point that modifies its state of uniform rotational motion around $O$. The torque is defined as the vector product of the position vector $\boldsymbol{r} \equiv \boldsymbol{O P}$ of the material point $P$ with respect to the point $O$ and of the force vector $\boldsymbol{F}$ (Fig. 9.2),

$$
\begin{equation*}
\boldsymbol{\tau}_{O}=\boldsymbol{O P} \times \boldsymbol{F}=\boldsymbol{r} \times \boldsymbol{F} \tag{9.2}
\end{equation*}
$$

### 9.1.3 Angular momentum theorem

Theorem 9.1 The angular momentum theorem states that the time derivative of the angular momentum $\boldsymbol{L}_{O}$ of a material point is equal to the sum of the external torques $\boldsymbol{\tau}_{O}^{\text {ext }}$ exerted on the material point,

$$
\sum \boldsymbol{\tau}_{O}^{e x t}=\frac{d \boldsymbol{L}_{O}}{d t}
$$

Demonstration Using the definition of the momentum (2.30), of the angular momentum (9.1), of the torque (9.2) as well as Newton's $2^{\text {nd }}$ law (2.19), we show that,

$$
\begin{equation*}
\frac{d \boldsymbol{L}_{O}}{d t}=\frac{d}{d t}(\boldsymbol{r} \times \boldsymbol{p})=\frac{d}{d t} \boldsymbol{r} \times \boldsymbol{p}+\boldsymbol{r} \times \frac{d}{d t} \boldsymbol{p}=\boldsymbol{v} \times m \boldsymbol{v}+\boldsymbol{r} \times \sum \boldsymbol{F}^{\mathrm{ext}}=\sum \boldsymbol{r} \times \boldsymbol{F}^{\mathrm{ext}}=\sum \boldsymbol{\tau}_{O}^{\mathrm{ext}} \tag{9.4}
\end{equation*}
$$

The angular momentum theorem (9.3) is the analog in rotation of Newton's $2^{\text {and }}$ law (2.19). It plays a very important role in rigid body dynamics.

### 9.1.4 Uniform circular motion

To illustrate the concept of angular momentum (9.1) and apply the angular momentum theorem (9.3), we consider the uniform circular motion of a material point $P$ around a point $O$. As we showed in chapter 4, the acceleration of a circular motion is a centripetal acceleration. The net force $\boldsymbol{F}$ applied on the material point $P$ is thus a radial force. Thus, according to the law of motion (2.33), taking into account the expression (4.69) of the centripetal acceleration and the definition (9.2) of the torque, we show that the net torque vanishes,

$$
\begin{equation*}
\boldsymbol{\tau}_{O}=\boldsymbol{r} \times \boldsymbol{F}=\boldsymbol{r} \times m \boldsymbol{a}=-m \omega^{2} \boldsymbol{r} \times \boldsymbol{r}=\mathbf{0} \tag{9.5}
\end{equation*}
$$

Thus, according to the angular momentum theorem (9.3), the angular momentum $\boldsymbol{L}_{O}$ of the material point with respect to the point $O$ is a constant for a uniform circular motion,

$$
\begin{equation*}
\boldsymbol{L}_{O}=\text { const } \tag{9.6}
\end{equation*}
$$

The circular motion occurs in the plane containing the position vector $\boldsymbol{r}$ and the momentum vector $\boldsymbol{p}$. According to the definition (9.1) of the angular momentum, the angular momentum vector $\boldsymbol{L}_{O}$ is orthogonal to the plane of motion. The vector $\boldsymbol{L}_{O}$ is thus collinear to the angular velocity vector $\boldsymbol{\omega}$ (Fig. 9.3).

The angular momentum is an essential concept to be able to deduce the law of universal gravitation based on Kepler's three laws.

### 9.2 Law of universal gravitation

The law of gravitation was established by Isaac Newton who based his work on Johannes Kepler's three laws of celestial mechanics. Using the very precise observations of his master Tycho Brahe, Johannes Kepler could establish the following three laws for the motion of the planets around the sun :

1) Law of orbits : The planetary orbits are ellipses where the sun is located at a focal point.
2) Law of areas : The area swept by the position vector, centred on the sun, per

Mécanique $\S 2.13$ unit of time is a constant.

3) Law of periods : The ratio of the orbital period squared divided by the semimajor axis of the ellipse cubed is a constant.

To establish the law of universal gravitation, we will use Kepler's $1^{\text {st }}$ and $3^{\text {rd }}$ laws as well as Newton's $2^{\text {nd }}$ law that contains Kepler's $2^{\text {nd }}$ law.

First, we define an inertial frame of reference consisting of the sun and three distant stars that can be considered as fixed. We take as origin $O$ the sun and choose cylindrical coordinates $(\rho, \phi, z)$ where the vertical axis $O z$ is orthogonal to the plane $z=0$ of the solar system containing the trajectory of the earth around the sun. We consider the earth as a material point of mass $m$, i.e. we do not take into account the rotational motion of the earth on itself. Taking into account the definition of the momentum (2.30), of the angular momentum (9.1), of the position vector (5.5) and of the velocity vector (5.8) in cylindrical coordinates, the angular momentum $\boldsymbol{L}_{O}$ of the earth around the sun is written,

$$
\begin{equation*}
\boldsymbol{L}_{O}=\boldsymbol{r} \times \boldsymbol{p}=m \boldsymbol{r} \times \boldsymbol{v}=m \rho \boldsymbol{e}_{\rho} \times\left(\dot{\rho} \boldsymbol{e}_{\rho}+\rho \dot{\phi} \boldsymbol{e}_{\phi}\right)=m \rho^{2} \dot{\phi} \boldsymbol{e}_{z} \equiv L \boldsymbol{e}_{z} \tag{9.7}
\end{equation*}
$$

Thus, the time derivative of the angular momentum (9.7) is written,

$$
\begin{equation*}
\frac{d \boldsymbol{L}_{O}}{d t}=m \rho(2 \dot{\rho} \dot{\phi}+\rho \ddot{\phi}) \boldsymbol{e}_{z} \tag{9.8}
\end{equation*}
$$

### 9.2.1 Kepler's $1^{\text {st }}$ law

According to Kepler's $1^{\text {st }}$ law, the motion of the earth around the sun is an ellipse where the sun, fixed at the origin, is located at a focal point. The other focal point is $O^{\prime}$. The ellipse is the locus of the points $P$ that are such that the distances $\rho$ and $\rho^{\prime}$ to the two fixed focal points $O$ and $O^{\prime}$ is a constant (Fig. 9.4).

In polar coordinates $(\rho, \phi)$, the definition of the ellipse is written explicitly as,

$$
\begin{equation*}
\rho+\rho^{\prime}=\rho+\sqrt{(\rho \sin \phi)^{2}+(2 c+\rho \cos \phi)^{2}}=2 a=\mathrm{const} \tag{9.9}
\end{equation*}
$$

where $a$ is the semi-major axis of the ellipse. Squaring equation (9.9) then simplifying it, yields the expression of the radial distance,

$$
\begin{equation*}
\rho=\frac{a\left(1-e^{2}\right)}{1+e \cos \phi} \tag{9.10}
\end{equation*}
$$

where the eccentricity of the ellipse is defined as $e=c / a$, which vanishes in the particular case where the ellipse reduces to a circle.

### 9.2.2 Newton's $2^{\text {nd }}$ law

The gravitational force $\boldsymbol{F}_{G}$ is an attractive force exerted by a material point on another. Thus, it has to be oriented along the line that connects these material points. In polar coordinates $(\rho, \phi)$, it is independent of the angle $\phi$. Thus, the gravitational force exerted by the sun on the earth is written,

$$
\begin{equation*}
\boldsymbol{F}_{G}=-F_{G}(\rho) \boldsymbol{e}_{\rho} \tag{9.11}
\end{equation*}
$$

where $F_{G}(\rho)>0$ is the norm of the gravitational force, which is a positive function of the radial distance $\rho$ that has to be determined. In order to do so, we use the law of motion (2.33) due only to the gravitational force,

$$
\begin{equation*}
\boldsymbol{F}_{G}=m \boldsymbol{a} \tag{9.12}
\end{equation*}
$$

Projecting the vectorial law of motion (9.12) along the two polar coordinate axes $\boldsymbol{e}_{\rho}$ and $\boldsymbol{e}_{\phi}$ respectively, taking into account the expression of the acceleration (5.10) and the expression (9.11) of the gravitational force, we obtain two scalar equations,

$$
\begin{align*}
-F_{G}(\rho) & =m\left(\ddot{\rho}-\rho \dot{\phi}^{2}\right) \\
0 & =m(\rho \ddot{\phi}+2 \dot{\rho} \dot{\phi}) \tag{9.13}
\end{align*}
$$

Taking into account the expressions (9.7) and (9.8), the second equation (9.13) implies that

$$
\begin{equation*}
\frac{d \boldsymbol{L}_{O}}{d t}=\mathbf{0} \quad \text { thus } \quad \boldsymbol{L}_{O}=\text { const } \quad \text { and } \quad L=\text { const } \tag{9.14}
\end{equation*}
$$

which means that the norm $L$ and the orientation $\boldsymbol{e}_{z}$ of the angular momentum vector $\boldsymbol{L}_{O}$ are constants. The angular momentum vector is thus a constant of the gravitational motion. In fact, this is a consequence of the angular momentum theorem for the system consisting of the earth and the sun. In fact, the gravitational force $\boldsymbol{F}_{G}$ is an internal force which means that there is no external torque and thus the angular momentum is a conserved quantity.

Now, we will take into account explicitly the conservation of angular momentum to recast the equation of motion. Equation (9.7) enables to express $\dot{\phi}$ as a function of $m, \rho$ and of $L$,

$$
\begin{equation*}
\dot{\phi}=\frac{L}{m \rho^{2}} \tag{9.15}
\end{equation*}
$$

Taking into account expression (9.15), the time derivative of the expression (9.10) of the radial distance is written,

$$
\begin{equation*}
\dot{\rho}=e \dot{\phi} \sin \phi \frac{a\left(1-e^{2}\right)}{(1+e \cos \phi)^{2}}=\frac{e L}{m a\left(1-e^{2}\right)} \sin \phi \tag{9.16}
\end{equation*}
$$

Taking into account expression (9.15), the time derivative of the expression (9.16) of the radial velocity is written,

$$
\begin{equation*}
\ddot{\rho}=\frac{e L}{m a\left(1-e^{2}\right)} \dot{\phi} \cos \phi=\frac{e L^{2}}{m^{2} a\left(1-e^{2}\right) \rho^{2}} \cos \phi \tag{9.17}
\end{equation*}
$$

Taking into account expressions (9.10), (9.15) and (9.17), the first equation (9.13) is recast as,

$$
\begin{equation*}
F_{G}(\rho)=m\left(\rho \dot{\phi}^{2}-\ddot{\rho}\right)=\frac{L^{2}}{m a\left(1-e^{2}\right) \rho^{2}}\left(\frac{a\left(1-e^{2}\right)}{\rho}-e \cos \phi\right)=\frac{L^{2}}{m a\left(1-e^{2}\right) \rho^{2}} \tag{9.18}
\end{equation*}
$$

Thus, the norm of the gravitational force $F_{G}(\rho)$ exerted by the sun on the earth is inversely proportional to the square of the radial distance $\rho$ separating the earth from the sun,

$$
\begin{equation*}
F_{G}(\rho)=\frac{K}{\rho^{2}} \quad \text { where } \quad K=\frac{L^{2}}{m a\left(1-e^{2}\right)}=\text { const }>0 \tag{9.19}
\end{equation*}
$$

### 9.2.3 Kepler's $3^{\text {rd }}$ law

Equation (9.15) can be recast in differential form as,

$$
\begin{equation*}
d t=\frac{m \rho^{2}}{L} d \phi \tag{9.20}
\end{equation*}
$$

Taking into account the radial distance (9.10), the orbital period $T$ is obtained by integrating the differential expression (9.20) on one revolution of the elliptic orbit,

$$
\begin{equation*}
T=\int_{0}^{T} d t=\int_{0}^{2 \pi} \frac{m \rho^{2}}{L} d \phi=\frac{m a^{2}\left(1-e^{2}\right)^{2}}{L} \int_{0}^{2 \pi} \frac{d \phi}{(1+e \cos \phi)^{2}} \tag{9.21}
\end{equation*}
$$

With a program like Mathematica, that uses the change of variables $u=\tan (\phi / 2)$ to recast the integrand of (9.21) as a rational function of $u$, we obtain the following result,

$$
\begin{equation*}
\int_{0}^{2 \pi} \frac{d \phi}{(1+e \cos \phi)^{2}}=\frac{2 \pi}{\left(1-e^{2}\right)^{3 / 2}} \tag{9.22}
\end{equation*}
$$

Kepler's $3^{\text {rd }}$ law is mathematically expressed as,

$$
\begin{equation*}
\frac{T^{2}}{a^{3}}=\mathrm{const} \tag{9.23}
\end{equation*}
$$

Taking into account equations (9.19), (9.20) and (9.22), Kepler's $3^{\text {rd }}$ law (9.23) is recast as,

$$
\begin{equation*}
\frac{T^{2}}{a^{3}}=\frac{4 \pi^{2} m^{2} a\left(1-e^{2}\right)}{L^{2}}=\frac{4 \pi^{2} m}{K}=\text { const } \quad \text { thus } \quad K \propto m \tag{9.24}
\end{equation*}
$$

Since the ratio $m / K$ has to be a constant for any value of $m$, i.e. for any planet, this means that $K$ is proportional to $m$. According to Newton's $3^{\text {rd }}$ law (8.1), the gravitational force $\boldsymbol{F}_{G}$ exerted by the sun on the earth is the opposite of the gravitational force $-\boldsymbol{F}_{G}$ exerted by the earth on the sun. According to Newton's $2^{\text {nd }}$ law (2.19), the force is proportional to the mass of the material point. Thus, the force $-\boldsymbol{F}_{G}$ exerted by the earth on the sun is proportional to the mass of the material point. Thus, the force $-\boldsymbol{F}_{G}$ exerted by the earth on the sun is proportional to the mass $M$ of the sun, i.e. $K \propto M$. Thus, the constant $K$ has to be proportional to the product of the masses,

$$
\begin{equation*}
K=G M m \quad \text { where } \quad G=6.67 \cdot 10^{11}\left[\mathrm{~m}^{3} / \mathrm{kg} \mathrm{s}^{2}\right] \tag{9.25}
\end{equation*}
$$

is the gravitational constant. The expressions (9.11), (9.19) and (9.24) yield the expression of the law of universal gravitation that we will now state.

### 9.2.4 Law of universal gravitation

The law of universal gravitation established by Isaac Newton can be stated as follows :

Two massive point particles are subjected to attractive gravitational forces that are equal and opposite, proportional to the product of the masses and inversely proportional to the square of the distance that separates them.

We locate the origin $O$ on a material point of mass $M$. The gravitational force $\boldsymbol{F}_{G}$ exerted by the material point of mass $M$ on the material point of mass $m$ is expressed mathematically as (Fig. 9.5),

$$
\begin{equation*}
\boldsymbol{F}_{G}=-\frac{G M m}{r^{2}} \hat{\boldsymbol{r}} \quad \text { where } \quad \hat{\boldsymbol{r}}=\frac{\boldsymbol{r}}{r} \tag{9.26}
\end{equation*}
$$

The gravitational force $\boldsymbol{F}_{G}$ is a central force, like the elastic force $\boldsymbol{F}_{e}$, since it is radial and always directed towards the centre. The value of the constant of universal gravitation $G$ was measured precisely by Henry Cavendish. His experiment called the Cavendish torsion balance is a torsion pendulum consisting of two small masses $m$ attached to an horizontal rod that can oscillate around a vertical axis. A mirror is fixed on the axis. Two large masses $M$ can be brought close to the two small masses. The net force consisting of the gravitational
attraction force $\boldsymbol{F}_{G}$ and of the elastic force $\boldsymbol{F}_{e}$ opposed to $\boldsymbol{F}_{G}$ gives rise to a damped harmonic oscillatory motion. The final deviation at the equilibrium position yields the value of the universal gravitational constant $G$ (Fig. 9.6).

Figure 9.6 The gravitational constant $G$ is measured using a torsion pendulum consisting of two small masses attached to a rod oscillating in a horizontal plane due to the gravitational attraction force generated by the two large masses.

### 9.2.5 Constants of motion

To establish the constants of gravitational motion, we will use the equation of motion expressed in cylindrical coordinates. Substituting relations (9.15) and (9.19) into the first equation (9.13), it can be recast as,

$$
\begin{equation*}
m \ddot{\rho}-\frac{L^{2}}{m \rho^{3}}+\frac{K}{\rho^{2}}=0 \tag{9.27}
\end{equation*}
$$

Multiplying equation (9.27) by $\dot{\rho}$, it can be recast as a time derivative,

$$
\begin{equation*}
m \ddot{\rho} \dot{\rho}-\frac{L^{2}}{m} \frac{\dot{\rho}}{\rho^{3}}+K \frac{\dot{\rho}}{\rho^{2}}=\frac{d}{d t}\left(\frac{1}{2} m \dot{\rho}^{2}+\frac{L^{2}}{2 m \rho^{2}}-\frac{K}{\rho}\right)=0 \tag{9.28}
\end{equation*}
$$

The indefinite time integral of expression (9.28) yields a constant that is the mechanical energy $E$ of the gravitational motion,

$$
\begin{equation*}
E=\frac{1}{2} m \dot{\rho}^{2}+\frac{L^{2}}{2 m \rho^{2}}-\frac{K}{\rho} \tag{9.29}
\end{equation*}
$$

Taking into account the expression (9.15) and the definition (5.8) of the velocity vector in cylindrical coordinates in the plane $z=0$, the gravitational mechanical energy (9.29) can be recast as,

$$
\begin{equation*}
E=\frac{1}{2} m\left(\dot{\rho}^{2}+\rho^{2} \dot{\phi}^{2}\right)-\frac{K}{\rho}=\frac{1}{2} m \boldsymbol{v}^{2}-\frac{K}{\rho} \tag{9.30}
\end{equation*}
$$

where the first term on the RHS is the kinetic energy $T$ of the material point of mass $m$ and the second term is its gravitational potential energy,

$$
\begin{equation*}
V_{G}=-\frac{K}{\rho}=-\frac{G M m}{\rho} \tag{9.31}
\end{equation*}
$$

according to relation $(9.25)$.

In addition to the angular momentum $\boldsymbol{L}_{O}$ and to the mechanical energy $E$, there is another vectorial constant of gravitational motion that we will now establish. Identifying expressions (9.11) and (9.12) of the gravitational force $\boldsymbol{F}_{G}$ taking into account the expression (9.19) of the norm of this force, the acceleration of the material point of mass $m$ is written,

$$
\begin{equation*}
\boldsymbol{a}=-\frac{K}{m \rho^{2}} \boldsymbol{e}_{\rho} \tag{9.32}
\end{equation*}
$$

Taking into account the expression (5.6) of the derivative of the basis vector $\dot{\boldsymbol{e}}_{\rho}$, the expression (9.7) of the angular momentum $\boldsymbol{L}_{O}$ can be recast as,

$$
\begin{equation*}
\boldsymbol{L}_{O}=m \rho \boldsymbol{e}_{\rho} \times\left(\dot{\rho} \boldsymbol{e}_{\rho}+\rho \dot{\boldsymbol{e}}_{\rho}\right)=m \rho^{2} \boldsymbol{e}_{\rho} \times \dot{\boldsymbol{e}}_{\rho} \tag{9.33}
\end{equation*}
$$

Using the vectorial identity (1.43), the vectorial product of the angular momentum vector (9.33) and of the acceleration vector (9.32) is written,

$$
\begin{equation*}
\boldsymbol{L}_{O} \times \boldsymbol{a}=-K\left(\boldsymbol{e}_{\rho} \times \dot{\boldsymbol{e}}_{\rho}\right) \times \boldsymbol{e}_{\rho}=-K \dot{\boldsymbol{e}}_{\rho} \tag{9.34}
\end{equation*}
$$

Since the angular momentum $\boldsymbol{L}_{O}$ is a constant, i.e. $\dot{\boldsymbol{L}}_{O}=\mathbf{0}$, and that the coefficient $K$ is a constant, i.e. $\dot{K}=0$, and that the acceleration is the time derivative of the velocity, i.e. $\boldsymbol{a}=\dot{\boldsymbol{v}}$, taking into account equation (9.34) we have,

$$
\begin{equation*}
\frac{d}{d t}\left(\boldsymbol{L}_{O} \times \boldsymbol{v}+K \boldsymbol{e}_{\rho}\right)=\boldsymbol{L}_{O} \times \boldsymbol{a}+K \dot{\boldsymbol{e}}_{\rho}=\mathbf{0} \tag{9.35}
\end{equation*}
$$

The indefinite integral (9.35) divided by the constant $K$ yields the eccentricity vector,

$$
\begin{equation*}
\boldsymbol{e}=\frac{1}{K} \boldsymbol{L}_{O} \times \boldsymbol{v}+\boldsymbol{e}_{\rho} \tag{9.36}
\end{equation*}
$$

that is a vector of norm equal to the eccentricity $e$ of the ellipse and of orientation parallel to the semi-major axis of the ellipse. Thus, it is a vector that accounts for the geometry of motion and that vanishes in the particular case of a circular motion. The vector $K \boldsymbol{e}$ is called the Laplace-Runge-Lenz vector. The conservation of the Laplace-Runge-Lenz vector holds for central forces that are inversely proportional to the distance squared. This is notably the case for the electrostatic force that binds the electrons to the atomic nucleus. The physicist Wolfgang Pauli used the invariance of this vector to determine the energy levels of the hydrogen atom.

### 9.2.6 Gravitational orbits

Mechanical energy (9.29) can be divided into two parts,

$$
\begin{equation*}
E=\frac{1}{2} m \dot{\rho}^{2}+V_{G}^{\mathrm{eff}} \tag{9.37}
\end{equation*}
$$

where the first term is the kinetic energy due to the radial part of motion and the second term is the effective gravitational energy $V_{G}^{\text {eff }}$ defined as,

$$
\begin{equation*}
V_{G}^{\text {eff }}=\frac{L^{2}}{2 m \rho^{2}}-\frac{K}{\rho} \tag{9.38}
\end{equation*}
$$

The first term on the RHS of expression (9.38) is a repulsive term called the gravitational potential barrier and the second term is an attractive term that is the gravitational potential energy $V_{G}$. The geometric shape of the gravitational orbit of a material point depends crucially on the numerical value of the effective gravitational energy $V_{G}^{\text {eff }}$. The asymptotic values of the effective gravitational potential energy $V_{G}^{\text {eff }}$ are,

$$
\begin{equation*}
\lim _{\rho \rightarrow \infty} V_{G}^{\text {eff }}=\lim _{\rho \rightarrow \infty}-\frac{K}{\rho}=-0 \quad \text { and } \quad \lim _{\rho \rightarrow 0} V_{G}^{\text {eff }}=\lim _{\rho \rightarrow \infty} \frac{L^{2}}{2 m \rho^{2}}=+\infty \tag{9.39}
\end{equation*}
$$

According to relation (9.37), the radial coordinate $\rho$ is an extremum, i.e. $\dot{\rho}=0$, when $E=V_{G}^{\text {eff }}$. Thus, there are four types of orbits that depend on the value of the mechanical energy $E$ (Fig. 9.7) :

A) Circular orbit $(e=0): E<0$ and $\rho_{\min }=\rho=\rho_{\max }$.

B) Elliptic orbit $(0<e<1): E<0$ and $\rho_{\min }<\rho<\rho_{\max }$.

C) Parabolic orbit $(e=1): E=0$ and $\rho_{\min }<\rho$.

D) Hyperbolic orbit $(e>1): E>0$ and $\rho_{\min }<\rho$.

The circular and elliptic orbits correspond to bound states (i.e. $E<0$ ) and the parabolic and hyperbolic orbits correspond to diffusion states (i.e. $E \geq 0$ ). As example of bound states, we can mention the motion of planets around the sun or of the earth around the sun or of the moon around the earth. As examples of diffusion states, we can mention the motion of certain asteroids and certain comets that go through the solar system without remaining there.

