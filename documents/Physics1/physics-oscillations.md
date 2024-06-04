# CHAPTER 15 Oscillations 

INTRODUCTION We begin the study of oscillations with simple systems of pendulums and springs. Although these systems may seem quite basic, the concepts involved have many real-life applications. For example, the Comcast Building in Philadelphia, Pennsylvania, stands approximately 305 meters ( 1000 feet) tall. As
buildings are built taller, they can act as inverted, physical pendulums, with the top floors oscillating due to seismic activity and fluctuating winds. In the Comcast Building, a tuned-mass damper is used to reduce the oscillations. Installed at the top of the building is a tuned, liquid-column mass damper, consisting of a 300,000-gallon reservoir of water. This U-shaped tank allows the water to oscillate freely at a frequency that matches the natural frequency of the building. Damping is provided by tuning the turbulence levels in the moving water using baffles.

### 15.1 Simple Harmonic Motion

When you pluck a guitar string, the resulting sound has a steady tone and lasts a long time (Figure 15.2). The string vibrates around an equilibrium position, and one oscillation is completed when the string starts from the initial position, travels to one of the extreme positions, then to the other extreme position, and returns to its initial position. We define periodic motion to be any motion that repeats itself at regular time intervals, such as exhibited by the guitar string or by a child swinging on a swing. In this section, we study the basic characteristics of oscillations and their mathematical description.

## Period and Frequency in Oscillations

In the absence of friction, the time to complete one oscillation remains constant and is called the period (T). Its units are usually seconds, but may be any convenient unit of time. The word 'period' refers to the time for some event whether repetitive or not, but in this chapter, we shall deal primarily in periodic motion, which is by definition repetitive.

A concept closely related to period is the frequency of an event. Frequency ( $f$ ) is defined to be the number of events per unit time. For periodic motion, frequency is the number of oscillations per unit time. The relationship between frequency and period is

$$
f=\frac{1}{T}
$$

The SI unit for frequency is the hertz $(\mathrm{Hz})$ and is defined as one cycle per second:

$$
1 \mathrm{~Hz}=1 \frac{\text { cycle }}{\mathrm{s}} \text { or } 1 \mathrm{~Hz}=\frac{1}{\mathrm{~s}}=1 \mathrm{~s}^{-1}
$$

A cycle is one complete oscillation.

## EXAMPLE 15.1

## Determining the Frequency of Medical Ultrasound

Ultrasound machines are used by medical professionals to make images for examining internal organs of the body. An ultrasound machine emits high-frequency sound waves, which reflect off the organs, and a computer receives the waves, using them to create a picture. We can use the formulas presented in this module to determine the frequency, based on what we know about oscillations. Consider a medical imaging device that produces ultrasound by oscillating with a period of $0.400 \mu \mathrm{s}$. What is the frequency of this oscillation?

## Strategy

The period $(T)$ is given and we are asked to find frequency ( $f$ ).

## Solution

Substitute $0.400 \mu \mathrm{s}$ for $T$ in $f=\frac{1}{T}$ :

$$
f=\frac{1}{T}=\frac{1}{0.400 \times 10^{-6} \mathrm{~s}}
$$

Solve to find

$$
f=2.50 \times 10^{6} \mathrm{~Hz}
$$

## Significance

This frequency of sound is much higher than the highest frequency that humans can hear (the range of human hearing is $20 \mathrm{~Hz}$ to $20,000 \mathrm{~Hz}$ ); therefore, it is called ultrasound. Appropriate oscillations at this frequency generate ultrasound used for noninvasive medical diagnoses, such as observations of a fetus in the womb.

## Characteristics of Simple Harmonic Motion

A very common type of periodic motion is called simple harmonic motion (SHM). A system that oscillates with $\mathrm{SHM}$ is called a simple harmonic oscillator.

## Simple Harmonic Motion

In simple harmonic motion, the acceleration of the system, and therefore the net force, is proportional to the displacement and acts in the opposite direction of the displacement.

A good example of SHM is an object with mass $m$ attached to a spring on a frictionless surface, as shown in Figure 15.3. The object oscillates around the equilibrium position, and the net force on the object is equal to the force provided by the spring. This force obeys Hooke's law $F_{S}=-k x$, as discussed in a previous chapter.

If the net force can be described by Hooke's law and there is no damping (slowing down due to friction or other nonconservative forces), then a simple harmonic oscillator oscillates with equal displacement on either side of the equilibrium position, as shown for an object on a spring in Figure 15.3. The maximum displacement from equilibrium is called the amplitude (A). The units for amplitude and displacement are the same but depend on the type of oscillation. For the object on the spring, the units of amplitude and displacement are meters.

What is so significant about SHM? For one thing, the period $T$ and frequency $f$ of a simple harmonic oscillator are independent of amplitude. The string of a guitar, for example, oscillates with the same frequency whether plucked gently or hard.

Two important factors do affect the period of a simple harmonic oscillator. The period is related to how stiff the system is. A very stiff object has a large force constant (k), which causes the system to have a smaller period. For example, you can adjust a diving board's stiffness-the stiffer it is, the faster it vibrates, and the shorter its period. Period also depends on the mass of the oscillating system. The more massive the system is, the longer the period. For example, a heavy person on a diving board bounces up and down more slowly than a light one. In fact, the mass $m$ and the force constant $k$ are the only factors that affect the period and frequency of SHM. To derive an equation for the period and the frequency, we must first define and analyze the equations of motion. Note that the force constant is sometimes referred to as the spring constant.

## Equations of SHM

Consider a block attached to a spring on a frictionless table (Figure 15.4). The equilibrium position (the position where the spring is neither stretched nor compressed) is marked as $x=0$. At the equilibrium position, the net force is zero.

Work is done on the block to pull it out to a position of $x=+A$, and it is then released from rest. The maximum $x$-position $(A)$ is called the amplitude of the motion. The block begins to oscillate in SHM between $x=+A$ and $x=-A$, where $A$ is the amplitude of the motion and $T$ is the period of the oscillation. The period is the time for one oscillation. Figure 15.5 shows the motion of the block as it completes one and a half oscillations after release. Figure 15.6 shows a plot of the position of the block versus time. When the position is plotted versus time, it is clear that the data can be modeled by a cosine function with an amplitude $A$ and a period $T$. The cosine function $\cos \theta$ repeats every multiple of $2 \pi$, whereas the motion of the block repeats every period $T$. However, the function $\cos \left(\frac{2 \pi}{T} t\right)$ repeats every integer multiple of the period. The maximum of the cosine function is one, so it is necessary to multiply the cosine function by the amplitude $A$.

$$
x(t)=A \cos \left(\frac{2 \pi}{T} t\right)=A \cos (\omega t)
$$

Recall from the chapter on rotation that the angular frequency equals $\omega=\frac{d \theta}{d t}$. In this case, the period is constant, so the angular frequency is defined as $2 \pi$ divided by the period, $\omega=\frac{2 \pi}{T}$.

The equation for the position as a function of time $x(t)=A \cos (\omega t)$ is good for modeling data, where the position of the block at the initial time $t=0.00 \mathrm{~s}$ is at the amplitude $A$ and the initial velocity is zero. Often when taking experimental data, the position of the mass at the initial time $t=0.00 \mathrm{~s}$ is not equal to the amplitude and the initial velocity is not zero. Consider 10 seconds of data collected by a student in lab, shown in Figure 15.7.

The data in Figure 15.7 can still be modeled with a periodic function, like a cosine function, but the function is shifted to the right. This shift is known as a phase shift and is usually represented by the Greek letter phi $(\phi)$. The equation of the position as a function of time for a block on a spring becomes

$$
x(t)=A \cos (\omega t+\phi)
$$

This is the generalized equation for SHM where $t$ is the time measured in seconds, $\omega$ is the angular frequency with units of inverse seconds, $A$ is the amplitude measured in meters or centimeters, and $\phi$ is the phase shift measured in radians (Figure 15.8). It should be noted that because sine and cosine functions differ only by a phase shift, this motion could be modeled using either the cosine or sine function.

The velocity of the mass on a spring, oscillating in SHM, can be found by taking the derivative of the position equation:

$$
v(t)=\frac{d x}{d t}=\frac{d}{d t}(A \cos (\omega t+\phi))=-A \omega \sin (\omega t+\omega)=-v_{\max } \sin (\omega t+\phi)
$$

Because the sine function oscillates between -1 and +1 , the maximum velocity is the amplitude times the angular frequency, $v_{\max }=A \omega$. The maximum velocity occurs at the equilibrium position $(x=0)$ when the mass is moving toward $x=+A$. The maximum velocity in the negative direction is attained at the equilibrium position $(x=0)$ when the mass is moving toward $x=-A$ and is equal to $-v_{\max }$.

The acceleration of the mass on the spring can be found by taking the time derivative of the velocity:

$$
a(t)=\frac{d v}{d t}=\frac{d}{d t}(-A \omega \sin (\omega t+\phi))=-A \omega^{2} \cos (\omega t+\varphi)=-a_{\max } \cos (\omega t+\phi)
$$

The maximum acceleration is $a_{\max }=A \omega^{2}$. The maximum acceleration occurs at the position $(x=-A)$, and the acceleration at the position $(x=-A)$ and is equal to $-a_{\max }$.

## Summary of Equations of Motion for SHM

In summary, the oscillatory motion of a block on a spring can be modeled with the following equations of motion:

$$
\begin{array}{cc}
x(t)=A \cos (\omega t+\phi) & 15.3 \\
v(t)=-v_{\max } \sin (\omega t+\phi) & 15.4 \\
a(t)=-a_{\max } \cos (\omega t+\phi) & 15.5 \\
x_{\max }=A & 15.6 \\
v_{\max }=A \omega & 15.7 \\
a_{\max }=A \omega^{2} & 15.8
\end{array}
$$

Here, $A$ is the amplitude of the motion, $T$ is the period, $\phi$ is the phase shift, and $\omega=\frac{2 \pi}{T}=2 \pi f$ is the angular frequency of the motion of the block.

## EXAMPLE 15.2

## Determining the Equations of Motion for a Block and a Spring

A $2.00-\mathrm{kg}$ block is placed on a frictionless surface. A spring with a force constant of $k=32.00 \mathrm{~N} / \mathrm{m}$ is attached to the block, and the opposite end of the spring is attached to the wall. The spring can be compressed or extended. The equilibrium position is marked as $x=0.00 \mathrm{~m}$.

Work is done on the block, pulling it out to $x=+0.02 \mathrm{~m}$. The block is released from rest and oscillates between $x=+0.02 \mathrm{~m}$ and $x=-0.02 \mathrm{~m}$. The period of the motion is $1.57 \mathrm{~s}$. Determine the equations of motion.

## Strategy

We first find the angular frequency. The phase shift is zero, $\phi=0.00$ rad, because the block is released from rest at $x=A=+0.02 \mathrm{~m}$. Once the angular frequency is found, we can determine the maximum velocity and maximum acceleration.

## Solution

The angular frequency can be found and used to find the maximum velocity and maximum acceleration:

$$
\begin{aligned}
\omega & =\frac{2 \pi}{1.57 \mathrm{~s}}=4.00 \mathrm{~s}^{-1} \\
v_{\max } & =A \omega=0.02 \mathrm{~m}\left(4.00 \mathrm{~s}^{-1}\right)=0.08 \mathrm{~m} / \mathrm{s} \\
a_{\max } & =A \omega^{2}=0.02 \mathrm{~m}\left(4.00 \mathrm{~s}^{-1}\right)^{2}=0.32 \mathrm{~m} / \mathrm{s}^{2}
\end{aligned}
$$

All that is left is to fill in the equations of motion:

$$
\begin{aligned}
& x(t)=A \cos (\omega t+\phi)=(0.02 \mathrm{~m}) \cos \left(4.00 \mathrm{~s}^{-1} t\right) \\
& v(t)=-v_{\max } \sin (\omega t+\phi)=(-0.08 \mathrm{~m} / \mathrm{s}) \sin \left(4.00 \mathrm{~s}^{-1} t\right) \\
& a(t)=-a_{\max } \cos (\omega t+\phi)=\left(-0.32 \mathrm{~m} / \mathrm{s}^{2}\right) \cos \left(4.00 \mathrm{~s}^{-1} t\right)
\end{aligned}
$$

## Significance

The position, velocity, and acceleration can be found for any time. It is important to remember that when using these equations, your calculator must be in radians mode.

## The Period and Frequency of a Mass on a Spring

One interesting characteristic of the SHM of an object attached to a spring is that the angular frequency, and therefore the period and frequency of the motion, depend on only the mass and the force constant, and not on other factors such as the amplitude of the motion. We can use the equations of motion and Newton's second law $\left(\overrightarrow{\mathbf{F}}_{\text {net }}=m \overrightarrow{\mathbf{a}}\right)$ to find equations for the angular frequency, frequency, and period.

Consider the block on a spring on a frictionless surface. There are three forces on the mass: the weight, the normal force, and the force due to the spring. The only two forces that act perpendicular to the surface are the weight and the normal force, which have equal magnitudes and opposite directions, and thus sum to zero. The only force that acts parallel to the surface is the force due to the spring, so the net force must be equal to the force of the spring:

$$
\begin{aligned}
F_{x} & =-k x \\
m a & =-k x \\
m \frac{d^{2} x}{d t^{2}} & =-k x \\
\frac{d^{2} x}{d t^{2}} & =-\frac{k}{m} x
\end{aligned}
$$

Substituting the equations of motion for $x$ and a gives us

$$
-A \omega^{2} \cos (\omega t+\phi)=-\frac{k}{m} A \cos (\omega t+\phi)
$$

Cancelling out like terms and solving for the angular frequency yields

$$
\omega=\sqrt{\frac{k}{m}}
$$

The angular frequency depends only on the force constant and the mass, and not the amplitude. The angular frequency is defined as $\omega=2 \pi / T$, which yields an equation for the period of the motion:

$$
T=2 \pi \sqrt{\frac{m}{k}}
$$

The period also depends only on the mass and the force constant. The greater the mass, the longer the period. The stiffer the spring, the shorter the period. The frequency is

$$
f=\frac{1}{T}=\frac{1}{2 \pi} \sqrt{\frac{k}{m}}
$$

## Vertical Motion and a Horizontal Spring

When a spring is hung vertically and a block is attached and set in motion, the block oscillates in SHM. In this case, there is no normal force, and the net effect of the force of gravity is to change the equilibrium position. Consider Figure 15.9. Two forces act on the block: the weight and the force of the spring. The weight is constant and the force of the spring changes as the length of the spring changes.

When the block reaches the equilibrium position, as seen in Figure 15.9, the force of the spring equals the weight of the block, $F_{\text {net }}=F_{\mathrm{s}}-m g=0$, where

$$
-k(-\Delta y)=m g
$$

From the figure, the change in the position is $\Delta y=y_{0}-y_{1}$ and since $-k(-\Delta y)=m g$, we have

$$
k\left(y_{0}-y_{1}\right)-m g=0
$$

If the block is displaced and released, it will oscillate around the new equilibrium position. As shown in Figure 15.10, if the position of the block is recorded as a function of time, the recording is a periodic function.

If the block is displaced to a position $y$, the net force becomes $F_{\text {net }}=k\left(y-y_{0}\right)-m g=0$. But we found that at the equilibrium position, $m g=k \Delta y=k y_{0}-k y_{1}$. Substituting for the weight in the equation yields

$$
F_{\text {net }}=k y-k y_{0}-\left(k y_{0}-k y_{1}\right)=-k\left(y-y_{1}\right)
$$

Recall that $y_{1}$ is just the equilibrium position and any position can be set to be the point $y=0.00 \mathrm{~m}$. So let's set $y_{1}$ to $y=0.00 \mathrm{~m}$. The net force then becomes

$$
\begin{aligned}
F_{\text {net }} & =-k y \\
m \frac{d^{2} y}{d t^{2}} & =-k y
\end{aligned}
$$

This is just what we found previously for a horizontally sliding mass on a spring. The constant force of gravity only served to shift the equilibrium location of the mass. Therefore, the solution should be the same form as for a block on a horizontal spring, $y(t)=A \cos (\omega t+\phi)$. The equations for the velocity and the acceleration also have the same form as for the horizontal case. Note that the inclusion of the phase shift means that the motion can actually be modeled using either a cosine or a sine function, since these two functions only differ by a phase shift.

### 15.2 Energy in Simple Harmonic Motion

To produce a deformation in an object, we must do work. That is, whether you pluck a guitar string or compress a car's shock absorber, a force must be exerted through a distance. If the only result is deformation, and no work goes into thermal, sound, or kinetic energy, then all the work is initially stored in the deformed object as some form of potential energy.

Consider the example of a block attached to a spring on a frictionless table, oscillating in SHM. The force of the spring is a conservative force (which you studied in the chapter on potential energy and conservation of energy), and we can define a potential energy for it. This potential energy is the energy stored in the spring when the spring is extended or compressed. In this case, the block oscillates in one dimension with the force of the spring acting parallel to the motion:

$$
W=\int_{x_{i}}^{x_{f}} F_{x} d x=\int_{x_{i}}^{x_{f}}-k x d x=\left[-\frac{1}{2} k x^{2}\right]_{x_{i}}^{x_{f}}=-\left[\frac{1}{2} k x_{f}^{2}-\frac{1}{2} k x_{i}^{2}\right]=-\left[U_{f}-U_{i}\right]=-\Delta U
$$

When considering the energy stored in a spring, the equilibrium position, marked as $x_{i}=0.00 \mathrm{~m}$, is the position at which the energy stored in the spring is equal to zero. When the spring is stretched or compressed a distance $x$, the potential energy stored in the spring is

$$
U=\frac{1}{2} k x^{2}
$$

## Energy and the Simple Harmonic Oscillator

To study the energy of a simple harmonic oscillator, we need to consider all the forms of energy. Consider the example of a block attached to a spring, placed on a frictionless surface, oscillating in SHM. The potential energy stored in the deformation of the spring is

$$
U=\frac{1}{2} k x^{2}
$$

In a simple harmonic oscillator, the energy oscillates between kinetic energy of the mass $K=\frac{1}{2} m v^{2}$ and potential energy $U=\frac{1}{2} k x^{2}$ stored in the spring. In the SHM of the mass and spring system, there are no dissipative forces, so the total energy is the sum of the potential energy and kinetic energy. In this section, we consider the conservation of energy of the system. The concepts examined are valid for all simple harmonic oscillators, including those where the gravitational force plays a role.

Consider Figure 15.11, which shows an oscillating block attached to a spring. In the case of undamped SHM, the energy oscillates back and forth between kinetic and potential, going completely from one form of energy to the other as the system oscillates. So for the simple example of an object on a frictionless surface attached to a spring, the motion starts with all of the energy stored in the spring as elastic potential energy. As the object starts to move, the elastic potential energy is converted into kinetic energy, becoming entirely kinetic energy at the equilibrium position. The energy is then converted back into elastic potential energy by the spring as it is stretched or compressed. The velocity becomes zero when the kinetic energy is completely converted, and this cycle then repeats. Understanding the conservation of energy in these cycles will provide extra insight here and in later applications of SHM, such as alternating circuits.

Consider Figure 15.11, which shows the energy at specific points on the periodic motion. While staying constant, the energy oscillates between the kinetic energy of the block and the potential energy stored in the spring:

$$
E_{\text {Total }}=U+K=\frac{1}{2} k x^{2}+\frac{1}{2} m v^{2}
$$

The motion of the block on a spring in SHM is defined by the position $x(t)=A \cos (\omega t+\phi)$ with a velocity of $v(t)=-A \omega \sin (\omega t+\phi)$. Using these equations, the trigonometric identity $\cos ^{2} \theta+\sin ^{2} \theta=1$ and $\omega=\sqrt{\frac{k}{m}}$, we can find the total energy of the system:

$$
\begin{aligned}
E_{\text {Total }} & =\frac{1}{2} k A^{2} \cos ^{2}(\omega t+\phi)+\frac{1}{2} m A^{2} \omega^{2} \sin ^{2}(\omega t+\phi) \\
& =\frac{1}{2} k A^{2} \cos ^{2}(\omega t+\phi)+\frac{1}{2} m A^{2}\left(\frac{k}{m}\right) \sin ^{2}(\omega t+\phi) \\
& =\frac{1}{2} k A^{2} \cos ^{2}(\omega t+\phi)+\frac{1}{2} k A^{2} \sin ^{2}(\omega t+\phi) \\
& =\frac{1}{2} k A^{2}\left(\cos ^{2}(\omega t+\phi)+\sin ^{2}(\omega t+\phi)\right) \\
& =\frac{1}{2} k A^{2}
\end{aligned}
$$

The total energy of the system of a block and a spring is equal to the sum of the potential energy stored in the spring plus the kinetic energy of the block and is proportional to the square of the amplitude $E_{\text {Total }}=(1 / 2) k A^{2}$. The total energy of the system is constant.

A closer look at the energy of the system shows that the kinetic energy oscillates like a sine-squared function, while the potential energy oscillates like a cosine-squared function. However, the total energy for the system is
constant and is proportional to the amplitude squared. Figure 15.12 shows a plot of the potential, kinetic, and total energies of the block and spring system as a function of time. Also plotted are the position and velocity as a function of time. Before time $t=0.0 \mathrm{~s}$, the block is attached to the spring and placed at the equilibrium position. Work is done on the block by applying an external force, pulling it out to a position of $x=+A$. The system now has potential energy stored in the spring. At time $t=0.00 \mathrm{~s}$, the position of the block is equal to the amplitude, the potential energy stored in the spring is equal to $U=\frac{1}{2} k A^{2}$, and the force on the block is maximum and points in the negative $x$-direction $\left(F_{S}=-k A\right)$. The velocity and kinetic energy of the block are zero at time $t=0.00 \mathrm{~s}$. At time $t=0.00 \mathrm{~s}$, the block is released from rest.

## Oscillations About an Equilibrium Position

We have just considered the energy of SHM as a function of time. Another interesting view of the simple harmonic oscillator is to consider the energy as a function of position. Figure 15.13 shows a graph of the energy versus position of a system undergoing SHM.

The potential energy curve in Figure 15.13 resembles a bowl. When a marble is placed in a bowl, it settles to the equilibrium position at the lowest point of the bowl $(x=0)$. This happens because a restoring force points toward the equilibrium point. This equilibrium point is sometimes referred to as a fixed point. When the marble is disturbed to a different position $(x=+A)$, the marble oscillates around the equilibrium position. Looking back at the graph of potential energy, the force can be found by looking at the slope of the potential energy graph $\left(F=-\frac{d U}{d x}\right)$. Since the force on either side of the fixed point points back toward the equilibrium point, the equilibrium point is called a stable equilibrium point. The points $x=A$ and $x=-A$ are called the turning points. (See Potential Energy and Conservation of Energy.)

Stability is an important concept. If an equilibrium point is stable, a slight disturbance of an object that is initially at the stable equilibrium point will cause the object to oscillate around that point. The stable equilibrium point occurs because the force on either side is directed toward it. For an unstable equilibrium point, if the object is disturbed slightly, it does not return to the equilibrium point.

Consider the marble in the bowl example. If the bowl is right-side up, the marble, if disturbed slightly, will oscillate around the stable equilibrium point. If the bowl is turned upside down, the marble can be balanced on the top, at the equilibrium point where the net force is zero. However, if the marble is disturbed slightly, it will not return to the equilibrium point, but will instead roll off the bowl. The reason is that the force on either side of the equilibrium point is directed away from that point. This point is an unstable equilibrium point.

The process of determining whether an equilibrium point is stable or unstable can be formalized. Consider the potential energy curves shown in Figure 15.15. The force can be found by analyzing the slope of the graph. The force is $F=-\frac{d U}{d x}$. In (a), the fixed point is at $x=0.00 \mathrm{~m}$. When $x<0.00 \mathrm{~m}$, the force is positive. When $x>0.00 \mathrm{~m}$, the force is negative. This is a stable point. In (b), the fixed point is at $x=0.00 \mathrm{~m}$. When $x<0.00 \mathrm{~m}$, the force is negative. When $x>0.00 \mathrm{~m}$, the force is also negative. This is an unstable point.

A practical application of the concept of stable equilibrium points is the force between two neutral atoms in a molecule. If two molecules are in close proximity, separated by a few atomic diameters, they can experience an attractive force. If the molecules move close enough so that the electron shells of the other electrons overlap, the force between the molecules becomes repulsive. The attractive force between the two atoms may cause the atoms to form a molecule. The force between the two molecules is not a linear force and cannot be modeled simply as two masses separated by a spring, but the atoms of the molecule can oscillate around an equilibrium point when displaced a small amount from the equilibrium position. The atoms oscillate due the attractive force and repulsive force between the two atoms.

Consider one example of the interaction between two atoms known as the van Der Waals interaction. It is beyond the scope of this chapter to discuss in depth the interactions of the two atoms, but the oscillations of the atoms can be examined by considering one example of a model of the potential energy of the system. One suggestion to model the potential energy of this molecule is with the Lennard-Jones 6-12 potential:

$$
U(x)=4 \varepsilon\left[\left(\frac{\sigma}{x}\right)^{12}-\left(\frac{\sigma}{x}\right)^{6}\right]
$$

A graph of this function is shown in Figure 15.16. The two parameters $\varepsilon$ and $\sigma$ are found experimentally.

From the graph, you can see that there is a potential energy well, which has some similarities to the potential energy well of the potential energy function of the simple harmonic oscillator discussed in Figure 15.13. The Lennard-Jones potential has a stable equilibrium point where the potential energy is minimum and the force on either side of the equilibrium point points toward equilibrium point. Note that unlike the simple harmonic oscillator, the potential well of the Lennard-Jones potential is not symmetric. This is due to the fact that the force between the atoms is not a Hooke's law force and is not linear. The atoms can still oscillate around the equilibrium position $x_{\min }$ because when $x<x_{\min }$, the force is positive; when $x>x_{\min }$, the force is negative. Notice that as $x$ approaches zero, the slope is quite steep and negative, which means that the force is large and positive. This suggests that it takes a large force to try to push the atoms close together. As $x$ becomes increasingly large, the slope becomes less steep and the force is smaller and negative. This suggests that if given a large enough energy, the atoms can be separated.

If you are interested in this interaction, find the force between the molecules by taking the derivative of the potential energy function. You will see immediately that the force does not resemble a Hooke's law force $(F=-k x)$, but if you are familiar with the binomial theorem:

$$
(1+x)^{n}=1+n x+\frac{n(n-1)}{2!} x^{2}+\frac{n(n-1)(n-2)}{3!} x^{3}+\cdots
$$

the force can be approximated by a Hooke's law force.

## Velocity and Energy Conservation

Getting back to the system of a block and a spring in Figure 15.11, once the block is released from rest, it begins to move in the negative direction toward the equilibrium position. The potential energy decreases and the magnitude of the velocity and the kinetic energy increase. At time $t=T / 4$, the block reaches the equilibrium position $x=0.00 \mathrm{~m}$, where the force on the block and the potential energy are zero. At the equilibrium position, the block reaches a negative velocity with a magnitude equal to the maximum velocity $v=-A \omega$. The kinetic energy is maximum and equal to $K=\frac{1}{2} m v^{2}=\frac{1}{2} m A^{2} \omega^{2}=\frac{1}{2} k A^{2}$. At this point, the force on the block is zero, but momentum carries the block, and it continues in the negative direction toward $x=-A$. As the block continues to move, the force on it acts in the positive direction and the magnitude of the velocity and kinetic energy decrease. The potential energy increases as the spring compresses. At time $t=T / 2$, the block reaches $x=-A$. Here the velocity and kinetic energy are equal to zero. The force on the block is $F=+k A$ and the potential energy stored in the spring is $U=\frac{1}{2} k A^{2}$. During the oscillations, the total energy is constant and equal to the sum of the potential energy and the kinetic energy of the system,

$$
E_{\text {Total }}=\frac{1}{2} k x^{2}+\frac{1}{2} m v^{2}=\frac{1}{2} k A^{2}
$$

The equation for the energy associated with SHM can be solved to find the magnitude of the velocity at any position:

$$
|\nu|=\sqrt{\frac{k}{m}\left(A^{2}-x^{2}\right)}
$$

The energy in a simple harmonic oscillator is proportional to the square of the amplitude. When considering many forms of oscillations, you will find the energy proportional to the amplitude squared.

### 15.3 Comparing Simple Harmonic Motion and Circular Motion

An easy way to model SHM is by considering uniform circular motion. Figure 15.17 shows one way of using this method. A peg (a cylinder of wood) is attached to a vertical disk, rotating with a constant angular frequency. Figure 15.18 shows a side view of the disk and peg. If a lamp is placed above the disk and peg, the peg produces a shadow. Let the disk have a radius of $r=A$ and define the position of the shadow that coincides with the center line of the disk to be $x=0.00 \mathrm{~m}$. As the disk rotates at a constant rate, the shadow oscillates between $x=+A$ and $x=-A$. Now imagine a block on a spring beneath the floor as shown in Figure 15.18.

If the disk turns at the proper angular frequency, the shadow follows along with the block. The position of the shadow can be modeled with the equation

$$
x(t)=A \cos (\omega t)
$$

Recall that the block attached to the spring does not move at a constant velocity. How often does the wheel have to turn to have the peg's shadow always on the block? The disk must turn at a constant angular frequency equal to $2 \pi$ times the frequency of oscillation $(\omega=2 \pi f)$.

Figure 15.19 shows the basic relationship between uniform circular motion and SHM. The peg lies at the tip of the radius, a distance $A$ from the center of the disk. The $x$-axis is defined by a line drawn parallel to the ground, cutting the disk in half. The $y$-axis (not shown) is defined by a line perpendicular to the ground, cutting the disk into a left half and a right half. The center of the disk is the point $(x=0, y=0)$. The projection of the position of the peg onto the fixed $x$-axis gives the position of the shadow, which undergoes SHM analogous to the system of the block and spring. At the time shown in the figure, the projection has position $x$ and moves to the left with velocity $v$. The tangential velocity of the peg around the circle equals $\bar{v}_{\max }$ of the block on the spring. The $x$-component of the velocity is equal to the velocity of the block on the spring.

We can use Figure 15.19 to analyze the velocity of the shadow as the disk rotates. The peg moves in a circle with a speed of $v_{\max }=A \omega$. The shadow moves with a velocity equal to the component of the peg's velocity that is parallel to the surface where the shadow is being produced:

$$
v=-v_{\max } \sin (\omega t)
$$

It follows that the acceleration is

$$
a=-a_{\max } \cos (\omega t)
$$

### 15.4 Pendulums

Pendulums are in common usage. Grandfather clocks use a pendulum to keep time and a pendulum can be used to measure the acceleration due to gravity. For small displacements, a pendulum is a simple harmonic oscillator.

## The Simple Pendulum

A simple pendulum is defined to have a point mass, also known as the pendulum bob, which is suspended from a string of length $L$ with negligible mass (Figure 15.20). Here, the only forces acting on the bob are the force of gravity (i.e., the weight of the bob) and tension from the string. The mass of the string is assumed to be negligible as compared to the mass of the bob.

Consider the torque on the pendulum. The force providing the restoring torque is the component of the weight of the pendulum bob that acts along the arc length. The torque is the length of the string $L$ times the component of the net force that is perpendicular to the radius of the arc. The minus sign indicates the torque acts in the opposite direction of the angular displacement:

$$
\begin{aligned}
\tau & =-L(m g \sin \theta) \\
I \alpha & =-L(m g \sin \theta) \\
I \frac{d^{2} \theta}{d t^{2}} & =-L(m g \sin \theta) \\
m L^{2} \frac{d^{2} \theta}{d t^{2}} & =-L(m g \sin \theta) \\
\frac{d^{2} \theta}{d t^{2}} & =-\frac{g}{L} \sin \theta
\end{aligned}
$$

The solution to this differential equation involves advanced calculus, and is beyond the scope of this text. But note that for small angles (less than 15 degrees), $\sin \theta$ and $\theta$ differ by less than $1 \%$, so we can use the small
angle approximation $\sin \theta \approx \theta$. The angle $\theta$ describes the position of the pendulum. Using the small angle approximation gives an approximate solution for small angles,

$$
\frac{d^{2} \theta}{d t^{2}}=-\frac{g}{L} \theta
$$

Because this equation has the same form as the equation for SHM, the solution is easy to find. The angular frequency is

$$
\omega=\sqrt{\frac{g}{L}}
$$

and the period is

$$
T=2 \pi \sqrt{\frac{L}{g}}
$$

The period of a simple pendulum depends on its length and the acceleration due to gravity. The period is completely independent of other factors, such as mass and the maximum displacement. As with simple harmonic oscillators, the period $T$ for a pendulum is nearly independent of amplitude, especially if $\theta$ is less than about $15^{\circ}$. Even simple pendulum clocks can be finely adjusted and remain accurate.

Note the dependence of $T$ on $g$. If the length of a pendulum is precisely known, it can actually be used to measure the acceleration due to gravity, as in the following example.

## EXAMPLE 15.3

## Measuring Acceleration due to Gravity by the Period of a Pendulum

What is the acceleration due to gravity in a region where a simple pendulum having a length $75.000 \mathrm{~cm}$ has a period of $1.7357 \mathrm{~s}$ ?

## Strategy

We are asked to find $g$ given the period $T$ and the length $L$ of a pendulum. We can solve $T=2 \pi \sqrt{\frac{L}{g}}$ for $g$, assuming only that the angle of deflection is less than $15^{\circ}$.

## Solution

1. Square $T=2 \pi \sqrt{\frac{L}{g}}$ and solve for $g$ :

$$
g=4 \pi^{2} \frac{L}{T^{2}}
$$

2. Substitute known values into the new equation:

$$
g=4 \pi^{2} \frac{0.75000 \mathrm{~m}}{(1.7357 \mathrm{~s})^{2}}
$$

3. Calculate to find $g$ :

$$
g=9.8281 \mathrm{~m} / \mathrm{s}^{2}
$$

## Significance

This method for determining $g$ can be very accurate, which is why length and period are given to five digits in this example. For the precision of the approximation $\sin \theta \approx \theta$ to be better than the precision of the pendulum length and period, the maximum displacement angle should be kept below about $0.5^{\circ}$.

## Physical Pendulum

Any object can oscillate like a pendulum. Consider a coffee mug hanging on a hook in the pantry. If the mug gets knocked, it oscillates back and forth like a pendulum until the oscillations die out. We have described a simple pendulum as a point mass and a string. A physical pendulum is any object whose oscillations are similar to those of the simple pendulum, but cannot be modeled as a point mass on a string, and the mass distribution must be included into the equation of motion.

As for the simple pendulum, the restoring force of the physical pendulum is the force of gravity. With the simple pendulum, the force of gravity acts on the center of the pendulum bob. In the case of the physical pendulum, the force of gravity acts on the center of mass (CM) of an object. The object oscillates about a point O. Consider an object of a generic shape as shown in Figure 15.21.

When a physical pendulum is hanging from a point but is free to rotate, it rotates because of the torque applied at the CM, produced by the component of the object's weight that acts tangent to the motion of the CM. Taking the counterclockwise direction to be positive, the component of the gravitational force that acts tangent to the motion is $-m g \sin \theta$. The minus sign is the result of the restoring force acting in the opposite direction of the increasing angle. Recall that the torque is equal to $\vec{\tau}=\overrightarrow{\mathbf{r}} \times \overrightarrow{\mathbf{F}}$. The magnitude of the torque is equal to the length of the radius arm times the tangential component of the force applied, $|\tau|=r F \sin \theta$. Here, the length $L$ of the radius arm is the distance between the point of rotation and the CM. To analyze the motion, start with the net torque. Like the simple pendulum, consider only small angles so that $\sin \theta \approx \theta$. Recall from Fixed-Axis Rotation on rotation that the net torque is equal to the moment of inertia $I=\int r^{2} d m$ times the angular acceleration $\alpha$, where $\alpha=\frac{d^{2} \theta}{d t^{2}}$ :

$$
I \alpha=\tau_{\text {net }}=L(-m g) \sin \theta
$$

Using the small angle approximation and rearranging:

$$
\begin{aligned}
I \alpha & =-L(m g) \theta \\
I \frac{d^{2} \theta}{d t^{2}} & =-L(m g) \theta \\
\frac{d^{2} \theta}{d t^{2}} & =-\left(\frac{m g L}{I}\right) \theta
\end{aligned}
$$

Once again, the equation says that the second time derivative of the position (in this case, the angle) equals minus a constant $\left(-\frac{m g L}{I}\right)$ times the position. The solution is

$$
\theta(t)=\Theta \cos (\omega t+\phi)
$$

where $\Theta$ is the maximum angular displacement. The angular frequency is

$$
\omega=\sqrt{\frac{m g L}{I}}
$$

The period is therefore

$$
T=2 \pi \sqrt{\frac{I}{m g L}}
$$

Note that for a simple pendulum, the moment of inertia is $I=\int r^{2} d m=m L^{2}$ and the period reduces to $T=2 \pi \sqrt{\frac{L}{g}}$.

## EXAMPLE 15.4

## Reducing the Swaying of a Skyscraper

In extreme conditions, skyscrapers can sway up to two meters with a frequency of up to $20.00 \mathrm{~Hz}$ due to high winds or seismic activity. Several companies have developed physical pendulums that are placed on the top of the skyscrapers. As the skyscraper sways to the right, the pendulum swings to the left, reducing the sway. Assuming the oscillations have a frequency of $0.50 \mathrm{~Hz}$, design a pendulum that consists of a long beam, of constant density, with a mass of 100 metric tons and a pivot point at one end of the beam. What should be the length of the beam?

## Strategy

We are asked to find the length of the physical pendulum with a known mass. We first need to find the moment of inertia of the beam. We can then use the equation for the period of a physical pendulum to find the length.

## Solution

1. Find the moment of inertia for the CM:
2. Use the parallel axis theorem to find the moment of inertia about the point of rotation:

$$
I=I_{\mathrm{CM}}+{\frac{L^{2}}{4}}^{M} M=\frac{1}{12} M L^{2}+\frac{1}{4} M L^{2}=\frac{1}{3} M L^{2}
$$

3. The period of a physical pendulum has a period of $T=2 \pi \sqrt{\frac{I}{m g L}}$. Use the moment of inertia to solve for the length $L$ :

$$
\begin{aligned}
T & =2 \pi \sqrt{\frac{I}{M g L}}=2 \pi \sqrt{\frac{\frac{1}{3} M L^{2}}{M g \frac{L}{2}}}=2 \pi \sqrt{\frac{2 L}{3 g}} \\
L & =\frac{3 T^{2} g}{8 \pi^{2}}=1.49 \mathrm{~m}
\end{aligned}
$$

4. This length $L$ is from the center of mass to the axis of rotation, which is half the length of the pendulum. Therefore the length $H$ of the pendulum is:

$$
H=2 L=5.96 \mathrm{~m}
$$

## Significance

There are many ways to reduce the oscillations, including modifying the shape of the skyscrapers, using multiple physical pendulums, and using tuned-mass dampers.

## Torsional Pendulum

A torsional pendulum consists of a rigid body suspended by a light wire or spring (Figure 15.22). When the body is twisted some small maximum angle $(\Theta)$ and released from rest, the body oscillates between $(\theta=+\Theta)$ and $(\theta=-\Theta)$. The restoring torque is supplied by the shearing of the string or wire.

The restoring torque can be modeled as being proportional to the angle:

$$
\tau=-\kappa \theta
$$

The variable kappa ( $\kappa$ ) is known as the torsion constant of the wire or string. The minus sign shows that the restoring torque acts in the opposite direction to increasing angular displacement. The net torque is equal to the moment of inertia times the angular acceleration:

$$
\begin{aligned}
& I \frac{d^{2} \theta}{d t^{2}}=-\kappa \theta \\
& \frac{d^{2} \theta}{d t^{2}}=-\frac{\kappa}{I} \theta
\end{aligned}
$$

This equation says that the second time derivative of the position (in this case, the angle) equals a negative constant times the position. This looks very similar to the equation of motion for the SHM $\frac{d^{2} x}{d t^{2}}=-\frac{k}{m} x$, where the period was found to be $T=2 \pi \sqrt{\frac{m}{k}}$. Therefore, the period of the torsional pendulum can be found using

$$
T=2 \pi \sqrt{\frac{I}{\kappa}}
$$

The units for the torsion constant are $[\kappa]=\mathrm{N}-\mathrm{m}=\left(\mathrm{kg} \frac{\mathrm{m}}{\mathrm{s}^{2}}\right) \mathrm{m}=\mathrm{kg} \frac{\mathrm{m}^{2}}{\mathrm{~s}^{2}}$ and the units for the moment of inertial are $[I]=\mathrm{kg}-\mathrm{m}^{2}$, which show that the unit for the period is the second.

## EXAMPLE 15.5

## Measuring the Torsion Constant of a String

A rod has a length of $l=0.30 \mathrm{~m}$ and a mass of $4.00 \mathrm{~kg}$. A string is attached to the $\mathrm{CM}$ of the rod and the system is hung from the ceiling (Figure 15.23). The rod is displaced 10 degrees from the equilibrium position and released from rest. The rod oscillates with a period of $0.5 \mathrm{~s}$. What is the torsion constant $\kappa$ ?

## Strategy

We are asked to find the torsion constant of the string. We first need to find the moment of inertia.

## Solution

1. Find the moment of inertia for the CM:

$$
I_{\mathrm{CM}}=\int x^{2} d m=\int_{-L / 2}^{+L / 2} x^{2} \lambda d x=\lambda\left[\frac{x^{3}}{3}\right]_{-L / 2}^{+L / 2}=\lambda \frac{2 L^{3}}{24}=\left(\frac{M}{L}\right) \frac{2 L^{3}}{24}=\frac{1}{12} M L^{2}
$$

2. Calculate the torsion constant using the equation for the period:

$$
\begin{aligned}
T & =2 \pi \sqrt{\frac{I}{\kappa}} \\
\kappa & =I\left(\frac{2 \pi}{T}\right)^{2}=\left(\frac{1}{12} M L^{2}\right)\left(\frac{2 \pi}{T}\right)^{2} \\
& =\left(\frac{1}{12}(4.00 \mathrm{~kg})(0.30 \mathrm{~m})^{2}\right)\left(\frac{2 \pi}{0.50 \mathrm{~s}}\right)^{2}=4.73 \mathrm{~N} \cdot \mathrm{m}
\end{aligned}
$$

## Significance

Like the force constant of the system of a block and a spring, the larger the torsion constant, the shorter the period.

### 15.5 Damped Oscillations

In the real world, oscillations seldom follow true SHM. Friction of some sort usually acts to dampen the motion so it dies away, or needs more force to continue. In this section, we examine some examples of damped harmonic motion and see how to modify the equations of motion to describe this more general case.

A guitar string stops oscillating a few seconds after being plucked. To keep swinging on a playground swing, you must keep pushing (Figure 15.24). Although we can often make friction and other nonconservative forces small or negligible, completely undamped motion is rare. In fact, we may even want to damp oscillations, such as with car shock absorbers.

Consider the forces acting on the mass. Note that the only contribution of the weight is to change the equilibrium position, as discussed earlier in the chapter. Therefore, the net force is equal to the force of the spring and the damping force $\left(F_{D}\right)$. If the magnitude of the velocity is small, meaning the mass oscillates slowly, the damping force is proportional to the velocity and acts against the direction of motion $\left(F_{D}=-b v\right)$. The net force on the mass is therefore

$$
m a=-b v-k x
$$

Writing this as a differential equation in $x$, we obtain

$$
m \frac{d^{2} x}{d t^{2}}+b \frac{d x}{d t}+k x=0
$$

To determine the solution to this equation, consider the plot of position versus time shown in Figure 15.26. The curve resembles a cosine curve oscillating in the envelope of an exponential function $A_{0} e^{-\alpha t}$ where $\alpha=\frac{b}{2 m}$. The solution is

$$
x(t)=A_{0} e^{-\frac{b}{2 m} t} \cos (\omega t+\phi)
$$

It is left as an exercise to prove that this is, in fact, the solution. To prove that it is the right solution, take the first and second derivatives with respect to time and substitute them into Equation 15.23. It is found that Equation 15.24 is the solution if

$$
\omega=\sqrt{\frac{k}{m}-\left(\frac{b}{2 m}\right)^{2}}
$$

Recall that the angular frequency of a mass undergoing SHM is equal to the square root of the force constant divided by the mass. This is often referred to as the natural angular frequency, which is represented as

$$
\omega_{0}=\sqrt{\frac{k}{m}}
$$

The angular frequency for damped harmonic motion becomes

$$
\omega=\sqrt{\omega_{0}^{2}-\left(\frac{b}{2 m}\right)^{2}}
$$

Recall that when we began this description of damped harmonic motion, we stated that the damping must be small. Two questions come to mind. Why must the damping be small? And how small is small? If you gradually increase the amount of damping in a system, the period and frequency begin to be affected, because damping opposes and hence slows the back and forth motion. (The net force is smaller in both directions.) If there is very large damping, the system does not even oscillate-it slowly moves toward equilibrium. The angular frequency is equal to

$$
\omega=\sqrt{\frac{k}{m}-\left(\frac{b}{2 m}\right)^{2}}
$$

As $b$ increases, $\frac{k}{m}-\left(\frac{b}{2 m}\right)^{2}$ becomes smaller and eventually reaches zero when $b=\sqrt{4 m k}$. If $b$ becomes any larger, $\frac{k}{m}-\left(\frac{b}{2 m}\right)^{2}$ becomes a negative number and $\sqrt{\frac{k}{m}-\left(\frac{b}{2 m}\right)^{2}}$ is a complex number.

Figure 15.27 shows the displacement of a harmonic oscillator for different amounts of damping. When the
damping constant is small, $b<\sqrt{4 m k}$, the system oscillates while the amplitude of the motion decays exponentially. This system is said to be underdamped, as in curve (a). Many systems are underdamped, and oscillate while the amplitude decreases exponentially, such as the mass oscillating on a spring. The damping may be quite small, but eventually the mass comes to rest. If the damping constant is $b=\sqrt{4 m k}$, the system is said to be critically damped, as in curve (b). An example of a critically damped system is the shock absorbers in a car. It is advantageous to have the oscillations decay as fast as possible. Here, the system does not oscillate, but asymptotically approaches the equilibrium condition as quickly as possible. Curve (c) in Figure 15.27 represents an overdamped system where $b>\sqrt{4 m k}$. An overdamped system will approach equilibrium over a longer period of time.

Critical damping is often desired, because such a system returns to equilibrium rapidly and remains at equilibrium as well. In addition, a constant force applied to a critically damped system moves the system to a new equilibrium position in the shortest time possible without overshooting or oscillating about the new position.

### 15.6 Forced Oscillations

Sit in front of a piano sometime and sing a loud brief note at it with the dampers off its strings (Figure 15.28). It will sing the same note back at you-the strings, having the same frequencies as your voice, are resonating in response to the forces from the sound waves that you sent to them. This is a good example of the fact that objects-in this case, piano strings-can be forced to oscillate, and oscillate most easily at their natural frequency. In this section, we briefly explore applying a periodic driving force acting on a simple harmonic oscillator. The driving force puts energy into the system at a certain frequency, not necessarily the same as the natural frequency of the system. Recall that the natural frequency is the frequency at which a system would
oscillate if there were no driving and no damping force.

Most of us have played with toys involving an object supported on an elastic band, something like the paddle ball suspended from a finger in Figure 15.29. Imagine the finger in the figure is your finger. At first, you hold your finger steady, and the ball bounces up and down with a small amount of damping. If you move your finger up and down slowly, the ball follows along without bouncing much on its own. As you increase the frequency at which you move your finger up and down, the ball responds by oscillating with increasing amplitude. When you drive the ball at its natural frequency, the ball's oscillations increase in amplitude with each oscillation for as long as you drive it. The phenomenon of driving a system with a frequency equal to its natural frequency is called resonance. A system being driven at its natural frequency is said to resonate. As the driving frequency gets progressively higher than the resonant or natural frequency, the amplitude of the oscillations becomes smaller until the oscillations nearly disappear, and your finger simply moves up and down with little effect on the ball.

Consider a simple experiment. Attach a mass $m$ to a spring in a viscous fluid, similar to the apparatus discussed in the damped harmonic oscillator. This time, instead of fixing the free end of the spring, attach the free end to a disk that is driven by a variable-speed motor. The motor turns with an angular driving frequency of $\omega$. The rotating disk provides energy to the system by the work done by the driving force $\left(F_{\mathrm{d}}=F_{0} \sin (\omega t)\right)$. The experimental apparatus is shown in Figure 15.30.

Using Newton's second law $\left(\overrightarrow{\mathbf{F}}_{\text {net }}=m \overrightarrow{\mathbf{a}}\right)$, we can analyze the motion of the mass. The resulting equation is similar to the force equation for the damped harmonic oscillator, with the addition of the driving force:

$$
-k x-b \frac{d x}{d t}+F_{0} \sin (\omega t)=m \frac{d^{2} x}{d t^{2}}
$$

When an oscillator is forced with a periodic driving force, the motion may seem chaotic. The motions of the oscillator is known as transients. After the transients die out, the oscillator reaches a steady state, where the motion is periodic. After some time, the steady state solution to this differential equation is

$$
x(t)=A \cos (\omega t+\phi)
$$

Once again, it is left as an exercise to prove that this equation is a solution. Taking the first and second time derivative of $x(t)$ and substituting them into the force equation shows that $x(t)=A \sin (\omega t+\phi)$ is a solution as long as the amplitude is equal to

$$
A=\frac{F_{0}}{\sqrt{m^{2}\left(\omega^{2}-\omega_{0}^{2}\right)^{2}+b^{2} \omega^{2}}}
$$

where $\omega_{0}=\sqrt{\frac{k}{m}}$ is the angular frequency of the driving force. Recall that the angular frequency, and therefore the frequency, of the motor can be adjusted. Looking at the denominator of the equation for the amplitude, when the driving frequency is much smaller, or much larger, than the natural frequency, the square of the difference of the two angular frequencies $\left(\omega^{2}-\omega_{0}^{2}\right)^{2}$ is positive and large, making the denominator large, and the result is a small amplitude for the oscillations of the mass. As the frequency of the driving force approaches the natural frequency of the system, the denominator becomes small and the amplitude of the oscillations becomes large. The maximum amplitude results when the frequency of the driving force equals the natural frequency of the system $\left(A_{\max }=\frac{F_{0}}{b \omega}\right)$.

Figure 15.31 shows a graph of the amplitude of a damped harmonic oscillator as a function of the frequency of the periodic force driving it. Each of the three curves on the graph represents a different amount of damping. All three curves peak at the point where the frequency of the driving force equals the natural frequency of the harmonic oscillator. The highest peak, or greatest response, is for the least amount of damping, because less

