# CHAPTER 4 <br> The Second Law of Thermodynamics 

INTRODUCTION According to the first law of thermodynamics, the only processes that can occur are those that conserve energy. But this cannot be the only restriction imposed by nature, because many seemingly possible thermodynamic processes that would conserve energy do not occur. For example, when two bodies are in thermal contact, heat never flows from the colder body to the warmer one, even though this is not
forbidden by the first law. So some other thermodynamic principles must be controlling the behavior of physical systems.

One such principle is the second law of thermodynamics, which limits the use of energy within a source. Energy cannot arbitrarily pass from one object to another, just as we cannot transfer heat from a cold object to a hot one without doing any work. We cannot unmix cream from coffee without a chemical process that changes the physical characteristics of the system or its environment. We cannot use internal energy stored in the air to propel a car, or use the energy of the ocean to run a ship, without disturbing something around that object.

In the chapter covering the first law of thermodynamics, we started our discussion with a joke by C. P. Snow stating that the first law means "you can't win." He paraphrased the second law as "you can't break even, except on a very cold day." Unless you are at zero kelvin, you cannot convert $100 \%$ of thermal energy into work. We start by discussing spontaneous processes and explain why some processes require work to occur even if energy would have been conserved.

### 4.1 Reversible and Irreversible Processes

Consider an ideal gas that is held in half of a thermally insulated container by a wall in the middle of the container. The other half of the container is under vacuum with no molecules inside. Now, if we remove the wall in the middle quickly, the gas expands and fills up the entire container immediately, as shown in Figure 4.2.

Because half of the container is under vacuum before the gas expands there, we do not expect any work to be done by the system-that is, $W=0$-because no force from the vacuum is exerted on the gas during the expansion. If the container is thermally insulated from the rest of the environment, we do not expect any heat transfer to the system either, so $Q=0$. Then the first law of thermodynamics leads to the change of the internal energy of the system,

$$
\Delta E_{\text {int }}=Q-W=0
$$

For an ideal gas, if the internal energy doesn't change, then the temperature stays the same. Thus, the equation of state of the ideal gas gives us the final pressure of the gas, $p=n R T / V=p_{0} / 2$, where $p_{0}$ is the pressure of the gas before the expansion. The volume is doubled and the pressure is halved, but nothing else seems to have changed during the expansion.

All of this discussion is based on what we have learned so far and makes sense. Here is what puzzles us: Can all the molecules go backward to the original half of the container in some future time? Our intuition tells us that this is going to be very unlikely, even though nothing we have learned so far prevents such an event from
happening, regardless of how small the probability is. What we are really asking is whether the expansion into the vacuum half of the container is reversible.

A reversible process is a process in which the system and environment can be restored to exactly the same initial states that they were in before the process occurred, if we go backward along the path of the process. The necessary condition for a reversible process is therefore the quasi-static requirement. Note that it is quite easy to restore a system to its original state; the hard part is to have its environment restored to its original state at the same time. For example, in the example of an ideal gas expanding into vacuum to twice its original volume, we can easily push it back with a piston and restore its temperature and pressure by removing some heat from the gas. The problem is that we cannot do it without changing something in its surroundings, such as dumping some heat there.

A reversible process is truly an ideal process that rarely happens. We can make certain processes close to reversible and therefore use the consequences of the corresponding reversible processes as a starting point or reference. In reality, almost all processes are irreversible, and some properties of the environment are altered when the properties of the system are restored. The expansion of an ideal gas, as we have just outlined, is irreversible because the process is not even quasi-static, that is, not in an equilibrium state at any moment of the expansion.

From the microscopic point of view, a particle described by Newton's second law can go backward if we flip the direction of time. But this is not the case, in practical terms, in a macroscopic system with more than $10^{23}$ particles or molecules, where numerous collisions between these molecules tend to erase any trace of memory of the initial trajectory of each of the particles. For example, we can actually estimate the chance for all the particles in the expanded gas to go back to the original half of the container, but the current age of the universe is still not long enough for it to happen even once.

An irreversible process is what we encounter in reality almost all the time. The system and its environment cannot be restored to their original states at the same time. Because this is what happens in nature, it is also called a natural process. The sign of an irreversible process comes from the finite gradient between the states occurring in the actual process. For example, when heat flows from one object to another, there is a finite temperature difference (gradient) between the two objects. More importantly, at any given moment of the process, the system most likely is not at equilibrium or in a well-defined state. This phenomenon is called irreversibility.

Let us see another example of irreversibility in thermal processes. Consider two objects in thermal contact: one at temperature $T_{1}$ and the other at temperature $T_{2}>T_{1}$, as shown in Figure 4.3.

We know from common personal experience that heat flows from a hotter object to a colder one. For example, when we hold a few pieces of ice in our hands, we feel cold because heat has left our hands into the ice. The opposite is true when we hold one end of a metal rod while keeping the other end over a fire. Based on all of the experiments that have been done on spontaneous heat transfer, the following statement summarizes the governing principle:

## Second Law of Thermodynamics (Clausius statement)

Heat never flows spontaneously from a colder object to a hotter object.

This statement turns out to be one of several different ways of stating the second law of thermodynamics. The form of this statement is credited to German physicist Rudolf Clausius (1822-1888) and is referred to as the Clausius statement of the second law of thermodynamics. The word "spontaneously" here means no other effort has been made by a third party, or one that is neither the hotter nor colder object. We will introduce some other major statements of the second law and show that they imply each other. In fact, all the different statements of the second law of thermodynamics can be shown to be equivalent, and all lead to the irreversibility of spontaneous heat flow between macroscopic objects of a very large number of molecules or particles.

Both isothermal and adiabatic processes sketched on a $p V$ graph (discussed in The First Law of Thermodynamics) are reversible in principle because the system is always at an equilibrium state at any point of the processes and can go forward or backward along the given curves. Other idealized processes can be represented by $p V$ curves; Table 4.1 summarizes the most common reversible processes.

Process Constant Quantity and Resulting Fact

| Isobaric | Constant pressure $W=p \Delta V$ |
| :--- | :--- |
| Isochoric | Constant volume $W=0$ |
| Isothermal | Constant temperature $\Delta T=0$ |
| Adiabatic | No heat transfer $Q=0$ |

Table 4.1 Summary of Simple Thermodynamic Processes

### 4.2 Heat Engines

A heat engine is a device used to extract heat from a source and then convert it into mechanical work that is used for all sorts of applications. For example, a steam engine on an old-style train can produce the work needed for driving the train. Several questions emerge from the construction and application of heat engines. For example, what is the maximum percentage of the heat extracted that can be used to do work? This turns out to be a question that can only be answered through the second law of thermodynamics.

The second law of thermodynamics can be formally stated in several ways. One statement presented so far is about the direction of spontaneous heat flow, known as the Clausius statement. A couple of other statements are based on heat engines. Whenever we consider heat engines and associated devices such as refrigerators and heat pumps, we do not use the normal sign convention for heat and work. For convenience, we assume that the symbols $Q_{\mathrm{h}}, Q_{\mathrm{c}}$, and $W$ represent only the amounts of heat transferred and work delivered, regardless what the givers or receivers are. Whether heat is entering or leaving a system and work is done to or by a system are indicated by proper signs in front of the symbols and by the directions of arrows in diagrams.

It turns out that we need more than one heat source/sink to construct a heat engine. We will come back to this point later in the chapter, when we compare different statements of the second law of thermodynamics. For the moment, we assume that a heat engine is constructed between a heat source (high-temperature reservoir or hot reservoir) and a heat sink (low-temperature reservoir or cold reservoir), represented schematically in Figure 4.4. The engine absorbs heat $Q_{\mathrm{h}}$ from a heat source (hot reservoir) of Kelvin temperature $T_{\mathrm{h}}$, uses some of that energy to produce useful work $W$, and then discards the remaining energy as heat $Q_{\mathrm{c}}$ into a heat sink (cold reservoir) of Kelvin temperature $T_{\mathrm{c}}$. Power plants and internal combustion engines are examples of
heat engines. Power plants use steam produced at high temperature to drive electric generators, while exhausting heat to the atmosphere or a nearby body of water in the role of the heat sink. In an internal combustion engine, a hot gas-air mixture is used to push a piston, and heat is exhausted to the nearby atmosphere in a similar manner.

Actual heat engines have many different designs. Examples include internal combustion engines, such as those used in most cars today, and external combustion engines, such as the steam engines used in old steamengine trains. Figure 4.5 shows a photo of a nuclear power plant in operation. The atmosphere around the reactors acts as the cold reservoir, and the heat generated from the nuclear reaction provides the heat from the hot reservoir.

Heat engines operate by carrying a working substance through a cycle. In a steam power plant, the working substance is water, which starts as a liquid, becomes vaporized, is then used to drive a turbine, and is finally condensed back into the liquid state. As is the case for all working substances in cyclic processes, once the water returns to its initial state, it repeats the same sequence.

For now, we assume that the cycles of heat engines are reversible, so there is no energy loss to friction or other irreversible effects. Suppose that the engine of Figure 4.4 goes through one complete cycle and that $Q_{\mathrm{h}}, Q_{\mathrm{c}}$, and $W$ represent the heats exchanged and the work done for that cycle. Since the initial and final states of the system are the same, $\Delta E_{\text {int }}=0$ for the cycle. We therefore have from the first law of thermodynamics,

$$
W=Q-\Delta E_{\text {int }}=\left(Q_{\mathrm{h}}-Q_{\mathrm{c}}\right)-0
$$

so that

$$
W=Q_{\mathrm{h}}-Q_{\mathrm{c}}
$$

The most important measure of a heat engine is its efficiency (e), which is simply "what we get out" divided by "what we put in" during each cycle, as defined by $e=W_{\text {out }} / Q_{\text {in }}$.

With a heat engine working between two heat reservoirs, we get out $W$ and put in $Q_{\mathrm{h}}$, so the efficiency of the engine is

$$
e=\frac{W}{Q_{\mathrm{h}}}=1-\frac{Q_{\mathrm{c}}}{Q_{\mathrm{h}}}
$$

Here, we used Equation 4.1, $W=Q_{\mathrm{h}}-Q_{\mathrm{c}}$, in the final step of this expression for the efficiency.

## EXAMPLE 4.1

## A Lawn Mower

A lawn mower is rated to have an efficiency of $25.0 \%$ and an average power of $3.00 \mathrm{~kW}$. What are (a) the average work and (b) the minimum heat discharge into the air by the lawn mower in one minute of use?

## Strategy

From the average power-that is, the rate of work production-we can figure out the work done in the given elapsed time. Then, from the efficiency given, we can figure out the minimum heat discharge $Q_{\mathrm{c}}=Q_{\mathrm{h}}(1-e)$ with $Q_{\mathrm{h}}=Q_{\mathrm{c}}+W$.

## Solution

a. The average work delivered by the lawn mower is

$$
W=P \Delta t=3.00 \times 10^{3} \times 60 \times 1.00 \mathrm{~J}=180 \mathrm{~kJ}
$$

b. The minimum heat discharged into the air is given by

$$
Q_{\mathrm{c}}=Q_{\mathrm{h}}(1-e)=\left(Q_{\mathrm{c}}+W\right)(1-e)
$$

which leads to

$$
Q_{\mathrm{c}}=W(1 / e-1)=180 \times(1 / 0.25-1) \mathrm{kJ}=540 \mathrm{~kJ}
$$

## Significance

As the efficiency rises, the minimum heat discharged falls. This helps our environment and atmosphere by not having as much waste heat expelled.

### 4.3 Refrigerators and Heat Pumps

The cycles we used to describe the engine in the preceding section are all reversible, so each sequence of steps can just as easily be performed in the opposite direction. In this case, the engine is known as a refrigerator or a heat pump, depending on what is the focus: the heat removed from the cold reservoir or the heat dumped to the hot reservoir. Either a refrigerator or a heat pump is an engine running in reverse. For a refrigerator, the focus is on removing heat from a specific area. For a heat pump, the focus is on dumping heat to a specific area.

We first consider a refrigerator (Figure 4.6). The purpose of this engine is to remove heat from the cold reservoir, which is the space inside the refrigerator for an actual household refrigerator or the space inside a building for an air-conditioning unit.

A refrigerator (or heat pump) absorbs heat $Q_{\mathrm{c}}$ from the cold reservoir at Kelvin temperature $T_{\mathrm{c}}$ and discards heat $Q_{\mathrm{h}}$ to the hot reservoir at Kelvin temperature $T_{\mathrm{h}}$, while work $W$ is done on the engine's working substance, as shown by the arrow pointing toward the system in the figure. A household refrigerator removes heat from the food within it while exhausting heat to the surrounding air. The required work, for which we pay in our electricity bill, is performed by the motor that moves a coolant through the coils. A schematic sketch of a household refrigerator is given in Figure 4.7.

The effectiveness or coefficient of performance $K_{\mathrm{R}}$ of a refrigerator is measured by the heat removed from
the cold reservoir divided by the work done by the working substance cycle by cycle:

$$
K_{\mathrm{R}}=\frac{Q_{\mathrm{c}}}{W}=\frac{Q_{\mathrm{c}}}{Q_{\mathrm{h}}-Q_{\mathrm{c}}}
$$

Note that we have used the condition of energy conservation, $W=Q_{\mathrm{h}}-Q_{\mathrm{c}}$, in the final step of this expression.

The effectiveness or coefficient of performance $K_{\mathrm{P}}$ of a heat pump is measured by the heat dumped to the hot reservoir divided by the work done to the engine on the working substance cycle by cycle:

$$
K_{\mathrm{P}}=\frac{Q_{\mathrm{h}}}{W}=\frac{Q_{\mathrm{h}}}{Q_{\mathrm{h}}-Q_{\mathrm{c}}}
$$

Once again, we use the energy conservation condition $W=Q_{\mathrm{h}}-Q_{\mathrm{c}}$ to obtain the final step of this expression.

### 4.4 Statements of the Second Law of Thermodynamics

Earlier in this chapter, we introduced the Clausius statement of the second law of thermodynamics, which is based on the irreversibility of spontaneous heat flow. As we remarked then, the second law of thermodynamics can be stated in several different ways, and all of them can be shown to imply the others. In terms of heat engines, the second law of thermodynamics may be stated as follows:

## Second Law of Thermodynamics (Kelvin statement)

It is impossible to convert the heat from a single source into work without any other effect.

This is known as the Kelvin statement of the second law of thermodynamics. This statement describes an unattainable "perfect engine," as represented schematically in Figure 4.8(a). Note that "without any other effect" is a very strong restriction. For example, an engine can absorb heat and turn it all into work, but not if it completes a cycle. Without completing a cycle, the substance in the engine is not in its original state and therefore an "other effect" has occurred. Another example is a chamber of gas that can absorb heat from a heat reservoir and do work isothermally against a piston as it expands. However, if the gas were returned to its initial state (that is, made to complete a cycle), it would have to be compressed and heat would have to be extracted from it.

The Kelvin statement is a manifestation of a well-known engineering problem. Despite advancing technology, we are not able to build a heat engine that is $100 \%$ efficient. The first law does not exclude the possibility of constructing a perfect engine, but the second law forbids it.

We can show that the Kelvin statement is equivalent to the Clausius statement if we view the two objects in the Clausius statement as a cold reservoir and a hot reservoir. Thus, the Clausius statement becomes: It is impossible to construct a refrigerator that transfers heat from a cold reservoir to a hot reservoir without aid from an external source. The Clausius statement is related to the everyday observation that heat never flows spontaneously from a cold object to a hot object. Heat transfer in the direction of increasing temperature always requires some energy input. A "perfect refrigerator," shown in Figure 4.8(b), which works without such external aid, is impossible to construct.

To prove the equivalence of the Kelvin and Clausius statements, we show that if one statement is false, it necessarily follows that the other statement is also false. Let us first assume that the Clausius statement is false, so that the perfect refrigerator of Figure 4.8(b) does exist. The refrigerator removes heat $Q$ from a cold reservoir at a temperature $T_{\mathrm{c}}$ and transfers all of it to a hot reservoir at a temperature $T_{\mathrm{h}}$. Now consider a real heat engine working in the same temperature range. It extracts heat $Q+\Delta Q$ from the hot reservoir, does work $W$, and discards heat $Q$ to the cold reservoir. From the first law, these quantities are related by $W=(Q+\Delta Q)-Q=\Delta Q$.

Suppose these two devices are combined as shown in Figure 4.9. The net heat removed from the hot reservoir is $\Delta Q$, no net heat transfer occurs to or from the cold reservoir, and work $W$ is done on some external body. Since $W=\Delta Q$, the combination of a perfect refrigerator and a real heat engine is itself a perfect heat engine, thereby contradicting the Kelvin statement. Thus, if the Clausius statement is false, the Kelvin statement must also be false.

Using the second law of thermodynamics, we now prove two important properties of heat engines operating between two heat reservoirs. The first property is that any reversible engine operating between two reservoirs has a greater efficiency than any irreversible engine operating between the same two reservoirs.

The second property to be demonstrated is that all reversible engines operating between the same two
reservoirs have the same efficiency. To show this, we start with the two engines D and E of Figure 4.10(a), which are operating between two common heat reservoirs at temperatures $T_{\mathrm{h}}$ and $T_{\mathrm{c}}$. First, we assume that D is a reversible engine and that $\mathrm{E}$ is a hypothetical irreversible engine that has a higher efficiency than $D$. If both engines perform the same amount of work $W$ per cycle, it follows from Equation 4.2 that $Q_{\mathrm{h}}>Q_{\mathrm{h}}^{\prime}$. It then follows from the first law that $Q_{\mathrm{c}}>Q_{\mathrm{c}}^{\prime}$.

Suppose the cycle of $\mathrm{D}$ is reversed so that it operates as a refrigerator, and the two engines are coupled such that the work output of E is used to drive D, as shown in Figure 4.10(b). Since $Q_{\mathrm{h}}>Q_{\mathrm{h}}^{\prime}$ and $Q_{\mathrm{c}}>Q_{\mathrm{c}}^{\prime}$, the net result of each cycle is equivalent to a spontaneous transfer of heat from the cold reservoir to the hot reservoir, a process the second law does not allow. The original assumption must therefore be wrong, and it is impossible to construct an irreversible engine such that $\mathrm{E}$ is more efficient than the reversible engine $\mathrm{D}$.

Now it is quite easy to demonstrate that the efficiencies of all reversible engines operating between the same reservoirs are equal. Suppose that D and E are both reversible engines. If they are coupled as shown in Figure 4.10(b), the efficiency of E cannot be greater than the efficiency of D, or the second law would be violated. If both engines are then reversed, the same reasoning implies that the efficiency of $\mathrm{D}$ cannot be greater than the efficiency of E. Combining these results leads to the conclusion that all reversible engines working between the same two reservoirs have the same efficiency.

### 4.5 The Carnot Cycle

In the early 1820s, Sadi Carnot (1786-1832), a French engineer, became interested in improving the efficiencies of practical heat engines. In 1824, his studies led him to propose a hypothetical working cycle with the highest possible efficiency between the same two reservoirs, known now as the Carnot cycle. An engine operating in this cycle is called a Carnot engine. The Carnot cycle is of special importance for a variety of reasons. At a practical level, this cycle represents a reversible model for the steam power plant and the refrigerator or heat pump. Yet, it is also very important theoretically, for it plays a major role in the
development of another important statement of the second law of thermodynamics. Finally, because only two reservoirs are involved in its operation, it can be used along with the second law of thermodynamics to define an absolute temperature scale that is truly independent of any substance used for temperature measurement.

With an ideal gas as the working substance, the steps of the Carnot cycle, as represented by Figure 4.11, are as follows.

1. Isothermal expansion. The gas is placed in thermal contact with a heat reservoir at a temperature $T_{\mathrm{h}}$. The gas absorbs heat $Q_{\mathrm{h}}$ from the heat reservoir and is allowed to expand isothermally, doing work $W_{1}$. Because the internal energy $E_{\text {int }}$ of an ideal gas is a function of the temperature only, the change of the internal energy is zero, that is, $\Delta E_{\text {int }}=0$ during this isothermal expansion. With the first law of thermodynamics, $\Delta E_{\text {int }}=Q-W$, we find that the heat absorbed by the gas is

$$
Q_{\mathrm{h}}=W_{1}=n R T_{\mathrm{h}} \ln \frac{V_{N}}{V_{M}}
$$

2. Adiabatic expansion. The gas is thermally isolated and allowed to expand further, doing work $W_{2}$. Because this expansion is adiabatic, the temperature of the gas falls-in this case, from $T_{\mathrm{h}}$ to $T_{\mathrm{c}}$. From $p V^{\gamma}=$ constant and the equation of state for an ideal gas, $p V=n R T$, we have

$$
T V^{\gamma-1}=\text { constant }
$$

so that

$$
T_{\mathrm{h}} V_{N}^{\gamma-1}=T_{\mathrm{c}} V_{O}^{\gamma-1}
$$

3. Isothermal compression. The gas is placed in thermal contact with a cold reservoir at temperature $T_{\mathrm{c}}$ and compressed isothermally. During this process, work $W_{3}$ is done on the gas and it gives up heat $Q_{\mathrm{c}}$ to the cold reservoir. The reasoning used in step 1 now yields

$$
Q_{\mathrm{c}}=n R T_{\mathrm{c}} \ln \frac{V_{O}}{V_{P}}
$$

where $Q_{\mathrm{c}}$ is the heat dumped to the cold reservoir by the gas.

4. Adiabatic compression. The gas is thermally isolated and returned to its initial state by compression. In this process, work $W_{4}$ is done on the gas. Because the compression is adiabatic, the temperature of the gas rises-from $T_{\mathrm{c}}$ to $T_{\mathrm{h}}$ in this particular case. The reasoning of step 2 now gives

$$
T_{\mathrm{c}} V_{P}^{\gamma-1}=T_{\mathrm{h}} V_{M}^{\gamma-1}
$$

The total work done by the gas in the Carnot cycle is given by

$$
W=W_{1}+W_{2}-W_{3}-W_{4}
$$

This work is equal to the area enclosed by the loop shown in the $p V$ diagram of Figure 4.12. Because the initial and final states of the system are the same, the change of the internal energy of the gas in the cycle must be zero, that is, $\Delta E_{\text {int }}=0$. The first law of thermodynamics then gives

$$
W=Q-\Delta E_{\text {int }}=\left(Q_{\mathrm{h}}-Q_{\mathrm{c}}\right)-0
$$

and

$$
W=Q_{\mathrm{h}}-Q_{\mathrm{c}}
$$

To find the efficiency of this engine, we first divide $Q_{\mathrm{c}}$ by $Q_{\mathrm{h}}$ :

$$
\frac{Q_{\mathrm{c}}}{Q_{\mathrm{h}}}=\frac{T_{\mathrm{c}}}{T_{\mathrm{h}}} \frac{\ln V_{O} / V_{P}}{\ln V_{N} / V_{M}}
$$

When the adiabatic constant from step 2 is divided by that of step 4, we find

$$
\frac{V_{O}}{V_{P}}=\frac{V_{N}}{V_{M}}
$$

Substituting this into the equation for $Q_{\mathrm{c}} / Q_{\mathrm{h}}$, we obtain

$$
\frac{Q_{\mathrm{c}}}{Q_{\mathrm{h}}}=\frac{T_{\mathrm{c}}}{T_{\mathrm{h}}}
$$

Finally, with Equation 4.2, we find that the efficiency of this ideal gas Carnot engine is given by

$$
e=1-\frac{T_{\mathrm{c}}}{T_{\mathrm{h}}}
$$

An engine does not necessarily have to follow a Carnot engine cycle. All engines, however, have the same net effect, namely the absorption of heat from a hot reservoir, the production of work, and the discarding of heat to a cold reservoir. This leads us to ask: Do all reversible cycles operating between the same two reservoirs have the same efficiency? The answer to this question comes from the second law of thermodynamics discussed earlier: All reversible engine cycles produce exactly the same efficiency. Also, as you might expect, all real engines operating between two reservoirs are less efficient than reversible engines operating between the same two reservoirs. This too is a consequence of the second law of thermodynamics shown earlier.

The cycle of an ideal gas Carnot refrigerator is represented by the $p V$ diagram of Figure 4.13. It is a Carnot engine operating in reverse. The refrigerator extracts heat $Q_{\mathrm{c}}$ from a cold-temperature reservoir at $T_{\mathrm{c}}$ when the ideal gas expands isothermally. The gas is then compressed adiabatically until its temperature reaches $T_{\mathrm{h}}$, after which an isothermal compression of the gas results in heat $Q_{\mathrm{h}}$ being discarded to a high-temperature reservoir at $T_{\mathrm{h}}$. Finally, the cycle is completed by an adiabatic expansion of the gas, causing its temperature to drop to $T_{\mathrm{c}}$.

The work done on the ideal gas is equal to the area enclosed by the path of the $p V$ diagram. From the first law, this work is given by

$$
W=Q_{\mathrm{h}}-Q_{\mathrm{c}}
$$

An analysis just like the analysis done for the Carnot engine gives

$$
\frac{Q_{\mathrm{c}}}{T_{\mathrm{c}}}=\frac{Q_{\mathrm{h}}}{T_{\mathrm{h}}}
$$

When combined with Equation 4.3, this yields

$$
K_{\mathrm{R}}=\frac{T_{\mathrm{c}}}{T_{\mathrm{h}}-T_{\mathrm{c}}}
$$

for the coefficient of performance of the ideal-gas Carnot refrigerator. Similarly, we can work out the coefficient of performance for a Carnot heat pump as

$$
K_{\mathrm{P}}=\frac{Q_{\mathrm{h}}}{Q_{\mathrm{h}}-Q_{\mathrm{c}}}=\frac{T_{\mathrm{h}}}{T_{\mathrm{h}}-T_{\mathrm{c}}}
$$

We have just found equations representing the efficiency of a Carnot engine and the coefficient of performance of a Carnot refrigerator or a Carnot heat pump, assuming an ideal gas for the working substance in both devices. However, these equations are more general than their derivations imply. We will soon show that they are both valid no matter what the working substance is.

Carnot summarized his study of the Carnot engine and Carnot cycle into what is now known as Carnot's principle:

## Carnot's Principle

No engine working between two reservoirs at constant temperatures can have a greater efficiency than a reversible engine.

This principle can be viewed as another statement of the second law of thermodynamics and can be shown to be equivalent to the Kelvin statement and the Clausius statement.

## The Carnot Engine

A Carnot engine has an efficiency of 0.60 and the temperature of its cold reservoir is $300 \mathrm{~K}$. (a) What is the temperature of the hot reservoir? (b) If the engine does $300 \mathrm{~J}$ of work per cycle, how much heat is removed from the high-temperature reservoir per cycle? (c) How much heat is exhausted to the low-temperature reservoir per cycle?

## Strategy

From the temperature dependence of the thermal efficiency of the Carnot engine, we can find the temperature of the hot reservoir. Then, from the definition of the efficiency, we can find the heat removed when the work done by the engine is given. Finally, energy conservation will lead to how much heat must be dumped to the cold reservoir.

## Solution

a. From $e=1-T_{\mathrm{c}} / T_{\mathrm{h}}$ we have

$$
0.60=1-\frac{300 \mathrm{~K}}{T_{\mathrm{h}}}
$$

so that the temperature of the hot reservoir is

$$
T_{\mathrm{h}}=\frac{300 \mathrm{~K}}{1-0.60}=750 \mathrm{~K}
$$

b. By definition, the efficiency of the engine is $e=W / Q$, so that the heat removed from the high-temperature reservoir per cycle is

$$
Q_{\mathrm{h}}=\frac{W}{e}=\frac{300 \mathrm{~J}}{0.60}=500 \mathrm{~J}
$$

c. From the first law, the heat exhausted to the low-temperature reservoir per cycle by the engine is

$$
Q_{\mathrm{c}}=Q_{\mathrm{h}}-W=500 \mathrm{~J}-300 \mathrm{~J}=200 \mathrm{~J}
$$

## Significance

A Carnot engine has the maximum possible efficiency of converting heat into work between two reservoirs, but this does not necessarily mean it is $100 \%$ efficient. As the difference in temperatures of the hot and cold reservoir increases, the efficiency of a Carnot engine increases.

## EXAMPLE 4.3

## A Carnot Heat Pump

Imagine a Carnot heat pump operates between an outside temperature of $0{ }^{\circ} \mathrm{C}$ and an inside temperature of $20.0^{\circ} \mathrm{C}$. What is the work needed if the heat delivered to the inside of the house is $30.0 \mathrm{~kJ}$ ?

## Strategy

Because the heat pump is assumed to be a Carnot pump, its performance coefficient is given by $K_{\mathrm{P}}=Q_{\mathrm{h}} / W=T_{\mathrm{h}} /\left(T_{\mathrm{h}}-T_{\mathrm{c}}\right)$. Thus, we can find the work $W$ from the heat delivered $Q_{\mathrm{h}}$.

## Solution

The work needed is obtained from

$$
W=Q_{\mathrm{h}} / K_{\mathrm{P}}=Q_{\mathrm{h}}\left(T_{\mathrm{h}}-T_{\mathrm{c}}\right) / T_{\mathrm{h}}=30 \mathrm{~kJ} \times(293 \mathrm{~K}-273 \mathrm{~K}) / 293 \mathrm{~K}=2 \mathrm{~kJ}
$$

## Significance

We note that this work depends not only on the heat delivered to the house but also on the temperatures outside and inside. The dependence on the temperature outside makes them impractical to use in areas where
the temperature is much colder outside than room temperature.

In terms of energy costs, the heat pump is a very economical means for heating buildings (Figure 4.14). Contrast this method with turning electrical energy directly into heat with resistive heating elements. In this case, one unit of electrical energy furnishes at most only one unit of heat. Unfortunately, heat pumps have problems that do limit their usefulness. They are quite expensive to purchase compared to resistive heating elements, and, as the performance coefficient for a Carnot heat pump shows, they become less effective as the outside temperature decreases. In fact, below about $-10^{\circ} \mathrm{C}$, the heat they furnish is less than the energy used to operate them.

### 4.6 Entropy

The second law of thermodynamics is best expressed in terms of a change in the thermodynamic variable known as entropy, which is represented by the symbol $S$. Entropy, like internal energy, is a state function. This means that when a system makes a transition from one state into another, the change in entropy $\Delta S$ is independent of path and depends only on the thermodynamic variables of the two states.

We first consider $\Delta S$ for a system undergoing a reversible process at a constant temperature. In this case, the change in entropy of the system is given by

$$
\Delta S=\frac{Q}{T}
$$

where $Q$ is the heat exchanged by the system kept at a temperature $T$ (in kelvin). If the system absorbs heat-that is, with $Q>0$-the entropy of the system increases. As an example, suppose a gas is kept at a constant temperature of $300 \mathrm{~K}$ while it absorbs $10 \mathrm{~J}$ of heat in a reversible process. Then from Equation 4.8, the entropy change of the gas is

$$
\Delta S=\frac{10 \mathrm{~J}}{300 \mathrm{~K}}=0.033 \mathrm{~J} / \mathrm{K}
$$

Similarly, if the gas loses $5.0 \mathrm{~J}$ of heat; that is, $Q=-5.0 \mathrm{~J}$, at temperature $T=200 \mathrm{~K}$, we have the entropy change of the system given by

$$
\Delta S=\frac{-5.0 \mathrm{~J}}{200 \mathrm{~K}}=-0.025 \mathrm{~J} / \mathrm{K}
$$

## EXAMPLE 4.4

## Entropy Change of Melting Ice

Heat is slowly added to a $50-\mathrm{g}$ chunk of ice at $0{ }^{\circ} \mathrm{C}$ until it completely melts into water at the same temperature. What is the entropy change of the ice?

## Strategy

Because the process is slow, we can approximate it as a reversible process. The temperature is a constant, and we can therefore use Equation 4.8 in the calculation.

## Solution

The ice is melted by the addition of heat:

$$
Q=m L_{\mathrm{f}}=50 \mathrm{~g} \times 335 \mathrm{~J} / \mathrm{g}=16.8 \mathrm{~kJ}
$$

In this reversible process, the temperature of the ice-water mixture is fixed at $0^{\circ} \mathrm{C}$ or $273 \mathrm{~K}$. Now from $\Delta S=Q / T$, the entropy change of the ice is

$$
\Delta S=\frac{16.8 \mathrm{~kJ}}{273 \mathrm{~K}}=61.5 \mathrm{~J} / \mathrm{K}
$$

when it melts to water at $0^{\circ} \mathrm{C}$.

## Significance

During a phase change, the temperature is constant, allowing us to use Equation 4.8 to solve this problem. The same equation could also be used if we changed from a liquid to a gas phase, since the temperature does not change during that process either.

The change in entropy of a system for an arbitrary, reversible transition for which the temperature is not necessarily constant is defined by modifying $\Delta S=Q / T$. Imagine a system making a transition from state $A$ to $B$ in small, discrete steps. The temperatures associated with these states are $T_{A}$ and $T_{B}$, respectively. During each step of the transition, the system exchanges heat $\Delta Q_{i}$ reversibly at a temperature $T_{i}$. This can be accomplished experimentally by placing the system in thermal contact with a large number of heat reservoirs of varying temperatures $T_{i}$, as illustrated in Figure 4.15. The change in entropy for each step is $\Delta S_{i}=Q_{i} / T_{i}$. The net change in entropy of the system for the transition is

$$
\Delta S=S_{B}-S_{A}=\sum_{i} \Delta S_{i}=\sum_{i} \frac{\Delta Q_{i}}{T_{i}}
$$

We now take the limit as $\Delta Q_{i} \rightarrow 0$, and the number of steps approaches infinity. Then, replacing the summation by an integral, we obtain

$$
\Delta S=S_{B}-S_{A}=\int_{A}^{B} \frac{d Q}{T}
$$

where the integral is taken between the initial state $A$ and the final state $B$. This equation is valid only if the transition from $A$ to $B$ is reversible.

As an example, let us determine the net entropy change of a reversible engine while it undergoes a single Carnot cycle. In the adiabatic steps 2 and 4 of the cycle shown in Figure 4.11, no heat exchange takes place, so $\Delta S_{2}=\Delta S_{4}=\int d Q / T=0$. In step 1, the engine absorbs heat $Q_{\mathrm{h}}$ at a temperature $T_{\mathrm{h}}$, so its entropy change is $\Delta S_{1}=Q_{\mathrm{h}} / T_{\mathrm{h}}$. Similarly, in step $3, \Delta S_{3}=-Q_{\mathrm{c}} / T_{\mathrm{c}}$. The net entropy change of the engine in one cycle of operation is then

$$
\Delta S_{E}=\Delta S_{1}+\Delta S_{2}+\Delta S_{3}+\Delta S_{4}=\frac{Q_{\mathrm{h}}}{T_{\mathrm{h}}}-\frac{Q_{\mathrm{c}}}{T_{\mathrm{c}}}
$$

However, we know that for a Carnot engine,

$$
\frac{Q_{\mathrm{h}}}{T_{\mathrm{h}}}=\frac{Q_{\mathrm{c}}}{T_{\mathrm{c}}}
$$

so

$$
\Delta S_{E}=0
$$

There is no net change in the entropy of the Carnot engine over a complete cycle. Although this result was obtained for a particular case, its validity can be shown to be far more general: There is no net change in the entropy of a system undergoing any complete reversible cyclic process. Mathematically, we write this statement as

$$
\oint d S=\oint \frac{d Q}{T}=0
$$

where $\oint$ represents the integral over a closed reversible path.

We can use Equation 4.11 to show that the entropy change of a system undergoing a reversible process between two given states is path independent. An arbitrary, closed path for a reversible cycle that passes through the states $A$ and $B$ is shown in Figure 4.16. From Equation 4.11, $\oint d S=0$ for this closed path. We may split this integral into two segments, one along I, which leads from $A$ to $B$, the other along II, which leads
from $B$ to $A$. Then

$$
\left[\int_{A}^{B} d S\right]_{\mathrm{I}}+\left[\int_{B}^{A} d S\right]_{\mathrm{II}}=0
$$

Since the process is reversible,

$$
\left[\int_{A}^{B} d S\right]_{\mathrm{I}}=\left[\int_{A}^{B} d S\right]_{\mathrm{II}}
$$

Hence, the entropy change in going from $A$ to $B$ is the same for paths I and II. Since paths I and II are arbitrary, reversible paths, the entropy change in a transition between two equilibrium states is the same for all the reversible processes joining these states. Entropy, like internal energy, is therefore a state function.

What happens if the process is irreversible? When the process is irreversible, we expect the entropy of a closed system, or the system and its environment (the universe), to increase. Therefore we can rewrite this expression as

$$
\Delta S \geq 0
$$

where $S$ is the total entropy of the closed system or the entire universe, and the equal sign is for a reversible process. The fact is the entropy statement of the second law of thermodynamics:

## Second Law of Thermodynamics (Entropy statement)

The entropy of a closed system and the entire universe never decreases.

We can show that this statement is consistent with the Kelvin statement, the Clausius statement, and the Carnot principle.

## EXAMPLE 4.5

## Entropy Change of a System during an Isobaric Process

Determine the entropy change of an object of mass $m$ and specific heat $c$ that is cooled rapidly (and irreversibly) at constant pressure from $T_{\mathrm{h}}$ to $T_{\mathrm{c}}$.

## Strategy

The process is clearly stated as an irreversible process; therefore, we cannot simply calculate the entropy change from the actual process. However, because entropy of a system is a function of state, we can imagine a
reversible process that starts from the same initial state and ends at the given final state. Then, the entropy change of the system is given by Equation 4.10, $\Delta S=\int_{A}^{B} d Q / T$.

## Solution

To replace this rapid cooling with a process that proceeds reversibly, we imagine that the hot object is put into thermal contact with successively cooler heat reservoirs whose temperatures range from $T_{\mathrm{h}}$ to $T_{\mathrm{c}}$. Throughout the substitute transition, the object loses infinitesimal amounts of heat $d Q$, so we have

$$
\Delta S=\int_{T_{\mathrm{h}}}^{T_{\mathrm{c}}} \frac{d Q}{T}
$$

From the definition of heat capacity, an infinitesimal exchange $d Q$ for the object is related to its temperature change $d T$ by

$$
d Q=m c d T
$$

Substituting this $d Q$ into the expression for $\Delta S$, we obtain the entropy change of the object as it is cooled at constant pressure from $T_{\mathrm{h}}$ to $T_{\mathrm{c}}$ :

$$
\Delta S=\int_{T_{\mathrm{h}}}^{T_{\mathrm{c}}} \frac{m c d T}{T}=m c \ln \frac{T_{\mathrm{c}}}{T_{\mathrm{h}}}
$$

Note that $\Delta S<0$ here because $T_{\mathrm{c}}<T_{\mathrm{h}}$. In other words, the object has lost some entropy. But if we count whatever is used to remove the heat from the object, we would still end up with $\Delta S_{\text {universe }}>0$ because the process is irreversible.

## Significance

If the temperature changes during the heat flow, you must keep it inside the integral to solve for the change in entropy. If, however, the temperature is constant, you can simply calculate the entropy change as the heat flow divided by the temperature.

## EXAMPLE 4.6

## Stirling Engine

The steps of a reversible Stirling engine are as follows. For this problem, we will use $0.0010 \mathrm{~mol}$ of a monatomic gas that starts at a temperature of $133^{\circ} \mathrm{C}$ and a volume of $0.10 \mathrm{~m}^{3}$, which will be called point $A$. Then it goes through the following steps:

1. Step $A B$ : isothermal expansion at $133^{\circ} \mathrm{C}$ from $0.10 \mathrm{~m}^{3}$ to $0.20 \mathrm{~m}^{3}$
2. Step $B C$ : isochoric cooling to $33^{\circ} \mathrm{C}$
3. Step $C D$ : isothermal compression at $33^{\circ} \mathrm{C}$ from $0.20 \mathrm{~m}^{3}$ to $0.10 \mathrm{~m}^{3}$
4. Step $D A$ : isochoric heating back to $133^{\circ} \mathrm{C}$ and $0.10 \mathrm{~m}^{3}$

(a) Draw the $p V$ diagram for the Stirling engine with proper labels.

(b) Fill in the following table.

| Step | $W(\mathrm{~J})$ | $Q(\mathrm{~J})$ | $\Delta S(\mathrm{~J} / \mathrm{K})$ |
| :--- | :--- | :--- | :--- |
| Step $A B$ |  |  |  |
| Step $B C$ |  |  |  |


| Step | $W(\mathrm{~J})$ | $Q(\mathrm{~J})$ | $\Delta S(\mathrm{~J} / \mathrm{K})$ |
| :--- | :--- | :--- | :--- |
| Step $C D$ |  |  |  |
| Step $D A$ |  |  |  |
| Complete cycle |  |  |  |

(c) How does the efficiency of the Stirling engine compare to the Carnot engine working within the same two heat reservoirs?

## Strategy

Using the ideal gas law, calculate the pressure at each point so that they can be labeled on the $p V$ diagram. Isothermal work is calculated using $W=n R T \ln \left(\frac{V_{2}}{V_{1}}\right)$, and an isochoric process has no work done. The heat flow is calculated from the first law of thermodynamics, $Q=\Delta E_{\text {int }}-W$ where $\Delta E_{\text {int }}=\frac{3}{2} n R \Delta T$ for monatomic gasses. Isothermal steps have a change in entropy of $Q / T$, whereas isochoric steps have $\Delta S=\frac{3}{2} n R \ln \left(\frac{T_{2}}{T_{1}}\right)$. The efficiency of a heat engine is calculated by using $e_{S t i r}=W / Q_{\mathrm{h}}$.

## Solution

b. The completed table is shown below.

| Step | $W(\mathrm{~J})$ | $Q(\mathrm{~J})$ | $\Delta S(\mathrm{~J} / \mathrm{K})$ |
| :--- | :--- | :--- | :--- |
| Step $A B$ Isotherm | 2.3 | 2.3 | 0.0057 |
| Step $B C$ Isochoric | 0 | -1.2 | 0.0035 |
| Step $C D$ Isotherm | -1.8 | -1.8 | -0.0059 |
| Step DA Isochoric | 0 | 1.2 | -0.0035 |
| Complete cycle | 0.5 | 0.5 | $\sim 0$ |

c. The efficiency of the Stirling heat engine is

$$
e_{\text {Stir }}=W / Q_{\mathrm{h}}=\left(Q_{A B}+Q_{C D}\right) /\left(Q_{A B}+Q_{D A}\right)=0.5 / 3.5=0.14
$$

If this were a Carnot engine operating between the same heat reservoirs, its efficiency would be

$$
e_{\mathrm{Car}}=1-\left(\frac{T_{\mathrm{c}}}{T_{\mathrm{h}}}\right)=0.25
$$

Therefore, the Carnot engine would have a greater efficiency than the Stirling engine.

## Significance

In the early days of steam engines, accidents would occur due to the high pressure of the steam in the boiler. Robert Stirling developed an engine in 1816 that did not use steam and therefore was safer. The Stirling engine was commonly used in the nineteenth century, but developments in steam and internal combustion engines have made it difficult to broaden the use of the Stirling engine.

The Stirling engine uses compressed air as the working substance, which passes back and forth between two chambers with a porous plug, called the regenerator, which is made of material that does not conduct heat as well. In two of the steps, pistons in the two chambers move in phase.

### 4.7 Entropy on a Microscopic Scale

We have seen how entropy is related to heat exchange at a particular temperature. In this section, we consider entropy from a statistical viewpoint. Although the details of the argument are beyond the scope of this textbook, it turns out that entropy can be related to how disordered or randomized a system is-the more it is disordered, the higher is its entropy. For example, a new deck of cards is very ordered, as the cards are arranged numerically by suit. In shuffling this new deck, we randomize the arrangement of the cards and therefore increase its entropy (Figure 4.17). Thus, by picking one card off the top of the deck, there would be no indication of what the next selected card will be.

The second law of thermodynamics requires that the entropy of the universe increase in any irreversible process. Thus, in terms of order, the second law may be stated as follows:

In any irreversible process, the universe becomes more disordered. For example, the irreversible free expansion of an ideal gas, shown in Figure 4.2, results in a larger volume for the gas molecules to occupy. A larger volume means more possible arrangements for the same number of atoms, so disorder is also increased. As a result, the entropy of the gas has gone up. The gas in this case is a closed system, and the
process is irreversible. Changes in phase also illustrate the connection between entropy and disorder.

## EXAMPLE 4.7

## Entropy Change of the Universe

Suppose we place $50 \mathrm{~g}$ of ice at $0^{\circ} \mathrm{C}$ in contact with a heat reservoir at $20^{\circ} \mathrm{C}$. Heat spontaneously flows from the reservoir to the ice, which melts and eventually reaches a temperature of $20^{\circ} \mathrm{C}$. Find the change in entropy of (a) the ice and (b) the universe.

## Strategy

Because the entropy of a system is a function of its state, we can imagine two reversible processes for the ice: (1) ice is melted at $0{ }^{\circ} \mathrm{C}\left(T_{A}\right)$; and (2) melted ice (water) is warmed up from $0{ }^{\circ} \mathrm{C}$ to $20^{\circ} \mathrm{C}\left(T_{B}\right)$ under constant pressure. Then, we add the change in entropy of the reservoir when we calculate the change in entropy of the universe.

## Solution

a. From Equation 4.10, the increase in entropy of the ice is

$$
\begin{aligned}
\Delta S_{\text {ice }} & =\Delta S_{1}+\Delta S_{2} \\
& =\frac{m L_{f}}{T_{A}}+m c \int_{A}^{B} \frac{d T}{T} \\
& =\left(\frac{50 \times 335}{273}+50 \times 4.19 \times \ln \frac{293}{273}\right) \mathrm{J} / \mathrm{K} \\
& =76.3 \mathrm{~J} / \mathrm{K}
\end{aligned}
$$

b. During this transition, the reservoir gives the ice an amount of heat equal to

$$
\begin{aligned}
Q & =m L_{f}+m c\left(T_{B}-T_{A}\right) \\
& =50 \times(335+4.19 \times 20) \mathrm{J} \\
& =2.10 \times 10^{4} \mathrm{~J}
\end{aligned}
$$

This leads to a change (decrease) in entropy of the reservoir:

$$
\Delta S_{\text {reservoir }}=\frac{-Q}{T_{B}}=-71.7 \mathrm{~J} / \mathrm{K}
$$

The increase in entropy of the universe is therefore

$$
\Delta S_{\text {universe }}=76.3 \mathrm{~J} / \mathrm{K}-71.7 \mathrm{~J} / \mathrm{K}=4.6 \mathrm{~J} / \mathrm{K}>0
$$

## Significance

The entropy of the universe therefore is greater than zero since the ice gains more entropy than the reservoir loses. If we considered only the phase change of the ice into water and not the temperature increase, the entropy change of the ice and reservoir would be the same, resulting in the universe gaining no entropy.

This process also results in a more disordered universe. The ice changes from a solid with molecules located at specific sites to a liquid whose molecules are much freer to move. The molecular arrangement has therefore become more randomized. Although the change in average kinetic energy of the molecules of the heat reservoir is negligible, there is nevertheless a significant decrease in the entropy of the reservoir because it has many more molecules than the melted ice cube. However, the reservoir's decrease in entropy is still not as large as the increase in entropy of the ice. The increased disorder of the ice more than compensates for the increased order of the reservoir, and the entropy of the universe increases by $4.6 \mathrm{~J} / \mathrm{K}$.

You might suspect that the growth of different forms of life might be a net ordering process and therefore a violation of the second law. After all, a single cell gathers molecules and eventually becomes a highly structured organism, such as a human being. However, this ordering process is more than compensated for by the disordering of the rest of the universe. The net result is an increase in entropy and an increase in the
disorder of the universe.

The second law of thermodynamics makes clear that the entropy of the universe never decreases during any thermodynamic process. For any other thermodynamic system, when the process is reversible, the change of the entropy is given by $\Delta S=Q / T$. But what happens if the temperature goes to zero, $T \rightarrow 0$ ? It turns out this is not a question that can be answered by the second law.

A fundamental issue still remains: Is it possible to cool a system all the way down to zero kelvin? We understand that the system must be at its lowest energy state because lowering temperature reduces the kinetic energy of the constituents in the system. What happens to the entropy of a system at the absolute zero temperature? It turns out the absolute zero temperature is not reachable-at least, not though a finite number of cooling steps. This is a statement of the third law of thermodynamics, whose proof requires quantum mechanics that we do not present here. In actual experiments, physicists have continuously pushed that limit downward, with the lowest temperature achieved at about $1 \times 10^{-10} \mathrm{~K}$ in a low-temperature lab at the Helsinki University of Technology in 2008.

Like the second law of thermodynamics, the third law of thermodynamics can be stated in different ways. One of the common statements of the third law of thermodynamics is: The absolute zero temperature cannot be reached through any finite number of cooling steps.

In other words, the temperature of any given physical system must be finite, that is, $T>0$. This produces a very interesting question in physics: Do we know how a system would behave if it were at the absolute zero temperature?

The reason a system is unable to reach $0 \mathrm{~K}$ is fundamental and requires quantum mechanics to fully understand its origin. But we can certainly ask what happens to the entropy of a system when we try to cool it down to $0 \mathrm{~K}$. Because the amount of heat that can be removed from the system becomes vanishingly small, we expect that the change in entropy of the system along an isotherm approaches zero, that is,

$$
\lim _{T \rightarrow 0}(\Delta S)_{T}=0
$$

This can be viewed as another statement of the third law, with all the isotherms becoming isentropic, or into a reversible ideal adiabat. We can put this expression in words: A system becomes perfectly ordered when its temperature approaches absolute zero and its entropy approaches its absolute minimum.

The third law of thermodynamics puts another limit on what can be done when we look for energy resources. If there could be a reservoir at the absolute zero temperature, we could have engines with efficiency of $100 \%$, which would, of course, violate the second law of thermodynamics.

## EXAMPLE 4.8

## Entropy Change of an Ideal Gas in Free Expansion

An ideal gas occupies a partitioned volume $V_{1}$ inside a box whose walls are thermally insulating, as shown in Figure 4.18(a). When the partition is removed, the gas expands and fills the entire volume $V_{2}$ of the box, as shown in part (b). What is the entropy change of the universe (the system plus its environment)?

## Strategy

The adiabatic free expansion of an ideal gas is an irreversible process. There is no change in the internal energy (and hence temperature) of the gas in such an expansion because no work or heat transfer has happened. Thus, a convenient reversible path connecting the same two equilibrium states is a slow, isothermal expansion from $V_{1}$ to $V_{2}$. In this process, the gas could be expanding against a piston while in thermal contact with a heat reservoir, as in step 1 of the Carnot cycle.

## Solution

Since the temperature is constant, the entropy change is given by $\Delta S=Q / T$, where

$$
Q=W=\int_{V_{1}}^{V_{2}} p d V
$$

because $\Delta E_{\text {int }}=0$. Now, with the help of the ideal gas law, we have

$$
Q=n R T \int_{V_{1}}^{V_{2}} \frac{d V}{V}=n R T \ln \frac{V_{2}}{V_{1}}
$$

so the change in entropy of the gas is

$$
\Delta S=\frac{Q}{T}=n R \ln \frac{V_{2}}{V_{1}}
$$

Because $V_{2}>V_{1}, \Delta S$ is positive, and the entropy of the gas has gone up during the free expansion.

## Significance

What about the environment? The walls of the container are thermally insulating, so no heat exchange takes place between the gas and its surroundings. The entropy of the environment is therefore constant during the expansion. The net entropy change of the universe is then simply the entropy change of the gas. Since this is positive, the entropy of the universe increases in the free expansion of the gas.

## EXAMPLE 4.9

## Entropy Change during Heat Transfer

Heat flows from a steel object of mass $4.00 \mathrm{~kg}$ whose temperature is $400 \mathrm{~K}$ to an identical object at $300 \mathrm{~K}$. Assuming that the objects are thermally isolated from the environment, what is the net entropy change of the universe after thermal equilibrium has been reached?

## Strategy

Since the objects are identical, their common temperature at equilibrium is $350 \mathrm{~K}$. To calculate the entropy changes associated with their transitions, we substitute the irreversible process of the heat transfer by two isobaric, reversible processes, one for each of the two objects. The entropy change for each object is then given
by $\Delta S=m c \ln \left(T_{B} / T_{A}\right)$.

## Solution

Using $c=450 \mathrm{~J} / \mathrm{kg} \cdot \mathrm{K}$, the specific heat of steel, we have for the hotter object

$$
\begin{aligned}
\Delta S_{\mathrm{h}} & =\int_{T_{1}}^{T_{2}} \frac{m c d T}{T}=m c \ln \frac{T_{2}}{T_{1}} \\
& =(4.00 \mathrm{~kg})(450 \mathrm{~J} / \mathrm{kg} \cdot \mathrm{K}) \ln \frac{350 \mathrm{~K}}{400 \mathrm{~K}}=-240 \mathrm{~J} / \mathrm{K}
\end{aligned}
$$

Similarly, the entropy change of the cooler object is

$$
\Delta S_{\mathrm{c}}=(4.00 \mathrm{~kg})(450 \mathrm{~J} / \mathrm{kg} \cdot \mathrm{K}) \ln \frac{350 \mathrm{~K}}{300 \mathrm{~K}}=277 \mathrm{~J} / \mathrm{K}
$$

The net entropy change of the two objects during the heat transfer is then

$$
\Delta S_{\mathrm{h}}+\Delta S_{\mathrm{c}}=37 \mathrm{~J} / \mathrm{K}
$$

## Significance

The objects are thermally isolated from the environment, so its entropy must remain constant. Thus, the entropy of the universe also increases by $37 \mathrm{~J} / \mathrm{K}$.

