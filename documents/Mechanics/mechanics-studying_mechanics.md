# Studying mechanics 

### 1.2 Derivatives

### 1.2.1 Derivatives of a function

In the context of mechanics, we seek most often to determine the time evolution of a system. We consider here functions of time $t$, which we assume to be a real continuous parameter, i.e. $t \in \mathbb{R}$. As an example, we choose as a function of time $t$ the position coordinate $x(t)$ along a fixed axis. We assume that the position coordinate is a continuous and twice differentiable function i.e. $x(t) \in \mathcal{C}^{2}(\mathbb{R})$. The scalar velocity or speed $v(t)$ along the coordinate axis is defined as the derivative of the position coordinate $x(t)$ with respect to time $t$. It is written explicitly,

$$
\begin{equation*}
v(t)=\lim _{\Delta t \rightarrow 0} \frac{\Delta x(t)}{\Delta t}=\lim _{\Delta t \rightarrow 0} \frac{x(t+\Delta t)-x(t)}{\Delta t} \tag{1.1}
\end{equation*}
$$

Physicists use the letter $d$ to represent the limit of an infinitesimal variation $\Delta$. The expression (1.1) of the speed $v \equiv v(t)$ can thus be written as,

$$
\begin{equation*}
v=\frac{d x}{d t}=\frac{x(t+d t)-x(t)}{d t} \quad \text { thus } \quad d x=v d t \tag{1.2}
\end{equation*}
$$

Geometrically, the derivative $v(t)$ represents the slope of the tangent to the function $x(t)$ at time $t$ (Fig. 1.3).

In fact, in the limit of an infinitesimal variation, the time interval $\Delta t$ reduces to the infinitesimal time interval $d t$ and the coordinate variation $\Delta x$ reduces to the variation of the infinitesimal position $d x$. Taking into account equation (1.2), we showed that $d x=v d t$, which implies that the speed $v$ is indeed the slope of the time derivative of the position coordinate $x$.

The scalar acceleration $a(t)$ along the coordinate axis is defined as the time derivative of the speed $v(t)$

$$
\begin{equation*}
a(t)=\lim _{\Delta t \rightarrow 0} \frac{\Delta v(t)}{\Delta t}=\lim _{\Delta t \rightarrow 0} \frac{v(t+\Delta t)-v(t)}{\Delta t} \tag{1.3}
\end{equation*}
$$

Using the notation of the physicists, the scalar acceleration $a \equiv a(t)$ is written as,

$$
\begin{equation*}
a=\frac{d v}{d t}=\frac{v(t+d t)-v(t)}{d t} \quad \text { thus } \quad d v=a d t \tag{1.4}
\end{equation*}
$$

The scalar acceleration $a(t)$ is the second time derivative of the position coordinate $x(t)$. Substituting the expression (1.1) of the speed in the expression of the acceleration (1.3), we obtain,

$$
\begin{equation*}
a(t)=\lim _{\Delta t \rightarrow 0} \frac{\Delta\left(\lim _{\Delta t \rightarrow 0} \frac{\Delta x(t)}{\Delta t}\right)}{\Delta t} \tag{1.5}
\end{equation*}
$$

Using the notation of the physicists, the scalar acceleration $a \equiv a(t)$ is written as,

$$
\begin{equation*}
a=\frac{d\left(\frac{d x}{d t}\right)}{d t}=\frac{d}{d t}\left(\frac{d x}{d t}\right)=\frac{d^{2} x}{d t^{2}} \tag{1.6}
\end{equation*}
$$

For derivatives of a function with respect to time $t$, and only with respect to time, physicists use a shortened notation consisting in replacing the differential operator $d / d t$ by a point. Taking into account the expressions (1.2), (1.4) and (1.6), in shortened notation, the speed is written,

$$
\begin{equation*}
v=\dot{x} \tag{1.7}
\end{equation*}
$$

and the acceleration is written,

$$
\begin{equation*}
a=\dot{v}=\ddot{x} \tag{1.8}
\end{equation*}
$$

### 1.2.2 Derivative of a functionnal

A functional is a function of a function. In mechanics, we often have to determine the time derivative of the function of a function of time. Now, we consider the case where the position coordinate $x(t)$ is a functional that is defined as the composition of a function $f(g)$ and of a function $g(t)$, i.e.

$$
\begin{equation*}
x(t) \equiv f(g(t)) \tag{1.9}
\end{equation*}
$$

The time derivative of the function $g(t)$ is written,

$$
\begin{equation*}
\frac{d g}{d t}=\frac{g(t+d t)-g(t)}{d t} \quad \text { thus } \quad g(t+d t)=g(t)+d g \tag{1.10}
\end{equation*}
$$

Similarly, the derivative of the functional $f(g)$ with respect to the function $g$ is written,

$$
\begin{equation*}
\frac{d f}{d g}=\frac{f(g+d g)-f(g)}{d g} \quad \text { thus } \quad f(g+d g)=f(g)+d f=f(g)+\frac{d f}{d g} d g \tag{1.11}
\end{equation*}
$$

Taking into account the expressions (1.10) and (1.11), the derivative of the functionnal $x(t)$ with respect to time is written,

$$
\begin{equation*}
\frac{d x}{d t}=\frac{f(g(t+d t))-f(g(t))}{d t}=\frac{f(g(t)+d g)-f(g(t))}{d t}=\frac{f(g(t))+\frac{d f}{d g} d g-f(g(t))}{d t} \tag{1.12}
\end{equation*}
$$

Thus, the time derivative of the functional $x(t)$ yields the chain rule for the time derivative of the composition of functions $f(g(t))$,

$$
\begin{equation*}
\frac{d x}{d t}=\frac{d f}{d g} \frac{d g}{d t} \tag{1.13}
\end{equation*}
$$

Now, we shall consider two applications of the time derivative of a composition of functions. The first is a one-dimensional harmonic oscillator whose position coordinate is defined as,

$$
\begin{equation*}
x(t)=x_{0} \cos (\omega t+\varphi) \tag{1.14}
\end{equation*}
$$

where $x_{0}$ is the oscillation amplitude, $\omega$ is the pulsation and $\varphi$ is the dephasing angle. The quantities $x_{0}, \omega$ and $\varphi$ are constants. From the differentiation rule (1.13), we obtain the oscillation speed,

$$
\begin{equation*}
\frac{d x}{d t}=\frac{d\left(x_{0} \cos (\omega t+\varphi)\right)}{d(\omega t+\varphi)} \frac{d(\omega t+\varphi)}{d t}=-x_{0} \omega \sin (\omega t+\varphi) \tag{1.15}
\end{equation*}
$$

The second is the kinetic energy of an object of constant mass $m$ in translation along the coordinate axis $x(t)$

$$
\begin{equation*}
T(t)=\frac{1}{2} m \dot{x}^{2} \tag{1.16}
\end{equation*}
$$

From the differentiation rule (1.13), we obtain the mechanical power applied on the object,

$$
\begin{equation*}
\frac{d T}{d t}=\frac{d\left(\frac{1}{2} m \dot{x}^{2}\right)}{d \dot{x}} \frac{d \dot{x}}{d t}=m \dot{x} \ddot{x} \tag{1.17}
\end{equation*}
$$

### 1.2.3 Power series expansion of a function

The power series expansion of a function, also called Taylor expansion of a function in reference to the mathematician Brook Taylor, is an approximation of the expression of a function in the neighbourhood of a fixed value of the variable.

Taking into account equation (1.2), the function $x(t+d t)$ evaluated at time $t+d t$ is expressed in terms of the function $x(t)$ evaluated at time $t$ as,

$$
\begin{equation*}
x(t+d t)=x(t)+\frac{d x}{d t} d t \tag{1.18}
\end{equation*}
$$

In this expression, there is no approximation since the time interval $d t$ is infinitesimal. We would like to find an analogous expression when the time interval $\Delta t$ is not infinitesimal. Equivalently, equation (1.18) can be written,

$$
\begin{equation*}
\lim _{\Delta t \rightarrow 0} x(t+\Delta t)=x(t)+\lim _{\Delta t \rightarrow 0} \frac{x(t+\Delta t)-x(t)}{\Delta t} \Delta t \tag{1.19}
\end{equation*}
$$

In the case where the time interval $\Delta t$ is not infinitesimal but sufficiently small, i.e. $\Delta t \ll t$, we can make the following approximation for the time derivative,

$$
\begin{equation*}
\frac{d x}{d t} \simeq \frac{x(t+\Delta t)-x(t)}{\Delta t} \tag{1.20}
\end{equation*}
$$

In this case, equation (1.20) leads to the following approximation,

$$
\begin{equation*}
x(t+\Delta t) \simeq x(t)+\frac{d x}{d t} \Delta t \tag{1.21}
\end{equation*}
$$

called the power series expansion to first-order in $\Delta t$ of the function $x(t)$ around $t$.

### 1.3 Scalar and vector products

Now, we shall introduce the tools of vectorial geometry which are needed to study mechanics. Kinematic quantities like position, speed and acceleration are vectorial quantites, because they are characterised by a norm and a spatial orientation. In a vector space, there are two ways of multiplying vectors; either we obtain a scalar or another vector. The first product is called the scalar product - or dot product - and the second product is called the vector product - or cross product.

The vector product was introduced by Josiah Willard Gibbs in order to describe rotations in the framework of a vector space. A vector space is not necessarily the most adapted mathematical framework to study kinematics and dynamics. We could also study mechanics in the framework of geometric algebra that enables a better visualisation of phenomena but has the disadvantage to be less widespread and sometimes harder and more subtle for algebraic manipulations. However, here we shall restrict ourselves to the vector space.

### 1.3.1 Direct frame

In practice, we need often to express a vector in terms of its components projected in a frame. In space, a frame is a geometric entity consisting of three non-vanishing and

Corkscrew rule orthogonal and of unit norm. These vectors have no physical dimension. An orthonormal frame is a direct frame if it satisfies the right hand rule, i.e. if the first vector is oriented along the index of the right hand and the second vector is oriented along the middle finger then the third vector is oriented along the thumb of the right hand. This orientation is called the dextrorotatory chirality. The choice of hand is a historical convention. We could also have chosen the opposite rule of the left hand obtained by mirror image. A frame that satisfies the rule of the left hand is an indirect frame. In this course, we shall consider only direct frames. Frames can be fixed or mobile depending whether their origin and orientation change or not.

Scalars are numbers, vectors are line elements defined by a norm and an orientation and tensors - of rank 2 - are linear applications that map vectors on other vectors. It is thus useful to distinguish them. In this course, we adopt the notation convention usually used in mechanics and in physics consisting in writing the scalars in normal font, the vector in bold font and the tensors in sans-serif font.

A direct Cartesian frame is written mathematically as $\left(O, \boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3}\right)$ where $O$ is the origin and $\boldsymbol{e}_{1}, \boldsymbol{e}_{2}$ and $\boldsymbol{e}_{3}$ are the fixed basis vectors, of norm unity that are orthogonal to each other. These vectors satisfy the the right hand rule (Fig. 1.4).

An equivalent convention consists in considering the corkscrew rule. If the rotation is performed in a plane from vector $\boldsymbol{e}_{1}$ towards vector $\boldsymbol{e}_{2}$ then the corkscrew sinks along the direction defined by vector $\boldsymbol{e}_{3}$.

### 1.3.2 Scalar product

The scalar product scalar product of two vectors is a scalar obtained by multiplying identical coordinates of these vectors expressed with respect to a direct frame. We consider two vectors $\boldsymbol{a}$ and $\boldsymbol{b}$ expressed as linear combinations of the basis vectors of the direct Cartesian frame $\left(O, \boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3}\right)$

$$
\begin{align*}
& \boldsymbol{a}=a_{1} \boldsymbol{e}_{1}+a_{2} \boldsymbol{e}_{2}+a_{3} \boldsymbol{e}_{3}  \tag{1.22}\\
& \boldsymbol{b}=b_{1} \boldsymbol{e}_{1}+b_{2} \boldsymbol{e}_{2}+b_{3} \boldsymbol{e}_{3}
\end{align*}
$$

where $\left(a_{1}, a_{2}, a_{3}\right)$ and $\left(b_{1}, b_{2}, b_{3}\right)$ are the Cartesian coordinates of these vectors. The scalar product between vectors $\boldsymbol{a}$ and $\boldsymbol{b}$ is written as,

$$
\begin{equation*}
\boldsymbol{a} \cdot \boldsymbol{b}=a_{1} b_{1}+a_{2} b_{2}+a_{3} b_{3} \tag{1.23}
\end{equation*}
$$

which implies that the scalar product is commutative, i.e. the order of the vectors can be changed without changing the expression of the scalar product,

$$
\begin{equation*}
a \cdot b=b \cdot a \tag{1.24}
\end{equation*}
$$

Substituting the expressions (1.22) for vectors $\boldsymbol{a}$ and $\boldsymbol{b}$, expressed as linear combinations of the basis vectors $\boldsymbol{e}_{1}, \boldsymbol{e}_{2}$ and $\boldsymbol{e}_{3}$ of the Cartesian frame, in the definition (1.23) of the scalar
product, we conclude that the scalar product of the basis vectors is given by,

$$
\begin{equation*}
\boldsymbol{e}_{i} \cdot \boldsymbol{e}_{j}=\delta_{i j} \quad \forall i, j=1,2,3 \tag{1.25}
\end{equation*}
$$

where the Kronecker symbol is a scalar defined as

$$
\delta_{i j}=\left\{\begin{array}{lll}
1 & \text { si } & i=j  \tag{1.26}\\
0 & \text { si } & i \neq j
\end{array}\right.
$$

In order to establish important properties of the scalar product, we can consider in all generality that vectors $\boldsymbol{a}$ and $\boldsymbol{b}$ have the same origin. Vector $\boldsymbol{a}$ can be written as the vectorial sum of vector $\boldsymbol{a}_{\|}$parallel to vector $\boldsymbol{b}$ and vector $\boldsymbol{a}_{\perp}$ perpendicular to vector $\boldsymbol{b}$,

$$
\begin{equation*}
a=a_{\|}+a_{\perp} \tag{1.27}
\end{equation*}
$$

We orient the Cartesian frame $\left(O, \boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3}\right)$ such that vector $\boldsymbol{b}$ is collinear to vector $\boldsymbol{e}_{2}$, vector $\boldsymbol{a}$ is in the plane spanned by vectors $\boldsymbol{e}_{1}$ and $\boldsymbol{e}_{2}$ and the orientation of vector $\boldsymbol{e}_{3}$ is defined by the right hand rule. The origin is taken at the intersection between vectors $\boldsymbol{a}$ and $\boldsymbol{b}$. We denote $\theta$ the angle between vectors $\boldsymbol{a}$ and $\boldsymbol{b}$, and $\|\boldsymbol{a}\|$ and $\|\boldsymbol{b}\|$ their norms (Fig. 1.5).

The Cartesian coordinates of vectors $\boldsymbol{a}$ and $\boldsymbol{b}$ are respectively $(\|\boldsymbol{a}\| \sin \theta,\|\boldsymbol{a}\| \cos \theta, 0)$ and $(0,\|\boldsymbol{b}\|, 0)$. The definition (1.23) of the scalar product then implies that,

$$
\begin{equation*}
\boldsymbol{a} \cdot \boldsymbol{b}=\|\boldsymbol{a}\|\|\boldsymbol{b}\| \cos \theta \tag{1.28}
\end{equation*}
$$

The Cartesian coordinates of vectors $\boldsymbol{a}_{\|}$and $\boldsymbol{a}_{\perp}$ are respectively $(0,\|\boldsymbol{a}\| \cos \theta, 0)$ and $(\|\boldsymbol{a}\| \sin \theta, 0,0)$. The definition (1.23) of the scalar product yields the three following properties,
(i) $\boldsymbol{a} \cdot \boldsymbol{a}=\|\boldsymbol{a}\|^{2}$
(ii) $\boldsymbol{a}_{\|} \cdot \boldsymbol{b}=\boldsymbol{a} \cdot \boldsymbol{b}$
(iii) $\boldsymbol{a}_{\perp} \cdot \boldsymbol{b}=0$

### 1.3.3 Vector product

The vector product of two vectors is a vector obtained by calculating the determinant of the basis vectors of the direct frame and the coordinates of two vectors expressed with respect to this direct frame. The vector product between vectors $\boldsymbol{a}$ and $\boldsymbol{b}$ is written,

$$
\boldsymbol{a} \times \boldsymbol{b}=\left|\begin{array}{lll}
\boldsymbol{e}_{1} & a_{1} & b_{1}  \tag{1.30}\\
\boldsymbol{e}_{2} & a_{2} & b_{2} \\
\boldsymbol{e}_{3} & a_{3} & b_{3}
\end{array}\right|=\left(a_{2} b_{3}-a_{3} b_{2}\right) \boldsymbol{e}_{1}+\left(a_{3} b_{1}-a_{1} b_{3}\right) \boldsymbol{e}_{2}+\left(a_{1} b_{2}-a_{2} b_{1}\right) \boldsymbol{e}_{3}
$$

This product is written explicitly in components as,

$$
\boldsymbol{a} \times \boldsymbol{b}=\left(\begin{array}{c}
a_{2} b_{3}-a_{3} b_{2}  \tag{1.31}\\
a_{3} b_{1}-a_{1} b_{3} \\
a_{1} b_{2}-a_{2} b_{1}
\end{array}\right)
$$

which implies that the vector product is anticommutative, i.e. by changing the order of the vectors we change the sign of the expression of the vector product,

$$
\begin{equation*}
a \times b=-b \times a \tag{1.32}
\end{equation*}
$$

Substituting the expressions (1.22) for vectors $\boldsymbol{a}$ and $\boldsymbol{b}$, expressed as linear combinations of the basis vectors $\boldsymbol{e}_{1}, \boldsymbol{e}_{2}$ and $\boldsymbol{e}_{3}$ of the Cartesian frame, in the definition (1.30) of the vector product, we conclude that the vector product of the basis vectors is given by,

$$
\begin{equation*}
\boldsymbol{e}_{i} \times \boldsymbol{e}_{j}=\varepsilon_{i j k} \boldsymbol{e}_{k} \quad \forall i, j, k=1,2,3 \tag{1.33}
\end{equation*}
$$

where the components of the totally antisymmetric Levi-Civita tensor are scalars defined as,

$$
\varepsilon_{i j k}=\left\{\begin{array}{rlll}
1 & \text { for } \varepsilon_{123}, & \varepsilon_{231}, & \varepsilon_{312}  \tag{1.34}\\
-1 & \text { for } \varepsilon_{321}, & \varepsilon_{213}, & \varepsilon_{132} \\
0 & \text { otherwise } & &
\end{array}\right.
$$

Thus, $\boldsymbol{e}_{i} \times \boldsymbol{e}_{i}=0$ for every $i=1,2,3$. Some authors use the symbol $\wedge$ instead of the symbol $x$ to represent the vector product. We shall not adopt this convention here since the symbol $\wedge$ is reserved to the external product of a geometic algebra, also called Clifford algebra, whereas the vector product is defined in the framework of a vectorial space. The external product is associative whereas the vector product is not. Indeed, the definition (1.30) applied to the vector product of three vectors implies that,

$$
\begin{equation*}
\boldsymbol{a} \times(\boldsymbol{b} \times \boldsymbol{c}) \neq(\boldsymbol{a} \times \boldsymbol{b}) \times \boldsymbol{c} \tag{1.35}
\end{equation*}
$$

The vector product can be defined only in a three dimensional space. In order to establish important properties of the vector product, we can consider in all generality that vectors $\boldsymbol{a}$ and $\boldsymbol{b}$ have the same origin. We orient the Cartesian frame $\left(O, \boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3}\right)$ such that vector $\boldsymbol{b}$ is collinear to vector $\boldsymbol{e}_{2}$, vector $\boldsymbol{a}$ is in the plane spanned by vectors $\boldsymbol{e}_{1}$ and $\boldsymbol{e}_{2}$ and the orientation of vector $\boldsymbol{e}_{3}$ is defined by the right hand rule. The origin is taken at the intersection between vectors $\boldsymbol{a}$ and $\boldsymbol{b}$. We denote $\theta$ the angle between vectors $\boldsymbol{a}$ and $\boldsymbol{b}$, and $\|\boldsymbol{a}\|$ and $\|\boldsymbol{b}\|$ their norms (Fig. 1.6).

The Cartesian coordinates of vectors $\boldsymbol{a}$ and $\boldsymbol{b}$ are respectively $(\|\boldsymbol{a}\| \sin \theta,\|\boldsymbol{a}\| \cos \theta, 0)$ and $(0,\|\boldsymbol{b}\|, 0)$. The definition (1.30) of the vector product then implies that,

$$
\begin{equation*}
\boldsymbol{a} \times \boldsymbol{b}=\|\boldsymbol{a}\|\|\boldsymbol{b}\| \sin \theta \boldsymbol{e}_{3} \tag{1.36}
\end{equation*}
$$

where the angle $\theta$ is acute. The geometric interpretation of equation (1.36) is that the norm of the vector product of two vectors corresponds to the surface of the parallelogram spanned by these vectors and that its orientation is orthogonal to this surface. The Cartesian coordinates of vectors $\boldsymbol{a}_{\|}$and $\boldsymbol{a}_{\perp}$ are respectively $(\|0, \boldsymbol{a}\| \cos \theta, 0)$ et $(\|\boldsymbol{a}\| \sin \theta, 0,0)$. The definition (1.30) of the vector product yields the three following properties,
(i) $\boldsymbol{a} \times \boldsymbol{a}=\mathbf{0}$
(ii) $\boldsymbol{a}_{\|} \times \boldsymbol{b}=\mathbf{0}$
(iii) $\boldsymbol{a}_{\perp} \times \boldsymbol{b}=\boldsymbol{a} \times \boldsymbol{b}$

### 1.3.4 Triple product

We consider three vectors $\boldsymbol{a}, \boldsymbol{b}$ and $\boldsymbol{c}$ expressed as linear combinations of the basis vectors of the direct Cartesian frame $\left(O, \boldsymbol{e}_{1}, \boldsymbol{e}_{2}, \boldsymbol{e}_{3}\right)$,

$$
\begin{align*}
& \boldsymbol{a}=a_{1} \boldsymbol{e}_{1}+a_{2} \boldsymbol{e}_{2}+a_{3} \boldsymbol{e}_{3} \\
& \boldsymbol{b}=b_{1} \boldsymbol{e}_{1}+b_{2} \boldsymbol{e}_{2}+b_{3} \boldsymbol{e}_{3}  \tag{1.38}\\
& \boldsymbol{c}=c_{1} \boldsymbol{e}_{1}+c_{2} \boldsymbol{e}_{2}+c_{3} \boldsymbol{e}_{3}
\end{align*}
$$

where $\left(a_{1}, a_{2}, a_{3}\right),\left(b_{1}, b_{2}, b_{3}\right)$ and $\left(c_{1}, c_{2}, c_{3}\right)$ are the Cartesian coordinates of these vectors. Taking the scalar product of the vector obtained by vectorial product of the vectors $\boldsymbol{a}$ and $\boldsymbol{b}$ and of the vector $\boldsymbol{c}$, we obtain the triple product,

$(\boldsymbol{a} \times \boldsymbol{b}) \cdot \boldsymbol{c}=\left|\begin{array}{ccc}c_{1} & a_{1} & b_{1} \\ c_{2} & a_{2} & b_{2} \\ c_{3} & a_{3} & b_{3}\end{array}\right|=\left(a_{2} b_{3}-a_{3} b_{2}\right) c_{1}+\left(a_{3} b_{1}-a_{1} b_{3}\right) c_{2}+\left(a_{1} b_{2}-a_{2} b_{1}\right) c_{3}$

The definition (1.39) of the triple product yields the following two properties,

$$
\begin{equation*}
\text { (i) } \quad(\boldsymbol{a} \times \boldsymbol{b}) \cdot \boldsymbol{c}=(\boldsymbol{b} \times \boldsymbol{c}) \cdot \boldsymbol{a}=(\boldsymbol{c} \times \boldsymbol{a}) \cdot \boldsymbol{b} \quad(i i) \quad(\boldsymbol{a} \times \boldsymbol{b}) \cdot \boldsymbol{a}=(\boldsymbol{a} \times \boldsymbol{b}) \cdot \boldsymbol{b}=0 \tag{1.40}
\end{equation*}
$$

The property (i) follows from the invariance of the determinant under the cyclic permutation of the colomns and the property (ii) follows from the fact that the determinant cancels if two columns are identical.

### 1.3.5 Vectorial identity

Now, we shall establish a very important vectorial identity for this course. Using the definition of the vector product (1.30), we show that

$$
\boldsymbol{a} \times(\boldsymbol{b} \times \boldsymbol{c})=\left|\begin{array}{ccc}
\boldsymbol{e}_{1} & a_{1} & \left(b_{2} c_{3}-b_{3} c_{2}\right)  \tag{1.41}\\
\boldsymbol{e}_{2} & a_{2} & \left(b_{3} c_{1}-b_{1} c_{3}\right) \\
\boldsymbol{e}_{3} & a_{3} & \left(b_{1} c_{2}-b_{2} c_{1}\right)
\end{array}\right|=\left(\begin{array}{c}
a_{2}\left(b_{1} c_{2}-b_{2} c_{1}\right)-a_{3}\left(b_{3} c_{1}-b_{1} c_{3}\right) \\
a_{3}\left(b_{2} c_{3}-b_{3} c_{2}\right)-a_{1}\left(b_{1} c_{2}-b_{2} c_{1}\right) \\
a_{1}\left(b_{3} c_{1}-b_{1} c_{3}\right)-a_{2}\left(b_{2} c_{3}-b_{3} c_{2}\right)
\end{array}\right)
$$

Moreover, using the definition of the scalar product (1.23), we show also that

$$
(\boldsymbol{a} \cdot \boldsymbol{c}) \boldsymbol{b}-(\boldsymbol{a} \cdot \boldsymbol{b}) \boldsymbol{c}=\left(\begin{array}{c}
\left(a_{1} e_{1}+a_{2} c_{2}+a_{3} c_{3}\right) b_{1}-\left(a_{1} b_{1}+a_{2} b_{2}+a_{3} b_{3}\right) c_{1}  \tag{1.42}\\
\left(a_{1} c_{1}+a_{2} e_{2}+a_{3} c_{3}\right) b_{2}-\left(a_{1} b_{1}+a_{2} b_{2}+a_{3} b_{3}\right) c_{2} \\
\left(a_{1} c_{1}+a_{2} c_{2}+a_{3} \bigodot_{3}\right) b_{3}-\left(a_{1} b_{1}+a_{2} b_{2}+a_{3} b_{3}\right) c_{3}
\end{array}\right)
$$

Identifying equations (1.41) and (1.42) after simplification, we obtain the vectorial identity,

$$
\begin{equation*}
\boldsymbol{a} \times(\boldsymbol{b} \times \boldsymbol{c})=(\boldsymbol{a} \cdot \boldsymbol{c}) \boldsymbol{b}-(\boldsymbol{a} \cdot \boldsymbol{b}) \boldsymbol{c} \tag{1.43}
\end{equation*}
$$

