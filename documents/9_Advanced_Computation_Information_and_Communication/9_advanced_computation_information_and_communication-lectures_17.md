Continuing with counting : Given that we want to select $r$ items from a set of $n$ items: this can be done with replacement (items can be selected more than once: characters in passwords) or without replacement (each item may be selected at most once: cards in a hand of poker; thus "without replacement" is always with $r \leq n$ ); and, independently, in such a way that the order is relevant ("permutation": characters in a password) or such that the order is irrelevant ("combination": cards in a hand of poker - the latter is independent of an order that an $r$-selection inherits from an order that may be implicit in the $n$ items). This leads to two times two equals four possible ways to select $r$ items from $n$ items. We derived the formulas for three of them (see November 9 lecture notes): $n^{r}$ permutations with replacement, $\frac{n!}{(n-r)!}$ permutations without replacement, and $\binom{n}{r}$ combinations without replacement. The "hardest" one, combinations with replacement, is discussed below. But even the "easier" ones already lead to interesting counting problems, of which we did two examples in class, counting the number of different five-card hands of poker that contain four of a kind, and the number of hands that contain a full house (three of a kind and two of a kind):

Four of a kind: There are 13 ways to select the kind, which determines 4 of the 5 cards, after which there are 48 choices for the fifth card; thus $13 \cdot 48=624$ of 2598960 (i.e., $\binom{52}{5}$, the total number of five-card hands of poker), which corresponds to $0.024 \%$.

Alternatively, first take the card that is not part of the four of a kind card ( 52 choices), after which any kind different from the first card selected ( 12 choices) determines the four of a kind: $52 \cdot 12=624$.

Full house: There are 13 choices for the kind of the triple and $\binom{4}{3}=4$ choices for its 3 suits (or, equivalently, $\binom{4}{1}$ choices for the alternative suit, i.e., the single suit not present among the three of a kind), after which there are 12 choices for the kind of the pair and $\binom{4}{2}=6$ choices for its 2 suits: thus $13 \cdot 4 \cdot 12 \cdot 6=3744$ of 2598960 , i.e., $0.144 \%$.

Alternatively, determine the three of a kind by selecting a card ( 52 choices) and taking the three cards of the same kind but of the three complementary suits as the three of a kind, after which a card (say card $A$ ) of the remaining 48 cards is selected, with three choices for a second card (say card $B$ ) of the same kind as $A$ (but a suit different from $A$ 's suit),
but divided by two because selecting $A$ and then $B$ is equivalent to first selecting $B$ and then $A: 52 \cdot \frac{48 \cdot 3}{2}=52 \cdot 72=3744$.

Note that multiple arguments for both counts are given; not so urgent for these relatively simple examples, but finding more arguments supporting the same solution is helpful if there is no other way to verify the correctness of a solution.

Order irrelevant (combination), with replacement (allowing repetition). This is the most complicated of the four " $r$ from $n$ " counting possibilities, and the one most people have trouble remembering. Note that there is no reason to require that $r \leq n$ : because the selection of any item may be repeated, the item may be selected any number of times (depending on $r$ ). We only assume that $r \geq 0$. In the explanation below the order of the selection is irrelevant:

$r=1$ : If $r=1$, there are $n=\binom{n}{1}$ ways to select a single item from a set of $n$ items.

$r=2$ : If $r=2$, there are $n$ ways to select a single item twice, and there are

$\binom{n}{2}$ ways to choose two distinct items once each and such that the order is irrelevant. Thus the total number of ways to select two items from $n$, order irrelevant, with replacement, is

$$
n+\binom{n}{2}=\frac{n(n+1)}{2}=\binom{n+1}{2}
$$

$r=3$ : If $r=3$, there are $n$ ways to select a single item three times, there are $\binom{n}{2}$ ways to choose two distinct items once, and thus $2\binom{n}{2}$ to double the choice of either the first or the second (in order to select three items in total; this can easily be counted in a different manner: there are $n$ choices for the item selected twice and $n-1$ choices remaining for another item which is selected just once, thus $n(n-1)$; the result, fortunately, equals $2\binom{n}{2}$ as found using the other counting method), and there are $\binom{n}{3}$ ways to choose three distinct items once each and such that the order is irrelevant. Thus the total number of ways to select three items from $n$, order irrelevant, with replacement, is

$$
n+2\binom{n}{2}+\binom{n}{3}=\frac{n(n+1)(n+2)}{6}=\binom{n+2}{3}
$$

General $r$ : The sequence $n=\binom{n}{1}$ for $r=1$, followed by $\binom{n+1}{2}$ for $r=2$ and $\binom{n+2}{3}$ for $r=3$ suggests that the count that we are looking for is

$\binom{n+r-1}{r}=C(n+r-1, r)=C(n+r-1, n-1)=\binom{n+r-1}{n-1}$.

This is indeed correct. This can be seen by establishing a bijection between the set of bitstrings of length $n+r-1$ with $n-1$ ones (and thus $r$ zeros) and the set of $n$-tuples $\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ of non-negative integers such that $\sum_{i=1}^{n} x_{i}=r:$

- Given a bitstring of length $n+r-1$ with $n-1$ ones and $r$ zeros, construct an $n$-tuple $\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ of non-negative integers such that $\sum_{i=1}^{n} x_{i}=r$ as follows. Initially let $x_{i}=0$ for $1 \leq i \leq n$, and let $\ell=1$. Processing the bits in the length $n+r-1$ bitstring from left to right increase $x_{\ell}$ by one if the bit is zero but increase $\ell$ by one if the bit is one (in class we may have done this the other way around with respect to the zeros and the ones, but that is immaterial). After doing this for all $n+r-1$ bits, it will be the case that $\sum_{i=1}^{n} x_{i}=r$ (because there are $r$ zero bits) and $\ell$ will be $n$ (because there are $n-1$ one bits). Note
that a different bitstring leads to a different $n$-tuple $\left(x_{1}, x_{2}, \ldots, x_{n}\right)$, so the mapping is injective.
- Conversely, given an $n$-tuple $\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ of non-negative integers with $\sum_{i=1}^{n} x_{i}=r$, construct a bitstring of length $n+r-1$ with $n-$ 1 ones and $r$ zeros as follows. Start with an empty bitstring. For $i=1,2, \ldots, n$ in succession first append $x_{i}$ zero bits to the bitstring and next, if $i<n$ append a single one bit to the bitstring. After doing this for all $i$, a total of $r$ zero bits have been appended (because $\sum_{i=1}^{n} x_{i}=r$ ) and a total of $n-1$ one bits have been appended (namely for each $i$ with $1 \leq i<n$ ), so the resulting bitstring has length $n+r-1$ and contains the prescribed numbers of zero and one bits. Note that a different $n$-tuple leads to a different bitstring, so the mapping is injective.
- The existence of these two injective mappings (which are easily seen to be each other's inverse) proves that the number of $n$-tuples as above equals the number of length $n+r-1$ bitstrings with $n-1$ ones and thus $r$ zeros (and that the injections are actually bijections). Because the number of such bitstrings is $\binom{n+r-1}{r}$, the result follows.

Examples of this least common (and hardest to remember) " $r$ from $n$ " counting method are also a bit less "natural":

- The most common one is "taking cookies from a jar": given $n$ types of cookies in a jar (that has an infinite and equal supply of all $n$ types of cookies), selecting $r$ cookies from the jar corresponds to drawing an $r$-combination out of $n$, with repetition. - At graduation of a class of $n$ students there are $r$ prizes to be divided among the $n$ students for "best performance" according to $r$ distinct criteria (for "highest average grade", for "best performance in math", for "most effectively sucking up to the teachers", for "best behavior", etc.). There are always those few top-performing students who take (almost) all the prizes, and indeed one student may receive all prizes. In how many ways can the $r$ prizes be divided among the $n$ students (where we do not distinguish between the types of prizes, but are only interested in the number of prizes per student)? Using the above notation in this context, the variable $x_{i}$ would refer to the number of prizes received by the $i$-th student, with $r$ the total number of prizes and $n$ the number of students.
- Generalizing this a bit: in how many ways can $n$ non-negative integers $x_{1}, x_{2}$, $\ldots, x_{n}$ be selected such that $\sum_{i=1}^{n} x_{i}=r$ (note that this is precisely what was used in the above proof)?
- Generalizing the previous bullet: what if, under the same non-negativety and integrality conditions (on the $x_{i}$ ) the targeted sum value is not strict but just an upperbound such as $\sum_{i=1}^{n} x_{i} \leq r$ or $\sum_{i=1}^{n} x_{i}<r$ ? And how to deal with lower bounds $\ell_{i}$, i.e., $x_{i} \geq \ell_{i}$ for $1 \leq i \leq n$ ? This question was partially answered in class (where the concept of a "slack variable" was used to transform the counting problem for $\sum_{i=1}^{n} x_{i} \leq r$ into the equivalent counting problem for $\sum_{i=1}^{n+1} x_{i}=r$, with the usual non-negative integrality condition on the slack variable $x_{n+1}$ ); the other generalizations will be discussed during the exercise sessions.

Summary of the four ways of selecting $r$ items from a set of cardinality $n$.

- If the order is relevant ("permutation") and replacement is allowed, the number of possible ways to select $r$ items from $n$ equals $n^{r}$.

Example with $n=5, r=2: n^{r}=5^{2}=25$; assuming the five items are the five digits " 1 ", " 2 ", " 3 ", " 4 ", and " 5 " the 25 possibilities are:

$$
11,12,13,14,15
$$

$$
21,22,23,24,25
$$

$$
\begin{aligned}
& 31,32,33,34,35 \\
& 41,42,43,44,45 \\
& 51,52,53,54,55
\end{aligned}
$$

- If the order is relevant ("permutation") and replacement is not allowed, the number of possible ways to select $r$ items from $n$ equals $\frac{n!}{(n-r)!}$.

Example with $n=5, r=2: \frac{n!}{(n-r)!}=\frac{5!}{3!}=20$; assuming the five items are the five digits " 1 ", " $2 ", " 3 ", " 4$ ", and " 5 " the 20 possibilities are:

$12,13,14,15$

$21,23,24,25$

$31,32,34,35$

$41,42,43,45$

$51,52,53,54$

- If the order is irrelevant ("combination") and replacement is not allowed, the number of possible ways to select $r$ items from $n$ equals $\binom{n}{r}$.

Example with $n=5, r=2:\binom{n}{r}=\binom{5}{2}=\frac{5!}{2!3!}=10$; assuming the five items are the five digits " 1 ", " $2 ", " 3$ ", " 4 ", and " 5 " the 10 possibilities are:

$$
12,13,14,15
$$

$23,24,25$

34,35

45

- If the order is irrelevant ("combination") and replacement is allowed, the number of possible ways to select $r$ items from $n$ equals $\binom{n+r-1}{r}$.

Example with $n=5, r=2:\binom{n+r-1}{r}=\binom{6}{2}=\frac{6!}{2!4!}=15$; assuming the five items are the five digits " $1 "$ ", " 2 ", " 3 ", " " 4 ", and " 5 " the 15 possibilities are:

$$
11,12,13,14,15
$$

$22,23,24,25$

$33,34,35$

44,45

Useful identities. The binomial coefficient $t^{1}$ " $n$ choose $r$ " $\binom{n}{r}$ is defined as $\binom{n}{r}=$ $\frac{n!}{(n-r)!r!}$ for integers $1 \leq r \leq n$. As we have seen it can be interpreted as the number of different $r$-subsets from an $n$-set (i.e., the number of distincts subsets of cardinality $r$ of a set of cardinality $n$ ). Binomial coefficients give rise to a large number of identities, many of which allow not just a formal proof (using algebraic manipulations, possibly involving induction) but also an insight why they should be true. This "insight" is commonly referred to as a combinatorial argument or a combinatorial proof (or "proof by intimidation").

- A useful result that we have seen already is Pascal's identity

$$
\binom{n}{r}=\binom{n-1}{r-1}+\binom{n-1}{r}
$$

for integers $1 \leq r \leq n$, where we follow the convention to define the not-yet-defined case $\binom{n-1}{n}$ as zero (reasonably so, because it is impossible to select $n$ distinct items from a set containing just $n-1$ elements). Pascal's identity is proved combinatorially by arguing that a particular item of the $n$-set is either contained or not contained in the $r$-combination. If the item is contained in the $r$-combination, it still remains to select $r-1$ other items from the remaining $n-1$ items in the set, which can be done in $\binom{n-1}{r-1}$ ways. If the item is not contained in the $r$-combination, the latter must consist of $r$ items chosen from the other $n-1$ items in the $n$-set, which can be done in $\binom{n-1}{r}$ ways. Because the two possibilities are disjoint, Pascal's identity follows (from the sum rule).

In the previous lecture notes the mathematical proof for the case $r<n$ was given. It uses the definition $\binom{n}{r}=\frac{n!}{(n-r)!r!}$ multiple times and is repeated below:

$$
\begin{aligned}
\binom{n-1}{r-1}+\binom{n-1}{r} & =\frac{(n-1)!}{(n-r)!(r-1)!}+\frac{(n-1)!}{(n-1-r)!r!} \\
& =\frac{(n-1)!r}{(n-r)!r!}+\frac{(n-1)!(n-r)}{(n-r)!r!} \\
& =\frac{(n-1)!(r+n-r)}{(n-r)!r!} \\
& =\frac{n!}{(n-r)!r!}=\binom{n}{r}
\end{aligned}
$$

To cover the case $r=n$, observe that $\binom{n-1}{n}=0$ (cf. earlier remark) and that $\binom{n}{n}=\binom{n-1}{n-1}=1$.

Pascal's identity immediately leads to Pascal's triangle (on the next page), which in turn gives rise to interesting new interpretations of $\binom{n}{r}$ and which makes it easier, to some at least, to "see" why certain identities involving binomial coefficients hold. Examples can be found below.

The red entries in Pascal's triangle suggest that for integers $n$ and $r$ with $r \leq n$ it is the case that

$$
\begin{equation*}
\binom{n+1}{r+1}=\sum_{i=r}^{n}\binom{i}{r} \tag{1}
\end{equation*}
$$

(where $n=6$ and $r=3$ in Figure 1). This identity follows from the (somewhat contrived) combinatorial argument that the right-most " 1 " of $r+1$ one-bits in a sequence of $n+1$ bits (which can be selected in $\binom{n+1}{r+1}$ ways) must be either at[^0]

Figure 1. (A non-triangular part of) Pascal's triangle, where the red and blue entries illustrate equations (1) above and (2) below.

the $(n+1)$-st location (with $\binom{n}{r}$ possibilities to select the other $r$ one-bits: the term for $i=n$ in the summation), or at the $n$-th location (with $\binom{n-1}{r}$ possibilities to select the other $r$ one-bits: the term for $i=n-1$ in the summation), or at the $(n-1)$-st location (with $\binom{n-2}{r}$ possibilities to select the other $r$ one-bits: the term for $i=n-2$ in the summation), $\ldots$, or at the ( $r+1$ )-st location (with $\binom{r}{r}$ possibilities to select the other $r$ one-bits: the term for $i=r$ in the summation).

Using the same (but mirrored) Pascal triangle argument (and $n \geq r$ ) one finds that

$$
\begin{equation*}
\binom{n+1}{r}=\sum_{i=0}^{r}\binom{n-i}{r-i} \tag{2}
\end{equation*}
$$

(cf. the blue entries in Figure 1, where $n=8$ and $r=4$ ). The (again a bit contrived) combinatorial argument goes as follows: selecting $r$ one-bits among $n+1$ locations can be done in $\binom{n+1}{r}$ ways; or it can be done by starting with $r$ one-bits followed by a zero-bit followed by selecting zero one-bits among the remaining $n+1-r-1=n-r$ locations in $\binom{n-r}{0}$ ways (the term corresponding to $i=r$ in the summation), or by starting with $r-1$ one-bits followed by a zero-bit followed by selecting one one-bit among the remaining $n+1-r+1-1=n-r+1$ locations in $\binom{n-r+1}{1}$ ways (the term corresponding to $i=r-1$ in the summation), or by starting with $r-2$ onebits followed by a zero-bit followed by selecting two one-bits among the remaining $n+1-r+2-1=n-r+2$ locations in $\binom{n-r+2}{2}$ ways (the term corresponding to $i=r-2$ in the summation), $\ldots$, or by starting with $r-r$ one-bits followed by a zero-bit, followed by selecting $r$ one-bits among the remaining $n+1-r+r-1=n$ locations in $\binom{n}{r}$ ways (the term corresponding to $i=0$ in the summation).

With $n-i=n-r+j$ and thus $r-i=j$ (so reverse the order of the summation) Equation (2) becomes

$$
\binom{n+1}{r}=\sum_{j=0}^{r}\binom{n-r+j}{j}
$$

and thus (with $n-r=m$ )

$$
\begin{equation*}
\binom{m+r+1}{r}=\sum_{j=0}^{r}\binom{m+j}{j} \tag{3}
\end{equation*}
$$

as in exercise 6.4.19. The combinatorial argument is virtually identical to the one directly above: given $m+r+1$ bit-locations, $r$ one-bits can be chosen directly in $\binom{m+r+1}{r}$ ways, or by putting, for $j=0,1, \ldots, r$, a sequence of a single zero-bit followed by $r-j$ one-bits at the right end, leaving $m+r+1-1-(r-j)=m+j$ locations for the remaining $j$ one-bits (for $\binom{m+j}{j}$ choices).

Equation (3) with $m=n-1$ becomes

$$
\binom{n+r-1}{r}=\sum_{j=0}^{r}\binom{n+j-2}{j}
$$

which allows an "order irrelevant, with replacement" interpretation: selecting an $r$ combination with replacement from $n$ items can be done (as seen earlier) in $\binom{n+r-1}{r}$ ways, but it can also be done by specifically looking at the number of occurrences of, say, the first of the $n$ items: if it does not occur, $r$ items still have to be selected from the other $n-1$ items (in $\binom{n-1+r-1}{r}=\binom{n+r-2}{r}$ ways, the last term in the summation), or it occurs once, so $r-1$ items still have to be selected from the other $n-1$ items (in $\binom{n-1+r-1-1}{r-1}=\binom{n+r-1-2}{r-1}$ ways, the second last term in the summation), or it occurs twice, so $r-2$ items still have to be selected from the other $n-1$ items (in $\binom{n-1+r-2-1}{r-2}=\binom{n+r-2-2}{r-2}$ ways, the third last term in the summation), $\ldots$, or it occurs $r-1$ times, so 1 item still has to be selected from the other $n-1$ items (in $\binom{n-1+1-1}{1}=\binom{n+1-2}{1}$ ways, the second term in the summation), or it occurs $r$ times, so no item still has to be selected from the other $n-1$ items (in $\binom{n-1+0-1}{0}=\binom{n-2}{0}$ ways, the first term in the summation). Because there are no other ways to select the first item, the correctness of the summation follows.

Equations (1) and (2) can of course also be proved using induction (cf. exercises).

## More combinatorial and analytic proofs.

- Last time we saw that $r\binom{n}{r}=n\binom{n-1}{r-1}$ for integers $r, n$ with $1 \leq r \leq n$ : given a group of $n$ people, a committee of $r$ including a chair of the committee can be chosen by first selecting the committee of $r$ (in $\binom{n}{r}$ ways) and by then selecting the chair as one of the committee members ( $r$ ways to do so), or by first selecting the committee-chair from the group of $n$ (there are $n$ ways to do so) after which the other $r-1$ committee members still need to be selected from the remaining group of $n-1$ (there are $\binom{n-1}{r-1}$ ways to do so). Because both approaches should give rise to the same overall number of possibilities we must have that $r\binom{n}{r}=n\binom{n-1}{r-1}$. This was indeed shown to be true using a simple analysis.
- An identical argument leads to $\binom{r}{k}\binom{n}{r}=\binom{n}{k}\binom{n-k}{r-k}$ for integers $k, n, r$ with $1 \leq$ $k \leq r \leq n$ : given a group of $n$ people, a committee of $r$ including a subcommittee of $k$ from the committee can be chosen by first selecting the committee of $r$ (in $\binom{n}{r}$ ways) and then selecting the subcommittee of $k$ from the committee of $r$ just selected $\left(\binom{r}{k}\right.$ ways to do so), or by first selecting the subcommittee of $k$ from the group of $n$ (there are $\binom{n}{k}$ ways to do so) after which the other $r-k$ committee
members still need to be selected from the remaining group of $n-k$ (there are $\binom{n-k}{r-k}$ ways to do so). Algebraically:

$$
\begin{aligned}
\binom{r}{k}\binom{n}{r} & =\frac{r!}{k!(r-k)!} \frac{n!}{r!(n-r)!} \\
& =\frac{n!(n-k)!}{k!(n-k)!(r-k)!((n-k)-(r-k))!} \\
& =\binom{n}{k}\binom{n-k}{r-k}
\end{aligned}
$$

note that the green factors cancel, and that two identical (blue) factors are added. - It won't surprise anyone that $2 n=n+n$. What is more interesting is that it can also be regarded as $\binom{2 n}{1}=\binom{n}{1}+\binom{n}{1}$ and thus as a simpler variant of the observation that $\binom{2 n}{2}=\binom{n}{2}+\binom{n}{2}+\binom{n}{1}^{2}=2\binom{n}{2}+n^{2}$. Further generalizing the same line of thought leads to something that looks less straightforward, namely Vandermonde's identity. Here's how it goes.

Let $A$ and $B$ be disjoint sets with $|A|=|B|=n$ with $n \geq 1$. Selecting a 1combination (repetition or not is irrelevant for a 1-combination) from $A \cup B$ can, obviously, be done in $\binom{2 n}{1}=2 n$ ways (note that $A$ and $B$ were assumed to be disjoint, so $|A \cup B|=2 n$ ), or it can be done by selecting the element either from $A$ (in $\binom{n}{1}=n$ ways) or from $B$ (again in $\binom{n}{1}=n$ ways); thus, unsurprisingly, $2 n=n+n$, which is not in any way an interesting result - except for the two different ways that we used to arrive at the same number, because the argument can be generalized in various ways, ultimately giving rise to an interesting result ${ }^{2}$.

With $A$ and $B$ as above (thus disjoint and of cardinality $n$ ) and assuming that $n \geq 2$, if a 2-combination from $A \cup B$ is selected without replacement (which can be done in $\binom{2 n}{2}$ ways: $\left.|A \cup B|=2 n\right)$, then either the two elements belong to $A$ (thus $\binom{n}{2}$ ways to select them), or to $B$ (again $\binom{n}{2}$ ways), or one element comes from $A$ and the other from $B$ (due to the product rule there are $n^{2}$ ways to do this): overall we get that $\binom{2 n}{2}=2\binom{n}{2}+n^{2}$. Algebraically:

$$
\binom{2 n}{2}=\frac{2 n(2 n-1)}{2}=n(2 n-1)=n(n-1)+n^{2}=2 \frac{n(n-1)}{2}+n^{2}=2\binom{n}{2}+n^{2}
$$

At this point we got stuck, because doubts arose why the term $n^{2}$ is correct and why it should not be $n^{2} / 2$ (or such because $n^{2} / 2$ cannot be correct to begin with for odd $n$ ). This question (why $n^{2}$ is correct and "dividing it by 2 in some way or another" is not) is left for you to ponder about (hint: the solution was mentioned during the lecture), because it is typical for counting problems that in the middle of an argument one forgets what is going on and why a proposed solution is "obvious" whereas another "obvious" solution is wrong.

This line of reasoning will be continued next time.

Next class. Reread sections 6.3 and 6.4 ; reading section 7.1 and 7.2 may turn out to be useful.[^1]


[^0]:    ${ }^{1}$ called this way for the reason explained during the next lecture.

[^1]:    ${ }^{2}$ The generalization of this result to $n=0$ is not $1=1+1$ but $1=1+1-1$; why?

