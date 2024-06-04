We (re)discussed several finer points and pitfalls of universal and existential quantifiers. We assumed familiarity with the regular negation rule for the universal quantifier (proved by intimidation in the book, informally using De Morgan during a previous lecture assuming a finite domain, a proof that we will later generalize to "countable" domains)

$$
\neg \forall x P(x) \equiv \exists x \neg P(x)
$$

where $P(x)$ is an arbitrary propositional function, and used it to prove the negation rule for the existential quantifer: because $\neg \forall x P(x) \equiv \exists x \neg P(x)$ holds for any propositional function $P(x)$ it also holds for $\neg P(x)$, so that $\neg \forall x \neg P(x) \equiv$ $\exists x \neg \neg P(x)$ and thus that $\neg \forall x \neg P(x) \equiv \exists x P(x)$. Negating both sides we find $\neg \neg \forall x \neg P(x) \equiv \neg \exists x P(x)$ and therefore

$$
\neg \exists x P(x) \equiv \forall x \neg P(x)
$$

which is the regular negation rule for the existential quantifier.

Negation of subdomain quantification. Although this was part of today's exercises, we repeat the complete proof that the same negation rules as above hold if the quantification takes place over a subdomain, namely that

$$
\neg \forall x \in A P(x) \equiv \exists x \in A \neg P(x) \quad \text { and } \quad \neg \exists x \in A P(x) \equiv \forall x \in A \neg P(x),
$$

where $A \subseteq D$ (and where $D$, as usual, denotes the domain) ${ }^{1}$. In particular it should be pointed out that $\neg \forall x \in A P(x)$ is in general not equivalent to $\exists x \notin A P(x)$ or $\exists x \notin A \neg P(x)$, and also that $\neg \exists x \in A \ldots$ in general does not lead to $\forall x \notin A \ldots$.

To prove the subdomain quantification negation rules, the second logical equivalence follows from the first one using the same trick that we used to prove the regular negation rule for the existential quantifier using the regular negation rule for the universal quantifier. So it suffices to show the full proof that $\neg \forall x \in A P(x)$
Here is how it goes:

$$
\begin{aligned}
\neg \forall x \in A P(x) & \equiv \neg \forall x x \in A \rightarrow P(x) \\
& \equiv \exists x \neg(x \in A \rightarrow P(x)) \quad \text { (regular negation rule) } \\
& \equiv \exists x \neg(x \notin A \vee P(x)) \\
& \equiv \exists x(x \in A \wedge \neg P(x)) \quad \text { (De Morgan) } \\
& \equiv \exists x \in A \neg P(x)
\end{aligned}
$$

where the two $\equiv$ 's use the explicit subdomain formulations that were discussed last time (and that were described in the previous lecture notes), and $\equiv$ uses the logical equivalence $(p \rightarrow q) \equiv(\neg p) \vee q$.

Common misunderstanding of subdomain quantification. Copying from the previous lecture notes: the intended meaning of the statement " $\forall x \in A P(x)$ " is indeed just what is expressed by " $\forall x(x \in A \rightarrow P(x))$ ", namely that if $x$ belongs to $A$ then $P(x)$ is true. It should not be interpreted as a statement about elements $x$ that do not belong to $A$ : in particular it does not follow from " $\forall x \in A P(x)$ " that for $x$ not belonging to $A$ the statement $P(x)$ is false.

The scope of quantification variables. The variable of a quantifier (the $x$ in quantified statements such as $\forall x P(x)$ or $\exists x Q(x))$ exists only within the quantified statement where it is used: before or after the statement the variable $x$ (as used in the quantified statement) does not exist. The scope of a variable is just a term used for the range, or places, where the variable has a meaning. For instance, in $\forall y[\forall x \in A P(x)] \wedge Q(y)$ the variable $\mathrm{x}$ exists only between [ and ], so the part between [ and ] is the scope of the variable $x$ and $x$ cannot occur in any way in $Q(y)$ because that would be out of $x$ 's scope.

It is common to write things like $(\forall x P(x)) \wedge(\exists x Q(x))$ where the variable $x$ in the first $(P)$ part has "nothing to do" with the variable $x$ in the second $(Q)$ part, because the scopes of the two variables do not overlap so that the same name can be used for them; it depends on the circumstances if it is confusing or not: $(\exists x x+1=0) \wedge(\exists x x-1=0)$, though possibly true (depending on the domain) some may find it not so elegant. It would be downright ugly to write things like $\forall x((\forall x \in A P(x)) \wedge Q(x))$, even though the inner $x$ that ranges over $A \subseteq D$ can be argued to have nothing to do with the outer $x$ that ranges over the entire domain $D$. There are no general rules to select variable names: use common sense and avoid misunderstandings. The same remark applies to the use of parentheses (do not be skimpy) and to the use of summation variables (as we will see later).

Unique existential quantification. To be able to derive a negation rule for the unique existential quantifier $\exists$ ! we first have to express $\exists$ ! in terms of the regular universal and existential quantifiers $\forall$ and $\exists$. After a few interesting suggestions we converged to

$$
\exists!x P(x) \equiv \exists x P(x) \wedge \forall z z \neq x \rightarrow \neg P(z)
$$

First of all, we need an $x$ for which $P(x)$ is true. So put that first (" $\exists x P(x)$ "), and call it $x$. Then start worrying about what other elements may do, if they exist: any $z$ that is not equal to $x$ must satisfy that $P(z)$ is false, which is expressed by the second part (to the right of the " $\wedge$ "). It is not always easy to find the right expression and it may be even harder to figure out why a proposed solution is correct or not. As usual it helps to follow different lines of reasoning that lead to the same solution. Practice helps.

The proposed solution is logically equivalent to

$$
\exists x P(x) \wedge \forall z(P(z) \rightarrow z=x)
$$

and also to the nicely concise formulation

$$
\exists x P(x) \wedge \forall z \neq x \neg P(z)
$$

Negation of unique existential quantification. Negation of the first alternative above immediately leads to (using standard manipulations)

$$
\neg \exists!x P(x) \equiv \forall x((\neg P(x)) \vee \exists z z \neq x \wedge P(z))
$$

which is logically equivalent to the concise formulation (which can also be derived directly from the third formulation above)

$$
\forall x(P(x) \rightarrow \exists z \neq x P(z))
$$

We had a closer look at the first formulation to make sure that it makes sense as the negation of a unique existence: if there is not a unique element with a certain property, then there is either no element at all with the property, or there are at least two distinct elements with the property. If $P(x)$ is false for all $x$, then $(\neg P(x)) \vee \exists z z \neq x \wedge P(z)$ is true for all $x$ because $\neg P(x)$ is true for all $x$, so that is all right. Now assume that there is an $x$, say $\bar{x}$, for which $P(\bar{x})$ is true and thus $\neg P(\bar{x})$ is false, then to make $(\neg P(\bar{x})) \vee \exists z z \neq \bar{x} \wedge P(z)$ true (which it must be, because $(\neg P(x)) \vee \exists z z \neq x \wedge P(z)$ is true for all $x)$, the $(\exists z z \neq \bar{x} \wedge P(z))$-part must be true, implying that indeed there must be some $z$ different from $\bar{x}$, for which $P(z)$ is true as well. This was discussed in class.

We did not consider the case where $P(\bar{x})$ is false, for some particular $\bar{x}$, so that $(\neg P(\bar{x})) \vee \exists z z \neq \bar{x} \wedge P(z)$ is true, but where the $(\exists z z \neq \bar{x} \wedge P(z))$-part is true as well due to the existence of a - possibly unique $-z \neq \bar{x}$ for which $P(z)$ is true. Can you argue why that $z$ does not cause trouble - and indeed cannot be the only (i.e., unique) element in the domain for which the propositional function evaluates to true?

Common empty (sub)domain pitfall. Copying from the previous lecture notes: intuition is often a poor guide when dealing with logical statements is the question

$$
\text { does " } \forall x \quad P(x) \text { " always imply " } \exists x \quad P(x) \text { "? }
$$

After all, intuitively, if $P(x)$ is true for all $x$, then there should be an $x$ for which $P(x)$ is true. As the above discussion on empty domains shows, however, the answer to the question is negative, because for an empty domain " $\forall x \quad P(x)$ " is true, while " $\exists x P(x)$ " is false (remember that "true $\rightarrow$ false" is false). If, however, it is known that the domain $D$ is not empty, then " $\forall x P(x) \rightarrow \exists x P(x)$ " is true - but even then, again, " $\forall x \in A P(x) \rightarrow \exists x \in A P(x)$ " is not true for all subdomains $A \subseteq D \neq \emptyset$ because it is false for $A=\emptyset \subset D$.

Nesting order. To show the effect of different nesting order of different quantifiers, let $X$ be a set $\left\{x_{1}, x_{2}, x_{3}\right\}$ of three vertices, let $Y$ be another set $\left\{y_{1}, y_{2}, y_{3}\right\}$ of three vertices, and let $S_{i}(x, y)$ for $0 \leq i<8$ be the eight distinct propositional functions from $X \times Y$ to $\{0,1\}$ where $S_{i}(x, y)$ is true if and only if there is an edge between $x$ and $y$ as pictured:

The table lists which of $\exists x \exists y S_{i}(x, y), \exists x \forall y S_{i}(x, y), \forall y \exists x S_{i}(x, y), \exists y \forall x S_{i}(x, y)$, $\forall x \exists y S_{i}(x, y)$ and $\forall x \forall y S_{i}(x, y)$ hold for $S_{i}$ for $0 \leq i<8$. Note that for any propositional function $S(x, y)$ (and not just for the $S_{i}$ 's considered here) it is the case that

$$
\exists x \forall y S(x, y) \rightarrow \forall y \exists x S(x, y)
$$

and, equivalently,

$$
\exists y \forall x S(x, y) \rightarrow \forall x \exists y S(x, y)
$$

(the two $\rightarrow$ 's in the table); this fact is further discussed below. The converse of those two implications does in general not hold, as proved by the two 4 's in the table.

It follows that, in general, the nesting order of distinct quantifiers matters and that switching distinct quantifiers around will change the meaning of the expression. Switching around directly consecutive identical quantifiers, however, does not change the meaning: " $\forall x \forall y \ldots$..." is equivalent to " $\forall y \forall x \ldots$..." (assuming the "..."-parts are the same) and may be written as " $\forall x, y \ldots$ ". Similarly, " $\exists x \exists y \ldots$.." is equivalent to " $\exists y \exists x \ldots . "$ (again assuming the "..."-parts are the same) and may be written as “ $\exists x, y \ldots$.

Rules of inference for quantifiers. See Table 2 in Section 1.6 of the book for these rules. Note that it is assumed that the domain is not empty.

Universal instantiation: from $\forall x P(x)$, it follows that $P(c)$ is true for arbitrary $c$ in the domain: thus, a $c$ may be chosen that already has a meaning in the context before the universal instantiation was applied. This is written in the following manner (with ".." pronounced as "therefore"):

Universal generalization: if $P(c)$ is true for arbitrary $c$ in the domain, it follows that $\forall x P(x)$ :

Existential instantiation: from $\exists x P(x)$, it follows that $P(c)$ is true for some $c$ in the domain - but this is a $c$ that is at this point newly introduced in the context, and that, in general, cannot be chosen as an element that already has a meaning in the context before the existential instantiation was applied:

$\exists x P(x)$

$\therefore \overline{P(c) \text { for some element } c}$

Existential generalization: if $P(c)$ is true for some particular $c$ in the domain, it follows that $\exists x P(x)$ :

$\therefore \quad \frac{P(c) \text { for some element } c}{\exists x P(x)}$

$\exists y \forall x$ implies $\forall x \exists y$ but not vice versa. The "not vice versa" part follows from the rightmost $\nLeftarrow$ above. The implication $\exists y \forall x S(x, y) \rightarrow \forall x \exists y S(x, y)$ can be argued to be correct in the following manner. We may consider " $\forall x S(x, y)$ " as a propositional function $Q(y)$ in the variable $y$, so that $\exists y \forall x S(x, y)$ becomes $\exists y Q(y)$. Using existential instantiation we get that $Q(d)$ is true for some element $d$ in the domain (of $y$ ) and thus that $\forall x S(x, d)$ is true for that $d$. For arbitrary $x$, say $\bar{x}$, it is thus the case that $S(\bar{x}, d)$ is true (universal instantiation) and thus, using existential generalization, that $\exists y S(\bar{x}, y)$ is true. Now $\exists y S(x, y)$ can be regarded as a propositional function in the variable $x$, which is true for arbitrary $x$, so that universal generalization leads to $\forall x \exists y S(x, y)$.

Trying to use the same proof approach to prove this the other way around fails obviously, because the other way around is wrong: if we apply existential instantiation to $\forall x \exists y S(x, y)$ we must realize that $\forall x \exists y S(x, y)$ stands for $\forall x(\exists y S(x, y))$ and that the existential instantiation is actually separately applied to each particular element $x$ in the domain of $x$. Thus, we get $\forall x\left(S\left(x, d_{x}\right)\right.$ for some $\left.d_{x}\right)$ where $d_{x}$ indicates that it is a value that may vary from one $x$ to the next. There is no way these possibly distinct $d_{x}$-values can be "pulled out of" the parentheses to lead to something like $\forall x(S(x, d))$ for some $d$, as would be required to be able to achieve $\exists y \forall x S(x, y)$. But, as mentioned, the counterexample given above already proves that $\forall x \exists y S(x, y)$ does in general not imply $\exists y \forall x S(x, y)$. Nevertheless, it may be useful to see where the proof-attempt fails.

More on quantifier rules of inference (not done in class). Last time we used the propositional function $F(x, y)$ " $x$ can fool $y$ " to express "Esmarelda can fool everybody" as $\forall y F$ (Esmarelda, $y$ ). Given " $\forall y F$ (Esmarelda, $y$ )" we can use universal instantiation to instantiate the $y$ with any person of our choice, so we can derive " $F$ (Esmarelda, Bruce)", " $F$ (Esmarelda, Marsellus)", or any other person we see fit: no matter whom we choose, he or she can be fooled by Esmarelda - even Bonnie can be fooled by Esmarelda. Intuitively that makes perfect sense because, after all, Esmarelda can fool everyone - which includes Bruce and Marsellus - and Bonnie. If we are just given " $F$ (Esmarelda, Bruce)" and " $F$ (Esmarelda, Marsellus)", however, and in particular not knowing that " $\forall y F$ (Esmarelda, $y$ )", we cannot conclude " $\forall y F($ Esmarelda, $y)$ " or even just " $F$ (Esmarelda, Bonnie)"

Given " $F($ Esmarelda, Bruce)" we can use existential generalization to generalize Esmarelda and find " $\exists x F(x$, Bruce)": there is someone who can fool Bruce, again an intuitively obvious consequence of the fact that Esmarelda can fool everyone. We could also have derived there is someone who can fool Bruce from " $\forall y F$ (Esmarelda, $y$ )" by first using existential generalization to generalize Esmarelda ${ }^{2}$, resulting in " $\exists x \forall y F(x, y)$ ": "there is someone who can fool everybody, and then apply universal instantiation to the " $\forall y F(x, y)$ "-part of " $\exists x \forall y F(x, y)$ " to obtain " $\exists x F(x$, Bruce $)$.

To further complicate matters, we could also apply the existential generalization to just the " $F$ (Esmarelda, $y$ )"-part of " $\forall y F$ (Esmarelda, $y$ )", but when doing so we have to keep in mind that if we consider just " $F$ (Esmarelda, $y$ )" (without remembering where it came from) we have no access to the information that " $F$ (Esmarelda, $y$ )" is valid for all $y$. Thus, when existentially generalizing in " $F$ (Esmarelda, $y$ )" Esmarelda to some $x$, the $x$ may, in principle, depend on $y$, which we denote by $x_{y}$ : we find " $\exists x_{y} F\left(x_{y}, y\right)$ ". Including this result " $\exists x_{y} F\left(x_{y}, y\right)$ " again in the statement " $\forall y F$ (Esmarelda, $y$ )" where it came from, we conclude that " $\forall y \exists x_{y} F\left(x_{y}, y\right)$ ": everyone can be fooled by someone, again an intuitively correct consequence of the fact that Esmarelda can fool everyone, but losing the fact that not just everyone can be fooled by someone, but everyone can be fooled by the same someone (namely Esmarelda). Note that " $\exists x \forall y F(x, y)$ " implies " $\forall y \exists x_{y} F\left(x_{y}, y\right)$ " (first existentially instantiate " $\exists x \forall y F(x, y)$ " resulting in " $\forall y F(c, y)$ " for some person $c$, and then existentially generalize the (now $y$-dependent!) " $F(c, y)$ "-part to obtain " $\forall y \exists x_{y} F\left(x_{y}, y\right)$ " - as seen in detail above); reverting the latter again to " $\exists x \forall y F(x, y)$ " is impossible because the $x_{y}$ is now, due to the way it was constructed, $y$-dependent.

The lecture was concluded by listing several common rules of inference (which you can find in Table 1 in Section 1.6 of the book), i.e., tautologies of the form $(A \wedge B) \rightarrow C$ and $B \rightarrow C$ (for compound propositions $A, B, C)$ which are written as

To prove that compound propositions of the form $(A \wedge B) \rightarrow C$ or $B \rightarrow C$ are tautologies it suffices to consider the cases where $A$ and $B$ are both true and to show that $C$ is true, because if the left hand sides are false, the implications are true anyhow. Thus, if $p$ is true, then $p \vee q$ is true, so that $p \rightarrow(p \vee q)$ is a tautology, known as "addition" and denoted as

$$
\therefore \frac{p}{p \vee q}
$$

Similarly, if $p \wedge q$ is true, then $p$ is true, so that $(p \wedge q) \rightarrow p$ is a tautology, known as "simplification" and denoted as

$$
\therefore p \text { p }
$$

That $(p \wedge q) \rightarrow(p \wedge q)$ is a tautology cannot come as a surprise: it leads to the "conjunction"

$$
\begin{gathered}
p \\
\therefore \frac{q}{p \wedge q}
\end{gathered}
$$[^0]

If $p$ is true then in order for $p \rightarrow q$ to be true, $q$ must be true, so $(p \wedge(p \rightarrow q)) \rightarrow q$ is a tautology, known as "modus ponens", and similarly if $\neg q$ is true then in order for $p \rightarrow q$ to be true, $p$ must be false, so $((\neg q) \wedge(p \rightarrow q)) \rightarrow \neg p$ is a tautology, known as "modus tollens":

$$
\begin{array}{ll}
p & \neg q \\
\therefore \bar{p} & \therefore \frac{p \rightarrow q}{\neg p}
\end{array}
$$

A more interesting tautology is called "resolution": in order for $p \vee q$ and $(\neg p) \vee r$ to be both true, $r$ must be true if $p$ is true and $q$ must be true if $p$ is false, so that $q \vee r$ must be true, which shows that $((p \vee q) \wedge((\neg p) \vee r)) \rightarrow(q \vee r)$ is a tautology:

$\begin{aligned} & p \vee q \\ & \therefore \frac{\neg p \vee r}{q \vee r}\end{aligned}$

With the usual "replace $p$ by $\neg p$ " trick, resolution is seen to be equivalent to the tautology $((p \rightarrow q) \wedge(\neg p \rightarrow r)) \rightarrow(q \vee r)$, which is intuitively obvious from a simple example such as "if it rains we go shopping and if it does not rain we go skiing, thus we go shopping or skiing" $"$.

Finally, there are the two syllogisms: the "hypothetical" one $((p \rightarrow q) \wedge(q \rightarrow$ $r)) \rightarrow(p \rightarrow r)$ and the "disjunctive" one $((p \vee q) \wedge(\neg p)) \rightarrow q$, which are both easily seen to be tautologies: for the former, if is $p$ false then $p \rightarrow r$ is true thus the left hand side is irrelevant, and if $p$ is true, $q$ must be true to make $p \rightarrow q$ true, so that $r$ must be true to make $q \rightarrow r$ true, so $p \rightarrow r$ is true as well. For the latter if $\neg p$ is true, the truth of $p \vee q$ implies the truth of $q$.

You may find it interesting to remember the names of the rules of inference, but for the exams they are not required.

Next time we will see a simple application of these rules of inference (including the ones for quantifiers) and then move to proofs.

Next class. Rules of inference example, elementary proof examples. Reading: sorry about the confusion, in these notes and on moodle, caused by the many different versions of the book. Briefly, read the remaining material in Chapter 1 until "chomp", but you can skip "normal forms". Thus, if you use the 8th edition, then read sections $1.6,1.7$, and 1.8 until "chomp"; if you use the printed 7 th edition, then read sections 1.6, 1.8, and 1.9 until "chomp" (section 1.7 on normal forms can be skipped); if you're using the online 7th edition, read section 1.6, 1.7, and 1.8 until "chomp". If you're using the 6 th edition, read sections $1.5,1.6$, and 1.7 until "chomp".[^1]


[^0]:    ${ }^{2}$ Let the propositional function $P(x)$ be " $x$ can fool everybody", then $P(x) \equiv \forall y F(x, y)$ and $P($ Esmarelda $) \equiv \forall y F($ Esmarelda, $y)$. Existential generalization of " $P($ Esmarelda)" leads to " $\exists x P(x)$ " which is logically equivalent to " $\exists x \forall y F(x, y)$ ".

[^1]:    ${ }^{3}$ Note that $((p \rightarrow q) \wedge(\neg p \rightarrow r)) \rightarrow(q \oplus r)$ is not a tautology, because with $q$ and $r$ both true the left hand side is true and the right hand side is false.

