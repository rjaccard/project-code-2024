## Rigid body kinematics and dynamics

In chapter 2, we established the material point kinematics and dynamics. In this chapter we will extend this model and consider the rigid body kinematics and dynamics. The first section is devoted to the rigid body kinematics and the second section is devoted to the rigid body dynamics. The last section is devoted to the inertia tensor and to the Euler equations.

### 12.1 Rigid body kinematics

In chapter 2, we defined the material point model. In this model, we ascribe the whole mass of an object to a point that corresponds to the centre of mass of the object. The kinematics and the dynamics of the object are entirely determined by the motion of the material point. In other words, we do not account for the orientation change of the object during its motion, which means that we ignore or neglect the intrinsic rotational motion of the object on itself around an axis passing through its centre of mass. It is the reason why we introduce now a more general model that takes into account the orientation of the rigid body over time. This model is the rigid body (Fig. 12.1).

### 12.1.1 Rigid body

A rigid body is a system consisting of a set of material points where the relative distances between the points are constant. Since the distances are constant, the volume or the shape of the rigid body do not change, only the spatial orientation of the rigid body changes. The frames of reference are rigid bodies. The elastic and plastic deformations of solids are studied in material science, which goes way beyond this course.

Theorem 12.16 coordinates are necessary to determine entirely the position and orientation of a rigid body of a given shape with respect to a given frame of reference.

Demonstration A rigid body can be considered as a frame of reference. Thus, we can completely determine the position and orientation of a rigid body using 4 non-coplanar material points. We can thus consider a regular tetrahedron with edges of length $r$ where the vertices are the material points $A, B, C$ and $D$, which implies that there is a distance $r$ between each couple of points. The respective orientation of points $A, B, C$ and $D$ is chosen such that $(\boldsymbol{A} \boldsymbol{B} \times \boldsymbol{A} \boldsymbol{C}) \cdot \boldsymbol{A} \boldsymbol{D}>0$.

To determine the position of point $A, 3$ coordinates are needed, for instance Cartesian coordinates. The material point $B$ is located on the sphere of radius $r$ centred on point $A$. 2 additional coordinates are needed to determine the position of point $B$, for instance two angles. The material point $C$ is located on the circle of radius obtained by intersection of the two spheres of radius $r$ centred on $A$ and $B$. A priori, there are two possible points on either side of plane $A B C$. However, the respective orientation condition of the material points $A$, $B, C$ and $D$ determines on which side of the plane $A B C$ the point $D$ is located. The point $D$ is thus entirely determined once the position of the points $A, B, C$ and $D$ is known. 6 coordinates are thus needed to determine the position and orientation of a rigid body with respect to a given frame of reference.

### 12.1.2 Euler angles

The orientation of a rigid body can be identified by particular angles called Euler angles. To determine these angles, we consider a Cartesian frame $\left(O, \hat{\boldsymbol{x}}_{1}, \hat{\boldsymbol{x}}_{2}, \hat{\boldsymbol{x}}_{3}\right)$ associated to the inertial frame and a Cartesian frame $\left(O, \hat{\boldsymbol{y}}_{1}, \hat{\boldsymbol{y}}_{2}, \hat{\boldsymbol{y}}_{3}\right)$ associated to the non-inertial frame of the rigid body rotating around point $O$. The Euler angles are defined as three rotation angles $(\phi, \theta, \psi)$ that bring the Cartesian frame $\left(O, \hat{\boldsymbol{x}}_{1}, \hat{\boldsymbol{x}}_{2}, \hat{\boldsymbol{x}}_{3}\right)$ on the Cartesian frame $\left(O, \hat{\boldsymbol{y}}_{1}, \hat{\boldsymbol{y}}_{2}, \hat{\boldsymbol{y}}_{3}\right)$.

The first Euler angle is the precession angle $\phi$ around the vertical axis $O x_{3}$ that brings the horizontal axis $O x_{1}$ on the nodal axis $O u$ (Fig. 12.3a). The second angle is the nutation angle $\theta$ around the nodal axis $O u$ that brings the vertical axis $O x_{3}$ on the axis $O y_{3}$ (Fig. 12.3b). The third Euler angle is the intrinsic rotation angle $\phi$ around the rotation axis $O y_{3}$ that brings the axis $O u$ on the axis $O y_{1}$ and the axis $O v$ on the axis $O y_{2}$ (Fig. 12.3c).

In general, rotations do not additive because they are linear applications of basis vector represented by $3 \times 3$ matrices that do not commute. However, the infinitesimal rotations always commute. The angular velocity vector $\boldsymbol{\Omega}$ of the rigid body with respect to an inertial frame is defined using the Poisson's formulae (10.18) - describing the evolution of infinitesimal rotations - yielding the time derivatives of the basis vectors of the frame attached to the rigid body. Thus, the angular velocity of the rigid body $\boldsymbol{\Omega}$ - that is a non-inertial frame - with respect to the inertial frame can be expressed as the sum of three angular velocity vectors where the norm is the time derivative of an Euler angle and where the orientation is given by the corresponding rotation axis,

$$
\begin{equation*}
\boldsymbol{\Omega}=\dot{\boldsymbol{\phi}}+\dot{\boldsymbol{\theta}}+\dot{\boldsymbol{\psi}}=\dot{\phi} \hat{\boldsymbol{x}}_{3}+\dot{\theta} \hat{\boldsymbol{u}}+\dot{\psi} \hat{\boldsymbol{y}}_{3} \tag{12.1}
\end{equation*}
$$

The vector $\dot{\boldsymbol{\phi}}$ is the precession angular velocity of the rigid body around the vertical axis $O x_{3}$. The vector $\dot{\boldsymbol{\theta}}$ is the nutation angular velocity of the rigid body around the nodal axis $O u$ and the vector $\dot{\psi}$ is the angular velocity of the intrinsic rotation of the rigid body around the intrinsic rotation axis $\mathrm{Oy}_{3}$.

These motions of precession, nutation and intrinsic rotation are well illustrated by the gyroscope consisting of a sphere on an air cushion (Fig. 12.4).

As other illustrations of these motions, we can mention the Chinese spinning top, that can turn its head by nutation, and the Euler disk where the angular velocity of the point of contact with the horizontal surface diverges when it stops (Fig. 12.5).

A variant of the Euler angles known as Tait-Bryan angles is used in aeronautics. The precession axis is called the $\boldsymbol{y a w}$ axis, the nutation axis is the pitch axis and the intrinsic rotation axis is called the roll axis (Fig. 12.6).

### 12.1.3 Velocity and acceleration of a rigid body

We consider a Cartesian frame $\left(O, \hat{\boldsymbol{x}}_{1}, \hat{\boldsymbol{x}}_{2}, \hat{\boldsymbol{x}}_{3}\right)$ associated to the absolute inertial frame of reference that is at rest and a Cartesian frame $\left(A, \hat{\boldsymbol{y}}_{1}, \hat{\boldsymbol{y}}_{2}, \hat{\boldsymbol{y}}_{3}\right)$ associated to the relative frame of reference of a rigid body that is rotating at angular velocity $\boldsymbol{\Omega}$ with respect to the absolute frame of reference (Fig. 10.5). We would like to express the velocity of an arbitrary material point $P$ of the rigid body in terms of the velocity of the material point $A$ at the origin of the frame and the angular velocity $\boldsymbol{\Omega}$ that accounts for the change of orientation of the rigid body with respect to the inertial frame of reference. Since the system is a rigid body and the material point $P$ belong to the rigid body, its relative velocity and its relative acceleration vanish,

$$
\begin{equation*}
\boldsymbol{v}_{r}(P)=\mathbf{0} \quad \text { and } \quad \boldsymbol{a}_{r}(P)=\mathbf{0} \tag{12.2}
\end{equation*}
$$

To simplify the writing, we denote the relative position of point $P$ and the absolute velocities and accelerations of points $A$ and $P$ as,

$$
\begin{equation*}
\boldsymbol{A} \boldsymbol{P} \equiv \boldsymbol{r}_{r}(P) \quad \boldsymbol{V}_{A} \equiv \boldsymbol{v}_{a}(A) \quad \boldsymbol{V}_{P} \equiv \boldsymbol{v}_{a}(P) \quad \boldsymbol{A}_{A} \equiv \boldsymbol{a}_{a}(A) \quad \boldsymbol{A}_{P} \equiv \boldsymbol{a}_{a}(P) \tag{12.3}
\end{equation*}
$$

Taking into account the conditions (12.2) and the notation (12.3), the identity between the velocities (10.24) - obtained in the framework of relative motion - for a rigid body reduces to,

$$
\begin{equation*}
\boldsymbol{V}_{P}=\boldsymbol{V}_{A}+\boldsymbol{\Omega} \times \boldsymbol{A} \boldsymbol{P} \tag{12.4}
\end{equation*}
$$

Theorem 12.2 The velocities $\boldsymbol{V}_{P}$ and $\boldsymbol{V}_{Q}$ of arbitrary material points $P$ and $Q$ that belong to the rigid body satisfy the relation,

$$
\begin{equation*}
\boldsymbol{V}_{Q}=\boldsymbol{V}_{P}+\boldsymbol{\Omega} \times \boldsymbol{P} \boldsymbol{Q} \tag{12.5}
\end{equation*}
$$

Demonstration Taking into account the identity (12.4), since the point $Q$ is an arbitrary
point of the rigid body like point $P$, this implies that,

$$
\begin{equation*}
\boldsymbol{V}_{Q}=\boldsymbol{V}_{A}+\boldsymbol{\Omega} \times \boldsymbol{A} \boldsymbol{Q} \tag{12.6}
\end{equation*}
$$

The difference between relations (12.6) and (12.4) is written,

$$
\begin{equation*}
\boldsymbol{V}_{Q}-\boldsymbol{V}_{P}=\boldsymbol{\Omega} \times(\boldsymbol{A} \boldsymbol{Q}-\boldsymbol{A} \boldsymbol{P})=\boldsymbol{\Omega} \times \boldsymbol{P} \boldsymbol{Q} \tag{12.7}
\end{equation*}
$$

Taking into account the conditions (12.2) and the notation (12.3), the identity between the accelerations (10.37) for a rigid body reduces to,

$$
\begin{equation*}
\boldsymbol{A}_{P}=\boldsymbol{A}_{A}+\boldsymbol{\Omega} \times(\boldsymbol{\Omega} \times \boldsymbol{A} \boldsymbol{P})+\dot{\boldsymbol{\Omega}} \times \boldsymbol{A} \boldsymbol{P} \tag{12.8}
\end{equation*}
$$

Theorem 12.3 The accelerations $\boldsymbol{A}_{P}$ and $\boldsymbol{A}_{Q}$ of arbitrary material points $P$ and $Q$ that belong to the rigid body satisfy the relation,

$$
\begin{equation*}
\boldsymbol{A}_{Q}=\boldsymbol{A}_{P}+\boldsymbol{\Omega} \times(\boldsymbol{\Omega} \times \boldsymbol{P Q})+\dot{\boldsymbol{\Omega}} \times \boldsymbol{P} \boldsymbol{Q} \tag{12.9}
\end{equation*}
$$

Demonstration Taking into account the identity (12.8), since point $Q$ is an arbitrary material point of the rigid body like point $P$, this implies that,

$$
\begin{equation*}
\boldsymbol{A}_{Q}=\boldsymbol{A}_{A}+\boldsymbol{\Omega} \times(\boldsymbol{\Omega} \times \boldsymbol{A} \boldsymbol{Q})+\dot{\boldsymbol{\Omega}} \times \boldsymbol{A} \boldsymbol{Q} \tag{12.10}
\end{equation*}
$$

The difference between relations (12.10) and (12.8) is written,

$$
\begin{align*}
\boldsymbol{A}_{Q}-\boldsymbol{A}_{P} & =\boldsymbol{\Omega} \times(\boldsymbol{\Omega} \times(\boldsymbol{A} \boldsymbol{Q}-\boldsymbol{A} \boldsymbol{P}))+\dot{\boldsymbol{\Omega}} \times(\boldsymbol{A} \boldsymbol{Q}-\boldsymbol{A} \boldsymbol{P})  \tag{12.11}\\
& =\boldsymbol{\Omega} \times(\boldsymbol{\Omega} \times \boldsymbol{P} \boldsymbol{Q})+\dot{\boldsymbol{\Omega}} \times \boldsymbol{P} \boldsymbol{Q}
\end{align*}
$$

### 12.1.4 Rolling without slipping

On a practical level, we are often confronted to rigid bodies that roll on a horizontal surface or on an inclined plane. These rigid bodies are in general cylinders or spheres. The kinematics of this rolling motion can be described in the vertical plane that goes through the centre of mass $G$ of the object. In this plane, the section of the object is a circle. The material point $C$ is the point of contact between the circle and the surface (Fig. 12.7).

If the rigid body slips without rolling, the velocity of the point of contact $\boldsymbol{V}_{C}$ has to be equal to the velocity of the centre of mass $\boldsymbol{V}_{G}$. If the rigid body slips and rolls, the velocity of the point of contact $\boldsymbol{V}_{C}$ and the velocity of the centre of mass $\boldsymbol{V}_{G}$ do not vanish, but they are not equal due to the rolling motion of the rigid body. If the rigid body rolls without slipping, the velocity of the point of contact $\boldsymbol{V}_{C}$ vanishes but the velocity of the centre of mass $\boldsymbol{V}_{G}$ does not vanish due to the rolling. Thus, according to the relation (12.5), the condition of rolling without slipping (12.5) is written explicitly,

$$
\begin{equation*}
\boldsymbol{V}_{G}=\boldsymbol{\Omega} \times \boldsymbol{C} \boldsymbol{G} \quad \text { since } \quad \boldsymbol{V}_{C}=\mathbf{0} \tag{12.12}
\end{equation*}
$$

When the rigid body rolls, the material point that corresponds to the point of contact $C$ between the rigid body and the surface changes over time during a rolling motion without slipping, but at each moment the velocity $\boldsymbol{V}_{C}$ of this point vanishes.

### 12.2 Rigid body dynamics

Since a rigid body is a set of points where the relative distances are fixed, the momentum theorem (11.62) and the centre of mass theorem (11.64) for a rigid body are identical to those obtained for a closed system of material points,

$$
\begin{equation*}
\boldsymbol{F}^{\mathrm{ext}}=\frac{d \boldsymbol{P}}{d t} \quad \text { and } \quad \boldsymbol{F}^{\mathrm{ext}}=M \boldsymbol{A}_{G} \tag{12.13}
\end{equation*}
$$

Similarly, with respect to a fixed point $O$ of the frame of reference, i.e. $\boldsymbol{V}_{O}=\mathbf{0}$, the momentum theorem (11.66) for a rigid body is identical to the one obtained for a closed system of material points,

$$
\begin{equation*}
\boldsymbol{\tau}_{O}^{\mathrm{ext}}=\frac{d \boldsymbol{L}_{O}}{d t} \tag{12.14}
\end{equation*}
$$

The angular momentum theorem (12.14) depends on the point with respect to which the angular moment and the net torque are evaluated. Now, we would like to generalise this theorem to an arbitrary point $P$ that belongs to the rigid body and in particular to the centre of mass $G$. In order to do so, we first have to establish the angular momentum and net torque transfer theorems.

### 12.2.1 Angular momentum transfer theorem and first König theorem

Theorem 12.4 The angular momentum transfer theorem states that the angular momentum theorem $\boldsymbol{L}_{P}$ of a rigid body evaluated with respect to an arbitrary point $P$ of the rigid body is expressed in terms of the angular momentum $\boldsymbol{L}_{O}$ of the rigid body evaluated with respect to a fixed point $O$ of the frame of reference as,

$$
\begin{equation*}
\boldsymbol{L}_{P}=\boldsymbol{P} \boldsymbol{O} \times M \boldsymbol{V}_{G}+\boldsymbol{L}_{O} \tag{12.15}
\end{equation*}
$$

Demonstration Taking into account expressions (11.52), (11.59) and (11.60)

$$
\begin{align*}
\boldsymbol{L}_{P} & =\sum_{\alpha} \boldsymbol{P} \boldsymbol{P}_{\alpha} \times \boldsymbol{p}_{\alpha}=\sum_{\alpha}\left(\boldsymbol{P} \boldsymbol{O}+\boldsymbol{O} \boldsymbol{P}_{\alpha}\right) \times \boldsymbol{p}_{\alpha} \\
& =\boldsymbol{P} \boldsymbol{O} \times \boldsymbol{P}+\sum_{\alpha} \boldsymbol{O} \boldsymbol{P}_{\alpha} \times \boldsymbol{p}_{\alpha}=\boldsymbol{P} \boldsymbol{O} \times M \boldsymbol{V}_{G}+\boldsymbol{L}_{O} \tag{12.16}
\end{align*}
$$

For the centre of mass $G$, the angular momentum transfer theorem (12.15) is called the first König theorem and is written,

$$
\begin{equation*}
\boldsymbol{L}_{O}=\boldsymbol{O} \boldsymbol{G} \times M \boldsymbol{V}_{G}+\boldsymbol{L}_{G} \tag{12.17}
\end{equation*}
$$

Johann Samuel

Koenig
Theorem 12.5 The angular momentum $\boldsymbol{L}_{P}$ of the rigid body, evaluated with respect to an arbitrary point $P$ of the rigid body, is expressed in terms of the angular momentum $\boldsymbol{L}_{G}$ of the rigid body evaluated with respect to the centre of mass $G$ as,

$$
\begin{equation*}
\boldsymbol{L}_{P}=\boldsymbol{P} G \times M \boldsymbol{V}_{G}+\boldsymbol{L}_{G} \tag{12.18}
\end{equation*}
$$

Demonstration Substituting the expression (12.17) of the angular momentum $\boldsymbol{L}_{O}$ into the expression (12.15) of the angular momentum $\boldsymbol{L}_{P}$, we obtain,

$$
\begin{equation*}
\boldsymbol{L}_{P}=(\boldsymbol{P} \boldsymbol{O}+\boldsymbol{O} \boldsymbol{G}) \times M \boldsymbol{V}_{G}+\boldsymbol{L}_{G}=\boldsymbol{P} \boldsymbol{G} \times M \boldsymbol{V}_{G}+\boldsymbol{L}_{G} \tag{12.19}
\end{equation*}
$$

### 12.2.2 Torque transfer theorem

Theorem 12.6 The torque transfer theorem states that the net external torque $\boldsymbol{\tau}_{P}^{\text {ext }}$ evaluated with respect to an arbitrary point $P$ of the rigid body is expressed in terms of the net torque $\boldsymbol{\tau}_{O}^{\text {ext }}$ evaluated with respect to a fixed point $O$ of the frame of reference as,

$$
\begin{equation*}
\boldsymbol{\tau}_{P}^{e x t}=\boldsymbol{P} \boldsymbol{O} \times M \boldsymbol{A}_{G}+\boldsymbol{\tau}_{O}^{e x t} \tag{12.20}
\end{equation*}
$$

Demonstration Taking into account expressions (11.54), (11.61) and (11.64)

$$
\begin{align*}
\boldsymbol{\tau}_{P}^{\mathrm{ext}} & =\sum_{\alpha} \boldsymbol{P} \boldsymbol{P}_{\alpha} \times \boldsymbol{F}_{\alpha}^{\mathrm{ext}}=\sum_{\alpha}\left(\boldsymbol{P} \boldsymbol{O}+\boldsymbol{O} \boldsymbol{P}_{\alpha}\right) \times \boldsymbol{F}_{\alpha}^{\mathrm{ext}}  \tag{12.21}\\
& =\boldsymbol{P} \boldsymbol{O} \times \boldsymbol{F}^{\mathrm{ext}}+\sum_{\alpha} \boldsymbol{O} \boldsymbol{P}_{\alpha} \times \boldsymbol{F}_{\alpha}^{\mathrm{ext}}=\boldsymbol{P} \boldsymbol{O} \times M \boldsymbol{A}_{G}+\boldsymbol{\tau}_{O}^{\mathrm{ext}}
\end{align*}
$$

For the centre of mass $G$, the torque transfer theorem (12.20) is written,

$$
\begin{equation*}
\boldsymbol{\tau}_{O}^{\mathrm{ext}}=\boldsymbol{O} \boldsymbol{G} \times M \boldsymbol{A}_{G}+\boldsymbol{\tau}_{G}^{\text {ext }} \tag{12.22}
\end{equation*}
$$

Theorem 12.7 The net external torque $\boldsymbol{\tau}_{P}^{\text {ext }}$ evaluated with respect to an arbitrary point $P$ of the rigid body is expressed in terms of the net external torque $\boldsymbol{\tau}_{G}^{\text {ext }}$ evaluated with respect to the centre of mass $G$ as,

$$
\begin{equation*}
\boldsymbol{\tau}_{P}^{e x t}=\boldsymbol{P} \boldsymbol{G} \times M \boldsymbol{A}_{G}+\boldsymbol{\tau}_{G}^{e x t} \tag{12.23}
\end{equation*}
$$

Demonstration Substituting the expression (12.22) of the net external torque $\boldsymbol{\tau}_{O}^{\text {ext }}$ into the expression (12.20) of the net external torque $\boldsymbol{\tau}_{P}^{\text {ext }}$, we obtain,

$$
\begin{equation*}
\boldsymbol{\tau}_{P}^{\text {ext }}=(\boldsymbol{P} \boldsymbol{O}+\boldsymbol{O} \boldsymbol{G}) \times M \boldsymbol{A}_{G}+\boldsymbol{\tau}_{G}^{\text {ext }}=\boldsymbol{P} \boldsymbol{G} \times M \boldsymbol{A}_{G}+\boldsymbol{\tau}_{G}^{\text {ext }} \tag{12.24}
\end{equation*}
$$

### 12.2.3 Angular momentum theorem with respect to a point of the rigid body

The time derivative of the angular momentum transfer theorem (12.15) is written,

$$
\begin{align*}
\frac{d \boldsymbol{L}_{P}}{d t} & =-\frac{d \boldsymbol{O} \boldsymbol{P}}{d t} \times M \boldsymbol{V}_{G}+\boldsymbol{P} \boldsymbol{O} \times M \frac{d \boldsymbol{V}_{G}}{d t}+\frac{d \boldsymbol{L}_{O}}{d t}  \tag{12.25}\\
& =-\boldsymbol{V}_{P} \times M \boldsymbol{V}_{G}+\boldsymbol{P} \boldsymbol{O} \times M \boldsymbol{A}_{G}+\frac{d \boldsymbol{L}_{O}}{d t}
\end{align*}
$$

because $\boldsymbol{V}_{P}=d \boldsymbol{O} \boldsymbol{P} / d t$ and $\boldsymbol{A}_{G}=d \boldsymbol{V}_{G} / d t$. Substituting the expressions (12.20) and (12.25) into the angular momentum theorem evaluated with respect to point $O$, we obtain the angular momentum theorem evaluated with respect to point $P$ that belongs to the rigid body,

$$
\begin{equation*}
\boldsymbol{\tau}_{P}^{\mathrm{ext}}=\frac{d \boldsymbol{L}_{P}}{d t}+\boldsymbol{V}_{P} \times M \boldsymbol{V}_{G} \tag{12.26}
\end{equation*}
$$

For the centre of mass $G$, the angular momentum theorem (12.26) reduces to,

$$
\begin{equation*}
\boldsymbol{\tau}_{G}^{\mathrm{ext}}=\frac{d \boldsymbol{L}_{G}}{d t} \tag{12.27}
\end{equation*}
$$

### 12.3 Inertia tensor and Euler equations

The momentum of the rigid body $\boldsymbol{P}$ is related to the velocity of the centre of mass $\boldsymbol{V}_{G}$ by the phenomenological relation (11.60),

$$
\begin{equation*}
\boldsymbol{P}=M \boldsymbol{V}_{G} \tag{12.28}
\end{equation*}
$$

where the mass $M$ of the rigid body is the proportionality constant between the collinear velocities $\boldsymbol{P}$ and $\boldsymbol{V}_{G}$. We would like to find a similar phenomenological relation to relate the angular momentum of the rigid body $\boldsymbol{L}_{G}$, evaluated with respect to its centre of mass $G$, to its rotational angular velocity $\boldsymbol{\Omega}$. In the general case, the angular momentum vector $\boldsymbol{L}_{G}$ is not necessarily collinear to the vector $\boldsymbol{\Omega}$. These vectors are related by a linear application called the inertia tensor $\mathrm{I}_{G}$ of the rigid body with respect to its centre of mass, that is represented by a $3 \times 3$ matrix. Thus, the phenomenological relation is written,

$$
\begin{equation*}
\boldsymbol{L}_{G}=\mathrm{I}_{G} \boldsymbol{\Omega} \tag{12.29}
\end{equation*}
$$

On a formal level, a tensor is a linear application that transforms in a particular manner under a change of frame of reference.

Theorem 12.8 The angular momentum of the rigid body $\boldsymbol{L}_{G}$, evaluated with respect to its centre of mass $G$, can be recast as,

$$
\begin{equation*}
\boldsymbol{L}_{G}=\sum_{\alpha} m_{\alpha} \boldsymbol{G} \boldsymbol{P}_{\alpha} \times\left(\boldsymbol{\Omega} \times \boldsymbol{G} \boldsymbol{P}_{\alpha}\right) \tag{12.30}
\end{equation*}
$$

Demonstration The identity between the velocities (12.5) for an arbitrary material point $P_{\alpha}$ that belongs to the rigid body and the centre of mass of the rigid body $G$ is written,

$$
\begin{equation*}
\boldsymbol{v}_{\alpha}=\boldsymbol{V}_{G}+\boldsymbol{\Omega} \times \boldsymbol{G} \boldsymbol{P}_{\alpha} \tag{12.31}
\end{equation*}
$$

Taking into account the expressions (11.39), (11.42), (11.51), (11.52) and (11.59), the angular momentum of the rigid body $\boldsymbol{L}_{G}$, evaluated with respect to its centre of mass $G$, is written,

$$
\begin{align*}
\boldsymbol{L}_{G} & =\sum_{\alpha} \boldsymbol{G} \boldsymbol{P}_{\alpha} \times \boldsymbol{p}_{\alpha}=\sum_{\alpha} \boldsymbol{G} \boldsymbol{P}_{\alpha} \times m_{\alpha} \boldsymbol{v}_{\alpha}=\sum_{\alpha} \boldsymbol{G} \boldsymbol{P}_{\alpha} \times m_{\alpha}\left(\boldsymbol{V}_{G}+\boldsymbol{\Omega} \times \boldsymbol{G} \boldsymbol{P}_{\alpha}\right) \\
& =\sum_{\alpha} m_{\alpha} \boldsymbol{r}_{\alpha}^{\prime} \times \boldsymbol{V}_{G}+\sum_{\alpha} m_{\alpha} \boldsymbol{G} \boldsymbol{P}_{\alpha} \times\left(\boldsymbol{\Omega} \times \boldsymbol{G} \boldsymbol{P}_{\alpha}\right)=\sum_{\alpha} m_{\alpha} \boldsymbol{G} \boldsymbol{P}_{\alpha} \times\left(\boldsymbol{\Omega} \times \boldsymbol{G} \boldsymbol{P}_{\alpha}\right) \tag{12.32}
\end{align*}
$$

### 12.3.1 Inertia tensor

According to the vectorial identity (1.43), the expression (12.30) of the angular momentum $\boldsymbol{L}_{G}$ can be recast according to,

$$
\begin{equation*}
\boldsymbol{L}_{G}=\sum_{\alpha} m_{\alpha}\left(\boldsymbol{G} \boldsymbol{P}_{\alpha}^{2} \boldsymbol{\Omega}-\left(\boldsymbol{G} \boldsymbol{P}_{\alpha} \cdot \boldsymbol{\Omega}\right) \boldsymbol{G} \boldsymbol{P}_{\alpha}\right) \tag{12.33}
\end{equation*}
$$

To determine the expression of the inertia tensor $\mathrm{I}_{G}$, we will now project the angular momentum $\boldsymbol{L}_{G}$ along the basis vectors $\left(\hat{\boldsymbol{y}}_{1}, \hat{\boldsymbol{y}}_{2}, \hat{\boldsymbol{y}}_{3}\right)$ of the Cartesian frame attached to the rigid body. The decomposition of the vector $\boldsymbol{\Omega}$ in this basis reads,

$$
\begin{equation*}
\boldsymbol{\Omega}=\sum_{j=1}^{3}\left(\boldsymbol{\Omega} \cdot \hat{\boldsymbol{y}}_{j}\right) \hat{\boldsymbol{y}}_{j} \tag{12.34}
\end{equation*}
$$

Taking into account the decomposition (12.34), the projection of the angular momentum $\boldsymbol{L}_{G}$ along the basis vector $\hat{\boldsymbol{y}}_{i}$ is written,

$$
\begin{align*}
\boldsymbol{L}_{G} \cdot \hat{\boldsymbol{y}}_{i} & =\sum_{\alpha} m_{\alpha}\left(\boldsymbol{G} \boldsymbol{P}_{\alpha}^{2}\left(\boldsymbol{\Omega} \cdot \hat{\boldsymbol{y}}_{i}\right)-\left(\boldsymbol{G} \boldsymbol{P}_{\alpha} \cdot \boldsymbol{\Omega}\right)\left(\boldsymbol{G} \boldsymbol{P}_{\alpha} \cdot \hat{\boldsymbol{y}}_{i}\right)\right) \\
& =\sum_{j=1}^{3} \sum_{\alpha} m_{\alpha}\left(\boldsymbol{G} \boldsymbol{P}_{\alpha}^{2}\left(\hat{\boldsymbol{y}}_{i} \cdot \hat{\boldsymbol{y}}_{j}\right)-\left(\boldsymbol{G} \boldsymbol{P}_{\alpha} \cdot \hat{\boldsymbol{y}}_{i}\right)\left(\boldsymbol{G} \boldsymbol{P}_{\alpha} \cdot \hat{\boldsymbol{y}}_{j}\right)\right)\left(\boldsymbol{\Omega} \cdot \hat{\boldsymbol{y}}_{j}\right) \\
& =\hat{\boldsymbol{y}}_{i} \cdot \sum_{j=1}^{3}\left(\sum_{\alpha} m_{\alpha}\left(\boldsymbol{G} \boldsymbol{P}_{\alpha}^{2} \mathbb{1}-\boldsymbol{G} \boldsymbol{P}_{\alpha} \otimes \boldsymbol{G} \boldsymbol{P}_{\alpha}\right) \hat{\boldsymbol{y}}_{j}\right)\left(\boldsymbol{\Omega} \cdot \hat{\boldsymbol{y}}_{j}\right)  \tag{12.35}\\
& \equiv \hat{\boldsymbol{y}}_{i} \cdot \sum_{j=1}^{3}\left(\mathrm{l}_{G} \hat{\boldsymbol{y}}_{j}\right)\left(\boldsymbol{\Omega} \cdot \hat{\boldsymbol{y}}_{j}\right)=\left(\mathrm{I}_{G} \boldsymbol{\Omega}\right) \cdot \hat{\boldsymbol{y}}_{i}
\end{align*}
$$

where $\mathbb{1}$ is the linear application identity that sends every vector on itself and the symbol $\otimes$ represents a tensor product. The inertia tensor $\mathrm{I}_{G}$ of the rigid body with respect to the centre of mass $G$ is written formally,

$$
\begin{equation*}
\mathrm{I}_{G}=\sum_{\alpha} m_{\alpha}\left(\boldsymbol{G} \boldsymbol{P}_{\alpha}^{2} \mathbb{1}-\boldsymbol{G} \boldsymbol{P}_{\alpha} \otimes \boldsymbol{G} \boldsymbol{P}_{\alpha}\right) \tag{12.36}
\end{equation*}
$$

The phenomenological relation (12.35) is written in components as,

$$
\begin{equation*}
L_{G, i}=\sum_{j=1}^{3} I_{G, i j} \Omega_{j} \tag{12.37}
\end{equation*}
$$

where the components $I_{G, i j}$ of the inertia tensor $I_{G}$ with respect to the basis $\left(\hat{\boldsymbol{y}}_{1}, \hat{\boldsymbol{y}}_{2}, \hat{\boldsymbol{y}}_{3}\right)$ are written,

$$
\begin{equation*}
I_{G, i j}=\sum_{\alpha} m_{\alpha}\left(\sum_{k=1}^{3} G P_{\alpha, k}^{2} \delta_{i j}-G P_{\alpha, i} G P_{\alpha, j}\right) \tag{12.38}
\end{equation*}
$$

The diagonal components $I_{G, 11}, I_{G, 22}$ and $I_{G, 33}$ of the inertia tensor $\mathrm{I}_{G}$ are written,

$$
\begin{align*}
& I_{G, 11}=\sum_{\alpha} m_{\alpha}\left(G P_{\alpha, 2}^{2}+G P_{\alpha, 3}^{2}\right) \equiv \sum_{\alpha} m_{\alpha} r_{\alpha, 23}^{2} \\
& I_{G, 22}=\sum_{\alpha} m_{\alpha}\left(G P_{\alpha, 3}^{2}+G P_{\alpha, 1}^{2}\right) \equiv \sum_{\alpha} m_{\alpha} r_{\alpha, 31}^{2}  \tag{12.39}\\
& I_{G, 33}=\sum_{\alpha} m_{\alpha}\left(G P_{\alpha, 1}^{2}+G P_{\alpha, 2}^{2}\right) \equiv \sum_{\alpha} m_{\alpha} r_{\alpha, 12}^{2}
\end{align*}
$$

where $r_{\alpha, 23}^{2}$ is the distance between the point $P_{\alpha}$ and the axis $G y_{1}, r_{\alpha, 31}^{2}$ is the distance between this point and the axis $G y_{2}$ and $r_{\alpha, 12}^{2}$ is the distance between this point and the axis $G y_{3}($ Fig 12.8).

### 12.3.2 Moments of inertia and principal axes

The components $I_{G, i j}$ of the inertia tensor are the elements of a symmetric $3 \times 3$ matrix with real coefficients, i.e. $I_{G, i j}=I_{G, j i}$. According to the spectral theorem of linear algebra, a symmetric matrix with real coefficients is diagonalisable. Thus, there is a vectors basis $\left(\boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3}\right)$ attached to the rigid body with respect to which the inertia tensor is diagonal. The Cartesian frame $\left(G, \boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3}\right)$ is called the principal axis frame and the axes $G e_{1}$, $G e_{2}, G_{3}$ are called the principal axes. With respect to the principal axis frame, the phenomenological relation (12.29) is written in components as,

$$
\left(\begin{array}{l}
L_{G, 1}  \tag{12.40}\\
L_{G, 2} \\
L_{G, 3}
\end{array}\right)=\left(\begin{array}{ccc}
I_{G, 1} & 0 & 0 \\
0 & I_{G, 2} & 0 \\
0 & 0 & I_{G, 3}
\end{array}\right)\left(\begin{array}{l}
\Omega_{1} \\
\Omega_{2} \\
\Omega_{3}
\end{array}\right)
$$

and vectorially as,

$$
\begin{equation*}
\boldsymbol{L}_{G}=\sum_{i=1}^{3} I_{G, i} \Omega_{i} \boldsymbol{e}_{i}=I_{G, 1} \Omega_{1} \boldsymbol{e}_{1}+I_{G, 2} \Omega_{2} \boldsymbol{e}_{2}+I_{G, 3} \Omega_{3} \boldsymbol{e}_{3} \tag{12.41}
\end{equation*}
$$

The eigenvalues of the inertia tensor $I_{G, 1}, I_{G, 2}$ and $I_{G, 3}$ are called the moments of inertia and the corresponding eigenvectors $\boldsymbol{e}_{1}, \boldsymbol{e}_{2} \boldsymbol{e}_{3}$ are the unit vectors along the principal axes. The moments of inertia are expressed as,

$$
\begin{equation*}
I_{G, 1}=\sum_{\alpha} m_{\alpha} r_{\alpha, 1}^{2} \quad I_{G, 2}=\sum_{\alpha} m_{\alpha} r_{\alpha, 2}^{2} \quad I_{G, 3}=\sum_{\alpha} m_{\alpha} r_{\alpha, 3}^{2} \tag{12.42}
\end{equation*}
$$

where $r_{\alpha, 1}^{2}$ is the distance between the point $P_{\alpha}$ and the principal axis $G e_{1}, r_{\alpha, 2}^{2}$ is the distance between this point and the principal axis $G e_{2}$ and $r_{\alpha, 3}^{2}$ is the distance between this point and the principal axis $G e_{3}$.

There are three types of homogeneous and regular rigid bodies. The first type is the ellipsoid for which the three moments of inertia are different. The second type is the cylinder for which the moment of inertia $I_{G \|}$ along the symmetry axis is different form the two moments of inertia $I_{G \perp}$ perpendicular to this axis that are equal. The third type is the sphere for which the three moments of inertia are equal (Fig. 12.9).

In the absence of net external torque with respect to the centre of mass $G$, i.e. $\boldsymbol{\tau}_{G}^{\text {ext }}=\mathbf{0}$, the angular momentum theorem implies that the angular momentum with respect to the centre of mass is conserved, i.e. $\boldsymbol{L}_{G}=$ const. If the rigid body has a rotational motion of angular velocity $\boldsymbol{\Omega}=\Omega_{3} \boldsymbol{e}_{3}$ around the vertical axis then the angular momentum (12.41) is expressed as $\boldsymbol{L}_{G}=I_{G, 3} \Omega_{3} \boldsymbol{e}_{3}$. Thus, if the moment of inertia $I_{G, 3}$ increases, the rotational angular velocity $\Omega_{3}$ decreases and vice versa. The moment of inertia increases if a part of the mass of the rigid body moves away from the axis. The ice skaters use this effect to accelerate or brake their rotational motion (Fig. 12.10).

### 12.3.3 Euler equations

The principal axis frame $\left(G, \boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3}\right)$ attached to the rigid body is a mobile frame. The time derivatives of the basis vectors satisfy Poisson's formulae,

$$
\begin{equation*}
\dot{\boldsymbol{e}}_{i}=\boldsymbol{\Omega} \times \boldsymbol{e}_{i} \quad \forall i=1,2,3 \tag{https://cdn.mathpix.com/cropped/2024_05_18_8fd7fb8affec5477e5d7g-10.jpg?height=45&width=112&top_left_y=2556&top_left_x=1760}
\end{equation*}
$$

For a rigid body, the moments of inertia are constant, i.e. $I_{G, i}=$ const. Taking into account Poisson's formulae (12.43), the time derivative of the angular momentum (12.41) is written,

$$
\begin{equation*}
\frac{d \boldsymbol{L}_{G}}{d t}=\sum_{i=1}^{3} I_{G, i} \dot{S}_{i} \boldsymbol{e}_{i}+\sum_{i=1}^{3} I_{G, i} \Omega_{i} \dot{e}_{i}=\sum_{i=1}^{3} I_{G, i} \dot{\Omega}_{i} \boldsymbol{e}_{i}+\boldsymbol{\Omega} \times\left(\sum_{i=1}^{3} I_{G, i} \Omega_{i} \boldsymbol{e}_{i}\right) \tag{12.44}
\end{equation*}
$$

In the particular case where the angular velocity is constant with respect to the principal axis frame, i.e. $\dot{\Omega}_{1}=\dot{\Omega}_{2}=\dot{\Omega}_{3}=0$, taking into account the expression (12.41) of the angular momentum, the relation (12.44) reduces to,

$$
\begin{equation*}
\frac{d \boldsymbol{L}_{G}}{d t}=\boldsymbol{\Omega} \times \boldsymbol{L}_{G} \tag{12.45}
\end{equation*}
$$

and describes the precession of the vector $\boldsymbol{L}_{G}$ around the vector $\boldsymbol{\Omega}$. In the general case, the relation (12.44) is recast as,

$$
\begin{align*}
\frac{d \boldsymbol{L}_{G}}{d t}= & I_{G, 1} \dot{\Omega}_{1} \boldsymbol{e}_{1}+I_{G, 2} \dot{\Omega}_{2} \boldsymbol{e}_{2}+I_{G, 3} \dot{\Omega}_{3} \boldsymbol{e}_{3} \\
& +\left(\Omega_{1} \boldsymbol{e}_{1}+\Omega_{2} \boldsymbol{e}_{2}+\Omega_{3} \boldsymbol{e}_{3}\right) \times\left(I_{G, 1} \Omega_{1} \boldsymbol{e}_{1}+I_{G, 2} \Omega_{2} \boldsymbol{e}_{2}+I_{G, 3} \Omega_{3} \boldsymbol{e}_{3}\right)  \tag{12.46}\\
= & I_{G, 1} \dot{\Omega}_{1} \boldsymbol{e}_{1}+I_{G, 2} \dot{\Omega}_{2} \boldsymbol{e}_{2}+I_{G, 3} \dot{\Omega}_{3} \boldsymbol{e}_{3}+\left(I_{G, 3}-I_{G, 2}\right) \Omega_{3} \Omega_{2} \boldsymbol{e}_{1} \\
& +\left(I_{G, 1}-I_{G, 3}\right) \Omega_{1} \Omega_{3} \boldsymbol{e}_{2}+\left(I_{G, 2}-I_{G, 1}\right) \Omega_{2} \Omega_{1} \boldsymbol{e}_{3}
\end{align*}
$$

The net external torque $\boldsymbol{\tau}_{G}^{\text {ext }}$ is decomposed in the principal axis frame as,

$$
\begin{equation*}
\boldsymbol{\tau}_{G}^{\mathrm{ext}}=\tau_{G, 1}^{\mathrm{ext}} \boldsymbol{e}_{1}+\tau_{G, 2}^{\mathrm{ext}} \boldsymbol{e}_{2}+\tau_{G, 3}^{\mathrm{ext}} \boldsymbol{e}_{3} \tag{12.47}
\end{equation*}
$$

Substituting expressions (12.46) and (12.47) into the angular momentum theorem (12.27) and projecting it then along the coordinate axes $G e_{1}, G e_{2}$ and $G e_{3}$, we obtain the Euler equations that determine the intrinsic rotational motion of the rigid body,

$$
\begin{align*}
\tau_{G, 1}^{\mathrm{ext}} & =I_{G, 1} \dot{\Omega}_{1}+\left(I_{G, 3}-I_{G, 2}\right) \Omega_{3} \Omega_{2} \\
\tau_{G, 2}^{\text {ext }} & =I_{G, 2} \dot{\Omega}_{2}+\left(I_{G, 1}-I_{G, 3}\right) \Omega_{1} \Omega_{3}  \tag{12.48}\\
\tau_{G, 3}^{\text {ext }} & =I_{G, 3} \dot{\Omega}_{3}+\left(I_{G, 2}-I_{G, 1}\right) \Omega_{2} \Omega_{1}
\end{align*}
$$

