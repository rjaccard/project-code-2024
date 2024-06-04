# 13 

## Rigid body with one fixed axis and gyroscopes

In chapter 12, we established the kinematics and the dynamics of rigid bodies. In the first section of this chapter, we shall compute explicitly the moments of inertia of certain rigid bodies with respect to a principal axis. The second section is devoted to the rigid body dynamics in rotation around a fixed axis. The third section is devoted to gyroscopes and to gyroscopic effects.

### 13.1 Moments of inertia

To compute the moment of inertia with respect to a principal axis, we assume that the material points $P_{\alpha}$ of the rigid body are sufficiently closed to each other to generate a continuum in a region of the three dimensional space that corresponds to the volume $V$ of the rigid body. In this case, the discrete sum of the definition (12.42) of the moment of inertia $I_{G, i}$ of the rigid body expressed with respect to an axis $G \boldsymbol{e}_{i}$ that goes through the centre of mass $G$ becomes an integral over the volume $V$ of the rigid body,

$$
\begin{equation*}
I_{G, i}=\sum_{\alpha} m_{\alpha} r_{\alpha, i}^{2} \quad \longrightarrow \quad I_{G, i}=\int_{V} d m r^{2} \tag{13.1}
\end{equation*}
$$

where $m_{\alpha}$ is the mass and $r_{\alpha, i}$ is the distance from the material point $P_{\alpha}$ to the axis of rotation $G \boldsymbol{e}_{i}$, and $d m_{\alpha}$ is the mass of an infinitesimal volume $d V$ of the rigid body and $r$ is the distance to the axis of rotation $G \boldsymbol{e}_{i}$.

Using the integral expression (13.1), we are now going to compute explicitly the moment of inertia of several regular rigid bodies. The regular rigid bodies are a thin rod, a hollow cylinder and a full cylinder.

### 13.1.1 Thin rod

We consider a homogeneous and very thin rod of mass $M$ such that its thickness $e$ is negligible with respect to its length $L$, i.e. $e \ll L$. Thus, we can consider that the whole mass of the rod is located on a segment of length $L$ (Fig. 13.1).

We would like to compute the moment of inertia $I_{G, 3}$ of the thin rod, oriented along the
axis $G e_{1}$, that is rotating in the horizontal plane around the vertical axis $G e_{3}$ going through its centre of mass $G$. Thus, its moment of inertia (13.1) is written,

$$
\begin{equation*}
I_{G, 3}=\int_{-L / 2}^{L / 2} d m \ell^{2} \tag{13.2}
\end{equation*}
$$

where $\ell \equiv r$ is the distance to the axis along the rod. The linear density of the homogeneous $\operatorname{rod} \rho_{\ell}$ is defined as the ratio between the mass $M$ and the length $L$ of the rod,

$$
\begin{equation*}
\rho_{\ell}=\frac{M}{L} \tag{13.3}
\end{equation*}
$$

The infinitesimal mass $d m$ is written in terms of the infinitesimal length $d \ell$ as,

$$
\begin{equation*}
d m=\rho_{\ell} d \ell=\frac{M}{L} d \ell \tag{13.4}
\end{equation*}
$$

Substituting the relation (13.4) in the integral (13.2), the moment of inertia $I_{G, 3}$ becomes,

$$
\begin{equation*}
I_{G, 3}=\frac{M}{L} \int_{-L / 2}^{L / 2} \ell^{2} d \ell=\left.\frac{M}{L} \frac{\ell^{3}}{3}\right|_{-L / 2} ^{L / 2}=\frac{M}{L} \frac{L^{3}}{12}=\frac{1}{12} M L^{2} \tag{13.5}
\end{equation*}
$$

### 13.1.2 Hollow Cylinder

We consider a homogeneous hollow cylinder of mass $M$, of height $L$, of radius $R$ and of thickness $e$ that is very thin with respect to its radius, i.e. $e \ll R$, which means that its radius can be considered as constant (Fig. 13.2).

We would like to compute the moment of inertia $I_{G, 3}$ of the hollow cylinder around the vertical axis $G \boldsymbol{e}_{3}$ going through its centre of mass $G$. Thus, its moment of inertia (13.1) is written,

$$
\begin{equation*}
I_{G, 3}=\int_{V} d m R^{2} \tag{13.6}
\end{equation*}
$$

where $R \equiv r$ is the constant radius of the hollow cylinder. We divide the hollow cylinder into elements of infinitesimal volume $d V$ of height $L$, of thickness $e$ and of width $R d \theta$ that are located at a distance $R$ from the vertical axis $G \boldsymbol{e}_{3}$, i.e.

$$
\begin{equation*}
d V=R L e d \theta \tag{13.7}
\end{equation*}
$$

The volumetric density $\rho$ of the hollow cylinder is defined as the ratio between the mass $M$ and the volume $V$ of the cylinder,

$$
\begin{equation*}
\rho=\frac{M}{V} \tag{13.8}
\end{equation*}
$$

Taking into account the expressions (13.7) and (13.8), the infinitesimal mass $d m$ is written in terms of the infinitesimal volume $d V$ of a parallelepiped as,

$$
\begin{equation*}
d m=\rho d V=\frac{M}{V} R L e d \theta \tag{13.9}
\end{equation*}
$$

Substituting expression (13.9) of the infinitesimal mass $d m$ into the integral (13.6), and integrating the angle $\theta$ from 0 to $2 \pi$, the moment of inertia $I_{G, 3}$ becomes,

$$
\begin{equation*}
I_{G, 3}=\frac{M}{V} R^{3} L e \int_{0}^{2 \pi} d \theta=2 \pi \frac{M}{V} R^{3} L e \tag{13.10}
\end{equation*}
$$

The volume $V$ of the hollow cylinder is equal to the product of the circumference $2 \pi R$ of the circular sections, of the length $L$ and of the thickness $e$,

$$
\begin{equation*}
V=2 \pi R L e \tag{13.11}
\end{equation*}
$$

Substituting the expression (13.11) of the volume of the cylinder into the expression (13.10) of the moment of inertia $I_{G, 3}$, it reduces to,

$$
\begin{equation*}
I_{G, 3}=M R^{2} \tag{13.12}
\end{equation*}
$$

### 13.1.3 Full cylinder

We consider a homogeneous full cylinder of mass $M$, of height $L$ and of radius $R$ (Fig. 13.2).

We would like to compute the moment of inertia $I_{G, 3}$ of the full cylinder around the vertical axis $G \boldsymbol{e}_{3}$ going through its centre of mass $G$. We divide the full cylinder into concentric hollow cylinders of infinitesimal volume $d V$, of height $L$, of circumference $2 \pi r$ and of thickness $d r$, i.e.

$$
\begin{equation*}
d V=2 \pi L r d r \tag{13.13}
\end{equation*}
$$

Taking into account the expressions (13.13) and (13.8), the infinitesimal mass $d m$ is written in terms of the infinitesimal volume $d V$ of a hollow cylinder as,

$$
\begin{equation*}
d m=\rho d V=\frac{M}{V} 2 \pi L r d r \tag{13.14}
\end{equation*}
$$

Substituting the expression (13.14) of the infinitesimal mass $d m$ into the integral (13.1), and by integrating the radius $r$ from 0 to $R$, the moment of inertia $I_{G, 3}$ becomes,

$$
\begin{equation*}
I_{G, 3}=2 \pi \frac{M}{V} L \int_{0}^{R} r^{3} d r=\left.2 \pi \frac{M}{V} L \frac{1}{4} r^{4}\right|_{0} ^{R}=\frac{\pi}{2} \frac{M}{V} L R^{4} \tag{13.15}
\end{equation*}
$$

The volume $V$ of the full cylinder is equal to the product of the surface of the section $\pi R^{2}$ and of the length $L$,

$$
\begin{equation*}
V=\pi R^{2} L \tag{13.16}
\end{equation*}
$$

Substituting the expression (13.16) of the volume of the cylinder into the expression (13.15) of the moment of inertia $I_{G, 3}$, it reduces to,

$$
\begin{equation*}
I_{G, 3}=\frac{1}{2} M R^{2} \tag{13.17}
\end{equation*}
$$

### 13.2 Rigid body with a fixed axis

In this section we shall consider the dynamics of a rigid body when the rigid body is in rotation around a fixed axis $A \boldsymbol{e}_{i}$. In order to do so, we shall begin by stating the HuygensSteiner theorem.

### 13.2.1 Huygens-Steiner theorem

Theorem 13.1 The Huygens-Steiner theorem also known as the parallel axis theorem states that the moment of inertia $I_{A, i}$ of a rigid body of mass $M$ in rotation around a fixed axis A $\boldsymbol{e}_{i}$, that is parallel to the principal axis $G \boldsymbol{e}_{i}$ and orthogonal to the vector $\boldsymbol{A} \boldsymbol{G}$ (Fig. 13.4), is expressed in terms of the moment of inertia $I_{G, i}$ and of the distance $d=\|\boldsymbol{A} \boldsymbol{G}\|=$ const as,

$$
\begin{equation*}
I_{A, i}=I_{G, i}+M d^{2} \tag{13.18}
\end{equation*}
$$

Demonstration Choosing as origin the material point $A$, the angular momentum transfer theorem (12.17) is written,

$$
\begin{equation*}
\boldsymbol{L}_{A}=\boldsymbol{A} \boldsymbol{G} \times M \boldsymbol{V}_{G}+\boldsymbol{L}_{G} \tag{13.19}
\end{equation*}
$$

Since the material point $A$ belongs to the rotation axis, its rotation velocity vanishes, i.e. $\boldsymbol{V}_{A}=\mathbf{0}$. Taking into account the relation (12.6), the velocity of the centre of mass is expressed in terms of the angular velocity vector $\boldsymbol{\Omega}$ associated to the rotation of the rigid body as,

$$
\begin{equation*}
\boldsymbol{V}_{G}=\boldsymbol{\Omega} \times \boldsymbol{A} \boldsymbol{G} \tag{13.20}
\end{equation*}
$$

Substituting equation (13.20) into equation (13.19), the angular momentum transfer theorem becomes,

$$
\begin{equation*}
\boldsymbol{L}_{A}=M \boldsymbol{A} \boldsymbol{G} \times(\boldsymbol{\Omega} \times \boldsymbol{A} \boldsymbol{G})+\boldsymbol{L}_{G} \tag{13.21}
\end{equation*}
$$

Taking into account the vectorial identity (1.43), the angular momentum transfer theorem (13.21) becomes,

$$
\begin{equation*}
\boldsymbol{L}_{A}=M\left(\boldsymbol{A} \boldsymbol{G}^{2} \boldsymbol{\Omega}-(\boldsymbol{A} \boldsymbol{G} \cdot \boldsymbol{\Omega}) \boldsymbol{A} \boldsymbol{G}\right)+\boldsymbol{L}_{G} \tag{13.22}
\end{equation*}
$$

The angular velocity vector $\boldsymbol{\Omega}$ is collinear to the fixed rotation axis $A \boldsymbol{e}_{i}$ and orthogonal to the vector $\boldsymbol{A} \boldsymbol{G}$, i.e. $\boldsymbol{A} \boldsymbol{G} \cdot \boldsymbol{\Omega}=0$. Thus, the angular momentum transfer theorem (13.22) reduces to,

$$
\begin{equation*}
\boldsymbol{L}_{A}=M d^{2} \boldsymbol{\Omega}+\boldsymbol{L}_{G} \tag{13.23}
\end{equation*}
$$

where $d=\|\boldsymbol{A} \boldsymbol{G}\|$. Since the angular velocity vector $\boldsymbol{\Omega}=\Omega \boldsymbol{e}_{i}$ is collinear to the principal axis $A \boldsymbol{e}_{i}$, that is parallel to the principal axis $G \boldsymbol{e}_{i}$, the angular momenta $\boldsymbol{L}_{A}$ and $\boldsymbol{L}_{G}$ of the rigid body are expressed in terms of the moments of inertia $I_{A, i}$ and $I_{G, i}$ respectively as,

$$
\begin{equation*}
\boldsymbol{L}_{A}=I_{A, i} \boldsymbol{\Omega} \quad \text { and } \quad \boldsymbol{L}_{G}=I_{G, i} \boldsymbol{\Omega} \tag{13.24}
\end{equation*}
$$

Substituting the equations (13.24) into the angular momentum transfer theorem (13.23), we obtain,

$$
\begin{equation*}
I_{A, i} \boldsymbol{\Omega}=\left(I_{G, i}+M d^{2}\right) \boldsymbol{\Omega} \tag{13.25}
\end{equation*}
$$

which implies that,

$$
\begin{equation*}
I_{A, i}=I_{G, i}+M d^{2} \tag{13.26}
\end{equation*}
$$

### 13.2.2 Translational and rotational kinetic energies

Since the kinetic energy (6.32) is an extensive quantity, the kinetic energy $T$ of a rigid body is the sum of the kinetic energies of all its material points $P_{\alpha}$, i.e.

$$
\begin{equation*}
T=\frac{1}{2} \sum_{\alpha} m_{\alpha} \boldsymbol{v}_{\alpha}^{2} \tag{13.27}
\end{equation*}
$$

Taking into account the relation (11.44), the kinetic energy (13.27) is recast as,

$$
\begin{equation*}
T=\frac{1}{2} \sum_{\alpha} m_{\alpha}\left(\boldsymbol{V}_{G}+\boldsymbol{v}_{\alpha}^{\prime}\right)^{2}=\frac{1}{2}\left(\sum_{\alpha} m_{\alpha}\right) \boldsymbol{V}_{G}^{2}+\boldsymbol{V}_{G} \cdot\left(\sum_{\alpha} m_{\alpha} \boldsymbol{v}_{\alpha}^{\prime}\right)+\frac{1}{2} \sum_{\alpha} m_{\alpha} \boldsymbol{v}_{\alpha}^{\prime 2} \tag{13.28}
\end{equation*}
$$

According to the relations (11.37) and (11.46), the kinetic energy (13.28) reduces to,

$$
\begin{equation*}
T=\frac{1}{2} M \boldsymbol{V}_{G}^{2}+\frac{1}{2} \sum_{\alpha} m_{\alpha} \boldsymbol{v}_{\alpha}^{\prime 2} \tag{13.29}
\end{equation*}
$$

Taking into account the relations (11.44), (11.39) and (12.5), the relative velocity $\boldsymbol{v}_{\alpha}^{\prime}$ of a material point $P_{\alpha}$ is written,

$$
\begin{equation*}
\boldsymbol{v}_{\alpha}^{\prime}=\boldsymbol{v}_{\alpha}-\boldsymbol{V}_{G}=\boldsymbol{\Omega} \times \boldsymbol{G} \boldsymbol{P}_{\alpha}=\boldsymbol{\Omega} \times \boldsymbol{r}_{\alpha}^{\prime} \tag{13.30}
\end{equation*}
$$

According to the first identity (1.40) and to expression (13.30), the relative velocity squared is recast as,

$$
\begin{equation*}
\boldsymbol{v}_{\alpha}^{\prime 2}=\left(\boldsymbol{\Omega} \times \boldsymbol{r}_{\alpha}^{\prime}\right) \cdot\left(\boldsymbol{\Omega} \times \boldsymbol{r}_{\alpha}^{\prime}\right)=\left(\boldsymbol{r}_{\alpha}^{\prime} \times\left(\boldsymbol{\Omega} \times \boldsymbol{r}_{\alpha}^{\prime}\right)\right) \cdot \boldsymbol{\Omega} \tag{13.31}
\end{equation*}
$$

Substituting equation (13.31) into equation (13.29), the kinetic energy becomes,

$$
\begin{equation*}
T=\frac{1}{2} M \boldsymbol{V}_{G}^{2}+\frac{1}{2}\left(\sum_{\alpha} m_{\alpha} \boldsymbol{r}_{\alpha}^{\prime} \times\left(\boldsymbol{\Omega} \times \boldsymbol{r}_{\alpha}^{\prime}\right)\right) \cdot \boldsymbol{\Omega} \tag{13.32}
\end{equation*}
$$

Taking into account the relations (11.39) and (12.30), the angular momentum $\boldsymbol{L}_{G}$ evaluated with respect to the centre of mass is written,

$$
\begin{equation*}
\boldsymbol{L}_{G}=\sum_{\alpha} m_{\alpha} \boldsymbol{r}_{\alpha}^{\prime} \times\left(\boldsymbol{\Omega} \times \boldsymbol{r}_{\alpha}^{\prime}\right) \tag{13.33}
\end{equation*}
$$

Substituting equation (13.33) into equation (13.32), the kinetic energy becomes,

$$
\begin{equation*}
T=\frac{1}{2} M \boldsymbol{V}_{G}^{2}+\frac{1}{2} \boldsymbol{L}_{G} \cdot \boldsymbol{\Omega} \tag{13.34}
\end{equation*}
$$

The first term on the RHS of equation (13.34) is the translational energy of the rigid body and the second term is the intrinsic rotational energy of the rigid body. Using the expression (12.41) of the angular momentum $\boldsymbol{L}_{G}$ expressed in the principal axis frame $\left(G, \boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3}\right)$, the expression of the kinetic energy (13.34) is recast as,

$$
\begin{equation*}
T=\frac{1}{2} M \boldsymbol{V}_{G}^{2}+\frac{1}{2} \sum_{j=1}^{3} I_{G, j} \Omega_{j}^{2} \tag{13.35}
\end{equation*}
$$

In the particular case where the rigid body is rotating around the principal axis $G \boldsymbol{e}_{i}$, the angular velocity vector $\boldsymbol{\Omega}=\Omega \boldsymbol{e}_{i}$, which implies that $\Omega_{j}=\Omega \delta_{i j}$. Thus, in this case, the kinetic energy (13.35) reduces to,

$$
\begin{equation*}
T=\frac{1}{2} M \boldsymbol{V}_{G}^{2}+\frac{1}{2} I_{G, i} \boldsymbol{\Omega}^{2} \quad \text { (fixed axis) } \tag{13.36}
\end{equation*}
$$

### 13.2.3 Kinetic energy theorem

Theorem 13.2 We consider the case where the moments of inertia expressed with respect to the principal axis frame of a rigid body are constants, i.e. $I_{G, j}=$ const where $j=1,2,3$. In this case, the time derivative of the kinetic energy of the rigid body where the centre of mass $G$ has a velocity $\boldsymbol{V}_{G}$ and that is rotating around the centre of mass $G$ at angular velocity $\boldsymbol{\Omega}$ is written,

$$
\begin{equation*}
\frac{d T}{d t}=\boldsymbol{F}^{e x t} \cdot \boldsymbol{V}_{G}+\boldsymbol{\tau}_{G}^{e x t} \cdot \boldsymbol{\Omega} \tag{13.37}
\end{equation*}
$$

where $\boldsymbol{F}^{\text {ext }}$ is the net external force and $\boldsymbol{\tau}_{G}^{\text {ext }}$ is the net external torque evaluated with respect to the centre of mass $G$.

Demonstration Using the expression (12.29) of the angular momentum $\boldsymbol{L}_{G}$, the kinetic energy (13.34) is recast as,

$$
\begin{equation*}
T=\frac{1}{2} M \boldsymbol{V}_{G}^{2}+\frac{1}{2} \sum_{j=1}^{3} I_{G, j} \Omega_{j}^{2} \tag{13.38}
\end{equation*}
$$

Since the mass $M$ and the components of the inertia tensor $I_{G, j}$ are constants, the time derivative of the kinetic energy (13.38) is written,

$$
\begin{equation*}
\frac{d T}{d t}=M \frac{d \boldsymbol{V}_{G}}{d t} \cdot \boldsymbol{V}_{G}+\sum_{j=1}^{3} I_{G, j} \frac{d \Omega_{j}}{d t} \Omega_{j}=\frac{d\left(M \boldsymbol{V}_{G}\right)}{d t} \cdot \boldsymbol{V}_{G}+\sum_{j=1}^{3} \frac{d\left(I_{G, j} \Omega_{j}\right)}{d t} \Omega_{j} \tag{13.39}
\end{equation*}
$$

Using the expression (11.60) of the momentum $\boldsymbol{P}$ and the expression (12.41) of the angular momentum $\boldsymbol{L}_{G}$, the equation (13.39) becomes,

$$
\begin{equation*}
\frac{d T}{d t}=\frac{d \boldsymbol{P}}{d t} \cdot \boldsymbol{V}_{G}+\frac{d \boldsymbol{L}_{G}}{d t} \cdot \boldsymbol{\Omega} \tag{13.40}
\end{equation*}
$$

Substituting the centre of mass theorem (12.13) and the angular momentum theorem (12.27) into the expressions of the time derivatives (13.40) of the momentum and the angular momentum, we obtain,

$$
\begin{equation*}
\frac{d T}{d t}=\boldsymbol{F}^{\mathrm{ext}} \cdot \boldsymbol{V}_{G}+\boldsymbol{\tau}_{G}^{\mathrm{ext}} \cdot \boldsymbol{\Omega} \tag{13.41}
\end{equation*}
$$

### 13.2.4 Unbalanced wheel

Before investigating gyroscopic effects, we consider first the case of an unbalanced wheel where the rotation axis is not a principal axis, in contrast to a well balanced wheel where the principal axis is the symmetry axis. The wheel can be considered as a cylinder that rotates at constant angular velocity $\boldsymbol{\Omega}$ around a fixed axis that goes through its centre of mass $G$. Let $\left(G, \boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3}\right)$ be the principal axis frame that is at rest with respect to the cylinder. The principal axis $G \boldsymbol{e}_{3}$ is the symmetry axis of the cylinder that makes a constant angle $\theta$ with respect to the fixed axis that is collinear to the angular velocity vector $\boldsymbol{\Omega}$ (Fig. 13.5).

Initially at $t=0$, the vector $\boldsymbol{e}_{2}$ is in the vertical plane spanned by the vectors $\boldsymbol{e}_{3}$ and $\boldsymbol{\Omega}$. The components of the angular velocity vector $\boldsymbol{\Omega}$ expressed in the principal axis frame are written,

$$
\begin{align*}
& \Omega_{1}=\Omega \sin \theta \sin (\Omega t) \\
& \Omega_{2}=\Omega \sin \theta \cos (\Omega t)  \tag{13.42}\\
& \Omega_{3}=\Omega \cos \theta
\end{align*}
$$

The angular velocity vector $\boldsymbol{\Omega}$ is constant with respect to the earth's inertial frame, but not with respect to the non-inertial frame of the wheel. The time derivative of the components (13.42) of the angular velocity vector are written,

$$
\begin{align*}
\dot{\Omega}_{1} & =\Omega^{2} \sin \theta \cos (\Omega t) \\
\dot{\Omega}_{2} & =-\Omega^{2} \sin \theta \sin (\Omega t)  \tag{13.43}\\
\dot{\Omega}_{3} & =0
\end{align*}
$$

The moment of inertia along the symmetry axis is $I_{G, 3} \equiv I_{G, \|}$ and the moments of inertia along the two other axes are $I_{G, 1}=I_{G, 2} \equiv I_{G, \perp}$. Taking into account the expressions (13.42) and (13.43), Euler's equations (12.48) are written explicitly,

$$
\begin{align*}
\tau_{G, 1}^{\text {ext }} & =I_{G, \perp} \Omega^{2} \sin \theta \cos (\Omega t)+\left(I_{G, \|}-I_{G, \perp}\right) \Omega^{2} \cos \theta \sin \theta \cos (\Omega t) \\
\tau_{G, 2}^{\text {ext }} & =-I_{G, \perp} \Omega^{2} \sin \theta \sin (\Omega t)+\left(I_{G, \perp}-I_{G, \|}\right) \Omega^{2} \cos \theta \sin \theta \sin (\Omega t)  \tag{13.44}\\
\tau_{G, 3}^{\text {ext }} & =0
\end{align*}
$$

According to the expression (12.47), the torque $\boldsymbol{\tau}_{G}^{\text {ext }}$ exerted by the rotation axis on the unbalanced wheel is written,

$$
\begin{align*}
\boldsymbol{\tau}_{G}^{\text {ext }}= & \left(I_{G, \perp}+\left(I_{G, \|}-I_{G, \perp}\right) \cos \theta\right) \Omega^{2} \sin \theta \cos (\Omega t) \boldsymbol{e}_{1} \\
& -\left(I_{G, \perp}+\left(I_{G, \|}-I_{G, \perp}\right) \cos \theta\right) \Omega^{2} \sin \theta \sin (\Omega t) \boldsymbol{e}_{2} \tag{13.45}
\end{align*}
$$

The torque $\boldsymbol{\tau}_{G}^{\text {ext }}$ depends periodically on time, which generates periodic shakes felt on the axis. In the limit where $\theta=0$, the torque vanishes, i.e. $\boldsymbol{\tau}_{G}^{\text {ext }}=\mathbf{0}$, and the wheel becomes

Balancing of a wheel well balanced. Measuring the torque exerted on the unbalanced wheel, a mechanic is able to identify where masses have to be added on the rim of a car wheel in order to balance the wheel.

### 13.3 Gyroscopes

A gyroscope is a rotating wheel or disk where the rotation axis keeps a given orientation. The wheel is mounted on two concentric frames that can rotate around orthogonal axes going through its centre of mass. When the wheel is rotating, the orientation of the axis is not modified by the rotation of the internal or external frame. Thus, gyroscopes are useful to measure or keep a given orientation. For instance, they are used in aeronautics.

The invention of the gyroscope is due to Leon Foucault. Following his experimental demonstration of the earth's rotation in 1851 using a pendulum attached at the top of the Pantheon dome, he then developed a tool that is able to keep a fixed orientation with respect to the plane of the solar system. This tool, that was designed to convince his most sceptical contemporaries that the earth is rotating around itself, is the gyroscope. The etymology of the word gyroscope denotes the tool that enables to see the rotation of the earth. The axis of the gyroscope is fixed with respect to the plane of the solar system, which means that from the earth's rotating frame of reference the rotation axis of the gyroscope has an apparent precession with respect to the earth's rotation axis. To establish this 24 hours precession period in order to experimentally show the earth's rotation, the rotation axis of the gyroscope has to be different from the earth's rotation axis.

### 13.3.1 Gyroscopic effects

By analogy with the gyroscope, gyroscopic effects denote the dynamical behaviour of a rotating disk or a wheel that resists any change of orientation of its rotation axis. These gyroscopic effects are related to the conservation of angular momentum in the absence of an external torque.

As a first example of gyroscopic effect, we consider a person sitting on a stool turning around a vertical axis who holds a wheel rotating around its symmetry axis (Fig. 13.7). Initially, the symmetry axis of the wheel is horizontal and the wheel rotates in a vertical plane. Thus, the vertical component of the angular momentum of the system consisting of the person, of the stool and of the wheel vanishes, i.e. $L_{z}=0$. The person exerts then a torque on the wheel to straighten it such that its symmetry axis becomes vertical and that its rotation occurs finally in a horizontal plane. Since the torque is an internal torque, the vertical component of the angular momentum of the system consisting of the person, the stool and the wheel does not change, i.e. $L_{z}=0$. Since the wheel rotates finally in a horizontal plane, the vertical component of its angular momentum is non zero. For the vertical component of the angular momentum of the system consisting of the person, of the stool and of the wheel to remain zero, the stool and the person have to turn around the vertical axis of the stool in the opposite direction to the wheel.

If the wheel is replaced by two identical wheels rotating around an axis with a scalar angular velocity of opposite sign, the gyroscopic effects disappears because the vectorial sum of the angular momenta of the two wheels cancels. Thus, when the axis is straightened, the person and the stool stay at rest.

When a wheel is spun around its symmetry axis and it is held by a person, the weight $\boldsymbol{P}$ of the wheel generates an external torque $\boldsymbol{\tau}_{O}^{\text {ext }}=\boldsymbol{r} \times \boldsymbol{P}$ on the wrist $O$ of the person, where $\boldsymbol{r}=\boldsymbol{O} \boldsymbol{G}$ (Fig. 13.8). This torque is oriented in the horizontal plane and it is orthogonal to the rotation axis. According to the angular momentum theorem (12.14), i.e. $\boldsymbol{\tau}_{O}^{\text {ext }}=d \boldsymbol{L}_{O} / d t$, the angular momentum variation $\boldsymbol{L}_{O}$ is collinear to the external torque $\boldsymbol{\tau}_{O}^{\text {ext }}$. Thus, the rotation axis changes orientation in the direction defined by the external torque $\tau_{O}^{\text {ext }}$, which leads to the precession of the rotation axis of the wheel around the vertical axis. To keep the rotation axis fixed, the person has to apply with his wrist on this axis a torque of equal norm and opposite direction.

In the case of a bike wheel rotating around an axis attached to a vertical rope, the gyroscopic effect is similar (Fig. 13.8). The torque $\boldsymbol{\tau}_{O}$ generated by the weight $\boldsymbol{P}$ of the wheel at the suspension point $O$ causes a precession of the wheel axis around the rope according to the angular momentum theorem (12.14).

### 13.3.2 Bike wheel

We consider a bike wheel of mass $M$ and of radius $R$ that rolls without slipping. The centre of mass $G$ of the wheel has a uniform circular motion of radius $\rho=$ const and a constant scalar angular velocity $\dot{\phi}=$ const around the vertical axis $O \boldsymbol{e}_{z}$ (Fig. 13.9). The precession angular velocity vector of the wheel is $\dot{\phi}=\dot{\phi} \boldsymbol{e}_{z}$. The wheel has an intrinsic rotational motion at scalar angular velocity $\dot{\psi}=$ const around the symmetry axis $G \boldsymbol{e}_{3}$. The rotation plane is inclined by a nutation angle $\theta=$ const with respect to the vertical axis. We associate the principal axis frame $\left(G, \boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3}\right)$ to the wheel. The principal axis frame is in general at rest with respect to the rigid body in order for the moments of inertia to be constant. Since the wheel is invariant under rotation around the intrinsic rotation axis $G \boldsymbol{e}_{3}$, the two other basis vectors of the frame do not need to be at rest with respect to the wheel but simply to be located in the plane of the wheel. Thus, the vector $\boldsymbol{e}_{1}=\boldsymbol{e}_{\phi}$ does not follow the intrinsic rotational motion of the wheel and it is located in the horizontal plane that contains the centre of mass $G$ at all times. The vector $\boldsymbol{e}_{2}$ does not follow either the intrinsic rotational motion of the wheel and it is located in the vertical plane containing the centre of mass $G$ and the vector $\boldsymbol{e}_{3}$ at all times. We consider that the radius of curvature $\rho$ is sufficiently large with respect to the radius $R$ of the wheel, i.e. $R \ll \rho$, and that the wheel is a hollow cylinder of negligible thickness and of radius $R$, i.e. that all the mass $M$ of the wheel is located on its circumference at distance $R$ from the centre of mass.

Now, we will perform an analysis of the dynamics of the wheel in order to determine the explicit expression of the angle $\theta$ that the plane of the wheel takes with respect to a vertical plane. First, we determine the kinematical quantities of interest. The total angular velocity vector $\boldsymbol{\Omega}$ is the sum of the precession angular velocity vector $\dot{\boldsymbol{\phi}}$ and the intrinsic angular velocity vector $\dot{\boldsymbol{\psi}}$, i.e.

$$
\begin{equation*}
\boldsymbol{\Omega}=\dot{\boldsymbol{\phi}}+\dot{\boldsymbol{\psi}}=\dot{\phi} \boldsymbol{e}_{z}-\dot{\psi} \boldsymbol{e}_{3}=\dot{\phi} \cos \theta \boldsymbol{e}_{2}+(\dot{\phi} \sin \theta-\dot{\psi}) \boldsymbol{e}_{3} \tag{13.46}
\end{equation*}
$$

The velocity $\boldsymbol{V}_{G}$ of the centre of mass that has a circular motion of radius $\rho$ and of angular velocity $\dot{\phi}$ in a horizontal plane is written,

$$
\begin{equation*}
\boldsymbol{V}_{G}=V_{G} \boldsymbol{e}_{\phi}=\rho \dot{\phi} \boldsymbol{e}_{\phi} \tag{13.47}
\end{equation*}
$$

Since the wheel rolls without slipping, taking into account the expression (12.12), the velocity of the centre of mass is written,

$$
\begin{equation*}
\boldsymbol{V}_{G}=\boldsymbol{\Omega} \times \boldsymbol{C} \boldsymbol{G}=\left(\dot{\phi} \cos \theta \boldsymbol{e}_{2}+(\dot{\phi} \sin \theta-\dot{\psi}) \boldsymbol{e}_{3}\right) \times R \boldsymbol{e}_{2}=-R(\dot{\phi} \sin \theta-\dot{\psi}) \boldsymbol{e}_{1} \tag{13.48}
\end{equation*}
$$

Identifying the expressions (13.47) and (13.48) of the velocity of the centre of mass $\boldsymbol{V}_{G}$, we obtain the following identity,

$$
\begin{equation*}
-R(\dot{\phi} \sin \theta-\dot{\psi})=\rho \dot{\phi} \tag{13.49}
\end{equation*}
$$

Taking into account the identity (13.49), the total angular velocity vector (13.46) is recast as,

$$
\begin{equation*}
\boldsymbol{\Omega}=\dot{\phi} \cos \theta \boldsymbol{e}_{2}-\frac{\rho}{R} \dot{\phi} \boldsymbol{e}_{3} \tag{13.50}
\end{equation*}
$$

Now, we determine the dynamical quantities of interest. The only two external forces that are exerted on the wheel are the weight $\boldsymbol{P}=-M g \boldsymbol{e}_{z}$, that is exerted on the centre of mass $G$ of the wheel, and the normal reaction force $\boldsymbol{N}$ exerted on the wheel by the ground at the point of contact $C$ between the wheel and the ground. Since the normal reaction force $\boldsymbol{N}$ is unknown, it is a good idea to evaluate the angular momentum and the net external torque exerted on the wheel at point $C$. The net external torque $\boldsymbol{\tau}_{C}^{\text {ext }}$ evaluated at the point of contact $C$ between the wheel and the ground is due only to the weight, i.e.

$$
\begin{equation*}
\boldsymbol{\tau}_{C}^{\mathrm{ext}}=\boldsymbol{C} \boldsymbol{G} \times \boldsymbol{P}=\left(R \boldsymbol{e}_{2}\right) \times\left(-M g \sin \theta \boldsymbol{e}_{3}\right)=-M R g \sin \theta \boldsymbol{e}_{1}=-M R g \sin \theta \boldsymbol{e}_{\phi} \tag{13.51}
\end{equation*}
$$

Taking into account the expressions (12.18) and (13.47), the angular momentum $\boldsymbol{L}_{C}$ of the wheel evaluated with respect to the point of contact $C$ is written,

$$
\begin{equation*}
\boldsymbol{L}_{C}=\boldsymbol{L}_{G}+\boldsymbol{C} \boldsymbol{G} \times M \boldsymbol{V}_{G}=\boldsymbol{L}_{G}+\left(R \boldsymbol{e}_{2}\right) \times\left(M \rho \dot{\phi} \boldsymbol{e}_{1}\right)=\boldsymbol{L}_{G}-M R \rho \dot{\phi} \boldsymbol{e}_{3} \tag{13.52}
\end{equation*}
$$

Taking into account the relations (12.37) and (13.50), the angular momentum $\boldsymbol{L}_{G}$ evaluated at the centre of mass $G$ is written,

$$
\begin{equation*}
\boldsymbol{L}_{G}=I_{G, 2} \dot{\phi} \cos \theta \boldsymbol{e}_{2}-I_{G, 3} \frac{\rho}{R} \dot{\phi} \boldsymbol{e}_{3} \tag{13.53}
\end{equation*}
$$

The moments of inertia of the wheel, that is considered as a hollow cylinder of mass $M$, of radius $R$ and of negligible thickness, are given by,

$$
\begin{equation*}
I_{G, 1}=I_{G, 2}=\frac{1}{2} M R^{2} \quad \text { and } \quad I_{G, 3}=M R^{2} \tag{13.54}
\end{equation*}
$$

Substituting the expressions (13.54) into the relation (13.53), the angular momentum evaluated with respect to the centre of mass $G$ becomes,

$$
\begin{equation*}
\boldsymbol{L}_{G}=\frac{1}{2} M R^{2} \dot{\phi} \cos \theta \boldsymbol{e}_{2}-M R \rho \dot{\phi} \boldsymbol{e}_{3} \tag{13.55}
\end{equation*}
$$

Substituting the expression (12.33) into the relation (13.52), the angular momentum evaluated with respect to the point of contact $C$ becomes,

$$
\begin{equation*}
\boldsymbol{L}_{C}=\frac{1}{2} M R^{2} \dot{\phi} \cos \theta \boldsymbol{e}_{2}-2 M R \rho \dot{\phi} \boldsymbol{e}_{3} \tag{13.56}
\end{equation*}
$$

The basis vectors $\boldsymbol{e}_{2}$ and $\boldsymbol{e}_{3}$ of the principal axis frame are expressed in terms of the basis vectors of the cylindrical frame $\boldsymbol{e}_{\rho}$ and $\boldsymbol{e}_{z}$ as,

$$
\begin{equation*}
\boldsymbol{e}_{2}=-\sin \theta \boldsymbol{e}_{\rho}+\cos \theta \boldsymbol{e}_{z} \quad \text { and } \quad \boldsymbol{e}_{3}=\cos \theta \boldsymbol{e}_{\rho}+\sin \theta \boldsymbol{e}_{z} \tag{13.57}
\end{equation*}
$$

Taking into account the change of basis formulae (13.57), the angular momentum evaluated with respect to the point of contact $C$ becomes,

$$
\begin{equation*}
\boldsymbol{L}_{C}=-\left(\frac{1}{2} M R^{2} \dot{\phi} \cos \theta \sin \theta+2 M R \rho \dot{\phi} \cos \theta\right) \boldsymbol{e}_{\rho}+\left(\frac{1}{2} M R^{2} \dot{\phi} \cos ^{2} \theta-2 M R \rho \dot{\phi} \sin \theta\right) \boldsymbol{e}_{z} \tag{13.58}
\end{equation*}
$$

The terms in brackets in relation (13.58) are constant. Using the expressions (5.6) of the time derivatives of the basis vectors, i.e. $\dot{\boldsymbol{e}}_{\rho}=\dot{\phi} \boldsymbol{e}_{\phi}$ and $\dot{\boldsymbol{e}}_{z}=\mathbf{0}$, the time derivative of the angular momentum $\boldsymbol{L}_{C}$ evaluated with respect to the point of contact $C$ is written,

$$
\begin{equation*}
\frac{d \boldsymbol{L}_{C}}{d t}=-2 M R \rho \dot{\phi}^{2} \cos \theta\left(1+\frac{R}{4 \rho} \sin \theta\right) \boldsymbol{e}_{\phi} \tag{13.59}
\end{equation*}
$$

Since the radius $R$ of the wheel is negligible with respect to the radius of curvature $\rho$, i.e. $R \ll \rho$, we can neglect the second term in brackets in the relation (13.59) to first approximation, i.e.

$$
\begin{equation*}
\frac{d \boldsymbol{L}_{C}}{d t}=-2 M R \rho \dot{\phi}^{2} \cos \theta \boldsymbol{e}_{\phi} \tag{13.60}
\end{equation*}
$$

The angular momentum theorem (12.26) applied to the point of contact $C$ reduces to,

$$
\begin{equation*}
\boldsymbol{\tau}_{C}^{\mathrm{ext}}=\frac{d \boldsymbol{L}_{C}}{d t} \tag{13.61}
\end{equation*}
$$

taking into account the fact that the velocity of the point of contact vanishes, i.e. $\boldsymbol{V}_{C}=\mathbf{0}$. Substituting equations (13.51) and (13.60) into the angular momentum theorem (13.61) taking into account the expression (13.47), we obtain the following condition on the angle $\theta$,

$$
\begin{equation*}
\tan \theta=\frac{2 \rho \dot{\phi}^{2}}{g}=\frac{2 V_{G}^{2}}{\rho g} \tag{13.62}
\end{equation*}
$$

The physical interpretation of the condition (13.62) enables us to understand the gyroscopic effects associated to the dynamics of a bike wheel in a turn. For a bike wheel that rolls at

Motorbike inside a turn a fixed velocity $V_{G}$, as the radius of curvature $\rho$ of the turn decreases the angle of vertical inclination $\theta$ increases and vice versa. For a bike wheel that takes a turn where the radius of curvature $\rho$ is fixed, as the velocity $V_{G}$ increases the inclination angle $\theta$ increases and inversely. The motorbikes have a large inclination angle $\theta$ inside a turn because their velocity $V_{G}$ is very high.

### 13.3.3 Spinning top

We consider a spinning top rotating with respect to its axis of symmetry $O \boldsymbol{e}_{3}$. We assume that the point of contact $O$ between the spinning top and the ground is fixed. The spinning top has a precession motion of angular velocity $\dot{\phi}=\dot{\phi} \boldsymbol{e}_{z}$, a nutation motion of angular velocity $\dot{\boldsymbol{\theta}}=\dot{\boldsymbol{\theta}} \boldsymbol{e}_{\phi}$ and an intrinsic rotation motion of angular velocity $\dot{\boldsymbol{\psi}}=\dot{\psi} \boldsymbol{e}_{3}$. We associate the principal axis frame $\left(G, \boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3}\right)$ to the spinning top (Fig. 13.10). The principal axis frame is in general at rest with respect to the rigid body in order for the moments of inertia to be constant. Since the spinning top is invariant under rotation around the intrinsic rotation axis $G \boldsymbol{e}_{3}$, the other two basis vectors of the frame do not need to be at rest with respect to the wheel but simply to be located in the plane that is orthogonal to the axis of symmetry of the spinning top. Thus, the vector $\boldsymbol{e}_{1}=\boldsymbol{e}_{\phi}$ does not follow the intrinsic rotational motion of the spinning top and is located in the horizontal plane that contains the centre of mass $G$ at all times. The vector $\boldsymbol{e}_{2}=-\boldsymbol{e}_{\theta}$ does not follow either the intrinsic rotational motion of the spinning top and is located in the vertical plane that contains the centre of mass $G$ and the vector $\boldsymbol{e}_{3}$ at all times.

The rotational angular velocity $\boldsymbol{\Omega}$ of the spinning top is written as,

$$
\begin{equation*}
\boldsymbol{\Omega}=\dot{\phi} \boldsymbol{e}_{z}+\dot{\theta} \boldsymbol{e}_{1}+\dot{\psi} \boldsymbol{e}_{3}=\dot{\theta} \boldsymbol{e}_{1}+\dot{\phi} \sin \theta \boldsymbol{e}_{2}+(\dot{\psi}+\dot{\phi} \cos \theta) \boldsymbol{e}_{3} \tag{13.63}
\end{equation*}
$$

The only two external forces exerted on the spinning top are the weight $\boldsymbol{P}=-M g \boldsymbol{e}_{z}$, that is exerted at the centre of mass $G$ of the spinning top, and the normal reaction force $\boldsymbol{N}$ exerted on the spinning top by the ground at the point of contact $O$ between the spinning top and the ground. Since the normal reaction force $\boldsymbol{N}$ is unknown, it is appropriate to evaluate the angular momentum and the net external torque exerted on the spinning top with respect to the point $O$. The net external torque $\boldsymbol{\tau}_{O}^{\text {ext }}$ evaluated at the point of contact $O$ of the spinning top with the ground is due only to the weight, i.e.

$\boldsymbol{\tau}_{O}^{\text {ext }}=\boldsymbol{O} \boldsymbol{G} \times \boldsymbol{P}=\left(\ell \boldsymbol{e}_{3}\right) \times\left(-M g \boldsymbol{e}_{z}\right)=-M g \ell \sin \theta \boldsymbol{e}_{3} \times \boldsymbol{e}_{2}=M g \ell \sin \theta \boldsymbol{e}_{1}=M g \ell \sin \theta \boldsymbol{e}_{\phi}$

where $\|\boldsymbol{O} \boldsymbol{G}\| \equiv \ell$. The moments of inertia along the axis of symmetry is $I_{O, 3}=I_{O, \|}$ and the moments of inertia along the two other axes are $I_{O, 1}=I_{O, 2}=I_{O, \perp}$. The expression of the angular momentum $\boldsymbol{L}_{O}$ evaluated with respect to point $O$ is obtained by evaluating the expression (12.41) at $O$,

$$
\begin{align*}
\boldsymbol{L}_{O} & =I_{O, \perp} \dot{\theta} \boldsymbol{e}_{1}+I_{O, \perp} \dot{\phi} \sin \theta \boldsymbol{e}_{2}+I_{O, \|}(\dot{\psi}+\dot{\phi} \cos \theta) \boldsymbol{e}_{3} \\
& =I_{O, \perp} \dot{\theta} \boldsymbol{e}_{\phi}-I_{O, \perp} \dot{\phi} \sin \theta \boldsymbol{e}_{\theta}+I_{O, \|}(\dot{\psi}+\dot{\phi} \cos \theta) \boldsymbol{e}_{r} \tag{13.65}
\end{align*}
$$

The time derivative of the angular momentum (13.65) is written,

$$
\begin{align*}
\frac{d \boldsymbol{L}_{O}}{d t}= & I_{O, \perp} \ddot{\theta} \boldsymbol{e}_{\phi}-I_{O, \perp}(\ddot{\phi} \sin \theta+\dot{\phi} \dot{\theta} \cos \theta) \boldsymbol{e}_{\theta}+I_{O, \|}(\ddot{\psi}+\ddot{\phi} \cos \theta-\dot{\phi} \dot{\theta} \sin \theta) \boldsymbol{e}_{r} \\
& +I_{O, \perp} \dot{\theta} \dot{\boldsymbol{e}}_{\phi}-I_{O, \perp} \dot{\phi} \sin \theta \dot{\boldsymbol{e}}_{\theta}+I_{O, \|}(\dot{\psi}+\dot{\phi} \cos \theta) \dot{\boldsymbol{e}}_{r} \tag{13.66}
\end{align*}
$$

Using the relations (5.16) for the time derivatives of the basis vectors of a spherical frame, the expression (13.66) becomes,

$$
\begin{align*}
\frac{d \boldsymbol{L}_{O}}{d t}= & I_{O, \perp} \ddot{\theta} \boldsymbol{e}_{\phi}-I_{O, \perp}(\ddot{\phi} \sin \theta+\dot{\phi} \dot{\theta} \cos \theta) \boldsymbol{e}_{\theta}+I_{O, \|}(\ddot{\psi}+\ddot{\phi} \cos \theta-\dot{\phi} \dot{\theta} \sin \theta) \boldsymbol{e}_{r} \\
& +I_{O, \perp} \dot{\theta}\left(-\dot{\phi}\left(\sin \theta \boldsymbol{e}_{r}+\cos \theta \boldsymbol{e}_{\theta}\right)\right)-I_{O, \perp} \dot{\phi} \sin \theta\left(-\dot{\theta} \boldsymbol{e}_{r}+\dot{\phi} \cos \theta \boldsymbol{e}_{\phi}\right) \\
& +I_{O, \|}(\dot{\psi}+\dot{\phi} \cos \theta)\left(\dot{\theta} \boldsymbol{e}_{\theta}+\dot{\phi} \sin \theta \boldsymbol{e}_{\phi}\right) \tag{13.67}
\end{align*}
$$

which can be factorised as,

$$
\begin{align*}
\frac{d \boldsymbol{L}_{O}}{d t}= & I_{O, \|}(\ddot{\psi}+\ddot{\phi} \cos \theta-\dot{\phi} \dot{\theta} \sin \theta) \boldsymbol{e}_{r} \\
& +\left(I_{O, \|}(\dot{\psi}+\dot{\phi} \cos \theta) \dot{\theta}-I_{O, \perp}(\ddot{\phi} \sin \theta+2 \dot{\phi} \dot{\theta} \cos \theta)\right) \boldsymbol{e}_{\theta}  \tag{13.68}\\
& +\left(I_{O, \perp} \ddot{\theta}+\left(I_{O, \|}-I_{O, \perp}\right) \dot{\phi}^{2} \sin \theta \cos \theta+I_{O, \|} \dot{\psi} \dot{\phi} \sin \theta\right) \boldsymbol{e}_{\phi}
\end{align*}
$$

The angular momentum theorem (12.14) applied to the point of contact $O$ reduces to,

$$
\begin{equation*}
\boldsymbol{\tau}_{O}^{\mathrm{ext}}=\frac{d \boldsymbol{L}_{O}}{d t} \tag{13.69}
\end{equation*}
$$

Substituting equations (13.64) and (13.68) into the angular momentum theorem (13.69), we obtain three scalar equations of motion along the three lines of coordinates,

$$
\begin{align*}
& I_{O, \|}(\ddot{\psi}+\ddot{\phi} \cos \theta-\dot{\phi} \dot{\theta} \sin \theta)=0 \\
& I_{O, \|}(\dot{\psi}+\dot{\phi} \cos \theta) \dot{\theta}-I_{O, \perp}(\ddot{\phi} \sin \theta+2 \dot{\phi} \dot{\theta} \cos \theta)=0  \tag{13.70}\\
& I_{O, \perp} \ddot{\theta}+\left(I_{O, \|}-I_{O, \perp}\right) \dot{\phi}^{2} \sin \theta \cos \theta+I_{O, \|} \dot{\psi} \dot{\phi} \sin \theta=M g \ell \sin \theta
\end{align*}
$$

In the particular case where the nutation motion of the spinning top is negligible, i.e.
$\dot{\theta}=0$ et $\ddot{\theta}=0$, the equations of motion (13.70) reduce to,

$$
\begin{align*}
& \ddot{\psi}+\ddot{\phi} \cos \theta=0 \\
& \ddot{\phi}=0  \tag{13.71}\\
& \left(I_{O, \|}-I_{O, \perp}\right) \dot{\phi}^{2} \cos \theta+I_{O, \|} \dot{\psi} \dot{\phi}=M g \ell
\end{align*}
$$

The first two equations imply that the precession angular velocity $\dot{\phi}=$ const and the intrinsic rotation angular velocity $\dot{\psi}=$ const are constants. In the limit where the precession is slow with respect to the intrinsic rotation, i.e. $\dot{\phi} \ll \dot{\psi}$, the third relation (13.71) shows that the precession angular velocity $\dot{\phi}$ is inversely proportional to the intrinsic rotation angular velocity $\dot{\psi}$,

$$
\begin{equation*}
\dot{\phi}=\frac{M g \ell}{I_{O, \|} \dot{\psi}} \tag{13.72}
\end{equation*}
$$

Using a bike wheel and two axes, we can build a spinning top that illustrates the precession, the nutation and the intrinsic rotation (Fig. 13.11).

A rattleback is a kind of spinning top with a very particular shape that has a precession motion for a rotation in one direction only. If the rattleback is thrown in the natural rotation direction, it turns fast. If it is thrown in the opposite direction, it stops quickly and moves backwards in the opposite direction. At first glance, the rattleback seems to be a half an ellipsoid of revolution, but in reality it is an ellipsoid that is cut along a plane that does not contain two axes of symmetry (Fig. 13.12). When it is thrown in the right direction, the rotation axis is a principal axis. When it is thrown in the wrong direction, the rotation axis is not a principal axis, which gives rise to a pitch and a roll - generated by a net external torque similar to the unbalanced wheel - that increases over time and brings the precession motion of the rattleback to an end before throwing it backwards in the opposite direction...

