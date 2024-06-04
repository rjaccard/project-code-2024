# Harmonic oscillator and circular motion 

### 4.1 Harmonic oscillator

Harmonic oscillatory motion plays a central role in physics. This motion is an ideal motion with a constant frequency and amplitude. The word harmonic comes from the fact that the oscillations are sinusoidal like sound waves. Lots of motions in physics can be considered as harmonic oscillatory motions. The motion of a spring is an oscillatory motion. Vibrational motions are harmonic oscillatory motions. Oscillatory motions around an equilibrium position can be considered also, to first approximation, as harmonic oscillatory motions. The harmonic oscillator is one of three models that can be solved exactly in quantum mechanics. This model is also found in cosmology to explain the formation of galaxies and other large structures of the universe. The vibrations between atoms called phonons can also be modelled as a series of harmonic oscillators. Thus, the study of the motion of a harmonic oscillator is a whole program...

A harmonic oscillatory motion in mechanics is in general due to an elastic force exerted on a material point. We have to begin by introducing a phenomenological model for the elastic force. Using this model, we will be able to define the law of motion and to determine the equation of motion by projection. Integrating the equation of motion, we find the general solution for a harmonic oscillatory motion. We can deduce the pulsation, the frequency and the period. Using the initial conditions on the position and velocity, we determine also the amplitude.

### 4.1.1 Elastic force

There are two types of deformation of a solid. The first called elastic deformation is reversible, i.e. the solid comes back to its initial shape after having been deformed. The second called plastic deformation is irreversible, i.e. the solid does not come back to its initial shape and remains thus partially deformed.

When a mechanical constraint is exerted on a soft spring the deformation is elastic if the constraint is sufficiently small. If the constraint is larger, the deformation becomes plastic until a critical value where fracture occurs and the spring breaks. We consider here only elastic deformations.

The first model of elastic force is due to Robert Hooke who, based on empirical results, stated a law that bears his name. For an elastic deformation that is sufficiently small, Hooke's law states that the elastic force $\boldsymbol{F}_{e}$ exerted on the material point is proportional to the deformation $\boldsymbol{r}$ with respect to the equilibrium position $O$ and oriented towards the equilibrium position,

$$
\begin{equation*}
\boldsymbol{F}_{e}=-k \boldsymbol{r} \tag{4.1}
\end{equation*}
$$

where $k$ is the spring constant of the material. Hooke wrote that this law meant that the extension is proportional to the force.

The force is measured by a force sensor and the displacement by a displacement sensor. For sufficiently small elastic deformations, the extension is proportional to the applied force. This verifies Hooke's law for the elastic force (Fig. 4.2).

Intuitively, we realise that the oscillatory motion of a mass suspended to a spring is

Oscillator (air, water) damped by air friction. If we observe this motion during a sufficiently small time interval, we can neglect the viscous friction force between the mass and the air. When this motion occurs in water, we have to take into account the viscous friction of water because water has a much higher viscosity. In this section, we consider only a free harmonic oscillator, i.e. we neglect the action of the viscous friction force. We shall take the friction explicitly into account in the next section.

### 4.1.2 Harmonic oscillatory law of motion

Using expression (2.33) of Newton's $2^{\text {nd }}$ law and expression (4.1) of Hooke's law, we are now able to establish the dynamical law of the harmonic oscillatory motion in the absence of friction. We consider a material material point of sufficiently small mass $m$ such that its weight $\boldsymbol{P}$ can neglected with respect to the elastic force $\boldsymbol{F}_{e}$, i.e. $\boldsymbol{P} \ll \boldsymbol{F}_{e}$. The only external force $\boldsymbol{F}^{\text {ext }}$ is the elastic force $\boldsymbol{F}_{e}$ exerted on the object. Thus, the harmonic oscillatory law of motion (2.33) is written,

$$
\begin{equation*}
\boldsymbol{F}^{\mathrm{ext}}=\boldsymbol{F}_{e}=m \boldsymbol{a} \tag{4.2}
\end{equation*}
$$

Substituting expression (4.1) of Hooke's law into the equation of motion, we obtain,

$$
\begin{equation*}
m \boldsymbol{a}=-k \boldsymbol{r} \tag{4.3}
\end{equation*}
$$

Since the elastic force $\boldsymbol{F}_{e}=-k \boldsymbol{r}$ is a central force oriented towards the suspension point of the spring, motion occurs in a plane. In the case where the initial velocity vanishes or is oriented along the axis defined by the suspension point and the material point, the harmonic oscillatory motion is linear.

### 4.1.3 Harmonic oscillatory equation of motion

We consider here only linear harmonic oscillatory motions. We choose the axis $O x$ connecting the suspension point of the spring and the material point that is oriented positively along the direction of the material point of mass $m$. The position is written $\boldsymbol{r}=x \boldsymbol{e}_{x}$ and the acceleration is given by $\boldsymbol{a}=\ddot{\boldsymbol{x}} \boldsymbol{e}_{x}$. Projecting the harmonic oscillatory vectorial law of
motion (4.3) along the axis $O x$, we obtain the linear harmonic oscillatory equation of motion,

$$
\begin{equation*}
m \ddot{x}=-k x \tag{4.4}
\end{equation*}
$$

The pulsation of this harmonic oscillatory motion in the absence of friction is defined as,

$$
\omega=\sqrt{\frac{k}{m}}
$$

The harmonic oscillatory equation of motion (4.4) can be recast as,

$$
\begin{equation*}
\ddot{x}+\omega^{2} x=0 \quad \text { or } \quad \ddot{x}=-\omega^{2} x \tag{4.6}
\end{equation*}
$$

Equation (4.6) admits the following mathematical solutions,

$$
\begin{equation*}
x(t)=e^{\sqrt{-\omega^{2}} t}=e^{ \pm i \omega t}=\cos (\omega t) \pm i \sin (\omega t) \tag{4.7}
\end{equation*}
$$

where the second identity is Euler's formula (Fig. 4.3) obtained graphically taking into account the fact that the mathematical solutions are complex numbers of unit modulus,

$$
\left|e^{ \pm i \omega t}\right|^{2}=e^{ \pm i \omega t} e^{\mp i \omega t}=e^{0}=1
$$

This solution is complex, i.e. $x(t) \in \mathbb{C}$, but the oscillation amplitude is real, i.e. $x(t) \in \mathbb{R}$. The physical solutions of the harmonic oscillatory equation of motion (4.3) are real linear combinations of the linearly independent mathematical solutions (4.7) with a pulsation $\omega$ and a pulsation $-\omega$. Thus, there are two types of linearly independent physical solutions,

$$
\begin{equation*}
\text { (i) } x(t)=\cos (\omega t)=\frac{e^{i \omega t}+e^{-i \omega t}}{2} \quad \text { (ii) } \quad x(t)=\sin (\omega t)=\frac{e^{i \omega t}-e^{-i \omega t}}{2 i} \tag{4.8}
\end{equation*}
$$

If a differential equation admits linearly independent solutions, the general solution is a linear combination of these two solutions,

$$
\begin{equation*}
x(t)=A \cos (\omega t)+B \sin (\omega t) \tag{4.9}
\end{equation*}
$$

where $A$ and $B$ are constant lengths depending on the initial conditions. Introducing the following change of variables,

$$
A=C \cos \varphi \quad \text { and } \quad B=-C \sin \varphi
$$

the general solution can be expressed as,

$$
x(t)=C(\cos (\omega t) \cos \varphi-\sin (\omega t) \sin \varphi)
$$

Using the trigonometric formula,

$$
\cos (\omega t+\varphi)=\cos (\omega t) \cos \varphi-\sin (\omega t) \sin \varphi
$$

the general solution is reduced to (Fig. 4.4),

$$
\begin{equation*}
x(t)=C \cos (\omega t+\varphi) \tag{4.10}
\end{equation*}
$$

where $\varphi$ is the dephasing angle and $C$ is the oscillation amplitude, which depend on the initial conditions.

The amplitude $C$ corresponds to the maximal deformation length of the position equation (4.10). The dephasing $\varphi$ corresponds to a translation angle of the position equation (4.10). The oscillation frequency $f$ is related to the pulsation $\omega$ by,

$$
\begin{equation*}
\omega=2 \pi f \tag{4.11}
\end{equation*}
$$

The oscillation period $T$ is the inverse of the frequency,

$$
\begin{equation*}
T=\frac{1}{f} \tag{4.12}
\end{equation*}
$$

The physical unit of the oscillation period $T$ in the international system of units is the second denoted $[s]$. Thus, the physical unit of the oscillation frequency and of the pulsation is denoted $[1 / s]$.

The position equation (4.10) allows a clearer identification of the physical quantities characterising the harmonic oscillatory motion than equation (4.9). The expression of the velocity is obtained by taking the time derivative of the position equation (4.10) (Fig. 4.5),

$$
\begin{equation*}
\dot{x}(t)=-\omega C \sin (\omega t+\varphi) \tag{4.13}
\end{equation*}
$$

The expression of the acceleration is obtained by taking the time derivative of the velocity equation (4.13) (Fig. 4.5),

$$
\begin{equation*}
\ddot{x}(t)=-\omega^{2} C \cos (\omega t+\varphi) \tag{4.14}
\end{equation*}
$$

The position equation (4.10) of a harmonic oscillatory motion can also be expressed explicitly in terms of the sinus function by choosing another dephasing angle $\varphi^{\prime}=\varphi+\pi / 2$

(Fig. 4.6),

$$
\begin{equation*}
x(t)=C \sin \left(\omega t+\varphi^{\prime}\right) \tag{4.15}
\end{equation*}
$$

The expression of the velocity is obtained by taking the time derivative of the position equation (4.15),

$$
\begin{equation*}
\dot{x}(t)=\omega C \cos \left(\omega t+\varphi^{\prime}\right) \tag{4.16}
\end{equation*}
$$

The expression of the acceleration is obtained by taking the time derivative of the velocity equation $(4.16)$,

$$
\begin{equation*}
\ddot{x}(t)=-\omega^{2} C \sin \left(\omega t+\varphi^{\prime}\right) \tag{4.17}
\end{equation*}
$$

It is possible to observe a similar oscillatory motion for a rotating system. For instance, in the case of a torsion pendulum, a thick rigid rod suspended to a thin metallic rod oscillates around the vertical axis corresponding to the thin rod. We can visualise these small amplitude oscillations on the wall of the auditorium using a laser beam reflected on a mirror glued to the thick rod.

### 4.1.4 Initial conditions

Until now, we established the general expressions (4.10) and (4.15) of the position equation for a harmonic oscillator. In all generality, the harmonic oscillatory motion is determined by two parameters : the amplitude $C$ and the dephasing angle $\varphi$ or $\varphi^{\prime}$. Two initial conditions are needed to determine these two parameters that give rise to a specific motion : one for the position and the other for the velocity.

As an example of specific motion, we consider a harmonic oscillator with an initial deformation $x_{0}$ and a vanishing initial velocity. The initial condition on the position is written,

$$
\begin{equation*}
x(0)=x_{0} \tag{4.18}
\end{equation*}
$$

and the initial condition on the velocity is written,

$$
\begin{equation*}
\dot{x}(0)=0 \tag{4.19}
\end{equation*}
$$

The substitution of the initial condition (4.19) on the velocity into the expressions (4.13) and (4.16) for the velocity yields the dephasing angles $\varphi$ and $\varphi^{\prime}$,

$$
\begin{equation*}
\varphi=0 \quad \text { and } \quad \varphi^{\prime}=\frac{\pi}{2} \tag{4.20}
\end{equation*}
$$

The substitution of the initial condition (4.18) on the position into the expressions (4.10) and (4.15) for the position, taking into account the expressions of the dephasing angles (4.20), yields the amplitude,

$$
\begin{equation*}
C=x_{0} \tag{4.21}
\end{equation*}
$$

Substituting the conditions (4.20) and (4.21) into the expressions (4.10) and (4.15) for the position, we show that they are identical and expressed as,

$$
\begin{equation*}
x(t)=x_{0} \cos (\omega t)=x_{0} \sin \left(\omega t+\frac{\pi}{2}\right) \tag{4.22}
\end{equation*}
$$

### 4.2 Damped harmonic oscillator

The case where the dynamics of the harmonic oscillator is described only by an elastic force is an ideal case. In reality, most oscillators are subjected to friction forces due to the environment. The oscillations of a mass suspended to a spring are damped by the air friction. If this mass is immersed in a container filled with water, the friction forces play an important role. Now, we will examine the physical model that will enable us to describe the dynamics of a harmonic oscillator in the presence of friction.

The approach that we shall adopt is the following. The first step consists in identifying the forces acting on the material point. After having established done that, we can state the law of motion and project it to obtain the equations of motion. The formal description of the physical system stops there. We shall then solve mathematically these differential equations of motion. We shall see that this relatively simple differential equation has quite complex solutions. In particular, we have to consider three qualitatively different types of damping. Using general solutions for these three types of damping, we will determine particular solutions taking into account identical initial conditions. Finally, we will illustrate graphically these particular solutions.

### 4.2.1 Damped harmonic oscillatory law of motion

We consider a material point of sufficiently small mass $m$ in order to be able to neglect its weight $\boldsymbol{P}$ with respect to the elastic force $\boldsymbol{F}_{e}$, i.e. $\boldsymbol{P} \ll \boldsymbol{F}_{e}$. The external forces $\boldsymbol{F}^{\text {ext }}$ are the elastic force $\boldsymbol{F}_{e}$ and the viscous friction force $\boldsymbol{F}_{f}$ given by Stoke's law. Thus, the damped harmonic oscillatory law of motion is written,

$$
\begin{equation*}
\sum \boldsymbol{F}^{\mathrm{ext}}=\boldsymbol{F}_{e}+\boldsymbol{F}_{f}=m \boldsymbol{a} \tag{4.23}
\end{equation*}
$$

The substitution of Hooke's law (4.1) and Stoke's law (3.3) into the law of motion (4.23) yields,

$$
\begin{equation*}
m \boldsymbol{a}=-k \boldsymbol{r}-b \boldsymbol{v} \tag{4.24}
\end{equation*}
$$

### 4.2.2 Damped harmonic oscillatory equation of motion

We consider here only linear damped harmonic oscillatory motions. We choose the axis $O x$ connecting the suspension point of the spring and the material point. We obtain the linear harmonic oscillatory equation of motion,

$$
\begin{equation*}
m \ddot{x}=-b \dot{x}-k x \tag{4.25}
\end{equation*}
$$

The pulsation of this harmonic oscillatory motion in the absence of friction is defined as,

$$
\begin{equation*}
\omega_{0}=\sqrt{\frac{k}{m}} \tag{4.26}
\end{equation*}
$$

which is different from the pulsation $\omega$ of the harmonic motion in the presence of friction. The damping factor $\gamma$ is defined as,

$$
\begin{equation*}
\gamma=\frac{b}{2 m} \tag{4.27}
\end{equation*}
$$

Taking into account the definitions (4.26) and (4.27), the equation of motion (4.25) can be recast as,

$$
\begin{equation*}
\ddot{x}+2 \gamma \dot{x}+\omega_{0}^{2} x=0 \tag{4.28}
\end{equation*}
$$

The mathematical solution (4.7) of the harmonic oscillatory motion without friction is an imaginary exponential of type $e^{i \omega t}$. Moreover, in the presence of viscous friction the motion is exponentially damped, as in the case of a damped ballistic motion along the horizontal axis that contains a term proportional to $e^{-t / \tau}$. Thus, the damped harmonic oscillatory equation of motion (4.24) admits as a mathematical solution a product of the two solutions mentioned above, i.e. an exponential with a complex argument,

$$
\begin{equation*}
x(t)=e^{\lambda t} \tag{4.29}
\end{equation*}
$$

where $\lambda \in \mathbb{C}$. Substituting the solution (4.29) into the equation of motion (4.28), we obtain the characteristic equation that has to be satisfied at all times $t$,

$$
\begin{equation*}
e^{\lambda t}\left(\lambda^{2}+2 \gamma \lambda+\omega_{0}^{2}\right)=0 \quad \text { thus } \quad \lambda^{2}+2 \gamma \lambda+\omega_{0}^{2}=0 \tag{4.30}
\end{equation*}
$$

The characteristic equation (4.30) to second-order in $\lambda$ has two complex solutions,

$$
\begin{equation*}
\lambda_{1}=-\gamma+\sqrt{\gamma^{2}-\omega_{0}^{2}} \quad \text { and } \quad \lambda_{2}=-\gamma-\sqrt{\gamma^{2}-\omega_{0}^{2}} \tag{4.31}
\end{equation*}
$$

where $\lambda_{1}, \lambda_{2} \in \mathbb{C}$. The general mathematical solution is a linear combination of these two particular solutions,

$$
\begin{equation*}
x(t)=A_{1} e^{\lambda_{1} t}+A_{2} e^{\lambda_{2} t} \tag{4.32}
\end{equation*}
$$

where the coefficients $A_{1}, A_{2} \in \mathbb{C}$. The type of damping of an oscillatory harmonic motion depends on the argument under the square root of the solutions $\lambda_{1}$ and $\lambda_{2}$. Thus, it depends on the respective value of the pulsation $\omega_{0}$ and the damping factor $\gamma$. There are three types of damping : a weak damping if $\gamma<\omega_{0}$, a strong damping if $\gamma>\omega_{0}$ and a critical damping if $\gamma=\omega_{0}$.

### 4.2.3 Weak damping

The pulsation $\omega$ of the harmonic oscillatory motion with friction is defined as,

$$
\begin{equation*}
\omega=\sqrt{\left|\gamma^{2}-\omega_{0}^{2}\right|} \tag{4.33}
\end{equation*}
$$

Using the definition (4.33), the solutions (4.31) of the characteristic equation are written,

$$
\begin{equation*}
\lambda_{1}=-\gamma+i \omega \quad \text { and } \quad \lambda_{2}=-\gamma-i \omega \tag{4.34}
\end{equation*}
$$

because $\gamma^{2}<\omega_{0}^{2}$ for a weak damping. The position equation $x(t)$ has to be real. For it to be real, the coefficients $A_{1}$ and $A_{2}$ have to be complex conjugates, i.e. $A_{1}=A$ and $A_{2}=A^{*}$. Thus, taking into account the solutions (4.34) of the characteristic equation, the general solution (4.32) is expressed as,

$$
\begin{equation*}
x(t)=e^{-\gamma t}\left(A e^{i \omega t}+A^{*} e^{-i \omega t}\right) \tag{4.35}
\end{equation*}
$$

Using Euler's formula (4.7), the general solution (4.35) becomes,

$$
\begin{equation*}
x(t)=e^{-\gamma t}\left(\left(A+A^{*}\right) \cos (\omega t)+\left(A-A^{*}\right) i \sin (\omega t)\right) \tag{4.36}
\end{equation*}
$$

where $A+A^{*}=2 \operatorname{Re}(A) \in \mathbb{R}$ and $\left(A-A^{*}\right) i=-2 \operatorname{Im}(A) \in \mathbb{R}$, which shows that it is a real solution. Introducing the following change of variables,

$$
\begin{equation*}
\left(A+A^{*}\right)=C \cos \varphi \quad \text { and } \quad\left(A-A^{*}\right) i=-C \sin \varphi \tag{4.37}
\end{equation*}
$$

we can express the general solution as,

$$
\begin{equation*}
x(t)=C e^{-\gamma t}(\cos (\omega t) \cos \varphi-\sin (\omega t) \sin \varphi) \tag{4.38}
\end{equation*}
$$

Using the trigonometric formula,

$$
\begin{equation*}
\cos (\omega t+\varphi)=\cos (\omega t) \cos \varphi-\sin (\omega t) \sin \varphi \tag{4.39}
\end{equation*}
$$

the general solution (4.38) reduces to,

$$
\begin{equation*}
x(t)=C e^{-\gamma t} \cos (\omega t+\varphi) \tag{4.40}
\end{equation*}
$$

which corresponds to a harmonic oscillatory motion of amplitude $C e^{-\gamma t}$ that is exponentially damped (Fig 4.7).

It is possible to observe a similar weakly damped harmonic oscillatory motion for a rotating system. For instance, we can build a torsion pendulum consisting of an egg suspended to a metallic rod. We consider two analogous torsion pendula : one consists of a raw egg and the other of a cooked egg. How can they be distinguished? The raw egg is liquid inside and the rotation of the liquid generates a viscous friction force inside the egg that slows down its rotation motion. The cooked egg is solid and the viscous friction is negligible. Thus, the raw egg is weakly damped whereas the cooked egg is not.

### 4.2.4 Strong damping

Using the definition (4.33), the solutions (4.31) of the characteristic equation are written,

$$
\begin{equation*}
\lambda_{1}=-\gamma+\omega \quad \text { and } \quad \lambda_{2}=-\gamma-\omega \tag{4.41}
\end{equation*}
$$

because $\gamma^{2}>\omega_{0}^{2}$ for a strong damping. The position equation $x(t)$ has to be real. For it to be real, the coefficients $A_{1}$ and $A_{2}$ have to be real. The damping times $\tau_{1}$ and $\tau_{2}$ are defined as,

$$
\begin{equation*}
\tau_{1}=\frac{1}{\gamma-\omega} \quad \text { and } \quad \tau_{2}=\frac{1}{\gamma+\omega} \tag{4.42}
\end{equation*}
$$

Thus, taking into account the solutions (4.41) of the characteristic equation, the general solution (4.32) is expressed as (Fig. 4.7),

$$
\begin{equation*}
x(t)=A_{1} e^{-\frac{t}{\tau_{1}}}+A_{2} e^{-\frac{t}{\tau_{2}}} \tag{4.43}
\end{equation*}
$$

When there is a strong damping, the friction is too large with respect to the action of the elastic force and the oscillator is damped before having been able to oscillate.

### 4.2.5 Critical damping

For a critical damping, i.e. $\gamma=\omega_{0}$, which implies that the pulsation $\omega=0$ and that $\gamma=1 / \tau_{1}=1 / \tau_{2}$. The critical damping is the limiting case of the weak and strong damping. Thus, the general solutions of the position equation (4.36) and (4.43) imply that the general solution for a critical solution is proportional to $e^{-\omega_{0} t}$. The factor that multiplies the exponential $e^{-\omega_{0} t}$ has to contain two independent real parameters $A$ and $B$ since the equation of motion (4.24) is a second-order equation. The factor of lowest order in $t$ is of type $A+B t$. Thus, the general solution for a harmonic oscillatory motion with critical damping is (Fig. 4.7),

$$
\begin{equation*}
x(t)=(A+B t) e^{-\omega_{0} t} \tag{4.44}
\end{equation*}
$$

When there is critical damping, the friction compensates the action of the elastic force and the oscillator is damped at the oscillation threshold.

### 4.2.6 Initial conditions

We consider a specific damped harmonic oscillatory motion determined by the following initial conditions on the position and the velocity,

$$
\begin{equation*}
x(0)=x_{0} \quad \text { and } \quad \dot{x}(0)=0 \tag{4.45}
\end{equation*}
$$

## Weak damping

The velocity equation for a weak damping is obtained by taking the time derivative of the position equation (4.40),

$$
\begin{equation*}
\dot{x}(t)=-C e^{-\gamma t}(\gamma \cos (\omega t+\varphi)+\omega \sin (\omega t+\varphi)) \tag{4.46}
\end{equation*}
$$

The initial condition (4.45) on the velocity is written,

$$
\begin{equation*}
\tan \varphi=-\frac{\gamma}{\omega} \quad \text { thus } \quad \varphi=-\arctan \left(\frac{\gamma}{\omega}\right) \tag{4.47}
\end{equation*}
$$

The initial condition (4.45) on the position is written as,

$$
\begin{equation*}
x_{0}=C \cos \varphi \tag{4.48}
\end{equation*}
$$

Using the trigonometric identity

$$
\begin{equation*}
\cos ( \pm \arctan \theta)=\frac{1}{\sqrt{1+\theta^{2}}} \tag{4.49}
\end{equation*}
$$

for $\theta=\gamma / \omega$, the amplitude $C$ is written explicitly,

$$
\begin{equation*}
C=\frac{x_{0}}{\cos \varphi}=x_{0} \sqrt{1+\frac{\gamma^{2}}{\omega^{2}}} \tag{4.50}
\end{equation*}
$$

The position equation (4.40) of the weakly damped harmonic oscillatory motion satisfying the conditions (4.47) and (4.50) is then written explicitly as,

$$
\begin{equation*}
x(t)=x_{0} \sqrt{1+\frac{\gamma^{2}}{\omega^{2}}} e^{-\gamma t} \cos \left(\omega t-\arctan \left(\frac{\gamma}{\omega}\right)\right) \tag{4.51}
\end{equation*}
$$

## Strong damping

The velocity equation for a strong damping is obtained by taking the time derivative of the position equation (4.43),

$$
\begin{equation*}
\dot{x}(t)=-\frac{A_{1}}{\tau_{1}} e^{-\frac{t}{\tau_{1}}}-\frac{A_{2}}{\tau_{2}} e^{-\frac{t}{\tau_{2}}} \tag{4.52}
\end{equation*}
$$

The initial conditions (4.45) on the position and the velocity are written,

$$
\begin{equation*}
A_{1}+A_{2}=x_{0} \quad \text { and } \quad-\frac{A_{1}}{\tau_{1}}-\frac{A_{2}}{\tau_{2}}=0 \tag{4.53}
\end{equation*}
$$

Thus, the coefficients $A_{1}$ and $A_{2}$ are given by,

$$
\begin{equation*}
A_{1}=\frac{x_{0} \tau_{1}}{\tau_{1}-\tau_{2}} \quad \text { and } \quad A_{2}=-\frac{x_{0} \tau_{2}}{\tau_{1}-\tau_{2}} \tag{4.54}
\end{equation*}
$$

The position equation (4.43) of the strongly damped harmonic oscillatory motion satisfying the conditions (4.54) is then written explicitly as,

$$
\begin{equation*}
x(t)=\frac{x_{0}}{\tau_{1}-\tau_{2}}\left(\tau_{1} e^{-\frac{t}{\tau_{1}}}-\tau_{2} e^{-\frac{t}{\tau_{2}}}\right) \tag{4.55}
\end{equation*}
$$

## Critical damping

The velocity equation for a critical damping is obtained by taking the time derivative of the position equation (4.44),

$$
\begin{equation*}
\dot{x}(t)=\left(B-\omega_{0}(A+B t)\right) e^{-\omega_{0} t} \tag{4.56}
\end{equation*}
$$

The initial conditions (4.45) on the position and the velocity are written,

$$
\begin{equation*}
A=x_{0} \quad \text { and } \quad B=A \omega_{0}=x_{0} \omega_{0} \tag{4.57}
\end{equation*}
$$

The position equation (4.44) of the critically damped oscillatory harmonic motion satisfying the conditions (4.57) is then written explicitly as,

$$
\begin{equation*}
x(t)=x_{0}\left(1+\omega_{0} t\right) e^{-\omega_{0} t} \tag{4.58}
\end{equation*}
$$

### 4.3 Circular motion and angular velocity

A material point that moves on a circle of constant radius with a constant scalar velocity has a uniform circular motion. This motion is characterised by two scalar quantities that are the radius $R$ of the circular trajectory and the constant angular velocity $\omega$, that has to same physical unit - denoted $[1 / s]$ - and plays an analogous role to the pulsation for the harmonic oscillatory motion. A uniform circular motion is also characterised by a centripetal acceleration, since according to Newton's $1^{\text {st }}$ law a material point follows a uniform linear motion in the absence of acceleration.

### 4.3.1 Curvilinear abscissa

A uniform circular motion occurs on a circle that is a particular curve. The distance traveled by the material point $P$, from the origin $O$, along an arbitrary curve in the curvilinear abscissa denoted $s(t)$ (Fig. 4.8).

The speed $v(t)$ along the curve is defined as the time derivative of the curvilinear abscissa,

$$
\begin{equation*}
v(t)=\frac{d s}{d t} \tag{4.59}
\end{equation*}
$$

It is the speed indicated by the speedometer of a vehicule.

### 4.3.2 Scalar angular velocity

The curvilinear abscissa of a material point that has a uniform circular motion on a circle of constant radius $R$ is given by,

$$
\begin{equation*}
s(t)=R \phi(t) \quad \text { where } \quad R=\text { const } \tag{4.60}
\end{equation*}
$$

where $\phi$ is the rotation angle positively defined counterclockwise (Fig. 4.9).

Taking into account the definition (4.59), the scalar velocity is written as,

$$
\begin{equation*}
v=R \dot{\phi} \tag{4.61}
\end{equation*}
$$

The scalar angular velocity $\omega$ is defined as the time derivative of the angular coordinate $\phi(t)$,

$$
\begin{equation*}
\omega=\dot{\phi} \tag{4.62}
\end{equation*}
$$

thus,

$$
\begin{equation*}
v=R \omega \quad \text { and } \quad \omega=\frac{v}{R} \tag{4.63}
\end{equation*}
$$

Since the scalar velocity $v$ is constant for a uniform circular motion, the scalar angular velocity has to be also constant,

$$
\begin{equation*}
v=\text { const } \quad \text { thus } \quad \omega=\text { const } \tag{4.64}
\end{equation*}
$$

Integrating equation (4.62) over time, we express the angle $\phi(t)$ as a function of the scalar angular velocity,

$$
\begin{equation*}
\phi(t)=\omega t \tag{4.65}
\end{equation*}
$$

### 4.3.3 Centripetal acceleration

We consider the uniform centripetal motion of radius $R$ of a material point $P$ centred at the origin $O$. This motion occurs at constant angular velocity $\omega$ in the plane $O x y$ and the material point moves counterclockwise (Fig. 4.9). We describe this motion in Cartesian coordinates. The material point is initially located on the axis $O x$. The Cartesian coordinates of the position vector $\boldsymbol{r}(t)$ are

$$
\begin{align*}
& x(t)=R \cos (\omega t) \\
& y(t)=R \sin (\omega t)  \tag{4.66}\\
& z(t)=0
\end{align*}
$$

Projecting the uniform circular motion along the Cartesian axes $O x$ and $O y$, we obtain two harmonic oscillatory motions dephased by a angle of $90^{\circ}$ (Fig. 4.10).

The Cartesian coordinates of the velocity vector $\boldsymbol{v}(t)=\dot{\boldsymbol{r}}(t)$ are obtained by taking the time derivative of the position vector $\boldsymbol{r}(t)$, i.e.

$$
\begin{align*}
& \dot{x}(t)=-R \omega \sin (\omega t) \\
& \dot{y}(t)=R \omega \cos (\omega t)  \tag{4.67}\\
& \dot{z}(t)=0
\end{align*}
$$

and the speed $v=\sqrt{\dot{x}^{2}+\dot{y}^{2}+\dot{z}^{2}}=R \omega$. The Cartesian components of the acceleration vector $\boldsymbol{a}(t)=\dot{\boldsymbol{v}}(t)$ are obtained by taking the time derivative of the velocity vector $\boldsymbol{v}(t)$, i.e.

$$
\begin{align*}
& \ddot{x}(t)=-R \omega^{2} \cos (\omega t) \\
& \ddot{y}(t)=-R \omega^{2} \sin (\omega t)  \tag{4.68}\\
& \ddot{z}(t)=0
\end{align*}
$$

Comparing the components (4.66) and (4.68) of the position vector $\boldsymbol{r}(t)$ and of the acceleration vector $\boldsymbol{a}(t)$, we conclude that the acceleration vector is radial and oriented in the
direction opposed to the position vector, i.e.

$$
\begin{equation*}
\boldsymbol{a}(t)=-\omega^{2} \boldsymbol{r}(t) \tag{4.69}
\end{equation*}
$$

This acceleration directed towards the centre is called centripetal acceleration. The norm of the centripetal acceleration $\boldsymbol{a}(t)$ is given by,

$$
\begin{equation*}
\|\boldsymbol{a}\|=\sqrt{\ddot{x}^{2}+\ddot{y}^{2}+\ddot{z}^{2}}=R \omega^{2}=\frac{v^{2}}{R} \tag{4.70}
\end{equation*}
$$

### 4.3.4 Angular velocity vector

For a circular motion, the angular velocity vector $\boldsymbol{\omega}$ is oriented along the rotation axis. For a circular motion in the plane $O x y$ that occurs counterclockwise, the rotation axis $O z$ is normal to the plane $O x y$. In this case, the angular velocity vector $\boldsymbol{\omega}$ is positively defined along the axis $O z$, i.e. $\boldsymbol{\omega}=\omega \boldsymbol{e}_{z}$.

Now we establish two relations between the position vector $\boldsymbol{r}$, the velocity vector $\boldsymbol{v}$, the acceleration vector $\boldsymbol{a}$ and the angular velocity vector $\boldsymbol{\omega}$ for the circular motion mentioned above. These vectors are expressed in Cartesian coordinates as $\boldsymbol{r}=(R \cos (\omega t), R \sin (\omega t), 0)$, $\boldsymbol{v}=(-R \omega \sin (\omega t), R \omega \cos (\omega t), 0), \boldsymbol{a}=\left(-R \omega^{2} \cos (\omega t),-R \omega \sin (\omega t), 0\right)$ and $\boldsymbol{\omega}=$ $(0,0, \omega)$. Thus, these vectors satisfy the important following vectorial relations (Fig. 4.11),

$$
\begin{align*}
\boldsymbol{v} & \equiv \dot{\boldsymbol{r}}=\boldsymbol{\omega} \times \boldsymbol{r} \\
\boldsymbol{a} & \equiv \dot{\boldsymbol{v}}=\boldsymbol{\omega} \times \dot{\boldsymbol{r}}=\boldsymbol{\omega} \times \boldsymbol{v}=\boldsymbol{\omega} \times(\boldsymbol{\omega} \times \boldsymbol{r}) \tag{4.71}
\end{align*}
$$

The velocity vector $\boldsymbol{v}$ is tangent to the circular trajectory, because it is orthogonal to the position vector $\boldsymbol{r}$ that is radial. The first relation (4.71) applies also to the case where the position vector $\boldsymbol{r}$ is not orthogonal to the angular velocity vector $\boldsymbol{\omega}$. If the position vector $\boldsymbol{r}$ is collinear to the angular velocity vector $\boldsymbol{\omega}$, the material point is located on the rotation axis at remains at rest during the circular motion. The acceleration vector $\boldsymbol{a}$ is collinear to the position vector $\boldsymbol{r}$, because it is orthogonal to the velocity vector $\boldsymbol{v}$ and to the angular velocity vector $\boldsymbol{\omega}$ that are orthogonal to the position vector $\boldsymbol{r}$. Indeed, using the vectorial identity (1.43), the second vectorial relation (4.71) is written as,

$$
\begin{equation*}
\boldsymbol{a}=\boldsymbol{\omega} \times(\boldsymbol{\omega} \times \boldsymbol{r})=(\boldsymbol{\omega} \cdot \boldsymbol{r}) \boldsymbol{\omega}-(\boldsymbol{\omega} \cdot \boldsymbol{\omega}) \boldsymbol{r}=-\omega^{2} \boldsymbol{r} \tag{4.72}
\end{equation*}
$$

because $\boldsymbol{\omega} \cdot \boldsymbol{r}=0$ and $\boldsymbol{\omega} \cdot \boldsymbol{\omega}=\omega^{2}$.

