# 11 

## Earth's dynamics, Foucault pendulum and system of material points

In the first section of this chapter, we will consider the earth as a rotating non-inertial frame. In the second section, we will see that the earth's rotation is highlighted by the rotation of the oscillation plane of the Foucault pendulum. Finally, we will examine in detail the pstringrties and the physical conservation laws of a system of material points.

### 11.1 Earth's dynamics

Until now, we considered the earth as a non-inertial frame of reference. Actually, the earth is not an inertial frame because it rotates on itself and its centre of mass is rotating around the sun. For many physical systems at a given time scale, we can neglect the earth's rotational motion. In this chapter, we will see that this is not always the case. To describe the earth's dynamics, we consider an absolute sidereal frame of reference consisting of the sun and of three fixed and non-coplanar stars. We consider a relative frame of reference in uniform rotational motion. The rotational period of the earth on itself is 1 day whereas the rotation period of the earth around the sun is 365.24 days. Thus, we can neglect the norm $\Omega^{\prime}=1.99 \cdot 10^{-7}\left[\mathrm{~s}^{-1}\right]$ of the rotational angular velocity of the earth around the sun with respect to the norm $\Omega=7.27 \cdot 10^{-5}\left[\mathrm{~s}^{-1}\right]$ of the rotational angular velocity of the earth on itself. The earth's dynamics is the rotational motion of the relative earthly frame of reference with respect to the absolute sidereal frame of reference. In fact, the earth is an ellipsoid of revolution with a polar radius $r_{-}=6357[\mathrm{~km}]$ that is slightly smaller than the equatorial radius $r_{+}=6378[\mathrm{~km}]$. The ellipsoid of revolution is due to the centrifugal force $\boldsymbol{F}_{c}$ that causes a flattening at the earth's poles. Since the eccentricity $e \ll 1$ of the earth's ellipsoid of revolution is very weak,

$$
\begin{equation*}
e=\sqrt{1-\frac{r_{-}^{2}}{r_{+}^{2}}}=0.08 \tag{11.1}
\end{equation*}
$$

we will now consider that the earth is a sphere of radius $r_{0}=6371[\mathrm{~km}]$ where the volume is identical to the earth's ellipsoid of revolution.

### 11.1.1 Earth's gravitational field

We consider the observer as a material point $P$ of mass $m$ at the surface of the earth. We associate the Cartesian frame $\left(O, \hat{\boldsymbol{x}}_{1}, \hat{\boldsymbol{x}}_{2}, \hat{\boldsymbol{x}}_{3}\right)$ to the sidereal absolute frame of reference and the Cartesian frame $\left(A, \hat{\boldsymbol{y}}_{1}, \hat{\boldsymbol{y}}_{2}, \hat{\boldsymbol{y}}_{3}\right)$ to the relative earthly frame of reference. The inclination angle $\theta$ of the axis $A y_{3}$ with respect to the axis $O x_{3}$ is the co-latitude defined as the complementary angle to the latitude $\lambda$, i.e. $\theta=\pi / 2-\lambda$ (Fig. 11.1).

The earth's rotational angular velocity $\boldsymbol{\Omega}$ is constant, i.e. $\dot{\boldsymbol{\Omega}}=\mathbf{0}$, and the point $A$ has a uniform circular motion, which implies that its absolute acceleration is a centripetal acceleration, i.e. $\boldsymbol{a}_{a}(A)=\boldsymbol{\Omega} \times(\boldsymbol{\Omega} \times \boldsymbol{O} \boldsymbol{A})$. Taking into account these considerations and the fact that the relative position of the material point $\boldsymbol{r}_{r}(P)=\boldsymbol{A} \boldsymbol{P}$, the equation of relative motion (10.43) reduces to,

$$
\begin{equation*}
\sum \boldsymbol{F}^{\mathrm{ext}}-m \boldsymbol{\Omega} \times(\boldsymbol{\Omega} \times(\boldsymbol{O} \boldsymbol{A}+\boldsymbol{A} \boldsymbol{P}))-2 m \boldsymbol{\Omega} \times \boldsymbol{v}_{r}(P)=m \boldsymbol{a}_{r}(P) \tag{11.2}
\end{equation*}
$$

Mécanique $\S 1.16$

The earth's gravitational field $\boldsymbol{g}_{0}$ is defined with respect to the sidereal absolute frame of reference. To obtain the expression of the apparent earthly gravitational field $\boldsymbol{g}$ expressed with respect to the relative earthly frame of reference, the material point is suspended to a string of negligible mass and reaches an equilibrium state in the earthly relative frame of reference. At equilibrium, the relative velocity and acceleration vanish, i.e. $\boldsymbol{v}_{r}(P)=\mathbf{0}$ and $\boldsymbol{a}_{r}(P)=\mathbf{0}$. The forces exerted on the material point are its weight $m \boldsymbol{g}_{0}$ and the tension in the string $\boldsymbol{T}$ where $\boldsymbol{g}_{0}$ is the gravitational field in the absence of the earth's rotation. The distance $\|\boldsymbol{A} \boldsymbol{P}\|$ between the material point $P$ and the point $A$ located at the earth's surface is negligible compared to the earth's radius $r_{0}=\|\boldsymbol{O A}\|$, i.e. $\|\boldsymbol{A P}\| \ll\|\boldsymbol{O} \boldsymbol{A}\|$ (Fig. 11.2).

Thus, at equilibrium, the earth's equation of relative motion (11.2) reduces to,

$$
\begin{equation*}
m \boldsymbol{g}_{0}+\boldsymbol{T}-m \boldsymbol{\Omega} \times(\boldsymbol{\Omega} \times \boldsymbol{O} \boldsymbol{A})=\mathbf{0} \quad \text { thus } \quad \boldsymbol{T}=-m\left(\boldsymbol{g}_{0}-\boldsymbol{\Omega} \times(\boldsymbol{\Omega} \times \boldsymbol{O} \boldsymbol{A})\right) \tag{11.3}
\end{equation*}
$$

The apparent weight $m \boldsymbol{g}$ is defined as the force that is equal and opposed to the tension in the string $\boldsymbol{T}$,

$$
\begin{equation*}
m \boldsymbol{g}=-\boldsymbol{T}=m\left(\boldsymbol{g}_{0}-\boldsymbol{\Omega} \times(\boldsymbol{\Omega} \times \boldsymbol{O} \boldsymbol{A})\right) \tag{11.4}
\end{equation*}
$$

Taking into account the equation (11.4), the apparent earthly gravitational field is written,

$$
\begin{equation*}
\boldsymbol{g}=\boldsymbol{g}_{0}-\boldsymbol{\Omega} \times(\boldsymbol{\Omega} \times \boldsymbol{O A}) \tag{11.5}
\end{equation*}
$$

The apparent earthly gravitational field $\boldsymbol{g}$ and the apparent weight $m \boldsymbol{g}$ are not oriented towards the earth's centre when the centrifugal force $-m \boldsymbol{\Omega} \times(\boldsymbol{\Omega} \times \boldsymbol{O} \boldsymbol{A})$ does not vanish. Taking into account the relations $\boldsymbol{g}_{0}-\boldsymbol{g}=-\left(g_{0}-g\right) \hat{\boldsymbol{x}}_{1}$, where $g_{0}>g$, and $\boldsymbol{\Omega} \times(\boldsymbol{\Omega} \times \boldsymbol{O} \boldsymbol{A})=$ $-r_{0} \Omega^{2} \sin \theta \hat{\boldsymbol{x}}_{1}$, the norm of the apparent earthly gravitational field $g$ is expressed in terms of the norm of the earthly gravitational field $g_{0}$ as (Fig. 11.2),

$$
\begin{equation*}
g=g_{0}-r_{0} \Omega^{2} \sin \theta=g_{0}-r_{0} \Omega^{2} \cos \lambda \tag{11.6}
\end{equation*}
$$

Thus, the gravitational field is minimal at the equator (i.e. $\lambda=0$ ) due to the action of the centrifugal force that is opposed to the gravitational force in the earthly frame of reference. It is maximal (i.e. $\lambda=\pi / 2$ ) at the poles where the centrifugal force vanishes. That's why the earth has the shape of an ellipsoid of revolution. The relative correction due to the rotation of the earth in the expression of the gravitational field is very weak,

$$
\begin{equation*}
\frac{\delta g_{0}}{g_{0}}=\frac{g_{0}-g}{g_{0}}=\frac{r_{0} \Omega^{2} \cos \lambda}{g_{0}} \leq 0.3 \% \tag{11.7}
\end{equation*}
$$

which implies that the earth is almost a sphere.

### 11.1.2 Vertical relative motion

In this section, we would like to describe the influence of the earth's rotation on an object with an initial motion along the vertical axis, i.e. a vertical shot or a free fall at the surface of the earth. To simplify the notation, the Cartesian frame associated to the earth's relative frame of reference shall be denoted $(A, \hat{\boldsymbol{x}}, \hat{\boldsymbol{y}}, \hat{\boldsymbol{z}})$ (Fig. 11.3).

The only external force is the weight $\boldsymbol{P}=m \boldsymbol{g}$ where $\boldsymbol{g}$ is the apparent gravitational field (11.5). Since the rotation occurs at constant angular velocity $\boldsymbol{\Omega}$, i.e. $\dot{\boldsymbol{\Omega}}=\mathbf{0}$, this means that the non negligible contribution of the driving force $\boldsymbol{F}_{e}=-m \boldsymbol{a}_{a}(A)=-m \boldsymbol{\Omega} \times$ $(\boldsymbol{\Omega} \times \boldsymbol{O A})$ is contained in the expression of the apparent weight $m \boldsymbol{g}$. Taking into account the expression (10.44) of the Coriolis force $\boldsymbol{F}_{C}$, the law of relative motion (10.46) is written explicitly,

$$
\begin{equation*}
m \boldsymbol{g}-2 m \boldsymbol{\Omega} \times \boldsymbol{v}_{r}(P)=m \boldsymbol{a}_{r}(P) \tag{11.8}
\end{equation*}
$$

The vectorial quantities are expressed in the Cartesian frame as,

$$
\begin{array}{ll}
\boldsymbol{\Omega}=-\Omega \cos \lambda \hat{\boldsymbol{x}}+\Omega \sin \lambda \hat{\boldsymbol{z}} & \boldsymbol{g}=-g \hat{\boldsymbol{z}}  \tag{11.9}\\
\boldsymbol{v}_{r}(P)=\dot{x} \hat{\boldsymbol{x}}+\dot{y} \hat{\boldsymbol{y}}+\dot{z} \hat{\boldsymbol{z}} & \boldsymbol{a}_{r}(P)=\ddot{x} \hat{\boldsymbol{x}}+\ddot{y} \hat{\boldsymbol{y}}+\ddot{z} \hat{\boldsymbol{z}}
\end{array}
$$

Thus, the Coriolis force $\boldsymbol{F}_{C}$ is written in components as,

$$
\begin{align*}
\boldsymbol{F}_{C} & =-2 m \boldsymbol{\Omega} \times \boldsymbol{v}_{r}(P)=-2 m(-\Omega \cos \lambda \hat{\boldsymbol{x}}+\Omega \sin \lambda \hat{\boldsymbol{z}}) \times(\dot{x} \hat{\boldsymbol{x}}+\dot{y} \hat{\boldsymbol{y}}+\dot{z} \hat{\boldsymbol{z}})  \tag{11.10}\\
& =2 m \Omega \dot{y} \sin \lambda \hat{\boldsymbol{x}}-2 m \Omega(\dot{z} \cos \lambda+\dot{x} \sin \lambda) \hat{\boldsymbol{y}}+2 m \Omega \dot{y} \cos \lambda \hat{\boldsymbol{z}}
\end{align*}
$$

Taking into account expressions (11.9) and (11.10), the projections of the law of motion (11.8) along the coordinate axis $A x, A y$ and $A z$ divided by the mass $m$ are given by,

$$
\begin{align*}
& \ddot{x}=2 \Omega \dot{y} \sin \lambda \\
& \ddot{y}=-2 \Omega(\dot{z} \cos \lambda+\dot{x} \sin \lambda)  \tag{11.11}\\
& \ddot{z}=-g+2 \Omega \dot{y} \cos \lambda
\end{align*}
$$

The initial conditions on the relative position and velocity are,

$$
\begin{equation*}
\boldsymbol{r}_{r}(0)=z_{0} \hat{\boldsymbol{z}} \quad \boldsymbol{v}_{r}(0)=v_{0} \hat{\boldsymbol{z}} \tag{11.12}
\end{equation*}
$$

Taking into account the initial conditions (11.12), the velocity equations, obtained by integrating the equations of motion (11.11) with respect to time, are given by,

$$
\begin{align*}
& \dot{x}=2 \Omega y \sin \lambda \\
& \dot{y}=-2 \Omega\left(\left(z-z_{0}\right) \cos \lambda+x \sin \lambda\right)  \tag{11.13}\\
& \dot{z}=v_{0}-g t+2 \Omega y \cos \lambda
\end{align*}
$$

The substitution of the velocity equations (11.13) into the equation of motion along the axis $A y$ is written,

$$
\begin{equation*}
\ddot{y}=-2 \Omega \cos \lambda\left(v_{0}-g t+2 \Omega y \cos \lambda\right)-2 \Omega \sin \lambda(2 \Omega y \sin \lambda) \tag{11.14}
\end{equation*}
$$

Since the norm of the earth's rotational angular velocity $\Omega$ is very weak, we can neglect the terms in $\Omega^{2}$. Then, to $1^{\text {st }}$ order in $\Omega$ the equation of motion (11.14) reduces to,

$$
\begin{equation*}
\ddot{y}=-2 \Omega \cos \lambda\left(v_{0}-g t\right) \tag{11.15}
\end{equation*}
$$

Integrating the equation of motion (11.15) twice successively, taking into account the initial conditions (11.12), we obtain the position equation along the axis $A y$,

$$
\begin{equation*}
y(t)=-\Omega \cos \lambda\left(v_{0} t^{2}-\frac{1}{3} g t^{3}\right) \tag{11.16}
\end{equation*}
$$

Substituting the position equation (11.16) into the velocity equations (11.13), we obtain,

$$
\begin{equation*}
\dot{x}=-2 \Omega^{2} \sin \lambda \cos \lambda\left(v_{0} t^{2}-\frac{1}{3} g t^{3}\right) \quad \text { and } \quad \dot{z}=v_{0}-g t-2 \Omega^{2} \cos ^{2} \lambda\left(v_{0} t^{2}-\frac{1}{3} g t^{3}\right) \tag{11.17}
\end{equation*}
$$

To $1^{\text {st }}$ order in $\Omega$, the velocity equations (11.17) reduce to,

$$
\begin{equation*}
\dot{x}=0 \quad \text { and } \quad \dot{z}=v_{0}-g t \tag{11.18}
\end{equation*}
$$

The position equations along the axis $A x$ and $A z$ are obtained by integrating the velocity equations (11.18) with respect to time,

$$
\begin{equation*}
x(t)=0 \quad \text { and } \quad z(t)=z_{0}+v_{0} t-\frac{1}{2} g t^{2} \tag{11.19}
\end{equation*}
$$

Thus, to first-order in $\Omega$, the position equations in the vertical plane $A x z$ are identical to the position equations (3.15) of a ballistic motion where the earth is considered as an absolute frame of reference. The deviation due to the Coriolis force is given by the position equation (11.16) along the axis $A y$.

As an example, we consider a ball thrown vertically at the surface of the earth, i.e. $z_{0}=0$, with an initial velocity $v_{0}=10[\mathrm{~m} / \mathrm{s}]$ at a latitude $\lambda=\pi / 4$. At time $T=v_{0} / g$, the material point reaches its maximal height since its vertical velocity vanishes, i.e. $\dot{z}(T)=0$. The maximal height $z(T)$ and the lateral deviation $y(2 T)$ of the ball when it reaches the ground at time $2 T=2 v_{0} / g$ are,

$$
\begin{equation*}
z(T)=\frac{v_{0}^{2}}{2 g}=5.1[\mathrm{~m}] \quad \text { and } \quad y(2 T)=-\frac{4}{3} \frac{v_{0}^{3}}{g^{2}} \Omega \cos \lambda=-0.71[\mathrm{~mm}] \tag{11.20}
\end{equation*}
$$

Since $y(2 T)<0$, the deviation occurs towards the west. This deviation is about 4 orders of magnitude smaller than the maximal height.

### 11.1.3 Horizontal relative motion

In a horizontal plane locally parallel to the earth's surface, i.e. $z=$ const, the equations of motion (11.11) reduce to

$$
\begin{equation*}
\ddot{x}=2 \Omega \sin \lambda \dot{y} \quad \text { and } \quad \ddot{y}=-2 \Omega \sin \lambda \dot{x} \tag{11.21}
\end{equation*}
$$

The equations of motion are proportional to $\sin \lambda$ which means that the effect of the earth's rotation - described by the Coriolis force - on the horizontal motion vanishes at the equator (i.e. $\lambda=0$ ) and is maximal at the poles, i.e. (i.e. $\lambda= \pm \pi / 2$ ). According to the equations
of relative motion (11.21), the relative velocity vector $\boldsymbol{v}_{r}(P)$ and the relative acceleration vector $\boldsymbol{a}_{r}(P)$ of a material point $P$, expressed in components as,

$$
\begin{equation*}
\boldsymbol{v}_{r}(P)=\dot{x} \hat{\boldsymbol{x}}+\dot{y} \hat{\boldsymbol{y}} \quad \text { and } \quad \boldsymbol{a}_{r}(P)=\ddot{x} \hat{\boldsymbol{x}}+\ddot{y} \hat{\boldsymbol{y}} \tag{11.22}
\end{equation*}
$$

are orthogonal,

$$
\begin{equation*}
\boldsymbol{v}_{r}(P) \cdot \boldsymbol{a}_{r}(P)=\dot{x} \ddot{x}+\dot{y} \ddot{y}=0 \tag{11.23}
\end{equation*}
$$

as in the case of a circular motion. To understand the qualitative behaviour of the horizontal relative motion, we consider four particular cases (Fig. 11.4).

Taking into account the equations of motion (11.21), the trajectories of the material point $P$ in the four particular cases below are illustrated on the four quadrants (Fig. 11.4).

1. If $\lambda>0$ then $\dot{y}>0 \rightarrow \ddot{x}>0$ and $\dot{y}<0 \rightarrow \ddot{x}<0$.
2. If $\lambda>0 \quad$ then $\quad \dot{x}>0 \rightarrow \ddot{y}<0 \quad$ and $\quad \dot{x}<0 \rightarrow \ddot{y}>0$.
3. If $\lambda<0$ then $\dot{y}>0 \rightarrow \ddot{x}<0$ and $\dot{y}<0 \rightarrow \ddot{x}>0$.
4. If $\lambda<0 \quad$ then $\quad \dot{x}>0 \rightarrow \ddot{y}>0$ and $\dot{x}<0 \rightarrow \ddot{y}<0$.

Observing the qualitative trajectories of the horizontal relative motions at the earth's surface (Fig. 11.4), we see that the effect of the Coriolis force due to the earth's rotation is to deviate the trajectory of the material point $P$ in a clockwise manner in the northern hemisphere (i.e. $\lambda>0$ ) and in a counterclockwise manner in the southern hemisphere (i.e. $\lambda<0$ ). The Coriolis force is responsible for the creation of cyclones that can be easily seen on a satellite picture. In a cyclone, the trajectory of the clouds is even a spiral due to the presence of a pressure gradient between the centre and the exterior. Since the Coriolis force vanishes at the equator, the air masses are pushed from the tropical zones of the northern and southern hemispheres towards the equator - that plays the role of an attractor - which generates a tropical wind called a trade wind.

In 1851, Léon Foucault demonstrated experimentally the rotation of the earth using a pendulum suspended at the top of the dome of the Panthéon in Paris. The Foucault pendulum of the Panthéon consists of a mass $m=28[\mathrm{~kg}]$ suspended to a string of length $\ell=67[\mathrm{~m}]$. The amplitude of the oscillations is weak compared to the length of the pendulum. Taking into account the relation (6.18), the oscillation period is $T=16$ [s] (Fig. 11.5). The working principle of the pendulum is the following. With respect to the sidereal absolute frame of reference, the vertical plane of oscillation of the pendulum is fixed. Since the earth rotates on itself, the vertical plan of oscillation of the pendulum in the earthly relative frame of reference has a circular motion at constant angular velocity that depends on the latitude $\lambda$.

To describe the motion of the Foucault pendulum, we take the law of vertical relative motion (11.8) and add to the weight $m \boldsymbol{g}$ of the material point $P$ the tension $\boldsymbol{T}$ exerted on the string,

$$
\begin{equation*}
m \boldsymbol{g}+\boldsymbol{T}-2 m \boldsymbol{\Omega} \times \boldsymbol{v}_{r}(P)=m \boldsymbol{a}_{r}(P) \tag{11.24}
\end{equation*}
$$

The projections of the apparent gravitational field $\boldsymbol{g}$ and of the angular velocity $\boldsymbol{\Omega}$ in the Cartesian frame $(A, \hat{\boldsymbol{x}}, \hat{\boldsymbol{y}}, \hat{\boldsymbol{z}})$ associated to the earthly relative frame of reference are written (Fig. 11.6),

$$
\begin{equation*}
\boldsymbol{g}=g \hat{\boldsymbol{z}} \quad \text { and } \quad \boldsymbol{\Omega}=\Omega \cos \lambda \hat{\boldsymbol{y}}-\Omega \sin \lambda \hat{\boldsymbol{z}} \tag{11.25}
\end{equation*}
$$

In order to account for the symmetries of motion, we express the vectors $\hat{\boldsymbol{y}}$ and $\hat{\boldsymbol{z}}$ in terms of the vectors $\boldsymbol{e}_{r}, \boldsymbol{e}_{\theta}$ and $\boldsymbol{e}_{\phi}$ of the spherical frame attached to the material point $P$ using the cylindrical vector $\boldsymbol{e}_{\rho}$ (Fig. 11.7).

$$
\begin{align*}
& \hat{\boldsymbol{z}}=\cos \theta \boldsymbol{e}_{r}-\sin \theta \boldsymbol{e}_{\theta} \quad \text { and } \quad \boldsymbol{e}_{\rho}=\sin \theta \boldsymbol{e}_{r}+\cos \theta \boldsymbol{e}_{\theta}  \tag{11.26}\\
& \hat{\boldsymbol{y}}=\cos \phi \hat{\boldsymbol{e}}_{\phi}+\sin \phi \boldsymbol{e}_{\rho}=\sin \phi \sin \theta \boldsymbol{e}_{r}+\sin \phi \cos \theta \boldsymbol{e}_{\theta}+\cos \phi \boldsymbol{e}_{\phi}
\end{align*}
$$

There are two geometrical constraints, namely that the length $\ell$ of the pendulum is a constant and that the rotational angular velocity $\dot{\phi}$ of the vertical oscillation plane is a constant,

$$
\begin{array}{lllll}
r=\ell=\text { const } & \text { thus } & \dot{r}=0 & \text { and } & \ddot{r}=0 \\
\dot{\phi}=\text { const } & \text { thus } & \ddot{\phi}=0 & & \tag{https://cdn.mathpix.com/cropped/2024_05_18_a6e4f050ed236177a3e1g-07.jpg?height=49&width=112&top_left_y=1146&top_left_x=1463}
\end{array}
$$

Since the oscillation angle $\theta$ is small and that the angular velocities $\Omega$ and $\dot{\phi}$ are also small, to $1^{\text {st }}$ order in $\theta, \Omega$ and $\dot{\phi}$, we neglect the $2^{\text {nd }}$ order terms, namely the terms in $\theta^{2}, \Omega^{2}, \dot{\phi}^{2}$, $\theta \Omega, \theta \dot{\phi}$ and $\Omega \dot{\phi}$. Moreover, to $1^{\text {st }}$ order, $\sin \theta=\theta$ and $\cos \theta=1$. Thus, the vectors (11.26) reduce to $1^{\text {st }}$ order to,

$$
\begin{equation*}
\hat{\boldsymbol{z}}=\boldsymbol{e}_{r}-\theta \boldsymbol{e}_{\theta} \quad \text { and } \quad \hat{\boldsymbol{y}}=\theta \sin \phi \boldsymbol{e}_{r}+\sin \phi \boldsymbol{e}_{\theta}+\cos \phi \boldsymbol{e}_{\phi} \tag{11.28}
\end{equation*}
$$

Taking into account the expressions (11.28), the vectors (11.25) and the tension in the string $\boldsymbol{T}$ are expressed to $1^{\text {st }}$ order as,

$$
\begin{align*}
& \boldsymbol{g}=g \boldsymbol{e}_{r}-g \theta \boldsymbol{e}_{\theta} \quad \text { and } \quad \boldsymbol{T}=-T \boldsymbol{e}_{r} \\
& \boldsymbol{\Omega}=\Omega \cos \lambda\left(\underline{\theta \sin \phi \overline{\boldsymbol{e}_{r}}}+\sin \phi \boldsymbol{e}_{\theta}+\cos \phi \boldsymbol{e}_{\phi}\right)-\Omega \sin \lambda\left(\boldsymbol{e}_{r}-\theta \widehat{\boldsymbol{e}_{\theta}}\right)  \tag{11.29}\\
& =-\Omega \sin \lambda \boldsymbol{e}_{r}+\Omega \cos \lambda \sin \phi \boldsymbol{e}_{\theta}+\Omega \cos \lambda \cos \phi \boldsymbol{e}_{\phi}
\end{align*}
$$

Taking into account the constraints (11.27), the relative velocity vector (5.18) and the relative acceleration vector (5.20) reduce to $1^{\text {st }}$ order to,

$$
\begin{equation*}
\boldsymbol{v}_{r}(P)=\ell \dot{\theta} \boldsymbol{e}_{\theta} \quad \text { and } \quad \boldsymbol{a}_{r}(P)=-\ell \dot{\theta}^{2} \boldsymbol{e}_{r}+\ell \ddot{\theta} \boldsymbol{e}_{\theta}+2 \ell \dot{\theta} \dot{\phi} \boldsymbol{e}_{\phi} \tag{11.30}
\end{equation*}
$$

Thus, taking into account expressions (11.29) and (11.30), the Coriolis force $\boldsymbol{F}_{C}$ is expressed to $1^{\text {st }}$ order as,

$$
\begin{align*}
& \boldsymbol{F}_{C}=-2 m \boldsymbol{\Omega} \times \boldsymbol{v}_{r}(P)=-2 m\left(-\Omega \sin \lambda \boldsymbol{e}_{r}+\underline{\Omega} \cos \lambda \sin \phi \overline{\boldsymbol{e}_{\theta}}+\Omega \cos \lambda \cos \phi \boldsymbol{e}_{\phi}\right) \times \ell \dot{\theta} \boldsymbol{e}_{\theta} \\
& =2 m \ell \dot{\theta} \Omega \cos \lambda \cos \phi \boldsymbol{e}_{r}+2 m \ell \dot{\theta} \Omega \sin \lambda \boldsymbol{e}_{\phi} \tag{11.31}
\end{align*}
$$

Substituting the expressions of the vectorial quantities (11.29), (11.30) and (11.31) into the equation of relative motion (11.24) and projecting it along the coordinate axes collinear to the vectors $\boldsymbol{e}_{r}, \boldsymbol{e}_{\theta}$ and $\boldsymbol{e}_{\phi}$ respectively, we obtain the three scalar equations,

$$
\begin{align*}
& m g-T+2 m \ell \dot{\theta} \Omega \cos \lambda \cos \phi=-m \ell \dot{\theta}^{2} \\
& -m g \theta=m \ell \ddot{\theta}  \tag{11.32}\\
& 2 m \ell \dot{\theta} \Omega \sin \lambda=2 m \ell \dot{\theta} \dot{\phi}
\end{align*}
$$

The first equation (11.32) yields the norm $T$ of the tension in the string,

$$
\begin{equation*}
T=m\left(g+\ell \dot{\theta}^{2}+2 \ell \dot{\theta} \Omega \cos \lambda \cos \phi\right) \tag{11.33}
\end{equation*}
$$

where the second term accounts for the centrifugal force due to the oscillation of the pendulum and the last term accounts for the Coriolis force due to the oscillation of the pendulum and to the earth's rotation. The second equation (11.32) is the equation of an harmonic oscillatory motion of small amplitude around the equilibrium position $\theta=0$,

$$
\begin{equation*}
\ddot{\theta}+\omega^{2} \theta=0 \quad \text { where } \quad \omega^{2}=\frac{g}{\ell} \tag{11.34}
\end{equation*}
$$

The last equation expresses the rotational angular velocity $\dot{\phi}$ of the vertical oscillation plane of the pendulum in terms of the rotational angular velocity $\Omega$ of the earth on itself,

$$
\begin{equation*}
\dot{\phi}=\Omega \sin \lambda \tag{11.35}
\end{equation*}
$$

Thus, the rotational velocity $\dot{\phi}$ vanishes at the equator and it is maximal at the poles where $\dot{\phi}= \pm \Omega$. The rotation of the oscillation plane changes direction when we cross the equator. In Lausanne (i.e. $\lambda=46.5^{\circ}$ ), the rotation period $T$ is,

$$
\begin{equation*}
T=\frac{2 \pi}{\dot{\phi}}=\frac{2 \pi}{\Omega \sin \lambda}=33.1[\mathrm{~h}] \tag{11.36}
\end{equation*}
$$

This means that the rotational angular velocity of the oscillation plane is $10.9^{\circ} / \mathrm{h}$ (Fig. 11.8).

### 11.3 System of material points

In chapter 9, to analyse the collisions between material points, we introduced the notion of a system consisting of a set of material points. We adopt the usual convention consisting to denote these material points by a Greek letter, for instance the index $\alpha$. The time evolution of the system of material points is determined by the motion of material points $P_{\alpha}$ of mass $m_{\alpha}$.

### 11.3.1 Centre of mass

We consider a frame of origin $O$ associated to a given frame of reference. The centre of mass or the barycentre $G$ of the system, consisting of material points $P_{\alpha}$ of mass $m_{\alpha}$, is the mean position of these material points weighted by their mass,

$$
\begin{equation*}
\boldsymbol{O} \boldsymbol{G}=\frac{1}{M} \sum_{\alpha} m_{\alpha} \boldsymbol{O} \boldsymbol{P}_{\alpha} \quad \quad \text { where } \quad M=\sum_{\alpha} m_{\alpha} \tag{11.37}
\end{equation*}
$$

Theorem 11.1 The definition (11.37) of the centre of mass $G$ of the system of material points $P_{\alpha}$ is independent of the choice of origin $O$ of the frame.

Demonstration We consider a frame of origin $O^{\prime}$ and we call $G^{\prime}$ the centre of mass of
the system of material points $P_{\alpha}$ expressed with respect to this frame. According to the definition (11.37),

$$
\begin{align*}
\boldsymbol{O}^{\prime} \boldsymbol{G}^{\prime} & =\frac{1}{M} \sum_{\alpha} m_{\alpha} \boldsymbol{O}^{\prime} \boldsymbol{P}_{\alpha}=\frac{1}{M} \sum_{\alpha} m_{\alpha}\left(\boldsymbol{O}^{\prime} \boldsymbol{O}+\boldsymbol{O} \boldsymbol{P}_{\alpha}\right) \\
& =\left(\frac{1}{M} \sum_{\alpha} m_{\alpha}\right) \boldsymbol{O}^{\prime} \boldsymbol{O}+\frac{1}{M} \sum_{\alpha} m_{\alpha} \boldsymbol{O} \boldsymbol{P}_{\alpha}=\boldsymbol{O}^{\prime} \boldsymbol{O}+\boldsymbol{O} \boldsymbol{G}=\boldsymbol{O}^{\prime} \boldsymbol{G} \tag{11.38}
\end{align*}
$$

Thus, we conclude that the centres of mass coincide, i.e. $G=G^{\prime}$.

The frame of reference where the centre of mass is at rest is called frame of reference of the centre of mass. To adopt the same convention as the one used in chapter 9 to treat the two body problem, we define the position vector of the centre of mass $\boldsymbol{R}_{G}$, the position vector $\boldsymbol{r}_{\alpha}$ and the relative position vector $\boldsymbol{r}_{\alpha}^{\prime}$ of the material point $P_{\alpha}$ as,

$$
\begin{equation*}
\boldsymbol{R}_{G}=\boldsymbol{O} \boldsymbol{G} \quad \boldsymbol{r}_{\alpha}=\boldsymbol{O} \boldsymbol{P}_{\alpha} \quad \boldsymbol{r}_{\alpha}^{\prime}=\boldsymbol{G} \boldsymbol{P}_{\alpha} \tag{11.39}
\end{equation*}
$$

Taking into account the definitions (11.39),

$$
\begin{equation*}
\boldsymbol{r}_{\alpha}=\boldsymbol{R}_{G}+\boldsymbol{r}_{\alpha}^{\prime} \quad \text { since } \quad \boldsymbol{O} \boldsymbol{P}_{\alpha}=\boldsymbol{O} \boldsymbol{G}+\boldsymbol{G} \boldsymbol{P}_{\alpha} \tag{11.40}
\end{equation*}
$$

The position of the centre of mass (11.37) can be expressed in terms of the vectors (11.39) as,

$$
\begin{equation*}
\boldsymbol{R}_{G}=\frac{1}{M} \sum_{\alpha} m_{\alpha} \boldsymbol{r}_{\alpha} \tag{11.41}
\end{equation*}
$$

Using the relations (11.40) and (11.41),

$$
\begin{equation*}
\sum_{\alpha} m_{\alpha} \boldsymbol{r}_{\alpha}^{\prime}=\sum_{\alpha} m_{\alpha}\left(\boldsymbol{r}_{\alpha}-\boldsymbol{R}_{G}\right)=\sum_{\alpha} m_{\alpha} \boldsymbol{r}_{\alpha}-M \boldsymbol{R}_{G}=\mathbf{0} \tag{11.42}
\end{equation*}
$$

The velocity vector of the centre of mass $\boldsymbol{V}_{G}$, the velocity vector $\boldsymbol{v}_{\alpha}$ and the relative velocity vector $\boldsymbol{v}_{\alpha}^{\prime}$ of the material point $P_{\alpha}$ are defined as,

$$
\begin{equation*}
\boldsymbol{V}_{G}=\dot{\boldsymbol{R}}_{G} \quad \boldsymbol{v}_{\alpha}=\dot{\boldsymbol{r}}_{\alpha} \quad \boldsymbol{v}_{\alpha}^{\prime}=\dot{\boldsymbol{r}}_{\alpha}^{\prime} \tag{11.43}
\end{equation*}
$$

Taking into account the definitions (11.43),

$$
\begin{equation*}
\boldsymbol{v}_{\alpha}=\boldsymbol{V}_{G}+\boldsymbol{v}_{\alpha}^{\prime} \quad \text { since } \quad \dot{\boldsymbol{r}}_{\alpha}=\dot{\boldsymbol{R}}_{G}+\dot{\boldsymbol{r}}_{\alpha}^{\prime} \tag{11.44}
\end{equation*}
$$

The velocity of the centre of mass is obtained by taking the time derivative of the position (11.37) of the centre of mass,

$$
\begin{equation*}
\boldsymbol{V}_{G}=\frac{1}{M} \sum_{\alpha} m_{\alpha} \boldsymbol{v}_{\alpha} \tag{11.45}
\end{equation*}
$$

Using the relations (11.44) and (11.45),

$$
\begin{equation*}
\sum_{\alpha} m_{\alpha} \boldsymbol{v}_{\alpha}^{\prime}=\sum_{\alpha} m_{\alpha}\left(\boldsymbol{v}_{\alpha}-\boldsymbol{V}_{G}\right)=\sum_{\alpha} m_{\alpha} \boldsymbol{v}_{\alpha}-M \boldsymbol{V}_{G}=\mathbf{0} \tag{11.46}
\end{equation*}
$$

The acceleration vector of the centre of mass $\boldsymbol{A}_{G}$, the acceleration vector $\boldsymbol{a}_{\alpha}$ and the relative acceleration vector $\boldsymbol{a}_{\alpha}^{\prime}$ of the material point $P_{\alpha}$ are defined as,

$$
\begin{equation*}
\boldsymbol{A}_{G}=\dot{\boldsymbol{V}}_{G} \quad \boldsymbol{a}_{\alpha}=\dot{\boldsymbol{v}}_{\alpha} \quad \boldsymbol{a}_{\alpha}^{\prime}=\dot{\boldsymbol{v}}_{\alpha}^{\prime} \tag{11.47}
\end{equation*}
$$

Taking into account the definitions (11.47),

$$
\begin{equation*}
\boldsymbol{a}_{\alpha}=\boldsymbol{A}_{G}+\boldsymbol{a}_{\alpha}^{\prime} \quad \text { since } \quad \dot{\boldsymbol{v}}_{\alpha}=\dot{\boldsymbol{V}}_{G}+\dot{\boldsymbol{v}}_{\alpha}^{\prime} \tag{11.48}
\end{equation*}
$$

The acceleration of the centre of mass is obtained by taking the time derivative of the velocity (11.45) of the centre of mass,

$$
\begin{equation*}
\boldsymbol{A}_{G}=\frac{1}{M} \sum_{\alpha} m_{\alpha} \boldsymbol{a}_{\alpha} \tag{11.49}
\end{equation*}
$$

Using the relations (11.48) and (11.49),

$$
\begin{equation*}
\sum_{\alpha} m_{\alpha} \boldsymbol{a}_{\alpha}^{\prime}=\sum_{\alpha} m_{\alpha}\left(\boldsymbol{a}_{\alpha}-\boldsymbol{A}_{G}\right)=\sum_{\alpha} m_{\alpha} \boldsymbol{a}_{\alpha}-M \boldsymbol{A}_{G}=\mathbf{0} \tag{11.50}
\end{equation*}
$$

### 11.3.2 Dynamics of a system of material points

According to the definition (2.30), the momentum of a material point $P_{\alpha}$ is written,

$$
\begin{equation*}
\boldsymbol{p}_{\alpha}=m_{\alpha} \boldsymbol{v}_{\alpha} \tag{11.51}
\end{equation*}
$$

and according to the definition (9.1), the angular momentum of the material point $P_{\alpha}$ with respect to the point $O$ is written,

$$
\begin{equation*}
\boldsymbol{L}_{O, \alpha}=\boldsymbol{O} \boldsymbol{P}_{\alpha} \times \boldsymbol{p}_{\alpha}=\boldsymbol{r}_{\alpha} \times \boldsymbol{p}_{\alpha} \tag{11.52}
\end{equation*}
$$

Newton's $2^{\text {nd }}$ law (2.19) and the angular momentum theorem (11.66) applied to the material point $P_{\alpha}$ are written,

$$
\begin{equation*}
\frac{d \boldsymbol{p}_{\alpha}}{d t}=\boldsymbol{F}_{\alpha} \quad \text { and } \quad \frac{d \boldsymbol{L}_{O, \alpha}}{d t}=\boldsymbol{\tau}_{O, \alpha} \tag{11.53}
\end{equation*}
$$

where $\boldsymbol{F}_{\alpha}$ is the net force and $\boldsymbol{\tau}_{O, \alpha}$ is net torque exerted on the material point $P_{\alpha}$. According to the definition (9.2), the torque exerted on the material point $P_{\alpha}$ is written,

$$
\begin{equation*}
\boldsymbol{\tau}_{O, \alpha}=\boldsymbol{O} \boldsymbol{P}_{\alpha} \times \boldsymbol{F}_{\alpha}=\boldsymbol{r}_{\alpha} \times \boldsymbol{F}_{\alpha} \tag{11.54}
\end{equation*}
$$

The net force $\boldsymbol{F}_{\alpha}$ and the net torque $\boldsymbol{\tau}_{O, \alpha}$ applied on the material point $P_{\alpha}$ are external to $P_{\alpha}$ but can be internal to the system of material points.

Now, we have to distinguish the forces and torques internal and external to the system of material points. For a system of material points, Newton's $3^{\text {rd }}$ law (8.1) is written,

$$
\begin{equation*}
\boldsymbol{F}^{\alpha \rightarrow \beta}=-\boldsymbol{F}^{\beta \rightarrow \alpha} \quad \forall \alpha, \beta \tag{11.55}
\end{equation*}
$$

The sum of internal forces $\boldsymbol{F}_{\alpha}^{\text {int }}$ exerted on the set of material points $P_{\alpha}$, is expressed in terms of the forces $\boldsymbol{F}^{\beta \rightarrow \alpha}$ exerted by the material points $P_{\beta}$ on the material points $P_{\alpha}$. Taking into account Newton's $3^{\text {rd }}$ law (11.55),

$$
\begin{align*}
\sum_{\alpha} \boldsymbol{F}_{\alpha}^{\mathrm{int}} & =\sum_{\alpha} \sum_{\beta \mid \beta \neq \alpha} \boldsymbol{F}^{\beta \rightarrow \alpha}=\sum_{\alpha} \sum_{\beta \mid \beta>\alpha} \boldsymbol{F}^{\beta \rightarrow \alpha}+\sum_{\alpha} \sum_{\beta \mid \beta<\alpha} \boldsymbol{F}^{\beta \rightarrow \alpha} \\
& \stackrel{\alpha \leftrightarrow}{=} \sum_{\alpha} \sum_{\beta \mid \beta>\alpha}\left(\boldsymbol{F}^{\beta \rightarrow \alpha}+\boldsymbol{F}^{\alpha \rightarrow \beta}\right)=\mathbf{0} \tag{11.56}
\end{align*}
$$

we make the reasonable assumption that the internal force $\boldsymbol{F}^{\beta \rightarrow \alpha}$ exerted by the material point $P_{\beta}$ on the material point $P_{\alpha}$ is oriented along the axis that connects these material points, which implies that,

$$
\begin{equation*}
\boldsymbol{P}_{\beta} \boldsymbol{P}_{\alpha} \times \boldsymbol{F}^{\beta \rightarrow \alpha}=\mathbf{0} \quad \forall \alpha, \beta \tag{11.57}
\end{equation*}
$$

According to the definition (11.54), the sum of the internal torques $\boldsymbol{\tau}_{O, \alpha}^{\mathrm{int}}$ exerted on the set of material points $P_{\alpha}$ evaluated with respect to the point $O$ is expressed in terms of the internal forces $\boldsymbol{F}_{\alpha}^{\text {int }}$ exerted by the set of material points $P_{\alpha}$. According to the equations (11.56), it is eventually expressed in terms of the forces $\boldsymbol{F}^{\beta \rightarrow \alpha}$ exerted by the material points $P_{\beta}$ on the material points $P_{\alpha}$. Taking into account Newton's $3^{\text {rd }}$ law (11.55) and the condition (11.57),

$$
\begin{align*}
\sum_{\alpha} \boldsymbol{\tau}_{O, \alpha}^{\mathrm{int}} & =\sum_{\alpha} \boldsymbol{O} \boldsymbol{P}_{\alpha} \times \boldsymbol{F}_{\alpha}^{\mathrm{int}}=\sum_{\alpha} \sum_{\beta \mid \beta \neq \alpha} \boldsymbol{O} \boldsymbol{P}_{\alpha} \times \boldsymbol{F}^{\beta \rightarrow \alpha} \\
& =\sum_{\alpha} \sum_{\beta \mid \beta>\alpha} \boldsymbol{O} \boldsymbol{P}_{\alpha} \times \boldsymbol{F}^{\beta \rightarrow \alpha}+\sum_{\alpha} \sum_{\beta \mid \beta<\alpha} \boldsymbol{O} \boldsymbol{P}_{\alpha} \times \boldsymbol{F}^{\beta \rightarrow \alpha} \\
& \stackrel{\alpha \leftrightarrow \beta}{=} \sum_{\alpha} \sum_{\beta \mid \beta>\alpha}\left(\boldsymbol{O} \boldsymbol{P}_{\alpha} \times \boldsymbol{F}^{\beta \rightarrow \alpha}+\boldsymbol{O} \boldsymbol{P}_{\beta} \times \boldsymbol{F}^{\alpha \rightarrow \beta}\right)  \tag{11.58}\\
& =\sum_{\alpha} \sum_{\beta \mid \beta>\alpha}\left(\boldsymbol{O} \boldsymbol{P}_{\alpha}-\boldsymbol{O} \boldsymbol{P}_{\beta}\right) \times \boldsymbol{F}^{\beta \rightarrow \alpha}=\sum_{\alpha} \sum_{\beta \mid \beta>\alpha} \boldsymbol{P}_{\beta} \boldsymbol{P}_{\alpha} \times \boldsymbol{F}^{\beta \rightarrow \alpha}=\mathbf{0}
\end{align*}
$$

The total momentum $\boldsymbol{P}$ and the total angular momentum $\boldsymbol{L}_{O}$ with respect to the point $O$ are defined as,

$$
\begin{equation*}
\boldsymbol{P}=\sum_{\alpha} \boldsymbol{p}_{\alpha} \quad \boldsymbol{L}_{O}=\sum_{\alpha} \boldsymbol{L}_{O, \alpha} \tag{11.59}
\end{equation*}
$$

Taking into account the relation (11.44) between the velocities and the expressions (11.51) and (11.46) of the momentum and of the relative momentum, the total momentum reduces to,

$$
\begin{equation*}
\boldsymbol{P}=\sum_{\alpha} m_{\alpha} \boldsymbol{v}_{\alpha}=\sum_{\alpha} m_{\alpha}\left(\boldsymbol{V}_{G}+\boldsymbol{v}_{\alpha}^{\prime}\right)=M \boldsymbol{V}_{G}+\sum_{\alpha} m_{\alpha} \boldsymbol{v}_{\alpha}^{\prime}=M \boldsymbol{V}_{G} \tag{11.60}
\end{equation*}
$$

The net external force $\boldsymbol{F}^{\text {ext }}$ and the net external torque $\boldsymbol{\tau}_{O}^{\text {ext }}$ applied on the system at point $O$ are given by,

$$
\begin{equation*}
\boldsymbol{F}^{\mathrm{ext}}=\sum_{\alpha} \boldsymbol{F}_{\alpha}^{\mathrm{ext}} \quad \boldsymbol{\tau}_{O}^{\mathrm{ext}}=\sum_{\alpha} \boldsymbol{\tau}_{O, \alpha}^{\mathrm{ext}} \tag{11.61}
\end{equation*}
$$

Theorem 11.2 The momentum theorem of a system of material points states that,

$$
\begin{equation*}
\boldsymbol{F}^{e x t}=\frac{d \boldsymbol{P}}{d t} \tag{11.62}
\end{equation*}
$$

Demonstration Taking into account equations (11.53), (11.56), (11.59) and (11.61) and the fact that the forces $\boldsymbol{F}_{\alpha}$ are either internal forces $\boldsymbol{F}_{\alpha}^{\text {int }}$ or external forces $\boldsymbol{F}_{\alpha}^{\text {ext }}$,

$$
\begin{equation*}
\frac{d \boldsymbol{P}}{d t}=\sum_{\alpha} \frac{d \boldsymbol{p}_{\alpha}}{d t}=\sum_{\alpha} \boldsymbol{F}_{\alpha}=\sum_{\alpha} \boldsymbol{F}_{\alpha}^{\mathrm{int}}+\sum_{\alpha} \boldsymbol{F}_{\alpha}^{\mathrm{ext}}=\boldsymbol{F}^{\mathrm{ext}} \tag{11.63}
\end{equation*}
$$

Theorem 11.3 For a closed system of material points, the centre of mass momentum theorem states that,

$$
\begin{equation*}
\boldsymbol{F}^{e x t}=M \boldsymbol{A}_{G} \tag{11.64}
\end{equation*}
$$

Demonstration The total mass $M$ of a closed system of material points is constant. Taking into account the expression (11.47) of the acceleration of the centre of mass and of the expression (11.60) for the momentum, the momentum theorem (11.62) is recast as,

$$
\begin{equation*}
\boldsymbol{F}^{\mathrm{ext}}=\frac{d \boldsymbol{P}}{d t}=\frac{d M}{d t} \boldsymbol{V}_{G}+M \frac{d \boldsymbol{V}_{G}}{d t}=M \boldsymbol{A}_{G} \tag{11.65}
\end{equation*}
$$

Theorem 11.4 The angular momentum theorem of a system of material points states that,

$$
\begin{equation*}
\boldsymbol{\tau}_{O}^{e x t}=\frac{d \boldsymbol{L}_{O}}{d t} \tag{11.66}
\end{equation*}
$$

Demonstration Taking into account equations (11.53), (11.58), (11.59) and (11.61) and the fact that the torques $\boldsymbol{\tau}_{O, \alpha}$ are either internal torques $\boldsymbol{\tau}_{O, \alpha}^{\text {int }}$ or external torques $\boldsymbol{\tau}_{O, \alpha}^{\text {ext }}$,

$$
\begin{equation*}
\frac{d \boldsymbol{L}_{O}}{d t}=\sum_{\alpha} \frac{d \boldsymbol{L}_{O, \alpha}}{d t}=\sum_{\alpha} \boldsymbol{\tau}_{O, \alpha}=\sum_{\alpha} \boldsymbol{\tau}_{O, \alpha}^{\mathrm{int}}+\sum_{\alpha} \boldsymbol{\tau}_{O, \alpha}^{\mathrm{ext}}=\boldsymbol{\tau}_{O}^{\mathrm{ext}} \tag{11.67}
\end{equation*}
$$

### 11.3.3 Conservation laws

The momentum theorem (11.62) and the angular momentum theorem (11.66) allow us to state two conservation laws for an isolated system. If the system is isolated or if the net external force vanishes, the momentum theorem implies that the total momentum is conserved,

$$
\begin{equation*}
\frac{d \boldsymbol{P}}{d t}=\mathbf{0} \quad \text { thus } \quad \boldsymbol{P}=\mathbf{c o n s t} \tag{11.68}
\end{equation*}
$$

which means that the total momentum is a constant of motion. If the system is isolated or if the net external torque vanishes, the angular momentum theorem implies that the total angular momentum is conserved,

$$
\begin{equation*}
\frac{d \boldsymbol{L}_{O}}{d t}=\mathbf{0} \quad \text { thus } \quad \boldsymbol{L}_{O}=\text { const } \tag{11.69}
\end{equation*}
$$

Rotating ice skater which means that the total angular momentum is a constant of motion. The conservation laws of momentum (11.68) and angular momentum go way beyond classical mechanics since they are valid in quantum mechanics and in general relativity. In fact, if the physical system is invariant under translation, the total momentum $\boldsymbol{P}$ is a constant of motion, and if it is invariant under rotation around a point $O$, the total angular momentum $\boldsymbol{L}_{O}$ is a constant of motion. As an example, we can mention the conservation of the total momentum of a system consisting of a gun and a bullet during a shot. We can also mention the conservation of total angular momentum of an ice skater during a rotational motion on the ice.

