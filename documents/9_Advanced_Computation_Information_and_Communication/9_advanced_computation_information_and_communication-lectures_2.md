Remember the definition of logical equivalence: if for compound propositions $r$ and $s$ (so both $r$ and $s$ consist of any valid formula involving any number of propositional variables and logical operators) it is the case that $r \leftrightarrow s$ is a tautology (i.e., $r \leftrightarrow s$ is always true irrespective of the truth values of the propositional variables that occur in $r$ and $s$ - which does not imply that $r$ is always true or that $s$ is always true!), then $r$ and $s$ are logically equivalent, denoted by $r \equiv s$.

Familiarize yourself with the logical equivalences in Table 6 . No need to learn their names by heart, with one exception: it is useful to know what "De Morgan" refers to: the negation of a conjunction is "the same as" (i.e., logically equivalent to) the disjunction of the negations $(\neg(p \wedge q) \equiv(\neg p) \vee(\neg q))$, and the negation of a disjunction is the same as the conjunction of the negations $(\neg(p \vee q) \equiv(\neg p) \wedge(\neg q))$.

Given $\neg(p \wedge q) \equiv(\neg p) \vee(\neg q)$ (which was proved using a truth table) we proved that $\neg(p \vee q) \equiv(\neg p) \wedge(\neg q)$ using two simple substitutions of variable names, a trick that is often found to be confusing - this time was no exception. Keep in mind that in a statement such as $\neg(p \wedge q) \equiv(\neg p) \vee(\neg q)$ the $p$ and $q$ are just arbitrary names for propositional values, and may be replaced by any other name or any other propositional value one sees fit. As a slight (and possibly even more confusing) variation on the substitutions used in class, we may replace $p$ by $\neg p$ and $q$ by $\neg q$ (after all, if $p$ and $q$ are arbitrary propositional values, then so are $\neg p$ and $\neg q)$ in $\neg(p \wedge q) \equiv(\neg p) \vee(\neg q)$, which results in $\neg((\neg p) \wedge(\neg q)) \equiv(\neg \neg p) \vee(\neg \neg q)$ which is trivially equivalent to $\neg((\neg p) \wedge(\neg q)) \equiv p \vee q$ (just omit the two occurrences of " $\neg \neg$ "), which is equivalent to $\neg \neg((\neg p) \wedge(\neg q)) \equiv \neg(p \vee q)$ (negate both sides) and thus to $(\neg p) \wedge(\neg q) \equiv \neg(p \vee q)$ which is the same as the desired $\neg(p \vee q) \equiv(\neg p) \wedge(\neg q)$.

In Table 7 you will find some logical equivalences that may be less intuitive than the ones from Table 6. Useful to remember are the equivalences $(p \rightarrow q) \equiv((\neg p) \vee q)$ and $(p \rightarrow q) \equiv((\neg q) \rightarrow(\neg p))$. Here $(\neg q) \rightarrow(\neg p)$ is the "contrapositive" of $p \rightarrow q$ : thus, an implication and its contrapositive are logically equivalent. In this context, two other common terms are the "converse" and the "inverse" of $p \rightarrow q$ : the converse of $p \rightarrow q$ is $q \rightarrow p$ and the inverse of $p \rightarrow q$ is $(\neg p) \rightarrow(\neg q)$; note that the converse and inverse are logically equivalent. They are not logically equivalent to the implication $p \rightarrow q$ or its contrapositive $(\neg q) \rightarrow(\neg p)$.

Two logical equivalences from Table 7 that may be particularly confusing are

$$
(p \rightarrow r) \wedge(q \rightarrow r) \equiv(p \vee q) \rightarrow r \quad \text { and } \quad(p \rightarrow r) \vee(q \rightarrow r) \equiv(p \wedge q) \rightarrow r
$$

As shown below, the right-hand side of the former, i.e., $(p \vee q) \rightarrow r$, (and thus, due to the logical equivalence, the left hand side $(p \rightarrow r) \wedge(q \rightarrow r)$ as well), implies $(p \wedge q) \rightarrow r$ for any choice of truth values of $p, q$, and $r$, i.e., $((p \vee q) \rightarrow r) \rightarrow$ $((p \wedge q) \rightarrow r)$ is a tautology. However, it is not the case that $(p \vee q) \rightarrow r$ and $(p \wedge q) \rightarrow r$ are logically equivalent: indeed, $(p \wedge q) \rightarrow r$ does not imply $(p \vee q) \rightarrow r$. These statements can be verified by inspecting the truth table below:

| $p$ | $q$ | $r$ | $p \rightarrow r$ | $q \rightarrow r$ | $(p \rightarrow r) \wedge(q \rightarrow r)$ | $p \vee q$ | $(p \vee q) \rightarrow r$ | $(p \rightarrow r) \vee(q \rightarrow r)$ | $p \wedge q$ | $(p \wedge q) \rightarrow r$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 |
| 0 | 0 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 |
| 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 |  |
| 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 |
|  |  |  |  | 1 |  |  | 1 | 1 |  |  |

In this table, the blue columns are identical (showing that $((p \rightarrow r) \wedge(q \rightarrow r)) \leftrightarrow$ $((p \vee q) \rightarrow r)$ is a tautology and thus that $(p \rightarrow r) \wedge(q \rightarrow r) \equiv(p \vee q) \rightarrow r)$ and so are the red ones (showing that $((p \rightarrow r) \vee(q \rightarrow r)) \leftrightarrow((p \wedge q) \rightarrow r)$ is a tautology and thus that $(p \rightarrow r) \vee(q \rightarrow r) \equiv(p \wedge q) \rightarrow r)$. Furthermore, for each row, for a value $v$ in the blue column and $w$ in the red column the implication $v \rightarrow w$ is true, whereas the converse $w \rightarrow v$ is not always true (as indicated by the two $\leftarrow \mathrm{s}$ ); said differently, $((p \vee q) \rightarrow r) \rightarrow((p \wedge q) \rightarrow r)$ is a tautology, but the converse $((p \wedge q) \rightarrow r) \rightarrow((p \vee q) \rightarrow r)$ is a contingency.

As a side remark note that the truth table above has eight rows: there are two distinct choices for the truth value $p$, for each distinct choice of $p$ the truth value $q$ can be chosen in two distinct ways, giving rise to a total of $2 \times 2=4$ distinct choices for the pair of truth values $(p, q)^{1}$, and for each of those four distinct choices of a pair of truth values the truth value $r$ can be chosen in two distinct ways, finally leading to a total of $4 \times 2=8$ distinct choices for the triple of truth values $(p, q, r)$. This is an example of two applications of the "product rule", one of the basic counting principles that we will discuss more extensively later in the course. Looks very obvious, and it is obvious indeed, but you may want to ponder why the number of distinct pairs above is indeed $2 \times 2=4$ and "not" $2+2$, despite the fact that the latter is also equal to four.

Except for the tautologies of the form $r \leftrightarrow s$ that lead to logical equivalences, there are tautologies of the form $r \wedge s \rightarrow t$ (for compound propositions $r, s$, and $t$ ). They are also considered to be useful, because they lead to so-called "rules of inference" (which we will see more of next week). For instance $(p \wedge(p \rightarrow q)) \rightarrow q$ is a tautology ${ }^{2}$, and is known as "modus ponens": no matter what the individual truth values of $p$ and $q$ may be, the "rule" $(p \wedge(p \rightarrow q)) \rightarrow q$ is always valid. Other rules of inference will be discussed later.

During the Tuesday September 25 lecture we will discuss some examples (cf. below) involving logical values, after which we will discuss logic circuits, have a brief look at (binary) addition, carries, and various ways to multiply integers, before we move (probably not before Friday September 28) to propositional functions and quantifiers.[^0]


[^0]:    ${ }^{1}$ In the terminology of the Tuesday September 18 lecture, these are ordered pairs.

    ${ }^{2}$ It is not the case that $(p \wedge(p \rightarrow q)) \equiv q$ as we - painfully - noticed using a truth table.

