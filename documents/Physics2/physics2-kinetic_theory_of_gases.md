# CHAPTER 2 The Kinetic Theory of Gases 

INTRODUCTION Gases are literally all around us-the air that we breathe is a mixture of gases. Other gases include those that make breads and cakes soft, those that make drinks fizzy, and those that burn to heat many homes. Engines and refrigerators depend on the behaviors of gases, as we will see in later chapters.

As we discussed in the preceding chapter, the study of heat and temperature is part of an area of physics known as thermodynamics, in which we require a system to be macroscopic, that is, to consist of a huge number (such as $10^{23}$ ) of molecules. We begin by considering some macroscopic properties of gases: volume, pressure, and temperature. The simple model of a hypothetical "ideal gas" describes these properties of a gas very accurately under many conditions. We move from the ideal gas model to a more widely applicable approximation, called the Van der Waals model.

To understand gases even better, we must also look at them on the microscopic scale of molecules. In gases, the molecules interact weakly, so the microscopic behavior of gases is relatively simple, and they serve as a good introduction to systems of many molecules. The molecular model of gases is called the kinetic theory of gases and is one of the classic examples of a molecular model that explains everyday behavior.

### 2.1 Molecular Model of an Ideal Gas

In this section, we explore the thermal behavior of gases. Our word "gas" comes from the Flemish word meaning "chaos," first used for vapors by the seventeenth-century chemist J. B. van Helmont. The term was more appropriate than he knew, because gases consist of molecules moving and colliding with each other at random. This randomness makes the connection between the microscopic and macroscopic domains simpler for gases than for liquids or solids.

How do gases differ from solids and liquids? Under ordinary conditions, such as those of the air around us, the difference is that the molecules of gases are much farther apart than those of solids and liquids. Because the typical distances between molecules are large compared to the size of a molecule, as illustrated in Figure 2.2, the forces between them are considered negligible, except when they come into contact with each other during collisions. Also, at temperatures well above the boiling temperature, the motion of molecules is fast, and the gases expand rapidly to occupy all of the accessible volume. In contrast, in liquids and solids, molecules are closer together, and the behavior of molecules in liquids and solids is highly constrained by the molecules' interactions with one another. The macroscopic properties of such substances depend strongly on the forces between the molecules, and since many molecules are interacting, the resulting "many-body problems" can be extremely complicated (see Condensed Matter Physics).

## The Gas Laws

In the previous chapter, we saw one consequence of the large intermolecular spacing in gases: Gases are easily compressed. Table 1.2 shows that gases have larger coefficients of volume expansion than either solids or liquids. These large coefficients mean that gases expand and contract very rapidly with temperature changes. We also saw (in the section on thermal expansion) that most gases expand at the same rate or have the same coefficient of volume expansion, $\beta$. This raises a question: Why do all gases act in nearly the same way, when all the various liquids and solids have widely varying expansion rates?

To study how the pressure, temperature, and volume of a gas relate to one another, consider what happens when you pump air into a deflated car tire. The tire's volume first increases in direct proportion to the amount of air injected, without much increase in the tire pressure. Once the tire has expanded to nearly its full size, the tire's walls limit its volume expansion. If we continue to pump air into the tire, the pressure increases. When
the car is driven and the tires flex, their temperature increases, and therefore the pressure increases even further (Figure 2.3).

Figure 2.4 shows data from the experiments of Robert Boyle (1627-1691), illustrating what is now called Boyle's law: At constant temperature and number of molecules, the absolute pressure of a gas and its volume are inversely proportional. (Recall from Fluid Mechanics that the absolute pressure is the true pressure and the gauge pressure is the absolute pressure minus the ambient pressure, typically atmospheric pressure.) The graph in Figure 2.4 displays this relationship as an inverse proportionality of volume to pressure.

Similar is Amonton's or Gay-Lussac's law, which states that at constant volume and number of molecules, the pressure is proportional to the temperature. That law is the basis of the constant-volume gas thermometer, discussed in the previous chapter. (The histories of these laws and the appropriate credit for them are more complicated than can be discussed here.)

It is known experimentally that for gases at low density (such that their molecules occupy a negligible fraction of the total volume) and at temperatures well above the boiling point, these proportionalities hold to a good approximation. Not surprisingly, with the other quantities held constant, either pressure or volume is proportional to the number of molecules. More surprisingly, when the proportionalities are combined into a single equation, the constant of proportionality is independent of the composition of the gas. The resulting equation for all gases applies in the limit of low density and high temperature; it's the same for oxygen as for helium or uranium hexafluoride. A gas at that limit is called an ideal gas; it obeys the ideal gas law, which is also called the equation of state of an ideal gas.

## Ideal Gas Law

The ideal gas law states that

$$
p V=N k_{\mathrm{B}} T
$$

where $p$ is the absolute pressure of a gas, $V$ is the volume it occupies, $N$ is the number of molecules in the gas, and $T$ is its absolute temperature.

The constant $k_{\mathrm{B}}$ is called the Boltzmann constant in honor of the Austrian physicist Ludwig Boltzmann (1844-1906) and has the value

$$
k_{\mathrm{B}}=1.38 \times 10^{-23} \mathrm{~J} / \mathrm{K}
$$

The ideal gas law describes the behavior of any real gas when its density is low enough or its temperature high enough that it is far from liquefaction. This encompasses many practical situations. In the next section, we'll see why it's independent of the type of gas.

2 http://chemed.chem.purdue.edu/genchem/history/charles.html

In many situations, the ideal gas law is applied to a sample of gas with a constant number of molecules; for instance, the gas may be in a sealed container. If $N$ is constant, then solving for $N$ shows that $p V / T$ is constant. We can write that fact in a convenient form:

$$
\frac{p_{1} V_{1}}{T_{1}}=\frac{p_{2} V_{2}}{T_{2}}
$$

where the subscripts 1 and 2 refer to any two states of the gas at different times. Again, the temperature must be expressed in kelvin and the pressure must be absolute pressure, which is the sum of gauge pressure and atmospheric pressure.

## EXAMPLE 2.1

## Calculating Pressure Changes Due to Temperature Changes

Suppose your bicycle tire is fully inflated, with an absolute pressure of $7.00 \times 10^{5} \mathrm{~Pa}$ (a gauge pressure of just under $90.0 \mathrm{lb} / \mathrm{in} .^{2}$ ) at a temperature of $18.0^{\circ} \mathrm{C}$. What is the pressure after its temperature has risen to $35.0^{\circ} \mathrm{C}$ on a hot day? Assume there are no appreciable leaks or changes in volume.

## Strategy

The pressure in the tire is changing only because of changes in temperature. We know the initial pressure $p_{0}=7.00 \times 10^{5} \mathrm{~Pa}$, the initial temperature $T_{0}=18.0^{\circ} \mathrm{C}$, and the final temperature $T_{\mathrm{f}}=35.0^{\circ} \mathrm{C}$. We must find the final pressure $p_{\mathrm{f}}$. Since the number of molecules is constant, we can use the equation

$$
\frac{p_{\mathrm{f}} V_{\mathrm{f}}}{T_{\mathrm{f}}}=\frac{p_{0} V_{0}}{T_{0}}
$$

Since the volume is constant, $V_{\mathrm{f}}$ and $V_{0}$ are the same and they divide out. Therefore,

$$
\frac{p_{\mathrm{f}}}{T_{\mathrm{f}}}=\frac{p_{0}}{T_{0}}
$$

We can then rearrange this to solve for $p_{\mathrm{f}}$ :

$$
p_{\mathrm{f}}=p_{0} \frac{T_{\mathrm{f}}}{T_{0}}
$$

where the temperature must be in kelvin.

## Solution

1. Convert temperatures from degrees Celsius to kelvin

$$
\begin{aligned}
& T_{0}=(18.0+273) \mathrm{K}=291 \mathrm{~K} \\
& T_{\mathrm{f}}=(35.0+273) \mathrm{K}=308 \mathrm{~K}
\end{aligned}
$$

2. Substitute the known values into the equation,

$$
p_{\mathrm{f}}=p_{0} \frac{T_{\mathrm{f}}}{T_{0}}=7.00 \times 10^{5} \mathrm{~Pa}\left(\frac{308 \mathrm{~K}}{291 \mathrm{~K}}\right)=7.41 \times 10^{5} \mathrm{~Pa}
$$

## Significance

The final temperature is about $6 \%$ greater than the original temperature, so the final pressure is about $6 \%$ greater as well. Note that absolute pressure (see Fluid Mechanics) and absolute temperature (see Temperature and Heat) must be used in the ideal gas law.

## EXAMPLE 2.2

## Calculating the Number of Molecules in a Cubic Meter of Gas

How many molecules are in a typical object, such as gas in a tire or water in a glass? This calculation can give us an idea of how large $N$ typically is. Let's calculate the number of molecules in the air that a typical healthy young adult inhales in one breath, with a volume of $500 \mathrm{~mL}$, at standard temperature and pressure (STP), which is defined as $0^{\circ} \mathrm{C}$ and atmospheric pressure. (Our young adult is apparently outside in winter.)

## Strategy

Because pressure, volume, and temperature are all specified, we can use the ideal gas law, $p V=N k_{\mathrm{B}} T$, to find $N$.

## Solution

1. Identify the knowns.

$$
T=0^{\circ} \mathrm{C}=273 \mathrm{~K}, p=1.01 \times 10^{5} \mathrm{~Pa}, V=500 \mathrm{~mL}=5 \times 10^{-4} \mathrm{~m}^{3}, k_{\mathrm{B}}=1.38 \times 10^{-23} \mathrm{~J} / \mathrm{K}
$$

2. Substitute the known values into the equation and solve for $N$.

$$
N=\frac{p V}{k_{\mathrm{B}} T}=\frac{\left(1.01 \times 10^{5} \mathrm{~Pa}\right)\left(5 \times 10^{-4} \mathrm{~m}^{3}\right)}{\left(1.38 \times 10^{-23} \mathrm{~J} / \mathrm{K}\right)(273 \mathrm{~K})}=1.34 \times 10^{22} \text { molecules }
$$

## Significance

$N$ is huge, even in small volumes. For example, $1 \mathrm{~cm}^{3}$ of a gas at STP contains $2.68 \times 10^{19}$ molecules. Once again, note that our result for $N$ is the same for all types of gases, including mixtures.

As we observed in the chapter on fluid mechanics, pascals are $\mathrm{N} / \mathrm{m}^{2}$, so $\mathrm{Pa} \cdot \mathrm{m}^{3}=\mathrm{N} \cdot \mathrm{m}=\mathrm{J}$. Thus, our result for $N$ is dimensionless, a pure number that could be obtained by counting (in principle) rather than measuring. As it is the number of molecules, we put "molecules" after the number, keeping in mind that it is an aid to communication rather than a unit.

## Moles and Avogadro's Number

It is often convenient to measure the amount of substance with a unit on a more human scale than molecules. The SI unit for this purpose was developed by the Italian scientist Amedeo Avogadro (1776-1856). (He worked from the hypothesis that equal volumes of gas at equal pressure and temperature contain equal numbers of molecules, independent of the type of gas. As mentioned above, this hypothesis has been confirmed when the ideal gas approximation applies.) A mole (abbreviated mol) is defined as the amount of any substance that contains as many molecules as there are atoms. (Technically, we should say "formula units," not "molecules," but this distinction is irrelevant for our purposes.) The number of molecules in one mole is called Avogadro's number $\left(N_{\mathrm{A}}\right)$, and the value of Avogadro's number is now known to be

$$
N_{\mathrm{A}}=6.02 \times 10^{23} \mathrm{~mol}^{-1}
$$

We can now write $N=N_{A} n$, where $n$ represents the number of moles of a substance.

Avogadro's number relates the mass of an amount of substance in grams to the number of protons and neutrons in an atom or molecule (12 for a carbon-12 atom), which roughly determine its mass. It's natural to define a unit of mass such that the mass of an atom is approximately equal to its number of neutrons and protons. The unit of that kind accepted for use with the SI is the unified atomic mass unit (u), also called the dalton. Specifically, a carbon-12 atom has a mass of exactly $12 \mathrm{u}$, so that its molar mass $M$ in grams per mole is numerically equal to the mass of one carbon-12 atom in $\mathrm{u}$. That equality holds for any substance. In other words, $N_{\mathrm{A}}$ is not only the conversion from numbers of molecules to moles, but it is also the conversion from $\mathrm{u}$ to grams: $6.02 \times 10^{23} \mathrm{u}=1 \mathrm{~g}$. See Figure 2.6.

Now letting $m_{\mathrm{s}}$ stand for the mass of a sample of a substance, we have $m_{\mathrm{s}}=n M$. Letting $m$ stand for the mass of a molecule, we have $M=N_{A} m$.

## The Ideal Gas Law Restated using Moles

A very common expression of the ideal gas law uses the number of moles in a sample, $n$, rather than the number of molecules, $N$. We start from the ideal gas law,

$$
p V=N k_{\mathrm{B}} T
$$

and multiply and divide the right-hand side of the equation by Avogadro's number $N_{\mathrm{A}}$. This gives us

$$
p V=\frac{N}{N_{\mathrm{A}}} N_{\mathrm{A}} k_{\mathrm{B}} T
$$

Note that $n=N / N_{\mathrm{A}}$ is the number of moles. We define the universal gas constant as $R=N_{\mathrm{A}} k_{\mathrm{B}}$, and obtain the ideal gas law in terms of moles.

## Ideal Gas Law (in terms of moles)

In terms of number of moles $n$, the ideal gas law is written as

$$
p V=n R T
$$

In SI units,

$$
R=N_{\mathrm{A}} k_{\mathrm{B}}=\left(6.02 \times 10^{23} \mathrm{~mol}^{-1}\right)\left(1.38 \times 10^{-23} \frac{\mathrm{J}}{\mathrm{K}}\right)=8.31 \frac{\mathrm{J}}{\mathrm{mol} \cdot \mathrm{K}}
$$

In other units,

$$
R=1.99 \frac{\mathrm{cal}}{\mathrm{mol} \cdot \mathrm{K}}=0.0821 \frac{\mathrm{L} \cdot \mathrm{atm}}{\mathrm{mol} \cdot \mathrm{K}}
$$

You can use whichever value of $R$ is most convenient for a particular problem.

## EXAMPLE 2.3

## Density of Air at STP and in a Hot Air Balloon

Calculate the density of dry air (a) under standard conditions and (b) in a hot air balloon at a temperature of $120^{\circ} \mathrm{C}$. Dry air is approximately $78 \% \mathrm{~N}_{2}, 21 \% \mathrm{O}_{2}$, and $1 \%$ Ar.

## Strategy and Solution

a. We are asked to find the density, or mass per cubic meter. We can begin by finding the molar mass. If we have a hundred molecules, of which 78 are nitrogen, 21 are oxygen, and 1 is argon, the average molecular mass is $\frac{78 m_{\mathrm{N}_{2}}+21 m_{\mathrm{O}_{2}}+m_{\mathrm{Ar}}}{100}$, or the mass of each constituent multiplied by its percentage. The same applies to the molar mass, which therefore is

$$
M=0.78 M_{\mathrm{N}_{2}}+0.21 M_{\mathrm{O}_{2}}+0.01 M_{\mathrm{Ar}}=29.0 \mathrm{~g} / \mathrm{mol}
$$

Now we can find the number of moles per cubic meter. We use the ideal gas law in terms of moles, $p V=n R T$, with $p=1.00 \mathrm{~atm}, T=273 \mathrm{~K}, V=1 \mathrm{~m}^{3}$, and $R=8.31 \mathrm{~J} / \mathrm{mol} \cdot \mathrm{K}$. The most convenient choice for $R$ in this case is $R=8.31 \mathrm{~J} / \mathrm{mol} \cdot \mathrm{K}$ because the known quantities are in SI units:

$$
n=\frac{p V}{R T}=\frac{\left(1.00 \times 10^{5} \mathrm{~Pa}\right)\left(1 \mathrm{~m}^{3}\right)}{(8.31 \mathrm{~J} / \mathrm{mol} \cdot \mathrm{K})(273 \mathrm{~K})}=44.1 \mathrm{~mol}
$$

Then, the mass $m_{\mathrm{s}}$ of that air is

$$
m_{\mathrm{s}}=n M=(44.1 \mathrm{~mol})(29.0 \mathrm{~g} / \mathrm{mol})=1290 \mathrm{~g}=1.28 \mathrm{~kg}
$$

Finally the density of air at STP is

$$
\rho=\frac{m_{\mathrm{s}}}{V}=\frac{1.28 \mathrm{~kg}}{1 \mathrm{~m}^{3}}=1.28 \mathrm{~kg} / \mathrm{m}^{3}
$$

b. The air pressure inside the balloon is still $1 \mathrm{~atm}$ because the bottom of the balloon is open to the atmosphere. The calculation is the same except that we use a temperature of $120^{\circ} \mathrm{C}$, which is $393 \mathrm{~K}$. We can repeat the calculation in (a), or simply observe that the density is proportional to the number of moles, which is inversely proportional to the temperature. Then using the subscripts 1 for air at STP and 2 for the hot air, we have

$$
\rho_{2}=\frac{T_{1}}{T_{2}} \rho_{1}=\frac{273 \mathrm{~K}}{393 \mathrm{~K}}\left(1.28 \mathrm{~kg} / \mathrm{m}^{3}\right)=0.889 \mathrm{~kg} / \mathrm{m}^{3}
$$

## Significance

Using the methods of Archimedes' Principle and Buoyancy, we can find that the net force on $2200 \mathrm{~m}^{3}$ of air at $120^{\circ} \mathrm{C}$ is $F_{b}-F_{g}=\rho_{\text {atmosphere }} V g-\rho_{\text {hot air }} V g=8.49 \times 10^{3} \mathrm{~N}$, or enough to lift about $867 \mathrm{~kg}$. The mass density and molar density of air at STP, found above, are often useful numbers. From the molar density, we can easily determine another useful number, the volume of a mole of any ideal gas at STP, which is $22.4 \mathrm{~L}$.

The ideal gas law is closely related to energy: The units on both sides of the equation are joules. The right-hand side of the ideal gas law equation is $N k_{\mathrm{B}} T$. This term is roughly the total translational kinetic energy (which, when discussing gases, refers to the energy of translation of a molecule, not that of vibration of its atoms or rotation) of $N$ molecules at an absolute temperature $T$, as we will see formally in the next section. The left-hand side of the ideal gas law equation is $p V$. As mentioned in the example on the number of molecules in an ideal gas, pressure multiplied by volume has units of energy. The energy of a gas can be changed when the gas does work as it increases in volume, something we explored in the preceding chapter, and the amount of work is related to the pressure. This is the process that occurs in gasoline or steam engines and turbines, as we'll see
in the next chapter.

## PROBLEM-SOLVING STRATEGY

## The Ideal Gas Law

Step 1. Examine the situation to determine that an ideal gas is involved. Most gases are nearly ideal unless they are close to the boiling point or at pressures far above atmospheric pressure.

Step 2. Make a list of what quantities are given or can be inferred from the problem as stated (identify the known quantities).

Step 3. Identify exactly what needs to be determined in the problem (identify the unknown quantities). A written list is useful.

Step 4. Determine whether the number of molecules or the number of moles is known or asked for to decide whether to use the ideal gas law as $p V=N k_{\mathrm{B}} T$, where $N$ is the number of molecules, or $p V=n R T$, where $n$ is the number of moles.

Step 5. Convert known values into proper SI units (K for temperature, Pa for pressure, $\mathrm{m}^{3}$ for volume, molecules for $N$, and moles for $n$ ). If the units of the knowns are consistent with one of the non-SI values of $R$, you can leave them in those units. Be sure to use absolute temperature and absolute pressure.

Step 6. Solve the ideal gas law for the quantity to be determined (the unknown quantity). You may need to take a ratio of final states to initial states to eliminate the unknown quantities that are kept fixed.

Step 7. Substitute the known quantities, along with their units, into the appropriate equation and obtain numerical solutions complete with units.

Step 8. Check the answer to see if it is reasonable: Does it make sense?

## The Van der Waals Equation of State

We have repeatedly noted that the ideal gas law is an approximation. How can it be improved upon? The van der Waals equation of state (named after the Dutch physicist Johannes van der Waals, 1837-1923) improves it by taking into account two factors. First, the attractive forces between molecules, which are stronger at higher density and reduce the pressure, are taken into account by adding to the pressure a term equal to the square of the molar density multiplied by a positive coefficient a. Second, the volume of the molecules is represented by a positive constant $b$, which can be thought of as the volume of a mole of molecules. This is subtracted from the total volume to give the remaining volume that the molecules can move in. The constants $a$ and $b$ are determined experimentally for each gas. The resulting equation is

$$
\left[p+a\left(\frac{n}{V}\right)^{2}\right](V-n b)=n R T
$$

In the limit of low density (small $n$ ), the $a$ and $b$ terms are negligible, and we have the ideal gas law, as we should for low density. On the other hand, if $V-n b$ is small, meaning that the molecules are very close together, the pressure must be higher to give the same $n R T$, as we would expect in the situation of a highly compressed gas. However, the increase in pressure is less than that argument would suggest, because at high density the $(n / V)^{2}$ term is significant. Since it's positive, it causes a lower pressure to give the same $n R T$.

The van der Waals equation of state works well for most gases under a wide variety of conditions. As we'll see in the next module, it even predicts the gas-liquid transition.

## $p V$ Diagrams

We can examine aspects of the behavior of a substance by plotting a $\boldsymbol{p} \boldsymbol{V}$ diagram, which is a graph of pressure versus volume. When the substance behaves like an ideal gas, the ideal gas law $p V=n R T$ describes the
relationship between its pressure and volume. On a $p V$ diagram, it's common to plot an isotherm, which is a curve showing $p$ as a function of $V$ with the number of molecules and the temperature fixed. Then, for an ideal gas, $p V=$ constant. For example, the volume of the gas decreases as the pressure increases. The resulting graph is a hyperbola.

However, if we assume the van der Waals equation of state, the isotherms become more interesting, as shown in Figure 2.7. At high temperatures, the curves are approximately hyperbolas, representing approximately ideal behavior at various fixed temperatures. At lower temperatures, the curves look less and less like hyperbolas-that is, the gas is not behaving ideally. There is a critical temperature $T_{\mathrm{c}}$ at which the curve has a point with zero slope. Below that temperature, the curves do not decrease monotonically; instead, they each have a "hump," meaning that for a certain range of volume, increasing the volume increases the pressure.

Such behavior would be completely unphysical. Instead, the curves are understood as describing a liquid-gas phase transition. The oscillating part of the curve is replaced by a horizontal line, showing that as the volume increases at constant temperature, the pressure stays constant. That behavior corresponds to boiling and condensation; when a substance is at its boiling temperature for a particular pressure, it can increase in volume as some of the liquid turns to gas, or decrease as some of the gas turns to liquid, without any change in temperature or pressure.

Figure 2.8 shows similar isotherms that are more realistic than those based on the van der Waals equation. The steep parts of the curves to the left of the transition region show the liquid phase, which is almost incompressible-a slight decrease in volume requires a large increase in pressure. The flat parts show the liquid-gas transition; the blue regions that they define represent combinations of pressure and volume where liquid and gas can coexist.

The isotherms above $T_{\mathrm{c}}$ do not go through the liquid-gas transition. Therefore, liquid cannot exist above that temperature, which is the critical temperature (described in the chapter on temperature and heat). At sufficiently low pressure above that temperature, the gas has the density of a liquid but will not condense; the gas is said to be supercritical. At higher pressure, it is solid. Carbon dioxide, for example, has no liquid phase at a temperature above $31.0^{\circ} \mathrm{C}$. The critical pressure is the maximum pressure at which the liquid can exist. The point on the $p V$ diagram at the critical pressure and temperature is the critical point (which you learned about in the chapter on temperature and heat). Table 2.1 lists representative critical temperatures and pressures.

| Substance | Critical temperature |  | Critical pressure |  |
| :--- | :--- | :--- | :--- | :--- |
|  | $\mathrm{K}$ | ${ }^{\circ} \mathrm{C}$ | $\mathrm{Pa}$ | $\mathrm{atm}$ |
| Water | 647.4 | 374.3 | $22.12 \times 10^{6}$ | 219.0 |
| Sulfur dioxide | 430.7 | 157.6 | $7.88 \times 10^{6}$ | 78.0 |
| Ammonia | 405.5 | 132.4 | $11.28 \times 10^{6}$ | 111.7 |
| Carbon dioxide | 304.2 | 31.1 | $7.39 \times 10^{6}$ | 73.2 |
| Oxygen | 154.8 | -118.4 | $5.08 \times 10^{6}$ | 50.3 |
| Nitrogen | 126.2 | -146.9 | $3.39 \times 10^{6}$ | 33.6 |
| Hydrogen | 33.3 | -239.9 | $1.30 \times 10^{6}$ | 12.9 |
| Helium | 5.3 | -267.9 | $0.229 \times 10^{6}$ | 2.27 |

Table 2.1 Critical Temperatures and Pressures for Various Substances

### 2.2 Pressure, Temperature, and RMS Speed

We have examined pressure and temperature based on their macroscopic definitions. Pressure is the force divided by the area on which the force is exerted, and temperature is measured with a thermometer. We can gain a better understanding of pressure and temperature from the kinetic theory of gases, the theory that relates the macroscopic properties of gases to the motion of the molecules they consist of. First, we make two assumptions about molecules in an ideal gas.

1. There is a very large number $N$ of molecules, all identical and each having mass $m$.
2. The molecules obey Newton's laws and are in continuous motion, which is random and isotropic, that is, the same in all directions.

To derive the ideal gas law and the connection between microscopic quantities such as the energy of a typical molecule and macroscopic quantities such as temperature, we analyze a sample of an ideal gas in a rigid container, about which we make two further assumptions:

3. The molecules are much smaller than the average distance between them, so their total volume is much less than that of their container (which has volume V). In other words, we take the Van der Waals constant $b$, the volume of a mole of gas molecules, to be negligible compared to the volume of a mole of gas in the container.
4. The molecules make perfectly elastic collisions with the walls of the container and with each other. Other forces on them, including gravity and the attractions represented by the Van der Waals constant a, are negligible (as is necessary for the assumption of isotropy).

The collisions between molecules do not appear in the derivation of the ideal gas law. They do not disturb the derivation either, since collisions between molecules moving with random velocities give new random velocities. Furthermore, if the velocities of gas molecules in a container are initially not random and isotropic, molecular collisions are what make them random and isotropic.

We make still further assumptions that simplify the calculations but do not affect the result. First, we let the container be a rectangular box. Second, we begin by considering monatomic gases, those whose molecules consist of single atoms, such as helium. Then, we can assume that the atoms have no energy except their translational kinetic energy; for instance, they have neither rotational nor vibrational energy. (Later, we discuss the validity of this assumption for real monatomic gases and dispense with it to consider diatomic and polyatomic gases.)

Figure 2.9 shows a collision of a gas molecule with the wall of a container, so that it exerts a force on the wall (by Newton's third law). These collisions are the source of pressure in a gas. As the number of molecules increases, the number of collisions, and thus the pressure, increases. Similarly, if the average velocity of the molecules is higher, the gas pressure is higher.

In a sample of gas in a container, the randomness of the molecular motion causes the number of collisions of molecules with any part of the wall in a given time to fluctuate. However, because a huge number of molecules collide with the wall in a short time, the number of collisions on the scales of time and space we measure fluctuates by only a tiny, usually unobservable fraction from the average. We can compare this situation to that of a casino, where the outcomes of the bets are random and the casino's takings fluctuate by the minute and the hour. However, over long times such as a year, the casino's takings are very close to the averages expected from the odds. A tank of gas has enormously more molecules than a casino has bettors in a year, and the molecules make enormously more collisions in a second than a casino has bets.

A calculation of the average force exerted by molecules on the walls of the box leads us to the ideal gas law and to the connection between temperature and molecular kinetic energy. (In fact, we will take two averages: one over time to get the average force exerted by one molecule with a given velocity, and then another average over molecules with different velocities.) This approach was developed by Daniel Bernoulli (1700-1782), who is best known in physics for his work on fluid flow (hydrodynamics). Remarkably, Bernoulli did this work before Dalton established the view of matter as consisting of atoms.

Figure 2.10 shows a container full of gas and an expanded view of an elastic collision of a gas molecule with a wall of the container, broken down into components. We have assumed that a molecule is small compared with the separation of molecules in the gas, and that its interaction with other molecules can be ignored. Under these conditions, the ideal gas law is experimentally valid. Because we have also assumed the wall is rigid and the particles are points, the collision is elastic (by conservation of energy-there's nowhere for a particle's kinetic energy to go). Therefore, the molecule's kinetic energy remains constant, and hence, its speed and the magnitude of its momentum remain constant as well. This assumption is not always valid, but the results in the rest of this module are also obtained in models that let the molecules exchange energy and momentum with the wall.

If the molecule's velocity changes in the $x$-direction, its momentum changes from $-m v_{x}$ to $+m v_{x}$. Thus, its change in momentum is $\Delta m v=+m v_{x}-\left(-m v_{x}\right)=2 m v_{x}$. According to the impulse-momentum theorem given in the chapter on linear momentum and collisions, the force exerted on the $i$ th molecule, where $i$ labels the molecules from 1 to $N$, is given by

$$
F_{i}=\frac{\Delta p_{i}}{\Delta t}=\frac{2 m v_{i x}}{\Delta t}
$$

(In this equation alone, $p$ represents momentum, not pressure.) There is no force between the wall and the molecule except while the molecule is touching the wall. During the short time of the collision, the force between the molecule and wall is relatively large, but that is not the force we are looking for. We are looking for the average force, so we take $\Delta t$ to be the average time between collisions of the given molecule with this wall, which is the time in which we expect to find one collision. Let $l$ represent the length of the box in the $x$-direction. Then $\Delta t$ is the time the molecule would take to go across the box and back, a distance 21 , at a speed of $v_{x}$. Thus $\Delta t=2 l / v_{x}$, and the expression for the force becomes

$$
F_{i}=\frac{2 m v_{i x}}{2 l / v_{i x}}=\frac{m v_{i x}^{2}}{l}
$$

This force is due to one molecule. To find the total force on the wall, $F$, we need to add the contributions of all $N$ molecules:

$$
F=\sum_{i=1}^{N} F_{i}=\sum_{i=1}^{N} \frac{m v_{i x}^{2}}{l}=\frac{m}{l} \sum_{i=1}^{N} v_{i x}^{2}
$$

We now use the definition of the average, which we denote with a bar, to find the force:

$$
F=N \frac{m}{l}\left(\frac{1}{N} \sum_{i=1}^{N} v_{i x}^{2}\right)=N \frac{m \bar{v}_{x}^{2}}{l}
$$

We want the force in terms of the speed $v$, rather than the $x$-component of the velocity. Note that the total velocity squared is the sum of the squares of its components, so that

$$
\overline{v^{2}}=\overline{v_{x}^{2}}+\overline{v_{y}^{2}}+\overline{v_{z}^{2}}
$$

With the assumption of isotropy, the three averages on the right side are equal, so

$$
\overline{v^{2}}=3 v_{i x}^{\overline{2}}
$$

Substituting this into the expression for $F$ gives

$$
F=N \frac{m \bar{v}{ }^{2}}{3 l}
$$

The pressure is $F / A$, so we obtain

$$
p=\frac{F}{A}=N \frac{m \overline{v^{2}}}{3 A l}=\frac{N m \overline{v^{2}}}{3 V}
$$

where we used $V=A l$ for the volume. This gives the important result

$$
p V=\frac{1}{3} N m v^{2}
$$

Combining this equation with $p V=N k_{\mathrm{B}} T$ gives

$$
\frac{1}{3} N m v^{2}=N k_{\mathrm{B}} T
$$

We can get the average kinetic energy of a molecule, $\frac{1}{2} m \bar{v}$, from the left-hand side of the equation by dividing out $N$ and multiplying by $3 / 2$.

## Average Kinetic Energy per Molecule

The average kinetic energy of a molecule is directly proportional to its absolute temperature:

$$
\bar{K}=\frac{1}{2} m v^{2}=\frac{3}{2} k_{\mathrm{B}} T
$$

The equation $\bar{K}=\frac{3}{2} k_{\mathrm{B}} T$ is the average kinetic energy per molecule. Note in particular that nothing in this equation depends on the molecular mass (or any other property) of the gas, the pressure, or anything but the temperature. If samples of helium and xenon gas, with very different molecular masses, are at the same temperature, the molecules have the same average kinetic energy.

The internal energy of a thermodynamic system is the sum of the mechanical energies of all of the molecules in it. We can now give an equation for the internal energy of a monatomic ideal gas. In such a gas, the molecules' only energy is their translational kinetic energy. Therefore, denoting the internal energy by $E_{\text {int }}$, we simply have $E_{\text {int }}=N \bar{K}$, or

$$
E_{\text {int }}=\frac{3}{2} N k_{\mathrm{B}} T
$$

Often we would like to use this equation in terms of moles:

$$
E_{\mathrm{int}}=\frac{3}{2} n R T
$$

We can solve $\bar{K}=\frac{1}{2} m \overline{v^{2}}=\frac{3}{2} k_{\mathrm{B}} T$ for a typical speed of a molecule in an ideal gas in terms of temperature to determine what is known as the root-mean-square (rms) speed of a molecule.

## RMS Speed of a Molecule

The root-mean-square (rms) speed of a molecule, or the square root of the average of the square of the speed $\overline{v^{2}}$, is

$$
v_{\mathrm{rms}}=\sqrt{\overline{v^{2}}}=\sqrt{\frac{3 k_{\mathrm{B}} T}{m}}
$$

The rms speed is not the average or the most likely speed of molecules, as we will see in Distribution of Molecular Speeds, but it provides an easily calculated estimate of the molecules' speed that is related to their kinetic energy. Again we can write this equation in terms of the gas constant $R$ and the molar mass $M \mathrm{in} \mathrm{kg} /$ mol:

$$
v_{\mathrm{rms}}=\sqrt{\frac{3 R T}{M}}
$$

We digress for a moment to answer a question that may have occurred to you: When we apply the model to atoms instead of theoretical point particles, does rotational kinetic energy change our results? To answer this question, we have to appeal to quantum mechanics. In quantum mechanics, rotational kinetic energy cannot take on just any value; it's limited to a discrete set of values, and the smallest value is inversely proportional to the rotational inertia. The rotational inertia of an atom is tiny because almost all of its mass is in the nucleus, which typically has a radius less than $10^{-14} \mathrm{~m}$. Thus the minimum rotational energy of an atom is much more

than $\frac{1}{2} k_{\mathrm{B}} T$ for any attainable temperature, and the energy available is not enough to make an atom rotate. We will return to this point when discussing diatomic and polyatomic gases in the next section.

## EXAMPLE 2.4

## Calculating Kinetic Energy and Speed of a Gas Molecule

(a) What is the average kinetic energy of a gas molecule at $20.0^{\circ} \mathrm{C}$ (room temperature)? (b) Find the rms speed of a nitrogen molecule $\left(\mathrm{N}_{2}\right)$ at this temperature.

## Strategy

(a) The known in the equation for the average kinetic energy is the temperature:

$$
\bar{K}=\frac{1}{2} m \bar{v}^{2}=\frac{3}{2} k_{\mathrm{B}} T
$$

Before substituting values into this equation, we must convert the given temperature into kelvin: $T=(20.0+273) \mathrm{K}=293 \mathrm{~K}$. We can find the rms speed of a nitrogen molecule by using the equation

$$
v_{\mathrm{rms}}=\sqrt{\overline{v^{2}}}=\sqrt{\frac{3 k_{\mathrm{B}} T}{m}}
$$

but we must first find the mass of a nitrogen molecule. Obtaining the molar mass of nitrogen $\mathrm{N}_{2}$ from the periodic table, we find

$$
m=\frac{M}{N_{A}}=\frac{\left.2(14.0067) \times 10^{-3} \mathrm{~kg} / \mathrm{mol}\right)}{6.02 \times 10^{23} \mathrm{~mol}^{-1}}=4.65 \times 10^{-26} \mathrm{~kg}
$$

## Solution

a. The temperature alone is sufficient for us to find the average translational kinetic energy. Substituting the temperature into the translational kinetic energy equation gives

$$
\bar{K}=\frac{3}{2} k_{\mathrm{B}} T=\frac{3}{2}\left(1.38 \times 10^{-23} \mathrm{~J} / \mathrm{K}\right)(293 \mathrm{~K})=6.07 \times 10^{-21} \mathrm{~J}
$$

b. Substituting this mass and the value for $k_{\mathrm{B}}$ into the equation for $v_{\text {rms }}$ yields

$$
v_{\mathrm{rms}}=\sqrt{\frac{3 k_{\mathrm{B}} T}{m}}=\sqrt{\frac{3\left(1.38 \times 10^{-23} \mathrm{~J} / \mathrm{K}\right)(293 \mathrm{~K})}{4.65 \times 10^{-26} \mathrm{~kg}}}=511 \mathrm{~m} / \mathrm{s}
$$

## Significance

Note that the average kinetic energy of the molecule is independent of the type of molecule. The average translational kinetic energy depends only on absolute temperature. The kinetic energy is very small compared to macroscopic energies, so that we do not feel when an air molecule is hitting our skin. On the other hand, it is much greater than the typical difference in gravitational potential energy when a molecule moves from, say, the top to the bottom of a room, so our neglect of gravitation is justified in typical real-world situations. The rms speed of the nitrogen molecule is surprisingly large. These large molecular velocities do not yield macroscopic movement of air, since the molecules move in all directions with equal likelihood. The mean free path (the distance a molecule moves on average between collisions, discussed a bit later in this section) of molecules in air is very small, so the molecules move rapidly but do not get very far in a second. The high value for rms speed is reflected in the speed of sound, which is about $340 \mathrm{~m} / \mathrm{s}$ at room temperature. The higher the rms speed of air molecules, the faster sound vibrations can be transferred through the air. The speed of sound increases with temperature and is greater in gases with small molecular masses, such as helium (see Figure 2.11).

## EXAMPLE 2.5

## Calculating Temperature: Escape Velocity of Helium Atoms

To escape Earth's gravity, an object near the top of the atmosphere (at an altitude of $100 \mathrm{~km}$ ) must travel away from Earth at $11.1 \mathrm{~km} / \mathrm{s}$. This speed is called the escape velocity. At what temperature would helium atoms have an rms speed equal to the escape velocity?

## Strategy

Identify the knowns and unknowns and determine which equations to use to solve the problem.

## Solution

1. Identify the knowns: $v$ is the escape velocity, $11.1 \mathrm{~km} / \mathrm{s}$.
2. Identify the unknowns: We need to solve for temperature, $T$. We also need to solve for the mass $m$ of the helium atom.
3. Determine which equations are needed.

- To get the mass $m$ of the helium atom, we can use information from the periodic table:

$$
m=\frac{M}{N_{A}}
$$

- To solve for temperature $T$, we can rearrange

$$
\frac{1}{2} m v^{2}=\frac{3}{2} k_{\mathrm{B}} T
$$

to yield

$$
T=\frac{m \bar{v}}{3 k_{\mathrm{B}}}
$$

4. Substitute the known values into the equations and solve for the unknowns,

$$
m=\frac{M}{N_{A}}=\frac{4.0026 \times 10^{-3} \mathrm{~kg} / \mathrm{mol}}{6.02 \times 10^{23} \mathrm{~mol}}=6.65 \times 10^{-27} \mathrm{~kg}
$$

and

$$
T=\frac{\left(6.65 \times 10^{-27} \mathrm{~kg}\right)\left(11.1 \times 10^{3} \mathrm{~m} / \mathrm{s}\right)^{2}}{3\left(1.38 \times 10^{-23} \mathrm{~J} / \mathrm{K}\right)}=1.98 \times 10^{4} \mathrm{~K}
$$

## Significance

This temperature is much higher than atmospheric temperature, which is approximately $250 \mathrm{~K}$ $\left(-25^{\circ} \mathrm{C}\right.$ or $\left.-10^{\circ} \mathrm{F}\right)$ at high elevation. Very few helium atoms are left in the atmosphere, but many were present when the atmosphere was formed, and more are always being created by radioactive decay (see the chapter on nuclear physics). The reason for the loss of helium atoms is that a small number of helium atoms have speeds higher than Earth's escape velocity even at normal temperatures. The speed of a helium atom changes from one collision to the next, so that at any instant, there is a small but nonzero chance that the atom's speed is greater than the escape velocity. The chance is high enough that over the lifetime of Earth, almost all the helium atoms that have been in the atmosphere have reached escape velocity at high altitudes and escaped from Earth's gravitational pull. Heavier molecules, such as oxygen, nitrogen, and water, have smaller rms speeds, and so it is much less likely that any of them will have speeds greater than the escape velocity. In fact, the likelihood is so small that billions of years are required to lose significant amounts of heavier molecules from the atmosphere. Figure 2.12 shows the effect of a lack of an atmosphere on the Moon. Because the gravitational pull of the Moon is much weaker, it has lost almost its entire atmosphere. The atmospheres of Earth and other bodies are compared in this chapter's exercises.

## Vapor Pressure, Partial Pressure, and Dalton's Law

The pressure a gas would create if it occupied the total volume available is called the gas's partial pressure. If two or more gases are mixed, they will come to thermal equilibrium as a result of collisions between molecules; the process is analogous to heat conduction as described in the chapter on temperature and heat. As we have seen from kinetic theory, when the gases have the same temperature, their molecules have the same average kinetic energy. Thus, each gas obeys the ideal gas law separately and exerts the same pressure on the walls of a container that it would if it were alone. Therefore, in a mixture of gases, the total pressure is the sum of partial pressures of the component gases, assuming ideal gas behavior and no chemical reactions between the components. This law is known as Dalton's law of partial pressures, after the English scientist John Dalton (1766-1844) who proposed it. Dalton's law is consistent with the fact that pressures add according to Pascal's principle.

In a mixture of ideal gases in thermal equilibrium, the number of molecules of each gas is proportional to its partial pressure. This result follows from applying the ideal gas law to each in the form $p / n=R T / V$. Because the right-hand side is the same for any gas at a given temperature in a container of a given volume, the lefthand side is the same as well.

- Partial pressure is the pressure a gas would create if it existed alone.
- Dalton's law states that the total pressure is the sum of the partial pressures of all of the gases present.
- For any two gases (labeled 1 and 2 ) in equilibrium in a container, $\frac{p_{1}}{n_{1}}=\frac{p_{2}}{n_{2}}$.

An important application of partial pressure is that, in chemistry, it functions as the concentration of a gas in
determining the rate of a reaction. Here, we mention only that the partial pressure of oxygen in a person's lungs is crucial to life and health. Breathing air that has a partial pressure of oxygen below $0.16 \mathrm{~atm}$ can impair coordination and judgment, particularly in people not acclimated to a high elevation. Lower partial pressures of $\mathrm{O}_{2}$ have more serious effects; partial pressures below $0.06 \mathrm{~atm}$ can be quickly fatal, and permanent damage is likely even if the person is rescued. However, the sensation of needing to breathe, as when holding one's breath, is caused much more by high concentrations of carbon dioxide in the blood than by low concentrations of oxygen. Thus, if a small room or closet is filled with air having a low concentration of oxygen, perhaps because a leaking cylinder of some compressed gas is stored there, a person will not feel any "choking" sensation and may go into convulsions or lose consciousness without noticing anything wrong. Safety engineers give considerable attention to this danger.

Another important application of partial pressure is vapor pressure, which is the partial pressure of a vapor at which it is in equilibrium with the liquid (or solid, in the case of sublimation) phase of the same substance. At any temperature, the partial pressure of the water in the air cannot exceed the vapor pressure of the water at that temperature, because whenever the partial pressure reaches the vapor pressure, water condenses out of the air. Dew is an example of this condensation. The temperature at which condensation occurs for a sample of air is called the dew point. It is easily measured by slowly cooling a metal ball; the dew point is the temperature at which condensation first appears on the ball.

The vapor pressures of water at some temperatures of interest for meteorology are given in Table 2.2.

| $\boldsymbol{T}\left({ }^{\circ} \mathrm{C}\right)$ | Vapor Pressure (Pa) |
| :--- | :--- |
| 0 | 610.5 |
| 3 | 757.9 |
| 5 | 872.3 |
| 8 | 1073 |
| 10 | 1228 |
| 13 | 1497 |
| 15 | 1705 |
| 18 | 2063 |
| 20 | 2338 |
| 23 | 2809 |
| 25 | 3167 |
| 30 | 4243 |
| 35 | 5623 |
| 40 | 7376 |

Table 2.2 Vapor Pressure of Water at Various Temperatures

The relative humidity (R.H.) at a temperature $T$ is defined by

$$
\text { R.H. }=\frac{\text { Partial pressure of water vapor at } T}{\text { Vapor pressure of water at } T} \times 100 \%
$$

A relative humidity of $100 \%$ means that the partial pressure of water is equal to the vapor pressure; in other words, the air is saturated with water.

EXAMPLE 2.6

## Calculating Relative Humidity

What is the relative humidity when the air temperature is $25^{\circ} \mathrm{C}$ and the dew point is $15^{\circ} \mathrm{C}$ ?

## Strategy

We simply look up the vapor pressure at the given temperature and that at the dew point and find the ratio.

## Solution

$$
\text { R.H. }=\frac{\text { Partial pressure of water vapor at } 15^{\circ} \mathrm{C}}{\text { Partial pressure of water vapor at } 25^{\circ} \mathrm{C}} \times 100 \%=\frac{1705 \mathrm{~Pa}}{3167 \mathrm{~Pa}} \times 100 \%=53.8 \%
$$

## Significance

R.H. is important to our comfort. The value of $53.8 \%$ is within the range of $40 \%$ to $60 \%$ recommended for comfort indoors.

As noted in the chapter on temperature and heat, the temperature seldom falls below the dew point, because when it reaches the dew point or frost point, water condenses and releases a relatively large amount of latent heat of vaporization.

## Mean Free Path and Mean Free Time

We now consider collisions explicitly. The usual first step (which is all we'll take) is to calculate the mean free path, $\lambda$, the average distance a molecule travels between collisions with other molecules, and the mean free time $\tau$, the average time between the collisions of a molecule. If we assume all the molecules are spheres with a radius $r$, then a molecule will collide with another if their centers are within a distance $2 r$ of each other. For a given particle, we say that the area of a circle with that radius, $4 \pi r^{2}$, is the "cross-section" for collisions. As the particle moves, it traces a cylinder with that cross-sectional area. The mean free path is the length $\lambda$ such that the expected number of other molecules in a cylinder of length $\lambda$ and cross-section $4 \pi r^{2}$ is 1 . If we temporarily ignore the motion of the molecules other than the one we're looking at, the expected number is the number density of molecules, $N / V$, times the volume, and the volume is $4 \pi r^{2} \lambda$, so we have $(N / V) 4 \pi r^{2} \lambda=1$, or

$$
\lambda=\frac{V}{4 \pi r^{2} N}
$$

Taking the motion of all the molecules into account makes the calculation much harder, but the only change is a factor of $\sqrt{2}$. The result is

$$
\lambda=\frac{V}{4 \sqrt{2} \pi r^{2} N}
$$

In an ideal gas, we can substitute $V / N=k_{\mathrm{B}} T / p$ to obtain

$$
\lambda=\frac{k_{\mathrm{B}} T}{4 \sqrt{2} \pi r^{2} p}
$$

The mean free time $\tau$ is simply the mean free path divided by a typical speed, and the usual choice is the rms speed. Then

$$
\tau=\frac{k_{\mathrm{B}} T}{4 \sqrt{2} \pi r^{2} p v_{\mathrm{rms}}}
$$

## EXAMPLE 2.7

## Calculating Mean Free Time

Find the mean free time for argon atoms $(M=39.9 \mathrm{~g} / \mathrm{mol})$ at a temperature of $0{ }^{\circ} \mathrm{C}$ and a pressure of 1.00 atm. Take the radius of an argon atom to be $1.70 \times 10^{-10} \mathrm{~m}$.

## Solution

1. Identify the knowns and convert into SI units. We know the molar mass is $0.0399 \mathrm{~kg} / \mathrm{mol}$, the temperature is $273 \mathrm{~K}$, the pressure is $1.01 \times 10^{5} \mathrm{~Pa}$, and the radius is $1.70 \times 10^{-10} \mathrm{~m}$.
2. Find the rms speed: $v_{\mathrm{rms}}=\sqrt{\frac{3 R T}{M}}=413 \frac{\mathrm{m}}{\mathrm{s}}$.
3. Substitute into the equation for the mean free time:

$$
\tau=\frac{k_{\mathrm{B}} T}{4 \sqrt{2} \pi r^{2} p v_{\mathrm{rms}}}=\frac{\left(1.38 \times 10^{-23} \mathrm{~J} / \mathrm{K}\right)(273 \mathrm{~K})}{4 \sqrt{2} \pi\left(1.70 \times 10^{-10} \mathrm{~m}\right)^{2}\left(1.01 \times 10^{5} \mathrm{~Pa}\right)(413 \mathrm{~m} / \mathrm{s})}=1.76 \times 10^{-10} \mathrm{~s}
$$

## Significance

We can hardly compare this result with our intuition about gas molecules, but it gives us a picture of molecules colliding with extremely high frequency.

### 2.3 Heat Capacity and Equipartition of Energy

In the chapter on temperature and heat, we defined the specific heat capacity with the equation $Q=m c \Delta T$, or $c=(1 / m) Q / \Delta T$. However, the properties of an ideal gas depend directly on the number of moles in a sample, so here we define specific heat capacity in terms of the number of moles, not the mass. Furthermore, when talking about solids and liquids, we ignored any changes in volume and pressure with changes in temperature-a good approximation for solids and liquids, but for gases, we have to make some condition on volume or pressure changes. Here, we focus on the heat capacity with the volume held constant. We can calculate it for an ideal gas.

## Heat Capacity of an Ideal Monatomic Gas at Constant Volume

We define the molar heat capacity at constant volume $C_{V}$ as

$$
C_{V}=\frac{1}{n} \frac{Q}{\Delta T}, \text { with } V \text { held constant. }
$$

This is often expressed in the form

$$
Q=n C_{V} \Delta T
$$

If the volume does not change, there is no overall displacement, so no work is done, and the only change in internal energy is due to the heat flow $\Delta E_{\text {int }}=Q$. (This statement is discussed further in the next chapter.) We use the equation $E_{\text {int }}=3 n R T / 2$ to write $\Delta E_{\text {int }}=3 n R \Delta T / 2$ and substitute $\Delta E$ for $Q$ to find $Q=3 n R \Delta T / 2$, which gives the following simple result for an ideal monatomic gas:

$$
C_{V}=\frac{3}{2} R
$$

It is independent of temperature, which justifies our use of finite differences instead of a derivative. This formula agrees well with experimental results.

In the next chapter we discuss the molar specific heat at constant pressure $C_{p}$, which is always greater than $C_{V}$.

## EXAMPLE 2.8

## Calculating Temperature

A sample of $0.125 \mathrm{~kg}$ of xenon is contained in a rigid metal cylinder, big enough that the xenon can be modeled as an ideal gas, at a temperature of $20.0^{\circ} \mathrm{C}$. The cylinder is moved outside on a hot summer day. As the xenon comes into equilibrium by reaching the temperature of its surroundings, $180 \mathrm{~J}$ of heat are conducted to it through the cylinder walls. What is the equilibrium temperature? Ignore the expansion of the metal cylinder.

## Solution

1. Identify the knowns: We know the initial temperature $T_{1}$ is $20.0^{\circ} \mathrm{C}$, the heat $Q$ is $180 \mathrm{~J}$, and the mass $m$ of the xenon is $0.125 \mathrm{~kg}$.
2. Identify the unknown. We need the final temperature, so we'll need $\Delta T$.
3. Determine which equations are needed. Because xenon gas is monatomic, we can use $Q=3 n R \Delta T / 2$. Then we need the number of moles, $n=m / M$.
4. Substitute the known values into the equations and solve for the unknowns.

The molar mass of xenon is $131.3 \mathrm{~g}$, so we obtain

$$
\begin{gathered}
n=\frac{125 \mathrm{~g}}{131.3 \mathrm{~g} / \mathrm{mol}}=0.952 \mathrm{~mol} \\
\Delta T=\frac{2 Q}{3 n R}=\frac{2(180 \mathrm{~J})}{3(0.952 \mathrm{~mol})\left(8.31 \mathrm{~J} / \mathrm{mol} \cdot{ }^{\circ} \mathrm{C}\right)}=15.2^{\circ} \mathrm{C}
\end{gathered}
$$

Therefore, the final temperature is $35.2^{\circ} \mathrm{C}$. The problem could equally well be solved in kelvin; as a kelvin is the same size as a degree Celsius of temperature change, you would get $\Delta T=15.2 \mathrm{~K}$.

## Significance

The heating of an ideal or almost ideal gas at constant volume is important in car engines and many other practical systems.

We would like to generalize our results to ideal gases with more than one atom per molecule. In such systems, the molecules can have other forms of energy beside translational kinetic energy, such as rotational kinetic energy and vibrational kinetic and potential energies. We will see that a simple rule lets us determine the average energies present in these forms and solve problems in much the same way as we have for monatomic gases.

## Degrees of Freedom

In the previous section, we found that $\frac{1}{2} m \overline{v^{2}}=\frac{3}{2} k_{\mathrm{B}} T$ and $\overline{v^{2}}=3 \overline{v_{x}^{2}}$, from which it follows that $\frac{1}{2} m \overline{v_{x}^{2}}=\frac{1}{2} k_{\mathrm{B}} T$. The same equation holds for $\overline{v_{y}^{2}}$ and for $\overline{v_{z}^{2}}$. Thus, we can look at our energy of $\frac{3}{2} k_{\mathrm{B}} T$ as the sum of contributions of $\frac{1}{2} k_{\mathrm{B}} T$ from each of the three dimensions of translational motion. Shifting to the gas as a whole, we see that the 3 in the formula $C_{V}=\frac{3}{2} R$ also reflects those three dimensions. We define a degree of freedom as an independent possible motion of a molecule, such as each of the three dimensions of translation. Then, letting $d$ represent the number of degrees of freedom, the molar heat capacity at constant volume of a monatomic ideal gas is $C_{V}=\frac{d}{2} R$, where $d=3$.

The branch of physics called statistical mechanics tells us, and experiment confirms, that $C_{V}$ of any ideal gas is given by this equation, regardless of the number of degrees of freedom. This fact follows from a more general result, the equipartition theorem, which holds in classical (non-quantum) thermodynamics for systems in thermal equilibrium under technical conditions that are beyond our scope. Here, we mention only that in a system, the energy is shared among the degrees of freedom by collisions.

## Equipartition Theorem

The energy of a thermodynamic system in equilibrium is partitioned equally among its degrees of freedom. Accordingly, the molar heat capacity of an ideal gas is proportional to its number of degrees of freedom, $d$ :

$$
C_{V}=\frac{d}{2} R
$$

This result is due to the Scottish physicist James Clerk Maxwell (1831-1871), whose name will appear several more times in this book.

For example, consider a diatomic ideal gas (a good model for nitrogen, $\mathrm{N}_{2}$, and oxygen, $\mathrm{O}_{2}$ ). Such a gas has more degrees of freedom than a monatomic gas. In addition to the three degrees of freedom for translation, it has two degrees of freedom for rotation perpendicular to its axis. Furthermore, the molecule can vibrate along its axis. This motion is often modeled by imagining a spring connecting the two atoms, and we know from simple harmonic motion that such motion has both kinetic and potential energy. Each of these forms of energy corresponds to a degree of freedom, giving two more.

We might expect that for a diatomic gas, we should use 7 as the number of degrees of freedom; classically, if the molecules of a gas had only translational kinetic energy, collisions between molecules would soon make them rotate and vibrate. However, as explained in the previous module, quantum mechanics controls which degrees of freedom are active. The result is shown in Figure 2.13. Both rotational and vibrational energies are limited to discrete values. For temperatures below about $60 \mathrm{~K}$, the energies of hydrogen molecules are too low for a collision to bring the rotational state or vibrational state of a molecule from the lowest energy to the second lowest, so the only form of energy is translational kinetic energy, and $d=3$ or $C_{V}=3 R / 2$ as in a monatomic gas. Above that temperature, the two rotational degrees of freedom begin to contribute, that is, some molecules are excited to the rotational state with the second-lowest energy. (This temperature is much lower than that where rotations of monatomic gases contribute, because diatomic molecules have much higher rotational inertias and hence much lower rotational energies.) From about room temperature (a bit less than $300 \mathrm{~K}$ ) to about $600 \mathrm{~K}$, the rotational degrees of freedom are fully active, but the vibrational ones are not, and $d=5$. Then, finally, above about $3000 \mathrm{~K}$, the vibrational degrees of freedom are fully active, and $d=7$ as the classical theory predicted.

Polyatomic molecules typically have one additional rotational degree of freedom at room temperature, since they have comparable moments of inertia around any axis. Thus, at room temperature, they have $d=6$, and at high temperature, $d=8$. We usually assume that gases have the theoretical room-temperature values of $d$.

As shown in Table 2.3, the results agree well with experiments for many monatomic and diatomic gases, but the agreement for triatomic gases is only fair. The differences arise from interactions that we have ignored between and within molecules.

| Gas | $C_{V} / R$ at $25^{\circ} \mathrm{C}$ and 1 atm |
| :--- | :--- |
| $\mathrm{Ar}$ | 1.50 |
| $\mathrm{He}$ | 1.50 |
| $\mathrm{Ne}$ | 1.50 |
| $\mathrm{CO}$ | 2.50 |
| $\mathrm{H}_{2}$ | 2.47 |
| $\mathrm{N}_{2}$ | 2.50 |
| $\mathrm{O}_{2}$ | 2.53 |
| $\mathrm{F}_{2}$ | 2.8 |
| $\mathrm{CO}_{2}$ | 3.48 |
| $\mathrm{H}_{2} \mathrm{~S}$ | 3.13 |
| $\mathrm{N}_{2} \mathrm{O}$ | 3.66 |

Table 2.3 $C_{V} / R$ for Various Monatomic, Diatomic, and Triatomic Gases

What about internal energy for diatomic and polyatomic gases? For such gases, $C_{V}$ is a function of temperature (Figure 2.13), so we do not have the kind of simple result we have for monatomic ideal gases.

## Molar Heat Capacity of Solid Elements

The idea of equipartition leads to an estimate of the molar heat capacity of solid elements at ordinary temperatures. We can model the atoms of a solid as attached to neighboring atoms by springs (Figure 2.14).

Analogously to the discussion of vibration in the previous module, each atom has six degrees of freedom: one kinetic and one potential for each of the $x^{-}, y$-, and $z$-directions. Accordingly, the molar specific heat of a metal should be $3 R$. This result, known as the Law of Dulong and Petit, works fairly well experimentally at room temperature. (For every element, it fails at low temperatures for quantum-mechanical reasons. Since quantum effects are particularly important for low-mass particles, the Law of Dulong and Petit already fails at room temperature for some light elements, such as beryllium and carbon. It also fails for some heavier elements for various reasons beyond what we can cover.)

## PROBLEM-SOLVING STRATEGY

## Heat Capacity and Equipartition

The strategy for solving these problems is the same as the one in Phase Changes for the effects of heat transfer. The only new feature is that you should determine whether the case just presented-ideal gases at constant volume-applies to the problem. (For solid elements, looking up the specific heat capacity is generally better than estimating it from the Law of Dulong and Petit.) In the case of an ideal gas, determine the number $d$ of degrees of freedom from the number of atoms in the gas molecule and use it to calculate $C_{V}$ (or use $C_{V}$ to solve for $d$ ).

## EXAMPLE 2.9

## Calculating Temperature: Calorimetry with an Ideal Gas

A 300-g piece of solid gallium (a metal used in semiconductor devices) at its melting point of only $30.0^{\circ} \mathrm{C}$ is in contact with 12.0 moles of air (assumed diatomic) at $95.0^{\circ} \mathrm{C}$ in an insulated container. When the air reaches equilibrium with the gallium, $202 \mathrm{~g}$ of the gallium have melted. Based on those data, what is the heat of fusion
of gallium? Assume the volume of the air does not change and there are no other heat transfers.

## Strategy

We'll use the equation $Q_{\text {hot }}+Q_{\text {cold }}=0$. As some of the gallium doesn't melt, we know the final temperature is still the melting point. Then the only $Q_{\text {hot }}$ is the heat lost as the air cools, $Q_{\mathrm{hot}}=n_{\mathrm{air}} C_{V} \Delta T$, where $C_{V}=5 R / 2$. The only $Q_{\text {cold }}$ is the latent heat of fusion of the gallium, $Q_{\text {cold }}=m_{\mathrm{Ga}} L_{\mathrm{f}}$. It is positive because heat flows into the gallium.

## Solution

1. Set up the equation:

$$
n_{\mathrm{air}} C_{V} \Delta T+m_{\mathrm{Ga}} L_{\mathrm{f}}=0
$$

2. Substitute the known values and solve:

$$
(12.0 \mathrm{~mol})\left(\frac{5}{2}\right)\left(8.31 \frac{\mathrm{J}}{\mathrm{mol} \cdot{ }^{\circ} \mathrm{C}}\right)\left(30.0^{\circ} \mathrm{C}-95.0^{\circ} \mathrm{C}\right)+(0.202 \mathrm{~kg}) \mathrm{L}_{\mathrm{f}}=0
$$

We solve to find that the heat of fusion of gallium is $80.2 \mathrm{~kJ} / \mathrm{kg}$.

### 2.4 Distribution of Molecular Speeds

Particles in an ideal gas all travel at relatively high speeds, but they do not travel at the same speed. The rms speed is one kind of average, but many particles move faster and many move slower. The actual distribution of speeds has several interesting implications for other areas of physics, as we will see in later chapters.

## The Maxwell-Boltzmann Distribution

The motion of molecules in a gas is random in magnitude and direction for individual molecules, but a gas of many molecules has a predictable distribution of molecular speeds. This predictable distribution of molecular speeds is known as the Maxwell-Boltzmann distribution, after its originators, who calculated it based on kinetic theory, and it has since been confirmed experimentally (Figure 2.15).

To understand this figure, we must define a distribution function of molecular speeds, since with a finite number of molecules, the probability that a molecule will have exactly a given speed is 0 .

We define the distribution function $f(v)$ by saying that the expected number $N\left(v_{1}, v_{2}\right)$ of particles with speeds between $v_{1}$ and $v_{2}$ is given by

$$
N\left(v_{1}, v_{2}\right)=N \int_{v_{1}}^{v_{2}} f(v) d v
$$

[Since $N$ is dimensionless, the unit of $f(v)$ is seconds per meter.] We can write this equation conveniently in differential form:

$$
d N=N f(v) d v
$$

In this form, we can understand the equation as saying that the number of molecules with speeds between $v$ and $v+d v$ is the total number of molecules in the sample times $f(v)$ times $d v$. That is, the probability that a molecule's speed is between $v$ and $v+d v$ is $f(v) d v$.

We can now quote Maxwell's result, although the proof is beyond our scope.

## Maxwell-Boltzmann Distribution of Speeds

The distribution function for speeds of particles in an ideal gas at temperature $T$ is

$$
f(v)=\frac{4}{\sqrt{\pi}}\left(\frac{m}{2 k_{\mathrm{B}} T}\right)^{3 / 2} v^{2} e^{\left(-m v^{2} /\left(2 k_{\mathrm{B}} T\right)\right)}
$$

The factors before the $v^{2}$ are a normalization constant; they make sure that $N(0, \infty)=N$ by making sure that $\int_{0}^{\infty} f(v) d v=1$. Let's focus on the dependence on $v$. The factor of $v^{2}$ means that $f(0)=0$ and for small $v$, the curve looks like a parabola. The factor of $e^{-m_{0} v^{2} / 2 k_{\mathrm{B}} T}$ means that $\lim _{v \rightarrow \infty} f(v)=0$ and the graph has an exponential tail, which indicates that a few molecules may move at several times the rms speed. The interaction of these factors gives the function the single-peaked shape shown in the figure.

## EXAMPLE 2.10

## Calculating the Ratio of Numbers of Molecules Near Given Speeds

In a sample of nitrogen $\left(\mathrm{N}_{2}\right.$, with a molar mass of $\left.28.0 \mathrm{~g} / \mathrm{mol}\right)$ at a temperature of $27^{\circ} \mathrm{C}$, find the ratio of the number of molecules with a speed very close to $300 \mathrm{~m} / \mathrm{s}$ to the number with a speed very close to $100 \mathrm{~m} / \mathrm{s}$.

## Strategy

Since we're looking at a small range, we can approximate the number of molecules near $100 \mathrm{~m} / \mathrm{s}$ as $d N_{100}=f(100 \mathrm{~m} / \mathrm{s}) d v$. Then the ratio we want is

$$
\frac{d N_{300}}{d N_{100}}=\frac{f(300 \mathrm{~m} / \mathrm{s}) d v}{f(100 \mathrm{~m} / \mathrm{s}) d v}=\frac{f(300 \mathrm{~m} / \mathrm{s})}{f(100 \mathrm{~m} / \mathrm{s})}
$$

All we have to do is take the ratio of the two $f$ values.

## Solution

1. Identify the knowns and convert to SI units if necessary.

$$
T=300 \mathrm{~K}, k_{\mathrm{B}}=1.38 \times 10^{-23} \mathrm{~J} / \mathrm{K}
$$

$$
M=0.0280 \mathrm{~kg} / \mathrm{mol} \text { so } m=4.65 \times 10^{-26} \mathrm{~kg}
$$

2. Substitute the values and solve.

$$
\begin{aligned}
\frac{f(300 \mathrm{~m} / \mathrm{s})}{f(100 \mathrm{~m} / \mathrm{s})} & =\frac{\frac{4}{\sqrt{\pi}}\left(\frac{m}{2 k_{\mathrm{B}} T}\right)^{3 / 2}(300 \mathrm{~m} / \mathrm{s})^{2} \exp \left[-m(300 \mathrm{~m} / \mathrm{s})^{2} / 2 k_{\mathrm{B}} T\right]}{\frac{4}{\sqrt{\pi}}\left(\frac{m}{2 k_{\mathrm{B}} T}\right)^{3 / 2}(100 \mathrm{~m} / \mathrm{s})^{2} \exp \left[-m(100 \mathrm{~m} / \mathrm{s})^{2} / 2 k_{\mathrm{B}} T\right]} \\
& =\frac{(300 \mathrm{~m} / \mathrm{s})^{2} \exp \left[-\left(4.65 \times 10^{-26} \mathrm{~kg}\right)(300 \mathrm{~m} / \mathrm{s})^{2} / 2\left(1.38 \times 10^{-23} \mathrm{~J} / \mathrm{K}\right)(300 \mathrm{~K})\right]}{(100 \mathrm{~m} / \mathrm{s})^{2} \exp \left[-\left(4.65 \times 10^{-26} \mathrm{~kg}\right)(100 \mathrm{~m} / \mathrm{s})^{2} / 2\left(1.38 \times 10^{-23} \mathrm{~J} / \mathrm{K}\right)(300 \mathrm{~K})\right]} \\
& =3^{2} \exp \left[-\frac{\left(4.65 \times 10^{-26} \mathrm{~kg}\right)\left[(300 \mathrm{~m} / \mathrm{s})^{2}-(100 \mathrm{~ms})^{2}\right]}{2\left(1.38 \times 10^{-23} \mathrm{~J} / \mathrm{K}\right)(300 \mathrm{~K})}\right] \\
& =5.74
\end{aligned}
$$

Figure 2.16 shows that the curve is shifted to higher speeds at higher temperatures, with a broader range of speeds.

We can use a probability distribution to calculate average values by multiplying the distribution function by the quantity to be averaged and integrating the product over all possible speeds. (This is analogous to calculating averages of discrete distributions, where you multiply each value by the number of times it occurs, add the results, and divide by the number of values. The integral is analogous to the first two steps, and the normalization is analogous to dividing by the number of values.) Thus the average velocity is

$$
\bar{v}=\int_{0}^{\infty} v f(v) d v=\sqrt{\frac{8}{\pi} \frac{k_{\mathrm{B}} T}{m}}=\sqrt{\frac{8}{\pi} \frac{R T}{M}}
$$

Similarly,

$$
v_{\mathrm{rms}}=\sqrt{\overline{v^{2}}}=\sqrt{\int_{0}^{\infty} v^{2} f(v) d v}=\sqrt{\frac{3 k_{\mathrm{B}} T}{m}}=\sqrt{\frac{3 R T}{M}}
$$

as in Pressure, Temperature, and RMS Speed. The most probable speed, also called the peak speed $v_{p}$, is the speed at the peak of the velocity distribution. (In statistics it would be called the mode.) It is less than the rms speed $v_{\text {rms }}$. The most probable speed can be calculated by the more familiar method of setting the derivative of the distribution function, with respect to $v$, equal to 0 . The result is

$$
v_{p}=\sqrt{\frac{2 k_{\mathrm{B}} T}{m}}=\sqrt{\frac{2 R T}{M}}
$$

which is less than $v_{\text {rms }}$. In fact, the rms speed is greater than both the most probable speed and the average speed.

The peak speed provides a sometimes more convenient way to write the Maxwell-Boltzmann distribution function:

$$
f(v)=\frac{4 v^{2}}{\sqrt{\pi} v_{p}^{3}} e^{-v^{2} / v_{p}^{2}}
$$

In the factor $e^{-m v^{2} / 2 k_{\mathrm{B}} T}$, it is easy to recognize the translational kinetic energy. Thus, that expression is equal to $e^{-K / k_{\mathrm{B}} T}$. The distribution $f(v)$ can be transformed into a kinetic energy distribution by requiring that $f(K) d K=f(v) d v$. Boltzmann showed that the resulting formula is much more generally applicable if we replace the kinetic energy of translation with the total mechanical energy E. Boltzmann's result is

$$
f(E)=\frac{2}{\sqrt{\pi}}\left(k_{\mathrm{B}} T\right)^{-3 / 2} \sqrt{E} e^{-E / k_{\mathrm{B}} T}=\frac{2}{\sqrt{\pi}\left(k_{\mathrm{B}} T\right)^{3 / 2}} \frac{\sqrt{E}}{e^{E / k_{\mathrm{B}} T}}
$$

The first part of this equation, with the negative exponential, is the usual way to write it. We give the second part only to remark that $e^{E / k_{\mathrm{B}} T}$ in the denominator is ubiquitous in quantum as well as classical statistical mechanics.

## PROBLEM-SOLVING STRATEGY

## Speed Distribution

Step 1. Examine the situation to determine that it relates to the distribution of molecular speeds.

Step 2. Make a list of what quantities are given or can be inferred from the problem as stated (identify the known quantities).

Step 3. Identify exactly what needs to be determined in the problem (identify the unknown quantities). A written list is useful.

Step 4. Convert known values into proper SI units (K for temperature, Pa for pressure, $m^{3}$ for volume, molecules for $N$, and moles for $n$ ). In many cases, though, using $R$ and the molar mass will be more convenient than using $k_{\mathrm{B}}$ and the molecular mass.

Step 5. Determine whether you need the distribution function for velocity or the one for energy, and whether you are using a formula for one of the characteristic speeds (average, most probably, or rms), finding a ratio of values of the distribution function, or approximating an integral.

Step 6. Solve the appropriate equation for the ideal gas law for the quantity to be determined (the unknown quantity). Note that if you are taking a ratio of values of the distribution function, the normalization factors divide out. Or if approximating an integral, use the method asked for in the problem.

Step 7. Substitute the known quantities, along with their units, into the appropriate equation and obtain numerical solutions complete with units.

We can now gain a qualitative understanding of a puzzle about the composition of Earth's atmosphere.

Hydrogen is by far the most common element in the universe, and helium is by far the second-most common. Moreover, helium is constantly produced on Earth by radioactive decay. Why are those elements so rare in our atmosphere? The answer is that gas molecules that reach speeds above Earth's escape velocity, about $11 \mathrm{~km} / \mathrm{s}$, can escape from the atmosphere into space. Because of the lower mass of hydrogen and helium molecules, they move at higher speeds than other gas molecules, such as nitrogen and oxygen. Only a few exceed escape velocity, but far fewer heavier molecules do. Thus, over the billions of years that Earth has existed, far more hydrogen and helium molecules have escaped from the atmosphere than other molecules, and hardly any of either is now present.

We can also now take another look at evaporative cooling, which we discussed in the chapter on temperature and heat. Liquids, like gases, have a distribution of molecular energies. The highest-energy molecules are those that can escape from the intermolecular attractions of the liquid. Thus, when some liquid evaporates, the molecules left behind have a lower average energy, and the liquid has a lower temperature.

