# CHAPTER 8 Atomic Structure 

INTRODUCTION In this chapter, we use quantum mechanics to study the structure and properties of atoms. This study introduces ideas and concepts that are necessary to understand more complex systems, such as molecules, crystals, and metals. As we deepen our understanding of atoms, we build on things we already know, such as Rutherford's nuclear model of the atom, Bohr's model of the hydrogen atom, and de Broglie's wave hypothesis.

Figure 8.1 is NGC1763, an emission nebula in the small galaxy known as the Large Magellanic Cloud, which is a satellite of the Milky Way Galaxy. Ultraviolet light from hot stars ionizes the hydrogen atoms in the nebula. As
protons and electrons recombine, radiation of different frequencies is emitted. The details of this process can be correctly predicted by quantum mechanics and are examined in this chapter.

### 8.1 The Hydrogen Atom

The hydrogen atom is the simplest atom in nature and, therefore, a good starting point to study atoms and atomic structure. The hydrogen atom consists of a single negatively charged electron that moves about a positively charged proton (Figure 8.2). In Bohr's model, the electron is pulled around the proton in a perfectly circular orbit by an attractive Coulomb force. The proton is approximately 1800 times more massive than the electron, so the proton moves very little in response to the force on the proton by the electron. (This is analogous to the Earth-Sun system, where the Sun moves very little in response to the force exerted on it by Earth.) An explanation of this effect using Newton's laws is given in Photons and Matter Waves.

With the assumption of a fixed proton, we focus on the motion of the electron.

In the electric field of the proton, the potential energy of the electron is

$$
U(r)=-k \frac{e^{2}}{r}
$$

where $k=1 / 4 \pi \varepsilon_{0}$ and $r$ is the distance between the electron and the proton. As we saw earlier, the force on an object is equal to the negative of the gradient (or slope) of the potential energy function. For the special case of a hydrogen atom, the force between the electron and proton is an attractive Coulomb force.

Notice that the potential energy function $U(r)$ does not vary in time. As a result, Schrödinger's equation of the hydrogen atom reduces to two simpler equations: one that depends only on space ( $x, y, z$ ) and another that depends only on time $(t)$. (The separation of a wave function into space- and time-dependent parts for timeindependent potential energy functions is discussed in Quantum Mechanics.) We are most interested in the space-dependent equation:

$$
\frac{-\hbar^{2}}{2 m_{e}}\left(\frac{\partial^{2} \psi}{\partial x^{2}}+\frac{\partial^{2} \psi}{\partial y^{2}}+\frac{\partial^{2} \psi}{\partial z^{2}}\right)-k \frac{e^{2}}{r} \psi=E \psi
$$

where $\psi=\psi(x, y, z)$ is the three-dimensional wave function of the electron, $m_{e}$ is the mass of the electron, and $E$ is the total energy of the electron. Recall that the total wave function $\Psi(x, y, z, t)$, is the product of the space-dependent wave function $\psi=\psi(x, y, z)$ and the time-dependent wave function $\varphi=\varphi(t)$.

In addition to being time-independent, $U(r)$ is also spherically symmetrical. This suggests that we may solve Schrödinger's equation more easily if we express it in terms of the spherical coordinates $(r, \theta, \phi)$ instead of rectangular coordinates $(x, y, z)$. A spherical coordinate system is shown in Figure 8.3. In spherical coordinates, the variable $r$ is the radial coordinate, $\theta$ is the polar angle (relative to the vertical $z$-axis), and $\phi$ is the azimuthal angle (relative to the $x$-axis). The relationship between spherical and rectangular coordinates is $x=r \sin \theta \cos \phi, \quad y=r \sin \theta \sin \phi, \quad z=r \cos \theta$.

The factor $r \sin \theta$ is the magnitude of a vector formed by the projection of the polar vector onto the $x y$-plane. Also, the coordinates of $x$ and $y$ are obtained by projecting this vector onto the $x$ - and $y$-axes, respectively. The inverse transformation gives

$$
r=\sqrt{x^{2}+y^{2}+z^{2}}, \theta=\cos ^{-1}\left(\frac{z}{r}\right), \phi=\cos ^{-1}\left(\frac{x}{\sqrt{x^{2}+y^{2}}}\right)
$$

Schrödinger's wave equation for the hydrogen atom in spherical coordinates is discussed in more advanced courses in modern physics, so we do not consider it in detail here. However, due to the spherical symmetry of $U(r)$, this equation reduces to three simpler equations: one for each of the three coordinates $(r, \theta$, and $\phi)$. Solutions to the time-independent wave function are written as a product of three functions:

$$
\psi(r, \theta, \phi)=R(r) \Theta(\theta) \Phi(\phi)
$$

where $R$ is the radial function dependent on the radial coordinate $r$ only; $\Theta$ is the polar function dependent on the polar coordinate $\theta$ only; and $\Phi$ is the phi function of $\phi$ only. Valid solutions to Schrödinger's equation $\psi(r, \theta, \phi)$ are labeled by the quantum numbers $n, l$, and $m$.

$n: \quad$ principal quantum number

$l: \quad$ angular momentum quantum number

$m: \quad$ angular momentum projection quantum number

(The reasons for these names will be explained in the next section.) The radial function $R$ depends only on $n$ and $l$; the polar function $\Theta$ depends only on 1 and $m$; and the phi function $\Phi$ depends only on $m$. The dependence of each function on quantum numbers is indicated with subscripts:

$$
\psi_{n l m}(r, \theta, \phi)=R_{n l}(r) \Theta_{l m}(\theta) \Phi_{m}(\phi)
$$

Not all sets of quantum numbers $(n, l, m)$ are possible. For example, the orbital angular quantum number $l$ can never be greater or equal to the principal quantum number $n(l<n)$. Specifically, we have

$$
\begin{aligned}
n & =1,2,3, \ldots \\
l & =0,1,2, \ldots,(n-1) \\
m & =-l,(-l+1), \ldots, 0, \ldots,(+l-1),+l
\end{aligned}
$$

Notice that for the ground state, $n=1, l=0$, and $m=0$. In other words, there is only one quantum state with the wave function for $n=1$, and it is $\psi_{100}$. However, for $n=2$, we have

$$
\begin{aligned}
& l=0, \quad m=0 \\
& l=1, \quad m=-1,0,1
\end{aligned}
$$

Therefore, the allowed states for the $n=2$ state are $\psi_{200}, \psi_{21-1}, \psi_{210}$, and $\psi_{211}$. Example wave functions for the hydrogen atom are given in Table 8.1. Note that some of these expressions contain the letter $i$, which represents $\sqrt{-1}$. When probabilities are calculated, these complex numbers do not appear in the final answer.

| $n=1, l=0, m_{l}=0$ | $\psi_{100}=\frac{1}{\sqrt{\pi}} \frac{1}{a_{0} 3 / 2} e^{-r / a_{0}}$ |
| :--- | :--- |
| $n=2, l=0, m_{l}=0$ | $\psi_{200}=\frac{1}{4 \sqrt{2 \pi}} \frac{1}{a_{0} 3 / 2}\left(2-\frac{r}{a_{0}}\right) e^{-r / 2 a_{0}}$ |
| $n=2, l=1, m_{l}=-1$ | $\psi_{21-1}=\frac{1}{8 \sqrt{\pi}} \frac{1}{a_{0} 3 / 2} \frac{r}{a_{0}} e^{-r / 2 a_{0}} \sin \theta e^{-i \phi}$ |
| $n=2, l=1, m_{l}=0$ | $\psi_{210}=\frac{1}{4 \sqrt{2 \pi}} \frac{1}{a_{0} 3 / 2} \frac{r}{a_{0}} e^{-r / 2 a_{0}} \cos \theta$ |
| $n=2, l=1, m_{l}=1$ | $\psi_{211}=\frac{1}{8 \sqrt{\pi}} \frac{1}{a_{0} 3 / 2} \frac{r}{a_{0}} e^{-r / 2 a_{0}} \sin \theta e^{i \phi}$ |

Table 8.1 Wave Functions of the Hydrogen Atom

## Physical Significance of the Quantum Numbers

Each of the three quantum numbers of the hydrogen atom $(n, l, m)$ is associated with a different physical quantity. The principal quantum number $n$ is associated with the total energy of the electron, $E_{n}$. According to Schrödinger's equation:

$$
E_{n}=-\left(\frac{m_{e} k^{2} e^{4}}{2 \hbar^{2}}\right)\left(\frac{1}{n^{2}}\right)=-E_{0}\left(\frac{1}{n^{2}}\right)
$$

where $E_{0}=-13.6 \mathrm{eV}$. Notice that this expression is identical to that of Bohr's model. As in the Bohr model, the electron in a particular state of energy does not radiate.

## EXAMPLE 8.1

## How Many Possible States?

For the hydrogen atom, how many possible quantum states correspond to the principal number $n=3$ ? What are the energies of these states?

## Strategy

For a hydrogen atom of a given energy, the number of allowed states depends on its orbital angular momentum. We can count these states for each value of the principal quantum number, $n=1,2,3$. However, the total energy depends on the principal quantum number only, which means that we can use Equation 8.3 and the number of states counted.

## Solution

If $n=3$, the allowed values of $l$ are 0,1 , and 2. If $l=0, m=0$ (1 state). If $l=1, m=-1,0,+1$ (3 states); and if $l=2, m=-2,-1,0,+1,+2$ ( 5 states). In total, there are $1+3+5=9$ allowed states. Because the total energy depends only on the principal quantum number, $n=3$, the energy of each of these states is

$$
E_{n 3}=-E_{0}\left(\frac{1}{n^{2}}\right)=\frac{-13.6 \mathrm{eV}}{9}=-1.51 \mathrm{eV}
$$

## Significance

An electron in a hydrogen atom can occupy many different angular momentum states with the very same energy. As the orbital angular momentum increases, the number of the allowed states with the same energy increases.

The angular momentum orbital quantum number $l$ is associated with the orbital angular momentum of the electron in a hydrogen atom. Quantum theory tells us that when the hydrogen atom is in the state $\psi_{n l m}$, the magnitude of its orbital angular momentum is

$$
L=\sqrt{l(l+1)} \hbar
$$

where

$$
l=0,1,2, \ldots,(n-1)
$$

This result is slightly different from that found with Bohr's theory, which quantizes angular momentum according to the rule $L=n$, where $n=1,2,3, \ldots$.

Quantum states with different values of orbital angular momentum are distinguished using spectroscopic notation (Table 8.2). The designations $s, p, d$, and fresult from early historical attempts to classify atomic spectral lines. (The letters stand for sharp, principal, diffuse, and fundamental, respectively.) After $f$, the letters continue alphabetically.

The ground state of hydrogen is designated as the $1 s$ state, where " 1 " indicates the energy level $(n=1)$ and " $s$ " indicates the orbital angular momentum state $(l=0)$. When $n=2,1$ can be either 0 or 1 . The $n=2, l=0$ state is designated " $2 s$. ." The $n=2, l=1$ state is designated " $2 p$." When $n=3,1$ can be 0,1 , or 2 , and the states are $3 s, 3 p$, and $3 d$, respectively. Notation for other quantum states is given in Table 8.3 .

The angular momentum projection quantum number $m$ is associated with the azimuthal angle $\phi$ (see Figure 8.3) and is related to the $z$-component of orbital angular momentum of an electron in a hydrogen atom. This component is given by

$$
L_{z}=m \hbar
$$

where

$$
m=-l,-l+1, \ldots, 0, \ldots,+l-1, l
$$

The $z$-component of angular momentum is related to the magnitude of angular momentum by

$$
L_{z}=L \cos \theta
$$

where $\theta$ is the angle between the angular momentum vector and the $z$-axis. Note that the direction of the $z$-axis is determined by experiment-that is, along any direction, the experimenter decides to measure the angular momentum. For example, the $z$-direction might correspond to the direction of an external magnetic field. The relationship between $L_{z}$ and $L$ is given in Figure 8.4.

| Orbital Quantum Number $/$ | Angular Momentum | State | Spectroscopic Name |
| :--- | :--- | :--- | :--- |
| 0 | 0 | $s$ | Sharp |
| 1 | $\sqrt{2} h$ | $p$ | Principal |
| 2 | $\sqrt{6} h$ | $d$ | Diffuse |
| 3 | $\sqrt{12} h$ | $f$ | Fundamental |
| 4 | $\sqrt{20} h$ | $g$ |  |
| 5 | $\sqrt{30} h$ | $h$ |  |

Table 8.2 Spectroscopic Notation and Orbital Angular Momentum

|  | $l=0$ | $l=1$ | $l=2$ | $l=3$ | $l=4$ | $l=5$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $n=1$ | $1 s$ |  |  |  |  |  |
| $n=2$ | $2 s$ | $2 p$ |  |  |  |  |
| $n=3$ | $3 s$ | $3 p$ | $3 d$ |  |  |  |
| $n=4$ | $4 s$ | $4 p$ | $4 d$ | $4 f$ |  |  |
| $n=5$ | $5 s$ | $5 p$ | $5 d$ | $5 f$ | $5 g$ |  |
| $n=6$ | $6 s$ | $6 p$ | $6 d$ | $6 f$ | $6 g$ | $6 h$ |

Table 8.3 Spectroscopic Description of Quantum States

The quantization of $L_{z}$ is equivalent to the quantization of $\theta$. Substituting $\sqrt{l(l+1)} \hbar$ for $L$ and $m$ for $L_{z}$ into this equation, we find

$$
m \hbar=\sqrt{l(l+1)} \hbar \cos \theta .
$$

Thus, the angle $\theta$ is quantized with the particular values

$$
\theta=\cos ^{-1}\left(\frac{m}{\sqrt{l(l+1)}}\right)
$$

Notice that both the polar angle $(\theta)$ and the projection of the angular momentum vector onto an arbitrary $z$-axis $\left(L_{z}\right)$ are quantized.

The quantization of the polar angle for the $l=3$ state is shown in Figure 8.5. The orbital angular momentum vector lies somewhere on the surface of a cone with an opening angle $\theta$ relative to the $z$-axis (unless $m=0$, in which case $\theta=90^{\circ}$ and the vector points are perpendicular to the $z$-axis).

A detailed study of angular momentum reveals that we cannot know all three components simultaneously. In the previous section, the $z$-component of orbital angular momentum has definite values that depend on the quantum number $m$. This implies that we cannot know both $x$ - and $y$-components of angular momentum, $L_{x}$ and $L_{y}$, with certainty. As a result, the precise direction of the orbital angular momentum vector is unknown.

EXAMPLE 8.2

## What Are the Allowed Directions?

Calculate the angles that the angular momentum vector $\mathbf{\mathbf { L }}$ can make with the $z$-axis for $l=1$, as shown in Figure 8.6.

## Strategy

The vectors $\overrightarrow{\mathbf{L}}$ and $\overrightarrow{\mathbf{L}}_{z}$ (in the $z$-direction) form a right triangle, where $\overrightarrow{\mathbf{L}}$ is the hypotenuse and $\overrightarrow{\mathbf{L}}_{z}$ is the adjacent side. The ratio of $L_{z}$ to $|\overrightarrow{\mathbf{L}}|$ is the cosine of the angle of interest. The magnitudes $L=|\overrightarrow{\mathbf{L}}|$ and $L_{z}$ are given by

$$
L=\sqrt{l(l+1)} \hbar \text { and } L_{z}=m \hbar
$$

## Solution

We are given $l=1$, so $\mathrm{m} l$ can be $+1,0$, or -1 . Thus, $L$ has the value given by

$$
L=\sqrt{l(l+1)} \hbar=\sqrt{2} \hbar
$$

The quantity $L_{z}$ can have three values, given by $L_{z}=m_{l} \hbar$.

$$
L_{z}=m_{l} \hbar=\left\{\begin{aligned}
\hbar, m_{l} & =+1 \\
0, m_{l} & =0 \\
-\hbar, m_{l} & =-1
\end{aligned}\right.
$$

As you can see in Figure $8.6, \cos \theta=L_{z} / L$, so for $m=+1$, we have

$$
\cos \theta_{1}=\frac{L_{Z}}{L}=\frac{\hbar}{\sqrt{2} \hbar}=\frac{1}{\sqrt{2}}=0.707
$$

Thus,

$$
\theta_{1}=\cos ^{-1} 0.707=45.0^{\circ}
$$

Similarly, for $m=0$, we find $\cos \theta_{2}=0$; this gives

$$
\theta_{2}=\cos ^{-1} 0=90.0^{\circ}
$$

Then for $m_{l}=-1$ :

$$
\cos \theta_{3}=\frac{L_{Z}}{L}=\frac{-\hbar}{\sqrt{2} \hbar}=-\frac{1}{\sqrt{2}}=-0.707
$$

so that

$$
\theta_{3}=\cos ^{-1}(-0.707)=135.0^{\circ}
$$

## Significance

The angles are consistent with the figure. Only the angle relative to the $z$-axis is quantized. $L$ can point in any direction as long as it makes the proper angle with the $z$-axis. Thus, the angular momentum vectors lie on cones, as illustrated. To see how the correspondence principle holds here, consider that the smallest angle $\left(\theta_{1}\right.$ in the example) is for the maximum value of $m_{l}$, namely $m_{l}=l$. For that smallest angle,

$$
\cos \theta=\frac{L_{z}}{L}=\frac{l}{\sqrt{l(l+1)}}
$$

which approaches 1 as 1 becomes very large. If $\cos \theta=1$, then $\theta=0^{\circ}$. Furthermore, for large 1 , there are many values of $m_{l}$, so that all angles become possible as 1 gets very large.

## Using the Wave Function to Make Predictions

As we saw earlier, we can use quantum mechanics to make predictions about physical events by the use of probability statements. It is therefore proper to state, "An electron is located within this volume with this probability at this time," but not, "An electron is located at the position $(x, y, z)$ at this time." To determine the probability of finding an electron in a hydrogen atom in a particular region of space, it is necessary to integrate the probability density $\left|\psi_{n l m}\right|^{2}$ over that region:

$$
\text { Probability }=\int_{\text {volume }}\left|\psi_{n l m}\right|^{2} d V
$$

where $d V$ is an infinitesimal volume element. If this integral is computed for all space, the result is 1 , because the probability of the particle to be located somewhere is $100 \%$ (the normalization condition). In a more advanced course on modern physics, you will find that $\left|\psi_{n l m}\right|^{2}=\psi_{n l m}^{*} \psi_{n l m}$, where $\psi_{n l m}^{*}$ is the complex conjugate. This eliminates the occurrences of $i=\sqrt{-1}$ in the above calculation.

Consider an electron in a state of zero angular momentum $(l=0)$. In this case, the electron's wave function depends only on the radial coordinate $r$. (Refer to the states $\psi_{100}$ and $\psi_{200}$ in Table 8.1.) The infinitesimal volume element corresponds to a spherical shell of radius $r$ and infinitesimal thickness $d r$, written as

$$
d V=4 \pi r^{2} d r
$$

The probability of finding the electron in the region $r$ to $r+d r$ ("at approximately $r$ ") is

$$
P(r) d r=\left|\psi_{n 00}\right|^{2} 4 \pi r^{2} d r
$$

Here $P(r)$ is called the radial probability density function (a probability per unit length). For an electron in the
ground state of hydrogen, the probability of finding an electron in the region $r$ to $r+d r$ is

$$
\left|\psi_{n 00}\right|^{2} 4 \pi r^{2} d r=\left(4 / a_{0}^{3}\right) r^{2} \exp \left(-2 r / a_{0}\right) d r
$$

where $a_{0}=0.5$ angstroms. The radial probability density function $P(r)$ is plotted in Figure 8.7. The area under the curve between any two radial positions, say $r_{1}$ and $r_{2}$, gives the probability of finding the electron in that radial range. To find the most probable radial position, we set the first derivative of this function to zero $(d P / d r=0)$ and solve for $r$. The most probable radial position is not equal to the average or expectation value of the radial position because $\left|\psi_{n 00}\right|^{2}$ is not symmetrical about its peak value.

If the electron has orbital angular momentum $(l \neq 0)$, then the wave functions representing the electron depend on the angles $\theta$ and $\phi$; that is, $\psi_{n l m}=\psi_{n l m}(r, \theta, \phi)$. Atomic orbitals for three states with $n=2$ and $l=1$ are shown in Figure 8.8. An atomic orbital is a region in space that encloses a certain percentage (usually $90 \%)$ of the electron probability. (Sometimes atomic orbitals are referred to as "clouds" of probability.) Notice that these distributions are pronounced in certain directions. This directionality is important to chemists when they analyze how atoms are bound together to form molecules.

A slightly different representation of the wave function is given in Figure 8.9. In this case, light and dark regions indicate locations of relatively high and low probability, respectively. In contrast to the Bohr model of the hydrogen atom, the electron does not move around the proton nucleus in a well-defined path. Indeed, the uncertainty principle makes it impossible to know how the electron gets from one place to another.

### 8.2 Orbital Magnetic Dipole Moment of the Electron

In Bohr's model of the hydrogen atom, the electron moves in a circular orbit around the proton. The electron passes by a particular point on the loop in a certain time, so we can calculate a current $I=Q / t$. An electron that orbits a proton in a hydrogen atom is therefore analogous to current flowing through a circular wire (Figure 8.10). In the study of magnetism, we saw that a current-carrying wire produces magnetic fields. It is therefore reasonable to conclude that the hydrogen atom produces a magnetic field and interacts with other magnetic fields.

The orbital magnetic dipole moment is a measure of the strength of the magnetic field produced by the orbital angular momentum of an electron. From Force and Torque on a Current Loop, the magnitude of the orbital magnetic dipole moment for a current loop is

$$
\mu=I A
$$

where $I$ is the current and $A$ is the area of the loop. (For brevity, we refer to this as the magnetic moment.) The current $I$ associated with an electron in orbit about a proton in a hydrogen atom is

$$
I=\frac{e}{T}
$$

where $e$ is the magnitude of the electron charge and $T$ is its orbital period. If we assume that the electron travels in a perfectly circular orbit, the orbital period is

$$
T=\frac{2 \pi r}{v}
$$

where $r$ is the radius of the orbit and $v$ is the speed of the electron in its orbit. Given that the area of a circle is $\pi r^{2}$, the absolute magnetic moment is

$$
\mu=I A=\frac{e}{\left(\frac{2 \pi r}{v}\right)} \pi r^{2}=\frac{e v r}{2}
$$

It is helpful to express the magnetic momentum $\mu$ in terms of the orbital angular momentum $(\overrightarrow{\mathbf{L}}=\overrightarrow{\mathbf{r}} \times \overrightarrow{\mathbf{p}})$. Because the electron orbits in a circle, the position vector $\overrightarrow{\mathbf{r}}$ and the momentum vector $\overrightarrow{\mathbf{p}}$ form a right angle. Thus, the magnitude of the orbital angular momentum is

$$
L=|\overrightarrow{\mathbf{L}}|=|\overrightarrow{\mathbf{r}} \times \overrightarrow{\mathbf{p}}|=r p \sin \theta=r p=r m v
$$

Combining these two equations, we have

$$
\mu=\left(\frac{e}{2 m_{e}}\right) L
$$

In full vector form, this expression is written as

$$
\vec{\mu}=-\left(\frac{e}{2 m_{e}}\right) \vec{L}
$$

The negative sign appears because the electron has a negative charge. Notice that the direction of the magnetic moment of the electron is antiparallel to the orbital angular momentum, as shown in Figure 8.10(b). In the Bohr model of the atom, the relationship between $\vec{\mu}$ and $\overrightarrow{\mathbf{L}}$ in Equation 8.19 is independent of the radius of the orbit.

The magnetic moment $\mu$ can also be expressed in terms of the orbital angular quantum number 1 . Combining Equation 8.18 and Equation 8.15, the magnitude of the magnetic moment is

$$
\mu=\left(\frac{e}{2 m_{e}}\right) L=\left(\frac{e}{2 m_{e}}\right) \sqrt{l(l+1)} \hbar=\mu_{\mathrm{B}} \sqrt{l(l+1)}
$$

The $z$-component of the magnetic moment is

$$
\mu_{z}=-\left(\frac{e}{2 m_{e}}\right) L_{z}=-\left(\frac{e}{2 m_{e}}\right) m \hbar=-\mu_{\mathrm{B}} m
$$

The quantity $\mu_{\mathbf{B}}$ is a fundamental unit of magnetism called the Bohr magneton, which has the value $9.3 \times 10^{-24}$ joule/tesla $(\mathrm{J} / \mathrm{T})$ or $5.8 \times 10^{-5} \mathrm{eV} / \mathrm{T}$. Quantization of the magnetic moment is the result of quantization of the orbital angular momentum.

As we will see in the next section, the total magnetic dipole moment of the hydrogen atom is due to both the orbital motion of the electron and its intrinsic spin. For now, we ignore the effect of electron spin.

## EXAMPLE 8.3

## Orbital Magnetic Dipole Moment

What is the magnitude of the orbital dipole magnetic moment $\mu$ of an electron in the hydrogen atom in the (a) $s$ state, (b) $p$ state, and (c) $d$ state? (Assume that the spin of the electron is zero.)

## Strategy

The magnetic momentum of the electron is related to its orbital angular momentum L. For the hydrogen atom, this quantity is related to the orbital angular quantum number 1 . The states are given in spectroscopic notation, which relates a letter ( $s, p, d$, etc.) to a quantum number.

## Solution

The magnitude of the magnetic moment is given in Equation 8.20:

$$
\mu=\left(\frac{e}{2 m_{e}}\right) L=\left(\frac{e}{2 m_{e}}\right) \sqrt{l(l+1)} \hbar=\mu_{\mathrm{B}} \sqrt{l(l+1)}
$$

a. For the $s$ state, $l=0$ so we have $\mu=0$ and $\mu_{z}=0$.

b. For the $p$ state, $l=1$ and we have

$$
\begin{aligned}
& \mu=\mu_{\mathrm{B}} \sqrt{1(1+1)}=\sqrt{2} \mu_{\mathrm{B}} \\
& \mu_{z}=-\mu_{\mathrm{B}} m, \text { where } m=(-1,0,1), \text { so } \\
& \mu_{z}=\mu_{\mathrm{B}}, 0,-\mu_{\mathrm{B}}
\end{aligned}
$$

c. For the $d$ state, $l=2$ and we obtain

$$
\begin{aligned}
& \mu=\mu_{\mathrm{B}} \sqrt{2(2+1)}=\sqrt{6} \mu_{\mathrm{B}} \\
& \mu_{z}=-\mu_{\mathrm{B}} m, \text { where } m=(-2,-1,0,1,2), \text { so } \\
& \mu_{z}=2 \mu_{\mathrm{B}}, \mu_{\mathrm{B}}, 0,-\mu_{\mathrm{B}},-2 \mu_{\mathrm{B}}
\end{aligned}
$$

## Significance

In the $s$ state, there is no orbital angular momentum and therefore no magnetic moment. This does not mean that the electron is at rest, just that the overall motion of the electron does not produce a magnetic field. In the $p$ state, the electron has a magnetic moment with three possible values for the $z$-component of this magnetic moment; this means that magnetic moment can point in three different polar directions-each antiparallel to the orbital angular momentum vector. In the $d$ state, the electron has a magnetic moment with five possible values for the $z$-component of this magnetic moment. In this case, the magnetic moment can point in five
different polar directions.

A hydrogen atom has a magnetic field, so we expect the hydrogen atom to interact with an external magnetic field-such as the push and pull between two bar magnets. From Force and Torque on a Current Loop, we know that when a current loop interacts with an external magnetic field $\overrightarrow{\mathbf{B}}$, it experiences a torque given by

$$
\vec{\tau}=I(\overrightarrow{\mathbf{A}} \times \overrightarrow{\mathbf{B}})=\vec{\mu} \times \overrightarrow{\mathbf{B}}
$$

where $I$ is the current, $\overrightarrow{\mathbf{A}}$ is the area of the loop, $\vec{\mu}$ is the magnetic moment, and $\overrightarrow{\mathbf{B}}$ is the external magnetic field. This torque acts to rotate the magnetic moment vector of the hydrogen atom to align with the external magnetic field. Because mechanical work is done by the external magnetic field on the hydrogen atom, we can talk about energy transformations in the atom. The potential energy of the hydrogen atom associated with this magnetic interaction is given by Equation 8.23 :

$$
U=-\vec{\mu} \cdot \vec{B}
$$

If the magnetic moment is antiparallel to the external magnetic field, the potential energy is large, but if the magnetic moment is parallel to the field, the potential energy is small. Work done on the hydrogen atom to rotate the atom's magnetic moment vector in the direction of the external magnetic field is therefore associated with a drop in potential energy. The energy of the system is conserved, however, because a drop in potential energy produces radiation (the emission of a photon). These energy transitions are quantized because the magnetic moment can point in only certain directions.

If the external magnetic field points in the positive $z$-direction, the potential energy associated with the orbital magnetic dipole moment is

$$
U(\theta)=-\mu B \cos \theta=-\mu_{z} B=-\left(-\mu_{\mathrm{B}} m\right) B=m \mu_{\mathrm{B}} B
$$

where $\mu_{B}$ is the Bohr magneton and $m$ is the angular momentum projection quantum number (or magnetic orbital quantum number), which has the values

$$
m=-l,-l+1, \ldots, 0, \ldots, l-1, l
$$

For example, in the $l=1$ electron state, the total energy of the electron is split into three distinct energy levels corresponding to $U=-\mu_{\mathrm{B}} B, 0, \mu_{\mathrm{B}} B$.

The splitting of energy levels by an external magnetic field is called the Zeeman effect. Ignoring the effects of electron spin, transitions from the $l=1$ state to a common lower energy state produce three closely spaced spectral lines (Figure 8.11, left column). Likewise, transitions from the $l=2$ state produce five closely spaced spectral lines (right column). The separation of these lines is proportional to the strength of the external magnetic field. This effect has many applications. For example, the splitting of lines in the hydrogen spectrum of the Sun is used to determine the strength of the Sun's magnetic field. Many such magnetic field measurements can be used to make a map of the magnetic activity at the Sun's surface called a magnetogram (Figure 8.12).

### 8.3 Electron Spin

In this section, we consider the effects of electron spin. Spin introduces two additional quantum numbers to our model of the hydrogen atom. Both were discovered by looking at the fine structure of atomic spectra. Spin
is a fundamental characteristic of all particles, not just electrons, and is analogous to the intrinsic spin of extended bodies about their own axes, such as the daily rotation of Earth.

Spin is quantized in the same manner as orbital angular momentum. It has been found that the magnitude of the intrinsic spin angular momentum $S$ of an electron is given by

$$
S=\sqrt{s(s+1)} \hbar
$$

where $s$ is defined to be the spin quantum number. This is similar to the quantization of $L$ given in Equation 8.4, except that the only value allowed for $s$ for an electron is $s=1 / 2$. The electron is said to be a "spin-half particle." The spin projection quantum number $m_{s}$ is associated with the $z$-components of spin, expressed by

$$
S_{z}=m_{s} \hbar
$$

In general, the allowed quantum numbers are

$$
m_{s}=-s,-s+1, \ldots, 0, \ldots,+s-1, s
$$

For the special case of an electron $(s=1 / 2)$,

$$
m_{s}=-\frac{1}{2}, \frac{1}{2}
$$

Directions of intrinsic spin are quantized, just as they were for orbital angular momentum. The $m_{s}=-1 / 2$ state is called the "spin-down" state and has a $z$-component of spin, $s_{z}=-1 / 2$; the $m_{s}=+1 / 2$ state is called the "spin-up" state and has a $z$-component of spin, $s_{z}=+1 / 2$. These states are shown in Figure 8.13.

The intrinsic magnetic dipole moment of an electron $\mu_{e}$ can also be expressed in terms of the spin quantum number. In analogy to the orbital angular momentum, the magnitude of the electron magnetic moment is

$$
\mu_{s}=\left(\frac{e}{2 m_{e}}\right) S
$$

According to the special theory of relativity, this value is low by a factor of 2 . Thus, in vector form, the spin magnetic moment is

$$
\vec{\mu}=\left(\frac{e}{m_{e}}\right) \overrightarrow{\mathbf{S}}
$$

The $z$-component of the magnetic moment is

$$
\mu_{z}=-\left(\frac{e}{m_{e}}\right) S_{z}=-\left(\frac{e}{m_{e}}\right) m_{s} \hbar
$$

The spin projection quantum number has just two values $\left(m_{s}= \pm 1 / 2\right)$, so the $z$-component of the magnetic moment also has just two values:

$$
\mu_{z}= \pm\left(\frac{e}{2 m_{e}}\right) \hbar= \pm \mu_{\mathrm{B}} \hbar
$$

where $\mu_{\mathrm{B}}$ is one Bohr magneton. An electron is magnetic, so we expect the electron to interact with other magnetic fields. We consider two special cases: the interaction of a free electron with an external (nonuniform) magnetic field, and an electron in a hydrogen atom with a magnetic field produced by the orbital angular momentum of the electron.

## EXAMPLE 8.4

## Electron Spin and Radiation

A hydrogen atom in the ground state is placed in an external uniform magnetic field ( $B=1.5 \mathrm{~T}$ ). Determine the frequency of radiation produced in a transition between the spin-up and spin-down states of the electron.

## Strategy

The spin projection quantum number is $m_{s}= \pm 1 / 2$, so the $z$-component of the magnetic moment is

$$
\mu_{z}= \pm\left(\frac{e}{2 m_{e}}\right)= \pm \mu_{\mathrm{B}} \hbar
$$

The potential energy associated with the interaction between the electron magnetic moment and the external magnetic field is

$$
U=-\mu_{z} B=\mp \mu_{\mathrm{B}} B
$$

The frequency of light emitted is proportional to the energy $(\Delta E)$ difference between these two states.

## Solution

The energy difference between these states is $\Delta E=2 \mu_{\mathrm{B}} B$, so the frequency of radiation produced is

$$
f=\frac{\Delta E}{h}=\frac{2 \mu_{B} B}{h}=\frac{2\left(5.79 \times \frac{10^{-5} \mathrm{eV}}{\mathrm{T}}\right)(1.5 \mathrm{~T})}{4.136 \times 10^{-15} \mathrm{eV} \cdot \mathrm{s}}=4.2 \times 10^{10} \frac{\mathrm{cycles}}{\mathrm{s}}
$$

## Significance

The electron magnetic moment couples with the external magnetic field. The energy of this system is different whether the electron is aligned or not with the proton. The frequency of radiation produced by a transition between these states is proportional to the energy difference. If we double the strength of the magnetic field, holding all other things constant, the frequency of the radiation doubles and its wavelength is cut in half.

In a hydrogen atom, the electron magnetic moment can interact with the magnetic field produced by the orbital angular momentum of the electron, a phenomenon called spin-orbit coupling. The orbital angular momentum $(\vec{L})$, orbital magnetic moment $(\vec{\mu})$, spin angular momentum $(\vec{S})$, and spin magnetic moment $\left(\vec{\mu}_{s}\right)$ vectors are shown together in Figure 8.14.

Just as the energy levels of a hydrogen atom can be split by an external magnetic field, so too are the energy
levels of a hydrogen atom split by internal magnetic fields of the atom. If the magnetic moment of the electron and orbital magnetic moment of the electron are antiparallel, the potential energy from the magnetic interaction is relatively high, but when these moments are parallel, the potential energy is relatively small. Transition from each of these two states to a lower-energy level results in the emission of a photon of slightly different frequency. That is, the spin-orbit coupling "splits" the spectral line expected from a spin-less electron. The fine structure of the hydrogen spectrum is explained by spin-orbit coupling.

The Stern-Gerlach experiment provides experimental evidence that electrons have spin angular momentum. The experiment passes a stream of silver (Ag) atoms through an external, nonuniform magnetic field. The Ag atom has an orbital angular momentum of zero and contains a single unpaired electron in the outer shell. Therefore, the total angular momentum of the Ag atom is due entirely to the spin of the outer electron $(s=1 / 2)$. Due to electron spin, the Ag atoms act as tiny magnets as they pass through the magnetic field. These "magnets" have two possible orientations, which correspond to the spin-up and -down states of the electron. The magnetic field diverts the spin up atoms in one direction and the spin-down atoms in another direction. This produces two distinct bands on a screen (Figure 8.15).

According to classical predictions, the angular momentum (and, therefore, the magnetic moment) of the $\mathrm{Ag}$ atom can point in any direction, so one expects, instead, a continuous smudge on the screen. The resulting two bands of the Stern-Gerlach experiment provide startling support for the ideas of quantum mechanics.

Just like an electron, a proton is spin $1 / 2$ and has a magnetic moment. (According to nuclear theory, this moment is due to the orbital motion of quarks within the proton.) The hyperfine structure of the hydrogen spectrum is explained by the interaction between the magnetic moment of the proton and the magnetic moment of the electron, an interaction known as spin-spin coupling. The energy of the electron-proton system is different depending on whether or not the moments are aligned. Transitions between these states (spin-flip transitions) result in the emission of a photon with a wavelength of $\lambda \approx 21 \mathrm{~cm}$ (in the radio range). The $21-\mathrm{cm}$ line in atomic spectroscopy is a "fingerprint" of hydrogen gas. Astronomers exploit this spectral line to map the spiral arms of galaxies, which are composed mostly of hydrogen (Figure 8.16).

A complete specification of the state of an electron in a hydrogen atom requires five quantum numbers: $n, 1, m$, $s$, and $m_{s}$. The names, symbols, and allowed values of these quantum numbers are summarized in Table 8.4.

| Name | Symbol | Allowed values |
| :--- | :--- | :--- |
| Principal quantum number | $n$ | $1,2,3, \ldots$ |
| Angular momentum | 1 | $0,1,2, \ldots n-1$ |
| Angular momentum projection | $m$ | $0, \pm 1, \pm 2, \ldots \pm l$ |
| Spin | $S$ | $1 / 2$ (electrons) |
| Spin projection | $m_{s}$ | $-1 / 2,+1 / 2$ |

Table 8.4 Summary of Quantum Numbers of an Electron in a Hydrogen Atom

Note that the intrinsic quantum numbers introduced in this section ( $s$ and $m_{s}$ ) are valid for many particles, not just electrons. For example, quarks within an atomic nucleus are also spin-half particles. As we will see later, quantum numbers help to classify subatomic particles and enter into scientific models that attempt to explain how the universe works.

### 8.4 The Exclusion Principle and the Periodic Table

So far, we have studied only hydrogen, the simplest chemical element. We have found that an electron in the hydrogen atom can be completely specified by five quantum numbers:

```
$n: \quad$ principal quantum number
$l: \quad$ angular momentum quantum number
$m: \quad$ angular momentum projection quantum number
$s: \quad$ spin quantum number
$m_{s}: \quad$ spin projection quantum number
```

8.34

To construct the ground state of a neutral multi-electron atom, imagine starting with a nucleus of charge $Z e$ (that is, a nucleus of atomic number $Z$ ) and then adding $Z$ electrons one by one. Assume that each electron moves in a spherically symmetrical electric field produced by the nucleus and all other electrons of the atom. The assumption is valid because the electrons are distributed randomly around the nucleus and produce an average electric field (and potential) that is spherically symmetrical. The electric potential $U(r)$ for each electron does not follow the simple $-1 / r$ form because of interactions between electrons, but it turns out that we can still label each individual electron state by quantum numbers, $\left(n, l, m, s, m_{s}\right)$. (The spin quantum number $s$ is the same for all electrons, so it will not be used in this section.)

The structure and chemical properties of atoms are explained in part by Pauli's exclusion principle: No two electrons in an atom can have the same values for all four quantum numbers $\left(n, l, m, m_{s}\right)$. This principle is related to two properties of electrons: All electrons are identical ("when you've seen one electron, you've seen them all") and they have half-integral spin ( $s=1 / 2$ ). Sample sets of quantum numbers for the electrons in an atom are given in Table 8.5. Consistent with Pauli's exclusion principle, no two rows of the table have the exact same set of quantum numbers.

$n \quad I \quad m \quad m_{s}$ Subshell symbol No. of electrons: subshell No. of electrons: shell

| 1 | 0 | 0 | $1 / 2$ | $1 s$ | 2 | 2 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 0 | 0 | $-1 / 2$ |  |  |  |
| 2 | 0 | 0 | $1 / 2$ | $2 s$ | 2 | 8 |
| 2 | 0 | 0 | $-1 / 2$ |  |  |  |
| 2 | 1 | -1 | $1 / 2$ | $2 p$ | 6 |  |
| 2 | 1 | -1 | $-1 / 2$ |  |  |  |
| 2 | 1 | 0 | $1 / 2$ |  |  |  |
| 2 | 1 | 0 | $-1 / 2$ |  |  |  |


| $n$ | $I$ | $m$ | $m_{s}$ | Subshell symbol | No. of electrons: subshell | No. of electrons: shell |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 2 | 1 | 1 | $1 / 2$ |  |  |  |
| 2 | 1 | 1 | $-1 / 2$ |  |  |  |
| 3 | 0 | 0 | $1 / 2$ | $3 s$ | 2 | 18 |
| 3 | 0 | 0 | $-1 / 2$ |  |  |  |
| 3 | 1 | -1 | $1 / 2$ | $3 p$ | 6 |  |
| 3 | 1 | -1 | $-1 / 2$ |  |  |  |
| 3 | 1 | 0 | $1 / 2$ |  |  |  |
| 3 | 1 | 0 | $-1 / 2$ |  |  |  |
| 3 | 1 | 1 | $1 / 2$ |  |  |  |
| 3 | 1 | 1 | $-1 / 2$ |  |  |  |
| 3 | 2 | -2 | $1 / 2$ | $3 d$ | 10 |  |
| 3 | 2 | -2 | $-1 / 2$ |  |  |  |
| 3 | 2 | -1 | $1 / 2$ |  |  |  |
| 3 | 2 | -1 | $-1 / 2$ |  |  |  |
| 3 | 2 | 0 | $1 / 2$ |  |  |  |
| 3 | 2 | 0 | $-1 / 2$ |  |  |  |
| 3 | 2 | 1 | $1 / 2$ |  |  |  |
| 3 | 2 | 1 | $-1 / 2$ |  |  |  |
| 3 | 2 | 2 | $1 / 2$ |  |  |  |
| 3 | 2 | 2 | $-1 / 2$ |  |  |  |

Table 8.5 Electron States of Atoms Because of Pauli's exclusion principle, no two electrons in an atom have the same set of four quantum numbers.

Electrons with the same principal quantum number $n$ are said to be in the same shell, and those that have the same value of $l$ are said to occupy the same subshell. An electron in the $n=1$ state of a hydrogen atom is denoted $1 s$, where the first digit indicates the shell $(n=1)$ and the letter indicates the subshell $(s, p, d, f \ldots$ correspond to $l=0,1,2,3 \ldots)$. Two electrons in the $n=1$ state are denoted as $1 s^{2}$, where the superscript indicates the number of electrons. An electron in the $n=2$ state with $l=1$ is denoted $2 p$. The combination of two electrons in the $n=2$ and $l=0$ state, and three electrons in the $n=2$ and $l=1$ state is written as $2 s^{2} 2 p^{3}$, and so on. This representation of the electron state is called the electron configuration of
the atom. The electron configurations for several atoms are given in Table 8.6. Electrons in the outer shell of an atom are called valence electrons. Chemical bonding between atoms in a molecule are explained by the transfer and sharing of valence electrons.

| Element | Electron Configuration | Spin Alignment |
| :--- | :--- | :--- |
| $\mathrm{H}$ | $1 s^{1}$ | $(\uparrow)$ |
| $\mathrm{He}$ | $1 s^{2}$ | $(\uparrow \downarrow)$ |
| $\mathrm{Li}$ | $1 s^{2} 2 s^{1}$ | $(\uparrow)$ |
| $\mathrm{Be}$ | $1 s^{2} 2 s^{2}$ | $(\uparrow \downarrow)$ |
| $\mathrm{B}$ | $1 s^{2} 2 s^{2} 2 p^{1}$ | $(\uparrow \downarrow)(\uparrow)$ |
| $\mathrm{C}$ | $1 s^{2} 2 s^{2} 2 p^{2}$ | $(\uparrow \downarrow)(\uparrow)(\uparrow)$ |
| $\mathrm{N}$ | $1 s^{2} 2 s^{2} 2 p^{3}$ | $(\uparrow \downarrow)(\uparrow)(\uparrow)(\uparrow)$ |
| $\mathrm{O}$ | $1 s^{2} 2 s^{2} 2 p^{4}$ | $(\uparrow \downarrow)(\uparrow \downarrow)(\uparrow)(\uparrow)$ |
| $\mathrm{F}$ | $1 s^{2} 2 s^{2} 2 p^{5}$ | $(\uparrow \downarrow)(\uparrow \downarrow)(\uparrow \downarrow)(\uparrow)$ |
| $\mathrm{Ne}$ | $1 s^{2} 2 s^{2} 2 p^{6}$ | $(\uparrow \downarrow)(\uparrow \downarrow)(\uparrow \downarrow)(\uparrow \downarrow)$ |
| $\mathrm{Na}$ | $1 s^{2} 2 s^{2} 2 p^{6} 3 s^{1}$ | $(\uparrow)$ |
| $\mathrm{Mg}$ | $1 s^{2} 2 s^{2} 2 p^{6} 3 s^{2}$ | $(\uparrow \downarrow)$ |
| $\mathrm{Al}$ | $1 s^{2} 2 s^{2} 2 p^{6} 3 s^{2} 3 p^{1}$ | $(\uparrow \downarrow)(\uparrow)$ |

Table 8.6 Electron Configurations of Electrons in an Atom The symbol ( $\uparrow$ ) indicates an unpaired electron in the outer shell, whereas the symbol $(\uparrow \downarrow)$ indicates a pair of spin-up and -down electrons in an outer shell.

The maximum number of electrons in a subshell depends on the value of the angular momentum quantum number, 1 . For a given a value $l$, there are $2 l+1$ orbital angular momentum states. However, each of these states can be filled by two electrons (spin up and down, $\uparrow \downarrow$ ). Thus, the maximum number of electrons in a subshell is

$$
N=2(2 l+1)=4 l+2
$$

In the $2 s(l=0)$ subshell, the maximum number of electrons is 2 . In the $2 p(l=1)$ subshell, the maximum number of electrons is 6 . Therefore, the total maximum number of electrons in the $n=2$ shell (including both the $l=0$ and 1 subshells) is $2+6$ or 8 . In general, the maximum number of electrons in the $n$th shell is $2 n^{2}$.

EXAMPLE 8.5

## Subshells and Totals for $n=3$

How many subshells are in the $n=3$ shell? Identify each subshell and calculate the maximum number of electrons that will fill each. Show that the maximum number of electrons that fill an atom is $2 n^{2}$.

## Strategy

Subshells are determined by the value of 1 ; thus, we first determine which values of 1 are allowed, and then we apply the equation "maximum number of electrons that can be in a subshell $=2(2 l+1)$ " to find the number of electrons in each subshell.

## Solution

Because $n=3$, we know that $l$ can be 0,1 , or 2 ; thus, there are three possible subshells. In standard notation, they are labeled the $3 s, 3 p$, and $3 d$ subshells. We have already seen that two electrons can be in an $s$ state, and six in a $p$ state, but let us use the equation "maximum number of electrons that can be in a subshell $=2(2 l+1)$ " to calculate the maximum number in each:

$$
\begin{aligned}
& 3 s \text { has } l=0 \text {; thus, } 2(2 l+1)=2(0+1)=2 \\
& 3 p \text { has } l=1 \text {; thus, } 2(2 l+1)=2(2+1)=6 \\
& 3 d \text { has } l=2 ; \text { thus, } 2(2 l+1)=2(4+1)=10 \\
& \text { Total }=18 \\
& \text { (in the } n=3 \text { shell). }
\end{aligned}
$$

The equation "maximum number of electrons that can be in a shell $=2 n^{2}$ " gives the maximum number in the $n=3$ shell to be

$$
\text { Maximum number of electrons }=2 n^{2}=2(3)^{2}=2(9)=18
$$

## Significance

The total number of electrons in the three possible subshells is thus the same as the formula $2 n^{2}$. In standard (spectroscopic) notation, a filled $n=3$ shell is denoted as $3 s^{2} 3 p^{6} 3 d^{10}$. Shells do not fill in a simple manner. Before the $n=3$ shell is completely filled, for example, we begin to find electrons in the $n=4$ shell.

The structure of the periodic table (Figure 8.17) can be understood in terms of shells and subshells, and, ultimately, the total energy, orbital angular momentum, and spin of the electrons in the atom. A detailed discussion of the periodic table is left to a chemistry course-we sketch only its basic features here. In this discussion, we assume that the atoms are electrically neutral; that is, they have the same number of electrons and protons. (Recall that the total number of protons in an atomic nucleus is called the atomic number, Z.)

First, the periodic table is arranged into columns and rows. The table is read left to right and top to bottom in the order of increasing atomic number $Z$. Atoms that belong to the same column or chemical group share many of the same chemical properties. For example, the Li and Na atoms (in the first column) bond to other atoms in a similar way. The first row of the table corresponds to the $1 s(l=0)$ shell of an atom.

Consider the hypothetical procedure of adding electrons, one by one, to an atom. For hydrogen (H) (upper left), the $1 s$ shell is filled with either a spin up or down electron ( $\uparrow$ or $\downarrow$ ). This lone electron is easily shared with other atoms, so hydrogen is chemically active. For helium (He) (upper right), the $1 s$ shell is filled with both a spin up and a spin down $(\uparrow \downarrow)$ electron. This "fills" the $1 s$ shell, so a helium atom tends not to share electrons with other atoms. The helium atom is said to be chemically inactive, inert, or noble; likewise, helium gas is said to be an inert gas or noble gas.

The second row corresponds to the $2 s$ and $2 p$ subshells. For lithium (Li) (upper left), the $1 s$ shell is filled with a spin-up and spin-down electron ( $\uparrow \downarrow$ ) and the $2 s$ shell is filled with either a spin-up or -down electron ( $\uparrow$ or $\downarrow$ ). Its electron configuration is therefore $1 s^{2} 2 s^{1}$ or [He] $2 s$, where [He] indicates a helium core. Like hydrogen, the lone electron in the outermost shell is easily shared with other atoms. For beryllium (Be), the $2 s$ shell is filled with a spin-up and -down electron $(\uparrow \downarrow)$, and has the electron configuration $[\mathrm{He}] 2 s^{2}$.

Next, we look at the right side of the table. For boron (B), the $1 s$ and $2 s$ shells are filled and the $2 p(l=1)$ shell contains either a spin up or down electron ( $\uparrow$ or $\downarrow$ ). From carbon (C) to neon (N), we the fill the $2 p$ shell. The maximum number of electrons in the $2 p$ shells is $4 l+2=4(2)+2=6$. For neon (Ne), the $1 s$ shell is filled with a spin-up and spin-down electron ( $\uparrow \downarrow$ ), and the $2 p$ shell is filled with six electrons ( $\uparrow \downarrow \uparrow \downarrow \uparrow \downarrow$ ). This "fills" the $1 s, 2 s$, and $2 p$ subshells, so like helium, the neon atom tends not to share electrons with other atoms.

The process of electron filling repeats in the third row. However, beginning in the fourth row, the pattern is broken. The actual order of order of electron filling is given by

$1 s, 2 s, 2 p, 3 s, 3 p, 4 s, \mathbf{3 d}, 4 p, 5 s, \mathbf{4 d}, 5 p, 6 s, \mathbf{4 f}, \mathbf{5 d}, 6 p, 7 s, \ldots$

Notice that the $3 d, 4 d, 4 f$, and $5 d$ subshells (in bold) are filled out of order; this occurs because of interactions between electrons in the atom, which so far we have neglected. The transition metals are elements in the gap between the first two columns and the last six columns that contain electrons that fill the $d(l=1)$ subshell. As expected, these atoms are arranged in $4 l+2=4(2)+2=10$ columns. The structure of the periodic table can be understood in terms of the quantization of the total energy ( $n$ ), orbital angular momentum ( $($ ), and spin ( $s$ ). The first two columns correspond to the $s(l=0)$ subshell, the next six columns correspond to the $p(l=1)$ subshell, and the gap between these columns corresponds to the $d(l=2)$ subshell.

The periodic table also gives information on molecular bonding. To see this, consider atoms in the left-most column (the so-called alkali metals including: Li, $\mathrm{Na}$, and $\mathrm{K}$ ). These atoms contain a single electron in the $2 s$ subshell, which is easily donated to other atoms. In contrast, atoms in the second-to-right column (the halogens: for example, Cl, F, and Br) are relatively stingy in sharing electrons. These atoms would much rather accept an electron, because they are just one electron shy of a filled shell ("of being noble").

Therefore, if a Na atom is placed in close proximity to a $\mathrm{Cl}$ atom, the $\mathrm{Na}$ atom freely donates its $2 s$ electron and the $\mathrm{Cl}$ atom eagerly accepts it. In the process, the $\mathrm{Na}$ atom (originally a neutral charge) becomes positively charged and the $\mathrm{Cl}$ (originally a neutral charge) becomes negatively charged. Charged atoms are called ions. In this case, the ions are $\mathrm{Na}^{+}$and $\mathrm{Cl}^{-}$, where the superscript indicates charge of the ion. The electric (Coulomb) attraction between these atoms forms a $\mathrm{NaCl}$ (salt) molecule. A chemical bond between two ions is called an ionic bond. There are many kinds of chemical bonds. For example, in an oxygen molecule $\mathrm{O}_{2}$ electrons are equally shared between the atoms. The bonding of oxygen atoms is an example of a covalent bond.

### 8.5 Atomic Spectra and X-rays

The study of atomic spectra provides most of our knowledge about atoms. In modern science, atomic spectra are used to identify species of atoms in a range of objects, from distant galaxies to blood samples at a crime scene.

The theoretical basis of atomic spectroscopy is the transition of electrons between energy levels in atoms. For example, if an electron in a hydrogen atom makes a transition from the $n=3$ to the $n=2$ shell, the atom emits a photon with a wavelength

$$
\lambda=\frac{c}{f}=\frac{h \cdot c}{h \cdot f}=\frac{h c}{\Delta E}=\frac{h c}{E_{3}-E_{2}}
$$

where $\Delta E=E_{3}-E_{2}$ is energy carried away by the photon and $h c=1240 \mathrm{eV} \cdot \mathrm{nm}$. After this radiation passes through a spectrometer, it appears as a sharp spectral line on a screen. The Bohr model of this process is shown in Figure 8.18. If the electron later absorbs a photon with energy $\Delta E$, the electron returns to the $n=3$ shell. (We examined the Bohr model earlier, in Photons and Matter Waves.)

To understand atomic transitions in multi-electron atoms, it is necessary to consider many effects, including the Coulomb repulsion between electrons and internal magnetic interactions (spin-orbit and spin-spin couplings). Fortunately, many properties of these systems can be understood by neglecting interactions between electrons and representing each electron by its own single-particle wave function $\psi_{n l m}$.

Atomic transitions must obey selection rules. These rules follow from principles of quantum mechanics and symmetry. Selection rules classify transitions as either allowed or forbidden. (Forbidden transitions do occur, but the probability of the typical forbidden transition is very small.) For a hydrogen-like atom, atomic transitions that involve electromagnetic interactions (the emission and absorption of photons) obey the following selection rule:

$$
\Delta l= \pm 1
$$

where $l$ is associated with the magnitude of orbital angular momentum,

$$
L=\sqrt{l(l+1)} \hbar
$$

For multi-electron atoms, similar rules apply. To illustrate this rule, consider the observed atomic transitions in hydrogen $(\mathrm{H})$, sodium $(\mathrm{Na})$, and mercury $(\mathrm{Hg})$ (Figure 8.19). The horizontal lines in this diagram correspond to atomic energy levels, and the transitions allowed by this selection rule are shown by lines drawn between these levels. The energies of these states are on the order of a few electron volts, and photons emitted in transitions are in the visible range. Technically, atomic transitions can violate the selection rule, but such transitions are uncommon.

The hydrogen atom has the simplest energy-level diagram. If we neglect electron spin, all states with the same value of $n$ have the same total energy. However, spin-orbit coupling splits the $n=2$ states into two angular momentum states ( $s$ and $p$ ) of slightly different energies. (These levels are not vertically displaced, because the energy splitting is too small to show up in this diagram.) Likewise, spin-orbit coupling splits the $n=3$ states into three angular momentum states $(s, p$, and $d$ ).

The energy-level diagram for hydrogen is similar to sodium, because both atoms have one electron in the outer shell. The valence electron of sodium moves in the electric field of a nucleus shielded by electrons in the inner shells, so it does not experience a simple $1 / r$ Coulomb potential and its total energy depends on both $n$ and $l$. Interestingly, mercury has two separate energy-level diagrams; these diagrams correspond to two net spin states of its $6 s$ (valence) electrons.

## EXAMPLE 8.6

## The Sodium Doublet

The spectrum of sodium is analyzed with a spectrometer. Two closely spaced lines with wavelengths 589.00 $\mathrm{nm}$ and $589.59 \mathrm{~nm}$ are observed. (a) If the doublet corresponds to the excited (valence) electron that transitions from some excited state down to the $3 s$ state, what was the original electron angular momentum? (b) What is the energy difference between these two excited states?

## Strategy

Sodium and hydrogen belong to the same column or chemical group of the periodic table, so sodium is "hydrogen-like." The outermost electron in sodium is in the $3 s(l=0)$ subshell and can be excited to higher energy levels. As for hydrogen, subsequent transitions to lower energy levels must obey the selection rule:

$$
\Delta l= \pm 1
$$

We must first determine the quantum number of the initial state that satisfies the selection rule. Then, we can use this number to determine the magnitude of orbital angular momentum of the initial state.

## Solution

a. Allowed transitions must obey the selection rule. If the quantum number of the initial state is $l=0$, the transition is forbidden because $\Delta l=0$. If the quantum number of the initial state is $l=2,3,4, \ldots$ the transition is forbidden because $\Delta l>1$. Therefore, the quantum of the initial state must be $l=1$. The orbital angular momentum of the initial state is

$$
L=\sqrt{l(l+1)} \hbar=1.41 \hbar
$$

b. Because the final state for both transitions is the same (3s), the difference in energies of the photons is equal to the difference in energies of the two excited states. Using the equation

$$
\Delta E=h f=h\left(\frac{c}{\lambda}\right)
$$

we have

$$
\begin{aligned}
\Delta E & =h c\left(\frac{1}{\lambda_{1}}-\frac{1}{\lambda_{2}}\right) \\
& =\left(4.14 \times 10^{-15} \mathrm{eVs}\right)\left(3.00 \times 10^{8} \mathrm{~m} / \mathrm{s}\right) \times\left(\frac{1}{589.00 \times 10^{-9} \mathrm{~m}}-\frac{1}{589.59 \times 10^{-9} \mathrm{~m}}\right) \\
& =2.11 \times 10^{-3} \mathrm{eV}
\end{aligned}
$$

## Significance

To understand the difficulty of measuring this energy difference, we compare this difference with the average energy of the two photons emitted in the transition. Given an average wavelength of $589.30 \mathrm{~nm}$, the average energy of the photons is

$$
E=\frac{h c}{\lambda}=\frac{\left(4.14 \times 10^{-15} \mathrm{eVs}\right)\left(3.00 \times 10^{8} \mathrm{~m} / \mathrm{s}\right)}{589.30 \times 10^{-9} \mathrm{~m}}=2.11 \mathrm{eV}
$$

The energy difference $\Delta E$ is about $0.1 \%$ (1 part in 1000) of this average energy. However, a sensitive spectrometer can measure the difference.

## Atomic Fluorescence

Fluorescence occurs when an electron in an atom is excited several steps above the ground state by the absorption of a high-energy ultraviolet (UV) photon. Once excited, the electron "de-excites" in two ways. The electron can drop back to the ground state, emitting a photon of the same energy that excited it, or it can drop in a series of smaller steps, emitting several low-energy photons. Some of these photons may be in the visible range. Fluorescent dye in clothes can make colors seem brighter in sunlight by converting UV radiation into visible light. Fluorescent lights are more efficient in converting electrical energy into visible light than incandescent filaments (about four times as efficient). Figure 8.20 shows a scorpion illuminated by a UV lamp. Proteins near the surface of the skin emit a characteristic blue light.

## X-rays

The study of atomic energy transitions enables us to understand X-rays and X-ray technology. Like all electromagnetic radiation, X-rays are made of photons. X-ray photons are produced when electrons in the outermost shells of an atom drop to the inner shells. (Hydrogen atoms do not emit X-rays, because the electron energy levels are too closely spaced together to permit the emission of high-frequency radiation.) Transitions of this kind are normally forbidden because the lower states are already filled. However, if an inner shell has a vacancy (an inner electron is missing, perhaps from being knocked away by a high-speed electron), an electron from one of the outer shells can drop in energy to fill the vacancy. The energy gap for such a transition is relatively large, so wavelength of the radiated X-ray photon is relatively short.

X-rays can also be produced by bombarding a metal target with high-energy electrons, as shown in Figure 8.21. In the figure, electrons are boiled off a filament and accelerated by an electric field into a tungsten target. According to the classical theory of electromagnetism, any charged particle that accelerates emits radiation. Thus, when the electron strikes the tungsten target, and suddenly slows down, the electron emits braking radiation. (Braking radiation refers to radiation produced by any charged particle that is slowed by a medium.) In this case, braking radiation contains a continuous range of frequencies, because the electrons will collide with the target atoms in slightly different ways.

Braking radiation is not the only type of radiation produced in this interaction. In some cases, an electron collides with another inner-shell electron of a target atom, and knocks the electron out of the atom-billiard ball style. The empty state is filled when an electron in a higher shell drops into the state (drop in energy level) and emits an X-ray photon.

Historically, X-ray spectral lines were labeled with letters ( $K, L, M, N, \ldots$ ). These letters correspond to the atomic shells $(n=1,2,3,4, \ldots)$. X-rays produced by a transition from any higher shell to the $K(n=1)$ shell are labeled as $K$ X-rays. X-rays produced in a transition from the $L(n=2)$ shell are called $K_{\alpha}$ X-rays; X-rays produced in a transition from the $M(n=3)$ shell are called $K_{\beta}$ X-rays; X-rays produced in a transition from the $N(n=4)$ shell are called $K_{\gamma}$ X-rays; and so forth. Transitions from higher shells to $L$ and $M$ shells are labeled similarly. These transitions are represented by an energy-level diagram in Figure 8.22.

The distribution of X-ray wavelengths produced by striking metal with a beam of electrons is given in Figure 8.23. X-ray transitions in the target metal appear as peaks on top of the braking radiation curve. Photon frequencies corresponding to the spikes in the X-ray distribution are called characteristic frequencies, because they can be used to identify the target metal. The sharp cutoff wavelength (just below the $K_{\gamma}$ peak) corresponds to an electron that loses all of its energy to a single photon. Radiation of shorter wavelengths is forbidden by the conservation of energy.

## EXAMPLE 8.7

## X-Rays from Aluminum

Estimate the characteristic energy and frequency of the $K_{\alpha}$ X-ray for aluminum $(Z=13)$.

## Strategy

A $K_{\alpha}$ X-ray is produced by the transition of an electron in the $L(n=2)$ shell to the $K(n=1)$ shell. An electron in the $L$ shell "sees" a charge $Z=13-1=12$, because one electron in the $K$ shell shields the nuclear charge. (Recall, two electrons are not in the $K$ shell because the other electron state is vacant.) The frequency of the emitted photon can be estimated from the energy difference between the $L$ and $K$ shells.

## Solution

The energy difference between the $L$ and $K$ shells in a hydrogen atom is $10.2 \mathrm{eV}$. Assuming that other electrons in the $L$ shell or in higher-energy shells do not shield the nuclear charge, the energy difference between the $L$ and $K$ shells in an atom with $Z=13$ is approximately

$$
\Delta E_{L \rightarrow K} \approx(Z-1)^{2}(10.2 \mathrm{eV})=(13-1)^{2}(10.2 \mathrm{eV})=1.47 \times 10^{3} \mathrm{eV}
$$

Based on the relationship $f=\left(\Delta E_{L \rightarrow K}\right) / h$, the frequency of the X-ray is

$$
f=\frac{1.47 \times 10^{3} \mathrm{eV}}{4.14 \times 10^{-15} \mathrm{eV} \cdot \mathrm{s}}=3.55 \times 10^{17} \mathrm{~Hz}
$$

## Significance

The wavelength of the typical X-ray is $0.1-10 \mathrm{~nm}$. In this case, the wavelength is:

$$
\lambda=\frac{c}{f}=\frac{3.0 \times 10^{8} \mathrm{~m} / \mathrm{s}}{3.55 \times 10^{17} \mathrm{~Hz}}=8.5 \times 10^{-10}=0.85 \mathrm{~nm}
$$

Hence, the transition $L \rightarrow K$ in aluminum produces X-ray radiation.

X-ray production provides an important test of quantum mechanics. According to the Bohr model, the energy of a $K_{\alpha}$ X-ray depends on the nuclear charge or atomic number, $Z$. If $Z$ is large, Coulomb forces in the atom are large, energy differences $(\Delta E)$ are large, and, therefore, the energy of radiated photons is large. To illustrate, consider a single electron in a multi-electron atom. Neglecting interactions between the electrons, the allowed energy levels are

$$
E_{n}=-\frac{Z^{2}(13.6 \mathrm{eV})}{n^{2}}
$$

where $n=1,2, \ldots$ and $Z$ is the atomic number of the nucleus. However, an electron in the $L(n=2)$ shell "sees" a charge $Z-1$, because one electron in the $K$ shell shields the nuclear charge. (Recall that there is only one electron in the $K$ shell because the other electron was "knocked out.") Therefore, the approximate energies of the electron in the $L$ and $K$ shells are

$$
\begin{aligned}
& E_{L} \approx-\frac{(Z-1)^{2}(13.6 \mathrm{eV})}{2^{2}} \\
& E_{K} \approx-\frac{(Z-1)^{2}(13.6 \mathrm{eV})}{1^{2}}
\end{aligned}
$$

The energy carried away by a photon in a transition from the $L$ shell to the $K$ shell is therefore

$$
\begin{aligned}
\Delta E_{L \rightarrow K} & =(Z-1)^{2}(13.6 \mathrm{eV})\left(\frac{1}{1^{2}}-\frac{1}{2^{2}}\right) \\
& =(Z-1)^{2}(10.2 \mathrm{eV})
\end{aligned}
$$

where $Z$ is the atomic number. In general, the X-ray photon energy for a transition from an outer shell to the $K$ shell is

$$
\Delta E_{L \rightarrow K}=h f=\text { constant } \times(Z-1)^{2}
$$

or

$$
(Z-1)=\operatorname{constant} \sqrt{f}
$$

where $f$ is the frequency of a $K_{\alpha}$ X-ray. This equation is Moseley's law. For large values of $Z$, we have approximately

$$
Z \approx \text { constant } \sqrt{f}
$$

This prediction can be checked by measuring $f$ for a variety of metal targets. This model is supported if a plot of $Z$ versus $\sqrt{f}$ data (called a Moseley plot) is linear. Comparison of model predictions and experimental results, for both the $K$ and $L$ series, is shown in Figure 8.24. The data support the model that X-rays are produced when an outer shell electron drops in energy to fill a vacancy in an inner shell.

## EXAMPLE 8.8

## Characteristic X-Ray Energy

Calculate the approximate energy of a $K_{\alpha}$ X-ray from a tungsten anode in an X-ray tube.

## Strategy

Two electrons occupy a filled $K$ shell. A vacancy in this shell would leave one electron, so the effective charge for an electron in the $L$ shell would be $Z-1$ rather than $Z$. For tungsten, $Z=74$, so the effective charge is 73 . This number can be used to calculate the energy-level difference between the $L$ and $K$ shells, and, therefore, the energy carried away by a photon in the transition $L \rightarrow K$.

## Solution

The effective $Z$ is 73 , so the $K_{\alpha}$ X-ray energy is given by

$$
E_{K_{\alpha}}=\Delta E=E_{\mathrm{i}}-E_{\mathrm{f}}=E_{2}-E_{1},
$$

where

$$
E_{1}=-\frac{Z^{2}}{1^{2}} E_{0}=-\frac{73^{2}}{1}(13.6 \mathrm{eV})=-72.5 \mathrm{keV}
$$

and

$$
E_{2}=-\frac{Z^{2}}{2^{2}} E_{0}=-\frac{73^{2}}{4}(13.6 \mathrm{eV})=-18.1 \mathrm{keV}
$$

Thus,

$$
E_{K_{\alpha}}=-18.1 \mathrm{keV}-(-72.5 \mathrm{keV})=54.4 \mathrm{keV}
$$

## Significance

This large photon energy is typical of X-rays. X-ray energies become progressively larger for heavier elements because their energy increases approximately as $Z^{2}$. An acceleration voltage of more than 50,000 volts is needed to "knock out" an inner electron from a tungsten atom.

## X-ray Technology

$\mathrm{X}$-rays have many applications, such as in medical diagnostics (Figure 8.25), inspection of luggage at airports (Figure 8.26), and even detection of cracks in crucial aircraft components. The most common X-ray images are due to shadows. Because $\mathrm{X}$-ray photons have high energy, they penetrate materials that are opaque to visible light. The more energy an $\mathrm{X}$-ray photon has, the more material it penetrates. The depth of penetration is related to the density of the material, as well as to the energy of the photon. The denser the material, the fewer X-ray photons get through and the darker the shadow. X-rays are effective at identifying bone breaks and tumors; however, overexposure to $\mathrm{X}$-rays can damage cells in biological organisms.

A standard X-ray image provides a two-dimensional view of the object. However, in medical applications, this
view does not often provide enough information to draw firm conclusions. For example, in a two-dimensional X-ray image of the body, bones can easily hide soft tissues or organs. The CAT (computed axial tomography) scanner addresses this problem by collecting numerous X-ray images in "slices" throughout the body. Complex computer-image processing of the relative absorption of the X-rays, in different directions, can produce a highly detailed three-dimensional X-ray image of the body.

X-rays can also be used to probe the structures of atoms and molecules. Consider X-rays incident on the surface of a crystalline solid. Some X-ray photons reflect at the surface, and others reflect off the "plane" of atoms just below the surface. Interference between these photons, for different angles of incidence, produces a beautiful image on a screen (Figure 8.27). The interaction of X-rays with a solid is called X-ray diffraction. The most famous example using X-ray diffraction is the discovery of the double-helix structure of DNA.

### 8.6 Lasers

A laser is device that emits coherent and monochromatic light. The light is coherent if photons that compose the light are in-phase, and monochromatic if the photons have a single frequency (color). When a gas in the laser absorbs radiation, electrons are elevated to different energy levels. Most electrons return immediately to the ground state, but others linger in what is called a metastable state. It is possible to place a majority of these
atoms in a metastable state, a condition called a population inversion.

When a photon of energy disturbs an electron in a metastable state (Figure 8.28), the electron drops to the lower-energy level and emits an addition photon, and the two photons proceed off together. This process is called stimulated emission. It occurs with relatively high probability when the energy of the incoming photon is equal to the energy difference between the excited and "de-excited" energy levels of the electron $(\Delta E=h f)$. Hence, the incoming photon and the photon produced by de-excitation have the same energy, hf. These photons encounter more electrons in the metastable state, and the process repeats. The result is a cascade or chain reaction of similar de-excitations. Laser light is coherent because all light waves in laser light share the same frequency (color) and the same phase (any two points of along a line perpendicular to the direction of motion are on the "same part" of the wave"). A schematic diagram of coherent and incoherent light wave pattern is given in Figure 8.29.

Lasers are used in a wide range of applications, such as in communication (optical fiber phone lines), entertainment (laser light shows), medicine (removing tumors and cauterizing vessels in the retina), and in retail sales (bar code readers). Lasers can also be produced by a large range of materials, including solids (for example, the ruby crystal), gases (helium-gas mixture), and liquids (organic dyes). Recently, a laser was even created using gelatin-an edible laser! Below we discuss two practical applications in detail: CD players and Blu-Ray Players.

## CD Player

A CD player reads digital information stored on a compact disc (CD). A CD is 6-inch diameter disc made of plastic that contains small "bumps" and "pits" nears its surface to encode digital or binary data (Figure 8.30). The bumps and pits appear along a very thin track that spirals outwards from the center of the disc. The width of the track is smaller than 1/20th the width of a human hair, and the heights of the bumps are even smaller yet.

A CD player uses a laser to read this digital information. Laser light is suited to this purpose, because coherent light can be focused onto an incredibly small spot and therefore distinguish between bumps and pits in the CD. After processing by player components (including a diffraction grating, polarizer, and collimator), laser light is focused by a lens onto the CD surface. Light that strikes a bump ("land") is merely reflected, but light that strikes a "pit" destructively interferes, so no light returns (the details of this process are not important to this discussion). Reflected light is interpreted as a " 1 " and unreflected light is interpreted as a " 0 ." The resulting digital signal is converted into an analog signal, and the analog signal is fed into an amplifier that powers a device such as a pair of headphones. The laser system of a CD player is shown in Figure 8.31.

## Blu-Ray Player

Like a CD player, a Blu-Ray player reads digital information (video or audio) stored on a disc, and a laser is used to record this information. The pits on a Blu-Ray disc are much smaller and more closely packed together than for a CD, so much more information can be stored. As a result, the resolving power of the laser must be greater. This is achieved using short wavelength $(\lambda=405 \mathrm{~nm})$ blue laser light-hence, the name "Blu-" Ray. (CDs and DVDs use red laser light.) The different pit sizes and player-hardware configurations of a CD, DVD, and Blu-Ray player are shown in Figure 8.32. The pit sizes of a Blu-Ray disk are more than twice as small as the pits on a DVD or CD. Unlike a CD, a Blu-Ray disc store data on a polycarbonate layer, which places the data closer to the lens and avoids readability problems. A hard coating is used to protect the data since it is so close to the surface.

