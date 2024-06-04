Birthday paradox. Just like a random variable is not random and not a variable either, the birthday paradox (as the book's "birthday problem" is commonly referred to) is not a paradox, but just the mathematical fact that duplicate outcomes of experiments based on sampling with replacement are not as rare as most would intuitively expect. It follows that an "unexpectedly small" class size suffices to get a more than $50 \%$ probability that two students have the same birthday. The fact that duplicates (or "collisions") are so common has more important practical consequences too.

Let $S$ be a set of (thus distinct) outcomes with $|S|=n$. Consider an experiment where an element from $S$ is drawn at random, after which the element is returned to $S$ and the experiment is repeated. What can be said about the probability $p_{k}$ (the "collision probability") that at the $k$-th experiment an element is drawn that had been drawn before, i.e., a "duplicate element", or an element that "causes a collision"?

Clearly $p_{1}=0$ : the first element selected cannot be a duplicate. Each time a new element is selected that has not been drawn before, the pool of available "new" candidates shrinks while the pool of collision-causing candidates grows: indeed, $p_{k}=1$ for $k>n$ (obviously, or use the pigeonhole principle). Thus, the probability $p_{k}$ increases with $k$ (below it is argued more precisely that this is indeed the case), which leads to the question what the smallest value of $k$ is for which the collision probability $p_{k}$ is at least $\frac{1}{2}$.

Because as a result of each new non-duplicate drawing the number of available elements that can be drawn and that would cause a collision increases by one, the pool of available collision-causing candidates grows in a linear manner. It is natural to interpret this obvious linear growth of the collision-pool as a linear growth of the collision probability: intuitively, after drawing about $\frac{n}{2}$ non-duplicates, the probability to draw a duplicate should have become about $\frac{1}{2}$. This intuition turns out to be misleading: the pool of non-collision-causing drawings shrinks linearly, causing the non-collision probability, as a product of linearly shrinking factors, to decrease quadratically: this is simply based on the fact that linearly growing terms accumulate to a quadratic result $\left(\sum_{i=0}^{k} i=\frac{k(k+1)}{2}=\Theta\left(k^{2}\right)\right)$. The complementary probability - the collision probability - thus increases quadratically and not linearly. A more (but not fully) detailed version of this argument is given below.

Finding $p_{k}$ is conveniently done by considering the complementary probability $q_{k}=1-p_{k}$ that the first $k$ elements drawn are all distinct: it is easily seen that

$$
\begin{aligned}
q_{1} & =\frac{n}{n}=1 \\
q_{2} & =q_{1} \cdot \frac{n-1}{n}=\frac{n}{n} \frac{n-1}{n} \\
q_{3} & =q_{2} \cdot \frac{n-2}{n}=\frac{n}{n} \frac{n-1}{n} \frac{n-2}{n} \\
& \cdots \\
q_{k} & =q_{k-1} \cdot \frac{n-k+1}{n}=\prod_{i=0}^{k-1} \frac{n-i}{n}
\end{aligned}
$$

Note that the sequence of $q_{k}$-values is strictly decreasing and that $q_{k}=0$ for $k>n$, corresponding to our earlier observation that $p_{k}=1$ for $k>n$ (because $p_{k}+q_{k}=1$ ).

We are interested to find the least $k$ such that $p_{k} \geq \frac{1}{2}$. From $p_{k}+q_{k}=1$ it follows that this $k$ is the least $k$ such that $q_{k} \leq \frac{1}{2}$, so we have to

$$
\text { find the least } k \text { such that } \prod_{i=0}^{k-1}(n-i) \leq \frac{n^{k}}{2}
$$

This requires more calculus than we are ready to do in this class, but a quick-anddirty answer can be obtained by observing that

$$
\begin{aligned}
\prod_{i=0}^{k-1}(n-i) & =n^{k}-\left(\sum_{i=0}^{k-1} i\right) n^{k-1}+c n^{k-2}-\ldots \\
& =n^{k}-\frac{(k-1) k}{2} n^{k-1}+c n^{k-2}-\ldots
\end{aligned}
$$

for some $c$ and where the "..." stands for lower order terms. The condition becomes

$$
n^{k}-\frac{(k-1) k}{2} n^{k-1}+c n^{k-2}-\ldots \leq \frac{n^{k}}{2}
$$

thus

$$
n^{k} \leq(k-1) k n^{k-1}-2 c n^{k-2}+\ldots
$$

Assuming that the " $-2 c n^{k-2}+\ldots$ "-part is relatively unimportant, it follows that for $k$ close to $\sqrt{n}$ the left hand side $n^{k}$ cancels against the right hand side term $(k-1) k n^{k-1}$, and that for slightly larger $k$ the term $(k-1) k n^{k-1}$ will be bigger than $n^{k}+2 c n^{k-2}-\ldots$ as well. Thus for $k$ somewhat larger than $\sqrt{n}$ the probability $q_{k}$ will become $\leq \frac{1}{2}$ (the precise value depends on how the details of the " $-2 c n^{k-2}+\ldots$. "part work out).

The (counterintuitive) upshot is that it suffices to have just 23 students in a class to get a probability of more than $50 \%$ that two students have the same birthday ${ }^{1}$. The difference between 23 and the more "intuitive" $\frac{366}{2}$ is just an order of magnitude, and as far as I know the wrong intuition for this example has not led to major disasters. If the sample space $S$ is huge, however, the "gap" between the correct $\sqrt{|S|}$ and the intuitive but wrong $\frac{|S|}{2}$ turns out to be "incomprehensibly large" with practitioners failing to understand that only a "little" (relatively speaking) is needed to create an often undesirable collision. This is briefly elaborated upon in the gray part below.[^0]

The more problematic consequence of this result is that in circumstances where duplicate selection from the sample space leads to "problems" (such as security breaches), the sample space must be chosen relatively large: to make sure that drawing a duplicate requires effort at least $2^{n}$ (or happens with probability at most $\left.2^{-n}\right)$, the first requirement is that the sample space contains at least $2^{2 n}$ elements. Operating systems that seed their pseudo-random number generator (as used for the generation of cryptographic keys) with a 64 -bit number may be expected, across different platforms world-wide, to generate a seed already used earlier by someone else (and thus the same cryptographic keys as someone else) as soon as more than about $\sqrt{2^{64}}=2^{32}$ seeds have been generated: the question is not if duplicate keys have been generated, but how their (guaranteed) existence can be exploited. This problem is still only partially recognized by the software industry and has, so far, not been adequately addressed. It has, however, already led to a number of politely phrased - undesirable consequences.

## Chapter 8: advanced counting

This chapter contains a whole bunch of counting tricks. We will focus on the two most important ones, namely setting up a recurrence relation (section 8.1) and (solving them using) generating functions (section 8.4). In particular we will skip section 8.2 about solving linear (non)homogeneous recurrence relations because it is not particularly insightful and (mostly) follows from generating functions anyhow. Section 8.3 contains useful results on how to solve common recurrence relations that one runs into when analysing standard recursive divide-and-conquer algorithms: good to use as a reference when needed, but not of great general interest. Overall, for Chapter 8 it will suffice to restrict yourself to the material presented in the lecture notes (unless indicated otherwise). Also we will not have time to cover sections 8.5 and 8.6 .

Introduction to recurrence relations. Read Section 8.1 for a number of nice, and not all trivial, examples of recurrence relations: ways to express a parameterized value of interest in terms of the "same" value(s) but then with smaller parameter(s). Climbing a staircase: one stair at a time. As a most basic example, assume one is climbing a staircase ("escalier") consisting of $n$ stairs ("marches") one stair at a time, while never going back. So one starts at the bottom (at $i=0$ ), always moves from stair $i$ to stair $i+1$, and stops as soon as stair $n$ is reached. It is not hard to count the number $a_{n}$ of ways in which one can reach stair $n$ at the top: because there is never any choice to be made it is the case that $\forall n a_{n}=1$.

Climbing a staircase: one or two stairs at a time. The example gets more interesting if one either takes one stair or two stairs at a time: so a single step may consist of moving from stair $i<n$ to stair $i+1$ or from stair $i$ to stair $i+2 \leq n$. How do we count the number $d_{n}$ of ways in which one can reach stair $n$ at the top if one may take either one or two stairs at a time?

Standard combinatorial counting. If no double step is taken, the $n$-th stair can be reached in just a single way, as before. If $n \geq 2$ one may take two stairs at a time (i.e., in a single step): doing so exactly once, and taking all other stairs one-by-one, a total of $n-1$ steps are taken: once a double one and $n-2$ single steps, with $\binom{n-1}{1}$ choices when to take the single double step. If $n \geq 4$, one may take twice two stairs at a time: doing so exactly twice, and taking all other stairs one-by-one, a total of $n-2$ steps are taken: twice a double and $n-4$ single steps, with $\binom{n-2}{2}$ choices when to take the two double steps. We find that if none, one, or two double steps are taken (with $n \geq 4$ ) the $n$-th stair can be reached in $1+\binom{n-1}{1}+\binom{n-2}{2}$ distinct ways. Repeating the same argument with precisely three double steps, precisely
four double steps, etc., we find that

$$
\begin{equation*}
d_{n}=\sum_{i=0}^{\lfloor n / 2\rfloor}\binom{n-i}{i} \tag{1}
\end{equation*}
$$

Though this is a nice expression for $d_{n}$ it is not in "closed form" - i.e., not a simple function of $n$ that can be evaluated in $O(1)$ elementary operations on values of sizes comparable to the maximum of the result and the parameters involved ( $n$ in the present case): as follows from what is derived below the result $d_{n}$ grows as fast as $c^{n}$ for a constant $c>1$ so the overall calculation will require effort at least linear in $n$ anyhow. We can do better than computing $d_{n}$ using Equation (1), however.

Interpreting the result as a recurrence relation. Trying to interpret this value $d_{n}$ in the context of Pascal's triangle (where $d_{n}$ is the sum of the values along some sort of "diagonal": the sum of the green values in the picture below equals $d_{7}=21$; the blue values sum up to $d_{8}=34$; and the red ones to $d_{9}=55$ ) does not lead to an immediate closed form expression either. But, if we consider $d_{n}$ along with $d_{n+1}$ (while using Pascal's identity or Pascal's triangle) we find that $d_{n+2}=d_{n+1}+d_{n}$.

This expression $d_{n+2}=d_{n+1}+d_{n}$ is a recurrence relation and looks quite a bit more appealing than Expression (1), looks familiar (because it is the same recurrence relation as used to define the Fibonacci numbers), and is so simple that there must be an easier way to argue that this simple recurrence holds than deriving it via the Pascal triangle detour. Unfortunately, it still does not immediately lead to a closed form expression, but that is what is addressed in this chapter: how to derive a recurrence relation (such as the one that we have now stumbled upon for $d_{n+2}$ ) for a counting problem, and how to derive a closed form expression for the values given by the recurrence relation.

Finding the same recurrence relation directy. To directly derive recurrence relations for $a_{n}$ and $d_{n}$ one argues as follows. The only way to reach stair $i$ for any $i>0$ is via stair $i-1$, so $a_{i}=a_{i-1}$, implying that the number of ways in which stair $i$ can be reached is the same as the number of ways in which stair $i-1$ can be reached. If we take $a_{0}=1$ (counting the single way to start at the bottom of[^1]the staircase), we find $a_{1}=1, a_{2}=a_{1}=1, \ldots, a_{n}=a_{n-1}=1$ : there is just one way to reach the top of the staircase if one does it one stair at a time. We find that $a_{i}=a_{i-1}$, which is a recurrence relation but not a particularly interesting one. We refer to $a_{0}=1$ as the initial condition.

To solve $d_{n}$ via a recurrence relation there is one way to reach the bottom of the stair $\left(d_{0}=1\right)$, and stair 1 can still be reached in only one way (namely in a single step from the bottom of the staircase) so that $d_{1}=1$. But for $i \geq 2$ stair $i$ can be reached either in a single one-stair-step from stair $i-1$ or in a single two-stair-step from stair $i-2$. It follows that for $i \geq 2$ the number $d_{i}$ of ways in which one can reach stair $i$ is the sum of the number $d_{i-1}$ of ways in which one can reach stair $i-1$ plus the number $d_{i-2}$ of ways in which one can reach stair $i-2$. We find the recurrence relation $d_{i}=d_{i-1}+d_{i-2}$ for $i \geq 2$; along with the initial conditions $d_{0}=d_{1}=1$ this fully determines the sequence $d_{i}: d_{0}=1, d_{1}=1, d_{2}=2, d_{3}=3$, $d_{4}=5, d_{5}=8, d_{6}=13, d_{7}=21, d_{8}=34, d_{9}=55, \ldots$, and is indeed precisely the recurrence relation that we happened to find earlier based on what we know about Pascal's triangle. The numbers listed are the Fibonacci numbers, though the initial conditions are slightly different from the usual initial conditions for the Fibonacci sequence (in the October 17 lecture they were defined as $f_{0}=0, f_{1}=1$, and then $f_{i}=f_{i-1}+f_{i-2}$ for $i \geq 2$ ), causing the sequence $d_{n}$ to be one step ahead of the regular Fibonacci sequence. Note that Expression (1) now gives us a new way to express Fibonacci numbers:

$$
f_{n+1}=\sum_{i=0}^{\lfloor n / 2\rfloor}\binom{n-i}{i}
$$

plus a hand-waving argument (the color stuff in the earlier picture) why this identity should be valid (another example of a combinatorial argument).

At least one pair of consecutive zeros in an $n$-bit string. Let $a_{n}$ be the number of bit strings of length $n$ that contain at least one pair of consecutive zeros. Thus $a_{0}=a_{1}=0$ but $a_{2}=1$ (namely the bitstring " 00 "). To find a recurrence relation for $a_{n}$, we note the following: there are $a_{n-1}$ such bitstrings of length $n$ that have a final bit that is equal to 1 ; if the bitstring of length $n$ has a final bit equal to 0 , then there are two possibilities: either the second to last bit is 0 as well (in which case all $2^{n-2}$ possibilities are acceptable for the remaining $n-2$ bits); or the second to last bit is 1 (in which case there are $a_{n-2}$ possibilities for the remaining $n-2$ bits). Overall we find $a_{n}=a_{n-1}+a_{n-2}+2^{n-2}$. This turns out to have the closed form expression $2^{n}-f_{n+2}$ (where $f_{i}$ is the $i$-th Fibonacci number): refer to the book where the recurrence relation is derived for the number of "complementary" $n$-bit strings that do not contain a pair of consecutive zeros; the closed form expression $2^{n}-f_{n+2}$ then follows ${ }^{3}$. The recurrence relation $a_{n}=a_{n-1}+a_{n-2}+2^{n-2}$ can also be used directly to derive a generating function and a closed form expression for $a_{n}$ (we will not do so here, as it gets even messier than deriving the generating function and closed form expression for the Fibonacci numbers (which we will do next time)).

Precisely one pair of consecutive zeros. Let $b_{n}$ be the number of bit strings of length $n$ that contain precisely one pair of consecutive zeros. Thus $b_{0}=b_{1}=0$ but $b_{2}=1$ (namely the bitstring " 00 "). Looking at $b_{n}$ for $n \geq 3$, consider an $n$-bit string. If its final bit equals 1 , then there are $b_{n-1}$ ways to select the first $n-1$ bits. We may now assume that the final bit equals 0 . If the second to last bit equals 1 , then there are $\underline{b_{n-2}}$ ways to select the first $n-2$ bits. We may now assume that[^2]the final two bits both equals 0 . The third to last bit cannot be equal to zero, because that would imply two (overlapping) pairs of consecutive zeros. Thus, we now know that the third to last bit equals one, and $n-3$ bits still need to be chosen in such a way that there is no pair of consecutive zeros among the $n-3$ bits. This can be done in $2^{n-3}-a_{n-3}$ ways, with $a_{n-3}$ as above (thus the argument uses complementarity of the $a_{n}$-values as defined in the previous paragraph). Because $a_{n-3}=2^{n-3}-f_{n-1}$ (where $f_{i}$ is the $i$-th Fibonacci number) we find that $2^{n-3}-a_{n-3}=2^{n-3}-\left(2^{n-3}-f_{n-1}\right)=f_{n-1}$. Adding up the underlined parts, we find that $b_{n}=b_{n-1}+b_{n-2}+f_{n-1}$. I am not aware of an appealing closed form expression: if interested, check out www.oeis.org.


[^0]:    ${ }^{1}$ It also follows that, as mentioned in the October 9 lecture notes, with overwhelming probability there are two students in this class of about 380 students that have the same birthday on Jupiter (with 10563 Jupiter days in a Jupiter year).

[^1]:    ${ }^{2}$ Note that for even $n$ there is an exception at the far right too.

[^2]:    ${ }^{3}$ Note that $2^{n}-f_{n+2}$ is not yet a truly closed form expression until $f_{n+2}$ is replaced by a closed form expression.

