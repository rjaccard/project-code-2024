Rules of inference application example. Suppose that the following two statements are known to be true:

(1) There is someone here who has been to the USA,

(2) Everyone who has been to the USA likes BKBs,

where the domain is the set of people. For most it will not be hard to conclude that there is someone here who likes BKBs. But how do we "formally" derive this conclusion? That is what rules of inference are about. This application of rules of inference may not be truly convincing, but the same methodology can also be applied in circumstances where it may not be so simple for humans to derive the correct conclusion. Furthermore, rules of inference have the advantage that the line of reasoning can be "mechanically" verified.

In order to apply the rules of inference, we first need to define a few propositional functions:

- $H(x):$ " $x$ is in this class ("here")";
- $U(x):$ " $x$ has been to the USA";
- $L(x): " x$ likes BKBs".

Our initial true statements can now be translated:

fact1: $\exists x(H(x) \wedge U(x))$.

fact2: $\forall x(U(x) \rightarrow L(x))$.

Note the usage of " $\wedge$ " in fact1 and of " $\rightarrow$ " in fact2 and convince yourself that these are the right logical operators in this context: " $\exists x(H(x) \rightarrow U(x))$ " would also be true if the domain is empty, so there is no one, and in particular there is no one in this class, so it would not properly express that "there is someone here who has been to the USA" and, possibly more convincingly, if there even exists a single person not in this class (i.e., for whom $H(x)$ is false), the statement " $\exists x(H(x) \rightarrow U(x))$ " would be true; $\forall x(U(x) \wedge L(x))$ would express that everyone has been to the USA and that everyone likes BKBs, which is not equivalent to our "everyone who has been to the USA likes BKBs".

We are going to use quantified statements fact1 and fact2 along with the rules of inference, as defined in the book in section 1.6, to derive our conclusion "there is someone here who likes BKBs". Using the propositional functions, our desired conclusion "there is someone here who likes BKBs" can be translated into the quantified statement

$$
\text { conclusion: } \exists x(H(x) \wedge L(x))
$$

This may sound like a silly and useless exercise, but it will be seen that it can be done entirely by using the rules in the book, without having to think about, or get distracted by, the USA or BKBs (distraction due to interpretation of the meaning or intended meaning of statements is one of many reasons why proofs may derail).

(1) From " $\exists x(H(x) \wedge U(x))$ " in fact1 we find that $H(c) \wedge U(c)$ is true for some $c$; here we use existential instantiation of the existential quantification " $\exists x(H(x) \wedge U(x))$ ": we know an $x$ exists, so we take one and call it $c$. Note that $c$ is "just" some person $c$ that we did not know anything about before $c$ was selected, and that all we know about $c$ is that $H(c) \wedge U(c)$ is true.

(2) From the fact that $H(c) \wedge U(c)$ is true in (1) it follows that $U(c)$ is true; this is called "simplification".

(3) From the fact that $H(c) \wedge U(c)$ is true in (1) it also follows that $H(c)$ is true; "simplification" again.

(4) From " $\forall x(U(x) \rightarrow L(x))$ " in fact2 we find that $U(c) \rightarrow L(c)$ is true; we use universal instantiation of the universal quantification " $\forall x(U(x) \rightarrow L(x))$ ": we know it is true for all $x$, so in particular it is true for the $c$ that we have (carefully) selected already.

Remark. At this point it is important that the $c$ that is selected (in the universal instantiation) has the desirable properties that were derived in steps (2) and (3). Doing this universal instantiation before the existential instantiation in step (1) would have derailed the proof: if we would first universally instantiate " $\forall x(U(x) \rightarrow L(x))$ " and thus get some arbitrary $z$ for which $U(z) \rightarrow L(z)$ is true, then we cannot later existentially instantiate " $\exists x(H(x) \wedge U(x))$ " with that $z$ : sure, an $x$ exists, but why would it be equal to that particular $z$ ?

(5) Based on the fact that $U(c)$ is true from (2) and that $U(c) \rightarrow L(c)$ is true from (4) we use "modus ponens" to conclude that $L(c)$ is true.

(6) Based on the fact that $H(c)$ is true from (3) and that $L(c)$ is true from (5) we use "conjunction" to conclude that $H(c) \wedge L(c)$ is true.

(7) Finally, using that $H(c) \wedge L(c)$ is true from (6) we use existential generalization to reach the desired conclusion $\exists x(H(x) \wedge L(x))$.

Proofs (almost everything we discussed related to proofs can be found in the book). If the compound proposition $p \rightarrow q$ is shown to be correct by

- assuming that $p$ is true
- followed by some number of correct steps (i.e., rules of inference) that ultimately result in the conclusion that $q$ is true,

then the proof (that $q$ follows from $p$ - which does not imply that $q$ is true, because $p$ is not known to be true but was only assumed to be true) is called a direct proof. If it turns out that the assumption that $p$ is true is correct, then $q$ follows: if we are still clueless about the truth value of $p$ we cannot conclude anything about $q$ yet, but at least we know that if, lo and behold, $p$ turns out to be true, then $q$ is true as well - the correctness of the line of reasoning (the correct pasting together of the rules of inference) has, in principle, nothing to do with the truth value of the input assumptions.

Direct proofs lead in a (more or less) direct manner from the hypotheses ( $p$ in our case) to the conclusion ( $q$ in our case). Sometimes deriving a direct proof works, sometimes it fails or becomes cumbersome, and it may be a better idea to resort to an indirect proof. Indirect proofs come in many variants. Two important ones are very commonly used (and very commonly confused with each other):

A proof by contraposition of $p \rightarrow q$ is nothing but a direct proof of the contrapositive $\neg q \rightarrow \neg p$ (which is, as we have seen in previous lectures, logically equivalent to $p \rightarrow q$ ). Thus, the truth of $\neg q$ is assumed and after a number of correct steps (such as given by rules of inference) the conclusion $\neg p$ is reached. The proof of $p \rightarrow q$ follows because $p \rightarrow q$ is logically equivalent to its contrapositive $\neg q \rightarrow \neg p$. If then $p$ can indeed be shown to be true, the implication $p \rightarrow q$ (logically equivalent to $\neg q \rightarrow \neg p$ ) may then be used to prove $q$ : after all, if $\neg q$, then $\neg p$, contradicting $p$, thus $q$. Note that in particular the input assumption to the proof of $\neg q \rightarrow \neg p$, namely that $\neg q$ is true, is not used in this final line of reasoning quite on the contrary.

and

A proof by contradiction, where the truth of $p$ and $\neg q$ is assumed after which a direct proof is used to derive something that is false leading to the conclusion that at least one of the input assumptions must be wrong. Therefore, if $p$ is known to be true, it must be the case that $\neg q=$ false, so that $q$ must be true. This shows $p \rightarrow q$ because $(p \rightarrow q) \equiv((p \wedge \neg q) \rightarrow$ false $)$ : make sure that you understand the underlined logical equivalence and that you make a truth table if you are not sure that it is correct (as was done in class). This line of reasoning may also be used without $p$, in which case a proof by contradiction of the isolated statement $q$ consists of showing that $\neg q \rightarrow$ false (using that $q \equiv(\neg q \rightarrow$ false) $)$.

Other useful equivalences to consider are " $\neg(p \rightarrow q) \equiv(p \wedge \neg q)$ " (counterexample), "(false $\rightarrow q) \equiv$ true" (vacuous proof: proving that $p \rightarrow q$ is true based on proving that $p$ is false), " $p \rightarrow$ true) $\equiv$ true" (trivial proof: proving that $p \rightarrow q$ is true based on proving that $q$ is true no matter what), and " $p \vee \neg p) \equiv$ true" (case-by-case). If the hypothesis $p$ is not needed, proving $q$ by itself is equivalent to proving $q \vee$ false or the logically equivalent $\neg q \rightarrow$ false.

Proof examples. We followed the examples from the book:

- the direct proof that the product of two integers is odd, which you should be able to reconstruct;
- the corollary that the square of an odd integer is odd, which follows right away indeed;
- the proof by contraposition that if an integer square $a^{2}$ is even, then the number $a$ is even, as a direct proof gets much too complicated, whereas the contraposition leads to a very simple proof based on the above corollary: the square of an odd number (i.e., the negation of the desired conclusion) is odd (according to the corollary) which is the negation of the hypothesis;
- the slightly more involved proof by contradiction that $\sqrt{2}$ is not a rational number (i.e., is irrational, thus in $\mathbf{R}-\mathbf{Q}$ (which is also often written as $\mathbf{R} \backslash \mathbf{Q})$ ), where rationality of $\sqrt{2}$ (i.e., $\sqrt{2}=\frac{r}{s}$ for integers $r$ and $s \neq 0$ that do not have an integer factor $>1$ in common, i.e., $r$ and $s$ are co-prime) leads, with two applications of the fact that "if a square is even it is the square of an even number", to the conclusion that both $r$ and $s$ are even and thus a contradiction with the assumption that $r$ and $s$ are co-prime;
- (skipped in class) the constructive existence proof of two consecutive integers one of which is a cube and the other one is a square. This is easily shown to be the case by providing the example $8=2^{3}$ and $9=3^{2}$;
- (not from the book) another constructive existence proof (partially via intimidation) that there exist primes that consist of only ones, namely the numbers $\frac{10^{k}-1}{9}$ for $k=2,19,23,317,1031,49081,86453,109297,270343-$ where it is conjectured that there are infinitely many integers $k$ for which $\frac{10^{k}-1}{9}$ is prime, even though only nine are known ${ }^{1}$;
- the nonconstructive existence proof that integers $x$ and $y$ exists such that $x$ and $y$ are irrational but $x^{y}$ is rational, where it was shown that if $x=y=$ $\sqrt{2}$ does not work as example then $x=\sqrt{2}^{\sqrt{2}}$ and $y=\sqrt{2}$ is an example ${ }^{2}$.
- a very common nonconstructive existence proof, is the pigeonhole principle: if more than $N$ items are distributed in any manner over $N$ bins, there must be a bin containing at least two items (which can simply be proved using contradiction: if each bin contains at most a single item, then the total number of items is at most $N$, which contradicts the hypothesis that there are more than $N$ items), but we have no clue which bin contains two or more items.

With 383 students in this class and $366<383$, you should be able to prove that there are at least two students in our class that have the same birthday. A much more interesting result is that with overwhelming probability it is the case that among these only 383 students there are two that have the same birthday on Jupiter, despite the fact that 383 is much smaller than the number 10563 of days in a Jupiter year. We will see later in this course why that is the case.
- an example of the pigeonhole principle where we proved that in any group of $n>1$ people there are at least two persons that have the same number of friends among that group ${ }^{3}$. It looks impossible to apply the pigeonhole principle, because anyone can have from zero up to $n-1$ friends, so there are $n$ bins (bin identified with number of friends) for $n$ people - but this can be fixed by the single smart observation that if there is someone with $n-1$ friends, there cannot be someone without friends (due to the symmetry of friendship): in this case there are only $n-1$ bins for $n$ people and two people must land in the same bin, i.e., have the same number of friends. And if there is no one with $n-1$ friends, that bin is empty, so there will be a "number of friends collision" in the remaining $n-1$ bins
- with ten people seated around a table, each eating a (non-zero) number of BKBs distinct from the number of BKBs eaten by anyone else on the table, there are 3 adjacent eaters whose combined number of BKBs is at least 17:
- We use a proof by contradiction and thus assume that the combined number of BKBs eaten by any triple consisting of 3 adjacent eaters is at most 16 .
- For $i=1,2, \ldots, 10$ let $a_{i}$ be the number of BKBs eaten by eater $i$, then the $a_{i}$ are distinct positive integers (no partially eaten BKBs),[^0]$\min _{1 \leq i \leq 10}\left\{a_{i}\right\} \geq 1$, and thus the total number $T$ of BKBs eaten satisfies $T=\sum_{i=1}^{10} a_{i} \geq \sum_{i=1}^{10} i=55$ (found as 10 (number of terms) times the sum of 1 (first term) and 10 (last term) divided by 2: this rule holds for any arithmetic sequence, as we will see next time).
- There are ten distinct (but overlapping) triples of 3 adjacent eaters: $\left(a_{1}, a_{2}, a_{3}\right),\left(a_{2}, a_{3}, a_{4}\right),\left(a_{3}, a_{4}, a_{5}\right),\left(a_{4}, a_{5}, a_{6}\right),\left(a_{5}, a_{6}, a_{7}\right),\left(a_{6}, a_{7}, a_{8}\right)$, $\left(a_{7}, a_{8}, a_{9}\right),\left(a_{8}, a_{9}, a_{10}\right),\left(a_{9}, a_{10}, a_{1}\right),\left(a_{10}, a_{1}, a_{2}\right)$
- From our assumption that the combined number of BKBs eaten by any triple consisting of 3 adjacent eaters is at most 16 it follows that $s_{1}=a_{1}+a_{2}+a_{3} \leq 16, s_{2}=a_{2}+a_{3}+a_{4} \leq 16, \ldots, s_{10}=a_{10}+a_{1}+a_{2} \leq$ 16.
- From $s_{j} \leq 16$ for $1 \leq j \leq 10$ it follows that $\sum_{j=1}^{10} s_{j} \leq \sum_{j=1}^{10} 16=160$.
- On the other hand $\sum_{j=1}^{10} s_{j}=3 T$ (this follows from the fact that each $a_{i}$ occurs in precisely three distinct triples) so that with $T \geq 55$ it follows that $\sum_{j=1}^{10} s_{j} \geq 3 * 55=165$. This is a contradiction with the earlier $\sum_{j=1}^{10} s_{j} \leq 160$.
- From this contradition it follows that the assumption that the combined number of BKBs eaten by any triple consisting of 3 adjacent eaters is at most 16 is wrong.

The 17 can easily be improved to 18 :

- If we try the previous proof assuming that the combined number of BKBs eaten by any triple consisting of 3 adjacent eaters is at most 17 we get " $\sum_{j=1}^{10} s_{j} \leq 170$ and $\sum_{j=1}^{10} s_{j} \geq 165$ ", which is not a contradiction, so that fails. But we still use a proof by contradiction and thus still assume that the combined number of BKBs eaten by any triple consisting of 3 adjacent eaters is at most 17 .
- Without loss of generality (and using the same notation as above), let $a_{1}$ be the smallest value among the $a_{i}$. It follows that $a_{i} \geq 2$ for $2 \leq i \leq 10$. Given that they are all distinct, it follows that $T^{\prime}=$ $\sum_{i=2}^{10} a_{i} \geq \sum_{i=2}^{10} i=54$ (found by subtracting 1 from the above 55 or as 9 (number of terms) times the sum of 2 (first term) and 10 (last term) divided by 2 ).
- Look at the three non-overlapping triples $\left(a_{2}, a_{3}, a_{4}\right),\left(a_{5}, a_{6}, a_{7}\right)$, and $\left(a_{8}, a_{9}, a_{10}\right)$ with $s_{2}=a_{2}+a_{3}+a_{4}, s_{5}=a_{5}+a_{6}+a_{7}$, and $s_{8}=$ $a_{8}+a_{9}+a_{10}$, then it follows from our assumption that the combined number of BKBs eaten by any triple consisting of 3 adjacent eaters is at most 17 that $s_{2} \leq 17, s_{5} \leq 17$, and $s_{8} \leq 17$, and thus that $s_{2}+s_{5}+s_{8} \leq 3 * 17=51$.
- On the other hand $s_{2}+s_{5}+s_{8}=T^{\prime} \geq 54$. This is a contradiction with the earlier $s_{2}+s_{5}+s_{8} \leq 3 * 17=51$.
- From this contradition it follows that the assumption that the combined number of BKBs eaten by any triple consisting of 3 adjacent eaters is at most 17 is wrong.

Next class. We will briefly discuss sets and then move to sequences, summations, cardinalities and countability. It is useful to read Chapter 2 (omitting both the Schröder-Bernstein theorem and the continuum hypothesis in section 2.5). Note that we will not be discussing set operations, functions, or matrices, all of which you are supposed to be familiar with.


[^0]:    ${ }^{1}$ For the next lecture it is useful to have a close look at this expression $\frac{10^{k}-1}{9}$ (a simple closed form function of $k$ ) and what it expresses (" $k$ ones in decimal", i.e., the sum of the first $k$ powers of 10$)$.

    ${ }^{2}$ Some find it annoying that, though the argument proves that such $x$ and $y$ indeed exist, at the end of the proof one still does not have irrational $x$ and $y$ for which $x^{y}$ is rational. To fix that, a constructive existence proof of the same fact is given by $x=\sqrt{2}$ and $y=\log _{2}(9)$ - make sure you can give the direct proof of the fact that this $y$ is irrational, and that you can figure out why $\sqrt{2}^{\log _{2}(9)}$ is rational. After the lecture someone suggested to simply take $x=e$ and $y=i \pi$ because $e^{i \pi}=-1$; a great example (of an even much crazier fact), except that we have not seen a proof that $x$ is irrational (it is), and that $y$ is not even real (but indeed in $i \mathbf{R}-i \mathbf{Q}$ ).

    ${ }^{3}$ Here friendship is supposed to be symmetric (if Daisy is Oswaldo's friend, then Oswaldo is Daisy's friend) and non-reflexive (no one is his or her own friend, not even Marsellus).

