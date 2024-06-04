Logical operators are just functions from a particular domain $D$ to the codomain $C=\{0,1\}$ where $D=C$ for the negation operator $\neg$ and $D=C^{2}$ for $\wedge, \vee, \oplus, \rightarrow$ and $\leftrightarrow^{1}$ (except they are written a bit differently from how functions are normally written: we do not write $\neg(p)$ or $\wedge(p, q)$ but write $\neg p$ and $p \wedge q)$. Note that $\neg$ is a bijection ${ }^{2}$ and that $\wedge, \vee, \oplus, \rightarrow$ and $\leftrightarrow$ are surjective but not injective (and thus not bijections). Compound propositions are compositions of the functions $\neg, \wedge, \vee, \oplus, \rightarrow$ and $\leftrightarrow$. A compound proposition that is surjective is called a "contingency" and a compound proposition that is not surjective is either a "contradiction" (if its range equals $\{0\} \subsetneq\{0,1\}=C$ ) or a "tautology" (if its range equals $\{1\} \subsetneq\{0,1\}=C$ ) — note that the negation of a contradiction is a tautology and vice versa, and that the negation of a contingency is again a contingency. Note that the compound propositions $p \wedge q, p \vee q, p \oplus q, p \rightarrow q$, and $p \leftrightarrow q$ are all contingencies.

Two types of tautologies are noteworthy:

Logical equivalence: If a compound proposition of the form $A \leftrightarrow B$ (for compound propositions $A$ and $B$ ) is a tautology, then $A \equiv B: A$ and $B$ are "logically equivalent".

Rules of inference: If a compound proposition of the form $(A \wedge B) \rightarrow C$ (for compound propositions $A, B$ and $C$ ) is a tautology, it may be referred to as a "rule of inference".

As we have seen last time, $C^{2}$ is the Cartesian product of $C=\{0,1\}$ by itself, so the elements of $D=C^{2}$ are the four (namely $|C|^{2}=2^{2}=4$ ) ordered pairs $(0,0),(0,1),(1,0),(1,1)$.

Useful observation. For compound propositions $p$ and $q$, we have seen that

- $p \vee q \equiv \neg(\neg p \wedge \neg q)$
- $p \oplus q \equiv(\neg(\neg p \wedge \neg q)) \wedge \neg(p \wedge q)$
- $p \rightarrow q \equiv \neg(p \wedge \neg q)$
- $p \leftrightarrow q \equiv(\neg(p \wedge \neg q)) \wedge(\neg(\neg p \wedge q))$

where we only have negations and conjunctions on the right hand sides. All logical operators can thus be expressed using just negations and conjunctions.

Logic circuits. We very informally introduced nmos and pmos transistors and how they can be used to realize negation.

nmos transistor. The leftmost part of Figure 1 on the next page shows the $\underline{n} m o s$ ("pull-down") transistor: if there is current (' 1 ') on the leftmost (horizontal) wire, then there is a connection between the vertical bottom and top wires on the right (as illustrated in the middle picture of Figure 1), but if there is no current (' 0 ') on the leftmost (horizontal) wire, then there is no connection between the vertical bottom and top wires on the right (as illustrated in the rightmost picture of Figure 1). The nmos transistor is particularly effective for grounding, i.e., to pull the current in a wire down to zero, a value that we treat as a "logical zero", or "false".

pmos transistor. Similarly but conversely, the leftmost part of Figure 2 on the next page shows the pmos ("pull-up") transistor: if there is current (' 1 ') on the leftmost (horizontal) wire, then there is no connection between the vertical top and bottom wires on the right (as illustrated in the middle picture of Figure 2), but if there is no current (' 0 ') on the leftmost (horizontal) wire, then there is a connection between the vertical top and bottom wires on the right (as illustrated in the rightmost picture of Figure 2). The pmos transistor is particularly effective to let the current flow, i.e., to pull the current in a wire up to one, a value that we treat as a "logical one", or "true".

In both figure 1 and 2 the direction of the arrows is irrelevant: the only thing that matters is if there is a connection or not.

cmos circuit. Using these two basic building blocks (nmos and pmos transistors), we considered the cmos (complementary metal-oxide-semiconductor) circuit depicted in the leftmost part of Figure 3 on the next page (the leftmost part of which is a "battery"), and argued that the output $X$ equals $\neg A$, where $A \in\{0,1\}$ is the input. Make sure that you understand how this works given what we have assumed about the functionality of the nmos and pmos transistors; the middle and rightmost part of Figure 3 may be helpful. There are two important design principles behind this particular cmos circuit (and behind the design of all cmos circuits considered in this class):

(1) The top right part of the left picture of Figure 3 computes a value that is complementary to (i.e., the negation of) what is computed by the lower right part of the left picture; it follows that the output signal $X$ is always connected to either "current" (" 1 ') or to "ground" (' 0 ') and thus

- never at the same time to both "current" and "ground" (which would be a short-circuit - not good);
- never connected to neither "current" nor "ground" (which would lead to undefined logical values - not good): because double negations are not good either, note that this is equivalent to saying "always connected to either "current" or "ground"",

all this under the assumption that the input signal $A$ is well-defined (i.e., a proper ' 0 ' or ' 1 ').

(2) The top part consists of only pmos transistors (which are good at providing current), whereas the bottom part uses only nmos transistors (which are good at grounding).

