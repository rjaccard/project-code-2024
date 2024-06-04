## Variable-mass system and non-inertial frames of reference

In the first part of this chapter, we will examine variable-mass systems. In the second section, we will study the dynamics of a material point in a non-inertial frame of reference. Finally, in the last part, we will discuss a few examples of motions described with respect to a non-inertial frame of reference.

### 10.1 Variable-mass system

A variable-mass system is a system with a mass $m(t)$ that varies over time. A variablemass system is an open system, which means that it exchanges matter, or mass, with the exterior. There are many different variable-mass systems. For instance, let us mention the case of a bath that is being filled or emptied, a chain that falls progressively in a container or a rocket that takes off. In chapter 2 , we stated Newton's $2^{\text {nd }}$ law and then we deduced from it an expression of the law of motion (2.33) for a material point of constant mass. Since the mass is varying, we will have to take that explicitly into account, i.e. we will base our analysis on the general form (2.19) of Newton's $2^{\text {nd }}$ law.

### 10.1.1 Thrust of a rocket

We consider a variable-mass system consisting of a rocket and of its fuel. The gas are ejected with an relative ejection velocity $\boldsymbol{u}$ measured with respect to the frame of reference of the rocket, i.e. it is opposed to the velocity $\boldsymbol{v}$ of the rocket, i.e. $\boldsymbol{u} \cdot \boldsymbol{v}<0$. We consider the evolution of the system during an infinitesimal time interval $d t$. Taking into account the identity (1.18), the mass $m(t+d t)$ of the rocket is written,

$$
\begin{equation*}
m(t+d t)=m(t)+d m \quad \text { where } \quad d m=\frac{d m}{d t} d t<0 \tag{10.1}
\end{equation*}
$$

and $d m<0$ is the mass variation of the rocket due to the ejection of the gas. The momentum $\boldsymbol{p}(t+d t)$ of the system consisting of the rocket and the gas is written to $1^{\text {st }}$ order,

$$
\begin{equation*}
\boldsymbol{p}(t+d t)=\underbrace{(m(t)+d m)(\boldsymbol{v}(t)+d \boldsymbol{v})}_{\text {rocket }}+\underbrace{(-d m)(\boldsymbol{v}+\boldsymbol{u})}_{\text {gas }}=m(t) \boldsymbol{v}(t)+m(t) d \boldsymbol{v}-d m \boldsymbol{u} \tag{10.2}
\end{equation*}
$$

where we neglected the term $d m d \boldsymbol{v}$ that is of $2^{\text {nd }}$ order. Taking into account the definition of the momentum (2.30) and the expression (10.2), the infinitesimal variation of momentum $d \boldsymbol{p}$ is given by,

$$
\begin{equation*}
d \boldsymbol{p}=\boldsymbol{p}(t+d t)-\boldsymbol{p}(t)=m(t) d \boldsymbol{v}-d m \boldsymbol{u} \tag{10.3}
\end{equation*}
$$

Substituting expression (10.3) into Newton's $2^{\text {nd }}$ law, we obtain,

$$
\begin{equation*}
\sum \boldsymbol{F}^{\mathrm{ext}}=m \frac{d \boldsymbol{v}}{d t}-\frac{d m}{d t} \boldsymbol{u} \tag{10.4}
\end{equation*}
$$

Taking into account the definition of the acceleration vector (2.2), the law of motion (10.4) can be recast as (Fig. 10.1),

$$
\begin{equation*}
\sum \boldsymbol{F}^{\mathrm{ext}}+\frac{d m}{d t} \boldsymbol{u}=m \boldsymbol{a} \tag{10.5}
\end{equation*}
$$

In the particular case where the air friction is negligible, the only external force acting on the rocket is its weight $\boldsymbol{P}$. Thus, the law of motion (10.5) reduces to,

$$
\begin{equation*}
\boldsymbol{P}+\frac{d m}{d t} \boldsymbol{u}=m \boldsymbol{a} \tag{10.6}
\end{equation*}
$$

The second term on the LHS $\frac{d m}{d t} \boldsymbol{u}$ is a force called the thrust that is opposed to the weight $\boldsymbol{P}$ and sets the rocket in motion. Indeed, the velocity vector $\boldsymbol{u}$ is opposed to the motion and $d m / d t<0$, thus the thrust is oriented in the direction of motion.

The thrust allows a physics teacher to be propelled on a tricycle while he empties a $\mathrm{CO}_{2}$ tank. The thrust increases the apparent weight of a chain that falls at constant speed into a container (Fig. 10.2).

### 10.1.2 Takeoff condition and velocity

We will consider the particular case where the ejection velocity of the gas $\boldsymbol{u}$ with respect to the frame of reference of the rocket is constant and oriented downwards. We consider a vertical takeoff of the rocket along the axis $O z$ centred on the launching ramp and oriented positively upwards. The projections of the vectorial quantities along the vertical axis are written,

$$
\begin{align*}
& \boldsymbol{P}=m \boldsymbol{g}=-m g \boldsymbol{e}_{z} \\
& \boldsymbol{u}=-u \boldsymbol{e}_{z}  \tag{10.7}\\
& \boldsymbol{a}=\ddot{z} \boldsymbol{e}_{z}
\end{align*}
$$

The projection of the law of motion (10.6) along the vertical coordinate axis yields,

$$
\begin{equation*}
-m g-\frac{d m}{d t} u=m \ddot{z} \tag{10.8}
\end{equation*}
$$

For the rocket to takeoff at the initial time $t=0$, the vertical acceleration needs to be positive,

$$
\begin{equation*}
\ddot{z}(0)>0 \quad \text { thus } \quad\left|\frac{d m}{d t}(0)\right|>\frac{m(0) g}{u} \tag{10.9}
\end{equation*}
$$

which implies that the outflow of burned gas needs to be sufficient. In order to obtain the equation for the speed as a function of time, the equation of motion (10.8) is recast as,

$$
\begin{equation*}
d \dot{z}(t)=-g d t-u \frac{d m(t)}{m(t)} \tag{10.10}
\end{equation*}
$$

The integral of equation (10.10) over time is written explicitly,

$$
\begin{equation*}
\int_{0}^{v(t)} d \dot{z}\left(t^{\prime}\right)=-g \int_{0}^{t} d t^{\prime}-u \int_{m(0)}^{m(t)} \frac{d m^{\prime}\left(t^{\prime}\right)}{m^{\prime}\left(t^{\prime}\right)} \tag{10.11}
\end{equation*}
$$

The solution of the integral (10.11) is,

$$
\begin{equation*}
v(t)=-g t-u \ln \left(\frac{m(t)}{m(0)}\right) \tag{10.12}
\end{equation*}
$$

where the argument of the logarithm is positive and inferior to 1 because the mass of the rocket diminishes, which implies that the logarithm is negative. Thus for a sufficiently small time, the second term dominates and the speed $v(t)$ is positive. Now, we assume that the mass $m(t)$ of the rocket is equal to the sum of the mass $M$ without fuel and of the fuel mass that decreases exponentially according to,

$$
\begin{equation*}
m(t)=M+(m(0)-M) e^{-t / \tau} \tag{10.13}
\end{equation*}
$$

The asymptotic values of the mass $m(t)$ are given by (Fig. 10.3),

$$
\begin{equation*}
\lim _{t \rightarrow 0} m(t)=m(0) \quad \text { and } \quad \lim _{t \rightarrow \infty} m(t)=M \tag{10.14}
\end{equation*}
$$

The substitution of the expression (10.13) of the mass $m(t)$ into the expression (10.12) yields,

$$
\begin{equation*}
v(t)=-g t-u \ln \left(\frac{M}{m(0)}+\left(1-\frac{M}{m(0)}\right) e^{-t / \tau}\right) \tag{10.15}
\end{equation*}
$$

### 10.2 Non-inertial frames of reference

In chapter 2, we defined an inertial frame of reference using Newton's $1^{\text {st }}$ law. Then, we showed that Newton's $2^{\text {nd }}$ law is the same for all the inertial frames of reference. Now we would like to extend our analysis to non-inertial frames of reference defined by the fact that the material points of this frame of reference are accelerating with respect to
the material points of an inertial frame of reference. In particular, we would like to know what is the expression of Newton's $2^{\text {nd }}$ law in a non-inertial frame of reference. This is very important in practice. How would we describe the motion of a material point in a car that takes a turn? What is the motion of a pendulum in an accelerating train? To answer these questions, we will now describe the dynamics of a material in a non-inertial frame of reference. For instance, in the frame of reference of a rotating water jet, the trajectory of the water - filmed by a rotating camera - is a curve (Fig. 10.4). This is due to the action of forces called inertial forces.

### 10.2.1 Relative position

To describe a motion with respect to an non-inertial frame, the inertial frame with respect to which the absolute motion of a material point is described is called the absolute frame of reference. The non-inertial frame with respect to which the relative motion of a material point is described is called the relative frame of reference. The dynamics of the material point $P$ with respect to the absolute frame of reference is described using the Cartesian frame $\left(O, \hat{\boldsymbol{x}}_{1}, \hat{\boldsymbol{x}}_{2}, \hat{\boldsymbol{x}}_{3}\right)$ of origin $O$ and its dynamics with respect to the relative frame of reference is described using the Cartesian frame $\left(A, \hat{\boldsymbol{y}}_{1}, \hat{\boldsymbol{y}}_{2}, \hat{\boldsymbol{y}}_{3}\right)$ of origin $A$.

The absolute position $\boldsymbol{r}_{a}(P)$ and the relative position $\boldsymbol{r}_{r}(P)$ of the material point $P$ are defined as (Fig. 10.5)

$$
\begin{equation*}
\boldsymbol{r}_{a}(P)=\boldsymbol{O} \boldsymbol{P}=\sum_{i=1}^{3} x_{i} \hat{\boldsymbol{x}}_{i} \quad \text { and } \quad \boldsymbol{r}_{r}(P)=\boldsymbol{A} \boldsymbol{P}=\sum_{i=1}^{3} y_{i} \hat{\boldsymbol{y}}_{i} \tag{10.16}
\end{equation*}
$$

and the absolute position of the point $A$ is written $\boldsymbol{r}_{a}(A)=\boldsymbol{O} \boldsymbol{A}$. Thus, as $\boldsymbol{O P}=\boldsymbol{O} \boldsymbol{A}+\boldsymbol{A} \boldsymbol{P}$, the absolute position of the material point $P$ is related to its relative position by,

$$
\begin{equation*}
\boldsymbol{r}_{a}(P)=\boldsymbol{r}_{a}(A)+\boldsymbol{r}_{r}(P) \tag{https://cdn.mathpix.com/cropped/2024_05_18_03953ee7979e7967f125g-05.jpg?height=52&width=114&top_left_y=308&top_left_x=1462}
\end{equation*}
$$

### 10.2.2 Relative velocity

In all generality, the Cartesian frame $\left(O, \hat{\boldsymbol{x}}_{1}, \hat{\boldsymbol{x}}_{2}, \hat{\boldsymbol{x}}_{3}\right)$ is at rest and the Cartesian frame $\left(A, \hat{\boldsymbol{y}}_{1}, \hat{\boldsymbol{y}}_{2}, \hat{\boldsymbol{y}}_{3}\right)$ is rotating at angular velocity $\boldsymbol{\Omega}$ with respect to the Cartesian frame $\left(O, \hat{\boldsymbol{x}}_{1}, \hat{\boldsymbol{x}}_{2}, \hat{\boldsymbol{x}}_{3}\right)$. Taking into account the Poisson formulae (5.33), the time derivatives of the basis vectors are written,

$$
\begin{equation*}
\dot{\hat{\boldsymbol{x}}}_{i}=\mathbf{0} \quad \text { and } \quad \dot{\hat{\boldsymbol{y}}}_{i}=\boldsymbol{\Omega} \times \hat{\boldsymbol{y}}_{i} \quad \forall i=1,2,3 \tag{10.18}
\end{equation*}
$$

The time derivative of equation (10.17) is written,

$$
\begin{equation*}
\dot{\boldsymbol{r}}_{a}(P)=\dot{\boldsymbol{r}}_{a}(A)+\dot{\boldsymbol{r}}_{r}(P) \tag{https://cdn.mathpix.com/cropped/2024_05_18_03953ee7979e7967f125g-05.jpg?height=51&width=114&top_left_y=834&top_left_x=1462}
\end{equation*}
$$

Taking into account relations (10.16),

$$
\begin{equation*}
\dot{\boldsymbol{r}}_{a}(P)=\sum_{i=1}^{3} \dot{x}_{i} \hat{\boldsymbol{x}}_{i} \quad \text { and } \quad \dot{\boldsymbol{r}}_{r}(P)=\sum_{i=1}^{3} \dot{y}_{i} \hat{\boldsymbol{y}}_{i}+\sum_{i=1}^{3} y_{i} \dot{\hat{\boldsymbol{y}}}_{i} \tag{https://cdn.mathpix.com/cropped/2024_05_18_03953ee7979e7967f125g-05.jpg?height=54&width=114&top_left_y=1001&top_left_x=1462}
\end{equation*}
$$

According to relations (10.16) and (10.18), the last term on the RHS of the second equation (10.20) can be recast as,

$$
\begin{equation*}
\sum_{i=1}^{3} y_{i} \dot{\hat{\boldsymbol{y}}}_{i}=\sum_{i=1}^{3} y_{i}\left(\boldsymbol{\Omega} \times \hat{\boldsymbol{y}}_{i}\right)=\boldsymbol{\Omega} \times\left(\sum_{i=1}^{3} y_{i} \hat{\boldsymbol{y}}_{i}\right)=\boldsymbol{\Omega} \times \boldsymbol{r}_{r}(P) \tag{10.21}
\end{equation*}
$$

The absolute velocity $\boldsymbol{v}_{a}(P)$ and the relative velocity $\boldsymbol{v}_{r}(P)$ of the material point $P$ are defined as,

$$
\begin{equation*}
\boldsymbol{v}_{a}(P)=\sum_{i=1}^{3} \dot{x}_{i} \hat{\boldsymbol{x}}_{i} \quad \text { and } \quad \boldsymbol{v}_{r}(P)=\sum_{i=1}^{3} \dot{y}_{i} \hat{\boldsymbol{y}}_{i} \tag{10.22}
\end{equation*}
$$

Taking into account equation (10.21) and the definitions (10.22), the time derivative of the positions (10.20) become,

$$
\begin{equation*}
\dot{\boldsymbol{r}}_{a}(P)=\boldsymbol{v}_{a}(P) \quad \text { and } \quad \dot{\boldsymbol{r}}_{r}(P)=\boldsymbol{v}_{r}(P)+\boldsymbol{\Omega} \times \boldsymbol{r}_{r}(P) \tag{10.23}
\end{equation*}
$$

Substituting equations (10.23) and the absolute velocity of point $A$, that is written $\boldsymbol{v}_{a}(A)=$ $\dot{\boldsymbol{r}}_{a}(A)$, into equation (10.19), we obtain the following velocity identity,

$$
\begin{equation*}
\boldsymbol{v}_{a}(P)=\boldsymbol{v}_{a}(A)+\boldsymbol{v}_{r}(P)+\boldsymbol{\Omega} \times \boldsymbol{r}_{r}(P) \tag{https://cdn.mathpix.com/cropped/2024_05_18_03953ee7979e7967f125g-05.jpg?height=49&width=114&top_left_y=1866&top_left_x=1462}
\end{equation*}
$$

The driving velocity $\boldsymbol{v}_{e}(P)$ of the material point $P$ is defined as the velocity that the material point would have if it were fixed in the non-inertial frame, i.e. if $\boldsymbol{v}_{r}(P)=\mathbf{0}$,

$$
\begin{equation*}
\boldsymbol{v}_{e}(P)=\boldsymbol{v}_{a}(A)+\boldsymbol{\Omega} \times \boldsymbol{r}_{r}(P) \tag{10.25}
\end{equation*}
$$

Thus, the absolute velocity (10.24) of the material point $P$ can be written,

$$
\begin{equation*}
\boldsymbol{v}_{a}(P)=\boldsymbol{v}_{e}(P)+\boldsymbol{v}_{r}(P) \tag{10.26}
\end{equation*}
$$

Theorem 10.1 The angular velocity $\boldsymbol{\Omega}$ is independent of the choice of material point $A$ fixed with respect to the relative frame, and taken as origin of the relative Cartesian frame.

Demonstration Using the definition (10.16), the velocity identity (10.24) is recast as,

$$
\begin{equation*}
\boldsymbol{v}_{a}(P)=\boldsymbol{v}_{a}(A)+\boldsymbol{v}_{r}(P)+\boldsymbol{\Omega} \times \boldsymbol{A} \boldsymbol{P} \tag{10.27}
\end{equation*}
$$

We consider another material point $B$ fixed with respect to the relative frame of reference, which means that its relative velocity vanishes, i.e. $\boldsymbol{v}_{r}(B)=\mathbf{0}$. Thus, for the material point $B$, the velocity identity (10.27) reduces to,

$$
\begin{equation*}
\boldsymbol{v}_{a}(B)=\boldsymbol{v}_{a}(A)+\boldsymbol{\Omega} \times \boldsymbol{A} \boldsymbol{B} \quad \text { thus } \quad \boldsymbol{v}_{a}(A)=\boldsymbol{v}_{a}(B)+\boldsymbol{\Omega} \times \boldsymbol{B} \boldsymbol{A} \tag{10.28}
\end{equation*}
$$

Substituting equation (10.28) into equation (10.27), we obtain,

$$
\begin{equation*}
\boldsymbol{v}_{a}(P)=\boldsymbol{v}_{a}(B)+\boldsymbol{v}_{r}(P)+\boldsymbol{\Omega} \times \boldsymbol{B} \boldsymbol{A}+\boldsymbol{\Omega} \times \boldsymbol{A} \boldsymbol{P}=\boldsymbol{v}_{a}(B)+\boldsymbol{v}_{r}(P)+\boldsymbol{\Omega} \times(\boldsymbol{B} \boldsymbol{A}+\boldsymbol{A} \boldsymbol{P}) \tag{10.29}
\end{equation*}
$$

and taking into account the vectorial identity $\boldsymbol{B} \boldsymbol{P}=\boldsymbol{B} \boldsymbol{A}+\boldsymbol{A} \boldsymbol{P}$, it reduces to,

$$
\begin{equation*}
\boldsymbol{v}_{a}(P)=\boldsymbol{v}_{a}(B)+\boldsymbol{v}_{r}(P)+\boldsymbol{\Omega} \times \boldsymbol{B} \boldsymbol{P} \tag{10.30}
\end{equation*}
$$

Replacing the material point $A$ by the material point $B$ in the velocity identity (10.27), we obtain the velocity identity (10.30) without changing the angular velocity vector $\boldsymbol{\Omega}$.

### 10.2.3 Relative acceleration

The time derivative of equation (10.24) is written,

$$
\begin{equation*}
\dot{\boldsymbol{v}}_{a}(P)=\dot{\boldsymbol{v}}_{a}(A)+\dot{\boldsymbol{v}}_{r}(P)+\boldsymbol{\Omega} \times \dot{\boldsymbol{r}}_{r}(P)+\dot{\boldsymbol{\Omega}} \times \boldsymbol{r}_{r}(P) \tag{https://cdn.mathpix.com/cropped/2024_05_18_03953ee7979e7967f125g-06.jpg?height=49&width=108&top_left_y=781&top_left_x=1762}
\end{equation*}
$$

Taking into account relations (10.22),

$$
\begin{equation*}
\dot{\boldsymbol{v}}_{a}(P)=\sum_{i=1}^{3} \ddot{x}_{i} \hat{\boldsymbol{x}}_{i} \quad \text { and } \quad \dot{\boldsymbol{v}}_{r}(P)=\sum_{i=1}^{3} \ddot{y}_{i} \hat{\boldsymbol{y}}_{i}+\sum_{i=1}^{3} \dot{y}_{i} \dot{\hat{\boldsymbol{y}}}_{i} \tag{https://cdn.mathpix.com/cropped/2024_05_18_03953ee7979e7967f125g-06.jpg?height=45&width=108&top_left_y=957&top_left_x=1762}
\end{equation*}
$$

According to the relations (10.22) and (10.18), the last term on the RHS of the second equation (10.32) can be recast as,

$$
\begin{equation*}
\sum_{i=1}^{3} \dot{y}_{i} \dot{\hat{\boldsymbol{y}}}_{i}=\sum_{i=1}^{3} \dot{y}_{i}\left(\boldsymbol{\Omega} \times \hat{\boldsymbol{y}}_{i}\right)=\boldsymbol{\Omega} \times\left(\sum_{i=1}^{3} \dot{y}_{i} \hat{\boldsymbol{y}}_{i}\right)=\boldsymbol{\Omega} \times \boldsymbol{v}_{r}(P) \tag{10.33}
\end{equation*}
$$

The absolute acceleration $\boldsymbol{a}_{a}(P)$ and the relative acceleration $\boldsymbol{a}_{r}(P)$ of the material point $P$ are defined as,

$$
\begin{equation*}
\boldsymbol{a}_{a}(P)=\sum_{i=1}^{3} \ddot{x}_{i} \hat{\boldsymbol{x}}_{i} \quad \text { and } \quad \boldsymbol{a}_{r}(P)=\sum_{i=1}^{3} \ddot{y}_{i} \hat{\boldsymbol{y}}_{i} \tag{10.34}
\end{equation*}
$$

Taking into account equation (10.33) and the definitions (10.34), the time derivatives of the velocities (10.32) become,

$$
\begin{equation*}
\dot{\boldsymbol{v}}_{a}(P)=\boldsymbol{a}_{a}(P) \quad \text { and } \quad \dot{\boldsymbol{v}}_{r}(P)=\boldsymbol{a}_{r}(P)+\boldsymbol{\Omega} \times \boldsymbol{v}_{r}(P) \tag{10.35}
\end{equation*}
$$

Taking into account the time derivative of the relative position (10.20),

$$
\begin{equation*}
\boldsymbol{\Omega} \times \dot{\boldsymbol{r}}_{r}(P)=\boldsymbol{\Omega} \times\left(\boldsymbol{v}_{r}(P)+\boldsymbol{\Omega} \times \boldsymbol{r}_{r}(P)\right)=\boldsymbol{\Omega} \times \boldsymbol{v}_{r}(P)+\boldsymbol{\Omega} \times\left(\boldsymbol{\Omega} \times \boldsymbol{r}_{r}(P)\right) \tag{10.36}
\end{equation*}
$$

Substituting equations (10.35), (10.36) and the absolute acceleration of point $A$, that is written $\boldsymbol{a}_{a}(A)=\dot{\boldsymbol{v}}_{a}(A)$, into equation (10.31), we obtain the following acceleration identity,

$$
\begin{equation*}
\boldsymbol{a}_{a}(P)=\boldsymbol{a}_{a}(A)+\boldsymbol{a}_{r}(P)+2 \boldsymbol{\Omega} \times \boldsymbol{v}_{r}(P)+\boldsymbol{\Omega} \times\left(\boldsymbol{\Omega} \times \boldsymbol{r}_{r}(P)\right)+\dot{\boldsymbol{\Omega}} \times \boldsymbol{r}_{r}(P) \tag{10.37}
\end{equation*}
$$

The Coriolis acceleration $\boldsymbol{a}_{C}(P)$ and the centripetal acceleration $\boldsymbol{a}_{c}(P)$ of the material point $P$ are defined respectively as,

$$
\begin{equation*}
\boldsymbol{a}_{C}(P)=2 \boldsymbol{\Omega} \times \boldsymbol{v}_{r}(P) \quad \text { and } \quad \boldsymbol{a}_{c}(P)=\boldsymbol{\Omega} \times\left(\boldsymbol{\Omega} \times \boldsymbol{r}_{r}(P)\right) \tag{10.38}
\end{equation*}
$$

The driving acceleration $\boldsymbol{a}_{e}(P)$ of the material point $P$ is defined as the acceleration that the material point would have if it were fixed in the non-inertial frame of reference, i.e. if $\boldsymbol{v}_{r}(P)=\mathbf{0}$ and $\boldsymbol{a}_{r}(P)=\mathbf{0}$,

$$
\begin{equation*}
\boldsymbol{a}_{e}(P)=\boldsymbol{a}_{a}(A)+\boldsymbol{a}_{c}(P)+\dot{\boldsymbol{\Omega}} \times \boldsymbol{r}_{r}(P) \tag{10.39}
\end{equation*}
$$

Taking into account the definitions (10.38) and (10.39), the absolute acceleration (10.37) of the material point $P$ can be written,

$$
\begin{equation*}
\boldsymbol{a}_{a}(P)=\boldsymbol{a}_{e}(P)+\boldsymbol{a}_{r}(P)+\boldsymbol{a}_{C}(P) \tag{10.40}
\end{equation*}
$$

### 10.2.4 Inertial forces

The law of absolute motion (2.33) of the material point $P$ is written,

$$
\begin{equation*}
\sum \boldsymbol{F}^{\mathrm{ext}}=m \boldsymbol{a}_{a}(P) \tag{10.41}
\end{equation*}
$$

Taking into account the expression (10.37) of the absolute acceleration, the law of motion (10.41) can be recast as,

$$
\begin{equation*}
\sum \boldsymbol{F}^{\mathrm{ext}}=m\left(\boldsymbol{a}_{a}(A)+\boldsymbol{a}_{r}(P)+2 \boldsymbol{\Omega} \times \boldsymbol{v}_{r}(P)+\boldsymbol{\Omega} \times\left(\boldsymbol{\Omega} \times \boldsymbol{r}_{r}(P)\right)+\dot{\boldsymbol{\Omega}} \times \boldsymbol{r}_{r}(P)\right) \tag{10.42}
\end{equation*}
$$

Moving all the terms from the RHS of equation (10.42) to the LHS except the term $m \boldsymbol{a}_{r}(P)$, we obtain the law of relative motion of the material point $P$,

$$
\begin{equation*}
\sum \boldsymbol{F}^{\mathrm{ext}}-m\left(\boldsymbol{a}_{a}(A)+2 \boldsymbol{\Omega} \times \boldsymbol{v}_{r}(P)+\boldsymbol{\Omega} \times\left(\boldsymbol{\Omega} \times \boldsymbol{r}_{r}(P)\right)+\dot{\boldsymbol{\Omega}} \times \boldsymbol{r}_{r}(P)\right)=m \boldsymbol{a}_{r}(P) \tag{10.43}
\end{equation*}
$$

The terms on the LHS of equation (10.43) are forces that have to be characterised physically. The Coriolis force $\boldsymbol{F}_{C}$ and the centrifugal force $\boldsymbol{F}_{c}$ are respectively defined as,

$$
\begin{align*}
& \boldsymbol{F}_{C}=-m \boldsymbol{a}_{C}(P)=-2 m \boldsymbol{\Omega} \times \boldsymbol{v}_{r}(P) \\
& \boldsymbol{F}_{c}=-m \boldsymbol{a}_{c}(P)=-m \boldsymbol{\Omega} \times\left(\boldsymbol{\Omega} \times \boldsymbol{r}_{r}(P)\right) \tag{10.44}
\end{align*}
$$

The Coriolis force $\boldsymbol{F}_{C}$ exerted on a material point $P$ is oriented in the opposite direction to the Coriolis acceleration $\boldsymbol{a}_{C}(P)$. The centrifugal force $\boldsymbol{F}_{c}$ exerted on the material point $P$ is oriented in the opposite direction to the centripetal acceleration $\boldsymbol{a}_{c}(P)$, where the latter is oriented towards the centre or the origin $O$. Thus, the centrifugal force $\boldsymbol{F}_{c}$ is oriented radially towards the exterior. The driving force $\boldsymbol{F}_{e}$ is the force exerted on the material point $P$ when it is at rest in the non-inertial frame, i.e. when $\boldsymbol{v}_{r}(P)=\mathbf{0}$,

$$
\begin{equation*}
\boldsymbol{F}_{e}=-m \boldsymbol{a}_{e}(P)=-m \boldsymbol{a}_{a}(A)+\boldsymbol{F}_{c}-m \dot{\boldsymbol{\Omega}} \times \boldsymbol{r}_{r}(P) \tag{10.45}
\end{equation*}
$$

Thus, taking into account the definitions (10.44) and (10.45), the law of relative motion (10.43) reduces to,

$$
\begin{equation*}
\sum \boldsymbol{F}^{\mathrm{ext}}+\boldsymbol{F}_{e}+\boldsymbol{F}_{C}=m \boldsymbol{a}_{r}(P) \tag{10.46}
\end{equation*}
$$

Formally, the sum of inertial forces $\boldsymbol{F}^{\text {in }}$ is the sum of the driving force $\boldsymbol{F}_{e}$ and of the Coriolis force $\boldsymbol{F}_{C}$,

$$
\begin{equation*}
\sum \boldsymbol{F}^{\mathrm{in}}=\boldsymbol{F}_{e}+\boldsymbol{F}_{C} \tag{10.47}
\end{equation*}
$$

Thus, the law of relative motion (10.46) is written,

$$
\begin{equation*}
\sum \boldsymbol{F}^{\mathrm{ext}}+\sum \boldsymbol{F}^{\mathrm{in}}=m \boldsymbol{a}_{r}(P) \tag{10.48}
\end{equation*}
$$

The expressions of the laws of absolute motion (10.41) and of relative motion (10.48) are rigorously identical mathematically but their physical meaning is different. The driving acceleration $\boldsymbol{a}_{e}(P)$ and the Coriolis acceleration $\boldsymbol{a}_{C}(P)$ of the material point $P$ in the law of absolute motion are effects, and the driving force $\boldsymbol{F}_{e}$ and the Coriolis force $\boldsymbol{F}_{C}$ in the law of relative motion are causes.

As an example, let us consider a car that takes a turn. With respect to the absolute reference frame of the earth, the driver, that can be considered as a material point $P$, is subjected to a centripetal acceleration $\boldsymbol{a}_{c}(P)$ oriented radially towards the centre of the turn. With respect to the non-inertial frame of reference of the car, the driver is subjected to a centrifugal force $\boldsymbol{F}_{c}$ that pushes him radially towards the exterior of the turn in the opposite direction to the centripetal acceleration.

In the experiment of the rotating camera that films a rotating water jet (Fig. 10.4), the absolute frame of reference is the auditorium and the non-inertial frame of reference is the rotating nozzle or the rotating camera. Since these frames of reference are rotating with respect to each other, the material points $O$ and $A$ at the centre of the Cartesian frames coincide, which implies that $\boldsymbol{a}_{a}(A)=\mathbf{0}$. Since the nozzle and the camera are rotating at constant angular velocity $\boldsymbol{\Omega}$, this implies that $\dot{\boldsymbol{\Omega}}=\mathbf{0}$. Thus, the inertial forces acting on the water drops in the non-inertial frame - considered as material points $P$ that flow out of the

In the experiment of the pen in circular motion on a horizontal plate, we consider two types of motions. Firstly, when the plate is at rest and the pen rotates at constant angular velocity $\boldsymbol{\Omega}$, the plate is the absolute frame of reference. Thus, when the pen is released, it is has a uniform linear motion. Secondly, when the plate and the pen rotate at constant angular velocity $\boldsymbol{\Omega}$, the plate is the relative frame of reference and the pen is at rest with respect to the plate. Thus, when the pen is released, it is subjected to the Coriolis force $\boldsymbol{F}_{C}$ and to the centrifugal force $\boldsymbol{F}_{c}$. Thus, the motion of the pen is a curve in this frame of reference. When the pen is released, the Coriolis force vanishes since the relative velocity vanishes. However, since the pen is accelerated by the centrifugal force, the Coriolis force is progressively exerted on the pen. Thus, after the pen is released, its trajectory is initially radial, because the centrifugal force dominates. This is not the case for the rotating water jet where the initial trajectory is almost tangential because the Coriolis force initially dominates.

### 10.3 Relative motion

In the previous section, we established the law of relative motion in a non-inertial frame of reference. In this section, we will consider four examples of relative motion. In the first example, we examine the dynamics of a mathematical pendulum in a uniformly accelerating train. In the second example, we would like to determine the apparent weight of a person in a uniformly accelerating elevator. In the third example, we describe the motion of a material point in a centrifuge. In the fourth example, we consider a pendulum oscillating in the plane of a rotating door.

### 10.3.1 Pendulum in an accelerating train

Let us consider a train that has a uniform linear motion with respect to the rails. A mathematical pendulum, consisting of a material point of mass $m$ suspended to a rope of negligible mass, is attached to the ceiling of the train. The Cartesian frame $\left(O, \hat{\boldsymbol{x}}_{1}, \hat{\boldsymbol{x}}_{2}\right)$ is associated to the absolute frame of reference of the rails and the Cartesian frame $\left(A, \hat{\boldsymbol{y}}_{1}, \hat{\boldsymbol{y}}_{2}\right)$ is associated to the Cartesian frame of the train (Fig. 10.6).

The external forces are the weight $\boldsymbol{P}=m \boldsymbol{g}$ and the tension $\boldsymbol{T}$ in the rope. Since the relative frame of reference has a translational motion with respect to the absolute frame of reference, the angular velocity vanishes, i.e. $\boldsymbol{\Omega}=\mathbf{0}$. This implies that the only inertial force is the driving force $\boldsymbol{F}_{e}=-m \boldsymbol{a}_{a}(A)$. Thus, the law of relative motion (10.48) reduces to,

$$
\begin{equation*}
m \boldsymbol{g}+\boldsymbol{T}-m \boldsymbol{a}_{a}(A)=m \boldsymbol{a}_{r}(P) \tag{10.49}
\end{equation*}
$$

We assume that the pendulum reached its equilibrium position with respect to the relative
frame of reference, which means that its relative acceleration vanishes, i.e. $\boldsymbol{a}_{r}(P)=\mathbf{0}$. The projection of the vectorial quantities in the frame $\left(A, \hat{\boldsymbol{y}}_{1}, \hat{\boldsymbol{y}}_{2}, \hat{\boldsymbol{y}}_{3}\right)$ is written,

$$
\begin{equation*}
\boldsymbol{g}=-g \hat{\boldsymbol{y}}_{2} \quad \boldsymbol{T}=T \sin \theta \hat{\boldsymbol{y}}_{1}+T \cos \theta \hat{\boldsymbol{y}}_{2} \quad \boldsymbol{a}_{a}(A)=\boldsymbol{a}=a \hat{\boldsymbol{y}}_{1} \tag{10.50}
\end{equation*}
$$

Taking into account the expressions (10.50), the projections of the law of motion (10.49) along the coordinate axes $O y_{1}$ and $O y_{2}$ are written,

$$
\begin{equation*}
T \sin \theta-m a=0 \quad \text { and } \quad-m g+T \cos \theta=0 \tag{10.51}
\end{equation*}
$$

Thus, the equilibrium position satisfies the relation,

$$
\begin{equation*}
\tan \theta=\frac{a}{g} \tag{10.52}
\end{equation*}
$$

Thus, if the train brakes uniformly, i.e. if the sign of the acceleration becomes negative, then the angle of the equilibrium position of the pendulum will become negative as well (Fig. 10.6).

### 10.3.2 Apparent weight

We would like to find an analytical expression for the apparent weight of a person in a elevator that has a uniform linearly accelerated motion. The apparent weight $\boldsymbol{P}^{\prime}$ corresponds to the weight measured by a scale in the elevator. To model this, we consider the person as a material point of mass $m$ attached to a dynamometer consisting of a spring suspended to the ceiling of the elevator. The vertical coordinate axis $A y_{3}$ is associated to relative frame of reference of the elevator (Fig. 10.7). The external forces are the weight $\boldsymbol{P}=m \boldsymbol{g}$ and the
tension $\boldsymbol{T}$ in the rope. Since the relative frame of reference has a linear uniform motion with respect to the absolute frame of reference, the driving angular velocity vanishes, i.e. $\boldsymbol{\Omega}=\mathbf{0}$, which implies that the only inertial force is the driving force $\boldsymbol{F}_{e}=-m \boldsymbol{a}_{a}(A)$. Thus, the vectorial law of relative motion is the same as that of the pendulum (10.49). We consider that the material point reached its equilibrium position with respect to the relative frame of reference, which means that its relative acceleration vanishes, i.e. $\boldsymbol{a}_{r}(P)=\mathbf{0}$. The projection of the vectorial quantities on the vectorial axis $A y_{3}$ is written,

$$
\begin{equation*}
\boldsymbol{g}=-g \hat{\boldsymbol{y}}_{3} \quad \boldsymbol{T}=T \hat{\boldsymbol{y}}_{3} \quad \boldsymbol{a}_{a}(A)=\boldsymbol{a}=a \hat{\boldsymbol{y}}_{3} \tag{10.53}
\end{equation*}
$$

Taking into account expressions (10.53), the projection of the law of relative motion (10.49) along the coordinate axis $O y_{3}$ is written,

$$
\begin{equation*}
-m g+T-m a=0 \quad \text { thus } \quad T=m(a+g) \tag{10.54}
\end{equation*}
$$

The apparent weight $\boldsymbol{P}^{\prime}=-\boldsymbol{T}$ is the force that compensates the tension $\boldsymbol{T}$ in the rope. Thus,

$$
\begin{equation*}
\boldsymbol{P}^{\prime}=-m(g+a) \hat{\boldsymbol{y}}_{3} \tag{10.55}
\end{equation*}
$$

If the elevator accelerates upwards, i.e. $a>0$, the norm of the apparent weight $m(g+a)$ is superior to the norm of the real weight $m g$. However, if the elevator accelerates downwards, i.e. $a<0$, the norm of the apparent weight is inferior to the real weight. In the case where the elevator is in free fall, i.e. $g=-a$, the apparent weight vanishes, which means that the person is in a state of weightlessness. The parabolic flights allowing to experiment weightlessness work according to this principle.

### 10.3.3 Centrifuge

Let us consider a centrifuge consisting of a tube that rotates in a horizontal plane at constant angular velocity $\boldsymbol{\Omega}$ around its extremity located at point $O$. A material point $P$ of mass $m$ has to move inside the tube. The Cartesian frame $\left(O, \hat{\boldsymbol{x}}_{1}, \hat{\boldsymbol{x}}_{2}, \hat{\boldsymbol{x}}_{3}\right)$ is associated to the absolute frame of reference of the centrifuge and the Cartesian frame $\left(O, \hat{\boldsymbol{y}}_{1}, \hat{\boldsymbol{y}}_{2}, \hat{\boldsymbol{y}}_{3}\right)$ is associated to the relative frame of reference of the tube where the axis $O y_{1}$ is oriented along the tube (Fig. 10.8).

The external forces are the weight $\boldsymbol{P}=m \boldsymbol{g}$ and the normal reaction force $\boldsymbol{R}$ of the tube. Since the relative frame of reference has a uniform rotational motion with respect to the absolute frame of reference, the time derivative of the driving angular velocity vanishes, i.e. $\dot{\boldsymbol{\Omega}}=\mathbf{0}$. In this case, the inertial forces are the Coriolis force $\boldsymbol{F}_{C}$ and the driving force, that reduces to the centrifugal force $\boldsymbol{F}_{c}$. Thus, the law of relative motion (10.48) is written,

$$
\begin{equation*}
m \boldsymbol{g}+\boldsymbol{R}+\boldsymbol{F}_{c}+\boldsymbol{F}_{C}=m \boldsymbol{a}_{r}(P) \tag{10.56}
\end{equation*}
$$

Since the material point moves in a tube oriented along the axis $O y_{1}$ in the relative frame of reference, the projections of the relative position $\boldsymbol{r}_{r}(P)$, of the relative velocity $\boldsymbol{v}_{r}(P)$ and of the relative acceleration $\boldsymbol{a}_{r}(P)$ in this frame of reference are given by,

$$
\begin{equation*}
\boldsymbol{r}_{r}(P)=y_{1} \hat{\boldsymbol{y}}_{1} \quad \boldsymbol{v}_{r}(P)=\dot{y}_{1} \hat{\boldsymbol{y}}_{1} \quad \boldsymbol{a}_{r}(P)=\ddot{y}_{1} \hat{\boldsymbol{y}}_{1} \tag{10.57}
\end{equation*}
$$

The projections of the angular velocity $\boldsymbol{\Omega}$, of the gravitational field $\boldsymbol{g}$ and of the normal reaction force $\boldsymbol{R}$ in the relative frame of reference are given by,

$$
\begin{equation*}
\boldsymbol{\Omega}=\Omega \hat{\boldsymbol{y}}_{3} \quad \boldsymbol{g}=-g \hat{\boldsymbol{y}}_{3} \quad \boldsymbol{R}=R_{2} \hat{\boldsymbol{y}}_{2}+R_{3} \hat{\boldsymbol{y}}_{3} \tag{10.58}
\end{equation*}
$$

Taking into account expressions (10.57) and (10.58), the projections of the centrifugal force $\boldsymbol{F}_{c}$ and of the Coriolis force $\boldsymbol{F}_{C}$ in the relative frame of reference are given by,

$$
\begin{align*}
& \boldsymbol{F}_{c}=-m \boldsymbol{\Omega} \times\left(\boldsymbol{\Omega} \times \boldsymbol{r}_{r}(P)\right)=-m \Omega^{2} y_{1} \hat{\boldsymbol{y}}_{3} \times\left(\hat{\boldsymbol{y}}_{3} \times \hat{\boldsymbol{y}}_{1}\right)=m \Omega^{2} y_{1} \hat{\boldsymbol{y}}_{1}  \tag{10.59}\\
& \boldsymbol{F}_{C}=-2 m \boldsymbol{\Omega} \times \boldsymbol{v}_{r}(P)=-2 m \Omega \dot{y}_{1} \hat{\boldsymbol{y}}_{3} \times \hat{\boldsymbol{y}}_{1}=-2 m \Omega \dot{y}_{1} \hat{\boldsymbol{y}}_{2}
\end{align*}
$$

Taking into account expressions (10.57), (10.58) and (10.59), the projection of the law of
relative motion (10.56) along the coordinate axes $O y_{1}, O y_{2}$ and $O y_{3}$ yields three equations,

$$
\begin{equation*}
m \Omega^{2} y_{1}=m \ddot{y}_{1} \quad-2 m \Omega \dot{y}_{1}+R_{2}=0 \quad-m g+R_{3}=0 \tag{10.60}
\end{equation*}
$$

The first equation (10.60) is the equation of motion that can be expressed as,

$$
\begin{equation*}
\ddot{y}_{1}-\Omega^{2} y_{1}=0 \tag{10.61}
\end{equation*}
$$

and the two other equations yield the components $R_{2}$ and $R_{3}$ of the normal reaction force $\boldsymbol{R}$. The position equation of the material point $P$, which is a solution of the equation of motion (10.61), is written,

$$
\begin{equation*}
y_{1}(t)=y_{1}(0) e^{\Omega t} \tag{10.62}
\end{equation*}
$$

which means that the material point recedes exponentially fast in the radial direction under the action of the centrifugal force, hence its name : the centrifuge.

### 10.3.4 Pendulum on a rotating door

A mathematical pendulum consisting of a material point $P$ of mass $m$ suspended at the end of a rope of length $\ell$ and of negligible mass, is attached to the hinge of a door. The pendulum has to oscillate in the plane of the door that has a uniform circular motion of constant angular velocity $\boldsymbol{\Omega}$. The Cartesian frame $\left(O, \hat{\boldsymbol{x}}_{1}, \hat{\boldsymbol{x}}_{2}, \hat{\boldsymbol{x}}_{3}\right)$ is associated to absolute frame of reference of the building and the spherical frame $(A, \hat{\boldsymbol{r}}, \hat{\boldsymbol{\theta}}, \hat{\boldsymbol{\phi}})$ is associated to the relative frame of reference of the door (Fig. 10.9).

The external forces are the weight $\boldsymbol{P}=m \boldsymbol{g}$, the normal reaction force $\boldsymbol{R}$ of the door and the tension $\boldsymbol{T}$ in the rope. Since the relative reference frame has a uniform circular motion with respect to the absolute frame, the time derivative of the driving angular velocity vanishes, i.e. $\dot{\boldsymbol{\Omega}}=\mathbf{0}$. In this case, the inertial forces are the Coriolis force $\boldsymbol{F}_{C}$ and the driving force, that reduces to the centrifugal force $\boldsymbol{F}_{c}$. Thus, the law of relative motion (10.48) is written,

$$
\begin{equation*}
m \boldsymbol{g}+\boldsymbol{R}+\boldsymbol{T}+\boldsymbol{F}_{c}+\boldsymbol{F}_{C}=m \boldsymbol{a}_{r}(P) \tag{10.63}
\end{equation*}
$$

Since the material point at the end of the rope of length $\ell$ moves in the plane of the door $\phi=$ const described with respect to the relative frame of reference, the relative position (5.15), the relative velocity (5.18) and the relative acceleration (5.20) in this frame of reference are given by,

$$
\begin{equation*}
\boldsymbol{r}_{r}(P)=\ell \hat{\boldsymbol{r}} \quad \boldsymbol{v}_{r}(P)=\ell \dot{\theta} \hat{\boldsymbol{\theta}} \quad \boldsymbol{a}_{r}(P)=-\ell \dot{\theta}^{2} \hat{\boldsymbol{r}}+\ell \ddot{\theta} \hat{\boldsymbol{\theta}} \tag{10.64}
\end{equation*}
$$

The projections of the angular velocity $\boldsymbol{\Omega}$ and of the gravitational field $\boldsymbol{g}$ in the relative frame of reference are given by,

$$
\begin{equation*}
\boldsymbol{\Omega}=-\Omega \cos \theta \hat{\boldsymbol{r}}+\Omega \sin \theta \hat{\boldsymbol{\theta}} \quad \text { and } \quad \boldsymbol{g}=g \cos \theta \hat{\boldsymbol{r}}-g \sin \theta \hat{\boldsymbol{\theta}} \tag{10.65}
\end{equation*}
$$

The projections of the normal reaction force $\boldsymbol{R}$ and of the tension $\boldsymbol{T}$ in the relative frame of reference are given by,

$$
\begin{equation*}
\boldsymbol{R}=-R \hat{\boldsymbol{\phi}} \quad \text { and } \quad \boldsymbol{T}=-T \hat{\boldsymbol{r}} \tag{10.66}
\end{equation*}
$$

Taking into account expressions (10.64) and (10.65), the projections of the centrifugal force $\boldsymbol{F}_{c}$ and of the Coriolis force $\boldsymbol{F}_{C}$ in the relative frame of reference are given by,

$$
\begin{align*}
\boldsymbol{F}_{c} & =-m \boldsymbol{\Omega} \times\left(\boldsymbol{\Omega} \times \boldsymbol{r}_{r}(P)\right)=-m \ell \Omega^{2}(\cos \theta \hat{\boldsymbol{r}}-\sin \theta \hat{\boldsymbol{\theta}}) \times((\cos \theta \overline{\boldsymbol{r}}-\sin \theta \hat{\boldsymbol{\theta}}) \times \hat{\boldsymbol{r}}) \\
& =m \ell \Omega^{2} \sin ^{2} \theta \hat{\boldsymbol{r}}+m \ell \Omega^{2} \sin \theta \cos \theta \hat{\boldsymbol{\theta}} \\
\boldsymbol{F}_{C} & =-2 m \boldsymbol{\Omega} \times \boldsymbol{v}_{r}(P)=2 m \ell \Omega \dot{\theta}(\cos \theta \hat{\boldsymbol{r}}-\sin \theta \hat{\boldsymbol{\theta}}) \times \hat{\boldsymbol{\theta}}=2 m \ell \Omega \dot{\theta} \cos \theta \hat{\boldsymbol{\phi}} \tag{10.67}
\end{align*}
$$

Taking into account expressions (10.64), (10.65), (10.66) and (10.67), the projection of the law of relative motion (10.63) along the coordinate axis of orientation $\hat{\boldsymbol{r}}, \hat{\boldsymbol{\theta}}$ and $\hat{\boldsymbol{\phi}}$ yields three equations,

$$
\begin{align*}
& m g \cos \theta-T+m \ell \Omega^{2} \sin ^{2} \theta=-m \ell \dot{\theta}^{2} \\
& -m g \sin \theta+m \ell \Omega^{2} \sin \theta \cos \theta=m \ell \ddot{\theta}  \tag{10.68}\\
& -R+2 m \ell \Omega \dot{\theta} \cos \theta=0
\end{align*}
$$

The second equation (10.68) is the equation of motion that can be expressed as,

$$
\begin{equation*}
\ddot{\theta}+\left(\frac{g}{\ell}-\Omega^{2} \cos \theta\right) \sin \theta=0 \tag{10.69}
\end{equation*}
$$

and the two other equations yield the component $R$ of the normal reaction force $\boldsymbol{R}$ and the component $T$ of the tension $\boldsymbol{T}$.

