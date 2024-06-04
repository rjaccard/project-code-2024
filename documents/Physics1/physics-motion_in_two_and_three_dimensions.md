# CHAPTER 4 Motion in Two and Three Dimensions 

INTRODUCTION To give a complete description of kinematics, we must explore motion in two and three dimensions. After all, most objects in our universe do not move in straight lines; rather, they follow curved paths. From kicked footballs to the flight paths of birds to the orbital motions of celestial bodies and down to the flow of blood plasma in your veins, most motion follows curved trajectories.

Fortunately, the treatment of motion in one dimension in the previous chapter has given us a foundation on which to build, as the concepts of position, displacement, velocity, and acceleration defined in one dimension can be expanded to two and three dimensions. Consider the Red Arrows, also known as the Royal Air Force

Aerobatic team of the United Kingdom. Each jet follows a unique curved trajectory in three-dimensional airspace, as well as has a unique velocity and acceleration. Thus, to describe the motion of any of the jets accurately, we must assign to each jet a unique position vector in three dimensions as well as a unique velocity and acceleration vector. We can apply the same basic equations for displacement, velocity, and acceleration we derived in Motion Along a Straight Line to describe the motion of the jets in two and three dimensions, but with some modifications-in particular, the inclusion of vectors.

In this chapter we also explore two special types of motion in two dimensions: projectile motion and circular motion. Last, we conclude with a discussion of relative motion. In the chapter-opening picture, each jet has a relative motion with respect to any other jet in the group or to the people observing the air show on the ground.

### 4.1 Displacement and Velocity Vectors

Displacement and velocity in two or three dimensions are straightforward extensions of the one-dimensional definitions. However, now they are vector quantities, so calculations with them have to follow the rules of vector algebra, not scalar algebra.

## Displacement Vector

To describe motion in two and three dimensions, we must first establish a coordinate system and a convention for the axes. We generally use the coordinates $x, y$, and $z$ to locate a particle at point $P(x, y, z)$ in three dimensions. If the particle is moving, the variables $x, y$, and $z$ are functions of time $(t)$ :

$$
x=x(t) \quad y=y(t) \quad z=z(t)
$$

The position vector from the origin of the coordinate system to point $P$ is $\overrightarrow{\mathbf{r}}(t)$. In unit vector notation, introduced in Coordinate Systems and Components of a Vector, $\overrightarrow{\mathbf{r}}(t)$ is

$$
\overrightarrow{\mathbf{r}}(t)=x(t) \hat{\mathbf{i}}+y(t) \hat{\mathbf{j}}+z(t) \hat{\mathbf{k}}
$$

Figure 4.2 shows the coordinate system and the vector to point $P$, where a particle could be located at a particular time $t$. Note the orientation of the $x, y$, and $z$ axes. This orientation is called a right-handed coordinate system (Coordinate Systems and Components of a Vector) and it is used throughout the chapter.

With our definition of the position of a particle in three-dimensional space, we can formulate the threedimensional displacement. Figure 4.3 shows a particle at time $t_{1}$ located at $P_{1}$ with position vector $\overrightarrow{\mathbf{r}}\left(t_{1}\right)$. At a
later time $t_{2}$, the particle is located at $P_{2}$ with position vector $\overrightarrow{\mathbf{r}}\left(t_{2}\right)$. The displacement vector $\Delta \overrightarrow{\mathbf{r}}$ is found by subtracting $\overrightarrow{\mathbf{r}}\left(t_{1}\right)$ from $\overrightarrow{\mathbf{r}}\left(t_{2}\right) \quad:$

$$
\Delta \overrightarrow{\mathbf{r}}=\overrightarrow{\mathbf{r}}\left(t_{2}\right)-\overrightarrow{\mathbf{r}}\left(t_{1}\right)
$$

Vector addition is discussed in Vectors. Note that this is the same operation we did in one dimension, but now the vectors are in three-dimensional space.

The following examples illustrate the concept of displacement in multiple dimensions.

## EXAMPLE 4.1

## Polar Orbiting Satellite

A satellite is in a circular polar orbit around Earth at an altitude of $400 \mathrm{~km}$-meaning, it passes directly overhead at the North and South Poles. What is the magnitude and direction of the displacement vector from when it is directly over the North Pole to when it is at $-45^{\circ}$ latitude?

## Strategy

We make a picture of the problem to visualize the solution graphically. This will aid in our understanding of the displacement. We then use unit vectors to solve for the displacement.

## Solution

Figure 4.4 shows the surface of Earth and a circle that represents the orbit of the satellite. Although satellites are moving in three-dimensional space, they follow trajectories of ellipses, which can be graphed in two dimensions. The position vectors are drawn from the center of Earth, which we take to be the origin of the coordinate system, with the $y$-axis as north and the $x$-axis as east. The vector between them is the displacement of the satellite. We take the radius of Earth as $6370 \mathrm{~km}$, so the length of each position vector is $6770 \mathrm{~km}$.

In unit vector notation, the position vectors are

$$
\begin{aligned}
& \overrightarrow{\mathbf{r}}\left(t_{1}\right)=6770 \cdot \mathrm{km} \hat{\mathbf{j}} \\
& \overrightarrow{\mathbf{r}}\left(t_{2}\right)=6770 \cdot \mathrm{km}\left(\cos \left(-45^{\circ}\right)\right) \hat{\mathbf{i}}+6770 \cdot \mathrm{km}\left(\sin \left(-45^{\circ}\right)\right) \hat{\mathbf{j}}
\end{aligned}
$$

Evaluating the sine and cosine, we have

$$
\begin{aligned}
\overrightarrow{\mathbf{r}}\left(t_{1}\right) & =6770 \cdot \hat{\mathbf{j}} \\
\overrightarrow{\mathbf{r}}\left(t_{2}\right) & =4787 \hat{\mathbf{i}}-4787 \hat{\mathbf{j}}
\end{aligned}
$$

Now we can find $\Delta \overrightarrow{\mathbf{r}}$, the displacement of the satellite:

$$
\Delta \overrightarrow{\mathbf{r}}=\overrightarrow{\mathbf{r}}\left(t_{2}\right)-\overrightarrow{\mathbf{r}}\left(t_{1}\right)=4787 \hat{\mathbf{i}}-11,557 \hat{\mathbf{j}}
$$

The magnitude of the displacement is $|\Delta \overrightarrow{\mathbf{r}}|=\sqrt{(4787)^{2}+(-11,557)^{2}}=12,509 \mathrm{~km}$. The angle the displacement makes with the $x$-axis is $\theta=\tan ^{-1}\left(\frac{-11,557}{4787}\right)=-67.5^{\circ}$.

## Significance

Plotting the displacement gives information and meaning to the unit vector solution to the problem. When plotting the displacement, we need to include its components as well as its magnitude and the angle it makes with a chosen axis-in this case, the $x$-axis (Figure 4.5).

Note that the satellite took a curved path along its circular orbit to get from its initial position to its final position in this example. It also could have traveled $4787 \mathrm{~km}$ east, then $11,557 \mathrm{~km}$ south to arrive at the same location. Both of these paths are longer than the length of the displacement vector. In fact, the displacement vector gives the shortest path between two points in one, two, or three dimensions.

Many applications in physics can have a series of displacements, as discussed in the previous chapter. The total displacement is the sum of the individual displacements, only this time, we need to be careful, because we are adding vectors. We illustrate this concept with an example of Brownian motion.

EXAMPLE 4.2

## Brownian Motion

Brownian motion is a chaotic random motion of particles suspended in a fluid, resulting from collisions with the molecules of the fluid. This motion is three-dimensional. The displacements in numerical order of a particle undergoing Brownian motion could look like the following, in micrometers (Figure 4.6):

$$
\begin{aligned}
& \Delta \overrightarrow{\mathbf{r}}_{1}=2.0 \hat{\mathbf{i}}+\hat{\mathbf{j}}+3.0 \widehat{\mathbf{k}} \\
& \Delta \overrightarrow{\mathbf{r}}_{2}=-\hat{\mathbf{i}}+3.0 \hat{\mathbf{k}} \\
& \Delta \overrightarrow{\mathbf{r}}_{3}=4.0 \hat{\mathbf{i}}-2.0 \hat{\mathbf{j}}+\hat{\mathbf{k}} \\
& \Delta \overrightarrow{\mathbf{r}}_{4}=-3.0 \hat{\mathbf{i}}+\hat{\mathbf{j}}+2.0 \widehat{\mathbf{k}}
\end{aligned}
$$

What is the total displacement of the particle from the origin?

## Solution

We form the sum of the displacements and add them as vectors:

$$
\begin{aligned}
\Delta \overrightarrow{\mathbf{r}}_{\text {Total }} & =\sum \Delta \overrightarrow{\mathbf{r}}_{i}=\Delta \overrightarrow{\mathbf{r}}_{1}+\Delta \overrightarrow{\mathbf{r}}_{2}+\Delta \overrightarrow{\mathbf{r}}_{3}+\Delta \overrightarrow{\mathbf{r}}_{4} \\
& =(2.0-1.0+4.0-3.0) \hat{\mathbf{i}}+(1.0+0-2.0+1.0) \hat{\mathbf{j}}+(3.0+3.0+1.0+2.0) \widehat{\mathbf{k}} \\
& =2.0 \hat{\mathbf{i}}+0 \hat{\mathbf{j}}+9.0 \widehat{\mathbf{k}} \boldsymbol{\mu} \mathrm{m}
\end{aligned}
$$

To complete the solution, we express the displacement as a magnitude and direction,

$$
\left|\Delta \overrightarrow{\mathbf{r}}_{\text {Total }}\right|=\sqrt{2.0^{2}+0^{2}+9.0^{2}}=9.2 \mu \mathrm{m}, \quad \theta=\tan ^{-1}\left(\frac{9}{2}\right)=77^{\circ}
$$

with respect to the $x$-axis in the $x z$-plane.

## Significance

From the figure we can see the magnitude of the total displacement is less than the sum of the magnitudes of the individual displacements.

## Velocity Vector

In the previous chapter we found the instantaneous velocity by calculating the derivative of the position function with respect to time. We can do the same operation in two and three dimensions, but we use vectors. The instantaneous velocity vector is now

$$
\overrightarrow{\mathbf{v}}(t)=\lim _{\Delta t \rightarrow 0} \frac{\overrightarrow{\mathbf{r}}(t+\Delta t)-\overrightarrow{\mathbf{r}}(t)}{\Delta t}=\frac{d \overrightarrow{\mathbf{r}}}{d t}
$$

Let's look at the relative orientation of the position vector and velocity vector graphically. In Figure 4.7 we show the vectors $\overrightarrow{\mathbf{r}}(t)$ and $\overrightarrow{\mathbf{r}}(t+\Delta t)$, which give the position of a particle moving along a path represented by the gray line. As $\Delta t$ goes to zero, the velocity vector, given by Equation 4.4, becomes tangent to the path of the particle at time $t$.

Equation 4.4 can also be written in terms of the components of $\overrightarrow{\mathbf{v}}(t)$. Since

$$
\overrightarrow{\mathbf{r}}(t)=x(t) \hat{\mathbf{i}}+y(t) \hat{\mathbf{j}}+z(t) \widehat{\mathbf{k}}
$$

we can write

$$
\overrightarrow{\mathbf{v}}(t)=v_{x}(t) \hat{\mathbf{i}}+v_{y}(t) \hat{\mathbf{j}}+v_{z}(t) \hat{\mathbf{k}}
$$

where

$$
v_{x}(t)=\frac{d x(t)}{d t}, \quad v_{y}(t)=\frac{d y(t)}{d t}, \quad v_{z}(t)=\frac{d z(t)}{d t}
$$

If only the average velocity is of concern, we have the vector equivalent of the one-dimensional average velocity for two and three dimensions:

$$
\overrightarrow{\mathbf{v}}_{\text {avg }}=\frac{\overrightarrow{\mathbf{r}}\left(t_{2}\right)-\overrightarrow{\mathbf{r}}\left(t_{1}\right)}{t_{2}-t_{1}}
$$

## EXAMPLE 4.3

## Calculating the Velocity Vector

The position function of a particle is $\overrightarrow{\mathbf{r}}(t)=2.0 t^{2} \hat{\mathbf{i}}+(2.0+3.0 t) \hat{\mathbf{j}}+5.0 t \hat{\mathbf{k}}$. (a) What is the instantaneous velocity and speed at $t=2.0 \mathrm{~s}$ ? (b) What is the average velocity between $1.0 \mathrm{~s}$ and $3.0 \mathrm{~s}$ ?

## Solution

Using Equation 4.5 and Equation 4.6, and taking the derivative of the position function with respect to time, we find

(a) $v(t)=\frac{d \mathbf{r}(t)}{d t}=4.0 t \hat{\mathbf{i}}+3.0 \widehat{\mathbf{j}}+5.0 \widehat{\mathbf{k}} \mathrm{m} / \mathrm{s}$

$$
\begin{aligned}
& \overrightarrow{\mathbf{v}}(2.0 \mathrm{~s})=8.0 \hat{\mathbf{i}}+3.0 \hat{\mathbf{j}}+5.0 \hat{\mathbf{k}} \mathrm{m} / \mathrm{s} \\
& \text { Speed }|\overrightarrow{\mathbf{v}}(2.0 \mathrm{~s})|=\sqrt{8^{2}+3^{2}+5^{2}}=9.9 \mathrm{~m} / \mathrm{s}
\end{aligned}
$$

(b) From Equation 4.7,

$$
\begin{aligned}
\overrightarrow{\mathbf{v}}_{\mathrm{avg}} & =\frac{\overrightarrow{\mathbf{r}}\left(t_{2}\right)-\overrightarrow{\mathbf{r}}\left(t_{1}\right)}{t_{2}-t_{1}}=\frac{\overrightarrow{\mathbf{r}}(3.0 \mathrm{~s})-\overrightarrow{\mathbf{r}}(1.0 \mathrm{~s})}{3.0 \mathrm{~s}-1.0 \mathrm{~s}}=\frac{(18 \hat{\mathbf{i}}+11 \hat{\mathbf{j}}+15 \widehat{\mathbf{k}}) \mathrm{m}-(2 \hat{\mathbf{i}}+5 \hat{\mathbf{j}}+5 \hat{\mathbf{k}}) \mathrm{m}}{2.0 \mathrm{~s}} \\
& =\frac{(16 \hat{\mathbf{i}}+6 \widehat{\mathbf{j}}+10 \widehat{\mathbf{k}}) \mathrm{m}}{2.0 \mathrm{~s}}=8.0 \hat{\mathbf{i}}+3.0 \hat{\mathbf{j}}+5.0 \widehat{\mathbf{k}} \mathrm{m} / \mathrm{s}
\end{aligned}
$$

## Significance

We see the average velocity is the same as the instantaneous velocity at $t=2.0 \mathrm{~s}$, as a result of the velocity function being linear. This need not be the case in general. In fact, most of the time, instantaneous and average velocities are not the same.

## The Independence of Perpendicular Motions

When we look at the three-dimensional equations for position and velocity written in unit vector notation, Equation 4.2 and Equation 4.5, we see the components of these equations are separate and unique functions of time that do not depend on one another. Motion along the $x$ direction has no part of its motion along the $y$ and $z$ directions, and similarly for the other two coordinate axes. Thus, the motion of an object in two or three dimensions can be divided into separate, independent motions along the perpendicular axes of the coordinate system in which the motion takes place.

To illustrate this concept with respect to displacement, consider a woman walking from point $A$ to point $B$ in a city with square blocks. The woman taking the path from $A$ to $B$ may walk east for so many blocks and then north (two perpendicular directions) for another set of blocks to arrive at $B$. How far she walks east is affected only by her motion eastward. Similarly, how far she walks north is affected only by her motion northward.

## Independence of Motion

In the kinematic description of motion, we are able to treat the horizontal and vertical components of motion separately. In many cases, motion in the horizontal direction does not affect motion in the vertical direction, and vice versa.

An example illustrating the independence of vertical and horizontal motions is given by two baseballs. One baseball is dropped from rest. At the same instant, another is thrown horizontally from the same height and it follows a curved path. A stroboscope captures the positions of the balls at fixed time intervals as they fall (Figure 4.8).

It is remarkable that for each flash of the strobe, the vertical positions of the two balls are the same. This similarity implies vertical motion is independent of whether the ball is moving horizontally. (Assuming no air resistance, the vertical motion of a falling object is influenced by gravity only, not by any horizontal forces.) Careful examination of the ball thrown horizontally shows it travels the same horizontal distance between flashes. This is because there are no additional forces on the ball in the horizontal direction after it is thrown. This result means horizontal velocity is constant and is affected neither by vertical motion nor by gravity (which is vertical). Note this case is true for ideal conditions only. In the real world, air resistance affects the speed of the balls in both directions.

The two-dimensional curved path of the horizontally thrown ball is composed of two independent onedimensional motions (horizontal and vertical). The key to analyzing such motion, called projectile motion, is to resolve it into motions along perpendicular directions. Resolving two-dimensional motion into perpendicular components is possible because the components are independent.

### 4.2 Acceleration Vector

## Instantaneous Acceleration

In addition to obtaining the displacement and velocity vectors of an object in motion, we often want to know its acceleration vector at any point in time along its trajectory. This acceleration vector is the instantaneous
acceleration and it can be obtained from the derivative with respect to time of the velocity function, as we have seen in a previous chapter. The only difference in two or three dimensions is that these are now vector quantities. Taking the derivative with respect to time $\overrightarrow{\mathbf{v}}(t)$, we find

$$
\overrightarrow{\mathbf{a}}(t)=\lim _{t \rightarrow 0} \frac{\overrightarrow{\mathbf{v}}(t+\Delta t)-\overrightarrow{\mathbf{v}}(t)}{\Delta t}=\frac{d \overrightarrow{\mathbf{v}}(t)}{d t}
$$

The acceleration in terms of components is

$$
\overrightarrow{\mathbf{a}}(t)=\frac{d v_{x}(t)}{d t} \hat{\mathbf{i}}+\frac{d v_{y}(t)}{d t} \widehat{\mathbf{j}}+\frac{d v_{z}(t)}{d t} \widehat{\mathbf{k}}
$$

Also, since the velocity is the derivative of the position function, we can write the acceleration in terms of the second derivative of the position function:

$$
\overrightarrow{\mathbf{a}}(t)=\frac{d^{2} x(t)}{d t^{2}} \hat{\mathbf{i}}+\frac{d^{2} y(t)}{d t^{2}} \hat{\mathbf{j}}+\frac{d^{2} z(t)}{d t^{2}} \hat{\mathbf{k}}
$$

## EXAMPLE 4.4

## Finding an Acceleration Vector

A particle has a velocity of $\overrightarrow{\mathbf{v}}(t)=5.0 t \hat{\mathbf{i}}+t^{2} \hat{\mathbf{j}}-2.0 t^{3} \widehat{\mathbf{k}} \mathrm{m} / \mathrm{s}$. (a) What is the acceleration function? (b) What is the acceleration vector at $t=2.0 \mathrm{~s}$ ? Find its magnitude and direction.

## Solution

(a) We take the first derivative with respect to time of the velocity function to find the acceleration. The derivative is taken component by component:

$$
\overrightarrow{\mathbf{a}}(t)=5.0 \hat{\mathbf{i}}+2.0 t \hat{\mathbf{j}}-6.0 t^{2} \widehat{\mathbf{k}} \mathrm{m} / \mathrm{s}^{2}
$$

(b) Evaluating $\overrightarrow{\mathbf{a}}(2.0 \mathrm{~s})=5.0 \hat{\mathbf{i}}+4.0 \hat{\mathbf{j}}-24.0 \widehat{\mathbf{k}} \mathrm{m} / \mathrm{s}^{2}$ gives us the direction in unit vector notation. The magnitude of the acceleration is $|\overrightarrow{\mathbf{a}}(2.0 \mathrm{~s})|=\sqrt{5.0^{2}+4.0^{2}+(-24.0)^{2}}=24.8 \mathrm{~m} / \mathrm{s}^{2}$.

## Significance

In this example we find that acceleration has a time dependence and is changing throughout the motion. Let's consider a different velocity function for the particle.

## EXAMPLE 4.5

## Finding a Particle Acceleration

A particle has a position function $\overrightarrow{\mathbf{r}}(t)=\left(10 t-t^{2}\right) \hat{\mathbf{i}}+5 t \hat{\mathbf{j}}+5 t \hat{\mathbf{k}} \mathrm{m}$. (a) What is the velocity? (b) What is the acceleration? (c) Describe the motion from $t=0 \mathrm{~s}$.

## Strategy

We can gain some insight into the problem by looking at the position function. It is linear in $y$ and $z$, so we know the acceleration in these directions is zero when we take the second derivative. Also, note that the position in the $x$ direction is zero for $t=0 \mathrm{~s}$ and $t=10 \mathrm{~s}$.

## Solution

(a) Taking the derivative with respect to time of the position function, we find

$$
\overrightarrow{\mathbf{v}}(t)=(10-2 t) \hat{\mathbf{i}}+5 \hat{\mathbf{j}}+5 \hat{\mathbf{k}} \mathrm{m} / \mathrm{s}
$$

The velocity function is linear in time in the $x$ direction and is constant in the $y$ and $z$ directions.

(b) Taking the derivative of the velocity function, we find

$$
\overrightarrow{\mathbf{a}}(t)=-2 \hat{\mathbf{i}} \mathrm{m} / \mathrm{s}^{2}
$$

The acceleration vector is a constant in the negative $x$-direction.

(c) The trajectory of the particle can be seen in Figure 4.9. Let's look in the $y$ and $z$ directions first. The particle's position increases steadily as a function of time with a constant velocity in these directions. In the $x$ direction, however, the particle follows a path in positive $x$ until $t=5 \mathrm{~s}$, when it reverses direction. We know this from looking at the velocity function, which becomes zero at this time and negative thereafter. We also know this because the acceleration is negative and constant-meaning, the particle is accelerating in the opposite direction. The particle's position reaches $25 \mathrm{~m}$, where it then reverses direction and begins to accelerate in the negative $x$ direction. The position reaches zero at $t=10 \mathrm{~s}$.

## Significance

By graphing the trajectory of the particle, we can better understand its motion, given by the numerical results of the kinematic equations.

## Constant Acceleration

Multidimensional motion with constant acceleration can be treated the same way as shown in the previous chapter for one-dimensional motion. Earlier we showed that three-dimensional motion is equivalent to three one-dimensional motions, each along an axis perpendicular to the others. To develop the relevant equations in each direction, let's consider the two-dimensional problem of a particle moving in the xy plane with constant acceleration, ignoring the $z$-component for the moment. The acceleration vector is

$$
\overrightarrow{\mathbf{a}}=a_{0 x} \hat{\mathbf{i}}+a_{0 y} \hat{\mathbf{j}}
$$

Each component of the motion has a separate set of equations similar to Equation 3.10-Equation 3.14 of the previous chapter on one-dimensional motion. We show only the equations for position and velocity in the $x$ and $y$-directions. A similar set of kinematic equations could be written for motion in the $z$-direction:

$$
\begin{array}{ll}
x(t)=x_{0}+\left(v_{x}\right)_{\mathrm{avg}} t & 4.11 \\
\quad v_{x}(t)=v_{0 x}+a_{x} t & 4.12 \\
x(t)=x_{0}+v_{0 x} t+\frac{1}{2} a_{x} t^{2} & 4.13 \\
v_{x}^{2}(t)=v_{0 x}^{2}+2 a_{x}\left(x-x_{0}\right) & 4.14 \\
\quad y(t)=y_{0}+\left(v_{y}\right)_{\mathrm{avg}} t & 4.15 \\
\quad v_{y}(t)=v_{0 y}+a_{y} t & 4.16 \\
y(t)=y_{0}+v_{0 y} t+\frac{1}{2} a_{y} t^{2} & 4.17 \\
v_{y}^{2}(t)=v_{0 y}^{2}+2 a_{y}\left(y-y_{0}\right) & 4.18
\end{array}
$$

Here the subscript 0 denotes the initial position or velocity. Equation 4.11 to Equation 4.18 can be substituted into Equation 4.2 and Equation 4.5 without the $z$-component to obtain the position vector and velocity vector as a function of time in two dimensions:

$$
\overrightarrow{\mathbf{r}}(t)=x(t) \hat{\mathbf{i}}+y(t) \hat{\mathbf{j}} \text { and } \overrightarrow{\mathbf{v}}(t)=v_{x}(t) \hat{\mathbf{i}}+v_{y}(t) \hat{\mathbf{j}}
$$

The following example illustrates a practical use of the kinematic equations in two dimensions.

## EXAMPLE 4.6

## A Skier

Figure 4.10 shows a skier moving with an acceleration of $2.1 \mathrm{~m} / \mathrm{s}^{2}$ down a slope of $15^{\circ}$ at $t=0$. With the origin of the coordinate system at the front of the lodge, her initial position and velocity are

$$
\overrightarrow{\mathbf{r}}(0)=(75.0 \hat{\mathbf{i}}-50.0 \widehat{\mathbf{j}}) \mathrm{m}
$$

and

$$
\overrightarrow{\mathbf{v}}(0)=(4.1 \hat{\mathbf{i}}-1.1 \widehat{\mathbf{j}}) \mathrm{m} / \mathrm{s}
$$

(a) What are the $x$ - and $y$-components of the skier's position and velocity as functions of time? (b) What are her position and velocity at $t=10.0 \mathrm{~s}$ ?

## Strategy

Since we are evaluating the components of the motion equations in the $x$ and $y$ directions, we need to find the components of the acceleration and put them into the kinematic equations. The components of the acceleration are found by referring to the coordinate system in Figure 4.10. Then, by inserting the components of the initial position and velocity into the motion equations, we can solve for her position and velocity at a later time $t$.

## Solution

(a) The origin of the coordinate system is at the top of the hill with $y$-axis vertically upward and the $x$-axis horizontal. By looking at the trajectory of the skier, the $x$-component of the acceleration is positive and the $y$-component is negative. Since the angle is $15^{\circ}$ down the slope, we find

$$
\begin{gathered}
a_{x}=\left(2.1 \mathrm{~m} / \mathrm{s}^{2}\right) \cos \left(15^{\circ}\right)=2.0 \mathrm{~m} / \mathrm{s}^{2} \\
a_{y}=\left(-2.1 \mathrm{~m} / \mathrm{s}^{2}\right) \sin 15^{\circ}=-0.54 \mathrm{~m} / \mathrm{s}^{2}
\end{gathered}
$$

Inserting the initial position and velocity into Equation 4.12 and Equation 4.13 for $x$, we have

$$
\begin{gathered}
x(t)=75.0 \mathrm{~m}+(4.1 \mathrm{~m} / \mathrm{s}) t+\frac{1}{2}\left(2.0 \mathrm{~m} / \mathrm{s}^{2}\right) t^{2} \\
v_{x}(t)=4.1 \mathrm{~m} / \mathrm{s}+\left(2.0 \mathrm{~m} / \mathrm{s}^{2}\right) t
\end{gathered}
$$

For $y$, we have

$$
\begin{gathered}
y(t)=-50.0 \mathrm{~m}+(-1.1 \mathrm{~m} / \mathrm{s}) t+\frac{1}{2}\left(-0.54 \mathrm{~m} / \mathrm{s}^{2}\right) t^{2} \\
v_{y}(t)=-1.1 \mathrm{~m} / \mathrm{s}+\left(-0.54 \mathrm{~m} / \mathrm{s}^{2}\right) t
\end{gathered}
$$

(b) Now that we have the equations of motion for $x$ and $y$ as functions of time, we can evaluate them at $t=10.0$ s:

$$
\begin{gathered}
x(10.0 \mathrm{~s})=75.0 \mathrm{~m}+\left(4.1 \mathrm{~m} / \mathrm{s}^{2}\right)(10.0 \mathrm{~s})+\frac{1}{2}\left(2.0 \mathrm{~m} / \mathrm{s}^{2}\right)(10.0 \mathrm{~s})^{2}=216.0 \mathrm{~m} \\
v_{x}(10.0 \mathrm{~s})=4.1 \mathrm{~m} / \mathrm{s}+\left(2.0 \mathrm{~m} / \mathrm{s}^{2}\right)(10.0 \mathrm{~s})=24.1 \mathrm{~m} / \mathrm{s}
\end{gathered}
$$

$$
\begin{gathered}
y(10.0 \mathrm{~s})=-50.0 \mathrm{~m}+(-1.1 \mathrm{~m} / \mathrm{s})(10.0 \mathrm{~s})+\frac{1}{2}\left(-0.54 \mathrm{~m} / \mathrm{s}^{2}\right)(10.0 \mathrm{~s})^{2}=-88.0 \mathrm{~m} \\
v_{y}(10.0 \mathrm{~s})=-1.1 \mathrm{~m} / \mathrm{s}+\left(-0.54 \mathrm{~m} / \mathrm{s}^{2}\right)(10.0 \mathrm{~s})=-6.5 \mathrm{~m} / \mathrm{s}
\end{gathered}
$$

The position and velocity at $t=10.0 \mathrm{~s}$ are, finally,

$$
\begin{aligned}
& \overrightarrow{\mathbf{r}}(10.0 \mathrm{~s})=(216.0 \hat{\mathbf{i}}-88.0 \hat{\mathbf{j}}) \mathrm{m} \\
& \overrightarrow{\mathbf{v}}(10.0 \mathrm{~s})=(24.1 \hat{\mathbf{i}}-6.5 \hat{\mathbf{j}}) \mathrm{m} / \mathrm{s}
\end{aligned}
$$

The magnitude of the velocity of the skier at $10.0 \mathrm{~s}$ is $25 \mathrm{~m} / \mathrm{s}$, which is $60 \mathrm{mi} / \mathrm{h}$.

## Significance

It is useful to know that, given the initial conditions of position, velocity, and acceleration of an object, we can find the position, velocity, and acceleration at any later time.

With Equation 4.8 through Equation 4.10 we have completed the set of expressions for the position, velocity, and acceleration of an object moving in two or three dimensions. If the trajectories of the objects look something like the "Red Arrows" in the opening picture for the chapter, then the expressions for the position, velocity, and acceleration can be quite complicated. In the sections to follow we examine two special cases of motion in two and three dimensions by looking at projectile motion and circular motion.

### 4.3 Projectile Motion

Projectile motion is the motion of an object thrown or projected into the air, subject only to acceleration as a result of gravity. The applications of projectile motion in physics and engineering are numerous. Some examples include meteors as they enter Earth's atmosphere, fireworks, and the motion of any ball in sports. Such objects are called projectiles and their path is called a trajectory. The motion of falling objects as discussed in Motion Along a Straight Line is a simple one-dimensional type of projectile motion in which there is no horizontal movement. In this section, we consider two-dimensional projectile motion, and our treatment neglects the effects of air resistance.

The most important fact to remember here is that motions along perpendicular axes are independent and thus can be analyzed separately. We discussed this fact in Displacement and Velocity Vectors, where we saw that vertical and horizontal motions are independent. The key to analyzing two-dimensional projectile motion is to break it into two motions: one along the horizontal axis and the other along the vertical. (This choice of axes is the most sensible because acceleration resulting from gravity is vertical; thus, there is no acceleration along the horizontal axis when air resistance is negligible.) As is customary, we call the horizontal axis the $x$-axis and the vertical axis the $y$-axis. It is not required that we use this choice of axes; it is simply convenient in the case of gravitational acceleration. In other cases we may choose a different set of axes. Figure 4.11 illustrates the notation for displacement, where we define $\overrightarrow{\mathbf{s}}$ to be the total displacement, and $\overrightarrow{\mathbf{x}}$ and $\overrightarrow{\mathbf{y}}$ are its component vectors along the horizontal and vertical axes, respectively. The magnitudes of these vectors are $s, x$, and $y$.

To describe projectile motion completely, we must include velocity and acceleration, as well as displacement. We must find their components along the $x$ - and $y$-axes. Let's assume all forces except gravity (such as air resistance and friction, for example) are negligible. Defining the positive direction to be upward, the components of acceleration are then very simple:

$$
a_{y}=-g=-9.8 \mathrm{~m} / \mathrm{s}^{2}\left(-32 \mathrm{ft} / \mathrm{s}^{2}\right)
$$

Because gravity is vertical, $a_{x}=0$. If $a_{x}=0$, this means the initial velocity in the $x$ direction is equal to the final velocity in the $x$ direction, or $v_{x}=v_{0 x}$. With these conditions on acceleration and velocity, we can write the kinematic Equation 4.11 through Equation 4.18 for motion in a uniform gravitational field, including the rest of the kinematic equations for a constant acceleration from Motion with Constant Acceleration. The kinematic equations for motion in a uniform gravitational field become kinematic equations with

$a_{y}=-g, a_{x}=0:$

Horizontal Motion

$$
v_{0 x}=v_{x}, x=x_{0}+v_{x} t
$$

Vertical Motion

$$
\begin{gather*}
y=y_{0}+\frac{1}{2}\left(v_{0 y}+v_{y}\right) t \\
v_{y}=v_{0 y}-g t \\
y=y_{0}+v_{0 y} t-\frac{1}{2} g t^{2} \\
v_{y}^{2}=v_{0 y}^{2}-2 g\left(y-y_{0}\right)
\end{gather*}
$$

Using this set of equations, we can analyze projectile motion, keeping in mind some important points.

## PROBLEM-SOLVING STRATEGY

## Projectile Motion

1. Resolve the motion into horizontal and vertical components along the $x$ - and $y$-axes. The magnitudes of the components of displacement $\overrightarrow{\mathbf{s}}$ along these axes are $x$ and $y$. The magnitudes of the components of velocity $\overrightarrow{\mathbf{v}}$ are $v_{x}=v \cos \theta$ and $v_{y}=v \sin \theta$, where $v$ is the magnitude of the velocity and $\theta$ is its direction
relative to the horizontal, as shown in Figure 4.12.
2. Treat the motion as two independent one-dimensional motions: one horizontal and the other vertical. Use the kinematic equations for horizontal and vertical motion presented earlier.
3. Solve for the unknowns in the two separate motions: one horizontal and one vertical. Note that the only common variable between the motions is time $t$. The problem-solving procedures here are the same as those for one-dimensional kinematics and are illustrated in the following solved examples.
4. Recombine quantities in the horizontal and vertical directions to find the total displacement $\overrightarrow{\mathbf{s}}$ and velocity $\overrightarrow{\mathbf{v}}$. Solve for the magnitude and direction of the displacement and velocity using

$$
s=\sqrt{x^{2}+y^{2}}, \quad \Phi=\tan ^{-1}(y / x), v=\sqrt{v_{x}^{2}+v_{y}^{2}}
$$

where $\Phi$ is the direction of the displacement $\overrightarrow{\mathbf{s}}$.

## EXAMPLE 4.7

## A Fireworks Projectile Explodes High and Away

During a fireworks display, a shell is shot into the air with an initial speed of $70.0 \mathrm{~m} / \mathrm{s}$ at an angle of $75.0^{\circ}$ above the horizontal, as illustrated in Figure 4.13. The fuse is timed to ignite the shell just as it reaches its highest
point above the ground. (a) Calculate the height at which the shell explodes. (b) How much time passes between the launch of the shell and the explosion? (c) What is the horizontal displacement of the shell when it explodes? (d) What is the total displacement from the point of launch to the highest point?

## Strategy

The motion can be broken into horizontal and vertical motions in which $a_{x}=0$ and $a_{y}=-g$. We can then define $x_{0}$ and $y_{0}$ to be zero and solve for the desired quantities.

## Solution

(a) By "height" we mean the altitude or vertical position $y$ above the starting point. The highest point in any trajectory, called the apex, is reached when $v_{y}=0$. Since we know the initial and final velocities, as well as the initial position, we use the following equation to find $y$ :

$$
v_{y}^{2}=v_{0 y}^{2}-2 g\left(y-y_{0}\right)
$$

Because $y_{0}$ and $v_{y}$ are both zero, the equation simplifies to

$$
0=v_{0 y}^{2}-2 g y
$$

Solving for $y$ gives

$$
y=\frac{v_{0 y}^{2}}{2 g}
$$

Now we must find $v_{0 y}$, the component of the initial velocity in the $y$ direction. It is given by $v_{0 y}=v_{0} \sin \theta_{0}$, where $v_{0}$ is the initial velocity of $70.0 \mathrm{~m} / \mathrm{s}$ and $\theta_{0}=75^{\circ}$ is the initial angle. Thus,

$$
v_{0 y}=v_{0} \sin \theta=(70.0 \mathrm{~m} / \mathrm{s}) \sin 75^{\circ}=67.6 \mathrm{~m} / \mathrm{s}
$$

and $y$ is

$$
y=\frac{(67.6 \mathrm{~m} / \mathrm{s})^{2}}{2\left(9.80 \mathrm{~m} / \mathrm{s}^{2}\right)}
$$

Thus, we have

$$
y=233 \mathrm{~m}
$$

Note that because up is positive, the initial vertical velocity is positive, as is the maximum height, but the acceleration resulting from gravity is negative. Note also that the maximum height depends only on the vertical component of the initial velocity, so that any projectile with a $67.6-\mathrm{m} / \mathrm{s}$ initial vertical component of
velocity reaches a maximum height of $233 \mathrm{~m}$ (neglecting air resistance). The numbers in this example are reasonable for large fireworks displays, the shells of which do reach such heights before exploding. In practice, air resistance is not completely negligible, so the initial velocity would have to be somewhat larger than that given to reach the same height.

(b) As in many physics problems, there is more than one way to solve for the time the projectile reaches its highest point. In this case, the easiest method is to use $v_{y}=v_{0 y}-g t$. Because $v_{y}=0$ at the apex, this equation reduces to simply

$$
0=v_{0 y}-g t
$$

or

$$
t=\frac{v_{0 y}}{g}=\frac{67.6 \mathrm{~m} / \mathrm{s}}{9.80 \mathrm{~m} / \mathrm{s}^{2}}=6.90 \mathrm{~s}
$$

This time is also reasonable for large fireworks. If you are able to see the launch of fireworks, notice that several seconds pass before the shell explodes. Another way of finding the time is by using $y=y_{0}+\frac{1}{2}\left(v_{0 y}+v_{y}\right) t$. This is left for you as an exercise to complete.

(c) Because air resistance is negligible, $a_{x}=0$ and the horizontal velocity is constant, as discussed earlier. The horizontal displacement is the horizontal velocity multiplied by time as given by $x=x_{0}+v_{x} t$, where $x_{0}$ is equal to zero. Thus,

$$
x=v_{x} t
$$

where $v_{x}$ is the $x$-component of the velocity, which is given by

$$
v_{x}=v_{0} \cos \theta=(70.0 \mathrm{~m} / \mathrm{s}) \cos 75^{\circ}=18.1 \mathrm{~m} / \mathrm{s}
$$

Time $t$ for both motions is the same, so $x$ is

$$
x=(18.1 \mathrm{~m} / \mathrm{s}) 6.90 \mathrm{~s}=125 \mathrm{~m} .
$$

Horizontal motion is a constant velocity in the absence of air resistance. The horizontal displacement found here could be useful in keeping the fireworks fragments from falling on spectators. When the shell explodes, air resistance has a major effect, and many fragments land directly below.

(d) The horizontal and vertical components of the displacement were just calculated, so all that is needed here is to find the magnitude and direction of the displacement at the highest point:

$$
\begin{gathered}
\overrightarrow{\mathbf{s}}=125 \hat{\mathbf{i}}+233 \hat{\mathbf{j}} \\
|\overrightarrow{\mathbf{s}}|=\sqrt{125^{2}+233^{2}}=264 \mathrm{~m} \\
\Phi=\tan ^{-1}\left(\frac{233}{125}\right)=61.8^{\circ}
\end{gathered}
$$

Note that the angle for the displacement vector is less than the initial angle of launch. To see why this is, review Figure 4.11, which shows the curvature of the trajectory toward the ground level.

When solving Example 4.7(a), the expression we found for $y$ is valid for any projectile motion when air resistance is negligible. Call the maximum height $y=h$. Then,

$$
h=\frac{v_{0 y}^{2}}{2 g}
$$

This equation defines the maximum height of a projectile above its launch position and it depends only on the vertical component of the initial velocity.

## EXAMPLE 4.8

## Calculating Projectile Motion: Tennis Player

A tennis player wins a match at Arthur Ashe stadium and hits a ball into the stands at $30 \mathrm{~m} / \mathrm{s}$ and at an angle $45^{\circ}$ above the horizontal (Figure 4.14). On its way down, the ball is caught by a spectator $10 \mathrm{~m}$ above the point where the ball was hit. (a) Calculate the time it takes the tennis ball to reach the spectator. (b) What are the magnitude and direction of the ball's velocity at impact?

## Strategy

Again, resolving this two-dimensional motion into two independent one-dimensional motions allows us to solve for the desired quantities. The time a projectile is in the air is governed by its vertical motion alone. Thus, we solve for $t$ first. While the ball is rising and falling vertically, the horizontal motion continues at a constant velocity. This example asks for the final velocity. Thus, we recombine the vertical and horizontal results to obtain $\vec{v}$ at final time $t$, determined in the first part of the example.

## Solution

(a) While the ball is in the air, it rises and then falls to a final position $10.0 \mathrm{~m}$ higher than its starting altitude.

We can find the time for this by using Equation 4.22:

$$
y=y_{0}+v_{0 y} t-\frac{1}{2} g t^{2}
$$

If we take the initial position $y_{0}$ to be zero, then the final position is $y=10 \mathrm{~m}$. The initial vertical velocity is the vertical component of the initial velocity:

$$
v_{0 y}=v_{0} \sin \theta_{0}=(30.0 \mathrm{~m} / \mathrm{s}) \sin 45^{\circ}=21.2 \mathrm{~m} / \mathrm{s}
$$

Substituting into Equation 4.22 for $y$ gives us

$$
10.0 \mathrm{~m}=(21.2 \mathrm{~m} / \mathrm{s}) t-\left(4.90 \mathrm{~m} / \mathrm{s}^{2}\right) t^{2}
$$

Rearranging terms gives a quadratic equation in $t$ :

$$
\left(4.90 \mathrm{~m} / \mathrm{s}^{2}\right) t^{2}-(21.2 \mathrm{~m} / \mathrm{s}) t+10.0 \mathrm{~m}=0
$$

Use of the quadratic formula yields $t=3.79 \mathrm{~s}$ and $t=0.54 \mathrm{~s}$. Since the ball is at a height of $10 \mathrm{~m}$ at two times during its trajectory-once on the way up and once on the way down-we take the longer solution for the time it takes the ball to reach the spectator:

$$
t=3.79 \mathrm{~s}
$$

The time for projectile motion is determined completely by the vertical motion. Thus, any projectile that has an initial vertical velocity of $21.2 \mathrm{~m} / \mathrm{s}$ and lands $10.0 \mathrm{~m}$ below its starting altitude spends $3.79 \mathrm{~s}$ in the air.

(b) We can find the final horizontal and vertical velocities $v_{x}$ and $v_{y}$ with the use of the result from (a). Then, we can combine them to find the magnitude of the total velocity vector $\overrightarrow{\mathbf{v}}$ and the angle $\theta$ it makes with the horizontal. Since $v_{x}$ is constant, we can solve for it at any horizontal location. We choose the starting point because we know both the initial velocity and the initial angle. Therefore,

$$
v_{x}=v_{0} \cos \theta_{0}=(30 \mathrm{~m} / \mathrm{s}) \cos 45^{\circ}=21.2 \mathrm{~m} / \mathrm{s}
$$

The final vertical velocity is given by Equation 4.21:

$$
v_{y}=v_{0 y}-g t .
$$

Since $v_{0 y}$ was found in part (a) to be $21.2 \mathrm{~m} / \mathrm{s}$, we have

$$
v_{y}=21.2 \mathrm{~m} / \mathrm{s}-9.8 \mathrm{~m} / \mathrm{s}^{2}(3.79 \mathrm{~s})=-15.9 \mathrm{~m} / \mathrm{s}
$$

The magnitude of the final velocity $\overrightarrow{\mathbf{v}}$ is

$$
v=\sqrt{v_{x}^{2}+v_{y}^{2}}=\sqrt{(21.2 \mathrm{~m} / \mathrm{s})^{2}+(-15.9 \mathrm{~m} / \mathrm{s})^{2}}=26.5 \mathrm{~m} / \mathrm{s}
$$

The direction $\theta_{v}$ is found using the inverse tangent:

$$
\theta_{v}=\tan ^{-1}\left(\frac{v_{y}}{v_{x}}\right)=\tan ^{-1}\left(\frac{-15.9}{21.2}\right)=36.9^{\circ} \text { below the horizon. }
$$

## Significance

(a) As mentioned earlier, the time for projectile motion is determined completely by the vertical motion. Thus, any projectile that has an initial vertical velocity of $21.2 \mathrm{~m} / \mathrm{s}$ and lands $10.0 \mathrm{~m}$ above its starting altitude spends $3.79 \mathrm{~s}$ in the air. (b) The negative angle means the velocity is $36.9^{\circ}$ below the horizontal at the point of impact. This result is consistent with the fact that the ball is impacting at a point on the other side of the apex of the trajectory and therefore has a negative $y$ component of the velocity. The magnitude of the velocity is less than the magnitude of the initial velocity we expect since it is impacting $10.0 \mathrm{~m}$ above the launch elevation.

## Time of Flight, Trajectory, and Range

Of interest are the time of flight, trajectory, and range for a projectile launched on a flat horizontal surface and impacting on the same surface. In this case, kinematic equations give useful expressions for these quantities, which are derived in the following sections.

## Time of flight

We can solve for the time of flight of a projectile that is both launched and impacts on a flat horizontal surface by performing some manipulations of the kinematic equations. We note the position and displacement in $y$ must be zero at launch and at impact on an even surface. Thus, we set the displacement in y equal to zero and find

$$
y-y_{0}=v_{0 y} t-\frac{1}{2} g t^{2}=\left(v_{0} \sin \theta_{0}\right) t-\frac{1}{2} g t^{2}=0
$$

Factoring, we have

$$
t\left(v_{0} \sin \theta_{0}-\frac{g t}{2}\right)=0
$$

Solving for $t$ gives us

$$
T_{\text {tof }}=\frac{2\left(v_{0} \sin \theta_{0}\right)}{g}
$$

This is the time of flight for a projectile both launched and impacting on a flat horizontal surface. Equation 4.24 does not apply when the projectile lands at a different elevation than it was launched, as we saw in Example 4.8 of the tennis player hitting the ball into the stands. The other solution, $t=0$, corresponds to the time at launch. The time of flight is linearly proportional to the initial velocity in the $y$ direction and inversely proportional to $g$. Thus, on the Moon, where gravity is one-sixth that of Earth, a projectile launched with the same velocity as on Earth would be airborne six times as long.

## Trajectory

The trajectory of a projectile can be found by eliminating the time variable $t$ from the kinematic equations for arbitrary $t$ and solving for $y(x)$. We take $x_{0}=y_{0}=0$ so the projectile is launched from the origin. The kinematic equation for $x$ gives

$$
x=v_{0 x} t \Rightarrow t=\frac{x}{v_{0 x}}=\frac{x}{v_{0} \cos \theta_{0}}
$$

Substituting the expression for $t$ into the equation for the position $y=\left(v_{0} \sin \theta_{0}\right) t-\frac{1}{2} g t^{2}$ gives

$$
y=\left(v_{0} \sin \theta_{0}\right)\left(\frac{x}{v_{0} \cos \theta_{0}}\right)-\frac{1}{2} g\left(\frac{x}{v_{0} \cos \theta_{0}}\right)^{2}
$$

Rearranging terms, we have

$$
y=\left(\tan \theta_{0}\right) x-\left[\frac{g}{2\left(v_{0} \cos \theta_{0}\right)^{2}}\right] x^{2}
$$

This trajectory equation is of the form $y=a x+b x^{2}$, which is an equation of a parabola with coefficients

$$
a=\tan \theta_{0}, \quad b=-\frac{g}{2\left(v_{0} \cos \theta_{0}\right)^{2}}
$$

## Range

From the trajectory equation we can also find the range, or the horizontal distance traveled by the projectile. Factoring Equation 4.25, we have

$$
y=x\left[\tan \theta_{0}-\frac{g}{2\left(v_{0} \cos \theta_{0}\right)^{2}} x\right]
$$

The position $y$ is zero for both the launch point and the impact point, since we are again considering only a flat horizontal surface. Setting $y=0$ in this equation gives solutions $x=0$, corresponding to the launch point, and

$$
x=\frac{2 v_{0}^{2} \sin \theta_{0} \cos \theta_{0}}{g}
$$

corresponding to the impact point. Using the trigonometric identity $2 \sin \theta \cos \theta=\sin 2 \theta$ and setting $x=R$ for range, we find

$$
R=\frac{v_{0}^{2} \sin 2 \theta_{0}}{g}
$$

Note particularly that Equation 4.26 is valid only for launch and impact on a horizontal surface. We see the range is directly proportional to the square of the initial speed $v_{0}$ and $\sin 2 \theta_{0}$, and it is inversely proportional to the acceleration of gravity. Thus, on the Moon, the range would be six times greater than on Earth for the same initial velocity. Furthermore, we see from the factor $\sin 2 \theta_{0}$ that the range is maximum at $45^{\circ}$. These results are shown in Figure 4.15. In (a) we see that the greater the initial velocity, the greater the range. In (b), we see that
the range is maximum at $45^{\circ}$. This is true only for conditions neglecting air resistance. If air resistance is considered, the maximum angle is somewhat smaller. It is interesting that the same range is found for two initial launch angles that sum to $90^{\circ}$. The projectile launched with the smaller angle has a lower apex than the higher angle, but they both have the same range.

## EXAMPLE 4.9

## Comparing Golf Shots

A golfer finds himself in two different situations on different holes. On the second hole he is $120 \mathrm{~m}$ from the green and wants to hit the ball $90 \mathrm{~m}$ and let it run onto the green. He angles the shot low to the ground at $30^{\circ}$ to the horizontal to let the ball roll after impact. On the fourth hole he is $90 \mathrm{~m}$ from the green and wants to let the ball drop with a minimum amount of rolling after impact. Here, he angles the shot at $70^{\circ}$ to the horizontal to minimize rolling after impact. Both shots are hit and impacted on a level surface.

(a) What is the initial speed of the ball at the second hole?

(b) What is the initial speed of the ball at the fourth hole?

(c) Write the trajectory equation for both cases.

(d) Graph the trajectories.

## Strategy

We see that the range equation has the initial speed and angle, so we can solve for the initial speed for both (a) and (b). When we have the initial speed, we can use this value to write the trajectory equation.

## Solution

(a) $R=\frac{v_{0}^{2} \sin 2 \theta_{0}}{g} \Rightarrow v_{0}=\sqrt{\frac{R g}{\sin 2 \theta_{0}}}=\sqrt{\frac{90.0 \mathrm{~m}\left(9.8 \mathrm{~m} / \mathrm{s}^{2}\right)}{\sin \left(2\left(30^{\circ}\right)\right)}}=31.9 \mathrm{~m} / \mathrm{s}$

(b) $R=\frac{v_{0}^{2} \sin 2 \theta_{0}}{g} \Rightarrow v_{0}=\sqrt{\frac{R g}{\sin 2 \theta_{0}}}=\sqrt{\frac{90.0 \mathrm{~m}\left(9.8 \mathrm{~m} / \mathrm{s}^{2}\right)}{\sin \left(2\left(70^{\circ}\right)\right)}}=37.0 \mathrm{~m} / \mathrm{s}$

(c)

$y=x\left[\tan \theta_{0}-\frac{g}{2\left(v_{0} \cos \theta_{0}\right)^{2}} x\right]$

Second hole: $y=x\left[\tan 30^{\circ}-\frac{9.8 \mathrm{~m} / \mathrm{s}^{2}}{2\left[(31.9 \mathrm{~m} / \mathrm{s})\left(\cos 30^{\circ}\right)\right]^{2}} x\right]=0.58 x-0.0064 x^{2}$

Fourth hole: $y=x\left[\tan 70^{\circ}-\frac{9.8 \mathrm{~m} / \mathrm{s}^{2}}{2\left[(37.0 \mathrm{~m} / \mathrm{s})\left(\cos 70^{\circ}\right)\right]^{2}} x\right]=2.75 x-0.0306 x^{2}$

(d) Using a graphing utility, we can compare the two trajectories, which are shown in Figure 4.16.

## Significance

The initial speed for the shot at $70^{\circ}$ is greater than the initial speed of the shot at $30^{\circ}$. Note from Figure 4.16 that two projectiles launched at the same speed but at different angles have the same range if the launch angles add to $90^{\circ}$. The launch angles in this example add to give a number greater than $90^{\circ}$. Thus, the shot at $70^{\circ}$ has to have a greater launch speed to reach $90 \mathrm{~m}$, otherwise it would land at a shorter distance.

### 4.4 Uniform Circular Motion

Uniform circular motion is a specific type of motion in which an object travels in a circle with a constant speed. For example, any point on a propeller spinning at a constant rate is executing uniform circular motion. Other examples are the second, minute, and hour hands of a watch. It is remarkable that points on these rotating objects are actually accelerating, although the rotation rate is a constant. To see this, we must analyze the
motion in terms of vectors.

## Centripetal Acceleration

In one-dimensional kinematics, objects with a constant speed have zero acceleration. However, in two- and three-dimensional kinematics, even if the speed is a constant, a particle can have acceleration if it moves along a curved trajectory such as a circle. In this case the velocity vector is changing, or $d \overrightarrow{\mathbf{v}} / d t \neq 0$. This is shown in Figure 4.18. As the particle moves counterclockwise in time $\Delta t$ on the circular path, its position vector moves from $\overrightarrow{\mathbf{r}}(t)$ to $\overrightarrow{\mathbf{r}}(t+\Delta t)$. The velocity vector has constant magnitude and is tangent to the path as it changes from $\overrightarrow{\mathbf{v}}(t)$ to $\overrightarrow{\mathbf{v}}(t+\Delta t)$, changing its direction only. Since the velocity vector $\overrightarrow{\mathbf{v}}(t)$ is perpendicular to the position vector $\overrightarrow{\mathbf{r}}(t)$, the triangles formed by the position vectors and $\Delta \overrightarrow{\mathbf{r}}$, and the velocity vectors and $\Delta \overrightarrow{\mathbf{v}}$ are similar. Furthermore, since $|\overrightarrow{\mathbf{r}}(t)|=|\overrightarrow{\mathbf{r}}(t+\Delta t)|$ and $|\overrightarrow{\mathbf{v}}(t)|=|\overrightarrow{\mathbf{v}}(t+\Delta t)|$, the two triangles are isosceles. From these facts we can make the assertion

$\frac{\Delta v}{v}=\frac{\Delta r}{r}$ or $\Delta v=\frac{v}{r} \Delta r$

We can find the magnitude of the acceleration from

$$
a=\lim _{\Delta t \rightarrow 0}\left(\frac{\Delta v}{\Delta t}\right)=\frac{v}{r}\left(\lim _{\Delta t \rightarrow 0} \frac{\Delta r}{\Delta t}\right)=\frac{v^{2}}{r}
$$

The direction of the acceleration can also be found by noting that as $\Delta t$ and therefore $\Delta \theta$ approach zero, the vector $\Delta \overrightarrow{\mathbf{v}}$ approaches a direction perpendicular to $\overrightarrow{\mathbf{v}}$. In the limit $\Delta t \rightarrow 0, \Delta \overrightarrow{\mathbf{v}}$ is perpendicular to $\overrightarrow{\mathbf{v}}$. Since $\overrightarrow{\mathbf{v}}$ is tangent to the circle, the acceleration $d \overrightarrow{\mathbf{v}} / d t$ points toward the center of the circle. Summarizing, a particle moving in a circle at a constant speed has an acceleration with magnitude

$$
a_{\mathrm{c}}=\frac{v^{2}}{r}
$$

The direction of the acceleration vector is toward the center of the circle (Figure 4.19). This is a radial acceleration and is called the centripetal acceleration, which is why we give it the subscript c. The word centripetal comes from the Latin words centrum (meaning "center") and petere (meaning "to seek"), and thus takes the meaning "center seeking."

Let's investigate some examples that illustrate the relative magnitudes of the velocity, radius, and centripetal acceleration.

## EXAMPLE 4.10

## Creating an Acceleration of $1 \mathbf{g}$

A jet is flying at $134.1 \mathrm{~m} / \mathrm{s}$ along a straight line and makes a turn along a circular path level with the ground. What does the radius of the circle have to be to produce a centripetal acceleration of $1 \mathrm{~g}$ on the pilot and jet toward the center of the circular trajectory?

## Strategy

Given the speed of the jet, we can solve for the radius of the circle in the expression for the centripetal acceleration.

## Solution

Set the centripetal acceleration equal to the acceleration of gravity: $9.8 \mathrm{~m} / \mathrm{s}^{2}=v^{2} / r$.

Solving for the radius, we find

$$
r=\frac{(134.1 \mathrm{~m} / \mathrm{s})^{2}}{9.8 \mathrm{~m} / \mathrm{s}^{2}}=1835 \mathrm{~m}=1.835 \mathrm{~km}
$$

## Significance

To create a greater acceleration than $g$ on the pilot, the jet would either have to decrease the radius of its circular trajectory or increase its speed on its existing trajectory or both.

Centripetal acceleration can have a wide range of values, depending on the speed and radius of curvature of the circular path. Typical centripetal accelerations are given in the following table.

| Earth around the Sun | $5.93 \times 10^{-3}$ |
| :--- | :--- |
| Moon around the Earth | $2.73 \times 10^{-3}$ |
| Satellite in geosynchronous orbit | 0.233 |
| Outer edge of a CD when playing | 5.78 |
| Jet in a barrel roll | $(2-3 \mathrm{~g})$ |
| Roller coaster | $(5 \mathrm{~g})$ |
| Electron orbiting a proton in a simple Bohr model of the <br> atom | $9.0 \times 10^{22}$ |

Table 4.1 Typical Centripetal Accelerations

## Equations of Motion for Uniform Circular Motion

A particle executing circular motion can be described by its position vector $\overrightarrow{\mathbf{r}}(t)$. Figure 4.20 shows a particle executing circular motion in a counterclockwise direction. As the particle moves on the circle, its position vector sweeps out the angle $\theta$ with the $x$-axis. Vector $\overrightarrow{\mathbf{r}}(t)$ making an angle $\theta$ with the $x$-axis is shown with its components along the $x$ - and $y$-axes. The magnitude of the position vector is $A=|\overrightarrow{\mathbf{r}}(t)|$ and is also the radius of the circle, so that in terms of its components,

$$
\overrightarrow{\mathbf{r}}(t)=A \cos \omega t \hat{\mathbf{i}}+A \sin \omega t \hat{\mathbf{j}}
$$

Here, $\omega$ is a constant called the angular frequency of the particle. The angular frequency has units of radians (rad) per second and is simply the number of radians of angular measure through which the particle passes per second. The angle $\theta$ that the position vector has at any particular time is $\omega t$.

If $T$ is the period of motion, or the time to complete one revolution ( $2 \pi \mathrm{rad}$ ), then

$$
\omega=\frac{2 \pi}{T} .
$$

Velocity and acceleration can be obtained from the position function by differentiation:

$$
\overrightarrow{\mathbf{v}}(t)=\frac{d \overrightarrow{\mathbf{r}}(t)}{d t}=-A \omega \sin \omega t \hat{\mathbf{i}}+A \omega \cos \omega t \hat{\mathbf{j}}
$$

It can be shown from Figure 4.20 that the velocity vector is tangential to the circle at the location of the particle, with magnitude $A \omega$. Similarly, the acceleration vector is found by differentiating the velocity:

$$
\overrightarrow{\mathbf{a}}(t)=\frac{d \overrightarrow{\mathbf{v}}(t)}{d t}=-A \omega^{2} \cos \omega t \hat{\mathbf{i}}-A \omega^{2} \sin \omega t \hat{\mathbf{j}}
$$

From this equation we see that the acceleration vector has magnitude $A \omega^{2}$ and is directed opposite the position vector, toward the origin, because $\overrightarrow{\mathbf{a}}(t)=-\omega^{2} \overrightarrow{\mathbf{r}}(t)$.

## EXAMPLE 4.11

## Circular Motion of a Proton

A proton has speed $5 \times 10^{6} \mathrm{~m} / \mathrm{s}$ and is moving in a circle in the xy plane of radius $r=0.175 \mathrm{~m}$. What is its position in the xy plane at time $t=2.0 \times 10^{-7} \mathrm{~s}=200 \mathrm{~ns}$ ? At $t=0$, the position of the proton is $0.175 \mathrm{mi}$ and it circles counterclockwise. Sketch the trajectory.

## Solution

From the given data, the proton has period and angular frequency:

$$
\begin{gathered}
T=\frac{2 \pi r}{v}=\frac{2 \pi(0.175 \mathrm{~m})}{5.0 \times 10^{6} \mathrm{~m} / \mathrm{s}}=2.20 \times 10^{-7} \mathrm{~s} \\
\omega=\frac{2 \pi}{T}=\frac{2 \pi}{2.20 \times 10^{-7} \mathrm{~s}}=2.856 \times 10^{7} \mathrm{rad} / \mathrm{s}
\end{gathered}
$$

The position of the particle at $t=2.0 \times 10^{-7} \mathrm{~s}$ with $A=0.175 \mathrm{~m}$ is

$$
\begin{aligned}
\overrightarrow{\mathbf{r}}\left(2.0 \times 10^{-7} \mathrm{~s}\right)= & A \cos \omega\left(2.0 \times 10^{-7} \mathrm{~s}\right) \hat{\mathbf{i}}+A \sin \omega\left(2.0 \times 10^{-7} \mathrm{~s}\right) \hat{\mathbf{j}} \mathrm{m} \\
= & 0.175 \cos \left[\left(2.856 \times 10^{7} \mathrm{rad} / \mathrm{s}\right)\left(2.0 \times 10^{-7} \mathrm{~s}\right)\right] \hat{\mathbf{i}} \\
& +0.175 \sin \left[\left(2.856 \times 10^{7} \mathrm{rad} / \mathrm{s}\right)\left(2.0 \times 10^{-7} \mathrm{~s}\right)\right] \hat{\mathbf{j}} \mathrm{m} \\
= & 0.175 \cos (5.712 \mathrm{rad}) \hat{\mathbf{i}}+0.175 \sin (5.712 \mathrm{rad}) \hat{\mathbf{j}}=0.147 \hat{\mathbf{i}}-0.095 \widehat{\mathbf{j}} \mathrm{m}
\end{aligned}
$$

From this result we see that the proton is located slightly below the $x$-axis. This is shown in Figure 4.21.

## Significance

We picked the initial position of the particle to be on the $x$-axis. This was completely arbitrary. If a different starting position were given, we would have a different final position at $t=200 \mathrm{~ns}$.

## Nonuniform Circular Motion

Circular motion does not have to be at a constant speed. A particle can travel in a circle and speed up or slow down, showing an acceleration in the direction of the motion.

In uniform circular motion, the particle executing circular motion has a constant speed and the circle is at a fixed radius. If the speed of the particle is changing as well, then we introduce an additional acceleration in the direction tangential to the circle. Such accelerations occur at a point on a top that is changing its spin rate, or any accelerating rotor. In Displacement and Velocity Vectors we showed that centripetal acceleration is the time rate of change of the direction of the velocity vector. If the speed of the particle is changing, then it has a tangential acceleration that is the time rate of change of the magnitude of the velocity:

$$
a_{\mathrm{T}}=\frac{d|\overrightarrow{\mathbf{v}}|}{d t}
$$

The direction of tangential acceleration is tangent to the circle whereas the direction of centripetal acceleration is radially inward toward the center of the circle. Thus, a particle in circular motion with a tangential acceleration has a total acceleration that is the vector sum of the centripetal and tangential accelerations:

$$
\overrightarrow{\mathbf{a}}=\overrightarrow{\mathbf{a}}_{\mathrm{c}}+\overrightarrow{\mathbf{a}}_{\mathrm{T}}
$$

The acceleration vectors are shown in Figure 4.22. Note that the two acceleration vectors $\overrightarrow{\mathbf{a}}_{\mathrm{c}}$ and $\overrightarrow{\mathbf{a}}_{\mathrm{T}}$ are perpendicular to each other, with $\overrightarrow{\mathbf{a}}_{\mathrm{c}}$ in the radial direction and $\overrightarrow{\mathbf{a}}_{\mathrm{T}}$ in the tangential direction. The total acceleration $\overrightarrow{\mathbf{a}}$ points at an angle between $\overrightarrow{\mathbf{a}}_{\mathrm{c}}$ and $\overrightarrow{\mathbf{a}}_{\mathrm{T}}$.

## EXAMPLE 4.12

## Total Acceleration during Circular Motion

A particle moves in a circle of radius $r=2.0 \mathrm{~m}$. During the time interval from $t=1.5 \mathrm{~s}$ to $t=4.0 \mathrm{~s}$ its speed varies with time according to

$$
v(t)=c_{1}-\frac{c_{2}}{t^{2}}, c_{1}=4.0 \mathrm{~m} / \mathrm{s}, c_{2}=6.0 \mathrm{~m} \cdot \mathrm{s}
$$

What is the total acceleration of the particle at $t=2.0 \mathrm{~s}$ ?

## Strategy

We are given the speed of the particle and the radius of the circle, so we can calculate centripetal acceleration easily. The direction of the centripetal acceleration is toward the center of the circle. We find the magnitude of the tangential acceleration by taking the derivative with respect to time of $|v(t)|$ using Equation 4.31 and evaluating it at $t=2.0 \mathrm{~s}$. We use this and the magnitude of the centripetal acceleration to find the total acceleration.

## Solution

Centripetal acceleration is

$$
\begin{gathered}
v(2.0 \mathrm{~s})=\left(4.0-\frac{6.0}{(2.0)^{2}}\right) \mathrm{m} / \mathrm{s}=2.5 \mathrm{~m} / \mathrm{s} \\
a_{\mathrm{c}}=\frac{v^{2}}{r}=\frac{(2.5 \mathrm{~m} / \mathrm{s})^{2}}{2.0 \mathrm{~m}}=3.1 \mathrm{~m} / \mathrm{s}^{2}
\end{gathered}
$$

directed toward the center of the circle. Tangential acceleration is

$$
a_{\mathrm{T}}=\left|\frac{d \overrightarrow{\mathbf{v}}}{d t}\right|=\frac{2 c_{2}}{t^{3}}=\frac{12.0}{(2.0)^{3}} \mathrm{~m} / \mathrm{s}^{2}=1.5 \mathrm{~m} / \mathrm{s}^{2}
$$

Total acceleration is

$$
|\overrightarrow{\mathbf{a}}|=\sqrt{3.1^{2}+1.5^{2}} \mathrm{~m} / \mathrm{s}^{2}=3.44 \mathrm{~m} / \mathrm{s}^{2}
$$

and $\theta=\tan ^{-1} \frac{3.1}{1.5}=64^{\circ}$ from the tangent to the circle. See Figure 4.23.

## Significance

The directions of centripetal and tangential accelerations can be described more conveniently in terms of a polar coordinate system, with unit vectors in the radial and tangential directions. This coordinate system, which is used for motion along curved paths, is discussed in detail later in the book.

### 4.5 Relative Motion in One and Two Dimensions

Motion does not happen in isolation. If you're riding in a train moving at $10 \mathrm{~m} / \mathrm{s}$ east, this velocity is measured relative to the ground on which you're traveling. However, if another train passes you at $15 \mathrm{~m} / \mathrm{s}$ east, your velocity relative to this other train is different from your velocity relative to the ground. Your velocity relative to the other train is $5 \mathrm{~m} / \mathrm{s}$ west. To explore this idea further, we first need to establish some terminology.

## Reference Frames

To discuss relative motion in one or more dimensions, we first introduce the concept of reference frames. When we say an object has a certain velocity, we must state it has a velocity with respect to a given reference frame. In most examples we have examined so far, this reference frame has been Earth. If you say a person is sitting in a train moving at $10 \mathrm{~m} / \mathrm{s}$ east, then you imply the person on the train is moving relative to the surface of Earth at this velocity, and Earth is the reference frame. We can expand our view of the motion of the person on the train and say Earth is spinning in its orbit around the Sun, in which case the motion becomes more complicated. In this case, the solar system is the reference frame. In summary, all discussion of relative motion must define the reference frames involved. We now develop a method to refer to reference frames in relative motion.

## Relative Motion in One Dimension

We introduce relative motion in one dimension first, because the velocity vectors simplify to having only two possible directions. Take the example of the person sitting in a train moving east. If we choose east as the positive direction and Earth as the reference frame, then we can write the velocity of the train with respect to the Earth as $\overrightarrow{\mathbf{v}}_{\mathrm{TE}}=10 \mathrm{~m} / \mathrm{s} \hat{\mathbf{i}}$ east, where the subscripts TE refer to train and Earth. Let's now say the person gets up out of her seat and walks toward the back of the train at $2 \mathrm{~m} / \mathrm{s}$. This tells us she has a velocity relative to the reference frame of the train. Since the person is walking west, in the negative direction, we write her velocity with respect to the train as $\overrightarrow{\mathbf{v}}_{\mathrm{PT}}=-2 \mathrm{~m} / \mathrm{s} \hat{\mathbf{i}}$. We can add the two velocity vectors to find the velocity of
the person with respect to Earth. This relative velocity is written as

$$
\overrightarrow{\mathbf{v}}_{\mathrm{PE}}=\overrightarrow{\mathbf{v}}_{\mathrm{PT}}+\overrightarrow{\mathbf{v}}_{\mathrm{TE}}
$$

Note the ordering of the subscripts for the various reference frames in Equation 4.33. The subscripts for the coupling reference frame, which is the train, appear consecutively in the right-hand side of the equation. Figure 4.24 shows the correct order of subscripts when forming the vector equation.

$$
\overrightarrow{\mathbf{v}}_{\mathrm{PE}}=\overrightarrow{\mathbf{v}}_{\mathrm{PT}}^{+}+\overrightarrow{\mathbf{v}}_{\mathrm{TE}}
$$

Figure 4.24 When constructing the vector equation, the subscripts for the coupling reference frame appear consecutively on the inside. The subscripts on the left-hand side of the equation are the same as the two outside subscripts on the right-hand side of the equation.

Adding the vectors, we find $\overrightarrow{\mathbf{v}}_{\mathrm{PE}}=8 \mathrm{~m} / \mathrm{s} \hat{\mathbf{i}}$, so the person is moving $8 \mathrm{~m} / \mathrm{s}$ east with respect to Earth. Graphically, this is shown in Figure 4.25.

## Relative Velocity in Two Dimensions

We can now apply these concepts to describing motion in two dimensions. Consider a particle $P$ and reference frames $S$ and $S^{\prime}$, as shown in Figure 4.26. The position of the origin of $S^{\prime}$ as measured in $S$ is $\overrightarrow{\mathbf{r}}_{S^{\prime}} S_{\text {t }}$, the position of $P$ as measured in $S^{\prime}$ is $\overrightarrow{\mathbf{r}}_{P S^{\prime}}$, and the position of $P$ as measured in $S$ is $\overrightarrow{\mathbf{r}}_{P S}$.

From Figure 4.26 we see that

$$
\overrightarrow{\mathbf{r}}_{P S}=\overrightarrow{\mathbf{r}}_{P S^{\prime}}+\overrightarrow{\mathbf{r}}_{S^{\prime} S}
$$

The relative velocities are the time derivatives of the position vectors. Therefore,

$$
\overrightarrow{\mathbf{v}}_{P S}=\overrightarrow{\mathbf{v}}_{P S^{\prime}}+\overrightarrow{\mathbf{v}}_{S^{\prime} S}
$$

The velocity of a particle relative to $S$ is equal to its velocity relative to $S^{\prime}$ plus the velocity of $S^{\prime}$ relative to $S$. We can extend Equation 4.35 to any number of reference frames. For particle $P$ with velocities
$\overrightarrow{\mathbf{v}}_{P A}, \overrightarrow{\mathbf{v}}_{P B}$, and $\overrightarrow{\mathbf{v}}_{P C}$ in frames $A, B$, and $C$,

$$
\overrightarrow{\mathbf{v}}_{P C}=\overrightarrow{\mathbf{v}}_{P A}+\overrightarrow{\mathbf{v}}_{A B}+\overrightarrow{\mathbf{v}}_{B C}
$$

We can also see how the accelerations are related as observed in two reference frames by differentiating Equation 4.35:

$$
\overrightarrow{\mathbf{a}}_{P S}=\overrightarrow{\mathbf{a}}_{P S^{\prime}}+\overrightarrow{\mathbf{a}}_{S^{\prime} S}
$$

We see that if the velocity of $S^{\prime}$ relative to $S$ is a constant, then $\overrightarrow{\mathbf{a}}_{S^{\prime} S}=0$ and

$$
\overrightarrow{\mathbf{a}}_{P S}=\overrightarrow{\mathbf{a}}_{P S^{\prime}}
$$

This says the acceleration of a particle is the same as measured by two observers moving at a constant velocity relative to each other.

## EXAMPLE 4.13

## Motion of a Car Relative to a Truck

A truck is traveling south at a speed of $70 \mathrm{~km} / \mathrm{h}$ toward an intersection. A car is traveling east toward the intersection at a speed of $80 \mathrm{~km} / \mathrm{h}$ (Figure 4.27). What is the velocity of the car relative to the truck?

## Strategy

First, we must establish the reference frame common to both vehicles, which is Earth. Then, we write the velocities of each with respect to the reference frame of Earth, which enables us to form a vector equation that links the car, the truck, and Earth to solve for the velocity of the car with respect to the truck.

## Solution

The velocity of the car with respect to Earth is $\overrightarrow{\mathbf{v}}_{\mathrm{CE}}=80 \mathrm{~km} / \mathrm{h} \hat{\mathbf{i}}$. The velocity of the truck with respect to Earth is $\overrightarrow{\mathbf{v}}_{\mathrm{TE}}=-70 \mathrm{~km} / \mathrm{h} \hat{\mathbf{j}}$. Using the velocity addition rule, the relative motion equation we are seeking is

$$
\overrightarrow{\mathbf{v}}_{\mathrm{CT}}=\overrightarrow{\mathbf{v}}_{\mathrm{CE}}+\overrightarrow{\mathbf{v}}_{\mathrm{ET}}
$$

Here, $\overrightarrow{\mathbf{v}}_{\mathrm{CT}}$ is the velocity of the car with respect to the truck, and Earth is the connecting reference frame. Since we have the velocity of the truck with respect to Earth, the negative of this vector is the velocity of Earth with respect to the truck: $\overrightarrow{\mathbf{v}}_{\mathrm{ET}}=-\overrightarrow{\mathbf{v}}_{\mathrm{TE}}$. The vector diagram of this equation is shown in Figure 4.28.

We can now solve for the velocity of the car with respect to the truck:

$$
\left|\overrightarrow{\mathbf{v}}_{\mathrm{CT}}\right|=\sqrt{(80.0 \mathrm{~km} / \mathrm{h})^{2}+(70.0 \mathrm{~km} / \mathrm{h})^{2}}=106 . \mathrm{km} / \mathrm{h}
$$

and

$$
\theta=\tan ^{-1}\left(\frac{70.0}{80.0}\right)=41.2^{\circ} \text { north of east. }
$$

## Significance

Drawing a vector diagram showing the velocity vectors can help in understanding the relative velocity of the two objects.

## EXAMPLE 4.14

## Flying a Plane in a Wind

A pilot must fly his plane due north to reach his destination. The plane can fly at $300 \mathrm{~km} / \mathrm{h}$ in still air. A wind is blowing out of the northeast at $90 \mathrm{~km} / \mathrm{h}$. (a) What is the speed of the plane relative to the ground? (b) In what direction must the pilot head her plane to fly due north?

## Strategy

The pilot must point her plane somewhat east of north to compensate for the wind velocity. We need to construct a vector equation that contains the velocity of the plane with respect to the ground, the velocity of the plane with respect to the air, and the velocity of the air with respect to the ground. Since these last two quantities are known, we can solve for the velocity of the plane with respect to the ground. We can graph the vectors and use this diagram to evaluate the magnitude of the plane's velocity with respect to the ground. The diagram will also tell us the angle the plane's velocity makes with north with respect to the air, which is the direction the pilot must head her plane.

## Solution

The vector equation is $\overrightarrow{\mathbf{v}}_{\mathrm{PG}}=\overrightarrow{\mathbf{v}}_{\mathrm{PA}}+\overrightarrow{\mathbf{v}}_{\mathrm{AG}}$, where $\mathrm{P}=$ plane, $\mathrm{A}=$ air, and $\mathrm{G}=$ ground. From the geometry in Figure 4.29, we can solve easily for the magnitude of the velocity of the plane with respect to the ground and the angle of the plane's heading, $\theta$.

(a) Known quantities:

$$
\begin{aligned}
& \left|\vec{v}_{\mathrm{PA}}\right|=300 \mathrm{~km} / \mathrm{h} \\
& \left|\overrightarrow{\mathbf{v}}_{\mathrm{AG}}\right|=90 \mathrm{~km} / \mathrm{h}
\end{aligned}
$$

Substituting into the equation of motion, we obtain $\left|\overrightarrow{\mathbf{v}}_{\mathrm{PG}}\right|=230 \mathrm{~km} / \mathrm{h}$.

(b) The angle $\theta=\tan ^{-1} \frac{63.64}{300}=12^{\circ}$ east of north.

