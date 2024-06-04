## Counting

In counting problems one wants to know in how many ways some number of objects can be selected in such a way that the resulting collection of objects satisfies a certain condition. Often there is no clear way to check if a proposed solution is correct, which makes counting challenging. If you are not sure about your approach, try to come up with a different argument that should lead to the same result. It often helps to try small examples, and to generalize your findings to larger cases; practice helps a lot, so refer to the exercises in the book.

A commuter's problem. We began the lecture by considering the example of counting the number of shortest walks between two points in a perfectly rectangular grid. More specifically, we wanted to figure out if a commuter's lifetime would suffice to make all possible shortest walks in Manhattan from the intersection of 8th Avenue and 41st street to the intersection of 3rd Avenue and 53rd street ${ }^{1}$. For this example we concluded that we have to walk $53-41=12$ blocks along avenues (to go from street to street) and that we have to walk $8+2-3=7$ (much longer!) blocks along streets (to go from avenue to avenue), where the " +2 " is due to the fact that there is not just a single but three avenues between 3rd and 5th avenue (namely Lexington ( $3 \frac{1}{2}$ th), Park (4th), and Madison ( $4 \frac{1}{2}$ th)). Thus, a total of $12+7=19$ blocks, of which 7 in roughly easterly direction (29 degrees to the south) along a street, and (thus, complementary) 12 in roughly northerly direction (29 degrees to the east) along an avenue; we introduced $\tilde{P}(19,7)$ to denote the total possible number of shortest walks 2 .[^0]

Looking at simpler problems we concluded that from our starting point on 8th Avenue and 41st street, there is just one way to reach any destination on 8th Avenue (just follow 8th Avenue) or any destination on 41st street (just follow 41 street), as making any left or right turn would make the walk longer than necessary (and therefore not shortest possible). Thus $\tilde{P}(n, 0)=\tilde{P}(n, n)=1$ for any integer $n \geq 0$. We also concluded that our destination on 3rd Avenue and 53rd street can only be reached via a shortest path either by going via the intersection of 3rd Avenue and $52 \mathrm{rd}$ street or via the intersection of Lexington Avenue and 53rd street. It follows from this simple observation that $\tilde{P}(19,7)=\tilde{P}(18,7)+\tilde{P}(18,6)$. Along with the boundary conditions $(\tilde{P}(n, 0)=\tilde{P}(n, n)=1$ for any integer $n \geq 0)$ this makes it possible to compute $\tilde{P}(n, r)$ for any integer $n \geq 0$ and integer $r$ with $0 \leq r \leq n-$ such as our case $\tilde{P}(19,7)$ - for instance using an easy to write recursive program: either a boundary condition applies or $\tilde{P}(n, r)=\tilde{P}(n-1, r)+\tilde{P}(n-1, r-1)^{3}$.

This "solution", however, does not give us a nice "closed formula" for $\tilde{P}(n, r)$. To find such a formula we used common sense counting (i.e., basic counting rules, cf. below) to count in how many ways we can select $r$ of our $n$ blocks as "street blocks" (and thus the remaining ones as "avenue blocks") - or vice versa. We have to select $r$ blocks out of $n$, so after selecting a first block (in $n$ possible ways), a second block can only be selected among the $n-1$ remaining blocks (thus in $n-1$ ways), the third among the then remaining $n-2$ blocks (in $n-2$ ways), etc., until the $r$ th block among the final remaining $n-r+1$ blocks in $n-r+1$ ways. This leads to a total of $n(n-1)(n-2) \ldots(n-r+1)=\frac{n!}{(n-r)!}$ possible ways to select $r$ blocks. But then we observed that, for instance, first selecting the fifth block and later the ninth block is equivalent to first selecting the ninth block and later the fifth block, and concluded that the order in which the blocks are selected is irrelevant. Because each distinct selection (i.e., distinct set of blocks selected) occurs $r$ ! times in our overall count (namely, the number of ways $r$ items can be ordered), our count $\frac{n!}{(n-r)!}$ must be divided by $r!$. This leads to the result $\tilde{P}(n, r)=\frac{n!}{r!(n-r)!}$ which is commonly denoted as $\tilde{P}(n, r)=\binom{n}{r}$ (pronounced as " $n$ choose $r$ ").

It is easily verified that the formula $\binom{n}{r}$ satisfies the above boundary conditions and that the newly found closed formula satisfies the recursive relation $\tilde{P}(n, r)=$ $\tilde{P}(n-1, r)+\tilde{P}(n-1, r-1):$

$$
\begin{aligned}
\binom{n-1}{r-1}+\binom{n-1}{r} & =\frac{(n-1)!}{(n-r)!(r-1)!}+\frac{(n-1)!}{(n-1-r)!r!} \\
& =\frac{(n-1)!r}{(n-r)!r!}+\frac{(n-1)!(n-r)}{(n-r)!r!} \\
& =\frac{(n-1)!(r+n-r)}{(n-r)!r!} \\
& =\frac{n!}{(n-r)!r!} \\
& =\binom{n}{r}
\end{aligned}
$$

Using the boundary conditions as the basis step, interpreting the above derivation as the induction step, and putting all arguments in the right order, this can be turned into an induction proof of the fact that indeed $\tilde{P}(n, r)=\binom{n}{r}$ - and that[^1]indeed $\binom{n}{r}$ is an integer, other than via the hand-waving argument that " $\frac{n!}{(n-r)!}$ must be divided by $r$ !" (and is indeed divisible by $r$ !).

To make a long story short, $\tilde{P}(19,7)$, the number of shortest walks from 8 th and 41st to 3rd and 53rd, equals $\frac{19!}{7!12!}=50388$. With 260 as an estimate for the number of working days, it would take more than 190 years to walk all possible shortest walks. Also, with $\tilde{P}(18,3)=816$ and $\tilde{P}(7,3)=35$, there are $816 \cdot 35=28560$ longer walks that pass through the tasteful lobby of the building at the intersection of 5th and 56th before reaching one's destination; still more than a century of commuting. Always making a stop at the shop in the middle of the 46th-47th street block on 5th Avenue, implies there are $\tilde{P}(8,3) \tilde{P}(10,4)=56 \cdot 210=11760$ optimal walks (we still walk 19 blocks, but for one block we do not have a choice, so " $8+10$ "): good for more than 45 years of commuting, but unfortunately incompatible with the shop's fate (http://nymag.com/nymetro/news/people/columns/intelligencer/10497/). Finally, the nearest town where you can try these types of walks for yourself is La Chaux-de-Fonds; the naming of the streets there is, however, not computationallycompatible.

Counting examples. Below more (and simpler) examples of the very basic counting methods: the product rule, the sum rule, and the principle of inclusion-exclusion (which are also extensively described in the book).

Password selection. For the examples, assume that passwords may contain any number of lower case alphabetic characters (a through z), upper case alphabetic characters (A through Z), decimal digits (0 through 9), and special characters!, @, $\#, \$, \%,+, \&, *$ (no accents of any sort).

- Because the four classes of characters ("lower case", "upper case", "digits", "special") are all distinct, the number of possibilities for each character of the password follows from the sum rule and equals $70=26+26+10+8$.
- It then follows from the product rule that the number of length 12 passwords is $70^{12}$.
- Similarly, the number of length 12 passwords that begins with a digit is $10 \cdot 70^{11}$, and the number of length 12 passwords that begins with a special character is $8 \cdot 70^{11}$.
- Because "digit" and "special character" are mutually exclusive the number of length 12 passwords that begins with a digit or a special character is $10 \cdot 70^{11}+8$. $70^{11}=18 \cdot 70^{11}$ due to the sum rule, and the number of length 12 passwords that begins with a digit and a special character is zero.
- The number of length 12 passwords that begins with a digit and ends with a special character is $10 \cdot 70^{10} \cdot 8=80 \cdot 70^{10}$. But the number of length 12 passwords that begins with a digit or ends with a special character is not $10 \cdot 70^{11}+70^{11} \cdot 8=18 \cdot 70^{11}$ but $18 \cdot 70^{11}-80 \cdot 70^{10}$, due to the principle of inclusion-exclusion: for sets $A$ and $B$ it is the case that $|A \cup B|=|A|+|B|-|A \cap B|$. Note that it immediately follows (as shown in class) that

$$
|A \cup B \cup C|=|A|+|B|+|C|-|A \cap B|-|A \cap C|-|B \cap C|+|A \cap B \cap C| \text {. }
$$

- Sometimes it is more cumbersome to "directly" count a number of possibilities with a certain property than it is to count the number of possibilities without that property; if that is the case the number of possibilities with the property follows by simple complementarity.

For instance, directly counting the number of length 12 passwords that contain at least one digit is a bit cumbersome ${ }^{4}$, but easily done by noticing that it is the complement of the set of length 12 passwords that do not contain a digit:

- The number of length 12 passwords not containing a digit is $60^{12}$ (because there are $60=26+26+8$ ways to select a single non-digit).
- Thus the number of length 12 passwords that contain at least one digit equals $70^{12}-60^{12}$.

Selecting $r$ items from a set of $n$ items. Obviously, the order of the characters of a password is relevant, and in general characters may be used more than once in a password. But if we consider the example of selecting a hand of poker from a regular deck of cards $^{5}$ the order of the selection is not relevant, and per hand or combination of hands any card can be chosen at most once. Thus (using the product rule) there are four (two times two) ways to count the number of ways to select $r$ items from a set of $n$ items: the order of selection of items is relevant or irrelevant, and for each of those approaches items may be selected just once or more than once.

If the order is relevant one commonly refers to selecting a permutation; if the order is irrelevant one calls it a combination. If items may be selected more than once the selection is with replacement or allows repetition, otherwise it is without replacement or without repetition. Thus we have to consider the following four possibilities:

(1) Permutation with replacement;

(2) Permutation without replacement;

(3) Combination without replacement;

(4) Combination with replacement.

These four possibilities are further described below in the scenario where $r$ items are selected from a set of $n$ items.

Order relevant (permutation), with replacement (allowing repetition). It follows from the product rule (and as seen above) that with $n$ items to choose from, and doing so $r$ times, there are

$$
n^{r}
$$[^2]ways to select $r$ items from a set of $n$ items if the selection order is relevant and items may be selected more than once. Note that the only requirement on $r$ is that $r \geq 0$.

Examples:

- Passwords of length $r$ using an alphabet consisting of $n$ characters.
- The number of functions from a domain consisting of $r$ elements to a codomain consisting of $n$ elements (because for each element $x$ from the domain there are $n$ possible choices for the image of $x$ ). Thus the number of functions from finite domain $A$ to finite domain $B$ equals $|B|^{|A|}$.

Order relevant (permutation), without replacement (no repetition). With $n$ items to choose from, and doing so $r$ times but in such a way that no item is selected more than once, there are $n$ choices for the first item selected, $n-1$ possible choices left for the second item (the item that was selected first cannot be selected again), $n-2$ possible choices left for the third item (the two items that were selected first and second cannot be selected again), ..., until $n-r+1$ possible choices left for the $r$-th item (the $r-1$ items chosen earlier cannot be selected again). Note that the number of ways to do this is zero if $r>n$, so we assume that $0 \leq r \leq n$. It follows from the product rule that there are

$$
n(n-1)(n-2) \ldots(n-r+1)=\frac{n!}{(n-r)!} \stackrel{\text { definition }}{=} P(n, r)
$$

ways to select $r$ items from a set of $n$ items if the selection order is relevant, items cannot be selected more than once, and it is assumed that $r \leq n$.

Examples (where it is assumed that $0 \leq r \leq n$ ):

- Given a group of $n$ competing athletes, 3 distinct athletes receive the top 3 prizes (a gold medal, a silver medal, and a bronze one): there are $P(n, 3)=n(n-1)(n-2)$ possible outcomes.
- the number of injective functions from a domain consisting of $r$ elements to a codomain consisting of $n$ elements: assuming the domain consists of the elements $x_{1}, x_{2}, \ldots x_{r}$, while choosing a function $f$ by successively selecting the values $f\left(x_{1}\right), f\left(x_{2}\right), \ldots, f\left(x_{r}\right)$ there are $n-i+1$ choices for the value $f\left(x_{i}\right)$ because, due to the injectivity, the values in $\left\{f\left(x_{1}\right), f\left(x_{2}\right), \ldots, f\left(x_{i-1}\right)\right\}$ cannot be used. Thus the number of injective functions from finite domain $A$ to finite domain $B$ equals $|B|(|B|-1)(|B|-2) \ldots(|B|-|A|+1)=\frac{|B|!}{(|B|-|A|)!}$.

Order irrelevant (combination), without replacement (no repetition). This follows from the previous case (and was already argued when finding a closed formula for $\tilde{P}$ as defined earlier) by noticing that if the same set of $r$ items is selected again but in a different order, it counts as a different selection there but as the same selection here. The selection of items does not allow repetition, so that the $r$ items selected are always distinct and consequently there are $r$ ! ways to order the items in any particular selection of $r$ items. It follows that each particular set of $r$ items is counted $r$ ! times in $P(n, r)$. Thus (or, if you like, using the division rule; and again under the condition that $0 \leq r \leq n$ ) a set of cardinality $n$ has

![](https://cdn.mathpix.com/cropped/2024_05_17_d35b823ec0297184b804g-5.jpg?height=135&width=836&top_left_y=2294&top_left_x=610)

distinct $r$-element subsets.

Note that it follows immediately from the definition of $\binom{n}{r}$ that $\binom{n}{r}=\binom{n}{n-r}$ and thus that $C(n, r)=C(n, n-r)$; the combinatorial argument is equally simple: each way of selecting $r$ elements from $n$ can be interpreted as a way to select
$n-r$ elements from $n$ (namely the $n-r$ elements that were not selected); or, the complement of any $r$-element subset of an $n$-element set is an $n-r$-element subset, so their numbers are equal.

Examples (where it is assumed that $0 \leq r \leq n$ ):

- There are $\binom{52}{5}$ different hands of poker. Hands of poker satisfying additional properties will be discussed next time.
- There are $\binom{n}{r}$ different committees consisting of $r$ students representing a class of $n$ students.
- If the above committee appoints one of its $r$ members as its chair, there are a total of $r\binom{n}{r}$ ways to choose an $r$-member committee including a chair, to represent a class of $n$ students. But, one could also first select the chair from the entire class (in $n$ ways), after which the other $r-1$ committee members are selected from the $n-1$ remaining students in $\binom{n-1}{r-1}$ ways, resulting in $n\binom{n-1}{r-1}$ ways to choose an $r$-member committee including a chair, to represent a class of $n$ students. These two different looking results count the same quantity, and therefore it should be the case that $r\binom{n}{r}$ equals $n\binom{n-1}{r-1}$. This is an example of a combinatorial argument that $r\binom{n}{r}=n\binom{n-1}{r-1}$ because the argument shows that the left hand side and the right hand side count the same quantity and are therefore the same. A mathematical proof that $r\binom{n}{r}$ equals $n\binom{n-1}{r-1}$ is easy too:

$$
\begin{aligned}
r\binom{n}{r} & =\frac{n!r}{r!(n-r)!} \\
& =\frac{n!}{(r-1)!((n-1)-(r-1))!} \\
& =\frac{(n-1)!n}{(r-1)!((n-1)-(r-1))!} \\
& =n\binom{n-1}{r-1}
\end{aligned}
$$

Next class. A bewildering variety of formulas and (combinatorial and mathematical) proofs involving "binomial coefficients", i.e., $\binom{n}{r}$, possibly followed by counting different hands of poker and pigeonhole principle examples. To prepare, (re)read sections 6.1 through 6.5 .


[^0]:    ${ }^{1}$ We make the assumption that the relevant part of Manhattan is a perfect grid. This is incorrect, but close enough to reality to make our numbers not totally nonsensical. Note that Broadway does not (or hardly) interfere with our shortest walks because following Broadway would be suboptimal.

    ${ }^{2}$ This somewhat unfortunate notation $\tilde{P}(n, r)$ was used during the lecture, which is why we stick to this notation in these notes; keep in mind, though, that $\tilde{P}(n, r)$ is the same as $C(n, r)$ as introduced below (and in the book)

[^1]:    ${ }^{3}$ If precisely this recursive function is directly used without memoization or other attempt not to be excessively stupid, the number of recursive calls to compute $\tilde{P}(n, r)$ will be $\tilde{P}(n, r)-1$ : really bad

[^2]:    ${ }^{4}$ Once we have had more exposure to various counting results (i.e., the background required to fully understand this footnote will be presented later), it makes sense to try to digest the following argument that does not use complementarity to count the number of length 12 passwords that contain at least one digit. It uses relatively heavy artillery and proceeds as follows: "at least one digit" (in twelve locations) is the same as "precisely one digit, or precisely two digits, or precisely three digits, or ..., or precisely eleven digits, or precisely twelve digits". Given some $k$ with $0<k \leq 12$, the number of passwords with precisely $k$ digits is $\binom{12}{k}$ (for the $k$ digit-locations among twelve locations) times $10^{k}$ (for the $k$ digits at those $k$ digit-locations, with order relevant) times $60^{12-k}$ (for the $12-k$ non-digits at the remaining $12-k$ non-digit-locations, with order relevant) for a total of $\binom{12}{k} 10^{k} 60^{12-k}$ passwords with precisely $k$ digits. Thus the number of passwords with at least one digit is $\sum_{k=1}^{12}\binom{12}{k} 10^{k} 60^{12-k}$. Because $\sum_{k=0}^{12}\binom{12}{k} 10^{k} 60^{12-k}=70^{12}$ (why?) we find that $\sum_{k=1}^{12}\binom{12}{k} 10^{k} 60^{12-k}=70^{12}-\binom{12}{0} 10^{0} 60^{12-0}=70^{12}-60^{12}$.

    ${ }^{5} \mathrm{~A}$ deck of cards is a set consisting of 52 cards. A hand of poker is a subset of 5 cards from the deck (thus, being a subset of a set, the cards in a hand of poker are distinct and their order is irrelevant). To be able to pose interesting counting problems it is good to know that each card in a deck has one of four possible suits/couleurs, namely spades/piques/ $\mathbf{\uparrow}$, hearts/cours $/ \odot$, diamonds/carreaux/ $\diamond$, or clubs/trèfles/\&, and each suit consist of 13 different kinds/rangs, namely ace/as $/ A, 2$ through 10 , jack/valet $/ J$, queen/dame $/ Q$, and king/roi/K.

