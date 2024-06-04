# CHAPTER 12 <br> Static Equilibrium and Elasticity 

INTRODUCTION In earlier chapters, you learned about forces and Newton's laws for translational motion. You then studied torques and the rotational motion of a body about a fixed axis of rotation. You also learned that static equilibrium means no motion at all and that dynamic equilibrium means motion without acceleration.

In this chapter, we combine the conditions for static translational equilibrium and static rotational equilibrium to describe situations typical for any kind of construction. What type of cable will support a suspension bridge? What type of foundation will support an office building? Will this prosthetic arm function correctly? These are examples of questions that contemporary engineers must be able to answer.

The elastic properties of materials are especially important in engineering applications, including bioengineering. For example, materials that can stretch or compress and then return to their original form or position make good shock absorbers. In this chapter, you will learn about some applications that combine
equilibrium with elasticity to construct real structures that last.

### 12.1 Conditions for Static Equilibrium

We say that a rigid body is in equilibrium when both its linear and angular acceleration are zero relative to an inertial frame of reference. This means that a body in equilibrium can be moving, but if so, its linear and angular velocities must be constant. We say that a rigid body is in static equilibrium when it is at rest in our selected frame of reference. Notice that the distinction between the state of rest and a state of uniform motion is artificial-that is, an object may be at rest in our selected frame of reference, yet to an observer moving at constant velocity relative to our frame, the same object appears to be in uniform motion with constant velocity. Because the motion is relative, what is in static equilibrium to us is in dynamic equilibrium to the moving observer, and vice versa. Since the laws of physics are identical for all inertial reference frames, in an inertial frame of reference, there is no distinction between static equilibrium and equilibrium.

According to Newton's second law of motion, the linear acceleration of a rigid body is caused by a net force acting on it, or

$$
\sum_{k} \overrightarrow{\mathbf{F}}_{k}=m \overrightarrow{\mathbf{a}}_{\mathrm{CM}}
$$

Here, the sum is of all external forces acting on the body, where $m$ is its mass and $\overrightarrow{\mathbf{a}}_{\mathrm{CM}}$ is the linear acceleration of its center of mass (a concept we discussed in Linear Momentum and Collisions on linear momentum and collisions). In equilibrium, the linear acceleration is zero. If we set the acceleration to zero in Equation 12.1, we obtain the following equation:

## First Equilibrium Condition

The first equilibrium condition for the static equilibrium of a rigid body expresses translational equilibrium:

$$
\sum_{k} \overrightarrow{\mathbf{F}}_{k}=\overrightarrow{\mathbf{0}}
$$

The first equilibrium condition, Equation 12.2, is the equilibrium condition for forces, which we encountered when studying applications of Newton's laws.

This vector equation is equivalent to the following three scalar equations for the components of the net force:

$$
\sum_{k} F_{k x}=0, \quad \sum_{k} F_{k y}=0, \quad \sum_{k} F_{k z}=0
$$

Analogously to Equation 12.1, we can state that the rotational acceleration $\overrightarrow{\boldsymbol{\alpha}}$ of a rigid body about a fixed axis of rotation is caused by the net torque acting on the body, or

$$
\sum_{k} \overrightarrow{\boldsymbol{\tau}}_{k}=I \overrightarrow{\boldsymbol{\alpha}}
$$

Here $\boldsymbol{I}$ is the rotational inertia of the body in rotation about this axis and the summation is over all torques $\overrightarrow{\boldsymbol{\tau}}_{k}$ of external forces in Equation 12.2. In equilibrium, the rotational acceleration is zero. By setting to zero the right-hand side of Equation 12.4, we obtain the second equilibrium condition:

## Second Equilibrium Condition

The second equilibrium condition for the static equilibrium of a rigid body expresses rotational equilibrium:

$$
\sum_{k} \overrightarrow{\boldsymbol{\tau}}_{k}=\overrightarrow{\mathbf{0}}
$$

The second equilibrium condition, Equation 12.5, is the equilibrium condition for torques that we encountered when we studied rotational dynamics. It is worth noting that this equation for equilibrium is generally valid for rotational equilibrium about any axis of rotation (fixed or otherwise). Again, this vector equation is equivalent to three scalar equations for the vector components of the net torque:

$$
\sum_{k} \tau_{k x}=0, \quad \sum_{k} \tau_{k y}=0, \quad \sum_{k} \tau_{k z}=0
$$

The second equilibrium condition means that in equilibrium, there is no net external torque to cause rotation about any axis.

The first and second equilibrium conditions are stated in a particular reference frame. The first condition involves only forces and is therefore independent of the origin of the reference frame. However, the second condition involves torque, which is defined as a cross product, $\overrightarrow{\boldsymbol{\tau}}_{k}=\overrightarrow{\mathbf{r}}_{k} \times \overrightarrow{\mathbf{F}}_{k}$, where the position vector $\overrightarrow{\mathbf{r}}_{k}$ with respect to the axis of rotation of the point where the force is applied enters the equation. Therefore, torque depends on the location of the axis in the reference frame. However, when rotational and translational equilibrium conditions hold simultaneously in one frame of reference, then they also hold in any other inertial frame of reference, so that the net torque about any axis of rotation is still zero. The explanation for this is fairly straightforward.

Suppose vector $\overrightarrow{\mathbf{R}}$ is the position of the origin of a new inertial frame of reference $S^{\prime}$ in the old inertial frame of reference $S$. From our study of relative motion, we know that in the new frame of reference $S^{\prime}$, the position vector $\overrightarrow{\mathbf{r}}_{k}^{\prime}$ of the point where the force $\overrightarrow{\mathbf{F}}_{k}$ is applied is related to $\overrightarrow{\mathbf{r}}_{k}$ via the equation

$$
\overrightarrow{\mathbf{r}}_{k}^{\prime}=\overrightarrow{\mathbf{r}}_{k}-\overrightarrow{\mathbf{R}}
$$

Now, we can sum all torques $\overrightarrow{\boldsymbol{\tau}}^{\prime}{ }_{k}=\overrightarrow{\mathbf{r}}^{\prime}{ }_{k} \times \overrightarrow{\mathbf{F}}_{k}$ of all external forces in a new reference frame, $\boldsymbol{S}^{\prime}$ :

$$
\sum_{k} \overrightarrow{\boldsymbol{\tau}}^{\prime}{ }_{k}=\sum_{k} \overrightarrow{\mathbf{r}}_{k}^{\prime} \times \overrightarrow{\mathbf{F}}_{k}=\sum_{k}\left(\overrightarrow{\mathbf{r}}_{k}-\overrightarrow{\mathbf{R}}\right) \times \overrightarrow{\mathbf{F}}_{k}=\sum_{k} \overrightarrow{\mathbf{r}}_{k} \times \overrightarrow{\mathbf{F}}_{k}-\sum_{k} \overrightarrow{\mathbf{R}} \times \overrightarrow{\mathbf{F}}_{k}=\sum_{k} \overrightarrow{\boldsymbol{\tau}}_{k}-\overrightarrow{\mathbf{R}} \times \sum_{k} \overrightarrow{\mathbf{F}}_{k}=\overrightarrow{\mathbf{0}}
$$

In the final step in this chain of reasoning, we used the fact that in equilibrium in the old frame of reference, $S$, the first term vanishes because of Equation 12.5 and the second term vanishes because of Equation 12.2 . Hence, we see that the net torque in any inertial frame of reference $S^{\prime}$ is zero, provided that both conditions for equilibrium hold in an inertial frame of reference $S$.

The practical implication of this is that when applying equilibrium conditions for a rigid body, we are free to choose any point as the origin of the reference frame. Our choice of reference frame is dictated by the physical specifics of the problem we are solving. In one frame of reference, the mathematical form of the equilibrium conditions may be quite complicated, whereas in another frame, the same conditions may have a simpler mathematical form that is easy to solve. The origin of a selected frame of reference is called the pivot point.

In the most general case, equilibrium conditions are expressed by the six scalar equations (Equation 12.3 and Equation 12.6). For planar equilibrium problems with rotation about a fixed axis, which we consider in this chapter, we can reduce the number of equations to three. The standard procedure is to adopt a frame of reference where the $z$-axis is the axis of rotation. With this choice of axis, the net torque has only a $z$-component, all forces that have non-zero torques lie in the $x y$-plane, and therefore contributions to the net torque come from only the $x$ - and $y$-components of external forces. Thus, for planar problems with the axis of rotation perpendicular to the $x y$-plane, we have the following three equilibrium conditions for forces and
torques:

$$
\begin{gather*}
F_{1 x}+F_{2 x}+\cdots+F_{N x}=0 \\
F_{1 y}+F_{2 y}+\cdots+F_{N y}=0 \\
\tau_{1}+\tau_{2}+\cdots+\tau_{N}=0
\end{gather*}
$$

where the summation is over all $N$ external forces acting on the body and over their torques. In Equation 12.9 , we simplified the notation by dropping the subscript $z$, but we understand here that the summation is over all contributions along the $z$-axis, which is the axis of rotation. In Equation 12.9, the $z$-component of torque $\vec{\tau}_{k}$ from the force $\overrightarrow{\mathbf{F}}_{k}$ is

$$
\tau_{k}=r_{k} F_{k} \sin \theta
$$

where $r_{k}$ is the length of the lever arm of the force and $F_{k}$ is the magnitude of the force (as you saw in FixedAxis Rotation). The angle $\theta$ is the angle between vectors $\overrightarrow{\mathbf{r}}_{k}$ and $\overrightarrow{\mathbf{F}}_{k}$, measuring from vector $\overrightarrow{\mathbf{r}}_{k}$ to vector $\overrightarrow{\mathbf{F}}_{k}$ in the counterclockwise direction (Figure 12.2). When using Equation 12.10, we often compute the magnitude of torque and assign its sense as either positive (+) or negative (-), depending on the direction of rotation caused by this torque alone. In Equation 12.9, net torque is the sum of terms, with each term computed from Equation 12.10, and each term must have the correct sense. Similarly, in Equation 12.7, we assign the + sign to force components in the $+x$-direction and the - sign to components in the $-x$-direction. The same rule must be consistently followed in Equation 12.8, when computing force components along the $y$-axis.

In many equilibrium situations, one of the forces acting on the body is its weight. In free-body diagrams, the weight vector is attached to the center of gravity of the body. For all practical purposes, the center of gravity is identical to the center of mass, as you learned in Linear Momentum and Collisions on linear momentum and collisions. Only in situations where a body has a large spatial extension so that the gravitational field is nonuniform throughout its volume, are the center of gravity and the center of mass located at different points. In practical situations, however, even objects as large as buildings or cruise ships are located in a uniform gravitational field on Earth's surface, where the acceleration due to gravity has a constant magnitude of
$g=9.8 \mathrm{~m} / \mathrm{s}^{2}$. In these situations, the center of gravity is identical to the center of mass. Therefore, throughout this chapter, we use the center of mass (CM) as the point where the weight vector is attached. Recall that the CM has a special physical meaning: When an external force is applied to a body at exactly its CM, the body as a whole undergoes translational motion and such a force does not cause rotation.

When the CM is located off the axis of rotation, a net gravitational torque occurs on an object. Gravitational torque is the torque caused by weight. This gravitational torque may rotate the object if there is no support present to balance it. The magnitude of the gravitational torque depends on how far away from the pivot the CM is located. For example, in the case of a tipping truck (Figure 12.3), the pivot is located on the line where the tires make contact with the road's surface. If the CM is located high above the road's surface, the gravitational torque may be large enough to turn the truck over. Passenger cars with a low-lying CM, close to the pavement, are more resistant to tipping over than are trucks.

## EXAMPLE 12.1

## Center of Gravity of a Car

A passenger car with a $2.5-\mathrm{m}$ wheelbase has $52 \%$ of its weight on the front wheels on level ground, as illustrated in Figure 12.4. Where is the CM of this car located with respect to the rear axle?

## Strategy

We do not know the weight $w$ of the car. All we know is that when the car rests on a level surface, $0.52 w$ pushes down on the surface at contact points of the front wheels and $0.48 \mathrm{w}$ pushes down on the surface at contact points of the rear wheels. Also, the contact points are separated from each other by the distance $d=2.5 \mathrm{~m}$. At these contact points, the car experiences normal reaction forces with magnitudes $F_{\mathrm{F}}=0.52 w$ and $F_{\mathrm{R}}=0.48 w$ on the front and rear axles, respectively. We also know that the car is an example of a rigid body in equilibrium whose entire weight $w$ acts at its CM. The CM is located somewhere between the points where the normal reaction forces act, somewhere at a distance $x$ from the point where $F_{R}$ acts. Our task is to find $x$. Thus, we identify three forces acting on the body (the car), and we can draw a free-body diagram for the extended rigid body, as shown in Figure 12.5 .

We are almost ready to write down equilibrium conditions Equation 12.7 through Equation 12.9 for the car, but first we must decide on the reference frame. Suppose we choose the $x$-axis along the length of the car, the $y$-axis vertical, and the $z$-axis perpendicular to this $x y$-plane. With this choice we only need to write Equation 12.7 and Equation 12.9 because all the $y$-components are identically zero. Now we need to decide on the location of the pivot point. We can choose any point as the location of the axis of rotation ( $z$-axis). Suppose we place the axis of rotation at CM, as indicated in the free-body diagram for the car. At this point, we are ready to write the equilibrium conditions for the car.

## Solution

Each equilibrium condition contains only three terms because there are $N=3$ forces acting on the car. The first equilibrium condition, Equation 12.7, reads

$$
+F_{\mathrm{F}}-w+F_{\mathrm{R}}=0
$$

This condition is trivially satisfied because when we substitute the data, Equation 12.11 becomes $+0.52 w-w+0.48 w=0$. The second equilibrium condition, Equation 12.9 , reads

$$
\tau_{\mathrm{F}}+\tau_{w}+\tau_{\mathrm{R}}=0
$$

where $\tau_{\mathrm{F}}$ is the torque of force $F_{\mathrm{F}}, \tau_{w}$ is the gravitational torque of force $w$, and $\tau_{\mathrm{R}}$ is the torque of force $F_{\mathrm{R}}$. When the pivot is located at CM, the gravitational torque is identically zero because the lever arm of the weight with respect to an axis that passes through CM is zero. The lines of action of both normal reaction forces are perpendicular to their lever arms, so in Equation 12.10, we have $|\sin \theta|=1$ for both forces. From the freebody diagram, we read that torque $\tau_{\mathrm{F}}$ causes clockwise rotation about the pivot at $\mathrm{CM}$, so its sense is negative; and torque $\tau_{\mathrm{R}}$ causes counterclockwise rotation about the pivot at $\mathrm{CM}$, so its sense is positive. With this information, we write the second equilibrium condition as

$$
-r_{\mathrm{F}} F_{\mathrm{F}}+r_{\mathrm{R}} F_{\mathrm{R}}=0
$$

With the help of the free-body diagram, we identify the force magnitudes $F_{\mathrm{R}}=0.48 w$ and $F_{\mathrm{F}}=0.52 w$, and their corresponding lever arms $r_{\mathrm{R}}=x$ and $r_{\mathrm{F}}=d-x$. We can now write the second equilibrium condition, Equation 12.13, explicitly in terms of the unknown distance $x$ :

$$
-0.52(d-x) w+0.48 x w=0
$$

Here the weight $w$ cancels and we can solve the equation for the unknown position $x$ of the CM. The answer is $x=0.52 d=0.52(2.5 \mathrm{~m})=1.3 \mathrm{~m}$.

## Solution

Choosing the pivot at the position of the front axle does not change the result. The free-body diagram for this pivot location is presented in Figure 12.6. For this choice of pivot point, the second equilibrium condition is

$$
-r_{w} w+r_{\mathrm{R}} F_{\mathrm{R}}=0
$$

When we substitute the quantities indicated in the diagram, we obtain

$$
-(d-x) w+0.48 d w=0
$$

The answer obtained by solving Equation 12.13 is, again, $x=0.52 d=1.3 \mathrm{~m}$.

## Significance

This example shows that when solving static equilibrium problems, we are free to choose the pivot location. For different choices of the pivot point we have different sets of equilibrium conditions to solve. However, all choices lead to the same solution to the problem.

A special case of static equilibrium occurs when all external forces on an object act at or along the axis of rotation or when the spatial extension of the object can be disregarded. In such a case, the object can be effectively treated like a point mass. In this special case, we need not worry about the second equilibrium condition, Equation 12.9, because all torques are identically zero and the first equilibrium condition (for forces) is the only condition to be satisfied. The free-body diagram and problem-solving strategy for this special case were outlined in Newton's Laws of Motion and Applications of Newton's Laws. You will see a typical equilibrium situation involving only the first equilibrium condition in the next example.

## EXAMPLE 12.2

## A Breaking Tension

A small pan of mass $42.0 \mathrm{~g}$ is supported by two strings, as shown in Figure 12.7. The maximum tension that the string can support is $2.80 \mathrm{~N}$. Mass is added gradually to the pan until one of the strings snaps. Which string is it? How much mass must be added for this to occur?

## Strategy

This mechanical system consisting of strings, masses, and the pan is in static equilibrium. Specifically, the knot that ties the strings to the pan is in static equilibrium. The knot can be treated as a point; therefore, we need only the first equilibrium condition. The three forces pulling at the knot are the tension $\overrightarrow{\mathbf{T}}_{1}$ in the $5.0-\mathrm{cm}$ string, the tension $\overrightarrow{\mathbf{T}}_{2}$ in the 10.0-cm string, and the weight $\overrightarrow{\mathbf{w}}$ of the pan holding the masses. We adopt a rectangular coordinate system with the $y$-axis pointing opposite to the direction of gravity and draw the freebody diagram for the knot (see Figure 12.8). To find the tension components, we must identify the direction angles $\alpha_{1}$ and $\alpha_{2}$ that the strings make with the horizontal direction that is the $x$-axis. As you can see in Figure 12.7, the strings make two sides of a right triangle. We can use the Pythagorean theorem to solve this triangle, shown in Figure 12.8, and find the sine and cosine of the angles $\alpha_{1}$ and $\alpha_{2}$. Then we can resolve the tensions into their rectangular components, substitute in the first condition for equilibrium (Equation 12.7 and Equation 12.8), and solve for the tensions in the strings. The string with a greater tension will break first.

## Solution

The weight $w$ pulling on the knot is due to the mass $M$ of the pan and mass $m$ added to the pan, or $w=(M+m) g$. With the help of the free-body diagram in Figure 12.8, we can set up the equilibrium conditions for the knot:

$$
\begin{array}{lr}
\text { in the } x \text {-direction, } & -T_{1 x}+T_{2 x}=0 \\
\text { in the } y \text {-direction, } \quad+T_{1 y}+T_{2 y}-w=0
\end{array}
$$

From the free-body diagram, the magnitudes of components in these equations are

$$
\begin{array}{ll}
T_{1 x}=T_{1} \cos \alpha_{1}=T_{1} / \sqrt{5}, & T_{1 y}=T_{1} \sin \alpha_{1}=2 T_{1} / \sqrt{5} \\
T_{2 x}=T_{2} \cos \alpha_{2}=2 T_{2} / \sqrt{5}, & T_{2 y}=T_{2} \sin \alpha_{2}=T_{2} / \sqrt{5}
\end{array}
$$

We substitute these components into the equilibrium conditions and simplify. We then obtain two equilibrium equations for the tensions:

$$
\begin{array}{lrl}
\text { in } x \text {-direction, } & T_{1} & =2 T_{2} \\
\text { in } y \text {-direction, } & \frac{2 T_{1}}{\sqrt{5}}+\frac{T_{2}}{\sqrt{5}} & =(M+m) g
\end{array}
$$

The equilibrium equation for the $x$-direction tells us that the tension $T_{1}$ in the $5.0-\mathrm{cm}$ string is twice the tension $T_{2}$ in the $10.0-\mathrm{cm}$ string. Therefore, the shorter string will snap. When we use the first equation to eliminate $T_{2}$ from the second equation, we obtain the relation between the mass $m$ on the pan and the tension $T_{1}$ in the shorter string:

$$
2.5 T_{1} / \sqrt{5}=(M+m) g
$$

The string breaks when the tension reaches the critical value of $T_{1}=2.80 \mathrm{~N}$. The preceding equation can be solved for the critical mass $m$ that breaks the string:

$$
m=\frac{2.5}{\sqrt{5}} \frac{T_{1}}{g}-M=\frac{2.5}{\sqrt{5}} \frac{2.80 \mathrm{~N}}{9.8 \mathrm{~m} / \mathrm{s}^{2}}-0.042 \mathrm{~kg}=0.277 \mathrm{~kg}=277.0 \mathrm{~g}
$$

## Significance

Suppose that the mechanical system considered in this example is attached to a ceiling inside an elevator going up. As long as the elevator moves up at a constant speed, the result stays the same because the weight $w$ does not change. If the elevator moves up with acceleration, the critical mass is smaller because the weight of $M+m$ becomes larger by an apparent weight due to the acceleration of the elevator. Still, in all cases the shorter string breaks first.

### 12.2 Examples of Static Equilibrium

All examples in this chapter are planar problems. Accordingly, we use equilibrium conditions in the component form of Equation 12.7 to Equation 12.9. We introduced a problem-solving strategy in Example 12.1 to illustrate the physical meaning of the equilibrium conditions. Now we generalize this strategy in a list of steps to follow when solving static equilibrium problems for extended rigid bodies. We proceed in five practical steps.

## PROBLEM-SOLVING STRATEG

## Static Equilibrium

1. Identify the object to be analyzed. For some systems in equilibrium, it may be necessary to consider more than one object. Identify all forces acting on the object. Identify the questions you need to answer. Identify the information given in the problem. In realistic problems, some key information may be implicit in the situation rather than provided explicitly.
2. Set up a free-body diagram for the object. (a) Choose the $x y$-reference frame for the problem. Draw a freebody diagram for the object, including only the forces that act on it. When suitable, represent the forces in terms of their components in the chosen reference frame. As you do this for each force, cross out the original force so that you do not erroneously include the same force twice in equations. Label all forces-you will need this for correct computations of net forces in the $x$ - and $y$-directions. For an unknown force, the direction must be assigned arbitrarily; think of it as a 'working direction' or 'suspected direction.' The correct direction is determined by the sign that you obtain in the final solution. A plus sign $(+)$ means that the working direction is the actual direction. A minus sign (-) means that the actual direction is opposite to the assumed working direction. (b) Choose the location of the rotation axis; in other words, choose the pivot point with respect to which you will compute torques of acting forces. On the free-body diagram, indicate the location of the pivot and the lever arms of acting forces-you will need this for correct computations of torques. In the selection of the pivot, keep in mind that the pivot can be placed anywhere you wish, but the guiding principle is that the best choice will simplify as much as possible the calculation of the net torque along the rotation axis.
3. Set up the equations of equilibrium for the object. (a) Use the free-body diagram to write a correct equilibrium condition Equation 12.7 for force components in the $x$-direction. (b) Use the free-body diagram to write a correct equilibrium condition Equation 12.11 for force components in the $y$-direction. (c) Use the free-body diagram to write a correct equilibrium condition Equation 12.9 for torques along the axis of rotation. Use Equation 12.10 to evaluate torque magnitudes and senses.
4. Simplify and solve the system of equations for equilibrium to obtain unknown quantities. At this point, your work involves algebra only. Keep in mind that the number of equations must be the same as the
number of unknowns. If the number of unknowns is larger than the number of equations, the problem cannot be solved.
5. Evaluate the expressions for the unknown quantities that you obtained in your solution. Your final answers should have correct numerical values and correct physical units. If they do not, then use the previous steps to track back a mistake to its origin and correct it. Also, you may independently check for your numerical answers by shifting the pivot to a different location and solving the problem again, which is what we did in Example 12.1.

Note that setting up a free-body diagram for a rigid-body equilibrium problem is the most important component in the solution process. Without the correct setup and a correct diagram, you will not be able to write down correct conditions for equilibrium. Also note that a free-body diagram for an extended rigid body that may undergo rotational motion is different from a free-body diagram for a body that experiences only translational motion (as you saw in the chapters on Newton's laws of motion). In translational dynamics, a body is represented as its CM, where all forces on the body are attached and no torques appear. This does not hold true in rotational dynamics, where an extended rigid body cannot be represented by one point alone. The reason for this is that in analyzing rotation, we must identify torques acting on the body, and torque depends both on the acting force and on its lever arm. Here, the free-body diagram for an extended rigid body helps us identify external torques.

## EXAMPLE 12.3

## The Torque Balance

Three masses are attached to a uniform meter stick, as shown in Figure 12.9. The mass of the meter stick is $150.0 \mathrm{~g}$ and the masses to the left of the fulcrum are $m_{1}=50.0 \mathrm{~g}$ and $m_{2}=75.0 \mathrm{~g}$. Find the mass $m_{3}$ that balances the system when it is attached at the right end of the stick, and the normal reaction force at the fulcrum when the system is balanced.

## Strategy

For the arrangement shown in the figure, we identify the following five forces acting on the meter stick:

$w_{1}=m_{1} g$ is the weight of mass $m_{1} ; w_{2}=m_{2} g$ is the weight of mass $m_{2}$;

$w=m g$ is the weight of the entire meter stick; $w_{3}=m_{3} g$ is the weight of unknown mass $m_{3}$;

$F_{S}$ is the normal reaction force at the support point $S$.

We choose a frame of reference where the direction of the $y$-axis is the direction of gravity, the direction of the $x$-axis is along the meter stick, and the axis of rotation (the $z$-axis) is perpendicular to the $x$-axis and passes through the support point $S$. In other words, we choose the pivot at the point where the meter stick touches the support. This is a natural choice for the pivot because this point does not move as the stick rotates. Now we are ready to set up the free-body diagram for the meter stick. We indicate the pivot and attach five vectors representing the five forces along the line representing the meter stick, locating the forces with respect to the
pivot Figure 12.10. At this stage, we can identify the lever arms of the five forces given the information provided in the problem. For the three hanging masses, the problem is explicit about their locations along the stick, but the information about the location of the weight $w$ is given implicitly. The key word here is "uniform." We know from our previous studies that the CM of a uniform stick is located at its midpoint, so this is where we attach the weight $w$, at the $50-\mathrm{cm}$ mark.

## Solution

With Figure 12.9 and Figure 12.10 for reference, we begin by finding the lever arms of the five forces acting on the stick:

$$
\begin{aligned}
r_{1} & =30.0 \mathrm{~cm}+40.0 \mathrm{~cm}=70.0 \mathrm{~cm} \\
r_{2} & =40.0 \mathrm{~cm} \\
r & =50.0 \mathrm{~cm}-30.0 \mathrm{~cm}=20.0 \mathrm{~cm} \\
r_{S} & =0.0 \mathrm{~cm} \text { (because } F_{S} \text { is attached at the pivot) } \\
r_{3} & =30.0 \mathrm{~cm}
\end{aligned}
$$

Now we can find the five torques with respect to the chosen pivot:

$$
\begin{aligned}
\tau_{1} & =+r_{1} w_{1} \sin 90^{\circ}=+r_{1} m_{1} g & & \text { (counterclockwise rotation, positive sense) } \\
\tau_{2} & =+r_{2} w_{2} \sin 90^{\circ}=+r_{2} m_{2} g & & \text { (counterclockwise rotation, positive sense) } \\
\tau & =+r w \sin 90^{\circ}=+r m g & & \text { (gravitational torque) } \\
\tau_{S} & =r_{S} F_{S} \sin \theta_{S}=0 & & \text { (because } \left.r_{S}=0 \mathrm{~cm}\right) \\
\tau_{3} & =-r_{3} w_{3} \sin 90^{\circ}=-r_{3} m_{3} g & & \text { (clockwise rotation, negative sense) }
\end{aligned}
$$

The second equilibrium condition (equation for the torques) for the meter stick is

$$
\tau_{1}+\tau_{2}+\tau+\tau_{S}+\tau_{3}=0
$$

When substituting torque values into this equation, we can omit the torques giving zero contributions. In this way the second equilibrium condition is

$$
+r_{1} m_{1} g+r_{2} m_{2} g+r m g-r_{3} m_{3} g=0
$$

Selecting the $+y$-direction to be parallel to $\vec{F}_{S}$, the first equilibrium condition for the stick is

$$
-w_{1}-w_{2}-w+F_{S}-w_{3}=0
$$

Substituting the forces, the first equilibrium condition becomes

$$
-m_{1} g-m_{2} g-m g+F_{S}-m_{3} g=0
$$

We solve these equations simultaneously for the unknown values $m_{3}$ and $F_{S}$. In Equation 12.17, we cancel the $g$ factor and rearrange the terms to obtain

$$
r_{3} m_{3}=r_{1} m_{1}+r_{2} m_{2}+r m
$$

To obtain $m_{3}$ we divide both sides by $r_{3}$, so we have

$$
\begin{align*}
m_{3} & =\frac{r_{1}}{r_{3}} m_{1}+\frac{r_{2}}{r_{3}} m_{2}+\frac{r}{r_{3}} m \\
& =\frac{70}{30}(50.0 \mathrm{~g})+\frac{40}{30}(75.0 \mathrm{~g})+\frac{20}{30}(150.0 \mathrm{~g})=316.0 \frac{2}{3} \mathrm{~g} \simeq 317 \mathrm{~g}
\end{align*}
$$

To find the normal reaction force, we rearrange the terms in Equation 12.18, converting grams to kilograms:

$$
\begin{align*}
F_{S} & =\left(m_{1}+m_{2}+m+m_{3}\right) g \\
& =(50.0+75.0+150.0+316.7) \times 10^{-3} \mathrm{~kg} \times 9.8 \frac{\mathrm{m}}{\mathrm{s}^{2}}=5.8 \mathrm{~N}
\end{align*}
$$

## Significance

Notice that Equation 12.17 is independent of the value of $g$. The torque balance may therefore be used to measure mass, since variations in $g$-values on Earth's surface do not affect these measurements. This is not the case for a spring balance because it measures the force.

## EXAMPLE 12.4

## Forces in the Forearm

A weightlifter is holding a 50.0-lb weight (equivalent to $222.4 \mathrm{~N}$ ) with his forearm, as shown in Figure 12.11 . His forearm is positioned at $\beta=60^{\circ}$ with respect to his upper arm. The forearm is supported by a contraction of the biceps muscle, which causes a torque around the elbow. Assuming that the tension in the biceps acts along the vertical direction given by gravity, what tension must the muscle exert to hold the forearm at the position shown? What is the force on the elbow joint? Assume that the forearm's weight is negligible. Give your final answers in SI units.

## Strategy

We identify three forces acting on the forearm: the unknown force $\overrightarrow{\mathbf{F}}$ at the elbow; the unknown tension $\overrightarrow{\mathbf{T}}_{\mathrm{M}}$ in the muscle; and the weight $\overrightarrow{\mathbf{w}}$ with magnitude $w=50 \mathrm{lb}$. We adopt the frame of reference with the $x$-axis along the forearm and the pivot at the elbow. The vertical direction is the direction of the weight, which is the same as the direction of the upper arm. The $x$-axis makes an angle $\beta=60^{\circ}$ with the vertical. The $y$-axis is perpendicular to the $x$-axis. Now we set up the free-body diagram for the forearm. First, we draw the axes, the pivot, and the three vectors representing the three identified forces. Then we locate the angle $\beta$ and represent each force by its $x$ - and $y$-components, remembering to cross out the original force vector to avoid double counting. Finally, we label the forces and their lever arms. The free-body diagram for the forearm is shown in Figure 12.12. At this point, we are ready to set up equilibrium conditions for the forearm. Each force has $x$ - and $y$-components; therefore, we have two equations for the first equilibrium condition, one equation for each component of the net force acting on the forearm.

Notice that in our frame of reference, contributions to the second equilibrium condition (for torques) come only from the $y$-components of the forces because the $x$-components of the forces are all parallel to their lever arms, so that for any of them we have $\sin \theta=0$ in Equation 12.10. For the $y$-components we have $\theta= \pm 90^{\circ}$ in Equation 12.10. Also notice that the torque of the force at the elbow is zero because this force is attached at the pivot. So the contribution to the net torque comes only from the torques of $T_{y}$ and of $w_{y}$.

## Solution

We see from the free-body diagram that the $x$-component of the net force satisfies the equation

$$
+F_{x}+T_{x}-w_{x}=0
$$

and the $y$-component of the net force satisfies

$$
+F_{y}+T_{y}-w_{y}=0
$$

Equation 12.21 and Equation 12.22 are two equations of the first equilibrium condition (for forces). Next, we read from the free-body diagram that the net torque along the axis of rotation is

$$
+r_{T} T_{y}-r_{w} w_{y}=0
$$

Equation 12.23 is the second equilibrium condition (for torques) for the forearm. The free-body diagram shows that the lever arms are $r_{T}=1.5 \mathrm{in}$. and $r_{w}=13.0 \mathrm{in}$. At this point, we do not need to convert inches into SI units, because as long as these units are consistent in Equation 12.23, they cancel out. Using the free-body diagram again, we find the magnitudes of the component forces:

$$
\begin{aligned}
F_{x} & =F \cos \beta=F \cos 60^{\circ}=F / 2 \\
T_{x} & =T \cos \beta=T \cos 60^{\circ}=T / 2 \\
w_{x} & =w \cos \beta=w \cos 60^{\circ}=w / 2 \\
F_{y} & =F \sin \beta=F \sin 60^{\circ}=F \sqrt{3} / 2 \\
T_{y} & =T \sin \beta=T \sin 60^{\circ}=T \sqrt{3} / 2 \\
w_{y} & =w \sin \beta=w \sin 60^{\circ}=w \sqrt{3} / 2
\end{aligned}
$$

We substitute these magnitudes into Equation 12.21, Equation 12.22, and Equation 12.23 to obtain, respectively,

$$
\begin{aligned}
F / 2+T / 2-w / 2 & =0 \\
F \sqrt{3} / 2+T \sqrt{3} / 2-w \sqrt{3} / 2 & =0 \\
r_{T} T \sqrt{3} / 2-r_{w} w \sqrt{3} / 2 & =0
\end{aligned}
$$

When we simplify these equations, we see that we are left with only two independent equations for the two unknown force magnitudes, $F$ and $T$, because Equation 12.21 for the $x$-component is equivalent to Equation 12.22 for the $y$-component. In this way, we obtain the first equilibrium condition for forces

$$
F+T-w=0
$$

and the second equilibrium condition for torques

$$
r_{T} T-r_{w} w=0
$$

The magnitude of tension in the muscle is obtained by solving Equation 12.25 :

$$
T=\frac{r_{w}}{r_{T}} w=\frac{13.0}{1.5}(50 \mathrm{lb})=433 \frac{1}{3} \mathrm{lb} \simeq 433.3 \mathrm{lb}
$$

The force at the elbow is obtained by solving Equation 12.24:

$$
F=w-T=50.0 \mathrm{lb}-433.3 \mathrm{lb}=-383.3 \mathrm{lb}
$$

The negative sign in the equation tells us that the actual force at the elbow is antiparallel to the working direction adopted for drawing the free-body diagram. In the final answer, we convert the forces into SI units of force. The answer is

$$
\begin{gathered}
F=383.3 \mathrm{lb}=383.3(4.448 \mathrm{~N})=1705 \mathrm{~N} \text { downward } \\
T=433.3 \mathrm{lb}=433.3(4.448 \mathrm{~N})=1927 \mathrm{~N} \text { upward }
\end{gathered}
$$

## Significance

Two important issues here are worth noting. The first concerns conversion into SI units, which can be done at
the very end of the solution as long as we keep consistency in units. The second important issue concerns the hinge joints such as the elbow. In the initial analysis of a problem, hinge joints should always be assumed to exert a force in an arbitrary direction, and then you must solve for all components of a hinge force independently. In this example, the elbow force happens to be vertical because the problem assumes the tension by the biceps to be vertical as well. Such a simplification, however, is not a general rule.

## Solution

Suppose we adopt a reference frame with the direction of the $y$-axis along the $50-\mathrm{lb}$ weight and the pivot placed at the elbow. In this frame, all three forces have only $y$-components, so we have only one equation for the first equilibrium condition (for forces). We draw the free-body diagram for the forearm as shown in Figure 12.13, indicating the pivot, the acting forces and their lever arms with respect to the pivot, and the angles $\theta_{T}$ and $\theta_{w}$ that the forces $\overrightarrow{\mathbf{T}}_{\mathrm{M}}$ and $\overrightarrow{\mathbf{w}}$ (respectively) make with their lever arms. In the definition of torque given by Equation 12.10, the angle $\theta_{T}$ is the direction angle of the vector $\vec{T}_{\mathrm{M}}$, counted counterclockwise from the radial direction of the lever arm that always points away from the pivot. By the same convention, the angle $\theta_{w}$ is measured counterclockwise from the radial direction of the lever arm to the vector $\overrightarrow{\mathbf{w}}$. Done this way, the nonzero torques are most easily computed by directly substituting into Equation 12.10 as follows:

The second equilibrium condition, $\tau_{T}+\tau_{w}=0$, can be now written as

$$
r_{T} T \sqrt{3} / 2-r_{w} w \sqrt{3} / 2=0
$$

From the free-body diagram, the first equilibrium condition (for forces) is

$$
-F+T-w=0
$$

Equation 12.26 is identical to Equation 12.25 and gives the result $T=433.3 \mathrm{lb}$. Equation 12.27 gives

$$
F=T-w=433.3 \mathrm{lb}-50.0 \mathrm{lb}=383.3 \mathrm{lb}
$$

We see that these answers are identical to our previous answers, but the second choice for the frame of reference leads to an equivalent solution that is simpler and quicker because it does not require that the forces be resolved into their rectangular components.

## A Ladder Resting Against a Wall

A uniform ladder is $L=5.0 \mathrm{~m}$ long and weighs $400.0 \mathrm{~N}$. The ladder rests against a slippery vertical wall, as shown in Figure 12.14. The inclination angle between the ladder and the rough floor is $\beta=53^{\circ}$. Find the reaction forces from the floor and from the wall on the ladder and the coefficient of static friction $\mu_{\mathrm{s}}$ at the interface of the ladder with the floor that prevents the ladder from slipping.

## Strategy

We can identify four forces acting on the ladder. The first force is the normal reaction force $N$ from the floor in the upward vertical direction. The second force is the static friction force $f=\mu_{\mathrm{s}} N$ directed horizontally along the floor toward the wall-this force prevents the ladder from slipping. These two forces act on the ladder at its contact point with the floor. The third force is the weight $w$ of the ladder, attached at its CM located midway between its ends. The fourth force is the normal reaction force $F$ from the wall in the horizontal direction away from the wall, attached at the contact point with the wall. There are no other forces because the wall is slippery, which means there is no friction between the wall and the ladder. Based on this analysis, we adopt the frame of reference with the $y$-axis in the vertical direction (parallel to the wall) and the $x$-axis in the horizontal direction (parallel to the floor). In this frame, each force has either a horizontal component or a vertical component but not both, which simplifies the solution. We select the pivot at the contact point with the floor. In the free-body diagram for the ladder, we indicate the pivot, all four forces and their lever arms, and the angles between lever arms and the forces, as shown in Figure 12.15. With our choice of the pivot location, there is no torque either from the normal reaction force $N$ or from the static friction $f$ because they both act at the pivot.

## Solution

From the free-body diagram, the net force in the $x$-direction is

$$
+f-F=0
$$

the net force in the $y$-direction is

$$
+N-w=0
$$

and the net torque along the rotation axis at the pivot point is

$$
\tau_{w}+\tau_{F}=0
$$

where $\tau_{w}$ is the torque of the weight $w$ and $\tau_{F}$ is the torque of the reaction $F$. From the free-body diagram, we identify that the lever arm of the reaction at the wall is $r_{F}=L=5.0 \mathrm{~m}$ and the lever arm of the weight is $r_{w}=L / 2=2.5 \mathrm{~m}$. With the help of the free-body diagram, we identify the angles to be used in Equation 12.10 for torques: $\theta_{F}=180^{\circ}-\beta$ for the torque from the reaction force with the wall, and $\theta_{w}=180^{\circ}+\left(90^{\circ}-\beta\right)$ for the torque due to the weight. Now we are ready to use Equation 12.10 to compute torques:

$$
\begin{gathered}
\tau_{w}=r_{w} w \sin \theta_{w}=r_{w} w \sin \left(180^{\circ}+90^{\circ}-\beta\right)=-\frac{L}{2} w \sin \left(90^{\circ}-\beta\right)=-\frac{L}{2} w \cos \beta \\
\tau_{F}=r_{F} F \sin \theta_{F}=r_{F} F \sin \left(180^{\circ}-\beta\right)=L F \sin \beta
\end{gathered}
$$

We substitute the torques into Equation 12.30 and solve for $\boldsymbol{F}$ :

$$
\begin{align*}
-\frac{L}{2} w \cos \beta+L F \sin \beta & =0 \\
F=\frac{w}{2} \cot \beta=\frac{400.0 \mathrm{~N}}{2} \cot 53^{\circ} & =150.7 \mathrm{~N}
\end{align*}
$$

We obtain the normal reaction force with the floor by solving Equation 12.29: $N=w=400.0 \mathrm{~N}$. The magnitude of friction is obtained by solving Equation 12.28 : $f=F=150.7 \mathrm{~N}$. The coefficient of static friction is $\mu_{\mathrm{s}}=f / N=150.7 / 400.0=0.377$.

The net force on the ladder at the contact point with the floor is the vector sum of the normal reaction from the floor and the static friction forces:

$$
\overrightarrow{\mathbf{F}}_{\text {floor }}=\overrightarrow{\mathbf{f}}+\overrightarrow{\mathbf{N}}=(150.7 \mathrm{~N})(-\hat{\mathbf{i}})+(400.0 \mathrm{~N})(+\hat{\mathbf{j}})=(-150.7 \hat{\mathbf{i}}+400.0 \hat{\mathbf{j}}) \mathrm{N}
$$

Its magnitude is

$$
F_{\text {floor }}=\sqrt{f^{2}+N^{2}}=\sqrt{150.7^{2}+400.0^{2}} \mathrm{~N}=427.4 \mathrm{~N}
$$

and its direction is

$$
\varphi=\tan ^{-1}(N / f)=\tan ^{-1}(400.0 / 150.7)=69.3^{\circ} \text { above the floor. }
$$

We should emphasize here two general observations of practical use. First, notice that when we choose a pivot point, there is no expectation that the system will actually pivot around the chosen point. The ladder in this example is not rotating at all but firmly stands on the floor; nonetheless, its contact point with the floor is a good choice for the pivot. Second, notice when we use Equation 12.10 for the computation of individual torques, we do not need to resolve the forces into their normal and parallel components with respect to the direction of the lever arm, and we do not need to consider a sense of the torque. As long as the angle in Equation 12.10 is correctly identified-with the help of a free-body diagram-as the angle measured counterclockwise from the direction of the lever arm to the direction of the force vector, Equation 12.10 gives both the magnitude and the sense of the torque. This is because torque is the vector product of the lever-arm vector crossed with the force vector, and Equation 12.10 expresses the rectangular component of this vector product along the axis of rotation.

## Significance

This result is independent of the length of the ladder because $L$ is cancelled in the second equilibrium condition, Equation 12.31. No matter how long or short the ladder is, as long as its weight is $400 \mathrm{~N}$ and the angle with the floor is $53^{\circ}$, our results hold. But the ladder will slip if the net torque becomes negative in Equation 12.31. This happens for some angles when the coefficient of static friction is not great enough to prevent the ladder from slipping.

## EXAMPLE 12.6

## Forces on Door Hinges

A swinging door that weighs $w=400.0 \mathrm{~N}$ is supported by hinges $A$ and $B$ so that the door can swing about a vertical axis passing through the hinges Figure 12.16. The door has a width of $b=1.00 \mathrm{~m}$, and the door slab has a uniform mass density. The hinges are placed symmetrically at the door's edge in such a way that the door's weight is evenly distributed between them. The hinges are separated by distance $a=2.00 \mathrm{~m}$. Find the forces on the hinges when the door rests half-open.

## Strategy

The forces that the door exerts on its hinges can be found by simply reversing the directions of the forces that the hinges exert on the door. Hence, our task is to find the forces from the hinges on the door. Three forces act on the door slab: an unknown force $\overrightarrow{\mathbf{A}}$ from hinge $A$, an unknown force $\overrightarrow{\mathbf{B}}$ from hinge $B$, and the known weight $\overrightarrow{\mathbf{w}}$ attached at the center of mass of the door slab. The CM is located at the geometrical center of the door because the slab has a uniform mass density. We adopt a rectangular frame of reference with the $y$-axis along the direction of gravity and the $x$-axis in the plane of the slab, as shown in panel (a) of Figure 12.17, and resolve all forces into their rectangular components. In this way, we have four unknown component forces: two components of force $\overrightarrow{\mathbf{A}}\left(A_{x}\right.$ and $\left.A_{y}\right)$, and two components of force $\overrightarrow{\mathbf{B}}\left(\boldsymbol{B}_{x}\right.$ and $\left.\boldsymbol{B}_{y}\right)$. In the free-body diagram, we represent the two forces at the hinges by their vector components, whose assumed orientations are arbitrary. Because there are four unknowns $\left(A_{x}, B_{x}, A_{y}\right.$, and $\left.B_{y}\right)$, we must set up four independent equations. One equation is the equilibrium condition for forces in the $x$-direction. The second equation is the equilibrium condition for forces in the $y$-direction. The third equation is the equilibrium condition for torques in rotation about a hinge. Because the weight is evenly distributed between the hinges, we have the fourth equation, $A_{y}=B_{y}$. To set up the equilibrium conditions, we draw a free-body diagram and choose the pivot point at the upper hinge, as shown in panel (b) of Figure 12.17. Finally, we solve the equations for the unknown force components and find the forces.

## Solution

From the free-body diagram for the door we have the first equilibrium condition for forces:

$$
\begin{aligned}
& \text { in } x \text {-direction: }-A_{x}+B_{x}=0 \Rightarrow A_{x}=B_{x} \\
& \text { in } y \text {-direction: }+A_{y}+B_{y}-w=0 \Rightarrow A_{y}=B_{y}=\frac{w}{2}=\frac{400.0 \mathrm{~N}}{2}=200.0 \mathrm{~N}
\end{aligned}
$$

We select the pivot at point $P$ (upper hinge, per the free-body diagram) and write the second equilibrium condition for torques in rotation about point $P$ :

$$
\text { pivot at } P: \tau_{w}+\tau_{B x}+\tau_{B y}=0
$$

We use the free-body diagram to find all the terms in this equation:

$$
\begin{aligned}
\tau_{w} & =d w \sin (-\beta)=-d w \sin \beta=-d w \frac{b / 2}{d}=-w \frac{b}{2} \\
\tau_{B x} & =a B_{x} \sin 90^{\circ}=+a B_{x} \\
\tau_{B y} & =a B_{y} \sin 180^{\circ}=0
\end{aligned}
$$

In evaluating $\sin \beta$, we use the geometry of the triangle shown in part (a) of the figure. Now we substitute these torques into Equation 12.32 and compute $\boldsymbol{B}_{x}$ :

$$
\text { pivot at } P:-w \frac{b}{2}+a B_{x}=0 \Rightarrow B_{x}=w \frac{b}{2 a}=(400.0 \mathrm{~N}) \frac{1}{2 \cdot 2}=100.0 \mathrm{~N}
$$

Therefore the magnitudes of the horizontal component forces are $A_{x}=B_{x}=100.0 \mathrm{~N}$. The forces on the door are

at the upper hinge: $\overrightarrow{\mathbf{F}}_{A \text { on door }}=-100.0 \mathrm{~N} \hat{\mathbf{i}}+200.0 \mathrm{~N} \hat{\mathbf{j}}$

at the lower hinge: $\overrightarrow{\mathbf{F}}_{\boldsymbol{B}}$ on door $=+100.0 \mathrm{~N} \hat{\mathbf{i}}+200.0 \mathrm{~N} \hat{\mathbf{j}}$.

The forces on the hinges are found from Newton's third law as

on the upper hinge: $\overrightarrow{\mathbf{F}}_{\text {door on } A}=100.0 \mathrm{Ni}-200.0 \mathrm{~N} \hat{\mathbf{j}}$

on the lower hinge: $\overrightarrow{\mathbf{F}}_{\text {door on } B}=-100.0 \mathrm{Ni}-200.0 \mathrm{~N} \hat{\mathbf{j}}$.

## Significance

Note that if the problem were formulated without the assumption of the weight being equally distributed between the two hinges, we wouldn't be able to solve it because the number of the unknowns would be greater than the number of equations expressing equilibrium conditions.

### 12.3 Stress, Strain, and Elastic Modulus

A model of a rigid body is an idealized example of an object that does not deform under the actions of external forces. It is very useful when analyzing mechanical systems-and many physical objects are indeed rigid to a great extent. The extent to which an object can be perceived as rigid depends on the physical properties of the material from which it is made. For example, a ping-pong ball made of plastic is brittle, and a tennis ball made of rubber is elastic when acted upon by squashing forces. However, under other circumstances, both a pingpong ball and a tennis ball may bounce well as rigid bodies. Similarly, someone who designs prosthetic limbs may be able to approximate the mechanics of human limbs by modeling them as rigid bodies; however, the actual combination of bones and tissues is an elastic medium.

For the remainder of this chapter, we move from consideration of forces that affect the motion of an object to those that affect an object's shape. A change in shape due to the application of a force is known as a deformation. Even very small forces are known to cause some deformation. Deformation is experienced by objects or physical media under the action of external forces-for example, this may be squashing, squeezing, ripping, twisting, shearing, or pulling the objects apart. In the language of physics, two terms describe the forces on objects undergoing deformation: stress and strain.

Stress is a quantity that describes the magnitude of forces that cause deformation. Stress is generally defined as force per unit area. When forces pull on an object and cause its elongation, like the stretching of an elastic band, we call such stress a tensile stress. When forces cause a compression of an object, we call it a compressive stress. When an object is being squeezed from all sides, like a submarine in the depths of an ocean, we call this kind of stress a bulk stress (or volume stress). In other situations, the acting forces may be neither tensile nor compressive, and still produce a noticeable deformation. For example, suppose you hold a book tightly between the palms of your hands, then with one hand you press-and-pull on the front cover away from you, while with the other hand you press-and-pull on the back cover toward you. In such a case, when deforming forces act tangentially to the object's surface, we call them 'shear' forces and the stress they cause is called shear stress.

The SI unit of stress is the pascal (Pa). When one newton of force presses on a unit surface area of one meter squared, the resulting stress is one pascal:

$$
\text { one pascal }=1.0 \mathrm{~Pa}=\frac{1.0 \mathrm{~N}}{1.0 \mathrm{~m}^{2}}
$$

In the British system of units, the unit of stress is 'psi,' which stands for 'pound per square inch' (lb/in $\left.{ }^{2}\right)$. Another unit that is often used for bulk stress is the atm (atmosphere). Conversion factors are

$$
\begin{gathered}
1 \mathrm{psi}=6895 \mathrm{~Pa} \text { and } 1 \mathrm{~Pa}=1.450 \times 10^{-4} \mathrm{psi} \\
1 \mathrm{~atm}=1.013 \times 10^{5} \mathrm{~Pa}=14.7 \mathrm{psi}
\end{gathered}
$$

An object or medium under stress becomes deformed. The quantity that describes this deformation is called strain. Strain is given as a fractional change in either length (under tensile stress) or volume (under bulk stress) or geometry (under shear stress). Therefore, strain is a dimensionless number. Strain under a tensile stress is called tensile strain, strain under bulk stress is called bulk strain (or volume strain), and that caused by shear stress is called shear strain.

The greater the stress, the greater the strain; however, the relation between strain and stress does not need to be linear. Only when stress is sufficiently low is the deformation it causes in direct proportion to the stress value. The proportionality constant in this relation is called the elastic modulus. In the linear limit of low stress values, the general relation between stress and strain is

As we can see from dimensional analysis of this relation, the elastic modulus has the same physical unit as stress because strain is dimensionless.

We can also see from Equation 12.33 that when an object is characterized by a large value of elastic modulus, the effect of stress is small. On the other hand, a small elastic modulus means that stress produces large strain and noticeable deformation. For example, a stress on a rubber band produces larger strain (deformation) than the same stress on a steel band of the same dimensions because the elastic modulus for rubber is two orders of magnitude smaller than the elastic modulus for steel.

The elastic modulus for tensile stress is called Young's modulus; that for the bulk stress is called the bulk modulus; and that for shear stress is called the shear modulus. Note that the relation between stress and strain is an observed relation, measured in the laboratory. Elastic moduli for various materials are measured under various physical conditions, such as varying temperature, and collected in engineering data tables for reference (Table 12.1). These tables are valuable references for industry and for anyone involved in engineering or construction. In the next section, we discuss strain-stress relations beyond the linear limit represented by Equation 12.33, in the full range of stress values up to a fracture point. In the remainder of this section, we study the linear limit expressed by Equation 12.33.

| Material | Young's modulus <br> $\times 10^{10} \mathrm{~Pa}$ | Bulk modulus <br> $\times 10^{10} \mathrm{~Pa}$ | Shear modulus <br> $\times 10^{10} \mathrm{~Pa}$ |
| :--- | :--- | :--- | :--- |
| Aluminum | 7.0 | 7.5 | 2.5 |
| Bone (tension) | 1.6 | 0.8 | 8.0 |
| Bone (compression) | 0.9 |  |  |
| Brass | 9.0 | 6.0 | 3.5 |
| Brick | 1.5 |  |  |
| Concrete | 2.0 | 14.0 | 4.4 |
| Copper | 11.0 | 5.0 | 2.5 |
| Crown glass | 6.0 | 4.5 | 2.0 |
| Granite | 4.5 | 17.0 |  |
| Hair (human) | 1.0 | 4.1 | 0.6 |
| Hardwood | 1.5 | 1.0 | 2.0 |
| Iron | 21.0 | 7.0 |  |
| Lead | 1.6 | 6.0 |  |
| Marble | 6.0 |  |  |
| Nickel | 21.0 |  |  |


| Material | Young's modulus <br> $\times 10^{10} \mathrm{~Pa}$ | Bulk modulus <br> $\times 10^{10} \mathrm{~Pa}$ | Shear modulus <br> $\times 10^{10} \mathrm{~Pa}$ |
| :--- | :--- | :--- | :--- |
| Polystyrene | 3.0 |  |  |
| Silk | 6.0 |  |  |
| Spider thread | 3.0 |  |  |
| Steel | 20.0 | 16.0 | 7.5 |
| Acetone |  | 0.07 |  |
| Ethanol |  | 0.09 |  |
| Glycerin |  | 0.45 |  |
| Mercury |  | 0.22 |  |
| Water |  | 2.5 |  |

Table 12.1 Approximate Elastic Moduli for Selected Materials

## Tensile or Compressive Stress, Strain, and Young's Modulus

Tension or compression occurs when two antiparallel forces of equal magnitude act on an object along only one of its dimensions, in such a way that the object does not move. One way to envision such a situation is illustrated in Figure 12.18. A rod segment is either stretched or squeezed by a pair of forces acting along its length and perpendicular to its cross-section. The net effect of such forces is that the rod changes its length from the original length $L_{0}$ that it had before the forces appeared, to a new length $L$ that it has under the action of the forces. This change in length $\Delta L=L-L_{0}$ may be either elongation (when $L$ is larger than the original length $L_{0}$ ) or contraction (when $L$ is smaller than the original length $L_{0}$ ). Tensile stress and strain occur when the forces are stretching an object, causing its elongation, and the length change $\Delta L$ is positive. Compressive stress and strain occur when the forces are contracting an object, causing its shortening, and the length change $\Delta L$ is negative.

In either of these situations, we define stress as the ratio of the deforming force $F_{\perp}$ to the cross-sectional area $A$ of the object being deformed. The symbol $F_{\perp}$ that we reserve for the deforming force means that this force acts perpendicularly to the cross-section of the object. Forces that act parallel to the cross-section do not change the length of an object. The definition of the tensile stress is

$$
\text { tensile stress }=\frac{F_{\perp}}{A}
$$

Tensile strain is the measure of the deformation of an object under tensile stress and is defined as the fractional change of the object's length when the object experiences tensile stress

$$
\text { tensile strain }=\frac{\Delta L}{L_{0}}
$$

Compressive stress and strain are defined by the same formulas, Equation 12.34 and Equation 12.35, respectively. The only difference from the tensile situation is that for compressive stress and strain, we take absolute values of the right-hand sides in Equation 12.34 and Equation 12.35.

Young's modulus $Y$ is the elastic modulus when deformation is caused by either tensile or compressive stress, and is defined by Equation 12.33 . Dividing this equation by tensile strain, we obtain the expression for Young's modulus:

$$
Y=\frac{\text { tensile stress }}{\text { tensile strain }}=\frac{F_{\perp} / A}{\Delta L / L_{0}}=\frac{F_{\perp}}{A} \frac{L_{0}}{\Delta L}
$$

## EXAMPLE 12.7

## Compressive Stress in a Pillar

A sculpture weighing $10,000 \mathrm{~N}$ rests on a horizontal surface at the top of a $6.0-\mathrm{m}$-tall vertical pillar Figure 12.19. The pillar's cross-sectional area is $0.20 \mathrm{~m}^{2}$ and it is made of granite with a mass density of $2700 \mathrm{~kg} / \mathrm{m}^{3}$. Find the compressive stress at the cross-section located $3.0 \mathrm{~m}$ below the top of the pillar and the value of the compressive strain of the top $3.0-\mathrm{m}$ segment of the pillar.

## Strategy

First we find the weight of the $3.0-\mathrm{m}$-long top section of the pillar. The normal force that acts on the crosssection located $3.0 \mathrm{~m}$ down from the top is the sum of the pillar's weight and the sculpture's weight. Once we have the normal force, we use Equation 12.34 to find the stress. To find the compressive strain, we find the value of Young's modulus for granite in Table 12.1 and invert Equation 12.36.

## Solution

The volume of the pillar segment with height $h=3.0 \mathrm{~m}$ and cross-sectional area $A=0.20 \mathrm{~m}^{2}$ is

$$
V=A h=\left(0.20 \mathrm{~m}^{2}\right)(3.0 \mathrm{~m})=0.60 \mathrm{~m}^{3}
$$

With the density of granite $\rho=2.7 \times 10^{3} \mathrm{~kg} / \mathrm{m}^{3}$, the mass of the pillar segment is

$$
m=\rho V=\left(2.7 \times 10^{3} \mathrm{~kg} / \mathrm{m}^{3}\right)\left(0.60 \mathrm{~m}^{3}\right)=1.60 \times 10^{3} \mathrm{~kg}
$$

The weight of the pillar segment is

$$
w_{p}=m g=\left(1.60 \times 10^{3} \mathrm{~kg}\right)\left(9.80 \mathrm{~m} / \mathrm{s}^{2}\right)=1.568 \times 10^{4} \mathrm{~N}
$$

The weight of the sculpture is $w_{s}=1.0 \times 10^{4} \mathrm{~N}$, so the normal force on the cross-sectional surface located 3.0 $\mathrm{m}$ below the sculpture is

$$
F_{\perp}=w_{p}+w_{s}=(1.568+1.0) \times 10^{4} \mathrm{~N}=2.568 \times 10^{4} \mathrm{~N}
$$

Therefore, the stress is

$$
\text { stress }=\frac{F_{\perp}}{A}=\frac{2.568 \times 10^{4} \mathrm{~N}}{0.20 \mathrm{~m}^{2}}=1.284 \times 10^{5} \mathrm{~Pa}=128.4 \mathrm{kPa}
$$

Young's modulus for granite is $Y=4.5 \times 10^{10} \mathrm{~Pa}=4.5 \times 10^{7} \mathrm{kPa}$. Therefore, the compressive strain at this position is

$$
\text { strain }=\frac{\text { stress }}{Y}=\frac{128.4 \mathrm{kPa}}{4.5 \times 10^{7} \mathrm{kPa}}=2.85 \times 10^{-6}
$$

## Significance

Notice that the normal force acting on the cross-sectional area of the pillar is not constant along its length, but varies from its smallest value at the top to its largest value at the bottom of the pillar. Thus, if the pillar has a
uniform cross-sectional area along its length, the stress is largest at its base.

## EXAMPLE 12.8

## Stretching a Rod

A $2.0-\mathrm{m}-$ long steel rod has a cross-sectional area of $0.30 \mathrm{~cm}^{2}$. The rod is a part of a vertical support that holds a heavy $550-\mathrm{kg}$ platform that hangs attached to the rod's lower end. Ignoring the weight of the rod, what is the tensile stress in the rod and the elongation of the rod under the stress?

## Strategy

First we compute the tensile stress in the rod under the weight of the platform in accordance with Equation 12.34. Then we invert Equation 12.36 to find the rod's elongation, using $L_{0}=2.0 \mathrm{~m}$. From Table 12.1, Young's modulus for steel is $Y=2.0 \times 10^{11} \mathrm{~Pa}$.

## Solution

Substituting numerical values into the equations gives us

$$
\begin{aligned}
\frac{F_{\perp}}{A} & =\frac{(550 \mathrm{~kg})\left(9.8 \mathrm{~m} / \mathrm{s}^{2}\right)}{3.0 \times 10^{-5} \mathrm{~m}^{2}}=1.8 \times 10^{8} \mathrm{~Pa} \\
\Delta L & =\frac{F_{\perp}}{A} \frac{L_{0}}{Y}=\left(1.8 \times 10^{8} \mathrm{~Pa}\right) \frac{2.0 \mathrm{~m}}{2.0 \times 10^{11} \mathrm{~Pa}}=1.8 \times 10^{-3} \mathrm{~m}=1.8 \mathrm{~mm}
\end{aligned}
$$

## Significance

Similarly as in the example with the column, the tensile stress in this example is not uniform along the length of the rod. Unlike in the previous example, however, if the weight of the rod is taken into consideration, the stress in the rod is largest at the top and smallest at the bottom of the rod where the equipment is attached.

Objects can often experience both compressive stress and tensile stress simultaneously Figure 12.20. One example is a long shelf loaded with heavy books that sags between the end supports under the weight of the books. The top surface of the shelf is in compressive stress and the bottom surface of the shelf is in tensile stress. Similarly, long and heavy beams sag under their own weight. In modern building construction, such bending strains can be almost eliminated with the use of I-beams Figure 12.21.

## Bulk Stress, Strain, and Modulus

When you dive into water, you feel a force pressing on every part of your body from all directions. What you are experiencing then is bulk stress, or in other words, pressure. Bulk stress always tends to decrease the volume enclosed by the surface of a submerged object. The forces of this "squeezing" are always perpendicular to the submerged surface Figure 12.22. The effect of these forces is to decrease the volume of the submerged object by an amount $\Delta V$ compared with the volume $V_{0}$ of the object in the absence of bulk stress. This kind of deformation is called bulk strain and is described by a change in volume relative to the original volume:

$$
\text { bulk strain }=\frac{\Delta V}{V_{0}} \text {. }
$$

The bulk strain results from the bulk stress, which is a force $F_{\perp}$ normal to a surface that presses on the unit surface area $A$ of a submerged object. This kind of physical quantity, or pressure $p$, is defined as

$$
\text { pressure }=p \equiv \frac{F_{\perp}}{A}
$$

We will study pressure in fluids in greater detail in Fluid Mechanics. An important characteristic of pressure is that it is a scalar quantity and does not have any particular direction; that is, pressure acts equally in all possible directions. When you submerge your hand in water, you sense the same amount of pressure acting on the top surface of your hand as on the bottom surface, or on the side surface, or on the surface of the skin between your fingers. What you are perceiving in this case is an increase in pressure $\Delta p$ over what you are used to feeling when your hand is not submerged in water. What you feel when your hand is not submerged in the water is the normal pressure $p_{0}$ of one atmosphere, which serves as a reference point. The bulk stress is this increase in pressure, or $\Delta p$, over the normal level, $p_{0}$.

When the bulk stress increases, the bulk strain increases in response, in accordance with Equation 12.33 . The proportionality constant in this relation is called the bulk modulus, $B$, or

$$
B=\frac{\text { bulk stress }}{\text { bulk strain }}=-\frac{\Delta p}{\Delta V / V_{0}}=-\Delta p \frac{V_{0}}{\Delta V}
$$

The minus sign that appears in Equation 12.39 is for consistency, to ensure that $B$ is a positive quantity. Note that the minus sign (-) is necessary because an increase $\Delta p$ in pressure (a positive quantity) always causes a decrease $\Delta V$ in volume, and decrease in volume is a negative quantity. The reciprocal of the bulk modulus is called compressibility $k$, or

$$
k=\frac{1}{B}=-\frac{\Delta V / V_{0}}{\Delta p}
$$

The term 'compressibility' is used in relation to fluids (gases and liquids). Compressibility describes the change in the volume of a fluid per unit increase in pressure. Fluids characterized by a large compressibility are relatively easy to compress. For example, the compressibility of water is $4.64 \times 10^{-5} / \mathrm{atm}$ and the compressibility of acetone is $1.45 \times 10^{-4} / \mathrm{atm}$. This means that under a 1.0 -atm increase in pressure, the relative decrease in volume is approximately three times as large for acetone as it is for water.

## EXAMPLE 12.9

## Hydraulic Press

In a hydraulic press Figure 12.23, a 250 -liter volume of oil is subjected to a 2300 -psi pressure increase. If the compressibility of oil is $2.0 \times 10^{-5} / \mathrm{atm}$, find the bulk strain and the absolute decrease in the volume of oil when the press is operating.

## Strategy

We must invert Equation 12.40 to find the bulk strain. First, we convert the pressure increase from psi to atm,
$\Delta p=2300 \mathrm{psi}=2300 / 14.7 \mathrm{~atm} \approx 160 \mathrm{~atm}$, and identify $V_{0}=250 \mathrm{~L}$.

## Solution

Substituting values into the equation, we have

$$
\text { bulk strain }=\frac{\Delta V}{V_{0}}=\frac{\Delta p}{B}=k \Delta p=\left(2.0 \times 10^{-5} / \mathrm{atm}\right)(160 \mathrm{~atm})=0.0032
$$

answer: $\Delta V=0.0032 V_{0}=0.0032(250 \mathrm{~L})=0.78 \mathrm{~L}$.

## Significance

Notice that since the compressibility of water is 2.32 times larger than that of oil, if the working substance in the hydraulic press of this problem were changed to water, the bulk strain as well as the volume change would be 2.32 times larger.

## Shear Stress, Strain, and Modulus

The concepts of shear stress and strain concern only solid objects or materials. Buildings and tectonic plates are examples of objects that may be subjected to shear stresses. In general, these concepts do not apply to fluids.

Shear deformation occurs when two antiparallel forces of equal magnitude are applied tangentially to opposite surfaces of a solid object, causing no deformation in the transverse direction to the line of force, as in the typical example of shear stress illustrated in Figure 12.24. Shear deformation is characterized by a gradual shift $\Delta x$ of layers in the direction tangent to the acting forces. This gradation in $\Delta x$ occurs in the transverse direction along some distance $L_{0}$. Shear strain is defined by the ratio of the largest displacement $\Delta x$ to the transverse distance $L_{0}$

$$
\text { shear strain }=\frac{\Delta x}{L_{0}}
$$

Shear strain is caused by shear stress. Shear stress is due to forces that act parallel to the surface. We use the symbol $F_{\|}$for such forces. The magnitude $F_{\|}$per surface area $A$ where shearing force is applied is the measure of shear stress

$$
\text { shear stress }=\frac{F_{\|}}{A} \text {. }
$$

The shear modulus is the proportionality constant in Equation 12.33 and is defined by the ratio of stress to strain. Shear modulus is commonly denoted by $S$ :

$$
S=\frac{\text { shear stress }}{\text { shear strain }}=\frac{F_{\|} / A}{\Delta x / L_{0}}=\frac{F_{\|}}{A} \frac{L_{0}}{\Delta x}
$$

## EXAMPLE 12.10

## An Old Bookshelf

A cleaning person tries to move a heavy, old bookcase on a carpeted floor by pushing tangentially on the surface of the very top shelf. However, the only noticeable effect of this effort is similar to that seen in Figure 12.24, and it disappears when the person stops pushing. The bookcase is $180.0 \mathrm{~cm}$ tall and $90.0 \mathrm{~cm}$ wide with four $30.0-\mathrm{cm}$-deep shelves, all partially loaded with books. The total weight of the bookcase and books is 600.0 $\mathrm{N}$. If the person gives the top shelf a $50.0-\mathrm{N}$ push that displaces the top shelf horizontally by $15.0 \mathrm{~cm}$ relative to the motionless bottom shelf, find the shear modulus of the bookcase.

## Strategy

The only pieces of relevant information are the physical dimensions of the bookcase, the value of the tangential force, and the displacement this force causes. We identify $F_{\|}=50.0 \mathrm{~N}, \Delta x=15.0 \mathrm{~cm}, L_{0}=180.0 \mathrm{~cm}$, and $A=(30.0 \mathrm{~cm})(90.0 \mathrm{~cm})=2700.0 \mathrm{~cm}^{2}$, and we use Equation 12.43 to compute the shear modulus.

## Solution

Substituting numbers into the equations, we obtain for the shear modulus

$$
S=\frac{F_{\|}}{A} \frac{L_{0}}{\Delta x}=\frac{50.0 \mathrm{~N}}{2700.0 \mathrm{~cm}^{2}} \frac{180.0 \mathrm{~cm} .}{15.0 \mathrm{~cm} .}=\frac{2}{9} \frac{\mathrm{N}}{\mathrm{cm}^{2}}=\frac{2}{9} \times 10^{4} \frac{\mathrm{N}}{\mathrm{m}^{2}}=\frac{20}{9} \times 10^{3} \mathrm{~Pa}=2.222 \mathrm{kPa}
$$

We can also find shear stress and strain, respectively:

$$
\begin{aligned}
& \frac{F_{\|}}{A}=\frac{50.0 \mathrm{~N}}{2700.0 \mathrm{~cm}^{2}}=\frac{5}{27} \mathrm{kPa}=185.2 \mathrm{~Pa} \\
& \frac{\Delta x}{L_{0}}=\frac{15.0 \mathrm{~cm}}{180.0 \mathrm{~cm}}=\frac{1}{12}=0.083
\end{aligned}
$$

## Significance

If the person in this example gave the shelf a healthy push, it might happen that the induced shear would collapse it to a pile of rubbish. Much the same shear mechanism is responsible for failures of earth-filled dams and levees; and, in general, for landslides.

### 12.4 Elasticity and Plasticity

We referred to the proportionality constant between stress and strain as the elastic modulus. But why do we call it that? What does it mean for an object to be elastic and how do we describe its behavior?

Elasticity is the tendency of solid objects and materials to return to their original shape after the external forces (load) causing a deformation are removed. An object is elastic when it comes back to its original size and shape when the load is no longer present. Physical reasons for elastic behavior vary among materials and depend on the microscopic structure of the material. For example, the elasticity of polymers and rubbers is caused by stretching polymer chains under an applied force. In contrast, the elasticity of metals is caused by resizing and reshaping the crystalline cells of the lattices (which are the material structures of metals) under the action of externally applied forces.

The two parameters that determine the elasticity of a material are its elastic modulus and its elastic limit. A high elastic modulus is typical for materials that are hard to deform; in other words, materials that require a high load to achieve a significant strain. An example is a steel band. A low elastic modulus is typical for materials that are easily deformed under a load; for example, a rubber band. If the stress under a load becomes too high, then when the load is removed, the material no longer comes back to its original shape and size, but relaxes to a different shape and size: The material becomes permanently deformed. The elastic limit is the stress value beyond which the material no longer behaves elastically but becomes permanently deformed.

Our perception of an elastic material depends on both its elastic limit and its elastic modulus. For example, all rubbers are characterized by a low elastic modulus and a high elastic limit; hence, it is easy to stretch them and the stretch is noticeably large. Among materials with identical elastic limits, the most elastic is the one with the lowest elastic modulus.

When the load increases from zero, the resulting stress is in direct proportion to strain in the way given by Equation 12.33, but only when stress does not exceed some limiting value. For stress values within this linear limit, we can describe elastic behavior in analogy with Hooke's law for a spring. According to Hooke's law, the stretch value of a spring under an applied force is directly proportional to the magnitude of the force. Conversely, the response force from the spring to an applied stretch is directly proportional to the stretch. In the same way, the deformation of a material under a load is directly proportional to the load, and, conversely, the resulting stress is directly proportional to strain. The linearity limit (or the proportionality limit) is the largest stress value beyond which stress is no longer proportional to strain. Beyond the linearity limit, the relation between stress and strain is no longer linear. When stress becomes larger than the linearity limit but still within the elasticity limit, behavior is still elastic, but the relation between stress and strain becomes nonlinear.

For stresses beyond the elastic limit, a material exhibits plastic behavior. This means the material deforms irreversibly and does not return to its original shape and size, even when the load is removed. When stress is gradually increased beyond the elastic limit, the material undergoes plastic deformation. Rubber-like materials show an increase in stress with the increasing strain, which means they become more difficult to stretch and, eventually, they reach a fracture point where they break. Ductile materials such as metals show a gradual decrease in stress with the increasing strain, which means they become easier to deform as stressstrain values approach the breaking point. Microscopic mechanisms responsible for plasticity of materials are different for different materials.

We can graph the relationship between stress and strain on a stress-strain diagram. Each material has its own characteristic strain-stress curve. A typical stress-strain diagram for a ductile metal under a load is shown in Figure 12.25. In this figure, strain is a fractional elongation (not drawn to scale). When the load is gradually
increased, the linear behavior (red line) that starts at the no-load point (the origin) ends at the linearity limit at point $H$. For further load increases beyond point $H$, the stress-strain relation is nonlinear but still elastic. In the figure, this nonlinear region is seen between points $H$ and $E$. Ever larger loads take the stress to the elasticity limit $E$, where elastic behavior ends and plastic deformation begins. Beyond the elasticity limit, when the load is removed, for example at $P$, the material relaxes to a new shape and size along the green line. This is to say that the material becomes permanently deformed and does not come back to its initial shape and size when stress becomes zero.

The material undergoes plastic deformation for loads large enough to cause stress to go beyond the elasticity limit at $E$. The material continues to be plastically deformed until the stress reaches the fracture point (breaking point). Beyond the fracture point, we no longer have one sample of material, so the diagram ends at the fracture point. For the completeness of this qualitative description, it should be said that the linear, elastic, and plasticity limits denote a range of values rather than one sharp point.

The value of stress at the fracture point is called breaking stress (or ultimate stress). Materials with similar elastic properties, such as two metals, may have very different breaking stresses. For example, ultimate stress for aluminum is $2.2 \times 10^{8} \mathrm{~Pa}$ and for steel it may be as high as $20.0 \times 10^{8} \mathrm{~Pa}$, depending on the kind of steel. We can make a quick estimate, based on Equation 12.34, that for rods with a $1-\mathrm{in}^{2}$ cross-sectional area, the breaking load for an aluminum rod is $3.2 \times 10^{4} \mathrm{lb}$, and the breaking load for a steel rod is about nine times larger.

