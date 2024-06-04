# CHAPTER 7 Quantum Mechanics 

INTRODUCTION Quantum mechanics is a powerful framework for understanding the motions and interactions of particles at small scales, such as atoms and molecules. The ideas behind quantum mechanics often appear quite strange. In many ways, our everyday experience with the macroscopic physical world does not prepare us for the microscopic world of quantum mechanics. The purpose of this chapter is to introduce you to this exciting world.

Pictured above is a quantum-computer processor. This device is the "brain" of a quantum computer that operates at near-absolute zero temperatures. Unlike a digital computer, which encodes information in binary digits (definite states of either zero or one), a quantum computer encodes information in quantum bits or
qubits (mixed states of zero and one). Quantum computers are discussed in the first section of this chapter.

### 7.1 Wave Functions

In the preceding chapter, we saw that particles act in some cases like particles and in other cases like waves. But what does it mean for a particle to "act like a wave"? What precisely is "waving"? What rules govern how this wave changes and propagates? How is the wave function used to make predictions? For example, if the amplitude of an electron wave is given by a function of position and time, $\Psi(x, t)$, defined for all $x$, where exactly is the electron? The purpose of this chapter is to answer these questions.

## Using the Wave Function

A clue to the physical meaning of the wave function $\Psi(x, t)$ is provided by the two-slit interference of monochromatic light (Figure 7.2). (See also Electromagnetic Waves and Interference.) The wave function of a light wave is given by $E(x, t)$, and its energy density is given by $|E|^{2}$, where $E$ is the electric field strength. The energy of an individual photon depends only on the frequency of light, $\varepsilon_{\text {photon }}=h f$, so $|E|^{2}$ is proportional to the number of photons. When light waves from $S_{1}$ interfere with light waves from $S_{2}$ at the viewing screen (a distance $D$ away), an interference pattern is produced (part (a) of the figure). Bright fringes correspond to points of constructive interference of the light waves, and dark fringes correspond to points of destructive interference of the light waves (part (b)).

Suppose the screen is initially unexposed to light. If the screen is exposed to very weak light, the interference pattern appears gradually (Figure 7.2(c), left to right). Individual photon hits on the screen appear as dots. The dot density is expected to be large at locations where the interference pattern will be, ultimately, the most intense. In other words, the probability (per unit area) that a single photon will strike a particular spot on the screen is proportional to the square of the total electric field, $|E|^{2}$ at that point. Under the right conditions, the same interference pattern develops for matter particles, such as electrons.

The square of the matter wave $|\Psi|^{2}$ in one dimension has a similar interpretation as the square of the electric field $|E|^{2}$. It gives the probability that a particle will be found at a particular position and time per unit length, also called the probability density. The probability $(P)$ a particle is found in a narrow interval $(x, x+d x)$ at time $t$ is therefore

$$
P(x, x+d x)=|\Psi(x, t)|^{2} d x
$$

(Later, we define the magnitude squared for the general case of a function with "imaginary parts.") This probabilistic interpretation of the wave function is called the Born interpretation. Examples of wave functions and their squares for a particular time $t$ are given in Figure 7.3.

If the wave function varies slowly over the interval $\Delta x$, the probability a particle is found in the interval is approximately

$$
P(x, x+\Delta x) \approx|\Psi(x, t)|^{2} \Delta x
$$

Notice that squaring the wave function ensures that the probability is positive. (This is analogous to squaring the electric field strength-which may be positive or negative-to obtain a positive value of intensity.) However, if the wave function does not vary slowly, we must integrate:

$$
P(x, x+\Delta x)=\int_{x}^{x+\Delta x}|\Psi(x, t)|^{2} d x
$$

This probability is just the area under the function $|\Psi(x, t)|^{2}$ between $x$ and $x+\Delta x$. The probability of finding the particle "somewhere" (the normalization condition) is

$$
P(-\infty,+\infty)=\int_{-\infty}^{\infty}|\Psi(x, t)|^{2} d x=1
$$

For a particle in two dimensions, the integration is over an area and requires a double integral; for a particle in three dimensions, the integration is over a volume and requires a triple integral. For now, we stick to the simple one-dimensional case.

## EXAMPLE 7.1

## Where Is the Ball? (Part I)

A ball is constrained to move along a line inside a tube of length $L$. The ball is equally likely to be found anywhere in the tube at some time $t$. What is the probability of finding the ball in the left half of the tube at that
time? (The answer is $50 \%$, of course, but how do we get this answer by using the probabilistic interpretation of the quantum mechanical wave function?)

## Strategy

The first step is to write down the wave function. The ball is equally like to be found anywhere in the box, so one way to describe the ball with a constant wave function (Figure 7.4). The normalization condition can be used to find the value of the function and a simple integration over half of the box yields the final answer.

## Solution

The wave function of the ball can be written as $\Psi(x, t)=C(0<x<L)$, where $C$ is a constant, and $\Psi(x, t)=0$ otherwise. We can determine the constant $C$ by applying the normalization condition (we set $t=0$ to simplify the notation):

$$
P(x=-\infty,+\infty)=\int_{-\infty}^{\infty}|C|^{2} d x=1
$$

This integral can be broken into three parts: (1) negative infinity to zero, (2) zero to $L$, and (3) $L$ to infinity. The particle is constrained to be in the tube, so $C=0$ outside the tube and the first and last integrations are zero. The above equation can therefore be written

$$
P(x=0, L)=\int_{0}^{L}|C|^{2} d x=1
$$

The value $C$ does not depend on $x$ and can be taken out of the integral, so we obtain

$$
||^{2} \int_{0}^{\mathrm{L}} d x=1
$$

Integration gives

$$
C=\sqrt{\frac{1}{L}}
$$

To determine the probability of finding the ball in the first half of the box $(0<x<L)$, we have

$$
P(x=0, L / 2)=\int_{0}^{L / 2}\left|\sqrt{\frac{1}{L}}\right|^{2} d x=\left(\frac{1}{L}\right) \frac{L}{2}=0.50
$$

## Significance

The probability of finding the ball in the first half of the tube is $50 \%$, as expected. Two observations are noteworthy. First, this result corresponds to the area under the constant function from $x=0$ to $L / 2$ (the area of a square left of $L / 2)$. Second, this calculation requires an integration of the square of the wave function. A common mistake in performing such calculations is to forget to square the wave function before integration.

## EXAMPLE 7.2

## Where Is the Ball? (Part II)

A ball is again constrained to move along a line inside a tube of length $L$. This time, the ball is found preferentially in the middle of the tube. One way to represent its wave function is with a simple cosine function (Figure 7.5). What is the probability of finding the ball in the last one-quarter of the tube?

## Strategy

We use the same strategy as before. In this case, the wave function has two unknown constants: One is associated with the wavelength of the wave and the other is the amplitude of the wave. We determine the amplitude by using the boundary conditions of the problem, and we evaluate the wavelength by using the normalization condition. Integration of the square of the wave function over the last quarter of the tube yields the final answer. The calculation is simplified by centering our coordinate system on the peak of the wave function.

## Solution

The wave function of the ball can be written

$$
\Psi(x, 0)=A \cos (k x)(-L / 2<x<L / 2)
$$

where $A$ is the amplitude of the wave function and $k=2 \pi / \lambda$ is its wave number. Beyond this interval, the amplitude of the wave function is zero because the ball is confined to the tube. Requiring the wave function to terminate at the right end of the tube gives

$$
\Psi\left(x=\frac{L}{2}, 0\right)=0
$$

Evaluating the wave function at $x=L / 2$ gives

$$
A \cos (k L / 2)=0
$$

This equation is satisfied if the argument of the cosine is an integral multiple of $\pi / 2,3 \pi / 2,5 \pi / 2$, and so on. In this case, we have

$$
\frac{k L}{2}=\frac{\pi}{2}
$$

or

$$
k=\frac{\pi}{L}
$$

Applying the normalization condition gives $A=\sqrt{2 / L}$, so the wave function of the ball is

$$
\Psi(x, 0)=\sqrt{\frac{2}{L}} \cos (\pi x / L),-L / 2<x<L / 2
$$

To determine the probability of finding the ball in the last quarter of the tube, we square the function and integrate:

$$
P(x=L / 4, L / 2)=\int_{L / 4}^{L / 2}\left|\sqrt{\frac{2}{L}} \cos \left(\frac{\pi x}{L}\right)\right|^{2} d x=0.091
$$

## Significance

The probability of finding the ball in the last quarter of the tube is $9.1 \%$. The ball has a definite wavelength $(\lambda=2 L)$. If the tube is of macroscopic length $(L=1 \mathrm{~m})$, the momentum of the ball is

$$
p=\frac{h}{\lambda}=\frac{h}{2 L} \sim 10^{-36} \mathrm{~m} / \mathrm{s}
$$

This momentum is much too small to be measured by any human instrument.

## An Interpretation of the Wave Function

We are now in position to begin to answer the questions posed at the beginning of this section. First, for a traveling particle described by $\Psi(x, t)=A \sin (k x-\omega t)$, what is "waving?" Based on the above discussion, the answer is a mathematical function that can, among other things, be used to determine where the particle is likely to be when a position measurement is performed. Second, how is the wave function used to make predictions? If it is necessary to find the probability that a particle will be found in a certain interval, square the wave function and integrate over the interval of interest. Soon, you will learn soon that the wave function can be used to make many other kinds of predictions, as well.

Third, if a matter wave is given by the wave function $\Psi(x, t)$, where exactly is the particle? Two answers exist: (1) when the observer is not looking (or the particle is not being otherwise detected), the particle is everywhere $(x=-\infty,+\infty)$; and (2) when the observer is looking (the particle is being detected), the particle "jumps into" a particular position state $(x, x+d x)$ with a probability given by $P(x, x+d x)=|\Psi(x, t)|^{2} d x-$ a process called state reduction or wave function collapse. This answer is called the Copenhagen interpretation of the wave function, or of quantum mechanics.

To illustrate this interpretation, consider the simple case of a particle that can occupy a small container either at $x_{1}$ or $x_{2}$ (Figure 7.6). In classical physics, we assume the particle is located either at $x_{1}$ or $x_{2}$ when the observer is not looking. However, in quantum mechanics, the particle may exist in a state of indefinite position-that is, it may be located at $x_{1}$ and $x_{2}$ when the observer is not looking. The assumption that a particle can only have one value of position (when the observer is not looking) is abandoned. Similar comments can be made of other measurable quantities, such as momentum and energy.

The bizarre consequences of the Copenhagen interpretation of quantum mechanics are illustrated by a creative thought experiment first articulated by Erwin Schrödinger (National Geographic, 2013) (Figure 7.7):

"A cat is placed in a steel box along with a Geiger counter, a vial of poison, a hammer, and a radioactive substance. When the radioactive substance decays, the Geiger detects it and triggers the hammer to release the poison, which subsequently kills the cat. The radioactive decay is a random [probabilistic] process, and there is no way to predict when it will happen. Physicists say the atom exists in a state known as a superposition-both decayed and not decayed at the same time. Until the box is opened, an observer doesn't know whether the cat is alive or dead-because the cat's fate is intrinsically tied to whether or not the atom has decayed and the cat would [according to the Copenhagen interpretation] be "living and dead ... in equal parts" until it is observed."

Schrödinger took the absurd implications of this thought experiment (a cat simultaneously dead and alive) as an argument against the Copenhagen interpretation. However, this interpretation remains the most commonly taught view of quantum mechanics.

Two-state systems (left and right, atom decays and does not decay, and so on) are often used to illustrate the principles of quantum mechanics. These systems find many applications in nature, including electron spin and mixed states of particles, atoms, and even molecules. Two-state systems are also finding application in the quantum computer, as mentioned in the introduction of this chapter. Unlike a digital computer, which encodes information in binary digits (zeroes and ones), a quantum computer stores and manipulates data in the form of quantum bits, or qubits. In general, a qubit is not in a state of zero or one, but rather in a mixed state of zero and one. If a large number of qubits are placed in the same quantum state, the measurement of an individual qubit would produce a zero with a probability $p$, and a one with a probability $q=1-p$. Many scientists believe that quantum computers are the future of the computer industry.

## Complex Conjugates

Later in this section, you will see how to use the wave function to describe particles that are "free" or bound by forces to other particles. The specific form of the wave function depends on the details of the physical system. A peculiarity of quantum theory is that these functions are usually complex functions. A complex function is one that contains one or more imaginary numbers $(i=\sqrt{-1})$. Experimental measurements produce real (nonimaginary) numbers only, so the above procedure to use the wave function must be slightly modified. In general, the probability that a particle is found in the narrow interval $(x, x+d x)$ at time $t$ is given by

$$
P(x, x+d x)=|\Psi(x, t)|^{2} d x=\Psi^{*}(x, t) \Psi(x, t) d x
$$

where $\Psi^{*}(x, t)$ is the complex conjugate of the wave function. The complex conjugate of a function is obtaining by replacing every occurrence of $i=\sqrt{-1}$ in that function with $-i$. This procedure eliminates complex numbers in all predictions because the product $\Psi^{*}(x, t) \Psi(x, t)$ is always a real number.

Consider the motion of a free particle that moves along the $x$-direction. As the name suggests, a free particle experiences no forces and so moves with a constant velocity. As we will see in a later section of this chapter, a formal quantum mechanical treatment of a free particle indicates that its wave function has real and complex parts. In particular, the wave function is given by

$$
\Psi(x, t)=A \cos (k x-\omega t)+i A \sin (k x-\omega t)
$$

where $A$ is the amplitude, $k$ is the wave number, and $\omega$ is the angular frequency. Using Euler's formula, $e^{i \phi}=\cos (\phi)+i \sin (\phi)$, this equation can be written in the form

$$
\Psi(x, t)=A e^{i(k x-\omega t)}=A e^{i \phi}
$$

where $\phi$ is the phase angle. If the wave function varies slowly over the interval $\Delta x$, the probability of finding the particle in that interval is

$$
P(x, x+\Delta x) \approx \Psi^{*}(x, t) \Psi(x, t) \Delta x=\left(A e^{i \phi}\right)\left(A^{*} e^{-i \phi}\right) \Delta x=\left(A^{*} A\right) \Delta x
$$

If $A$ has real and complex parts $(a+i b$, where $a$ and $b$ are real constants), then

$$
A^{*} A=(a+i b)(a-i b)=a^{2}+b^{2}
$$

Notice that the complex numbers have vanished. Thus,

$$
P(x, x+\Delta x) \approx|A|^{2} \Delta x
$$

is a real quantity. The interpretation of $\Psi^{*}(x, t) \Psi(x, t)$ as a probability density ensures that the predictions of quantum mechanics can be checked in the "real world."

## Expectation Values

In classical mechanics, the solution to an equation of motion is a function of a measurable quantity, such as $x(t)$, where $x$ is the position and $t$ is the time. Note that the particle has one value of position for any time $t$. In quantum mechanics, however, the solution to an equation of motion is a wave function, $\Psi(x, t)$. The particle has many values of position for any time $t$, and only the probability density of finding the particle, $|\Psi(x, t)|^{2}$, can be known. The average value of position for a large number of particles with the same wave function is expected to be

$$
\langle x\rangle=\int_{-\infty}^{\infty} x P(x, t) d x=\int_{-\infty}^{\infty} x \Psi^{*}(x, t) \Psi(x, t) d x
$$

This is called the expectation value of the position. It is usually written

where the $x$ is sandwiched between the wave functions. The reason for this will become apparent soon. Formally, $x$ is called the position operator.

At this point, it is important to stress that a wave function can be written in terms of other quantities as well, such as velocity ( $v$ ), momentum ( $p$ ), and kinetic energy $(K)$. The expectation value of momentum, for example, can be written

$$
\langle p\rangle=\int_{-\infty}^{\infty} \Psi^{*}(p, t) p \Psi(p, t) d p
$$

Where $d p$ is used instead of $d x$ to indicate an infinitesimal interval in momentum. In some cases, we know the wave function in position, $\Psi(x, t)$, but seek the expectation of momentum. The procedure for doing this is

$$
\langle p\rangle=\int_{-\infty}^{\infty} \Psi^{*}(x, t)\left(-i \hbar \frac{d}{d x}\right) \Psi(x, t) d x
$$

where the quantity in parentheses, sandwiched between the wave functions, is called the momentum operator in the $x$-direction. [The momentum operator in Equation 7.9 is said to be the position-space representation of the momentum operator.] The momentum operator must act (operate) on the wave function to the right, and then the result must be multiplied by the complex conjugate of the wave function on the left, before integration. The momentum operator in the $x$-direction is sometimes denoted

$$
\left(p_{x}\right)_{\mathrm{op}}=-i \hbar \frac{d}{d x}
$$

Momentum operators for the $y$ - and $z$-directions are defined similarly. This operator and many others are derived in a more advanced course in modern physics. In some cases, this derivation is relatively simple. For example, the kinetic energy operator is just

$$
(K)_{\mathrm{op}}=\frac{1}{2} m\left(v_{x}\right)_{\mathrm{op}}^{2}=\frac{\left(p_{x}\right)_{\mathrm{op}}^{2}}{2 m}=\frac{\left(-i \hbar \frac{d}{d x}\right)^{2}}{2 m}=\frac{-\hbar^{2}}{2 m}\left(\frac{d}{d x}\right)\left(\frac{d}{d x}\right)
$$

Thus, if we seek an expectation value of kinetic energy of a particle in one dimension, two successive ordinary derivatives of the wave function are required before integration.

Expectation-value calculations are often simplified by exploiting the symmetry of wave functions. Symmetric wave functions can be even or odd. An even function is a function that satisfies

$$
\psi(x)=\psi(-x)
$$

In contrast, an odd function is a function that satisfies

$$
\psi(x)=-\psi(-x)
$$

An example of even and odd functions is shown in Figure 7.8. An even function is symmetric about the $y$-axis. This function is produced by reflecting $\psi(x)$ for $x>0$ about the vertical $y$-axis. By comparison, an odd function is generated by reflecting the function about the $y$-axis and then about the $x$-axis. (An odd function is also referred to as an anti-symmetric function.)

In general, an even function times an even function produces an even function. A simple example of an even function is the product $x^{2} e^{-x^{2}}$ (even times even is even). Similarly, an odd function times an odd function produces an even function, such as $x \sin x$ (odd times odd is even). However, an odd function times an even function produces an odd function, such as $x e^{-x^{2}}$ (odd times even is odd). The integral over all space of an odd function is zero, because the total area of the function above the $x$-axis cancels the (negative) area below it. As the next example shows, this property of odd functions is very useful.

## EXAMPLE 7.3

## Expectation Value (Part I)

The normalized wave function of a particle is

$$
\psi(x)=e^{-|x| / x_{0}} / \sqrt{x_{0}}
$$

Find the expectation value of position.

## Strategy

Substitute the wave function into Equation 7.7 and evaluate. The position operator introduces a multiplicative factor only, so the position operator need not be "sandwiched."

## Solution

First multiply, then integrate:

$$
\langle x\rangle=\int_{-\infty}^{+\infty} d x x|\psi(x)|^{2}=\int_{-\infty}^{+\infty} d x x\left|\frac{e^{-|x| / x_{0}}}{\sqrt{x_{0}}}\right|^{2}=\frac{1}{x_{0}} \int_{-\infty}^{+\infty} d x x e^{-2|x| / x_{0}}=0
$$

## Significance

The function in the integrand ( $\left.x e^{-2|x| / x_{0}}\right)$ is odd since it is the product of an odd function ( $x$ ) and an even function $\left(e^{-2|x| / x_{0}}\right)$. The integral vanishes because the total area of the function about the $x$-axis cancels the (negative) area below it. The result $(\langle x\rangle=0)$ is not surprising since the probability density function is symmetric about $x=0$.

## EXAMPLE 7.4

## Expectation Value (Part II)

The time-dependent wave function of a particle confined to a region between 0 and $L$ is

$$
\psi(x, t)=A e^{-i \omega t} \sin (\pi x / L)
$$

where $\omega$ is angular frequency and $E$ is the energy of the particle. (Note: The function varies as a sine because of the limits $(0$ to $L$ ). When $x=0$, the sine factor is zero and the wave function is zero, consistent with the boundary conditions.) Calculate the expectation values of position, momentum, and kinetic energy.

## Strategy

We must first normalize the wave function to find $A$. Then we use the operators to calculate the expectation values.

## Solution

Computation of the normalization constant:

$1=\int_{0}^{L} d x \psi^{*}(x) \psi(x)=\int_{0}^{L} d x\left(A e^{+i \omega t} \sin \frac{\pi x}{L}\right)\left(A e^{-i \omega t} \sin \frac{\pi x}{L}\right)=A^{2} \int_{0}^{L} d x \sin ^{2} \frac{\pi x}{L}=A^{2} \frac{L}{2} \Rightarrow A=\sqrt{\frac{2}{L}}$.

The expectation value of position is

$$
\langle x\rangle=\int_{0}^{L} d x \psi^{*}(x) x \psi(x)=\int_{0}^{L} d x\left(A e^{+i \omega t} \sin \frac{\pi x}{L}\right) x\left(A e^{-i \omega t} \sin \frac{\pi x}{L}\right)=A^{2} \int_{0}^{L} d x x \sin ^{2} \frac{\pi x}{L}=A^{2} \frac{L^{2}}{4}=\frac{L}{2}
$$

The expectation value of momentum in the $x$-direction also requires an integral. To set this integral up, the associated operator must- by rule-act to the right on the wave function $\psi(x)$ :

$$
-i \hbar \frac{d}{d x} \psi(x)=-i \hbar \frac{d}{d x} A e^{-i \omega t} \sin \frac{\pi x}{L}=-i \frac{A h}{2 L} e^{-i \omega t} \cos \frac{\pi x}{L}
$$

Therefore, the expectation value of momentum is

$$
\langle p\rangle=\int_{0}^{L} d x\left(A e^{+i \omega t} \sin \frac{\pi x}{L}\right)\left(-i \frac{A h}{2 L} e^{-i \omega t} \cos \frac{\pi x}{L}\right)=-i \frac{A^{2} h}{4 L} \int_{0}^{L} d x \sin \frac{2 \pi x}{L}=0
$$

The function in the integral is a sine function with a wavelength equal to the width of the well, $L-$ an odd function about $x=L / 2$. As a result, the integral vanishes.

The expectation value of kinetic energy in the $x$-direction requires the associated operator to act on the wave
function:

$$
-\frac{\hbar^{2}}{2 m} \frac{d^{2}}{d x^{2}} \psi(x)=-\frac{\hbar^{2}}{2 m} \frac{d^{2}}{d x^{2}} A e^{-i \omega t} \sin \frac{\pi x}{L}=-\frac{\hbar^{2}}{2 m} A e^{-i \omega t} \frac{d^{2}}{d x^{2}} \sin \frac{\pi x}{L}=\frac{A h^{2}}{8 m L^{2}} e^{-i \omega t} \sin \frac{\pi x}{L}
$$

Thus, the expectation value of the kinetic energy is

$$
\begin{gathered}
\langle K\rangle=\int_{0}^{L} d x\left(A e^{+i \omega t} \sin \frac{\pi x}{L}\right)\left(\frac{A h^{2}}{8 m L^{2}} e^{-i \omega t} \sin \frac{\pi x}{L}\right) \\
=\frac{A^{2} h^{2}}{8 m L^{2}} \int_{0}^{L} d x \sin ^{2} \frac{\pi x}{L}=\frac{A^{2} h^{2}}{8 m L^{2}} \frac{L}{2}=\frac{h^{2}}{8 m L^{2}}
\end{gathered}
$$

## Significance

The average position of a large number of particles in this state is $L / 2$. The average momentum of these particles is zero because a given particle is equally likely to be moving right or left. However, the particle is not at rest because its average kinetic energy is not zero. Finally, the probability density is

$$
|\psi|^{2}=(2 / L) \sin ^{2}(\pi x / L)
$$

This probability density is largest at location $L / 2$ and is zero at $x=0$ and at $x=L$. Note that these conclusions do not depend explicitly on time.

Quantum mechanics makes many surprising predictions. However, in 1920, Niels Bohr (founder of the Niels Bohr Institute in Copenhagen, from which we get the term "Copenhagen interpretation") asserted that the predictions of quantum mechanics and classical mechanics must agree for all macroscopic systems, such as orbiting planets, bouncing balls, rocking chairs, and springs. This correspondence principle is now generally accepted. It suggests the rules of classical mechanics are an approximation of the rules of quantum mechanics for systems with very large energies. Quantum mechanics describes both the microscopic and macroscopic world, but classical mechanics describes only the latter.

### 7.2 The Heisenberg Uncertainty Principle

Heisenberg's uncertainty principle is a key principle in quantum mechanics. Very roughly, it states that if we know everything about where a particle is located (the uncertainty of position is small), we know nothing about its momentum (the uncertainty of momentum is large), and vice versa. Versions of the uncertainty principle also exist for other quantities as well, such as energy and time. We discuss the momentum-position and energy-time uncertainty principles separately.

## Momentum and Position

To illustrate the momentum-position uncertainty principle, consider a free particle that moves along the $x$-direction. The particle moves with a constant velocity $u$ and momentum $p=m u$. According to de Broglie's relations, $p=\hbar k$ and $E=\hbar \omega$. As discussed in the previous section, the wave function for this particle is given by

and the probability density $\left|\psi_{k}(x, t)\right|^{2}=A^{2}$ is uniform and independent of time. The particle is equally likely to be found anywhere along the $x$-axis but has definite values of wavelength and wave number, and therefore momentum. The uncertainty of position is infinite (we are completely uncertain about position) and the uncertainty of the momentum is zero (we are completely certain about momentum). This account of a free particle is consistent with Heisenberg's uncertainty principle.

Similar statements can be made of localized particles. In quantum theory, a localized particle is modeled by a linear superposition of free-particle (or plane-wave) states called a wave packet. An example of a wave packet is shown in Figure 7.9. A wave packet contains many wavelengths and therefore by de Broglie's relations many momenta-possible in quantum mechanics! This particle also has many values of position, although the particle is confined mostly to the interval $\Delta x$. The particle can be better localized ( $\Delta x$ can be decreased) if more plane-wave states of different wavelengths or momenta are added together in the right way ( $\Delta p$ is increased). According to Heisenberg, these uncertainties obey the following relation.

## The Heisenberg Uncertainty Principle

The product of the uncertainty in position of a particle and the uncertainty in its momentum can never be less than one-half of the reduced Planck constant:

$$
\Delta x \quad \Delta p \geq \hbar / 2
$$

This relation expresses Heisenberg's uncertainty principle. It places limits on what we can know about a particle from simultaneous measurements of position and momentum. If $\Delta x$ is large, $\Delta p$ is small, and vice versa. Equation 7.15 can be derived in a more advanced course in modern physics. Reflecting on this relation in his work The Physical Principles of the Quantum Theory, Heisenberg wrote "Any use of the words 'position' and 'velocity' with accuracy exceeding that given by [the relation] is just as meaningless as the use of words whose sense is not defined."

Note that the uncertainty principle has nothing to do with the precision of an experimental apparatus. Even for perfect measuring devices, these uncertainties would remain because they originate in the wave-like nature of matter. The precise value of the product $\Delta x \Delta p$ depends on the specific form of the wave function. Interestingly, the Gaussian function (or bell-curve distribution) gives the minimum value of the uncertainty product: $\Delta x \quad \Delta p=\hbar / 2$.

## EXAMPLE 7.5

## The Uncertainty Principle Large and Small

Determine the minimum uncertainties in the positions of the following objects if their speeds are known with a precision of $1.0 \times 10^{-3} \mathrm{~m} / \mathrm{s}$ : (a) an electron and (b) a bowling ball of mass $6.0 \mathrm{~kg}$.

## Strategy

Given the uncertainty in speed $\Delta u=1.0 \times 10^{-3} \mathrm{~m} / \mathrm{s}$, we have to first determine the uncertainty in momentum $\Delta p=m \quad \Delta u$ and then invert Equation 7.15 to find the uncertainty in position $\Delta x=\hbar /(2 \Delta p)$.

## Solution

a. For the electron:

$$
\begin{aligned}
\Delta p & =m \Delta u=\left(9.1 \times 10^{-31} \mathrm{~kg}\right)\left(1.0 \times 10^{-3} \mathrm{~m} / \mathrm{s}\right)=9.1 \times 10^{-34} \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s} \\
\Delta x & =\frac{\hbar}{2 \Delta p}=5.8 \mathrm{~cm}
\end{aligned}
$$

b. For the bowling ball:

$$
\begin{aligned}
\Delta p & =m \Delta u=(6.0 \mathrm{~kg})\left(1.0 \times 10^{-3} \mathrm{~m} / \mathrm{s}\right)=6.0 \times 10^{-3} \mathrm{~kg} \cdot \mathrm{m} / \mathrm{s} \\
\Delta x & =\frac{\hbar}{2 \Delta p}=8.8 \times 10^{-33} \mathrm{~m}
\end{aligned}
$$

## Significance

Unlike the position uncertainty for the electron, the position uncertainty for the bowling ball is immeasurably small. Planck's constant is very small, so the limitations imposed by the uncertainty principle are not noticeable in macroscopic systems such as a bowling ball.

## EXAMPLE 7.6

## Uncertainty and the Hydrogen Atom

Estimate the ground-state energy of a hydrogen atom using Heisenberg's uncertainty principle. (Hint: According to early experiments, the size of a hydrogen atom is approximately $0.1 \mathrm{~nm}$.)

## Strategy

An electron bound to a hydrogen atom can be modeled by a particle bound to a one-dimensional box of length $L=0.1 \mathrm{~nm}$. The ground-state wave function of this system is a half wave, like that given in Example 7.1. This is the largest wavelength that can "fit" in the box, so the wave function corresponds to the lowest energy state. Note that this function is very similar in shape to a Gaussian (bell curve) function. We can take the average energy of a particle described by this function $(E)$ as a good estimate of the ground state energy $\left(E_{0}\right)$. This average energy of a particle is related to its average of the momentum squared, which is related to its momentum uncertainty.

## Solution

To solve this problem, we must be specific about what is meant by "uncertainty of position" and "uncertainty
of momentum." We identify the uncertainty of position $(\Delta x)$ with the standard deviation of position $\left(\sigma_{x}\right)$, and the uncertainty of momentum $(\Delta p)$ with the standard deviation of momentum $\left(\sigma_{p}\right)$. For the Gaussian function, the uncertainty product is

$$
\sigma_{x} \sigma_{p}=\frac{\hbar}{2}
$$

where

$$
\sigma_{x}^{2}=x^{2}-\bar{x}^{2} \text { and } \sigma_{p}^{2}=p^{2}-p^{2}
$$

The particle is equally likely to be moving left as moving right, so $\bar{p}=0$. Also, the uncertainty of position is comparable to the size of the box, so $\sigma_{x}=L$. The estimated ground state energy is therefore

$$
E_{0}=E_{\text {Gaussian }}=\frac{\overline{p^{2}}}{m}=\frac{\sigma_{p}^{2}}{2 m}=\frac{1}{2 m}\left(\frac{\hbar}{2 \sigma_{x}}\right)^{2}=\frac{1}{2 m}\left(\frac{\hbar}{2 L}\right)^{2}=\frac{\hbar^{2}}{8 m L^{2}}
$$

Multiplying numerator and denominator by $c^{2}$ gives

$$
E_{0}=\frac{(\hbar \mathrm{c})^{2}}{8\left(m c^{2}\right) L^{2}}=\frac{(197.3 \mathrm{eV} \cdot \mathrm{nm})^{2}}{8\left(0.511 \cdot 10^{6} \mathrm{eV}\right)(0.1 \mathrm{~nm})^{2}}=0.952 \mathrm{eV} \approx 1 \mathrm{eV}
$$

## Significance

Based on early estimates of the size of a hydrogen atom and the uncertainty principle, the ground-state energy of a hydrogen atom is in the eV range. The ionization energy of an electron in the ground-state energy is approximately $10 \mathrm{eV}$, so this prediction is roughly confirmed. (Note: The product $\hbar c$ is often a useful value in performing calculations in quantum mechanics.)

## Energy and Time

Another kind of uncertainty principle concerns uncertainties in simultaneous measurements of the energy of a quantum state and its lifetime,

$$
\Delta E \Delta t \geq \frac{\hbar}{2}
$$

where $\Delta E$ is the uncertainty in the energy measurement and $\Delta t$ is the uncertainty in the lifetime measurement. The energy-time uncertainty principle does not result from a relation of the type expressed by Equation 7.15 for technical reasons beyond this discussion. Nevertheless, the general meaning of the energy-time principle is that a quantum state that exists for only a short time cannot have a definite energy. The reason is that the frequency of a state is inversely proportional to time and the frequency connects with the energy of the state, so to measure the energy with good precision, the state must be observed for many cycles.

To illustrate, consider the excited states of an atom. The finite lifetimes of these states can be deduced from the shapes of spectral lines observed in atomic emission spectra. Each time an excited state decays, the emitted energy is slightly different and, therefore, the emission line is characterized by a distribution of spectral frequencies (or wavelengths) of the emitted photons. As a result, all spectral lines are characterized by spectral widths. The average energy of the emitted photon corresponds to the theoretical energy of the excited state and gives the spectral location of the peak of the emission line. Short-lived states have broad spectral widths and long-lived states have narrow spectral widths.

## EXAMPLE 7.7

## Atomic Transitions

An atom typically exists in an excited state for about $\Delta t=10^{-8} \mathrm{~s}$. Estimate the uncertainty $\Delta f$ in the frequency of emitted photons when an atom makes a transition from an excited state with the simultaneous emission of a photon with an average frequency of $f=7.1 \times 10^{14} \mathrm{~Hz}$. Is the emitted radiation monochromatic?

## Strategy

We invert Equation 7.16 to obtain the energy uncertainty $\Delta E \approx \hbar / 2 \Delta t$ and combine it with the photon energy $E=h \quad f$ to obtain $\Delta f$. To estimate whether or not the emission is monochromatic, we evaluate $\Delta f / f$.

## Solution

The spread in photon energies is $\Delta \quad E=h \Delta \quad f$. Therefore,

$$
\begin{aligned}
\Delta E & \approx \frac{\hbar}{2 \Delta t} \Rightarrow h \Delta f \approx \frac{\hbar}{2 \Delta t} \Rightarrow \Delta f \approx \frac{1}{4 \pi \Delta t}=\frac{1}{4 \pi\left(10^{-8} s_{s}\right.}=8.0 \times 10^{6} \mathrm{~Hz} \\
\frac{\Delta f}{f} & =\frac{8.0 \times 10^{6} \mathrm{~Hz}}{7.1 \times 10^{14} \mathrm{~Hz}}=1.1 \times 10^{-8}
\end{aligned}
$$

## Significance

Because the emitted photons have their frequencies within $1.1 \times 10^{-6}$ percent of the average frequency, the emitted radiation can be considered monochromatic.

### 7.3 The Schrödinger Equation

In the preceding two sections, we described how to use a quantum mechanical wave function and discussed Heisenberg's uncertainty principle. In this section, we present a complete and formal theory of quantum mechanics that can be used to make predictions. In developing this theory, it is helpful to review the wave theory of light. For a light wave, the electric field $E(x, t)$ obeys the relation

$$
\frac{\partial^{2} E}{\partial x^{2}}=\frac{1}{c^{2}} \frac{\partial^{2} E}{\partial t^{2}}
$$

where $c$ is the speed of light and the symbol $\partial$ represents a partial derivative. (Recall from Oscillations that a partial derivative is closely related to an ordinary derivative, but involves functions of more than one variable. When taking the partial derivative of a function by a certain variable, all other variables are held constant.) A light wave consists of a very large number of photons, so the quantity $|E(x, t)|^{2}$ can interpreted as a probability density of finding a single photon at a particular point in space (for example, on a viewing screen).

There are many solutions to this equation. One solution of particular importance is

$$
E(x, t)=A \sin (k x-\omega t),
$$

where $A$ is the amplitude of the electric field, $k$ is the wave number, and $\omega$ is the angular frequency. Combing this equation with Equation 7.17 gives

$$
k^{2}=\frac{\omega^{2}}{c^{2}}
$$

According to de Broglie's equations, we have $p=\hbar k$ and $E=\hbar \omega$. Substituting these equations in Equation 7.19 gives

$$
p=\frac{E}{c}
$$

or

$$
E=p c
$$

Therefore, according to Einstein's general energy-momentum equation (Equation 5.11), Equation 7.17 describes a particle with a zero rest mass. This is consistent with our knowledge of a photon.

This process can be reversed. We can begin with the energy-momentum equation of a particle and then ask what wave equation corresponds to it. The energy-momentum equation of a nonrelativistic particle in one dimension is

$$
E=\frac{p^{2}}{2 m}+U(x, t)
$$

where $p$ is the momentum, $m$ is the mass, and $U$ is the potential energy of the particle. The wave equation that goes with it turns out to be a key equation in quantum mechanics, called Schrödinger's time-dependent equation.

The Schrödinger Time-Dependent Equation

The equation describing the energy and momentum of a wave function is known as the Schrödinger equation:

$$
-\frac{\hbar^{2}}{2 m} \frac{\partial^{2} \Psi(x, t)}{\partial x^{2}}+U(x, t) \Psi(x, t)=i \hbar \frac{\partial \Psi(x, t)}{\partial t}
$$

As described in Potential Energy and Conservation of Energy, the force on the particle described by this equation is given by

$$
F=-\frac{\partial U(x, t)}{\partial x}
$$

This equation plays a role in quantum mechanics similar to Newton's second law in classical mechanics. Once the potential energy of a particle is specified-or, equivalently, once the force on the particle is specified-we can solve this differential equation for the wave function. The solution to Newton's second law equation (also a differential equation) in one dimension is a function $x(t)$ that specifies where an object is at any time $t$. The solution to Schrödinger's time-dependent equation provides a tool-the wave function-that can be used to determine where the particle is likely to be. This equation can be also written in two or three dimensions. Solving Schrödinger's time-dependent equation often requires the aid of a computer.

Consider the special case of a free particle. A free particle experiences no force $(F=0)$. Based on Equation 7.24, this requires only that

$$
U(x, t)=U_{0}=\text { constant }
$$

For simplicity, we set $U_{0}=0$. Schrödinger's equation then reduces to

$$
-\frac{\hbar^{2}}{2 m} \frac{\partial^{2} \Psi(x, t)}{\partial x^{2}}=i \hbar \frac{\partial \Psi(x, t)}{\partial t}
$$

A valid solution to this equation is

$$
\Psi(x, t)=A e^{i(k x-\omega t)}
$$

Not surprisingly, this solution contains an imaginary number $(i=\sqrt{-1})$ because the differential equation itself contains an imaginary number. As stressed before, however, quantum-mechanical predictions depend only on $|\Psi(x, t)|^{2}$, which yields completely real values. Notice that the real plane-wave solutions, $\Psi(x, t)=A \sin (k x-\omega t)$ and $\Psi(x, t)=A \cos (k x-\omega t)$, do not obey Schrödinger's equation. The temptation to think that a wave function can be seen, touched, and felt in nature is eliminated by the appearance of an imaginary number. In Schrödinger's theory of quantum mechanics, the wave function is merely a tool for calculating things.

If the potential energy function ( $U$ ) does not depend on time, it is possible to show that

$$
\Psi(x, t)=\psi(x) e^{-i \omega t}
$$

satisfies Schrödinger's time-dependent equation, where $\psi(x)$ is a time-independent function and $e^{-i \omega t}$ is a space-independent function. In other words, the wave function is separable into two parts: a space-only part and a time-only part. The factor $e^{-i \omega t}$ is sometimes referred to as a time-modulation factor since it modifies the space-only function. According to de Broglie, the energy of a matter wave is given by $E=\hbar \omega$, where $E$ is its total energy. Thus, the above equation can also be written as

$$
\Psi(x, t)=\psi(x) e^{-i E t / \hbar}
$$

Any linear combination of such states (mixed state of energy or momentum) is also valid solution to this equation. Such states can, for example, describe a localized particle (see Figure 7.9)

Combining Equation 7.23 and Equation 7.28, Schrödinger's time-dependent equation reduces to

$$
-\frac{\hbar^{2}}{2 m} \frac{d^{2} \psi(x)}{d x^{2}}+U(x) \psi(x)=E \psi(x)
$$

where $E$ is the total energy of the particle (a real number). This equation is called Schrödinger's timeindependent equation. Notice that we use "big psi" $(\Psi)$ for the time-dependent wave function and "little psi" $(\psi)$ for the time-independent wave function. The wave-function solution to this equation must be multiplied by the time-modulation factor to obtain the time-dependent wave function.

In the next sections, we solve Schrödinger's time-independent equation for three cases: a quantum particle in a box, a simple harmonic oscillator, and a quantum barrier. These cases provide important lessons that can be used to solve more complicated systems. The time-independent wave function $\psi(x)$ solutions must satisfy three conditions:

- $\psi(x)$ must be a continuous function.
- The first derivative of $\psi(x)$ with respect to space, $d \psi(x) / d x$, must be continuous, unless $V(x)=\infty$.
- $\psi(x)$ must not diverge ("blow up") at $x= \pm \infty$.

The first condition avoids sudden jumps or gaps in the wave function. The second condition requires the wave function to be smooth at all points, except in special cases. (In a more advanced course on quantum mechanics, for example, potential spikes of infinite depth and height are used to model solids). The third condition requires the wave function be normalizable. This third condition follows from Born's interpretation of quantum mechanics. It ensures that $|\psi(x)|^{2}$ is a finite number so we can use it to calculate probabilities.

### 7.4 The Quantum Particle in a Box

In this section, we apply Schrödinger's equation to a particle bound to a one-dimensional box. This special case provides lessons for understanding quantum mechanics in more complex systems. The energy of the particle is quantized as a consequence of a standing wave condition inside the box.

Consider a particle of mass $m$ that is allowed to move only along the $x$-direction and its motion is confined to the region between hard and rigid walls located at $x=0$ and at $x=L$ (Figure 7.10). Between the walls, the particle moves freely. This physical situation is called the infinite square well, described by the potential energy function

$$
U(x)= \begin{cases}0, & 0 \leq x \leq L \\ \infty, & \text { otherwise }\end{cases}
$$

Combining this equation with Schrödinger's time-independent wave equation gives

$$
\frac{-\hbar^{2}}{2 m} \frac{d^{2} \psi(x)}{d x^{2}}=E \psi(x), \text { for } 0 \leq x \leq L
$$

where $E$ is the total energy of the particle. What types of solutions do we expect? The energy of the particle is a positive number, so if the value of the wave function is positive (right side of the equation), the curvature of the wave function is negative, or concave down (left side of the equation). Similarly, if the value of the wave function is negative (right side of the equation), the curvature of the wave function is positive or concave up (left side of equation). This condition is met by an oscillating wave function, such as a sine or cosine wave. Since these waves are confined to the box, we envision standing waves with fixed endpoints at $x=0$ and $x=L$.

Solutions $\psi(x)$ to this equation have a probabilistic interpretation. In particular, the square $|\psi(x)|^{2}$ represents the probability density of finding the particle at a particular location $x$. This function must be integrated to determine the probability of finding the particle in some interval of space. We are therefore looking for a normalizable solution that satisfies the following normalization condition:

$$
\int_{0}^{L} d x|\psi(x)|^{2}=1
$$

The walls are rigid and impenetrable, which means that the particle is never found beyond the wall. Mathematically, this means that the solution must vanish at the walls:

$$
\psi(0)=\psi(L)=0
$$

We expect oscillating solutions, so the most general solution to this equation is

$$
\psi_{k}(x)=A_{k} \cos k x+B_{k} \sin k x
$$

where $k$ is the wave number, and $A_{k}$ and $B_{k}$ are constants. Applying the boundary condition expressed by Equation 7.34 gives

$$
\psi_{k}(0)=A_{k} \cos (k \cdot 0)+B_{k} \sin (k \cdot 0)=A_{k}=0
$$

Because we have $A_{k}=0$, the solution must be

$$
\psi_{k}(x)=B_{k} \sin k x
$$

If $\boldsymbol{B}_{k}$ is zero, $\psi_{k}(x)=0$ for all values of $x$ and the normalization condition, Equation 7.33, cannot be satisfied. Assuming $B_{k} \neq 0$, Equation 7.34 for $x=L$ then gives

$$
0=B_{k} \sin (k L) \Rightarrow \sin (k L)=0 \Rightarrow k L=n \pi, n=1,2,3, \ldots
$$

We discard the $n=0$ solution because $\psi(x)$ for this quantum number would be zero everywhere-an unnormalizable and therefore unphysical solution. Substituting Equation 7.37 into Equation 7.32 gives

$$
-\frac{\hbar^{2}}{2 m} \frac{d^{2}}{d x^{2}}\left(B_{k} \sin (k x)\right)=E\left(B_{k} \sin (k x)\right)
$$

Computing these derivatives leads to

$$
E=E_{k}=\frac{\hbar^{2} k^{2}}{2 m}
$$

According to de Broglie, $p=\hbar k$, so this expression implies that the total energy is equal to the kinetic energy, consistent with our assumption that the "particle moves freely." Combining the results of Equation 7.38 and Equation 7.40 gives

$$
E_{n}=n^{2} \frac{\pi^{2} \hbar^{2}}{2 m L^{2}}, n=1,2,3, \ldots
$$

Strange! A particle bound to a one-dimensional box can only have certain discrete (quantized) values of energy. Further, the particle cannot have a zero kinetic energy-it is impossible for a particle bound to a box to be "at rest."

To evaluate the allowed wave functions that correspond to these energies, we must find the normalization constant $\boldsymbol{B}_{n}$. We impose the normalization condition Equation 7.33 on the wave function

$$
\psi_{n}(x)=B_{n} \sin n \pi x / L
$$

$$
1=\int_{0}^{L} d x\left|\psi_{n}(x)\right|^{2}=\int_{0}^{L} d x B_{n}^{2} \sin ^{2} \frac{n \pi}{L} x=B_{n}^{2} \int_{0}^{L} d x \sin ^{2} \frac{n \pi}{L} x=B_{n}^{2} \frac{L}{2} \Rightarrow B_{n}=\sqrt{\frac{2}{L}}
$$

Hence, the wave functions that correspond to the energy values given in Equation 7.41 are

$$
\psi_{n}(x)=\sqrt{\frac{2}{L}} \sin \frac{n \pi x}{L}, n=1,2,3, \ldots
$$

For the lowest energy state or ground state energy, we have

$$
E_{1}=\frac{\pi^{2} \hbar^{2}}{2 m L^{2}}, \psi_{1}(x)=\sqrt{\frac{2}{L}} \sin \left(\frac{\pi x}{L}\right)
$$

All other energy states can be expressed as

$$
E_{n}=n^{2} E_{1}, \psi_{n}(x)=\sqrt{\frac{2}{L}} \sin \left(\frac{n \pi x}{L}\right)
$$

The index $n$ is called the energy quantum number or principal quantum number. The state for $n=2$ is the first excited state, the state for $n=3$ is the second excited state, and so on. The first three quantum states (for $n=1,2$, and 3) of a particle in a box are shown in Figure 7.11.

The wave functions in Equation 7.45 are sometimes referred to as the "states of definite energy." Particles in these states are said to occupy energy levels, which are represented by the horizontal lines in Figure 7.11. Energy levels are analogous to rungs of a ladder that the particle can "climb" as it gains or loses energy.

The wave functions in Equation 7.45 are also called stationary states and standing wave states. These functions are "stationary," because their probability density functions, $|\Psi(x, t)|^{2}$, do not vary in time, and "standing waves" because their real and imaginary parts oscillate up and down like a standing wave-like a rope waving between two children on a playground. Stationary states are states of definite energy [Equation 7.45], but linear combinations of these states, such as $\psi(x)=a \psi_{1}+b \psi_{2}$ (also solutions to Schrödinger's equation) are states of mixed energy.

Energy quantization is a consequence of the boundary conditions. If the particle is not confined to a box but wanders freely, the allowed energies are continuous. However, in this case, only certain energies $\left(E_{1}, 4 E_{1}, 9 E_{1}, \ldots\right)$ are allowed. The energy difference between adjacent energy levels is given by

$$
\Delta E_{n+1, n}=E_{n+1}-E_{n}=(n+1)^{2} E_{1}-n^{2} E_{1}=(2 n+1) E_{1}
$$

Conservation of energy demands that if the energy of the system changes, the energy difference is carried in some other form of energy. For the special case of a charged particle confined to a small volume (for example, in an atom), energy changes are often carried away by photons. The frequencies of the emitted photons give us information about the energy differences (spacings) of the system and the volume of containment-the size of the "box" [see Equation 7.44].

## EXAMPLE 7.8

## A Simple Model of the Nucleus

Suppose a proton is confined to a box of width $L=1.00 \times 10^{-14} \mathrm{~m}$ (a typical nuclear radius). What are the energies of the ground and the first excited states? If the proton makes a transition from the first excited state to the ground state, what are the energy and the frequency of the emitted photon?

## Strategy

If we assume that the proton confined in the nucleus can be modeled as a quantum particle in a box, all we need to do is to use Equation 7.41 to find its energies $E_{1}$ and $E_{2}$. The mass of a proton is $m=1.76 \times 10^{-27} \mathrm{~kg}$. The emitted photon carries away the energy difference $\Delta E=E_{2}-E_{1}$. We can use the relation $E_{f}=h f$ to find its frequency $f$.

## Solution

The ground state:

$$
E_{1}=\frac{\pi^{2} \hbar^{2}}{2 m L^{2}}=\frac{\pi^{2}\left(1.05 \times 10^{-34} \mathrm{~J} \cdot \mathrm{s}\right)^{2}}{2\left(1.67 \times 10^{-27} \mathrm{~kg}\right)\left(1.00 \times 10^{-14} \mathrm{~m}\right)^{2}}=3.28 \times 10^{-13} \mathrm{~J}=2.05 \mathrm{MeV}
$$

The first excited state: $E_{2}=2^{2} E_{1}=4(2.05 \mathrm{MeV})=8.20 \mathrm{MeV}$.

The energy of the emitted photon is $E_{f}=\Delta E=E_{2}-E_{1}=8.20 \mathrm{MeV}-2.05 \mathrm{MeV}=6.15 \mathrm{MeV}$.

The frequency of the emitted photon is

$$
f=\frac{E_{f}}{h}=\frac{6.15 \mathrm{MeV}}{4.14 \times 10^{-21} \mathrm{MeV} \cdot \mathrm{s}}=1.49 \times 10^{21} \mathrm{~Hz}
$$

## Significance

This is the typical frequency of a gamma ray emitted by a nucleus. The energy of this photon is about 10 million times greater than that of a visible light photon.

The expectation value of the position for a particle in a box is given by

$$
\langle x\rangle=\int_{0}^{L} d x \psi_{n}^{*}(x) x \psi_{n}(x)=\int_{0}^{L} d x x\left|\psi_{n}^{*}(x)\right|^{2}=\int_{0}^{L} d x x \frac{2}{L} \sin ^{2} \frac{n \pi x}{L}=\frac{L}{2}
$$

We can also find the expectation value of the momentum or average momentum of a large number of particles in a given state:

$$
\begin{align*}
\langle p\rangle & =\int_{0}^{L} d x \psi_{n}^{*}(x)\left[-i \hbar \frac{d}{d x} \psi_{n}(x)\right] \\
& =-i \hbar \int_{0}^{L} d x \sqrt{\frac{2}{L}} \sin \frac{n \pi x}{L}\left[\frac{d}{d x} \sqrt{\frac{2}{L}} \sin \frac{n \pi x}{L}\right]=-i \frac{2 \hbar}{L} \int_{0}^{L} d x \sin \frac{n \pi x}{L}\left[\frac{n \pi}{L} \cos \frac{n \pi x}{L}\right] \\
& =-i \frac{2 n \pi \hbar}{L^{2}} \int_{0}^{L} d x \frac{1}{2} \sin \frac{2 n \pi x}{L}=-i \frac{n \pi \hbar}{L^{2}} \frac{L}{2 n \pi} \int_{0}^{2 \pi n} d \varphi \sin \varphi=-i \frac{\hbar}{2 L} \cdot 0=0 .
\end{align*}
$$

Thus, for a particle in a state of definite energy, the average position is in the middle of the box and the average momentum of the particle is zero-as it would also be for a classical particle. Note that while the minimum energy of a classical particle can be zero (the particle can be at rest in the middle of the box), the minimum energy of a quantum particle is nonzero and given by Equation 7.44. The average particle energy in the $n t h$ quantum state-its expectation value of energy-is

$$
E_{n}=\langle E\rangle=n^{2} \frac{\pi^{2} \hbar^{2}}{2 m}
$$

The result is not surprising because the standing wave state is a state of definite energy. Any energy measurement of this system must return a value equal to one of these allowed energies.

Our analysis of the quantum particle in a box would not be complete without discussing Bohr's correspondence principle. This principle states that for large quantum numbers, the laws of quantum physics must give identical results as the laws of classical physics. To illustrate how this principle works for a quantum particle in a box, we plot the probability density distribution

$$
\left|\psi_{n}(x)\right|^{2}=\frac{2}{L} \sin ^{2}(n \pi x / L)
$$

for finding the particle around location $x$ between the walls when the particle is in quantum state $\psi_{n}$. Figure 7.12 shows these probability distributions for the ground state, for the first excited state, and for a highly excited state that corresponds to a large quantum number. We see from these plots that when a quantum particle is in the ground state, it is most likely to be found around the middle of the box, where the probability
distribution has the largest value. This is not so when the particle is in the first excited state because now the probability distribution has the zero value in the middle of the box, so there is no chance of finding the particle there. When a quantum particle is in the first excited state, the probability distribution has two maxima, and the best chance of finding the particle is at positions close to the locations of these maxima. This quantum picture is unlike the classical picture.

The probability density of finding a classical particle between $x$ and $x+\Delta x$ depends on how much time $\Delta t$ the particle spends in this region. Assuming that its speed $u$ is constant, this time is $\Delta t=\Delta x / u$, which is also constant for any location between the walls. Therefore, the probability density of finding the classical particle at $x$ is uniform throughout the box, and there is no preferable location for finding a classical particle. This classical picture is matched in the limit of large quantum numbers. For example, when a quantum particle is in a highly excited state, shown in Figure 7.12, the probability density is characterized by rapid fluctuations and then the probability of finding the quantum particle in the interval $\Delta x$ does not depend on where this interval is located between the walls.

## EXAMPLE 7.9

## A Classical Particle in a Box

A small $0.40-\mathrm{kg}$ cart is moving back and forth along an air track between two bumpers located $2.0 \mathrm{~m}$ apart. We assume no friction; collisions with the bumpers are perfectly elastic so that between the bumpers, the car maintains a constant speed of $0.50 \mathrm{~m} / \mathrm{s}$. Treating the cart as a quantum particle, estimate the value of the principal quantum number that corresponds to its classical energy.

## Strategy

We find the kinetic energy $K$ of the cart and its ground state energy $E_{1}$ as though it were a quantum particle. The energy of the cart is completely kinetic, so $K=n^{2} E_{1}$ (Equation 7.45). Solving for $n$ gives $n=\left(K / E_{1}\right)^{1 / 2}$.

## Solution

The kinetic energy of the cart is

$$
K=\frac{1}{2} m u^{2}=\frac{1}{2}(0.40 \mathrm{~kg})(0.50 \mathrm{~m} / \mathrm{s})^{2}=0.050 \mathrm{~J}
$$

The ground state of the cart, treated as a quantum particle, is

$$
E_{1}=\frac{\pi^{2} \hbar^{2}}{2 m L^{2}}=\frac{\pi^{2}\left(1.05 \times 10^{-34} \mathrm{~J} \cdot \mathrm{s}\right)^{2}}{2(0.40 \mathrm{~kg})(2.0 \mathrm{~m})^{2}}=1.700 \times 10^{-68} \mathrm{~J}
$$

Therefore, $n=\left(K / E_{1}\right)^{1 / 2}=\left(0.050 / 1.700 \times 10^{-68}\right)^{1 / 2}=1.2 \times 10^{33}$.

## Significance

We see from this example that the energy of a classical system is characterized by a very large quantum number. Bohr's correspondence principle concerns this kind of situation. We can apply the formalism of quantum mechanics to any kind of system, quantum or classical, and the results are correct in each case. In the limit of high quantum numbers, there is no advantage in using quantum formalism because we can obtain the same results with the less complicated formalism of classical mechanics. However, we cannot apply classical formalism to a quantum system in a low-number energy state.

Having found the stationary states $\psi_{n}(x)$ and the energies $E_{n}$ by solving the time-independent Schrödinger equation Equation 7.32 , we use Equation 7.28 to write wave functions $\Psi_{n}(x, t)$ that are solutions of the timedependent Schrödinger's equation given by Equation 7.23. For a particle in a box this gives

$$
\Psi_{n}(x, t)=e^{-i \omega_{n} t} \psi_{n}(x)=\sqrt{\frac{2}{L}} e^{-i E_{n} t / \hbar} \sin \frac{n \pi x}{L}, n=1,2,3, \ldots
$$

where the energies are given by Equation 7.41.

The quantum particle in a box model has practical applications in a relatively newly emerged field of optoelectronics, which deals with devices that convert electrical signals into optical signals. This model also deals with nanoscale physical phenomena, such as a nanoparticle trapped in a low electric potential bounded by high-potential barriers.

### 7.5 The Quantum Harmonic Oscillator

Oscillations are found throughout nature, in such things as electromagnetic waves, vibrating molecules, and the gentle back-and-forth sway of a tree branch. In previous chapters, we used Newtonian mechanics to study macroscopic oscillations, such as a block on a spring and a simple pendulum. In this chapter, we begin to study oscillating systems using quantum mechanics. We begin with a review of the classic harmonic oscillator.

## The Classic Harmonic Oscillator

A simple harmonic oscillator is a particle or system that undergoes harmonic motion about an equilibrium position, such as an object with mass vibrating on a spring. In this section, we consider oscillations in onedimension only. Suppose a mass moves back-and-forth along the
$x$-direction about the equilibrium position, $x=0$. In classical mechanics, the particle moves in response to a linear restoring force given by $F_{x}=-k x$, where $x$ is the displacement of the particle from its equilibrium position. The motion takes place between two turning points, $x= \pm A$, where $A$ denotes the amplitude of the motion. The position of the object varies periodically in time with angular frequency $\omega=\sqrt{k / m}$, which depends on the mass $m$ of the oscillator and on the force constant $k$ of the net force, and can be written as

$$
x(t)=A \cos \quad(\omega \quad t+\phi)
$$

The total energy $E$ of an oscillator is the sum of its kinetic energy $K=m u^{2} / 2$ and the elastic potential energy of the force $U(x)=k \quad x^{2} / 2$,

$$
E=\frac{1}{2} m u^{2}+\frac{1}{2} k x^{2}
$$

At turning points $x= \pm A$, the speed of the oscillator is zero; therefore, at these points, the energy of oscillation is solely in the form of potential energy $E=k \quad A^{2} / 2$. The plot of the potential energy $U(x)$ of the oscillator versus its position $x$ is a parabola (Figure 7.13). The potential-energy function is a quadratic function of $x$, measured with respect to the equilibrium position. On the same graph, we also plot the total energy $E$ of the oscillator, as a horizontal line that intercepts the parabola at $x= \pm A$. Then the kinetic energy $K$ is represented as the vertical distance between the line of total energy and the potential energy parabola.

In this plot, the motion of a classical oscillator is confined to the region where its kinetic energy is nonnegative, which is what the energy relation Equation 7.53 says. Physically, it means that a classical oscillator can never be found beyond its turning points, and its energy depends only on how far the turning points are from its equilibrium position. The energy of a classical oscillator changes in a continuous way. The lowest energy that a classical oscillator may have is zero, which corresponds to a situation where an object is at rest at its equilibrium position. The zero-energy state of a classical oscillator simply means no oscillations and no motion at all (a classical particle sitting at the bottom of the potential well in Figure 7.13). When an object oscillates, no matter how big or small its energy may be, it spends the longest time near the turning points, because this is where it slows down and reverses its direction of motion. Therefore, the probability of finding a classical oscillator between the turning points is highest near the turning points and lowest at the equilibrium position. (Note that this is not a statement of preference of the object to go to lower energy. It is a statement about how quickly the object moves through various regions.)

## The Quantum Harmonic Oscillator

One problem with this classical formulation is that it is not general. We cannot use it, for example, to describe vibrations of diatomic molecules, where quantum effects are important. A first step toward a quantum formulation is to use the classical expression $k=m \quad \omega^{2}$ to limit mention of a "spring" constant between the atoms. In this way the potential energy function can be written in a more general form,

$$
U(x)=\frac{1}{2} m \omega^{2} x^{2}
$$

Combining this expression with the time-independent Schrödinger equation gives

$$
-\frac{\hbar}{2 m} \frac{d^{2} \psi(x)}{d x^{2}}+\frac{1}{2} m \omega{ }^{2} x{ }^{2} \psi(x)=E \psi(x)
$$

To solve Equation 7.55 -that is, to find the allowed energies $E$ and their corresponding wave functions $\psi(x)$ -we require the wave functions to be symmetric about $x=0$ (the bottom of the potential well) and to be normalizable. These conditions ensure that the probability density $|\psi(x)|^{2}$ must be finite when integrated over the entire range of $x$ from $-\infty$ to $+\infty$. How to solve Equation 7.55 is the subject of a more advanced course in quantum mechanics; here, we simply cite the results. The allowed energies are

$$
E_{n}=\left(n+\frac{1}{2}\right) \hbar \omega=\frac{2 n+1}{2} \hbar \omega, n=0,1,2,3, \ldots
$$

The wave functions that correspond to these energies (the stationary states or states of definite energy) are

$$
\psi_{n}(x)=N_{n} e^{-\beta{ }_{x}^{2}{ }^{2} / 2} H_{n}(\beta x), n=0,1,2,3, \ldots
$$

where $\beta=\sqrt{m \quad \omega / \hbar}, N_{n}$ is the normalization constant, and $H_{n}(y)$ is a polynomial of degree $n$ called a Hermite polynomial. The first four Hermite polynomials are

$$
\begin{aligned}
& H_{0}(y)=1 \\
& H_{1}(y)=2 y \\
& H_{2}(y)=4 y^{2}-2 \\
& H_{3}(y)=8 y^{3}-12 y .
\end{aligned}
$$

A few sample wave functions are given in Figure 7.14. As the value of the principal number increases, the solutions alternate between even functions and odd functions about $x=0$.

## Classical Region of Harmonic Oscillations

Find the amplitude $A$ of oscillations for a classical oscillator with energy equal to the energy of a quantum oscillator in the quantum state $n$.

## Strategy

To determine the amplitude $A$, we set the classical energy $E=k x^{2} / 2=m \quad \omega^{2} A^{2} / 2$ equal to $E_{n}$ given by Equation 7.56 .

## Solution

We obtain

$$
E_{n}=m \quad \omega^{2} A_{n}^{2} / 2 \Rightarrow A_{n}=\sqrt{\frac{2}{m \omega^{2}} E_{n}}=\sqrt{\frac{2}{m \omega^{2}} \frac{2 n+1}{2} \hbar \omega}=\sqrt{(2 n+1) \frac{\hbar}{m \omega}}
$$

## Significance

As the quantum number $n$ increases, the energy of the oscillator and therefore the amplitude of oscillation increases (for a fixed natural angular frequency. For large $n$, the amplitude is approximately proportional to the square root of the quantum number.

Several interesting features appear in this solution. Unlike a classical oscillator, the measured energies of a quantum oscillator can have only energy values given by Equation 7.56. Moreover, unlike the case for a quantum particle in a box, the allowable energy levels are evenly spaced,

$$
\Delta E=E_{n+1}-E_{n}=\frac{2(n+1)+1}{2} \hbar \omega-\frac{2 n+1}{2} \hbar \omega=\hbar \omega=h \quad f
$$

When a particle bound to such a system makes a transition from a higher-energy state to a lower-energy state, the smallest-energy quantum carried by the emitted photon is necessarily hf. Similarly, when the particle makes a transition from a lower-energy state to a higher-energy state, the smallest-energy quantum that can
be absorbed by the particle is hf. A quantum oscillator can absorb or emit energy only in multiples of this smallest-energy quantum. This is consistent with Planck's hypothesis for the energy exchanges between radiation and the cavity walls in the blackbody radiation problem.

## EXAMPLE 7.11

## Vibrational Energies of the Hydrogen Chloride Molecule

The $\mathrm{HCl}$ diatomic molecule consists of one chlorine atom and one hydrogen atom. Because the chlorine atom is 35 times more massive than the hydrogen atom, the vibrations of the $\mathrm{HCl}$ molecule can be quite well approximated by assuming that the $\mathrm{Cl}$ atom is motionless and the $\mathrm{H}$ atom performs harmonic oscillations due to an elastic molecular force modeled by Hooke's law. The infrared vibrational spectrum measured for hydrogen chloride has the lowest-frequency line centered at $f=8.88 \times 10{ }^{13} \mathrm{~Hz}$. What is the spacing between the vibrational energies of this molecule? What is the force constant $k$ of the atomic bond in the $\mathrm{HCl}$ molecule?

## Strategy

The lowest-frequency line corresponds to the emission of lowest-frequency photons. These photons are emitted when the molecule makes a transition between two adjacent vibrational energy levels. Assuming that energy levels are equally spaced, we use Equation 7.58 to estimate the spacing. The molecule is well approximated by treating the $\mathrm{Cl}$ atom as being infinitely heavy and the $\mathrm{H}$ atom as the mass $m$ that performs the oscillations. Treating this molecular system as a classical oscillator, the force constant is found from the classical relation $k=m \quad \omega^{2}$.

## Solution

The energy spacing is

$$
\Delta E=h \quad f=\left(4.14 \times 10^{-15} \mathrm{eV} \cdot \mathrm{s}\right)\left(8.88 \times 10^{13} \mathrm{~Hz}\right)=0.368 \mathrm{eV}
$$

The force constant is

$$
k=m \quad \omega^{2}=m \quad(2 \pi f)^{2}=\left(1.67 \times 10^{-27} \mathrm{~kg}\right)\left(2 \pi \times 8.88 \times 10^{13} \mathrm{~Hz}\right)^{2}=520 \mathrm{~N} / \mathrm{m}
$$

## Significance

The force between atoms in an $\mathrm{HCl}$ molecule is surprisingly strong. The typical energy released in energy transitions between vibrational levels is in the infrared range. As we will see later, transitions in between vibrational energy levels of a diatomic molecule often accompany transitions between rotational energy levels.

The quantum oscillator differs from the classic oscillator in three ways:

First, the ground state of a quantum oscillator is $E_{0}=\hbar \omega / 2$, not zero. In the classical view, the lowest energy is zero. The nonexistence of a zero-energy state is common for all quantum-mechanical systems because of omnipresent fluctuations that are a consequence of the Heisenberg uncertainty principle. If a quantum particle sat motionless at the bottom of the potential well, its momentum as well as its position would have to be simultaneously exact, which would violate the Heisenberg uncertainty principle. Therefore, the lowestenergy state must be characterized by uncertainties in momentum and in position, so the ground state of a
quantum particle must lie above the bottom of the potential well.

Second, a particle in a quantum harmonic oscillator potential can be found with nonzero probability outside the interval $-A \leq x \leq+A$. In a classic formulation of the problem, the particle would not have any energy to be in this region. The probability of finding a ground-state quantum particle in the classically forbidden region is about $16 \%$.

Third, the probability density distributions $\left|\psi_{n}(x)\right|^{2}$ for a quantum oscillator in the ground low-energy state, $\psi_{0}(x)$, is largest at the middle of the well $(x=0)$. For the particle to be found with greatest probability at the center of the well, we expect that the particle spends the most time there as it oscillates. This is opposite to the behavior of a classical oscillator, in which the particle spends most of its time moving with relative small speeds near the turning points.

Quantum probability density distributions change in character for excited states, becoming more like the classical distribution when the quantum number gets higher. We observe this change already for the first excited state of a quantum oscillator because the distribution $\left|\psi_{1}(x)\right|^{2}$ peaks up around the turning points and vanishes at the equilibrium position, as seen in Figure 7.13. In accordance with Bohr's correspondence principle, in the limit of high quantum numbers, the quantum description of a harmonic oscillator converges to the classical description, which is illustrated in Figure 7.15. The classical probability density distribution corresponding to the quantum energy of the $n=12$ state is a reasonably good approximation of the quantum probability distribution for a quantum oscillator in this excited state. This agreement becomes increasingly better for highly excited states.

### 7.6 The Quantum Tunneling of Particles through Potential Barriers

Quantum tunneling is a phenomenon in which particles penetrate a potential energy barrier with a height greater than the total energy of the particles. The phenomenon is interesting and important because it violates the principles of classical mechanics. Quantum tunneling is important in models of the Sun and has a wide range of applications, such as the scanning tunneling microscope and the tunnel diode.

## Tunneling and Potential Energy

To illustrate quantum tunneling, consider a ball rolling along a surface with a kinetic energy of $100 \mathrm{~J}$. As the ball rolls, it encounters a hill. The potential energy of the ball placed atop the hill is $10 \mathrm{~J}$. Therefore, the ball (with $100 \mathrm{~J}$ of kinetic energy) easily rolls over the hill and continues on. In classical mechanics, the probability that the ball passes over the hill is exactly 1-it makes it over every time. If, however, the height of the hill is increased-a ball placed atop the hill has a potential energy of $200 \mathrm{~J}$-the ball proceeds only part of the way up the hill, stops, and returns in the direction it came. The total energy of the ball is converted entirely into potential energy before it can reach the top of the hill. We do not expect, even after repeated attempts, for the 100-J ball to ever be found beyond the hill. Therefore, the probability that the ball passes over the hill is exactly 0 , and probability it is turned back or "reflected" by the hill is exactly 1 . The ball never makes it over the hill. The existence of the ball beyond the hill is an impossibility or "energetically forbidden."

However, according to quantum mechanics, the ball has a wave function and this function is defined over all space. The wave function may be highly localized, but there is always a chance that as the ball encounters the hill, the ball will suddenly be found beyond it. Indeed, this probability is appreciable if the "wave packet" of the ball is wider than the barrier.

In the language of quantum mechanics, the hill is characterized by a potential barrier. A finite-height square barrier is described by the following potential-energy function:

$$
U(x)=\left\{\begin{align*}
0, & \text { when } x<0 \\
U_{0}, & \text { when } 0 \leq x \leq L \\
0, & \text { when } x>L
\end{align*}\right.
$$

The potential barrier is illustrated in Figure 7.16. When the height $U_{0}$ of the barrier is infinite, the wave packet representing an incident quantum particle is unable to penetrate it, and the quantum particle bounces back from the barrier boundary, just like a classical particle. When the width $L$ of the barrier is infinite and its height is finite, a part of the wave packet representing an incident quantum particle can filter through the barrier boundary and eventually perish after traveling some distance inside the barrier.

When both the width $L$ and the height $U_{0}$ are finite, a part of the quantum wave packet incident on one side of the barrier can penetrate the barrier boundary and continue its motion inside the barrier, where it is gradually attenuated on its way to the other side. A part of the incident quantum wave packet eventually emerges on the other side of the barrier in the form of the transmitted wave packet that tunneled through the barrier. How much of the incident wave can tunnel through a barrier depends on the barrier width $L$ and its height $U_{0}$, and on the energy $E$ of the quantum particle incident on the barrier. This is the physics of tunneling.

Barrier penetration by quantum wave functions was first analyzed theoretically by Friedrich Hund in 1927, shortly after Schrödinger published the equation that bears his name. A year later, George Gamow used the formalism of quantum mechanics to explain the radioactive $\alpha$-decay of atomic nuclei as a quantum-tunneling phenomenon. The invention of the tunnel diode in 1957 made it clear that quantum tunneling is important to the semiconductor industry. In modern nanotechnologies, individual atoms are manipulated using a knowledge of quantum tunneling.

## Tunneling and the Wave Function

Suppose a uniform and time-independent beam of electrons or other quantum particles with energy $E$ traveling along the $x$-axis (in the positive direction to the right) encounters a potential barrier described by Equation 7.59. The question is: What is the probability that an individual particle in the beam will tunnel through the potential barrier? The answer can be found by solving the boundary-value problem for the timeindependent Schrödinger equation for a particle in the beam. The general form of this equation is given by Equation 7.60, which we reproduce here:

$$
-\frac{\hbar^{2}}{2 m} \frac{d^{2} \psi(x)}{d x^{2}}+U(x) \psi(x)=E \psi(x), \text { where }-\infty<x<+\infty
$$

In Equation 7.60, the potential function $U(x)$ is defined by Equation 7.59. We assume that the given energy $E$ of the incoming particle is smaller than the height $U_{0}$ of the potential barrier, $E<U_{0}$, because this is the interesting physical case. Knowing the energy $E$ of the incoming particle, our task is to solve Equation 7.60 for a function $\psi(x)$ that is continuous and has continuous first derivatives for all $x$. In other words, we are looking for a "smooth-looking" solution (because this is how wave functions look) that can be given a probabilistic interpretation so that $|\psi(x)|^{2}=\psi^{*}(x) \psi(x)$ is the probability density.

We divide the real axis into three regions with the boundaries defined by the potential function in Equation 7.59 (illustrated in Figure 7.16) and transcribe Equation 7.60 for each region. Denoting by $\psi_{\mathrm{I}}(x)$ the solution in region I for $x<0$, by $\psi_{\mathrm{II}}(x)$ the solution in region II for $0 \leq x \leq L$, and by $\psi_{\mathrm{III}}(x)$ the solution in region III for $x>L$, the stationary Schrödinger equation has the following forms in these three regions:

$$
\begin{gather*}
-\frac{\hbar^{2}}{2 m} \frac{d^{2} \psi_{\mathrm{I}}(x)}{d x^{2}}=E \psi_{\mathrm{I}}(x), \text { in region I: }-\infty<x<0 \\
-\frac{\hbar^{2}}{2 m} \frac{d^{2} \psi_{\mathrm{II}}(x)}{d x^{2}}+U_{0} \psi_{\mathrm{II}}(x)=E \psi_{\mathrm{II}}(x), \text { in region II: } 0 \leq x \leq L \\
-\frac{\hbar^{2}}{2 m} \frac{d^{2} \psi_{\mathrm{III}}(x)}{d x^{2}}=E \psi_{\mathrm{III}}(x), \text { in region III: } L<x<+\infty
\end{gather*}
$$

The continuity condition at region boundaries requires that:

$$
\psi_{\mathrm{I}}(0)=\psi_{\mathrm{II}}(0) \text {, at the boundary between regions I and II and }
$$

and

$$
\psi_{\mathrm{II}}(L)=\psi_{\mathrm{III}}(L) \text {, at the boundary between regions II and III. }
$$

The "smoothness" condition requires the first derivative of the solution be continuous at region boundaries:

$$
\left.\frac{d \psi_{\mathrm{I}}(x)}{d x}\right|_{x=0}=\left.\frac{d \psi_{\mathrm{II}}(x)}{d x}\right|_{x=0}, \text { at the boundary between regions I and II; }
$$

and

$$
\left.\frac{d \psi_{\mathrm{II}}(x)}{d x}\right|_{x=L}=\left.\frac{d \psi_{\mathrm{III}}(x)}{d x}\right|_{x=L}, \text { at the boundary between regions II and III. }
$$

In what follows, we find the functions $\psi_{\mathrm{I}}(x), \psi_{\mathrm{II}}(x)$, and $\psi_{\mathrm{III}}(x)$.

We can easily verify (by substituting into the original equation and differentiating) that in regions I and III, the solutions must be in the following general forms:

$$
\begin{gather*}
\psi_{\mathrm{I}}(x)=A e^{+i k x}+B e^{-i k x} \\
\psi_{\mathrm{III}}(x)=F e^{+i k x}+G e^{-i k x}
\end{gather*}
$$

where $k=\sqrt{2 m E} / \hbar$ is a wave number and the complex exponent denotes oscillations,

$$
e^{ \pm i k x}=\cos k x \pm i \sin k x
$$

The constants $A, B, F$, and $G$ in Equation 7.68 and Equation 7.69 may be complex. These solutions are illustrated in Figure 7.16. In region I, there are two waves-one is incident (moving to the right) and one is reflected (moving to the left)-so none of the constants $A$ and $B$ in Equation 7.68 may vanish. In region III, there is only one wave (moving to the right), which is the transmitted wave, so the constant $G$ must be zero in Equation $7.69, G=0$. We can write explicitly that the incident wave is $\psi_{\text {in }}(x)=A e^{+i k x}$ and that the reflected wave is $\psi_{\mathrm{ref}}(x)=B e^{-i k x}$, and that the transmitted wave is $\psi_{\operatorname{tra}}(x)=F e^{+i k x}$. The amplitude of the incident wave is

$$
\left|\psi_{\text {in }}(x)\right|^{2}=\psi_{\text {in }}^{*}(x) \psi_{\text {in }}(x)=\left(A e^{+i k x}\right)^{*} A e^{+i k x}=A^{*} e^{-i k x} A e^{+i k x}=A^{*} A=|A|^{2}
$$

Similarly, the amplitude of the reflected wave is $\left|\psi_{\mathrm{ref}}(x)\right|^{2}=|B|^{2}$ and the amplitude of the transmitted wave is $\left|\psi_{\text {tra }}(x)\right|^{2}=|F|^{2}$. We know from the theory of waves that the square of the wave amplitude is directly proportional to the wave intensity. If we want to know how much of the incident wave tunnels through the barrier, we need to compute the square of the amplitude of the transmitted wave. The transmission probability or tunneling probability is the ratio of the transmitted intensity $\left(|F|^{2}\right)$ to the incident intensity
$\left(|A|^{2}\right)$, written as

$$
T(L, E)=\frac{\left|\psi_{\text {tra }}(x)\right|^{2}}{\left|\psi_{\text {in }}(x)\right|^{2}}=\frac{|F|^{2}}{|A|^{2}}=\left|\frac{F}{A}\right|^{2}
$$

where $L$ is the width of the barrier and $E$ is the total energy of the particle. This is the probability an individual particle in the incident beam will tunnel through the potential barrier. Intuitively, we understand that this probability must depend on the barrier height $U_{0}$.

In region II, the terms in equation Equation 7.62 can be rearranged to

$$
\frac{d^{2} \psi_{\mathrm{II}}(x)}{d x^{2}}=\beta^{2} \psi_{\mathrm{II}}(x)
$$

where $\beta^{2}$ is positive because $U_{0}>E$ and the parameter $\beta$ is a real number,

$$
\beta^{2}=\frac{2 m}{\hbar^{2}}\left(U_{0}-E\right)
$$

The general solution to Equation 7.72 is not oscillatory (unlike in the other regions) and is in the form of exponentials that describe a gradual attenuation of $\psi_{\mathrm{II}}(x)$,

$$
\psi_{\mathrm{II}}(x)=C e^{-\beta x}+D e^{+\beta x}
$$

The two types of solutions in the three regions are illustrated in Figure 7.17.

Now we use the boundary conditions to find equations for the unknown constants. Equation 7.68 and Equation 7.74 are substituted into Equation 7.64 to give

$$
A+B=C+D
$$

Equation 7.74 and Equation 7.69 are substituted into Equation 7.65 to give

$$
C e^{-\beta L}+D e^{+\beta L}=F e^{+i k L}
$$

Similarly, we substitute Equation 7.68 and Equation 7.74 into Equation 7.66, differentiate, and obtain

$$
-i k(A-B)=\beta(D-C)
$$

Similarly, the boundary condition Equation 7.67 reads explicitly

$$
\beta\left(D e^{+\beta L}-C e^{-\beta L}\right)=-i k F e^{+i k L}
$$

We now have four equations for five unknown constants. However, because the quantity we are after is the transmission coefficient, defined in Equation 7.71 by the fraction $F / A$, the number of equations is exactly right because when we divide each of the above equations by $A$, we end up having only four unknown fractions: $B / A$, $C / A, D / A$, and $F / A$, three of which can be eliminated to find $F / A$. The actual algebra that leads to expression for $F / A$ is pretty lengthy, but it can be done either by hand or with a help of computer software. The end result is

$$
\frac{F}{A}=\frac{e^{-i k L}}{\cosh (\beta L)+i(\gamma / 2) \sinh (\beta L)}
$$

In deriving Equation 7.79, to avoid the clutter, we use the substitutions $\gamma \equiv \beta / k-k / \beta$,

$$
\cosh y=\frac{e^{y}+e^{-y}}{2}, \text { and } \sinh y=\frac{e^{y}-e^{-y}}{2}
$$

We substitute Equation 7.79 into Equation 7.71 and obtain the exact expression for the transmission coefficient for the barrier,

$$
T(L, E)=\left(\frac{F}{A}\right)^{*} \frac{F}{A}=\frac{e^{+i k L}}{\cosh (\beta L)-i(\gamma / 2) \sinh (\beta L)} \cdot \frac{e^{-i k L}}{\cosh (\beta L)+i(\gamma / 2) \sinh (\beta L)}
$$

or

$$
T(L, E)=\frac{1}{\cosh ^{2}(\beta L)+(\gamma / 2)^{2} \sinh ^{2}(\beta L)}
$$

where

$$
\left(\frac{\gamma}{2}\right)^{2}=\frac{1}{4}\left(\frac{1-E / U_{0}}{E / U_{0}}+\frac{E / U_{0}}{1-E / U_{0}}-2\right)
$$

For a wide and high barrier that transmits poorly, Equation 7.80 can be approximated by

$$
T(L, E)=16 \frac{E}{U_{0}}\left(1-\frac{E}{U_{0}}\right) e^{-2 \beta L}
$$

Whether it is the exact expression Equation 7.80 or the approximate expression Equation 7.81 , we see that the tunneling effect very strongly depends on the width $L$ of the potential barrier. In the laboratory, we can adjust both the potential height $U_{0}$ and the width $L$ to design nano-devices with desirable transmission coefficients.

## EXAMPLE 7.12

## Transmission Coefficient

Two copper nanowires are insulated by a copper oxide nano-layer that provides a $10.0-\mathrm{eV}$ potential barrier. Estimate the tunneling probability between the nanowires by $7.00-\mathrm{eV}$ electrons through a $5.00-\mathrm{nm}$ thick oxide layer. What if the thickness of the layer were reduced to just $1.00 \mathrm{~nm}$ ? What if the energy of electrons were increased to $9.00 \mathrm{eV}$ ?

## Strategy

Treating the insulating oxide layer as a finite-height potential barrier, we use Equation 7.81. We identify $U_{0}=10.0 \mathrm{eV}, E_{1}=7.00 \mathrm{eV}, E_{2}=9.00 \mathrm{eV}, L_{1}=5.00 \mathrm{~nm}$, and $L_{2}=1.00 \mathrm{~nm}$. We use Equation 7.73 to compute the exponent. Also, we need the rest mass of the electron $m=511 \mathrm{keV} / c^{2}$ and Planck's constant $\hbar=0.1973 \mathrm{keV} \cdot \mathrm{nm} / c$. It is typical for this type of estimate to deal with very small quantities that are often not
suitable for handheld calculators. To make correct estimates of orders, we make the conversion $e^{y}=10^{y / \ln 10}$.

## Solution

Constants:

$$
\begin{gathered}
\frac{2 m}{\hbar^{2}}=\frac{2\left(511 \mathrm{keV} / c^{2}\right)}{(0.1973 \mathrm{keV} \cdot \mathrm{nm} / c)^{2}}=26,254 \frac{1}{\mathrm{keV} \cdot(\mathrm{nm})^{2}} \\
\beta=\sqrt{\frac{2 m}{\hbar^{2}}\left(U_{0}-E\right)}=\sqrt{26,254 \frac{(10.0 \mathrm{eV}-E)}{\mathrm{keV} \cdot(\mathrm{nm})^{2}}}=\sqrt{26.254(10.0 \mathrm{eV}-E) / \mathrm{eV}} \frac{1}{\mathrm{~nm}}
\end{gathered}
$$

For a lower-energy electron with $E_{1}=7.00 \mathrm{eV}$ :

$$
\begin{gathered}
\beta_{1}=\sqrt{26.254\left(10.00 \mathrm{eV}-E_{1}\right) / \mathrm{eV}} \frac{1}{\mathrm{~nm}}=\sqrt{26.254(10.00-7.00)} \frac{1}{\mathrm{~nm}}=\frac{8.875}{\mathrm{~nm}} \\
T\left(L, E_{1}\right)=16 \frac{E_{1}}{U_{0}}\left(1-\frac{E_{1}}{U_{0}}\right) e^{-2 \beta_{1} L}=16 \frac{7}{10}\left(1-\frac{7}{10}\right) e^{-17.75 L / \mathrm{nm}}=3.36 e^{-17.75 L / \mathrm{nm}}
\end{gathered}
$$

For a higher-energy electron with $E_{2}=9.00 \mathrm{eV}$ :

$$
\begin{aligned}
\beta_{2} & =\sqrt{26.254\left(10.00 \mathrm{eV}-E_{2}\right) / \mathrm{eV}} \frac{1}{\mathrm{~nm}}=\sqrt{26.254(10.00-9.00)} \frac{1}{\mathrm{~nm}}=\frac{5.124}{\mathrm{~nm}} \\
T\left(L, E_{2}\right) & =16 \frac{E_{2}}{U_{0}}\left(1-\frac{E_{2}}{U_{0}}\right) e^{-2 \beta_{2} L}=16 \frac{9}{10}\left(1-\frac{9}{10}\right) e^{-10.25 L / \mathrm{nm}}=1.44 e^{-10.25 L / \mathrm{nm}}
\end{aligned}
$$

For a broad barrier with $L_{1}=5.00 \mathrm{~nm}$ :

$$
T\left(L_{1}, E_{1}\right)=3.36 e^{-17.75 L_{1} / \mathrm{nm}}=3.36 e^{-17.75 \cdot 5.00 \mathrm{~nm} / \mathrm{nm}}=3.36 e^{-88}=3.36\left(6.2 \times 10^{-39}\right)=2.1 \% \times 10^{-36}
$$

$T\left(L_{1}, E_{2}\right)=1.44 e^{-10.25 L_{1} / \mathrm{nm}}=1.44 e^{-10.25 \cdot 5.00 \mathrm{~nm} / \mathrm{nm}}=1.44 e^{-51.2}=1.44\left(5.81 \times 10^{-12}\right)=8.36 \% \times 10^{-25}$.

For a narrower barrier with $L_{2}=1.00 \mathrm{~nm}$ :

$$
\begin{gathered}
T\left(L_{2}, E_{1}\right)=3.36 e^{-17.75 L_{2} / \mathrm{nm}}=3.36 e^{-17.75 \cdot 1.00 \mathrm{~nm} / \mathrm{nm}}=3.36 e^{-17.75}=3.36\left(5.1 \times 10^{-7}\right)=1.7 \% \times 10^{-4} \\
T\left(L_{2}, E_{2}\right)=1.44 e^{-10.25 L_{2} / \mathrm{nm}}=1.44 e^{-10.25 \cdot 1.00 \mathrm{~nm} / \mathrm{nm}}=1.44 e^{-10.25}=1.44\left(3.53 \times 10^{-5}\right)=5.09 \% \times 10^{-7}
\end{gathered}
$$

## Significance

We see from these estimates that the probability of tunneling is affected more by the width of the potential barrier than by the energy of an incident particle. In today's technologies, we can manipulate individual atoms on metal surfaces to create potential barriers that are fractions of a nanometer, giving rise to measurable tunneling currents. One of many applications of this technology is the scanning tunneling microscope (STM), which we discuss later in this section.

## Radioactive Decay

In 1928, Gamow identified quantum tunneling as the mechanism responsible for the radioactive decay of atomic nuclei. He observed that some isotopes of thorium, uranium, and bismuth disintegrate by emitting $\alpha$-particles (which are doubly ionized helium atoms or, simply speaking, helium nuclei). In the process of emitting an $\alpha$-particle, the original nucleus is transformed into a new nucleus that has two fewer neutrons and two fewer protons than the original nucleus. The $\alpha$-particles emitted by one isotope have approximately the
same kinetic energies. When we look at variations of these energies among isotopes of various elements, the lowest kinetic energy is about $4 \mathrm{MeV}$ and the highest is about $9 \mathrm{MeV}$, so these energies are of the same order of magnitude. This is about where the similarities between various isotopes end.

When we inspect half-lives (a half-life is the time in which a radioactive sample loses half of its nuclei due to decay), different isotopes differ widely. For example, the half-life of polonium-214 is $160 \mu \mathrm{s}$ and the half-life of uranium is 4.5 billion years. Gamow explained this variation by considering a 'spherical-box' model of the nucleus, where $\alpha$-particles can bounce back and forth between the walls as free particles. The confinement is provided by a strong nuclear potential at a spherical wall of the box. The thickness of this wall, however, is not infinite but finite, so in principle, a nuclear particle has a chance to escape this nuclear confinement. On the inside wall of the confining barrier is a high nuclear potential that keeps the $\alpha$-particle in a small confinement. But when an $\alpha$-particle gets out to the other side of this wall, it is subject to electrostatic Coulomb repulsion and moves away from the nucleus. This idea is illustrated in Figure 7.18. The width $L$ of the potential barrier that separates an $\alpha$-particle from the outside world depends on the particle's kinetic energy $E$. This width is the distance between the point marked by the nuclear radius $R$ and the point $R_{0}$ where an $\alpha$-particle emerges on the other side of the barrier, $L=R_{0}-R$. At the distance $R_{0}$, its kinetic energy must at least match the electrostatic energy of repulsion, $E=\left(4 \pi \varepsilon_{0}\right)^{-1} Z e^{2} / R_{0}$ (where $+Z e$ is the charge of the nucleus). In this way we can estimate the width of the nuclear barrier,

$$
L=\frac{e^{2}}{4 \pi \varepsilon_{0}} \frac{Z}{E}-R
$$

We see from this estimate that the higher the energy of $\alpha$-particle, the narrower the width of the barrier that it is to tunnel through. We also know that the width of the potential barrier is the most important parameter in tunneling probability. Thus, highly energetic $\alpha$-particles have a good chance to escape the nucleus, and, for such nuclei, the nuclear disintegration half-life is short. Notice that this process is highly nonlinear, meaning a small increase in the $\alpha$-particle energy has a disproportionately large enhancing effect on the tunneling probability and, consequently, on shortening the half-life. This explains why the half-life of polonium that emits 8-MeV $\alpha$-particles is only hundreds of milliseconds and the half-life of uranium that emits 4-MeV $\alpha$-particles is billions of years.

## Field Emission

Field emission is a process of emitting electrons from conducting surfaces due to a strong external electric field that is applied in the direction normal to the surface (Figure 7.19). As we know from our study of electric fields in earlier chapters, an applied external electric field causes the electrons in a conductor to move to its surface and stay there as long as the present external field is not excessively strong. In this situation, we have a constant electric potential throughout the inside of the conductor, including its surface. In the language of potential energy, we say that an electron inside the conductor has a constant potential energy $U(x)=-U_{0}$ (here, the $x$ means inside the conductor). In the situation represented in Figure 7.19, where the external electric field is uniform and has magnitude $E_{g}$, if an electron happens to be outside the conductor at a distance $x$ away from its surface, its potential energy would have to be $U(x)=-e E_{g} x$ (here, $x$ denotes distance to the surface). Taking the origin at the surface, so that $x=0$ is the location of the surface, we can represent the potential energy of conduction electrons in a metal as the potential energy barrier shown in Figure 7.20. In the absence of the external field, the potential energy becomes a step barrier defined by $U(x \leq 0)=-U_{0}$ and by $U(x>0)=0$.

When an external electric field is strong, conduction electrons at the surface may get detached from it and accelerate along electric field lines in a direction antiparallel to the external field, away from the surface. In short, conduction electrons may escape from the surface. The field emission can be understood as the quantum tunneling of conduction electrons through the potential barrier at the conductor's surface. The physical principle at work here is very similar to the mechanism of $\alpha$-emission from a radioactive nucleus.

Suppose a conduction electron has a kinetic energy $E$ (the average kinetic energy of an electron in a metal is the work function $\phi$ for the metal and can be measured, as discussed for the photoelectric effect in Photons and Matter Waves), and an external electric field can be locally approximated by a uniform electric field of
strength $E_{g}$. The width $L$ of the potential barrier that the electron must cross is the distance from the conductor's surface to the point outside the surface where its kinetic energy matches the value of its potential energy in the external field. In Figure 7.20, this distance is measured along the dashed horizontal line $U(x)=E$ from $x=0$ to the intercept with $U(x)=-e E_{g} x$, so the barrier width is

$$
L=\frac{e^{-1} E}{E_{g}}=\frac{e^{-1} \phi}{E_{g}}
$$

We see that $L$ is inversely proportional to the strength $E_{g}$ of an external field. When we increase the strength of the external field, the potential barrier outside the conductor becomes steeper and its width decreases for an electron with a given kinetic energy. In turn, the probability that an electron will tunnel across the barrier (conductor surface) becomes exponentially larger. The electrons that emerge on the other side of this barrier form a current (tunneling-electron current) that can be detected above the surface. The tunneling-electron current is proportional to the tunneling probability. The tunneling probability depends nonlinearly on the barrier width $L$, and $L$ can be changed by adjusting $E_{g}$. Therefore, the tunneling-electron current can be tuned by adjusting the strength of an external electric field at the surface. When the strength of an external electric field is constant, the tunneling-electron current has different values at different elevations $L$ above the surface.

The quantum tunneling phenomenon at metallic surfaces, which we have just described, is the physical principle behind the operation of the scanning tunneling microscope (STM), invented in 1981 by Gerd Binnig and Heinrich Rohrer. The STM device consists of a scanning tip (a needle, usually made of tungsten, platinumiridium, or gold); a piezoelectric device that controls the tip's elevation in a typical range of 0.4 to $0.7 \mathrm{~nm}$ above the surface to be scanned; some device that controls the motion of the tip along the surface; and a computer to display images. While the sample is kept at a suitable voltage bias, the scanning tip moves along the surface (Figure 7.21), and the tunneling-electron current between the tip and the surface is registered at each position. The amount of the current depends on the probability of electron tunneling from the surface to the tip, which, in turn, depends on the elevation of the tip above the surface. Hence, at each tip position, the distance from the tip to the surface is measured by measuring how many electrons tunnel out from the surface to the tip. This method can give an unprecedented resolution of about $0.001 \mathrm{~nm}$, which is about $1 \%$ of the average diameter of an atom. In this way, we can see individual atoms on the surface, as in the image of a carbon nanotube in Figure 7.22.

## Resonant Quantum Tunneling

Quantum tunneling has numerous applications in semiconductor devices such as electronic circuit components or integrated circuits that are designed at nanoscales; hence, the term 'nanotechnology.' For example, a diode (an electric-circuit element that causes an electron current in one direction to be different from the current in the opposite direction, when the polarity of the bias voltage is reversed) can be realized by a tunneling junction between two different types of semiconducting materials. In such a tunnel diode, electrons tunnel through a single potential barrier at a contact between two different semiconductors. At the junction, tunneling-electron current changes nonlinearly with the applied potential difference across the junction and may rapidly decrease as the bias voltage is increased. This is unlike the Ohm's law behavior that we are familiar with in household circuits. This kind of rapid behavior (caused by quantum tunneling) is desirable in high-speed electronic devices.

Another kind of electronic nano-device utilizes resonant tunneling of electrons through potential barriers that occur in quantum dots. A quantum dot is a small region of a semiconductor nanocrystal that is grown, for example, in a silicon or aluminum arsenide crystal. Figure 7.23(a) shows a quantum dot of gallium arsenide embedded in an aluminum arsenide wafer. The quantum-dot region acts as a potential well of a finite height (shown in Figure 7.23(b)) that has two finite-height potential barriers at dot boundaries. Similarly, as for a quantum particle in a box (that is, an infinite potential well), lower-lying energies of a quantum particle trapped in a finite-height potential well are quantized. The difference between the box and the well potentials is that a quantum particle in a box has an infinite number of quantized energies and is trapped in the box indefinitely, whereas a quantum particle trapped in a potential well has a finite number of quantized energy levels and can tunnel through potential barriers at well boundaries to the outside of the well. Thus, a quantum dot of gallium arsenide sitting in aluminum arsenide is a potential well where low-lying energies of an electron are quantized, indicated as $E_{\text {dot }}$ in part (b) in the figure. When the energy $E_{\text {electron }}$ of an electron in the outside region of the dot does not match its energy $\boldsymbol{E}_{\text {dot }}$ that it would have in the dot, the electron does not tunnel through the region of the dot and there is no current through such a circuit element, even if it were kept at an electric voltage difference (bias). However, when this voltage bias is changed in such a way that one of the barriers is lowered, so that $E_{\text {dot }}$ and $E_{\text {electron }}$ become aligned, as seen in part (c) of the figure, an electron current flows through the dot. When the voltage bias is now increased, this alignment is lost and the current stops flowing. When the voltage bias is increased further, the electron tunneling becomes improbable until the bias voltage reaches a value for which the outside electron energy matches the next electron energy level in the dot. The word 'resonance' in the device name means that the tunneling-electron current occurs only when a selected energy level is matched by tuning an applied voltage bias, such as in the operation mechanism of the resonant-tunneling diode just described. Resonant-tunneling diodes are used as super-fast nano-switches.

