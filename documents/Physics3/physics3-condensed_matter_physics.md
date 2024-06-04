# CHAPTER9 <br> Condensed Matter Physics 

INTRODUCTION In this chapter, we examine applications of quantum mechanics to more complex systems, such as molecules, metals, semiconductors, and superconductors. We review and develop concepts of the previous chapters, including wave functions, orbitals, and quantum states. We also introduce many new concepts, including covalent bonding, rotational energy levels, Fermi energy, energy bands, doping, and Cooper pairs.

The main topic in this chapter is the crystal structure of solids. For centuries, crystalline solids have been prized for their beauty, including gems like diamonds and emeralds, as well as geological crystals of quartz and metallic ores. But the crystalline structures of semiconductors such as silicon have also made possible the electronics industry of today. In this chapter, we study how the structures of solids give them properties from strength and transparency to electrical conductivity.

### 9.1 Types of Molecular Bonds

Quantum mechanics has been extraordinarily successful at explaining the structure and bonding in molecules, and is therefore the foundation for all of chemistry. Quantum chemistry, as it is sometimes called, explains such basic questions as why $\mathrm{H}_{2} \mathrm{O}$ molecules exist, why the bonding angle between hydrogen atoms in this molecule is precisely $104.5^{\circ}$, and why these molecules bind together to form liquid water at room temperature. Applying quantum mechanics to molecules can be very difficult mathematically, so our discussion will be qualitative only.

As we study molecules and then solids, we will use many different scientific models. In some cases, we look at a molecule or crystal as a set of point nuclei with electrons whizzing around the outside in well-defined trajectories, as in the Bohr model. In other cases, we employ our full knowledge of quantum mechanics to study these systems using wave functions and the concept of electron spin. It is important to remember that we study modern physics with models, and that different models are useful for different purposes. We do not always use the most powerful model, when a less-powerful, easier-to-use model will do the job.

## Types of Bonds

Chemical units form by many different kinds of chemical bonds. An ionic bond forms when an electron transfers from one atom to another. A covalent bond occurs when two or more atoms share electrons. A van der Waals bond occurs due to the attraction of charge-polarized molecules and is considerably weaker than ionic or covalent bonds. Many other types of bonding exist as well. Often, bonding occurs via more than one mechanism. The focus of this section is ionic and covalent bonding.

## lonic bonds

The ionic bond is perhaps the easiest type of bonding to understand. It explains the formation of salt compounds, such as sodium chloride, $\mathrm{NaCl}$. The sodium atom (symbol $\mathrm{Na}$ ) has the same electron arrangement as a neon atom plus one $3 s$ electron. Only $5.14 \mathrm{eV}$ of energy is required to remove this one electron from the sodium atom. Therefore, Na can easily give up or donate this electron to an adjacent (nearby) atom, attaining a more stable arrangement of electrons. Chlorine (symbol Cl) requires just one electron to complete its valence shell, so it readily accepts this electron if it is near the sodium atom. We therefore say that chlorine has a large electron affinity, which is the energy associated with an accepted electron. The energy given up by the chlorine atom in this process is $3.62 \mathrm{eV}$. After the electron transfers from the sodium atom to the chlorine atom, the sodium atom becomes a positive ion and the chlorine atom becomes a negative ion. The total energy required for this transfer is given by

$$
E_{\text {transfer }}=5.14 \mathrm{eV}-3.62 \mathrm{eV}=1.52 \mathrm{eV}
$$

The positive sodium ion and negative chloride ion experience an attractive Coulomb force. The potential energy associated with this force is given by

$$
U_{\text {coul }}=-\frac{k e^{2}}{r_{0}}
$$

where $k e^{2}=1.440 \mathrm{eV}-\mathrm{nm}$ and $r_{0}$ is the distance between the ions.

As the sodium and chloride ions move together ("descend the potential energy hill"), the force of attraction between the ions becomes stronger. However, if the ions become too close, core-electron wave functions in the two ions begin to overlap. Due to the exclusion principle, this action promotes the core electrons-and
therefore the entire molecule-into a higher energy state. The equilibrium separation distance (or bond length) between the ions occurs when the molecule is in its lowest energy state. For diatomic $\mathrm{NaCl}$, this distance is $0.236 \mathrm{~nm}$. Figure 9.2 shows the total energy of $\mathrm{NaCl}$ as a function of the distance of separation between ions.

The total energy required to form a single salt unit is

$$
U_{\text {form }}=E_{\text {transfer }}+U_{\text {coul }}+U_{\mathrm{ex}}
$$

where $U_{\mathrm{ex}}$ is the energy associated with the repulsion between core electrons due to Pauli's exclusion principle. The value of $U_{\text {form }}$ must be negative for the bond to form spontaneously. The dissociation energy is defined as the energy required to separate the unit into its constituent ions, written

$$
U_{\text {diss }}=-U_{\text {form }}
$$

Every diatomic formula unit has its own characteristic dissociation energy and equilibrium separation length. Sample values are given in Table 9.1.

Molecule Dissociation Energy(eV) Equilibrium Separation (nm)(Bond length)

| $\mathrm{NaCl}$ | 4.26 | 0.236 |
| :--- | :--- | :--- |
| $\mathrm{NaF}$ | 4.99 | 0.193 |
| $\mathrm{NaBr}$ | 3.8 | 0.250 |
| $\mathrm{NaI}$ | 3.1 | 0.271 |
| $\mathrm{NaH}$ | 2.08 | 0.189 |
| $\mathrm{LiCl}$ | 4.86 | 0.202 |
| $\mathrm{LiH}$ | 2.47 | 0.239 |
| $\mathrm{LiI}$ | 3.67 | 0.238 |


| Molecule | Dissociation Energy(eV) | Equilibrium Separation (nm)(Bond length) |
| :--- | :--- | :--- |
| $\mathrm{KCl}$ | 4.43 | 0.267 |
| $\mathrm{KBr}$ | 3.97 | 0.282 |
| $\mathrm{RbF}$ | 5.12 | 0.227 |
| $\mathrm{RbCl}$ | 4.64 | 0.279 |
| $\mathrm{CsI}$ | 3.57 | 0.337 |
| $\mathrm{H}-\mathrm{H}$ | 4.5 | 0.075 |
| $\mathrm{N}-\mathrm{N}$ | 9.8 | 0.11 |
| $\mathrm{O}-\mathrm{O}$ | 5.2 | 0.12 |
| F-F | 1.6 | 0.14 |
| $\mathrm{Cl}-\mathrm{Cl}$ | 2.5 | 0.20 |

Table 9.1 Bond Length

## EXAMPLE 9.1

## The Energy of Salt

What is the dissociation energy of a salt formula unit $(\mathrm{NaCl})$ ?

## Strategy

Sodium chloride $(\mathrm{NaCl})$ is a salt formed by ionic bonds. The energy change associated with this bond depends on three main processes: the ionization of $\mathrm{Na}$; the acceptance of the electron from a $\mathrm{Na}$ atom by a $\mathrm{Cl}$ atom; and Coulomb attraction of the resulting ions $\left(\mathrm{Na}^{+}\right.$and $\left.\mathrm{Cl}^{-}\right)$. If the ions get too close, they repel due to the exclusion principle $(0.32 \mathrm{eV})$. The equilibrium separation distance is $r_{0}=0.236 \mathrm{~nm}$.

## Solution

The energy change associated with the transfer of an electron from $\mathrm{Na}$ to $\mathrm{Cl}$ is $1.52 \mathrm{eV}$, as discussed earlier in this section. At equilibrium separation, the atoms are $r_{0}=0.236 \mathrm{~nm}$ apart. The electrostatic potential energy of the atoms is

$$
U_{\text {coul }}=-\frac{k e^{2}}{r_{0}}=-\frac{1.44 \mathrm{eV} \cdot \mathrm{nm}}{0.236 \mathrm{~nm}}=-6.10 \mathrm{eV}
$$

The total energy difference associated with the formation of a $\mathrm{NaCl}$ formula unit is

$$
E_{\text {form }}=E_{\text {xfr }}+U_{\text {coul }}+U_{\mathrm{ex}}=1.52 \mathrm{eV}+(-6.10 \mathrm{eV})+0.32 \mathrm{eV}=-4.26 \mathrm{eV}
$$

Therefore, the dissociated energy of $\mathrm{NaCl}$ is $4.26 \mathrm{eV}$.

## Significance

The formation of a $\mathrm{NaCl}$ formula unit by ionic bonding is energetically favorable. The dissociation energy, or energy required to separate the $\mathrm{NaCl}$ unit into $\mathrm{Na}^{+}$and $\mathrm{Cl}^{-}$ions is $4.26 \mathrm{eV}$, consistent with $\underline{\mathrm{Fig}}$ igre 9.2 .

For a sodium ion in an ionic $\mathrm{NaCl}$ crystal, the expression for Coulomb potential energy $U_{\text {coul }}$ must be modified by a factor known as the Madelung constant. This factor takes into account the interaction of the sodium ion with all nearby chloride and sodium ions. The Madelung constant for a $\mathrm{NaCl}$ crystal is about 1.75 . This value implies an equilibrium separation distance between $\mathrm{Na}^{+}$and $\mathrm{Cl}^{-}$ions of $0.280 \mathrm{~nm}$-slightly larger than for diatomic $\mathrm{NaCl}$. We will return to this point again later.

## Covalent bonds

In an ionic bond, an electron transfers from one atom to another. However, in a covalent bond, an electron is shared between two atoms. The ionic bonding mechanism cannot explain the existence of such molecules as $\mathrm{H}_{2}, \mathrm{O}_{2}$, and $\mathrm{CO}$, since no separation distance exists for which the negative potential energy of attraction is greater in magnitude than the energy needed to create ions. Understanding precisely how such molecules are covalently bonded relies on a deeper understanding of quantum mechanics that goes beyond the coverage of this book, but we will qualitatively describe the mechanisms in the following section.

Covalent bonds can be understood using the simple example of a $\mathrm{H}_{2}^{+}$molecule, which consists of one electron in the electric field of two protons. This system can be modeled by an electron in a double square well (Figure 9.3). The electron is equally likely to be found in each well, so the wave function is either symmetric or antisymmetric about a point midway between the wells.

Now imagine that the two wells are separated by a large distance. In the ground state, the wave function exists in one of two possible states: either a single positive peak (a sine wave-like "hump") in both wells (symmetric case), or a positive peak in one well and a negative peak in the other (antisymmetric case). These states have the same energy. However, when the wells are brought together, the symmetric wave function becomes the ground state and the antisymmetric state becomes the first excited state-in other words, the energy level of the electron is split. Notice, the space-symmetric state becomes the energetically favorable (lower energy) state.

The same analysis is appropriate for an electron bound to two hydrogen atoms. Here, the shapes of the groundstate wave functions have the form $e^{-r / a_{0}}$ or $e^{\left(-|x| / a_{0}\right)}$ in one dimension. The energetically favorable, spacesymmetric state implies a high charge density midway between the protons where the electrons are likely to pull the positively charged protons together.

If a second electron is added to this system to form a $\mathrm{H}_{2}$ molecule, the wave function must describe both particles, including their spatial relationship and relative spins. This wave function must also respect the indistinguishability of electrons. ("If you've seen one electron, you've seen them all.") In particular, switching or exchanging the electrons should not produce an observable effect, a property called exchange symmetry. Exchange symmetry can be symmetric, producing no change in the wave function, or antisymmetric, producing an overall change in the sign of the wave function-neither of which is observable.

As we discuss later, the total wave function of two electrons must be antisymmetric on exchange. For example,
two electrons bound to a hydrogen molecule can be in a space-symmetric state with antiparallel spins ( $\uparrow \downarrow$ ) or space-antisymmetric state with parallel spins $(\uparrow \uparrow)$. The state with antiparallel spins is energetically favorable and therefore used in covalent bonding. If the protons are drawn too closely together, however, repulsion between the protons becomes important. (In other molecules, this effect is supplied by the exclusion principle.) As a result, $\mathrm{H}_{2}$ reaches an equilibrium separation of about $0.074 \mathrm{~nm}$ with a binding energy is 4.52 eV.

Quantum mechanics excludes many types of molecules. For example, the molecule $\mathrm{H}_{3}$ does not form, because if a third $\mathrm{H}$ atom approaches diatomic hydrogen, the wave function of the electron in this atom overlaps the electrons in the other two atoms. If all three electrons are in the ground states of their respective atoms, one pair of electrons shares all the same quantum numbers, which is forbidden by the exclusion principle. Instead, one of the electrons is forced into a higher energy state. No separation between three protons exists for which the total energy change of this process is negative-that is, where bonding occurs spontaneously. Similarly, $\mathrm{He}_{2}$ is not covalently bonded under normal conditions, because these atoms have no valence electrons to share. As the atoms are brought together, the wave functions of the core electrons overlap, and due to the exclusion principle, the electrons are forced into a higher energy state. No separation exists for which such a molecule is energetically favorable.

## Bonding in Polyatomic Molecules

A polyatomic molecule is a molecule made of more than two atoms. Examples range from a simple water molecule to a complex protein molecule. The structures of these molecules can often be understood in terms of covalent bonding and hybridization. Hybridization is a change in the energy structure of an atom in which mixed states (states that can be written as a linear superposition of others) participate in bonding.

To illustrate hybridization, consider the bonding in a simple water molecule, $\mathrm{H}_{2} \mathrm{O}$. The electron configuration of oxygen is $1 s^{2} 2 s^{2} 2 p^{4}$. The $1 s$ and $2 s$ electrons are in "closed shells" and do not participate in bonding. The remaining four electrons are the valence electrons. These electrons can fill six possible states $(l=1, m=0$, $\pm 1$, plus spin up and down). The energies of these states are the same, so the oxygen atom can exploit any linear combination of these states in bonding with the hydrogen atoms. These linear combinations (which you learned about in the chapter on atomic structure) are called atomic orbitals, and they are denoted by $p_{x}, p_{y}$, and $p_{z}$. The electron charge distributions for these orbitals are given in Figure 9.4.

The transformation of the electron wave functions of oxygen to $p_{x}, p_{y}$, and $p_{z}$ orbitals in the presence of the hydrogen atoms is an example of hybridization. Two electrons are found in the $p_{z}$ orbital with paired spins $(\uparrow \downarrow)$. One electron is found in each of the $p_{x}$ and $p_{y}$ orbitals, with unpaired spins. The latter orbitals participate in bonding with the hydrogen atoms. Based on Figure 9.4, we expect the bonding angle for $\mathrm{H}-\mathrm{O}-\mathrm{H}$ to be $90^{\circ}$.

However, if we include the effects of repulsion between atoms, the bond angle is $104.5^{\circ}$. The same arguments can be used to understand the tetrahedral shape of methane $\left(\mathrm{CH}_{4}\right)$ and other molecules.

### 9.2 Molecular Spectra

Molecular energy levels are more complicated than atomic energy levels because molecules can also vibrate and rotate. The energies associated with such motions lie in different ranges and can therefore be studied separately. Electronic transitions are of order $1 \mathrm{eV}$, vibrational transitions are of order $10^{-2} \mathrm{eV}$, and rotational transitions are of order $10^{-3} \mathrm{eV}$. For complex molecules, these energy changes are difficult to characterize, so we begin with the simple case of a diatomic molecule.

According to classical mechanics, the energy of rotation of a diatomic molecule is given by

$$
E_{r}=\frac{L^{2}}{2 I}
$$

where $I$ is the moment of inertia and $L$ is the angular momentum. According to quantum mechanics, the rotational angular momentum is quantized:

$$
L=\sqrt{l(l+1)} \hbar(l=0,1,2,3, \ldots)
$$

where $l$ is the orbital angular quantum number. The allowed rotational energy level of a diatomic molecule is therefore

$$
E_{r}=l(l+1) \frac{\hbar^{2}}{2 I}=l(l+1) E_{0 r} \quad(l=0,1,2,3, \ldots)
$$

where the characteristic rotational energy of a molecule is defined as

$$
E_{0 r}=\frac{\hbar^{2}}{2 I}
$$

For a diatomic molecule, the moment of inertia with reduced mass $\mu$ is

$$
I=\mu r_{0}^{2}
$$

where $r_{0}$ is the total distance between the atoms. The energy difference between rotational levels is therefore

$$
\Delta E_{r}=E_{l+1}-E_{l}=2(l+1) E_{0 r}
$$

A detailed study of transitions between rotational energy levels brought about by the absorption or emission of radiation (a so-called electric dipole transition) requires that

$$
\Delta l= \pm 1
$$

This rule, known as a selection rule, limits the possible transitions from one quantum state to another. Equation 9.10 is the selection rule for rotational energy transitions. It applies only to diatomic molecules that have an electric dipole moment. For this reason, symmetric molecules such as $\mathrm{H}_{2}$ and $\mathrm{N}_{2}$ do not experience rotational energy transitions due to the absorption or emission of electromagnetic radiation.

## EXAMPLE 9.2

## The Rotational Energy of HCl

Determine the lowest three rotational energy levels of a hydrogen chloride ( $\mathrm{HCl}$ ) molecule.

## Strategy

Hydrogen chloride $(\mathrm{HCl})$ is a diatomic molecule with an equilibrium separation distance of $0.127 \mathrm{~nm}$. Rotational energy levels depend only on the momentum of inertia $I$ and the orbital angular momentum quantum number $l$ (in this case, $l=0,1$, and 2). The momentum of inertia depends, in turn, on the equilibrium separation distance (which is given) and the reduced mass, which depends on the masses of the $\mathrm{H}$ and $\mathrm{Cl}$ atoms.

## Solution

First, we compute the reduced mass. If Particle 1 is hydrogen and Particle 2 is chloride, we have

$$
\mu=\frac{m_{1} m_{2}}{m_{1}+m_{2}}=\frac{(1.0 \mathrm{u})(35.4 \mathrm{u})}{1.0 \mathrm{u}+35.4 \mathrm{u}}=0.97 \mathrm{u}=0.97 \mathrm{u}\left(\frac{931.5 \frac{\mathrm{MeV}}{c^{2}}}{1 \mathrm{u}}\right)=906 \frac{\mathrm{MeV}}{c^{2}}
$$

The corresponding rest mass energy is therefore

$$
\mu c^{2}=9.06 \times 10^{8} \mathrm{eV}
$$

This allows us to calculate the characteristic energy:

$$
E_{0 r}=\frac{\hbar^{2}}{2 I}=\frac{\hbar^{2}}{2\left(\mu r_{0}^{2}\right)}=\frac{(\hbar c)^{2}}{2\left(\mu c^{2}\right) r_{0}^{2}}=\frac{(197.3 \mathrm{eV} \cdot \mathrm{nm})^{2}}{2\left(9.06 \times 10^{8} \mathrm{eV}\right)(0.127 \mathrm{~nm})^{2}}=1.33 \times 10^{-3} \mathrm{eV}
$$

(Notice how this expression is written in terms of the rest mass energy. This technique is common in modern physics calculations.) The rotational energy levels are given by

$$
E_{r}=l(l+1) \frac{\hbar^{2}}{2 I}=l(l+1) E_{0 r}
$$

where $l$ is the orbital quantum number. The three lowest rotational energy levels of an $\mathrm{HCl}$ molecule are therefore

$$
\begin{gathered}
l=0 ; E_{r}=0 \mathrm{eV} \text { (no rotation) } \\
l=1 ; E_{r}=2 E_{0 r}=2.66 \times 10^{-3} \mathrm{eV} \\
l=2 ; E_{r}=6 E_{0 r}=7.99 \times 10^{-3} \mathrm{eV}
\end{gathered}
$$

## Significance

The rotational spectrum is associated with weak transitions (1/1000 to $1 / 100$ of an eV). By comparison, the energy of an electron in the ground state of hydrogen is $-13.6 \mathrm{eV}$.

The vibrational energy level, which is the energy level associated with the vibrational energy of a molecule, is more difficult to estimate than the rotational energy level. However, we can estimate these levels by assuming that the two atoms in the diatomic molecule are connected by an ideal spring of spring constant $k$. The potential energy of this spring system is

$$
U_{\mathrm{osc}}=\frac{1}{2} k \Delta r^{2}
$$

Where $\Delta r$ is a change in the "natural length" of the molecule along a line that connects the atoms. Solving Schrödinger's equation for this potential gives

$$
E_{n}=\left(n+\frac{1}{2}\right) \hbar \omega(n=0,1,2, \ldots)
$$

Where $\omega$ is the natural angular frequency of vibration and $n$ is the vibrational quantum number. The prediction that vibrational energy levels are evenly spaced $(\Delta E=\hbar \omega)$ turns out to be good at lower energies. A detailed study of transitions between vibrational energy levels induced by the absorption or emission of radiation (and the specifically so-called electric dipole transition) requires that

$$
\Delta n= \pm 1
$$

Equation 9.13 represents the selection rule for vibrational energy transitions. As mentioned before, this rule applies only to diatomic molecules that have an electric dipole moment. Symmetric molecules do not experience such transitions.

Due to the selection rules, the absorption or emission of radiation by a diatomic molecule involves a transition in vibrational and rotational states. Specifically, if the vibrational quantum number (n) changes by one unit, then the rotational quantum number ( $I$ changes by one unit. An energy-level diagram of a possible transition is given in Figure 9.5. The absorption spectrum for such transitions in hydrogen chloride ( $\mathrm{HCl}$ ) is shown in Figure 9.6. The absorption peaks are due to transitions from the $n=0$ to $n=1$ vibrational states. Energy differences for the band of peaks at the left and right are, respectively,

$\Delta E_{l \rightarrow l+1}=\hbar \omega+2(l+1) E_{0 r}=\hbar \omega+2 E_{0 r}, \hbar \omega+4 E_{0 r}, \hbar \omega+6 E_{0 r}, \ldots$ (right band) and $\Delta E_{l \rightarrow l-1}=\hbar \omega-2 l E_{0 r}=\hbar \omega-2 E_{0 r}, \hbar \omega-4 E_{0 r}, \hbar \omega-6 E_{0 r}, \ldots$ (left band).

The moment of inertia can then be determined from the energy spacing between individual peaks $\left(2 E_{0 r}\right)$ or from the gap between the left and right bands $\left(4 E_{0 r}\right)$. The frequency at the center of this gap is the frequency of vibration.

### 9.3 Bonding in Crystalline Solids

Beginning in this section, we study crystalline solids, which consist of atoms arranged in an extended regular pattern called a lattice. Solids that do not or are unable to form crystals are classified as amorphous solids. Although amorphous solids (like glass) have a variety of interesting technological applications, the focus of this chapter will be on crystalline solids.

Atoms arrange themselves in a lattice to form a crystal because of a net attractive force between their constituent electrons and atomic nuclei. The crystals formed by the bonding of atoms belong to one of three categories, classified by their bonding: ionic, covalent, and metallic. Molecules can also bond together to form crystals; these bonds, not discussed here, are classified as molecular. Early in the twentieth century, the atomic model of a solid was speculative. We now have direct evidence of atoms in solids (Figure 9.7).

## lonic Bonding in Solids

Many solids form by ionic bonding. A prototypical example is the sodium chloride crystal, as we discussed earlier. Electrons transfer from sodium atoms to adjacent chlorine atoms, since the valence electrons in sodium are loosely bound and chlorine has a large electron affinity. The positively charged sodium ions and negatively charged chlorine (chloride) ions organize into an extended regular array of atoms (Figure 9.8).

The charge distributions of the sodium and chloride ions are spherically symmetric, and the chloride ion is about two times the diameter of the sodium ion. The lowest energy arrangement of these ions is called the face-centered cubic (FCC) structure. In this structure, each ion is closest to six ions of the other species. The unit cell is a cube-an atom occupies the center and corners of each "face" of the cube. The attractive potential
energy of the $\mathrm{Na}^{+}$ion due to the fields of these six $\mathrm{Cl}^{-}$ions is written

$$
U_{1}=-6 \frac{e^{2}}{4 \pi \varepsilon_{0} r}
$$

where the minus sign designates an attractive potential (and we identify $k=1 / 4 \pi \varepsilon_{0}$ ). At a distance $\sqrt{2} r$ are its next-nearest neighbors: twelve $\mathrm{Na}^{+}$ions of the same charge. The total repulsive potential energy associated with these ions is

$$
U_{2}=12 \frac{e^{2}}{4 \pi \varepsilon_{0} \sqrt{2} r}
$$

Next closest are eight $\mathrm{Cl}^{-}$ions a distance $\sqrt{3} r$ from the $\mathrm{Na}^{+}$ion. The potential energy of the $\mathrm{Na}^{+}$ion in the field of these eight ions is

$$
U_{3}=-8 \frac{e^{2}}{4 \pi \varepsilon_{0} \sqrt{3} r}
$$

Continuing in the same manner with alternate sets of $\mathrm{Cl}^{-}$and $\mathrm{Na}^{+}$ions, we find that the net attractive potential energy $U_{\mathrm{A}}$ of the single $\mathrm{Na}^{+}$ion can be written as

$$
U_{\text {coul }}=-\alpha \frac{e^{2}}{4 \pi \varepsilon_{0} r}
$$

where $\alpha$ is the Madelung constant, introduced earlier. From this analysis, we can see that this constant is the infinite converging sum

$$
\alpha=6-\frac{12}{\sqrt{2}}+\frac{8}{\sqrt{3}}+\cdots
$$

Distant ions make a significant contribution to this sum, so it converges slowly, and many terms must be used to calculate $\alpha$ accurately. For all FCC ionic solids, $\alpha$ is approximately 1.75 .

Other possible packing arrangements of atoms in solids include simple cubic and body-centered cubic (BCC). These three different packing structures of solids are compared in Figure 9.9. The first row represents the location, but not the size, of the ions; the second row indicates the unit cells of each structure or lattice; and the third row represents the location and size of the ions. The BCC structure has eight nearest neighbors, with a Madelung constant of about 1.76-only slightly different from that for the FCC structure. Determining the Madelung constant for specific solids is difficult work and the subject of current research.

The energy of the sodium ions is not entirely due to attractive forces between oppositely charged ions. If the ions are bought too close together, the wave functions of core electrons of the ions overlap, and the electrons repel due to the exclusion principle. The total potential energy of the $\mathrm{Na}^{+}$ion is therefore the sum of the attractive Coulomb potential $\left(U_{\text {coul }}\right)$ and the repulsive potential associated with the exclusion principle $\left(U_{\mathrm{ex}}\right)$. Calculating this repulsive potential requires powerful computers. Fortunately, however, this energy can be described accurately by a simple formula that contains adjustable parameters:

$$
U_{\mathrm{ex}}=\frac{A}{r^{n}}
$$

where the parameters $A$ and $n$ are chosen to give predictions consistent with experimental data. For the problem at the end of this chapter, the parameter $n$ is referred to as the repulsion constant. The total potential energy of the $\mathrm{Na}^{+}$ion is therefore

$$
U=-\alpha \frac{e^{2}}{4 \pi \varepsilon_{0} r}+\frac{A}{r^{n}}
$$

At equilibrium, there is no net force on the ion, so the distance between neighboring $\mathrm{Na}^{+}$and $\mathrm{Cl}^{-}$ions must be the value $r_{0}$ for which $U$ is a minimum. Setting $\frac{d U}{d r}=0$, we have

$$
0=\frac{\alpha e^{2}}{4 \pi \varepsilon_{0} r_{0}{ }^{2}}-\frac{n A}{r_{0}{ }^{n+1}}
$$

Thus,

$$
A=\frac{\alpha e^{2} r_{0}^{n-1}}{4 \pi \varepsilon_{0} n}
$$

Inserting this expression into the expression for the total potential energy, we have

$$
U=-\frac{\alpha e^{2}}{4 \pi \varepsilon_{0} r_{0}}\left[\frac{r_{0}}{r}-\frac{1}{n}\left(\frac{r_{0}}{r}\right)^{n}\right]
$$

Notice that the total potential energy now has only one adjustable parameter, $n$. The parameter $A$ has been replaced by a function involving $r_{0}$, the equilibrium separation distance, which can be measured by a diffraction experiment (you learned about diffraction in a previous chapter). The total potential energy is plotted in Figure 9.10 for $n=8$, the approximate value of $n$ for $\mathrm{NaCl}$.

As long as $n>1$, the curve for $U$ has the same general shape: $U$ approaches infinity as $r \rightarrow 0$ and $U$ approaches zero as $r \rightarrow \infty$. The minimum value of the potential energy is given by

$$
U_{\min }\left(r=r_{0}\right)=-\alpha \frac{k e^{2}}{r_{0}}\left(1-\frac{1}{n}\right)
$$

The energy per ion pair needed to separate the crystal into ions is therefore

$$
U_{\mathrm{diss}}=\alpha \frac{k e^{2}}{r_{0}}\left(1-\frac{1}{n}\right)
$$

This is the dissociation energy of the solid. The dissociation energy can also be used to describe the total energy needed to break a mole of a solid into its constituent ions, often expressed in $\mathrm{kJ} / \mathrm{mole}$. The dissociation energy can be determined experimentally using the latent heat of vaporization. Sample values are given in the
following table.

|  | $\mathrm{F}^{-}$ | $\mathrm{Cl}^{-}$ | $\mathrm{Br}^{-}$ | $\mathrm{I}^{-}$ |
| :--- | :--- | :--- | :--- | :--- |
| $\mathrm{Li}^{+}$ | 1036 | 853 | 807 | 757 |
| $\mathrm{Na}^{+}$ | 923 | 787 | 747 | 704 |
| $\mathrm{K}^{+}$ | 821 | 715 | 682 | 649 |
| $\mathrm{Rb}^{+}$ | 785 | 689 | 660 | 630 |
| $\mathrm{Cs}^{+}$ | 740 | 659 | 631 | 604 |

Table 9.2 Lattice Energy for Alkali Metal Halides

Thus, we can determine the Madelung constant from the crystal structure and $n$ from the lattice energy. For $\mathrm{NaCl}$, we have $r_{0}=2.81 \AA, n \approx 8$, and $U_{\text {diss }}=7.84 \mathrm{eV} /$ ion pair. This dissociation energy is relatively large. The most energetic photon from the visible spectrum, for example, has an energy of approximately

$$
h f=\left(4.14 \times 10^{-15} \mathrm{eV} \cdot \mathrm{s}\right)\left(7.5 \times 10^{14} \mathrm{~Hz}\right)=3.1 \mathrm{eV}
$$

Because the ions in crystals are so tightly bound, ionic crystals have the following general characteristics:

1. They are fairly hard and stable.
2. They vaporize at relatively high temperatures (1000 to $2000 \mathrm{~K}$ ).
3. They are transparent to visible radiation, because photons in the visible portion of the spectrum are not energetic enough to excite an electron from its ground state to an excited state.
4. They are poor electrical conductors, because they contain effectively no free electrons.
5. They are usually soluble in water, because the water molecule has a large dipole moment whose electric field is strong enough to break the electrostatic bonds between the ions.

## EXAMPLE 9.3

## The Dissociation Energy of Salt

Determine the dissociation energy of sodium chloride ( $\mathrm{NaCl}$ ) in $\mathrm{kJ} / \mathrm{mol}$. (Hint: The repulsion constant $n$ of $\mathrm{NaCl}$ is approximately 8.$)$

## Strategy

A sodium chloride crystal has an equilibrium separation of $0.282 \mathrm{~nm}$. (Compare this value with $0.236 \mathrm{~nm}$ for a free diatomic unit of $\mathrm{NaCl}$.) The dissociation energy depends on the separation distance, repulsion constant, and Madelung constant for an FCC structure. The separation distance depends in turn on the molar mass and measured density. We can determine the separation distance, and then use this value to determine the dissociation energy for one mole of the solid.

## Solution

The atomic masses of $\mathrm{Na}$ and $\mathrm{Cl}$ are $23.0 \mathrm{u}$ and $58.4 \mathrm{u}$, so the molar mass of $\mathrm{NaCl}$ is $58.4 \mathrm{~g} / \mathrm{mol}$. The density of $\mathrm{NaCl}$ is $2.16 \mathrm{~g} / \mathrm{cm}^{3}$. The relationship between these quantities is

$$
\rho=\frac{M}{V}=\frac{M}{2 N_{\mathrm{A}} r_{0}^{3}}
$$

where $M$ is the mass of one mole of salt, $N_{\mathrm{A}}$ is Avogadro's number, and $r_{0}$ is the equilibrium separation distance. The factor 2 is needed since both the sodium and chloride ions represent a cubic volume $r_{0}^{3}$. Solving for the distance, we get

$$
r_{0}^{3}=\frac{M}{2 N_{\mathrm{A}} \rho}=\frac{58.4 \mathrm{~g} / \mathrm{mol}}{2\left(6.03 \times 10^{23}\right)\left(2.160 \mathrm{~g} / \mathrm{cm}^{3}\right)}=2.23 \times 10^{-23} \mathrm{~cm}^{3}
$$

or

$$
r_{0}=2.80 \times 10^{-8} \mathrm{~cm}=0.280 \mathrm{~nm}
$$

The potential energy of one ion pair $\left(\mathrm{Na}^{+} \mathrm{Cl}^{-}\right)$is

$$
U=-\alpha \frac{k e^{2}}{r_{0}}\left(1-\frac{1}{n}\right)
$$

where $\alpha$ is the Madelung constant, $r_{0}$ is the equilibrium separation distance, and $n$ is the repulsion constant. $\mathrm{NaCl}$ is FCC, so the Madelung constant is $\alpha=1.7476$. Substituting these values, we get

$$
U=-1.75 \frac{1.44 \mathrm{eV} \cdot \mathrm{nm}}{0.280 \mathrm{~nm}}\left(1-\frac{1}{8}\right)=-7.88 \frac{\mathrm{eV}}{\text { ion pair }}
$$

The dissociation energy of one mole of sodium chloride is therefore

$$
D=\left(\frac{7.88 \mathrm{eV}}{\text { ion pair }}\right)\left(\frac{\frac{23.052 \mathrm{kcal}}{1 \mathrm{~mol}}}{\frac{1 \mathrm{eV}}{\text { ion pair }}}\right)=182 \mathrm{kcal} / \mathrm{mol}=760 \mathrm{~kJ} / \mathrm{mol}
$$

## Significance

This theoretical value of the dissociation energy of $766 \mathrm{~kJ} / \mathrm{mol}$ is close to the accepted experimental value of $787 \mathrm{~kJ} / \mathrm{mol}$. Notice that for larger density, the equilibrium separation distance between ion pairs is smaller, as expected. This small separation distance drives up the force between ions and therefore the dissociation energy. The conversion at the end of the equation took advantage of the conversion factor $1 \mathrm{~kJ}=0.239 \mathrm{kcal}$.

## Covalent Bonding in Solids

Crystals can also be formed by covalent bonding. For example, covalent bonds are responsible for holding carbon atoms together in diamond crystals. The electron configuration of the carbon atom is $1 s^{2} 2 s^{2} 2 p^{2}-\mathrm{a} \mathrm{He}$ core plus four valence electrons. This electron configuration is four electrons short of a full shell, so by sharing these four electrons with other carbon atoms in a covalent bond, the shells of all carbon atoms are filled. Diamond has a more complicated structure than most ionic crystals (Figure 9.11). Each carbon atom is the center of a regular tetrahedron, and the angle between the bonds is $110^{\circ}$. This angle is a direct consequence of the directionality of the $p$ orbitals of carbon atoms.

Covalently bonded crystals are not as uniform as ionic crystals but are reasonably hard, difficult to melt, and are insoluble in water. For example, diamond has an extremely high melting temperature ( $4000 \mathrm{~K}$ ) and is transparent to visible light. In comparison, covalently bonded tin (also known as alpha-tin, which is nonmetallic) is relatively soft, melts at $600 \mathrm{~K}$, and reflects visible light. Two other important examples of covalently bonded crystals are silicon and germanium. Both of these solids are used extensively in the manufacture of diodes, transistors, and integrated circuits. We will return to these materials later in our discussion of semiconductors.

## Metallic Bonding in Solids

As the name implies, metallic bonding is responsible for the formation of metallic crystals. The valence electrons are essentially free of the atoms and are able to move relatively easily throughout the metallic crystal. Bonding is due to the attractive forces between the positive ions and the conduction electrons. Metallic bonds are weaker than ionic or covalent bonds, with dissociation energies in the range $1-3 \mathrm{eV}$.

### 9.4 Free Electron Model of Metals

Metals, such as copper and aluminum, are held together by bonds that are very different from those of molecules. Rather than sharing and exchanging electrons, a metal is essentially held together by a system of free electrons that wander throughout the solid. The simplest model of a metal is the free electron model. This model views electrons as a gas. We first consider the simple one-dimensional case in which electrons move freely along a line, such as through a very thin metal rod. The potential function $U(x)$ for this case is a one-dimensional infinite square well where the walls of the well correspond to the edges of the rod. This model ignores the interactions between the electrons but respects the exclusion principle. For the special case of $T=0 \mathrm{~K}, N$ electrons fill up the energy levels, from lowest to highest, two at a time (spin up and spin down), until the highest energy level is filled. The highest energy filled is called the Fermi energy.

The one-dimensional free electron model can be improved by considering the three-dimensional case: electrons moving freely in a three-dimensional metal block. This system is modeled by a three-dimensional
infinite square well. Determining the allowed energy states requires us to solve the time-independent Schrödinger equation

$$
-\frac{h^{2}}{2 m_{\mathrm{e}}}\left(\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial^{2}}{\partial y^{2}}+\frac{\partial^{2}}{\partial z^{2}}\right) \psi(x, y, z)=E \psi(x, y, z)
$$

where we assume that the potential energy inside the box is zero and infinity otherwise. The allowed wave functions describing the electron's quantum states can be written as

$$
\psi(x, y, z)=\left(\sqrt{\frac{2}{L_{x}}} \sin \frac{n_{x} \pi x}{L_{x}}\right)\left(\sqrt{\frac{2}{L_{y}}} \sin \frac{n_{y} \pi y}{L_{y}}\right)\left(\sqrt{\frac{2}{L_{z}}} \sin \frac{n_{z} \pi z}{L_{z}}\right)
$$

where $n_{x}, n_{y}$, and $n_{z}$ are positive integers representing quantum numbers corresponding to the motion in the $x^{-}, y$-, and $z$-directions, respectively, and $L_{x}, L_{y}$, and $L_{z}$ are the dimensions of the box in those directions. Equation 9.27 is simply the product of three one-dimensional wave functions. The allowed energies of an electron in a cube $\left(L=L_{x}=L_{y}=L_{z}\right)$ are

$$
E=\frac{\pi^{2} \hbar^{2}}{2 m L^{2}}\left(n_{1}^{2}+n_{2}^{2}+n_{3}^{2}\right)
$$

Associated with each set of quantum numbers $\left(n_{x}, n_{y}, n_{z}\right)$ are two quantum states, spin up and spin down. In a real material, the number of filled states is enormous. For example, in a cubic centimeter of metal, this number is on the order of $10^{22}$. Counting how many particles are in which state is difficult work, which often requires the help of a powerful computer. The effort is worthwhile, however, because this information is often an effective way to check the model.

## EXAMPLE 9.4

## Energy of a Metal Cube

Consider a solid metal cube of edge length $2.0 \mathrm{~cm}$. (a) What is the lowest energy level for an electron within the metal? (b) What is the spacing between this level and the next energy level?

## Strategy

An electron in a metal can be modeled as a wave. The lowest energy corresponds to the largest wavelength and smallest quantum number: $n_{x}, n_{y}, n_{z}=(1,1,1)$. Equation 9.28 supplies this "ground state" energy value. Since the energy of the electron increases with the quantum number, the next highest level involves the smallest increase in the quantum numbers, or $\left(n_{x}, n_{y}, n_{z}\right)=(2,1,1),(1,2,1)$, or $(1,1,2)$.

## Solution

The lowest energy level corresponds to the quantum numbers $n_{x}=n_{y}=n_{z}=1$. From Equation 9.28, the energy of this level is

$$
\begin{aligned}
E(1,1,1) & =\frac{\pi^{2} h^{2}}{2 m_{e} L^{2}}\left(1^{2}+1^{2}+1^{2}\right) \\
& =\frac{3 \pi^{2}(1.05 \times 10-34 \mathrm{~J} \cdot \mathrm{s})^{2}}{2\left(9.11 \times 10^{-31} \mathrm{~kg}\right)\left(2.00 \times 10^{-2} \mathrm{~m}\right)^{2}} \\
& =4.48 \times 10^{-34} \mathrm{~J}=2.80 \times 10^{-15} \mathrm{eV}
\end{aligned}
$$

The next-higher energy level is reached by increasing any one of the three quantum numbers by 1 . Hence, there are actually three quantum states with the same energy. Suppose we increase $n_{x}$ by 1 . Then the energy becomes

$$
\begin{aligned}
E(2,1,1) & =\frac{\pi^{2} h^{2}}{2 m_{\mathrm{e}} L^{2}}\left(2^{2}+1^{2}+1^{2}\right) \\
& =\frac{6 \pi^{2}(1.05 \times 10-34 \mathrm{~J} \cdot \mathrm{s})^{2}}{2\left(9.11 \times 10^{-31} \mathrm{~kg}\right)\left(2.00 \times 10^{-2} \mathrm{~m}\right)^{2}} \\
& =8.96 \times 10^{-34} \mathrm{~J}=5.60 \times 10^{-15} \mathrm{eV}
\end{aligned}
$$

The energy spacing between the lowest energy state and the next-highest energy state is therefore

$$
\mathrm{E}(2,1,1)-\mathrm{E}(1,1,1)=2.80 \times 10^{-15} \mathrm{eV}
$$

## Significance

This is a very small energy difference. Compare this value to the average kinetic energy of a particle, $k_{\mathrm{B}} T$, where $k_{\mathrm{B}}$ is Boltzmann's constant and $T$ is the temperature. The product $k_{\mathrm{B}} T$ is about 1000 times greater than the energy spacing.

Often, we are not interested in the total number of particles in all states, but rather the number of particles $d N$ with energies in a narrow energy interval. This value can be expressed by

$$
d N=n(E) d E=g(E) d E \cdot F
$$

where $n(E)$ is the electron number density, or the number of electrons per unit volume; $g(E)$ is the density of states, or the number of allowed quantum states per unit energy; $d E$ is the size of the energy interval; and $F$ is the Fermi factor. The Fermi factor is the probability that the state will be filled. For example, if $g(E) d E$ is 100 available states, but $F$ is only $5 \%$, then the number of particles in this narrow energy interval is only five. Finding $g(E)$ requires solving Schrödinger's equation (in three dimensions) for the allowed energy levels. The calculation is involved even for a crude model, but the result is simple:

$$
g(E)=\frac{\pi V}{2}\left(\frac{8 m_{e}}{h^{2}}\right)^{3 / 2} E^{1 / 2}
$$

where $V$ is the volume of the solid, $m_{e}$ is the mass of the electron, and $E$ is the energy of the state. Notice that the density of states increases with the square root of the energy. More states are available at high energy than at low energy. This expression does not provide information of the density of the electrons in physical space, but rather the density of energy levels in "energy space." For example, in our study of the atomic structure, we learned that the energy levels of a hydrogen atom are much more widely spaced for small energy values (near than ground state) than for larger values.

This equation tells us how many electron states are available in a three-dimensional metallic solid. However, it does not tell us how likely these states will be filled. Thus, we need to determine the Fermi factor, $F$. Consider the simple case of $T=0 \mathrm{~K}$. From classical physics, we expect that all the electrons ( $\left.\sim 10^{22} / \mathrm{cm}^{3}\right)$ would simply go into the ground state to achieve the lowest possible energy. However, this violates Pauli's exclusion principle, which states that no two electrons can be in the same quantum state. Hence, when we begin filling the states with electrons, the states with lowest energy become occupied first, then states with progressively higher energies. The last electron we put in has the highest energy. This energy is the Fermi energy $E_{\mathrm{F}}$ of the free electron gas. A state with energy $E<E_{\mathrm{F}}$ is occupied by a single electron, and a state with energy $E>E_{\mathrm{F}}$ is unoccupied. To describe this in terms of a probability $F(E)$ that a state of energy $E$ is occupied, we write for $T=0 \mathrm{~K}:$

$$
\begin{array}{ll}
F(E)=1 & \left(E<E_{\mathrm{F}}\right) \\
F(E)=0 & \left(E>E_{\mathrm{F}}\right)
\end{array}
$$

The density of states, Fermi factor, and electron number density are plotted against energy in Figure 9.12.

A few notes are in order. First, the electron number density (last row) distribution drops off sharply at the Fermi energy. According to the theory, this energy is given by

$$
E_{\mathrm{F}}=\frac{h^{2}}{8 m_{e}}\left(\frac{3 N}{\pi V}\right)^{2 / 3}
$$

Fermi energies for selected materials are listed in the following table.

Element Conduction Band Electron Density $\left(10^{28} \mathrm{~m}^{-3}\right) \quad$ Free-Electron Model Fermi Energy (eV)

| $\mathrm{Al}$ | 18.1 | 11.7 |
| :--- | :--- | :--- |
| $\mathrm{Ba}$ | 3.15 | 3.64 |
| $\mathrm{Cu}$ | 8.47 | 7.00 |
| $\mathrm{Au}$ | 5.90 | 5.53 |
| $\mathrm{Fe}$ | 17.0 | 11.1 |
| $\mathrm{Ag}$ | 5.86 | 5.49 |

Table 9.3 Conduction Electron Densities and Fermi Energies for Some Metals

Note also that only the graph in part (c) of the figure, which answers the question, "How many particles are found in the energy range?" is checked by experiment. The Fermi temperature or effective "temperature" of an electron at the Fermi energy is

$$
T_{\mathrm{F}}=\frac{E_{\mathrm{F}}}{k_{\mathrm{B}}}
$$

## EXAMPLE 9.5

## Fermi Energy of Silver

Metallic silver is an excellent conductor. It has $5.86 \times 10^{28}$ conduction electrons per cubic meter. (a) Calculate its Fermi energy. (b) Compare this energy to the thermal energy $k_{\mathrm{B}} T$ of the electrons at a room temperature of $300 \mathrm{~K}$.

## Solution

a. From Equation 9.31, the Fermi energy is

$$
\begin{aligned}
E_{\mathrm{F}} & =\frac{h^{2}}{2 m_{e}}\left(3 \pi^{2} n_{e}\right)^{2 / 3} \\
& =\frac{\left(1.05 \times 10^{-34} \mathrm{~J} \cdot \mathrm{s}\right)^{2}}{2\left(9.11 \times 10^{-31} \mathrm{~kg}\right)} \times\left[\left(3 \pi^{2}\left(5.86 \times 10^{28} \mathrm{~m}^{-3}\right)\right]^{2 / 3}\right. \\
& =8.79 \times 10^{-19} \mathrm{~J}=5.49 \mathrm{eV}
\end{aligned}
$$

This is a typical value of the Fermi energy for metals, as can be seen from Table 9.3.

b. We can associate a Fermi temperature $T_{\mathrm{F}}$ with the Fermi energy by writing $k_{\mathrm{B}} T_{\mathrm{F}}=E_{\mathrm{F}}$. We then find for the Fermi temperature

$$
T_{\mathrm{F}}=\frac{8.79 \times 10^{-19} \mathrm{~J}}{1.38 \times 10^{-23} \mathrm{~J} / \mathrm{K}}=6.37 \times 10^{4} \mathrm{~K}
$$

which is much higher than room temperature and also the typical melting point $\left(\sim 10^{3} \mathrm{~K}\right)$ of a metal. The ratio of the Fermi energy of silver to the room-temperature thermal energy is

$$
\frac{E_{\mathrm{F}}}{k_{\mathrm{B}} T}=\frac{T_{\mathrm{F}}}{T} \approx 210
$$

To visualize how the quantum states are filled, we might imagine pouring water slowly into a glass, such as that of Figure 9.13. The first drops of water (the electrons) occupy the bottom of the glass (the states with lowest energy). As the level rises, states of higher and higher energy are occupied. Furthermore, since the glass has a wide opening and a narrow stem, more water occupies the top of the glass than the bottom. This reflects the fact that the density of states $g(E)$ is proportional to $E^{1 / 2}$, so there is a relatively large number of higher energy electrons in a free electron gas. Finally, the level to which the glass is filled corresponds to the Fermi energy.

Suppose that at $T=0 \mathrm{~K}$, the number of conduction electrons per unit volume in our sample is $n_{e}$. Since each field state has one electron, the number of filled states per unit volume is the same as the number of electrons per unit volume.

### 9.5 Band Theory of Solids

The free electron model explains many important properties of conductors but is weak in at least two areas. First, it assumes a constant potential energy within the solid. (Recall that a constant potential energy is associated with no forces.) Figure 9.14 compares the assumption of a constant potential energy (dotted line) with the periodic Coulomb potential, which drops as $-1 / r$ at each lattice point, where $r$ is the distance from the ion core (solid line). Second, the free electron model assumes an impenetrable barrier at the surface. This assumption is not valid, because under certain conditions, electrons can escape the surface-such as in the photoelectric effect. In addition to these assumptions, the free electron model does not explain the dramatic differences in electronic properties of conductors, semiconductors, and insulators. Therefore, a more complete model is needed.

We can produce an improved model by solving Schrödinger's equation for the periodic potential shown in Figure 9.14. However, the solution requires technical mathematics far beyond our scope. We again seek a qualitative argument based on quantum mechanics to find a way forward.

We first review the argument used to explain the energy structure of a covalent bond. Consider two identical hydrogen atoms so far apart that there is no interaction whatsoever between them. Further suppose that the electron in each atom is in the same ground state: a $1 s$ electron with an energy of $-13.6 \mathrm{eV}$ (ignore spin). When the hydrogen atoms are brought closer together, the individual wave functions of the electrons overlap and, by the exclusion principle, can no longer be in the same quantum state, which splits the original equivalent energy levels into two different energy levels. The energies of these levels depend on the interatomic distance, $\alpha$ (Figure 9.15).

If four hydrogen atoms are brought together, four levels are formed from the four possible symmetries-a single sine wave "hump" in each well, alternating up and down, and so on. In the limit of a very large number $N$ of atoms, we expect a spread of nearly continuous bands of electronic energy levels in a solid (see Figure 9.15(c)). Each of these bands is known as an energy band. (The allowed states of energy and wave number are still technically quantized, but for large numbers of atoms, these states are so close together that they are
consider to be continuous or "in the continuum.")

Energy bands differ in the number of electrons they hold. In the $1 s$ and $2 s$ energy bands, each energy level holds up to two electrons (spin up and spin down), so this band has a maximum occupancy of $2 N$ electrons. In the $2 p$ energy band, each energy level holds up to six electrons, so this band has a maximum occupancy of $6 \mathrm{~N}$ electrons (Figure 9.16).

Each energy band is separated from the other by an energy gap. The electrical properties of conductors and insulators can be understood in terms of energy bands and gaps. The highest energy band that is filled is known as a valence band. The next available band in the energy structure is known as a conduction band. In a conductor, the highest energy band that contains electrons is partially filled, whereas in an insulator, the highest energy band containing electrons is completely filled. The difference between a conductor and insulator is illustrated in Figure 9.17.

A conductor differs from an insulator in how its electrons respond to an applied electric field. If a significant number of electrons are set into motion by the field, the material is a conductor. In terms of the band model, electrons in the partially filled conduction band gain kinetic energy from the electric field by filling higher energy states in the conduction band. By contrast, in an insulator, electrons belong to completely filled bands. When the field is applied, the electrons cannot make such transitions (acquire kinetic energy from the electric field) due to the exclusion principle. As a result, the material does not conduct electricity.

A semiconductor has a similar energy structure to an insulator except it has a relatively small energy gap between the lowest completely filled band and the next available unfilled band. This type of material forms the basis of modern electronics. At $T=0 \mathrm{~K}$, the semiconductor and insulator both have completely filled bands. The only difference is in the size of the energy gap (or band gap) $E_{g}$ between the highest energy band that is filled (the valence band) and the next-higher empty band (the conduction band). In a semiconductor, this gap is small enough that a substantial number of electrons from the valence band are thermally excited into the conduction band at room temperature. These electrons are then in a nearly empty band and can respond to an applied field. As a general rule of thumb, the band gap of a semiconductor is about $1 \mathrm{eV}$. (See Table 9.4 for silicon.) A band gap of greater than approximately $1 \mathrm{eV}$ is considered an insulator. For comparison, the energy gap of diamond (an insulator) is several electron-volts.

| Material | Energy $\mathrm{Gap} E_{g}(\mathrm{eV})$ |
| :--- | :--- |
| $\mathrm{Si}$ | 1.14 |
| $\mathrm{Ge}$ | 0.67 |
| GaAs | 1.43 |
| $\mathrm{GaP}$ | 2.26 |
| GaSb | 0.69 |
| InAs | 0.35 |
| InP | 1.35 |


| Material | Energy Gap $E_{g}(\mathrm{eV})$ |
| :--- | :--- |
| $\mathrm{InSb}$ | 0.16 |
| $\mathrm{C}$ (diamond) | 5.48 |

Table 9.4 Energy Gap for Various Materials at $300 \mathrm{~K}$ Note: Except for diamond, the materials listed are all semiconductors.

### 9.6 Semiconductors and Doping

In the preceding section, we considered only the contribution to the electric current due to electrons occupying states in the conduction band. However, moving an electron from the valence band to the conduction band leaves an unoccupied state or hole in the energy structure of the valence band, which a nearby electron can move into. As these holes are filled by other electrons, new holes are created. The electric current associated with this filling can be viewed as the collective motion of many negatively charged electrons or the motion of the positively charged electron holes.

To illustrate, consider the one-dimensional lattice in Figure 9.18. Assume that each lattice atom contributes one valence electron to the current. As the hole on the right is filled, this hole moves to the left. The current can be interpreted as the flow of positive charge to the left. The density of holes, or the number of holes per unit volume, is represented by $p$. Each electron that transitions into the conduction band leaves behind a hole. If the conduction band is originally empty, the conduction electron density $p$ is equal to the hole density, that is, $n=p$.

As mentioned, a semiconductor is a material with a filled valence band, an unfilled conduction band, and a relatively small energy gap between the bands. Excess electrons or holes can be introduced into the material by the substitution into the crystal lattice of an impurity atom, which is an atom of a slightly different valence number. This process is known as doping. For example, suppose we add an arsenic atom to a crystal of silicon (Figure 9.19(a)).

Arsenic has five valence electrons, whereas silicon has only four. This extra electron must therefore go into the conduction band, since there is no room in the valence band. The arsenic ion left behind has a net positive charge that weakly binds the delocalized electron. The binding is weak because the surrounding atomic lattice shields the ion's electric field. As a result, the binding energy of the extra electron is only about $0.02 \mathrm{eV}$. In other words, the energy level of the impurity electron is in the band gap below the conduction band by $0.02 \mathrm{eV}$, a much smaller value than the energy of the gap, $1.14 \mathrm{eV}$. At room temperature, this impurity electron is easily excited into the conduction band and therefore contributes to the conductivity (Figure 9.20(a)). An impurity with an extra electron is known as a donor impurity, and the doped semiconductor is called an $\boldsymbol{n}$-type semiconductor because the primary carriers of charge (electrons) are negative.

By adding more donor impurities, we can create an impurity band, a new energy band created by semiconductor doping, as shown in Figure 9.20(b). The Fermi level is now between this band and the conduction band. At room temperature, many impurity electrons are thermally excited into the conduction band and contribute to the conductivity. Conduction can then also occur in the impurity band as vacancies are created there. Note that changes in the energy of an electron correspond to a change in the motion (velocities or kinetic energy) of these charge carriers with the semiconductor, but not the bulk motion of the semiconductor itself.

Doping can also be accomplished using impurity atoms that typically have one fewer valence electron than the semiconductor atoms. For example, $\mathrm{Al}$, which has three valence electrons, can be substituted for $\mathrm{Si}$, as shown in Figure 9.19(b). Such an impurity is known as an acceptor impurity, and the doped semiconductor is called a p-type semiconductor, because the primary carriers of charge (holes) are positive. If a hole is treated as a positive particle weakly bound to the impurity site, then an empty electron state is created in the band gap just above the valence band. When this state is filled by an electron thermally excited from the valence band (Figure 9.21(a)), a mobile hole is created in the valence band. By adding more acceptor impurities, we can create an impurity band, as shown in Figure 9.21(b).

The electric current of a doped semiconductor can be due to the motion of a majority carrier, in which holes are contributed by an impurity atom, or due to a minority carrier, in which holes are contributed purely by thermal excitations of electrons across the energy gap. In an $n$-type semiconductor, majority carriers are free electrons contributed by impurity atoms, and minority carriers are free electrons produced by thermal excitations from the valence to the conduction band. In a $p$-type semiconductor, the majority carriers are free holes contributed by impurity atoms, and minority carriers are free holes left by the filling of states due to thermal excitation of electrons across the gap. In general, the number of majority carriers far exceeds the minority carriers. The concept of a majority and minority carriers will be used in the next section to explain the operation of diodes and transistors.

In studying $p$ - and $n$-type doping, it is natural to ask: Do "electron holes" really act like particles? The existence of holes in a doped $p$-type semiconductor is demonstrated by the Hall effect. The Hall effect is the production of a potential difference due to the motion of a conductor through an external magnetic field (see The Hall Effect). A schematic of the Hall effect is shown in Figure 9.22(a). A semiconductor strip is bathed in a uniform magnetic field (which points into the paper). As the electron holes move from left to right through the semiconductor, a Lorentz force drives these charges toward the upper end of the strip. (Recall that the motion of the positively charged carriers is determined by the right-hand rule.) Positive charge continues to collect on the upper edge of the strip until the force associated with the downward electric field between the upper and lower edges of the strip $\left(F_{E}=E q\right)$ just balances the upward magnetic force $\left(F_{B}=q v B\right)$. Setting these forces equal to each other, we have $E=v B$. The voltage that develops across the strip is therefore

$$
V_{\mathrm{H}}=v B w
$$

where $V_{\mathrm{H}}$ is the Hall voltage; $v$ is the hole's drift velocity, or average velocity of a particle that moves in a partially random fashion; $B$ is the magnetic field strength; and $w$ is the width of the strip. Note that the Hall voltage is transverse to the voltage that initially produces current through the material. A measurement of the sign of this voltage (or potential difference) confirms the collection of holes on the top side of the strip. The magnitude of the Hall voltage yields the drift velocity ( $v$ ) of the majority carriers.

Additional information can also be extracted from the Hall voltage. Note that the electron current density (the amount of current per unit cross-sectional area of the semiconductor strip) is

$$
j=n q v
$$

where $q$ is the magnitude of the charge, $n$ is the number of charge carriers per unit volume, and $v$ is the drift velocity. The current density is easily determined by dividing the total current by the cross-sectional area of the strip, $q$ is charge of the hole (the magnitude of the charge of a single electron), and $u$ is determined by the Hall effect Equation 9.34. Hence, the above expression for the electron current density gives the number of charge carriers per unit volume, n. A similar analysis can be conducted for negatively charged carriers in an $n$-type material (see Figure 9.22).

### 9.7 Semiconductor Devices

Semiconductors have many applications in modern electronics. We describe some basic semiconductor devices in this section. A great advantage of using semiconductors for circuit elements is the fact that many thousands or millions of semiconductor devices can be combined on the same tiny piece of silicon and connected by conducting paths. The resulting structure is called an integrated circuit (ic), and ic chips are the basis of many modern devices, from computers and smartphones to the internet and global communications networks.

## Diodes

Perhaps the simplest device that can be created with a semiconductor is a diode. A diode is a circuit element that allows electric current to flow in only one direction, like a one-way valve (see Model of Conduction in Metals). A diode is created by joining a $p$-type semiconductor to an $n$-type semiconductor (Figure 9.23). The junction between these materials is called a $\boldsymbol{p}-\boldsymbol{n}$ junction. A comparison of the energy bands of a silicon-based diode is shown in Figure 9.23(b). The positions of the valence and conduction bands are the same, but the impurity levels are quite different. When a $p-n$ junction is formed, electrons from the conduction band of the $n$-type material diffuse to the $p$-side, where they combine with holes in the valence band. This migration of charge leaves positive ionized donor ions on the $n$-side and negative ionized acceptor ions on the $p$-side, producing a narrow double layer of charge at the $p-n$ junction called the depletion layer. The electric field associated with the depletion layer prevents further diffusion. The potential energy for electrons across the $p-$ $n$ junction is given by Figure 9.24 .

The behavior of a semiconductor diode can now be understood. If the positive side of the battery is connected to the $n$-type material, the depletion layer is widened, and the potential energy difference across the $p-n$ junction is increased. Few or none of the electrons (holes) have enough energy to climb the potential barrier, and current is significantly reduced. This is called the reverse bias configuration. On the other hand, if the positive side of a battery is connected to the $p$-type material, the depletion layer is narrowed, the potential energy difference across the $p-n$ junction is reduced, and electrons (holes) flow easily. This is called the forward bias configuration of the diode. In sum, the diode allows current to flow freely in one direction but prevents current flow in the opposite direction. In this sense, the semiconductor diode is a one-way valve.

We can estimate the mathematical relationship between the current and voltage for a diode using the electric potential concept. Consider $N$ negatively charged majority carriers (electrons donated by impurity atoms) in the $n$-type material and a potential barrier $V$ across the $p-n$ junction. According to the Maxwell-Boltzmann distribution, the fraction of electrons that have enough energy to diffuse across the potential barrier is $N e^{-e V / k_{\mathrm{B}} T}$. However, if a battery of voltage $V_{b}$ is applied in the forward-bias configuration, this fraction improves to $N e^{-e\left(V-V_{b}\right) / k_{\mathrm{B}} T}$. The electric current due to the majority carriers from the $n$-side to the $p$-side is therefore

$$
I=N e^{-e V / k_{\mathrm{B}} T} e^{e V_{b} / k_{\mathrm{B}} T}=I_{0} e^{e V_{b} / k_{\mathrm{B}} T}
$$

where $I_{0}$ is the current with no applied voltage and $T$ is the temperature. Current due to the minority carriers (thermal excitation of electrons from the valence band to the conduction band on the $p$-side and subsequent attraction to the $n$-side) is $-I_{0}$, independent of the bias voltage. The net current is therefore

$$
I_{\text {net }}=I_{0}\left(e^{e V_{b} / k_{\mathrm{B}} T}-1\right)
$$

A sample graph of the current versus bias voltage is given in Figure 9.25. In the forward bias configuration, small changes in the bias voltage lead to large changes in the current. In the reverse bias configuration, the current is $I_{\text {net }} \approx-I_{0}$. For extreme values of reverse bias, the atoms in the material are ionized which triggers an avalanche of current. This case occurs at the breakdown voltage.

## EXAMPLE 9.6

## Diode Current

Attaching the positive end of a battery to the $p$-side and the negative end to the $n$-side of a semiconductor diode produces a current of $4.5 \times 10^{-1} \mathrm{~A}$. The reverse saturation current is $2.2 \times 10^{-8} \mathrm{~A}$. (The reverse saturation current is the current of a diode in a reverse bias configuration such as this.) The battery voltage is $0.12 \mathrm{~V}$. What is the diode temperature?

## Strategy

The first arrangement is a forward bias configuration, and the second is the reverse bias configuration. In either case, Equation 9.2 gives the current.

## Solution

The current in the forward and reverse bias configurations is given by

$$
I_{\mathrm{net}}=I_{0}\left(e^{e V_{b} / k_{\mathrm{B}} T}-1\right)
$$

The current with no bias is related to the reverse saturation current by

$$
I_{0} \approx-I_{\mathrm{sat}}=2.2 \times 10^{-8}
$$

Therefore

$$
\frac{I_{\text {net }}}{I_{0}}=\frac{4.5 \times 10^{-1} \mathrm{~A}}{2.2 \times 10^{-8} \mathrm{~A}}=2.0 \times 10^{8}
$$

Equation 9.2 can be written as

$$
\frac{I_{\mathrm{net}}}{I_{0}}+1=e^{e V_{b} / k_{\mathrm{B}} T}
$$

This ratio is much greater than one, so the second term on the left-hand side of the equation vanishes. Taking the natural log of both sides gives

$$
\frac{e V_{b}}{k_{\mathrm{B}} T}=19
$$

The temperature is therefore

$$
T=\frac{e V_{b}}{k_{\mathrm{B}}}\left(\frac{1}{19}\right)=\frac{e(0.12 \mathrm{~V})}{8.617 \times 10^{-5} \mathrm{eV} / \mathrm{K}}\left(\frac{1}{19}\right)=73 \mathrm{~K}
$$

## Significance

The current moving through a diode in the forward and reverse bias configuration is sensitive to the temperature of the diode. If the potential energy supplied by the battery is large compared to the thermal energy of the diode's surroundings, $k_{\mathrm{B}} T$, then the forward bias current is very large compared to the reverse saturation current.

## Junction Transistor

If diodes are one-way valves, transistors are one-way valves that can be carefully opened and closed to control current. A special kind of transistor is a junction transistor. A junction transistor has three parts, including an $n$-type semiconductor, also called the emitter; a thin $p$-type semiconductor, which is the base; and another $n$-type semiconductor, called the collector (Figure 9.26). When a positive terminal is connected to the $p$-type layer (the base), a small current of electrons, called the base current $I_{B}$, flows to the terminal. This causes a large collector current $I_{c}$ to flow through the collector. The base current can be adjusted to control the large collector current. The current gain is therefore

$$
I_{c}=\beta I_{B} .
$$

A junction transistor can be used to amplify the voltage from a microphone to drive a loudspeaker. In this application, sound waves cause a diaphragm inside the microphone to move in and out rapidly (Figure 9.27). When the diaphragm is in the "in" position, a tiny positive voltage is applied to the base of the transistor. This
opens the transistor "valve" and allows a large electrical current flow to the loudspeaker. When the diaphragm is in the "out" position, a tiny negative voltage is applied to the base of the transistor, which shuts off the transistor valve so that no current flows to the loudspeaker. This shuts the transistor "valve" off so no current flows to the loudspeaker. In this way, current to the speaker is controlled by the sound waves, and the sound is amplified. Any electric device that amplifies a signal is called an amplifier.

In modern electronic devices, digital signals are used with diodes and transistors to perform tasks such as data manipulation. Electric circuits carry two types of electrical signals: analog and digital (Figure 9.28). An analog signal varies continuously, whereas a digital signal switches between two fixed voltage values, such as plus 1 volt and zero volts. In digital circuits like those found in computers, a transistor behaves like an on-off switch. The transistor is either on, meaning the valve is completely open, or it is off, meaning the valve is completely closed. Integrated circuits contain vast collections of transistors on a single piece of silicon. They are designed to handle digital signals that represent ones and zeroes, which is also known as binary code. The invention of the ic helped to launch the modern computer revolution.

### 9.8 Superconductivity

Electrical resistance can be considered as a measure of the frictional force in electrical current flow. Thus, electrical resistance is a primary source of energy dissipation in electrical systems such as electromagnets, electric motors, and transmission lines. Copper wire is commonly used in electrical wiring because it has one of the lowest room-temperature electrical resistivities among common conductors. (Actually, silver has a lower resistivity than copper, but the high cost and limited availability of silver outweigh its savings in energy over copper.)

Although our discussion of conductivity seems to imply that all materials must have electrical resistance, we know that this is not the case. When the temperature decreases below a critical value for many materials, their electrical resistivity drops to zero, and the materials become superconductors (see Superconductors).

## Properties of Superconductors

In addition to zero electrical resistance, superconductors also have perfect diamagnetism. In other words, in the presence of an applied magnetic field, the net magnetic field within a superconductor is always zero (Figure 9.29). Therefore, any magnetic field lines that pass through a superconducting sample when it is in its normal state are expelled once the sample becomes superconducting. These are manifestations of the Meissner effect, which you learned about in the chapter on current and resistance.

Interestingly, the Meissner effect is not a consequence of the resistance being zero. To see why, suppose that a sample placed in a magnetic field undergoes a transition in which its resistance drops to zero. From Ohm's law,
the current density, $j$, in the sample is related to the net internal electric field, $E$, and the resistivity $\rho$ by $j=E / \rho$. If $\rho$ is zero, $E$ must also be zero so that $j$ can remain finite. Now $E$ and the magnetic flux $\Phi_{\mathrm{m}}$ through the sample are related by Faraday's law as

$$
\oint E d I=-\frac{d \Phi_{\mathrm{m}}}{d t}
$$

If $E$ is zero, $d \Phi_{\mathrm{m}} / d t$ is also zero, that is, the magnetic flux through the sample cannot change. The magnetic field lines within the sample should therefore not be expelled when the transition occurs. Hence, it does not follow that a material whose resistance goes to zero has to exhibit the Meissner effect. Rather, the Meissner effect is a special property of superconductors.

Another important property of a superconducting material is its critical temperature, $T_{\mathrm{c}}$, the temperature below which the material is superconducting. The known range of critical temperatures is from a fraction of 1 K to slightly above $100 \mathrm{~K}$. Superconductors with critical temperatures near this higher limit are commonly known as "high-temperature" superconductors. From a practical standpoint, superconductors for which $T_{\mathrm{c}} \gg 77 \mathrm{~K}$ are very important. At present, applications involving superconductors often still require that superconducting materials be immersed in liquid helium (4.2 K) in order to keep them below their critical temperature. The liquid helium baths must be continually replenished because of evaporation, and cooling costs can easily outweigh the savings in using a superconductor. However, $77 \mathrm{~K}$ is the temperature of liquid nitrogen, which is far more abundant and inexpensive than liquid helium. It would be much more costeffective if we could easily fabricate and use high-temperature superconductor components that only need to be kept in liquid nitrogen baths to maintain their superconductivity.

High-temperature superconducting materials are presently in use in various applications. An example is the production of magnetic fields in some particle accelerators. The ultimate goal is to discover materials that are superconducting at room temperature. Without any cooling requirements, the bulk of electronic components and transmission lines could be superconducting, resulting in dramatic and unprecedented increases in efficiency and performance.

Another important property of a superconducting material is its critical magnetic field $B_{\mathrm{c}}(T)$, which is the maximum applied magnetic field at a temperature $T$ that will allow a material to remain superconducting. An applied field that is greater than the critical field will destroy the superconductivity. The critical field is zero at the critical temperature and increases as the temperature decreases. Plots of the critical field versus temperature for several superconducting materials are shown in Figure 9.30. The temperature dependence of the critical field can be described approximately by

$$
B_{\mathrm{c}}(T)=B_{\mathrm{c}}(0)\left[1-\left(\frac{T}{T_{\mathrm{c}}}\right)^{2}\right]
$$

where $B_{\mathrm{c}}(0)$ is the critical field at absolute zero temperature. Table 9.5 lists the critical temperatures and fields for two classes of superconductors: type I superconductor and type II superconductor. In general, type I superconductors are elements, such as aluminum and mercury. They are perfectly diamagnetic below a critical field $B_{C}(T)$, and enter the normal non-superconducting state once that field is exceeded. The critical fields of type I superconductors are generally quite low (well below one tesla). For this reason, they cannot be used in applications requiring the production of high magnetic fields, which would destroy their superconducting state.

| $\mathrm{Al}$ | 1.2 | 0.011 |
| :--- | :--- | :--- |
| $\mathrm{Ga}$ | 1.1 | 0.0051 |
| $\mathrm{Hg}(\alpha)$ | 4.2 | 0.041 |
| $\mathrm{In}$ | 3.4 | 0.029 |
| $\mathrm{Nb}$ | 9.3 | 0.20 |
| $\mathrm{Pb}$ | 7.2 | 0.080 |
| $\mathrm{Sn}$ | 3.7 | 0.031 |
| $\mathrm{Th}$ | 1.4 | 0.00016 |
| $\mathrm{Zn}$ | 0.87 | 0.0053 |


| $\mathrm{Nb}_{3} \mathrm{Al}$ | 18 | 32 |
| :--- | :--- | :--- |
| $\mathrm{Nb}_{3} \mathrm{Ge}$ | 23 | 38 |
| $\mathrm{Nb}_{3} \mathrm{Sn}$ | 18 | 25 |
| $\mathrm{NbTi}$ | 9.3 | 15 |

Table 9.5 Critical Temperature and Critical Magnetic Field at $T=0 \mathrm{~K}$ for Various Superconductors

Type II superconductors are generally compounds or alloys involving transition metals or actinide series elements. Almost all superconductors with relatively high critical temperatures are type II. They have two critical fields, represented by $B_{\mathrm{c} 1}(T)$ and $B_{\mathrm{c} 2}(T)$. When the field is below $B_{\mathrm{c} 1}(T)$, type II superconductors are perfectly diamagnetic, and no magnetic flux penetration into the material can occur. For a field exceeding $B_{\mathrm{c} 2}(T)$, they are driven into their normal state. When the field is greater than $B_{\mathrm{c} 1}(T)$ but less than $B_{\mathrm{c} 2}(T)$, type II superconductors are said to be in a mixed state. Although there is some magnetic flux penetration in the mixed state, the resistance of the material is zero. Within the superconductor, filament-like regions exist that have normal electrical and magnetic properties interspersed between regions that are superconducting with perfect diamagnetism. A representation of this state is given in Figure 9.31. The magnetic field is expelled from the superconducting regions but exists in the normal regions. In general, $B_{\mathrm{c} 2}(T)$ is very large compared with the critical fields of type I superconductors, so wire made of type II superconducting material is suitable for the windings of high-field magnets.

## EXAMPLE 9.7

## Niobium Wire

In an experiment, a niobium (Nb) wire of radius $0.25 \mathrm{~mm}$ is immersed in liquid helium ( $T=4.2 \mathrm{~K}$ ) and required to carry a current of $300 \mathrm{~A}$. Does the wire remain superconducting?

## Strategy

The applied magnetic field can be determined from the radius of the wire and current. The critical magnetic field can be determined from Equation 9.1, the properties of the superconductor, and the temperature. If the
applied magnetic field is greater than the critical field, then superconductivity in the Nb wire is destroyed.

## Solution

At $T=4.2 \mathrm{~K}$, the critical field for $\mathrm{Nb}$ is, from Equation 9.1 and Table 9.5,

$$
B_{\mathrm{c}}(4.2 \mathrm{~K})=B_{\mathrm{c}}(0)\left[1-\left(\frac{4.2 \mathrm{~K}}{9.3 \mathrm{~K}}\right)^{2}\right]=(0.20 \mathrm{~T})(0.80)=0.16 \mathrm{~T}
$$

In an earlier chapter, we learned the magnetic field inside a current-carrying wire of radius a is given by

$$
B=\frac{\mu_{0} I}{2 \pi a}
$$

where $r$ is the distance from the central axis of the wire. Thus, the field at the surface of the wire is $\frac{\mu_{0} I_{r}}{2 \pi a}$. For the niobium wire, this field is

$$
B=\frac{\left(4 \pi \times 10^{-7} \mathrm{Tm} / \mathrm{A}\right)(300 \mathrm{~A})}{2 \pi\left(2.5 \times 10^{-4} \mathrm{~m}\right)}=0.24 \mathrm{~T}
$$

Since this exceeds the critical $0.16 \mathrm{~T}$, the wire does not remain superconducting.

## Significance

Superconductivity requires low temperatures and low magnetic fields. These simultaneous conditions are met less easily for Nb than for many other metals. For example, aluminum superconducts at temperatures 7 times lower and magnetic fields 18 times lower.

## Theory of Superconductors

A successful theory of superconductivity was developed in the 1950s by John Bardeen, Leon Cooper, and J. Robert Schrieffer, for which they received the Nobel Prize in 1972. This theory is known as the BCS theory. BCS theory is complex, so we summarize it qualitatively below.

In a normal conductor, the electrical properties of the material are due to the most energetic electrons near the Fermi energy. In 1956, Cooper showed that if there is any attractive interaction between two electrons at the Fermi level, then the electrons can form a bound state in which their total energy is less than $2 E_{\mathrm{F}}$. Two such electrons are known as a Cooper pair.

It is hard to imagine two electrons attracting each other, since they have like charge and should repel. However, the proposed interaction occurs only in the context of an atomic lattice. A depiction of the attraction is shown in Figure 9.32. Electron 1 slightly displaces the positively charged atomic nuclei toward itself as it travels past because of the Coulomb attraction. Electron 2 "sees" a region with a higher density of positive charge relative to the surroundings and is therefore attracted into this region and, therefore indirectly, to electron 1. Because of the exclusion principle, the two electrons of a Cooper pair must have opposite spin.

The BCS theory extends Cooper's ideas, which are for a single pair of electrons, to the entire free electron gas. When the transition to the superconducting state occurs, all the electrons pair up to form Cooper pairs. On an atomic scale, the distance between the two electrons making up a Cooper pair is quite large. Between these electrons are typically about $10^{6}$ other electrons, each also pairs with a distant electron. Hence, there is considerable overlap between the wave functions of the individual Cooper pairs, resulting in a strong correlation among the motions of the pairs. They all move together "in step," like the members of a marching band. In the superconducting transition, the density of states becomes drastically changed near the Fermi level. As shown in Figure 9.33, an energy gap appears around $\boldsymbol{E}_{F}$ because the collection of Cooper pairs has lower ground state energy than the Fermi gas of noninteracting electrons. The appearance of this gap characterizes the superconducting state. If this state is destroyed, then the gap disappears, and the density of states reverts to that of the free electron gas.

The BCS theory is able to predict many of the properties observed in superconductors. Examples include the Meissner effect, the critical temperature, the critical field, and, perhaps most importantly, the resistivity becoming zero at a critical temperature. We can think about this last phenomenon qualitatively as follows. In a normal conductor, resistivity results from the interaction of the conduction electrons with the lattice. In this
interaction, the energy exchanged is on the order of $k_{\mathrm{B}} T$, the thermal energy. In a superconductor, electric current is carried by the Cooper pairs. The only way for a lattice to scatter a Cooper pair is to break it up. The destruction of one pair then destroys the collective motion of all the pairs. This destruction requires energy on the order of $10^{-3} \mathrm{eV}$, which is the size of the energy gap. Below the critical temperature, there is not enough thermal energy available for this process, so the Cooper pairs travel unimpeded throughout the superconductor.

Finally, it is interesting to note that no evidence of superconductivity has been found in the best normal conductors, such as copper and silver. This is not unexpected, given the BCS theory. The basis for the formation of the superconducting state is an interaction between the electrons and the lattice. In the best conductors, the electron-lattice interaction is weakest, as evident from their minimal resistivity. We might expect then that in these materials, the interaction is so weak that Cooper pairs cannot be formed, and superconductivity is therefore precluded.

