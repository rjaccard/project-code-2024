Quantifiers. Refer to the book for additional background on the material presented during this lecture.

Propositional functions and the quantifiers $\forall, \exists$, and $\exists$ !. A propositional function is a statement involving a number of variables that becomes a proposition (a statement that is either true or false, but not both) as soon as values have been chosen for all variables. Example: $P(x)$ can be defined as the statement " $x$ is prime". It follows that $P(1)$ is false (because 1 is not a prime but a unit), $P(2)$ and $P(3)$ are true, $P(4)$ is false, etc. $Q(x, y)$ can be defined as the statement $x+y=7$. Then $Q(x, 6)$ is still a propositional function (though in one variable), and $Q(3,4)$ is true, $Q(2,6)$ is false, etc.

Universal quantifier. If a propositional function $P(x)$ evaluates to true for all possible values of $x$ in the domain $D$ of $P$, then we can write

$$
\forall x \quad P(x)
$$

and we say "for all $x \in D$ it is the case that $P(x)$ is true". One could argue that it is better to say "for all $x$ it is the case that if $x \in D$ then $P(x)$ is true", because the latter formulation implies that any statement of the form " $\forall x P(x)$ " is true, irrespective of $P(x)$, if the domain of $x$ is empty. See more on this issue below.

Domain restrictions on $x$ can be included in any (clear) way you see fit. For instance

$$
\forall x \in S \quad P(x)
$$

states that for all $x$ in the subset ${ }^{1} S$ of the domain $D$ of $P$ it is the case that $P(x)$ is true; but see below for an important remark on this subdomain notation.[^0]

Existential quantifier. Similarly, if a propositional function $Q(x)$ evaluates to true for at least one value $x$ in the domain $D$ of $Q$, then we can write

$$
\exists x Q(x)
$$

and we say "there exists an $x \in D$ for which it is the case that $Q(x)$ is true". Further domain restrictions can be imposed in any (clear) way you like, as with the universal quantifier $\forall$. For instance, one may write $\exists x \in S Q(x)$ for a subset $S$ of $D$ to express that there exists an $x$ in the subset $S$ of $D$ for which $Q(x)$ is true.

To express that there is precisely one value $x$ in the domain of $R$ for which $R(x)$ evaluates to true, we can write

$$
\exists!x R(x)
$$

and we say "there exists precisely one $x$ for which it is the case that $R(x)$ is true".

Quantification over a subdomain. As mentioned above the following types of expressions are quite common (though mostly avoided in the book):

$$
\forall x \in A P(x) \quad \text { and } \quad \exists x \in A P(x)
$$

(One also commonly uses, for some $y \in D$, expressions such as $\forall x \neq y P(x)$ or $\exists x \neq y \quad P(x)$ but these were not discussed in class. They are treated in the same manner as the " $x \in A$ " examples below.)

To be able to correctly manipulate these expressions, it should be properly understood what precisely is meant by them. After a brief discussion in class it was agreed that $\forall x \in A P(x)$ corresponds to

$$
\forall x(x \in A \rightarrow P(x))
$$

but that $\exists x \in A P(x)$ corresponds to

$$
\exists x(x \in A \wedge P(x))
$$

Although this may be "intuitive" or "obvious" to some, it may nevertheless be somewhat confusing that for the " $\forall$ " the proper complete formulation of the expression involves an implication, but that for the " $\exists$ " a conjunction is required, so it makes sense to further illustrate this with a few more examples. These examples were also given during the lecture.

First a brief remark, however, triggered by several questions that I got. The intended meaning of the statement " $\forall x \in A P(x)$ " is indeed just what is expressed by " $\forall x(x \in A \rightarrow P(x))$ ", namely that if $x$ belongs to $A$ then $P(x)$ is true. It should not be interpreted as a statement about elements $x$ that do not belong to $A$ : in particular it does not follow from " $\forall x \in A P(x)$ " that for $x$ not belonging to $A$ the statement $P(x)$ is false.

As a first example, let $D=\{1,2\}, A=\{2\}$, and $P(x)$ the propositional function " $x$ is even". The statement that for all $x$ in $A$ it is the case that $x$ is even (i.e., " $\forall x \in A P(x)$ ") is true, and that is properly expressed by " $\forall x(x \in A \rightarrow P(x))$ ": "for all $x$ in $D$, if $x$ is in $A$ then $x$ is even" is true. However, " $\forall x(x \in A \wedge P(x))$ " would be an incorrect interpretation of " $\forall x \in A P(x)$ ": it is not the case that for all $x$ in the domain it is the case that $x \in A$ (so that " $(x \in A \wedge P(x))$ " is false) because $1 \in D$ but $1 \notin A$ and therefore " $\forall x(x \in A \wedge P(x))$ " is false. That is not the case, so the interpretation " $\forall x(x \in A \wedge P(x))$ " of " $\forall x \in A P(x)$ " is wrong.

Note that whenever $A$ is empty it is the case that " $x \in A$ " is false for all $x$ in the domain, so that " $x \in A \rightarrow P(x)$ " is true irrespective of $P(x)$. It follows that " $\forall x(x \in A \rightarrow P(x))$ " is always true for empty $A$ and therefore " $\forall x \in A P(x)$ " is always true for empty $A$; that this is indeed "reasonable" is further elaborated upon below.

As a second example, let $D=\{1,2\}, B=\{1\}$, and $P(x)$ the propositional function " $x$ is even". The statement that there exists an $x$ in $B$ for which $x$ is even (i.e., " $\exists x \in B \quad P(x)$ ") is false, and that is properly expressed by " $\exists x(x \in B \wedge P(x))$ ": "there exists an $x$ in $D$, such that $x$ is in $B$ and $x$ is even" is false. However, " $\exists x(x \in B \rightarrow P(x))$ " would be an incorrect interpretation of " $\exists x \in B \quad P(x)$ ": there is an $x$ in the domain for which it is the case that $x \notin B$ (so that " $(x \in B \rightarrow P(x))$ " is true) because $2 \in D$ but $2 \notin B$ and therefore " $\exists x(x \in B \rightarrow P(x))$ " is true. That is not the case, so the interpretation " $\exists x(x \in B \rightarrow P(x))$ " of " $\exists x \in B P(x)$ " is wrong.

Note that $x \wedge y$ implies $x \rightarrow y$ but not vice versa, so the $\wedge$-interpretation of " $\forall x \in A$ " is incorrect because it is too restrictive (a true statement could be found false), and the $\rightarrow$-interpretation of " $\exists x \in A$ " is incorrect because it is too liberal (a false statement could be found true).

Quantification over an empty domain. Another example that was discussed during the lecture elaborates further on the fact that irrespective of $P(x)$ the statement " $\forall x \in A P(x)$ " is always true for empty $A$. To simplify matters, assume that the domain $D$ is empty (the same argumentation holds when we restrict ourselves to an empty subdomain $A$ of an non-empty domain $D$; taking an empty domain $D$ simplifies the notation while not affecting the essence of the argument). Everyone (or almost everyone) in class agreed that because there is no $x$ in $D$, the statement " $\exists x P(x)$ " is false, irrespective of $P(x)$, and thus also the statement " $\exists x \neg P(x)$ " is false. Because we allow only two possible truth values we must conclude that the negations " $\neg(\exists x P(x))$ " and " $\neg(\exists x \neg P(x))$ " are both true. This leads to a brief sideremark on the negation of quantifiers, in order to be able to rephrase " $\neg(\exists x P(x))$ " and " $\neg(\exists x \neg P(x))$ " in a useful manner.

Negating existential and universal quantifiers. As argued in the book (and informally shown in class, using "De Morgan" under the assumption that the domain consists of a finite number of elements) is it the case that "if it is not the case that there exists an $x$ such that $P(x)$ is true", then it must be the case that " $P(x)$ is false for all $x$ ", and vice versa. Said differently, the statements " $\neg \exists x P(x)$ " and " $\forall x \neg P(x)$ " are logically equivalent:

$$
\neg(\exists x P(x)) \equiv \forall x \neg P(x)
$$

Negating both sides, we find that " $\neg(\neg(\exists x P(x))) \equiv \neg(\forall x \neg P(x))$ " and therefore (because the two consecutive negations cancel each other) " $\exists x P(x) \equiv \neg(\forall x \neg P(x))$ ". With $Q(x)=\neg P(x)$ and thus $P(x) \equiv \neg Q(x)$ it follows that

$$
\neg(\forall x Q(x)) \equiv \exists x \neg Q(x)
$$

This expresses that if $Q(x)$ is not true for all $x$, then there must be an $x$ for which $Q(x)$ is false, and vice versa.

Returning to the earlier observation that if the domain is empty, then " $\exists x P(x)$ " and " $\exists x \neg P(x)$ " are both false irrespective of $P(x)$ so that " $\neg(\exists x P(x))$ " and " $\neg(\exists x \neg P(x))$ " are both true irrespective of the choice of the propositional function $P(x)$, it now follows, with our two negation rules, that

" $\forall x \neg P(x)$ " and " $\forall x P(x)$ " are both always true whenever the domain is empty, and irrespective of the choice of the propositional function $P(x)$.

Another example (not mentioned in class) that shows that intuition is often a poor guide when dealing with logical statements is the question
does " $\forall x \quad P(x)$ " always imply " $\exists x \quad P(x)$ "?

After all, intuitively, if $P(x)$ is true for all $x$, then there should be an $x$ for which $P(x)$ is true. As the above discussion on empty domains shows, however, the answer to the question is negative, because for an empty domain " $\forall x \quad P(x)$ " is true, while " $\exists x \quad P(x)$ " is false (remember that "true $\rightarrow$ false" is false). If, however, it is known that the domain $D$ is not empty, then " $\forall x P(x) \rightarrow \exists x P(x)$ " is true - but even then, again, " $\forall x \in A P(x) \rightarrow \exists x \in A P(x)$ " is not true for all subdomains $A \subseteq D \neq \emptyset$ because it is false for $A=\emptyset \subset D$.

Nested quantifiers, relevance of nesting order, negation. We introduced nesting of quantifiers using the following example. Let $f$ be some function from a domain $E$ to a codomain $F$, and let $Q(y)$ for $y \in F$ be the propositional function " $y$ has a preimage under $f$ ". Surjectivity of $f$ is then expressed by saying that " $\forall y Q(y) "$, where the domain for $y$ is $F$. But the propositional function $Q(y)$ (" $y$ has a preimage under $f$ ") can equivalently be expressed as "there exists an $x \in E$ such that $f(x)=y$ " and thus as " $\exists x f(x)=y$ " (where the domain for $x$ is understood to be $E$ ). Note that this expression " $\exists x f(x)=y$ " can only make sense in an environment where $y$ exists; because we are trying to express the propositional function $Q(y)$, this $y$ indeed exists.

Using this alternative version of $Q(y)$ we find that surjectivity of $f$ is expressed as $\forall y \exists x f(x)=y$ where the domain of $x \times y$ is $E \times F$. This is an example of the usage of nested quantifiers. Note that the order of the quantifiers and of the variables is important and that just swapping things around leads to entirely different statements:

- $\forall x \exists y f(x)=y$ does not say anything other than that each $x \in E$ has an image, i.e., that $f$ is a function with domain $E$ (and codomain $F$ ) - which we already knew.
- $\exists x \forall y f(x)=y$ says that there is an $x$ that maps to all values $y$ in the codomain. Because $f$ is a function it maps any $x$ to precisely one value, so we find that the codomain has cardinality one.
- $\exists y \forall x f(x)=y$ says that the range (i.e, the set $\{f(x): x \in S\}$ consists of just a single value; note that this is not equivalent to the codomain consisting of a single value as expressed by $\exists x \forall y f(x)=y$. (Remember that the range of a function is not necessarily equal to its codomain; if it is, then the function is surjective.)

Next lecture we will discuss the various nesting possibilities a bit more in depth.

We also saw that injectivity is expressed as $\forall x_{1} \forall x_{2}\left(x_{1} \neq x_{2}\right) \rightarrow\left(f\left(x_{1}\right) \neq f\left(x_{2}\right)\right)$ which, using our subdomain quantification considerations (namely the "hidden" implication when the universal quantifier is used), we can rewrite as $\forall x_{1} \forall x_{2} \neq$ $x_{1} f\left(x_{1}\right) \neq f\left(x_{2}\right)$. Bijectivity is expressed as $\forall y \exists!x f(x)=y$.

Negation of nested quantifiers works just as before: $\neg \exists x P(x) \equiv \forall x \neg P(x)$ and $\neg \forall x Q(x) \equiv \exists x \neg Q(x)$ for any propositional functions $P(x)$ and $Q(x)$. For instance if $P(x)$ is the propositional function " $\forall y R(x, y)$ ", then we find that

$$
\neg \exists x \forall y R(x, y) \equiv \neg \exists x P(x) \equiv \forall x \neg P(x) \equiv \forall x \neg \forall y R(x, y)
$$

which then, using $\neg \forall y R(x, y) \equiv \exists y \neg R(x, y)$, is equivalent to

$$
\forall x \exists y \neg R(x, y)
$$

so that

$$
\neg \exists x \forall y \quad R(x, y) \equiv \forall x \exists y \neg R(x, y) .
$$

The general rule that follows from this example should be clear: when negating a statement consisting of a sequence of quantifiers over some propositional function,
just stubbornly (and blindly) replace all universal quantifiers by existential ones and (simultaneously) all existential quantifiers by universal ones, and negate the propositional function:

$$
\neg \forall x_{1} \exists x_{4} \forall x_{5} \forall x_{2} \exists x_{6} \forall x_{3} \quad T\left(x_{1}, x_{2}, x_{3}, x_{4}, x_{5}, x_{6}\right)
$$

is equivalent to

$$
\exists x_{1} \forall x_{4} \exists x_{5} \exists x_{2} \forall x_{6} \exists x_{3} \neg T\left(x_{1}, x_{2}, x_{3}, x_{4}, x_{5}, x_{6}\right) .
$$

Fooling example. We concluded with the example of the propositional function $F(x, y)$ " $x$ can fool $y$ ", where the domain of $x$ and $y$ consists of some arbitrary set of people. A slightly more extensive discussion than done in class follows below:

- Everybody can fool Zed: $\forall x F(x$, Zed) or $\forall y F(y$, Zed): the name of the quantified variable is irrelevant, as long as there is no conflict with other choices you have made.
- Donald can fool everybody: $\forall y F$ (Donald, $y$ ) or $\forall x F$ (Donald, $x$ ) or $\forall w$ w $F($ Donald,$w)$.
- Everybody can fool somebody: $\forall x \exists y F(x, y)$ or $\forall y \exists x F(y, x)$ but not $\forall y \exists x F(x, y)$ because that would be "everybody can be fooled by somebody"; and, obviously, you cannot replace the name $y$ of the second quantified variable in " $\forall x \exists y F(x, y)$ " by $x$, because $x$ has been used already for another purpose (if you nevertheless insist on doing so, then you will first have to rename $x$ : " $\forall x \exists x \quad F(x, x)$ " is nonsensical but " $\forall z \exists z \quad F(z, x)$ " is correct.

Note that also $\exists y \forall x F(x, y)$ is not correct, as this would mean that there is a person (y) that can be fooled by everyone - $\exists y \forall x F(x, y)$ implies $\forall x \exists y F(x, y)$, but $\forall x \exists y F(x, y)$ does not imply $\exists y \forall x F(x, y)$ : in $\exists y \forall x F(x, y)$ the fooled person is the same for everyone, in $\forall x \exists y F(x, y)$ everyone can fool someone, but it is not necessarily the case that the fooled person is the same person for everyone.

- There is no one who can fool everybody: $\neg \exists x \forall y F(x, y)$ which is equivalent to $\forall x \exists y \neg F(x, y)$ (just blindy apply the negation rules resulting in "for every person $x$ there is someone who will not be fooled by $x$ ", which indeed sounds equivalent).
- Everyone can be fooled by somebody: see above, $\forall y \exists x \quad F(x, y)$.
- No one can fool both Vincent and Jules: $\neg \exists x(F(x$, Vincent $) \wedge F(x$, Jules $))$ which is equivalent to $\forall x \neg(F(x$, Vincent $) \wedge F(x$, Jules $))$ and thus to $\forall x(\neg(F(x$, Vincent $) \vee \neg(F(x$, Jules $))))$.
- Mia can fool exactly two people:

$\exists y \exists z \neq y(F($ Mia, $y) \wedge F(\mathrm{Mia}, z) \wedge \forall x(F(\mathrm{Mia}, x) \rightarrow(x=y \vee x=z)))$.

The solution

$\exists y \exists z \neq y \forall x \notin\{y, z\}(F($ Mia, $y) \wedge F($ Mia, $z) \wedge \neg F($ Mia, $x))$ looks good until one considers a universe that consists of two people, making the domain for the $\forall$ quantifier empty (because $x \notin\{y, z\}$ does not exists) implying (by the "red and bold" statement above) that irrespective of what happens to $y$ and $z$ it is the case that " $\forall x \notin\{y, z\}(F($ Mia, $y) \wedge F($ Mia, $z) \wedge \neg F($ Mia, $x))$ " is true - even if $F(\mathrm{Mia}, y)$ or $F(\mathrm{Mia}, z)$ is false (because, from the point of view of the "V" quantifer, $y$ and $z$ are just environmental variables). Thus, irrespective of how many people Mia can fool, the statement is true in the universe of two people.

To address this problem, the existence of the proper $y$ and $z$ (the two people that Mia can fool) has to be pulled in front of the " $\forall$ ", which is indeed what the first solution does. Note that we can change the correct solution to get another solution:

$\exists y \exists z \neq y(F($ Mia,$y) \wedge F($ Mia,$z) \wedge \forall x \notin\{y, z\} \neg F($ Mia,$x))$ :

now the " $\forall x$ " results in a condition over an empty range (if there are only two people), which is true (see above red and bold again), implying (due to the " $\wedge$ " right in front of it) that it has no effect on the overall truth value of the statement.

As a final remark, note that

$[\exists y \exists z \neq y(F(\mathrm{Mia}, y) \wedge F(\mathrm{Mia}, z))] \wedge \forall x(F(\mathrm{Mia}, x) \rightarrow(x=y \vee x=z))$

is incorrect, because by the time we reach the " $\forall$ " we have left the range of $y$ and $z$ implying that $y$ and $z$ are undefined in the " $(x=y \vee x=z)$ " part.

- There is exactly one person whom everybody can fool: $\exists!y \forall x F(x, y)$. If you prefer not to use $\exists$ ! this becomes more complicated and will be discussed in class during the next lecture. One way to express it would be $\exists y(\forall x F(x, y) \wedge \forall z(\forall x \quad F(x, z) \rightarrow y=z))$.
- No one can fool himself or herself: $\neg \exists F(x, x)$ or equivalently $\forall x \neg F(x, x)$.
- There is someone who can fool exactly one person besides himself or herself: $\exists x \exists y \neq x \quad F(x, y) \wedge \forall z((F(x, z) \wedge x \neq z) \rightarrow y=z)$.
- Esmarelda is the only person who can fool herself: $(\exists!x F(x, x)) \wedge F($ Esmarelda, Esmarelda) or $F($ Esmarelda, Esmarelda) $\wedge \forall x(F(x, x) \rightarrow x=$ Esmarelda) or $F$ (Esmarelda, Esmarelda) $\wedge \forall x \neq$ Esmarelda $\neg F(x, x)$. $\forall x(F(x, x) \rightarrow x=$ Esmarelda) is incorrect, because $F$ (Esmarelda, Esmarelda) may still be false: if " $\forall x \neg F(x, x)$ ", then " $\forall x(F(x, x) \rightarrow$ any_balderdash)" is true because the implication " $0 \rightarrow \ldots$ " is always true, irrespective of what the dots are.

$\exists!x(F(x, x) \wedge x=$ Esmarelda $)$ is incorrect because there may still be someone else (than Esmarelda) that can fool himself or herself: the statement only says that there is a single Esmarelda who can fool herself, but leaves open the possibility that also Marsellus and Butch can fool themselves.

Next lecture. More on nested quantifiers, their negation, and the scope of the quantified variable (Sections 1.4 and 1.5), then moving to rules of inference (Section 1.6 ) and proofs (Section 1.7 and Section 1.8 until "chomp").


[^0]:    ${ }^{1}$ Refer to the book for the definition of a subset of a set. Unfortunately, there is no agreement on subset notation. The book uses $S \subseteq D$ to express that $S$ is a subset of $D$ (i.e., all elements of $S$ belong to $D$ as well) and uses $S \subset D$ to express that $S$ is a proper subset of $D$ (i.e., $S$ is a subset of $D$ but also there is an element in $D$ that does not belong to $S$ ). Others use the symbol $\subsetneq$ for a proper subset. It is quite common (in France, for instance) to use $\subset$ where the book would use $\subseteq$; with this notation $A=B \leftrightarrow(A \subset B) \wedge(B \subset A)$ (for sets $A$ and $B)$ which would, in the book's notation be nonsensical because it should be $A=B \leftrightarrow(A \subseteq B) \wedge(B \subseteq A)$. Confusion galore. In this course we will (try to) make sure that it is always clear what is meant. Similar confusion exists for interval notation, with the French $[0,1[$ incomprehensible to Anglo-Saxons who would write $[0,1)$ : both refer to the real numbers $x$ with $0 \leq x<1$.

