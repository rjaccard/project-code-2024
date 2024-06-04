# CHAPTER 11 Angular Momentum 

INTRODUCTION Angular momentum is the rotational counterpart of linear momentum. Any massive object that rotates about an axis carries angular momentum, including rotating flywheels, planets, stars, hurricanes, tornadoes, whirlpools, and so on. The helicopter shown in the chapter-opening picture can be used to illustrate the concept of angular momentum. The lift blades spin about a vertical axis through the main body and carry angular momentum. The body of the helicopter tends to rotate in the opposite sense in order to conserve angular momentum. The small rotors at the tail of the aircraft provide a counter thrust against the body to prevent this from happening, and the helicopter stabilizes itself. The concept of conservation of angular momentum is discussed later in this chapter. In the main part of this chapter, we explore the intricacies of angular momentum of rigid bodies such as a top, and also of point particles and systems of particles. But to be complete, we start with a discussion of rolling motion, which builds upon the concepts of the previous chapter.

### 11.1 Rolling Motion

Rolling motion is that common combination of rotational and translational motion that we see everywhere, every day. Think about the different situations of wheels moving on a car along a highway, or wheels on a plane landing on a runway, or wheels on a robotic explorer on another planet. Understanding the forces and torques involved in rolling motion is a crucial factor in many different types of situations.

For analyzing rolling motion in this chapter, refer to Figure 10.20 in Fixed-Axis Rotation to find moments of inertia of some common geometrical objects. You may also find it useful in other calculations involving rotation.

## Rolling Motion without Slipping

People have observed rolling motion without slipping ever since the invention of the wheel. For example, we can look at the interaction of a car's tires and the surface of the road. If the driver depresses the accelerator to the floor, such that the tires spin without the car moving forward, there must be kinetic friction between the wheels and the surface of the road. If the driver depresses the accelerator slowly, causing the car to move forward, then the tires roll without slipping. It is surprising to most people that, in fact, the bottom of the wheel is at rest with respect to the ground, indicating there must be static friction between the tires and the road surface. In Figure 11.2, the bicycle is in motion with the rider staying upright. The tires have contact with the road surface, and, even though they are rolling, the bottoms of the tires deform slightly, do not slip, and are at rest with respect to the road surface for a measurable amount of time. There must be static friction between the tire and the road surface for this to be so.

To analyze rolling without slipping, we first derive the linear variables of velocity and acceleration of the center
of mass of the wheel in terms of the angular variables that describe the wheel's motion.

From Figure 11.3(a), we see the force vectors involved in preventing the wheel from slipping. In (b), point $P$ that touches the surface is at rest relative to the surface. Relative to the center of mass, point $P$ has velocity $-R \omega \hat{\mathbf{i}}$, where $R$ is the radius of the wheel and $\omega$ is the wheel's angular velocity about its axis. Since the wheel is rolling, the velocity of $P$ with respect to the surface is its velocity with respect to the center of mass plus the velocity of the center of mass with respect to the surface:

$$
\overrightarrow{\mathbf{v}}_{P}=-R \omega \hat{\mathbf{i}}+v_{\mathrm{CM}} \hat{\mathbf{i}}
$$

Since the velocity of $P$ relative to the surface is zero, $v_{P}=0$, this says that

$$
v_{\mathrm{CM}}=R \omega
$$

Thus, the velocity of the wheel's center of mass is its radius times the angular velocity about its axis. We show the correspondence of the linear variable on the left side of the equation with the angular variable on the right side of the equation. This is done below for the linear acceleration.

If we differentiate Equation 11.1 on the left side of the equation, we obtain an expression for the linear acceleration of the center of mass. On the right side of the equation, $R$ is a constant and since $\alpha=\frac{d \omega}{d t}$, we have

$$
a_{\mathrm{CM}}=R \alpha
$$

Furthermore, we can find the distance the wheel travels in terms of angular variables by referring to Figure 11.4. As the wheel rolls from point $A$ to point $B$, its outer surface maps onto the ground by exactly the distance travelled, which is $d_{\mathrm{CM}}$. We see from Figure 11.4 that the length of the outer surface that maps onto the ground is the arc length $R \theta \quad$. Equating the two distances, we obtain

$$
d_{\mathrm{CM}}=R \theta
$$

Arc length $A B$ maps onto wheel's surface

## EXAMPLE 11.1

## Rolling Down an Inclined Plane

A solid cylinder rolls down an inclined plane without slipping, starting from rest. It has mass $m$ and radius $r$. (a) What is its acceleration? (b) What condition must the coefficient of static friction $\mu_{\mathrm{s}}$ satisfy so the cylinder does not slip?

## Strategy

Draw a sketch and free-body diagram, and choose a coordinate system. We put $x$ in the direction down the plane and y upward perpendicular to the plane. Identify the forces involved. These are the normal force, the force of gravity, and the force due to friction. Write down Newton's laws in the $x$ - and $y$-directions, and Newton's law for rotation, and then solve for the acceleration and force due to friction.

## Solution

a. The free-body diagram and sketch are shown in Figure 11.5, including the normal force, components of the weight, and the static friction force. There is barely enough friction to keep the cylinder rolling without slipping. Since there is no slipping, the magnitude of the friction force is less than or equal to $\mu_{S} N$. Writing down Newton's laws in the $x$ - and $y$-directions, we have

$$
\sum F_{x}=m a_{x} ; \quad \sum F_{y}=m a_{y}
$$

Substituting in from the free-body diagram,

$$
\begin{aligned}
m g \sin \theta-f_{\mathrm{s}} & =m\left(a_{\mathrm{CM}}\right)_{x} \\
N-m g \cos \theta & =0
\end{aligned}
$$

we can then solve for the linear acceleration of the center of mass from these equations:

$$
a_{\mathrm{CM}}=g \sin \theta-\frac{f_{\mathrm{s}}}{m}
$$

However, it is useful to express the linear acceleration in terms of the moment of inertia. For this, we write down Newton's second law for rotation,

$$
\sum \tau_{\mathrm{CM}}=I_{\mathrm{CM}} \alpha
$$

The torques are calculated about the axis through the center of mass of the cylinder. The only nonzero torque is provided by the friction force. We have

$$
f_{\mathrm{s}} r=I_{\mathrm{CM}} \alpha
$$

Finally, the linear acceleration is related to the angular acceleration by

$$
\left(a_{\mathrm{CM}}\right)_{x}=r \alpha
$$

These equations can be used to solve for $a_{\mathrm{CM}}, \alpha$, and $f_{\mathrm{s}}$ in terms of the moment of inertia, where we have dropped the $x$-subscript. We rewrite $a_{\mathrm{CM}}$ in terms of the vertical component of gravity and the friction force, and make the following substitutions.

$$
f_{\mathrm{s}}=\frac{I_{\mathrm{CM}} \alpha}{r}=\frac{I_{\mathrm{CM}} a_{\mathrm{CM}}}{r^{2}}
$$

From this we obtain

$$
\begin{aligned}
a_{\mathrm{CM}} & =g \sin \theta-\frac{I_{\mathrm{CM}}{ }^{a} \mathrm{CM}}{m r^{2}} \\
& =\frac{m g \sin \theta}{m+\left(I_{\mathrm{CM}} r^{2}\right)}
\end{aligned}
$$

Note that this result is independent of the coefficient of static friction, $\mu_{\mathrm{s}}$.

Since we have a solid cylinder, from Figure 10.20 , we have $I_{\mathrm{CM}}=m r^{2} / 2$ and

$$
a_{\mathrm{CM}}=\frac{m g \sin \theta}{m+\left(m r^{2} / 2 r^{2}\right)}=\frac{2}{3} g \sin \theta
$$

Therefore, we have

$$
\alpha=\frac{a_{\mathrm{CM}}}{r}=\frac{2}{3 r} g \sin \theta
$$

b. Because slipping does not occur, $f_{\mathrm{s}} \leq \mu_{\mathrm{s}} N$. Solving for the friction force,

$$
f_{\mathrm{s}}=I_{\mathrm{CM}} \frac{\alpha}{r}=I_{\mathrm{CM}} \frac{\left(a_{\mathrm{CM}}\right)}{r^{2}}=\frac{I_{\mathrm{CM}}}{r^{2}}\left(\frac{m g \sin \theta}{m+\left(I_{\mathrm{CM}} / r^{2}\right)}\right)=\frac{m g I_{\mathrm{CM}} \sin \theta}{m r^{2}+I_{\mathrm{CM}}}
$$

Substituting this expression into the condition for no slipping, and noting that $N=m g \cos \theta$, we have

$$
\frac{m g I_{\mathrm{CM}} \sin \theta}{m r^{2}+I_{\mathrm{CM}}} \leq \mu_{\mathrm{s}} m g \cos \theta
$$

or

$$
\mu_{\mathrm{s}} \geq \frac{\tan \theta}{1+\left(m r^{2} / I_{\mathrm{CM}}\right)}
$$

For the solid cylinder, this becomes

$$
\mu_{\mathrm{s}} \geq \frac{\tan \theta}{1+\left(2 m r^{2} / m r^{2}\right)}=\frac{1}{3} \tan \theta
$$

## Significance

a. The linear acceleration is linearly proportional to $\sin \theta$. Thus, the greater the angle of the incline, the greater the linear acceleration, as would be expected. The angular acceleration, however, is linearly proportional to $\sin \theta$ and inversely proportional to the radius of the cylinder. Thus, the larger the radius, the smaller the angular acceleration.

b. For no slipping to occur, the coefficient of static friction must be greater than or equal to ( $1 / 3) \tan \theta$. Thus, the greater the angle of incline, the greater the coefficient of static friction must be to prevent the cylinder from slipping.

## Rolling Motion with Slipping

In the case of rolling motion with slipping, we must use the coefficient of kinetic friction, which gives rise to the kinetic friction force since static friction is not present. The situation is shown in Figure 11.6. In the case of slipping, $v_{\mathrm{CM}}-R \omega \neq 0$, because point $P$ on the wheel is not at rest on the surface, and $v_{P} \neq 0$. Thus, $\omega \neq \frac{v_{\mathrm{CM}}}{R}, \alpha \neq \frac{a_{\mathrm{CM}}}{R}$.

## EXAMPLE 11.2

## Rolling Down an Inclined Plane with Slipping

A solid cylinder rolls down an inclined plane from rest and undergoes slipping (Figure 11.7). It has mass $m$ and radius $r$. (a) What is its linear acceleration? (b) What is its angular acceleration about an axis through the center of mass?

## Strategy

Draw a sketch and free-body diagram showing the forces involved. The free-body diagram is similar to the noslipping case except for the friction force, which is kinetic instead of static. Use Newton's second law to solve for the acceleration in the $x$-direction. Use Newton's second law of rotation to solve for the angular acceleration.

## Solution

The sum of the forces in the $y$-direction is zero, so the friction force is now $f_{\mathrm{k}}=\mu_{\mathrm{k}} N=\mu_{\mathrm{k}} m g \cos \theta$.

Newton's second law in the $x$-direction becomes

$$
\begin{gathered}
\sum F_{x}=m a_{x} \\
m g \sin \theta-\mu_{\mathrm{k}} m g \cos \theta=m\left(a_{\mathrm{CM}}\right)_{x}
\end{gathered}
$$

or

$$
\left(a_{\mathrm{CM}}\right)_{x}=g\left(\sin \theta-\mu_{\mathrm{k}} \cos \theta\right)
$$

The friction force provides the only torque about the axis through the center of mass, so Newton's second law of rotation becomes

$$
\begin{gathered}
\sum \tau_{\mathrm{CM}}=I_{\mathrm{CM}} \alpha \\
f_{\mathrm{k}} r=I_{\mathrm{CM}} \alpha=\frac{1}{2} m r^{2} \alpha
\end{gathered}
$$

Solving for $\alpha$, we have

$$
\alpha=\frac{2 f_{\mathrm{k}}}{m r}=\frac{2 \mu_{\mathrm{k}} g \cos \theta}{r}
$$

## Significance

We write the linear and angular accelerations in terms of the coefficient of kinetic friction. The linear acceleration is the same as that found for an object sliding down an inclined plane with kinetic friction. The angular acceleration about the axis of rotation is linearly proportional to the normal force, which depends on the cosine of the angle of inclination. As $\theta \rightarrow 90^{\circ}$, this force goes to zero, and, thus, the angular acceleration goes to zero.

## Conservation of Mechanical Energy in Rolling Motion

In the preceding chapter, we introduced rotational kinetic energy. Any rolling object carries rotational kinetic energy, as well as translational kinetic energy and potential energy if the system requires. Including the gravitational potential energy, the total mechanical energy of an object rolling is

$$
E_{\mathrm{T}}=\frac{1}{2} m v_{\mathrm{CM}}^{2}+\frac{1}{2} I_{\mathrm{CM}} \omega^{2}+m g h
$$

In the absence of any nonconservative forces that would take energy out of the system in the form of heat, the total energy of a rolling object without slipping is conserved and is constant throughout the motion. Examples where energy is not conserved are a rolling object that is slipping, production of heat as a result of kinetic friction, and a rolling object encountering air resistance.

You may ask why a rolling object that is not slipping conserves energy, since the static friction force is nonconservative. The answer can be found by referring back to Figure 11.3. Point $P$ in contact with the surface is at rest with respect to the surface. Therefore, its infinitesimal displacement $d \overrightarrow{\mathbf{r}}$ with respect to the surface is zero, and the incremental work done by the static friction force is zero. We can apply energy conservation to our study of rolling motion to bring out some interesting results.

## EXAMPLE 11.3

## Curiosity Rover

The Curiosity rover, shown in Figure 11.8, was deployed on Mars on August 6, 2012. The wheels of the rover have a radius of $25 \mathrm{~cm}$. Suppose astronauts arrive on Mars in the year 2050 and find the now-inoperative Curiosity on the side of a basin. While they are dismantling the rover, an astronaut accidentally loses a grip on one of the wheels, which rolls without slipping down into the bottom of the basin 25 meters below. If the wheel has a mass of $5 \mathrm{~kg}$, what is its velocity at the bottom of the basin?

## Strategy

We use mechanical energy conservation to analyze the problem. At the top of the hill, the wheel is at rest and has only potential energy. At the bottom of the basin, the wheel has rotational and translational kinetic energy,
which must be equal to the initial potential energy by energy conservation. Since the wheel is rolling without slipping, we use the relation $v_{\mathrm{CM}}=r \omega$ to relate the translational variables to the rotational variables in the energy conservation equation. We then solve for the velocity. From Figure 11.8, we see that a hollow cylinder is a good approximation for the wheel, so we can use this moment of inertia to simplify the calculation.

## Solution

Energy at the top of the basin equals energy at the bottom:

$$
m g h=\frac{1}{2} m v_{\mathrm{CM}}^{2}+\frac{1}{2} I_{\mathrm{CM}} \omega^{2}
$$

The known quantities are $I_{\mathrm{CM}}=m r^{2}, r=0.25 \mathrm{~m}$, and $h=25.0 \mathrm{~m}$.

We rewrite the energy conservation equation eliminating $\omega$ by using $\omega=\frac{v_{\mathrm{CM}}}{r}$. We have

$$
m g h=\frac{1}{2} m v_{\mathrm{CM}}^{2}+\frac{1}{2} m r^{2} \frac{v_{\mathrm{CM}}^{2}}{r^{2}}
$$

or

$$
g h=\frac{1}{2} v_{\mathrm{CM}}^{2}+\frac{1}{2} v_{\mathrm{CM}}^{2} \Rightarrow v_{\mathrm{CM}}=\sqrt{g h}
$$

On Mars, the acceleration of gravity is $3.71 \mathrm{~m} / \mathrm{s}^{2}$, which gives the magnitude of the velocity at the bottom of the basin as

$$
v_{\mathrm{CM}}=\sqrt{\left(3.71 \mathrm{~m} / \mathrm{s}^{2}\right) 25.0 \mathrm{~m}}=9.63 \mathrm{~m} / \mathrm{s}
$$

## Significance

This is a fairly accurate result considering that Mars has very little atmosphere, and the loss of energy due to air resistance would be minimal. The result also assumes that the terrain is smooth, such that the wheel wouldn't encounter rocks and bumps along the way.

Also, in this example, the kinetic energy, or energy of motion, is equally shared between linear and rotational motion. If we look at the moments of inertia in Figure 10.20, we see that the hollow cylinder has the largest moment of inertia for a given radius and mass. If the wheels of the rover were solid and approximated by solid cylinders, for example, there would be more kinetic energy in linear motion than in rotational motion. This would give the wheel a larger linear velocity than the hollow cylinder approximation. Thus, the solid cylinder would reach the bottom of the basin faster than the hollow cylinder.

### 11.2 Angular Momentum

By the end of this section, you will be able to:

- Describe the vector nature of angular momentum
- Find the total angular momentum and torque about a designated origin of a system of particles
- Calculate the angular momentum of a rigid body rotating about a fixed axis
- Calculate the torque on a rigid body rotating about a fixed axis
- Use conservation of angular momentum in the analysis of objects that change their rotation rate

Why does Earth keep on spinning? What started it spinning to begin with? Why doesn't Earth's gravitational attraction not bring the Moon crashing in toward Earth? And how does an ice skater manage to spin faster and faster simply by pulling her arms in? Why does she not have to exert a torque to spin faster?

Questions like these have answers based in angular momentum, the rotational analog to linear momentum. In this chapter, we first define and then explore angular momentum from a variety of viewpoints. First, however, we investigate the angular momentum of a single particle. This allows us to develop angular momentum for a system of particles and for a rigid body that is cylindrically symmetric.

## Angular Momentum of a Single Particle

Figure 11.9 shows a particle at a position $\overrightarrow{\mathbf{r}}$ with linear momentum $\overrightarrow{\mathbf{p}}=m \overrightarrow{\mathbf{v}}$ with respect to the origin. Even if the particle is not rotating about the origin, we can still define an angular momentum in terms of the position vector and the linear momentum.

## Angular Momentum of a Particle

The angular momentum $\overrightarrow{\mathbf{I}}$ of a particle is defined as the cross-product of $\overrightarrow{\mathbf{r}}$ and $\overrightarrow{\mathbf{p}}$, and is perpendicular to the plane containing $\overrightarrow{\mathbf{r}}$ and $\overrightarrow{\mathbf{p}}$ :

$$
\overrightarrow{\mathbf{I}}=\overrightarrow{\mathbf{r}} \times \overrightarrow{\mathbf{p}}
$$

$\overrightarrow{\mathbf{r}}$ and $\overrightarrow{\mathbf{p}}$ are in the $x y$-plane

The intent of choosing the direction of the angular momentum to be perpendicular to the plane containing $\overrightarrow{\mathbf{r}}$ and $\overrightarrow{\mathbf{p}}$ is similar to choosing the direction of torque to be perpendicular to the plane of $\overrightarrow{\mathbf{r}}$ and $\overrightarrow{\mathbf{F}}$, as discussed in Fixed-Axis Rotation. The magnitude of the angular momentum is found from the definition of the crossproduct,

$$
l=r p \sin \theta
$$

where $\theta$ is the angle between $\overrightarrow{\mathbf{r}}$ and $\overrightarrow{\mathbf{p}}$. The units of angular momentum are $\mathrm{kg} \cdot \mathrm{m}^{2} / \mathrm{s}$.

As with the definition of torque, we can define a lever $\operatorname{arm} r_{\perp}$ that is the perpendicular distance from the momentum vector $\overrightarrow{\mathbf{p}}$ to the origin, $r_{\perp}=r \sin \theta$. With this definition, the magnitude of the angular momentum becomes

$$
l=r_{\perp} p=r_{\perp} m v
$$

We see that if the direction of $\overrightarrow{\mathbf{p}}$ is such that it passes through the origin, then $\theta=0$, and the angular momentum is zero because the lever arm is zero. In this respect, the magnitude of the angular momentum depends on the choice of origin.

If we take the time derivative of the angular momentum, we arrive at an expression for the torque on the particle:

$$
\frac{d \overrightarrow{\mathbf{l}}}{d t}=\frac{d \overrightarrow{\mathbf{r}}}{d t} \times \overrightarrow{\mathbf{p}}+\overrightarrow{\mathbf{r}} \times \frac{d \overrightarrow{\mathbf{p}}}{d t}=\overrightarrow{\mathbf{v}} \times m \overrightarrow{\mathbf{v}}+\overrightarrow{\mathbf{r}} \times \frac{d \overrightarrow{\mathbf{p}}}{d t}=\overrightarrow{\mathbf{r}} \times \frac{d \overrightarrow{\mathbf{p}}}{d t}
$$

Here we have used the definition of $\overrightarrow{\mathbf{p}}$ and the fact that a vector crossed into itself is zero. From Newton's second law, $\frac{d \overrightarrow{\mathbf{p}}}{d t}=\sum \overrightarrow{\mathbf{F}}$, the net force acting on the particle, and the definition of the net torque, we can write

$$
\frac{d \overrightarrow{\mathbf{l}}}{d t}=\sum \vec{\tau}
$$

Note the similarity with the linear result of Newton's second law, $\frac{d \overrightarrow{\mathbf{p}}}{d t}=\sum \overrightarrow{\mathbf{F}}$. The following problem-solving strategy can serve as a guideline for calculating the angular momentum of a particle.

## PROBLEM-SOLVING STRATEGY

## Angular Momentum of a Particle

1. Choose a coordinate system about which the angular momentum is to be calculated.
2. Write down the radius vector to the point particle in unit vector notation.
3. Write the linear momentum vector of the particle in unit vector notation.
4. Take the cross product $\overrightarrow{\mathbf{I}}=\overrightarrow{\mathbf{r}} \times \overrightarrow{\mathbf{p}}$ and use the right-hand rule to establish the direction of the angular momentum vector.
5. See if there is a time dependence in the expression of the angular momentum vector. If there is, then a torque exists about the origin, and use $\frac{d \overrightarrow{\mathbf{1}}}{d t}=\sum \overrightarrow{\boldsymbol{\tau}}$ to calculate the torque. If there is no time dependence in the expression for the angular momentum, then the net torque is zero.

## EXAMPLE 11.4

## Angular Momentum and Torque on a Meteor

A meteor enters Earth's atmosphere (Figure 11.10) and is observed by someone on the ground before it burns up in the atmosphere. The vector $\overrightarrow{\mathbf{r}}=25 \mathrm{~km} \hat{\mathbf{i}}+25 \mathrm{~km} \hat{\mathbf{j}}$ gives the position of the meteor with respect to the observer. At the instant the observer sees the meteor, it has linear momentum $\overrightarrow{\mathbf{p}}=15.0 \mathrm{~kg}(-2.0 \mathrm{~km} / \mathrm{s} \hat{\mathbf{j}})$, and it is accelerating at a constant $2.0 \mathrm{~m} / \mathrm{s}^{2}(-\hat{\mathbf{j}})$ along its path, which for our purposes can be taken as a straight line. (a) What is the angular momentum of the meteor about the origin, which is at the location of the observer? (b) What is the torque on the meteor about the origin?

## Strategy

We resolve the acceleration into $x$ - and $y$-components and use the kinematic equations to express the velocity as a function of acceleration and time. We insert these expressions into the linear momentum and then calculate the angular momentum using the cross-product. Since the position and momentum vectors are in the $x y$-plane, we expect the angular momentum vector to be along the $z$-axis. To find the torque, we take the time derivative of the angular momentum.

## Solution

The meteor is entering Earth's atmosphere at an angle of $90.0^{\circ}$ below the horizontal, so the components of the acceleration in the $x$ - and $y$-directions are

$$
a_{x}=0, a_{y}=-2.0 \mathrm{~m} / \mathrm{s}^{2}
$$

We write the velocities using the kinematic equations.

$$
v_{x}=0, v_{y}=-2.0 \times 10^{3} \mathrm{~m} / \mathrm{s}-\left(2.0 \mathrm{~m} / \mathrm{s}^{2}\right) t
$$

a. The angular momentum is

$$
\begin{aligned}
\overrightarrow{\mathbf{i}} & =\overrightarrow{\mathbf{r}} \times \overrightarrow{\mathbf{p}}=(25.0 \mathrm{~km} \hat{\mathbf{i}}+25.0 \mathrm{~km} \hat{\mathbf{j}}) \times 15.0 \mathrm{~kg}\left(0 \hat{\mathbf{i}}+v_{y} \hat{\mathbf{j}}\right) \\
& =15.0 \mathrm{~kg}\left[25.0 \mathrm{~km}\left(v_{y}\right) \widehat{\mathbf{k}}\right] \\
& =15.0 \mathrm{~kg}\left[2.50 \times 10^{4} \mathrm{~m}\left(-2.0 \times 10^{3} \mathrm{~m} / \mathrm{s}-\left(2.0 \mathrm{~m} / \mathrm{s}^{2}\right) t\right) \widehat{\mathbf{k}}\right]
\end{aligned}
$$

At $t=0$, the angular momentum of the meteor about the origin is

$$
\overrightarrow{\mathbf{l}}_{0}=15.0 \mathrm{~kg}\left[2.50 \times 10^{4} \mathrm{~m}\left(-2.0 \times 10^{3} \mathrm{~m} / \mathrm{s}\right) \widehat{\mathbf{k}}\right]=7.50 \times 10^{8} \mathrm{~kg} \cdot \mathrm{m}^{2} / \mathrm{s}(-\widehat{\mathbf{k}})
$$

This is the instant that the observer sees the meteor.

b. To find the torque, we take the time derivative of the angular momentum. Taking the time derivative of $\overrightarrow{\mathbf{I}}$ as a function of time, which is the second equation immediately above, we have

$$
\frac{d \overrightarrow{\mathbf{l}}}{d t}=-15.0 \mathrm{~kg}\left(2.50 \times 10^{4} \mathrm{~m}\right)\left(2.0 \mathrm{~m} / \mathrm{s}^{2}\right) \widehat{\mathbf{k}}
$$

Then, since $\frac{d \overrightarrow{\mathbf{1}}}{d t}=\sum \overrightarrow{\boldsymbol{\tau}}$, we have

$$
\sum \vec{\tau}=-7.5 \times 10^{5} \mathrm{~N} \cdot \mathrm{m} \widehat{\mathbf{k}}
$$

The units of torque are given as newton-meters, not to be confused with joules. As a check, we note that the lever arm is the $x$-component of the vector $\overrightarrow{\mathbf{r}}$ in Figure 11.10 since it is perpendicular to the force acting on the meteor, which is along its path. By Newton's second law, this force is

$$
\overrightarrow{\mathbf{F}}=m a(-\widehat{\mathbf{j}})=15.0 \mathrm{~kg}\left(2.0 \mathrm{~m} / \mathrm{s}^{2}\right)(-\widehat{\mathbf{j}})=30.0 \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s}^{2}(-\widehat{\mathbf{j}})
$$

The lever arm is

$$
\overrightarrow{\mathbf{r}}_{\perp}=2.5 \times 10^{4} \mathrm{~m} \hat{\mathbf{i}}
$$

Thus, the torque is

$$
\begin{aligned}
\sum \overrightarrow{\boldsymbol{\tau}}=\overrightarrow{\mathbf{r}}_{\perp} \times \overrightarrow{\mathbf{F}} & =\left(2.5 \times 10^{4} \mathrm{~m} \hat{\mathbf{i}}\right) \times\left(-30.0 \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s}^{2} \widehat{\mathbf{j}}\right) \\
& =7.5 \times 10^{5} \mathrm{~N} \cdot \mathrm{m}(-\widehat{\mathbf{k}})
\end{aligned}
$$

## Significance

Since the meteor is accelerating downward toward Earth, its radius and velocity vector are changing. Therefore, since $\overrightarrow{\mathbf{I}}=\overrightarrow{\mathbf{r}} \times \overrightarrow{\mathbf{p}}$, the angular momentum is changing as a function of time. The torque on the meteor about the origin, however, is constant, because the lever arm $\overrightarrow{\mathbf{r}}_{\perp}$ and the force on the meteor are constants. This example is important in that it illustrates that the angular momentum depends on the choice of origin about which it is calculated. The methods used in this example are also important in developing angular momentum for a system of particles and for a rigid body.

## Angular Momentum of a System of Particles

The angular momentum of a system of particles is important in many scientific disciplines, one being astronomy. Consider a spiral galaxy, a rotating island of stars like our own Milky Way. The individual stars can be treated as point particles, each of which has its own angular momentum. The vector sum of the individual angular momenta give the total angular momentum of the galaxy. In this section, we develop the tools with which we can calculate the total angular momentum of a system of particles.

In the preceding section, we introduced the angular momentum of a single particle about a designated origin. The expression for this angular momentum is $\overrightarrow{\mathbf{l}}=\overrightarrow{\mathbf{r}} \times \overrightarrow{\mathbf{p}}$, where the vector $\overrightarrow{\mathbf{r}}$ is from the origin to the particle, and $\overrightarrow{\mathbf{p}}$ is the particle's linear momentum. If we have a system of $N$ particles, each with position vector from the origin given by $\overrightarrow{\mathbf{r}}_{i}$ and each having momentum $\overrightarrow{\mathbf{p}}_{i}$, then the total angular momentum of the system of particles about the origin is the vector sum of the individual angular momenta about the origin. That is,

$$
\overrightarrow{\mathbf{L}}=\overrightarrow{\mathbf{l}}_{1}+\overrightarrow{\mathbf{l}}_{2}+\cdots+\overrightarrow{\mathbf{l}}_{N}
$$

Similarly, if particle $i$ is subject to a net torque $\vec{\tau}_{i}$ about the origin, then we can find the net torque about the origin due to the system of particles by differentiating Equation 11.7:

$$
\frac{d \overrightarrow{\mathbf{L}}}{d t}=\sum_{i} \frac{d \overrightarrow{\mathbf{l}}_{i}}{d t}=\sum_{i} \overrightarrow{\boldsymbol{\tau}}_{i}
$$

The sum of the individual torques produces a net external torque on the system, which we designate $\sum \overrightarrow{\boldsymbol{\tau}}$. Thus,

$$
\frac{d \overrightarrow{\mathbf{L}}}{d t}=\sum \vec{\tau}
$$

Equation 11.8 states that the rate of change of the total angular momentum of a system is equal to the net external torque acting on the system when both quantities are measured with respect to a given origin. Equation 11.8 can be applied to any system that has net angular momentum, including rigid bodies, as discussed in the next section.

## Angular Momentum of Three Particles

Referring to Figure 11.11(a), determine the total angular momentum due to the three particles about the origin. (b) What is the rate of change of the angular momentum?

## Strategy

Write down the position and momentum vectors for the three particles. Calculate the individual angular momenta and add them as vectors to find the total angular momentum. Then do the same for the torques.

## Solution

a. Particle 1: $\overrightarrow{\mathbf{r}}_{1}=-2.0 \mathrm{~m} \hat{\mathbf{i}}+1.0 \mathrm{~m} \hat{\mathbf{j}}, \overrightarrow{\mathbf{p}}_{1}=2.0 \mathrm{~kg}(4.0 \mathrm{~m} / \mathrm{s} \hat{\mathbf{j}})=8.0 \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s} \hat{\mathbf{j}}$,

$$
\overrightarrow{\mathbf{l}}_{1}=\overrightarrow{\mathbf{r}}_{1} \times \overrightarrow{\mathbf{p}}_{1}=-16.0 \mathrm{~kg} \cdot \mathrm{m}^{2} / / \mathrm{s} \hat{\mathbf{k}}
$$

Particle 2: $\overrightarrow{\mathbf{r}}_{2}=4.0 \mathrm{~m} \hat{\mathbf{i}}+1.0 \mathrm{~m} \hat{\mathbf{j}}, \quad \overrightarrow{\mathbf{p}}_{2}=4.0 \mathrm{~kg}(5.0 \mathrm{~m} / \mathrm{s} \hat{\mathbf{i}})=20.0 \mathrm{~kg} \cdot \mathrm{m} / \hat{\mathbf{s}}$,

$$
\overrightarrow{\mathbf{l}}_{2}=\overrightarrow{\mathbf{r}}_{2} \times \overrightarrow{\mathbf{p}}_{2}=-20.0 \mathrm{~kg} \cdot \mathrm{m}^{2} / \widehat{\mathbf{s}}
$$

Particle 3: $\overrightarrow{\mathbf{r}}_{3}=2.0 \mathrm{~m} \hat{\mathbf{i}}-2.0 \mathrm{~m} \hat{\mathbf{j}}, \overrightarrow{\mathbf{p}}_{3}=1.0 \mathrm{~kg}(3.0 \mathrm{~m} / \mathrm{s} \hat{\mathbf{i}})=3.0 \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s} \hat{\mathbf{i}}$,

$$
\overrightarrow{\mathbf{i}}_{3}=\overrightarrow{\mathbf{r}}_{3} \times \overrightarrow{\mathbf{p}}_{3}=6.0 \mathrm{~kg} \cdot \mathrm{m}^{2} / \mathrm{s} \hat{\mathbf{k}}
$$

We add the individual angular momenta to find the total about the origin:

$$
\overrightarrow{\mathbf{l}}_{T}=\overrightarrow{\mathbf{l}}_{1}+\overrightarrow{\mathbf{l}}_{2}+\overrightarrow{\mathbf{l}}_{3}=-30 \mathrm{~kg} \cdot \mathrm{m}^{2} / \mathrm{s} \widehat{\mathbf{k}}
$$

b. The individual forces and lever arms are

$$
\begin{aligned}
& \overrightarrow{\mathbf{r}}_{1 \perp}=1.0 \mathrm{~m} \hat{\mathbf{j}}, \quad \overrightarrow{\mathbf{F}}_{1}=-6.0 \mathrm{Ni}, \quad \vec{\tau}_{1}=6.0 \mathrm{~N} \cdot \mathbf{m} \hat{\mathbf{k}} \\
& \overrightarrow{\mathbf{r}}_{2 \perp}=4.0 \mathrm{~m} \hat{\mathbf{i}}, \quad \overrightarrow{\mathbf{F}}_{2}=10.0 \mathrm{~N} \hat{\mathbf{j}}, \quad \vec{\tau}_{2}=40.0 \mathrm{~N} \cdot \mathrm{m} \hat{\mathbf{k}} \\
& \overrightarrow{\mathbf{r}}_{3 \perp}=2.0 \mathrm{~m} \hat{\mathbf{i}}, \quad \overrightarrow{\mathbf{F}}_{3}=-8.0 \mathrm{~N} \hat{\mathbf{j}}, \quad \vec{\tau}_{3}=-16.0 \mathrm{~N} \cdot \mathrm{m} \hat{\mathbf{k}}
\end{aligned}
$$

Therefore:

$$
\sum_{i} \overrightarrow{\boldsymbol{\tau}}_{i}=\overrightarrow{\boldsymbol{\tau}}_{1}+\overrightarrow{\boldsymbol{\tau}}_{2}+\overrightarrow{\boldsymbol{\tau}}_{3}=30 \mathrm{~N} \cdot \mathrm{m} \widehat{\mathbf{k}}
$$

## Significance

This example illustrates the superposition principle for angular momentum and torque of a system of particles. Care must be taken when evaluating the radius vectors $\overrightarrow{\mathbf{r}}_{i}$ of the particles to calculate the angular momenta, and the lever arms, $\overrightarrow{\mathbf{r}}_{i \perp}$ to calculate the torques, as they are completely different quantities.

## Angular Momentum of a Rigid Body

We have investigated the angular momentum of a single particle, which we generalized to a system of particles. Now we can use the principles discussed in the previous section to develop the concept of the angular momentum of a rigid body. Celestial objects such as planets have angular momentum due to their spin and orbits around stars. In engineering, anything that rotates about an axis carries angular momentum, such as flywheels, propellers, and rotating parts in engines. Knowledge of the angular momenta of these objects is crucial to the design of the system in which they are a part.

To develop the angular momentum of a rigid body, we model a rigid body as being made up of small mass segments, $\Delta m_{i}$. In Figure 11.12, a rigid body is constrained to rotate about the $z$-axis with angular velocity $\omega$. All mass segments that make up the rigid body undergo circular motion about the $z$-axis with the same angular velocity. Part (a) of the figure shows mass segment $\Delta m_{i}$ with position vector $\overrightarrow{\mathbf{r}}_{i}$ from the origin and radius $R_{i}$ to the $z$-axis. The magnitude of its tangential velocity is $v_{i}=R_{i} \omega$. Because the vectors $\overrightarrow{\mathbf{v}}_{i}$ and $\overrightarrow{\mathbf{r}}_{i}$ are perpendicular to each other, the magnitude of the angular momentum of this mass segment is

$$
l_{i}=r_{i}\left(\Delta m v_{i}\right) \sin 90^{\circ}
$$

Using the right-hand rule, the angular momentum vector points in the direction shown in part (b). The sum of the angular momenta of all the mass segments contains components both along and perpendicular to the axis of rotation. Every mass segment has a perpendicular component of the angular momentum that will be cancelled by the perpendicular component of an identical mass segment on the opposite side of the rigid body, because it is cylindrically symmetric. Thus, the component along the axis of rotation is the only component that gives a nonzero value when summed over all the mass segments. From part (b), the component of $\overrightarrow{\mathbf{l}}_{i}$ along the axis of rotation is

$$
\begin{aligned}
\left(l_{i}\right)_{z} & =l_{i} \sin \theta_{i}=\left(r_{i} \Delta m_{i} v_{i}\right) \sin \theta_{i} \\
& =\left(r_{i} \sin \theta_{i}\right)\left(\Delta m_{i} v_{i}\right)=R_{i} \Delta m_{i} v_{i}
\end{aligned}
$$

The net angular momentum of the rigid body along the axis of rotation is

$$
L=\sum_{i}\left(\overrightarrow{\mathbf{l}}_{i}\right)_{z}=\sum_{i} R_{i} \Delta m_{i} v_{i}=\sum_{i} R_{i} \Delta m_{i}\left(R_{i} \omega\right)=\omega \sum_{i} \Delta m_{i}\left(\boldsymbol{R}_{i}\right)^{2}
$$

The summation $\sum_{i} \Delta m_{i}\left(R_{i}\right)^{2}$ is simply the moment of inertia $I$ of the rigid body about the axis of rotation. For a thin hoop rotating about an axis perpendicular to the plane of the hoop, all of the $R_{i}$ 's are equal to $R$ so the summation reduces to $R^{2} \sum_{i} \Delta m_{i}=m R^{2}$, which is the moment of inertia for a thin hoop found in Figure 10.20. Thus, the magnitude of the angular momentum along the axis of rotation of a rigid body rotating with angular velocity $\omega$ about the axis is

$$
L=I \omega
$$

This equation is analogous to the magnitude of the linear momentum $p=m v$. The direction of the angular momentum vector is directed along the axis of rotation given by the right-hand rule.

## EXAMPLE 11.6

## Angular Momentum of a Robot Arm

A robot arm on a Mars rover like Curiosity shown in Figure 11.8 is $1.0 \mathrm{~m}$ long and has forceps at the free end to pick up rocks. The mass of the arm is $2.0 \mathrm{~kg}$ and the mass of the forceps is $1.0 \mathrm{~kg}$. See Figure 11.13. The robot arm and forceps move from rest to $\omega=0.1 \pi \mathrm{rad} / \mathrm{s}$ in $0.1 \mathrm{~s}$. It rotates down and picks up a Mars rock that has mass $1.5 \mathrm{~kg}$. The axis of rotation is the point where the robot arm connects to the rover. (a) What is the angular momentum of the robot arm by itself about the axis of rotation after $0.1 \mathrm{~s}$ when the arm has stopped accelerating? (b) What is the angular momentum of the robot arm when it has the Mars rock in its forceps and is rotating upwards? (c) When the arm does not have a rock in the forceps, what is the torque about the point where the arm connects to the rover when it is accelerating from rest to its final angular velocity?

## Strategy

We use Equation 11.9 to find angular momentum in the various configurations. When the arm is rotating downward, the right-hand rule gives the angular momentum vector directed out of the page, which we will call the positive $z$-direction. When the arm is rotating upward, the right-hand rule gives the direction of the angular momentum vector into the page or in the negative $z$-direction. The moment of inertia is the sum of the individual moments of inertia. The arm can be approximated with a solid rod, and the forceps and Mars rock can be approximated as point masses located at a distance of $1 \mathrm{~m}$ from the origin. For part (c), we use Newton's
second law of motion for rotation to find the torque on the robot arm.

## Solution

a. Writing down the individual moments of inertia, we have

Robot arm: $I_{\mathrm{R}}=\frac{1}{3} m_{\mathrm{R}} r^{2}=\frac{1}{3}(2.00 \mathrm{~kg})(1.00 \mathrm{~m})^{2}=\frac{2}{3} \mathrm{~kg} \cdot \mathrm{m}^{2}$.

Forceps: $I_{\mathrm{F}}=m_{\mathrm{F}} r^{2}=(1.0 \mathrm{~kg})(1.0 \mathrm{~m})^{2}=1.0 \mathrm{~kg} \cdot \mathrm{m}^{2}$.

Mars rock: $I_{\mathrm{MR}}=m_{\mathrm{MR}} r^{2}=(1.5 \mathrm{~kg})(1.0 \mathrm{~m})^{2}=1.5 \mathrm{~kg} \cdot \mathrm{m}^{2}$.

Therefore, without the Mars rock, the total moment of inertia is

$$
I_{\text {Total }}=I_{\mathrm{R}}+I_{\mathrm{F}}=1.67 \mathrm{~kg} \cdot \mathrm{m}^{2}
$$

and the magnitude of the angular momentum is

$$
L=I \omega=1.67 \mathrm{~kg} \cdot \mathrm{m}^{2}(0.1 \pi \mathrm{rad} / \mathrm{s})=0.17 \pi \mathrm{kg} \cdot \mathrm{m}^{2} / \mathrm{s}
$$

The angular momentum vector is directed out of the page in the $\hat{\mathbf{k}}$ direction since the robot arm is rotating counterclockwise.

b. We must include the Mars rock in the calculation of the moment of inertia, so we have

$$
I_{\text {Total }}=I_{\mathrm{R}}+I_{\mathrm{F}}+I_{\mathrm{MR}}=3.17 \mathrm{~kg} \cdot \mathrm{m}^{2}
$$

and

$$
L=I \omega=3.17 \mathrm{~kg} \cdot \mathrm{m}^{2}(0.1 \pi \mathrm{rad} / \mathrm{s})=0.32 \pi \mathrm{kg} \cdot \mathrm{m}^{2} / \mathrm{s}
$$

Now the angular momentum vector is directed into the page in the $-\widehat{\mathbf{k}}$ direction, by the right-hand rule, since the robot arm is now rotating clockwise.

c. We find the torque when the arm does not have the rock by taking the derivative of the angular momentum using Equation $11.8 \frac{d \overrightarrow{\mathbf{L}}}{d t}=\sum \vec{\tau}$. But since $L=I \omega$, and understanding that the direction of the angular momentum and torque vectors are along the axis of rotation, we can suppress the vector notation and find

$$
\frac{d L}{d t}=\frac{d(I \omega)}{d t}=I \frac{d \omega}{d t}=I \alpha=\sum \tau
$$

which is Newton's second law for rotation. Since $\alpha=\frac{0.1 \pi \mathrm{rad} / \mathrm{s}}{0.1 \mathrm{~s}}=\pi \mathrm{rad} / \mathrm{s}^{2}$, we can calculate the net torque:

$$
\sum \tau=I \alpha=1.67 \mathrm{~kg} \cdot \mathrm{m}^{2}\left(\pi \mathrm{rad} / \mathrm{s}^{2}\right)=1.67 \pi \mathrm{N} \cdot \mathrm{m}
$$

## Significance

The angular momentum in (a) is less than that of (b) due to the fact that the moment of inertia in (b) is greater than (a), while the angular velocity is the same.

### 11.3 Conservation of Angular Momentum

So far, we have looked at the angular momentum of systems consisting of point particles and rigid bodies. We have also analyzed the torques involved, using the expression that relates the external net torque to the change in angular momentum, Equation 11.8. Examples of systems that obey this equation include a freely spinning bicycle tire that slows over time due to torque arising from friction, or the slowing of Earth's rotation over millions of years due to frictional forces exerted on tidal deformations.

However, suppose there is no net external torque on the system, $\sum \overrightarrow{\boldsymbol{\tau}}=0$. In this case, Equation 11.8 becomes the law of conservation of angular momentum.

## Law of Conservation of Angular Momentum

The angular momentum of a system of particles around a point in a fixed inertial reference frame is conserved if there is no net external torque around that point:

$$
\frac{d \overrightarrow{\mathbf{L}}}{d t}=0
$$

or

$$
\overrightarrow{\mathbf{L}}=\overrightarrow{\mathbf{l}}_{1}+\overrightarrow{\mathbf{l}}_{2}+\cdots+\overrightarrow{\mathbf{l}}_{N}=\text { constant. }
$$

Note that the total angular momentum $\overrightarrow{\mathbf{L}}$ is conserved. Any of the individual angular momenta can change as long as their sum remains constant. This law is analogous to linear momentum being conserved when the external force on a system is zero.

As an example of conservation of angular momentum, Figure 11.14 shows an ice skater executing a spin. The net torque on her is very close to zero because there is relatively little friction between her skates and the ice. Also, the friction is exerted very close to the pivot point. Both $|\overrightarrow{\mathbf{F}}|$ and $|\overrightarrow{\mathbf{r}}|$ are small, so $|\overrightarrow{\boldsymbol{\tau}}|$ is negligible.

Consequently, she can spin for quite some time. She can also increase her rate of spin by pulling her arms and legs in. Why does pulling her arms and legs in increase her rate of spin? The answer is that her angular momentum is constant, so that

$$
L^{\prime}=L
$$

or

$$
I^{\prime} \omega^{\prime}=I \omega
$$

where the primed quantities refer to conditions after she has pulled in her arms and reduced her moment of inertia. Because $I^{\prime}$ is smaller, the angular velocity $\omega^{\prime}$ must increase to keep the angular momentum constant.

It is interesting to see how the rotational kinetic energy of the skater changes when she pulls her arms in. Her initial rotational energy is

$$
K_{\text {Rot }}=\frac{1}{2} I \omega^{2}
$$

whereas her final rotational energy is

$$
K_{\text {Rot }}^{\prime}=\frac{1}{2} I^{\prime}\left(\omega^{\prime}\right)^{2}
$$

Since $I^{\prime} \omega^{\prime}=I \omega$, we can substitute for $\omega^{\prime}$ and find

$$
K_{\text {Rot }}^{\prime}=\frac{1}{2} I^{\prime}\left(\omega^{\prime}\right)^{2}=\frac{1}{2} I^{\prime}\left(\frac{I}{I^{\prime}} \omega\right)^{2}=\frac{1}{2} I \omega^{2}\left(\frac{I}{I^{\prime}}\right)=K_{\text {Rot }}\left(\frac{I}{I^{\prime}}\right)
$$

Because her moment of inertia has decreased, $I^{\prime}<I$, her final rotational kinetic energy has increased. The source of this additional rotational kinetic energy is the work required to pull her arms inward. Note that the skater's arms do not move in a perfect circle-they spiral inward. This work causes an increase in the rotational kinetic energy, while her angular momentum remains constant. Since she is in a frictionless environment, no energy escapes the system. Thus, if she were to extend her arms to their original positions, she would rotate at her original angular velocity and her kinetic energy would return to its original value.

The solar system is another example of how conservation of angular momentum works in our universe. Our solar system was born from a huge cloud of gas and dust that initially had rotational energy. Gravitational forces caused the cloud to contract, and the rotation rate increased as a result of conservation of angular momentum (Figure 11.15).

## Coupled Flywheels

A flywheel rotates without friction at an angular velocity $\omega_{0}=600 \mathrm{rev} / \mathrm{min}$ on a frictionless, vertical shaft of negligible rotational inertia. A second flywheel, which is at rest and has a moment of inertia three times that of the rotating flywheel, is dropped onto it (Figure 11.16). Because friction exists between the surfaces, the flywheels very quickly reach the same rotational velocity, after which they spin together. (a) Use the law of conservation of angular momentum to determine the angular velocity $\omega$ of the combination. (b) What fraction of the initial kinetic energy is lost in the coupling of the flywheels?

## Strategy

Part (a) is straightforward to solve for the angular velocity of the coupled system. We use the result of (a) to compare the initial and final kinetic energies of the system in part (b).

## Solution

a. No external torques act on the system. The force due to friction produces an internal torque, which does not affect the angular momentum of the system. Therefore conservation of angular momentum gives

$$
\begin{aligned}
& I_{0} \omega_{0}=\left(I_{0}+3 I_{0}\right) \omega \\
& \omega=\frac{1}{4} \omega_{0}=150 \mathrm{rev} / \mathrm{min}=15.7 \mathrm{rad} / \mathrm{s}
\end{aligned}
$$

b. Before contact, only one flywheel is rotating. The rotational kinetic energy of this flywheel is the initial rotational kinetic energy of the system, $\frac{1}{2} I_{0} \omega_{0}^{2}$. The final kinetic energy

is $\frac{1}{2}\left(4 I_{0}\right) \omega^{2}=\frac{1}{2}\left(4 I_{0}\right)\left(\frac{\omega_{0}}{4}\right)^{2}=\frac{1}{8} I_{0} \omega_{0}^{2}$.

Therefore, the ratio of the final kinetic energy to the initial kinetic energy is

$$
\frac{\frac{1}{8} I_{0} \omega_{0}^{2}}{\frac{1}{2} I_{0} \omega_{0}^{2}}=\frac{1}{4}
$$

Thus, $3 / 4$ of the initial kinetic energy is lost to the coupling of the two flywheels.

## Significance

Since the rotational inertia of the system increased, the angular velocity decreased, as expected from the law of conservation of angular momentum. In this example, we see that the final kinetic energy of the system has decreased, as energy is lost to the coupling of the flywheels. Compare this to the example of the skater in Figure 11.14 doing work to bring her arms inward and adding rotational kinetic energy.

## EXAMPLE 11.8

## Dismount from a High Bar

An 80.0-kg gymnast dismounts from a high bar. He starts the dismount at full extension, then tucks to complete a number of revolutions before landing. His moment of inertia when fully extended can be approximated as a rod of length $1.8 \mathrm{~m}$ and when in the tuck a rod of half that length. If his rotation rate at full extension is $1.0 \mathrm{rev} / \mathrm{s}$ and he enters the tuck when his center of mass is at $3.0 \mathrm{~m}$ height moving horizontally to
the floor, how many revolutions can he execute if he comes out of the tuck at $1.8 \mathrm{~m}$ height? See Figure 11.17.

## Strategy

Using conservation of angular momentum, we can find his rotation rate when in the tuck. Using the equations of kinematics, we can find the time interval from a height of $3.0 \mathrm{~m}$ to $1.8 \mathrm{~m}$. Since he is moving horizontally with respect to the ground, the equations of free fall simplify. This will allow the number of revolutions that can be executed to be calculated. Since we are using a ratio, we can keep the units as rev/s and don't need to convert to radians/s.

## Solution

The moment of inertia at full extension is $I_{0}=\frac{1}{12} m L^{2}=\frac{1}{12} 80.0 \mathrm{~kg}(1.8 \mathrm{~m})^{2}=21.6 \mathrm{~kg} \cdot \mathrm{m}^{2}$.

The moment of inertia in the tuck is $I_{\mathrm{f}}=\frac{1}{12} m L_{\mathrm{f}}^{2}=\frac{1}{12} 80.0 \mathrm{~kg}(0.9 \mathrm{~m})^{2}=5.4 \mathrm{~kg} \cdot \mathrm{m}^{2}$.

Conservation of angular momentum: $I_{\mathrm{f}} \omega_{\mathrm{f}}=I_{0} \omega_{0} \Rightarrow \omega_{\mathrm{f}}=\frac{I_{0} \omega_{0}}{I_{\mathrm{f}}}=\frac{21.6 \mathrm{~kg} \cdot \mathrm{m}^{2}(1.0 \mathrm{rev} / \mathrm{s})}{5.4 \mathrm{~kg} \cdot \mathrm{m}^{2}}=4.0 \mathrm{rev} / \mathrm{s}$.

Time interval in the tuck: $t=\sqrt{\frac{2 h}{g}}=\sqrt{\frac{2(3.0-1.8) \mathrm{m}}{9.8 \mathrm{~m} / \mathrm{s}}}=0.5 \mathrm{~s}$.

In $0.5 \mathrm{~s}$, he will be able to execute two revolutions at $4.0 \mathrm{rev} / \mathrm{s}$.

## Significance

Note that the number of revolutions he can complete will depend on how long he is in the air. In the problem, he is exiting the high bar horizontally to the ground. He could also exit at an angle with respect to the ground, giving him more or less time in the air depending on the angle, positive or negative, with respect to the ground. Gymnasts must take this into account when they are executing their dismounts.

## EXAMPLE 11.9

## Conservation of Angular Momentum of a Collision

A bullet of mass $m=2.0 \mathrm{~g}$ is moving horizontally with a speed of $500.0 \mathrm{~m} / \mathrm{s}$. The bullet strikes and becomes embedded in the edge of a solid disk of mass $M=3.2 \mathrm{~kg}$ and radius $R=0.5 \mathrm{~m}$. The cylinder is free to rotate
around its axis and is initially at rest (Figure 11.18). What is the angular velocity of the disk immediately after the bullet is embedded?

## Strategy

For the system of the bullet and the cylinder, no external torque acts along the vertical axis through the center of the disk. Thus, the angular momentum along this axis is conserved. The initial angular momentum of the bullet is $m v R$, which is taken about the rotational axis of the disk the moment before the collision. The initial angular momentum of the cylinder is zero. Thus, the net angular momentum of the system is $m v \boldsymbol{R}$. Since angular momentum is conserved, the initial angular momentum of the system is equal to the angular momentum of the bullet embedded in the disk immediately after impact.

## Solution

The initial angular momentum of the system is

$$
L_{i}=m v R
$$

The moment of inertia of the system with the bullet embedded in the disk is

$$
I=m R^{2}+\frac{1}{2} M R^{2}=\left(m+\frac{M}{2}\right) R^{2}
$$

The final angular momentum of the system is

$$
L_{f}=I \omega_{f}
$$

Thus, by conservation of angular momentum, $L_{i}=L_{f}$ and

$$
m v R=\left(m+\frac{M}{2}\right) R^{2} \omega_{f}
$$

Solving for $\omega_{f}$,

$$
\omega_{f}=\frac{m v R}{(m+M / 2) R^{2}}=\frac{\left(2.0 \times 10^{-3} \mathrm{~kg}\right)(500.0 \mathrm{~m} / \mathrm{s})}{\left(2.0 \times 10^{-3} \mathrm{~kg}+1.6 \mathrm{~kg}\right)(0.50 \mathrm{~m})}=1.2 \mathrm{rad} / \mathrm{s}
$$

## Significance

The system is composed of both a point particle and a rigid body. Care must be taken when formulating the angular momentum before and after the collision. Just before impact the angular momentum of the bullet is taken about the rotational axis of the disk.

### 11.4 Precession of a Gyroscope

Figure 11.19 shows a gyroscope, defined as a spinning disk in which the axis of rotation is free to assume any orientation. When spinning, the orientation of the spin axis is unaffected by the orientation of the body that encloses it. The body or vehicle enclosing the gyroscope can be moved from place to place and the orientation of the spin axis will remain the same. This makes gyroscopes very useful in navigation, especially where magnetic compasses can't be used, such as in piloted and unpiloted spacecrafts, intercontinental ballistic missiles, unmanned aerial vehicles, and satellites like the Hubble Space Telescope.

We illustrate the precession of a gyroscope with an example of a top in the next two figures. If the top is placed on a flat surface near the surface of Earth at an angle to the vertical and is not spinning, it will fall over, due to the force of gravity producing a torque acting on its center of mass. This is shown in Figure 11.20(a). However, if the top is spinning on its axis, rather than topple over due to this torque, it precesses about the vertical, shown in part (b) of the figure. This is due to the torque on the center of mass, which provides the change in angular momentum.

Figure 11.21 shows the forces acting on a spinning top. The torque produced is perpendicular to the angular momentum vector. This changes the direction of the angular momentum vector $\overrightarrow{\mathbf{L}}$ according to $d \overrightarrow{\mathbf{L}}=\overrightarrow{\boldsymbol{\tau}} d t$, but
not its magnitude. The top precesses around a vertical axis, since the torque is always horizontal and perpendicular to $\mathbf{\mathbf { L }}$. If the top is not spinning, it acquires angular momentum in the direction of the torque, and it rotates around a horizontal axis, falling over just as we would expect.

We can experience this phenomenon first hand by holding a spinning bicycle wheel and trying to rotate it about an axis perpendicular to the spin axis. As shown in Figure 11.22, the person applies forces perpendicular to the spin axis in an attempt to rotate the wheel, but instead, the wheel axis starts to change direction to her left due to the applied torque.

When forces are applied to the axle as shown, the wheel rotates toward the person.

We all know how easy it is for a bicycle to tip over when sitting on it at rest. But when riding the bicycle at a good pace, tipping it over involves changing the angular momentum vector of the spinning wheels.

Also, when a spinning disk is put in a box such as a Blu-Ray player, try to move it. It is easy to translate the box in a given direction but difficult to rotate it about an axis perpendicular to the axis of the spinning disk, since we are putting a torque on the box that will cause the angular momentum vector of the spinning disk to precess.

We can calculate the precession rate of the top in Figure 11.21. From Figure 11.21, we see that the magnitude of the torque is

$$
\tau=r M g \sin \theta
$$

Thus,

$$
d L=r M g \sin \theta d t
$$

The angle the top precesses through in time $d t$ is

$$
d \phi=\frac{d L}{L \sin \theta}=\frac{r M g \sin \theta}{L \sin \theta} d t=\frac{r M g}{L} d t
$$

The precession angular velocity is $\omega_{P}=\frac{d \phi}{d t}$ and from this equation we see that

$$
\begin{gather*}
\omega_{P}=\frac{r M g}{L} . \text { or, since } L=I \omega \\
\omega_{P}=\frac{r M g}{I \omega}
\end{gather*}
$$

In this derivation, we assumed that $\omega_{P} \ll \omega$, that is, that the precession angular velocity is much less than the
angular velocity of the gyroscope disk. The precession angular velocity adds a small component to the angular momentum along the $z$-axis. This is seen in a slight bob up and down as the gyroscope precesses, referred to as nutation.

Earth itself acts like a gigantic gyroscope. Its angular momentum is along its axis and currently points at Polaris, the North Star. But Earth is slowly precessing (once in about 26,000 years) due to the torque of the Sun and the Moon on its nonspherical shape.

## Period of Precession

A gyroscope spins with its tip on the ground and is spinning with negligible frictional resistance. The disk of the gyroscope has mass $0.3 \mathrm{~kg}$ and is spinning at $20 \mathrm{rev} / \mathrm{s}$. Its center of mass is $5.0 \mathrm{~cm}$ from the pivot and the radius of the disk is $5.0 \mathrm{~cm}$. What is the precessional period of the gyroscope?

## Strategy

We use Equation 11.12 to find the precessional angular velocity of the gyroscope. This allows us to find the period of precession.

## Solution

The moment of inertia of the disk is

$$
I=\frac{1}{2} m r^{2}=\frac{1}{2}(0.30 \mathrm{~kg})(0.05 \mathrm{~m})^{2}=3.75 \times 10^{-4} \mathrm{~kg} \cdot \mathrm{m}^{2}
$$

The angular velocity of the disk is

$$
20.0 \mathrm{rev} / \mathrm{s}=20.0(2 \pi) \mathrm{rad} / \mathrm{s}=125.66 \mathrm{rad} / \mathrm{s}
$$

We can now substitute in Equation 11.12. The precessional angular velocity is

$$
\omega_{P}=\frac{r M g}{I \omega}=\frac{(0.05 \mathrm{~m})(0.3 \mathrm{~kg})\left(9.8 \mathrm{~m} / \mathrm{s}^{2}\right)}{\left(3.75 \times 10^{-4} \mathrm{~kg} \cdot \mathrm{m}^{2}\right)(125.66 \mathrm{rad} / \mathrm{s})}=3.12 \mathrm{rad} / \mathrm{s}
$$

The precessional period of the gyroscope is

$$
T_{P}=\frac{2 \pi}{3.12 \mathrm{rad} / \mathrm{s}}=2.0 \mathrm{~s}
$$

## Significance

The precessional angular frequency of the gyroscope, $3.12 \mathrm{rad} / \mathrm{s}$, or about $0.5 \mathrm{rev} / \mathrm{s}$, is much less than the angular velocity $20 \mathrm{rev} / \mathrm{s}$ of the gyroscope disk. Therefore, we don't expect a large component of the angular momentum to arise due to precession, and Equation 11.12 is a good approximation of the precessional angular velocity.

