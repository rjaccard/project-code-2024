# CHAPTER 6 Photons and Matter Waves 

INTRODUCTION Two of the most revolutionary concepts of the twentieth century were the description of light as a collection of particles, and the treatment of particles as waves. These wave properties of matter have led to the discovery of technologies such as electron microscopy, which allows us to examine submicroscopic objects such as grains of pollen, as shown above.

In this chapter, you will learn about the energy quantum, a concept that was introduced in 1900 by the German physicist Max Planck to explain blackbody radiation. We discuss how Albert Einstein extended Planck's
concept to a quantum of light (a "photon") to explain the photoelectric effect. We also show how American physicist Arthur H. Compton used the photon concept in 1923 to explain wavelength shifts observed in X-rays. After a discussion of Bohr's model of hydrogen, we describe how matter waves were postulated in 1924 by Louis-Victor de Broglie to justify Bohr's model and we examine the experiments conducted in 1923-1927 by Clinton Davisson and Lester Germer that confirmed the existence of de Broglie's matter waves.

### 6.1 Blackbody Radiation

All bodies emit electromagnetic radiation over a range of wavelengths. In an earlier chapter, we learned that a cooler body radiates less energy than a warmer body. We also know by observation that when a body is heated and its temperature rises, the perceived wavelength of its emitted radiation changes from infrared to red, and then from red to orange, and so forth. As its temperature rises, the body glows with the colors corresponding to ever-smaller wavelengths of the electromagnetic spectrum. This is the underlying principle of the incandescent light bulb: A hot metal filament glows red, and when heating continues, its glow eventually covers the entire visible portion of the electromagnetic spectrum. The temperature (T) of the object that emits radiation, or the emitter, determines the wavelength at which the radiated energy is at its maximum. For example, the Sun, whose surface temperature is in the range between $5000 \mathrm{~K}$ and $6000 \mathrm{~K}$, radiates most strongly in a range of wavelengths about $560 \mathrm{~nm}$ in the visible part of the electromagnetic spectrum. Your body, when at its normal temperature of about $300 \mathrm{~K}$, radiates most strongly in the infrared part of the spectrum.

Radiation that is incident on an object is partially absorbed and partially reflected. At thermodynamic equilibrium, the rate at which an object absorbs radiation is the same as the rate at which it emits it. Therefore, a good absorber of radiation (any object that absorbs radiation) is also a good emitter. A perfect absorber absorbs all electromagnetic radiation incident on it; such an object is called a blackbody.

Although the blackbody is an idealization, because no physical object absorbs $100 \%$ of incident radiation, we can construct a close realization of a blackbody in the form of a small hole in the wall of a sealed enclosure known as a cavity radiator, as shown in Figure 6.2. The inside walls of a cavity radiator are rough and blackened so that any radiation that enters through a tiny hole in the cavity wall becomes trapped inside the cavity. At thermodynamic equilibrium (at temperature $T$ ), the cavity walls absorb exactly as much radiation as they emit. Furthermore, inside the cavity, the radiation entering the hole is balanced by the radiation leaving it. The emission spectrum of a blackbody can be obtained by analyzing the light radiating from the hole. Electromagnetic waves emitted by a blackbody are called blackbody radiation.

The intensity $I(\lambda, T)$ of blackbody radiation depends on the wavelength $\lambda$ of the emitted radiation and on the temperature $T$ of the blackbody (Figure 6.3). The function $I(\lambda, T)$ is the power intensity that is radiated per unit wavelength; in other words, it is the power radiated per unit area of the hole in a cavity radiator per unit wavelength. According to this definition, $I(\lambda, T) d \lambda$ is the power per unit area that is emitted in the wavelength interval from $\lambda$ to $\lambda+d \lambda$. The intensity distribution among wavelengths of radiation emitted by cavities was studied experimentally at the end of the nineteenth century. Generally, radiation emitted by materials only approximately follows the blackbody radiation curve (Figure 6.4); however, spectra of common stars do follow the blackbody radiation curve very closely.

Two important laws summarize the experimental findings of blackbody radiation: Wien's displacement law and Stefan's law. Wien's displacement law is illustrated in Figure 6.3 by the curve connecting the maxima on the intensity curves. In these curves, we see that the hotter the body, the shorter the wavelength corresponding to the emission peak in the radiation curve. Quantitatively, Wien's law reads

$$
\lambda_{\max } T=2.898 \times 10^{-3} \mathrm{~m} \cdot \mathrm{K}
$$

where $\lambda_{\max }$ is the position of the maximum in the radiation curve. In other words, $\lambda_{\max }$ is the wavelength at which a blackbody radiates most strongly at a given temperature $T$. Note that in Equation 6.1, the temperature is in kelvins. Wien's displacement law allows us to estimate the temperatures of distant stars by measuring the wavelength of radiation they emit.

## EXAMPLE 6.1

## Temperatures of Distant Stars

On a clear evening during the winter months, if you happen to be in the Northern Hemisphere and look up at the sky, you can see the constellation Orion (The Hunter). One star in this constellation, Rigel, flickers in a blue color and another star, Betelgeuse, has a reddish color, as shown in Figure 6.5. Which of these two stars is cooler, Betelgeuse or Rigel?

## Strategy

We treat each star as a blackbody. Then according to Wien's law, its temperature is inversely proportional to the wavelength of its peak intensity. The wavelength $\lambda_{\max }^{\text {(blue) }}$ of blue light is shorter than the wavelength $\lambda_{\max }^{\text {(red) }}$ of red light. Even if we do not know the precise wavelengths, we can still set up a proportion.

## Solution

Writing Wien's law for the blue star and for the red star, we have

$$
\lambda_{\max }^{(\mathrm{red})} T_{(\mathrm{red})}=2.898 \times 10^{-3} \mathrm{~m} \cdot \mathrm{K}=\lambda_{\max }^{(\text {blue })} T_{\text {(blue) }}
$$

When simplified, Equation 6.2 gives

$$
T_{(\text {red })}=\frac{\lambda_{\max }^{(\text {blue })}}{\lambda_{\max }^{(\text {red) }}} T_{(\text {blue })}<T_{(\text {blue })}
$$

Therefore, Betelgeuse is cooler than Rigel.

## Significance

Note that Wien's displacement law tells us that the higher the temperature of an emitting body, the shorter the wavelength of the radiation it emits. The qualitative analysis presented in this example is generally valid for any emitting body, whether it is a big object such as a star or a small object such as the glowing filament in an incandescent lightbulb.

Figure 6.5 In the Orion constellation, the red star Betelgeuse, which usually takes on a yellowish tint, appears as the figure's right shoulder (in the upper left). The giant blue star on the bottom right is Rigel, which appears as the hunter's left foot. (credit left: modification of work by Matthew Spinelli, NASA APOD)

The second experimental relation is Stefan's law, which concerns the total power of blackbody radiation emitted across the entire spectrum of wavelengths at a given temperature. In Figure 6.3, this total power is represented by the area under the blackbody radiation curve for a given $T$. As the temperature of a blackbody increases, the total emitted power also increases. Quantitatively, Stefan's law expresses this relation as

$$
P(T)=\sigma A T^{4}
$$

where $A$ is the surface area of a blackbody, $T$ is its temperature (in kelvins), and $\sigma$ is the Stefan-Boltzmann constant, $\sigma=5.670 \times 10^{-8} \mathrm{~W} /\left(\mathrm{m}^{2} \cdot \mathrm{K}^{4}\right)$. Stefan's law enables us to estimate how much energy a star is radiating by remotely measuring its temperature.

## EXAMPLE 6.2

## Power Radiated by Stars

A star such as our Sun will eventually evolve to a "red giant" star and then to a "white dwarf" star. A typical white dwarf is approximately the size of Earth, and its surface temperature is about $2.5 \times 10^{4} \mathrm{~K}$. A typical red giant has a surface temperature of $3.0 \times 10^{3} \mathrm{~K}$ and a radius $\sim 100,000$ times larger than that of a white dwarf. What is the average radiated power per unit area and the total power radiated by each of these types of stars? How do they compare?

## Strategy

If we treat the star as a blackbody, then according to Stefan's law, the total power that the star radiates is proportional to the fourth power of its temperature. To find the power radiated per unit area of the surface, we do not need to make any assumptions about the shape of the star because $P / A$ depends only on temperature. However, to compute the total power, we need to make an assumption that the energy radiates through a spherical surface enclosing the star, so that the surface area is $A=4 \pi R^{2}$, where $R$ is its radius.

## Solution

A simple proportion based on Stefan's law gives

$$
\frac{P_{\mathrm{dwarf}} / A_{\mathrm{dwarf}}}{P_{\text {giant }} / A_{\text {giant }}}=\frac{\sigma T_{\mathrm{dwarf}}^{4}}{\sigma T_{\text {giant }}^{4}}=\left(\frac{T_{\text {dwarf }}}{T_{\text {giant }}}\right)^{4}=\left(\frac{2.5 \times 10^{4}}{3.0 \times 10^{3}}\right)^{4}=4820
$$

The power emitted per unit area by a white dwarf is about 5000 times that the power emitted by a red giant. Denoting this ratio by $a=4.8 \times 10^{3}$, Equation 6.5 gives

$$
\frac{P_{\mathrm{dwarf}}}{P_{\text {giant }}}=a \frac{A_{\mathrm{dwarf}}}{A_{\text {giant }}}=a \frac{4 \pi R_{\mathrm{dwarf}}^{2}}{4 \pi R_{\mathrm{giant}}^{2}}=a\left(\frac{R_{\mathrm{dwarf}}}{R_{\text {giant }}}\right)^{2}=4.8 \times 10^{3}\left(\frac{R_{\mathrm{dwarf}}}{10^{5} R_{\mathrm{dwarf}}}\right)^{2}=4.8 \times 10^{-7}
$$

We see that the total power emitted by a white dwarf is a tiny fraction of the total power emitted by a red giant. Despite its relatively lower temperature, the overall power radiated by a red giant far exceeds that of the white dwarf because the red giant has a much larger surface area. To estimate the absolute value of the emitted power per unit area, we again use Stefan's law. For the white dwarf, we obtain

$$
\frac{P_{\mathrm{dwarf}}}{A_{\mathrm{dwarf}}}=\sigma T_{\mathrm{dwarf}}^{4}=5.670 \times 10^{-8} \frac{\mathrm{W}}{\mathrm{m}^{2} \cdot \mathrm{K}^{4}}\left(2.5 \times 10^{4} \mathrm{~K}\right)^{4}=2.2 \times 10^{10} \mathrm{~W} / \mathrm{m}^{2}
$$

The analogous result for the red giant is obtained by scaling the result for a white dwarf:

$$
\frac{P_{\text {giant }}}{A_{\text {giant }}}=\frac{2.2 \times 10^{10}}{4.82 \times 10^{3}} \frac{\mathrm{W}}{\mathrm{m}^{2}}=4.56 \times 10^{6} \frac{\mathrm{W}}{\mathrm{m}^{2}} \cong 4.6 \times 10^{6} \frac{\mathrm{W}}{\mathrm{m}^{2}}
$$

## Significance

To estimate the total power emitted by a white dwarf, in principle, we could use Equation 6.7. However, to find its surface area, we need to know the average radius, which is not given in this example. Therefore, the solution stops here. The same is also true for the red giant star.

The term "blackbody" was coined by Gustav R. Kirchhoff in 1862. The blackbody radiation curve was known experimentally, but its shape eluded physical explanation until the year 1900. The physical model of a blackbody at temperature $T$ is that of the electromagnetic waves enclosed in a cavity (see Figure 6.2) and at thermodynamic equilibrium with the cavity walls. The waves can exchange energy with the walls. The objective here is to find the energy density distribution among various modes of vibration at various wavelengths (or frequencies). In other words, we want to know how much energy is carried by a single wavelength or a band of wavelengths. Once we know the energy distribution, we can use standard statistical methods (similar to those studied in a previous chapter) to obtain the blackbody radiation curve, Stefan's law, and Wien's displacement law. When the physical model is correct, the theoretical predictions should be the same as the experimental curves.

In a classical approach to the blackbody radiation problem, in which radiation is treated as waves (as you have studied in previous chapters), the modes of electromagnetic waves trapped in the cavity are in equilibrium and continually exchange their energies with the cavity walls. There is no physical reason why a wave should do otherwise: Any amount of energy can be exchanged, either by being transferred from the wave to the material in the wall or by being received by the wave from the material in the wall. This classical picture is the basis of the model developed by Lord Rayleigh and, independently, by Sir James Jeans. The result of this classical model for blackbody radiation curves is known as the Rayleigh-Jeans law. However, as shown in Figure 6.6, the Rayleigh-Jeans law fails to correctly reproduce experimental results. In the limit of short wavelengths, the Rayleigh-Jeans law predicts infinite radiation intensity, which is inconsistent with the experimental results in which radiation intensity has finite values in the ultraviolet region of the spectrum. This divergence between the results of classical theory and experiments, which came to be called the ultraviolet catastrophe, shows how classical physics fails to explain the mechanism of blackbody radiation.

The blackbody radiation problem was solved in 1900 by Max Planck. Planck used the same idea as the Rayleigh-Jeans model in the sense that he treated the electromagnetic waves between the walls inside the cavity classically, and assumed that the radiation is in equilibrium with the cavity walls. The innovative idea that Planck introduced in his model is the assumption that the cavity radiation originates from atomic oscillations inside the cavity walls, and that these oscillations can have only discrete values of energy. Therefore, the radiation trapped inside the cavity walls can exchange energy with the walls only in discrete amounts. Planck's hypothesis of discrete energy values, which he called quanta, assumes that the oscillators inside the cavity walls have quantized energies. This was a brand new idea that went beyond the classical physics of the nineteenth century because, as you learned in a previous chapter, in the classical picture, the energy of an oscillator can take on any continuous value. Planck assumed that the energy of an oscillator $\left(E_{n}\right)$ can have only discrete, or quantized, values:

$$
E_{n}=n h f, \text { where } n=1,2,3, \ldots
$$

In Equation 6.9, $f$ is the frequency of Planck's oscillator. The natural number $n$ that enumerates these discrete energies is called a quantum number. The physical constant $h$ is called Planck's constant:

$$
h=6.626 \times 10^{-34} \mathrm{~J} \cdot \mathrm{s}=4.136 \times 10^{-15} \mathrm{eV} \cdot \mathrm{s}
$$

Each discrete energy value corresponds to a quantum state of a Planck oscillator. Quantum states are enumerated by quantum numbers. For example, when Planck's oscillator is in its first $n=1$ quantum state, its energy is $E_{1}=h f$; when it is in the $n=2$ quantum state, its energy is $E_{2}=2 h f$; when it is in the $n=3$ quantum state, $E_{3}=3 h f ;$ and so on.

Note that Equation 6.9 shows that there are infinitely many quantum states, which can be represented as a sequence $\{h f, 2 h f, 3 h f, \ldots,(n-1) h f, n h f,(n+1) h f, \ldots\}$. Each two consecutive quantum states in this sequence are separated by an energy jump, $\Delta E=h f$. An oscillator in the wall can receive energy from the radiation in the cavity (absorption), or it can give away energy to the radiation in the cavity (emission). The absorption process sends the oscillator to a higher quantum state, and the emission process sends the oscillator to a lower quantum state. Whichever way this exchange of energy goes, the smallest amount of energy that can be exchanged is $h f$. There is no upper limit to how much energy can be exchanged, but whatever is exchanged must be an integer multiple of $h f$. If the energy packet does not have this exact amount, it is neither absorbed nor emitted at the wall of the blackbody.

## Planck's Quantum Hypothesis

Planck's hypothesis of energy quanta states that the amount of energy emitted by the oscillator is carried by the quantum of radiation, $\Delta E$ :

$$
\Delta E=h f
$$

Recall that the frequency of electromagnetic radiation is related to its wavelength and to the speed of light by the fundamental relation $f \lambda=c$. This means that we can express Equation 6.10 equivalently in terms of wavelength $\lambda$. When included in the computation of the energy density of a blackbody, Planck's hypothesis gives the following theoretical expression for the power intensity of emitted radiation per unit wavelength:

$$
I(\lambda, T)=\frac{2 \pi h c^{2}}{\lambda^{5}} \frac{1}{e^{h c / \lambda k_{\mathrm{B}} T}-1}
$$

where $c$ is the speed of light in vacuum and $k_{\mathrm{B}}$ is Boltzmann's constant, $k_{\mathrm{B}}=1.380 \times 10^{-23} \mathrm{~J} / \mathrm{K}$. The theoretical formula expressed in Equation 6.11 is called Planck's blackbody radiation law. This law is in agreement with the experimental blackbody radiation curve (see Figure 6.7). In addition, Wien's displacement law and Stefan's law can both be derived from Equation 6.11. To derive Wien's displacement law, we use differential calculus to find the maximum of the radiation intensity curve $I(\lambda, T)$. To derive Stefan's law and find the value of the Stefan-Boltzmann constant, we use integral calculus and integrate $I(\lambda, T)$ to find the total power radiated by a blackbody at one temperature in the entire spectrum of wavelengths from $\lambda=0$ to $\lambda=\infty$. This derivation is left as an exercise later in this chapter.

## EXAMPLE 6.3

## Planck's Quantum Oscillator

A quantum oscillator in the cavity wall in Figure 6.2 is vibrating at a frequency of $5.0 \times 10^{14} \mathrm{~Hz}$. Calculate the spacing between its energy levels.

## Strategy

Energy states of a quantum oscillator are given by Equation 6.9. The energy spacing $\Delta E$ is obtained by finding the energy difference between two adjacent quantum states for quantum numbers $n+1$ and $n$.

## Solution

We can substitute the given frequency and Planck's constant directly into the equation:

$$
\Delta E=E_{n+1}-E_{n}=(n+1) h f-n h f=h f=\left(6.626 \times 10^{-34} \mathrm{~J} \cdot \mathrm{s}\right)\left(5.0 \times 10^{14} \mathrm{~Hz}\right)=3.3 \times 10^{-19} \mathrm{~J}
$$

## Significance

Note that we do not specify what kind of material was used to build the cavity. Here, a quantum oscillator is a theoretical model of an atom or molecule of material in the wall.

## EXAMPLE 6.4

## Quantum Theory Applied to a Classical Oscillator

A 1.0-kg mass oscillates at the end of a spring with a spring constant of $1000 \mathrm{~N} / \mathrm{m}$. The amplitude of these oscillations is $0.10 \mathrm{~m}$. Use the concept of quantization to find the energy spacing for this classical oscillator. Is the energy quantization significant for macroscopic systems, such as this oscillator?

## Strategy

We use Equation 6.10 as though the system were a quantum oscillator, but with the frequency $f$ of the mass vibrating on a spring. To evaluate whether or not quantization has a significant effect, we compare the quantum energy spacing with the macroscopic total energy of this classical oscillator.

## Solution

For the spring constant, $k=1.0 \times 10^{3} \mathrm{~N} / \mathrm{m}$, the frequency $f$ of the mass, $m=1.0 \mathrm{~kg}$, is

$$
f=\frac{1}{2 \pi} \sqrt{\frac{k}{m}}=\frac{1}{2 \pi} \sqrt{\frac{1.0 \times 10^{3} \mathrm{~N} / \mathrm{m}}{1.0 \mathrm{~kg}}} \simeq 5.0 \mathrm{~Hz}
$$

The energy quantum that corresponds to this frequency is

$$
\Delta E=h f=\left(6.626 \times 10^{-34} \mathrm{~J} \cdot \mathrm{s}\right)(5.0 \mathrm{~Hz})=3.3 \times 10^{-33} \mathrm{~J}
$$

When vibrations have amplitude $A=0.10 \mathrm{~m}$, the energy of oscillations is

$$
E=\frac{1}{2} k A^{2}=\frac{1}{2}(1000 \mathrm{~N} / \mathrm{m})(0.1 \mathrm{~m})^{2}=5.0 \mathrm{~J}
$$

## Significance

Thus, for a classical oscillator, we have $\Delta E / E \approx 10^{-34}$. We see that the separation of the energy levels is immeasurably small. Therefore, for all practical purposes, the energy of a classical oscillator takes on continuous values. This is why classical principles may be applied to macroscopic systems encountered in everyday life without loss of accuracy.

When Planck first published his result, the hypothesis of energy quanta was not taken seriously by the physics community because it did not follow from any established physics theory at that time. It was perceived, even by Planck himself, as a useful mathematical trick that led to a good theoretical "fit" to the experimental curve. This perception was changed in 1905 when Einstein published his explanation of the photoelectric effect, in which he gave Planck's energy quantum a new meaning: that of a particle of light.

### 6.2 Photoelectric Effect

When a metal surface is exposed to a monochromatic electromagnetic wave of sufficiently short wavelength (or equivalently, above a threshold frequency), the incident radiation is absorbed and the exposed surface emits electrons. This phenomenon is known as the photoelectric effect. Electrons that are emitted in this process are called photoelectrons.

The experimental setup to study the photoelectric effect is shown schematically in Figure 6.8. The target material serves as the cathode, which becomes the emitter of photoelectrons when it is illuminated by monochromatic radiation. We call this electrode the photoelectrode. Photoelectrons are collected at the anode, which is kept at a higher potential with respect to the cathode. The potential difference between the electrodes can be increased or decreased, or its polarity can be reversed. The electrodes are enclosed in an evacuated glass tube so that photoelectrons do not lose their kinetic energy on collisions with air molecules in the space between electrodes.

When the target material is not exposed to radiation, no current is registered in this circuit because the circuit is broken (note, there is a gap between the electrodes). But when the target material is connected to the negative terminal of a battery and exposed to radiation, a current is registered in this circuit; this current is
called the photocurrent. Suppose that we now reverse the potential difference between the electrodes so that the target material now connects with the positive terminal of a battery, and then we slowly increase the voltage. The photocurrent gradually dies out and eventually stops flowing completely at some value of this reversed voltage. The potential difference at which the photocurrent stops flowing is called the stopping potential.

## Characteristics of the Photoelectric Effect

The photoelectric effect has three important characteristics that cannot be explained by classical physics: (1) the absence of a lag time, (2) the independence of the kinetic energy of photoelectrons on the intensity of incident radiation, and (3) the presence of a cut-off frequency. Let's examine each of these characteristics.

The absence of lag time

When radiation strikes the target material in the electrode, electrons are emitted almost instantaneously, even at very low intensities of incident radiation. This absence of lag time contradicts our understanding based on classical physics. Classical physics predicts that for low-energy radiation, it would take significant time before irradiated electrons could gain sufficient energy to leave the electrode surface; however, such an energy buildup is not observed.

The intensity of incident radiation and the kinetic energy of photoelectrons

Typical experimental curves are shown in Figure 6.9, in which the photocurrent is plotted versus the applied potential difference between the electrodes. For the positive potential difference, the current steadily grows until it reaches a plateau. Furthering the potential increase beyond this point does not increase the photocurrent at all. A higher intensity of radiation produces a higher value of photocurrent. For the negative potential difference, as the absolute value of the potential difference increases, the value of the photocurrent decreases and becomes zero at the stopping potential. For any intensity of incident radiation, whether the intensity is high or low, the value of the stopping potential always stays at one value.

To understand why this result is unusual from the point of view of classical physics, we first have to analyze the energy of photoelectrons. A photoelectron that leaves the surface has kinetic energy K. It gained this energy from the incident electromagnetic wave. In the space between the electrodes, a photoelectron moves in the electric potential and its energy changes by the amount $q \Delta V$, where $\Delta V$ is the potential difference and $q=-e$. Because no forces are present but electric force, by applying the work-energy theorem, we obtain the energy balance $\Delta K-e \Delta V=0$ for the photoelectron, where $\Delta K$ is the change in the photoelectron's kinetic energy. When the stopping potential $-\Delta V_{s}$ is applied, the photoelectron loses its initial kinetic energy $K_{i}$ and comes to rest. Thus, its energy balance becomes $\left(0-K_{i}\right)-e\left(-\Delta V_{s}\right)=0$, so that $K_{i}=e \Delta V_{s}$. In the presence of the stopping potential, the largest kinetic energy $K_{\max }$ that a photoelectron can have is its initial kinetic energy, which it has at the surface of the photoelectrode. Therefore, the largest kinetic energy of photoelectrons can be directly measured by measuring the stopping potential:

$$
K_{\max }=e \Delta V_{s}
$$

At this point we can see where the classical theory is at odds with the experimental results. In classical theory, the photoelectron absorbs electromagnetic energy in a continuous way; this means that when the incident radiation has a high intensity, the kinetic energy in Equation 6.12 is expected to be high. Similarly, when the radiation has a low intensity, the kinetic energy is expected to be low. But the experiment shows that the maximum kinetic energy of photoelectrons is independent of the light intensity.

For any metal surface, there is a minimum frequency of incident radiation below which photocurrent does not occur. The value of this cut-off frequency for the photoelectric effect is a physical property of the metal: Different materials have different values of cut-off frequency. Experimental data show a typical linear trend (see Figure 6.10). The kinetic energy of photoelectrons at the surface grows linearly with the increasing frequency of incident radiation. Measurements for all metal surfaces give linear plots with one slope. None of these observed phenomena is in accord with the classical understanding of nature. According to the classical description, the kinetic energy of photoelectrons should not depend on the frequency of incident radiation at all, and there should be no cut-off frequency. Instead, in the classical picture, electrons receive energy from the incident electromagnetic wave in a continuous way, and the amount of energy they receive depends only on the intensity of the incident light and nothing else. So in the classical understanding, as long as the light is shining, the photoelectric effect is expected to continue.

## The Work Function

The photoelectric effect was explained in 1905 by A. Einstein. Einstein reasoned that if Planck's hypothesis about energy quanta was correct for describing the energy exchange between electromagnetic radiation and cavity walls, it should also work to describe energy absorption from electromagnetic radiation by the surface of a photoelectrode. He postulated that an electromagnetic wave carries its energy in discrete packets. Einstein's postulate goes beyond Planck's hypothesis because it states that the light itself consists of energy quanta. In other words, it states that electromagnetic waves are quantized.

In Einstein's approach, a beam of monochromatic light of frequency $f$ is made of photons. A photon is a particle of light. Each photon moves at the speed of light and carries an energy quantum $E_{f}$. A photon's energy depends only on its frequency $f$. Explicitly, the energy of a photon is

$$
E_{f}=h f
$$

where $h$ is Planck's constant. In the photoelectric effect, photons arrive at the metal surface and each photon gives away all of its energy to only one electron on the metal surface. This transfer of energy from photon to electron is of the "all or nothing" type, and there are no fractional transfers in which a photon would lose only part of its energy and survive. The essence of a quantum phenomenon is either a photon transfers its entire energy and ceases to exist or there is no transfer at all. This is in contrast with the classical picture, where fractional energy transfers are permitted. Having this quantum understanding, the energy balance for an electron on the surface that receives the energy $E_{f}$ from a photon is

$$
E_{f}=K_{\max }+\phi
$$

where $K_{\max }$ is the kinetic energy, given by Equation 6.12 , that an electron has at the very instant it gets detached from the surface. In this energy balance equation, $\phi$ is the energy needed to detach a photoelectron from the surface. This energy $\phi$ is called the work function of the metal. Each metal has its characteristic work function, as illustrated in Table 6.1. To obtain the kinetic energy of photoelectrons at the surface, we simply invert the energy balance equation and use Equation 6.13 to express the energy of the absorbed photon. This gives us the expression for the kinetic energy of photoelectrons, which explicitly depends on the frequency of incident radiation:

$$
K_{\max }=h f-\phi
$$

This equation has a simple mathematical form but its physics is profound. We can now elaborate on the physical meaning behind Equation 6.14.

Typical Values of the Work Function for Some Common Metals

| Metal | $\phi(\mathbf{e V})$ |
| :--- | :--- |
| $\mathrm{Na}$ | 2.46 |
| $\mathrm{Al}$ | 4.08 |
| $\mathrm{Pb}$ | 4.14 |
| $\mathrm{Zn}$ | 4.31 |
| $\mathrm{Fe}$ | 4.50 |
| $\mathrm{Cu}$ | 4.70 |
| $\mathrm{Ag}$ | 4.73 |
| $\mathrm{Pt}$ | 6.35 |

Table 6.1

In Einstein's interpretation, interactions take place between individual electrons and individual photons. The absence of a lag time means that these one-on-one interactions occur instantaneously. This interaction time cannot be increased by lowering the light intensity. The light intensity corresponds to the number of photons arriving at the metal surface per unit time. Even at very low light intensities, the photoelectric effect still occurs because the interaction is between one electron and one photon. As long as there is at least one photon with enough energy to transfer it to a bound electron, a photoelectron will appear on the surface of the photoelectrode.

The existence of the cut-off frequency $f_{c}$ for the photoelectric effect follows from Equation 6.14 because the kinetic energy $K_{\max }$ of the photoelectron can take only positive values. This means that there must be some threshold frequency for which the kinetic energy is zero, $0=h f_{c}-\phi$. In this way, we obtain the explicit formula for cut-off frequency:

$$
f_{c}=\frac{\phi}{h}
$$

Cut-off frequency depends only on the work function of the metal and is in direct proportion to it. When the work function is large (when electrons are bound fast to the metal surface), the energy of the threshold photon must be large to produce a photoelectron, and then the corresponding threshold frequency is large. Photons with frequencies larger than the threshold frequency $f_{c}$ always produce photoelectrons because they have $K_{\max }>0$. Photons with frequencies smaller than $f_{c}$ do not have enough energy to produce photoelectrons. Therefore, when incident radiation has a frequency below the cut-off frequency, the photoelectric effect is not observed. Because frequency $f$ and wavelength $\lambda$ of electromagnetic waves are related by the fundamental relation $\lambda f=c$ (where $c$ is the speed of light in vacuum), the cut-off frequency has its corresponding cut-off wavelength $\lambda_{c}$ :

$$
\lambda_{c}=\frac{c}{f_{c}}=\frac{c}{\phi / h}=\frac{h c}{\phi}
$$

In this equation, $h c=1240 \mathrm{eV} \cdot \mathrm{nm}$. Our observations can be restated in the following equivalent way: When the incident radiation has wavelengths longer than the cut-off wavelength, the photoelectric effect does not occur.

## Photoelectric Effect for Silver

Radiation with wavelength $300 \mathrm{~nm}$ is incident on a silver surface. Will photoelectrons be observed?

## Strategy

Photoelectrons can be ejected from the metal surface only when the incident radiation has a shorter wavelength than the cut-off wavelength. The work function of silver is $\phi=4.73 \mathrm{eV}$ (Table 6.1). To make the estimate, we use Equation 6.16.

## Solution

The threshold wavelength for observing the photoelectric effect in silver is

$$
\lambda_{c}=\frac{h c}{\phi}=\frac{1240 \mathrm{eV} \cdot \mathrm{nm}}{4.73 \mathrm{eV}}=262 \mathrm{~nm}
$$

The incident radiation has wavelength $300 \mathrm{~nm}$, which is longer than the cut-off wavelength; therefore, photoelectrons are not observed.

## Significance

If the photoelectrode were made of sodium instead of silver, the cut-off wavelength would be $504 \mathrm{~nm}$ and photoelectrons would be observed.

Equation 6.14 in Einstein's model tells us that the maximum kinetic energy of photoelectrons is a linear function of the frequency of incident radiation, which is illustrated in Figure 6.10. For any metal, the slope of this plot has a value of Planck's constant. The intercept with the $K_{\max }$-axis gives us a value of the work function that is characteristic for the metal. On the other hand, $K_{\max }$ can be directly measured in the experiment by measuring the value of the stopping potential $\Delta V_{s}$ (see Equation 6.12) at which the photocurrent stops. These direct measurements allow us to determine experimentally the value of Planck's constant, as well as work functions of materials.

Einstein's model also gives a straightforward explanation for the photocurrent values shown in Figure 6.9. For example, doubling the intensity of radiation translates to doubling the number of photons that strike the surface per unit time. The larger the number of photons, the larger is the number of photoelectrons, which leads to a larger photocurrent in the circuit. This is how radiation intensity affects the photocurrent. The photocurrent must reach a plateau at some value of potential difference because, in unit time, the number of photoelectrons is equal to the number of incident photons and the number of incident photons does not depend on the applied potential difference at all, but only on the intensity of incident radiation. The stopping potential does not change with the radiation intensity because the kinetic energy of photoelectrons (see Equation 6.14) does not depend on the radiation intensity.

## EXAMPLE 6.6

## Work Function and Cut-Off Frequency

When a 180-nm light is used in an experiment with an unknown metal, the measured photocurrent drops to zero at potential $-0.80 \mathrm{~V}$. Determine the work function of the metal and its cut-off frequency for the photoelectric effect.

## Strategy

To find the cut-off frequency $f_{c}$, we use Equation 6.15, but first we must find the work function $\phi$. To find $\phi$, we use Equation 6.12 and Equation 6.14. Photocurrent drops to zero at the stopping value of potential, so we identify $\Delta V_{s}=0.8 \mathrm{~V}$.

## Solution

We use Equation 6.12 to find the kinetic energy of the photoelectrons:

$$
K_{\max }=e \Delta V_{s}=e(0.80 \mathrm{~V})=0.80 \mathrm{eV}
$$

Now we solve Equation 6.14 for $\phi$ :

$$
\phi=h f-K_{\max }=\frac{h c}{\lambda}-K_{\max }=\frac{1240 \mathrm{eV} \cdot \mathrm{nm}}{180 \mathrm{~nm}}-0.80 \mathrm{eV}=6.09 \mathrm{eV}
$$

Finally, we use Equation 6.15 to find the cut-off frequency:

$$
f_{c}=\frac{\phi}{h}=\frac{6.09 \mathrm{eV}}{4.136 \times 10^{-15} \mathrm{eV} \cdot \mathrm{s}}=1.47 \times 10^{15} \mathrm{~Hz}
$$

## Significance

In calculations like the one shown in this example, it is convenient to use Planck's constant in the units of $\mathrm{eV} \cdot \mathrm{s}$ and express all energies in $\mathrm{eV}$ instead of joules.

## EXAMPLE 6.7

## The Photon Energy and Kinetic Energy of Photoelectrons

A 430-nm violet light is incident on a calcium photoelectrode with a work function of $2.71 \mathrm{eV}$.

Find the energy of the incident photons and the maximum kinetic energy of ejected electrons.

## Strategy

The energy of the incident photon is $E_{f}=h f=h c / \lambda$, where we use $f \lambda=c$. To obtain the maximum energy of the ejected electrons, we use Equation 6.16.

## Solution

$$
E_{f}=\frac{h c}{\lambda}=\frac{1240 \mathrm{eV} \cdot \mathrm{nm}}{430 \mathrm{~nm}}=2.88 \mathrm{eV}, K_{\max }=E_{f}-\phi=2.88 \mathrm{eV}-2.71 \mathrm{eV}=0.17 \mathrm{eV}
$$

## Significance

In this experimental setup, photoelectrons stop flowing at the stopping potential of $0.17 \mathrm{~V}$.

### 6.3 The Compton Effect

Two of Einstein's influential ideas introduced in 1905 were the theory of special relativity and the concept of a light quantum, which we now call a photon. Beyond 1905, Einstein went further to suggest that freely propagating electromagnetic waves consisted of photons that are particles of light in the same sense that electrons or other massive particles are particles of matter. A beam of monochromatic light of wavelength $\lambda$ (or equivalently, of frequency $f$ ) can be seen either as a classical wave or as a collection of photons that travel in a vacuum with one speed, $c$ (the speed of light), and all carrying the same energy, $E_{f}=h f$. This idea proved useful for explaining the interactions of light with particles of matter.

## Momentum of a Photon

Unlike a particle of matter that is characterized by its rest mass $m_{0}$, a photon is massless. In a vacuum, unlike a particle of matter that may vary its speed but cannot reach the speed of light, a photon travels at only one speed, which is exactly the speed of light. From the point of view of Newtonian classical mechanics, these two characteristics imply that a photon should not exist at all. For example, how can we find the linear momentum or kinetic energy of a body whose mass is zero? This apparent paradox vanishes if we describe a photon as a relativistic particle. According to the theory of special relativity, any particle in nature obeys the relativistic energy equation

$$
E^{2}=p^{2} c^{2}+m_{0}^{2} c^{4}
$$

This relation can also be applied to a photon. In Equation 6.17, $E$ is the total energy of a particle, $p$ is its linear momentum, and $m_{0}$ is its rest mass. For a photon, we simply set $m_{0}=0$ in this equation. This leads to the expression for the momentum $p_{f}$ of a photon

$$
p_{f}=\frac{E_{f}}{c}
$$

Here the photon's energy $E_{f}$ is the same as that of a light quantum of frequency $f$, which we introduced to explain the photoelectric effect:

$$
E_{f}=h f=\frac{h c}{\lambda}
$$

The wave relation that connects frequency $f$ with wavelength $\lambda$ and speed $c$ also holds for photons:

$$
\lambda f=c
$$

Therefore, a photon can be equivalently characterized by either its energy and wavelength, or its frequency and momentum. Equation 6.19 and Equation 6.20 can be combined into the explicit relation between a photon's momentum and its wavelength:

$$
p_{f}=\frac{h}{\lambda}
$$

Notice that this equation gives us only the magnitude of the photon's momentum and contains no information about the direction in which the photon is moving. To include the direction, it is customary to write the photon's momentum as a vector:

$$
\overrightarrow{\mathbf{p}}_{f}=\hbar \overrightarrow{\mathbf{k}}
$$

In Equation 6.22, $\hbar=h / 2 \pi$ is the reduced Planck's constant (pronounced "h-bar"), which is just Planck's constant divided by the factor $2 \pi$. Vector $\overrightarrow{\mathbf{k}}$ is called the "wave vector" or propagation vector (the direction in which a photon is moving). The propagation vector shows the direction of the photon's linear momentum vector. The magnitude of the wave vector is $k=|\overrightarrow{\mathbf{k}}|=2 \pi / \lambda$ and is called the wave number. Notice that this
equation does not introduce any new physics. We can verify that the magnitude of the vector in Equation 6.22 is the same as that given by Equation 6.18 .

## The Compton Effect

The Compton effect is the term used for an unusual result observed when X-rays are scattered on some materials. By classical theory, when an electromagnetic wave is scattered off atoms, the wavelength of the scattered radiation is expected to be the same as the wavelength of the incident radiation. Contrary to this prediction of classical physics, observations show that when X-rays are scattered off some materials, such as graphite, the scattered X-rays have different wavelengths from the wavelength of the incident X-rays. This classically unexplainable phenomenon was studied experimentally by Arthur H. Compton and his collaborators, and Compton gave its explanation in 1923.

To explain the shift in wavelengths measured in the experiment, Compton used Einstein's idea of light as a particle. The Compton effect has a very important place in the history of physics because it shows that electromagnetic radiation cannot be explained as a purely wave phenomenon. The explanation of the Compton effect gave a convincing argument to the physics community that electromagnetic waves can indeed behave like a stream of photons, which placed the concept of a photon on firm ground.

The schematics of Compton's experimental setup are shown in Figure 6.11. The idea of the experiment is straightforward: Monochromatic X-rays with wavelength $\lambda$ are incident on a sample of graphite (the "target"), where they interact with atoms inside the sample; they later emerge as scattered X-rays with wavelength $\lambda^{\prime}$. A detector placed behind the target can measure the intensity of radiation scattered in any direction $\theta$ with respect to the direction of the incident $\mathrm{X}$-ray beam. This scattering angle, $\theta$, is the angle between the direction of the scattered beam and the direction of the incident beam. In this experiment, we know the intensity and the wavelength $\lambda$ of the incoming (incident) beam; and for a given scattering angle $\theta$, we measure the intensity and the wavelength $\lambda^{\prime}$ of the outgoing (scattered) beam. Typical results of these measurements are shown in Figure 6.12, where the $x$-axis is the wavelength of the scattered X-rays and the $y$-axis is the intensity of the scattered X-rays, measured for different scattering angles (indicated on the graphs). For all scattering angles (except for $\theta=0^{\circ}$ ), we measure two intensity peaks. One peak is located at the wavelength $\lambda$, which is the wavelength of the incident beam. The other peak is located at some other wavelength, $\lambda^{\prime}$. The two peaks are separated by $\Delta \lambda$, which depends on the scattering angle $\theta$ of the outgoing beam (in the direction of observation). The separation $\Delta \lambda$ is called the Compton shift.

## Compton Shift

As given by Compton, the explanation of the Compton shift is that in the target material, graphite, valence electrons are loosely bound in the atoms and behave like free electrons. Compton assumed that the incident Xray radiation is a stream of photons. An incoming photon in this stream collides with a valence electron in the graphite target. In the course of this collision, the incoming photon transfers some part of its energy and momentum to the target electron and leaves the scene as a scattered photon. This model explains in qualitative terms why the scattered radiation has a longer wavelength than the incident radiation. Put simply, a photon that has lost some of its energy emerges as a photon with a lower frequency, or equivalently, with a longer wavelength. To show that his model was correct, Compton used it to derive the expression for the Compton shift. In his derivation, he assumed that both photon and electron are relativistic particles and that the collision obeys two commonsense principles: (1) the conservation of linear momentum and (2) the conservation of total relativistic energy.

In the following derivation of the Compton shift, $\boldsymbol{E}_{f}$ and $\overrightarrow{\mathbf{p}}_{f}$ denote the energy and momentum, respectively, of an incident photon with frequency $f$. The photon collides with a relativistic electron at rest, which means that immediately before the collision, the electron's energy is entirely its rest mass energy, $m_{0} c^{2}$. Immediately after the collision, the electron has energy $E$ and momentum $\overrightarrow{\mathbf{p}}$, both of which satisfy Equation 6.19.

Immediately after the collision, the outgoing photon has energy $\widetilde{E}_{f}$, momentum $\overrightarrow{\widetilde{\mathbf{p}}}_{f}$, and frequency $f^{\prime}$. The direction of the incident photon is horizontal from left to right, and the direction of the outgoing photon is at the angle $\theta$, as illustrated in Figure 6.11. The scattering angle $\theta$ is the angle between the momentum vectors $\overrightarrow{\mathbf{p}}_{f}$ and $\overrightarrow{\widetilde{\mathbf{p}}}_{f}$, and we can write their scalar product:

$$
\overrightarrow{\mathbf{p}}_{f} \cdot \overrightarrow{\widetilde{\mathbf{p}}}_{f}=p_{f} \widetilde{p}_{f} \cos \theta
$$

Following Compton's argument, we assume that the colliding photon and electron form an isolated system. This assumption is valid for weakly bound electrons that, to a good approximation, can be treated as free particles. Our first equation is the conservation of energy for the photon-electron system:

$$
E_{f}+m_{0} c^{2}=\widetilde{E}_{f}+E
$$

The left side of this equation is the energy of the system at the instant immediately before the collision, and the right side of the equation is the energy of the system at the instant immediately after the collision. Our second equation is the conservation of linear momentum for the photon-electron system where the electron is at rest at the instant immediately before the collision:

$$
\overrightarrow{\mathbf{p}}_{f}=\overrightarrow{\mathbf{p}}_{f}+\overrightarrow{\mathbf{p}}
$$

The left side of this equation is the momentum of the system right before the collision, and the right side of the equation is the momentum of the system right after collision. The entire physics of Compton scattering is contained in these three preceding equations--the remaining part is algebra. At this point, we could jump to the concluding formula for the Compton shift, but it is beneficial to highlight the main algebraic steps that lead to Compton's formula, which we give here as follows.

We start with rearranging the terms in Equation 6.24 and squaring it:

$$
\left[\left(E_{f}-\widetilde{E}_{f}\right)+m_{0} c^{2}\right]^{2}=E^{2}
$$

In the next step, we substitute Equation 6.19 for $E^{2}$, simplify, and divide both sides by $c^{2}$ to obtain

$$
\left(E_{f} / c-\widetilde{E}_{f} / c\right)^{2}+2 m_{0} c\left(E_{f} / c-\widetilde{E}_{f} / c\right)=p^{2}
$$

Now we can use Equation 6.21 to express this form of the energy equation in terms of momenta. The result is

$$
\left(p_{f}-\widetilde{p}_{f}\right)^{2}+2 m_{0} c\left(p_{f}-\widetilde{p}_{f}\right)=p^{2}
$$

To eliminate $p^{2}$, we turn to the momentum equation Equation 6.25, rearrange its terms, and square it to obtain

$$
\left(\overrightarrow{\mathbf{p}}_{f}-\overrightarrow{\widetilde{\mathbf{p}}}_{f}\right)^{2}=p^{2} \text { and }\left(\overrightarrow{\mathbf{p}}_{f}-\overrightarrow{\widetilde{\mathbf{p}}}_{f}\right)^{2}=p_{f}^{2}+\widetilde{p}_{f}^{2}-2 \overrightarrow{\mathbf{p}}_{f} \cdot \overrightarrow{\widetilde{\mathbf{p}}}_{f}
$$

The product of the momentum vectors is given by Equation 6.23. When we substitute this result for $p^{2}$ in Equation 6.26, we obtain the energy equation that contains the scattering angle $\theta$ :

$$
\left(p_{f}-\widetilde{p}_{f}\right)^{2}+2 m_{0} c\left(p_{f}-\widetilde{p}_{f}\right)=p_{f}^{2}+\widetilde{p}_{f}^{2}-2 p_{f} \widetilde{p}_{f} \cos \theta
$$

With further algebra, this result can be simplified to

$$
\frac{1}{\widetilde{p}_{f}}-\frac{1}{p_{f}}=\frac{1}{m_{0} c}(1-\cos \theta)
$$

Now recall Equation 6.21 and write: $1 / \widetilde{p}_{f}=\lambda^{\prime} / h$ and $1 / p_{f}=\lambda / h$. When these relations are substituted into Equation 6.27, we obtain the relation for the Compton shift:

$$
\lambda^{\prime}-\lambda=\frac{h}{m_{0} c}(1-\cos \theta)
$$

The factor $h / m_{0} c$ is called the Compton wavelength of the electron:

$$
\lambda_{c}=\frac{h}{m_{0} c}=0.00243 \mathrm{~nm}=2.43 \mathrm{pm}
$$

Denoting the shift as $\Delta \lambda=\lambda^{\prime}-\lambda$, the concluding result can be rewritten as

$$
\Delta \lambda=\lambda_{c}(1-\cos \theta)
$$

This formula for the Compton shift describes outstandingly well the experimental results shown in Figure 6.12. Scattering data measured for molybdenum, graphite, calcite, and many other target materials are in accord with this theoretical result. The nonshifted peak shown in Figure 6.12 is due to photon collisions with tightly bound inner electrons in the target material. Photons that collide with the inner electrons of the target atoms in fact collide with the entire atom. In this extreme case, the rest mass in Equation 6.29 must be changed to the rest mass of the atom. This type of shift is four orders of magnitude smaller than the shift caused by collisions with electrons and is so small that it can be neglected.

Compton scattering is an example of inelastic scattering, in which the scattered radiation has a longer wavelength than the wavelength of the incident radiation. In today's usage, the term "Compton scattering" is used for the inelastic scattering of photons by free, charged particles. In Compton scattering, treating photons as particles with momenta that can be transferred to charged particles provides the theoretical background to
explain the wavelength shifts measured in experiments; this is the evidence that radiation consists of photons.

## EXAMPLE 6.8

## Compton Scattering

An incident 71-pm X-ray is incident on a calcite target. Find the wavelength of the X-ray scattered at a $30^{\circ}$ angle. What is the largest shift that can be expected in this experiment?

## Strategy

To find the wavelength of the scattered X-ray, first we must find the Compton shift for the given scattering angle, $\theta=30^{\circ}$. We use Equation 6.30. Then we add this shift to the incident wavelength to obtain the scattered wavelength. The largest Compton shift occurs at the angle $\theta$ when $1-\cos \theta$ has the largest value, which is for the angle $\theta=180^{\circ}$.

## Solution

The shift at $\theta=30^{\circ}$ is

$$
\Delta \lambda=\lambda_{c}\left(1-\cos 30^{\circ}\right)=0.134 \lambda_{c}=(0.134)(2.43) \mathrm{pm}=0.325 \mathrm{pm}
$$

This gives the scattered wavelength:

$$
\lambda^{\prime}=\lambda+\Delta \lambda=(71+0.325) \mathrm{pm}=71.325 \mathrm{pm}
$$

The largest shift is

$$
(\Delta \lambda)_{\max }=\lambda_{c}\left(1-\cos 180^{\circ}\right)=2(2.43 \mathrm{pm})=4.86 \mathrm{pm}
$$

## Significance

The largest shift in wavelength is detected for the backscattered radiation; however, most of the photons from the incident beam pass through the target and only a small fraction of photons gets backscattered (typically, less than $5 \%)$. Therefore, these measurements require highly sensitive detectors.

### 6.4 Bohr's Model of the Hydrogen Atom

Historically, Bohr's model of the hydrogen atom is the very first model of atomic structure that correctly explained the radiation spectra of atomic hydrogen. The model has a special place in the history of physics because it introduced an early quantum theory, which brought about new developments in scientific thought and later culminated in the development of quantum mechanics. To understand the specifics of Bohr's model, we must first review the nineteenth-century discoveries that prompted its formulation.

When we use a prism to analyze white light coming from the sun, several dark lines in the solar spectrum are
observed (Figure 6.13). Solar absorption lines are called Fraunhofer lines after Joseph von Fraunhofer, who accurately measured their wavelengths. During 1854-1861, Gustav Kirchhoff and Robert Bunsen discovered that for the various chemical elements, the line emission spectrum of an element exactly matches its line absorption spectrum. The difference between the absorption spectrum and the emission spectrum is explained in Figure 6.14. An absorption spectrum is observed when light passes through a gas. This spectrum appears as black lines that occur only at certain wavelengths on the background of the continuous spectrum of white light (Figure 6.13). The missing wavelengths tell us which wavelengths of the radiation are absorbed by the gas. The emission spectrum is observed when light is emitted by a gas. This spectrum is seen as colorful lines on the black background (see Figure 6.15 and Figure 6.16). Positions of the emission lines tell us which wavelengths of the radiation are emitted by the gas. Each chemical element has its own characteristic emission spectrum. For each element, the positions of its emission lines are exactly the same as the positions of its absorption lines. This means that atoms of a specific element absorb radiation only at specific wavelengths and radiation that does not have these wavelengths is not absorbed by the element at all. This also means that the radiation emitted by atoms of each element has exactly the same wavelengths as the radiation they absorb.

Emission spectra of the elements have complex structures; they become even more complex for elements with higher atomic numbers. The simplest spectrum, shown in Figure 6.15, belongs to the hydrogen atom. Only four lines are visible to the human eye. As you read from right to left in Figure 6.15, these lines are: red (656 $\mathrm{nm})$, called the $\mathrm{H}-\alpha$ line; aqua ( $486 \mathrm{~nm}$ ), blue $(434 \mathrm{~nm})$, and violet $(410 \mathrm{~nm})$. The lines with wavelengths shorter than $400 \mathrm{~nm}$ appear in the ultraviolet part of the spectrum (Figure 6.15, far left) and are invisible to the human eye. There are infinitely many invisible spectral lines in the series for hydrogen.

An empirical formula to describe the positions (wavelengths) $\lambda$ of the hydrogen emission lines in this series was discovered in 1885 by Johann Balmer. It is known as the Balmer formula:

$$
\frac{1}{\lambda}=R_{H}\left(\frac{1}{2^{2}}-\frac{1}{n^{2}}\right)
$$

The constant $R_{\mathrm{H}}=1.09737 \times 10^{7} \mathrm{~m}^{-1}$ is called the Rydberg constant for hydrogen. In Equation 6.31 , the positive integer $n$ takes on values $n=3,4,5,6$ for the four visible lines in this series. The series of emission lines given by the Balmer formula is called the Balmer series for hydrogen. Other emission lines of hydrogen that were discovered in the twentieth century are described by the Rydberg formula, which summarizes all of the experimental data:

$$
\frac{1}{\lambda}=R_{\mathrm{H}}\left(\frac{1}{n_{f}^{2}}-\frac{1}{n_{i}^{2}}\right), \text { where } n_{i}=n_{f}+1, n_{f}+2, n_{f}+3, \ldots
$$

When $n_{f}=1$, the series of spectral lines is called the Lyman series. When $n_{f}=2$, the series is called the Balmer series, and in this case, the Rydberg formula coincides with the Balmer formula. When $n_{f}=3$, the series is called the Paschen series. When $n_{f}=4$, the series is called the Brackett series. When $n_{f}=5$, the series is called the Pfund series. When $n_{f}=6$, we have the Humphreys series. As you may guess, there are infinitely many such spectral bands in the spectrum of hydrogen because $n_{f}$ can be any positive integer number.

The Rydberg formula for hydrogen gives the exact positions of the spectral lines as they are observed in a laboratory; however, at the beginning of the twentieth century, nobody could explain why it worked so well. The Rydberg formula remained unexplained until the first successful model of the hydrogen atom was proposed in 1913.

## EXAMPLE 6.9

## Limits of the Balmer Series

Calculate the longest and the shortest wavelengths in the Balmer series.

## Strategy

We can use either the Balmer formula or the Rydberg formula. The longest wavelength is obtained when $1 / n_{i}$ is largest, which is when $n_{i}=n_{f}+1=3$, because $n_{f}=2$ for the Balmer series. The smallest wavelength is obtained when $1 / n_{i}$ is smallest, which is $1 / n_{i} \rightarrow 0$ when $n_{i} \rightarrow \infty$.

## Solution

The long-wave limit:

$$
\frac{1}{\lambda}=R_{\mathrm{H}}\left(\frac{1}{2^{2}}-\frac{1}{3^{2}}\right)=\left(1.09737 \times 10^{7}\right) \frac{1}{\mathrm{~m}}\left(\frac{1}{4}-\frac{1}{9}\right) \Rightarrow \lambda=656.3 \mathrm{~nm}
$$

The short-wave limit:

$$
\frac{1}{\lambda}=R_{\mathrm{H}}\left(\frac{1}{2^{2}}-0\right)=\left(1.09737 \times 10^{7}\right) \frac{1}{\mathrm{~m}}\left(\frac{1}{4}\right) \Rightarrow \lambda=364.6 \mathrm{~nm}
$$

## Significance

Note that there are infinitely many spectral lines lying between these two limits.

The key to unlocking the mystery of atomic spectra is in understanding atomic structure. Scientists have long known that matter is made of atoms. According to nineteenth-century science, atoms are the smallest indivisible quantities of matter. This scientific belief was shattered by a series of groundbreaking experiments that proved the existence of subatomic particles, such as electrons, protons, and neutrons.

The electron was discovered and identified as the smallest quantity of electric charge by J.J. Thomson in 1897 in his cathode ray experiments, also known as $\beta$-ray experiments: A $\boldsymbol{\beta}$-ray is a beam of electrons. In 1904, Thomson proposed the first model of atomic structure, known as the "plum pudding" model, in which an atom consisted of an unknown positively charged matter with negative electrons embedded in it like plums in a pudding. Around 1900, E. Rutherford, and independently, Paul Ulrich Villard, classified all radiation known at that time as $\alpha$-rays, $\beta$-rays, and $\boldsymbol{\gamma}$-rays (a $\gamma$-ray is a beam of highly energetic photons). In 1907 , Rutherford and Thomas Royds used spectroscopy methods to show that positively charged particles of $\alpha$-radiation (called $\alpha$-particles) are in fact doubly ionized atoms of helium. In 1909, Rutherford, Ernest Marsden, and Hans Geiger used $\alpha$-particles in their famous scattering experiment that disproved Thomson's model (see Linear Momentum and Collisions).

In the Rutherford gold foil experiment (also known as the Geiger-Marsden experiment), $\alpha$-particles were incident on a thin gold foil and were scattered by gold atoms inside the foil (see Types of Collisions). The outgoing particles were detected by a $360^{\circ}$ scintillation screen surrounding the gold target (for a detailed description of the experimental setup, see Linear Momentum and Collisions). When a scattered particle struck the screen, a tiny flash of light (scintillation) was observed at that location. By counting the scintillations seen at various angles with respect to the direction of the incident beam, the scientists could determine what fraction of the incident particles were scattered and what fraction were not deflected at all. If the plum pudding model were correct, there would be no back-scattered $\alpha$-particles. However, the results of the Rutherford experiment showed that, although a sizable fraction of $\alpha$-particles emerged from the foil not scattered at all as though the foil were not in their way, a significant fraction of $\alpha$-particles were back-scattered toward the source. This kind of result was possible only when most of the mass and the entire positive charge of the gold atom were concentrated in a tiny space inside the atom.

In 1911, Rutherford proposed a nuclear model of the atom. In Rutherford's model, an atom contained a positively charged nucleus of negligible size, almost like a point, but included almost the entire mass of the atom. The atom also contained negative electrons that were located within the atom but relatively far away from the nucleus. Ten years later, Rutherford coined the name proton for the nucleus of hydrogen and the name neutron for a hypothetical electrically neutral particle that would mediate the binding of positive protons in the nucleus (the neutron was discovered in 1932 by James Chadwick). Rutherford is credited with the discovery of the atomic nucleus; however, the Rutherford model of atomic structure does not explain the Rydberg formula for the hydrogen emission lines.

Bohr's model of the hydrogen atom, proposed by Niels Bohr in 1913, was the first quantum model that correctly explained the hydrogen emission spectrum. Bohr's model combines the classical mechanics of planetary motion with the quantum concept of photons. Once Rutherford had established the existence of the atomic nucleus, Bohr's intuition that the negative electron in the hydrogen atom must revolve around the positive nucleus became a logical consequence of the inverse-square-distance law of electrostatic attraction. Recall that Coulomb's law describing the attraction between two opposite charges has a similar form to Newton's universal law of gravitation in the sense that the gravitational force and the electrostatic force are both decreasing as $1 / r^{2}$, where $r$ is the separation distance between the bodies. In the same way as Earth revolves around the sun, the negative electron in the hydrogen atom can revolve around the positive nucleus. However, an accelerating charge radiates its energy. Classically, if the electron moved around the nucleus in a planetary fashion, it would be undergoing centripetal acceleration, and thus would be radiating energy that would cause it to spiral down into the nucleus. Such a planetary hydrogen atom would not be stable, which is contrary to what we know about ordinary hydrogen atoms that do not disintegrate. Moreover, the classical motion of the electron is not able to explain the discrete emission spectrum of hydrogen.

To circumvent these two difficulties, Bohr proposed the following three postulates of Bohr's model:

1. The negative electron moves around the positive nucleus (proton) in a circular orbit. All electron orbits are centered at the nucleus. Not all classically possible orbits are available to an electron bound to the nucleus.
2. The allowed electron orbits satisfy the first quantization condition: In the $n$th orbit, the angular momentum $L_{n}$ of the electron can take only discrete values:

$$
L_{n}=n \hbar, \text { where } n=1,2,3, \ldots
$$

This postulate says that the electron's angular momentum is quantized. Denoted by $r_{n}$ and $v_{n}$, respectively, the radius of the $n$th orbit and the electron's speed in it, the first quantization condition can be expressed explicitly as

$$
m_{e} v_{n} r_{n}=n \hbar
$$

3. An electron is allowed to make transitions from one orbit where its energy is $E_{n}$ to another orbit where its energy is $E_{m}$. When an atom absorbs a photon, the electron makes a transition to a higher-energy orbit. When an atom emits a photon, the electron transits to a lower-energy orbit. Electron transitions with the simultaneous photon absorption or photon emission take place instantaneously. The allowed electron transitions satisfy the second quantization condition:

$$
h f=\left|E_{n}-E_{m}\right|
$$

where $h f$ is the energy of either an emitted or an absorbed photon with frequency $f$. The second quantization condition states that an electron's change in energy in the hydrogen atom is quantized.

These three postulates of the early quantum theory of the hydrogen atom allow us to derive not only the Rydberg formula, but also the value of the Rydberg constant and other important properties of the hydrogen atom such as its energy levels, its ionization energy, and the sizes of electron orbits. Note that in Bohr's model, along with two nonclassical quantization postulates, we also have the classical description of the electron as a particle that is subjected to the Coulomb force, and its motion must obey Newton's laws of motion. The hydrogen atom, as an isolated system, must obey the laws of conservation of energy and momentum in the way we know from classical physics. Having this theoretical framework in mind, we are ready to proceed with our analysis.

## Electron Orbits

To obtain the size $r_{n}$ of the electron's $n$th orbit and the electron's speed $v_{n}$ in it, we turn to Newtonian mechanics. As a charged particle, the electron experiences an electrostatic pull toward the positively charged nucleus in the center of its circular orbit. This electrostatic pull is the centripetal force that causes the electron
to move in a circle around the nucleus. Therefore, the magnitude of centripetal force is identified with the magnitude of the electrostatic force:

$$
\frac{m_{e} v_{n}^{2}}{r_{n}}=\frac{1}{4 \pi \varepsilon_{0}} \frac{e^{2}}{r_{n}^{2}}
$$

Here, $e$ denotes the value of the elementary charge. The negative electron and positive proton have the same value of charge, $|q|=e$. When Equation 6.36 is combined with the first quantization condition given by Equation 6.34, we can solve for the speed, $v_{n}$, and for the radius, $r_{n}$ :

$$
\begin{align*}
v_{n} & =\frac{1}{4 \pi \varepsilon_{0}} \frac{e^{2}}{\hbar} \frac{1}{n} \\
r_{n} & =4 \pi \varepsilon_{0} \frac{\hbar^{2}}{m_{e} e^{2}} n^{2}
\end{align*}
$$

Note that these results tell us that the electron's speed as well as the radius of its orbit depend only on the index $n$ that enumerates the orbit because all other quantities in the preceding equations are fundamental constants. We see from Equation 6.38 that the size of the orbit grows as the square of $n$. This means that the second orbit is four times as large as the first orbit, and the third orbit is nine times as large as the first orbit, and so on. We also see from Equation 6.37 that the electron's speed in the orbit decreases as the orbit size increases. The electron's speed is largest in the first Bohr orbit, for $n=1$, which is the orbit closest to the nucleus. The radius of the first Bohr orbit is called the Bohr radius of hydrogen, denoted as $a_{0}$. Its value is obtained by setting $n=1$ in Equation 6.38 :

$$
a_{0}=4 \pi \varepsilon_{0} \frac{\hbar^{2}}{m_{e} e^{2}}=5.29 \times 10^{-11} \mathrm{~m}=0.529 \AA
$$

We can substitute $a_{0}$ in Equation 6.38 to express the radius of the $n$th orbit in terms of $a_{0}$ :

$$
r_{n}=a_{0} n^{2}
$$

This result means that the electron orbits in hydrogen atom are quantized because the orbital radius takes on only specific values of $a_{0}, 4 a_{0}, 9 a_{0}, 16 a_{0}, \ldots$ given by Equation 6.40 , and no other values are allowed.

## Electron Energies

The total energy $E_{n}$ of an electron in the $n$th orbit is the sum of its kinetic energy $K_{n}$ and its electrostatic potential energy $U_{n}$. Utilizing Equation 6.37, we find that

$$
K_{n}=\frac{1}{2} m_{e} v_{n}^{2}=\frac{1}{32 \pi^{2} \varepsilon_{0}^{2}} \frac{m_{e} e^{4}}{\hbar^{2}} \frac{1}{n^{2}}
$$

Recall that the electrostatic potential energy of interaction between two charges $q_{1}$ and $q_{2}$ that are separated by a distance $r_{12}$ is $\left(1 / 4 \pi \varepsilon_{0}\right) q_{1} q_{2} / r_{12}$. Here, $q_{1}=+e$ is the charge of the nucleus in the hydrogen atom (the charge of the proton), $q_{2}=-e$ is the charge of the electron and $r_{12}=r_{n}$ is the radius of the $n$th orbit. Now we use Equation 6.38 to find the potential energy of the electron:

$$
U_{n}=-\frac{1}{4 \pi \varepsilon_{0}} \frac{e^{2}}{r_{n}}=-\frac{1}{16 \pi^{2} \varepsilon_{0}^{2}} \frac{m_{e} e^{4}}{\hbar^{2}} \frac{1}{n^{2}}
$$

The total energy of the electron is the sum of Equation 6.41 and Equation 6.42:

$$
E_{n}=K_{n}+U_{n}=-\frac{1}{32 \pi^{2} \varepsilon_{0}^{2}} \frac{m_{e} e^{4}}{\hbar^{2}} \frac{1}{n^{2}}
$$

Note that the energy depends only on the index $n$ because the remaining symbols in Equation 6.43 are physical constants. The value of the constant factor in Equation 6.43 is

$$
E_{0}=\frac{1}{32 \pi^{2} \varepsilon_{0}^{2}} \frac{m_{e} e^{4}}{\hbar^{2}}=\frac{1}{8 \varepsilon_{0}^{2}} \frac{m_{e} e^{4}}{h^{2}}=2.17 \times 10^{-18} \mathrm{~J}=13.6 \mathrm{eV}
$$

It is convenient to express the electron's energy in the $n$th orbit in terms of this energy, as

$$
E_{n}=-E_{0} \frac{1}{n^{2}}
$$

Now we can see that the electron energies in the hydrogen atom are quantized because they can have only discrete values of $-E_{0},-E_{0} / 4,-E_{0} / 9,-E_{0} / 16, \ldots$ given by Equation 6.45 , and no other energy values are allowed. This set of allowed electron energies is called the energy spectrum of hydrogen (Figure 6.17). The index $n$ that enumerates energy levels in Bohr's model is called the energy quantum number. We identify the energy of the electron inside the hydrogen atom with the energy of the hydrogen atom. Note that the smallest value of energy is obtained for $n=1$, so the hydrogen atom cannot have energy smaller than that. This smallest value of the electron energy in the hydrogen atom is called the ground state energy of the hydrogen atom and its value is

$$
E_{1}=-E_{0}=-13.6 \mathrm{eV}
$$

The hydrogen atom may have other energies that are higher than the ground state. These higher energy states are known as excited energy states of a hydrogen atom.

There is only one ground state, but there are infinitely many excited states because there are infinitely many values of $n$ in Equation 6.45. We say that the electron is in the "first exited state" when its energy is $E_{2}$ (when $n=2$ ), the second excited state when its energy is $E_{3}$ (when $n=3$ ) and, in general, in the $n$th exited state when its energy is $E_{n+1}$. There is no highest-of-all excited state; however, there is a limit to the sequence of excited states. If we keep increasing $n$ in Equation 6.45, we find that the limit is $-\lim E_{0} / n^{2}=0$. In this limit,

$$
n \rightarrow \infty
$$

the electron is no longer bound to the nucleus but becomes a free electron. An electron remains bound in the hydrogen atom as long as its energy is negative. An electron that orbits the nucleus in the first Bohr orbit, closest to the nucleus, is in the ground state, where its energy has the smallest value. In the ground state, the electron is most strongly bound to the nucleus and its energy is given by Equation 6.46. If we want to remove this electron from the atom, we must supply it with enough energy, $E_{\infty}$, to at least balance out its ground state energy $E_{1}:$

$$
E_{\infty}+E_{1}=0 \Rightarrow E_{\infty}=-E_{1}=-\left(-E_{0}\right)=E_{0}=13.6 \mathrm{eV}
$$

The energy that is needed to remove the electron from the atom is called the ionization energy. The ionization energy $E_{\infty}$ that is needed to remove the electron from the first Bohr orbit is called the ionization limit of the

hydrogen atom. The ionization limit in Equation 6.47 that we obtain in Bohr's model agrees with experimental value.

## Spectral Emission Lines of Hydrogen

To obtain the wavelengths of the emitted radiation when an electron makes a transition from the $n$th orbit to the mth orbit, we use the second of Bohr's quantization conditions and Equation 6.45 for energies. The emission of energy from the atom can occur only when an electron makes a transition from an excited state to a lower-energy state. In the course of such a transition, the emitted photon carries away the difference of energies between the states involved in the transition. The transition cannot go in the other direction because the energy of a photon cannot be negative, which means that for emission we must have $E_{n}>E_{m}$ and $n>m$. Therefore, the third of Bohr's postulates gives

$$
h f=\left|E_{n}-E_{m}\right|=E_{n}-E_{m}=-E_{0} \frac{1}{n^{2}}+E_{0} \frac{1}{m^{2}}=E_{0}\left(\frac{1}{m^{2}}-\frac{1}{n^{2}}\right)
$$

Now we express the photon's energy in terms of its wavelength, $h f=h c / \lambda$, and divide both sides of Equation 6.48 by $h c$. The result is

$$
\frac{1}{\lambda}=\frac{E_{0}}{h c}\left(\frac{1}{m^{2}}-\frac{1}{n^{2}}\right)
$$

The value of the constant in this equation is

$$
\frac{E_{0}}{h c}=\frac{13.6 \mathrm{eV}}{\left(4.136 \times 10^{-15} \mathrm{eV} \cdot \mathrm{s}\right)\left(2.997 \times 10^{8} \mathrm{~m} / \mathrm{s}\right)}=1.097 \times 10^{7} \frac{1}{\mathrm{~m}}
$$

This value is exactly the Rydberg constant $R_{\mathrm{H}}$ in the Rydberg heuristic formula Equation 6.32. In fact, Equation 6.49 is identical to the Rydberg formula, because for a given $m$, we have $n=m+1, m+2, \ldots$ In this way, the Bohr quantum model of the hydrogen atom allows us to derive the experimental Rydberg constant from first principles and to express it in terms of fundamental constants. Transitions between the allowed electron orbits are illustrated in Figure 6.17.

We can repeat the same steps that led to Equation 6.49 to obtain the wavelength of the absorbed radiation; this again gives Equation 6.49 but this time for the positions of absorption lines in the absorption spectrum of hydrogen. The only difference is that for absorption, the quantum number $m$ is the index of the orbit occupied by the electron before the transition (lower-energy orbit) and the quantum number $n$ is the index of the orbit to which the electron makes the transition (higher-energy orbit). The difference between the electron energies in these two orbits is the energy of the absorbed photon.

## EXAMPLE 6.10

## Size and Ionization Energy of the Hydrogen Atom in an Excited State

If a hydrogen atom in the ground state absorbs a $93.7-\mathrm{nm}$ photon, corresponding to a transition line in the Lyman series, how does this affect the atom's energy and size? How much energy is needed to ionize the atom when it is in this excited state? Give your answers in absolute units, and relative to the ground state.

## Strategy

Before the absorption, the atom is in its ground state. This means that the electron transition takes place from the orbit $m=1$ to some higher $n$th orbit. First, we must determine $n$ for the absorbed wavelength $\lambda=93.7 \mathrm{~nm}$. Then, we can use Equation 6.45 to find the energy $\boldsymbol{E}_{n}$ of the excited state and its ionization energy $\boldsymbol{E}_{\infty, n}$, and use Equation 6.40 to find the radius $r_{n}$ of the atom in the excited state. To estimate $n$, we use Equation 6.49.

## Solution

Substitute $m=1$ and $\lambda=93.7 \mathrm{~nm}$ in Equation 6.49 and solve for $n$. You should not expect to obtain a perfect integer answer because of rounding errors, but your answer will be close to an integer, and you can estimate $n$ by taking the integral part of your answer:

$$
\frac{1}{\lambda}=R_{\mathrm{H}}\left(\frac{1}{1^{2}}-\frac{1}{n^{2}}\right) \Rightarrow n=\frac{1}{\sqrt{1-\frac{1}{\lambda R_{\mathrm{H}}}}}=\frac{1}{\sqrt{1-\frac{1}{\left(93.7 \times 10^{-9} \mathrm{~m}\right)\left(1.097 \times 10^{7} \mathrm{~m}^{-1}\right)}}}=6.07 \Rightarrow n=6
$$

The radius of the $n=6$ orbit is

$$
r_{n}=a_{0} n^{2}=a_{0} 6^{2}=36 a_{0}=36\left(0.529 \times 10^{-10} \mathrm{~m}\right)=19.04 \times 10^{-10} \mathrm{~m} \cong 19.0 \AA
$$

Thus, after absorbing the $93.7-\mathrm{nm}$ photon, the size of the hydrogen atom in the excited $n=6$ state is 36 times larger than before the absorption, when the atom was in the ground state. The energy of the fifth excited state $(n=6)$ is:

$$
E_{n}=-\frac{E_{0}}{n^{2}}=-\frac{E_{0}}{6^{2}}=-\frac{E_{0}}{36}=-\frac{13.6 \mathrm{eV}}{36} \cong-0.378 \mathrm{eV}
$$

After absorbing the $93.7-\mathrm{nm}$ photon, the energy of the hydrogen atom is larger than it was before the absorption. Ionization of the atom when it is in the fifth excited state $(n=6)$ requites 36 times less energy than is needed when the atom is in the ground state:

$$
E_{\infty, 6}=-E_{6}=-(-0.378 \mathrm{eV})=0.378 \mathrm{eV}
$$

## Significance

We can analyze any spectral line in the spectrum of hydrogen in the same way. Thus, the experimental measurements of spectral lines provide us with information about the atomic structure of the hydrogen atom.

Bohr's model of the hydrogen atom also correctly predicts the spectra of some hydrogen-like ions. Hydrogenlike ions are atoms of elements with an atomic number $Z$ larger than one ( $Z=1$ for hydrogen) but with all electrons removed except one. For example, an electrically neutral helium atom has an atomic number $Z=2$. This means it has two electrons orbiting the nucleus with a charge of $q=+Z e$. When one of the orbiting electrons is removed from the helium atom (we say, when the helium atom is singly ionized), what remains is a hydrogen-like atomic structure where the remaining electron orbits the nucleus with a charge of $q=+Z e$. This type of situation is described by the Bohr model. Assuming that the charge of the nucleus is not $+e$ but $+Z e$, we can repeat all steps, beginning with Equation 6.36, to obtain the results for a hydrogen-like ion:

$$
r_{n}=\frac{a_{0}}{Z} n^{2}
$$

where $a_{0}$ is the Bohr orbit of hydrogen, and

$$
E_{n}=-Z^{2} E_{0} \frac{1}{n^{2}}
$$

where $E_{0}$ is the ionization limit of a hydrogen atom. These equations are good approximations as long as the atomic number $Z$ is not too large.

The Bohr model is important because it was the first model to postulate the quantization of electron orbits in atoms. Thus, it represents an early quantum theory that gave a start to developing modern quantum theory. It introduced the concept of a quantum number to describe atomic states. The limitation of the early quantum theory is that it cannot describe atoms in which the number of electrons orbiting the nucleus is larger than one. The Bohr model of hydrogen is a semi-classical model because it combines the classical concept of electron orbits with the new concept of quantization. The remarkable success of this model prompted many physicists to seek an explanation for why such a model should work at all, and to seek an understanding of the physics behind the postulates of early quantum theory. This search brought about the onset of an entirely new concept of "matter waves."

### 6.5 De Broglie's Matter Waves

Compton's formula established that an electromagnetic wave can behave like a particle of light when interacting with matter. In 1924, Louis de Broglie proposed a new speculative hypothesis that electrons and other particles of matter can behave like waves. Today, this idea is known as de Broglie's hypothesis of matter waves. In 1926, De Broglie's hypothesis, together with Bohr's early quantum theory, led to the development of a new theory of wave quantum mechanics to describe the physics of atoms and subatomic particles. Quantum
mechanics has paved the way for new engineering inventions and technologies, such as the laser and magnetic resonance imaging (MRI). These new technologies drive discoveries in other sciences such as biology and chemistry.

According to de Broglie's hypothesis, massless photons as well as massive particles must satisfy one common set of relations that connect the energy $E$ with the frequency $f$, and the linear momentum $p$ with the wavelength $\lambda$. We have discussed these relations for photons in the context of Compton's effect. We are recalling them now in a more general context. Any particle that has energy and momentum is a de Broglie wave of frequency $f$ and wavelength $\lambda$ :

$$
\begin{align*}
& E=h f \\
& \lambda=\frac{h}{p}
\end{align*}
$$

Here, $E$ and $p$ are, respectively, the relativistic energy and the momentum of a particle. De Broglie's relations are usually expressed in terms of the wave vector $\overrightarrow{\mathbf{k}}, k=2 \pi / \lambda$, and the wave frequency $\omega=2 \pi f$, as we usually do for waves:

$$
\begin{align*}
& E=\hbar \omega \\
& 6.55 \\
& \overrightarrow{\mathbf{p}}=\hbar \overrightarrow{\mathbf{k}}
\end{align*}
$$

Wave theory tells us that a wave carries its energy with the group velocity. For matter waves, this group velocity is the velocity $u$ of the particle. Identifying the energy $E$ and momentum $p$ of a particle with its relativistic energy $m c^{2}$ and its relativistic momentum $m u$, respectively, it follows from de Broglie relations that matter waves satisfy the following relation:

$$
\lambda f=\frac{\omega}{k}=\frac{E / \hbar}{p / \hbar}=\frac{E}{p}=\frac{m c^{2}}{m u}=\frac{c^{2}}{u}=\frac{c}{\beta}
$$

where $\beta=u / c$. When a particle is massless we have $u=c$ and Equation 6.57 becomes $\lambda f=c$.

## EXAMPLE 6.11

## How Long Are de Broglie Matter Waves?

Calculate the de Broglie wavelength of: (a) a $0.65-\mathrm{kg}$ basketball thrown at a speed of $10 \mathrm{~m} / \mathrm{s}$, (b) a nonrelativistic electron with a kinetic energy of $1.0 \mathrm{eV}$, and (c) a relativistic electron with a kinetic energy of $108 \mathrm{keV}$.

## Strategy

We use Equation 6.57 to find the de Broglie wavelength. When the problem involves a nonrelativistic object moving with a nonrelativistic speed $u$, such as in (a) when $\beta=u / c \ll 1$, we use nonrelativistic momentum $p$. When the nonrelativistic approximation cannot be used, such as in (c), we must use the relativistic momentum $p=m u=m_{0} \gamma u=E_{0} \gamma \beta / c$, where the rest mass energy of a particle is $E_{0}=m c^{2}$ and $\gamma$ is the Lorentz factor $\gamma=1 / \sqrt{1-\beta^{2}}$. The total energy $E$ of a particle is given by Equation 6.53 and the kinetic energy is $K=E-E_{0}=(\gamma-1) E_{0}$. When the kinetic energy is known, we can invert Equation 6.18 to find the momentum $p=\sqrt{\left(E^{2}-E_{0}^{2}\right) / c^{2}}=\sqrt{K\left(K+2 E_{0}\right)} / c$ and substitute in Equation 6.57 to obtain

$$
\lambda=\frac{h}{p}=\frac{h c}{\sqrt{K\left(K+2 E_{0}\right)}}
$$

Depending on the problem at hand, in this equation we can use the following values for $h c$ :
$h c=\left(6.626 \times 10^{-34} \mathrm{~J} \cdot \mathrm{s}\right)\left(2.998 \times 10^{8} \mathrm{~m} / \mathrm{s}\right)=1.986 \times 10^{-25} \mathrm{~J} \cdot \mathrm{m}=1.241 \mathrm{eV} \cdot \mu \mathrm{m}$

## Solution

a. For the basketball, the kinetic energy is

$$
K=m u^{2} / 2=(0.65 \mathrm{~kg})(10 \mathrm{~m} / \mathrm{s})^{2} / 2=32.5 \mathrm{~J}
$$

and the rest mass energy is

$$
E_{0}=m c^{2}=(0.65 \mathrm{~kg})\left(2.998 \times 10^{8} \mathrm{~m} / \mathrm{s}\right)^{2}=5.84 \times 10^{16} \mathrm{~J}
$$

We see that $K /\left(K+E_{0}\right) \ll 1$ and use $p=m u=(0.65 \mathrm{~kg})(10 \mathrm{~m} / \mathrm{s})=6.5 \mathrm{~J} \cdot \mathrm{s} / \mathrm{m}$ :

$$
\lambda=\frac{h}{p}=\frac{6.626 \times 10^{-34} \mathrm{~J} \cdot \mathrm{s}}{6.5 \mathrm{~J} \cdot \mathrm{s} / \mathrm{m}}=1.02 \times 10^{-34} \mathrm{~m}
$$

b. For the nonrelativistic electron,

$$
E_{0}=m c^{2}=\left(9.109 \times 10^{-31} \mathrm{~kg}\right)\left(2.998 \times 10^{8} \mathrm{~m} / \mathrm{s}\right)^{2}=511 \mathrm{keV}
$$

and when $K=1.0 \mathrm{eV}$, we have $K /\left(K+E_{0}\right)=(1 / 512) \times 10^{-3} \ll 1$, so we can use the nonrelativistic formula. However, it is simpler here to use Equation 6.58:

$$
\lambda=\frac{h}{p}=\frac{h c}{\sqrt{K\left(K+2 E_{0}\right)}}=\frac{1.241 \mathrm{eV} \cdot \mu \mathrm{m}}{\sqrt{(1.0 \mathrm{eV})[1.0 \mathrm{eV}+2(511 \mathrm{keV})]}}=1.23 \mathrm{~nm}
$$

If we use nonrelativistic momentum, we obtain the same result because $1 \mathrm{eV}$ is much smaller than the rest mass of the electron.

c. For a fast electron with $K=108 \mathrm{keV}$, relativistic effects cannot be neglected because its total energy is $E=K+E_{0}=108 \mathrm{keV}+511 \mathrm{keV}=619 \mathrm{keV}$ and $K / E=108 / 619$ is not negligible:

$$
\lambda=\frac{h}{p}=\frac{h c}{\sqrt{K\left(K+2 E_{0}\right)}}=\frac{1.241 \mathrm{eV} \cdot \mu \mathrm{m}}{\sqrt{108 \mathrm{keV}[108 \mathrm{keV}+2(511 \mathrm{keV})]}}=3.55 \mathrm{pm}
$$

## Significance

We see from these estimates that De Broglie's wavelengths of macroscopic objects such as a ball are immeasurably small. Therefore, even if they exist, they are not detectable and do not affect the motion of macroscopic objects.

Using the concept of the electron matter wave, de Broglie provided a rationale for the quantization of the electron's angular momentum in the hydrogen atom, which was postulated in Bohr's quantum theory. The physical explanation for the first Bohr quantization condition comes naturally when we assume that an electron in a hydrogen atom behaves not like a particle but like a wave. To see it clearly, imagine a stretched guitar string that is clamped at both ends and vibrates in one of its normal modes. If the length of the string is $l$ (Figure 6.18), the wavelengths of these vibrations cannot be arbitrary but must be such that an integer $k$ number of half-wavelengths $\lambda / 2$ fit exactly on the distance $l$ between the ends. This is the condition $l=k \lambda / 2$ for a standing wave on a string. Now suppose that instead of having the string clamped at the walls, we bend its length into a circle and fasten its ends to each other. This produces a circular string that vibrates in normal modes, satisfying the same standing-wave condition, but the number of half-wavelengths must now be an even number $k, k=2 n$, and the length $l$ is now connected to the radius $r_{n}$ of the circle. This means that the radii are not arbitrary but must satisfy the following standing-wave condition:

$$
2 \pi r_{n}=2 n \frac{\lambda}{2}
$$

If an electron in the $n$th Bohr orbit moves as a wave, by Equation 6.59 its wavelength must be equal to $\lambda=2 \pi r_{n} / n$. Assuming that Equation 6.58 is valid, the electron wave of this wavelength corresponds to the
electron's linear momentum, $p=h / \lambda=n h /\left(2 \pi r_{n}\right)=n \hbar / r_{n}$. In a circular orbit, therefore, the electron's angular momentum must be

$$
L_{n}=r_{n} p=r_{n} \frac{n \hbar}{r_{n}}=n \hbar
$$

This equation is the first of Bohr's quantization conditions, given by Equation 6.36. Providing a physical explanation for Bohr's quantization condition is a convincing theoretical argument for the existence of matter waves.

## EXAMPLE 6.12

## The Electron Wave in the Ground State of Hydrogen

Find the de Broglie wavelength of an electron in the ground state of hydrogen.

## Strategy

We combine the first quantization condition in Equation 6.60 with Equation 6.36 and use Equation 6.38 for the first Bohr radius with $n=1$.

## Solution

When $n=1$ and $r_{n}=a_{0}=0.529 \AA$, the Bohr quantization condition gives $a_{0} p=1 \cdot \hbar \Rightarrow p=\hbar / a_{0}$. The electron wavelength is:

$$
\lambda=h / p=h / \hbar / a_{0}=2 \pi a_{0}=2 \pi(0.529 \AA)=3.324 \AA
$$

## Significance

We obtain the same result when we use Equation 6.58 directly.

Experimental confirmation of matter waves came in 1927 when C. Davisson and L. Germer performed a series of electron-scattering experiments that clearly showed that electrons do behave like waves. Davisson and Germer did not set up their experiment to confirm de Broglie's hypothesis: The confirmation came as a byproduct of their routine experimental studies of metal surfaces under electron bombardment.

In the particular experiment that provided the very first evidence of electron waves (known today as the Davisson-Germer experiment), they studied a surface of nickel. Their nickel sample was specially prepared
in a high-temperature oven to change its usual polycrystalline structure to a form in which large single-crystal domains occupy the volume. Figure 6.19 shows the experimental setup. Thermal electrons are released from a heated element (usually made of tungsten) in the electron gun and accelerated through a potential difference $\Delta V$, becoming a well-collimated beam of electrons produced by an electron gun. The kinetic energy $K$ of the electrons is adjusted by selecting a value of the potential difference in the electron gun. This produces a beam of electrons with a set value of linear momentum, in accordance with the conservation of energy:

$$
e \Delta V=K=\frac{p^{2}}{2 m} \Rightarrow p=\sqrt{2 m e \Delta V}
$$

The electron beam is incident on the nickel sample in the direction normal to its surface. At the surface, it scatters in various directions. The intensity of the beam scattered in a selected direction $\varphi$ is measured by a highly sensitive detector. The detector's angular position with respect to the direction of the incident beam can be varied from $\varphi=0^{\circ}$ to $\varphi=90^{\circ}$. The entire setup is enclosed in a vacuum chamber to prevent electron collisions with air molecules, as such thermal collisions would change the electrons' kinetic energy and are not desirable.

When the nickel target has a polycrystalline form with many randomly oriented microscopic crystals, the incident electrons scatter off its surface in various random directions. As a result, the intensity of the scattered electron beam is much the same in any direction, resembling a diffuse reflection of light from a porous surface. However, when the nickel target has a regular crystalline structure, the intensity of the scattered electron beam shows a clear maximum at a specific angle and the results show a clear diffraction pattern (see Figure 6.20). Similar diffraction patterns formed by X-rays scattered by various crystalline solids were studied in 1912 by father-and-son physicists William H. Bragg and William L. Bragg. The Bragg law in X-ray crystallography provides a connection between the wavelength $\lambda$ of the radiation incident on a crystalline lattice, the lattice spacing, and the position of the interference maximum in the diffracted radiation (see Diffraction).

The lattice spacing of the Davisson-Germer target, determined with X-ray crystallography, was measured to be $a=2.15$ Å. Unlike X-ray crystallography in which X-rays penetrate the sample, in the original Davisson-Germer experiment, only the surface atoms interact with the incident electron beam. For the surface diffraction, the maximum intensity of the reflected electron beam is observed for scattering angles that satisfy the condition $n \lambda=a \sin \varphi$ (see Figure 6.21). The first-order maximum (for $n=1$ ) is measured at a scattering angle of $\varphi \approx 50^{\circ}$ at $\Delta V \approx 54 \mathrm{~V}$, which gives the wavelength of the incident radiation as $\lambda=(2.15 \AA) \sin 50^{\circ}=1.64 \AA$. On the other hand, a $54-\mathrm{V}$ potential accelerates the incident electrons to kinetic energies of $K=54 \mathrm{eV}$. Their momentum, calculated from Equation 6.61, is $p=2.478 \times 10^{-5} \mathrm{eV} \cdot \mathrm{s} / \mathrm{m}$. When we substitute this result in Equation 6.58, the de Broglie wavelength is obtained as

$$
\lambda=\frac{h}{p}=\frac{4.136 \times 10^{-15} \mathrm{eV} \cdot \mathrm{s}}{2.478 \times 10^{-5} \mathrm{eV} \cdot \mathrm{s} / \mathrm{m}}=1.67 \AA
$$

The same result is obtained when we use $K=54 \mathrm{eV}$ in Equation 6.61. The proximity of this theoretical result to the Davisson-Germer experimental value of $\lambda=1.64 \AA$ is a convincing argument for the existence of de Broglie matter waves.

Diffraction lines measured with low-energy electrons, such as those used in the Davisson-Germer experiment, are quite broad (see Figure 6.20) because the incident electrons are scattered only from the surface. The resolution of diffraction images greatly improves when a higher-energy electron beam passes through a thin metal foil. This occurs because the diffraction image is created by scattering off many crystalline planes inside the volume, and the maxima produced in scattering at Bragg angles are sharp (see Figure 6.22).

Since the work of Davisson and Germer, de Broglie's hypothesis has been extensively tested with various experimental techniques, and the existence of de Broglie waves has been confirmed for numerous elementary particles. Neutrons have been used in scattering experiments to determine crystalline structures of solids from interference patterns formed by neutron matter waves. The neutron has zero charge and its mass is comparable with the mass of a positively charged proton. Both neutrons and protons can be seen as matter waves. Therefore, the property of being a matter wave is not specific to electrically charged particles but is true of all particles in motion. Matter waves of molecules as large as carbon $C_{60}$ have been measured. All physical objects, small or large, have an associated matter wave as long as they remain in motion. The universal character of de Broglie matter waves is firmly established.

## EXAMPLE 6.13

## Neutron Scattering

Suppose that a neutron beam is used in a diffraction experiment on a typical crystalline solid. Estimate the kinetic energy of a neutron (in $\mathrm{eV}$ ) in the neutron beam and compare it with kinetic energy of an ideal gas in equilibrium at room temperature.

## Strategy

We assume that a typical crystal spacing $a$ is of the order of $1.0 \AA$. To observe a diffraction pattern on such a lattice, the neutron wavelength $\lambda$ must be on the same order of magnitude as the lattice spacing. We use Equation 6.61 to find the momentum $p$ and kinetic energy $K$. To compare this energy with the energy $E_{T}$ of ideal gas in equilibrium at room temperature $T=300 \mathrm{~K}$, we use the relation $K=3 / 2 k_{B} T$, where $k_{B}=8.62 \times 10^{-5} \mathrm{eV} / \mathrm{K}$ is the Boltzmann constant.

## Solution

We evaluate $p c$ to compare it with the neutron's rest mass energy $E_{0}=940 \mathrm{MeV}$ :

$$
p=\frac{h}{\lambda} \Rightarrow p c=\frac{h c}{\lambda}=\frac{1.241 \times 10^{-6} \mathrm{eV} \cdot \mathrm{m}}{10^{-10} \mathrm{~m}}=12.41 \mathrm{keV}
$$

We see that $p^{2} c^{2} \ll E_{0}^{2}$ so $K \ll E_{0}$ and we can use the nonrelativistic kinetic energy:

$$
K=\frac{p^{2}}{2 m_{n}}=\frac{h^{2}}{2 \lambda^{2} m_{n}}=\frac{\left(6.63 \times 10^{-34} \mathrm{~J} \cdot \mathrm{s}\right)^{2}}{\left(2 \times 10^{-20} \mathrm{~m}^{2}\right)\left(1.66 \times 10^{-27} \mathrm{~kg}\right)}=1.32 \times 10^{-20} \mathrm{~J}=82.7 \mathrm{meV}
$$

Kinetic energy of ideal gas in equilibrium at $300 \mathrm{~K}$ is:

$$
K_{T}=\frac{3}{2} k_{B} T=\frac{3}{2}\left(8.62 \times 10^{-5} \mathrm{eV} / \mathrm{K}\right)(300 \mathrm{~K})=38.8 \mathrm{MeV}
$$

We see that these energies are of the same order of magnitude.

## Significance

Neutrons with energies in this range, which is typical for an ideal gas at room temperature, are called "thermal neutrons."

## EXAMPLE 6.14

## Wavelength of a Relativistic Proton

In a supercollider at CERN, protons can be accelerated to velocities of $0.75 c$. What are their de Broglie wavelengths at this speed? What are their kinetic energies?

## Strategy

The rest mass energy of a proton is $E_{0}=m_{0} c^{2}=\left(1.672 \times 10^{-27} \mathrm{~kg}\right)\left(2.998 \times 10^{8} \mathrm{~m} / \mathrm{s}\right)^{2}=938 \mathrm{MeV}$. When the proton's velocity is known, we have $\beta=0.75$ and $\beta \gamma=0.75 / \sqrt{1-0.75^{2}}=1.134$. We obtain the wavelength $\lambda$ and kinetic energy $K$ from relativistic relations.

## Solution

$$
\begin{gathered}
\lambda=\frac{h}{p}=\frac{h c}{p c}=\frac{h c}{\beta \gamma E_{0}}=\frac{1.241 \mathrm{eV} \cdot \mu \mathrm{m}}{1.134(938 \mathrm{MeV})}=1.16 \mathrm{fm} \\
K=E_{0}(\gamma-1)=938 \mathrm{MeV}\left(1 / \sqrt{1-0.75^{2}}-1\right)=480.1 \mathrm{MeV}
\end{gathered}
$$

## Significance

Notice that because a proton is 1835 times more massive than an electron, if this experiment were performed with electrons, a simple rescaling of these results would give us the electron's wavelength of $(1835) 0.77 \mathrm{fm}=1.4 \mathrm{pm}$ and its kinetic energy of $480.1 \mathrm{MeV} / 1835=261.6 \mathrm{keV}$.

### 6.6 Wave-Particle Duality

The energy of radiation detected by a radio-signal receiving antenna comes as the energy of an electromagnetic wave. The same energy of radiation detected by a photocurrent in the photoelectric effect comes as the energy of individual photon particles. Therefore, the question arises about the nature of electromagnetic radiation: Is a photon a wave or is it a particle? Similar questions may be asked about other
known forms of energy. For example, an electron that forms part of an electric current in a circuit behaves like a particle moving in unison with other electrons inside the conductor. The same electron behaves as a wave when it passes through a solid crystalline structure and forms a diffraction image. Is an electron a wave or is it a particle? The same question can be extended to all particles of matter-elementary particles, as well as compound molecules-asking about their true physical nature. At our present state of knowledge, such questions about the true nature of things do not have conclusive answers. All we can say is that wave-particle duality exists in nature: Under some experimental conditions, a particle appears to act as a particle, and under different experimental conditions, a particle appears to act a wave. Conversely, under some physical circumstances electromagnetic radiation acts as a wave, and under other physical circumstances, radiation acts as a beam of photons.

This dualistic interpretation is not a new physics concept brought about by specific discoveries in the twentieth century. It was already present in a debate between Isaac Newton and Christiaan Huygens about the nature of light, beginning in the year 1670. According to Newton, a beam of light is a collection of corpuscles of light. According to Huygens, light is a wave. The corpuscular hypothesis failed in 1803, when Thomas Young announced his double-slit interference experiment with light (see Figure 6.23), which firmly established light as a wave. In James Clerk Maxwell's theory of electromagnetism (completed by the year 1873), light is an electromagnetic wave. Maxwell's classical view of radiation as an electromagnetic wave is still valid today; however, it is unable to explain blackbody radiation and the photoelectric effect, where light acts as a beam of photons.

A similar dichotomy existed in the interpretation of electricity. From Benjamin Franklin's observations of electricity in 1751 until J.J. Thomson's discovery of the electron in 1897, electric current was seen as a flow in a continuous electric medium. Within this theory of electric fluid, the present theory of electric circuits was developed, and electromagnetism and electromagnetic induction were discovered. Thomson's experiment showed that the unit of negative electric charge (an electron) can travel in a vacuum without any medium to carry the charge around, as in electric circuits. This discovery changed the way in which electricity is understood today and gave the electron its particle status. In Bohr's early quantum theory of the hydrogen atom, both the electron and the proton are particles of matter. Likewise, in the Compton scattering of X-rays on
electrons, the electron is a particle. On the other hand, in electron-scattering experiments on crystalline structures, the electron behaves as a wave.

A skeptic may raise a question that perhaps an electron might always be nothing more than a particle, and that the diffraction images obtained in electron-scattering experiments might be explained within some macroscopic model of a crystal and a macroscopic model of electrons coming at it like a rain of ping-pong balls. As a matter of fact, to investigate this question, we do not need a complex model of a crystal but just a couple of simple slits in a screen that is opaque to electrons. In other words, to gather convincing evidence about the nature of an electron, we need to repeat the Young double-slit experiment with electrons. If the electron is a wave, we should observe the formation of interference patterns typical for waves, such as those described in Figure 6.23, even when electrons come through the slits one by one. However, if the electron is a not a wave but a particle, the interference fringes will not be formed.

The very first double-slit experiment with a beam of electrons, performed by Claus Jönsson in Germany in 1961, demonstrated that a beam of electrons indeed forms an interference pattern, which means that electrons collectively behave as a wave. The first double-slit experiments with single electrons passing through the slits one-by-one were performed by Giulio Pozzi in 1974 in Italy and by Akira Tonomura in 1989 in Japan. They show that interference fringes are formed gradually, even when electrons pass through the slits individually. This demonstrates conclusively that electron-diffraction images are formed because of the wave nature of electrons. The results seen in double-slit experiments with electrons are illustrated by the images of the interference pattern in Figure 6.24.

## EXAMPLE 6.15

## Double-Slit Experiment with Electrons

In one experimental setup for studying interference patterns of electron waves, two slits are created in a goldcoated silicon membrane. Each slit is $62-\mathrm{nm}$ wide and 4- $\mu \mathrm{m}$ long, and the separation between the slits is 272 $\mathrm{nm}$. The electron beam is created in an electron gun by heating a tungsten element and by accelerating the electrons across a 600-V potential. The beam is subsequently collimated using electromagnetic lenses, and the collimated beam of electrons is sent through the slits. Find the angular position of the first-order bright fringe on the viewing screen.

## Strategy

Recall that the angular position $\theta$ of the $n$th order bright fringe that is formed in Young's two-slit interference pattern (discussed in a previous chapter) is related to the separation, $d$, between the slits and to the wavelength, $\lambda$, of the incident light by the equation $d \sin \theta=n \lambda$, where $n=0, \pm 1, \pm 2, \ldots$. The separation is given and is equal to $d=272 \mathrm{~nm}$. For the first-order fringe, we take $n=1$. The only thing we now need is the wavelength of the incident electron wave.

Since the electron has been accelerated from rest across a potential difference of $\Delta V=600 \mathrm{~V}$, its kinetic energy is $K=e \Delta V=600 \mathrm{eV}$. The rest-mass energy of the electron is $E_{0}=511 \mathrm{keV}$.

We compute its de Broglie wavelength as that of a nonrelativistic electron because its kinetic energy $K$ is much smaller than its rest energy $E_{0}, K \ll E_{0}$.

## Solution

The electron's wavelength is

$$
\lambda=\frac{h}{p}=\frac{h}{\sqrt{2 m_{e} K}}=\frac{h}{\sqrt{2 E_{0} / c^{2} K}}=\frac{h c}{\sqrt{2 E_{0} K}}=\frac{1.241 \times 10^{-6} \mathrm{eV} \cdot \mathrm{m}}{\sqrt{2(511 \mathrm{keV})(600 \mathrm{eV})}}=0.050 \mathrm{~nm}
$$

This $\lambda$ is used to obtain the position of the first bright fringe:

$$
\sin \theta=\frac{1 \cdot \lambda}{d}=\frac{0.050 \mathrm{~nm}}{272 \mathrm{~nm}}=0.000184 \Rightarrow \theta=0.010^{\circ}
$$

## Significance

Notice that this is also the angular resolution between two consecutive bright fringes up to about $n=1000$. For example, between the zero-order fringe and the first-order fringe, between the first-order fringe and the second-order fringe, and so on.

The wave-particle dual nature of matter particles and of radiation is a declaration of our inability to describe physical reality within one unified classical theory because separately neither a classical particle approach nor a classical wave approach can fully explain the observed phenomena. This limitation of the classical approach was realized by the year 1928, and a foundation for a new statistical theory, called quantum mechanics, was put in place by Bohr, Edwin Schrödinger, Werner Heisenberg, and Paul Dirac. Quantum mechanics takes de Broglie's idea of matter waves to be the fundamental property of all particles and gives it a statistical interpretation. According to this interpretation, a wave that is associated with a particle carries information about the probable positions of the particle and about its other properties. A single particle is seen as a moving wave packet such as the one shown in Figure 6.25. We can intuitively sense from this example that if a particle is a wave packet, we will not be able to measure its exact position in the same sense as we cannot pinpoint a location of a wave packet in a vibrating guitar string. The uncertainty, $\Delta x$, in measuring the particle's position is connected to the uncertainty, $\Delta p$, in the simultaneous measuring of its linear momentum by Heisenberg's uncertainty principle:

$$
\Delta x \Delta p \geq \frac{1}{2} \hbar
$$

Heisenberg's principle expresses the law of nature that, at the quantum level, our perception is limited. For example, if we know the exact position of a body (which means that $\Delta x=0$ in Equation 6.63) at the same time we cannot know its momentum, because then the uncertainty in its momentum becomes infinite (because $\Delta p \geq 0.5 \hbar / \Delta x$ in Equation 6.63). The Heisenberg uncertainty principle sets the limit on the precision of simultaneous measurements of position and momentum of a particle; it shows that the best precision we can obtain is when we have an equals sign (=) in Equation 6.63, and we cannot do better than that, even with the best instruments of the future. Heisenberg's principle is a consequence of the wave nature of particles.

We routinely use many electronic devices that exploit wave-particle duality without even realizing the sophistication of the physics underlying their operation. One example of a technology based on the particle properties of photons and electrons is a charge-coupled device, which is used for light detection in any instrumentation where high-quality digital data are required, such as in digital cameras or in medical sensors. An example in which the wave properties of electrons is exploited is an electron microscope.

In 1931, physicist Ernst Ruska-building on the idea that magnetic fields can direct an electron beam just as lenses can direct a beam of light in an optical microscope-developed the first prototype of the electron microscope. This development originated the field of electron microscopy. In the transmission electron microscope (TEM), shown in Figure 6.26, electrons are produced by a hot tungsten element and accelerated by a potential difference in an electron gun, which gives them up to $400 \mathrm{keV}$ in kinetic energy. After leaving the electron gun, the electron beam is focused by electromagnetic lenses (a system of condensing lenses) and transmitted through a specimen sample to be viewed. The image of the sample is reconstructed from the transmitted electron beam. The magnified image may be viewed either directly on a fluorescent screen or indirectly by sending it, for example, to a digital camera or a computer monitor. The entire setup consisting of the electron gun, the lenses, the specimen, and the fluorescent screen are enclosed in a vacuum chamber to prevent the energy loss from the beam. Resolution of the TEM is limited only by spherical aberration (discussed in a previous chapter). Modern high-resolution models of a TEM can have resolving power greater than $0.5 \AA$ and magnifications higher than 50 million times. For comparison, the best resolving power obtained with light microscopy is currently about $97 \mathrm{~nm}$. A limitation of the TEM is that the samples must be about $100-\mathrm{nm}$ thick and biological samples require a special preparation involving chemical "fixing" to stabilize them for ultrathin slicing.

Such limitations do not appear in the scanning electron microscope (SEM), which was invented by Manfred von Ardenne in 1937. In an SEM, a typical energy of the electron beam is up to $40 \mathrm{keV}$ and the beam is not transmitted through a sample but is scattered off its surface. Surface topography of the sample is reconstructed by analyzing back-scattered electrons, transmitted electrons, and the emitted radiation produced by electrons interacting with atoms in the sample. The resolving power of an SEM is better than 1 $\mathrm{nm}$, and the magnification can be more than 250 times better than that obtained with a light microscope. The samples scanned by an SEM can be as large as several centimeters but they must be specially prepared, depending on electrical properties of the sample.

High magnifications of the TEM and SEM allow us to see individual molecules. High resolving powers of the TEM and SEM allow us to see fine details, such as those shown in the SEM micrograph of pollen at the beginning of this chapter (Figure 6.1).

## EXAMPLE 6.16

## Resolving Power of an Electron Microscope

If a 1.0-pm electron beam of a TEM passes through a $2.0-\mu \mathrm{m}$ circular opening, what is the angle between the two just-resolvable point sources for this microscope?

## Solution

We can directly use a formula for the resolving power, $\Delta \theta$, of a microscope (discussed in a previous chapter) when the wavelength of the incident radiation is $\lambda=1.0 \mathrm{pm}$ and the diameter of the aperture is $D=2.0 \mu \mathrm{m}$ :

$$
\Delta \theta=1.22 \frac{\lambda}{D}=1.22 \frac{1.0 \mathrm{pm}}{2.0 \mu \mathrm{m}}=6.10 \times 10^{-7} \mathrm{rad}=3.50 \times 10^{-5} \text { degree }
$$

## Significance

Note that if we used a conventional microscope with a $400-\mathrm{nm}$ light, the resolving power would be only $14^{\circ}$, which means that all of the fine details in the image would be blurred.

