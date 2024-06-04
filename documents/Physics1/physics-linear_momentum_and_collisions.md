# CHAPTER 9 <br> Linear Momentum and Collisions 

INTRODUCTION The concepts of work, energy, and the work-energy theorem are valuable for two primary reasons: First, they are powerful computational tools, making it much easier to analyze complex physical systems than is possible using Newton's laws directly (for example, systems with nonconstant forces); and second, the observation that the total energy of a closed system is conserved means that the system can only
evolve in ways that are consistent with energy conservation. In other words, a system cannot evolve randomly; it can only change in ways that conserve energy.

In this chapter, we develop and define another conserved quantity, called linear momentum, and another relationship (the impulse-momentum theorem), which will put an additional constraint on how a system evolves in time. Conservation of momentum is useful for understanding collisions, such as that shown in the above image. It is just as powerful, just as important, and just as useful as conservation of energy and the workenergy theorem.

### 9.1 Linear Momentum

Our study of kinetic energy showed that a complete understanding of an object's motion must include both its mass and its velocity $\left(K=(1 / 2) m v^{2}\right)$. However, as powerful as this concept is, it does not include any information about the direction of the moving object's velocity vector. We'll now define a physical quantity that includes direction.

Like kinetic energy, this quantity includes both mass and velocity; like kinetic energy, it is a way of characterizing the "quantity of motion" of an object. It is given the name momentum (from the Latin word movimentum, meaning "movement"), and it is represented by the symbol $p$.

## Momentum

The momentum $p$ of an object is the product of its mass and its velocity:

$$
\overrightarrow{\mathbf{p}}=m \overrightarrow{\mathbf{v}} .
$$

As shown in Figure 9.2, momentum is a vector quantity (since velocity is). This is one of the things that makes momentum useful and not a duplication of kinetic energy. It is perhaps most useful when determining whether an object's motion is difficult to change (Figure 9.3) or easy to change (Figure 9.4).

Unlike kinetic energy, momentum depends equally on an object's mass and velocity. For example, as you will learn when you study thermodynamics, the average speed of an air molecule at room temperature is approximately $500 \mathrm{~m} / \mathrm{s}$, with an average molecular mass of $6 \times 10^{-25} \mathrm{~kg}$; its momentum is thus

$$
p_{\text {molecule }}=\left(6 \times 10^{-25} \mathrm{~kg}\right)\left(500 \frac{\mathrm{m}}{\mathrm{s}}\right)=3 \times 10^{-22} \frac{\mathrm{kg} \cdot \mathrm{m}}{\mathrm{s}}
$$

For comparison, a typical automobile might have a speed of only $15 \mathrm{~m} / \mathrm{s}$, but a mass of $1400 \mathrm{~kg}$, giving it a momentum of

$$
p_{\text {car }}=(1400 \mathrm{~kg})\left(15 \frac{\mathrm{m}}{\mathrm{s}}\right)=21,000 \frac{\mathrm{kg} \cdot \mathrm{m}}{\mathrm{s}}
$$

These momenta are different by 27 orders of magnitude, or a factor of a billion billion billion!

### 9.2 Impulse and Collisions

We have defined momentum to be the product of mass and velocity. Therefore, if an object's velocity should change (due to the application of a force on the object), then necessarily, its momentum changes as well. This indicates a connection between momentum and force. The purpose of this section is to explore and describe that connection.

Suppose you apply a force on a free object for some amount of time. Clearly, the larger the force, the larger the object's change of momentum will be. Alternatively, the more time you spend applying this force, again the larger the change of momentum will be, as depicted in Figure 9.5. The amount by which the object's motion changes is therefore proportional to the magnitude of the force, and also to the time interval over which the force is applied.

Mathematically, if a quantity is proportional to two (or more) things, then it is proportional to the product of those things. The product of a force and a time interval (over which that force acts) is called impulse, and is given the symbol $\overrightarrow{\mathbf{J}}$.

## Impulse

Let $\overrightarrow{\mathbf{F}}(t)$ be the force applied to an object over some differential time interval $d t$ (Figure 9.6). The resulting impulse on the object is defined as

$$
d \overrightarrow{\mathbf{J}} \equiv \overrightarrow{\mathbf{F}}(t) d t
$$

The total impulse over the interval $t_{\mathrm{f}}-t_{\mathrm{i}}$ is

$$
\overrightarrow{\mathbf{J}}=\int_{t_{\mathrm{i}}}^{t_{\mathrm{f}}} d \overrightarrow{\mathbf{J}} \text { or } \overrightarrow{\mathbf{J}} \equiv \int_{t_{\mathrm{i}}}^{t_{\mathrm{f}}} \overrightarrow{\mathbf{F}}(t) d t
$$

Equation 9.2 and Equation 9.3 together say that when a force is applied for an infinitesimal time interval $d t$, it causes an infinitesimal impulse $d \overrightarrow{\mathbf{J}}$, and the total impulse given to the object is defined to be the sum (integral) of all these infinitesimal impulses.

To calculate the impulse using Equation 9.3, we need to know the force function $F(t)$, which we often don't. However, a result from calculus is useful here: Recall that the average value of a function over some interval is calculated by

$$
f(x)_{\mathrm{ave}}=\frac{1}{\Delta x} \int_{x_{\mathrm{i}}}^{x_{\mathrm{f}}} f(x) d x
$$

where $\Delta x=x_{\mathrm{f}}-x_{\mathrm{i}}$. Applying this to the time-dependent force function, we obtain

$$
\overrightarrow{\mathbf{F}}_{\mathrm{ave}}=\frac{1}{\Delta t} \int_{t_{\mathrm{i}}}^{t_{\mathrm{f}}} \overrightarrow{\mathbf{F}}(t) d t
$$

Therefore, from Equation 9.3,

$$
\overrightarrow{\mathbf{J}}=\overrightarrow{\mathbf{F}}_{\mathrm{ave}} \Delta t
$$

The idea here is that you can calculate the impulse on the object even if you don't know the details of the force as a function of time; you only need the average force. In fact, though, the process is usually reversed: You determine the impulse (by measurement or calculation) and then calculate the average force that caused that impulse.

To calculate the impulse, a useful result follows from writing the force in Equation 9.3 as $\overrightarrow{\mathbf{F}}(t)=m \overrightarrow{\mathbf{a}}(t)$ :

$$
\overrightarrow{\mathbf{J}}=\int_{t_{\mathrm{i}}}^{t_{\mathrm{f}}} \overrightarrow{\mathbf{F}}(t) d t=m \int_{t_{\mathrm{i}}}^{t_{\mathrm{f}}} \overrightarrow{\mathbf{a}}(t) d t=m\left[\overrightarrow{\mathbf{v}}\left(t_{\mathrm{f}}\right)-\overrightarrow{\mathbf{v}}_{\mathrm{i}}\right]
$$

For a constant force $\overrightarrow{\mathbf{F}}_{\text {ave }}=\overrightarrow{\mathbf{F}}=m \overrightarrow{\mathbf{a}}$, this simplifies to

$$
\overrightarrow{\mathbf{J}}=m \overrightarrow{\mathbf{a}} \Delta t=m \overrightarrow{\mathbf{v}}_{\mathrm{f}}-m \overrightarrow{\mathbf{v}}_{\mathrm{i}}=m\left(\overrightarrow{\mathbf{v}}_{\mathrm{f}}-\overrightarrow{\mathbf{v}}_{\mathrm{i}}\right)
$$

That is,

$$
\overrightarrow{\mathbf{J}}=m \Delta \overrightarrow{\mathbf{v}}
$$

Note that the integral form, Equation 9.3, applies to constant forces as well; in that case, since the force is independent of time, it comes out of the integral, which can then be trivially evaluated.

## EXAMPLE 9.1

## The Arizona Meteor Crater

Approximately 50,000 years ago, a large (radius of $25 \mathrm{~m}$ ) iron-nickel meteorite collided with Earth at an estimated speed of $1.28 \times 10^{4} \mathrm{~m} / \mathrm{s}$ in what is now the northern Arizona desert, in the United States. The impact produced a crater that is still visible today (Figure 9.7); it is approximately $1200 \mathrm{~m}$ (three-quarters of a mile) in diameter, $170 \mathrm{~m}$ deep, and has a rim that rises $45 \mathrm{~m}$ above the surrounding desert plain. Iron-nickel meteorites typically have a density of $\rho=7970 \mathrm{~kg} / \mathrm{m}^{3}$. Use impulse considerations to estimate the average force and the maximum force that the meteor applied to Earth during the impact.

## Strategy

It is conceptually easier to reverse the question and calculate the force that Earth applied on the meteor in order to stop it. Therefore, we'll calculate the force on the meteor and then use Newton's third law to argue that the force from the meteor on Earth was equal in magnitude and opposite in direction.

Using the given data about the meteor, and making reasonable guesses about the shape of the meteor and impact time, we first calculate the impulse using Equation 9.6. We then use the relationship between force and impulse Equation 9.5 to estimate the average force during impact. Next, we choose a reasonable force function for the impact event, calculate the average value of that function Equation 9.4, and set the resulting expression equal to the calculated average force. This enables us to solve for the maximum force.

## Solution

Define upward to be the $+y$-direction. For simplicity, assume the meteor is traveling vertically downward prior to impact. In that case, its initial velocity is $\overrightarrow{\mathbf{v}}_{\mathrm{i}}=-v_{\mathrm{i}} \hat{\mathbf{j}}$, and the force Earth exerts on the meteor points upward, $\overrightarrow{\mathbf{F}}(t)=+F(t) \hat{\mathbf{j}}$. The situation at $t=0$ is depicted below.

The average force during the impact is related to the impulse by

$$
\overrightarrow{\mathbf{F}}_{\mathrm{ave}}=\frac{\overrightarrow{\mathbf{J}}}{\Delta t}
$$

From Equation 9.6, $\overrightarrow{\mathbf{J}}=m \Delta \overrightarrow{\mathbf{v}}$, so we have

$$
\overrightarrow{\mathbf{F}}_{\mathrm{ave}}=\frac{m \Delta \overrightarrow{\mathbf{v}}}{\Delta t}
$$

The mass is equal to the product of the meteor's density and its volume:

$$
m=\rho V
$$

If we assume (guess) that the meteor was roughly spherical, we have

$$
V=\frac{4}{3} \pi R^{3}
$$

Thus we obtain

$$
\overrightarrow{\mathbf{F}}_{\mathrm{ave}}=\frac{\rho V \Delta \overrightarrow{\mathbf{v}}}{\Delta t}=\frac{\rho\left(\frac{4}{3} \pi R^{3}\right)\left(\overrightarrow{\mathbf{v}}_{\mathrm{f}}-\overrightarrow{\mathrm{v}}_{\mathrm{i}}\right)}{\Delta t}
$$

The problem says the velocity at impact was $-1.28 \times 10^{4} \mathrm{~m} / \mathrm{s} \hat{\mathbf{j}}$ (the final velocity is zero); also, we guess that the primary impact lasted about $t_{\max }=2 \mathrm{~s}$. Substituting these values gives

$$
\begin{aligned}
\overrightarrow{\mathbf{F}}_{\mathrm{ave}} & =\frac{\left(7970 \frac{\mathrm{kg}}{\mathrm{m}^{3}}\right)\left[\frac{4}{3} \pi(25 \mathrm{~m})^{3}\right]\left[0 \frac{\mathrm{m}}{\mathrm{s}}-\left(-1.28 \times 10^{4} \frac{\mathrm{m}}{\mathrm{s}} \hat{\mathbf{j}}\right)\right]}{2 \mathrm{~s}} \\
& =+\left(3.33 \times 10^{12} \mathrm{~N}\right) \hat{\mathbf{j}}
\end{aligned}
$$

This is the average force applied during the collision. Notice that this force vector points in the same direction as the change of velocity vector $\Delta \overrightarrow{\mathbf{v}}$.

Next, we calculate the maximum force. The impulse is related to the force function by

$$
\overrightarrow{\mathbf{J}}=\int_{t_{\mathrm{i}}}^{t_{\max }} \overrightarrow{\mathbf{F}}(t) d t
$$

We need to make a reasonable choice for the force as a function of time. We define $t=0$ to be the moment the meteor first touches the ground. Then we assume the force is a maximum at impact, and rapidly drops to zero. A function that does this is

$$
F(t)=F_{\max } e^{-t^{2} /\left(2 \tau^{2}\right)}
$$

(The parameter $\tau$ represents how rapidly the force decreases to zero.) The average force is

$$
F_{\text {ave }}=\frac{1}{\Delta t} \int_{0}^{t_{\max }} F_{\max } e^{-t^{2} /\left(2 \tau^{2}\right)} d t
$$

where $\Delta t=t_{\max }-0 \mathrm{~s}$. Since we already have a numeric value for $F_{\text {ave }}$, we can use the result of the integral to obtain $F_{\max }$.

Choosing $\tau=\frac{1}{e} t_{\max }$ (this is a common choice, as you will see in later chapters), and guessing that $t_{\max }=2 \mathrm{~s}$, this integral evaluates to

$$
F_{\mathrm{avg}}=0.458 F_{\max }
$$

Thus, the maximum force has a magnitude of

$$
\begin{aligned}
0.458 F_{\max } & =3.33 \times 10^{12} \mathrm{~N} \\
F_{\max } & =7.27 \times 10^{12} \mathrm{~N}
\end{aligned}
$$

The complete force function, including the direction, is

$$
\overrightarrow{\mathbf{F}}(t)=\left(7.27 \times 10^{12} \mathrm{~N}\right) e^{-t^{2} /\left(8 \mathrm{~s}^{2}\right)} \widehat{\mathbf{j}}
$$

This is the force Earth applied to the meteor; by Newton's third law, the force the meteor applied to Earth is

$$
\overrightarrow{\mathbf{F}}(t)=-\left(7.27 \times 10^{12} \mathrm{~N}\right) e^{-t^{2} /\left(8 \mathrm{~s}^{2}\right)} \widehat{\mathbf{j}}
$$

which is the answer to the original question.

## Significance

The graph of this function contains important information. Let's graph (the magnitude of) both this function and the average force together (Figure 9.8).

## Meteor Impact Force

Notice that the area under each plot has been filled in. For the plot of the (constant) force $F_{\text {ave }}$, the area is a rectangle, corresponding to $F_{\text {ave }} \Delta t=J$. As for the plot of $F(t)$, recall from calculus that the area under the plot of a function is numerically equal to the integral of that function, over the specified interval; so here, that is $\int_{0}^{t_{\max }} F(t) d t=J$. Thus, the areas are equal, and both represent the impulse that the meteor applied to Earth during the two-second impact. The average force on Earth sounds like a huge force, and it is. Nevertheless, Earth barely noticed it. The acceleration Earth obtained was just

$$
\overrightarrow{\mathbf{a}}=\frac{-\overrightarrow{\mathbf{F}}_{\mathrm{ave}}}{M_{\text {Earth }}}=\frac{-\left(3.33 \times 10^{12} \mathrm{~N}\right) \hat{\mathbf{j}}}{5.97 \times 10^{24} \mathrm{~kg}}=-\left(5.6 \times 10^{-13} \frac{\mathrm{m}}{\mathrm{s}^{2}}\right) \hat{\mathbf{j}}
$$

which is completely immeasurable. That said, the impact created seismic waves that nowadays could be detected by modern monitoring equipment.

## EXAMPLE 9.2

## The Benefits of Impulse

A car traveling at $27 \mathrm{~m} / \mathrm{s}$ collides with a building. The collision with the building causes the car to come to a stop in approximately 1 second. The driver, who weighs $860 \mathrm{~N}$, is protected by a combination of a variabletension seatbelt and an airbag (Figure 9.9). (In effect, the driver collides with the seatbelt and airbag and not with the building.) The airbag and seatbelt slow his velocity, such that he comes to a stop in approximately 2.5 s.

a. What average force does the driver experience during the collision?

b. Without the seatbelt and airbag, his collision time (with the steering wheel) would have been approximately $0.20 \mathrm{~s}$. What force would he experience in this case?

## Strategy

We are given the driver's weight, his initial and final velocities, and the time of collision; we are asked to calculate a force. Impulse seems the right way to tackle this; we can combine Equation 9.5 and Equation 9.6.

## Solution

a. Define the $+x$-direction to be the direction the car is initially moving. We know

$$
\overrightarrow{\mathbf{J}}=\overrightarrow{\mathbf{F}} \Delta t
$$

and

$$
\overrightarrow{\mathbf{J}}=m \Delta \overrightarrow{\mathbf{v}}
$$

Since $J$ is equal to both those things, they must be equal to each other:

$$
\overrightarrow{\mathbf{F}} \Delta t=m \Delta \overrightarrow{\mathbf{v}}
$$

We need to convert this weight to the equivalent mass, expressed in SI units:

$$
\frac{860 \mathrm{~N}}{9.8 \mathrm{~m} / \mathrm{s}^{2}}=87.8 \mathrm{~kg}
$$

Remembering that $\Delta \overrightarrow{\mathbf{v}}=\overrightarrow{\mathbf{v}}_{\mathrm{f}}-\overrightarrow{\mathbf{v}}_{\mathbf{i}}$, and noting that the final velocity is zero, we solve for the force:

$$
\overrightarrow{\mathbf{F}}=m \frac{0-v_{\mathrm{i}} \hat{\mathbf{i}}}{\Delta t}=(87.8 \mathrm{~kg})\left(\frac{-(27 \mathrm{~m} / \mathrm{s}) \hat{\mathbf{i}}}{2.5 \mathrm{~s}}\right)=-(948 \mathrm{~N}) \hat{\mathbf{i}}
$$

The negative sign implies that the force slows him down. For perspective, this is about 1.1 times his own weight.

b. Same calculation, just the different time interval:

$$
\overrightarrow{\mathbf{F}}=(87.8 \mathrm{~kg})\left(\frac{-(27 \mathrm{~m} / \mathrm{s}) \hat{\mathbf{i}}}{0.20 \mathrm{~s}}\right)=-(11,853 \mathrm{~N}) \hat{\mathbf{i}}
$$

which is about 14 times his own weight. Big difference!

## Significance

You see that the value of an airbag is how greatly it reduces the force on the vehicle occupants. For this reason, they have been required on all passenger vehicles in the United States since 1991, and have been commonplace throughout Europe and Asia since the mid-1990s. The change of momentum in a crash is the same, with or without an airbag; the force, however, is vastly different.

## Effect of Impulse

Since an impulse is a force acting for some amount of time, it causes an object's motion to change. Recall

## Equation 9.6:

$$
\overrightarrow{\mathbf{J}}=m \Delta \overrightarrow{\mathbf{v}}
$$

Because $m \overrightarrow{\mathbf{v}}$ is the momentum of a system, $m \Delta \overrightarrow{\mathbf{v}}$ is the change of momentum $\Delta \overrightarrow{\mathbf{p}}$. This gives us the following relation, called the impulse-momentum theorem (or relation).

## Impulse-Momentum Theorem

An impulse applied to a system changes the system's momentum, and that change of momentum is exactly equal to the impulse that was applied:

$$
\overrightarrow{\mathbf{J}}=\Delta \overrightarrow{\mathbf{p}}
$$

There are two crucial concepts in the impulse-momentum theorem:

1. Impulse is a vector quantity; an impulse of, say, $-(10 \mathrm{~N} \cdot \mathrm{s}) \hat{\mathbf{i}}$ is very different from an impulse of $+(10 \mathrm{~N} \cdot \mathrm{s}) \hat{\mathbf{i}}$; they cause completely opposite changes of momentum.
2. An impulse does not cause momentum; rather, it causes a change in the momentum of an object. Thus, you must subtract the final momentum from the initial momentum, and-since momentum is also a vector quantity-you must take careful account of the signs of the momentum vectors.

The most common questions asked in relation to impulse are to calculate the applied force, or the change of velocity that occurs as a result of applying an impulse. The general approach is the same.

## PROBLEM-SOLVING STRATEG

## Impulse-Momentum Theorem

1. Express the impulse as force times the relevant time interval.
2. Express the impulse as the change of momentum, usually $m \Delta v$.
3. Equate these and solve for the desired quantity.

## EXAMPLE 9.3 - Moving the Enterprise

When Captain Picard commands, “Take us out; ahead one-quarter impulse," the starship Enterprise (Figure 9.11) starts from rest to a final speed of $v_{\mathrm{f}}=1 / 4\left(3.0 \times 10^{8} \mathrm{~m} / \mathrm{s}\right)$. Assuming this maneuver is completed in 60 $\mathrm{s}$, what average force did the impulse engines apply to the ship?

## Strategy

We are asked for a force; we know the initial and final speeds (and hence the change in speed), and we know the time interval over which this all happened. In particular, we know the amount of time that the force acted. This suggests using the impulse-momentum relation. To use that, though, we need the mass of the Enterprise. An internet search gives a best estimate of the mass of the Enterprise (in the 2009 movie) as $2 \times 10^{9} \mathrm{~kg}$.

## Solution

Because this problem involves only one direction (i.e., the direction of the force applied by the engines), we only need the scalar form of the impulse-momentum theorem Equation 9.7, which is

$$
\Delta p=J
$$

with

$$
\Delta p=m \Delta v
$$

and

$$
J=F \Delta t .
$$

Equating these expressions gives

$$
F \Delta t=m \Delta v
$$

Solving for the magnitude of the force and inserting the given values leads to

$$
F=\frac{m \Delta v}{\Delta t}=\frac{\left(2 \times 10^{9} \mathrm{~kg}\right)\left(7.5 \times 10^{7} \mathrm{~m} / \mathrm{s}\right)}{60 \mathrm{~s}}=2.5 \times 10^{15} \mathrm{~N}
$$

## Significance

This is an unimaginably huge force. It goes almost without saying that such a force would kill everyone on board instantly, as well as destroying every piece of equipment. Fortunately, the Enterprise has "inertial dampeners." It is left as an exercise for the reader's imagination to determine how these work.

## EXAMPLE 9.4

## The iPhone Drop

Apple released its iPhone 6 Plus in November 2014. According to many reports, it was originally supposed to have a screen made from sapphire, but that was changed at the last minute for a hardened glass screen.

Reportedly, this was because the sapphire screen cracked when the phone was dropped. What force did the iPhone 6 Plus experience as a result of being dropped?

## Strategy

The force the phone experiences is due to the impulse applied to it by the floor when the phone collides with the floor. Our strategy then is to use the impulse-momentum relationship. We calculate the impulse, estimate the impact time, and use this to calculate the force.

We need to make a couple of reasonable estimates, as well as find technical data on the phone itself. First, let's suppose that the phone is most often dropped from about chest height on an average-height person. Second, assume that it is dropped from rest, that is, with an initial vertical velocity of zero. Finally, we assume that the phone bounces very little-the height of its bounce is assumed to be negligible.

## Solution

Define upward to be the $+y$-direction. A typical height is approximately $h=1.5 \mathrm{~m}$ and, as stated, $\overrightarrow{\mathbf{v}}_{\mathrm{i}}=(0 \mathrm{~m} / \mathrm{s}) \hat{\mathbf{i}}$. The average force on the phone is related to the impulse the floor applies on it during the collision:

$$
\overrightarrow{\mathbf{F}}_{\mathrm{ave}}=\frac{\overrightarrow{\mathbf{J}}}{\Delta t}
$$

The impulse $\overrightarrow{\mathbf{J}}$ equals the change in momentum,

$$
\overrightarrow{\mathbf{J}}=\Delta \overrightarrow{\mathbf{p}}
$$

so

$$
\overrightarrow{\mathbf{F}}_{\mathrm{ave}}=\frac{\Delta \overrightarrow{\mathbf{p}}}{\Delta t}
$$

Next, the change of momentum is

$$
\Delta \overrightarrow{\mathbf{p}}=m \Delta \overrightarrow{\mathbf{v}}
$$

We need to be careful with the velocities here; this is the change of velocity due to the collision with the floor. But the phone also has an initial drop velocity $\left[\overrightarrow{\mathbf{v}}_{\mathbf{i}}=(0 \mathrm{~m} / \mathrm{s}) \hat{\mathbf{j}}\right]$, so we label our velocities. Let:

- $\overrightarrow{\mathbf{v}}_{\mathrm{i}}=$ the initial velocity with which the phone was dropped (zero, in this example)
- $\overrightarrow{\mathbf{v}}_{1}=$ the velocity the phone had the instant just before it hit the floor
- $\overrightarrow{\mathbf{v}}_{2}=$ the final velocity of the phone as a result of hitting the floor

With these definitions, the change of momentum of the phone during the collision with the floor is

$$
m \Delta \overrightarrow{\mathbf{v}}=m\left(\overrightarrow{\mathbf{v}}_{\mathbf{2}}-\overrightarrow{\mathbf{v}}_{\mathbf{1}}\right)
$$

Since we assume the phone doesn't bounce at all when it hits the floor (or at least, the bounce height is negligible), then $\overrightarrow{\mathbf{v}}_{2}$ is zero, so

$$
\begin{aligned}
& m \Delta \overrightarrow{\mathbf{v}}=m\left[0-\left(-v_{1} \hat{\mathbf{j}}\right)\right] \\
& m \Delta \overrightarrow{\mathbf{v}}=+m v_{1} \hat{\mathbf{j}}
\end{aligned}
$$

We can get the speed of the phone just before it hits the floor using either kinematics or conservation of energy. We'll use conservation of energy here; you should re-do this part of the problem using kinematics and prove that you get the same answer.

First, define the zero of potential energy to be located at the floor. Conservation of energy then gives us:

$$
\begin{aligned}
E_{\mathrm{i}} & =E_{1} \\
K_{\mathrm{i}}+U_{\mathrm{i}} & =K_{1}+U_{1} \\
\frac{1}{2} m v_{\mathrm{i}}^{2}+m g h_{\text {drop }} & =\frac{1}{2} m v_{1}^{2}+m g h_{\text {floor }}
\end{aligned}
$$

Defining $h_{\text {floor }}=0$ and using $\overrightarrow{\mathbf{v}}_{\mathrm{i}}=(0 \mathrm{~m} / \mathrm{s}) \hat{\mathbf{j}}$ gives

$$
\begin{aligned}
\frac{1}{2} m v_{1}^{2} & =m g h_{\text {drop }} \\
v_{1} & = \pm \sqrt{2 g h_{\text {drop }}}
\end{aligned}
$$

Because $v_{1}$ is a vector magnitude, it must be positive. Thus, $m \Delta v=m v_{1}=m \sqrt{2 g h_{\text {drop }}}$. Inserting this result into the expression for force gives

$$
\begin{aligned}
\overrightarrow{\mathbf{F}} & =\frac{\Delta \overrightarrow{\mathbf{p}}}{\Delta t} \\
& =\frac{m \Delta \overrightarrow{\mathbf{v}}}{\Delta t} \\
& =\frac{+m v_{1} \hat{\mathbf{j}}}{\Delta t} \\
& =\frac{m \sqrt{2 g h}}{\Delta t} \hat{\mathbf{j}}
\end{aligned}
$$

Finally, we need to estimate the collision time. One common way to estimate a collision time is to calculate how long the object would take to travel its own length. The phone is moving at $5.4 \mathrm{~m} / \mathrm{s}$ just before it hits the floor, and it is $0.14 \mathrm{~m}$ long, giving an estimated collision time of $0.026 \mathrm{~s}$. Inserting the given numbers, we obtain

$$
\overrightarrow{\mathbf{F}}=\frac{(0.172 \mathrm{~kg}) \sqrt{2\left(9.8 \mathrm{~m} / \mathrm{s}^{2}\right)(1.5 \mathrm{~m})}}{0.026 \mathrm{~s}} \widehat{\mathbf{j}}=(36 \mathrm{~N}) \hat{\mathbf{j}}
$$

## Significance

The iPhone itself weighs just $(0.172 \mathrm{~kg})\left(9.81 \mathrm{~m} / \mathrm{s}^{2}\right)=1.68 \mathrm{~N}$; the force the floor applies to it is therefore over 20 times its weight.

## Momentum and Force

In Example 9.3, we obtained an important relationship:

$$
\overrightarrow{\mathbf{F}}_{\mathrm{ave}}=\frac{\Delta \overrightarrow{\mathbf{p}}}{\Delta t}
$$

In words, the average force applied to an object is equal to the change of the momentum that the force causes, divided by the time interval over which this change of momentum occurs. This relationship is very useful in situations where the collision time $\Delta t$ is small, but measureable; typical values would be 1/10th of a second, or even one thousandth of a second. Car crashes, punting a football, or collisions of subatomic particles would meet this criterion.

For a continuously changing momentum-due to a continuously changing force-this becomes a powerful conceptual tool. In the limit $\Delta t \rightarrow d t$, Equation 9.2 becomes

$$
\overrightarrow{\mathbf{F}}=\frac{d \overrightarrow{\mathbf{p}}}{d t}
$$

This says that the rate of change of the system's momentum (implying that momentum is a function of time) is exactly equal to the net applied force (also, in general, a function of time). This is, in fact, Newton's second law, written in terms of momentum rather than acceleration. This is the relationship Newton himself presented in his Principia Mathematica (although he called it "quantity of motion" rather than "momentum").

If the mass of the system remains constant, Equation 9.3 reduces to the more familiar form of Newton's second law. We can see this by substituting the definition of momentum:

$$
\overrightarrow{\mathbf{F}}=\frac{d(m \overrightarrow{\mathbf{v}})}{d t}=m \frac{d \overrightarrow{\mathbf{v}}}{d t}=m \overrightarrow{\mathbf{a}}
$$

The assumption of constant mass allowed us to pull $m$ out of the derivative. If the mass is not constant, we cannot use this form of the second law, but instead must start from Equation 9.3. Thus, one advantage to
expressing force in terms of changing momentum is that it allows for the mass of the system to change, as well as the velocity; this is a concept we'll explore when we study the motion of rockets.

## Newton's Second Law of Motion in Terms of Momentum

The net external force on a system is equal to the rate of change of the momentum of that system caused by the force:

$$
\overrightarrow{\mathbf{F}}=\frac{d \overrightarrow{\mathbf{p}}}{d t}
$$

Although Equation 9.3 allows for changing mass, as we will see in Rocket Propulsion, the relationship between momentum and force remains useful when the mass of the system is constant, as in the following example.

## EXAMPLE 9.5

## Calculating Force: Venus Williams' Tennis Serve

During the 2007 French Open, Venus Williams hit the fastest recorded serve in a premier women's match, reaching a speed of $58 \mathrm{~m} / \mathrm{s}(209 \mathrm{~km} / \mathrm{h})$. What is the average force exerted on the $0.057-\mathrm{kg}$ tennis ball by Venus Williams' racquet? Assume that the ball's speed just after impact is $58 \mathrm{~m} / \mathrm{s}$, as shown in Figure 9.13 , that the initial horizontal component of the velocity before impact is negligible, and that the ball remained in contact with the racquet for $5.0 \mathrm{~ms}$.

## Strategy

This problem involves only one dimension because the ball starts from having no horizontal velocity component before impact. Newton's second law stated in terms of momentum is then written as

$$
\overrightarrow{\mathbf{F}}=\frac{d \overrightarrow{\mathbf{p}}}{d t}
$$

As noted above, when mass is constant, the change in momentum is given by

$$
\Delta p=m \Delta v=m\left(v_{\mathrm{f}}-v_{\mathrm{i}}\right)
$$

where we have used scalars because this problem involves only one dimension. In this example, the velocity just after impact and the time interval are given; thus, once $\Delta p$ is calculated, we can use $F=\frac{\Delta p}{\Delta t}$ to find the force.

## Solution

To determine the change in momentum, insert the values for the initial and final velocities into the equation above:

$$
\begin{aligned}
\Delta p & =m\left(v_{\mathrm{f}}-v_{\mathrm{i}}\right) \\
& =(0.057 \mathrm{~kg})(58 \mathrm{~m} / \mathrm{s}-0 \mathrm{~m} / \mathrm{s}) \\
& =3.3 \frac{\mathrm{kg} \cdot \mathrm{m}}{\mathrm{s}}
\end{aligned}
$$

Now the magnitude of the net external force can be determined by using

$$
F=\frac{\Delta p}{\Delta t}=\frac{3.3 \frac{\mathrm{kg} \cdot \mathrm{m}}{\mathrm{s}}}{5.0 \times 10^{-3} \mathrm{~s}}=6.6 \times 10^{2} \mathrm{~N}
$$

where we have retained only two significant figures in the final step.

## Significance

This quantity was the average force exerted by Venus Williams' racquet on the tennis ball during its brief impact (note that the ball also experienced the $0.57-\mathrm{N}$ force of gravity, but that force was not due to the racquet). This problem could also be solved by first finding the acceleration and then using $F=m a$, but one additional step would be required compared with the strategy used in this example.

### 9.3 Conservation of Linear Momentum

Recall Newton's third law: When two objects of masses $m_{1}$ and $m_{2}$ interact (meaning that they apply forces on each other), the force that object 2 applies to object 1 is equal in magnitude and opposite in direction to the force that object 1 applies on object 2 . Let:

- $\overrightarrow{\mathbf{F}}_{21}=$ the force on $m_{1}$ from $m_{2}$
- $\overrightarrow{\mathbf{F}}_{12}=$ the force on $m_{2}$ from $m_{1}$

Then, in symbols, Newton's third law says

$$
\begin{align*}
\overrightarrow{\mathbf{F}}_{21} & =-\overrightarrow{\mathbf{F}}_{12} \\
m_{1} \overrightarrow{\mathbf{a}}_{\mathbf{1}} & =-m_{2} \overrightarrow{\mathbf{a}}_{2}
\end{align*}
$$

(Recall that these two forces do not cancel because they are applied to different objects. $F_{21}$ causes $m_{1}$ to accelerate, and $F_{12}$ causes $m_{2}$ to accelerate.)

Although the magnitudes of the forces on the objects are the same, the accelerations are not, simply because the masses (in general) are different. Therefore, the changes in velocity of each object are different:

$$
\frac{d \overrightarrow{\mathbf{v}}_{\mathbf{1}}}{d t} \neq \frac{d \overrightarrow{\mathbf{v}}_{\mathbf{2}}}{d t}
$$

However, the products of the mass and the change of velocity are equal (in magnitude):

$$
m_{1} \frac{d \overrightarrow{\mathbf{v}}_{\mathbf{1}}}{d t}=-m_{2} \frac{d \overrightarrow{\mathbf{v}}_{\mathbf{2}}}{d t}
$$

It's a good idea, at this point, to make sure you're clear on the physical meaning of the derivatives in Equation 9.3. Because of the interaction, each object ends up getting its velocity changed, by an amount $d v$. Furthermore, the interaction occurs over a time interval $d t$, which means that the change of velocities also occurs over $d t$. This time interval is the same for each object.

Let's assume, for the moment, that the masses of the objects do not change during the interaction. (We'll relax this restriction later.) In that case, we can pull the masses inside the derivatives:

$$
\frac{d}{d t}\left(m_{1} \overrightarrow{\mathbf{v}}_{\mathbf{1}}\right)=-\frac{d}{d t}\left(m_{2} \overrightarrow{\mathbf{v}}_{\mathbf{2}}\right)
$$

and thus

$$
\frac{d \overrightarrow{\mathbf{p}}_{\mathbf{1}}}{d t}=-\frac{d \overrightarrow{\mathbf{p}}_{\mathbf{2}}}{d t}
$$

This says that the rate at which momentum changes is the same for both objects. The masses are different, and the changes of velocity are different, but the rate of change of the product of $m$ and $\overrightarrow{\mathbf{v}}$ are the same.

Physically, this means that during the interaction of the two objects ( $m_{1}$ and $m_{2}$ ), both objects have their momentum changed; but those changes are identical in magnitude, though opposite in sign. For example, the momentum of object 1 might increase, which means that the momentum of object 2 decreases by exactly the same amount.

In light of this, let's re-write Equation 9.12 in a more suggestive form:

$$
\frac{d \overrightarrow{\mathbf{p}}_{\mathbf{1}}}{d t}+\frac{d \overrightarrow{\mathbf{p}}_{\mathbf{2}}}{d t}=0
$$

This says that during the interaction, although object 1's momentum changes, and object 2's momentum also changes, these two changes cancel each other out, so that the total change of momentum of the two objects together is zero.

Since the total combined momentum of the two objects together never changes, then we could write

$$
\frac{d}{d t}\left(\overrightarrow{\mathbf{p}}_{\mathbf{1}}+\overrightarrow{\mathbf{p}}_{\mathbf{2}}\right)=0
$$

from which it follows that

$$
\overrightarrow{\mathbf{p}}_{\mathbf{1}}+\overrightarrow{\mathbf{p}}_{\mathbf{2}}=\text { constant }
$$

As shown in Figure 9.14, the total momentum of the system before and after the collision remains the same.

Generalizing this result to $N$ objects, we obtain

$$
\begin{align*}
\overrightarrow{\mathbf{p}}_{\mathbf{1}}+\overrightarrow{\mathbf{p}}_{\mathbf{2}}+\overrightarrow{\mathbf{p}}_{\mathbf{3}}+\cdots+\overrightarrow{\mathbf{p}}_{\mathbf{N}} & =\text { constant } \\
\sum_{j=1}^{N} \overrightarrow{\mathbf{p}}_{\mathbf{j}} & =\text { constant }
\end{align*}
$$

Equation 9.17 is the definition of the total (or net) momentum of a system of $N$ interacting objects, along with the statement that the total momentum of a system of objects is constant in time-or better, is conserved.

## Conservation Laws

If the value of a physical quantity is constant in time, we say that the quantity is conserved.

## Requirements for Momentum Conservation

There is a complication, however. A system must meet two requirements for its momentum to be conserved:

1. The mass of the system must remain constant during the interaction.

As the objects interact (apply forces on each other), they may transfer mass from one to another; but any mass one object gains is balanced by the loss of that mass from another. The total mass of the system of objects, therefore, remains unchanged as time passes:

$$
\left[\frac{d m}{d t}\right]_{\text {system }}=0
$$

2. The net external force on the system must be zero.

As the objects collide, or explode, and move around, they exert forces on each other. However, all of these forces are internal to the system, and thus each of these internal forces is balanced by another internal force that is equal in magnitude and opposite in sign. As a result, the change in momentum caused by each internal force is cancelled by another momentum change that is equal in magnitude and opposite in direction. Therefore, internal forces cannot change the total momentum of a system because the changes sum to zero. However, if there is some external force that acts on all of the objects (gravity, for example, or friction), then this force changes the momentum of the system as a whole; that is to say, the momentum of the system is changed by the external force. Thus, for the momentum of the system to be conserved, we must have

$$
\overrightarrow{\mathbf{F}}_{\text {ext }}=\overrightarrow{\mathbf{0}}
$$

A system of objects that meets these two requirements is said to be a closed system (also called an isolated system). Thus, the more compact way to express this is shown below.

## Law of Conservation of Momentum

The total momentum of a closed system is conserved:

$$
\sum_{j=1}^{N} \overrightarrow{\mathbf{p}}_{\mathbf{j}}=\text { constant }
$$

This statement is called the Law of Conservation of Momentum. Along with the conservation of energy, it is one of the foundations upon which all of physics stands. All our experimental evidence supports this statement: from the motions of galactic clusters to the quarks that make up the proton and the neutron, and at every scale in between. In a closed system, the total momentum never changes.

Note that there absolutely can be external forces acting on the system; but for the system's momentum to remain constant, these external forces have to cancel, so that the net external force is zero. Billiard balls on a table all have a weight force acting on them, but the weights are balanced (canceled) by the normal forces, so there is no net force.

## The Meaning of ‘System'

A system (mechanical) is the collection of objects in whose motion (kinematics and dynamics) you are interested. If you are analyzing the bounce of a ball on the ground, you are probably only interested in the motion of the ball, and not of Earth; thus, the ball is your system. If you are analyzing a car crash, the two cars together compose your system (Figure 9.15).

## Conservation of Momentum

Using conservation of momentum requires four basic steps. The first step is crucial:

1. Identify a closed system (total mass is constant, no net external force acts on the system).
2. Write down an expression representing the total momentum of the system before the "event" (explosion or collision).
3. Write down an expression representing the total momentum of the system after the "event."
4. Set these two expressions equal to each other, and solve this equation for the desired quantity.

## EXAMPLE 9.6

## Colliding Carts

Two carts in a physics lab roll on a level track, with negligible friction. These carts have small magnets at their ends, so that when they collide, they stick together (Figure 9.16). The first cart has a mass of 675 grams and is rolling at $0.75 \mathrm{~m} / \mathrm{s}$ to the right; the second has a mass of 500 grams and is rolling at $1.33 \mathrm{~m} / \mathrm{s}$, also to the right. After the collision, what is the velocity of the two joined carts?

## Strategy

We have a collision. We're given masses and initial velocities; we're asked for the final velocity. This all suggests using conservation of momentum as a method of solution. However, we can only use it if we have a closed system. So we need to be sure that the system we choose has no net external force on it, and that its mass is not changed by the collision.

Defining the system to be the two carts meets the requirements for a closed system: The combined mass of the two carts certainly doesn't change, and while the carts definitely exert forces on each other, those forces are internal to the system, so they do not change the momentum of the system as a whole. In the vertical direction, the weights of the carts are canceled by the normal forces on the carts from the track.

## Solution

Conservation of momentum is

$$
\overrightarrow{\mathbf{p}}_{\mathbf{f}}=\overrightarrow{\mathbf{p}}_{\mathbf{i}}
$$

Define the direction of their initial velocity vectors to be the $+x$-direction. The initial momentum is then

$$
\overrightarrow{\mathbf{p}}_{\mathbf{i}}=m_{1} v_{1} \hat{\mathbf{i}}+m_{2} v_{2} \hat{\mathbf{i}}
$$

The final momentum of the now-linked carts is

$$
\overrightarrow{\mathbf{p}}_{\mathbf{f}}=\left(m_{1}+m_{2}\right) \overrightarrow{\mathbf{v}}_{\mathbf{f}}
$$

Equating:

$$
\begin{aligned}
\left(m_{1}+m_{2}\right) \overrightarrow{\mathbf{v}}_{\mathbf{f}} & =m_{1} v_{1} \hat{\mathbf{i}}+m_{2} v_{2} \hat{\mathbf{i}} \\
\overrightarrow{\mathbf{v}}_{\mathbf{f}} & =\left(\frac{m_{1} v_{1}+m_{2} v_{2}}{m_{1}+m_{2}}\right) \hat{\mathbf{i}}
\end{aligned}
$$

Substituting the given numbers:

$$
\begin{aligned}
\overrightarrow{\mathbf{v}}_{\mathbf{f}} & =\left[\frac{(0.675 \mathrm{~kg})(0.75 \mathrm{~m} / \mathrm{s})+(0.5 \mathrm{~kg})(1.33 \mathrm{~m} / \mathrm{s})}{1.175 \mathrm{~kg}}\right] \hat{\mathbf{i}} \\
& =(0.997 \mathrm{~m} / \mathrm{s}) \hat{\mathbf{i}}
\end{aligned}
$$

## Significance

The principles that apply here to two laboratory carts apply identically to all objects of whatever type or size. Even for photons, the concepts of momentum and conservation of momentum are still crucially important even at that scale. (Since they are massless, the momentum of a photon is defined very differently from the momentum of ordinary objects. You will learn about this when you study quantum physics.)

## EXAMPLE 9.7

## A Bouncing Superball

A superball of mass $0.25 \mathrm{~kg}$ is dropped from rest from a height of $h=1.50 \mathrm{~m}$ above the floor. It bounces with no loss of energy and returns to its initial height (Figure 9.17).

a. What is the superball's change of momentum during its bounce on the floor?

b. What was Earth's change of momentum due to the ball colliding with the floor?

c. What was Earth's change of velocity as a result of this collision?

(This example shows that you have to be careful about defining your system.)

## Strategy

Since we are asked only about the ball's change of momentum, we define our system to be the ball. But this is clearly not a closed system; gravity applies a downward force on the ball while it is falling, and the normal force from the floor applies a force during the bounce. Thus, we cannot use conservation of momentum as a strategy. Instead, we simply determine the ball's momentum just before it collides with the floor and just after, and calculate the difference. We have the ball's mass, so we need its velocities.

## Solution

a. Since this is a one-dimensional problem, we use the scalar form of the equations. Let:

- $p_{0}=$ the magnitude of the ball's momentum at time $t_{0}$, the moment it was released; since it was dropped from rest, this is zero.
- $p_{1}=$ the magnitude of the ball's momentum at time $t_{1}$, the instant just before it hits the floor.

$\circ p_{2}=$ the magnitude of the ball's momentum at time $t_{2}$, just after it loses contact with the floor after the bounce.

The ball's change of momentum is

$$
\begin{aligned}
\Delta \overrightarrow{\mathbf{p}} & =\overrightarrow{\mathbf{p}}_{\mathbf{2}}-\overrightarrow{\mathbf{p}}_{\mathbf{1}} \\
& =p_{2} \hat{\mathbf{j}}-\left(-p_{1} \hat{\mathbf{j}}\right) \\
& =\left(p_{2}+p_{1}\right) \hat{\mathbf{j}}
\end{aligned}
$$

Its velocity just before it hits the floor can be determined from either conservation of energy or kinematics. We use kinematics here; you should re-solve it using conservation of energy and confirm you get the same result.

We want the velocity just before it hits the ground (at time $t_{1}$ ). We know its initial velocity $v_{0}=0$ (at time $t_{0}$

), the height it falls, and its acceleration; we don't know the fall time. We could calculate that, but instead we use

$$
\overrightarrow{\mathbf{v}}_{\mathbf{1}}=-\hat{\mathbf{j}} \sqrt{2 g y}=-5.4 \mathrm{~m} / \mathrm{s} \hat{\mathbf{j}}
$$

Thus the ball has a momentum of

$$
\begin{aligned}
\overrightarrow{\mathbf{p}}_{\mathbf{1}} & =-(0.25 \mathrm{~kg})(-5.4 \mathrm{~m} / \mathrm{s} \hat{\mathbf{j}}) \\
& =-(1.4 \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s}) \hat{\mathbf{j}}
\end{aligned}
$$

We don't have an easy way to calculate the momentum after the bounce. Instead, we reason from the symmetry of the situation.

Before the bounce, the ball starts with zero velocity and falls $1.50 \mathrm{~m}$ under the influence of gravity, achieving some amount of momentum just before it hits the ground. On the return trip (after the bounce), it starts with some amount of momentum, rises the same $1.50 \mathrm{~m}$ it fell, and ends with zero velocity. Thus, the motion after the bounce was the mirror image of the motion before the bounce. From this symmetry, it must be true that the ball's momentum after the bounce must be equal and opposite to its momentum before the bounce. (This is a subtle but crucial argument; make sure you understand it before you go on.) Therefore,

$$
\overrightarrow{\mathbf{p}}_{\mathbf{2}}=-\overrightarrow{\mathbf{p}}_{\mathbf{1}}=+(1.4 \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s}) \hat{\mathbf{j}}
$$

Thus, the ball's change of momentum during the bounce is

$$
\begin{aligned}
\Delta \overrightarrow{\mathbf{p}} & =\overrightarrow{\mathbf{p}}_{\mathbf{2}}-\overrightarrow{\mathbf{p}}_{\mathbf{1}} \\
& =(1.4 \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s}) \hat{\mathbf{j}}-(-1.4 \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s}) \hat{\mathbf{j}} \\
& =+(2.8 \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s}) \hat{\mathbf{j}}
\end{aligned}
$$

b. What was Earth's change of momentum due to the ball colliding with the floor?

Your instinctive response may well have been either "zero; the Earth is just too massive for that tiny ball to have affected it" or possibly, "more than zero, but utterly negligible." But no-if we re-define our system to be the Superball + Earth, then this system is closed (neglecting the gravitational pulls of the Sun, the Moon, and the other planets in the solar system), and therefore the total change of momentum of this new system must be zero. Therefore, Earth's change of momentum is exactly the same magnitude:

$$
\Delta \overrightarrow{\mathbf{p}}_{\text {Earth }}=-2.8 \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s} \hat{\mathbf{j}}
$$

c. What was Earth's change of velocity as a result of this collision?

This is where your instinctive feeling is probably correct:

$$
\begin{aligned}
\Delta \overrightarrow{\mathbf{v}}_{\text {Earth }} & =\frac{\Delta \overrightarrow{\mathbf{p}}_{\text {Earth }}}{M_{\text {Earth }}} \\
& =-\frac{2.8 \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s}}{5.97 \times 10^{24} \mathrm{~kg}} \hat{\mathbf{j}} \\
& =-\left(4.7 \times 10^{-25} \mathrm{~m} / \mathrm{s}\right) \hat{\mathbf{j}}
\end{aligned}
$$

This change of Earth's velocity is utterly negligible.

## Significance

It is important to realize that the answer to part (c) is not a velocity; it is a change of velocity, which is a very different thing. Nevertheless, to give you a feel for just how small that change of velocity is, suppose you were moving with a velocity of $4.7 \times 10^{-25} \mathrm{~m} / \mathrm{s}$. At this speed, it would take you about 7 million years to travel a distance equal to the diameter of a hydrogen atom.

## EXAMPLE 9.8

## Ice Hockey 1

Two hockey pucks of identical mass are on a flat, horizontal ice hockey rink. The red puck is motionless; the blue puck is moving at $2.5 \mathrm{~m} / \mathrm{s}$ to the left (Figure 9.18). It collides with the motionless red puck. The pucks have a mass of $15 \mathrm{~g}$. After the collision, the red puck is moving at $2.5 \mathrm{~m} / \mathrm{s}$, to the left. What is the final velocity of the blue puck?

## Strategy

We're told that we have two colliding objects, we're told the masses and initial velocities, and one final velocity; we're asked for both final velocities. Conservation of momentum seems like a good strategy. Define the system to be the two pucks; there's no friction, so we have a closed system.

Before you look at the solution, what do you think the answer will be?

The blue puck final velocity will be:

- zero
- $2.5 \mathrm{~m} / \mathrm{s}$ to the left
- $2.5 \mathrm{~m} / \mathrm{s}$ to the right
- $1.25 \mathrm{~m} / \mathrm{s}$ to the left
- $1.25 \mathrm{~m} / \mathrm{s}$ to the right
- something else


## Solution

Define the $+x$-direction to point to the right. Conservation of momentum then reads

$$
\begin{aligned}
\overrightarrow{\mathbf{p}}_{\mathbf{f}} & =\overrightarrow{\mathbf{p}}_{\mathbf{i}} \\
m v_{\mathrm{r}_{\mathrm{f}}} \hat{\mathbf{i}}+m v_{\mathrm{b}_{\mathrm{f}}} \hat{\mathbf{i}} & =m v_{\mathrm{r}_{\mathrm{i}}} \hat{\mathbf{i}}-m v_{\mathrm{b}_{\mathrm{i}}} \hat{\mathbf{i}}
\end{aligned}
$$

Before the collision, the momentum of the system is entirely and only in the blue puck. Thus,

$$
\begin{aligned}
m v_{\mathrm{r}_{\mathrm{f}}} \hat{\mathbf{i}}+m v_{\mathrm{b}_{\mathrm{f}}} \hat{\mathbf{i}} & =-m v_{\mathrm{b}_{\mathrm{i}}} \hat{\mathbf{i}} \\
v_{\mathrm{r}_{\mathrm{f}}} \hat{\mathbf{i}}+v_{\mathrm{b}_{\mathrm{f}}} \hat{\mathbf{i}} & =-v_{\mathrm{b}_{\mathrm{i}}} \hat{\mathbf{i}}
\end{aligned}
$$

(Remember that the masses of the pucks are equal.) Substituting numbers:

$$
\begin{aligned}
-(2.5 \mathrm{~m} / \mathrm{s}) \hat{\mathbf{i}}+\overrightarrow{\mathbf{v}}_{\mathrm{b}_{\mathrm{f}}} & =-(2.5 \mathrm{~m} / \mathrm{s}) \hat{\mathbf{i}} \\
\overrightarrow{\mathbf{v}}_{\mathrm{b}_{\mathrm{f}}} & =0
\end{aligned}
$$

## Significance

Evidently, the two pucks simply exchanged momentum. The blue puck transferred all of its momentum to the red puck. In fact, this is what happens in similar collision where $m_{1}=m_{2}$.

## EXAMPLE 9.9

## Landing of Philae

On November 12, 2014, the European Space Agency successfully landed a probe named Philae on Comet 67P/ Churyumov/Gerasimenko (Figure 9.19). During the landing, however, the probe actually landed three times, because it bounced twice. Let's calculate how much the comet's speed changed as a result of the first bounce.

Let's define upward to be the $+y$-direction, perpendicular to the surface of the comet, and $y=0$ to be at the surface of the comet. Here's what we know:

- The mass of Comet 67P: $M_{c}=1.0 \times 10^{13} \mathrm{~kg}$
- The acceleration due to the comet's gravity: $\overrightarrow{\mathbf{a}}=-\left(5.0 \times 10^{-3} \mathrm{~m} / \mathrm{s}^{2}\right) \hat{\mathbf{j}}$
- Philae's mass: $M_{p}=96 \mathrm{~kg}$
- Initial touchdown speed: $\overrightarrow{\mathbf{v}}_{\mathbf{1}}=-(1.0 \mathrm{~m} / \mathrm{s}) \hat{\mathbf{j}}$
- Initial upward speed due to first bounce: $\overrightarrow{\mathbf{v}}_{\mathbf{2}}=(0.38 \mathrm{~m} / \mathrm{s}) \hat{\mathbf{j}}$
- Landing impact time: $\Delta t=1.3 \mathrm{~s}$


## Strategy

We're asked for how much the comet's speed changed, but we don't know much about the comet, beyond its mass and the acceleration its gravity causes. However, we are told that the Philae lander collides with (lands on) the comet, and bounces off of it. A collision suggests momentum as a strategy for solving this problem.

If we define a system that consists of both Philae and Comet 67/P, then there is no net external force on this system, and thus the momentum of this system is conserved. (We'll neglect the gravitational force of the sun.)

Thus, if we calculate the change of momentum of the lander, we automatically have the change of momentum of the comet. Also, the comet's change of velocity is directly related to its change of momentum as a result of the lander "colliding" with it.

## Solution

Let $\overrightarrow{\mathbf{p}}_{1}$ be Philae's momentum at the moment just before touchdown, and $\overrightarrow{\mathbf{p}}_{2}$ be its momentum just after the first bounce. Then its momentum just before landing was

$$
\overrightarrow{\mathbf{p}}_{\mathbf{1}}=M_{p} \overrightarrow{\mathbf{v}}_{\mathbf{1}}=(96 \mathrm{~kg})(-1.0 \mathrm{~m} / \mathrm{s} \hat{\mathbf{j}})=-(96 \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s}) \hat{\mathbf{j}}
$$

and just after was

$$
\overrightarrow{\mathbf{p}}_{\mathbf{2}}=M_{p} \overrightarrow{\mathbf{v}}_{\mathbf{2}}=(96 \mathrm{~kg})(+0.38 \mathrm{~m} / \mathrm{s} \hat{\mathbf{j}})=(36.5 \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s}) \hat{\mathbf{j}}
$$

Therefore, the lander's change of momentum during the first bounce is

$$
\begin{aligned}
& \Delta \overrightarrow{\mathbf{p}}=\overrightarrow{\mathbf{p}}_{2}-\overrightarrow{\mathbf{p}}_{\mathbf{1}} \\
&=(36.5 \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s}) \hat{\mathbf{j}}-(-96.0 \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s} \hat{\mathbf{j}})=(133 \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s}) \hat{\mathbf{j}}
\end{aligned}
$$

Notice how important it is to include the negative sign of the initial momentum.

Now for the comet. Since momentum of the system must be conserved, the comet's momentum changed by exactly the negative of this:

$$
\Delta \overrightarrow{\mathbf{p}}_{\mathbf{c}}=-\Delta \overrightarrow{\mathbf{p}}=-(133 \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s}) \hat{\mathbf{j}}
$$

Therefore, its change of velocity is

$$
\Delta \overrightarrow{\mathbf{v}}_{\mathbf{c}}=\frac{\Delta \overrightarrow{\mathbf{p}}_{\mathbf{c}}}{M_{c}}=\frac{-(133 \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s}) \hat{\mathbf{j}}}{1.0 \times 10^{13} \mathrm{~kg}}=-\left(1.33 \times 10^{-11} \mathrm{~m} / \mathrm{s}\right) \hat{\mathbf{j}}
$$

## Significance

This is a very small change in velocity, about a thousandth of a billionth of a meter per second. Crucially, however, it is not zero.

### 9.4 Types of Collisions

Although momentum is conserved in all interactions, not all interactions (collisions or explosions) are the same. The possibilities include:

- A single object can explode into multiple objects (explosions).
- Multiple objects can collide and stick together, forming a single object (inelastic).
- Multiple objects can collide and bounce off of each other, remaining as multiple objects (elastic). If they do bounce off each other, then they may recoil at the same speeds with which they approached each other before the collision, or they may move off more slowly.

It's useful, therefore, to categorize different types of interactions, according to how the interacting objects
move before and after the interaction.

## Explosions

The first possibility is that a single object may break apart into two or more pieces. An example of this is a firecracker, or a bow and arrow, or a rocket rising through the air toward space. These can be difficult to analyze if the number of fragments after the collision is more than about three or four; but nevertheless, the total momentum of the system before and after the explosion is identical.

Note that if the object is initially motionless, then the system (which is just the object) has no momentum and no kinetic energy. After the explosion, the net momentum of all the pieces of the object must sum to zero (since the momentum of this closed system cannot change). However, the system will have a great deal of kinetic energy after the explosion, although it had none before. Thus, we see that, although the momentum of the system is conserved in an explosion, the kinetic energy of the system most definitely is not; it increases. This interaction-one object becoming many, with an increase of kinetic energy of the system-is called an explosion.

Where does the energy come from? Does conservation of energy still hold? Yes; some form of potential energy is converted to kinetic energy. In the case of gunpowder burning and pushing out a bullet, chemical potential energy is converted to kinetic energy of the bullet, and of the recoiling gun. For a bow and arrow, it is elastic potential energy in the bowstring.

## Inelastic

The second possibility is the reverse: that two or more objects collide with each other and stick together, thus (after the collision) forming one single composite object. The total mass of this composite object is the sum of the masses of the original objects, and the new single object moves with a velocity dictated by the conservation of momentum. However, it turns out again that, although the total momentum of the system of objects remains constant, the kinetic energy doesn't; but this time, the kinetic energy decreases. This type of collision is called inelastic.

Any collision where the objects stick together will result in the maximum loss of kinetic energy (i.e., $K_{\mathrm{f}}$ will be a minimum).

Such a collision is called perfectly inelastic. In the extreme case, multiple objects collide, stick together, and remain motionless after the collision. Since the objects are all motionless after the collision, the final kinetic energy is also zero; therefore, the loss of kinetic energy is a maximum.

- If $0<K_{\mathrm{f}}<K_{\mathrm{i}}$, the collision is inelastic.
- If $K_{\mathrm{f}}$ is the lowest energy, or the energy lost by both objects is the most, the collision is perfectly inelastic (objects stick together).
- If $K_{\mathrm{f}}=K_{\mathrm{i}}$, the collision is elastic.


## Elastic

The extreme case on the other end is if two or more objects approach each other, collide, and bounce off each other, moving away from each other at the same relative speed at which they approached each other. In this case, the total kinetic energy of the system is conserved. Such an interaction is called elastic.

In any interaction of a closed system of objects, the total momentum of the system is conserved $\left(\overrightarrow{\mathbf{p}}_{f}=\overrightarrow{\mathbf{p}}_{\mathrm{i}}\right)$ but the kinetic energy may not be:

- If $0<K_{\mathrm{f}}<K_{\mathrm{i}}$, the collision is inelastic.
- If $K_{\mathrm{f}}=0$, the collision is perfectly inelastic.
- If $K_{\mathrm{f}}=K_{\mathrm{i}}$, the collision is elastic.
- If $K_{\mathrm{f}}>K_{\mathrm{i}}$, the interaction is an explosion.

The point of all this is that, in analyzing a collision or explosion, you can use both momentum and kinetic energy.

## Collisions

A closed system always conserves momentum; it might also conserve kinetic energy, but very often it doesn't. Energy-momentum problems confined to a plane (as ours are) usually have two unknowns. Generally, this approach works well:

1. Define a closed system.
2. Write down the expression for conservation of momentum.
3. If kinetic energy is conserved, write down the expression for conservation of kinetic energy; if not, write down the expression for the change of kinetic energy.
4. You now have two equations in two unknowns, which you solve by standard methods.

## EXAMPLE 9.10

## Formation of a Deuteron

A proton (mass $1.67 \times 10^{-27} \mathrm{~kg}$ ) collides with a neutron (with essentially the same mass as the proton) to form a particle called a deuteron. What is the velocity of the deuteron if it is formed from a proton moving with velocity $7.0 \times 10^{6} \mathrm{~m} / \mathrm{s}$ to the left and a neutron moving with velocity $4.0 \times 10^{6} \mathrm{~m} / \mathrm{s}$ to the right?

## Strategy

Define the system to be the two particles. This is a collision, so we should first identify what kind. Since we are told the two particles form a single particle after the collision, this means that the collision is perfectly inelastic. Thus, kinetic energy is not conserved, but momentum is. Thus, we use conservation of momentum to determine the final velocity of the system.

## Solution

Treat the two particles as having identical masses $M$. Use the subscripts $\mathrm{p}, \mathrm{n}$, and $\mathrm{d}$ for proton, neutron, and deuteron, respectively. This is a one-dimensional problem, so we have

$$
M v_{\mathrm{p}}-M v_{\mathrm{n}}=2 M v_{\mathrm{d}}
$$

The masses divide out:

$$
\begin{aligned}
v_{\mathrm{p}}-v_{\mathrm{n}} & =2 v_{\mathrm{d}} \\
7.0 \times 10^{6} \mathrm{~m} / \mathrm{s}-4.0 \times 10^{6} \mathrm{~m} / \mathrm{s} & =2 v_{\mathrm{d}} \\
v_{\mathrm{d}} & =1.5 \times 10^{6} \mathrm{~m} / \mathrm{s}
\end{aligned}
$$

The velocity is thus $\overrightarrow{\mathbf{v}}_{\mathrm{d}}=\left(1.5 \times 10^{6} \mathrm{~m} / \mathrm{s}\right) \hat{\mathbf{i}}$.

## Significance

This is essentially how particle colliders like the Large Hadron Collider work: They accelerate particles up to very high speeds (large momenta), but in opposite directions. This maximizes the creation of so-called "daughter particles."

## Ice Hockey 2

(This is a variation of an earlier example.)

Two ice hockey pucks of different masses are on a flat, horizontal hockey rink. The red puck has a mass of 15 grams, and is motionless; the blue puck has a mass of 12 grams, and is moving at $2.5 \mathrm{~m} / \mathrm{s}$ to the left. It collides with the motionless red puck (Figure 9.20). If the collision is perfectly elastic, what are the final velocities of the two pucks?

## Strategy

We're told that we have two colliding objects, and we're told their masses and initial velocities; we're asked for both final velocities. Conservation of momentum seems like a good strategy; define the system to be the two pucks. There is no friction, so we have a closed system. We have two unknowns (the two final velocities), but only one equation. The comment about the collision being perfectly elastic is the clue; it suggests that kinetic energy is also conserved in this collision. That gives us our second equation.

The initial momentum and initial kinetic energy of the system resides entirely and only in the second puck (the blue one); the collision transfers some of this momentum and energy to the first puck.

## Solution

Conservation of momentum, in this case, reads

$$
\begin{aligned}
p_{\mathrm{i}} & =p_{\mathrm{f}} \\
m_{2} v_{2, \mathrm{i}} & =m_{1} v_{1, \mathrm{f}}+m_{2} v_{2, \mathrm{f}}
\end{aligned}
$$

Conservation of kinetic energy reads

$$
\begin{aligned}
K_{\mathrm{i}} & =K_{\mathrm{f}} \\
\frac{1}{2} m_{2} v_{2, \mathrm{i}}^{2} & =\frac{1}{2} m_{1} v_{1, \mathrm{f}}^{2}+\frac{1}{2} m_{2} v_{2, \mathrm{f}}^{2}
\end{aligned}
$$

There are our two equations in two unknowns. The algebra is tedious but not terribly difficult; you definitely should work it through. The solution is

$$
\begin{aligned}
& v_{1, \mathrm{f}}=\frac{\left(m_{1}-m_{2}\right) v_{1, \mathrm{i}}+2 m_{2} v_{2, \mathrm{i}}}{m_{1}+m_{2}} \\
& v_{2 \mathrm{f}}=\frac{\left(m_{2}-m_{1}\right) v_{2, \mathrm{i}}+2 m_{1} v_{1, \mathrm{i}}}{m_{1}+m_{2}}
\end{aligned}
$$

Substituting the given numbers, we obtain

$$
\begin{aligned}
& v_{1, \mathrm{f}}=2.22 \frac{\mathrm{m}}{\mathrm{s}} \\
& v_{2, \mathrm{f}}=-0.28 \frac{\mathrm{m}}{\mathrm{s}}
\end{aligned}
$$

## Significance

Notice that after the collision, the blue puck is moving to the right; its direction of motion was reversed. The red puck is now moving to the left.

## EXAMPLE 9.12

## Thor vs. Iron Man

The 2012 movie "The Avengers" has a scene where Iron Man and Thor fight. At the beginning of the fight, Thor throws his hammer at Iron Man, hitting him and throwing him slightly up into the air and against a small tree, which breaks. From the video, Iron Man is standing still when the hammer hits him. The distance between Thor and Iron Man is approximately $10 \mathrm{~m}$, and the hammer takes about $1 \mathrm{~s}$ to reach Iron Man after Thor releases it. The tree is about $2 \mathrm{~m}$ behind Iron Man, which he hits in about $0.75 \mathrm{~s}$. Also from the video, Iron Man's trajectory to the tree is very close to horizontal. Assuming Iron Man's total mass is $200 \mathrm{~kg}$ :

a. Estimate the mass of Thor's hammer

b. Estimate how much kinetic energy was lost in this collision

## Strategy

After the collision, Thor's hammer is in contact with Iron Man for the entire time, so this is a perfectly inelastic collision. Thus, with the correct choice of a closed system, we expect momentum is conserved, but not kinetic energy. We use the given numbers to estimate the initial momentum, the initial kinetic energy, and the final kinetic energy. Because this is a one-dimensional problem, we can go directly to the scalar form of the equations.

## Solution

a. First, we posit conservation of momentum. For that, we need a closed system. The choice here is the system (hammer + Iron Man), from the time of collision to the moment just before Iron Man and the hammer hit the tree. Let:

- $M_{\mathrm{H}}=$ mass of the hammer
- $M_{\mathrm{I}}=$ mass of Iron Man
- $v_{\mathrm{H}}=$ velocity of the hammer before hitting Iron Man
- $v=$ combined velocity of Iron Man + hammer after the collision

Again, Iron Man's initial velocity was zero. Conservation of momentum here reads:

$$
M_{\mathrm{H}} v_{\mathrm{H}}=\left(M_{\mathrm{H}}+M_{\mathrm{I}}\right) v
$$

We are asked to find the mass of the hammer, so we have

$$
\begin{aligned}
M_{\mathrm{H}} v_{\mathrm{H}} & =M_{\mathrm{H}} v+M_{\mathrm{I}} v \\
M_{\mathrm{H}}\left(v_{\mathrm{H}}-v\right) & =M_{\mathrm{I}} v \\
M_{\mathrm{H}} & =\frac{M_{\mathrm{I}} v}{v_{\mathrm{H}^{-}}-v} \\
& =\frac{(200 \mathrm{~kg})\left(\frac{2 \mathrm{~m}}{0.75 \mathrm{~s}}\right)}{10 \frac{\mathrm{m}}{\mathrm{s}}-\left(\frac{2 \mathrm{~m}}{0.75 \mathrm{~s}}\right)} \\
& =73 \mathrm{~kg}
\end{aligned}
$$

Considering the uncertainties in our estimates, this should be expressed with just one significant figure; thus, $M_{\mathrm{H}}=7 \times 10^{1} \mathrm{~kg}$.

b. The initial kinetic energy of the system, like the initial momentum, is all in the hammer:

$$
\begin{aligned}
K_{\mathrm{i}} & =\frac{1}{2} M_{\mathrm{H}} v_{\mathrm{H}}^{2} \\
& =\frac{1}{2}(70 \mathrm{~kg})(10 \mathrm{~m} / \mathrm{s})^{2} \\
& =3500 \mathrm{~J}
\end{aligned}
$$

After the collision,

$$
\begin{aligned}
K_{\mathrm{f}} & =\frac{1}{2}\left(M_{\mathrm{H}}+M_{\mathrm{I}}\right) v^{2} \\
& =\frac{1}{2}(70 \mathrm{~kg}+200 \mathrm{~kg})(2.67 \mathrm{~m} / \mathrm{s})^{2} \\
& =960 \mathrm{~J}
\end{aligned}
$$

Thus, there was a loss of $3500 \mathrm{~J}-960 \mathrm{~J}=2540 \mathrm{~J}$.

## Significance

From other scenes in the movie, Thor apparently can control the hammer's velocity with his mind. It is possible, therefore, that he mentally causes the hammer to maintain its initial velocity of $10 \mathrm{~m} / \mathrm{s}$ while Iron Man is being driven backward toward the tree. If so, this would represent an external force on our system, so it would not be closed. Thor's mental control of his hammer is beyond the scope of this book, however.

## EXAMPLE 9.13

## Analyzing a Car Crash

At a stoplight, a large truck ( $3000 \mathrm{~kg}$ ) collides with a motionless small car ( $1200 \mathrm{~kg}$ ). The truck comes to an instantaneous stop; the car slides straight ahead, coming to a stop after sliding 10 meters. The measured coefficient of friction between the car's tires and the road was 0.62 . How fast was the truck moving at the moment of impact?

## Strategy

At first it may seem we don't have enough information to solve this problem. Although we know the initial speed of the car, we don't know the speed of the truck (indeed, that's what we're asked to find), so we don't know the initial momentum of the system. Similarly, we know the final speed of the truck, but not the speed of the car immediately after impact. The fact that the car eventually slid to a speed of zero doesn't help with the final momentum, since an external friction force caused that. Nor can we calculate an impulse, since we don't know the collision time, or the amount of time the car slid before stopping. A useful strategy is to impose a restriction on the analysis.

Suppose we define a system consisting of just the truck and the car. The momentum of this system isn't conserved, because of the friction between the car and the road. But if we could find the speed of the car the instant after impact-before friction had any measurable effect on the car-then we could consider the momentum of the system to be conserved, with that restriction.

Can we find the final speed of the car? Yes; we invoke the work-kinetic energy theorem.

## Solution

First, define some variables. Let:

- $M_{\mathrm{c}}$ and $M_{\mathrm{T}}$ be the masses of the car and truck, respectively
- $v_{\mathrm{T}, \mathrm{i}}$ and $v_{\mathrm{T}, \mathrm{f}}$ be the velocities of the truck before and after the collision, respectively
- $v_{\mathrm{c}, \mathrm{i}}$ and $v_{\mathrm{c}, \mathrm{f}} \mathrm{Z}$ be the velocities of the car before and after the collision, respectively
- $K_{\mathrm{i}}$ and $K_{\mathrm{f}}$ be the kinetic energies of the car immediately after the collision, and after the car has stopped sliding (so $K_{\mathrm{f}}=0$ ).
- $d$ be the distance the car slides after the collision before eventually coming to a stop.

Since we actually want the initial speed of the truck, and since the truck is not part of the work-energy calculation, let's start with conservation of momentum. For the car + truck system, conservation of momentum reads

$$
\begin{aligned}
& p_{\mathrm{i}}=p_{\mathrm{f}} \\
& M_{\mathrm{c}} v_{\mathrm{c}, \mathrm{i}}+M_{\mathrm{T}} v_{\mathrm{T}, \mathrm{i}}=M_{\mathrm{c}} v_{\mathrm{c}, \mathrm{f}}+M_{\mathrm{T}} v_{\mathrm{T}, \mathrm{f}}
\end{aligned}
$$

Since the car's initial velocity was zero, as was the truck's final velocity, this simplifies to

$$
v_{\mathrm{T}, \mathrm{i}}=\frac{M_{\mathrm{c}}}{M_{\mathrm{T}}} v_{\mathrm{c}, \mathrm{f}}
$$

So now we need the car's speed immediately after impact. Recall that

$$
W=\Delta K
$$

where

$$
\begin{aligned}
\Delta K & =K_{\mathrm{f}}-K_{\mathrm{i}} \\
& =0-\frac{1}{2} M_{\mathrm{c}} v_{\mathrm{c}, \mathrm{f}}^{2}
\end{aligned}
$$

Also,

$$
W=\overrightarrow{\mathbf{F}} \cdot \overrightarrow{\mathbf{d}}=F d \cos \theta
$$

The work is done over the distance the car slides, which we've called $d$. Equating:

$$
F d \cos \theta=-\frac{1}{2} M_{\mathrm{c}} v_{\mathrm{c}, \mathrm{f}}^{2}
$$

Friction is the force on the car that does the work to stop the sliding. With a level road, the friction force is

$$
F=\mu_{\mathrm{k}} M_{\mathrm{c}} g
$$

Since the angle between the directions of the friction force vector and the displacement $d$ is $180^{\circ}$, and $\cos \left(180^{\circ}\right)=-1$, we have

$$
-\left(\mu_{\mathrm{k}} M_{\mathrm{c}} g\right) d=-\frac{1}{2} M_{\mathrm{c}} v_{\mathrm{c}, \mathrm{f}}^{2}
$$

(Notice that the car's mass divides out; evidently the mass of the car doesn't matter.)

Solving for the car's speed immediately after the collision gives

$$
v_{\mathrm{c}, \mathrm{f}}=\sqrt{2 \mu_{\mathrm{k}} g d}
$$

Substituting the given numbers:

$$
\begin{aligned}
v_{\mathrm{c}, \mathrm{f}} & =\sqrt{2(0.62)\left(9.81 \frac{\mathrm{m}}{\mathrm{s}^{2}}\right)(10 \mathrm{~m})} \\
& =11.0 \mathrm{~m} / \mathrm{s}
\end{aligned}
$$

Now we can calculate the initial speed of the truck:

$$
v_{\mathrm{T}, \mathrm{i}}=\left(\frac{1200 \mathrm{~kg}}{3000 \mathrm{~kg}}\right)\left(11.0 \frac{\mathrm{m}}{\mathrm{s}}\right)=4.4 \mathrm{~m} / \mathrm{s}
$$

## Significance

This is an example of the type of analysis done by investigators of major car accidents. A great deal of legal and financial consequences depend on an accurate analysis and calculation of momentum and energy.

## Subatomic Collisions and Momentum

Conservation of momentum is crucial to our understanding of atomic and subatomic particles because much of what we know about these particles comes from collision experiments.

At the beginning of the twentieth century, there was considerable interest in, and debate about, the structure of the atom. It was known that atoms contain two types of electrically charged particles: negatively charged electrons and positively charged protons. (The existence of an electrically neutral particle was suspected, but would not be confirmed until 1932.) The question was, how were these particles arranged in the atom? Were they distributed uniformly throughout the volume of the atom (as J.J. Thomson proposed), or arranged at the corners of regular polygons (which was Gilbert Lewis' model), or rings of negative charge that surround the positively charged nucleus-rather like the planetary rings surrounding Saturn (as suggested by Hantaro Nagaoka), or something else?

The New Zealand physicist Ernest Rutherford (along with the German physicist Hans Geiger and the British physicist Ernest Marsden) performed the crucial experiment in 1909. They bombarded a thin sheet of gold foil with a beam of high-energy (that is, high-speed) alpha-particles (the nucleus of a helium atom). The alphaparticles collided with the gold atoms, and their subsequent velocities were detected and analyzed, using conservation of momentum and conservation of energy.

If the charges of the gold atoms were distributed uniformly (per Thomson), then the alpha-particles should collide with them and nearly all would be deflected through many angles, all small; the Nagaoka model would produce a similar result. If the atoms were arranged as regular polygons (Lewis), the alpha-particles would deflect at a relatively small number of angles.

What actually happened is that nearly none of the alpha-particles were deflected. Those that were, were deflected at large angles, some close to $180^{\circ}$-those alpha-particles reversed direction completely (Figure 9.21). None of the existing atomic models could explain this. Eventually, Rutherford developed a model of the atom that was much closer to what we now have-again, using conservation of momentum and energy as his starting point.

### 9.5 Collisions in Multiple Dimensions

It is far more common for collisions to occur in two dimensions; that is, the angle between the initial velocity vectors is neither zero nor $180^{\circ}$. Let's see what complications arise from this.

The first idea we need is that momentum is a vector; like all vectors, it can be expressed as a sum of perpendicular components (usually, though not always, an $x$-component and a $y$-component, and a $z$-component if necessary). Thus, when we write down the statement of conservation of momentum for a problem, our momentum vectors can be, and usually will be, expressed in component form.

The second idea we need comes from the fact that momentum is related to force:

$$
\overrightarrow{\mathbf{F}}=\frac{d \overrightarrow{\mathbf{p}}}{d t}
$$

Expressing both the force and the momentum in component form,

$$
F_{x}=\frac{d p_{x}}{d t}, \quad F_{y}=\frac{d p_{y}}{d t}, \quad F_{z}=\frac{d p_{z}}{d t}
$$

Remember, these equations are simply Newton's second law, in vector form and in component form. We know that Newton's second law is true in each direction, independently of the others. It follows therefore (via Newton's third law) that conservation of momentum is also true in each direction independently.

These two ideas motivate the solution to two-dimensional problems: We write down the expression for conservation of momentum twice: once in the $x$-direction and once in the $y$-direction.

$$
\begin{align*}
& p_{\mathrm{f}, x}=p_{1, \mathrm{i}, x}+p_{2, \mathrm{i}, x} \\
& p_{\mathrm{f}, y}=p_{1, \mathrm{i}, y}+p_{2, \mathrm{i}, y}
\end{align*}
$$

We solve each of these two component equations independently to obtain the $x$ - and $y$-components of the
desired velocity vector:

$$
\begin{aligned}
& v_{\mathrm{f}, x}=\frac{m_{1} v_{1, \mathrm{i}, x}+m_{2} v_{2, \mathrm{i}, x}}{m} \\
& v_{\mathrm{f}, y}=\frac{m_{1} v_{1, \mathrm{i}, y}+m_{2} v_{2, \mathrm{i}, y}}{m}
\end{aligned}
$$

(Here, $m$ represents the total mass of the system.) Finally, combine these components using the Pythagorean theorem,

$$
v_{\mathrm{f}}=\left|\overrightarrow{\mathbf{v}}_{\mathbf{f}}\right|=\sqrt{v_{\mathrm{f}, x}^{2}+v_{\mathrm{f}, y}^{2}}
$$

## PROBLEM-SOLVING STRATEGY

## Conservation of Momentum in Two Dimensions

The method for solving a two-dimensional (or even three-dimensional) conservation of momentum problem is generally the same as the method for solving a one-dimensional problem, except that you have to conserve momentum in both (or all three) dimensions simultaneously:

1. Identify a closed system.
2. Write down the equation that represents conservation of momentum in the $x$-direction, and solve it for the desired quantity. If you are calculating a vector quantity (velocity, usually), this will give you the $x$-component of the vector.
3. Write down the equation that represents conservation of momentum in the $y$-direction, and solve. This will give you the $y$-component of your vector quantity.
4. Assuming you are calculating a vector quantity, use the Pythagorean theorem to calculate its magnitude, using the results of steps 3 and 4 .

## EXAMPLE 9.14

## Traffic Collision

A small car of mass $1200 \mathrm{~kg}$ traveling east at $60 \mathrm{~km} / \mathrm{hr}$ collides at an intersection with a truck of mass $3000 \mathrm{~kg}$ that is traveling due north at $40 \mathrm{~km} / \mathrm{hr}$ (Figure 9.23). The two vehicles are locked together. What is the velocity of the combined wreckage?

## Strategy

First off, we need a closed system. The natural system to choose is the (car + truck), but this system is not closed; friction from the road acts on both vehicles. We avoid this problem by restricting the question to finding the velocity at the instant just after the collision, so that friction has not yet had any effect on the system. With that restriction, momentum is conserved for this system.

Since there are two directions involved, we do conservation of momentum twice: once in the $x$-direction and once in the $y$-direction.

## Solution

Before the collision the total momentum is

$$
\overrightarrow{\mathbf{p}}=m_{\mathrm{c}} \overrightarrow{\mathbf{v}}_{\mathrm{c}}+m_{\mathrm{T}} \overrightarrow{\mathbf{v}}_{\mathrm{T}}
$$

After the collision, the wreckage has momentum

$$
\overrightarrow{\mathbf{p}}=\left(m_{\mathrm{c}}+m_{\mathrm{T}}\right) \overrightarrow{\mathbf{v}}_{w}
$$

Since the system is closed, momentum must be conserved, so we have

$$
m_{\mathrm{c}} \overrightarrow{\mathbf{v}}_{\mathbf{c}}+m_{\mathrm{T}} \overrightarrow{\mathbf{v}}_{\mathrm{T}}=\left(m_{\mathrm{c}}+m_{\mathrm{T}}\right) \overrightarrow{\mathbf{v}}_{w}
$$

We have to be careful; the two initial momenta are not parallel. We must add vectorially (Figure 9.24).

If we define the $+x$-direction to point east and the $+y$-direction to point north, as in the figure, then (conveniently),

$$
\begin{aligned}
\overrightarrow{\mathbf{p}}_{\mathrm{c}} & =p_{\mathrm{c}} \hat{\mathbf{i}}=m_{\mathrm{c}} v_{\mathrm{c}} \hat{\mathbf{i}} \\
\overrightarrow{\mathbf{p}}_{\mathrm{T}} & =p_{\mathrm{T}} \hat{\mathbf{j}}=m_{\mathrm{T}} v_{\mathrm{T}} \hat{\mathbf{j}}
\end{aligned}
$$

Therefore, in the $x$-direction:

$$
\begin{aligned}
m_{\mathrm{c}} v_{\mathrm{c}} & =\left(m_{\mathrm{c}}+m_{\mathrm{T}}\right) v_{\mathrm{w}, x} \\
v_{\mathrm{w}, x} & =\left(\frac{m_{\mathrm{c}}}{m_{\mathrm{c}}+m_{\mathrm{T}}}\right) v_{\mathrm{c}}
\end{aligned}
$$

and in the $y$-direction:

$$
\begin{aligned}
m_{\mathrm{T}} v_{\mathrm{T}} & =\left(m_{\mathrm{c}}+m_{\mathrm{T}}\right) v_{\mathrm{w}, y} \\
v_{\mathrm{w}, y} & =\left(\frac{m_{\mathrm{T}}}{m_{\mathrm{c}}+m_{\mathrm{T}}}\right) v_{\mathrm{T}}
\end{aligned}
$$

Applying the Pythagorean theorem gives

$$
\begin{aligned}
\left|\overrightarrow{\mathbf{v}}_{w}\right| & =\sqrt{\left[\left(\frac{m_{\mathrm{c}}}{m_{\mathrm{c}}+m_{t}}\right) v_{\mathrm{c}}\right]^{2}+\left[\left(\frac{m_{t}}{m_{\mathrm{c}}+m_{t}}\right) v_{t}\right]^{2}} \\
& =\sqrt{\left[\left(\frac{1200 \mathrm{~kg}}{4200 \mathrm{~kg}}\right)\left(16.67 \frac{\mathrm{m}}{\mathrm{s}}\right)\right]^{2}+\left[\left(\frac{3000 \mathrm{~kg}}{4200 \mathrm{~kg}}\right)\left(11.1 \frac{\mathrm{m}}{\mathrm{s}}\right)\right]^{2}} \\
& =\sqrt{\left(4.76 \frac{\mathrm{m}}{\mathrm{s}}\right)^{2}+\left(7.93 \frac{\mathrm{m}}{\mathrm{s}}\right)^{2}} \\
& =9.25 \frac{\mathrm{m}}{\mathrm{s}} \approx 33.3 \frac{\mathrm{km}}{\mathrm{hr}}
\end{aligned}
$$

As for its direction, using the angle shown in the figure,

$$
\theta=\tan ^{-1}\left(\frac{v_{\mathrm{w}, x}}{v_{\mathrm{w}, y}}\right)=\tan ^{-1}\left(\frac{7.93 \mathrm{~m} / \mathrm{s}}{4.76 \mathrm{~m} / \mathrm{s}}\right)=59^{\circ}
$$

This angle is east of north, or $31^{\circ}$ counterclockwise from the $+x$-direction.

## Significance

As a practical matter, accident investigators usually work in the "opposite direction"; they measure the distance of skid marks on the road (which gives the stopping distance) and use the work-energy theorem along with conservation of momentum to determine the speeds and directions of the cars prior to the collision. We saw that analysis in an earlier section.

## EXAMPLE 9.15

## Exploding Scuba Tank

A common scuba tank is an aluminum cylinder that weighs 31.7 pounds empty (Figure 9.25). When full of compressed air, the internal pressure is between 2500 and $3000 \mathrm{psi}$ (pounds per square inch). Suppose such a tank, which had been sitting motionless, suddenly explodes into three pieces. The first piece, weighing 10 pounds, shoots off horizontally at 235 miles per hour; the second piece ( 7 pounds) shoots off at 172 miles per hour, also in the horizontal plane, but at a $19^{\circ}$ angle to the first piece. What is the mass and initial velocity of the third piece? (Do all work, and express your final answer, in SI units.)

## Strategy

To use conservation of momentum, we need a closed system. If we define the system to be the scuba tank, this is not a closed system, since gravity is an external force. However, the problem asks for just the initial velocity of the third piece, so we can neglect the effect of gravity and consider the tank by itself as a closed system. Notice that, for this system, the initial momentum vector is zero.

We choose a coordinate system where all the motion happens in the $x y$-plane. We then write down the equations for conservation of momentum in each direction, thus obtaining the $x$ - and $y$-components of the momentum of the third piece, from which we obtain its magnitude (via the Pythagorean theorem) and its direction. Finally, dividing this momentum by the mass of the third piece gives us the velocity.

## Solution

First, let's get all the conversions to SI units out of the way:

$$
\begin{aligned}
& 31.7 \mathrm{lb} \times \frac{1 \mathrm{~kg}}{2.2 \mathrm{lb}} \rightarrow 14.4 \mathrm{~kg} \\
& 10 \mathrm{lb} \rightarrow 4.5 \mathrm{~kg} \\
& 235 \frac{\text { miles }}{\text { hour }} \times \frac{1 \text { hour }}{3600 \mathrm{~s}} \times \frac{1609 \mathrm{~m}}{\text { mile }}=105 \frac{\mathrm{m}}{\mathrm{s}} \\
& 7 \mathrm{lb} \rightarrow 3.2 \mathrm{~kg} \\
& 172 \frac{\text { mile }}{\text { hour }}=77 \frac{\mathrm{m}}{\mathrm{s}} \\
& m_{3}=14.4 \mathrm{~kg}-(4.5 \mathrm{~kg}+3.2 \mathrm{~kg})=6.7 \mathrm{~kg}
\end{aligned}
$$

Now apply conservation of momentum in each direction.

$x$-direction:

$$
\begin{aligned}
p_{\mathrm{f}, x} & =p_{0, x} \\
p_{1, x}+p_{2, x}+p_{3, x} & =0 \\
m_{1} v_{1, x}+m_{2} v_{2, x}+p_{3, x} & =0 \\
p_{3, x} & =-m_{1} v_{1, x}-m_{2} v_{2, x}
\end{aligned}
$$

2 -direction:

$$
\begin{aligned}
p_{\mathrm{f}, y} & =p_{0, y} \\
p_{1, y}+p_{2, y}+p_{3, y} & =0 \\
m_{1} v_{1, y}+m_{2} v_{2, y}+p_{3, y} & =0 \\
p_{3, y} & =-m_{1} v_{1, y}-m_{2} v_{2, y}
\end{aligned}
$$

From our chosen coordinate system, we write the $x$-components as

$$
\begin{aligned}
p_{3, x} & =-m_{1} v_{1}-m_{2} v_{2} \cos \theta \\
& =-(4.5 \mathrm{~kg})\left(105 \frac{\mathrm{m}}{\mathrm{s}}\right)-(3.2 \mathrm{~kg})\left(77 \frac{\mathrm{m}}{\mathrm{s}}\right) \cos \left(19^{\circ}\right) \\
& =-705 \frac{\mathrm{kg} \cdot \mathrm{m}}{\mathrm{s}}
\end{aligned}
$$

For the $y$-direction, we have

$$
\begin{aligned}
p_{3 y} & =0-m_{2} v_{2} \sin \theta \\
& =-(3.2 \mathrm{~kg})\left(77 \frac{\mathrm{m}}{\mathrm{s}}\right) \sin \left(19^{\circ}\right) \\
& =-80.2 \frac{\mathrm{kg} \cdot \mathrm{m}}{\mathrm{s}}
\end{aligned}
$$

This gives the magnitude of $p_{3}$ :

$$
\begin{aligned}
p_{3} & =\sqrt{p_{3, x}^{2}+p_{3, y}^{2}} \\
& =\sqrt{\left(-705 \frac{\mathrm{kg} \cdot \mathrm{m}}{\mathrm{s}}\right)^{2}+\left(-80.2 \frac{\mathrm{kg} \cdot \mathrm{m}}{\mathrm{s}}\right)} \\
& =710 \frac{\mathrm{kg} \cdot \mathrm{m}}{\mathrm{s}}
\end{aligned}
$$

The velocity of the third piece is therefore

$$
v_{3}=\frac{p_{3}}{m_{3}}=\frac{710 \frac{\mathrm{kg} \cdot \mathrm{m}}{\mathrm{s}}}{6.7 \mathrm{~kg}}=106 \frac{\mathrm{m}}{\mathrm{s}}
$$

The direction of its velocity vector is the same as the direction of its momentum vector:

$$
\phi=\tan ^{-1}\left(\frac{p_{3, y}}{p_{3, x}}\right)=\tan ^{-1}\left(\frac{80.2 \frac{\mathrm{kg} \cdot \mathrm{m}}{\mathrm{s}}}{705 \frac{\mathrm{kg} \cdot \mathrm{m}}{\mathrm{s}}}\right)=6.49^{\circ}
$$

Because $\phi$ is below the $-x$-axis, the actual angle is $183.5^{\circ}$ from the $+x$-direction.

## Significance

The enormous velocities here are typical; an exploding tank of any compressed gas can easily punch through the wall of a house and cause significant injury, or death. Fortunately, such explosions are extremely rare, on a percentage basis.

### 9.6 Center of Mass

We have been avoiding an important issue up to now: When we say that an object moves (more correctly, accelerates) in a way that obeys Newton's second law, we have been ignoring the fact that all objects are actually made of many constituent particles. A car has an engine, steering wheel, seats, passengers; a football is leather and rubber surrounding air; a brick is made of atoms. There are many different types of particles, and they are generally not distributed uniformly in the object. How do we include these facts into our calculations?

Then too, an extended object might change shape as it moves, such as a water balloon or a cat falling (Figure 9.26). This implies that the constituent particles are applying internal forces on each other, in addition to the external force that is acting on the object as a whole. We want to be able to handle this, as well.

The problem before us, then, is to determine what part of an extended object is obeying Newton's second law when an external force is applied and to determine how the motion of the object as a whole is affected by both the internal and external forces.

Be warned: To treat this new situation correctly, we must be rigorous and completely general. We won't make any assumptions about the nature of the object, or of its constituent particles, or either the internal or external forces. Thus, the arguments will be complex.

## Internal and External Forces

Suppose we have an extended object of mass $M$, made of $N$ interacting particles. Let's label their masses as $m_{j}$, where $j=1,2,3, \ldots, N$. Note that

$$
M=\sum_{j=1}^{N} m_{j}
$$

If we apply some net external force $\overrightarrow{\mathbf{F}}_{\text {ext }}$ on the object, every particle experiences some "share" or some fraction of that external force. Let:

$$
\overrightarrow{\mathbf{f}}_{j}^{\mathrm{ext}}=\text { the fraction of the external force that the } j \text { th particle experiences. }
$$

Notice that these fractions of the total force are not necessarily equal; indeed, they virtually never are. (They can be, but they usually aren't.) In general, therefore,

$$
\overrightarrow{\mathbf{f}}_{1}^{\mathrm{ext}} \neq \overrightarrow{\mathbf{f}}_{2}^{\mathrm{ext}} \neq \cdots \neq \overrightarrow{\mathbf{f}}_{N}^{\mathrm{ext}}
$$

Next, we assume that each of the particles making up our object can interact (apply forces on) every other particle of the object. We won't try to guess what kind of forces they are; but since these forces are the result of particles of the object acting on other particles of the same object, we refer to them as internal forces $\overrightarrow{\mathbf{f}}_{j}^{\text {int }}$; thus:

$\overrightarrow{\mathbf{f}}_{j}^{\text {int }}=$ the net internal force that the $j$ th particle experiences from all the other particles that make up the object.

Now, the net force, internal plus external, on the $j$ th particle is the vector sum of these:

$$
\overrightarrow{\mathbf{f}}_{j}=\overrightarrow{\mathbf{f}}_{j}^{\mathrm{int}}+\overrightarrow{\mathbf{f}}_{j}^{\mathrm{ext}}
$$

where again, this is for all $N$ particles; $j=1,2,3, \ldots, N$.

As a result of this fractional force, the momentum of each particle gets changed:

$$
\begin{align*}
\overrightarrow{\mathbf{f}}_{j} & =\frac{d \overrightarrow{\mathbf{p}}_{j}}{d t} \\
\overrightarrow{\mathbf{f}}_{j}^{\text {int }}+\overrightarrow{\mathbf{f}}_{j}^{\mathrm{ext}} & =\frac{d \overrightarrow{\mathbf{p}}_{j}}{d t}
\end{align*}
$$

The net force $\overrightarrow{\mathbf{F}}$ on the object is the vector sum of these forces:

$$
\begin{align*}
\overrightarrow{\mathbf{F}}_{\text {net }} & =\sum_{j=1}^{N}\left(\overrightarrow{\mathbf{f}}_{\mathbf{j}}^{\text {int }}+\overrightarrow{\mathbf{f}}_{\mathbf{j}}^{\mathbf{e x t}}\right) \\
& =\sum_{j=1}^{N} \overrightarrow{\mathbf{f}}_{\mathbf{j}}^{\text {int }}+\sum_{j=1}^{N} \overrightarrow{\mathbf{f}}_{\mathbf{j}}^{\mathbf{e x t}}
\end{align*}
$$

This net force changes the momentum of the object as a whole, and the net change of momentum of the object must be the vector sum of all the individual changes of momentum of all of the particles:

$$
\overrightarrow{\mathbf{F}}_{\mathrm{net}}=\sum_{j=1}^{N} \frac{d \overrightarrow{\mathbf{p}}_{j}}{d t}
$$

Combining Equation 9.22 and Equation 9.23 gives

$$
\sum_{j=1}^{N} \overrightarrow{\mathbf{f}}_{j}^{\mathrm{int}}+\sum_{j=1}^{N} \overrightarrow{\mathbf{f}}_{j}^{\mathrm{ext}}=\sum_{j=1}^{N} \frac{d \overrightarrow{\mathbf{p}}_{j}}{d t}
$$

Let's now think about these summations. First consider the internal forces term; remember that each $\overrightarrow{\mathbf{f}}_{j}^{\text {int }}$ is the force on the $j$ th particle from the other particles in the object. But by Newton's third law, for every one of these forces, there must be another force that has the same magnitude, but the opposite sign (points in the opposite direction). These forces do not cancel; however, that's not what we're doing in the summation. Rather, we're simply mathematically adding up all the internal force vectors. That is, in general, the internal forces for any individual part of the object won't cancel, but when all the internal forces are added up, the internal forces must cancel in pairs. It follows, therefore, that the sum of all the internal forces must be zero:

$$
\sum_{j=1}^{N} \overrightarrow{\mathbf{f}}_{j}^{\text {int }}=0
$$

(This argument is subtle, but crucial; take plenty of time to completely understand it.)

For the external forces, this summation is simply the total external force that was applied to the whole object:

$$
\sum_{j=1}^{N} \overrightarrow{\mathbf{f}}_{j}^{\mathrm{ext}}=\overrightarrow{\mathbf{F}}_{\mathrm{ext}}
$$

As a result,

$$
\overrightarrow{\mathbf{F}}_{\mathrm{ext}}=\sum_{j=1}^{N} \frac{d \overrightarrow{\mathbf{p}}_{j}}{d t}
$$

This is an important result. Equation 9.25 tells us that the total change of momentum of the entire object (all $N$ particles) is due only to the external forces; the internal forces do not change the momentum of the object as a whole. This is why you can't lift yourself in the air by standing in a basket and pulling up on the handles: For the system of you + basket, your upward pulling force is an internal force.

## Force and Momentum

Remember that our actual goal is to determine the equation of motion for the entire object (the entire system of particles). To that end, let's define:

$\overrightarrow{\mathbf{p}}_{\mathrm{CM}}=$ the total momentum of the system of $N$ particles (the reason for the subscript will become clear shortly) Then we have

$$
\overrightarrow{\mathbf{p}}_{\mathrm{CM}} \equiv \sum_{j=1}^{N} \overrightarrow{\mathbf{p}}_{j}
$$

and therefore Equation 9.25 can be written simply as

$$
\overrightarrow{\mathbf{F}}=\frac{d \overrightarrow{\mathbf{p}}_{\mathrm{CM}}}{d t}
$$

Since this change of momentum is caused by only the net external force, we have dropped the "ext" subscript.

This is Newton's second law, but now for the entire extended object. If this feels a bit anticlimactic, remember what is hiding inside it: $\overrightarrow{\mathbf{p}}_{\mathrm{CM}}$ is the vector sum of the momentum of (in principle) hundreds of thousands of billions of billions of particles $\left(6.02 \times 10^{23}\right)$, all caused by one simple net external force-a force that you can calculate.

## Center of Mass

Our next task is to determine what part of the extended object, if any, is obeying Equation 9.26.

It's tempting to take the next step; does the following equation mean anything?

$$
\overrightarrow{\mathbf{F}}=M \overrightarrow{\mathbf{a}}
$$

If it does mean something (acceleration of what, exactly?), then we could write

$$
M \overrightarrow{\mathbf{a}}=\frac{d \overrightarrow{\mathbf{p}}_{\mathrm{CM}}}{d t}
$$

and thus

$$
M \overrightarrow{\mathbf{a}}=\sum_{j=1}^{N} \frac{d \overrightarrow{\mathbf{p}}_{j}}{d t}=\frac{d}{d t} \sum_{j=1}^{N} \overrightarrow{\mathbf{p}}_{j}
$$

which follows because the derivative of a sum is equal to the sum of the derivatives.

Now, $\overrightarrow{\mathbf{p}}_{j}$ is the momentum of the $j$ th particle. Defining the positions of the constituent particles (relative to some coordinate system) as $\overrightarrow{\mathbf{r}}_{\mathbf{j}}=\left(x_{j}, y_{j}, z_{j}\right)$, we thus have

$$
\overrightarrow{\mathbf{p}}_{j}=m_{j} \overrightarrow{\mathbf{v}}_{j}=m_{j} \frac{d \overrightarrow{\mathbf{r}}_{j}}{d t}
$$

Substituting back, we obtain

$$
\begin{aligned}
M \overrightarrow{\mathbf{a}} & =\frac{d}{d t} \sum_{j=1}^{N} m_{j} \frac{d \overrightarrow{\mathbf{r}}_{j}}{d t} \\
& =\frac{d^{2}}{d t^{2}} \sum_{j=1}^{N} m_{j} \overrightarrow{\mathbf{r}}_{j}
\end{aligned}
$$

Dividing both sides by $M$ (the total mass of the extended object) gives us

$$
\overrightarrow{\mathbf{a}}=\frac{d^{2}}{d t^{2}}\left(\frac{1}{M} \sum_{j=1}^{N} m_{j} \overrightarrow{\mathbf{r}}_{j}\right)
$$

Thus, the point in the object that traces out the trajectory dictated by the applied force in Equation 9.27 is inside the parentheses in Equation 9.28 .

Looking at this calculation, notice that (inside the parentheses) we are calculating the product of each particle's mass with its position, adding all $N$ of these up, and dividing this sum by the total mass of particles we summed. This is reminiscent of an average; inspired by this, we'll (loosely) interpret it to be the weighted average position of the mass of the extended object. It's actually called the center of mass of the object. Notice that the position of the center of mass has units of meters; that suggests a definition:

$$
\overrightarrow{\mathbf{r}}_{\mathrm{CM}} \equiv \frac{1}{M} \sum_{j=1}^{N} m_{j} \overrightarrow{\mathbf{r}}_{j}
$$

So, the point that obeys Equation 9.26 (and therefore Equation 9.27 as well) is the center of mass of the object, which is located at the position vector $\overrightarrow{\mathbf{r}}_{\mathrm{CM}}$.

It may surprise you to learn that there does not have to be any actual mass at the center of mass of an object. For example, a hollow steel sphere with a vacuum inside it is spherically symmetrical (meaning its mass is uniformly distributed about the center of the sphere); all of the sphere's mass is out on its surface, with no mass inside. But it can be shown that the center of mass of the sphere is at its geometric center, which seems reasonable. Thus, there is no mass at the position of the center of mass of the sphere. (Another example is a doughnut.) The procedure to find the center of mass is illustrated in Figure 9.27.

Since $\overrightarrow{\mathbf{r}}_{j}=x_{j} \hat{\mathbf{i}}+y_{j} \hat{\mathbf{j}}+z_{j} \hat{\mathbf{k}}$, it follows that:

$$
\begin{align*}
& r_{\mathrm{CM}, x}=\frac{1}{M} \sum_{j=1}^{N} m_{j} x_{j} \\
& r_{\mathrm{CM}, y}=\frac{1}{M} \sum_{j=1}^{N} m_{j} y_{j} \\
& r_{\mathrm{CM}, z}=\frac{1}{M} \sum_{j=1}^{N} m_{j} z_{j}
\end{align*}
$$

and thus

$$
\begin{aligned}
& \overrightarrow{\mathbf{r}}_{\mathrm{CM}}=r_{\mathrm{CM}, x} \hat{\mathbf{i}}+r_{\mathrm{CM}, y} \hat{\mathbf{j}}+r_{\mathrm{CM}, z} \hat{\mathbf{k}} \\
& r_{\mathrm{CM}}=\left|\overrightarrow{\mathbf{r}}_{\mathrm{CM}}\right|=\left(r_{\mathrm{CM}, x}^{2}+r_{\mathrm{CM}, y}^{2}+r_{\mathrm{CM}, z}^{2}\right)^{1 / 2}
\end{aligned}
$$

Therefore, you can calculate the components of the center of mass vector individually.

Finally, to complete the kinematics, the instantaneous velocity of the center of mass is calculated exactly as you might suspect:

$$
\overrightarrow{\mathbf{v}}_{\mathrm{CM}}=\frac{d}{d t}\left(\frac{1}{M} \sum_{j=1}^{N} m_{j} \overrightarrow{\mathbf{r}}_{j}\right)=\frac{1}{M} \sum_{j=1}^{N} m_{j} \overrightarrow{\mathbf{v}}_{j}
$$

and this, like the position, has $x^{-}, y$-, and $z$-components.

To calculate the center of mass in actual situations, we recommend the following procedure:

## PROBLEM-SOLVING STRATEG

## Calculating the Center of Mass

The center of mass of an object is a position vector. Thus, to calculate it, do these steps:

1. Define your coordinate system. Typically, the origin is placed at the location of one of the particles. This is not required, however.
2. Determine the $x, y, z$-coordinates of each particle that makes up the object.
3. Determine the mass of each particle, and sum them to obtain the total mass of the object. Note that the mass of the object at the origin must be included in the total mass.
4. Calculate the $x^{-}, y^{-}$, and $z$-components of the center of mass vector, using Equation 9.30, Equation 9.31, and Equation 9.32 .
5. If required, use the Pythagorean theorem to determine its magnitude.

Here are two examples that will give you a feel for what the center of mass is.

## EXAMPLE 9.16

## Center of Mass of the Earth-Moon System

Using data from text appendix, determine how far the center of mass of the Earth-moon system is from the center of Earth. Compare this distance to the radius of Earth, and comment on the result. Ignore the other objects in the solar system.

## Strategy

We get the masses and separation distance of the Earth and moon, impose a coordinate system, and use Equation 9.29 with just $N=2$ objects. We use a subscript "e" to refer to Earth, and subscript "m" to refer to the moon.

## Solution

Define the origin of the coordinate system as the center of Earth. Then, with just two objects, Equation 9.29 becomes

$$
R=\frac{m_{\mathrm{e}} r_{\mathrm{e}}+m_{\mathrm{m}} r_{\mathrm{m}}}{m_{\mathrm{e}}+m_{\mathrm{m}}}
$$

From Appendix D,

$$
\begin{aligned}
m_{\mathrm{e}} & =5.97 \times 10^{24} \mathrm{~kg} \\
m_{\mathrm{m}} & =7.36 \times 10^{22} \mathrm{~kg} \\
r_{\mathrm{m}} & =3.82 \times 10^{8} \mathrm{~m}
\end{aligned}
$$

We defined the center of Earth as the origin, so $r_{\mathrm{e}}=0 \mathrm{~m}$. Inserting these into the equation for $R$ gives

$$
\begin{aligned}
R & =\frac{\left(5.97 \times 10^{24} \mathrm{~kg}\right)(0 \mathrm{~m})+\left(7.36 \times 10^{22} \mathrm{~kg}\right)\left(3.82 \times 10^{8} \mathrm{~m}\right)}{5.97 \times 10^{24} \mathrm{~kg}+7.36 \times 10^{22} \mathrm{~kg}} \\
& =4.64 \times 10^{6} \mathrm{~m}
\end{aligned}
$$

## Significance

The radius of Earth is $6.37 \times 10^{6} \mathrm{~m}$, so the center of mass of the Earth-moon system is ( $6.37-4.64$ ) $\times 10^{6} \mathrm{~m}=1.73 \times 10^{6} \mathrm{~m}=1730 \mathrm{~km}$ (roughly 1080 miles) below the surface of Earth. The location of the center of mass is shown (not to scale).

## EXAMPLE 9.17

## Center of Mass of a Salt Crystal

Figure 9.28 shows a single crystal of sodium chloride-ordinary table salt. The sodium and chloride ions form a single unit, $\mathrm{NaCl}$. When multiple $\mathrm{NaCl}$ units group together, they form a cubic lattice. The smallest possible cube (called the unit cell) consists of four sodium ions and four chloride ions, alternating. The length of one edge of this cube (i.e., the bond length) is $2.36 \times 10^{-10} \mathrm{~m}$. Find the location of the center of mass of the unit cell. Specify it either by its coordinates $\left(r_{\mathrm{CM}, x}, r_{\mathrm{CM}, y}, r_{\mathrm{CM}, z}\right)$, or by $r_{\mathrm{CM}}$ and two angles.

## Strategy

We can look up all the ion masses. If we impose a coordinate system on the unit cell, this will give us the positions of the ions. We can then apply Equation 9.30, Equation 9.31, and Equation 9.32 (along with the Pythagorean theorem).

## Solution

Define the origin to be at the location of the chloride ion at the bottom left of the unit cell. Figure 9.29 shows the coordinate system.

There are eight ions in this crystal, so $N=8$ :

$$
\overrightarrow{\mathbf{r}}_{\mathrm{CM}}=\frac{1}{M} \sum_{j=1}^{8} m_{j} \overrightarrow{\mathbf{r}}_{j}
$$

The mass of each of the chloride ions is

$$
35.453 \mathrm{u} \times \frac{1.660 \times 10^{-27} \mathrm{~kg}}{\mathrm{u}}=5.885 \times 10^{-26} \mathrm{~kg}
$$

so we have

$$
m_{1}=m_{3}=m_{6}=m_{8}=5.885 \times 10^{-26} \mathrm{~kg}
$$

For the sodium ions,

$$
m_{2}=m_{4}=m_{5}=m_{7}=3.816 \times 10^{-26} \mathrm{~kg}
$$

The total mass of the unit cell is therefore

$$
M=(4)\left(5.885 \times 10^{-26} \mathrm{~kg}\right)+(4)\left(3.816 \times 10^{-26} \mathrm{~kg}\right)=3.880 \times 10^{-25} \mathrm{~kg}
$$

From the geometry, the locations are

$$
\begin{aligned}
& \overrightarrow{\mathbf{r}}_{1}=0 \\
& \overrightarrow{\mathbf{r}}_{2}=\left(2.36 \times 10^{-10} \mathrm{~m}\right) \hat{\mathbf{i}} \\
& \overrightarrow{\mathbf{r}}_{3}=r_{3 x} \hat{\mathbf{i}}+r_{3 y} \hat{\mathbf{j}}=\left(2.36 \times 10^{-10} \mathrm{~m}\right) \hat{\mathbf{i}}+\left(2.36 \times 10^{-10} \mathrm{~m}\right) \hat{\mathbf{j}} \\
& \overrightarrow{\mathbf{r}}_{4}=\left(2.36 \times 10^{-10} \mathrm{~m}\right) \hat{\mathbf{j}} \\
& \overrightarrow{\mathbf{r}}_{5}=\left(2.36 \times 10^{-10} \mathrm{~m}\right) \overrightarrow{\mathbf{k}} \\
& \overrightarrow{\mathbf{r}}_{6}=r_{6 x} \hat{\mathbf{i}}+r_{6 z} \widehat{\mathbf{k}}=\left(2.36 \times 10^{-10} \mathrm{~m}\right) \hat{\mathbf{i}}+\left(2.36 \times 10^{-10} \mathrm{~m}\right) \hat{\mathbf{k}} \\
& \overrightarrow{\mathbf{r}}_{7}=r_{7 x} \hat{\mathbf{i}}+r_{7 y} \hat{\mathbf{j}}+r_{7 z} \hat{\mathbf{k}}=\left(2.36 \times 10^{-10} \mathrm{~m}\right) \hat{\mathbf{i}}+\left(2.36 \times 10^{-10} \mathrm{~m}\right) \hat{\mathbf{j}}+\left(2.36 \times 10^{-10} \mathrm{~m}\right) \hat{\mathbf{k}} \\
& \overrightarrow{\mathbf{r}}_{8}=r_{8 y} \hat{\mathbf{j}}+r_{8 z} \widehat{\mathbf{k}}=\left(2.36 \times 10^{-10} \mathrm{~m}\right) \hat{\mathbf{j}}+\left(2.36 \times 10^{-10} \mathrm{~m}\right) \hat{\mathbf{k}}
\end{aligned}
$$

Substituting:

$$
\begin{aligned}
\left|\overrightarrow{\mathbf{r}}_{\mathrm{CM}, x}\right| & =\sqrt{r_{\mathrm{CM}, x}^{2}+r_{\mathrm{CM}, y}^{2}+r_{\mathrm{CM}, z}^{2}} \\
= & \frac{1}{M} \sum_{j=1}^{8} m_{j}\left(r_{x}\right)_{j} \\
= & \frac{1}{M}\left(m_{1} r_{1 x}+m_{2} r_{2 x}+m_{3} r_{3 x}+m_{4} r_{4 x}+m_{5} r_{5 x}+m_{6} r_{6 x}+m_{7} r_{7 x}+m_{8} r_{8 x}\right) \\
= & \frac{1}{3.8804 \times 10^{-25} \mathrm{~kg}}\left[\left(5.885 \times 10^{-26} \mathrm{~kg}\right)(0 \mathrm{~m})+\left(3.816 \times 10^{-26} \mathrm{~kg}\right)\left(2.36 \times 10^{-10} \mathrm{~m}\right)\right. \\
& +\left(5.885 \times 10^{-26} \mathrm{~kg}\right)\left(2.36 \times 10^{-10} \mathrm{~m}\right) \\
& +\left(3.816 \times 10^{-26} \mathrm{~kg}\right)\left(2.36 \times 10^{-10} \mathrm{~m}\right)+0+0 \\
& \left.+\left(3.816 \times 10^{-26} \mathrm{~kg}\right)\left(2.36 \times 10^{-10} \mathrm{~m}\right)+0\right] \\
& =1.18 \times 10^{-10} \mathrm{~m} .
\end{aligned}
$$

Similar calculations give $r_{\mathrm{CM}, y}=r_{\mathrm{CM}, z}=1.18 \times 10^{-10} \mathrm{~m}$ (you could argue that this must be true, by symmetry, but it's a good idea to check).

## Significance

Although this is a great exercise to determine the center of mass given a Chloride ion at the origin, in fact the origin could be chosen at any location. Therefore, there is no meaningful application of the center of mass of a unit cell beyond as an exercise.

Two crucial concepts come out of these examples:

1. As with all problems, you must define your coordinate system and origin. For center-of-mass calculations, it often makes sense to choose your origin to be located at one of the masses of your system. That choice automatically defines its distance in Equation 9.29 to be zero. However, you must still include the mass of the object at your origin in your calculation of $M$, the total mass Equation 9.19. In the Earth-moon system example, this means including the mass of Earth. If you hadn't, you'd have ended up with the center of mass of the system being at the center of the moon, which is clearly wrong.
2. In the second example (the salt crystal), notice that there is no mass at all at the location of the center of mass. This is an example of what we stated above, that there does not have to be any actual mass at the center of mass of an object.

## Center of Mass of Continuous Objects

If the object in question has its mass distributed uniformly in space, rather than as a collection of discrete particles, then $m_{j} \rightarrow d m$, and the summation becomes an integral:

$$
\overrightarrow{\mathbf{r}}_{\mathrm{CM}}=\frac{1}{M} \int \overrightarrow{\mathbf{r}} d m
$$

In this context, $r$ is a characteristic dimension of the object (the radius of a sphere, the length of a long rod). To generate an integrand that can actually be calculated, you need to express the differential mass element $d m$ as a function of the mass density of the continuous object, and the dimension $r$. An example will clarify this.

## EXAMPLE 9.18

## CM of a Uniform Thin Hoop

Find the center of mass of a uniform thin hoop (or ring) of mass $M$ and radius $r$.

## Strategy

First, the hoop's symmetry suggests the center of mass should be at its geometric center. If we define our coordinate system such that the origin is located at the center of the hoop, the integral should evaluate to zero.

We replace $d m$ with an expression involving the density of the hoop and the radius of the hoop. We then have an expression we can actually integrate. Since the hoop is described as "thin," we treat it as a one-dimensional object, neglecting the thickness of the hoop. Therefore, its density is expressed as the number of kilograms of material per meter. Such a density is called a linear mass density, and is given the symbol $\lambda$; this is the Greek letter "lambda," which is the equivalent of the English letter "l" (for "linear").

Since the hoop is described as uniform, this means that the linear mass density $\lambda$ is constant. Thus, to get our expression for the differential mass element $d m$, we multiply $\lambda$ by a differential length of the hoop, substitute, and integrate (with appropriate limits for the definite integral).

## Solution

First, define our coordinate system and the relevant variables (Figure 9.30).

The center of mass is calculated with Equation 9.34:

$$
\overrightarrow{\mathbf{r}}_{\mathrm{CM}}=\frac{1}{M} \int_{a}^{b} \overrightarrow{\mathbf{r}} d m
$$

We have to determine the limits of integration $a$ and $b$. Expressing $\overrightarrow{\mathbf{r}}$ in component form gives us

$$
\overrightarrow{\mathbf{r}}_{\mathrm{CM}}=\frac{1}{M} \int_{a}^{b}[(r \cos \theta) \hat{\mathbf{i}}+(r \sin \theta) \hat{\mathbf{j}}] d m
$$

In the diagram, we highlighted a piece of the hoop that is of differential length $d s$; it therefore has a differential mass $d m=\lambda d s$. Substituting:

$$
\overrightarrow{\mathbf{r}}_{\mathrm{CM}}=\frac{1}{M} \int_{a}^{b}[(r \cos \theta) \hat{\mathbf{i}}+(r \sin \theta) \hat{\mathbf{j}}] \lambda d s
$$

However, the arc length $d s$ subtends a differential angle $d \theta$, so we have

$$
d s=r d \theta
$$

and thus

$$
\overrightarrow{\mathbf{r}}_{\mathrm{CM}}=\frac{1}{M} \int_{a}^{b}[(r \cos \theta) \hat{\mathbf{i}}+(r \sin \theta) \hat{\mathbf{j}}] \lambda r d \theta
$$

One more step: Since $\lambda$ is the linear mass density, it is computed by dividing the total mass by the length of the hoop:

$$
\lambda=\frac{M}{2 \pi r}
$$

giving us

$$
\begin{aligned}
\overrightarrow{\mathbf{r}}_{\mathrm{CM}} & =\frac{1}{M} \int_{a}^{b}[(r \cos \theta) \hat{\mathbf{i}}+(r \sin \theta) \hat{\mathbf{j}}]\left(\frac{M}{2 \pi r}\right) r d \theta \\
& =\frac{1}{2 \pi} \int_{a}^{b}[(r \cos \theta) \hat{\mathbf{i}}+(r \sin \theta) \hat{\mathbf{j}}] d \theta
\end{aligned}
$$

Notice that the variable of integration is now the angle $\theta$. This tells us that the limits of integration (around the circular hoop) are $\theta=0$ to $\theta=2 \pi$, so $a=0$ and $b=2 \pi$. Also, for convenience, we separate the integral into the $x$ - and $y$-components of $\overrightarrow{\mathbf{r}}_{\mathrm{CM}}$. The final integral expression is

$$
\begin{aligned}
\overrightarrow{\mathbf{r}}_{\mathrm{CM}} & =r_{\mathrm{CM}, x} \hat{\mathbf{i}}+r_{\mathrm{CM}, y} \hat{\mathbf{j}} \\
& =\left[\frac{1}{2 \pi} \int_{0}^{2 \pi}(r \cos \theta) d \theta\right] \hat{\mathbf{i}}+\left[\frac{1}{2 \pi} \int_{0}^{2 \pi}(r \sin \theta) d \theta\right] \hat{\mathbf{j}} \\
& =0 \hat{\mathbf{i}}+0 \hat{\mathbf{j}}=\overrightarrow{\mathbf{0}}
\end{aligned}
$$

as expected.

## Center of Mass and Conservation of Momentum

How does all this connect to conservation of momentum?

Suppose you have $N$ objects with masses $m_{1}, m_{2}, m_{3}, \ldots m_{N}$ and initial velocities $\overrightarrow{\mathbf{v}}_{1}, \overrightarrow{\mathbf{v}}_{2}, \overrightarrow{\mathbf{v}}_{3}, \ldots, \overrightarrow{\mathbf{v}}_{N}$. The center of mass of the objects is

$$
\overrightarrow{\mathbf{r}}_{\mathrm{CM}}=\frac{1}{M} \sum_{j=1}^{N} m_{j} \overrightarrow{\mathbf{r}}_{j}
$$

Its velocity is

$$
\overrightarrow{\mathbf{v}}_{\mathrm{CM}}=\frac{d \overrightarrow{\mathbf{r}}_{\mathrm{CM}}}{d t}=\frac{1}{M} \sum_{j=1}^{N} m_{j} \frac{d \overrightarrow{\mathbf{r}}_{j}}{d t}
$$

and thus the initial momentum of the center of mass is

$$
\begin{aligned}
{\left[M \frac{d \overrightarrow{\mathbf{r}}_{\mathrm{CM}}}{d t}\right]_{\mathrm{i}} } & =\sum_{j=1}^{N} m_{j} \frac{d \overrightarrow{\mathbf{r}}_{j, \mathrm{i}}}{d t} \\
M \overrightarrow{\mathbf{v}}_{\mathrm{CM}, \mathrm{i}} & =\sum_{j=1}^{N} m_{j} \overrightarrow{\mathbf{v}}_{j, \mathrm{i}}
\end{aligned}
$$

After these masses move and interact with each other, the momentum of the center of mass is

$$
M \overrightarrow{\mathbf{v}}_{\mathrm{CM}, \mathrm{f}}=\sum_{j=1}^{N} m_{j} \overrightarrow{\mathbf{v}}_{j, \mathrm{f}}
$$

But conservation of momentum tells us that the right-hand side of both equations must be equal, which says

$$
M \overrightarrow{\mathbf{v}}_{\mathrm{CM}, \mathrm{f}}=M \overrightarrow{\mathbf{v}}_{\mathrm{CM}, \mathrm{i}}
$$

This result implies that conservation of momentum is expressed in terms of the center of mass of the system. Notice that as an object moves through space with no net external force acting on it, an individual particle of the object may accelerate in various directions, with various magnitudes, depending on the net internal force acting on that object at any time. (Remember, it is only the vector sum of all the internal forces that vanishes, not the internal force on a single particle.) Thus, such a particle's momentum will not be constant-but the momentum of the entire extended object will be, in accord with Equation 9.36.

Equation 9.36 implies another important result: Since $M$ represents the mass of the entire system of particles, it is necessarily constant. (If it isn't, we don't have a closed system, so we can't expect the system's momentum to be conserved.) As a result, Equation 9.36 implies that, for a closed system,

$$
\overrightarrow{\mathbf{v}}_{\mathrm{CM}, \mathrm{f}}=\overrightarrow{\mathbf{v}}_{\mathrm{CM}, \mathrm{i}}
$$

That is to say, in the absence of an external force, the velocity of the center of mass never changes.

You might be tempted to shrug and say, "Well yes, that's just Newton's first law," but remember that Newton's first law discusses the constant velocity of a particle, whereas Equation 9.37 applies to the center of mass of a (possibly vast) collection of interacting particles, and that there may not be any particle at the center of mass at all! So, this really is a remarkable result.

## EXAMPLE 9.19

## Fireworks Display

When a fireworks rocket explodes, thousands of glowing fragments fly outward in all directions, and fall to Earth in an elegant and beautiful display (Figure 9.31). Describe what happens, in terms of conservation of momentum and center of mass.

The picture shows radial symmetry about the central points of the explosions; this suggests the idea of center of mass. We can also see the parabolic motion of the glowing particles; this brings to mind projectile motion ideas.

## Solution

Initially, the fireworks rocket is launched and flies more or less straight upward; this is the cause of the moreor-less-straight, white trail going high into the sky below the explosion in the upper-right of the picture (the yellow explosion). This trail is not parabolic because the explosive shell, during its launch phase, is actually a rocket; the impulse applied to it by the ejection of the burning fuel applies a force on the shell during the risetime interval. (This is a phenomenon we will study in the next section.) The shell has multiple forces on it; thus, it is not in free-fall prior to the explosion.

At the instant of the explosion, the thousands of glowing fragments fly outward in a radially symmetrical pattern. The symmetry of the explosion is the result of all the internal forces summing to zero $\left(\sum_{j} \overrightarrow{\mathbf{f}}_{j}^{\text {int }}=0\right)$; for every internal force, there is another that is equal in magnitude and opposite in direction.

However, as we learned above, these internal forces cannot change the momentum of the center of mass of the (now exploded) shell. Since the rocket force has now vanished, the center of mass of the shell is now a projectile (the only force on it is gravity), so its trajectory does become parabolic. The two red explosions on the left show the path of their centers of mass at a slightly longer time after explosion compared to the yellow explosion on the upper right.

In fact, if you look carefully at all three explosions, you can see that the glowing trails are not truly radially symmetric; rather, they are somewhat denser on one side than the other. Specifically, the yellow explosion and the lower middle explosion are slightly denser on their right sides, and the upper-left explosion is denser on its left side. This is because of the momentum of their centers of mass; the differing trail densities are due to the momentum each piece of the shell had at the moment of its explosion. The fragment for the explosion on the upper left of the picture had a momentum that pointed upward and to the left; the middle fragment's momentum pointed upward and slightly to the right; and the right-side explosion clearly upward and to the right (as evidenced by the white rocket exhaust trail visible below the yellow explosion).

Finally, each fragment is a projectile on its own, thus tracing out thousands of glowing parabolas.

## Significance

In the discussion above, we said, "...the center of mass of the shell is now a projectile (the only force on it is gravity)...." This is not quite accurate, for there may not be any mass at all at the center of mass; in which case, there could not be a force acting on it. This is actually just verbal shorthand for describing the fact that the gravitational forces on all the particles act so that the center of mass changes position exactly as if all the mass of the shell were always located at the position of the center of mass.

You may sometimes hear someone describe an explosion by saying something like, "the fragments of the exploded object always move in a way that makes sure that the center of mass continues to move on its original trajectory." This makes it sound as if the process is somewhat magical: how can it be that, in every explosion, it always works out that the fragments move in just the right way so that the center of mass' motion is unchanged? Phrased this way, it would be hard to believe no explosion ever does anything differently.

The explanation of this apparently astonishing coincidence is: We defined the center of mass precisely so this is exactly what we would get. Recall that first we defined the momentum of the system:

$$
\overrightarrow{\mathbf{p}}_{\mathrm{CM}}=\sum_{j=1}^{N} \frac{d \overrightarrow{\mathbf{p}}_{j}}{d t}
$$

We then concluded that the net external force on the system (if any) changed this momentum:

$$
\overrightarrow{\mathbf{F}}=\frac{d \overrightarrow{\mathbf{p}}_{\mathrm{CM}}}{d t}
$$

and then-and here's the point-we defined an acceleration that would obey Newton's second law. That is, we demanded that we should be able to write

$$
\overrightarrow{\mathbf{a}}=\frac{\overrightarrow{\mathbf{F}}}{M}
$$

which requires that

$$
\overrightarrow{\mathbf{a}}=\frac{d^{2}}{d t^{2}}\left(\frac{1}{M} \sum_{j=1}^{N} m_{j} \overrightarrow{\mathbf{r}}_{j}\right)
$$

where the quantity inside the parentheses is the center of mass of our system. So, it's not astonishing that the center of mass obeys Newton's second law; we defined it so that it would.

### 9.7 Rocket Propulsion

Now we deal with the case where the mass of an object is changing. We analyze the motion of a rocket, which changes its velocity (and hence its momentum) by ejecting burned fuel gases, thus causing it to accelerate in the opposite direction of the velocity of the ejected fuel (see Figure 9.32). Specifically: A fully fueled rocket ship in deep space has a total mass $m_{0}$ (this mass includes the initial mass of the fuel). At some moment in time, the rocket has a velocity $\overrightarrow{\mathbf{v}}$ and mass $m$; this mass is a combination of the mass of the empty rocket and the mass of the remaining unburned fuel it contains. (We refer to $m$ as the "instantaneous mass" and $\overrightarrow{\mathbf{v}}$ as the "instantaneous velocity.") The rocket accelerates by burning the fuel it carries and ejecting the burned exhaust gases. If the burn rate of the fuel is constant, and the velocity at which the exhaust is ejected is also constant, what is the change of velocity of the rocket as a result of burning all of its fuel?

## Physical Analysis

Here's a description of what happens, so that you get a feel for the physics involved.

- As the rocket engines operate, they are continuously ejecting burned fuel gases, which have both mass and velocity, and therefore some momentum. By conservation of momentum, the rocket's momentum changes by this same amount (with the opposite sign). We will assume the burned fuel is being ejected at a constant rate, which means the rate of change of the rocket's momentum is also constant. By Equation 9.9, this represents a constant force on the rocket.
- However, as time goes on, the mass of the rocket (which includes the mass of the remaining fuel) continuously decreases. Thus, even though the force on the rocket is constant, the resulting acceleration is not; it is continuously increasing.
- So, the total change of the rocket's velocity will depend on the amount of mass of fuel that is burned, and that dependence is not linear.

The problem has the mass and velocity of the rocket changing; also, the total mass of ejected gases is changing. If we define our system to be the rocket + fuel, then this is a closed system (since the rocket is in deep space, there are no external forces acting on this system); as a result, momentum is conserved for this system. Thus, we can apply conservation of momentum to answer the question (Figure 9.33).

At the same moment that the total instantaneous rocket mass is $m$ (i.e., $m$ is the mass of the rocket body plus the mass of the fuel at that point in time), we define the rocket's instantaneous velocity to be $\overrightarrow{\mathbf{v}}=v \hat{\mathbf{i}}$ (in the $+x$-direction); this velocity is measured relative to an inertial reference system (the Earth, for example). Thus, the initial momentum of the system is

$\overrightarrow{\mathbf{p}}_{\mathrm{i}}=m v \hat{\mathbf{i}}$.

The rocket's engines are burning fuel at a constant rate and ejecting the exhaust gases in the $-x$-direction. During an infinitesimal time interval $d t$, the engines eject a (positive) infinitesimal mass of gas $d m_{g}$ at velocity $\overrightarrow{\mathbf{u}}=-u \hat{\mathbf{i}}$; note that although the rocket velocity $v \hat{\mathbf{i}}$ is measured with respect to Earth, the exhaust gas velocity is measured with respect to the (moving) rocket. Measured with respect to the Earth, therefore, the exhaust gas has velocity $(v-u) \hat{\mathbf{i}}$.

As a consequence of the ejection of the fuel gas, the rocket's mass decreases by $d m_{g}$, and its velocity increases by $d v \hat{\mathbf{i}}$. Therefore, including both the change for the rocket and the change for the exhaust gas, the final momentum of the system is

$$
\begin{aligned}
\overrightarrow{\mathbf{p}}_{\mathrm{f}} & =\overrightarrow{\mathbf{p}}_{\text {rocket }}+\overrightarrow{\mathbf{p}}_{\mathrm{gas}} \\
& =\left(m-d m_{g}\right)(v+d v) \hat{\mathbf{i}}+d m_{g}(v-u) \hat{\mathbf{i}}
\end{aligned}
$$

Since all vectors are in the $x$-direction, we drop the vector notation. Applying conservation of momentum, we obtain

$$
\begin{aligned}
& p_{\mathrm{i}}=p_{\mathrm{f}} \\
& m v=\left(m-d m_{g}\right)(v+d v)+d m_{g}(v-u) \\
& m v=m v+m d v-d m_{g} v-d m_{g} d v+d m_{g} v-d m_{g} u \\
& m d v=d m_{g} d v+d m_{g} u
\end{aligned}
$$

Now, $d m_{g}$ and $d v$ are each very small; thus, their product $d m_{g} d v$ is very, very small, much smaller than the other two terms in this expression. We neglect this term, therefore, and obtain:

$$
m d v=d m_{g} u
$$

Our next step is to remember that, since $d m_{g}$ represents an increase in the mass of ejected gases, it must also represent a decrease of mass of the rocket:

$$
d m_{g}=-d m
$$

Replacing this, we have

$$
m d v=-d m u
$$

or

$$
d v=-u \frac{d m}{m}
$$

Integrating from the initial mass $m_{0}$ to the final mass $m$ of the rocket gives us the result we are after:

$$
\begin{aligned}
\int_{v_{\mathrm{i}}}^{v} d v & =-u \int_{m_{0}}^{m} \frac{1}{m} d m \\
v-v_{\mathrm{i}} & =u \ln \left(\frac{m_{0}}{m}\right)
\end{aligned}
$$

and thus our final answer is

$$
\Delta v=u \ln \left(\frac{m_{0}}{m}\right)
$$

This result is called the rocket equation. It was originally derived by the Soviet physicist Konstantin Tsiolkovsky in 1897. It gives us the change of velocity that the rocket obtains from burning a mass of fuel that decreases the total rocket mass from $m_{0}$ down to $m$. As expected, the relationship between $\Delta v$ and the change of mass of the rocket is nonlinear.

## PROBLEM-SOLVING STRATEGY

## Rocket Propulsion

In rocket problems, the most common questions are finding the change of velocity due to burning some amount of fuel for some amount of time; or to determine the acceleration that results from burning fuel.

1. To determine the change of velocity, use the rocket equation Equation 9.38 .
2. To determine the acceleration, determine the force by using the impulse-momentum theorem, using the rocket equation to determine the change of velocity.

## EXAMPLE 9.20

## Thrust on a Spacecraft

A spacecraft is moving in gravity-free space along a straight path when its pilot decides to accelerate forward. He turns on the thrusters, and burned fuel is ejected at a constant rate of $2.0 \times 10^{2} \mathrm{~kg} / \mathrm{s}$, at a speed (relative to the rocket) of $2.5 \times 10^{2} \mathrm{~m} / \mathrm{s}$. The initial mass of the spacecraft and its unburned fuel is $2.0 \times 10^{4} \mathrm{~kg}$, and the thrusters are on for $30 \mathrm{~s}$.

a. What is the thrust (the force applied to the rocket by the ejected fuel) on the spacecraft?

b. What is the spacecraft's acceleration as a function of time?

c. What are the spacecraft's accelerations at $t=0,15,30$, and $35 \mathrm{~s}$ ?

## Strategy

a. The force on the spacecraft is equal to the rate of change of the momentum of the fuel.

b. Knowing the force from part (a), we can use Newton's second law to calculate the consequent acceleration. The key here is that, although the force applied to the spacecraft is constant (the fuel is being ejected at a constant rate), the mass of the spacecraft isn't; thus, the acceleration caused by the force won't be constant. We expect to get a function $a(t)$, therefore.

c. We'll use the function we obtain in part (b), and just substitute the numbers given. Important: We expect that the acceleration will get larger as time goes on, since the mass being accelerated is continuously decreasing (fuel is being ejected from the rocket).

## Solution

a. The momentum of the ejected fuel gas is

$$
p=m_{g} v
$$

The ejection velocity $v=2.5 \times 10^{2} \mathrm{~m} / \mathrm{s}$ is constant, and therefore the force is

$$
F=\frac{d p}{d t}=v \frac{d m_{g}}{d t}=-v \frac{d m}{d t}
$$

Now, $\frac{d m_{g}}{d t}$ is the rate of change of the mass of the fuel; the problem states that this is $2.0 \times 10^{2} \mathrm{~kg} / \mathrm{s}$. Substituting, we get

$$
\begin{aligned}
F & =v \frac{d m g}{d t} \\
& =\left(2.5 \times 10^{2} \frac{\mathrm{m}}{\mathrm{s}}\right)\left(2.0 \times 10^{2} \frac{\mathrm{kg}}{\mathrm{s}}\right) \\
& =5 \times 10^{4} \mathrm{~N}
\end{aligned}
$$

b. Above, we defined $m$ to be the combined mass of the empty rocket plus however much unburned fuel it contained: $m=m_{R}+m_{g}$. From Newton's second law,

$$
a=\frac{F}{m}=\frac{F}{m_{R}+m_{g}}
$$

The force is constant and the empty rocket mass $m_{R}$ is constant, but the fuel mass $m_{g}$ is decreasing at a uniform rate; specifically:

$$
m_{g}=m_{g}(t)=m_{g_{0}}-\left(\frac{d m_{g}}{d t}\right) t
$$

This gives us

$$
a(t)=\frac{F}{m_{g_{i}}-\left(\frac{d m_{g}}{d t}\right) t}=\frac{F}{M-\left(\frac{d m_{g}}{d t}\right) t}
$$

Notice that, as expected, the acceleration is a function of time. Substituting the given numbers:

$$
a(t)=\frac{5 \times 10^{4} \mathrm{~N}}{2.0 \times 10^{4} \mathrm{~kg}-\left(2.0 \times 10^{2} \frac{\mathrm{kg}}{\mathrm{s}}\right) t}
$$

c. At $t=0 \mathrm{~s}:$

$$
a(0 \mathrm{~s})=\frac{5 \times 10^{4} \mathrm{~N}}{2.0 \times 10^{4} \mathrm{~kg}-\left(2.0 \times 10^{2} \frac{\mathrm{kg}}{\mathrm{s}}\right)(0 \mathrm{~s})}=2.5 \frac{\mathrm{m}}{\mathrm{s}^{2}}
$$

At $t=15 \mathrm{~s}, a(15 \mathrm{~s})=2.9 \mathrm{~m} / \mathrm{s}^{2}$.

At $t=30 \mathrm{~s}, a(30 \mathrm{~s})=3.6 \mathrm{~m} / \mathrm{s}^{2}$.

Acceleration is increasing, as we expected.

## Significance

Notice that the acceleration is not constant; as a result, any dynamical quantities must be calculated either using integrals, or (more easily) conservation of total energy.

## Rocket in a Gravitational Field

Let's now analyze the velocity change of the rocket during the launch phase, from the surface of Earth. To keep the math manageable, we'll restrict our attention to distances for which the acceleration caused by gravity can be treated as a constant $g$.

The analysis is similar, except that now there is an external force of $\overrightarrow{\mathbf{F}}=-m g \hat{\mathbf{j}}$ acting on our system. This force applies an impulse $d \overrightarrow{\mathbf{J}}=\overrightarrow{\mathbf{F}} d t=-m g d t \hat{\mathbf{j}}$, which is equal to the change of momentum. This gives us

$$
\begin{aligned}
d \overrightarrow{\mathbf{p}} & =d \overrightarrow{\mathbf{J}} \\
\overrightarrow{\mathbf{p}}_{\mathrm{f}}-\overrightarrow{\mathbf{p}}_{\mathbf{i}} & =-m g d t \hat{\mathbf{j}} \\
{\left[\left(m-d m_{g}\right)(v+d v)+d m_{g}(v-u)-m v\right] \hat{\mathbf{j}} } & =-m g d t \hat{\mathbf{j}}
\end{aligned}
$$

and so

$$
m d v-d m_{g} u=-m g d t
$$

where we have again neglected the term $d m_{g} d v$ and dropped the vector notation. Next we replace $d m_{g}$ with $-d m:$

$$
\begin{aligned}
m d v+d m u & =-m g d t \\
m d v & =-d m u-m g d t
\end{aligned}
$$

Dividing through by $m$ gives

$$
d v=-u \frac{d m}{m}-g d t
$$

and integrating, we have

$$
\Delta v=u \ln \left(\frac{m_{0}}{m}\right)-g \Delta t .
$$

Unsurprisingly, the rocket's velocity is affected by the (constant) acceleration of gravity.

Remember that $\Delta t$ is the burn time of the fuel. Now, in the absence of gravity, Equation 9.38 implies that it makes no difference how much time it takes to burn the entire mass of fuel; the change of velocity does not
depend on $\Delta t$. However, in the presence of gravity, it matters a lot. The $-g \Delta t$ term in Equation 9.39 tells us that the longer the burn time is, the smaller the rocket's change of velocity will be. This is the reason that the launch of a rocket is so spectacular at the first moment of liftoff: It's essential to burn the fuel as quickly as possible, to get as large a $\Delta v$ as possible.

