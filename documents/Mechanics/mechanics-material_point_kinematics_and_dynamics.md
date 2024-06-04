# Material point kinematics and dynamics 

### 2.1 Material point kinematics

Mechanics is divided into two parts : kinematics and dynamics. Kinematics studies the motion of bodies without investigating the nature of the forces that give rise to this motion. On the other hand, dynamics seeks to identify the causes of this motion. The study of the motion of a material point requires a physical object of reference called the frame of reference. To describe mathematically the motion of the material point, it has to be expressed with respect to a geometric frame. Kinematics consists in describing the position, the velocity and the acceleration of a body. These quantities are vectors.

### 2.1.1 Material point

To begin this mechanics course, we shall use a very simple model. We shall assume that the physical object that we wish to describe can be represented simply by a material point which carries the mass, i.e. the amount of matter of this object. This point is a physical point called material point. This model of the material point is an idealisation of the physical reality. This model is never perfectly exact because the physical reality is always too complex. However, in certain circumstances, we can consider for instance that a pool ball, a pendulum, a man or even a plane are material points. These objects are of course different, but depending on the nature of their motion, they can be considered all as material points. The material point model is very simple, but it is a very good qualitative and quantitative approximation in numerous cases. In general, we choose as a material point the centre of mass - also called barycentre - of an object.

The material point model is very limited. It does not account for the rotation of a solid on itself. The difference between the material point and the rigid body is well illustrated by the example of a pool ball. Hitting a pool ball in different ways with a pool queue yields different effects. The white ball can stop after the collision, it can go forward or backwards. It can also follow a curved trajectory. This is impossible for a material point.

If a pendulum consists of a mass suspended at the extremity of a massless rod, the material point model will be a good model. We call such a pendulum, a simple pendulum or a mathematical pendulum. However, if the swing is a metallic rod with a thickness that is sufficiently large compared to its length, then it will have to be considered as a solid. If a man dives vertically from a 10 meter high diving board, the description of his free fall can be described accurately by the material point model. However if now he performs a triple somersault, his dynamics has to be described with the rigid body model. If you are an athlete you can try to experiment the difference between these two models at a swimming pool. A plane with a linear motion can be modelled as a material point. But when it turns, it rotates around its barycentre and then it has to be considered as solid. To treat all the mechanical problems that describe a rotational motion around the barycentre, we shall use rigid body dynamics.

Considering a solid as a material point leads to two types of errors : quantitative errors and qualitative errors. Treating a metallic rod as a material point leads to a quantitative error on the value of its oscillation period. Treating a pool ball as a material point leads to a qualitative error by not accounting for the rotational motion.

### 2.1.2 Frame of reference

The description of the motion of an object has to be made with respect to an object of reference. This object, that can be huge, is called the frame of reference. Formally, a frame of reference is a set of $N$ material points, where $N \geq 4$, that are non-coplanar and at constant distance with respect to each other.

To describe the physical experiments shown in this course, we choose the auditorium as frame of reference, i.e. the earth. If for instance, we choose to measure the relative speed of the waves with respect to a sailboat, we shall choose the sailboat as a frame of reference. To describe the motion of the earth around the sun, we shall choose the solar system consisting of the sun and three fixed stars as a frame of reference.

A physical object has to be rigid to serve as a frame of reference. A rigid body consists of non-coplanar material points at rest with respect to each other. To be a frame of reference, an object has to consist at least of four coplanar material points at constant distance with respect to each other. There can obviously be a large number of them but there have to be at least four. Why do the points have to be at constant distance with respect to each other? Because if it were not the case, there would be no invariant to define and measure distances. Why should a frame of reference be defined by at least four non-coplanar points? Because distances have to be defined and measured in three non-colinear spatial directions.

The choice of the frame of reference is very important. If we choose a non-inertial frame, we will have to take into account the inertial forces in the description of the motion. For instance, when a boat make a quick turn, a centrifugal force acts on the occupants in the frame of reference of the boat. We could mention as another example the Coriolis force acting on the motion of the clouds in the non-inertial frame of the earth that rotates on itself.

The choice of frame of reference has played a crucial role in the history of mechanics and of physics. Relativity is a matter of frame of reference! Special relativity requires the laws of physics to be the same with respect to all the inertial frame of reference. General relativity generalises special relativity to all the frames of reference, even non-inertial frames of reference.

### 2.1.3 Geometric frame

To describe mathematically the motion of a material point with respect to a frame of reference, we have to use a geometric frame also simply called a frame. A frame is a geometric concept. It is a vector basis consisting of three non coplanar vectors of constant norm attached to a spatial point. Since these vectors are non coplanar, they span a three dimensional space. Since they have a constant norm, they can be used to measure and quantify motion.

An orthonormal frame is a frame consisting of orthogonal basis vectors of unit norm. In material point mechanics and rigid body mechanics, we consider only orthonormal frames. However, if we were to describe deformable bodies or to study general relativity, we would have to consider also non orthonormal frames. The most famous example of direct frame is the Cartesian frame. However, there are also other frames like the cylindrical frame or the spherical frame that we shall define later and use extensively in this course.

Note that the geometric frame (or frame) should not be confused with the physical notion of frame of reference. The geometric frame is a geometric entity described in terms of spatial points and vectors. The geometric frame is used to measure distances with respect to the frame of reference and thus quantify motion.

### 2.1.4 Position vector

The position vector $\boldsymbol{O P}$ indicates the position of the material point $P$ with respect to the origin $O$ of a Cartesian frame (Fig. 2.1).

We shall denote the position vector $\boldsymbol{O P}$ of the material point $P$ in a more concise way as $\boldsymbol{r}(t)$ because the position of a material point is a function of time $t$. Indeed, when the
material point moves its position changes with time. In the Cartesian frame $\left(O, \boldsymbol{e}_{x}, \boldsymbol{e}_{y}, \boldsymbol{e}_{z}\right)$ that defines a system of axes $(x, y, z)$ intersecting at the origin $O$, the coordinates of the position vector are $(x(t), y(t), z(t))$.

Generally in physics and particularly in mechanics, when a quantity is introduced, its unit has to be specified. It is the main difference between physics and mathematics. In physics, we are interested with the real and tangible world. The physical unit of position in the international system of units (SI) is the metre denoted $[\mathrm{m}]$. The physical unit of time is the second denoted $[\mathrm{s}]$.

### 2.1.5 Trajectory

After having defined the position vector of a material point, we can now define the notion of trajectory. The trajectory of a material point is the set of spatial points where the material point is located over time. In mathematics, it is called the locus. For instance, the trajectory of a airliner is easy to observe on a blue sky.

Let us mention several example of particular trajectories of material points. The trajectory of a linear motion is a straight line. The trajectory of a circular motion is a circle. The

Trajectory ballistic trajectory of a projectile - a cannonball for instance - in the absence of friction is a parabola. The trajectory of the earth around the sun is an ellipse, this is what the law of orbits states. The trajectory of a comet crossing the solar system is a hyperbola.

### 2.1.6 Velocity vector

The velocity $\boldsymbol{v}(t)$ is a vector. It is a quantity with a well defined norm and an orientation like the position vector $\boldsymbol{r}(t)$. The velocity corresponds intuitively to the displacement over time. The velocity vector of a material point is expressed as the ratio of the displacement vector $\Delta \boldsymbol{r}(t)$ and of the time interval $\Delta t$. In order to obtain the instantaneous velocity at time $t$, we need to take the limit where the time interval $\Delta t$ tends towards 0 . The displacement vector $\Delta \boldsymbol{r}(t)$ is expressed as the vectorial difference between the position vectors $\boldsymbol{r}(t+\Delta t)$ and $\boldsymbol{r}(t)$ (Fig. 2.2).

The mathematical expression of the velocity vector is thus defined as the time derivative of the position vector,

$$
\begin{equation*}
\boldsymbol{v}(t)=\lim _{\Delta t \rightarrow 0} \frac{\Delta \boldsymbol{r}(t)}{\Delta t}=\lim _{\Delta t \rightarrow 0} \frac{\boldsymbol{r}(t+\Delta t)-\boldsymbol{r}(t)}{\Delta t}=\frac{d \boldsymbol{r}}{d t}=\dot{\boldsymbol{r}} \tag{2.1}
\end{equation*}
$$

Using the notation of the physicists, we denote this derivative as the ratio of the infinitesimal displacement $d \boldsymbol{r}$ and the infinitesimal time interval $d t$. The velocity vector is tangent to the

Speed measure trajectory of the material point represented in bold (Fig. 2.2). The physical unit of the velocity in the international system of units is denoted $[\mathrm{m} / \mathrm{s}]$.

As an example, let us mention the measure of the speed, or scalar velocity, of a gun bullet using two photoelectric cells that are one meter apart. The inverse of the time spent between the cells corresponds to the speed expressed in $[\mathrm{m} / \mathrm{s}]$.

### 2.1.7 Acceleration vector

The acceleration $\boldsymbol{a}(t)$ is a vector. It is a quantity with a well defined norm and orientation like the position vector $\boldsymbol{r}(t)$ and the velocity vector $\boldsymbol{v}(t)$. The acceleration corresponds intuitively to the variation of the velocity vector over time. The acceleration is expressed as the ratio of the variation of the velocity vector $\Delta \boldsymbol{v}(t)$ and of the time interval $\Delta t$. In order to obtain the instantaneous acceleration at time $t$, we need to take the limit where the time interval $\Delta t$ tends towards 0 . The velocity variation vector $\Delta \boldsymbol{r}(t)$ is expressed as the vectorial difference between the velocity vectors $\boldsymbol{v}(t+\Delta t)$ and $\boldsymbol{v}(t)$ (Fig. 2.3).

The mathematical expression of the acceleration vector is thus defined as the time derivative of the velocity vector,

$$
\begin{equation*}
\boldsymbol{a}(t)=\lim _{\Delta t \rightarrow 0} \frac{\Delta \boldsymbol{v}(t)}{\Delta t}=\lim _{\Delta t \rightarrow 0} \frac{\boldsymbol{v}(t+\Delta t)-\boldsymbol{v}(t)}{\Delta t}=\frac{d \boldsymbol{v}}{d t}=\dot{\boldsymbol{v}} \tag{2.2}
\end{equation*}
$$

Using the notation of the physicists, we denote this derivative as the ratio of the infinite-
simal velocity variation $d \boldsymbol{v}$ and the infinitesimal time interval $d t$. The physical unit of the acceleration in the international system of units is denoted $\left[\mathrm{m} / \mathrm{s}^{2}\right]$.

### 2.2 Linear motion

In this section, we shall consider two different linear motions. The uniform linear motion of a material point characterised by a constant speed, and the uniformly accelerated linear motion characterised by a constant acceleration. There are of course many linear motions characterised by a varying acceleration. However, here we shall consider only cases where the acceleration is constant or vanishes.

### 2.2.1 Uniform linear motion

A material point moving with constant speed along a straight line has a uniform linear motion. Its trajectory is thus a straight line. To characterise this motion, we choose an axis $x$ along the straight line. The position is thus determined by the coordinate $x(t)$. We seek to determine the position equation that yields the position over time. For a uniform linear motion, the speed $v$ along the axis $x$ is constant (Fig. 2.4). Thus, the velocity equation is written

$$
\begin{equation*}
v=\dot{x}=\frac{d x}{d t}=\text { const } \quad \text { and } \quad d x=v d t \tag{2.3}
\end{equation*}
$$

The indefinite integral of this equation over time $t$ is written,

$$
\begin{equation*}
x(t)=\int d x=v \int d t=v t+c_{0} \tag{2.4}
\end{equation*}
$$

where $c_{0}$ is an integration constant. To determine the constant $c_{0}$, the initial condition on the position coordinate has to be taken into account,

$$
\begin{equation*}
x(0)=x_{0} \tag{2.5}
\end{equation*}
$$

which implies that,

$$
\begin{equation*}
c_{0}=x_{0} \tag{2.6}
\end{equation*}
$$

Substituting expression (2.6) into the position equation (2.4) yields,

$$
\begin{equation*}
x(t)=v t+x_{0} \tag{2.7}
\end{equation*}
$$

The velocity equation (2.3) is a first-order time differential equation. Only one initial condition on the position (2.5) has to be specified in order to determine the position equation (2.7).

Let us mention the motion of a free glider on an horizontal air cushion bench, the motion of a curling stone on an ice skating rink or the motion of a gun bullet when the action of the gravitational force can be neglected.

### 2.2.2 Uniformly accelerated linear motion

A material point that moves along a straight line with constant acceleration has a uniformly accelerated linear motion. Its trajectory is a straight line. To characterise this motion, we choose an axis $x$ along the line. The position is thus determined by the coordinate $x(t)$. We seek to determine the position equation that yields the position over time.

For a uniformly accelerated linear motion, the acceleration $a$ along the axis $x$ is constant (Fig. 2.5). Thus, the motion equation is written,

$$
\begin{equation*}
a=\ddot{x}=\frac{d^{2} x}{d t^{2}}=\frac{d v}{d t}=\text { const } \quad \text { and } \quad d v=a d t \tag{2.8}
\end{equation*}
$$

The indefinite integral of this equation over time $t$ is written,

$$
\begin{equation*}
v(t)=\int d v=a \int d t=a t+c_{1} \tag{2.9}
\end{equation*}
$$

where $c_{1}$ is an integration constant. To determine the constant $c_{1}$, the initial condition on the velocity coordinate has to be taken into account,

$$
\begin{equation*}
v(0)=v_{0} \tag{2.10}
\end{equation*}
$$

which implies that,

$$
\begin{equation*}
c_{1}=v_{0} \tag{2.11}
\end{equation*}
$$

Substituting expression (2.11) into the velocity equation (2.9) yields,

$$
\begin{equation*}
v(t)=a t+v_{0} \tag{2.12}
\end{equation*}
$$

The speed is expressed as the derivative of the position,

$$
\begin{equation*}
v(t)=\frac{d x}{d t} \tag{2.13}
\end{equation*}
$$

Identifying the right-hand side of equations (2.12) and (2.13) yields,

$$
\begin{equation*}
\frac{d x}{d t}=a t+v_{0} \quad \text { thus } \quad d x=a t d t+v_{0} d t \tag{2.14}
\end{equation*}
$$

The indefinite time integral of equation (2.14) is written,

$$
\begin{equation*}
x(t)=\int d x=a \int t d t+v_{0} \int d t=\frac{1}{2} a t^{2}+v_{0} t+c_{2} \tag{2.15}
\end{equation*}
$$

To determine the constant $c_{2}$, the initial condition on the position coordinate has to be taken into account,

$$
\begin{equation*}
x(0)=x_{0} \tag{2.16}
\end{equation*}
$$

which implies that,

$$
\begin{equation*}
c_{2}=x_{0} \tag{2.17}
\end{equation*}
$$

Substituting expression (2.17) into the position equation (2.15) yields,

$$
\begin{equation*}
x(t)=\frac{1}{2} a t^{2}+v_{0} t+x_{0} \tag{2.18}
\end{equation*}
$$

The equation of motion (2.8) is a second-order time differential equation. Two initial conditions, one on the velocity (2.10) and another on the position (2.16) have to be specified in order to determine the position equation (2.18).

As an example, let us mentions the motion of a glider driven by a mass on a horizontal air cushion bench and the free fall of an apple subjected to the constant acceleration of the gravitational field.

### 2.3 Newton's laws

Until now, we defined kinematical quantities. Now we shall define dynamical quantities in order to be able to state the laws of dynamics generally called Newton's laws. There are three laws of Newton. We shall examine the first two in this section. The third shall be discussed later. The aim of this section is to be able to determine the motion of objects subjected to external forces.

### 2.3.1 Extensive and intensive quantities

Before introducing the characteristic quantities of dynamics, we shall first define the properties known as extensivity and intensivity.

A physical quantity is extensive if, for a set of objects, the quantity of the set is equal to the sum of this quantity for each object. This definition may seem a little abstract. Thus, we shall consider a few examples. The amount of matter is an extensive quantity. The amount of matter of two identical objects is equal to twice the amount of matter of an object. The momentum and the force are also extensive quantities. The net force applied on a system is equal to the sum of the forces. The volume is of course another example of an extensive quantity. The volume of two objects is equal to the sum of the volumes of the objects.

A physical quantity is intensive if, for a set of objects, the quantity is independent of the number of objects. The speed is a good example of intensive quantity. Let us consider a car that moves with a velocity $\boldsymbol{v}$. The car has four wheels that move with a velocity $\boldsymbol{v}$. The velocity of the car is not the sum of the velocities of each wheel, because the velocity is an intensive quantity. We shall see that the velocity is the ratio of two extensive quantities. Using the same line of thought, we show that the acceleration is also an extensive quantity. Finally, if two blocks that have the same temperature come into contact, the temperature of the system will be the temperature of each block and not the sum of their temperatures. The temperature is also an intensive quantity.

### 2.3.2 Mass

The mass $m$ of an object considered as a material point represents an amount of matter. Thus, it is an extensive quantity that is definite positive. If we take two objects, the total mass is the sum of the masses of the two objects. The mass is an additive quantity. Since the mass is an amount of matter, it has no orientation. It is thus a scalar quantity. The mass is a conserved quantity. In Newtonian mechanics, matter can neither be created nor destroyed. This is no more the case in relativity, since mass can be transformed into another type of energy $E$ as the famous formula of Albert Einstein shows : $E=m c^{2}$ where $c$ represents the propagation speed of light in vacuum.

In Newtonian mechanics, mass is globally conserved, but it can enter or leave the system. If the mass of a system changes, it means that mass entered or left the system. If there is no exchange of mass with the exterior, the system is said to be closed. When there is exchange of mass, it is said to be open. A gold bar of a given mass is a closed system, its mass is constant. A rocket taking off is an open system, its mass decreases over time since the rocket rejects gas into the atmosphere through combustion.

The unit of mass in the international system of units is the kilogram denoted $[\mathrm{kg}]$. The mass standard defining the kilogram is a bar of platinum-iridium that is located in the "Bureau International des Poids et Mesures" in Sevres near Paris.

Two masses are identical if they cause the same deformation when suspended at identical springs.

### 2.3.3 Momentum

The momentum $\boldsymbol{p}$ is a physical quantity that has been introduced by Isaac Newton. The brilliant idea of Newton was to introduce this physical quantity to describe motion. Since momentum is an extensive quantity, it allows specifically the descripton of the motion of
amount of matter. The momentum of two objects is the sum of the momentum of each object, in contrast to the velocity. This quantity has to be a vectorial quantity because motion has a precise orientation. For the time being, we are not yet able to define the physical unit of momentum. The motivation of our approach will become clearer after stating Newton's $1^{\text {st }}$ and $2^{\text {nd }}$ laws. The concept of momentum is absolutely central in physics and not only in mechanics. This concept applies also in special relativity and in quantum mechanics. Thus, it is a universal concept that Isaac Newton has defined!

### 2.3.4 Newton's $1^{\text {st }}$ law

Newton's $1^{\text {st }}$ law has actually not been discovered by Newton but by Galileo. This is a historical error. It is Galileo's law of inertia. I have lots of admiration for Newton, but I believe that we have to give to Galileo what belongs to Galileo. The Newton's $\mathbf{1}^{\text {st }} \boldsymbol{l a w}$ or Galileo's law of inertia is stated by Newton in his Principia Mathematica in the following way :

Every body perseveres in its state of rest, or of uniform motion in a right line, unless in so far as it is compelled to change that state by forces impressed thereon.

In more modern words, we would simply say :

A body has a uniform linear motion in the absence of a net external force. If its speed vanishes, then it is at rest.

Galileo found this law based on his own observations. This law was not at all obvious in Galileo's day. According to Aristotle, the motion of an object in the air is its natural motion. It is carried by the air. The observations of Galileo are radically opposed. The motion of an object in the air is not its natural motion. It is damped by the air. Its natural motion in the absence of a net external interaction is a uniform linear motion. This law of inertia is really a conceptual feat. The concept of force has been properly introduced by Newton. Galileo speaks only of the effect of the external world. Thus, this is why we mention the law of inertia by referring to Newton's $1^{\text {st }}$ law, because it is he who completed the statement of the law of inertia by attributing the cause of the acceleration of the motion to a force.

Why is this law called the law of inertia? What is the inertia? The inertia of an object is the resistance of this object to be set into motion. Inertia is what is opposed to an acceleration. The law of inertia defines under what condition an object has a uniform linear motion, i.e. a motion in absence of acceleration. The very general concept of inertia should not be confused with the specific notions of moment of inertia or of tensor of inertia of a solid. These two notions are a particular case of inertia for a rotating solid. We shall discuss this in more detail when we shall examine rigid body dynamics.

In the previous section, we defined the position, velocity and acceleration vectors. The question that arises here is to know with respect to which frame of reference can these notions be defined? Can we choose any frame of reference? The answer is no. These kinematical quantities depend on the chosen frame of reference. The law of inertia allows us to choose the frames of reference with respect to which the laws of dynamics can be defined. These frames of reference are inertial frames of reference. By definition, an inertial frame of reference is a frame of reference with respect to which the law of inertia is verified. Thus, in an inertial frame of reference, an object that is not subjected to a force is either at rest or in uniform linear motion.

We see straight away that by definition an inertial frame of reference is not unique. If we choose two frame of reference that move at constant speed with respect to the other, an object that has a uniform linear motion in one frame of reference will also have a uniform linear motion in the other. These two frames of reference are two inertial frame of reference. There are an infinity of inertial frames.

The concept of inertial frame of reference is not an absolute concept. It depends on the system to be described. If we would like to describe the dynamics of a small pendulum, about $10 \mathrm{~cm}$ in length, in a laboratory on a small time scale, during about one minute, we can consider that the earth is a good frame of reference. However, if we consider a large pendulum, about $67 \mathrm{~m}$ in length like the Foucault pendulum attached to the top of the dome of the Pantheon in Paris, and we would like to describe its dynamics, we will have to take into account the intrinsic rotational motion of the earth. The oscillation plane of the pendulum will shift over time. To describe the dynamics of such a pendulum, we will have to choose as a frame of inertia the solar system. If a train moves at constant speed, and that we would like to model the motion of a pendulum attached to the ceiling, we can choose as inertial frame of reference the train or the earth. In general, it will be easier to choose the train as frame of reference. In the case where the train accelerates, the dynamics of the pendulum changes and the train is no more an inertial frame of reference.

### 2.3.5 Force

The concept of force is very ancient. Archimedes introduced this concept to explain the buoyancy of an object. Simon Stevin used the static notion of force to describe equilibrium states in the $16^{\text {th }}$ century. However, it is Newton who gave to the notion of force a dynamical status. The force $\boldsymbol{F}$ is a physical quantity that modifies the state of rest or of uniform motion of an object. It is an extensive quantity that enables the description of the cause of the variation of the state of uniform motion of an object. It is a quantity that has to be additive to describe the cause of the motion of an amount of matter. If two forces are exerted on an object, the net force is the sum of the applied forces. A force has to be a vectorial quantity because it is exerted on the object in a specified direction.

If a force is applied on a material point, it can be measured with a dynamometer attached to a material point by a rod. The material point is kept at rest by the elastic force exerted by the dynamometer. The direction of the rod yields the direction of the force and the value read on the dynamometer, its intensity.

For the time being, we cannot define yet the physical unit of force. In order to determine it, we have to state Newton's $2^{\text {nd }}$ law. But before that, we shall examine the vectorial composition rule of forces discovered experimentally by Stevin and established theoretically by Newton. In Stevin's experiment (Fig. 2.6), the material point $P$ is at rest. This means that the vectorial sum of the forces $\boldsymbol{F}_{A}$ and $\boldsymbol{F}_{B}$ whose norms are indicated on the dynamometers at $A$ and $B$, is equal to the force $\boldsymbol{F}_{C}$, whose norm is indicated on the dynamometer at $C$. When two forces $\boldsymbol{F}_{A}$ and $\boldsymbol{F}_{B}$ are applied on the material point $P$, the vectorial sum of these
two forces is the net force $\boldsymbol{F}_{C}$ oriented along the diagonal of the parallelogram spanned by $\boldsymbol{F}_{A}$ and $\boldsymbol{F}_{B}$. The norm of the net force $\boldsymbol{F}_{C}$ corresponds to the length of the diagonal of the parallelogram (Fig. 2.7). When the forces are described by vectors, this vectorial composition rule seems natural and almost trivial, but this was not the case in Newton's day.

### 2.3.6 Newton's $2^{\text {nd }}$ law

After having defined the notions of inertial frame of reference, of momentum and of force, we can now state the Newton's $2^{\text {nd }}$ law and express it in mathematical form. Newton's $1^{\text {st }}$ law states that it is under the action of a force that a body modifies its state of motion. The physical quantity that characterises the state of motion is the momentum. Thus, the force will modify the momentum. Newton's $\mathbf{2}^{\text {nd }} \boldsymbol{l a w}$ is stated by Newton in his Principia Mathematica in the following way :

The change of motion is proportional to the motive force impressed; and is made in the direction of the straight line in which that force is impressed.

In more modern words, we would simply say :

The variation of momentum of a body over time is due to the net external force applied on this body.

There can be several forces applied on a body, but given that the force is an extensive quantity, the net force is the vectorial sum of the forces. Now, we would like to write Newton's $2^{\text {nd }}$ law also called law of motion in mathematical form. The variation of the momentum $\boldsymbol{p}$ over time, when the time interval tends to 0 is simply the time derivative of the momentum. Since the cause of the momentum variation is the vectorial sum of the external forces $\boldsymbol{F}^{\text {ext }}$, the equation of motion is simply written as,

$$
\begin{equation*}
\sum \boldsymbol{F}^{\mathrm{ext}}=\frac{d \boldsymbol{p}}{d t} \tag{2.19}
\end{equation*}
$$

This equation is very general since it is valid not only in mechanics, but also in electrodynamics, in quantum physics and even in special relativity. In general relativity, it is replaced by a more abstract concept. This concept is the curvature of space-time.

In order to establish the law of motion (2.19), it is essential to consider that momentum is an extensive quantity. Otherwise, we could not identify its time derivative with the net external force. In a physical equation, we can identify only quantities of the same nature. We see here the soundness of Newton's approach that postulates the existence of momentum to be able to establish an explicit link between the variation of the state of motion and its cause. We will now determine the explicit expression of the momentum of a material point.

### 2.3.7 Momentum and velocity

The momentum $\boldsymbol{p}$ has to satisfy the law of motion (2.19). Thus, the momentum is defined up to a constant since the law of motion is defined in terms of the derivative of the momentum. Thus two quantities that differ by a constant lead to the same equation of motion. The momentum is thus not uniquely defined. The convention is to choose the momentum such that it vanishes when the object is at rest. This convention called a gauge choice depends on the chosen frame of reference.

Now we would like to establish the relation between the momentum $\boldsymbol{p}$ and the velocity $\boldsymbol{v}$. The momentum $\boldsymbol{p}$ describes the motion of an amount of matter of mass $m$. Thus, the
momentum $\boldsymbol{p}(m)$ has to be a function of the mass $m$. Since the momentum is an extensive quantity, the momentum $\boldsymbol{p}(\mathrm{km})$ of a system consisting of $k$ identical material points of mass $m$ and of velocity $\boldsymbol{v}$ is equal to the sum of the momenta $\boldsymbol{p}(m)$ of every material point,

$$
\begin{equation*}
\boldsymbol{p}(k m)=k \boldsymbol{p}(m) \tag{2.20}
\end{equation*}
$$

Applying the definition (1.13) of the derivative of a functional, we differentiate the extensivity relation for the momentum (2.20) wth respect to $k$ keeping $m$ fixed, which is written as,

$$
\begin{equation*}
\frac{d \boldsymbol{p}(k m)}{d(k m)} \frac{d(k m)}{d k}=\frac{d k}{d k} \boldsymbol{p}(m) \tag{2.21}
\end{equation*}
$$

and reduces to,

$$
\begin{equation*}
\frac{d \boldsymbol{p}(k m)}{d(k m)} m=\boldsymbol{p}(m) \tag{2.22}
\end{equation*}
$$

Relation (2.22) has to be satisfied for every number $k$ of material points. In particular for $k=1$, it can be expressed as,

$$
\begin{equation*}
\frac{d \boldsymbol{p}(m)}{d m}=\frac{\boldsymbol{p}(m)}{m} \tag{2.23}
\end{equation*}
$$

Relation (2.23) implies that the momentum is proportional to the mass where the proportionality factor is a vectorial function $\boldsymbol{f}(\boldsymbol{v})$ of the velocity $\boldsymbol{v}$ that is independent of the mass $m$,

$$
\begin{equation*}
\boldsymbol{p}=m \boldsymbol{f}(\boldsymbol{v}) \tag{2.24}
\end{equation*}
$$

with $\boldsymbol{f}(\mathbf{0})=\mathbf{0}$, according to our choice of definition for the momentum. The expression (2.24) of the momentum is very general and is valid in classical mechanics and even in relativistic mechanics. The explicit expression of the vectorial function $\boldsymbol{f}(\boldsymbol{v})$ has to be inferred from experiment.

In order to do so, we restrict ourselves to the framework of classical mechanics where the velocities are very low compared to the propagation velocity of light in vacuum. The experiment consists of a perfectly inelastic collision between two identical gliders of mass $m$ on an horizontal air cushion bench. The two gliders remain attached after the collision (Fig. 2.8). The first glider that has a uniform linear motion of initial velocity $\boldsymbol{v}$ hits the
second glider with a spike that sinks into the plasticine fixed on the second one. After the collision, we observe that the system consisting of the two gliders has a uniform linear motion of velocity $\boldsymbol{v} / 2$. Since the net external force exerted on the system consisting of the two gliders vanishes, Newton's $2^{\text {nd }}$ law states that the total momentum is conserved during the collision. The initial momentum of the second glider vanishes. Thus, the initial momentum of the first glider has to be equal to the final momentum of the two gliders,

$$
\begin{equation*}
m \boldsymbol{f}(\boldsymbol{v})=2 m \boldsymbol{f}\left(\frac{\boldsymbol{v}}{2}\right) \tag{2.25}
\end{equation*}
$$

The derivative of relation (2.25) with respect to the velocity divided by the mass $m$ is written as,

$$
\begin{equation*}
\frac{d \boldsymbol{f}(\boldsymbol{v})}{d \boldsymbol{v}}=2 \frac{d \boldsymbol{f}\left(\frac{\boldsymbol{v}}{2}\right)}{d \boldsymbol{v}}=\frac{d \boldsymbol{f}\left(\frac{\boldsymbol{v}}{2}\right)}{d\left(\frac{\boldsymbol{v}}{2}\right)} \tag{2.26}
\end{equation*}
$$

Relation (2.26) implies that the derivative of the vectorial function $\boldsymbol{f}(\boldsymbol{v})$ is constant,

$$
\begin{equation*}
\frac{d \boldsymbol{f}(\boldsymbol{v})}{d \boldsymbol{v}}=\alpha=\mathrm{const} \tag{2.27}
\end{equation*}
$$

where the scalar quantity $\alpha>0$ is positive definite in order for the momentum to be oriented in the direction of motion defined by the velocity $\boldsymbol{v}$. Integrating relation (2.27) taking into account the initial condition $\boldsymbol{f}(\mathbf{0})=\mathbf{0}$, we conclude that the vectorial function $\boldsymbol{f}(\boldsymbol{v})$ is a linear function of the velocity $\boldsymbol{v}$,

$$
\begin{equation*}
\boldsymbol{f}(\boldsymbol{v})=\alpha \boldsymbol{v} \tag{2.28}
\end{equation*}
$$

Thus, for very low speeds compared to the propagation speed of light in vacuum, substituting relation (2.28) into relation (2.24), the latter becomes,

$$
\begin{equation*}
\boldsymbol{p}=\alpha m \boldsymbol{v} \tag{2.29}
\end{equation*}
$$

Without loss of generality, we can choose to take $\alpha=1$. In this case, the momentum (2.29) reduces to the product of mass and velocity,

$$
\begin{equation*}
\boldsymbol{p}=m \boldsymbol{v} \tag{2.30}
\end{equation*}
$$

which is a phenomenological expression since it is inferred from experiment. Taking into account the phenomenological relation (2.30), the physical unit of momentum in the international system of units is denoted $[\mathrm{kg} \cdot \mathrm{m} / \mathrm{s}]$.

### 2.3.8 Material point dynamics

Material point dynamics is obtained from the dynamics of a mechanical system by imposing an additional condition. A material point is characterised by a constant mass, which imposes the condition,

$$
\begin{equation*}
\frac{d m}{d t}=0 \tag{2.31}
\end{equation*}
$$

Substituting the expression (2.30) for the momentum into the law of motion (2.19), the latter is expressed explicitly in terms of the velocity as,

$$
\begin{equation*}
\sum \boldsymbol{F}^{\mathrm{ext}}=m \frac{d \boldsymbol{v}}{d t}+\frac{d m}{d t} \boldsymbol{v} \tag{2.32}
\end{equation*}
$$

Taking into account the condition (2.31) and the definition of the acceleration vector (2.2), Newton's $2^{\text {nd }}$ law $(2.32)$ reduces to the law of motion for a material point,

$$
\begin{equation*}
\sum \boldsymbol{F}^{\mathrm{ext}}=m \boldsymbol{a} \tag{2.33}
\end{equation*}
$$

Taking into account the law of motion (2.33), the physical unit of the force in the international system of units is the Newton denoted $[\mathrm{N}]=\left[\mathrm{kg} \cdot \mathrm{m} / \mathrm{s}^{2}\right]$.

