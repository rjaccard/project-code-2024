# CHAPTER 10 Fixed-Axis Rotation 

INTRODUCTION In previous chapters, we described motion (kinematics) and how to change motion (dynamics), and we defined important concepts such as energy for objects that can be considered as point masses. Point masses, by definition, have no shape and so can only undergo translational motion. However, we know from everyday life that rotational motion is also very important and that many objects that move have
both translation and rotation. The wind turbines in our chapter opening image are a prime example of how rotational motion impacts our daily lives, as the market for clean energy sources continues to grow.

We begin to address rotational motion in this chapter, starting with fixed-axis rotation. Fixed-axis rotation describes the rotation around a fixed axis of a rigid body; that is, an object that does not deform as it moves. We will show how to apply all the ideas we've developed up to this point about translational motion to an object rotating around a fixed axis. In the next chapter, we extend these ideas to more complex rotational motion, including objects that both rotate and translate, and objects that do not have a fixed rotational axis.

### 10.1 Rotational Variables

So far in this text, we have mainly studied translational motion, including the variables that describe it: displacement, velocity, and acceleration. Now we expand our description of motion to rotation-specifically, rotational motion about a fixed axis. We will find that rotational motion is described by a set of related variables similar to those we used in translational motion.

## Angular Velocity

Uniform circular motion (discussed previously in Motion in Two and Three Dimensions) is motion in a circle at constant speed. Although this is the simplest case of rotational motion, it is very useful for many situations, and we use it here to introduce rotational variables.

In Figure 10.2, we show a particle moving in a circle. The coordinate system is fixed and serves as a frame of reference to define the particle's position. Its position vector from the origin of the circle to the particle sweeps out the angle $\theta$, which increases in the counterclockwise direction as the particle moves along its circular path. The angle $\theta$ is called the angular position of the particle. As the particle moves in its circular path, it also traces an arc length $s$.

The angle is related to the radius of the circle and the arc length by

$$
\theta=\frac{s}{r}
$$

The angle $\theta$, the angular position of the particle along its path, has units of radians (rad). There are $2 \pi$ radians in $360^{\circ}$. Note that the radian measure is a ratio of length measurements, and therefore is a dimensionless quantity. As the particle moves along its circular path, its angular position changes and it undergoes angular displacements $\Delta \theta$.

We can assign vectors to the quantities in Equation 10.1. The angle $\overrightarrow{\boldsymbol{\theta}}$ is a vector out of the page in Figure 10.2. The angular position vector $\overrightarrow{\mathbf{r}}$ and the arc length $\overrightarrow{\mathbf{s}}$ both lie in the plane of the page. These three vectors are related to each other by

$$
\overrightarrow{\mathbf{s}}=\overrightarrow{\boldsymbol{\theta}} \times \overrightarrow{\mathbf{r}}
$$

That is, the arc length is the cross product of the angle vector and the position vector, as shown in Figure 10.3.

The magnitude of the angular velocity, denoted by $\omega$, is the time rate of change of the angle $\theta$ as the particle moves in its circular path. The instantaneous angular velocity is defined as the limit in which $\Delta t \rightarrow 0$ in the average angular velocity $\bar{\omega}=\frac{\Delta \theta}{\Delta t}$ :

$$
\omega=\lim _{\Delta t \rightarrow 0} \frac{\Delta \theta}{\Delta t}=\frac{d \theta}{d t}
$$

where $\theta$ is the angle of rotation (Figure 10.2). The units of angular velocity are radians per second (rad/s). Angular velocity can also be referred to as the rotation rate in radians per second. In many situations, we are given the rotation rate in revolutions/s or cycles/s. To find the angular velocity, we must multiply revolutions/s by $2 \pi$, since there are $2 \pi$ radians in one complete revolution. Since the direction of a positive angle in a circle is counterclockwise, we take counterclockwise rotations as being positive and clockwise rotations as negative.

We can see how angular velocity is related to the tangential speed of the particle by differentiating Equation 10.1 with respect to time. We rewrite Equation 10.1 as

$$
s=r \theta
$$

Taking the derivative with respect to time and noting that the radius $r$ is a constant, we have

$$
\frac{d s}{d t}=\frac{d}{d t}(r \theta)=\theta \frac{d r}{d t}+r \frac{d \theta}{d t}=r \frac{d \theta}{d t}
$$

where $\theta \frac{d r}{d t}=0$. Here $\frac{d s}{d t}$ is just the tangential speed $v_{\mathrm{t}}$ of the particle in Figure 10.2. Thus, by using Equation 10.3 , we arrive at

$$
v_{\mathrm{t}}=r \omega .
$$

That is, the tangential speed of the particle is its angular velocity times the radius of the circle. From Equation 10.4, we see that the tangential speed of the particle increases with its distance from the axis of rotation for a constant angular velocity. This effect is shown in Figure 10.4. Two particles are placed at different radii on a rotating disk with a constant angular velocity. As the disk rotates, the tangential speed increases linearly with the radius from the axis of rotation. In Figure 10.4, we see that $v_{1}=r_{1} \omega_{1}$ and $v_{2}=r_{2} \omega_{2}$. But the disk has a constant angular velocity, so $\omega_{1}=\omega_{2}$. This means $\frac{v_{1}}{r_{1}}=\frac{v_{2}}{r_{2}}$ or $v_{2}=\left(\frac{r_{2}}{r_{1}}\right) v_{1}$. Thus, since $r_{2}>r_{1}, v_{2}>v_{1}$.

Up until now, we have discussed the magnitude of the angular velocity $\omega=d \theta / d t$, which is a scalar quantity-the change in angular position with respect to time. The vector $\overrightarrow{\boldsymbol{\omega}}$ is the vector associated with the angular velocity and points along the axis of rotation. This is useful because when a rigid body is rotating, we want to know both the axis of rotation and the direction that the body is rotating about the axis, clockwise or counterclockwise. The angular velocity $\overrightarrow{\boldsymbol{\omega}}$ gives us this information. The angular velocity $\overrightarrow{\boldsymbol{\omega}}$ has a direction determined by what is called the right-hand rule. The right-hand rule is such that if the fingers of your right hand wrap counterclockwise from the $x$-axis (the direction in which $\theta$ increases) toward the $y$-axis, your thumb points in the direction of the positive $z$-axis (Figure 10.5). An angular velocity $\overrightarrow{\boldsymbol{\omega}}$ that points along the positive $z$-axis therefore corresponds to a counterclockwise rotation, whereas an angular velocity $\overrightarrow{\boldsymbol{\omega}}$ that points along the negative $z$-axis corresponds to a clockwise rotation.

## $\overrightarrow{\boldsymbol{\omega}}$

Similar to Equation 10.2, one can state a cross product relation to the vector of the tangential velocity as stated in Equation 10.4. Therefore, we have

$$
\overrightarrow{\mathbf{v}}=\overrightarrow{\boldsymbol{\omega}} \times \overrightarrow{\mathbf{r}}
$$

That is, the tangential velocity is the cross product of the angular velocity and the position vector, as shown in Figure 10.6. From part (a) of this figure, we see that with the angular velocity in the positive $z$-direction, the rotation in the $x y$-plane is counterclockwise. In part (b), the angular velocity is in the negative $z$-direction, giving a clockwise rotation in the $x y$-plane.

## Rotation of a Flywheel

A flywheel rotates such that it sweeps out an angle at the rate of $\theta=\omega t=(45.0 \mathrm{rad} / \mathrm{s}) t$ radians. The wheel
rotates counterclockwise when viewed in the plane of the page. (a) What is the angular velocity of the flywheel? (b) What direction is the angular velocity? (c) How many radians does the flywheel rotate through in 30 s? (d) What is the tangential speed of a point on the flywheel $10 \mathrm{~cm}$ from the axis of rotation?

## Strategy

The functional form of the angular position of the flywheel is given in the problem as $\theta(t)=\omega t$, so by taking the derivative with respect to time, we can find the angular velocity. We use the right-hand rule to find the angular velocity. To find the angular displacement of the flywheel during $30 \mathrm{~s}$, we seek the angular displacement $\Delta \theta$, where the change in angular position is between 0 and $30 \mathrm{~s}$. To find the tangential speed of a point at a distance from the axis of rotation, we multiply its distance times the angular velocity of the flywheel.

## Solution

a. $\omega=\frac{d \theta}{d t}=45 \mathrm{rad} / \mathrm{s}$. We see that the angular velocity is a constant.

b. By the right-hand rule, we curl the fingers in the direction of rotation, which is counterclockwise in the plane of the page, and the thumb points in the direction of the angular velocity, which is out of the page.
c. $\Delta \theta=\theta(30 \mathrm{~s})-\theta(0 \mathrm{~s})=45.0(30.0 \mathrm{~s})-45.0(0 \mathrm{~s})=1350.0 \mathrm{rad}$.
d. $v_{\mathrm{t}}=r \omega=(0.1 \mathrm{~m})(45.0 \mathrm{rad} / \mathrm{s})=4.5 \mathrm{~m} / \mathrm{s}$.

## Significance

In $30 \mathrm{~s}$, the flywheel has rotated through quite a number of revolutions, about 215 if we divide the angular displacement by $2 \pi$. A massive flywheel can be used to store energy in this way, if the losses due to friction are minimal. Recent research has considered superconducting bearings on which the flywheel rests, with zero energy loss due to friction.

## Angular Acceleration

We have just discussed angular velocity for uniform circular motion, but not all motion is uniform. Envision an ice skater spinning with his arms outstretched-when he pulls his arms inward, his angular velocity increases. Or think about a computer's hard disk slowing to a halt as the angular velocity decreases. We will explore these situations later, but we can already see a need to define an angular acceleration for describing situations where $\omega$ changes. The faster the change in $\omega$, the greater the angular acceleration. We define the instantaneous angular acceleration $\alpha$ as the derivative of angular velocity with respect to time:

$$
\alpha=\lim _{\Delta t \rightarrow 0} \frac{\Delta \omega}{\Delta t}=\frac{d \omega}{d t}=\frac{d^{2} \theta}{d t^{2}}
$$

where we have taken the limit of the average angular acceleration, $\bar{\alpha}=\frac{\Delta \omega}{\Delta t}$ as $\Delta t \rightarrow 0$.

The units of angular acceleration are (rad/s)/s, or rad/s ${ }^{2}$.

In the same way as we defined the vector associated with angular velocity $\overrightarrow{\boldsymbol{\omega}}$, we can define $\overrightarrow{\boldsymbol{\alpha}}$, the vector associated with angular acceleration (Figure 10.7). If the angular velocity is along the positive $z$-axis, as in Figure 10.5 , and $\frac{d \omega}{d t}$ is positive, then the angular acceleration $\overrightarrow{\boldsymbol{\alpha}}$ is positive and points along the $+z$ - axis. Similarly, if the angular velocity $\overrightarrow{\boldsymbol{\omega}}$ is along the positive $z$-axis and $\frac{d \omega}{d t}$ is negative, then the angular acceleration is negative and points along the $-z-$ axis.

We can express the tangential acceleration vector as a cross product of the angular acceleration and the position vector. This expression can be found by taking the time derivative of $\overrightarrow{\mathbf{v}}=\overrightarrow{\boldsymbol{\omega}} \times \overrightarrow{\mathbf{r}}$ and is left as an exercise:

$$
\overrightarrow{\mathbf{a}}=\overrightarrow{\boldsymbol{\alpha}} \times \overrightarrow{\mathbf{r}}
$$

The vector relationships for the angular acceleration and tangential acceleration are shown in Figure 10.8.

(b) The angular acceleration is in the negative $z$-direction and produces a tangential acceleration in the clockwise sense.

We can relate the tangential acceleration of a point on a rotating body at a distance from the axis of rotation in the same way that we related the tangential speed to the angular velocity. If we differentiate Equation 10.4 with respect to time, noting that the radius $r$ is constant, we obtain

$$
a_{\mathrm{t}}=r \alpha
$$

Thus, the tangential acceleration $a_{t}$ is the radius times the angular acceleration. Equation 10.4 and Equation 10.8 are important for the discussion of rolling motion (see Angular Momentum).

Let's apply these ideas to the analysis of a few simple fixed-axis rotation scenarios. Before doing so, we present a problem-solving strategy that can be applied to rotational kinematics: the description of rotational motion.

## PROBLEM-SOLVING STRATEGY

## Rotational Kinematics

1. Examine the situation to determine that rotational kinematics (rotational motion) is involved.
2. Identify exactly what needs to be determined in the problem (identify the unknowns). A sketch of the situation is useful.
3. Make a complete list of what is given or can be inferred from the problem as stated (identify the knowns).
4. Solve the appropriate equation or equations for the quantity to be determined (the unknown). It can be useful to think in terms of a translational analog, because by now you are familiar with the equations of translational motion.
5. Substitute the known values along with their units into the appropriate equation and obtain numerical solutions complete with units. Be sure to use units of radians for angles.
6. Check your answer to see if it is reasonable: Does your answer make sense?

Now let's apply this problem-solving strategy to a few specific examples.

## EXAMPLE 10.2

## A Spinning Bicycle Wheel

A bicycle mechanic mounts a bicycle on the repair stand and starts the rear wheel spinning from rest to a final angular velocity of $250 \mathrm{rpm}$ in $5.00 \mathrm{~s}$. (a) Calculate the average angular acceleration in $\mathrm{rad} / \mathrm{s}^{2}$. (b) If she now hits the brakes, causing an angular acceleration of $-87.3 \mathrm{rad} / \mathrm{s}^{2}$, how long does it take the wheel to stop?

## Strategy

The average angular acceleration can be found directly from its definition $\bar{\alpha}=\frac{\Delta \omega}{\Delta t}$ because the final angular velocity and time are given. We see that $\Delta \omega=\omega_{\text {final }}-\omega_{\text {initial }}=250 \mathrm{rev} / \mathrm{min}$ and $\Delta t$ is $5.00 \mathrm{~s}$. For part (b), we know the angular acceleration and the initial angular velocity. We can find the stopping time by using the definition of average angular acceleration and solving for $\Delta t$, yielding

$$
\Delta t=\frac{\Delta \omega}{\alpha}
$$

## Solution

a. Entering known information into the definition of angular acceleration, we get

$$
\bar{\alpha}=\frac{\Delta \omega}{\Delta t}=\frac{250 \mathrm{rpm}}{5.00 \mathrm{~s}}
$$

Because $\Delta \omega$ is in revolutions per minute ( $\mathrm{rpm}$ ) and we want the standard units of $\mathrm{rad} / \mathrm{s}^{2}$ for angular acceleration, we need to convert from rpm to rad/s:

$$
\Delta \omega=250 \frac{\mathrm{rev}}{\mathrm{min}} \cdot \frac{2 \pi \mathrm{rad}}{\mathrm{rev}} \cdot \frac{1 \mathrm{~min}}{60 \mathrm{~s}}=26.2 \frac{\mathrm{rad}}{\mathrm{s}}
$$

Entering this quantity into the expression for $\alpha$, we get

$$
\alpha=\frac{\Delta \omega}{\Delta t}=\frac{26.2 \mathrm{rad} / \mathrm{s}}{5.00 \mathrm{~s}}=5.24 \mathrm{rad} / \mathrm{s}^{2}
$$

b. Here the angular velocity decreases from $26.2 \mathrm{rad} / \mathrm{s}(250 \mathrm{rpm})$ to zero, so that $\Delta \omega$ is $-26.2 \mathrm{rad} / \mathrm{s}$, and $\alpha$ is given to be $-87.3 \mathrm{rad} / \mathrm{s}^{2}$. Thus,

$$
\Delta t=\frac{-26.2 \mathrm{rad} / \mathrm{s}}{-87.3 \mathrm{rad} / \mathrm{s}^{2}}=0.300 \mathrm{~s}
$$

## Significance

Note that the angular acceleration as the mechanic spins the wheel is small and positive; it takes $5 \mathrm{~s}$ to produce an appreciable angular velocity. When she hits the brake, the angular acceleration is large and negative. The angular velocity quickly goes to zero.

## Wind Turbine

A wind turbine (Figure 10.10) in a wind farm is being shut down for maintenance. It takes $30 \mathrm{~s}$ for the turbine to go from its operating angular velocity to a complete stop in which the angular velocity function is $\omega(t)=\left[\left(t \mathrm{~s}^{-1}-30.0\right)^{2} / 100.0\right] \mathrm{rad} / \mathrm{s}$. If the turbine is rotating counterclockwise looking into the page, (a) what are the directions of the angular velocity and acceleration vectors? (b) What is the average angular acceleration? (c) What is the instantaneous angular acceleration at $t=0.0,15.0,30.0 \mathrm{~s}$ ?

## Strategy

a. We are given the rotational sense of the turbine, which is counterclockwise in the plane of the page. Using the right hand rule (Figure 10.5), we can establish the directions of the angular velocity and acceleration vectors.

b. We calculate the initial and final angular velocities to get the average angular acceleration. We establish the sign of the angular acceleration from the results in (a).

c. We are given the functional form of the angular velocity, so we can find the functional form of the angular acceleration function by taking its derivative with respect to time.

## Solution

a. Since the turbine is rotating counterclockwise, angular velocity $\overrightarrow{\boldsymbol{\omega}}$ points out of the page. But since the angular velocity is decreasing, the angular acceleration $\overrightarrow{\boldsymbol{\alpha}}$ points into the page, in the opposite sense to the angular velocity.

b. The initial angular velocity of the turbine, setting $t=0$, is $\omega=9.0 \mathrm{rad} / \mathrm{s}$. The final angular velocity is zero, so the average angular acceleration is

$$
\bar{\alpha}=\frac{\Delta \omega}{\Delta t}=\frac{\omega-\omega_{0}}{t-t_{0}}=\frac{0-9.0 \mathrm{rad} / \mathrm{s}}{30.0-0 \mathrm{~s}}=-0.3 \mathrm{rad} / \mathrm{s}^{2}
$$

c. Taking the derivative of the angular velocity with respect to time gives $\alpha=\frac{d \omega}{d t}=(t-30.0) / 50.0 \mathrm{rad} / \mathrm{s}^{2}$

$$
\alpha(0.0 \mathrm{~s})=-0.6 \mathrm{rad} / \mathrm{s}^{2}, \alpha(15.0 \mathrm{~s})=-0.3 \mathrm{rad} / \mathrm{s}^{2}, \text { and } \alpha(30.0 \mathrm{~s})=0 \mathrm{rad} / \mathrm{s}
$$

## Significance

We found from the calculations in (a) and (b) that the angular acceleration $\alpha$ and the average angular acceleration $\bar{\alpha}$ are negative. The turbine has an angular acceleration in the opposite sense to its angular velocity.

We now have a basic vocabulary for discussing fixed-axis rotational kinematics and relationships between rotational variables. We discuss more definitions and connections in the next section.

### 10.2 Rotation with Constant Angular Acceleration

## Learning Objectives

By the end of this section, you will be able to:

- Derive the kinematic equations for rotational motion with constant angular acceleration
- Select from the kinematic equations for rotational motion with constant angular acceleration the appropriate equations to solve for unknowns in the analysis of systems undergoing fixed-axis rotation
- Use solutions found with the kinematic equations to verify the graphical analysis of fixed-axis rotation with constant angular acceleration

In the preceding section, we defined the rotational variables of angular displacement, angular velocity, and angular acceleration. In this section, we work with these definitions to derive relationships among these variables and use these relationships to analyze rotational motion for a rigid body about a fixed axis under a constant angular acceleration. This analysis forms the basis for rotational kinematics. If the angular acceleration is constant, the equations of rotational kinematics simplify, similar to the equations of linear kinematics discussed in Motion along a Straight Line and Motion in Two and Three Dimensions. We can then use this simplified set of equations to describe many applications in physics and engineering where the angular acceleration of the system is constant. Rotational kinematics is also a prerequisite to the discussion of rotational dynamics later in this chapter.

## Kinematics of Rotational Motion

Using our intuition, we can begin to see how the rotational quantities $\theta, \omega, \alpha$, and $t$ are related to one another. For example, we saw in the preceding section that if a flywheel has an angular acceleration in the same direction as its angular velocity vector, its angular velocity increases with time and its angular displacement also increases. On the contrary, if the angular acceleration is opposite to the angular velocity vector, its angular velocity decreases with time. We can describe these physical situations and many others with a consistent set of rotational kinematic equations under a constant angular acceleration. The method to investigate rotational motion in this way is called kinematics of rotational motion.

To begin, we note that if the system is rotating under a constant acceleration, then the average angular velocity follows a simple relation because the angular velocity is increasing linearly with time. The average angular velocity is just half the sum of the initial and final values:

$$
\bar{\omega}=\frac{\omega_{0}+\omega_{\mathrm{f}}}{2}
$$

From the definition of the average angular velocity, we can find an equation that relates the angular position, average angular velocity, and time:

$$
\bar{\omega}=\frac{\Delta \theta}{\Delta t}
$$

Solving for $\theta$, we have

$$
\theta_{\mathrm{f}}=\theta_{0}+\bar{\omega} t
$$

where we have set $t_{0}=0$. This equation can be very useful if we know the average angular velocity of the system. Then we could find the angular displacement over a given time period. Next, we find an equation relating $\omega, \alpha$, and $t$. To determine this equation, we start with the definition of angular acceleration:

$$
\alpha=\frac{d \omega}{d t}
$$

We rearrange this to get $\alpha d t=d \omega$ and then we integrate both sides of this equation from initial values to final values, that is, from $t_{0}$ to $t$ and $\omega_{0}$ to $\omega_{\mathrm{f}}$. In uniform rotational motion, the angular acceleration is constant so it can be pulled out of the integral, yielding two definite integrals:

$$
\alpha \int_{t_{0}}^{t} d t^{\prime}=\int_{\omega_{0}}^{\omega_{\mathrm{f}}} d \omega
$$

Setting $t_{0}=0$, we have

$$
\alpha t=\omega_{f}-\omega_{0}
$$

We rearrange this to obtain

$$
\omega_{\mathrm{f}}=\omega_{0}+\alpha t,
$$

where $\omega_{0}$ is the initial angular velocity. Equation 10.11 is the rotational counterpart to the linear kinematics equation $v_{\mathrm{f}}=v_{0}+a t$. With Equation 10.11, we can find the angular velocity of an object at any specified time $t$ given the initial angular velocity and the angular acceleration.

Let's now do a similar treatment starting with the equation $\omega=\frac{d \theta}{d t}$. We rearrange it to obtain $\omega d t=d \theta$ and integrate both sides from initial to final values again, noting that the angular acceleration is constant and does not have a time dependence. However, this time, the angular velocity is not constant (in general), so we substitute in what we derived above:

$$
\begin{aligned}
& \int_{t_{0}}^{t_{f}}\left(\omega_{0}+\alpha t^{\prime}\right) d t^{\prime}=\int_{\theta_{0}}^{\theta_{\mathrm{f}}} d \theta \\
& \int_{t_{0}}^{t} \omega_{0} d t+\int_{t_{0}}^{t} \alpha t^{\prime} d t^{\prime}=\int_{\theta_{0}}^{\theta_{\mathrm{f}}} d \theta=\left[\omega_{0} t^{\prime}+\alpha\left(\frac{\left(t^{\prime}\right)^{2}}{2}\right)\right]_{t_{0}}^{t}=\omega_{0} t+\alpha\left(\frac{t^{2}}{2}\right)=\theta_{\mathrm{f}}-\theta_{0}
\end{aligned}
$$

where we have set $t_{0}=0$. Now we rearrange to obtain

$$
\theta_{\mathrm{f}}=\theta_{0}+\omega_{0} t+\frac{1}{2} \alpha t^{2}
$$

Equation 10.12 is the rotational counterpart to the linear kinematics equation found in Motion Along a Straight Line for position as a function of time. This equation gives us the angular position of a rotating rigid body at any time $t$ given the initial conditions (initial angular position and initial angular velocity) and the angular acceleration.

We can find an equation that is independent of time by solving for $t$ in Equation 10.11 and substituting into Equation 10.12 . Equation 10.12 becomes

$$
\begin{aligned}
\theta_{\mathrm{f}} & =\theta_{0}+\omega_{0}\left(\frac{\omega_{\mathrm{f}}-\omega_{0}}{\alpha}\right)+\frac{1}{2} \alpha\left(\frac{\omega_{\mathrm{f}}-\omega_{0}}{\alpha}\right)^{2} \\
& =\theta_{0}+\frac{\omega_{0} \omega_{\mathrm{f}}}{\alpha}-\frac{\omega_{0}^{2}}{\alpha}+\frac{1}{2} \frac{\omega_{\mathrm{f}}^{2}}{\alpha}-\frac{\omega_{0} \omega_{\mathrm{f}}}{\alpha}+\frac{1}{2} \frac{\omega_{0}^{2}}{\alpha} \\
& =\theta_{0}+\frac{1}{2} \frac{\omega_{\mathrm{f}}^{2}}{\alpha}-\frac{1}{2} \frac{\omega_{0}^{2}}{\alpha} \\
\theta_{\mathrm{f}}-\theta_{0} & =\frac{\omega_{\mathrm{f}}^{2}-\omega_{0}^{2}}{2 \alpha}
\end{aligned}
$$

or

$$
\omega_{\mathrm{f}}^{2}=\omega_{0}^{2}+2 \alpha(\Delta \theta)
$$

Equation 10.10 through Equation 10.13 describe fixed-axis rotation for constant acceleration and are summarized in Table 10.1 .

| Angular displacement from average angular velocity | $\theta_{\mathrm{f}}=\theta_{0}+\bar{\omega} t$ |
| :--- | :--- |
| Angular velocity from angular acceleration | $\omega_{\mathrm{f}}=\omega_{0}+\alpha t$ |
| Angular displacement from angular velocity and angular acceleration | $\theta_{\mathrm{f}}=\theta_{0}+\omega_{0} t+\frac{1}{2} \alpha t^{2}$ |
| Angular velocity from angular displacement and angular acceleration | $\omega_{\mathrm{f}}^{2}=\omega_{0}{ }^{2}+2 \alpha(\Delta \theta)$ |

Table 10.1 Kinematic Equations

## Applying the Equations for Rotational Motion

Now we can apply the key kinematic relations for rotational motion to some simple examples to get a feel for how the equations can be applied to everyday situations.

## EXAMPLE 10.4

## Calculating the Acceleration of a Fishing Reel

A deep-sea fisherman hooks a big fish that swims away from the boat, pulling the fishing line from his fishing reel. The whole system is initially at rest, and the fishing line unwinds from the reel at a radius of $4.50 \mathrm{~cm}$ from its axis of rotation. The reel is given an angular acceleration of $110 \mathrm{rad} / \mathrm{s}^{2}$ for $2.00 \mathrm{~s}$ (Figure 10.11).

(a) What is the final angular velocity of the reel after $2 \mathrm{~s}$ ?

(b) How many revolutions does the reel make?

## Strategy

Identify the knowns and compare with the kinematic equations for constant acceleration. Look for the appropriate equation that can be solved for the unknown, using the knowns given in the problem description.

## Solution

a. We are given $\alpha$ and $t$ and want to determine $\omega$. The most straightforward equation to use is $\omega_{\mathrm{f}}=\omega_{0}+\alpha t$, since all terms are known besides the unknown variable we are looking for. We are given that $\omega_{0}=0$ (it starts from rest), so

$$
\omega_{\mathrm{f}}=0+\left(110 \mathrm{rad} / \mathrm{s}^{2}\right)(2.00 \mathrm{~s})=220 \mathrm{rad} / \mathrm{s}
$$

b. We are asked to find the number of revolutions. Because $1 \mathrm{rev}=2 \pi \mathrm{rad}$, we can find the number of revolutions by finding $\theta$ in radians. We are given $\alpha$ and $t$, and we know $\omega_{0}$ is zero, so we can obtain $\theta$ by
using

$$
\begin{aligned}
\theta_{\mathrm{f}} & =\theta_{\mathrm{i}}+\omega_{\mathrm{i}} t+\frac{1}{2} \alpha t^{2} \\
& =0+0+(0.500)\left(110 \mathrm{rad} / \mathrm{s}^{2}\right)(2.00 \mathrm{~s})^{2}=220 \mathrm{rad}
\end{aligned}
$$

Converting radians to revolutions gives

$$
\text { Number of rev }=(220 \mathrm{rad}) \frac{1 \mathrm{rev}}{2 \pi \mathrm{rad}}=35.0 \mathrm{rev}
$$

## Significance

This example illustrates that relationships among rotational quantities are highly analogous to those among linear quantities. The answers to the questions are realistic. After unwinding for two seconds, the reel is found to spin at $220 \mathrm{rad} / \mathrm{s}$, which is $2100 \mathrm{rpm}$. (No wonder reels sometimes make high-pitched sounds.)

In the preceding example, we considered a fishing reel with a positive angular acceleration. Now let us consider what happens with a negative angular acceleration.

## EXAMPLE 10.5

## Calculating the Duration When the Fishing Reel Slows Down and Stops

Now the fisherman applies a brake to the spinning reel, achieving an angular acceleration of $-300 \mathrm{rad} / \mathrm{s}^{2}$. How long does it take the reel to come to a stop?

## Strategy

We are asked to find the time $t$ for the reel to come to a stop. The initial and final conditions are different from those in the previous problem, which involved the same fishing reel. Now we see that the initial angular velocity is $\omega_{0}=220 \mathrm{rad} / \mathrm{s}$ and the final angular velocity $\omega$ is zero. The angular acceleration is given as $\alpha=-300 \mathrm{rad} / \mathrm{s}^{2}$. Examining the available equations, we see all quantities but $t$ are known in $\omega_{\mathrm{f}}=\omega_{0}+\alpha t$, making it easiest to use this equation.

## Solution

The equation states

$$
\omega_{\mathrm{f}}=\omega_{0}+\alpha t
$$

We solve the equation algebraically for $t$ and then substitute the known values as usual, yielding

$$
t=\frac{\omega_{\mathrm{f}}-\omega_{0}}{\alpha}=\frac{0-220.0 \mathrm{rad} / \mathrm{s}}{-300.0 \mathrm{rad} / \mathrm{s}^{2}}=0.733 \mathrm{~s}
$$

## Significance

Note that care must be taken with the signs that indicate the directions of various quantities. Also, note that the time to stop the reel is fairly small because the acceleration is rather large. Fishing lines sometimes snap because of the accelerations involved, and fishermen often let the fish swim for a while before applying brakes on the reel. A tired fish is slower, requiring a smaller acceleration.

## Angular Acceleration of a Propeller

Figure 10.12 shows a graph of the angular velocity of a propeller on an aircraft as a function of time. Its angular velocity starts at $30 \mathrm{rad} / \mathrm{s}$ and drops linearly to $0 \mathrm{rad} / \mathrm{s}$ over the course of 5 seconds. (a) Find the angular acceleration of the object and verify the result using the kinematic equations. (b) Find the angle through which the propeller rotates during these 5 seconds and verify your result using the kinematic equations.

## Strategy

a. Since the angular velocity varies linearly with time, we know that the angular acceleration is constant and does not depend on the time variable. The angular acceleration is the slope of the angular velocity vs. time graph, $\alpha=\frac{d \omega}{d t}$. To calculate the slope, we read directly from Figure 10.12, and see that $\omega_{0}=30 \mathrm{rad} / \mathrm{s}$ at $t=0 \mathrm{~s}$ and $\omega_{\mathrm{f}}=0 \mathrm{rad} / \mathrm{s}$ at $t=5 \mathrm{~s}$. Then, we can verify the result using $\omega=\omega_{0}+\alpha t$.

b. We use the equation $\omega=\frac{d \theta}{d t}$; since the time derivative of the angle is the angular velocity, we can find the angular displacement by integrating the angular velocity, which from the figure means taking the area under the angular velocity graph. In other words:

$$
\int_{\theta_{0}}^{\theta_{\mathrm{f}}} d \theta=\theta_{\mathrm{f}}-\theta_{0}=\int_{t_{0}}^{t_{\mathrm{f}}} \omega(t) d t
$$

Then we use the kinematic equations for constant acceleration to verify the result.

## Solution

a. Calculating the slope, we get

$$
\alpha=\frac{\omega-\omega_{0}}{t-t_{0}}=\frac{(0-30.0) \mathrm{rad} / \mathrm{s}}{(5.0-0) \mathrm{s}}=-6.0 \mathrm{rad} / \mathrm{s}^{2}
$$

We see that this is exactly Equation 10.11 with a little rearranging of terms.

b. We can find the area under the curve by calculating the area of the right triangle, as shown in Figure 10.13.

$$
\begin{aligned}
\Delta \theta & =\text { area }(\text { triangle }) \\
\Delta \theta & =\frac{1}{2}(30 \mathrm{rad} / \mathrm{s})(5 \mathrm{~s})=75 \mathrm{rad}
\end{aligned}
$$

We verify the solution using Equation 10.12 :

$$
\theta_{\mathrm{f}}=\theta_{0}+\omega_{0} t+\frac{1}{2} \alpha t^{2}
$$

Setting $\theta_{0}=0$, we have

$$
\theta_{f}=(30.0 \mathrm{rad} / \mathrm{s})(5.0 \mathrm{~s})+\frac{1}{2}\left(-6.0 \mathrm{rad} / \mathrm{s}^{2}\right)(5.0 \mathrm{rad} / \mathrm{s})^{2}=150.0-75.0=75.0 \mathrm{rad}
$$

This verifies the solution found from finding the area under the curve.

## Significance

We see from part (b) that there are alternative approaches to analyzing fixed-axis rotation with constant acceleration. We started with a graphical approach and verified the solution using the rotational kinematic equations. Since $\alpha=\frac{d \omega}{d t}$, we could do the same graphical analysis on an angular acceleration-vs.-time curve. The area under an $\alpha$-vs.- $t$ curve gives us the change in angular velocity. Since the angular acceleration is constant in this section, this is a straightforward exercise.

### 10.3 Relating Angular and Translational Quantities

In this section, we relate each of the rotational variables to the translational variables defined in Motion Along a Straight Line and Motion in Two and Three Dimensions. This will complete our ability to describe rigid-body rotations.

## Angular vs. Linear Variables

In Rotational Variables, we introduced angular variables. If we compare the rotational definitions with the definitions of linear kinematic variables from Motion Along a Straight Line and Motion in Two and Three Dimensions, we find that there is a mapping of the linear variables to the rotational ones. Linear position, velocity, and acceleration have their rotational counterparts, as we can see when we write them side by side:

## Linear Rotational

| Position | $X$ | $\theta$ |
| :--- | :--- | :--- |
| Velocity | $v=\frac{d x}{d t}$ | $\omega=\frac{d \theta}{d t}$ |
| Acceleration | $a=\frac{d v}{d t}$ | $\alpha=\frac{d \omega}{d t}$ |

Let's compare the linear and rotational variables individually. The linear variable of position has physical units of meters, whereas the angular position variable has dimensionless units of radians, as can be seen from the definition of $\theta=\frac{s}{r}$, which is the ratio of two lengths. The linear velocity has units of $\mathrm{m} / \mathrm{s}$, and its counterpart, the angular velocity, has units of rad/s. In Rotational Variables, we saw in the case of circular motion that the linear tangential speed of a particle at a radius $r$ from the axis of rotation is related to the angular velocity by the relation $v_{\mathrm{t}}=r \omega$. This could also apply to points on a rigid body rotating about a fixed axis. Here, we consider only circular motion. In circular motion, both uniform and nonuniform, there exists a centripetal acceleration (Motion in Two and Three Dimensions). The centripetal acceleration vector points inward from the particle executing circular motion toward the axis of rotation. The derivation of the magnitude of the centripetal acceleration is given in Motion in Two and Three Dimensions. From that derivation, the magnitude of the centripetal acceleration was found to be

$$
a_{\mathrm{c}}=\frac{v_{\mathrm{t}}^{2}}{r}
$$

where $r$ is the radius of the circle.

Thus, in uniform circular motion when the angular velocity is constant and the angular acceleration is zero, we have a linear acceleration-that is, centripetal acceleration-since the tangential speed in Equation 10.14 is a constant. If nonuniform circular motion is present, the rotating system has an angular acceleration, and we have both a linear centripetal acceleration that is changing (because $v_{\mathrm{t}}$ is changing) as well as a linear tangential acceleration. These relationships are shown in Figure 10.14, where we show the centripetal and tangential accelerations for uniform and nonuniform circular motion.

The centripetal acceleration is due to the change in the direction of tangential velocity, whereas the tangential acceleration is due to any change in the magnitude of the tangential velocity. The tangential and centripetal acceleration vectors $\overrightarrow{\mathbf{a}}_{t}$ and $\overrightarrow{\mathbf{a}}_{\mathrm{c}}$ are always perpendicular to each other, as seen in Figure 10.14. To complete this description, we can assign a total linear acceleration vector to a point on a rotating rigid body or a particle executing circular motion at a radius $r$ from a fixed axis. The total linear acceleration vector $\overrightarrow{\mathbf{a}}$ is the vector sum of the centripetal and tangential accelerations,

$$
\overrightarrow{\mathbf{a}}=\overrightarrow{\mathbf{a}}_{\mathrm{c}}+\overrightarrow{\mathbf{a}}_{\mathrm{t}}
$$

The total linear acceleration vector in the case of nonuniform circular motion points at an angle between the centripetal and tangential acceleration vectors, as shown in Figure 10.15 . Since $\overrightarrow{\mathbf{a}}_{\mathrm{c}} \perp \overrightarrow{\mathbf{a}}_{t}$, the magnitude of the total linear acceleration is

$$
|\overrightarrow{\mathbf{a}}|=\sqrt{a_{\mathrm{c}}^{2}+a_{\mathrm{t}}^{2}}
$$

Note that if the angular acceleration is zero, the total linear acceleration is equal to the centripetal acceleration.

## Relationships between Rotational and Translational Motion

We can look at two relationships between rotational and translational motion.

1. Generally speaking, the linear kinematic equations have their rotational counterparts. Table 10.2 lists the four linear kinematic equations and the corresponding rotational counterpart. The two sets of equations look similar to each other, but describe two different physical situations, that is, rotation and translation.

| Rotational | Translational |
| :--- | :--- |
| $\theta_{\mathrm{f}}=\theta_{0}+\bar{\omega} t$ | $x=x_{0}+\bar{v} t$ |
| $\omega_{\mathrm{f}}=\omega_{0}+\alpha t$ | $v_{\mathrm{f}}=v_{0}+a t$ |
| $\theta_{\mathrm{f}}=\theta_{0}+\omega_{0} t+\frac{1}{2} \alpha t^{2}$ | $x_{\mathrm{f}}=x_{0}+v_{0} t+\frac{1}{2} a t^{2}$ |
| $\omega_{\mathrm{f}}^{2}=\omega_{0}^{2}+2 \alpha(\Delta \theta)$ | $v_{\mathrm{f}}^{2}=v_{0}^{2}+2 a(\Delta x)$ |

Table 10.2 Rotational and Translational Kinematic Equations

2. The second correspondence has to do with relating linear and rotational variables in the special case of circular motion. This is shown in Table 10.3, where in the third column, we have listed the connecting equation that relates the linear variable to the rotational variable. The rotational variables of angular velocity and acceleration have subscripts that indicate their definition in circular motion.

| Rotational | Translational | Relationship ( $r$ = radius) |
| :--- | :--- | :--- |
| $\theta$ | $s$ | $\theta=\frac{s}{r}$ |
| $\omega$ | $v_{\mathrm{t}}$ | $\omega=\frac{v_{\mathrm{t}}}{r}$ |
| $\alpha$ | $a_{\mathrm{t}}$ | $\alpha=\frac{a_{\mathrm{t}}}{r}$ |
|  | $a_{\mathrm{c}}$ | $a_{\mathrm{c}}=\frac{v_{\mathrm{t}}^{2}}{r}$ |

Table 10.3 Rotational and Translational Quantities: Circular Motion

## EXAMPLE 10.7

## Linear Acceleration of a Centrifuge

A centrifuge has a radius of $20 \mathrm{~cm}$ and accelerates from a maximum rotation rate of $10,000 \mathrm{rpm}$ to rest in 30 seconds under a constant angular acceleration. It is rotating counterclockwise. What is the magnitude of the total acceleration of a point at the tip of the centrifuge at $t=29.0 \mathrm{~s}$ ? What is the direction of the total acceleration vector?

## Strategy

With the information given, we can calculate the angular acceleration, which then will allow us to find the tangential acceleration. We can find the centripetal acceleration at $t=0$ by calculating the tangential speed at this time. With the magnitudes of the accelerations, we can calculate the total linear acceleration. From the description of the rotation in the problem, we can sketch the direction of the total acceleration vector.

## Solution

The angular acceleration is

$$
\alpha=\frac{\omega-\omega_{0}}{t}=\frac{0-\left(1.0 \times 10^{4}\right) 2 \pi / 60.0 \mathrm{~s}(\mathrm{rad} / \mathrm{s})}{30.0 \mathrm{~s}}=-34.9 \mathrm{rad} / \mathrm{s}^{2}
$$

Therefore, the tangential acceleration is

$$
a_{\mathrm{t}}=r \alpha=0.2 \mathrm{~m}\left(-34.9 \mathrm{rad} / \mathrm{s}^{2}\right)=-7.0 \mathrm{~m} / \mathrm{s}^{2}
$$

The angular velocity at $t=29.0 \mathrm{~s}$ is

$$
\begin{aligned}
\omega & =\omega_{0}+\alpha t=1.0 \times 10^{4}\left(\frac{2 \pi}{60.0 \mathrm{~s}}\right)+\left(-34.9 \mathrm{rad} / \mathrm{s}^{2}\right)(29.0 \mathrm{~s}) \\
& =1047.2 \mathrm{rad} / \mathrm{s}-1012.71=35.1 \mathrm{rad} / \mathrm{s}
\end{aligned}
$$

Thus, the tangential speed at $t=29.0 \mathrm{~s}$ is

$$
v_{\mathrm{t}}=r \omega=0.2 \mathrm{~m}(35.1 \mathrm{rad} / \mathrm{s})=7.0 \mathrm{~m} / \mathrm{s}
$$

We can now calculate the centripetal acceleration at $t=29.0 \mathrm{~s}$ :

$$
a_{\mathrm{c}}=\frac{v^{2}}{r}=\frac{(7.0 \mathrm{~m} / \mathrm{s})^{2}}{0.2 \mathrm{~m}}=245.0 \mathrm{~m} / \mathrm{s}^{2}
$$

Since the two acceleration vectors are perpendicular to each other, the magnitude of the total linear acceleration is

$$
|\overrightarrow{\mathbf{a}}|=\sqrt{a_{\mathrm{c}}^{2}+a_{\mathrm{t}}^{2}}=\sqrt{(245.0)^{2}+(-7.0)^{2}}=245.1 \mathrm{~m} / \mathrm{s}^{2}
$$

Since the centrifuge has a negative angular acceleration, it is slowing down. The total acceleration vector is as shown in Figure 10.16. The angle with respect to the centripetal acceleration vector is

$$
\theta=\tan ^{-1} \frac{-7.0}{245.0}=-1.6^{\circ}
$$

The negative sign means that the total acceleration vector is angled toward the clockwise direction.

## Significance

From Figure 10.16, we see that the tangential acceleration vector is opposite the direction of rotation. The magnitude of the tangential acceleration is much smaller than the centripetal acceleration, so the total linear acceleration vector will make a very small angle with respect to the centripetal acceleration vector.

## CHECK YOUR UNDERSTANDING 10.3

A boy jumps on a merry-go-round with a radius of $5 \mathrm{~m}$ that is at rest. It starts accelerating at a constant rate up to an angular velocity of $5 \mathrm{rad} / \mathrm{s}$ in 20 seconds. What is the distance travelled by the boy?

### 10.4 Moment of Inertia and Rotational Kinetic Energy

So far in this chapter, we have been working with rotational kinematics: the description of motion for a rotating rigid body with a fixed axis of rotation. In this section, we define two new quantities that are helpful for analyzing properties of rotating objects: moment of inertia and rotational kinetic energy. With these properties defined, we will have two important tools we need for analyzing rotational dynamics.

## Rotational Kinetic Energy

Any moving object has kinetic energy. We know how to calculate this for a body undergoing translational motion, but how about for a rigid body undergoing rotation? This might seem complicated because each point on the rigid body has a different velocity. However, we can make use of angular velocity-which is the same for the entire rigid body-to express the kinetic energy for a rotating object. Figure 10.17 shows an example of a very energetic rotating body: an electric grindstone propelled by a motor. Sparks are flying, and noise and vibration are generated as the grindstone does its work. This system has considerable energy, some of it in the form of heat, light, sound, and vibration. However, most of this energy is in the form of rotational kinetic energy.

Energy in rotational motion is not a new form of energy; rather, it is the energy associated with rotational motion, the same as kinetic energy in translational motion. However, because kinetic energy is given by $K=\frac{1}{2} m v^{2}$, and velocity is a quantity that is different for every point on a rotating body about an axis, it makes sense to find a way to write kinetic energy in terms of the variable $\omega$, which is the same for all points on a rigid rotating body. For a single particle rotating around a fixed axis, this is straightforward to calculate. We can relate the angular velocity to the magnitude of the translational velocity using the relation $v_{\mathrm{t}}=\omega r$, where $r$ is the distance of the particle from the axis of rotation and $v_{t}$ is its tangential speed. Substituting into the equation for kinetic energy, we find

$$
K=\frac{1}{2} m v_{\mathrm{t}}^{2}=\frac{1}{2} m(\omega r)^{2}=\frac{1}{2}\left(m r^{2}\right) \omega^{2}
$$

In the case of a rigid rotating body, we can divide up any body into a large number of smaller masses, each with a mass $m_{j}$ and distance to the axis of rotation $r_{j}$, such that the total mass of the body is equal to the sum of the individual masses: $M=\sum_{j} m_{j}$. Each smaller mass has tangential speed $v_{j}$, where we have dropped the subscript $t$ for the moment. The total kinetic energy of the rigid rotating body is

$$
K=\sum_{j} \frac{1}{2} m_{j} v_{j}^{2}=\sum_{j} \frac{1}{2} m_{j}\left(r_{j} \omega_{j}\right)^{2}
$$

and since $\omega_{j}=\omega$ for all masses,

$$
K=\frac{1}{2}\left(\sum_{j} m_{j} r_{j}^{2}\right) \omega^{2}
$$

The units of Equation 10.16 are joules (J). The equation in this form is complete, but awkward; we need to find a way to generalize it.

## Moment of Inertia

If we compare Equation 10.16 to the way we wrote kinetic energy in Work and Kinetic Energy, $\left(\frac{1}{2} m v^{2}\right)$, this suggests we have a new rotational variable to add to our list of our relations between rotational and translational variables. The quantity $\sum_{j} m_{j} r_{j}^{2}$ is the counterpart for mass in the equation for rotational kinetic energy. This is an important new term for rotational motion. This quantity is called the moment of inertia $I$, with units of $\mathrm{kg} \cdot \mathrm{m}^{2}$ :

$$
I=\sum_{j} m_{j} r_{j}^{2}
$$

For now, we leave the expression in summation form, representing the moment of inertia of a system of point particles rotating about a fixed axis. We note that the moment of inertia of a single point particle about a fixed axis is simply $m r^{2}$, with $r$ being the distance from the point particle to the axis of rotation. In the next section, we explore the integral form of this equation, which can be used to calculate the moment of inertia of some regular-shaped rigid bodies.

The moment of inertia is the quantitative measure of rotational inertia, just as in translational motion, and mass is the quantitative measure of linear inertia-that is, the more massive an object is, the more inertia it has, and the greater is its resistance to change in linear velocity. Similarly, the greater the moment of inertia of a rigid body or system of particles, the greater is its resistance to change in angular velocity about a fixed axis of rotation. It is interesting to see how the moment of inertia varies with $r$, the distance to the axis of rotation of the mass particles in Equation 10.17. Rigid bodies and systems of particles with more mass concentrated at a greater distance from the axis of rotation have greater moments of inertia than bodies and systems of the same mass, but concentrated near the axis of rotation. In this way, we can see that a hollow cylinder has more
rotational inertia than a solid cylinder of the same mass when rotating about an axis through the center. Substituting Equation 10.17 into Equation 10.16, the expression for the kinetic energy of a rotating rigid body becomes

$$
K=\frac{1}{2} I \omega^{2}
$$

We see from this equation that the kinetic energy of a rotating rigid body is directly proportional to the moment of inertia and the square of the angular velocity. This is exploited in flywheel energy-storage devices, which are designed to store large amounts of rotational kinetic energy. Many carmakers are now testing flywheel energy storage devices in their automobiles, such as the flywheel, or kinetic energy recovery system, shown in Figure 10.18.

The rotational and translational quantities for kinetic energy and inertia are summarized in Table 10.4. The relationship column is not included because a constant doesn't exist by which we could multiply the rotational quantity to get the translational quantity, as can be done for the variables in Table 10.3.

| Rotational | Translational |
| :--- | :--- |
| $I=\sum_{j} m_{j} r_{j}^{2}$ | $m$ |
| $K=\frac{1}{2} I \omega^{2}$ | $K=\frac{1}{2} m v^{2}$ |

Table 10.4 Rotational and Translational Kinetic Energies and Inertia

## EXAMPLE 10.8

## Moment of Inertia of a System of Particles

Six small washers are spaced $10 \mathrm{~cm}$ apart on a rod of negligible mass and $0.5 \mathrm{~m}$ in length. The mass of each washer is $20 \mathrm{~g}$. The rod rotates about an axis located at $25 \mathrm{~cm}$, as shown in Figure 10.19. (a) What is the moment of inertia of the system? (b) If the two washers closest to the axis are removed, what is the moment of
inertia of the remaining four washers? (c) If the system with six washers rotates at $5 \mathrm{rev} / \mathrm{s}$, what is its rotational kinetic energy?

## Strategy

a. We use the definition for moment of inertia for a system of particles and perform the summation to evaluate this quantity. The masses are all the same so we can pull that quantity in front of the summation symbol.

b. We do a similar calculation.

c. We insert the result from (a) into the expression for rotational kinetic energy.

## Solution

a. $I=\sum_{j} m_{j} r_{j}^{2}=(0.02 \mathrm{~kg})\left(2 \times(0.25 \mathrm{~m})^{2}+2 \times(0.15 \mathrm{~m})^{2}+2 \times(0.05 \mathrm{~m})^{2}\right)=0.0035 \mathrm{~kg} \cdot \mathrm{m}^{2}$.
b. $I=\sum_{j} m_{j} r_{j}^{2}=(0.02 \mathrm{~kg})\left(2 \times(0.25 \mathrm{~m})^{2}+2 \times(0.15 \mathrm{~m})^{2}\right)=0.0034 \mathrm{~kg} \cdot \mathrm{m}^{2}$.
c. $K=\frac{1}{2} I \omega^{2}=\frac{1}{2}\left(0.0035 \mathrm{~kg} \cdot \mathrm{m}^{2}\right)(5.0 \times 2 \pi \mathrm{rad} / \mathrm{s})^{2}=1.73 \mathrm{~J}$.

## Significance

We can see the individual contributions to the moment of inertia. The masses close to the axis of rotation have a very small contribution. When we removed them, it had a very small effect on the moment of inertia.

In the next section, we generalize the summation equation for point particles and develop a method to calculate moments of inertia for rigid bodies. For now, though, Figure 10.20 gives values of rotational inertia for common object shapes around specified axes.

$$
I=\frac{M R^{2}}{12}
$$

$I=\frac{M R^{2}}{3}$

## Applying Rotational Kinetic Energy

Now let's apply the ideas of rotational kinetic energy and the moment of inertia table to get a feeling for the energy associated with a few rotating objects. The following examples will also help get you comfortable using these equations. First, let's look at a general problem-solving strategy for rotational energy.

## PROBLEM-SOLVING STRATEGY

## Rotational Energy

1. Determine that energy or work is involved in the rotation.
2. Determine the system of interest. A sketch usually helps.
3. Analyze the situation to determine the types of work and energy involved.
4. If there are no losses of energy due to friction and other nonconservative forces, mechanical energy is conserved, that is, $K_{\mathrm{i}}+U_{\mathrm{i}}=K_{\mathrm{f}}+U_{\mathrm{f}}$.
5. If nonconservative forces are present, mechanical energy is not conserved, and other forms of energy, such as heat and light, may enter or leave the system. Determine what they are and calculate them as necessary.
6. Eliminate terms wherever possible to simplify the algebra.
7. Evaluate the numerical solution to see if it makes sense in the physical situation presented in the wording
of the problem.

## EXAMPLE 10.9

## Calculating Helicopter Energies

A typical small rescue helicopter has four blades: Each is $4.00 \mathrm{~m}$ long and has a mass of $50.0 \mathrm{~kg}$ (Figure 10.21). The blades can be approximated as thin rods that rotate about one end of an axis perpendicular to their length. The helicopter has a total loaded mass of $1000 \mathrm{~kg}$. (a) Calculate the rotational kinetic energy in the blades when they rotate at $300 \mathrm{rpm}$. (b) Calculate the translational kinetic energy of the helicopter when it flies at $20.0 \mathrm{~m} / \mathrm{s}$, and compare it with the rotational energy in the blades.

## Strategy

Rotational and translational kinetic energies can be calculated from their definitions. The wording of the problem gives all the necessary constants to evaluate the expressions for the rotational and translational kinetic energies.

## Solution

a. The rotational kinetic energy is

$$
K=\frac{1}{2} I \omega^{2}
$$

We must convert the angular velocity to radians per second and calculate the moment of inertia before we can find $K$. The angular velocity $\omega$ is

$$
\omega=\frac{300 \mathrm{rev}}{1.00 \mathrm{~min}} \frac{2 \pi \mathrm{rad}}{1 \mathrm{rev}} \frac{1.00 \mathrm{~min}}{60.0 \mathrm{~s}}=31.4 \frac{\mathrm{rad}}{\mathrm{s}}
$$

The moment of inertia of one blade is that of a thin rod rotated about its end, listed in Figure 10.20. The total $I$ is four times this moment of inertia because there are four blades. Thus,

$$
I=4 \frac{M l^{2}}{3}=4 \times \frac{(50.0 \mathrm{~kg})(4.00 \mathrm{~m})^{2}}{3}=1067.0 \mathrm{~kg} \cdot \mathrm{m}^{2}
$$

Entering $\omega$ and $I$ into the expression for rotational kinetic energy gives

$$
K=0.5\left(1067 \mathrm{~kg} \cdot \mathrm{m}^{2}\right)(31.4 \mathrm{rad} / \mathrm{s})^{2}=5.26 \times 10^{5} \mathrm{~J}
$$

b. Entering the given values into the equation for translational kinetic energy, we obtain

$$
K=\frac{1}{2} m v^{2}=(0.5)(1000.0 \mathrm{~kg})(20.0 \mathrm{~m} / \mathrm{s})^{2}=2.00 \times 10^{5} \mathrm{~J}
$$

To compare kinetic energies, we take the ratio of translational kinetic energy to rotational kinetic energy. This ratio is

$$
\frac{2.00 \times 10^{5} \mathrm{~J}}{5.26 \times 10^{5} \mathrm{~J}}=0.380
$$

## Significance

The ratio of translational energy to rotational kinetic energy is only 0.380 . This ratio tells us that most of the kinetic energy of the helicopter is in its spinning blades.

## EXAMPLE 10.10

## Energy in a Boomerang

A person hurls a boomerang into the air with a velocity of $30.0 \mathrm{~m} / \mathrm{s}$ at an angle of $40.0^{\circ}$ with respect to the horizontal (Figure 10.22). It has a mass of $1.0 \mathrm{~kg}$ and is rotating at $10.0 \mathrm{rev} / \mathrm{s}$. The moment of inertia of the boomerang is given as $I=\frac{1}{12} m L^{2}$ where $L=0.7 \mathrm{~m}$. (a) What is the total energy of the boomerang when it leaves the hand? (b) How high does the boomerang go from the elevation of the hand, neglecting air resistance?

## Strategy

We use the definitions of rotational and linear kinetic energy to find the total energy of the system. The problem states to neglect air resistance, so we don't have to worry about energy loss. In part (b), we use conservation of mechanical energy to find the maximum height of the boomerang.

## Solution

a. $\quad$ Moment of inertia: $I=\frac{1}{12} m L^{2}=\frac{1}{12}(1.0 \mathrm{~kg})(0.7 \mathrm{~m})^{2}=0.041 \mathrm{~kg} \cdot \mathrm{m}^{2}$.

Angular velocity: $\omega=(10.0 \mathrm{rev} / \mathrm{s})(2 \pi)=62.83 \mathrm{rad} / \mathrm{s}$.

The rotational kinetic energy is therefore

$$
K_{\mathrm{R}}=\frac{1}{2}\left(0.041 \mathrm{~kg} \cdot \mathrm{m}^{2}\right)(62.83 \mathrm{rad} / \mathrm{s})^{2}=80.93 \mathrm{~J}
$$

The translational kinetic energy is

$$
K_{\mathrm{T}}=\frac{1}{2} m v^{2}=\frac{1}{2}(1.0 \mathrm{~kg})(30.0 \mathrm{~m} / \mathrm{s})^{2}=450.0 \mathrm{~J}
$$

Thus, the total energy in the boomerang is

$$
K_{\text {Total }}=K_{\mathrm{R}}+K_{\mathrm{T}}=80.93+450.0=530.93 \mathrm{~J}
$$

b. We use conservation of mechanical energy. Since the boomerang is launched at an angle, we need to write the total energies of the system in terms of its linear kinetic energies using the velocity in the $x$ - and $y$-directions. The total energy when the boomerang leaves the hand is

$$
E_{\text {Before }}=\frac{1}{2} m v_{x}^{2}+\frac{1}{2} m v_{y}^{2}+\frac{1}{2} I \omega^{2}
$$

The total energy at maximum height is

$$
E_{\text {Final }}=\frac{1}{2} m v_{x}^{2}+\frac{1}{2} I \omega^{2}+m g h
$$

By conservation of mechanical energy, $E_{\text {Before }}=E_{\text {Final }}$ so we have, after canceling like terms,

$$
\frac{1}{2} m v_{y}^{2}=m g h
$$

Since $v_{y}=30.0 \mathrm{~m} / \mathrm{s}\left(\sin 40^{\circ}\right)=19.28 \mathrm{~m} / \mathrm{s}$, we find

$$
h=\frac{(19.28 \mathrm{~m} / \mathrm{s})^{2}}{2\left(9.8 \mathrm{~m} / \mathrm{s}^{2}\right)}=18.97 \mathrm{~m}
$$

## Significance

In part (b), the solution demonstrates how energy conservation is an alternative method to solve a problem that normally would be solved using kinematics. In the absence of air resistance, the rotational kinetic energy was not a factor in the solution for the maximum height.

## CHECK YOUR UNDERSTANDING 10.4

A nuclear submarine propeller has a moment of inertia of $800.0 \mathrm{~kg} \cdot \mathrm{m}^{2}$. If the submerged propeller has a rotation rate of $4.0 \mathrm{rev} / \mathrm{s}$ when the engine is cut, what is the rotation rate of the propeller after $5.0 \mathrm{~s}$ when water resistance has taken $50,000 \mathrm{~J}$ out of the system?

### 10.5 Calculating Moments of Inertia

In the preceding section, we defined the moment of inertia but did not show how to calculate it. In this section, we show how to calculate the moment of inertia for several standard types of objects, as well as how to use known moments of inertia to find the moment of inertia for a shifted axis or for a compound object. This section is very useful for seeing how to apply a general equation to complex objects (a skill that is critical for more advanced physics and engineering courses).

## Moment of Inertia

We defined the moment of inertia $I$ of an object to be $I=\sum_{i} m_{i} r_{i}^{2}$ for all the point masses that make up the object. Because $r$ is the distance to the axis of rotation from each piece of mass that makes up the object, the moment of inertia for any object depends on the chosen axis. To see this, let's take a simple example of two masses at the end of a massless (negligibly small mass) rod (Figure 10.23) and calculate the moment of inertia about two different axes. In this case, the summation over the masses is simple because the two masses at the end of the barbell can be approximated as point masses, and the sum therefore has only two terms.

In the case with the axis in the center of the barbell, each of the two masses $m$ is a distance $R$ away from the axis, giving a moment of inertia of

$$
I_{1}=m R^{2}+m R^{2}=2 m R^{2}
$$

In the case with the axis at the end of the barbell-passing through one of the masses-the moment of inertia is

$$
I_{2}=m(0)^{2}+m(2 R)^{2}=4 m R^{2}
$$

From this result, we can conclude that it is twice as hard to rotate the barbell about the end than about its center.

In this example, we had two point masses and the sum was simple to calculate. However, to deal with objects that are not point-like, we need to think carefully about each of the terms in the equation. The equation asks us to sum over each 'piece of mass' a certain distance from the axis of rotation. But what exactly does each 'piece of mass' mean? Recall that in our derivation of this equation, each piece of mass had the same magnitude of velocity, which means the whole piece had to have a single distance $r$ to the axis of rotation. However, this is not possible unless we take an infinitesimally small piece of mass dm, as shown in Figure 10.24.

The need to use an infinitesimally small piece of mass $d m$ suggests that we can write the moment of inertia by evaluating an integral over infinitesimal masses rather than doing a discrete sum over finite masses:

$$
I=\sum_{i} m_{i} r_{i}^{2} \text { becomes } I=\int r^{2} d m
$$

This, in fact, is the form we need to generalize the equation for complex shapes. It is best to work out specific examples in detail to get a feel for how to calculate the moment of inertia for specific shapes. This is the focus of most of the rest of this section.

A uniform thin rod with an axis through the center

Consider a uniform (density and shape) thin rod of mass $M$ and length $L$ as shown in Figure 10.25. We want a
thin rod so that we can assume the cross-sectional area of the rod is small and the rod can be thought of as a string of masses along a one-dimensional straight line. In this example, the axis of rotation is perpendicular to the rod and passes through the midpoint for simplicity. Our task is to calculate the moment of inertia about this axis. We orient the axes so that the $z$-axis is the axis of rotation and the $x$-axis passes through the length of the rod, as shown in the figure. This is a convenient choice because we can then integrate along the $x$-axis.

We define $d m$ to be a small element of mass making up the rod. The moment of inertia integral is an integral over the mass distribution. However, we know how to integrate over space, not over mass. We therefore need to find a way to relate mass to spatial variables. We do this using the linear mass density $\lambda$ of the object, which is the mass per unit length. Since the mass density of this object is uniform, we can write

$$
\lambda=\frac{m}{l} \text { or } m=\lambda l
$$

If we take the differential of each side of this equation, we find

$$
d m=d(\lambda l)=\lambda(d l)
$$

since $\lambda$ is constant. We chose to orient the rod along the $x$-axis for convenience-this is where that choice becomes very helpful. Note that a piece of the rod $d l$ lies completely along the $x$-axis and has a length $d x$; in fact, $d l=d x$ in this situation. We can therefore write $d m=\lambda(d x)$, giving us an integration variable that we know how to deal with. The distance of each piece of mass $d m$ from the axis is given by the variable $x$, as shown in the figure. Putting this all together, we obtain

$$
I=\int r^{2} d m=\int x^{2} d m=\int x^{2} \lambda d x
$$

The last step is to be careful about our limits of integration. The rod extends from $x=-L / 2$ to $x=L / 2$, since the axis is in the middle of the rod at $x=0$. This gives us

$$
\begin{aligned}
I & =\int_{-L / 2}^{L / 2} x^{2} \lambda d x=\left.\lambda \frac{x^{3}}{3}\right|_{-L / 2} ^{L / 2}=\lambda\left(\frac{1}{3}\right)\left[\left(\frac{L}{2}\right)^{3}-\left(\frac{-L}{2}\right)^{3}\right] \\
& =\lambda\left(\frac{1}{3}\right) \frac{L^{3}}{8}(2)=\frac{M}{L}\left(\frac{1}{3}\right) \frac{L^{3}}{8}(2)=\frac{1}{12} M L^{2}
\end{aligned}
$$

Next, we calculate the moment of inertia for the same uniform thin rod but with a different axis choice so we can compare the results. We would expect the moment of inertia to be smaller about an axis through the center of mass than the endpoint axis, just as it was for the barbell example at the start of this section. This happens because more mass is distributed farther from the axis of rotation.

## A uniform thin rod with axis at the end

Now consider the same uniform thin rod of mass $M$ and length $L$, but this time we move the axis of rotation to the end of the rod. We wish to find the moment of inertia about this new axis (Figure 10.26). The quantity $d m$ is again defined to be a small element of mass making up the rod. Just as before, we obtain

$$
I=\int r^{2} d m=\int x^{2} d m=\int x^{2} \lambda d x
$$

However, this time we have different limits of integration. The rod extends from $x=0$ to $x=L$, since the axis is at the end of the rod at $x=0$. Therefore we find

$$
\begin{aligned}
I & =\int_{0}^{L} x^{2} \lambda d x=\left.\lambda \frac{x^{3}}{3}\right|_{0} ^{L}=\lambda\left(\frac{1}{3}\right)\left[(L)^{3}-(0)^{3}\right] \\
& =\lambda\left(\frac{1}{3}\right) L^{3}=\frac{M}{L}\left(\frac{1}{3}\right) L^{3}=\frac{1}{3} M L^{2} .
\end{aligned}
$$

Note the rotational inertia of the rod about its endpoint is larger than the rotational inertia about its center (consistent with the barbell example) by a factor of four.

## The Parallel-Axis Theorem

The similarity between the process of finding the moment of inertia of a rod about an axis through its middle and about an axis through its end is striking, and suggests that there might be a simpler method for determining the moment of inertia for a rod about any axis parallel to the axis through the center of mass. Such an axis is called a parallel axis. There is a theorem for this, called the parallel-axis theorem, which we state here but do not derive in this text.

## Parallel-Axis Theorem

Let $m$ be the mass of an object and let $d$ be the distance from an axis through the object's center of mass to a new axis. Then we have

$$
I_{\text {parallel-axis }}=I_{\text {center of mass }}+m d^{2}
$$

Let's apply this to the rod examples solved above:

$$
I_{\text {end }}=I_{\text {center of mass }}+m d^{2}=\frac{1}{12} m L^{2}+m\left(\frac{L}{2}\right)^{2}=\left(\frac{1}{12}+\frac{1}{4}\right) m L^{2}=\frac{1}{3} m L^{2}
$$

This result agrees with our more lengthy calculation from above. This is a useful equation that we apply in some of the examples and problems.

## CHECK YOUR UNDERSTANDING 10.5

What is the moment of inertia of a cylinder of radius $R$ and mass $m$ about an axis through a point on the surface, as shown below?

## A uniform thin disk about an axis through the center

Integrating to find the moment of inertia of a two-dimensional object is a little bit trickier, but one shape is commonly done at this level of study-a uniform thin disk about an axis through its center (Figure 10.27).

Since the disk is thin, we can take the mass as distributed entirely in the $x y$-plane. We again start with the relationship for the surface mass density, which is the mass per unit surface area. Since it is uniform, the surface mass density $\sigma$ is constant:

$$
\sigma=\frac{m}{A} \quad \text { or } \quad \sigma A=m, \text { so } d m=\sigma(d A)
$$

Now we use a simplification for the area. The area can be thought of as made up of a series of thin rings, where each ring is a mass increment $d m$ of radius $r$ equidistanct from the axis, as shown in part (b) of the figure. The infinitesimal area of each ring $d A$ is therefore given by the length of each ring $(2 \pi r)$ times the infinitesimmal width of each ring $d r$ :

$$
A=\pi r^{2}, d A=d\left(\pi r^{2}\right)=\pi d r^{2}=2 \pi r d r
$$

The full area of the disk is then made up from adding all the thin rings with a radius range from 0 to $R$. This radius range then becomes our limits of integration for $d r$, that is, we integrate from $r=0$ to $r=R$. Putting this all together, we have

$$
\begin{aligned}
I & =\int_{0}^{R} r^{2} \sigma(2 \pi r) d r=2 \pi \sigma \int_{0}^{R} r^{3} d r=\left.2 \pi \sigma \frac{r^{4}}{4}\right|_{0} ^{R}=2 \pi \sigma\left(\frac{R^{4}}{4}-0\right) \\
& =2 \pi \frac{m}{A}\left(\frac{R^{4}}{4}\right)=2 \pi \frac{m}{\pi R^{2}}\left(\frac{R^{4}}{4}\right)=\frac{1}{2} m R^{2}
\end{aligned}
$$

Note that this agrees with the value given in Figure 10.20 .

## Calculating the moment of inertia for compound objects

Now consider a compound object such as that in Figure 10.28, which depicts a thin disk at the end of a thin rod. This cannot be easily integrated to find the moment of inertia because it is not a uniformly shaped object. However, if we go back to the initial definition of moment of inertia as a summation, we can reason that a compound object's moment of inertia can be found from the sum of each part of the object:

$$
I_{\text {total }}=\sum_{i} I_{i}
$$

It is important to note that the moments of inertia of the objects in Equation 10.21 are about a common axis. In the case of this object, that would be a rod of length $L$ rotating about its end, and a thin disk of radius $R$ rotating about an axis shifted off of the center by a distance $L+R$, where $R$ is the radius of the disk. Let's define the mass of the rod to be $m_{\mathrm{r}}$ and the mass of the disk to be $m_{\mathrm{d}}$.

The moment of inertia of the rod is simply $\frac{1}{3} m_{\mathrm{r}} L^{2}$, but we have to use the parallel-axis theorem to find the moment of inertia of the disk about the axis shown. The moment of inertia of the disk about its center is $\frac{1}{2} m_{\mathrm{d}} R^{2}$ and we apply the parallel-axis theorem $I_{\text {parallel-axis }}=I_{\text {center of mass }}+m d^{2}$ to find

$$
I_{\text {parallel-axis }}=\frac{1}{2} m_{\mathrm{d}} R^{2}+m_{\mathrm{d}}(L+R)^{2}
$$

Adding the moment of inertia of the rod plus the moment of inertia of the disk with a shifted axis of rotation, we find the moment of inertia for the compound object to be

$$
I_{\text {total }}=\frac{1}{3} m_{\mathrm{r}} L^{2}+\frac{1}{2} m_{\mathrm{d}} R^{2}+m_{\mathrm{d}}(L+R)^{2}
$$

Applying moment of inertia calculations to solve problems

Now let's examine some practical applications of moment of inertia calculations.

## EXAMPLE 10.11

## Person on a Merry-Go-Round

A $25-\mathrm{kg}$ child stands at a distance $r=1.0 \mathrm{~m}$ from the axis of a rotating merry-go-round (Figure 10.29). The merry-go-round can be approximated as a uniform solid disk with a mass of $500 \mathrm{~kg}$ and a radius of $2.0 \mathrm{~m}$. Find the moment of inertia of this system.

## Strategy

This problem involves the calculation of a moment of inertia. We are given the mass and distance to the axis of rotation of the child as well as the mass and radius of the merry-go-round. Since the mass and size of the child are much smaller than the merry-go-round, we can approximate the child as a point mass. The notation we use is $m_{\mathrm{c}}=25 \mathrm{~kg}, r_{\mathrm{c}}=1.0 \mathrm{~m}, m_{\mathrm{m}}=500 \mathrm{~kg}, r_{\mathrm{m}}=2.0 \mathrm{~m}$.

Our goal is to find $I_{\text {total }}=\sum_{i} I_{i}$.

## Solution

For the child, $I_{\mathrm{c}}=m_{\mathrm{c}} r^{2}$, and for the merry-go-round, $I_{\mathrm{m}}=\frac{1}{2} m_{\mathrm{m}} r^{2}$. Therefore

$$
I_{\text {total }}=25(1)^{2}+\frac{1}{2}(500)(2)^{2}=25+1000=1025 \mathrm{~kg} \cdot \mathrm{m}^{2}
$$

## Significance

The value should be close to the moment of inertia of the merry-go-round by itself because it has much more mass distributed away from the axis than the child does.

## EXAMPLE 10.12

## Rod and Solid Sphere

Find the moment of inertia of the rod and solid sphere combination about the two axes as shown below. The rod has length $0.5 \mathrm{~m}$ and mass $2.0 \mathrm{~kg}$. The radius of the sphere is $20.0 \mathrm{~cm}$ and has mass $1.0 \mathrm{~kg}$.

## Strategy

Since we have a compound object in both cases, we can use the parallel-axis theorem to find the moment of inertia about each axis. In (a), the center of mass of the sphere is located at a distance $L+R$ from the axis of rotation. In (b), the center of mass of the sphere is located a distance $R$ from the axis of rotation. In both cases, the moment of inertia of the rod is about an axis at one end. Refer to Table 10.4 for the moments of inertia for the individual objects.
a. $I_{\text {total }}=\sum_{i} I_{i}=I_{\mathrm{Rod}}+I_{\text {Sphere }} ;$

$I_{\text {Sphere }}=I_{\text {center of mass }}+m_{\text {Sphere }}(L+R)^{2}=\frac{2}{5} m_{\text {Sphere }} R^{2}+m_{\text {Sphere }}(L+R)^{2}$;

$I_{\text {total }}=I_{\text {Rod }}+I_{\text {Sphere }}=\frac{1}{3} m_{\text {Rod }} L^{2}+\frac{2}{5} m_{\text {Sphere }} R^{2}+m_{\text {Sphere }}(L+R)^{2} ;$

$I_{\text {total }}=\frac{1}{3}(2.0 \mathrm{~kg})(0.5 \mathrm{~m})^{2}+\frac{2}{5}(1.0 \mathrm{~kg})(0.2 \mathrm{~m})^{2}+(1.0 \mathrm{~kg})(0.5 \mathrm{~m}+0.2 \mathrm{~m})^{2} ;$

$I_{\text {total }}=(0.167+0.016+0.490) \mathrm{kg} \cdot \mathrm{m}^{2}=0.673 \mathrm{~kg} \cdot \mathrm{m}^{2}$.
b. $I_{\text {Sphere }}=\frac{2}{5} m_{\text {Sphere }} R^{2}+m_{\text {Sphere }} R^{2}$;

$I_{\text {total }}=I_{\text {Rod }}+I_{\text {Sphere }}=\frac{1}{3} m_{\text {Rod }} L^{2}+\frac{2}{5} m_{\text {Sphere }} R^{2}+m_{\text {Sphere }} R^{2}$

$I_{\text {total }}=\frac{1}{3}(2.0 \mathrm{~kg})(0.5 \mathrm{~m})^{2}+\frac{2}{5}(1.0 \mathrm{~kg})(0.2 \mathrm{~m})^{2}+(1.0 \mathrm{~kg})(0.2 \mathrm{~m})^{2} ;$

$I_{\text {total }}=(0.167+0.016+0.04) \mathrm{kg} \cdot \mathrm{m}^{2}=0.223 \mathrm{~kg} \cdot \mathrm{m}^{2}$.

## Significance

Using the parallel-axis theorem eases the computation of the moment of inertia of compound objects. We see that the moment of inertia is greater in (a) than (b). This is because the axis of rotation is closer to the center of mass of the system in (b). The simple analogy is that of a rod. The moment of inertia about one end is $\frac{1}{3} m L^{2}$, but the moment of inertia through the center of mass along its length is $\frac{1}{12} m L^{2}$.

## Angular Velocity of a Pendulum

A pendulum in the shape of a rod (Figure 10.30) is released from rest at an angle of $30^{\circ}$. It has a length $30 \mathrm{~cm}$ and mass $300 \mathrm{~g}$. What is its angular velocity at its lowest point?

## Strategy

Use conservation of energy to solve the problem. At the point of release, the pendulum has gravitational potential energy, which is determined from the height of the center of mass above its lowest point in the swing. At the bottom of the swing, all of the gravitational potential energy is converted into rotational kinetic energy.

## Solution

The change in potential energy is equal to the change in rotational kinetic energy, $\Delta U+\Delta K=0$.

At the top of the swing: $U=m g h_{\mathrm{cm}}=m g \frac{L}{2}(\cos \theta)$. At the bottom of the swing, $U=m g \frac{L}{2}$.

At the top of the swing, the rotational kinetic energy is $K=0$. At the bottom of the swing, $K=\frac{1}{2} I \omega^{2}$.

Therefore:

$$
\Delta U+\Delta K=0 \Rightarrow\left(m g \frac{L}{2}(1-\cos \theta)-0\right)+\left(0-\frac{1}{2} I \omega^{2}\right)=0
$$

or

$$
\frac{1}{2} I \omega^{2}=m g \frac{L}{2}(1-\cos \theta)
$$

Solving for $\omega$, we have

$$
\omega=\sqrt{m g \frac{L}{I}(1-\cos \theta)}=\sqrt{m g \frac{L}{1 / 3 m L^{2}}(1-\cos \theta)}=\sqrt{g \frac{3}{L}(1-\cos \theta)}
$$

Inserting numerical values, we have

$$
\omega=\sqrt{9.8 \mathrm{~m} / \mathrm{s}^{2} \frac{3}{0.3 \mathrm{~m}}(1-\cos 30)}=3.6 \mathrm{rad} / \mathrm{s}
$$

## Significance

Note that the angular velocity of the pendulum does not depend on its mass.

### 10.6 Torque

An important quantity for describing the dynamics of a rotating rigid body is torque. We see the application of torque in many ways in our world. We all have an intuition about torque, as when we use a large wrench to unscrew a stubborn bolt. Torque is at work in unseen ways, as when we press on the accelerator in a car, causing the engine to put additional torque on the drive train. Or every time we move our bodies from a standing position, we apply a torque to our limbs. In this section, we define torque and make an argument for the equation for calculating torque for a rigid body with fixed-axis rotation.

## Defining Torque

So far we have defined many variables that are rotational equivalents to their translational counterparts. Let's consider what the counterpart to force must be. Since forces change the translational motion of objects, the rotational counterpart must be related to changing the rotational motion of an object about an axis. We call this rotational counterpart torque.

In everyday life, we rotate objects about an axis all the time, so intuitively we already know much about torque. Consider, for example, how we rotate a door to open it. First, we know that a door opens slowly if we push too close to its hinges; it is more efficient to rotate a door open if we push far from the hinges. Second, we know that we should push perpendicular to the plane of the door; if we push parallel to the plane of the door, we are not able to rotate it. Third, the larger the force, the more effective it is in opening the door; the harder you push, the more rapidly the door opens. The first point implies that the farther the force is applied from the axis of rotation, the greater the angular acceleration; the second implies that the effectiveness depends on the angle at which the force is applied; the third implies that the magnitude of the force must also be part of the equation. Note that for rotation in a plane, torque has two possible directions. Torque is either clockwise or counterclockwise relative to the chosen pivot point. Figure 10.31 shows counterclockwise rotations.

Now let's consider how to define torques in the general three-dimensional case.

## Torque

When a force $\overrightarrow{\mathbf{F}}$ is applied to a point $P$ whose position is $\overrightarrow{\mathbf{r}}$ relative to $O$ (Figure 10.32), the torque $\vec{\tau}$ around $O$ is

$$
\overrightarrow{\boldsymbol{\tau}}=\overrightarrow{\mathbf{r}} \times \overrightarrow{\mathbf{F}}
$$

From the definition of the cross product, the torque $\overrightarrow{\boldsymbol{\tau}}$ is perpendicular to the plane containing $\overrightarrow{\mathbf{r}}$ and $\overrightarrow{\mathbf{F}}$ and has magnitude

$$
|\vec{\tau}|=|\overrightarrow{\mathbf{r}} \times \overrightarrow{\mathbf{F}}|=r F \sin \theta
$$

where $\theta$ is the angle between the vectors $\overrightarrow{\mathbf{r}}$ and $\overrightarrow{\mathbf{F}}$. The SI unit of torque is newtons times meters, usually written as $\mathrm{N} \cdot \mathrm{m}$. The quantity $r_{\perp}=r \sin \theta$ is the perpendicular distance from $O$ to the line determined by the vector $\overrightarrow{\mathbf{F}}$ and is called the lever arm. Note that the greater the lever arm, the greater the magnitude of the torque. In terms of the lever arm, the magnitude of the torque is

$$
|\vec{\tau}|=r_{\perp} F
$$

The cross product $\overrightarrow{\mathbf{r}} \times \overrightarrow{\mathbf{F}}$ also tells us the sign of the torque. In Figure 10.32, the cross product $\overrightarrow{\mathbf{r}} \times \overrightarrow{\mathbf{F}}$ is along the positive $z$-axis, which by convention is a positive torque. If $\overrightarrow{\mathbf{r}} \times \overrightarrow{\mathbf{F}}$ is along the negative $z$-axis, this produces a negative torque.

If we consider a disk that is free to rotate about an axis through the center, as shown in Figure 10.33, we can see how the angle between the radius $\overrightarrow{\mathbf{r}}$ and the force $\overrightarrow{\mathbf{F}}$ affects the magnitude of the torque. If the angle is zero, the torque is zero; if the angle is $90^{\circ}$, the torque is maximum. The torque in Figure 10.33 is positive because the direction of the torque by the right-hand rule is out of the page along the positive $z$-axis. The disk rotates counterclockwise due to the torque, in the same direction as a positive angular acceleration.

Any number of torques can be calculated about a given axis. The individual torques add to produce a net torque about the axis. When the appropriate sign (positive or negative) is assigned to the magnitudes of individual torques about a specified axis, the net torque about the axis is the sum of the individual torques:

$$
\overrightarrow{\boldsymbol{\tau}}_{\mathrm{net}}=\sum_{i}\left|\overrightarrow{\boldsymbol{\tau}}_{i}\right|
$$

## Calculating Net Torque for Rigid Bodies on a Fixed Axis

In the following examples, we calculate the torque both abstractly and as applied to a rigid body.

We first introduce a problem-solving strategy.

## PROBLEM-SOLVING STRATEGY

## Finding Net Torque

1. Choose a coordinate system with the pivot point or axis of rotation as the origin of the selected coordinate system.
2. Determine the angle between the lever arm $\overrightarrow{\mathbf{r}}$ and the force vector.
3. Take the cross product of $\overrightarrow{\mathbf{r}}$ and $\overrightarrow{\mathbf{F}}$ to determine if the torque is positive or negative about the pivot point or axis.
4. Evaluate the magnitude of the torque using $r_{\perp} F$.
5. Assign the appropriate sign, positive or negative, to the magnitude.
6. Sum the torques to find the net torque.

## EXAMPLE 10.14

## Calculating Torque

Four forces are shown in Figure 10.34 at particular locations and orientations with respect to a given
$x y$-coordinate system. Find the torque due to each force about the origin, then use your results to find the net torque about the origin.

## Strategy

This problem requires calculating torque. All known quantities--forces with directions and lever arms--are given in the figure. The goal is to find each individual torque and the net torque by summing the individual torques. Be careful to assign the correct sign to each torque by using the cross product of $\overrightarrow{\mathbf{r}}$ and the force vector $\overrightarrow{\mathbf{F}}$.

## Solution

Use $|\overrightarrow{\boldsymbol{\tau}}|=r_{\perp} F=r F \sin \theta$ to find the magnitude and $\overrightarrow{\boldsymbol{\tau}}=\overrightarrow{\mathbf{r}} \times \overrightarrow{\mathbf{F}}$ to determine the sign of the torque.

The torque from force $40 \mathrm{~N}$ in the first quadrant is given by (4)(40) $\sin 90^{\circ}=160 \mathrm{~N} \cdot \mathrm{m}$.

The cross product of $\overrightarrow{\mathbf{r}}$ and $\overrightarrow{\mathbf{F}}$ is out of the page, positive.

The torque from force $20 \mathrm{~N}$ in the third quadrant is given by $-(3)(20) \sin 90^{\circ}=-60 \mathrm{~N} \cdot \mathrm{m}$.

The cross product of $\overrightarrow{\mathbf{r}}$ and $\overrightarrow{\mathbf{F}}$ is into the page, so it is negative.

The torque from force $30 \mathrm{~N}$ in the third quadrant is given by (5)(30) $\sin 53^{\circ}=120 \mathrm{~N} \cdot \mathrm{m}$.

The cross product of $\overrightarrow{\mathbf{r}}$ and $\overrightarrow{\mathbf{F}}$ is out of the page, positive.

The torque from force $20 \mathrm{~N}$ in the second quadrant is given by $(1)(20) \sin 30^{\circ}=10 \mathrm{~N} \cdot \mathrm{m}$.

The cross product of $\overrightarrow{\mathbf{r}}$ and $\overrightarrow{\mathbf{F}}$ is out of the page.

The net torque is therefore $\tau_{\text {net }}=\sum_{i}\left|\boldsymbol{\tau}_{i}\right|=160-60+120+10=230 \mathrm{~N} \cdot \mathrm{m}$.

## Significance

Note that each force that acts in the counterclockwise direction has a positive torque, whereas each force that acts in the clockwise direction has a negative torque. The torque is greater when the distance, force, or perpendicular components are greater.

## Calculating Torque on a rigid body

Figure 10.35 shows several forces acting at different locations and angles on a flywheel. We have $\left|\overrightarrow{\mathbf{F}}_{1}\right|=20 \mathrm{~N}$, $\left|\overrightarrow{\mathbf{F}}_{2}\right|=30 \mathrm{~N},\left|\overrightarrow{\mathbf{F}}_{3}\right|=30 \mathrm{~N}$, and $r=0.5 \mathrm{~m}$. Find the net torque on the flywheel about an axis through the center.

## Strategy

We calculate each torque individually, using the cross product, and determine the sign of the torque. Then we sum the torques to find the net torque.

## Solution

We start with $\overrightarrow{\mathbf{F}}_{1}$. If we look at Figure 10.35, we see that $\overrightarrow{\mathbf{F}}_{1}$ makes an angle of $90^{\circ}+60^{\circ}$ with the radius vector $\overrightarrow{\mathbf{r}}$. Taking the cross product, we see that it is out of the page and so is positive. We also see this from calculating its magnitude:

$$
\left|\overrightarrow{\boldsymbol{\tau}}_{1}\right|=r F_{1} \sin 150^{\circ}=0.5 \mathrm{~m}(20 \mathrm{~N})(0.5)=5.0 \mathrm{~N} \cdot \mathrm{m} .
$$

Next we look at $\overrightarrow{\mathbf{F}}_{2}$. The angle between $\overrightarrow{\mathbf{F}}_{2}$ and $\overrightarrow{\mathbf{r}}$ is $90^{\circ}$ and the cross product is into the page so the torque is negative. Its value is

$$
\left|\vec{\tau}_{2}\right|=-r F_{2} \sin 90^{\circ}=-0.5 \mathrm{~m}(30 \mathrm{~N})=-15.0 \mathrm{~N} \cdot \mathrm{m} .
$$

When we evaluate the torque due to $\overrightarrow{\mathbf{F}}_{3}$, we see that the angle it makes with $\overrightarrow{\mathbf{r}}$ is zero so $\overrightarrow{\mathbf{r}} \times \overrightarrow{\mathbf{F}}_{3}=0$. Therefore, $\overrightarrow{\mathbf{F}}_{3}$ does not produce any torque on the flywheel.

We evaluate the sum of the torques:

$$
\tau_{\text {net }}=\sum_{i}\left|\boldsymbol{\tau}_{i}\right|=5-15=-10 \mathrm{~N} \cdot \mathrm{m}
$$

## Significance

The axis of rotation is at the center of mass of the flywheel. Since the flywheel is on a fixed axis, it is not free to translate. If it were on a frictionless surface and not fixed in place, $\overrightarrow{\mathbf{F}}_{3}$ would cause the flywheel to translate, as well as $\overrightarrow{\mathbf{F}}_{1}$. Its motion would be a combination of translation and rotation.

### 10.7 Newton's Second Law for Rotation

In this section, we put together all the pieces learned so far in this chapter to analyze the dynamics of rotating rigid bodies. We have analyzed motion with kinematics and rotational kinetic energy but have not yet connected these ideas with force and/or torque. In this section, we introduce the rotational equivalent to Newton's second law of motion and apply it to rigid bodies with fixed-axis rotation.

## Newton's Second Law for Rotation

We have thus far found many counterparts to the translational terms used throughout this text, most recently, torque, the rotational analog to force. This raises the question: Is there an analogous equation to Newton's second law, $\Sigma \overrightarrow{\mathbf{F}}=m \overrightarrow{\mathbf{a}}$, which involves torque and rotational motion? To investigate this, we start with Newton's second law for a single particle rotating around an axis and executing circular motion. Let's exert a force $\overrightarrow{\mathbf{F}}$ on a point mass $m$ that is at a distance $r$ from a pivot point (Figure 10.37). The particle is constrained to move in a circular path with fixed radius and the force is tangent to the circle. We apply Newton's second law to determine the magnitude of the acceleration $a=F / m$ in the direction of $\overrightarrow{\mathbf{F}}$. Recall that the magnitude of the tangential acceleration is proportional to the magnitude of the angular acceleration by $a=r \alpha$. Substituting this expression into Newton's second law, we obtain

$$
F=m r \alpha
$$

Multiply both sides of this equation by $r$,

$$
r F=m r^{2} \alpha
$$

Note that the left side of this equation is the torque about the axis of rotation, where $r$ is the lever arm and $F$ is the force, perpendicular to $r$. Recall that the moment of inertia for a point particle is $I=m r^{2}$. The torque applied perpendicularly to the point mass in Figure 10.37 is therefore

$$
\tau=I \alpha
$$

The torque on the particle is equal to the moment of inertia about the rotation axis times the angular acceleration. We can generalize this equation to a rigid body rotating about a fixed axis.

## Newton's Second Law for Rotation

If more than one torque acts on a rigid body about a fixed axis, then the sum of the torques equals the moment of inertia times the angular acceleration:

$$
\sum_{i} \tau_{i}=I \alpha
$$

The term $I \alpha$ is a scalar quantity and can be positive or negative (counterclockwise or clockwise) depending upon the sign of the net torque. Remember the convention that counterclockwise angular acceleration is positive. Thus, if a rigid body is rotating clockwise and experiences a positive torque (counterclockwise), the angular acceleration is positive.

Equation 10.25 is Newton's second law for rotation and tells us how to relate torque, moment of inertia, and rotational kinematics. This is called the equation for rotational dynamics. With this equation, we can solve a whole class of problems involving force and rotation. It makes sense that the relationship for how much force it takes to rotate a body would include the moment of inertia, since that is the quantity that tells us how easy or hard it is to change the rotational motion of an object.

## Deriving Newton's Second Law for Rotation in Vector Form

As before, when we found the angular acceleration, we may also find the torque vector. The second law $\Sigma \overrightarrow{\mathbf{F}}=m \overrightarrow{\mathbf{a}}$ tells us the relationship between net force and how to change the translational motion of an object. We have a vector rotational equivalent of this equation, which can be found by using Equation 10.7 and Figure 10.8. Equation 10.7 relates the angular acceleration to the position and tangential acceleration vectors:

$$
\overrightarrow{\mathbf{a}}=\overrightarrow{\boldsymbol{\alpha}} \times \overrightarrow{\mathbf{r}}
$$

We form the cross product of this equation with $\overrightarrow{\mathbf{r}}$ and use a cross product identity (note that $\overrightarrow{\mathbf{r}} \cdot \overrightarrow{\boldsymbol{\alpha}}=0$ ):

$$
\overrightarrow{\mathbf{r}} \times \overrightarrow{\mathbf{a}}=\overrightarrow{\mathbf{r}} \times(\overrightarrow{\boldsymbol{\alpha}} \times \overrightarrow{\mathbf{r}})=\overrightarrow{\boldsymbol{\alpha}}(\overrightarrow{\mathbf{r}} \cdot \overrightarrow{\mathbf{r}})-\overrightarrow{\mathbf{r}}(\overrightarrow{\mathbf{r}} \cdot \overrightarrow{\boldsymbol{\alpha}})=\overrightarrow{\boldsymbol{\alpha}}(\overrightarrow{\mathbf{r}} \cdot \overrightarrow{\mathbf{r}})=\overrightarrow{\boldsymbol{\alpha}} r^{2}
$$

We now form the cross product of Newton's second law with the position vector $\overrightarrow{\mathbf{r}}$,

$$
\Sigma(\overrightarrow{\mathbf{r}} \times \overrightarrow{\mathbf{F}})=\overrightarrow{\mathbf{r}} \times(m \overrightarrow{\mathbf{a}})=m \overrightarrow{\mathbf{r}} \times \overrightarrow{\mathbf{a}}=m r^{2} \overrightarrow{\boldsymbol{\alpha}}
$$

Identifying the first term on the left as the sum of the torques, and $m r^{2}$ as the moment of inertia, we arrive at Newton's second law of rotation in vector form:

$$
\Sigma \vec{\tau}=I \overrightarrow{\boldsymbol{\alpha}}
$$

This equation is exactly Equation 10.25 but with the torque and angular acceleration as vectors. An important point is that the torque vector is in the same direction as the angular acceleration.

## Applying the Rotational Dynamics Equation

Before we apply the rotational dynamics equation to some everyday situations, let's review a general problemsolving strategy for use with this category of problems.

## PROBLEM-SOLVING STRATEGY

## Rotational Dynamics

1. Examine the situation to determine that torque and mass are involved in the rotation. Draw a careful sketch of the situation.
2. Determine the system of interest.
3. Draw a free-body diagram. That is, draw and label all external forces acting on the system of interest.
4. Identify the pivot point. If the object is in equilibrium, it must be in equilibrium for all possible pivot points--chose the one that simplifies your work the most.
5. Apply $\sum_{i} \tau_{i}=I \alpha$, the rotational equivalent of Newton's second law, to solve the problem. Care must be taken to use the correct moment of inertia and to consider the torque about the point of rotation.
6. As always, check the solution to see if it is reasonable.

## EXAMPLE 10.16

## Calculating the Effect of Mass Distribution on a Merry-Go-Round

Consider the father pushing a playground merry-go-round in Figure 10.38 . He exerts a force of $250 \mathrm{~N}$ at the edge of the 50.0-kg merry-go-round, which has a $1.50-\mathrm{m}$ radius. Calculate the angular acceleration produced (a) when no one is on the merry-go-round and (b) when an $18.0-\mathrm{kg}$ child sits $1.25 \mathrm{~m}$ away from the center. Consider the merry-go-round itself to be a uniform disk with negligible friction.

## Strategy

The net torque is given directly by the expression $\sum_{i} \tau_{i}=I \alpha$, To solve for $\alpha$, we must first calculate the net torque $\tau$ (which is the same in both cases) and moment of inertia $I$ (which is greater in the second case).

## Solution

a. The moment of inertia of a solid disk about this axis is given in Figure 10.20 to be

$$
\frac{1}{2} M R^{2}
$$

We have $M=50.0 \mathrm{~kg}$ and $R=1.50 \mathrm{~m}$, so

$$
I=(0.500)(50.0 \mathrm{~kg})(1.50 \mathrm{~m})^{2}=56.25 \mathrm{~kg}-\mathrm{m}^{2}
$$

To find the net torque, we note that the applied force is perpendicular to the radius and friction is negligible, so that

$$
\tau=r F \sin \theta=(1.50 \mathrm{~m})(250.0 \mathrm{~N})=375.0 \mathrm{~N}-\mathrm{m}
$$

Now, after we substitute the known values, we find the angular acceleration to be

$$
\alpha=\frac{\tau}{I}=\frac{375.0 \mathrm{~N}-\mathrm{m}}{56.25 \mathrm{~kg}-\mathrm{m}^{2}}=6.67 \frac{\mathrm{rad}}{\mathrm{s}^{2}}
$$

b. We expect the angular acceleration for the system to be less in this part because the moment of inertia is greater when the child is on the merry-go-round. To find the total moment of inertia $I$, we first find the child's moment of inertia $\boldsymbol{I}_{\mathrm{c}}$ by approximating the child as a point mass at a distance of $1.25 \mathrm{~m}$ from the axis. Then

$$
I_{\mathrm{c}}=m R^{2}=(18.0 \mathrm{~kg})(1.25 \mathrm{~m})^{2}=28.13 \mathrm{~kg}-\mathrm{m}^{2}
$$

The total moment of inertia is the sum of the moments of inertia of the merry-go-round and the child (about the same axis):

$$
I=28.13 \mathrm{~kg}-\mathrm{m}^{2}+56.25 \mathrm{~kg}-\mathrm{m}^{2}=84.38 \mathrm{~kg}-\mathrm{m}^{2}
$$

Substituting known values into the equation for $\alpha$ gives

$$
\alpha=\frac{\tau}{I}=\frac{375.0 \mathrm{~N}-\mathrm{m}}{84.38 \mathrm{~kg}-\mathrm{m}^{2}}=4.44 \frac{\mathrm{rad}}{\mathrm{s}^{2}}
$$

## Significance

The angular acceleration is less when the child is on the merry-go-round than when the merry-go-round is empty, as expected. The angular accelerations found are quite large, partly due to the fact that friction was considered to be negligible. If, for example, the father kept pushing perpendicularly for $2.00 \mathrm{~s}$, he would give the merry-go-round an angular velocity of $13.3 \mathrm{rad} / \mathrm{s}$ when it is empty but only $8.89 \mathrm{rad} / \mathrm{s}$ when the child is on it. In terms of revolutions per second, these angular velocities are $2.12 \mathrm{rev} / \mathrm{s}$ and $1.41 \mathrm{rev} / \mathrm{s}$, respectively. The
father would end up running at about $50 \mathrm{~km} / \mathrm{h}$ in the first case.

### 10.8 Work and Power for Rotational Motion

Thus far in the chapter, we have extensively addressed kinematics and dynamics for rotating rigid bodies around a fixed axis. In this final section, we define work and power within the context of rotation about a fixed axis, which has applications to both physics and engineering. The discussion of work and power makes our treatment of rotational motion almost complete, with the exception of rolling motion and angular momentum, which are discussed in Angular Momentum. We begin this section with a treatment of the work-energy theorem for rotation.

## Work for Rotational Motion

Now that we have determined how to calculate kinetic energy for rotating rigid bodies, we can proceed with a discussion of the work done on a rigid body rotating about a fixed axis. Figure 10.39 shows a rigid body that has rotated through an angle $d \theta$ from $A$ to $B$ while under the influence of a force $\overrightarrow{\mathbf{F}}$. The external force $\overrightarrow{\mathbf{F}}$ is applied to point $P$, whose position is $\overrightarrow{\mathbf{r}}$, and the rigid body is constrained to rotate about a fixed axis that is perpendicular to the page and passes through $O$. The rotational axis is fixed, so the vector $\overrightarrow{\mathbf{r}}$ moves in a circle of radius $r$, and the vector $d \overrightarrow{\mathbf{s}}$ is perpendicular to $\overrightarrow{\mathbf{r}}$.

From Equation 10.2, we have

$$
\overrightarrow{\mathbf{s}}=\overrightarrow{\boldsymbol{\theta}} \times \overrightarrow{\mathbf{r}}
$$

Thus,

$$
d \overrightarrow{\mathbf{s}}=d(\overrightarrow{\boldsymbol{\theta}} \times \overrightarrow{\mathbf{r}})=d \overrightarrow{\boldsymbol{\theta}} \times \overrightarrow{\mathbf{r}}+d \overrightarrow{\mathbf{r}} \times \overrightarrow{\boldsymbol{\theta}}=d \overrightarrow{\boldsymbol{\theta}} \times \overrightarrow{\mathbf{r}}
$$

Note that $d \overrightarrow{\mathbf{r}}$ is zero because $\overrightarrow{\mathbf{r}}$ is fixed on the rigid body from the origin $O$ to point $P$. Using the definition of work, we obtain

$$
W=\int \sum \overrightarrow{\mathbf{F}} \cdot d \overrightarrow{\mathbf{s}}=\int \sum \overrightarrow{\mathbf{F}} \cdot(d \overrightarrow{\boldsymbol{\theta}} \times \overrightarrow{\mathbf{r}})=\int d \overrightarrow{\boldsymbol{\theta}} \cdot\left(\overrightarrow{\mathbf{r}} \times \sum \overrightarrow{\mathbf{F}}\right)
$$

where we used the identity $\overrightarrow{\mathbf{a}} \cdot(\overrightarrow{\mathbf{b}} \times \overrightarrow{\mathbf{c}})=\overrightarrow{\mathbf{b}} \cdot(\overrightarrow{\mathbf{c}} \times \overrightarrow{\mathbf{a}})$. Noting that $\left(\overrightarrow{\mathbf{r}} \times \sum \vec{F}\right)=\sum \overrightarrow{\boldsymbol{\tau}}$, we arrive at the expression for the rotational work done on a rigid body:

$$
W=\int \sum \overrightarrow{\boldsymbol{\tau}} \cdot d \overrightarrow{\boldsymbol{\theta}}
$$

The total work done on a rigid body is the sum of the torques integrated over the angle through which the body rotates. The incremental work is

$$
d W=\left(\sum_{i} \tau_{i}\right) d \theta
$$

where we have taken the dot product in Equation 10.27, leaving only torques along the axis of rotation. In a rigid body, all particles rotate through the same angle; thus the work of every external force is equal to the torque times the common incremental angle $d \theta$. The quantity $\left(\sum_{i} \tau_{i}\right)$ is the net torque on the body due to external forces.

Similarly, we found the kinetic energy of a rigid body rotating around a fixed axis by summing the kinetic energy of each particle that makes up the rigid body. Since the work-energy theorem $W_{i}=\Delta K_{i}$ is valid for each particle, it is valid for the sum of the particles and the entire body.

## Work-Energy Theorem for Rotation

The work-energy theorem for a rigid body rotating around a fixed axis is

$$
W_{A B}=K_{B}-K_{A}
$$

where

$$
K=\frac{1}{2} I \omega^{2}
$$

and the rotational work done by a net force rotating a body from point $A$ to point $B$ is

$$
W_{A B}=\int_{\theta_{A}}^{\theta_{B}}\left(\sum_{i} \tau_{i}\right) d \theta
$$

We give a strategy for using this equation when analyzing rotational motion.

## Work-Energy Theorem for Rotational Motion

1. Identify the forces on the body and draw a free-body diagram. Calculate the torque for each force.
2. Calculate the work done during the body's rotation by every torque.
3. Apply the work-energy theorem by equating the net work done on the body to the change in rotational kinetic energy.

Let's look at two examples and use the work-energy theorem to analyze rotational motion.

## EXAMPLE 10.17

## Rotational Work and Energy

A $12.0 \mathrm{~N} \cdot \mathrm{m}$ torque is applied to a flywheel that rotates about a fixed axis and has a moment of inertia of $30.0 \mathrm{~kg} \cdot \mathrm{m}^{2}$. If the flywheel is initially at rest, what is its angular velocity after it has turned through eight revolutions?

## Strategy

We apply the work-energy theorem. We know from the problem description what the torque is and the angular displacement of the flywheel. Then we can solve for the final angular velocity.

## Solution

The flywheel turns through eight revolutions, which is $16 \pi$ radians. The work done by the torque, which is constant and therefore can come outside the integral in Equation 10.30, is

$$
W_{A B}=\tau\left(\theta_{B}-\theta_{A}\right)
$$

We apply the work-energy theorem:

$$
W_{A B}=\tau\left(\theta_{B}-\theta_{A}\right)=\frac{1}{2} I \omega_{B}^{2}-\frac{1}{2} I \omega_{A}^{2}
$$

With $\tau=12.0 \mathrm{~N} \cdot \mathrm{m}, \theta_{B}-\theta_{A}=16.0 \pi \mathrm{rad}, I=30.0 \mathrm{~kg} \cdot \mathrm{m}^{2}$, and $\omega_{A}=0$, we have

$$
12.0 \mathrm{~N}-\mathrm{m}(16.0 \pi \mathrm{rad})=\frac{1}{2}\left(30.0 \mathrm{~kg} \cdot \mathrm{m}^{2}\right)\left(\omega_{B}^{2}\right)-0
$$

Therefore,

$$
\omega_{B}=6.3 \mathrm{rad} / \mathrm{s}
$$

This is the angular velocity of the flywheel after eight revolutions.

## Significance

The work-energy theorem provides an efficient way to analyze rotational motion, connecting torque with rotational kinetic energy.

## EXAMPLE 10.18

## Rotational Work: A Pulley

A string wrapped around the pulley in Figure 10.40 is pulled with a constant downward force $\overrightarrow{\mathbf{F}}$ of magnitude $50 \mathrm{~N}$. The radius $R$ and moment of inertia $I$ of the pulley are $0.10 \mathrm{~m}$ and $2.5 \times 10^{-3} \mathrm{~kg}-\mathrm{m}^{2}$, respectively. If the string does not slip, what is the angular velocity of the pulley after $1.0 \mathrm{~m}$ of string has unwound? Assume the pulley starts from rest.

## Strategy

Looking at the free-body diagram, we see that neither $\overrightarrow{\mathbf{B}}$, the force on the bearings of the pulley, nor $M \overrightarrow{\mathbf{g}}$, the weight of the pulley, exerts a torque around the rotational axis, and therefore does no work on the pulley. As the pulley rotates through an angle $\theta, \overrightarrow{\mathbf{F}}$ acts through a distance $d$ such that $d=R \theta$.

## Solution

Since the torque due to $\overrightarrow{\mathbf{F}}$ has magnitude $\tau=R F$, we have

$$
W=\tau \theta=(F R) \theta=F d
$$

If the force on the string acts through a distance of $1.0 \mathrm{~m}$, we have, from the work-energy theorem,

$$
\begin{aligned}
W_{A B} & =K_{B}-K_{A} \\
F d & =\frac{1}{2} I \omega^{2}-0 \\
(50.0 \mathrm{~N})(1.0 \mathrm{~m}) & =\frac{1}{2}\left(2.5 \times 10^{-3} \mathrm{~kg}-\mathrm{m}^{2}\right) \omega^{2}
\end{aligned}
$$

Solving for $\omega$, we obtain

$$
\omega=200.0 \mathrm{rad} / \mathrm{s}
$$

## Power for Rotational Motion

Power always comes up in the discussion of applications in engineering and physics. Power for rotational motion is equally as important as power in linear motion and can be derived in a similar way as in linear motion when the force is a constant. The linear power when the force is a constant is $\boldsymbol{P}=\overrightarrow{\mathbf{F}} \cdot \overrightarrow{\mathbf{v}}$. If the net torque is constant over the angular displacement, Equation 10.25 simplifies and the net torque can be taken out of the integral. In the following discussion, we assume the net torque is constant. We can apply the definition of power derived in Power to rotational motion. From Work and Kinetic Energy, the instantaneous power (or just power) is defined as the rate of doing work,

$$
P=\frac{d W}{d t}
$$

If we have a constant net torque, Equation 10.25 becomes $W=\tau \theta$ and the power is

$$
P=\frac{d W}{d t}=\frac{d}{d t}(\tau \theta)=\tau \frac{d \theta}{d t}
$$

or

$$
P=\tau \omega
$$

## EXAMPLE 10.19

## Torque on a Boat Propeller

A boat engine operating at $9.0 \times 10^{4} \mathrm{~W}$ is running at $300 \mathrm{rev} / \mathrm{min}$. What is the torque on the propeller shaft?

## Strategy

We are given the rotation rate in rev/min and the power consumption, so we can easily calculate the torque.

## Solution

$$
\begin{gathered}
300.0 \mathrm{rev} / \mathrm{min}=31.4 \mathrm{rad} / \mathrm{s} \\
\tau=\frac{P}{\omega}=\frac{9.0 \times 10^{4} \mathrm{~N} \cdot \mathrm{m} / \mathrm{s}}{31.4 \mathrm{rad} / \mathrm{s}}=2864.8 \mathrm{~N} \cdot \mathrm{m}
\end{gathered}
$$

## Significance

It is important to note the radian is a dimensionless unit because its definition is the ratio of two lengths. It therefore does not appear in the solution.

## Rotational and Translational Relationships Summarized

The rotational quantities and their linear analog are summarized in three tables. Table 10.5 summarizes the rotational variables for circular motion about a fixed axis with their linear analogs and the connecting equation, except for the centripetal acceleration, which stands by itself. Table 10.6 summarizes the rotational and translational kinematic equations. Table 10.7 summarizes the rotational dynamics equations with their linear analogs.

| Rotational | Translational | Relationship |
| :--- | :--- | :--- |
| $\theta$ | $x$ | $\theta=\frac{s}{r}$ |
| $\omega$ | $v_{t}$ | $\omega=\frac{v_{t}}{r}$ |
| $\alpha$ | $a_{\mathrm{t}}$ | $\alpha=\frac{a_{\mathrm{t}}}{r}$ |
|  | $a_{\mathrm{c}}$ | $a_{\mathrm{c}}=\frac{v_{\mathrm{t}}^{2}}{r}$ |

Table 10.5 Rotational and Translational Variables: Summary

| Rotational | Translational |
| :--- | :--- |
| $\theta_{\mathrm{f}}=\theta_{0}+\bar{\omega} t$ | $x=x_{0}+\bar{v} t$ |
| $\omega_{\mathrm{f}}=\omega_{0}+\alpha t$ | $v_{\mathrm{f}}=v_{0}+a t$ |

Rotational

$$
\begin{array}{l|l}
\theta_{\mathrm{f}}=\theta_{0}+\omega_{0} t+\frac{1}{2} \alpha t^{2} & x_{\mathrm{f}}=x_{0}+v_{0} t+\frac{1}{2} a t^{2} \\
\hline \omega_{\mathrm{f}}^{2}=\omega_{0}^{2}+2 \alpha(\Delta \theta) & v_{\mathrm{f}}^{2}=v_{0}^{2}+2 a(\Delta x)
\end{array}
$$

Table 10.6 Rotational and Translational Kinematic Equations: Summary

| Rotational | Translational |
| :--- | :--- |
| $I=\sum_{i} m_{i} r_{i}^{2}$ | $m$ |
| $K=\frac{1}{2} I \omega^{2}$ | $K=\frac{1}{2} m v^{2}$ |
| $\sum_{i} \tau_{i}=I \alpha$ | $\sum_{i} \overrightarrow{\mathbf{F}}_{i}=m \overrightarrow{\mathbf{a}}$ |
| $W_{A B}=\int_{\theta_{A}}^{\theta_{R}}\left(\sum_{i} \tau_{i}\right) d \theta$ | $W=\int \overrightarrow{\mathbf{F}} \cdot d \overrightarrow{\mathbf{s}}$ |
| $P=\tau \omega$ | $P=\overrightarrow{\mathbf{F}} \cdot \overrightarrow{\mathbf{v}}$ |

Table 10.7 Rotational and Translational Equations: Dynamics

