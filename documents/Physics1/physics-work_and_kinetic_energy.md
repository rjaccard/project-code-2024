# CHAPTER 7 <br> Work and Kinetic Energy 

INTRODUCTION In this chapter, we discuss some basic physical concepts involved in every physical motion in the universe, going beyond the concepts of force and change in motion, which we discussed in Motion in Two and Three Dimensions and Newton's Laws of Motion. These concepts are work, kinetic energy, and power. We explain how these quantities are related to one another, which will lead us to a fundamental relationship called the work-energy theorem. In the next chapter, we generalize this idea to the broader principle of conservation of energy.

The application of Newton's laws usually requires solving differential equations that relate the forces acting on an object to the accelerations they produce. Often, an analytic solution is intractable or impossible, requiring lengthy numerical solutions or simulations to get approximate results. In such situations, more general relations, like the work-energy theorem (or the conservation of energy), can still provide useful answers to
many questions and require a more modest amount of mathematical calculation. In particular, you will see how the work-energy theorem is useful in relating the speeds of a particle, at different points along its trajectory, to the forces acting on it, even when the trajectory is otherwise too complicated to deal with. Thus, some aspects of motion can be addressed with fewer equations and without vector decompositions.

### 7.1 Work

In physics, work is done on an object when energy is transferred to the object. In other words, work is done when a force acts on something that undergoes a displacement from one position to another. Forces can vary as a function of position, and displacements can be along various paths between two points. We first define the increment of work $d W$ done by a force $\overrightarrow{\mathbf{F}}$ acting through an infinitesimal displacement $d \overrightarrow{\mathbf{r}}$ as the dot product of these two vectors:

$$
d W=\overrightarrow{\mathbf{F}} \cdot d \overrightarrow{\mathbf{r}}=|\overrightarrow{\mathbf{F}}||d \overrightarrow{\mathbf{r}}| \cos \theta
$$

Then, we can add up the contributions for infinitesimal displacements, along a path between two positions, to get the total work.

## Work Done by a Force

The work done by a force is the integral of the force with respect to displacement along the path of the displacement:

$$
W_{A B}=\int_{\text {path } A B} \overrightarrow{\mathbf{F}} \cdot d \overrightarrow{\mathbf{r}}
$$

The vectors involved in the definition of the work done by a force acting on a particle are illustrated in Figure 7.2 .

We choose to express the dot product in terms of the magnitudes of the vectors and the cosine of the angle between them, because the meaning of the dot product for work can be put into words more directly in terms of magnitudes and angles. We could equally well have expressed the dot product in terms of the various components introduced in Vectors. In two dimensions, these were the $x$ - and $y$-components in Cartesian coordinates, or the $r$ - and $\varphi$-components in polar coordinates; in three dimensions, it was just $x^{-}, y^{-}$- and $z$-components. Which choice is more convenient depends on the situation. In words, you can express Equation 7.1 for the work done by a force acting over a displacement as a product of one component acting parallel to the other component. From the properties of vectors, it doesn't matter if you take the component of the force parallel to the displacement or the component of the displacement parallel to the force-you get the same
result either way.

Recall that the magnitude of a force times the cosine of the angle the force makes with a given direction is the component of the force in the given direction. The components of a vector can be positive, negative, or zero, depending on whether the angle between the vector and the component-direction is between $0^{\circ}$ and $90^{\circ}$ or $90^{\circ}$ and $180^{\circ}$, or is equal to $90^{\circ}$. As a result, the work done by a force can be positive, negative, or zero, depending on whether the force is generally in the direction of the displacement, generally opposite to the displacement, or perpendicular to the displacement. The maximum work is done by a given force when it is along the direction of the displacement $(\cos \theta= \pm 1)$, and zero work is done when the force is perpendicular to the displacement $(\cos \theta=0)$.

The units of work are units of force multiplied by units of length, which in the SI system is newtons times meters, $\mathrm{N} \cdot \mathrm{m}$. This combination is called a joule, for historical reasons that we will mention later, and is abbreviated as J. In the English system, still used in the United States, the unit of force is the pound (lb) and the unit of distance is the foot ( $\mathrm{ft}$ ), so the unit of work is the foot-pound ( $\mathrm{ft} \cdot \mathrm{lb}$ ).

## Work Done by Constant Forces and Contact Forces

The simplest work to evaluate is that done by a force that is constant in magnitude and direction. In this case, we can factor out the force; the remaining integral is just the total displacement, which only depends on the end points $A$ and $B$, but not on the path between them:

$$
W_{A B}=\overrightarrow{\mathbf{F}} \cdot \int_{A}^{B} d \overrightarrow{\mathbf{r}}=\overrightarrow{\mathbf{F}} \cdot\left(\overrightarrow{\mathbf{r}}_{B}-\overrightarrow{\mathbf{r}}_{A}\right)=|\overrightarrow{\mathbf{F}}|\left|\overrightarrow{\mathbf{r}}_{B}-\overrightarrow{\mathbf{r}}_{A}\right| \cos \theta \text { (constant force) }
$$

We can also see this by writing out Equation 7.2 in Cartesian coordinates and using the fact that the components of the force are constant:

$$
\begin{aligned}
W_{A B} & =\int_{\text {path } A B} \overrightarrow{\mathbf{F}} \cdot d \overrightarrow{\mathbf{r}}=\int_{\text {path } A B}\left(F_{x} d x+F_{y} d y+F_{z} d z\right)=F_{x} \int_{A}^{B} d x+F_{y} \int_{A}^{B} d y+F_{z} \int_{A}^{B} d z \\
& =F_{x}\left(x_{B}-x_{A}\right)+F_{y}\left(y_{B}-y_{A}\right)+F_{z}\left(z_{B}-z_{A}\right)=\overrightarrow{\mathbf{F}} \cdot\left(\overrightarrow{\mathbf{r}}_{B}-\overrightarrow{\mathbf{r}}_{A}\right)
\end{aligned}
$$

Figure 7.3(a) shows a person exerting a constant force $\overrightarrow{\mathbf{F}}$ along the handle of a lawn mower, which makes an angle $\theta$ with the horizontal. The horizontal displacement of the lawn mower, over which the force acts, is $\mathbf{\mathbf { d }}$. The work done on the lawn mower is $W=\overrightarrow{\mathbf{F}} \cdot \overrightarrow{\mathbf{d}}=F d \cos \theta$, which the figure also illustrates as the horizontal component of the force times the magnitude of the displacement.

Figure 7.3(b) shows a person holding a briefcase. The person must exert an upward force, equal in magnitude to the weight of the briefcase, but this force does no work, because the displacement over which it acts is zero.

In Figure 7.3(c), where the person in (b) is walking horizontally with constant speed, the work done by the person on the briefcase is still zero, but now because the angle between the force exerted and the displacement is $90^{\circ}(\overrightarrow{\mathbf{F}}$ perpendicular to $\overrightarrow{\mathbf{d}})$ and $\cos 90^{\circ}=0$.

EXAMPLE 7.1

## Calculating the Work You Do to Push a Lawn Mower

How much work is done on the lawn mower by the person in Figure 7.3 (a) if he exerts a constant force of 75.0 $\mathrm{N}$ at an angle $35^{\circ}$ below the horizontal and pushes the mower $25.0 \mathrm{~m}$ on level ground?

## Strategy

We can solve this problem by substituting the given values into the definition of work done on an object by a constant force, stated in the equation $W=F d \cos \theta$. The force, angle, and displacement are given, so that only the work $W$ is unknown.

## Solution

The equation for the work is

$$
W=F d \cos \theta
$$

Substituting the known values gives

$$
W=(75.0 \mathrm{~N})(25.0 \mathrm{~m}) \cos \left(35.0^{\circ}\right)=1.54 \times 10^{3} \mathrm{~J}
$$

## Significance

Even though one and a half kilojoules may seem like a lot of work, we will see in Potential Energy and Conservation of Energy that it's only about as much work as you could do by burning one sixth of a gram of fat.

When you mow the grass, other forces act on the lawn mower besides the force you exert-namely, the contact force of the ground and the gravitational force of Earth. Let's consider the work done by these forces in general. For an object moving on a surface, the displacement $d \overrightarrow{\mathbf{r}}$ is tangent to the surface. The part of the contact force on the object that is perpendicular to the surface is the normal force $\mathbf{\mathbf { N }}$. Since the cosine of the angle between the normal and the tangent to a surface is zero, we have

$$
d W_{\mathrm{N}}=\overrightarrow{\mathbf{N}} \cdot d \overrightarrow{\mathbf{r}}=\overrightarrow{\mathbf{0}}
$$

The normal force never does work under these circumstances. (Note that if the displacement $d \overrightarrow{\mathbf{r}}$ did have a relative component perpendicular to the surface, the object would either leave the surface or break through it, and there would no longer be any normal contact force. However, if the object is more than a particle, and has an internal structure, the normal contact force can do work on it, for example, by displacing it or deforming its shape. This will be mentioned in the next chapter.)

The part of the contact force on the object that is parallel to the surface is friction, $\overrightarrow{\mathbf{f}}$. For this object sliding along the surface, kinetic friction $\overrightarrow{\mathbf{f}}_{\mathrm{k}}$ is opposite to $d \overrightarrow{\mathbf{r}}$, relative to the surface, so the work done by kinetic friction is negative. If the magnitude of $\overrightarrow{\mathbf{f}}_{\mathrm{k}}$ is constant (as it would be if all the other forces on the object were constant), then the work done by friction is

$$
W_{\mathrm{fr}}=\int_{A}^{B} \overrightarrow{\mathbf{f}}_{k} \cdot d \overrightarrow{\mathbf{r}}=-f_{k} \int_{A}^{B}|d r|=-f_{k}\left|l_{A B}\right|
$$

where $\left|l_{A B}\right|$ is the path length on the surface. The force of static friction does no work in the reference frame between two surfaces because there is never displacement between the surfaces. As an external force, static friction can do work. Static friction can keep someone from sliding off a sled when the sled is moving and perform positive work on the person. If you're driving your car at the speed limit on a straight, level stretch of highway, the negative work done by air resistance is balanced by the positive work done by the static friction of the road on the drive wheels. You can pull the rug out from under an object in such a way that it slides backward relative to the rug, but forward relative to the floor. In this case, kinetic friction exerted by the rug on the object could be in the same direction as the displacement of the object, relative to the floor, and do positive work. The bottom line is that you need to analyze each particular case to determine the work done by the forces, whether positive, negative or zero.

## EXAMPLE 7.2

## Moving a Couch

You decide to move your couch to a new position on your horizontal living room floor. The normal force on the couch is $1 \mathrm{kN}$ and the coefficient of friction is 0.6 . (a) You first push the couch $3 \mathrm{~m}$ parallel to a wall and then 1 $\mathrm{m}$ perpendicular to the wall ( $A$ to $B$ in Figure 7.4). How much work is done by the frictional force? (b) You don't like the new position, so you move the couch straight back to its original position ( $B$ to $A$ in Figure 7.4). What was the total work done against friction moving the couch away from its original position and back again?

## Strategy

The magnitude of the force of kinetic friction on the couch is constant, equal to the coefficient of friction times the normal force, $f_{K}=\mu_{K} N$. Therefore, the work done by it is $W_{\mathrm{fr}}=-f_{K} d$, where $d$ is the path length traversed. The segments of the paths are the sides of a right triangle, so the path lengths are easily calculated. In part (b), you can use the fact that the work done against a force is the negative of the work done by the force.

## Solution

a. The work done by friction $\mathrm{i}$

$$
W=-(0.6)(1 \mathrm{kN})(3 \mathrm{~m}+1 \mathrm{~m})=-2.4 \mathrm{~kJ}
$$

b. The length of the path along the hypotenuse is $\sqrt{10} \mathrm{~m}$, so the total work done against friction is

$$
W=(0.6)(1 \mathrm{kN})(3 \mathrm{~m}+1 \mathrm{~m}+\sqrt{10} \mathrm{~m})=4.3 \mathrm{~kJ}
$$

## Significance

The total path over which the work of friction was evaluated began and ended at the same point (it was a closed path), so that the total displacement of the couch was zero. However, the total work was not zero. The reason is that forces like friction are classified as nonconservative forces, or dissipative forces, as we discuss in the next chapter.

## EXAMPLE 7.3

## Shelving a Book

You lift an oversized library book, weighing $20 \mathrm{~N}, 1 \mathrm{~m}$ vertically down from a shelf, and carry it $3 \mathrm{~m}$ horizontally to a table (Figure 7.5). How much work does gravity do on the book? (b) When you're finished, you
move the book in a straight line back to its original place on the shelf. What was the total work done against gravity, moving the book away from its original position on the shelf and back again?

## Strategy

We have just seen that the work done by a constant force of gravity depends only on the weight of the object moved and the difference in height for the path taken, $W_{A B}=-m g\left(y_{B}-y_{A}\right)$. We can evaluate the difference in height to answer (a) and (b).

## Solution

a. Since the book starts on the shelf and is lifted down $y_{B}-y_{A}=-1 \mathrm{~m}$, we have

$$
W=-(20 \mathrm{~N})(-1 \mathrm{~m})=20 \mathrm{~J}
$$

b. There is zero difference in height for any path that begins and ends at the same place on the shelf, so $W=0$.

## Significance

Gravity does positive work $(20 \mathrm{~J})$ when the book moves down from the shelf. The gravitational force between two objects is an attractive force, which does positive work when the objects get closer together. Gravity does zero work $(0 \mathrm{~J})$ when the book moves horizontally from the shelf to the table and negative work $(-20 \mathrm{~J})$ when the book moves from the table back to the shelf. The total work done by gravity is zero $[20 \mathrm{~J}+0 \mathrm{~J}+(-20 \mathrm{~J})=0]$. Unlike friction or other dissipative forces, described in Example 7.2, the total work done against gravity, over any closed path, is zero. Positive work is done against gravity on the upward parts of a closed path, but an equal amount of negative work is done against gravity on the downward parts. In other words, work done against gravity, lifting an object up, is "given back" when the object comes back down. Forces like gravity (those that do zero work over any closed path) are classified as conservative forces and play an important role in physics.

## Work Done by Forces that Vary

In general, forces may vary in magnitude and direction at points in space, and paths between two points may be curved. The infinitesimal work done by a variable force can be expressed in terms of the components of the force and the displacement along the path,

$$
d W=F_{x} d x+F_{y} d y+F_{z} d z
$$

Here, the components of the force are functions of position along the path, and the displacements depend on the equations of the path. (Although we chose to illustrate $d W$ in Cartesian coordinates, other coordinates are better suited to some situations.) Equation 7.2 defines the total work as a line integral, or the limit of a sum of infinitesimal amounts of work. The physical concept of work is straightforward: you calculate the work for tiny
displacements and add them up. Sometimes the mathematics can seem complicated, but the following example demonstrates how cleanly they can operate.

## EXAMPLE 7.4

## Work Done by a Variable Force over a Curved Path

An object moves along a parabolic path $y=\left(0.5 \mathrm{~m}^{-1}\right) x^{2}$ from the origin $A=(0,0)$ to the point $B=(2 \mathrm{~m}, 2 \mathrm{~m})$ under the action of a force $\overrightarrow{\mathbf{F}}=(5 \mathrm{~N} / \mathrm{m}) y \hat{\mathbf{i}}+(10 \mathrm{~N} / \mathrm{m}) x \hat{\mathbf{j}}$ (Figure 7.6). Calculate the work done.

## Strategy

The components of the force are given functions of $x$ and $y$. We can use the equation of the path to express $y$ and $d y$ in terms of $x$ and $d x$; namely,

$$
y=\left(0.5 \mathrm{~m}^{-1}\right) x^{2} \text { and } d y=2\left(0.5 \mathrm{~m}^{-1}\right) x d x
$$

Then, the integral for the work is just a definite integral of a function of $x$.

## Solution

The infinitesimal element of work is

$$
\begin{aligned}
d W & =F_{x} d x+F_{y} d y=(5 \mathrm{~N} / \mathrm{m}) y d x+(10 \mathrm{~N} / \mathrm{m}) x d y \\
& =(5 \mathrm{~N} / \mathrm{m})\left(0.5 \mathrm{~m}^{-1}\right) x^{2} d x+(10 \mathrm{~N} / \mathrm{m}) 2\left(0.5 \mathrm{~m}^{-1}\right) x^{2} d x=\left(12.5 \mathrm{~N} / \mathrm{m}^{2}\right) x^{2} d x
\end{aligned}
$$

The integral of $x^{2}$ is $x^{3} / 3$, so

$$
W=\int_{0}^{2 \mathrm{~m}}\left(12.5 \mathrm{~N} / \mathrm{m}^{2}\right) x^{2} d x=\left.\left(12.5 \mathrm{~N} / \mathrm{m}^{2}\right) \frac{x^{3}}{3}\right|_{0} ^{2 \mathrm{~m}}=\left(12.5 \mathrm{~N} / \mathrm{m}^{2}\right)\left(\frac{8}{3}\right)=33.3 \mathrm{~J}
$$

## Significance

This integral was not hard to do. You can follow the same steps, as in this example, to calculate line integrals representing work for more complicated forces and paths. In this example, everything was given in terms of $x$ and $y$-components, which are easiest to use in evaluating the work in this case. In other situations, magnitudes and angles might be easier.

## EXAMPLE 7.5

## Work Done by a Spring Force

A perfectly elastic spring requires $0.54 \mathrm{~J}$ of work to stretch $6 \mathrm{~cm}$ from its equilibrium position, as in Figure 7.7(b). (a) What is its spring constant $k$ ? (b) How much work is required to stretch it an additional $6 \mathrm{~cm}$ ?

## Strategy

Work "required" means work done against the spring force, which is the negative of the work in Equation 7.5, that is

$$
W=\frac{1}{2} k\left(x_{B}^{2}-x_{A}^{2}\right)
$$

For part (a), $x_{A}=0$ and $x_{B}=6 \mathrm{~cm}$; for part (b), $x_{B}=6 \mathrm{~cm}$ and $x_{B}=12 \mathrm{~cm}$. In part (a), the work is given and you can solve for the spring constant; in part (b), you can use the value of $k$, from part (a), to solve for the work.

## Solution

a. $W=0.54 \mathrm{~J}=\frac{1}{2} k\left[(6 \mathrm{~cm})^{2}-0\right]$, so $k=3 \mathrm{~N} / \mathrm{cm}$.
b. $W=\frac{1}{2}(3 \mathrm{~N} / \mathrm{cm})\left[(12 \mathrm{~cm})^{2}-(6 \mathrm{~cm})^{2}\right]=1.62 \mathrm{~J}$.

## Significance

Since the work done by a spring force is independent of the path, you only needed to calculate the difference in the quantity $1 / 2 k x^{2}$ at the end points. Notice that the work required to stretch the spring from 0 to $12 \mathrm{~cm}$ is four times that required to stretch it from 0 to $6 \mathrm{~cm}$, because that work depends on the square of the amount of stretch from equilibrium, $1 / 2 k x^{2}$. In this circumstance, the work to stretch the spring from 0 to $12 \mathrm{~cm}$ is also equal to the work for a composite path from 0 to $6 \mathrm{~cm}$ followed by an additional stretch from $6 \mathrm{~cm}$ to $12 \mathrm{~cm}$. Therefore, $4 W(0 \mathrm{~cm}$ to $6 \mathrm{~cm})=W(0 \mathrm{~cm}$ to $6 \mathrm{~cm})+W(6 \mathrm{~cm}$ to $12 \mathrm{~cm})$, or $W(6 \mathrm{~cm}$ to $12 \mathrm{~cm})=3 W(0 \mathrm{~cm}$ to $6 \mathrm{~cm})$, as we found above.

### 7.2 Kinetic Energy

It's plausible to suppose that the greater the velocity of a body, the greater effect it could have on other bodies. This does not depend on the direction of the velocity, only its magnitude. At the end of the seventeenth century, a quantity was introduced into mechanics to explain collisions between two perfectly elastic bodies, in which one body makes a head-on collision with an identical body at rest. The first body stops, and the second body moves off with the initial velocity of the first body. (If you have ever played billiards or croquet, or seen a model of Newton's Cradle, you have observed this type of collision.) The idea behind this quantity was related to the forces acting on a body and was referred to as "the energy of motion." Later on, during the eighteenth century, the name kinetic energy was given to energy of motion.

With this history in mind, we can now state the classical definition of kinetic energy. Note that when we say "classical," we mean non-relativistic, that is, at speeds much less that the speed of light. At speeds comparable to the speed of light, the special theory of relativity requires a different expression for the kinetic energy of a particle, as discussed in Relativity.

Since objects (or systems) of interest vary in complexity, we first define the kinetic energy of a particle with mass $m$.

## Kinetic Energy

The kinetic energy of a particle is one-half the product of the particle's mass $m$ and the square of its speed $v$.

$$
K=\frac{1}{2} m v^{2}
$$

We then extend this definition to any system of particles by adding up the kinetic energies of all the constituent
particles:

$$
K=\sum \frac{1}{2} m v^{2}
$$

Note that just as we can express Newton's second law in terms of either the rate of change of momentum or mass times the rate of change of velocity, so the kinetic energy of a particle can be expressed in terms of its mass and momentum $(\overrightarrow{\mathbf{p}}=m \overrightarrow{\mathbf{v}})$, instead of its mass and velocity. Since $v=p / m$, we see that

$$
K=\frac{1}{2} m\left(\frac{p}{m}\right)^{2}=\frac{p^{2}}{2 m}
$$

also expresses the kinetic energy of a single particle. Sometimes, this expression is more convenient to use than Equation 7.6.

The units of kinetic energy are mass times the square of speed, or $\mathrm{kg} \cdot \mathrm{m}^{2} / \mathrm{s}^{2}$. But the units of force are mass times acceleration, $\mathrm{kg} \cdot \mathrm{m} / \mathrm{s}^{2}$, so the units of kinetic energy are also the units of force times distance, which are the units of work, or joules. You will see in the next section that work and kinetic energy have the same units, because they are different forms of the same, more general, physical property.

## EXAMPLE 7.6

## Kinetic Energy of an Object

(a) What is the kinetic energy of an $80-\mathrm{kg}$ athlete, running at $10 \mathrm{~m} / \mathrm{s}$ ? (b) The Chicxulub crater in Yucatan, one of the largest existing impact craters on Earth, is thought to have been created by an asteroid, traveling at $22 \mathrm{~km} / \mathrm{s}$ and releasing $4.2 \times 10^{23} \mathrm{~J}$ of kinetic energy upon impact. What was its mass? (c) In nuclear reactors, thermal neutrons, traveling at about $2.2 \mathrm{~km} / \mathrm{s}$, play an important role. What is the kinetic energy of such a particle?

## Strategy

To answer these questions, you can use the definition of kinetic energy in Equation 7.6. You also have to look up the mass of a neutron.

## Solution

Don't forget to convert $\mathrm{km}$ into $\mathrm{m}$ to do these calculations, although, to save space, we omitted showing these conversions.
a. $K=\frac{1}{2}(80 \mathrm{~kg})(10 \mathrm{~m} / \mathrm{s})^{2}=4.0 \mathrm{~kJ}$.
b. $m=2 K / v^{2}=2\left(4.2 \times 10^{23} \mathrm{~J}\right) /(22 \mathrm{~km} / \mathrm{s})^{2}=1.7 \times 10^{15} \mathrm{~kg}$.
c. $K=\frac{1}{2}\left(1.68 \times 10^{-27} \mathrm{~kg}\right)(2.2 \mathrm{~km} / \mathrm{s})^{2}=4.1 \times 10^{-21} \mathrm{~J}$.

## Significance

In this example, we used the way mass and speed are related to kinetic energy, and we encountered a very wide range of values for the kinetic energies. Different units are commonly used for such very large and very small values. The energy of the impactor in part (b) can be compared to the explosive yield of TNT and nuclear explosions, 1 megaton $=4.18 \times 10^{15} \mathrm{~J}$. The Chicxulub asteroid's kinetic energy was about a hundred million megatons. At the other extreme, the energy of subatomic particle is expressed in electron-volts, $1 \mathrm{eV}=1.6 \times 10^{-19} \mathrm{~J}$. The thermal neutron in part (c) has a kinetic energy of about one fortieth of an electronvolt.

## EXAMPLE 7.7

## Kinetic Energy Relative to Different Frames

A $75.0-\mathrm{kg}$ person walks down the central aisle of a subway car at a speed of $1.50 \mathrm{~m} / \mathrm{s}$ relative to the car, whereas the train is moving at $15.0 \mathrm{~m} / \mathrm{s}$ relative to the tracks. (a) What is the person's kinetic energy relative to the car? (b) What is the person's kinetic energy relative to the tracks? (c) What is the person's kinetic energy relative to a frame moving with the person?

## Strategy

Since speeds are given, we can use $\frac{1}{2} m v^{2}$ to calculate the person's kinetic energy. However, in part (a), the person's speed is relative to the subway car (as given); in part (b), it is relative to the tracks; and in part (c), it is zero. If we denote the car frame by C, the track frame by $\mathrm{T}$, and the person by $\mathrm{P}$, the relative velocities in part (b) are related by $\overrightarrow{\mathbf{v}}_{\mathrm{PT}}=\overrightarrow{\mathbf{v}}_{\mathrm{PC}}+\overrightarrow{\mathbf{v}}_{\mathrm{CT}}$. We can assume that the central aisle and the tracks lie along the same line, but the direction the person is walking relative to the car isn't specified, so we will give an answer for each possibility, $v_{\mathrm{PT}}=v_{\mathrm{CT}} \pm v_{\mathrm{PC}}$, as shown in Figure 7.10.

## Solution

a. $K=\frac{1}{2}(75.0 \mathrm{~kg})(1.50 \mathrm{~m} / \mathrm{s})^{2}=84.4 \mathrm{~J}$.
b. $v_{\mathrm{PT}}=(15.0 \pm 1.50) \mathrm{m} / \mathrm{s}$. Therefore, the two possible values for kinetic energy relative to the car are

$$
K=\frac{1}{2}(75.0 \mathrm{~kg})(13.5 \mathrm{~m} / \mathrm{s})^{2}=6.83 \mathrm{~kJ}
$$

and

$$
K=\frac{1}{2}(75.0 \mathrm{~kg})(16.5 \mathrm{~m} / \mathrm{s})^{2}=10.2 \mathrm{~kJ}
$$

c. In a frame where $v_{\mathrm{P}}=0, K=0$ as well.

## Significance

You can see that the kinetic energy of an object can have very different values, depending on the frame of reference. However, the kinetic energy of an object can never be negative, since it is the product of the mass and the square of the speed, both of which are always positive or zero.

## EXAMPLE 7.8

## Special Names for Kinetic Energy

(a) A player lobs a mid-court pass with a $624-\mathrm{g}$ basketball, which covers $15 \mathrm{~m}$ in $2 \mathrm{~s}$. What is the basketball's horizontal translational kinetic energy while in flight? (b) An average molecule of air, in the basketball in part (a), has a mass of $29 \mathrm{u}$, and an average speed of $500 \mathrm{~m} / \mathrm{s}$, relative to the basketball. There are about $3 \times 10^{23}$ molecules inside it, moving in random directions, when the ball is properly inflated. What is the average translational kinetic energy of the random motion of all the molecules inside, relative to the basketball? (c) How fast would the basketball have to travel relative to the court, as in part (a), so as to have a kinetic energy equal to the amount in part (b)?

## Strategy

In part (a), first find the horizontal speed of the basketball and then use the definition of kinetic energy in terms of mass and speed, $K=\frac{1}{2} m v^{2}$. Then in part (b), convert unified units to kilograms and then use $K=\frac{1}{2} m v^{2}$ to get the average translational kinetic energy of one molecule, relative to the basketball. Then multiply by the number of molecules to get the total result. Finally, in part (c), we can substitute the amount of kinetic energy in part (b), and the mass of the basketball in part (a), into the definition $K=\frac{1}{2} m v^{2}$, and solve for $v$.

## Solution

a. The horizontal speed is $(15 \mathrm{~m}) /(2 \mathrm{~s})$, so the horizontal kinetic energy of the basketball is

$$
\frac{1}{2}(0.624 \mathrm{~kg})(7.5 \mathrm{~m} / \mathrm{s})^{2}=17.6 \mathrm{~J}
$$

b. The average translational kinetic energy of a molecule is

$$
\frac{1}{2}(29 \mathrm{u})\left(1.66 \times 10^{-27} \mathrm{~kg} / \mathrm{u}\right)(500 \mathrm{~m} / \mathrm{s})^{2}=6.02 \times 10^{-21} \mathrm{~J}
$$

and the total kinetic energy of all the molecules is

$$
\left(3 \times 10^{23}\right)\left(6.02 \times 10^{-21} \mathrm{~J}\right)=1.80 \mathrm{~kJ}
$$

c. $v=\sqrt{2(1.8 \mathrm{~kJ}) /(0.624 \mathrm{~kg})}=76.0 \mathrm{~m} / \mathrm{s}$.

## Significance

In part (a), this kind of kinetic energy can be called the horizontal kinetic energy of an object (the basketball), relative to its surroundings (the court). If the basketball were spinning, all parts of it would have not just the average speed, but it would also have rotational kinetic energy. Part (b) reminds us that this kind of kinetic energy can be called internal or thermal kinetic energy. Notice that this energy is about a hundred times the energy in part (a). How to make use of thermal energy will be the subject of the chapters on thermodynamics. In part (c), since the energy in part (b) is about 100 times that in part (a), the speed should be about 10 times as big, which it is ( 76 compared to $7.5 \mathrm{~m} / \mathrm{s}$ ).

### 7.3 Work-Energy Theorem

We have discussed how to find the work done on a particle by the forces that act on it, but how is that work manifested in the motion of the particle? According to Newton's second law of motion, the sum of all the forces acting on a particle, or the net force, determines the rate of change in the momentum of the particle, or its motion. Therefore, we should consider the work done by all the forces acting on a particle, or the net work, to see what effect it has on the particle's motion.

Let's start by looking at the net work done on a particle as it moves over an infinitesimal displacement, which is the dot product of the net force and the displacement: $d W_{\text {net }}=\overrightarrow{\mathbf{F}}_{\text {net }} \cdot d \overrightarrow{\mathbf{r}}$. Newton's second law tells us that $\overrightarrow{\mathbf{F}}_{\text {net }}=m(d \overrightarrow{\mathbf{v}} / d t)$, so $d W_{\text {net }}=m(d \overrightarrow{\mathbf{v}} / d t) \cdot d \overrightarrow{\mathbf{r}}$. For the mathematical functions describing the motion of a physical particle, we can rearrange the differentials $d t$, etc., as algebraic quantities in this expression, that is,

$$
d W_{\text {net }}=m\left(\frac{d \overrightarrow{\mathbf{v}}}{d t}\right) \cdot d \overrightarrow{\mathbf{r}}=m d \overrightarrow{\mathbf{v}} \cdot\left(\frac{d \overrightarrow{\mathbf{r}}}{d t}\right)=m \overrightarrow{\mathbf{v}} \cdot d \overrightarrow{\mathbf{v}}
$$

where we substituted the velocity for the time derivative of the displacement and used the commutative property of the dot product [Equation 2.30]. Since derivatives and integrals of scalars are probably more familiar to you at this point, we express the dot product in terms of Cartesian coordinates before we integrate between any two points $A$ and $B$ on the particle's trajectory. This gives us the net work done on the particle:

$$
\begin{align*}
W_{\mathrm{net}, A B} & =\int_{A}^{B}\left(m v_{x} d v_{x}+m v_{y} d v_{y}+m v_{z} d v_{z}\right) \\
& =\frac{1}{2} m\left|v_{x}^{2}+v_{y}^{2}+v_{z}^{2}\right|_{A}^{B}=\left|\frac{1}{2} m v^{2}\right|_{A}^{B}=K_{B}-K_{A}
\end{align*}
$$

In the middle step, we used the fact that the square of the velocity is the sum of the squares of its Cartesian components, and in the last step, we used the definition of the particle's kinetic energy. This important result is called the work-energy theorem (Figure 7.11).

## Work-Energy Theorem

The net work done on a particle equals the change in the particle's kinetic energy:

$$
W_{\text {net }}=K_{B}-K_{A}
$$

According to this theorem, when an object slows down, its final kinetic energy is less than its initial kinetic energy, the change in its kinetic energy is negative, and so is the net work done on it. If an object speeds up, the net work done on it is positive. When calculating the net work, you must include all the forces that act on an object. If you leave out any forces that act on an object, or if you include any forces that don't act on it, you will get a wrong result.

The importance of the work-energy theorem, and the further generalizations to which it leads, is that it makes some types of calculations much simpler to accomplish than they would be by trying to solve Newton's second law. For example, in Newton's Laws of Motion, we found the speed of an object sliding down a frictionless plane by solving Newton's second law for the acceleration and using kinematic equations for constant acceleration, obtaining

$$
v_{\mathrm{f}}^{2}=v_{\mathrm{i}}^{2}+2 g\left(s_{\mathrm{f}}-s_{\mathrm{i}}\right) \sin \theta
$$

where $s$ is the displacement down the plane.

We can also get this result from the work-energy theorem in Equation 7.1. Since only two forces are acting on the object-gravity and the normal force-and the normal force doesn't do any work, the net work is just the work done by gravity. The work dW is the dot product of the force of gravity or $\overrightarrow{\mathbf{F}}=-\mathrm{mg} \hat{\mathrm{j}}$ and the displacement $\overrightarrow{d r}=d x \hat{i}+d y \hat{j}$. After taking the dot product and integrating from an initial position $y_{i}$ to a final position $y_{f}$, one finds the net work as

$$
W_{\text {net }}=W_{\text {grav }}=-m g\left(y_{\mathrm{f}}-y_{\mathrm{i}}\right)
$$

where $y$ is positive up. The work-energy theorem says that this equals the change in kinetic energy:

$$
-m g\left(y_{\mathrm{f}}-y_{\mathrm{i}}\right)=\frac{1}{2} m\left(v_{\mathrm{f}}^{2}-v_{\mathrm{i}}^{2}\right)
$$

Using a right triangle, we can see that $\left(y_{\mathrm{f}}-y_{\mathrm{i}}\right)=\left(s_{\mathrm{f}}-s_{\mathrm{i}}\right) \sin \theta$, so the result for the final speed is the same.

What is gained by using the work-energy theorem? The answer is that for a frictionless plane surface, not much. However, Newton's second law is easy to solve only for this particular case, whereas the work-energy theorem gives the final speed for any shaped frictionless surface. For an arbitrary curved surface, the normal force is not constant, and Newton's second law may be difficult or impossible to solve analytically. Constant or not, for motion along a surface, the normal force never does any work, because it's perpendicular to the displacement. A calculation using the work-energy theorem avoids this difficulty and applies to more general situations.

## PROBLEM-SOLVING STRATEG

## Work-Energy Theorem

1. Draw a free-body diagram for each force on the object.
2. Determine whether or not each force does work over the displacement in the diagram. Be sure to keep any positive or negative signs in the work done.
3. Add up the total amount of work done by each force.
4. Set this total work equal to the change in kinetic energy and solve for any unknown parameter.
5. Check your answers. If the object is traveling at a constant speed or zero acceleration, the total work done should be zero and match the change in kinetic energy. If the total work is positive, the object must have sped up or increased kinetic energy. If the total work is negative, the object must have slowed down or decreased kinetic energy.

## EXAMPLE 7.9

## Loop-the-Loop

The frictionless track for a toy car includes a loop-the-loop of radius $R$. How high, measured from the bottom of the loop, must the car be placed to start from rest on the approaching section of track and go all the way around the loop?

## Strategy

The free-body diagram at the final position of the object is drawn in Figure 7.12. The gravitational work is the only work done over the displacement that is not zero. Since the weight points in the same direction as the net vertical displacement, the total work done by the gravitational force is positive. From the work-energy theorem, the starting height determines the speed of the car at the top of the loop,

$$
-m g\left(y_{2}-y_{1}\right)=\frac{1}{2} m v_{2}^{2}
$$

where the notation is shown in the accompanying figure. At the top of the loop, the normal force and gravity are both down and the acceleration is centripetal, so

$$
a_{\text {top }}=\frac{F}{m}=\frac{N+m g}{m}=\frac{v_{2}^{2}}{R}
$$

The condition for maintaining contact with the track is that there must be some normal force, however slight; that is, $N>0$. Substituting for $v_{2}^{2}$ and $N$, we can find the condition for $y_{1}$.

## Solution

Implement the steps in the strategy to arrive at the desired result:

$$
N=-m g+\frac{m v_{2}^{2}}{R}=\frac{-m g R+2 m g\left(y_{1}-R\right)}{R}>0 \text { or } y_{1}>\frac{5 R}{2} \text {. }
$$

## Significance

On the surface of the loop, the normal component of gravity and the normal contact force must provide the centripetal acceleration of the car going around the loop. The tangential component of gravity slows down or speeds up the car. A child would find out how high to start the car by trial and error, but now that you know the work-energy theorem, you can predict the minimum height (as well as other more useful results) from physical principles. By using the work-energy theorem, you did not have to solve a differential equation to determine the height.

## EXAMPLE 7.10

## Determining a Stopping Force

A bullet has a mass of 40 grains $(2.60 \mathrm{~g})$ and a muzzle velocity of $1100 \mathrm{ft} . / \mathrm{s}(335 \mathrm{~m} / \mathrm{s})$. It can penetrate eight 1-inch pine boards, each with thickness 0.75 inches. What is the average stopping force exerted by the wood, as shown in Figure 7.13 ?

## Strategy

We can assume that under the general conditions stated, the bullet loses all its kinetic energy penetrating the boards, so the work-energy theorem says its initial kinetic energy is equal to the average stopping force times the distance penetrated. The change in the bullet's kinetic energy and the net work done stopping it are both negative, so when you write out the work-energy theorem, with the net work equal to the average force times the stopping distance, that's what you get. The total thickness of eight 1-inch pine boards that the bullet penetrates is $8 \times \frac{3}{4} \mathrm{in} .=6 \mathrm{in} .=15.2 \mathrm{~cm}$.

## Solution

Applying the work-energy theorem, we get

$$
W_{\text {net }}=-F_{\text {ave }} \Delta s_{\text {stop }}=-K_{\text {initial }}
$$

$$
F_{\text {ave }}=\frac{\frac{1}{2} m v^{2}}{\Delta s_{\text {stop }}}=\frac{\frac{1}{2}\left(2.6 \times 10^{-3} \mathrm{~kg}\right)(335 \mathrm{~m} / \mathrm{s})^{2}}{0.152 \mathrm{~m}}=960 \mathrm{~N}
$$

## Significance

We could have used Newton's second law and kinematics in this example, but the work-energy theorem also supplies an answer to less simple situations. The penetration of a bullet, fired vertically upward into a block of wood, is discussed in one section of Asif Shakur's recent article ["Bullet-Block Science Video Puzzle." The Physics Teacher (January 2015) 53(1): 15-16]. If the bullet is fired dead center into the block, it loses all its kinetic energy and penetrates slightly farther than if fired off-center. The reason is that if the bullet hits offcenter, it has a little kinetic energy after it stops penetrating, because the block rotates. The work-energy theorem implies that a smaller change in kinetic energy results in a smaller penetration. You will understand more of the physics in this interesting article after you finish reading Angular Momentum.

### 7.4 Power

The concept of work involves force and displacement; the work-energy theorem relates the net work done on a body to the difference in its kinetic energy, calculated between two points on its trajectory. None of these quantities or relations involves time explicitly, yet we know that the time available to accomplish a particular amount of work is frequently just as important to us as the amount itself. In the chapter-opening figure, several sprinters may have achieved the same velocity at the finish, and therefore did the same amount of work, but the winner of the race did it in the least amount of time.

We express the relation between work done and the time interval involved in doing it, by introducing the concept of power. Since work can vary as a function of time, we first define average power as the work done during a time interval, divided by the interval,

$$
P_{\mathrm{ave}}=\frac{\Delta W}{\Delta t}
$$

Then, we can define the instantaneous power (frequently referred to as just plain power).

## Power

Power is defined as the rate of doing work, or the limit of the average power for time intervals approaching zero,

$$
P=\frac{d W}{d t}
$$

If the power is constant over a time interval, the average power for that interval equals the instantaneous power, and the work done by the agent supplying the power is $W=P \Delta t$. If the power during an interval varies with time, then the work done is the time integral of the power,

$$
W=\int P d t
$$

The work-energy theorem relates how work can be transformed into kinetic energy. Since there are other forms of energy as well, as we discuss in the next chapter, we can also define power as the rate of transfer of energy. Work and energy are measured in units of joules, so power is measured in units of joules per second, which has been given the SI name watts, abbreviation $\mathrm{W}: 1 \mathrm{~J} / \mathrm{s}=1 \mathrm{~W}$. Another common unit for expressing the power capability of everyday devices is horsepower: $1 \mathrm{hp}=746 \mathrm{~W}$.

## EXAMPLE 7.11

## Pull-Up Power

An 80-kg army trainee does pull-ups on a horizontal bar (Figure 7.14). It takes the trainee 0.8 seconds to raise the body from a lower position to where the chin is above the bar. How much power do the trainee's muscles supply moving his body from the lower position to where the chin is above the bar? (Hint: Make reasonable estimates for any quantities needed.)

## Strategy

The work done against gravity, going up or down a distance $\Delta y$, is $m g \Delta y$. Let's assume that $\Delta y=2 \mathrm{ft} \approx 60 \mathrm{~cm}$. Also, assume that the arms comprise $10 \%$ of the body mass and are not included in the moving mass. With these assumptions, we can calculate the work done.

## Solution

The result we get, applying our assumptions, is

$$
P=\frac{\mathrm{mg}(\Delta y)}{t}=\frac{0.9(80 \mathrm{~kg})\left(9.8 \mathrm{~m} / \mathrm{s}^{2}\right)(0.60 \mathrm{~m})}{0.8 \mathrm{~s}}=529 \mathrm{~W}
$$

## Significance

This is typical for power expenditure in strenuous exercise; in everyday units, it's somewhat more than one horsepower $(1 \mathrm{hp}=746 \mathrm{~W})$.

## EXAMPLE 7.12

## Automotive Power Driving Uphill

How much power must an automobile engine expend to move a $1200-\mathrm{kg}$ car up a $15 \%$ grade at $90 \mathrm{~km} / \mathrm{h}$ (Figure 7.15)? Assume that $25 \%$ of this power is dissipated overcoming air resistance and friction.

## Strategy

At constant velocity, there is no change in kinetic energy, so the net work done to move the car is zero.

Therefore the power supplied by the engine to move the car equals the power expended against gravity and air resistance. By assumption, $75 \%$ of the power is supplied against gravity, which equals $m \overrightarrow{\mathbf{g}} \cdot \overrightarrow{\mathbf{v}}=m g v \sin \theta$, where $\theta$ is the angle of the incline. A $15 \%$ grade means $\tan \theta=0.15$. This reasoning allows us to solve for the power required.

## Solution

Carrying out the suggested steps, we find

$$
0.75 P=m g v \sin \left(\tan ^{-1} 0.15\right)
$$

or

$$
P=\frac{(1200 \times 9.8 \mathrm{~N})(90 \mathrm{~m} / 3.6 \mathrm{~s}) \sin \left(8.53^{\circ}\right)}{0.75}=58 \mathrm{~kW}
$$

or about $78 \mathrm{hp}$. (You should supply the steps used to convert units.)

## Significance

This is a reasonable amount of power for the engine of a small to mid-size car to supply ( $1 \mathrm{hp}=0.746 \mathrm{~kW}$ ). Note that this is only the power expended to move the car. Much of the engine's power goes elsewhere, for example, into waste heat. That's why cars need radiators. Any remaining power could be used for acceleration, or to operate the car's accessories.

