## Continuing with the basics of discrete probability theory

Independence. The following conditions are equivalent for events $E$ and $F$ with $p(E)>0$ and $p(F)>0$ :

- $E$ and $F$ are independent;
- $p(E \cap F)=p(E) p(F)$
- $p(E \mid F)=p(E)$
- $p(F \mid E)=p(F)$ (this follows from the definition $P(F \mid E)=\frac{p(E \cap F)}{p(E)}$ along with $p(E \cap F)=p(E) p(F)$ so that $\left.P(F \mid E)=\frac{p(E) p(F)}{p(E)}=p(F)\right)$.

If $E$ and $F$ are independent, then so are $\bar{E}$ (the complement of $E$ ) and $F$. This can be proved in many ways, such as $p(E \mid F)+p(\bar{E} \mid F)=1$ (why is that the case?) $\rightarrow$ $p(\bar{E} \mid F)=1-p(E \mid F)=1-p(E)$ (because $P(E \mid F)=p(E)$ due to the independence of $E$ and $F) \rightarrow p(\bar{E} \mid F)=p(\bar{E}) \rightarrow \bar{E}$ and $F$ are independent.

Pairwise and mutual independence. The definition of independence can be extended in two obvious ways to more than two events: with $\ell$ events $F_{1}, F_{2}, \ldots$, $F_{\ell}$, events are pairwise independent if for any two $i, j$ with $1 \leq i<j \leq \ell$ it is the case that $p\left(F_{i}\right) p\left(F_{j}\right)=p\left(F_{i} \cap F_{j}\right)$. The events are mutually independent if for any index-set $J \subseteq\{1,2, \ldots, \ell\}$ with $J \geq 2$ it is the case that $\prod_{j \in J} p\left(F_{j}\right)=p\left(\bigcap_{j \in J} F_{j}\right)$.

Obviously mutual independence implies pairwise independence. The other way around is not necessarily the case: a simple and well-known example (very informally described: try to make this description formal using our current tools, or use random variables as discussed later) is an experiment where a fair coin is independently tossed twice, $F_{1}$ is the event that outcome of the first toss is one, $F_{2}$ is the event that the outcome of the second toss is one, and $F_{3}$ is the XOR of the outcomes of the first and the second toss (thus the XOR of $F_{1}$ and $F_{2}$ ). It is easily checked that $F_{1}, F_{2}$, and $F_{3}$ are pairwise independent, but because $p\left(F_{1} \cap F_{2} \cap F_{3}\right)=0 \neq \frac{1}{8}=p\left(F_{1}\right) p\left(F_{2}\right) p\left(F_{3}\right)$ they are not mutually independent.

## More basics of discrete probability theory: things you must have seen

Tossing a fair coin $n$ times. If a fair coin is tossed $n$ times and the order of the outcomes is relevant, then there are $2^{n}$ different outcomes, each of which occurs with probability $2^{-n}$. If the order of the heads or tails is not considered to be relevant (so all that counts is the number of heads versus the number of tails), there are $n+1$ distinct outcomes: namely from zero to $n$ times heads among $n$ possibilities (this can also be counted as selecting an $n$-combination from a 2 -set with replacement, thus $\binom{2+n-1}{n}=\binom{n+1}{n}=n+1$ distinct possibilities: note that, confusingly, $n$ is here playing the role of $r$ in the earlier lectures, and that the $n$ from there is equal to 2 here).

Counting combinations using polynomial multiplications (a preview of coming attractions). For $n=1$ we represented the single possibility to toss tails (" 0 ") as $1 \cdot X^{0}$ and the single possibility to toss heads (" $1 "$ ) as $1 \cdot X^{1}$, and thus the possible outcomes of the first toss (tails or heads) as $1 \cdot X^{0}+1 \cdot X^{1}=1+X$. This same $1+X$ can be used to represent the possible outcomes of a second toss, and thus the product $(1+X)(1+X)=\left(1 \cdot X^{0}+1 \cdot X^{1}\right)\left(1 \cdot X^{0}+1 \cdot X^{1}\right)=$ $1 \cdot X^{0} X^{0}+1 \cdot X^{0} X^{1}+1 \cdot X^{1} X^{0}+1 \cdot X^{1} X^{1}=1+2 X+X^{2}$ as the representation of all possible outcomes of two coin tosses (if this is mystifying, see "further explanation" below): note that in the polynomial product all possible outcomes of the first toss are combined with all possible outcomes of the second toss and that due to $X^{0} \cdot X^{1}=X^{1} \cdot X^{0}$ the order "tail-heads" is considered to be the same as the order "heads-tails".

With $1+2 X+X^{2}=1 \cdot X^{0}+2 \cdot X^{1}+1 \cdot X^{2}$ we find that there is one way to toss no heads (tails twice; " $1 \cdot X^{0}$ "), there are two ways to toss heads once (thus tails once; " $2 \cdot X^{1}$ ") and there is one way to toss heads twice (" $1 \cdot X^{2}$ "). Continuing in this manner, with $(1+X)^{3}=1+3 X+3 X^{2}+X^{3}$, there is one way to toss no heads, three ways to toss heads once, three to toss heads twice, and one to toss heads three times; with $(1+X)^{4}=1+4 X+6 X^{2}+4 X^{3}+X^{4}$ one way to toss no heads, four ways to toss one head, six ways to toss two heads, four ways to toss three heads, and one way to toss four heads. Etc. With $(1+X)^{n}=\sum_{k=0}^{n}\binom{n}{k} X^{k}$ (due to the binomial theorem): there are $\binom{n}{k}$ ways to toss $k$ heads. And - a nice side-result that is immediately confirmed by the binomial theorem with $X=1=Y$ - all possibilities together must add up to $2^{n}$, so $\sum_{k=0}^{n}\binom{n}{k}=2^{n}$ (which you can also see by partitioning the set of all subsets of an $n$-set (i.e., its power set, thus of cardinality $2^{n}$ ) into the subsets of zero elements (of which there are $\binom{n}{0}$ ), the subsets containing one element ( $\binom{n}{1}$ of those), the subsets containing two elements $\left.\binom{n}{2}\right)$, etc. $)$

Further explanation. Suppose that there is some goal function that works additively, i.e., first achieving goal $i$ and then goal $j$ implies having achieved goal $i+j$. For instance, tossing heads $k$ times, as a result of a first experiment, and then tossing heads $\ell$ times (for some $k \neq \ell$ ), as a result of a second experiment, implies having tossed heads $k+\ell$ times (as a result of the two experiments). If the first (tossing heads $k$ times) can be achieved in $a$ ways, and the second (tossing heads $\ell$ times) in $b$ ways, then $k+\ell$ can be achieved in $a b$ ways. Or $2 k$ can be achieved in $a^{2}$ ways by repeating the first experiment. If we represent the " $k$ in $a$ ways" by $a X^{k}$ and the " $\ell$ in $b$ ways" by $b X^{\ell}$, then the combined " $k+\ell$ in $a b$ ways" is represented by the product $a b X^{k+\ell}$ of $a X^{k}$ and $b X^{\ell}$

This simple "trick" immediately generalizes to sums of polynomials and their products. If, as a result of an experiment, $k$ can be achieved in $a_{1}$ ways or $\ell$ can be
achieved in $a_{2}$ ways (where $k \neq \ell$ ), then we represent this as $a_{1} X^{k}+a_{2} X^{\ell}$. Then, with $b_{1} X^{k}+b_{2} X^{\ell}$ representing that, as a result of some experiment (independent of the first), $k$ can be achieved in $b_{1}$ ways or $\ell$ in $b_{2}$ ways, then the product

$$
\left(a_{1} X^{k}+a_{2} X^{\ell}\right)\left(b_{1} X^{k}+b_{2} X^{\ell}\right)=a_{1} b_{1} X^{2 k}+\left(a_{1} b_{2}+a_{2} b_{1}\right) X^{k+\ell}+a_{2} b_{2} X^{2 \ell}
$$

tells us that, as a result of the two experiments, $k+\ell$ can be achieved in $a_{1} b_{2}+$ $a_{2} b_{1}$ ways (where our usage of $X^{k} X^{\ell}=X^{k+\ell}=X^{\ell+k}=X^{\ell} X^{k}$ implies that we are not interested in the order in which the goals are achieved: we are counting combinations, not permutations).

A simple example: $X+X^{2}+X^{3}+X^{4}+X^{5}+X^{6}$ represents (using the method sketched above) the outcome of throwing a die. Thus the coefficients of the polynomial $\left(X+X^{2}+X^{3}+X^{4}+X^{5}+X^{6}\right)^{2}=X^{2}+2 X^{3}+3 X^{4}+4 X^{5}+5 X^{6}+$ $6 X^{7}+5 X^{8}+4 X^{9}+3 X^{10}+2 X^{11}+X^{12}$ tell us in how many ways one can achieve a certain sum of throws of two dice: sum 8 can be achieved in 5 ways. With $X+X^{2}+X^{3}+X^{4}+X^{5}+X^{6}=X\left(1+X+X^{2}+X^{3}+X^{4}+X^{5}\right)=\frac{X\left(X^{6}-1\right)}{X-1}$, the sum of throws of $n$ dice is fully specified by the coefficients of the polynomial $\frac{X^{n}\left(X^{6}-1\right)^{n}}{(X-1)^{n}}$. If there is anything else bothering you concerning this method to count combinations using polynomials, make sure to ask questions in class, because this approach will be instrumental for our later, more advanced counting methods.

Computing the average number of heads. With heads and tails equally likely, on average one should get $\frac{n}{2}$ heads and $\frac{n}{2}$ tails. This can be formally derived in the following manner.

Because for each $k$ with $0 \leq k \leq n$ there are $\binom{n}{k}$ tosses among the $2^{n}$ distinct $n$-permutations (resulting from $n$ coin tosses) that have $k$ heads, the average number of heads equals ${ }^{1} \frac{1}{2^{n}} \sum_{k=0}^{n} k\binom{n}{k}=\frac{1}{2^{n}} \sum_{k=1}^{n} \frac{k n!}{k!(n-k)!}=\frac{1}{2^{n}} \sum_{k=1}^{n} \frac{n!}{(k-1)!(n-k)!}$. Replacing $k-1$ by $k$ this becomes $\frac{1}{2^{n}} \sum_{k=0}^{n-1} \frac{n!}{k!(n-k-1)!}=\frac{n}{2^{n}} \sum_{k=0}^{n-1} \frac{(n-1)!}{k!(n-1-k)!}=$ $\frac{n}{2^{n}} \sum_{k=0}^{n-1}\binom{n-1}{k}$. Because (due to the binomial theorem) $\sum_{k=0}^{n-1}\binom{n-1}{k}=2^{n-1}$ we find that the average number of heads equals $\frac{n \cdot 2^{n-1}}{2^{n}}=\frac{n}{2}$, as expected.

Obviously, we get precisely the same if in the calculation of our average $\frac{1}{2^{n}} \sum_{k=0}^{n} k\binom{n}{k}$ we pull the probability $\frac{1}{2^{n}}$ in the summation, resulting in $\sum_{k=0}^{n} k\binom{n}{k} \frac{1}{2^{n}}$, with $\binom{n}{k} \frac{1}{2^{n}}$ representing the probability to toss heads $k$ times as a result of $n$ coin tosses.

More traditional way to count the number of combinations. Of the $n+1$ outcomes, there is 1 with no heads (and thus $n$ tails): it occurs with probability $2^{-n}$. A single heads (and thus $n-1$ tails) can be realized in $n$ distinct manners (the single heads at the first place, or at the second place, or at the third place,..., or at the second to last place, or at the last place), and thus occurs with probability $n \cdot 2^{-n}$ (because all $n$ possibilities are distinct as $n$-permutations, though identical as $n$-combinations). Two heads can be realized in $\binom{n}{2}$ ways, and therefore occurs with probability $\binom{n}{2} 2^{-n}$. More in general, for any integer $k$ with $0 \leq k \leq n$ (thus indeed representing all $n+1$ possibilities), there are $\binom{n}{k}$ distinct ways to realize $k$ heads and $n-k$ tails, each with probaility $2^{-n}$, and thus $k$ heads and $n-k$ tails occurs with probability $\binom{n}{k} 2^{-n}$. Denoting by $p(k)$ the probability of finding $k$ times[^0]heads when a fair coin is tossed $n$ times, we find that

$$
p(k)=\binom{n}{k} 2^{-n}
$$

This indeed leads to a probability distribution on the sample space $S=\{0,1,2, \ldots, n\}$ (i.e., the number of heads among $n$ coin tosses) because

$$
\sum_{k=0}^{n} p(k)=\sum_{k=0}^{n}\binom{n}{k} 2^{-n}=2^{-n} \sum_{k=0}^{n}\binom{n}{k}=2^{-n} 2^{n}=1
$$

due to the binomial theorem (with $X=Y=1$ ).

Not necessarily fair coin. More in general, if the coin is not necessarily fair and has probability $p$ of heads and complementary probability $q=1-p$ of tails, then the (equal) probabilities $2^{-n}$ (irrespective of $k$ ) above must be replaced by probabilities that depend on the applicable $k$-value: if there are $k$ heads and (thus) $n-k$ tails, the probability becomes $p^{k} q^{n-k}$. It follows that $p(k)=\binom{n}{k} p^{k} q^{n-k}$ for any integer $k$ with $0 \leq k \leq n$. This is known as Bernoulli trials and is further described below.

Using this observation that, in general, the $2^{-n}$ should be replaced by $p^{k} q^{n-k}$, the formula in red in the above calculation of the average number of heads would change into $\sum_{k=0}^{n} k\binom{n}{k} p^{k} q^{n-k}$, and the ensuing calculation would, after a simple modification, results in $n p$ (as opposed to the earlier "average $\frac{n}{2}$ "). This new value $n p$ is no longer referred to as the "average", but as the "expected value", as further explained below (where you can also find the full modified calculation that results in $n p)$.

Bernoulli trials. Let $p$ be the probability of success of an experiment, with complementary probability $q=1-p$ of failure. An experiment of this sort is called a Bernoulli trial. Assume that a sequence of $n$ Bernoulli trials is conducted, and that the $n$ trials are mutually independent (as defined last time), i.e., the success of either subset of the $n$ trials does not affect the success of any of the other trials: each trial has success probability $p$ and failure probability $q=1-p$, irrespective of what happened before or after it in the sequence of $n$ trials. (In virtually all practical circumstances this "mutual independence" is just an assumption that is very hard to verify and even harder to realize, in particular if the "same" experiment is repeated over and over again, such as roulette.)

The set $S$ of outcomes of $n$ Bernoulli trials has cardinality $2^{n}$ (because there are $n$ experiments, and each experiment has two possible outcomes). Let $E_{i}$ denote the event that the $i$-th trial is successful, thus $p\left(E_{i}\right)=p, p\left(\bar{E}_{i}\right)=q$, the $E_{i}$ are mutually independent and the $\bar{E}_{i}$ are mutually independent (why?). Then $E_{i} \subset S$, $\bar{E}_{i} \subset S$, and $\left|E_{i}\right|=\left|\bar{E}_{i}\right|=2^{n-1}$. Also, for any choice of $C_{i} \in\left\{E_{i}, \bar{E}_{i}\right\}$ for $1 \leq i \leq n$, the $C_{i}$ are mutually independent (why?); note that $p\left(C_{i}\right)=p$ if $C_{i}=E_{i}$ and that $p\left(C_{i}\right)=q$ if $C_{i}=\bar{E}_{i}$.

Now $\bigcap_{i=1}^{n} E_{i}$ is the event that all $n$ trials are successful, and $\left|\bigcap_{i=1}^{n} E_{i}\right|=1$. According to the mutual independence $p\left(\bigcap_{i=1}^{n} E_{i}\right)=\prod_{i=1}^{n} p\left(E_{i}\right)=p^{n}$. Similarly, $\bigcap_{i=1}^{n} \bar{E}_{i}$ is the event that all $n$ trials fail, $\left|\bigcap_{i=1}^{n} \bar{E}_{i}\right|=1$, and $p\left(\bigcap_{i=1}^{n} \bar{E}_{i}\right)=$ $\prod_{i=1}^{n} p\left(\bar{E}_{i}\right)=q^{n}$. Furthermore, assuming that for $k$ of the $n$ values of $i$ we have that $C_{i}=E_{i}$ and that $C_{i}=\bar{E}_{i}$ for the other $n-k$ values of $i$, the probability $p\left(\bigcap_{i=1}^{n} C_{i}\right)$ equals $\prod_{i=1}^{n} p\left(C_{i}\right)=p^{k} q^{n-k}$. Because there are $\binom{n}{k}$ different ways to select the set $\left\{C_{i}: 1 \leq i \leq n\right\}$ in such a way that $C_{i}=E_{i}$ for $k$ of the $n$ values of $i$ and $C_{i}=\bar{E}_{i}$ for the other $n-k$ of the $i$-values, it follows (using the fact that the probability of the union of non-intersecting events is the sum of the probabilities
of the events) that the probability that there are $k$ successes among the $n$ trials is $\binom{n}{k} p^{k} q^{n-k}$

The above two (gray) paragraphs (which are for your entertainment only) are a somewhat more detailed version of the proof of Theorem 2 in section 7.2, arguing that among $n$ mutually independent Bernoulli trials there are $k$ successes with probability $\binom{n}{k} p^{k} q^{n-k}$ (as also explained in a somewhat more down-to-earth manner in the example of the $n$ coin tosses), thus constructing a probability distribution from the bottom up. As usual, it must be checked that this is a probability distribution. This is indeed the case because the number $k$ of successes must satisfy $0 \leq k \leq n$, because $\sum_{k=0}^{n}\binom{n}{k} p^{k} q^{n-k}=(p+q)^{n}=1$ (the binomial theorem), and because each term $\binom{n}{k} p^{k} q^{n-k}$ in the sum is non-negative while their sum equals one, so that no term $\binom{n}{k} p^{k} q^{n-k}$ can be greater than one. This probability distribution is called the binomial distribution.

Random variables. A convenient manner to move from any probability distribution to some other, possibly more interesting or relevant, distribution is by using a random variable - which is neither random nor a variable, but just a real-valued function that acts on the sample space of a distribution. Thus, a random variable assigns a real value to each outcome of the experiment.

The probability that a random variable, say $X$, when applied to an outcome of an experiment attains a certain value, say $x$ (in the codomain of $X$ ), depends in the obvious manner on the probability that the experiment results in an outcome, say $s$, that maps, under $X$, to $x$. More precisely: given some countable sample space $S$ and probability distribution $p: S \rightarrow \mathbf{R}$ on $S$ (thus $\forall s \in S \quad 0 \leq p(s) \leq 1$ and $\sum_{s \in S} p(s)=1$ ), the random variable $X: S \rightarrow \mathbf{R}$ inherits the probability distribution $p$ in the following simple manner:

$$
p(X=x)=\sum_{\{s: s \in S, X(s)=x\}} p(s)
$$

Thus (the same in words): the probability that $X$ attains the value $x$ is the sum of the probabilities of the $s \in S$ for which $X(s)=x$.

It follows that $p: X \rightarrow \mathbf{R}$ thus defined is a probability distribution on $X(S)$ :

$$
\begin{aligned}
\sum_{x \in X(S)} p(X=x) & \left.=\sum_{x \in X(S)}\left(\sum_{\{s: s \in S, X(s)=x\}} p(s)\right) \text { (using the definition of } p(X=x)\right) \\
& =\sum_{s \in S} p(s) \text { (figure out why the two summations collapse to one) } \\
& =1 \text { (because } p \text { is a probability distribution on } S)
\end{aligned}
$$

it is obvious that $0 \leq p(X=x)$ and $p(X=x) \leq 1$ now follows.

The pairs $(x, p(X=x))$ with $x$ ranging over the set $X(S)=\{x: \exists s \in S X(s)=$ $x\}$ is called the distribution of $X$ on $S$ given the probability distribution $p$ on $S$. Note the different notation: " $p(s)$ " denotes the (original) probability of the outcome $s \in S$, whereas " $p(X=x)$ " denotes the probability that $X$, when applied to the outcome of the experiment, attains the value $x$; the part " $X=$ " may be dropped from " $p(X=x)$ " if it is clear from the context.

Random variable example: sum of two dice (not done in class, but possibly instructive). As an example, let $\widetilde{S}$ be the set of 21 unordered pairs $(i, j)$ with $1 \leq i \leq j \leq 6$ resulting from simultaneously rolling two indistinguishable dice (thus with $p((i, i))=\frac{1}{36}$ for $1 \leq i \leq 6$ and $p((i, j))=\frac{1}{18}$ for $\left.1 \leq i<j \leq 6\right)$. Let the random variable $X: \widetilde{S} \rightarrow \mathbf{R}$ defined by $X((i, j))=i+j$. It follows
that $p(X=2)=\frac{1}{36}$, because when applied to an element from $\widetilde{S}$ the random variable $X$ can attain the value 2 only for $(1,1) \in \widetilde{S}$ and $p((1,1))=\frac{1}{36}$; similarly, $p(X=12)=\frac{1}{36}$ with $(6,6)$ as sole pre-image in $\widetilde{S}$ of 12 and $p((6,6))=\frac{1}{36}$. Furthermore, $p(X=3)=\frac{1}{18}$ because $(1,2)$ is the sole pre-image in $\widetilde{S}$ of 3 and $p((1,2))=\frac{1}{18}$; and $p(X=4)=\frac{1}{12}$ because $(1,3)$ and $(2,2)$ are the only two preimages in $\widetilde{S}$ of $4, p((1,3))=\frac{1}{18}, p((2,2))=\frac{1}{36}$, and $\frac{1}{18}+\frac{1}{36}=\frac{1}{12}$. Reasoning similarly for the other values in $X(\widetilde{S})$ the complete distribution of $X$ on $\widetilde{S}$ is:

$\left(2, \frac{1}{36}\right),\left(3, \frac{1}{18}\right),\left(4, \frac{1}{12}\right),\left(5, \frac{1}{9}\right),\left(6, \frac{5}{36}\right),\left(7, \frac{1}{6}\right),\left(8, \frac{5}{36}\right),\left(9, \frac{1}{9}\right),\left(10, \frac{1}{12}\right),\left(11, \frac{1}{18}\right),\left(12, \frac{1}{36}\right)$ which can also be written as

$$
\left(7+i, \frac{6-|i|}{36}\right) \text { for }-5 \leq i \leq 5
$$

The same example can be done on the set of 36 ordered pairs $(i, j)$ with $1 \leq i, j \leq 6$. Then, for instance, sum equal to 3 is obtained by the two ordered pairs $(1,2)$ and $(2,1)$, each of which occurs with probability $\frac{1}{36}$ for a total probability of $\frac{2}{36}=\frac{1}{18}$, whereas sum 3 is obtained only by the unordered pair $(1,2)$, which occurs with probability $\frac{1}{18}$ : it all boils down to the same. Also note the similarities and the difference between this example and Example 12 in Section 7.2.

As a simple exercise, you may want to check that the random variable $Y$ on $\widetilde{S}$ defined by $Y((i, j))=\max (i, j)$ has distribution $\left(1, \frac{1}{36}\right),\left(2, \frac{1}{12}\right),\left(3, \frac{5}{36}\right),\left(4, \frac{7}{36}\right)$, $\left(5, \frac{1}{4}\right),\left(6, \frac{11}{36}\right)$ (note that $1+3+5+7+9+11=36$ : make sure you understand where those numbers come from and why it is relevant that their sum is 36).

Random variable example: Bernoulli trials. Given the set $S$ of outcomes of $n$ Bernoulli trials (mutually independent and with probability $p$ of success per trial), we may define a random function $X$ on $S$ that counts the number of successes. From what we have seen above, at length, it follows that $p(X=k)=\binom{n}{k} p^{k} q^{n-k}$ for any integer $k$ with $0 \leq k \leq n$ is indeed a distribution of $X$ on $S-$ or, equivalently, a probability distribution on $X(S)$.

Obviously, if we do, say, 100 trials (i.e., $n=100$ ) and each trial has a probability of $25 \%$ to be successful (i.e., $p=\frac{1}{4}$ ) we may expect 25 successes overall, i.e., the expected value of $X$ would be 25 . This intuitive notion of expected value is defined in the following manner.

The expected value or mean of a random variable $X$ on a sample space $S$ is defined as

$$
\begin{equation*}
E(X)=\sum_{s \in S} p(s) X(s) \tag{1}
\end{equation*}
$$

which is equivalent to

$$
\begin{equation*}
E(X)=\sum_{x \in X(S)} p(X=x) x \tag{2}
\end{equation*}
$$

The equivalence follows from the definition $p(X=x)=\sum_{\{s: s \in S, X(s)=x\}} p(s)$ so that

$$
p(X=x) x=\sum_{\{s: s \in S, X(s)=x\}} p(s) X(s)
$$

and thus

$$
\sum_{x \in X(S)} p(X=x) x=\sum_{x \in X(S)} \sum_{\{s: s \in S, X(s)=x\}} p(s) X(s)
$$

combined with the observation that the summations " $\sum_{x \in X(S)} \sum_{\{s: s \in S, X(s)=x\}}$ " and " $\sum_{s \in S}$ " both range over the same $s$-values (the argument here is precisely the
same as you had to figure out before with the two summations that collapsed into a single one).

Which of the two ways of computing the expected value $E(X)$ of the random variable $X$, i.e.,

$$
E(X)=\sum_{s \in S} p(s) X(s) \quad \text { or } \quad E(X)=\sum_{x \in X(S)} p(X=x) x
$$

is the most convenient to use depends on the circumstances.

Examples of expected values. As a first example (not done in class), let $S$ be the set of outcomes of rolling two dice, and let $Y$ be the maximum of the two dice: what is $E(Y)$ ? Note this is essentially the same as $Y$ on $\widetilde{S}$ above, but here done on $S$ instead. With $S$ as ordered pairs $(i, j)$ with $p((i, j))=\frac{1}{36}$ and $Y((i, j))=\max (i, j)$ for $1 \leq i \leq 6$ and $1 \leq j \leq 6$ the definition $E(Y)=\sum_{s \in S} p(s) Y(s)$ leads to

$$
\begin{aligned}
& \frac{\max (1,1)}{36}+ \frac{\max (1,2)}{36}+\frac{\max (1,3)}{36}+\frac{\max (1,4)}{36}+\frac{\max (1,5)}{36}+\frac{\max (1,6)}{36}+ \\
& \frac{\max (2,1)}{36}+ \frac{\max (2,2)}{36}+\frac{\max (2,3)}{36}+\frac{\max (2,4)}{36}+\frac{\max (2,5)}{36}+\frac{\max (2,6)}{36}+ \\
& \frac{\max (3,1)}{36}+ \frac{\max (3,2)}{36}+\frac{\max (3,3)}{36}+\frac{\max (3,4)}{36}+\frac{\max (3,5)}{36}+\frac{\max (3,6)}{36}+ \\
& \frac{\max (4,1)}{36}+ \frac{\max (4,2)}{36}+\frac{\max (4,3)}{36}+\frac{\max (4,4)}{36}+\frac{\max (4,5)}{36}+\frac{\max (4,6)}{36}+ \\
& \frac{\max (5,1)}{36}+ \frac{\max (5,2)}{36}+\frac{\max (5,3)}{36}+\frac{\max (5,4)}{36}+\frac{\max (5,5)}{36}+\frac{\max (2,6)}{36}+ \\
& \frac{\max (6,1)}{36}+ \frac{\max (6,2)}{36}+\frac{\max (6,3)}{36}+\frac{\max (6,4)}{36}+\frac{\max (6,5)}{36}+\frac{\max (6,6)}{36}= \\
& \frac{1}{36}+\frac{2}{36}+\frac{3}{36}+\frac{4}{36}+\frac{5}{36}+\frac{6}{36}+ \\
& \frac{2}{36}+\frac{2}{36}+\frac{3}{36}+\frac{4}{36}+\frac{5}{36}+\frac{6}{36}+ \\
& \frac{3}{36}+\frac{3}{36}+\frac{3}{36}+\frac{4}{36}+\frac{5}{36}+\frac{6}{36}+ \\
& \frac{4}{36}+\frac{4}{36}+\frac{4}{36}+\frac{4}{36}+\frac{5}{36}+\frac{6}{36}+ \\
& \frac{5}{36}+\frac{5}{36}+\frac{5}{36}+\frac{5}{36}+\frac{5}{36}+\frac{6}{36}+ \\
& \frac{6}{36}+\frac{6}{36}+\frac{6}{36}+\frac{6}{36}+\frac{6}{36}+\frac{6}{36}= \\
& \frac{21}{36}+\frac{22}{36}+\frac{24}{36}+\frac{27}{36}+\frac{31}{36}+\frac{36}{36}=\frac{161}{36}=4+\frac{17}{36} .
\end{aligned}
$$

That worked, but it is cumbersome. It is probably easier to first derive the probability distribution of $Y$, by noticing that $Y(s)=1$ only for $s=(1,1)$, so that $p(Y=1)=\frac{1}{36}$, that $Y(s)=2$ only for $s \in\{(1,2),(2,1),(2,2)\}$ so that $p(Y=2)=\frac{3}{36}$, etc., resulting in

$$
p(Y=i)=\frac{2 i-1}{36} \text { for } 1 \leq i \leq 6
$$

and (using $\left.E(Y)=\sum_{y \in Y(S)} p(Y=y) y\right)$

$$
E(Y)=\sum_{i=1}^{6} \frac{i(2 i-1)}{36}=4+\frac{17}{36}
$$

Yet another way to compute $E(Y)$ would be via the unordered pairs $\widetilde{S}$ as introduced earlier.

As a second example, for $X((i, j))=i+j$ as defined earlier, one finds the distribution

$$
\left(7+i, \frac{6-|i|}{36}\right) \text { for }-5 \leq i \leq 5
$$

Combining $7+i$-values with the same $|i|$-value, it follows that the expected value $E(X)$ of the sum equals

$$
\frac{(2+12)+(3+11) 2+(4+10) 3+(5+9) 4+(6+8) 5+(7) 6}{36}
$$

and thus

$$
\frac{14}{36}(1+2+3+4+5+6-3)=7
$$

Expected value of $n$ Bernoulli trials. To confirm our earlier suspicion that we may expect 25 successful outcomes when we do 100 identical and mutually independent Bernoulli trials with success probability $\frac{1}{4}$, let $X$ be the number of successes of $n>0$ identical and mutually independent Bernoulli trials with succcess probability $p$ and let, as above, $p(X=k)=\binom{n}{k} p^{k} q^{n-k}$. Using $E(X)=\sum_{s \in S} p(s) X(s)$ is inconvenient, but using $E(X)=\sum_{x \in X(S)} p(X=x) x$ works nicely, as illustrated below:

$$
\begin{aligned}
E(X) & =\sum_{k=0}^{n} p(X=k) k \\
& =\sum_{k=0}^{n} k\binom{n}{k} p^{k} q^{n-k}=\sum_{k=1}^{n} k\binom{n}{k} p^{k} q^{n-k} \\
& =\sum_{k=1}^{n} \frac{k n!}{k!(n-k)!} p^{k} q^{n-k} \\
& =n p \sum_{k=1}^{n} \frac{(n-1)!}{(k-1)!(n-k)!} p^{k-1} q^{n-k} \\
& =n p \sum_{k=1}^{n} \frac{(n-1)!}{(k-1)!(n-1-(k-1))!} p^{k-1} q^{n-1-(k-1)} \\
& =n p \sum_{\ell=0}^{n-1} \frac{(n-1)!}{\ell!(n-1-\ell)!} p^{\ell} q^{n-1-\ell} \\
& =n p \sum_{\ell=0}^{m} \frac{m!}{\ell!(m-\ell)!} p^{\ell} q^{m-\ell}(\text { where } m=n-1 \geq 0) \\
& =n p \sum_{\ell=0}^{m}\binom{m}{\ell} p^{\ell} q^{m-\ell} \\
& =n p(p+q)^{m}(\text { due to the binomial theorem }) \\
& =n p .
\end{aligned}
$$

This is indeed the result one would intuitively have expected: for $n$ experiments with probability of success $p$ per experiment one may expect to find $n p$ successes overall. Note that the calculation is essentially identical to the calculation of the average number of heads among $n$ fair coin tosses, as done above, and is only a bit more complicated due to the additional powers of $p$ and $q$ : for $p=q=\frac{1}{2}$ it is the same calculation. It turns out, however, that this was a lot of work for nothing
(because the same result can be proved in a much easier manner) and that the mutual independence (used to derive $\left.p(X=k)=\binom{n}{k} p^{k} q^{n-k}\right)$ is not even necessary. This will be shown during the next lecture.

Deviating from the expected value. One reason to compute an expected value is to gain insight in the "behavior" of a random variable, i.e., how likely it is that it attains values that are "far away" from the expected value. For instance, Markov's inequality says that if $X$ is non-zero and non-negative (i.e., $\exists s \in S X(s) \neq 0$ and $\forall s \in S X(s) \geq 0$ ), then the probability is at most $\frac{1}{M}$ (for some $M>0$ ) that the random variable attains a value at least $M$ times its expected value $E(X)$. Said differently, if $X$ is non-zero and non-negative then for any positive real number $a$ the value $E(X) / a$ is an upper bound for the probability that $X(s) \geq a$ :

$$
\begin{aligned}
E(X) / a & =\sum_{x \in X(S)} x p(X=x) / a \text { (now use that } X \text { is non-negative:) } \\
& \geq \sum_{x \in X(S), x \geq a} x p(X=x) / a(\text { and now that } x / a \geq 1:) \\
& \geq \sum_{x \in X(S), x \geq a} p(X=x) \\
& =p(X \geq a)
\end{aligned}
$$

Thus, with $a=M \cdot E(X)$, the probability $p(X \geq M \cdot E(X))$ that $X$ attains a value that is at least $M \cdot E(X)$ is bounded from above by $\frac{E(X)}{M \cdot E(X)}=\frac{1}{M}$. For 100 Bernoulli trials with $25 \%$ probability of succes per trial where we expect 25 successes, Markov's inequality tells us that we have probability at most $\frac{1}{2}$ to find 50 or more successes, and probability at most $\frac{1}{3}$ to have 75 or more successes. These are pretty weak results. A somewhat "better" bound requires an additional definition and will be discussed next time.

Next class. (Re)read Chapter 7. In the unlikely case that we manage to quickly wrap up basic probabilities then it is useful to read Section 8.1 (otherwise doing so is useful for Friday's lecture).


[^0]:    ${ }^{1}$ If you do not understand this formula, do a small example. For instance, for $n=3$, there are $2^{3}=8$ distinct sequences of 3 throws $(000,001,010,011,100,101,110,111)$, one with no heads (000), three with one heads $(001,010,100)$, three with two heads $(011,101,110)$, and one with three heads (111). Thus the average number of heads is $\frac{0+1+1+1+2+2+2+3}{8}=\frac{12}{8}=\frac{3}{2}$; this is more conveniently (because involving only $n+1=4$ terms as opposed to $2^{n}=8$ terms) written as the summation $\frac{0\binom{3}{0}+1\binom{3}{1}+2\binom{3}{2}+3\binom{3}{3}}{8}$ and thus as $\frac{1}{2^{3}} \sum_{k=0}^{3} k\binom{3}{k}$, i.e., the formula for $n=3$.

