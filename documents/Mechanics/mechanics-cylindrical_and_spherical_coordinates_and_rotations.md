# Cylindrical and spherical coordinates, and rotations 

Until now, we described the motion of a material point with Cartesian coordinates. The Cartesian coordinates are often the most adapted to describe the dynamics of a material point when this dynamics has no particular symmetry. But when the material point moves for example on a sphere or a cylinder, it is more convenient to use more appropriate coordinates. To describe a motion with cylindrical symmetry we will choose cylindrical coordinates and to describe a motion with spherical symmetry we will choose spherical coordinates. We can do the opposite, but this is not appropriate because the computation is much longer. We choose the right coordinates for a specific problem primarily for practical purposes. Choosing the appropriate coordinates, we simplify considerably the mathematical resolution of the problem and it becomes easier to discover the dynamical properties of motion.

### 5.1 Cylindrical coordinates

The polar coordinates were used for the first time by Bonaventura Cavalieri. A century later, Leonhard Euler extended the polar coordinates to a three dimensional space and introduced cylindrical and spherical coordinates. The polar coordinates are particularly adapted to describe a circular motion in a plane and the cylindrical coordinates are adapted to described a motion that has a cylindrical symmetry in space. This is for instance the case of a system consisting of a pen in relative motion with respect to a circular horizontal board (Fig. 5.1).

First, we introduce the cylindrical coordinates, Then, we will define a cylindrical frame attached to the material point. We shall see that we have to take into account the displacement of the frame attached to the material point. Therefore, it is necessary to take into account the motion of the cylindrical frame with respect to the Cartesian frame. The Cartesian frame is a fixed frame whereas the cylindrical frame is a moving frame. Then, we will be able to express the kinematical quantities like the position, the velocity and the acceleration with respect to the cylindrical frame.

The cylindrical coordinates $(\rho, \phi, z)$ of a material point $P$ are three scalar quantities. The first coordinate is the distance $\rho$ between the origin $O$ and the point obtained by projection of point $P$ on the horizontal plane containing $O$. The second coordinate is the angle $\phi$ that determines the orientation of the vertical plane containing points $O$ and $P$. The third
coordinate is the height $z$ of the plane containing point $P$, i.e. the distance between the horizontal planes containing the origin $O$ and the material point $P$ respectively (Fig. 5.2). The Cartesian coordinates $\left(x_{1}, x_{2}, x_{3}\right)$ are expressed in terms of the cylindrical coordinates $(\rho, \phi, z)$ as,

$$
\begin{equation*}
x_{1}=\rho \cos \phi \quad x_{2}=\rho \sin \phi \quad x_{3}=z \tag{5.1}
\end{equation*}
$$

In order to be able to define the frames associated to the cylindrical coordinates, we introduce the notion of coordinate line. A coordinate line is the locus of points that have two fixed coordinates. Fixing two coordinates, we impose two mathematical constraints - i.e. two equations - in a three dimensional space which defines a line or a curve, that corresponds to the coordinate line. A coordinate line is oriented in the increasing direction of the varying coordinate. In cylindrical coordinates, the first line of coordinates $(\phi, z)$ is the horizontal and radial half-line of angle $\phi$ contained in the horizontal plane at height $z$. The second line of coordinates $(z, \rho)$ is the horizontal circle of radius $\rho$ at height $z$. The third line of coordinates $(\rho, \phi)$ is the vertical half-line contained in the vertical plane of orientation angle $\phi$, separated from the origin $O$ by a distance $\rho$ (Fig. 5.3).

### 5.1.1 Cylindrical frame

Now, we are able to define the cylindrical frame $\left(P, \boldsymbol{e}_{\rho}, \boldsymbol{e}_{\phi}, \boldsymbol{e}_{z}\right)$ attached to the material point $P$ that is a direct orthonormal frame geometrically built along the lines of coordinates. The first vector $\boldsymbol{e}_{\rho}$ is a unit vector oriented along the first line of coordinates $(\phi, z)$ where $\rho$ varies. The second vector $\boldsymbol{e}_{\phi}$ is a unit vector tangent to the second line of coordinates
$(z, \rho)$ where $\phi$ varies. The third vector $\boldsymbol{e}_{z}$ is a unit vector oriented along the third line of coordinates $(\rho, \phi)$ where $z$ varies (Fig. 5.4). Since the frame is orthonormal, the basis vectors are orthogonal unit vectors,

$$
\begin{align*}
& \boldsymbol{e}_{\rho} \cdot \boldsymbol{e}_{\rho}=\boldsymbol{e}_{\phi} \cdot \boldsymbol{e}_{\phi}=\boldsymbol{e}_{z} \cdot \boldsymbol{e}_{z}=1 \\
& \boldsymbol{e}_{\rho} \cdot \boldsymbol{e}_{\phi}=\boldsymbol{e}_{\phi} \cdot \boldsymbol{e}_{z}=\boldsymbol{e}_{z} \cdot \boldsymbol{e}_{\rho}=0 \tag{5.2}
\end{align*}
$$

Moreover, this frame is direct. This means that these vectors satisfy the right hand rule,

$$
\boldsymbol{e}_{\rho} \times \boldsymbol{e}_{\phi}=\boldsymbol{e}_{z} \quad \boldsymbol{e}_{\phi} \times \boldsymbol{e}_{z}=\boldsymbol{e}_{\rho} \quad \boldsymbol{e}_{z} \times \boldsymbol{e}_{\rho}=\boldsymbol{e}_{\phi}
$$

The basis vectors of the cylindrical frame are expressed in terms of basis vectors of the Cartesian frame as,

$$
\begin{align*}
& \boldsymbol{e}_{\rho}=\cos \phi \boldsymbol{e}_{1}+\sin \phi \boldsymbol{e}_{2} \\
& \boldsymbol{e}_{\phi}=-\sin \phi \boldsymbol{e}_{1}+\cos \phi \boldsymbol{e}_{2}  \tag{5.4}\\
& \boldsymbol{e}_{z}=\boldsymbol{e}_{3}
\end{align*}
$$

The cylindrical frame $\left(P, \boldsymbol{e}_{\rho}, \boldsymbol{e}_{\phi}, \boldsymbol{e}_{z}\right)$ is a moving frame attached to a material point, which means that the basis vectors can change their orientation over time according to the motion of the material point $P$. The vectors $\boldsymbol{e}_{\rho}$ and $\boldsymbol{e}_{\phi}$ change their orientation when the angle $\phi$ changes whereas the vector $\boldsymbol{e}_{z}$ keeps its vertical orientation at all times.

### 5.1.2 Position vector

The cylindrical frame is a moving frame attached to the material point $P$ and rotating around a vertical axis. Thus, the orientation of the unit vectors $\boldsymbol{e}_{\rho}$ and $\boldsymbol{e}_{\phi}$ changes over time. The position vector $\boldsymbol{r}=\boldsymbol{O P}$ of the material point $P$ can be expressed as the vectorial sum of the horizontal vector $\boldsymbol{O} \boldsymbol{P}^{\prime}$ and the vertical vector $\boldsymbol{P}^{\prime} \boldsymbol{P}$ where point $P^{\prime}$ is the projection of point $P$ on the horizontal plane containing the origin $O$. Vector $\boldsymbol{O} \boldsymbol{P}^{\prime}$ has a norm $\rho$ and it is collinear to the unit vector $\boldsymbol{e}_{\rho}$. Vector $\boldsymbol{P}^{\prime} \boldsymbol{P}$ has a norm $z$ and it is collinear to the unit vector $\boldsymbol{e}_{z}$. Thus, the position vector $\boldsymbol{r}$ of the material point $P$ in cylindrical coordinates is written as,

$$
\begin{equation*}
\boldsymbol{r}=\rho \boldsymbol{e}_{\rho}+z \boldsymbol{e}_{z} \tag{5.5}
\end{equation*}
$$

where the unit vector $\boldsymbol{e}_{\rho}$ is a function of the angle $\phi$ according to the first relation (5.4). Therefore, the position vector $\boldsymbol{r}$ is a function of the cylindrical coordinates $\rho, \phi$ and $z$.

### 5.1.3 Velocity vector

When the norm or the orientation of a vector changes over time its time derivative is non zero. The basis vectors $\boldsymbol{e}_{1}, \boldsymbol{e}_{2}$ and $\boldsymbol{e}_{3}$ of the Cartesian frame are unit vectors, which means that their norm is constant. Since the Cartesian frame is fixed its orientation is also constant. Thus, the time derivatives of the basis vectors of the Cartesian frame vanish. The basis vectors $\boldsymbol{e}_{\rho}, \boldsymbol{e}_{\phi}$ and $\boldsymbol{e}_{z}$ of the cylindrical frame are unit vectors, which means that their norm is constant. Since the cylindrical frame is moving its orientation changes. Thus, the time derivative of the basis vectors of the cylindrical frame can be non zero. The time derivatives of the expressions (5.4) of the basis vectors of the cylindrical frame are written,

$$
\begin{align*}
& \dot{\boldsymbol{e}}_{\rho}=\dot{\phi}\left(-\sin \phi \boldsymbol{e}_{1}+\cos \phi \boldsymbol{e}_{2}\right)=\dot{\phi} \boldsymbol{e}_{\phi} \\
& \dot{\boldsymbol{e}}_{\phi}=-\dot{\phi}\left(\cos \phi \boldsymbol{e}_{1}+\sin \phi \boldsymbol{e}_{2}\right)=-\dot{\phi} \boldsymbol{e}_{\rho}  \tag{5.6}\\
& \dot{\boldsymbol{e}}_{z}=\mathbf{0}
\end{align*}
$$

The velocity vector $\boldsymbol{v}$ is the time derivative of the position vector $\boldsymbol{r}$. The time derivative of the position vector (5.5) expressed in cylindrical coordinates yields,

$$
\begin{equation*}
\boldsymbol{v}=\dot{\boldsymbol{r}}=\dot{\rho} \boldsymbol{e}_{\rho}+\rho \dot{\boldsymbol{e}}_{\rho}+\dot{z} \boldsymbol{e}_{z}+z \dot{\boldsymbol{e}}_{z} \tag{5.7}
\end{equation*}
$$

Taking into account the expressions (5.6) for the time derivative of the basis vectors, the velocity vector (5.7) reduces to,

$$
\begin{equation*}
\boldsymbol{v}=\dot{\rho} \boldsymbol{e}_{\rho}+\rho \dot{\phi} \boldsymbol{e}_{\phi}+\dot{z} \boldsymbol{e}_{z} \tag{https://cdn.mathpix.com/cropped/2024_05_18_56557b7d0de9d4b5fad4g-04.jpg?height=52&width=77&top_left_y=1122&top_left_x=1796}
\end{equation*}
$$

The geometric interpretation of the velocity vector (5.8) expressed in cylindrical coordinates is the following : the term $\dot{\rho}$ is the horizontal radial velocity, the term $\rho \dot{\phi}$ is the horizontal tangential velocity and the term $\dot{z}$ is the vertical velocity.

### 5.1.4 Acceleration vector

The acceleration vector $\boldsymbol{a}$ is the time derivative of the velocity vector $\boldsymbol{a}$. Taking the time derivative of the velocity vector (5.8) expressed in cylindrical coordinates, we obtain

$$
\begin{equation*}
\boldsymbol{a}=\dot{\boldsymbol{v}}=\ddot{\rho} \boldsymbol{e}_{\rho}+\dot{\rho} \dot{\boldsymbol{e}}_{\rho}+(\dot{\rho} \dot{\phi}+\rho \ddot{\phi}) \boldsymbol{e}_{\phi}+\rho \dot{\phi} \dot{\boldsymbol{e}}_{\phi}+\ddot{z} \boldsymbol{e}_{z}+\dot{z} \dot{\boldsymbol{e}}_{z} \tag{5.9}
\end{equation*}
$$

Taking into account expressions (5.6) for the time derivative of the basis vectors, the acceleration vector $(5.9)$ reduces to,

$$
\begin{equation*}
\boldsymbol{a}=\left(\ddot{\rho}-\rho \dot{\phi}^{2}\right) \boldsymbol{e}_{\rho}+(\rho \ddot{\phi}+2 \dot{\rho} \dot{\phi}) \boldsymbol{e}_{\phi}+\ddot{z} \boldsymbol{e}_{z} \tag{https://cdn.mathpix.com/cropped/2024_05_18_56557b7d0de9d4b5fad4g-04.jpg?height=48&width=91&top_left_y=1799&top_left_x=1779}
\end{equation*}
$$

The geometric interpretation of the acceleration vector (5.10) expressed in cylindrical coordinates is the following : the term $\ddot{\rho}$ is the radial acceleration, the term $\rho \dot{\phi}^{2}$ is the centripetal acceleration, the term $\rho \ddot{\phi}$ is the tangential acceleration, the term $2 \dot{\rho} \dot{\phi}$ is the Coriolis acceleration and the term $\ddot{z}$ is the vertical acceleration.

### 5.2 Spherical coordinates

The spherical coordinates are an appropriate choice to describe a motion that has a spherical symmetry in space. It is for instance the case for a ball that moves in a rotating hemispherical ring (Fig. 5.5).

The spherical coordinates $(r, \theta, \phi)$ of a material point $P$ are three scalar quantities. The first coordinate is the distance $r$ between the origin $O$ and the material point $P$. The second coordinate is the angle $\theta$ that determines the inclination of the line that connects the points $O$ and $P$ with respect to the vertical axis. The third coordinate is the angle $\phi$ that determines the orientation of the plane containing points $O$ and $P$ (Fig. 5.6). The Cartesian coordinates $\left(x_{1}, x_{2}, x_{3}\right)$ are expressed in terms of the spherical coordinates $(r, \theta, \phi)$ as,

$$
\begin{equation*}
x_{1}=r \sin \theta \cos \phi \quad x_{2}=r \sin \theta \sin \phi \quad x_{3}=r \cos \theta \tag{5.11}
\end{equation*}
$$

In spherical coordinates, the first line of coordinates $(\theta, \phi)$ is the line inclined by an angle $\theta$ with respect the vertical axis contained in the vertical plane of orientation angle $\phi$. The second line of coordinates $(\phi, r)$ is the circle of radius $r$ contained in the vertical plane of orientation angle $\phi$. The third line of coordinates $(r, \theta)$ is the circle of radius $r \sin \theta$ contained in the horizontal plane at height $r \cos \theta$ (Fig. 5.7).

### 5.2.1 Spherical frame

Now, we are able to define the spherical frame $\left(P, \boldsymbol{e}_{r}, \boldsymbol{e}_{\theta}, \boldsymbol{e}_{\phi}\right)$ attached to the material point $P$ that is a direct orthonormal frame built geometrically on the lines of coordinates. The first vector $\boldsymbol{e}_{r}$ is a unit vector oriented along the first line of coordinates $(\theta, \phi)$ where $\rho$ varies. The second vector $\boldsymbol{e}_{\theta}$ is a unit vector tangent to the second line of coordinates $(\phi, r)$ where $\theta$ varies. The third vector $\boldsymbol{e}_{\phi}$ is a unit vector tangent to the third line of coordinates $(r, \theta)$ where $z$ varies (Fig. 5.8). Since the frame is orthonormal, the basis vectors are orthogonal unit vectors,

$$
\begin{align*}
& \boldsymbol{e}_{r} \cdot \boldsymbol{e}_{r}=\boldsymbol{e}_{\theta} \cdot \boldsymbol{e}_{\theta}=\boldsymbol{e}_{\phi} \cdot \boldsymbol{e}_{\phi}=1  \tag{5.12}\\
& \boldsymbol{e}_{r} \cdot \boldsymbol{e}_{\theta}=\boldsymbol{e}_{\theta} \cdot \boldsymbol{e}_{\phi}=\boldsymbol{e}_{\phi} \cdot \boldsymbol{e}_{r}=0
\end{align*}
$$

Moreover, this frame is direct. This means that these vectors satisfy the right hand rule,

$$
\begin{equation*}
\boldsymbol{e}_{r} \times \boldsymbol{e}_{\theta}=\boldsymbol{e}_{\phi} \quad \boldsymbol{e}_{\theta} \times \boldsymbol{e}_{\phi}=\boldsymbol{e}_{r} \quad \boldsymbol{e}_{\phi} \times \boldsymbol{e}_{r}=\boldsymbol{e}_{\theta} \tag{5.13}
\end{equation*}
$$

The basis vectors of the spherical frame are expressed in terms of the basis vectors of the Cartesian frame as,

$$
\begin{align*}
& \boldsymbol{e}_{r}=\sin \theta \cos \phi \boldsymbol{e}_{1}+\sin \theta \sin \phi \boldsymbol{e}_{2}+\cos \theta \boldsymbol{e}_{3} \\
& \boldsymbol{e}_{\theta}=\cos \theta \cos \phi \boldsymbol{e}_{1}+\cos \theta \sin \phi \boldsymbol{e}_{2}-\sin \theta \boldsymbol{e}_{3}  \tag{5.14}\\
& \boldsymbol{e}_{\phi}=-\sin \phi \boldsymbol{e}_{1}+\cos \phi \boldsymbol{e}_{2}
\end{align*}
$$

The spherical frame $\left(P, \boldsymbol{e}_{r}, \boldsymbol{e}_{\theta}, \boldsymbol{e}_{\phi}\right)$ is a moving frame attached to the material point $P$, which means that the basis vectors can change their orientation over time according to the motion of the material point $P$. The vectors $\boldsymbol{e}_{r}$ and $\boldsymbol{e}_{\theta}$ change their orientation when the angles $\theta$ and $\phi$ change and the vector $\boldsymbol{e}_{\phi}$ changes its orientation when the angle $\phi$ changes.

### 5.2.2 Position vector

The spherical frame is a moving frame attached to the material point $P$ and rotating around a vertical and a horizontal axis. Thus, the orientation of the unit vectors $\boldsymbol{e}_{r}, \boldsymbol{e}_{\theta}$ and $\boldsymbol{e}_{\phi}$ changes over time. The position vector $\boldsymbol{r}=\boldsymbol{O} \boldsymbol{P}$ has a norm $r$ and it is collinear to the radial unit vector $\boldsymbol{e}_{r}$. Thus, the position vector $\boldsymbol{r}$ of the material point $P$ in spherical coordinates is written as,

$$
\begin{equation*}
\boldsymbol{r}=r \boldsymbol{e}_{r} \tag{5.15}
\end{equation*}
$$

where the unit vector $\boldsymbol{e}_{r}$ is a function of the angles $\theta$ and $\phi$ according to the first relation (5.14). Therefore, the position vector $\boldsymbol{r}$ is a function of the spherical coordinates $r, \theta$ and $\phi$.

### 5.2.3 Velocity vector

The basis vectors $\boldsymbol{e}_{r}, \boldsymbol{e}_{\theta}$ and $\boldsymbol{e}_{\phi}$ of the spherical frame are unit vectors, which means that their norm is constant. Since the spherical frame is moving its orientation changes. Thus, the time derivative of the basis vectors of the spherical frame can be non zero. The time derivatives of the expressions (5.14) of the basis vectors of the spherical frame are written,

$$
\begin{align*}
\dot{\boldsymbol{e}}_{r} & =\dot{\theta}\left(\cos \theta \cos \phi \boldsymbol{e}_{1}+\cos \theta \sin \phi \boldsymbol{e}_{2}-\sin \theta \boldsymbol{e}_{3}\right)+\dot{\phi} \sin \theta\left(-\sin \phi \boldsymbol{e}_{1}+\cos \phi \boldsymbol{e}_{2}\right) \\
& =\dot{\theta} \boldsymbol{e}_{\theta}+\dot{\phi} \sin \theta \boldsymbol{e}_{\phi} \\
\dot{\boldsymbol{e}}_{\theta} & =-\dot{\theta}\left(\sin \theta \cos \phi \boldsymbol{e}_{1}+\sin \theta \sin \phi \boldsymbol{e}_{2}+\cos \theta \boldsymbol{e}_{3}\right)+\dot{\phi} \cos \theta\left(-\sin \phi \boldsymbol{e}_{1}+\cos \phi \boldsymbol{e}_{2}\right)  \tag{5.16}\\
& =-\dot{\theta} \boldsymbol{e}_{r}+\dot{\phi} \cos \theta \boldsymbol{e}_{\phi} \\
\dot{\boldsymbol{e}}_{\phi} & =-\dot{\phi}\left(\cos \phi \boldsymbol{e}_{1}+\sin \phi \boldsymbol{e}_{2}\right)=-\dot{\phi} \boldsymbol{e}_{\rho}=-\dot{\phi}\left(\sin \theta \boldsymbol{e}_{r}+\cos \theta \boldsymbol{e}_{\theta}\right)
\end{align*}
$$

where the last expression is deduced by graphical inspection (Fig. 5.9). The velocity vector
$\boldsymbol{v}$ is the time derivative of the position vector $\boldsymbol{r}$. Taking the time derivative of the position vector (5.15) expressed in spherical coordinates, we obtain,

$$
\begin{equation*}
\boldsymbol{v}=\dot{\boldsymbol{r}}=\dot{r} \boldsymbol{e}_{r}+r \dot{\boldsymbol{e}}_{r} \tag{5.17}
\end{equation*}
$$

Taking into account the expression (5.16) of time derivative of the first basis vector, the velocity vector (5.17) reduces to

$$
\begin{equation*}
\boldsymbol{v}=\dot{\boldsymbol{r}} \boldsymbol{e}_{r}+r \dot{\theta} \boldsymbol{e}_{\theta}+r \dot{\phi} \sin \theta \boldsymbol{e}_{\phi} \tag{5.18}
\end{equation*}
$$

The geometric interpretation of the velocity vector (5.18) expressed in spherical coordinates is the following : the term $\dot{r}$ is the radial velocity, the term $r \dot{\theta}$ is the vertical tangential velocity and the term $r \dot{\phi} \sin \theta$ is the horizontal tangential velocity.

### 5.2.4 Acceleration vector

The acceleration vector $\boldsymbol{a}$ is the time derivative of the velocity vector $\boldsymbol{v}$. Taking the time derivative of the velocity (5.18) expressed in spherical coordinates, we obtain

$\boldsymbol{a}=\dot{\boldsymbol{v}}=\ddot{\boldsymbol{r}} \boldsymbol{e}_{r}+\dot{\boldsymbol{r}} \dot{\boldsymbol{e}}_{r}+(\dot{r} \dot{\theta}+r \ddot{\theta}) \boldsymbol{e}_{\theta}+r \dot{\theta} \dot{\boldsymbol{e}}_{\theta}+(\dot{r} \dot{\phi} \sin \theta+r \ddot{\phi} \sin \theta+r \dot{\phi} \dot{\theta} \cos \theta) \boldsymbol{e}_{\phi}+r \dot{\phi} \sin \theta \dot{\boldsymbol{e}}_{\phi}$

Taking into account the expressions (5.16) of the time derivative of the basis vectors, the acceleration vector (5.19) becomes,

$$
\begin{align*}
\boldsymbol{a}= & \left(\ddot{\boldsymbol{r}}-r \dot{\theta}^{2}-r \dot{\phi}^{2} \sin ^{2} \theta\right) \boldsymbol{e}_{r}+\left(r \ddot{\theta}+2 \dot{\boldsymbol{r}} \dot{\theta}-r \dot{\phi}^{2} \sin \theta \cos \theta\right) \boldsymbol{e}_{\theta}  \tag{5.20}\\
& +(r \ddot{\phi} \sin \theta+2 \dot{\boldsymbol{r}} \dot{\phi} \sin \theta+2 r \dot{\phi} \dot{\theta} \cos \theta) \boldsymbol{e}_{\phi}
\end{align*}
$$

The physical interpretation of the acceleration vector (5.20) expressed in spherical coordinates is the following : the term $\ddot{r}$ is the radial acceleration, the term $r \dot{\theta}^{2}$ is the centripetal acceleration in the vertical plane, the term $r \dot{\phi}^{2} \sin ^{2} \theta$ is the radial projection of the centripetal acceleration in the horizontal plane, the term $r \ddot{\theta}$ is the tangential acceleration in the vertical plane, the term $2 \dot{r} \dot{\theta}$ is the nodal component of the Coriolis acceleration, the term $r \dot{\phi}^{2} \sin \theta \cos \theta$ is the tangential projection of the centripetal acceleration in the horizontal plane, the term $r \ddot{\phi} \sin \theta$ is the tangential acceleration in the horizontal plane, the terms $2 \dot{r} \dot{\phi} \sin \theta$ and $2 r \dot{\phi} \dot{\theta} \cos \theta$ are the azimuthal components of the Coriolis acceleration.

### 5.3 Rotations

In dynamics, an arbitrary motion can be expressed as the combination of a translational and a rotational motion. Two types of rotational motion have to be distinguished. The first is the rotational motion of a material point - circular motion for instance - and the second is the rotational motion of a rigid body on itself. In this section, we shall only consider the first type of rotational motion. The notion of rotation of a material point involves an axis and a rotation angle. The orientation of the axis is defined by the corkscrew rule characterised mathematically by the vectorial product.

The notion of rotation is very intuitive, which is not the case of its formal expression. In this section, we shall formalise this notation and express it in a rigorous mathematical language. The notion of rotation is central to describe the dynamics with respect to a cylindrical or spherical frame. The reason is the following : these frames are moving and in rotation around one or several axes. These frames simplify the mathematical expression of the dynamics by taking into account the symmetries of motion.

### 5.3.1 Rotation of a moving direct frame

We would like to define the time derivative of the position vector $\boldsymbol{r}$ of a material point at rest with respect to a moving direct frame $\left(P, \boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3}\right)$ attached to the material point $P$. The translational motions do not change the orientation of the frame, only the rotational motions can change the orientation of the unit basis vectors of the frame. Thus, we begin by determining the time evolution of the unit vectors of the frame during an orientation change. The basis vectors are unit vectors. Thus,

$$
\begin{equation*}
\boldsymbol{e}_{i} \cdot \boldsymbol{e}_{i}=1 \quad \forall \quad i=1,2,3 \tag{5.21}
\end{equation*}
$$

The time derivative of equation (5.21) is written explicitly as,

$$
\begin{equation*}
\dot{\boldsymbol{e}}_{i} \cdot \boldsymbol{e}_{i}+\boldsymbol{e}_{i} \cdot \dot{\boldsymbol{e}}_{i}=0 \quad \text { thus } \quad \dot{\boldsymbol{e}}_{i} \cdot \boldsymbol{e}_{i}=0 \quad \forall \quad i=1,2,3 \tag{5.22}
\end{equation*}
$$

Hence, the time derivative of the basis vectors is orthogonal to the basis vectors since they are unit vectors. We have already seen this fact for the basis vectors of the cylindrical and spherical frame. According to equation (5.22), there must be scalar quantities $\omega_{i j}$ such that,

$$
\begin{equation*}
\dot{\boldsymbol{e}}_{i}=\sum_{j=1}^{3} \omega_{i j} \boldsymbol{e}_{j} \quad \text { where } \quad \omega_{i i}=0 \quad \forall i=1,2,3 \tag{5.23}
\end{equation*}
$$

The basis vectors are orthogonal. Thus,

$$
\begin{equation*}
\boldsymbol{e}_{i} \cdot \boldsymbol{e}_{k}=\delta_{i k} \quad \forall \quad i, k=1,2,3 \tag{5.24}
\end{equation*}
$$

The time derivative of equation (5.24) is written explicitly as,

$$
\begin{equation*}
\dot{\boldsymbol{e}}_{i} \cdot \boldsymbol{e}_{k}+\boldsymbol{e}_{i} \cdot \dot{\boldsymbol{e}}_{k}=0 \quad \forall \quad i, k=1,2,3 \tag{5.25}
\end{equation*}
$$

The substitution of expression (5.23) into equation (5.25) yields

$$
\begin{equation*}
\left(\sum_{j=1}^{3} \omega_{i j} \boldsymbol{e}_{j}\right) \cdot \boldsymbol{e}_{k}+\boldsymbol{e}_{i} \cdot\left(\sum_{j=1}^{3} \omega_{k j} \boldsymbol{e}_{j}\right)=0 \quad \forall i, k=1,2,3 \tag{5.26}
\end{equation*}
$$

Taking into account the orthogonality relation (5.24), equation (5.26) reduces to,

$$
\begin{equation*}
\omega_{i k}+\omega_{k i}=0 \quad \text { thus } \quad \omega_{k i}=-\omega_{i k} \quad \forall \quad i, k=1,2,3 \tag{5.27}
\end{equation*}
$$

### 5.3.2 Poisson's formulae

According to relation (5.23), there is a linear application that sends the vector $\left(\boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3}\right)$ onto the vector $\left(\dot{\boldsymbol{e}}_{1}, \dot{\boldsymbol{e}}_{2}, \dot{\boldsymbol{e}}_{3}\right)$. Taking into account the condition (5.27), this linear application is represented by an antisymmetric $3 \times 3$ matrix. It is written explicitly,

$$
\left(\begin{array}{l}
\dot{e}_{1}  \tag{5.28}\\
\dot{e}_{2} \\
\dot{e}_{3}
\end{array}\right)=\left(\begin{array}{ccc}
0 & \omega_{12} & \omega_{13} \\
-\omega_{12} & 0 & \omega_{23} \\
-\omega_{13} & -\omega_{23} & 0
\end{array}\right)\left(\begin{array}{l}
e_{1} \\
e_{2} \\
e_{3}
\end{array}\right)
$$

The antisymmetric matrix is determined by three independent scalar quantities, i.e. $\omega_{12}$, $\omega_{13}$ and $\omega_{23}$. The change in orientation of the unit vectors of the moving frame is due to the rotation of the frame. This rotation is described by the angular velocity vector $\boldsymbol{\omega}$ that has three scalar components. In order for the angular velocity vector $\boldsymbol{\omega}$ to be oriented according to the corkscrew rule during the frame rotation, the components $\omega_{1}, \omega_{2}$ and $\omega_{3}$ of vector $\boldsymbol{\omega}$ are defined as,

$$
\omega_{1} \equiv \omega_{23} \quad \text { and } \quad \omega_{2} \equiv \omega_{31}=-\omega_{13} \quad \text { and } \quad \omega_{3} \equiv \omega_{12}
$$

Thus, the linear application (5.28) is recast as,

$$
\left(\begin{array}{l}
\dot{\boldsymbol{e}}_{1}  \tag{5.29}\\
\dot{\boldsymbol{e}}_{2} \\
\dot{\boldsymbol{e}}_{3}
\end{array}\right)=\left(\begin{array}{ccc}
0 & \omega_{3} & -\omega_{2} \\
-\omega_{3} & 0 & \omega_{1} \\
\omega_{2} & -\omega_{1} & 0
\end{array}\right)\left(\begin{array}{l}
\boldsymbol{e}_{1} \\
\boldsymbol{e}_{2} \\
\boldsymbol{e}_{3}
\end{array}\right)
$$

The three components of the linear application (5.29) are written as,

$$
\begin{equation*}
\dot{\boldsymbol{e}}_{1}=\omega_{3} \boldsymbol{e}_{2}-\omega_{2} \boldsymbol{e}_{3} \quad \dot{\boldsymbol{e}}_{2}=\omega_{1} \boldsymbol{e}_{3}-\omega_{3} \boldsymbol{e}_{1} \quad \dot{\boldsymbol{e}}_{3}=\omega_{2} \boldsymbol{e}_{1}-\omega_{1} \boldsymbol{e}_{2} \tag{https://cdn.mathpix.com/cropped/2024_05_18_56557b7d0de9d4b5fad4g-09.jpg?height=49&width=95&top_left_y=1363&top_left_x=1483}
\end{equation*}
$$

The angular velocity vector $\boldsymbol{\omega}$ is expressed explicitly in components with respect to the moving frame as,

$$
\begin{equation*}
\boldsymbol{\omega}=\omega_{1} \boldsymbol{e}_{1}+\omega_{2} \boldsymbol{e}_{2}+\omega_{3} \boldsymbol{e}_{3} \tag{https://cdn.mathpix.com/cropped/2024_05_18_56557b7d0de9d4b5fad4g-09.jpg?height=49&width=97&top_left_y=1529&top_left_x=1479}
\end{equation*}
$$

Taking into account the expression (5.31) of the angular velocity vector, equations (5.30) can be recast as,

$$
\begin{equation*}
\dot{e}_{1}=\boldsymbol{\omega} \times \boldsymbol{e}_{1} \quad \dot{e}_{2}=\boldsymbol{\omega} \times \boldsymbol{e}_{2} \quad \dot{e}_{3}=\boldsymbol{\omega} \times \boldsymbol{e}_{3} \tag{https://cdn.mathpix.com/cropped/2024_05_18_56557b7d0de9d4b5fad4g-09.jpg?height=54&width=95&top_left_y=1698&top_left_x=1483}
\end{equation*}
$$

and are called Poisson's formulae,

$$
\begin{equation*}
\dot{\boldsymbol{e}}_{i}=\boldsymbol{\omega} \times \boldsymbol{e}_{i} \quad \forall \quad i=1,2,3 \tag{5.33}
\end{equation*}
$$

since they were established by Siméon Denis Poisson.

### 5.3.3 Rotation of the position vector

We consider a material point at rest with respect to a rotating frame in the absence of translation. In this frame, the position vector of the material point is written explicitly as,

$$
\begin{equation*}
\boldsymbol{r}=r_{1} \boldsymbol{e}_{1}+r_{2} \boldsymbol{e}_{2}+r_{3} \boldsymbol{e}_{3} \quad \text { where } \quad \dot{r}_{1}=\dot{r}_{2}=\dot{r}_{3}=0 \tag{https://cdn.mathpix.com/cropped/2024_05_18_56557b7d0de9d4b5fad4g-09.jpg?height=46&width=95&top_left_y=2170&top_left_x=1483}
\end{equation*}
$$

because there is no relative motion with respect to the frame. The velocity vector $\boldsymbol{v}$ is obtained by taking the time derivative of the position vector $\boldsymbol{r}$,

$$
\begin{equation*}
\boldsymbol{v}=\dot{\boldsymbol{r}}=r_{1} \dot{\boldsymbol{e}}_{1}+r_{2} \dot{\boldsymbol{e}}_{2}+r_{3} \dot{\boldsymbol{e}}_{3} \tag{5.35}
\end{equation*}
$$

Taking into account Poisson's formulae (5.32) and the expression (5.34) of the position vector $\boldsymbol{r}$, the expression (5.35) of the velocity vector $\boldsymbol{v}$ can be recast as,

$$
\begin{equation*}
\boldsymbol{v}=r_{1}\left(\boldsymbol{\omega} \times \boldsymbol{e}_{1}\right)+r_{2}\left(\boldsymbol{\omega} \times \boldsymbol{e}_{2}\right)+r_{3}\left(\boldsymbol{\omega} \times \boldsymbol{e}_{3}\right)=\boldsymbol{\omega} \times\left(r_{1} \boldsymbol{e}_{1}+r_{2} \boldsymbol{e}_{2}+r_{3} \boldsymbol{e}_{3}\right)=\boldsymbol{\omega} \times \boldsymbol{r} \tag{https://cdn.mathpix.com/cropped/2024_05_18_56557b7d0de9d4b5fad4g-09.jpg?height=51&width=97&top_left_y=2513&top_left_x=1479}
\end{equation*}
$$

Thus, in the absence of translation, the expression of the velocity vector (5.36) is the same as the one obtained in the case of a circular motion (4.71). This is not surprising because a

### 5.3.4 Polar and axial vectors

There are three fundamental symmetries in physics. The time reversal symmetry $T$, the parity symmetry $P$ and the charge conjugation symmetry $C$. A theorem of quantum mechanics, established by Julian Schwinger in 1951, called the CPT theorem, states that the product of these three symmetries has never been violated during an interaction between elementary particles. In other words, the physical laws do not change when the particles involved in an interaction are replaced by their antiparticle, the three directions of space are reversed and time is reversed. It is known that nature violates the $C P$ symmetry, but there is no experimental violation of the $C P T$ symmetry. Such a violation would be be contrary to the theory of special relativity. The linear application of parity sends the basis vectors $\left(\boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3}\right)$ onto their opposite,

$$
\begin{equation*}
\left(e_{1}, e_{2}, e_{3}\right) \longrightarrow\left(-e_{1},-e_{2},-e_{3}\right) \tag{5.37}
\end{equation*}
$$

The polar vectors change sign under the parity linear application. For instance, we could mention the position vector $\boldsymbol{r}$, the velocity vector $\boldsymbol{v}$, the acceleration vector $\boldsymbol{a}$, the momentum vector $\boldsymbol{p}$ and the force vector $\boldsymbol{F}$, that transform under the parity application as,

$$
\begin{array}{lll}
r \longrightarrow-r & v \longrightarrow-v & a \longrightarrow-a \\
p \longrightarrow-p & F \longrightarrow-F &
\end{array}
$$

The axial vectors do not change sign under the parity linear application. For instance, we can mention the angular velocity vector $\boldsymbol{\omega}$, the angular momentum vector $\boldsymbol{L}$ and the torque $\tau$ that we will define later,

$$
\begin{equation*}
\omega \longrightarrow \omega \quad L \longrightarrow L \quad \tau \quad \tau \longrightarrow \tau \tag{5.39}
\end{equation*}
$$

The scalar product of two polar vectors or two axial vectors yields a scalar. If the two
vectors are identical, this scalar is the square of the norm of the vector. According to the definitions (5.38) and (5.39), the vectorial product of two polar vectors yields an axial vector and the vectorial product of one polar vector and one axial vector yields a polar vector (Fig. 5.10).

