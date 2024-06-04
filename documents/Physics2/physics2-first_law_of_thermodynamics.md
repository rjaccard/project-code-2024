# CHAPTER 3 <br> The First Law of Thermodynamics 

INTRODUCTION Heat is the transfer of energy due to a temperature difference between two systems. Heat describes the process of converting from one form of energy into another. A car engine, for example, burns gasoline. Heat is produced when the burned fuel is chemically transformed into mostly $\mathrm{CO}_{2}$ and $\mathrm{H}_{2} \mathrm{O}$, which are gases at the combustion temperature. These gases exert a force on a piston through a displacement, doing work and converting the piston's kinetic energy into a variety of other forms-into the car's kinetic energy; into electrical energy to run the spark plugs, radio, and lights; and back into stored energy in the car's battery.

Energy is conserved in all processes, including those associated with thermodynamic systems. The roles of heat transfer and internal energy change vary from process to process and affect how work is done by the system in that process. We will see that the first law of thermodynamics explains that a change in the internal energy of a system comes from changes in heat or work. Understanding the laws that govern thermodynamic processes and the relationship between the system and its surroundings is therefore paramount in gaining scientific knowledge of energy and energy consumption.

### 3.1 Thermodynamic Systems

A thermodynamic system includes anything whose thermodynamic properties are of interest. It is embedded in its surroundings or environment; it can exchange heat with, and do work on, its environment through a boundary, which is the imagined wall that separates the system and the environment (Figure 3.2). In reality, the immediate surroundings of the system are interacting with it directly and therefore have a much stronger influence on its behavior and properties. For example, if we are studying a car engine, the burning gasoline inside the cylinder of the engine is the thermodynamic system; the piston, exhaust system, radiator, and air outside form the surroundings of the system. The boundary then consists of the inner surfaces of the cylinder and piston.

Normally, a system must have some interactions with its surroundings. A system is called an isolated and closed system if it is completely separated from its environment-for example, a gas that is surrounded by immovable and thermally insulating walls. In reality, a closed system does not exist unless the entire universe is treated as the system, or it is used as a model for an actual system that has minimal interactions with its environment. Most systems are known as an open system, which can exchange energy and/or matter with its surroundings (Figure 3.3).

When we examine a thermodynamic system, we ignore the difference in behavior from place to place inside the system for a given moment. In other words, we concentrate on the macroscopic properties of the system, which are the averages of the microscopic properties of all the molecules or entities in the system. Any thermodynamic system is therefore treated as a continuum that has the same behavior everywhere inside. We assume the system is in equilibrium. You could have, for example, a temperature gradient across the system. However, when we discuss a thermodynamic system in this chapter, we study those that have uniform properties throughout the system.

Before we can carry out any study on a thermodynamic system, we need a fundamental characterization of the system. When we studied a mechanical system, we focused on the forces and torques on the system, and their balances dictated the mechanical equilibrium of the system. In a similar way, we should examine the heat transfer between a thermodynamic system and its environment or between the different parts of the system, and its balance should dictate the thermal equilibrium of the system. Intuitively, such a balance is reached if the temperature becomes the same for different objects or parts of the system in thermal contact, and the net heat transfer over time becomes zero.

Thus, when we say two objects (a thermodynamic system and its environment, for example) are in thermal equilibrium, we mean that they are at the same temperature, as we discussed in Temperature and Heat. Let us consider three objects at temperatures $T_{1}, T_{2}$, and $T_{3}$, respectively. How do we know whether they are in thermal equilibrium? The governing principle here is the zeroth law of thermodynamics, as described in Temperature and Heat on temperature and heat:

If object 1 is in thermal equilibrium with objects 2 and 3, respectively, then objects 2 and 3 must also be in thermal equilibrium.

Mathematically, we can simply write the zeroth law of thermodynamics as

$$
\text { If } T_{1}=T_{2} \text { and } T_{1}=T_{3} \text {, then } T_{2}=T_{3}
$$

This is the most fundamental way of defining temperature: Two objects must be at the same temperature thermodynamically if the net heat transfer between them is zero when they are put in thermal contact and have reached a thermal equilibrium.

The zeroth law of thermodynamics is equally applicable to the different parts of a closed system and requires that the temperature everywhere inside the system be the same if the system has reached a thermal equilibrium. To simplify our discussion, we assume the system is uniform with only one type of material-for example, water in a tank. The measurable properties of the system at least include its volume, pressure, and temperature. The range of specific relevant variables depends upon the system. For example, for a stretched
rubber band, the relevant variables would be length, tension, and temperature. The relationship between these three basic properties of the system is called the equation of state of the system and is written symbolically for a closed system as

$$
f(p, V, T)=0
$$

where $V, p$, and $T$ are the volume, pressure, and temperature of the system at a given condition.

In principle, this equation of state exists for any thermodynamic system but is not always readily available. The forms of $f(p, V, T)=0$ for many materials have been determined either experimentally or theoretically. In the preceding chapter, we saw an example of an equation of state for an ideal gas, $f(p, V, T)=p V-n R T=0$.

We have so far introduced several physical properties that are relevant to the thermodynamics of a thermodynamic system, such as its volume, pressure, and temperature. We can separate these quantities into two generic categories. The quantity associated with an amount of matter is an extensive variable, such as the volume and the number of moles. The other properties of a system are intensive variables, such as the pressure and temperature. An extensive variable doubles its value if the amount of matter in the system doubles, provided all the intensive variables remain the same. For example, the volume or total energy of the system doubles if we double the amount of matter in the system while holding the temperature and pressure of the system unchanged.

### 3.2 Work, Heat, and Internal Energy

We discussed the concepts of work and energy earlier in mechanics. Examples and related issues of heat transfer between different objects have also been discussed in the preceding chapters. Here, we want to expand these concepts to a thermodynamic system and its environment. Specifically, we elaborated on the concepts of heat and heat transfer in the previous two chapters. Here, we want to understand how work is done by or to a thermodynamic system; how heat is transferred between a system and its environment; and how the total energy of the system changes under the influence of the work done and heat transfer.

## Work Done by a System

A force created from any source can do work by moving an object through a displacement. Then how does a thermodynamic system do work? Figure 3.4 shows a gas confined to a cylinder that has a movable piston at one end. If the gas expands against the piston, it exerts a force through a distance and does work on the piston. If the piston compresses the gas as it is moved inward, work is also done-in this case, on the gas. The work associated with such volume changes can be determined as follows: Let the gas pressure on the piston face be $p$. Then the force on the piston due to the gas is $p A$, where $A$ is the area of the face. When the piston is pushed outward an infinitesimal distance $d x$, the magnitude of the work done by the gas is

$$
d W=F d x=p A d x
$$

Since the change in volume of the gas is $d V=A d x$, this becomes

$$
d W=p d V
$$

For a finite change in volume from $V_{1}$ to $V_{2}$, we can integrate this equation from $V_{1}$ to $V_{2}$ to find the net work:

$$
W=\int_{V_{1}}^{V_{2}} p d V
$$

This integral is only meaningful for a quasi-static process, which means a process that takes place in infinitesimally small steps, keeping the system at thermal equilibrium. (We examine this idea in more detail later in this chapter.) Only then does a well-defined mathematical relationship (the equation of state) exist between the pressure and volume. This relationship can be plotted on a $p V$ diagram of pressure versus volume, where the curve is the change of state. We can approximate such a process as one that occurs slowly, through a series of equilibrium states. The integral is interpreted graphically as the area under the $p V$ curve (the shaded area of Figure 3.5). Work done by the gas is positive for expansion and negative for compression.

Consider the two processes involving an ideal gas that are represented by paths $A C$ and $A B C$ in Figure 3.6. The first process is an isothermal expansion, with the volume of the gas changing its volume from $V_{1}$ to $V_{2}$. This isothermal process is represented by the curve between points $A$ and $C$. The gas is kept at a constant temperature $T$ by keeping it in thermal equilibrium with a heat reservoir at that temperature. From Equation 3.4 and the ideal gas law,

$$
W=\int_{V_{1}}^{V_{2}} p d V=\int_{V_{1}}^{V_{2}}\left(\frac{n R T}{V}\right) d V
$$

The expansion is isothermal, so $T$ remains constant over the entire process. Since $n$ and $R$ are also constant, the only variable in the integrand is $V$, so the work done by an ideal gas in an isothermal process is

$$
W=n R T \int_{V_{1}}^{V_{2}} \frac{d V}{V}=n R T \ln \frac{V_{2}}{V_{1}}
$$

Notice that if $V_{2}>V_{1}$ (expansion), $W$ is positive, as expected.

The straight lines from $A$ to $B$ and then from $B$ to $C$ represent a different process. Here, a gas at a pressure $p_{1}$ first expands isobarically (constant pressure) and quasi-statically from $V_{1}$ to $V_{2}$, after which it cools quasistatically at the constant volume $V_{2}$ until its pressure drops to $p_{2}$. From $A$ to $B$, the pressure is constant at $p$, so the work over this part of the path is

$$
W=\int_{V_{1}}^{V_{2}} p d V=p_{1} \int_{V_{1}}^{V_{2}} d V=p_{1}\left(V_{2}-V_{1}\right)
$$

From $B$ to $C$, there is no change in volume and therefore no work is done. The net work over the path $A B C$ is then

$$
W=p_{1}\left(V_{2}-V_{1}\right)+0=p_{1}\left(V_{2}-V_{1}\right)
$$

A comparison of the expressions for the work done by the gas in the two processes of Figure 3.6 shows that they are quite different. This illustrates a very important property of thermodynamic work: It is path dependent. We cannot determine the work done by a system as it goes from one equilibrium state to another unless we know its thermodynamic path. Different values of the work are associated with different paths.

## EXAMPLE 3.1

## Isothermal Expansion of a van der Waals Gas

Studies of a van der Waals gas require an adjustment to the ideal gas law that takes into consideration that gas molecules have a definite volume (see The Kinetic Theory of Gases). One mole of a van der Waals gas has an equation of state

$$
\left(p+\frac{a}{V^{2}}\right)(V-b)=R T
$$

where $a$ and $b$ are two parameters for a specific gas. Suppose the gas expands isothermally and quasi-statically from volume $V_{1}$ to volume $V_{2}$. How much work is done by the gas during the expansion?

## Strategy

Because the equation of state is given, we can use Equation 3.4 to express the pressure in terms of $V$ and $T$. Furthermore, temperature $T$ is a constant under the isothermal condition, so $V$ becomes the only changing
variable under the integral.

## Solution

To evaluate this integral, we must express $p$ as a function of $V$. From the given equation of state, the gas pressure is

$$
p=\frac{R T}{V-b}-\frac{a}{V^{2}}
$$

Because $T$ is constant under the isothermal condition, the work done by $1 \mathrm{~mol}$ of a van der Waals gas in expanding from a volume $V_{1}$ to a volume $V_{2}$ is thus

$$
\begin{aligned}
W & =\int_{V_{1}}^{V_{2}}\left(\frac{R T}{V-b}-\frac{a}{V^{2}}\right) d V=\left|R T \ln (V-b)+\frac{a}{V}\right|_{V_{1}}^{V_{2}} \\
& =R T \ln \left(\frac{V_{2}-b}{V_{1}-b}\right)+a\left(\frac{1}{V_{2}}-\frac{1}{V_{1}}\right)
\end{aligned}
$$

## Significance

By taking into account the volume of molecules, the expression for work is much more complex. If, however, we set $a=0$ and $b=0$, we see that the expression for work matches exactly the work done by an isothermal process for one mole of an ideal gas.

## Internal Energy

The internal energy $E_{\text {int }}$ of a thermodynamic system is, by definition, the sum of the mechanical energies of all the molecules or entities in the system. If the kinetic and potential energies of molecule $i$ are $K_{i}$ and $U_{i}$, respectively, then the internal energy of the system is the average of the total mechanical energy of all the entities:

$$
E_{\text {int }}=\sum_{i}\left(\bar{K}_{i}+\bar{U}_{i}\right)
$$

where the summation is over all the molecules of the system, and the bars over $K$ and $U$ indicate average values. The kinetic energy $K_{i}$ of an individual molecule includes contributions due to its rotation and vibration, as well as its translational energy $m_{i} v_{i}^{2} / 2$, where $v_{i}$ is the molecule's speed measured relative to the center of mass of the system. The potential energy $U_{i}$ is associated only with the interactions between molecule $i$ and the other molecules of the system. In fact, neither the system's location nor its motion is of any consequence as far as the internal energy is concerned. The internal energy of the system is not affected by moving it from the basement to the roof of a 100-story building or by placing it on a moving train.

In an ideal monatomic gas, each molecule is a single atom. Consequently, there is no rotational or vibrational kinetic energy and $K_{i}=m_{i} v_{i}^{2} / 2$. Furthermore, there are no interatomic interactions (collisions notwithstanding), so $U_{i}=$ constant, which we set to zero. The internal energy is therefore due to translational kinetic energy only and

$$
E_{\mathrm{int}}=\sum_{i} \bar{K}_{i}=\sum_{i} \frac{1}{2} m_{i} \overline{v_{i}^{2}}
$$

From the discussion in the preceding chapter, we know that the average kinetic energy of a molecule in an ideal monatomic gas is

$$
\frac{1}{2} m_{i} \overline{v_{i}^{2}}=\frac{3}{2} k_{\mathrm{B}} T
$$

where $T$ is the Kelvin temperature of the gas. Consequently, the average mechanical energy per molecule of an ideal monatomic gas is also $3 k_{\mathrm{B}} T / 2$, that is,

$$
\overline{K_{i}+U_{i}}=\bar{K}_{i}=\frac{3}{2} k_{\mathrm{B}} T
$$

The internal energy is just the number of molecules multiplied by the average mechanical energy per molecule. Thus for $n$ moles of an ideal monatomic gas,

$$
E_{\text {int }}=n N_{\mathrm{A}}\left(\frac{3}{2} k_{\mathrm{B}} T\right)=\frac{3}{2} n R T
$$

Notice that the internal energy of a given quantity of an ideal monatomic gas depends on just the temperature and is completely independent of the pressure and volume of the gas. For other systems, the internal energy cannot be expressed so simply. However, an increase in internal energy can often be associated with an increase in temperature.

We know from the zeroth law of thermodynamics that when two systems are placed in thermal contact, they eventually reach thermal equilibrium, at which point they are at the same temperature. As an example, suppose we mix two monatomic ideal gases. Now, the energy per molecule of an ideal monatomic gas is proportional to its temperature. Thus, when the two gases are mixed, the molecules of the hotter gas must lose energy and the molecules of the colder gas must gain energy. This continues until thermal equilibrium is reached, at which point, the temperature, and therefore the average translational kinetic energy per molecule, is the same for both gases. The approach to equilibrium for real systems is somewhat more complicated than for an ideal monatomic gas. Nevertheless, we can still say that energy is exchanged between the systems until their temperatures are the same.

### 3.3 First Law of Thermodynamics

Now that we have seen how to calculate internal energy, heat, and work done for a thermodynamic system undergoing change during some process, we can see how these quantities interact to affect the amount of change that can occur. This interaction is given by the first law of thermodynamics. British scientist and novelist C. P. Snow (1905-1980) is credited with a joke about the four laws of thermodynamics. His humorous statement of the first law of thermodynamics is stated "you can't win," or in other words, you cannot get more energy out of a system than you put into it. We will see in this chapter how internal energy, heat, and work all play a role in the first law of thermodynamics.

Suppose $Q$ represents the heat exchanged between a system and the environment, and $W$ is the work done by or on the system. The first law states that the change in internal energy of that system is given by $Q-W$. Since added heat increases the internal energy of a system, $Q$ is positive when it is added to the system and negative when it is removed from the system.

When a gas expands, it does work and its internal energy decreases. Thus, $W$ is positive when work is done by the system and negative when work is done on the system. This sign convention is summarized in Table 3.1. The first law of thermodynamics is stated as follows:

## First Law of Thermodynamics

Associated with every equilibrium state of a system is its internal energy $E_{\text {int }}$. The change in $E_{\text {int }}$ for any
transition between two equilibrium states is

$$
\Delta E_{\text {int }}=Q-W
$$

where $Q$ and $W$ represent, respectively, the heat exchanged by the system and the work done by or on the system.

Thermodynamic Sign Conventions for Heat and Work

| Process | Convention |
| :--- | :--- |
| Heat added to system | $Q>0$ |
| Heat removed from system | $Q<0$ |
| Work done by system | $W>0$ |
| Work done on system | $W<0$ |

Table 3.1

The first law is a statement of energy conservation. It tells us that a system can exchange energy with its surroundings by the transmission of heat and by the performance of work. The net energy exchanged is then equal to the change in the total mechanical energy of the molecules of the system (i.e., the system's internal energy). Thus, if a system is isolated, its internal energy must remain constant.

Although $Q$ and $W$ both depend on the thermodynamic path taken between two equilibrium states, their difference $Q-W$ does not. Figure 3.7 shows the $p V$ diagram of a system that is making the transition from $A$ to $B$ repeatedly along different thermodynamic paths. Along path 1, the system absorbs heat $Q_{1}$ and does work $W_{1}$; along path 2 , it absorbs heat $Q_{2}$ and does work $W_{2}$, and so on. The values of $Q_{i}$ and $W_{i}$ may vary from path to path, but we have

$$
Q_{1}-W_{1}=Q_{2}-W_{2}=\cdots=Q_{i}-W_{i}=\cdots
$$

or

$$
\Delta E_{\text {int } 1}=\Delta E_{\mathrm{int} 2}=\cdots=\Delta E_{\mathrm{int} i}=\cdots
$$

That is, the change in the internal energy of the system between $A$ and $B$ is path independent. In the chapter on potential energy and the conservation of energy, we encountered another path-independent quantity: the change in potential energy between two arbitrary points in space. This change represents the negative of the work done by a conservative force between the two points. The potential energy is a function of spatial coordinates, whereas the internal energy is a function of thermodynamic variables. For example, we might write $E_{\text {int }}(T, p)$ for the internal energy. Functions such as internal energy and potential energy are known as state functions because their values depend solely on the state of the system.

Often the first law is used in its differential form, which is

$$
d E_{\mathrm{int}}=d Q-d W
$$

Here $d E_{\text {int }}$ is an infinitesimal change in internal energy when an infinitesimal amount of heat $d Q$ is exchanged with the system and an infinitesimal amount of work $d W$ is done by (positive in sign) or on (negative in sign) the system.

## EXAMPLE 3.2

## Changes of State and the First Law

During a thermodynamic process, a system moves from state $A$ to state $B$, it is supplied with $400 \mathrm{~J}$ of heat and does $100 \mathrm{~J}$ of work. (a) For this transition, what is the system's change in internal energy? (b) If the system then moves from state $B$ back to state $A$, what is its change in internal energy? (c) If in moving from $A$ to $B$ along a different path, $W^{\prime}{ }_{A B}=400 \mathrm{~J}$ of work is done on the system, how much heat does it absorb?

## Strategy

The first law of thermodynamics relates the internal energy change, work done by the system, and the heat transferred to the system in a simple equation. The internal energy is a function of state and is therefore fixed at any given point regardless of how the system reaches the state.

## Solution

a. From the first law, the change in the system's internal energy is

$$
\Delta E_{\text {int } A B}=Q_{A B}-W_{A B}=400 \mathrm{~J}-100 \mathrm{~J}=300 \mathrm{~J}
$$

b. Consider a closed path that passes through the states $A$ and $B$. Internal energy is a state function, so $\Delta E_{\text {int }}$ is zero for a closed path. Thus

$$
\Delta E_{\text {int }}=\Delta E_{\text {int } A B}+\Delta E_{\text {int } B A}=0
$$

and

$$
\Delta E_{\text {int } A B}=-\Delta E_{\text {int } B A}
$$

This yields

$$
\Delta E_{\text {int } B A}=-300 \mathrm{~J}
$$

c. The change in internal energy is the same for any path, so

$$
\begin{aligned}
\Delta E_{\text {int } A B} & =\Delta E_{\operatorname{int} A B}^{\prime}=Q_{A B}^{\prime}-W_{A B}^{\prime} \\
300 \mathrm{~J} & =Q_{A B^{-}}(-400 \mathrm{~J})
\end{aligned}
$$

and the heat exchanged is

$$
Q_{A B}^{\prime}=-100 \mathrm{~J}
$$

The negative sign indicates that the system loses heat in this transition.

## Significance

When a closed cycle is considered for the first law of thermodynamics, the change in internal energy around the whole path is equal to zero. If friction were to play a role in this example, less work would result from this heat added. Example 3.3 takes into consideration what happens if friction plays a role.

Notice that in Example 3.2, we did not assume that the transitions were quasi-static. This is because the first law is not subject to such a restriction. It describes transitions between equilibrium states but is not concerned with the intermediate states. The system does not have to pass through only equilibrium states. For example, if a gas in a steel container at a well-defined temperature and pressure is made to explode by means of a spark, some of the gas may condense, different gas molecules may combine to form new compounds, and there may be all sorts of turbulence in the container-but eventually, the system will settle down to a new equilibrium state. This system is clearly not in equilibrium during its transition; however, its behavior is still governed by the first law because the process starts and ends with the system in equilibrium states.

## EXAMPLE 3.3

## Polishing a Fitting

A machinist polishes a $0.50-\mathrm{kg}$ copper fitting with a piece of emery cloth for $2.0 \mathrm{~min}$. He moves the cloth across the fitting at a constant speed of $1.0 \mathrm{~m} / \mathrm{s}$ by applying a force of $20 \mathrm{~N}$, tangent to the surface of the fitting. (a) What is the total work done on the fitting by the machinist? (b) What is the increase in the internal energy of the fitting? Assume that the change in the internal energy of the cloth is negligible and that no heat is exchanged between the fitting and its environment. (c) What is the increase in the temperature of the fitting?

## Strategy

The machinist's force over a distance that can be calculated from the speed and time given is the work done on the system. The work, in turn, increases the internal energy of the system. This energy can be interpreted as the heat that raises the temperature of the system via its heat capacity. Be careful with the sign of each quantity.

## Solution

a. The power created by a force on an object or the rate at which the machinist does frictional work on the fitting is $\overrightarrow{\mathbf{F}} \cdot \overrightarrow{\mathbf{v}}=-\boldsymbol{F} \boldsymbol{v}$. Thus, in an elapsed time $\Delta t(2.0 \mathrm{~min})$, the work done on the fitting is

$$
\begin{aligned}
W & =-F v \Delta t=-(20 \mathrm{~N})(1.0 \mathrm{~m} / \mathrm{s})\left(1.2 \times 10^{2} \mathrm{~s}\right) \\
& =-2.4 \times 10^{3} \mathrm{~J}
\end{aligned}
$$

b. By assumption, no heat is exchanged between the fitting and its environment, so the first law gives for the change in the internal energy of the fitting:

$$
\Delta E_{\text {int }}=-W=2.4 \times 10^{3} \mathrm{~J}
$$

c. Since $\Delta E_{\text {int }}$ is path independent, the effect of the $2.4 \times 10^{3} \mathrm{~J}$ of work is the same as if it were supplied at atmospheric pressure by a transfer of heat. Thus,

$$
2.4 \times 10^{3} \mathrm{~J}=m c \Delta T=(0.50 \mathrm{~kg})\left(3.9 \times 10^{2} \mathrm{~J} / \mathrm{kg} \cdot{ }^{\circ} \mathrm{C}\right) \Delta T
$$

and the increase in the temperature of the fitting is

$$
\Delta T=12^{\circ} \mathrm{C}
$$

where we have used the value for the specific heat of copper, $c=3.9 \times 10^{2} \mathrm{~J} / \mathrm{kg} \cdot{ }^{\circ} \mathrm{C}$.

## Significance

If heat were released, the change in internal energy would be less and cause less of a temperature change than what was calculated in the problem.

## EXAMPLE 3.4

## An Ideal Gas Making Transitions between Two States

Consider the quasi-static expansions of an ideal gas between the equilibrium states $A$ and $C$ of Figure 3.6. If $515 \mathrm{~J}$ of heat are added to the gas as it traverses the path $A B C$, how much heat is required for the transition along $A D C$ ? Assume that $p_{1}=2.10 \times 10^{5} \mathrm{~N} / \mathrm{m}^{2}, p_{2}=1.05 \times 10^{5} \mathrm{~N} / \mathrm{m}^{2}, V_{1}=2.25 \times 10^{-3} \mathrm{~m}^{3}$, and $V_{2}=4.50 \times 10^{-3} \mathrm{~m}^{3}$.

## Strategy

The difference in work done between process $A B C$ and process $A D C$ is the area enclosed by $A B C D$. Because the change of the internal energy (a function of state) is the same for both processes, the difference in work is thus the same as the difference in heat transferred to the system.

## Solution

For path $A B C$, the heat added is $Q_{A B C}=515 \mathrm{~J}$ and the work done by the gas is the area under the path on the $p V$ diagram, which is

$$
W_{A B C}=p_{1}\left(V_{2}-V_{1}\right)=473 \mathrm{~J}
$$

Along $A D C$, the work done by the gas is again the area under the path:

$$
W_{A D C}=p_{2}\left(V_{2}-V_{1}\right)=236 \mathrm{~J}
$$

Then using the strategy we just described, we have

$$
Q_{A D C}-Q_{A B C}=W_{A D C}-W_{A B C}
$$

which leads to

$$
Q_{A D C}=Q_{A B C}+W_{A D C}-W_{A B C}=(515+236-473) \mathrm{J}=278 \mathrm{~J}
$$

## Significance

The work calculations in this problem are made simple since no work is done along $A D$ and $B C$ and along $A B$ and $D C$; the pressure is constant over the volume change, so the work done is simply $p \Delta V$. An isothermal line could also have been used, as we have derived the work for an isothermal process as $W=n R T \ln \frac{V_{2}}{V_{1}}$.

## EXAMPLE 3.5

## Isothermal Expansion of an Ideal Gas

Heat is added to $1 \mathrm{~mol}$ of an ideal monatomic gas confined to a cylinder with a movable piston at one end. The gas expands quasi-statically at a constant temperature of $300 \mathrm{~K}$ until its volume increases from $V$ to $3 V$. (a) What is the change in internal energy of the gas? (b) How much work does the gas do? (c) How much heat is added to the gas?

## Strategy

(a) Because the system is an ideal gas, the internal energy only changes when the temperature changes. (b) The heat added to the system is therefore purely used to do work that has been calculated in Work, Heat, and Internal Energy. (c) Lastly, the first law of thermodynamics can be used to calculate the heat added to the gas.

## Solution

a. We saw in the preceding section that the internal energy of an ideal monatomic gas is a function only of temperature. Since $\Delta T=0$, for this process, $\Delta E_{\text {int }}=0$.

b. The quasi-static isothermal expansion of an ideal gas was considered in the preceding section and was found to be

$$
\begin{aligned}
W & =n R T \ln \frac{V_{2}}{V_{1}}=n R T \ln \frac{3 V}{V} \\
& =(1.00 \mathrm{~mol})(8.314 \mathrm{~J} / \mathrm{K} \cdot \mathrm{mol})(300 \mathrm{~K})(\ln 3)=2.74 \times 10^{3} \mathrm{~J}
\end{aligned}
$$

c. With the results of parts (a) and (b), we can use the first law to determine the heat added:

$$
\Delta E_{\mathrm{int}}=Q-W=0
$$

which leads to

$$
Q=W=2.74 \times 10^{3} \mathrm{~J}
$$

## Significance

An isothermal process has no change in the internal energy. Based on that, the first law of thermodynamics reduces to $Q=W$.

## EXAMPLE 3.6

## Vaporizing Water

When $1.00 \mathrm{~g}$ of water at $100^{\circ} \mathrm{C}$ changes from the liquid to the gas phase at atmospheric pressure, its change in volume is $1.67 \times 10^{-3} \mathrm{~m}^{3}$. (a) How much heat must be added to vaporize the water? (b) How much work is done by the water against the atmosphere in its expansion? (c) What is the change in the internal energy of the water?

## Strategy

We can first figure out how much heat is needed from the latent heat of vaporization of the water. From the volume change, we can calculate the work done from $W=p \Delta V$ because the pressure is constant. Then, the first law of thermodynamics provides us with the change in the internal energy.

## Solution

a. With $L_{v}$ representing the latent heat of vaporization, the heat required to vaporize the water is

$$
Q=m L_{v}=(1.00 \mathrm{~g})\left(2.26 \times 10^{3} \mathrm{~J} / \mathrm{g}\right)=2.26 \times 10^{3} \mathrm{~J}
$$

b. Since the pressure on the system is constant at $1.00 \mathrm{~atm}=1.01 \times 10^{5} \mathrm{~N} / \mathrm{m}^{2}$, the work done by the water as it is vaporized is

$$
W=p \Delta V=\left(1.01 \times 10^{5} \mathrm{~N} / \mathrm{m}^{2}\right)\left(1.67 \times 10^{-3} \mathrm{~m}^{3}\right)=169 \mathrm{~J}
$$

c. From the first law, the thermal energy of the water during its vaporization changes by

$$
\Delta E_{\text {int }}=Q-W=2.26 \times 10^{3} \mathrm{~J}-169 \mathrm{~J}=2.09 \times 10^{3} \mathrm{~J}
$$

## Significance

We note that in part (c), we see a change in internal energy, yet there is no change in temperature. Ideal gases that are not undergoing phase changes have the internal energy proportional to temperature. Internal energy in general is the sum of all energy in the system.

### 3.4 Thermodynamic Processes

In solving mechanics problems, we isolate the body under consideration, analyze the external forces acting on it, and then use Newton's laws to predict its behavior. In thermodynamics, we take a similar approach. We start by identifying the part of the universe we wish to study; it is also known as our system. (We defined a system at the beginning of this chapter as anything whose properties are of interest to us; it can be a single atom or the entire Earth.) Once our system is selected, we determine how the environment, or surroundings, interact with the system. Finally, with the interaction understood, we study the thermal behavior of the system with the help of the laws of thermodynamics.

The thermal behavior of a system is described in terms of thermodynamic variables. For an ideal gas, these variables are pressure, volume, temperature, and the number of molecules or moles of the gas. Different types of systems are generally characterized by different sets of variables. For example, the thermodynamic variables for a stretched rubber band are tension, length, temperature, and mass.

The state of a system can change as a result of its interaction with the environment. The change in a system can be fast or slow and large or small. The manner in which a state of a system can change from an initial state to a final state is called a thermodynamic process. For analytical purposes in thermodynamics, it is helpful to divide up processes as either quasi-static or non-quasi-static, as we now explain.

## Quasi-static and Non-quasi-static Processes

A quasi-static process refers to an idealized or imagined process where the change in state is made infinitesimally slowly so that at each instant, the system can be assumed to be at a thermodynamic equilibrium with itself and with the environment. For instance, imagine heating $1 \mathrm{~kg}$ of water from a temperature $20^{\circ} \mathrm{C}$ to $21^{\circ} \mathrm{C}$ at a constant pressure of 1 atmosphere. To heat the water very slowly, we may imagine placing the container with water in a large bath that can be slowly heated such that the temperature of the bath can rise infinitesimally slowly from $20^{\circ} \mathrm{C}$ to $21^{\circ} \mathrm{C}$. If we put $1 \mathrm{~kg}$ of water at $20^{\circ} \mathrm{C}$ directly into a bath at $21^{\circ} \mathrm{C}$, the temperature of the water will rise rapidly to $21^{\circ} \mathrm{C}$ in a non-quasi-static way.

Quasi-static processes are done slowly enough that the system remains at thermodynamic equilibrium at each instant, despite the fact that the system changes over time. The thermodynamic equilibrium of the system is necessary for the system to have well-defined values of macroscopic properties such as the temperature and the pressure of the system at each instant of the process. Therefore, quasi-static processes can be shown as well-defined paths in state space of the system.

Since quasi-static processes cannot be completely realized for any finite change of the system, all processes in nature are non-quasi-static. Examples of quasi-static and non-quasi-static processes are shown in Figure 3.8. Despite the fact that all finite changes must occur essentially non-quasi-statically at some stage of the change, we can imagine performing infinitely many quasi-static process corresponding to every quasi-static process. Since quasi-static processes can be analyzed analytically, we mostly study quasi-static processes in this book. We have already seen that in a quasi-static process the work by a gas is given by $p d V$.

## Isothermal Processes

An isothermal process is a change in the state of the system at a constant temperature. This process is accomplished by keeping the system in thermal equilibrium with a large heat bath during the process. Recall that a heat bath is an idealized "infinitely" large system whose temperature does not change. In practice, the temperature of a finite bath is controlled by either adding or removing a finite amount of energy as the case may be.

As an illustration of an isothermal process, consider a cylinder of gas with a movable piston immersed in a large water tank whose temperature is maintained constant. Since the piston is freely movable, the pressure inside $P_{\text {in }}$ is balanced by the pressure outside $P_{\text {out }}$ by some weights on the piston, as in Figure 3.9.

As weights on the piston are removed, an imbalance of forces on the piston develops. The net nonzero force on the piston would cause the piston to accelerate, resulting in an increase in volume. The expansion of the gas cools the gas to a lower temperature, which makes it possible for the heat to enter from the heat bath into the system until the temperature of the gas is reset to the temperature of the heat bath. If weights are removed in infinitesimal steps, the pressure in the system decreases infinitesimally slowly. This way, an isothermal process can be conducted quasi-statically. An isothermal line on a ( $p, V$ ) diagram is represented by a curved line from starting point $A$ to finishing point $B$, as seen in Figure 3.10. For an ideal gas, an isothermal process is hyperbolic, since for an ideal gas at constant temperature, $p \propto \frac{1}{V}$.

An isothermal process studied in this chapter is quasi-statically performed, since to be isothermal throughout the change of volume, you must be able to state the temperature of the system at each step, which is possible only if the system is in thermal equilibrium continuously. The system must go out of equilibrium for the state to change, but for quasi-static processes, we imagine that the process is conducted in infinitesimal steps such that these departures from equilibrium can be made as brief and as small as we like.

Other quasi-static processes of interest for gases are isobaric and isochoric processes. An isobaric process is a process where the pressure of the system does not change, whereas an isochoric process is a process where the volume of the system does not change.

## Adiabatic Processes

In an adiabatic process, the system is insulated from its environment so that although the state of the system changes, no heat is allowed to enter or leave the system, as seen in Figure 3.11. An adiabatic process can be conducted either quasi-statically or non-quasi-statically. When a system expands adiabatically, it must do work against the outside world, and therefore its energy goes down, which is reflected in the lowering of the temperature of the system. An adiabatic expansion leads to a lowering of temperature, and an adiabatic compression leads to an increase of temperature. We discuss adiabatic expansion again in Adiabatic Processes for an ideal Gas.

## Cyclic Processes

We say that a system goes through a cyclic process if the state of the system at the end is same as the state at the beginning. Therefore, state properties such as temperature, pressure, volume, and internal energy of the system do not change over a complete cycle:

$$
\Delta E_{\mathrm{int}}=0
$$

When the first law of thermodynamics is applied to a cyclic process, we obtain a simple relation between heat into the system and the work done by the system over the cycle:

$$
Q=W \text { (cyclic process). }
$$

Thermodynamic processes are also distinguished by whether or not they are reversible. A reversible process is one that can be made to retrace its path by differential changes in the environment. Such a process must therefore also be quasi-static. Note, however, that a quasi-static process is not necessarily reversible, since there may be dissipative forces involved. For example, if friction occurred between the piston and the walls of the cylinder containing the gas, the energy lost to friction would prevent us from reproducing the original states of the system.

We considered several thermodynamic processes:

1. An isothermal process, during which the system's temperature remains constant
2. An adiabatic process, during which no heat is transferred to or from the system
3. An isobaric process, during which the system's pressure does not change
4. An isochoric process, during which the system's volume does not change

Many other processes also occur that do not fit into any of these four categories.

### 3.5 Heat Capacities of an Ideal Gas

We learned about specific heat and molar heat capacity in Temperature and Heat; however, we have not considered a process in which heat is added. We do that in this section. First, we examine a process where the system has a constant volume, then contrast it with a system at constant pressure and show how their specific heats are related.

Let's start with looking at Figure 3.12, which shows two vessels $A$ and $B$, each containing 1 mol of the same type of ideal gas at a temperature $T$ and a volume $V$. The only difference between the two vessels is that the piston at the top of $A$ is fixed, whereas the one at the top of $B$ is free to move against a constant external pressure $p$. We now consider what happens when the temperature of the gas in each vessel is slowly increased to $T+d T$ with the addition of heat.

Since the piston of vessel $A$ is fixed, the volume of the enclosed gas does not change. Consequently, the gas does no work, and we have from the first law

$$
d E_{\text {int }}=d Q-d W=d Q
$$

We represent the fact that the heat is exchanged at constant volume by writing

$$
d Q=C_{V} n d T
$$

where $C_{V}$ is the molar heat capacity at constant volume of the gas. In addition, since $d E_{\text {int }}=d Q$ for this particular process,

$$
d E_{\mathrm{int}}=C_{V} n d T
$$

We obtained this equation assuming the volume of the gas was fixed. However, internal energy is a state function that depends on only the temperature of an ideal gas. Therefore, $d E_{\text {int }}=C_{V} n d T$ gives the change in internal energy of an ideal gas for any process involving a temperature change $d T$.

When the gas in vessel $B$ is heated, it expands against the movable piston and does work $d W=p d V$. In this case, the heat is added at constant pressure, and we write

$$
d Q=C_{p} n d T
$$

where $C_{p}$ is the molar heat capacity at constant pressure of the gas. Furthermore, since the ideal gas expands against a constant pressure,

$$
d(p V)=d(R n T)
$$

becomes

$$
p d V=R n d T
$$

Finally, inserting the expressions for $d Q$ and $p d V$ into the first law, we obtain

$$
d E_{\mathrm{int}}=d Q-p d V=\left(C_{p} n-R n\right) d T
$$

We have found $d E_{\text {int }}$ for both an isochoric and an isobaric process. Because the internal energy of an ideal gas depends only on the temperature, $d E_{\text {int }}$ must be the same for both processes. Thus,

$$
C_{V} n d T=\left(C_{p} n-R n\right) d T
$$

and

$$
C_{p}=C_{V}+R
$$

The derivation of Equation 3.10 was based only on the ideal gas law. Consequently, this relationship is approximately valid for all dilute gases, whether monatomic like He, diatomic like $\mathrm{O}_{2}$, or polyatomic like $\mathrm{CO}_{2}$ or $\mathrm{NH}_{3}$.

In the preceding chapter, we found the molar heat capacity of an ideal gas under constant volume to be

$$
C_{V}=\frac{d}{2} R
$$

where $d$ is the number of degrees of freedom of a molecule in the system. Table 3.3 shows the molar heat capacities of some dilute ideal gases at room temperature. The heat capacities of real gases are somewhat higher than those predicted by the expressions of $C_{V}$ and $C_{p}$ given in Equation 3.10. This indicates that vibrational motion in polyatomic molecules is significant, even at room temperature. Nevertheless, the difference in the molar heat capacities, $C_{p}-C_{V}$, is very close to $R$, even for the polyatomic gases.

Molar Heat Capacities of Dilute Ideal Gases at Room Temperature

| Type of Molecule | Gas | $C_{p}$ <br> $(\mathrm{~J} / \mathrm{mol} \mathrm{K})$ | $C_{V}$ <br> $(\mathrm{~J} / \mathrm{mol} \mathrm{K})$ | $C_{p}-C_{V}$ <br> $(\mathrm{~J} / \mathrm{mol} \mathrm{K})$ |
| :--- | :---: | :---: | :---: | :---: |
| Monatomic | Ideal | $\frac{5}{2} R=20.79$ | $\frac{3}{2} R=12.47$ | $R=8.31$ |
| Diatomic | Ideal | $\frac{7}{2} R=29.10$ | $\frac{5}{2} R=20.79$ | $R=8.31$ |
| Polyatomic | Ideal | $4 R=33.26$ | $3 R=24.94$ | $R=8.31$ |

Table 3.3

### 3.6 Adiabatic Processes for an Ideal Gas

When an ideal gas is compressed adiabatically $(Q=0)$, work is done on it and its temperature increases; in an adiabatic expansion, the gas does work and its temperature drops. Adiabatic compressions actually occur in the cylinders of a car, where the compressions of the gas-air mixture take place so quickly that there is no time for the mixture to exchange heat with its environment. Nevertheless, because work is done on the mixture during the compression, its temperature does rise significantly. In fact, the temperature increases can be so large that the mixture can explode without the addition of a spark. Such explosions, since they are not timed, make a car run poorly-it usually "knocks." Because ignition temperature rises with the octane of gasoline, one way to overcome this problem is to use a higher-octane gasoline.

Another interesting adiabatic process is the free expansion of a gas. Figure 3.13 shows a gas confined by a membrane to one side of a two-compartment, thermally insulated container. When the membrane is punctured, gas rushes into the empty side of the container, thereby expanding freely. Because the gas expands "against a vacuum" $(p=0)$, it does no work, and because the vessel is thermally insulated, the expansion is adiabatic. With $Q=0$ and $W=0$ in the first law, $\Delta E_{\text {int }}=0$, so $E_{\text {int } i}=E_{\text {int } f}$ for the free expansion.

If the gas is ideal, the internal energy depends only on the temperature. Therefore, when an ideal gas expands freely, its temperature does not change.

A quasi-static, adiabatic expansion of an ideal gas is represented in Figure 3.14, which shows an insulated cylinder that contains $1 \mathrm{~mol}$ of an ideal gas. The gas is made to expand quasi-statically by removing one grain of sand at a time from the top of the piston. When the gas expands by $d V$, the change in its temperature is $d T$. The work done by the gas in the expansion is $d W=p d V ; d Q=0$ because the cylinder is insulated; and the change in the internal energy of the gas is, from Equation 3.9, $d E_{\text {int }}=C_{V} n d T$. Therefore, from the first law,

$$
C_{V} n d T=0-p d V=-p d V
$$

so

$$
d T=-\frac{p d V}{C_{V} n}
$$

Also, for $1 \mathrm{~mol}$ of an ideal gas,

$$
d(p V)=d(R n T)
$$

so

$$
p d V+V d p=R n d T
$$

and

$$
d T=\frac{p d V+V d p}{R n}
$$

We now have two equations for $d T$. Upon equating them, we find that

$$
C_{V} n V d p+\left(C_{V} n+R n\right) p d V=0
$$

Now, we divide this equation by $n p V$ and use $C_{p}=C_{V}+R$. We are then left with

$$
C_{V} \frac{d p}{p}+C_{p} \frac{d V}{V}=0
$$

which becomes

$$
\frac{d p}{p}+\gamma \frac{d V}{V}=0
$$

where we define $\gamma$ as the ratio of the molar heat capacities:

$$
\gamma=\frac{C_{p}}{C_{V}}
$$

Thus,

$$
\int \frac{d p}{p}+\gamma \int \frac{d V}{V}=0
$$

and

$$
\ln p+\gamma \ln V=\text { constant. }
$$

Finally, using $\ln \left(A^{x}\right)=x \ln A$ and $\ln A B=\ln A+\ln B$, we can write this in the form

$$
p V^{\gamma}=\text { constant }
$$

This equation is the condition that must be obeyed by an ideal gas in a quasi-static adiabatic process. For example, if an ideal gas makes a quasi-static adiabatic transition from a state with pressure and volume $p_{1}$ and $V_{1}$ to a state with $p_{2}$ and $V_{2}$, then it must be true that $p_{1} V_{1}^{\gamma}=p_{2} V_{2}^{\gamma}$.

The adiabatic condition of Equation 3.12 can be written in terms of other pairs of thermodynamic variables by combining it with the ideal gas law. In doing this, we find that

$$
p^{1-\gamma} T^{\gamma}=\text { constant }
$$

and

$$
T V^{\gamma-1}=\text { constant }
$$

A reversible adiabatic expansion of an ideal gas is represented on the $p V$ diagram of Figure 3.15. The slope of the curve at any point is

$$
\frac{d p}{d V}=\frac{d}{d V}\left(\frac{\text { constant }}{V^{\gamma}}\right)=-\gamma \frac{p}{V}
$$

The dashed curve shown on this $p V$ diagram represents an isothermal expansion where $T$ (and therefore $p V$ ) is constant. The slope of this curve is useful when we consider the second law of thermodynamics in the next chapter. This slope is

$$
\frac{d p}{d V}=\frac{d}{d V} \frac{n R T}{V}=-\frac{p}{V}
$$

Because $\gamma>1$, the isothermal curve is not as steep as that for the adiabatic expansion.

## EXAMPLE 3.7

## Compression of an Ideal Gas in an Automobile Engine

Gasoline vapor is injected into the cylinder of an automobile engine when the piston is in its expanded position. The temperature, pressure, and volume of the resulting gas-air mixture are $20^{\circ} \mathrm{C}, 1.00 \times 10^{5} \mathrm{~N} / \mathrm{m}^{2}$, and $240 \mathrm{~cm}^{3}$, respectively. The mixture is then compressed adiabatically to a volume of $40 \mathrm{~cm}^{3}$. Note that in the actual operation of an automobile engine, the compression is not quasi-static, although we are making that assumption here. (a) What are the pressure and temperature of the mixture after the compression? (b) How much work is done by the mixture during the compression?

## Strategy

Because we are modeling the process as a quasi-static adiabatic compression of an ideal gas, we have $p V^{\gamma}=$ constant and $p V=n R T$. The work needed can then be evaluated with $W=\int_{V_{1}}^{V_{2}} p d V$.

## Solution

a. For an adiabatic compression we have

$$
p_{2}=p_{1}\left(\frac{V_{1}}{V_{2}}\right)^{\gamma}
$$

so after the compression, the pressure of the mixture is

$$
p_{2}=\left(1.00 \times 10^{5} \mathrm{~N} / \mathrm{m}^{2}\right)\left(\frac{240 \times 10^{-6} \mathrm{~m}^{3}}{40 \times 10^{-6} \mathrm{~m}^{3}}\right)^{1.40}=1.23 \times 10^{6} \mathrm{~N} / \mathrm{m}^{2}
$$

From the ideal gas law, the temperature of the mixture after the compression is

$$
\begin{aligned}
T_{2} & =\left(\frac{p_{2} V_{2}}{p_{1} V_{1}}\right) T_{1} \\
& =\frac{\left(1.23 \times 10^{6} \mathrm{~N} / \mathrm{m}^{2}\right)\left(40 \times 10^{-6} \mathrm{~m}^{3}\right)}{\left(1.00 \times 10^{5} \mathrm{~N} / \mathrm{m}^{2}\right)\left(240 \times 10^{-6} \mathrm{~m}^{3}\right)} \cdot 293 \mathrm{~K} \\
& =600 \mathrm{~K}=328^{\circ} \mathrm{C}
\end{aligned}
$$

b. The work done by the mixture during the compression is

$$
W=\int_{V_{1}}^{V_{2}} p d V
$$

With the adiabatic condition of Equation 3.12, we may write $p$ as $K / V^{\gamma}$, where $K=p_{1} V_{1}^{\gamma}=p_{2} V_{2}^{\gamma}$. The work is therefore

$$
\begin{aligned}
W & =\int_{V_{1}}^{V_{2}} \frac{K}{V^{\gamma}} d V \\
& =\frac{K}{1-\gamma}\left(\frac{1}{V_{2}^{\gamma-1}}-\frac{1}{V_{1}^{\gamma-1}}\right) \\
& =\frac{1}{1-\gamma}\left(\frac{p_{2} V_{2}^{\gamma}}{V_{2}^{\gamma-1}}-\frac{p_{1} V_{1}^{\gamma}}{V_{1}^{\gamma-1}}\right) \\
& =\frac{1}{1-\gamma}\left(p_{2} V_{2}-p_{1} V_{1}\right) \\
& =\frac{1}{1-1.40}\left[\left(1.23 \times 10^{6} \mathrm{~N} / \mathrm{m}^{2}\right)\left(40 \times 10^{-6} \mathrm{~m}^{3}\right)\right. \\
& \left.-\left(1.00 \times 10^{5} \mathrm{~N} / \mathrm{m}^{2}\right)\left(240 \times 10^{-6} \mathrm{~m}^{3}\right)\right] \\
& =-63 \mathrm{~J}
\end{aligned}
$$

## Significance

The negative sign on the work done indicates that the piston does work on the gas-air mixture. The engine would not work if the gas-air mixture did work on the piston.

