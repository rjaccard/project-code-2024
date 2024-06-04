# CHAPTER 8 <br> Potential Energy and Conservation of Energy 

INTRODUCTION In George Rhoads' rolling ball sculpture, the principle of conservation of energy governs the changes in the ball's kinetic energy and relates them to changes and transfers for other types of energy associated with the ball's interactions. In this chapter, we introduce the important concept of potential energy. This will enable us to formulate the law of conservation of mechanical energy and to apply it to simple systems, making solving problems easier. In the final section on sources of energy, we will consider energy transfers and the general law of conservation of energy. Throughout this book, the law of conservation of energy will be applied in increasingly more detail, as you encounter more complex and varied systems, and other forms of
energy.

### 8.1 Potential Energy of a System

In Work, we saw that the work done on an object by the constant gravitational force, near the surface of Earth, over any displacement is a function only of the difference in the positions of the end-points of the displacement. This property allows us to define a different kind of energy for the system than its kinetic energy, which is called potential energy. We consider various properties and types of potential energy in the following subsections.

## Potential Energy Basics

In Motion in Two and Three Dimensions, we analyzed the motion of a projectile, like kicking a football in Figure 8.2. For this example, let's ignore friction and air resistance. As the football rises, the work done by the gravitational force on the football is negative, because the ball's displacement is positive vertically and the force due to gravity is negative vertically. We also noted that the ball slowed down until it reached its highest point in the motion, thereby decreasing the ball's kinetic energy. This loss in kinetic energy translates to a gain in gravitational potential energy of the football-Earth system.

As the football falls toward Earth, the work done on the football is now positive, because the displacement and the gravitational force both point vertically downward. The ball also speeds up, which indicates an increase in kinetic energy. Therefore, energy is converted from gravitational potential energy back into kinetic energy.

Based on this scenario, we can define the difference of potential energy from point $A$ to point $B$ as the negative of the work done:

$$
\Delta U_{A B}=U_{B}-U_{A}=-W_{A B}
$$

This formula explicitly states a potential energy difference, not just an absolute potential energy. Therefore, we need to define potential energy at a given position in such a way as to state standard values of potential energy on their own, rather than potential energy differences. We do this by rewriting the potential energy function in terms of an arbitrary constant,

$$
\Delta U=U(\overrightarrow{\mathbf{r}})-U\left(\overrightarrow{\mathbf{r}}_{0}\right)
$$

The choice of the potential energy at a starting location of $\overrightarrow{\mathbf{r}}_{0}$ is made out of convenience in the given problem. Most importantly, whatever choice is made should be stated and kept consistent throughout the given problem. There are some well-accepted choices of initial potential energy. For example, the lowest height in a problem is usually defined as zero potential energy, or if an object is in space, the farthest point away from the system is often defined as zero potential energy. Then, the potential energy, with respect to zero at $\overrightarrow{\mathbf{r}}_{0}$, is just $U(\vec{r})$.

As long as there is no friction or air resistance, the change in kinetic energy of the football equals negative of the change in gravitational potential energy of the football. This can be generalized to any potential energy:

$$
\Delta K_{A B}=-\Delta U_{A B}
$$

Let's look at a specific example, choosing zero potential energy for gravitational potential energy at convenient points.

## EXAMPLE 8.1

## Basic Properties of Potential Energy

A particle moves along the $x$-axis under the action of a force given by $F=-a x^{2}$, where $a=3 \mathrm{~N} / \mathrm{m}^{2}$. (a) What is the difference in its potential energy as it moves from $x_{A}=1 \mathrm{~m}$ to $x_{B}=2 \mathrm{~m}$ ? (b) What is the particle's potential energy at $x=1 \mathrm{~m}$ with respect to a given $0.5 \mathrm{~J}$ of potential energy at $x=0$ ?

## Strategy

(a) The difference in potential energy is the negative of the work done, as defined by Equation 8.1. The work is defined in the previous chapter as the dot product of the force with the distance. Since the particle is moving forward in the $x$-direction, the dot product simplifies to a multiplication $(\hat{\mathbf{i}} \cdot \hat{\mathbf{i}}=1)$. To find the total work done, we need to integrate the function between the given limits. After integration, we can state the work or the change in potential energy. (b) The potential energy function, with respect to zero at $x=0$, is the indefinite integral encountered in part (a), with the constant of integration determined from Equation 8.3. Then, we substitute the $x$-value into the function of potential energy to calculate the potential energy at $x=1 \mathrm{~m}$.

## Solution

a. The work done by the given force as the particle moves from coordinate $x$ to $x+d x$ in one dimension is

$$
d W=\overrightarrow{\mathbf{F}} \cdot d \overrightarrow{\mathbf{r}}=F d x=-a x^{2} d x
$$

Substituting this expression into Equation 8.1, we obtain

$$
\Delta U=-W=\int_{x_{1}}^{x_{2}} a x^{2} d x=\left.\frac{1}{3}\left(3 \mathrm{~N} / \mathrm{m}^{2}\right) x^{3}\right|_{1 \mathrm{~m}} ^{2 \mathrm{~m}}=7 \mathrm{~J}
$$

b. The indefinite integral for the potential energy function in part (a) is

$$
U(x)=\frac{1}{3} a x^{3}+\text { const. }
$$

and we want the constant to be determined by

$$
U(0)=0.5 \mathrm{~J}
$$

Thus, the potential energy with respect to zero at $x=0$ is just

$$
U(x)=\frac{1}{3} a x^{3}+0.5 \mathrm{~J}
$$

Therefore, the potential energy at $x=1 \mathrm{~m}$ is

$$
U(1 \mathrm{~m})=\frac{1}{3}\left(3 \mathrm{~N} / \mathrm{m}^{2}\right)(1 \mathrm{~m})^{3}+0.5 \mathrm{~J}=1.5 \mathrm{~J}
$$

## Significance

In this one-dimensional example, any function we can integrate, independent of path, is conservative. Notice how we applied the definition of potential energy difference to determine the potential energy function with respect to zero at a chosen point. Also notice that the potential energy, as determined in part (b), at $x=1 \mathrm{~m}$ is $U(1 \mathrm{~m})=1 \mathrm{~J}$ and at $x=2 \mathrm{~m}$ is $U(2 \mathrm{~m})=8 \mathrm{~J}$; their difference is the result in part (a).

## Systems of Several Particles

In general, a system of interest could consist of several particles. The difference in the potential energy of the system is the negative of the work done by gravitational or elastic forces, which, as we will see in the next section, are conservative forces. The potential energy difference depends only on the initial and final positions of the particles, and on some parameters that characterize the interaction (like mass for gravity or the spring constant for a Hooke's law force).

It is important to remember that potential energy is a property of the interactions between objects in a chosen system, and not just a property of each object. This is especially true for electric forces, although in the examples of potential energy we consider below, parts of the system are either so big (like Earth, compared to an object on its surface) or so small (like a massless spring), that the changes those parts undergo are negligible when included in the system.

## Types of Potential Energy

For each type of interaction present in a system, you can label a corresponding type of potential energy. The total potential energy of the system is the sum of the potential energies of all the types. (This follows from the additive property of the dot product in the expression for the work done.) Let's look at some specific examples of types of potential energy discussed in Work. First, we consider each of these forces when acting separately, and then when both act together.

## Gravitational potential energy near Earth's surface

The system of interest consists of our planet, Earth, and one or more particles near its surface (or bodies small enough to be considered as particles, compared to Earth). The gravitational force on each particle (or body) is just its weight $m g$ near the surface of Earth, acting vertically down. According to Newton's third law, each particle exerts a force on Earth of equal magnitude but in the opposite direction. Newton's second law tells us that the magnitude of the acceleration produced by each of these forces on Earth is $m g$ divided by Earth's mass. Since the ratio of the mass of any ordinary object to the mass of Earth is vanishingly small, the motion of Earth can be completely neglected. Therefore, we consider this system to be a group of single-particle systems, subject to the uniform gravitational force of Earth.

In Work, the work done on a body by Earth's uniform gravitational force, near its surface, depended on the mass of the body, the acceleration due to gravity, and the difference in height the body traversed, as given by Equation 7.4. By definition, this work is the negative of the difference in the gravitational potential energy, so that difference is

$$
\Delta U_{\text {grav }}=-W_{\text {grav }, A B}=m g\left(y_{B}-y_{A}\right)
$$

You can see from this that the gravitational potential energy function, near Earth's surface, is

$$
U(y)=m g y+\text { const. }
$$

You can choose the value of the constant, as described in the discussion of Equation 8.2; however, for solving most problems, the most convenient constant to choose is zero for when $y=0$, which is the lowest vertical
position in the problem.

EXAMPLE 8.2

## Gravitational Potential Energy of a Hiker

The summit of Great Blue Hill in Milton, MA, is $147 \mathrm{~m}$ above its base and has an elevation above sea level of $195 \mathrm{~m}$ (Figure 8.3). (Its Native American name, Massachusett, was adopted by settlers for naming the Bay Colony and state near its location.) A $75-\mathrm{kg}$ hiker ascends from the base to the summit. What is the gravitational potential energy of the hiker-Earth system with respect to zero gravitational potential energy at base height, when the hiker is (a) at the base of the hill, (b) at the summit, and (c) at sea level, afterward?

## Strategy

First, we need to pick an origin for the $y$-axis and then determine the value of the constant that makes the potential energy zero at the height of the base. Then, we can determine the potential energies from Equation 8.5, based on the relationship between the zero potential energy height and the height at which the hiker is located.

## Solution

a. Let's choose the origin for the $y$-axis at base height, where we also want the zero of potential energy to be. This choice makes the constant equal to zero and

$$
U(\text { base })=U(0)=0
$$

b. At the summit, $y=147 \mathrm{~m}$, so

$$
U(\text { summit })=U(147 \mathrm{~m})=m g h=(75 \times 9.8 \mathrm{~N})(147 \mathrm{~m})=108 \mathrm{~kJ}
$$

c. At sea level, $y=(147-195) \mathrm{m}=-48 \mathrm{~m}$, so

$$
U(\text { sea-level })=(75 \times 9.8 \mathrm{~N})(-48 \mathrm{~m})=-35.3 \mathrm{~kJ}
$$

## Significance

Besides illustrating the use of Equation 8.4 and Equation 8.5, the values of gravitational potential energy we found are reasonable. The gravitational potential energy is higher at the summit than at the base, and lower at sea level than at the base. Gravity does work on you on your way up, too! It does negative work and not quite as much (in magnitude), as your muscles do. But it certainly does work. Similarly, your muscles do work on your way down, as negative work. The numerical values of the potential energies depend on the choice of zero of potential energy, but the physically meaningful differences of potential energy do not. [Note that since Equation 8.2 is a difference, the numerical values do not depend on the origin of coordinates.]

## Elastic potential energy

In Work, we saw that the work done by a perfectly elastic spring, in one dimension, depends only on the spring constant and the squares of the displacements from the unstretched position, as given in Equation 7.5. This
work involves only the properties of a Hooke's law interaction and not the properties of real springs and whatever objects are attached to them. Therefore, we can define the difference of elastic potential energy for a spring force as the negative of the work done by the spring force in this equation, before we consider systems that embody this type of force. Thus,

$$
\Delta U=-W_{A B}=\frac{1}{2} k\left(x_{B}^{2}-x_{A}^{2}\right)
$$

where the object travels from point $A$ to point $B$. The potential energy function corresponding to this difference is

$$
U(x)=\frac{1}{2} k x^{2}+\text { const }
$$

If the spring force is the only force acting, it is simplest to take the zero of potential energy at $x=0$, when the spring is at its unstretched length. Then, the constant is Equation 8.7 is zero. (Other choices may be more convenient if other forces are acting.)

## EXAMPLE 8.3

## Spring Potential Energy

A system contains a perfectly elastic spring, with an unstretched length of $20 \mathrm{~cm}$ and a spring constant of $4 \mathrm{~N} /$ cm. (a) How much elastic potential energy does the spring contribute when its length is $23 \mathrm{~cm}$ ? (b) How much more potential energy does it contribute if its length increases to $26 \mathrm{~cm}$ ?

## Strategy

When the spring is at its unstretched length, it contributes nothing to the potential energy of the system, so we can use Equation 8.7 with the constant equal to zero. The value of $x$ is the length minus the unstretched length. When the spring is expanded, the spring's displacement or difference between its relaxed length and stretched length should be used for the $x$-value in calculating the potential energy of the spring.

## Solution

a. The displacement of the spring is $x=23 \mathrm{~cm}-20 \mathrm{~cm}=3 \mathrm{~cm}$, so the contributed potential energy is $U=\frac{1}{2} k x^{2}=\frac{1}{2}(4 \mathrm{~N} / \mathrm{cm})(3 \mathrm{~cm})^{2}=0.18 \mathrm{~J}$.

b. When the spring's displacement is $x=26 \mathrm{~cm}-20 \mathrm{~cm}=6 \mathrm{~cm}$, the potential energy is

$U=\frac{1}{2} k x^{2}=\frac{1}{2}(4 \mathrm{~N} / \mathrm{cm})(6 \mathrm{~cm})^{2}=0.72 \mathrm{~J}$, which is a $0.54-\mathrm{J}$ increase over the amount in part (a).

## Significance

Calculating the elastic potential energy and potential energy differences from Equation 8.7 involves solving for the potential energies based on the given lengths of the spring. Since $U$ depends on $x^{2}$, the potential energy for a compression (negative $x$ ) is the same as for an extension of equal magnitude.

## Gravitational and elastic potential energy

A simple system embodying both gravitational and elastic types of potential energy is a one-dimensional, vertical mass-spring system. This consists of a massive particle (or block), hung from one end of a perfectly elastic, massless spring, the other end of which is fixed, as illustrated in Figure 8.4.

First, let's consider the potential energy of the system. We need to define the constant in the potential energy function of Equation 8.5. Often, the ground is a suitable choice for when the gravitational potential energy is zero; however, in this case, the highest point or when $y=0$ is a convenient location for zero gravitational potential energy. Note that this choice is arbitrary, and the problem can be solved correctly even if another choice is picked.

We must also define the elastic potential energy of the system and the corresponding constant, as detailed in Equation 8.7. This is where the spring is unstretched, or at the $y=0$ position.

If we consider that the total energy of the system is conserved, then the energy at point A equals point C. The block is placed just on the spring so its initial kinetic energy is zero. By the setup of the problem discussed previously, both the gravitational potential energy and elastic potential energy are equal to zero. Therefore, the initial energy of the system is zero. When the block arrives at point C, its kinetic energy is zero. However, it now has both gravitational potential energy and elastic potential energy. Therefore, we can solve for the distance y that the block travels before coming to a stop:

$$
\begin{aligned}
K_{\mathrm{A}} & +U_{A}=K_{C}+U_{\mathrm{C}} \\
0 & =0+m g y_{C}+\frac{1}{2} k\left(y_{C}\right)^{2} \\
y_{\mathrm{C}} & =\frac{-2 m g}{k}
\end{aligned}
$$

## EXAMPLE 8.4

## Potential Energy of a Vertical Mass-Spring System

A block weighing $1.2 \mathrm{~N}$ is hung from a spring with a spring constant of $6.0 \mathrm{~N} / \mathrm{m}$, as shown in Figure 8.4. (a) What is the maximum expansion of the spring, as seen at point C? (b) What is the total potential energy at point $\mathrm{B}$, halfway between $\mathrm{A}$ and $\mathrm{C}$ ? (c) What is the speed of the block at point $\mathrm{B}$ ?

## Strategy

In part (a) we calculate the distance $y_{C}$ as discussed in the previous text. Then in part (b), we use half of the $\mathrm{y}$ value to calculate the potential energy at point B using equations Equation 8.4 and Equation 8.6. This energy must be equal to the kinetic energy, Equation 7.6, at point B since the initial energy of the system is zero. By calculating the kinetic energy at point $\mathrm{B}$, we can now calculate the speed of the block at point $\mathrm{B}$.

## Solution

a. Since the total energy of the system is zero at point A as discussed previously, the maximum expansion of the spring is calculated to be:

$$
\begin{aligned}
& y_{\mathrm{C}}=\frac{-2 m g}{k} \\
& y_{\mathrm{C}}=\frac{-2(1.2 \mathrm{~N})}{(6.0 \mathrm{~N} / \mathrm{m})}=-0.40 \mathrm{~m}
\end{aligned}
$$

b. The position of $y_{B}$ is half of the position at $y_{C}$ or $-0.20 \mathrm{~m}$. The total potential energy at point B would therefore be:

$$
\begin{aligned}
& U_{B}=m g y_{B}+\frac{1}{2} k\left(y_{C}\right)^{2} \\
& U_{B}=(1.2 \mathrm{~N})(-0.20 \mathrm{~m})+\frac{1}{2}(6 \mathrm{~N} / \mathrm{m})(-0.20 \mathrm{~m})^{2} \\
& U_{\mathrm{B}}=-0.12 \mathrm{~J}
\end{aligned}
$$

c. The mass of the block is the weight divided by gravity.

$$
m=\frac{F_{w}}{g}=\frac{1.2 \mathrm{~N}}{9.8 \mathrm{~m} / \mathrm{s}^{2}}=0.12 \mathrm{~kg}
$$

The kinetic energy at point $\mathrm{B}$ therefore is $0.12 \mathrm{~J}$ because the total energy is zero. Therefore, the speed of the block at point $B$ is equal to

$$
\begin{aligned}
& K=\frac{1}{2} m v^{2} \\
& v=\sqrt{\frac{2 K}{m}}=\sqrt{\frac{2(0.12 \mathrm{~J})}{(0.12 \mathrm{~kg})}}=1.4 \mathrm{~m} / \mathrm{s}
\end{aligned}
$$

## Significance

Even though the potential energy due to gravity is relative to a chosen zero location, the solutions to this problem would be the same if the zero energy points were chosen at different locations.

A sample chart of a variety of energies is shown in Table 8.1 to give you an idea about typical energy values associated with certain events. Some of these are calculated using kinetic energy, whereas others are calculated by using quantities found in a form of potential energy that may not have been discussed at this point.

| Object/phenomenon | Energy in joules |
| :--- | :--- |
| Big Bang | $10^{68}$ |
| Annual world energy use | $4.0 \times 10^{20}$ |
| Large fusion bomb (9 megaton) | $3.8 \times 10^{16}$ |
| Hiroshima-size fission bomb (10 kiloton) | $4.2 \times 10^{13}$ |
| 1 barrel crude oil | $5.9 \times 10^{9}$ |
| 1 metric ton TNT | $4.2 \times 10^{9}$ |
| 1 gallon of gasoline | $1.2 \times 10^{8}$ |
| Daily adult food intake (recommended) | $1.2 \times 10^{7}$ |
| $1000-\mathrm{kg}$ car at $90 \mathrm{~km} / \mathrm{h}$ | $3.1 \times 10^{5}$ |
| Tennis ball at $100 \mathrm{~km} / \mathrm{h}$ | 22 |
| Mosquito $\left(10^{-2} \mathrm{~g}\right.$ at $\left.0.5 \mathrm{~m} / \mathrm{s}\right)$ | $1.3 \times 10^{-6}$ |

Table 8.1 Energy of Various Objects and Phenomena

### 8.2 Conservative and Non-Conservative Forces

In Potential Energy and Conservation of Energy, any transition between kinetic and potential energy conserved the total energy of the system. This was path independent, meaning that we can start and stop at any two points in the problem, and the total energy of the system-kinetic plus potential-at these points are equal to each other. This is characteristic of a conservative force. We dealt with conservative forces in the preceding section, such as the gravitational force and spring force. When comparing the motion of the football in Figure 8.2, the total energy of the system never changes, even though the gravitational potential energy of the football increases, as the ball rises relative to ground and falls back to the initial gravitational potential energy when the football player catches the ball. Non-conservative forces are dissipative forces such as friction or air resistance. These forces take energy away from the system as the system progresses, energy that you can't get back. These forces are path dependent; therefore it matters where the object starts and stops.

## Conservative Force

The work done by a conservative force is independent of the path; in other words, the work done by a conservative force is the same for any path connecting two points:

$$
W_{A B, \text { path }-1}=\int_{A B, \text { path }-1} \overrightarrow{\mathbf{F}}_{\text {cons }} \cdot d \overrightarrow{\mathbf{r}}=W_{A B, \text { path- } 2}=\int_{A B, \text { path }-2} \overrightarrow{\mathbf{F}}_{\mathrm{cons}} \cdot d \overrightarrow{\mathbf{r}}
$$

The work done by a non-conservative force depends on the path taken.

Equivalently, a force is conservative if the work it does around any closed path is zero:

$$
W_{\text {closed path }}=\oint \overrightarrow{\mathbf{F}}_{\text {cons }} \cdot d \overrightarrow{\mathbf{r}}=0
$$

[In Equation 8.9, we use the notation of a circle in the middle of the integral sign for a line integral over a closed path, a notation found in most physics and engineering texts.] Equation 8.8 and Equation 8.9 are equivalent because any closed path is the sum of two paths: the first going from $A$ to $B$, and the second going from $B$ to $A$. The work done going along a path from $B$ to $A$ is the negative of the work done going along the same path from $A$ to $B$, where $A$ and $B$ are any two points on the closed path:

$$
\begin{aligned}
0=\int \overrightarrow{\mathbf{F}}_{\text {cons }} \cdot d \overrightarrow{\mathbf{r}} & =\int_{A B, \text { path-1 }} \overrightarrow{\mathbf{F}}_{\text {cons }} \cdot d \overrightarrow{\mathbf{r}}+\int_{B A, \text { path- } 2} \overrightarrow{\mathbf{F}}_{\text {cons }} \cdot d \overrightarrow{\mathbf{r}} \\
& =\int_{A B, \text { path-1 }} \overrightarrow{\mathbf{F}}_{\text {cons }} \cdot d \overrightarrow{\mathbf{r}}-\int_{A B, \text { path-2 }} \overrightarrow{\mathbf{F}}_{\text {cons }} \cdot d \overrightarrow{\mathbf{r}}=0
\end{aligned}
$$

You might ask how we go about proving whether or not a force is conservative, since the definitions involve any and all paths from $A$ to $B$, or any and all closed paths, but to do the integral for the work, you have to choose a particular path. One answer is that the work done is independent of path if the infinitesimal work $\overrightarrow{\mathbf{F}} \cdot d \overrightarrow{\mathbf{r}}$ is an exact differential, the way the infinitesimal net work was equal to the exact differential of the kinetic energy, $d W_{\text {net }}=m \overrightarrow{\mathbf{v}} \cdot d \overrightarrow{\mathbf{v}}=d \frac{1}{2} m \mathrm{v}^{2}$,

when we derived the work-energy theorem in Work-Energy Theorem. There are mathematical conditions that you can use to test whether the infinitesimal work done by a force is an exact differential, and the force is conservative. These conditions only involve differentiation and are thus relatively easy to apply. In two dimensions, the condition for $\overrightarrow{\mathbf{F}} \cdot d \overrightarrow{\mathbf{r}}=F_{x} d x+F_{y} d y$ to be an exact differential is

$$
\frac{d F_{x}}{d y}=\frac{d F_{y}}{d x}
$$

You may recall that the work done by the force in Example 7.4 depended on the path. For that force,

$$
F_{x}=(5 \mathrm{~N} / \mathrm{m}) y \text { and } F_{y}=(10 \mathrm{~N} / \mathrm{m}) x
$$

Therefore,

$$
\left(d F_{x} / d y\right)=5 \mathrm{~N} / \mathrm{m} \neq\left(d F_{y} / d x\right)=10 \mathrm{~N} / \mathrm{m}
$$

which indicates it is a non-conservative force. Can you see what you could change to make it a conservative force?

## EXAMPLE 8.5

## Conservative or Not?

Which of the following two-dimensional forces are conservative and which are not? Assume $a$ and $b$ are constants with appropriate units:
(a) $a x y^{3} \hat{\mathbf{i}}+a y x^{3} \hat{\mathbf{j}}$,
(b) $a\left[\left(y^{2} / x\right) \hat{\mathbf{i}}+2 y \ln (x / b) \hat{\mathbf{j}}\right]$
(c) $\frac{a x \hat{\mathbf{i}}+a y \hat{\mathbf{j}}}{x^{2}+y^{2}}$

## Strategy

Apply the condition stated in Equation 8.10, namely, using the derivatives of the components of each force indicated. If the derivative of the $y$-component of the force with respect to $x$ is equal to the derivative of the $x$-component of the force with respect to $y$, the force is a conservative force, which means the path taken for potential energy or work calculations always yields the same results.

## Solution

a. $\frac{d F_{x}}{d y}=\frac{d\left(a x y^{3}\right)}{d y}=3 a x y^{2}$ and $\frac{d F_{y}}{d x}=\frac{d\left(a y x^{3}\right)}{d x}=3 a y x^{2}$, so this force is non-conservative.
b. $\frac{d F_{x}}{d y}=\frac{d\left(a y^{2} / x\right)}{d y}=\frac{2 a y}{x}$ and $\frac{d F_{y}}{d x}=\frac{d(2 a y \ln (x / b))}{d x}=\frac{2 a y}{x}$, so this force is conservative.
c. $\frac{d F_{x}}{d y}=\frac{d\left(a x /\left(x^{2}+y^{2}\right)\right)}{d y}=-\frac{a x(2 y)}{\left(x^{2}+y^{2}\right)^{2}}=\frac{d F_{y}}{d x}=\frac{d\left(a y /\left(x^{2}+y^{2}\right)\right)}{d x}$, again conservative.

## Significance

The conditions in Equation 8.10 are derivatives as functions of a single variable; in three dimensions, similar conditions exist that involve more derivatives.

Before leaving this section, we note that non-conservative forces do not have potential energy associated with them because the energy is lost to the system and can't be turned into useful work later. So there is always a conservative force associated with every potential energy. We have seen that potential energy is defined in relation to the work done by conservative forces. That relation, Equation 8.1, involved an integral for the work; starting with the force and displacement, you integrated to get the work and the change in potential energy. However, integration is the inverse operation of differentiation; you could equally well have started with the potential energy and taken its derivative, with respect to displacement, to get the force. The infinitesimal increment of potential energy is the dot product of the force and the infinitesimal displacement,

$$
d U=-\overrightarrow{\mathbf{F}} \cdot d \overrightarrow{\mathbf{l}}=-F_{l} d l
$$

Here, we chose to represent the displacement in an arbitrary direction by $d \overrightarrow{\mathbf{l}}$, so as not to be restricted to any particular coordinate direction. We also expressed the dot product in terms of the magnitude of the infinitesimal displacement and the component of the force in its direction. Both these quantities are scalars, so you can divide by $d l$ to get

$$
F_{l}=-\frac{d U}{d l}
$$

This equation gives the relation between force and the potential energy associated with it. In words, the component of a conservative force, in a particular direction, equals the negative of the derivative of the corresponding potential energy, with respect to a displacement in that direction. For one-dimensional motion, say along the $x$-axis, Equation 8.11 give the entire vector force, $\overline{\mathbf{F}}=F_{x} \hat{\mathbf{i}}=-\frac{\partial U}{\partial x} \hat{\mathbf{i}}$.

In two dimensions,

$$
\overline{\mathbf{F}}=F_{x} \hat{\mathbf{i}}+F_{y} \hat{\mathbf{j}}=-\left(\frac{\partial U}{\partial x}\right) \hat{\mathbf{i}}-\left(\frac{\partial U}{\partial y}\right) \hat{\mathbf{j}}
$$

From this equation, you can see why Equation 8.11 is the condition for the work to be an exact differential, in
terms of the derivatives of the components of the force. In general, a partial derivative notation is used. If a function has many variables in it, the derivative is taken only of the variable the partial derivative specifies. The other variables are held constant. In three dimensions, you add another term for the $z$-component, and the result is that the force is the negative of the gradient of the potential energy. However, we won't be looking at three-dimensional examples just yet.

## EXAMPLE 8.6

## Force due to a Quartic Potential Energy

The potential energy for a particle undergoing one-dimensional motion along the $x$-axis is

$$
U(x)=\frac{1}{4} c x^{4}
$$

where $c=8 \mathrm{~N} / \mathrm{m}^{3}$. Its total energy at $x=0$ is $2 \mathrm{~J}$, and it is not subject to any non-conservative forces. Find (a) the positions where its kinetic energy is zero and (b) the forces at those positions.

## Strategy

(a) We can find the positions where $K=0$, so the potential energy equals the total energy of the given system. (b) Using Equation 8.11, we can find the force evaluated at the positions found from the previous part, since the mechanical energy is conserved.

## Solution

a. The total energy of the system of $2 \mathrm{~J}$ equals the quartic elastic energy as given in the problem,

$$
2 \mathrm{~J}=\frac{1}{4}\left(8 \mathrm{~N} / \mathrm{m}^{3}\right) x_{\mathrm{f}}^{4}
$$

Solving for $x_{\mathrm{f}}$ results in $x_{\mathrm{f}}= \pm 1 \mathrm{~m}$.

b. From Equation 8.11,

$$
F_{x}=-d U / d x=-c x^{3}
$$

Thus, evaluating the force at $\pm 1 \mathrm{~m}$, we get

$$
\overrightarrow{\mathbf{F}}=-\left(8 \mathrm{~N} / \mathrm{m}^{3}\right)( \pm 1 \mathrm{~m})^{3} \hat{\mathbf{i}}= \pm 8 \mathrm{~N} \hat{\mathbf{i}}
$$

At both positions, the magnitude of the forces is $8 \mathrm{~N}$ and the directions are toward the origin, since this is the potential energy for a restoring force.

## Significance

Finding the force from the potential energy is mathematically easier than finding the potential energy from the force, because differentiating a function is generally easier than integrating one.

### 8.3 Conservation of Energy

In this section, we elaborate and extend the result we derived in Potential Energy of a System, where we rewrote the work-energy theorem in terms of the change in the kinetic and potential energies of a particle. This will lead us to a discussion of the important principle of the conservation of mechanical energy. As you
continue to examine other topics in physics, in later chapters of this book, you will see how this conservation law is generalized to encompass other types of energy and energy transfers. The last section of this chapter provides a preview.

The terms 'conserved quantity' and 'conservation law' have specific, scientific meanings in physics, which are different from the everyday meanings associated with the use of these words. (The same comment is also true about the scientific and everyday uses of the word 'work.') In everyday usage, you could conserve water by not using it, or by using less of it, or by re-using it. Water is composed of molecules consisting of two atoms of hydrogen and one of oxygen. Bring these atoms together to form a molecule and you create water; dissociate the atoms in such a molecule and you destroy water. However, in scientific usage, a conserved quantity for a system stays constant, changes by a definite amount that is transferred to other systems, and/or is converted into other forms of that quantity. A conserved quantity, in the scientific sense, can be transformed, but not strictly created or destroyed. Thus, there is no physical law of conservation of water.

## Systems with a Single Particle or Object

We first consider a system with a single particle or object. Returning to our development of Equation 8.2, recall that we first separated all the forces acting on a particle into conservative and non-conservative types, and wrote the work done by each type of force as a separate term in the work-energy theorem. We then replaced the work done by the conservative forces by the change in the potential energy of the particle, combining it with the change in the particle's kinetic energy to get Equation 8.2. Now, we write this equation without the middle step and define the sum of the kinetic and potential energies, $K+U=E$; to be the mechanical energy of the particle.

## Conservation of Energy

The mechanical energy $E$ of a particle stays constant unless forces outside the system or non-conservative forces do work on it, in which case, the change in the mechanical energy is equal to the work done by the non-conservative forces:

$$
W_{\mathrm{nc}, A B}=\Delta(K+U)_{A B}=\Delta E_{A B}
$$

This statement expresses the concept of energy conservation for a classical particle as long as there is no non-conservative work. Recall that a classical particle is just a point mass, is nonrelativistic, and obeys Newton's laws of motion. In Relativity, we will see that conservation of energy still applies to a non-classical particle, but for that to happen, we have to make a slight adjustment to the definition of energy.

It is sometimes convenient to separate the case where the work done by non-conservative forces is zero, either because no such forces are assumed present, or, like the normal force, they do zero work when the motion is parallel to the surface. Then

$$
0=W_{\mathrm{nc}, A B}=\Delta(K+U)_{A B}=\Delta E_{A B}
$$

In this case, the conservation of mechanical energy can be expressed as follows: The mechanical energy of a particle does not change if all the non-conservative forces that may act on it do no work. Understanding the concept of energy conservation is the important thing, not the particular equation you use to express it.

## PROBLEM-SOLVING STRATEG

## Conservation of Energy

1. Identify the body or bodies to be studied (the system). Often, in applications of the principle of mechanical energy conservation, we study more than one body at the same time.
2. Identify all forces acting on the body or bodies.
3. Determine whether each force that does work is conservative. If a non-conservative force (e.g., friction) is
doing work, then mechanical energy is not conserved. The system must then be analyzed with nonconservative work, Equation 8.13 .
4. For every force that does work, choose a reference point and determine the potential energy function for the force. The reference points for the various potential energies do not have to be at the same location.
5. Apply the principle of mechanical energy conservation by setting the sum of the kinetic energies and potential energies equal at every point of interest.

## EXAMPLE 8.7

## Simple Pendulum

A particle of mass $m$ is hung from the ceiling by a massless string of length $1.0 \mathrm{~m}$, as shown in Figure 8.7 . The particle is released from rest, when the angle between the string and the downward vertical direction is $30^{\circ}$. What is its speed when it reaches the lowest point of its arc?

## Strategy

Using our problem-solving strategy, the first step is to define that we are interested in the particle-Earth system. Second, only the gravitational force is acting on the particle, which is conservative (step 3). We neglect air resistance in the problem, and no work is done by the string tension, which is perpendicular to the arc of the motion. Therefore, the mechanical energy of the system is conserved, as represented by Equation 8.13, $0=\Delta(K+U)$. Because the particle starts from rest, the increase in the kinetic energy is just the kinetic energy at the lowest point. This increase in kinetic energy equals the decrease in the gravitational potential energy, which we can calculate from the geometry. In step 4, we choose a reference point for zero gravitational potential energy to be at the lowest vertical point the particle achieves, which is mid-swing. Lastly, in step 5, we set the sum of energies at the highest point (initial) of the swing to the lowest point (final) of the swing to ultimately solve for the final speed.

## Solution

We are neglecting non-conservative forces, so we write the energy conservation formula relating the particle at the highest point (initial) and the lowest point in the swing (final) as

$$
K_{\mathrm{i}}+U_{\mathrm{i}}=K_{\mathrm{f}}+U_{\mathrm{f}}
$$

Since the particle is released from rest, the initial kinetic energy is zero. At the lowest point, we define the gravitational potential energy to be zero. Therefore our conservation of energy formula reduces to

$$
\begin{aligned}
0+m g h & =\frac{1}{2} m v^{2}+0 \\
v & =\sqrt{2 g h}
\end{aligned}
$$

The vertical height of the particle is not given directly in the problem. This can be solved for by using
trigonometry and two givens: the length of the pendulum and the angle through which the particle is vertically pulled up. Looking at the diagram, the vertical dashed line is the length of the pendulum string. The vertical height is labeled $h$. The other partial length of the vertical string can be calculated with trigonometry. That piece is solved for by

$$
\cos \theta=x / L, x=L \cos \theta
$$

Therefore, by looking at the two parts of the string, we can solve for the height $h$,

$$
\begin{aligned}
x+h & =L \\
L \cos \theta+h & =L \\
h & =L-L \cos \theta=L(1-\cos \theta)
\end{aligned}
$$

We substitute this height into the previous expression solved for speed to calculate our result:

$$
v=\sqrt{2 g L(1-\cos \theta)}=\sqrt{2\left(9.8 \mathrm{~m} / \mathrm{s}^{2}\right)(1 \mathrm{~m})\left(1-\cos 30^{\circ}\right)}=1.62 \mathrm{~m} / \mathrm{s}
$$

## Significance

We found the speed directly from the conservation of mechanical energy, without having to solve the differential equation for the motion of a pendulum (see Oscillations). We can approach this problem in terms of bar graphs of total energy. Initially, the particle has all potential energy, being at the highest point, and no kinetic energy. When the particle crosses the lowest point at the bottom of the swing, the energy moves from the potential energy column to the kinetic energy column. Therefore, we can imagine a progression of this transfer as the particle moves between its highest point, lowest point of the swing, and back to the highest point (Figure 8.8). As the particle travels from the lowest point in the swing to the highest point on the far right hand side of the diagram, the energy bars go in reverse order from (c) to (b) to (a).

## EXAMPLE 8.8

## Air Resistance on a Falling Object

A helicopter is hovering at an altitude of $1 \mathrm{~km}$ when a panel from its underside breaks loose and plummets to the ground (Figure 8.9). The mass of the panel is $15 \mathrm{~kg}$, and it hits the ground with a speed of $45 \mathrm{~m} / \mathrm{s}$. How
much mechanical energy was dissipated by air resistance during the panel's descent?

## Strategy

Step 1: Here only one body is being investigated.

Step 2: Gravitational force is acting on the panel, as well as air resistance, which is stated in the problem.

Step 3: Gravitational force is conservative; however, the non-conservative force of air resistance does negative work on the falling panel, so we can use the conservation of mechanical energy, in the form expressed by Equation 8.12, to find the energy dissipated. This energy is the magnitude of the work:

$$
\Delta E_{\mathrm{diss}}=\left|W_{\mathrm{nc}, \mathrm{if}}\right|=\left|\Delta(K+U)_{\mathrm{if}}\right|
$$

Step 4: The initial kinetic energy, at $y_{\mathrm{i}}=1 \mathrm{~km}$, is zero. We set the gravitational potential energy to zero at ground level out of convenience.

Step 5: The non-conservative work is set equal to the energies to solve for the work dissipated by air resistance.

## Solution

The mechanical energy dissipated by air resistance is the algebraic sum of the gain in the kinetic energy and loss in potential energy. Therefore the calculation of this energy is

$$
\begin{aligned}
\Delta E_{\text {diss }} & =\left|K_{\mathrm{f}}-K_{\mathrm{i}}+U_{\mathrm{f}}-U_{\mathrm{i}}\right| \\
& =\left|\frac{1}{2}(15 \mathrm{~kg})(45 \mathrm{~m} / \mathrm{s})^{2}-0+0-(15 \mathrm{~kg})\left(9.8 \mathrm{~m} / \mathrm{s}^{2}\right)(1000 \mathrm{~m})\right|=130 \mathrm{~kJ}
\end{aligned}
$$

## Significance

Most of the initial mechanical energy of the panel $\left(U_{\mathrm{i}}\right), 147 \mathrm{~kJ}$, was lost to air resistance. Notice that we were able to calculate the energy dissipated without knowing what the force of air resistance was, only that it was dissipative.

In these examples, we were able to use conservation of energy to calculate the speed of a particle just at particular points in its motion. But the method of analyzing particle motion, starting from energy conservation, is more powerful than that. More advanced treatments of the theory of mechanics allow you to calculate the full time dependence of a particle's motion, for a given potential energy. In fact, it is often the case that a better model for particle motion is provided by the form of its kinetic and potential energies, rather than an equation for force acting on it. (This is especially true for the quantum mechanical description of particles like electrons or atoms.)

We can illustrate some of the simplest features of this energy-based approach by considering a particle in onedimensional motion, with potential energy $U(x)$ and no non-conservative interactions present. Equation 8.12 and the definition of velocity require

$$
\begin{aligned}
K & =\frac{1}{2} m v^{2}=E-U(x) \\
v & =\frac{d x}{d t}=\sqrt{\frac{2(E-U(x))}{m}}
\end{aligned}
$$

Separate the variables $x$ and $t$ and integrate, from an initial time $t=0$ to an arbitrary time, to get

$$
t=\int_{0}^{t} d t=\int_{x_{0}}^{x} \frac{d x}{\sqrt{2[E-U(x)] / m}}
$$

If you can do the integral in Equation 8.14, then you can solve for $x$ as a function of $t$.

## EXAMPLE 8.9

## Constant Acceleration

Use the potential energy $U(x)=-E\left(x / x_{0}\right)$, for $E>0$, in Equation 8.14 to find the position $x$ of a particle as a function of time $t$.

## Strategy

Since we know how the potential energy changes as a function of $x$, we can substitute for $U(x)$ in Equation 8.14, integrate, and then solve for $x$. This results in an expression of $x$ as a function of time with constants of energy $E$, mass $m$, and the initial position $x_{0}$.

## Solution

Following the first two suggested steps in the above strategy,

$$
t=\int_{x_{0}}^{x} \frac{d x}{\sqrt{\left(2 E / m x_{0}\right)\left(x_{0}-x\right)}}=\frac{1}{\sqrt{\left(2 E / m x_{0}\right)}}\left|-2 \sqrt{\left(x_{0}-x\right)}\right|_{x_{0}}^{x}=-\frac{2 \sqrt{\left(x_{0}-x\right)}}{\sqrt{\left(2 E / m x_{0}\right)}}
$$

Solving for the position, we obtain $x(t)=x_{0}-\frac{1}{2}\left(E / m x_{0}\right) t^{2}$.

## Significance

The position as a function of time, for this potential, represents one-dimensional motion with constant acceleration, $a=\left(E / m x_{0}\right)$, starting at rest from position $x_{0}$. This is not so surprising, since this is a potential energy for a constant force, $F=-d U / d x=E / x_{0}$, and $a=F / m$.

## Systems with Several Particles or Objects

Systems generally consist of more than one particle or object. However, the conservation of mechanical energy, in one of the forms in Equation 8.12 or Equation 8.13, is a fundamental law of physics and applies to any system. You just have to include the kinetic and potential energies of all the particles, and the work done by all the non-conservative forces acting on them. Until you learn more about the dynamics of systems composed of many particles, in Linear Momentum and Collisions, Fixed-Axis Rotation, and Angular Momentum, it is better to postpone discussing the application of energy conservation to then.

### 8.4 Potential Energy Diagrams and Stability

Often, you can get a good deal of useful information about the dynamical behavior of a mechanical system just by interpreting a graph of its potential energy as a function of position, called a potential energy diagram. This is most easily accomplished for a one-dimensional system, whose potential energy can be plotted in one two-dimensional graph-for example, $U(x)$ versus $x$-on a piece of paper or a computer program. For systems whose motion is in more than one dimension, the motion needs to be studied in three-dimensional space. We will simplify our procedure for one-dimensional motion only.

First, let's look at an object, freely falling vertically, near the surface of Earth, in the absence of air resistance. The mechanical energy of the object is conserved, $\boldsymbol{E}=\boldsymbol{K}+\boldsymbol{U}$, and the potential energy, with respect to zero at ground level, is $U(y)=m g y$, which is a straight line through the origin with slope $m g$. In the graph shown in Figure 8.10, the $x$-axis is the height above the ground $y$ and the $y$-axis is the object's energy.

The line at energy E represents the constant mechanical energy of the object, whereas the kinetic and potential energies, $K_{A}$ and $U_{A}$, are indicated at a particular height $y_{A}$. You can see how the total energy is divided between kinetic and potential energy as the object's height changes. Since kinetic energy can never be negative, there is a maximum potential energy and a maximum height, which an object with the given total energy cannot exceed:

$$
\begin{aligned}
& K=E-U \geq 0 \\
& U \leq E
\end{aligned}
$$

If we use the gravitational potential energy reference point of zero at $y_{0}$, we can rewrite the gravitational potential energy $U$ as $m g y$. Solving for $y$ results in

$$
y \leq E / m g=y_{\max }
$$

We note in this expression that the quantity of the total energy divided by the weight $(\mathrm{mg})$ is located at the maximum height of the particle, or $y_{\max }$. At the maximum height, the kinetic energy and the speed are zero, so if the object were initially traveling upward, its velocity would go through zero there, and $y_{\max }$ would be a turning point in the motion. At ground level, $y_{0}=0$, the potential energy is zero, and the kinetic energy and the speed are maximum:

$$
\begin{aligned}
U_{0} & =0=E-K_{0} \\
E & =K_{0}=\frac{1}{2} m v_{0}^{2} \\
v_{0} & = \pm \sqrt{2 E / m}
\end{aligned}
$$

The maximum speed $\pm v_{0}$ gives the initial velocity necessary to reach $y_{\max }$, the maximum height, and $-v_{0}$ represents the final velocity, after falling from $y_{\max }$. You can read all this information, and more, from the potential energy diagram we have shown.

Consider a mass-spring system on a frictionless, stationary, horizontal surface, so that gravity and the normal contact force do no work and can be ignored (Figure 8.11). This is like a one-dimensional system, whose mechanical energy $E$ is a constant and whose potential energy, with respect to zero energy at zero displacement from the spring's unstretched length, $x=0$, is $U(x)=\frac{1}{2} k x^{2}$.

You can read off the same type of information from the potential energy diagram in this case, as in the case for the body in vertical free fall, but since the spring potential energy describes a variable force, you can learn more from this graph. As for the object in vertical free fall, you can deduce the physically allowable range of motion and the maximum values of distance and speed, from the limits on the kinetic energy, $0 \leq K \leq E$. Therefore, $K=0$ and $U=E$ at a turning point, of which there are two for the elastic spring potential energy,

$$
x_{\max }= \pm \sqrt{2 E / k}
$$

The glider's motion is confined to the region between the turning points, $-x_{\max } \leq x \leq x_{\max }$. This is true for any (positive) value of $E$ because the potential energy is unbounded with respect to $x$. For this reason, as well as the shape of the potential energy curve, $U(x)$ is called an infinite potential well. At the bottom of the potential well, $x=0, U=0$ and the kinetic energy is a maximum, $K=E$, so $v_{\max }= \pm \sqrt{2 E / m}$.

However, from the slope of this potential energy curve, you can also deduce information about the force on the glider and its acceleration. We saw earlier that the negative of the slope of the potential energy is the spring force, which in this case is also the net force, and thus is proportional to the acceleration. When $x=0$, the
slope, the force, and the acceleration are all zero, so this is an equilibrium point. The negative of the slope, on either side of the equilibrium point, gives a force pointing back to the equilibrium point, $F= \pm k x$, so the equilibrium is termed stable and the force is called a restoring force. This implies that $U(x)$ has a relative minimum there. If the force on either side of an equilibrium point has a direction opposite from that direction of position change, the equilibrium is termed unstable, and this implies that $U(x)$ has a relative maximum there.

## EXAMPLE 8.10

## Quartic and Quadratic Potential Energy Diagram

The potential energy for a particle undergoing one-dimensional motion along the $x$-axis is $U(x)=2\left(x^{4}-x^{2}\right)$, where $U$ is in joules and $x$ is in meters. The particle is not subject to any non-conservative forces and its mechanical energy is constant at $E=-0.25 \mathrm{~J}$. (a) Is the motion of the particle confined to any regions on the $x$-axis, and if so, what are they? (b) Are there any equilibrium points, and if so, where are they and are they stable or unstable?

## Strategy

First, we need to graph the potential energy as a function of $x$. The function is zero at the origin, becomes negative as $x$ increases in the positive or negative directions ( $x^{2}$ is larger than $x^{4}$ for $x<1$ ), and then becomes positive at sufficiently large $|x|$. Your graph should look like a double potential well, with the zeros determined by solving the equation $U(x)=0$, and the extremes determined by examining the first and second derivatives of $U(x)$, as shown in Figure 8.12 .

You can find the values of (a) the allowed regions along the $x$-axis, for the given value of the mechanical energy, from the condition that the kinetic energy can't be negative, and (b) the equilibrium points and their stability from the properties of the force (stable for a relative minimum and unstable for a relative maximum of potential energy).

You can just eyeball the graph to reach qualitative answers to the questions in this example. That, after all, is the value of potential energy diagrams. You can see that there are two allowed regions for the motion $(E>U)$ and three equilibrium points (slope $d U / d x=0$ ), of which the central one is unstable $\left(d^{2} U / d x^{2}<0\right)$, and the
other two are stable $\left(d^{2} U / d x^{2}>0\right)$.

## Solution

a. To find the allowed regions for $x$, we use the condition

$$
K=E-U=-\frac{1}{4}-2\left(x^{4}-x^{2}\right) \geq 0
$$

If we complete the square in $x^{2}$, this condition simplifies to $2\left(x^{2}-\frac{1}{2}\right)^{2} \leq \frac{1}{4}$, which we can solve to obtain

$$
\frac{1}{2}-\sqrt{\frac{1}{8}} \leq x^{2} \leq \frac{1}{2}+\sqrt{\frac{1}{8}}
$$

This represents two allowed regions, $x_{p} \leq x \leq x_{R}$ and $-x_{R} \leq x \leq-x_{p}$, where $x_{p}=0.38$ and $x_{R}=0.92$ (in meters).

b. To find the equilibrium points, we solve the equation

$$
d U / d x=8 x^{3}-4 x=0
$$

and find $x=0$ and $x= \pm x_{Q}$, where $x_{Q}=1 / \sqrt{2}=0.707$ (meters). The second derivative

$$
d^{2} U / d x^{2}=24 x^{2}-4
$$

is negative at $x=0$, so that position is a relative maximum and the equilibrium there is unstable. The second derivative is positive at $x= \pm x_{Q}$, so these positions are relative minima and represent stable equilibria.

## Significance

The particle in this example can oscillate in the allowed region about either of the two stable equilibrium points we found, but it does not have enough energy to escape from whichever potential well it happens to initially be in. The conservation of mechanical energy and the relations between kinetic energy and speed, and potential energy and force, enable you to deduce much information about the qualitative behavior of the motion of a particle, as well as some quantitative information, from a graph of its potential energy.

## EXAMPLE 8.11

## Sinusoidal Oscillations

Find $x(t)$ for a particle moving with a constant mechanical energy $E>0$ and a potential energy $U(x)=\frac{1}{2} k x^{2}$, when the particle starts from rest at time $t=0$.

## Strategy

We follow the same steps as we did in Example 8.9. Substitute the potential energy $U$ into Equation 8.14 and factor out the constants, like $m$ or $k$. Integrate the function and solve the resulting expression for position, which is now a function of time.

## Solution

Substitute the potential energy in Equation 8.14 and integrate using an integral solver found on a web search:

$$
t=\int_{x_{0}}^{x} \frac{d x}{\sqrt{(k / m)\left[(2 E / k)-x^{2}\right]}}=\sqrt{\frac{m}{k}}\left[\sin ^{-1}\left(\frac{x}{\sqrt{2 E / k}}\right)-\sin ^{-1}\left(\frac{x_{0}}{\sqrt{2 E / k}}\right)\right]
$$

From the initial conditions at $t=0$, the initial kinetic energy is zero and the initial potential energy is $\frac{1}{2} k x_{0}^{2}=E$, from which you can see that $x_{0} / \sqrt{(2 E / k)}= \pm 1$ and $\sin ^{-1}( \pm)= \pm 90^{0}$. Now you can solve for $x$ :

$$
x(t)=\sqrt{(2 E / k)} \sin \left[(\sqrt{k / m}) t \pm 90^{0}\right]= \pm \sqrt{(2 E / k)} \cos [(\sqrt{k / m}) t]
$$

## Significance

A few paragraphs earlier, we referred to this mass-spring system as an example of a harmonic oscillator. Here, we anticipate that a harmonic oscillator executes sinusoidal oscillations with a maximum displacement of $\sqrt{(2 E / k)}$ (called the amplitude) and a rate of oscillation of $(1 / 2 \pi) \sqrt{k / m}$ (called the frequency). Further discussions about oscillations can be found in Oscillations.

### 8.5 Sources of Energy

In this chapter, we have studied energy. We learned that energy can take different forms and can be transferred from one form to another. You will find that energy is discussed in many everyday, as well as scientific, contexts, because it is involved in all physical processes. It will also become apparent that many situations are best understood, or most easily conceptualized, by considering energy. So far, no experimental results have contradicted the conservation of energy. In fact, whenever measurements have appeared to conflict with energy conservation, new forms of energy have been discovered or recognized in accordance with this principle.

What are some other forms of energy? Many of these are covered in later chapters (also see Figure 8.13), but let's detail a few here:

- Atoms and molecules inside all objects are in random motion. The internal kinetic energy from these random motions is called thermal energy, because it is related to the temperature of the object. Note that thermal energy can also be transferred from one place to another, not transformed or converted, by the familiar processes of conduction, convection, and radiation. In this case, the energy is known as heat energy.
- Electrical energy is a common form that is converted to many other forms and does work in a wide range of practical situations.
- Fuels, such as gasoline and food, have chemical energy, which is potential energy arising from their molecular structure. Chemical energy can be converted into thermal energy by reactions like oxidation. Chemical reactions can also produce electrical energy, such as in batteries. Electrical energy can, in turn, produce thermal energy and light, such as in an electric heater or a light bulb.
- Light is just one kind of electromagnetic radiation, or radiant energy, which also includes radio, infrared, ultraviolet, X-rays, and gamma rays. All bodies with thermal energy can radiate energy in electromagnetic waves.
- Nuclear energy comes from reactions and processes that convert measurable amounts of mass into energy. Nuclear energy is transformed into radiant energy in the Sun, into thermal energy in the boilers of
nuclear power plants, and then into electrical energy in the generators of power plants. These and all other forms of energy can be transformed into one another and, to a certain degree, can be converted into mechanical work.

The transformation of energy from one form into another happens all the time. The chemical energy in food is converted into thermal energy through metabolism; light energy is converted into chemical energy through photosynthesis. Another example of energy conversion occurs in a solar cell. Sunlight impinging on a solar cell produces electricity, which can be used to run electric motors or heat water. In an example encompassing many steps, the chemical energy contained in coal is converted into thermal energy as it burns in a furnace, to transform water into steam, in a boiler. Some of the thermal energy in the steam is then converted into mechanical energy as it expands and spins a turbine, which is connected to a generator to produce electrical energy. In these examples, not all of the initial energy is converted into the forms mentioned, because some energy is always transferred to the environment.

Energy is an important element at all levels of society. We live in a very interdependent world, and access to adequate and reliable energy resources is crucial for economic growth and for maintaining the quality of our lives. The principal energy resources used in the world are shown in Figure 8.14. The figure distinguishes between two major types of energy sources: renewable and non-renewable, and further divides each type into a few more specific kinds. Renewable sources are energy sources that are replenished through naturally occurring, ongoing processes, on a time scale that is much shorter than the anticipated lifetime of the civilization using the source. Non-renewable sources are depleted once some of the energy they contain is
extracted and converted into other kinds of energy. The natural processes by which non-renewable sources are formed typically take place over geological time scales.

| Renewables |  |
| :---: | :---: |
| Biomass heat | $11.44 \%$ |
| Solar hotwater | $0.17 \%$ |
| Geothermal heat | $0.12 \%$ |
| Hydropower | $3.34 \%$ |
| Ethanol | $0.50 \%$ |
| Biodiesel | $0.17 \%$ |
| Biomass electricity | $0.28 \%$ |
| Wind power | $0.51 \%$ |
| Geothermal electricity | $0.07 \%$ |
| Solar PV power | $0.06 \%$ |
| Solar CSP | $0.002 \%$ |
| ■ocean power | $0.001 \%$ |

Figure 8.14 World energy consumption by source; the percentage of renewables is increasing, accounting for $19 \%$ in 2012.

Our most important non-renewable energy sources are fossil fuels, such as coal, petroleum, and natural gas. These account for about $81 \%$ of the world's energy consumption, as shown in the figure. Burning fossil fuels creates chemical reactions that transform potential energy, in the molecular structures of the reactants, into thermal energy and products. This thermal energy can be used to heat buildings or to operate steam-driven machinery. Internal combustion and jet engines convert some of the energy of rapidly expanding gases, released from burning gasoline, into mechanical work. Electrical power generation is mostly derived from transferring energy in expanding steam, via turbines, into mechanical work, which rotates coils of wire in magnetic fields to generate electricity. Nuclear energy is the other non-renewable source shown in Figure 8.14 and supplies about $3 \%$ of the world's consumption. Nuclear reactions release energy by transforming potential energy, in the structure of nuclei, into thermal energy, analogous to energy release in chemical reactions. The thermal energy obtained from nuclear reactions can be transferred and converted into other forms in the same ways that energy from fossil fuels are used.

An unfortunate byproduct of relying on energy produced from the combustion of fossil fuels is the release of carbon dioxide into the atmosphere and its contribution to global warming. Nuclear energy poses environmental problems as well, including the safety and disposal of nuclear waste. Besides these important consequences, reserves of non-renewable sources of energy are limited and, given the rapidly growing rate of world energy consumption, may not last for more than a few hundred years. Considerable effort is going on to develop and expand the use of renewable sources of energy, involving a significant percentage of the world's physicists and engineers.

Four of the renewable energy sources listed in Figure 8.14-those using material from plants as fuel (biomass heat, ethanol, biodiesel, and biomass electricity)-involve the same types of energy transformations and conversions as just discussed for fossil and nuclear fuels. The other major types of renewable energy sources are hydropower, wind power, geothermal power, and solar power.

Hydropower is produced by converting the gravitational potential energy of falling or flowing water into kinetic energy and then into work to run electric generators or machinery. Converting the mechanical energy in ocean surface waves and tides is in development. Wind power also converts kinetic energy into work, which can be used directly to generate electricity, operate mills, and propel sailboats.

The interior of Earth has a great deal of thermal energy, part of which is left over from its original formation (gravitational potential energy converted into thermal energy) and part of which is released from radioactive minerals (a form of natural nuclear energy). It will take a very long time for this geothermal energy to escape
into space, so people generally regard it as a renewable source, when actually, it's just inexhaustible on human time scales.

The source of solar power is energy carried by the electromagnetic waves radiated by the Sun. Most of this energy is carried by visible light and infrared (heat) radiation. When suitable materials absorb electromagnetic waves, radiant energy is converted into thermal energy, which can be used to heat water, or when concentrated, to make steam and generate electricity (Figure 8.15). However, in another important physical process, known as the photoelectric effect, energetic radiation impinging on certain materials is directly converted into electricity. Materials that do this are called photovoltaics (PV in Figure 8.14). Some solar power systems use lenses or mirrors to concentrate the Sun's rays, before converting their energy through photovoltaics, and these are qualified as CSP in Figure 8.14.

As we finish this chapter on energy and work, it is relevant to draw some distinctions between two sometimes misunderstood terms in the area of energy use. As we mentioned earlier, the "law of conservation of energy" is a very useful principle in analyzing physical processes. It cannot be proven from basic principles but is a very good bookkeeping device, and no exceptions have ever been found. It states that the total amount of energy in an isolated system always remains constant. Related to this principle, but remarkably different from it, is the important philosophy of energy conservation. This concept has to do with seeking to decrease the amount of energy used by an individual or group through reducing activities (e.g., turning down thermostats, diving fewer kilometers) and/or increasing conversion efficiencies in the performance of a particular task, such as developing and using more efficient room heaters, cars that have greater miles-per-gallon ratings, energyefficient compact fluorescent lights, etc.

Since energy in an isolated system is not destroyed, created, or generated, you might wonder why we need to be concerned about our energy resources, since energy is a conserved quantity. The problem is that the final result of most energy transformations is waste heat, that is, work that has been "degraded" in the energy transformation. We will discuss this idea in more detail in the chapters on thermodynamics.

