## Wrapping up basics of discrete probability theory

More on deviating from the expected value. At the end of the previous lecture we saw that for a non-zero, non-negative random variable $X$ a weak estimate can be given for $X$ to deviate much from its expected value $E(X)$ : Markov's inequality tells us that for any $M>0$ it is the case that $p(X \geq M \cdot E(X)) \leq \frac{1}{M}$. Applying this to, for instance, 100 independent Bernoulli trials with probability $p=\frac{1}{4}$ of success (per trial) and with $X$ the random variable that counts the number of successes, we find that $E(X)=n p=\frac{100}{4}=25$; with $M>2$ it follows that $p(X>50)<\frac{1}{2}$. For $p=\frac{1}{2}$ and thus $E(X)=50$ one finds with $M>2$ that $p(X>100)<\frac{1}{2}$, which is useless because $p(X>100)=0$ anyhow.

Another, also rather weak but often more useful and completely general estimate is given by Chebyshev's inequality which tells us something about the probability $p(|X(s)-E(X)| \geq \delta)$ that a random variable $X$ deviates at least $\delta$ from its expected value $E(X)$. Unlike Markov' inequality, it is independent of any properties of the random variable, but it requires the introduction of the variance of a random variable.

Variance. The variance $V(X)$ of a random variable $X$ on a sample space $S$ is defined as follows:

$$
V(X) \stackrel{\text { def. }}{=} \sum_{s \in S}(X(s)-E(X))^{2} p(s)
$$

(it follows from the definition of the expected value of the random variable ( $X-$ $E(X))^{2}$ that $\left.V(X)=E\left((X-E(X))^{2}\right)\right)$. With $(X(s)-E(X))^{2}=X(s)^{2}-$ $2 X(s) E(X)+E(X)^{2}$ and noting that the value $X(s)^{2}$ equals $X^{2}(s)$ where $X^{2}$ is the random variable that equals the square of the random variable $X$, it follows that

$$
\begin{aligned}
V(X) & =\sum_{s \in S}\left(X^{2}(s) p(s)-2 X(s) E(X) p(s)+E(X)^{2} p(s)\right) \\
& =\left(\sum_{s \in S} X^{2}(s) p(s)\right)-\left(2 E(X) \sum_{s \in S} X(s) p(s)\right)+\left(E(X)^{2} \sum_{s \in S} p(s)\right)
\end{aligned}
$$

Using the definitions of $E\left(X^{2}\right)$ and $E(X)$ and the fact that $\sum_{s \in S} p(s)=1$ we find

$$
\begin{aligned}
V(X) & =E\left(X^{2}\right)-2 E(X) E(X)+E(X)^{2} \\
& =E\left(X^{2}\right)-E(X)^{2}
\end{aligned}
$$

It follows that the variance of a random variable $X$ equals the expected value of its square minus the square of its expected value.

Standard deviation. The value $\sqrt{V(X)}$ of the squareroot of the variance is referred to as the standard deviation, for a reason that should become apparent below. The standard deviation of $X$ is often denoted by $\sigma(X)$.

Chebyshev's inequality. Let $\delta$ be some positive real number and let $\Delta$ be the event $\{s \in S:|X(s)-E(X)| \geq \delta\}$ that a random variable $X$ deviates at least $\delta$ from its expected value $E(X)$. Because $V(X)=\sum_{s \in S}(X(s)-E(X))^{2} p(s)$ can be written as

$$
V(X)=\sum_{s \in \Delta}(X(s)-E(X))^{2} p(s)+\sum_{s \in S \backslash \Delta}(X(s)-E(X))^{2} p(s)
$$

(note that " $S \backslash \Delta$ " is the same as, and a common notation for, " $S-\Delta$ ") and the second sum is non-negative, it follows that

$$
V(X) \geq \sum_{s \in \Delta}(X(s)-E(X))^{2} p(s)
$$

But $s \in \Delta$ implies that $|X(s)-E(X)| \geq \delta$ and thus that $(X(s)-E(X))^{2} \geq \delta^{2}$, so that

$$
V(X) \geq\left(\delta^{2} \sum_{s \in \Delta} p(s)\right)=\delta^{2} p(\Delta)
$$

It follows that

$$
p(\Delta) \leq V(X) / \delta^{2}
$$

and thus that

$$
p(|X(s)-E(X)| \geq \delta) \leq V(X) / \delta^{2}
$$

This is Chebyshev's inequality. With $\delta=\sigma(X)=\sqrt{V(X)}$ it becomes (if $V(X) \neq 0$ )

$$
p(|X(s)-E(X)| \geq \sigma(X)) \leq 1
$$

which is not saying much except that deviating by $\sigma(X)$ from $E(X)$ is something that should be considered to be "standard": Chebyshev's inequality provides no useful upper bound on the probability to be $\sigma(X)$ away from $E(X)$. On the other hand, Chebyshev's inequality also tells us that being "two (or four) standard deviations away from the expected value" (take $\delta=2 \sigma(X)$ (or $\delta=4 \sigma(X)$ ) ) has a probability of at most $25 \%\left(=\frac{1}{4}\right)$ (or $6.25 \%\left(=\frac{1}{16}\right)$ ), which may be useful.

Applying Chebyshev's inequality to the binomial distribution. To be able to use Chebyshev's inequality to get an idea of, for instance, the deviations from the expected value that may be expected when Bernoulli trials are conducted we have to calculate the variance. For $n$ Bernoulli trials with probability $p$ of success (per trial) and with $X$ counting the number of successes among them (and using $\left.V(X)=E\left(X^{2}\right)-E(X)^{2}\right)$ we have to calculate $E\left(X^{2}\right)=\sum_{k=0}^{n} k^{2}\binom{n}{k} p^{k}(1-p)^{n-k}$ (assuming the trials are independent). This is a simple matter: write the sum as

$$
E\left(X^{2}\right)=\sum_{k=0}^{n} k(k-1)\binom{n}{k} p^{k} q^{n-k}+\sum_{k=0}^{n} k\binom{n}{k} p^{k} q^{n-k}
$$

where $q=1-p$, and conclude that $E\left(X^{2}\right)=p^{2} n(n-1)+n p=n^{2} p^{2}+n p(1-p)=$ $n^{2} p^{2}+n p q$ so that $V(X)=E\left(X^{2}\right)-E(X)^{2}=n^{2} p^{2}+n p q-n^{2} p^{2}=n p q$.

For $n$ independent Bernoulli trials with $n=100, p=\frac{1}{4}$ and (thus) $q=\frac{3}{4}$, we have that the expected number of successes is $n p=\frac{100}{4}=25$, and that the variance is $n p q=\frac{100 \cdot 3}{4 \cdot 4}=18.75$. It follows that the standard deviation is $\sqrt{18.75}$ which is approximately equal to 4.33 and thus that the probability to find more than 33 or fewer than 17 successes is less than $25 \%$. These estimates may be compared to what we would find using Markov's inequality applied to the same $n=100$ independent Bernoulli trials with probability $p=\frac{1}{4}$ of success per trial: $p(X(s) \geq 33)=p\left(X(s) \geq \frac{33}{25} \cdot 25\right) \leq \frac{25}{33} \approx 0.758$, i.e., more than $75 \%$.

For $n=100$ fair coin tosses (so $p=q=\frac{1}{2}$ ) we have that $n p=50$ and $n p q=25$, so the standard deviation is $\sqrt{25}=5$, and the probability to find at least 70 or at most 30 times tails is less than $\frac{1}{16}$. This result is quite a bit more informative than what would follow from Markov's inequality: with $M=\frac{7}{5}$ we find that $p(X(s) \geq 70)=p\left(X(s) \geq \frac{7}{5} \cdot 50\right) \leq \frac{5}{7}$.

Expected values are always additive (and linear; mentioned but not proved during the lecture). Let $X_{1}, X_{2}, \ldots, X_{\ell}$ be any collection of $\ell$ random variables on a set of outcomes $S$, then $X=\sum_{i=1}^{\ell} X_{i}$ is defined as the random variable on $S$ that equals the sum of the functions $X_{i}$, thus, $X(s)=\sum_{i=1}^{\ell} X_{i}(s)$.

Using the definition $E(X)=\sum_{s \in S} p(s) X(s)$ (this time around using the alternative version $E(X)=\sum_{x \in X(S)} p(X=x) x$ is more cumbersome: see the solution to this week's first exercise) it follows that

$$
\begin{aligned}
E(X) & =\sum_{s \in S} p(s) X(s) \\
& =\sum_{s \in S} p(s) \sum_{i=1}^{\ell} X_{i}(s) \\
& =\sum_{s \in S} \sum_{i=1}^{\ell} p(s) X_{i}(s) \text { (now swap the summations:) } \\
& =\sum_{i=1}^{\ell} \sum_{s \in S} p(s) X_{i}(s) \text { (make sure you understand this can be done!) } \\
& \left.=\sum_{i=1}^{\ell} E\left(X_{i}\right) \text { (using the definition of } E\left(X_{i}\right)\right) .
\end{aligned}
$$

In an equally straightforward fashion it follows that for any real constants $a, b$ it is the case that the random function $a X+b$ has expected value $a E(X)+b$ (the proof uses the fact that the distribution on $X$ is a probability distribution).

Example of additivity of expected values. As an application of this "additive" property of the expected value, the expected value when rolling a single die is $\frac{7}{2}$ (this follows from $\left.\frac{1}{6}(1+2+3+4+5+6)=\frac{21}{6}=\frac{7}{2}\right)$, so the expected value of the sum of rolling two dice is $\frac{7}{2}+\frac{7}{2}=7$ : this is an easier way to derive this result than we have seen before (on page 8 of the November 30 lecture notes). Similarly, with $X_{i}$ counting the number of successes of the $i$-th of $n$ identical Bernoulli trials (thus $\left.X_{i} \in\{0,1\}\right)$ with success probability $p$ per trial, $E\left(X_{i}\right)=0 \cdot(1-p)+$ $1 \cdot p=p$, and thus (using $X=\sum_{i=1}^{n} X_{i}$ as above, with $\ell$ replaced by $n$ ), the expected number of successes of $n$ trials is $\sum_{i=1}^{n} p=n p$. This holds whether the $n$ trials are independent or not, and it does not rely on the fact that, if the $n$ trials are mutually independent, $p(X=k)=\binom{n}{k} p^{k} q^{n-k}$.

Check out the "hat check problem" in the book for a nice application of the linearity of expectations: it turns a nasty calculation into a completely trivial one.

Variances are in general not additive. Although the computation of $V(X)$ is relatively painless (if the expected values of $X$ and $X^{2}$ are known or easy to calculate), it would in general be convenient to have more tools at our disposal to compute $V(X)$. For instance, the random variable $X$ counting the number of successes of $n$ Bernoulli trials can be seen as the sum of $n$ random variables $X_{i}$, where $X_{i}$ counts the number of successes of the $i$-th of the $n$ Bernoulli trials. It was seen above that $E(X)=\sum_{i=1}^{n} E\left(X_{i}\right)$ so the obvious question arises if a similar additive property holds for the variance. Given that $E\left(X_{i}^{2}\right)=0^{2} \cdot q+1^{2} \cdot p=p$ for a single Bernoulli trial, it follows that $V\left(X_{i}\right)=E\left(X_{i}^{2}\right)-E\left(X_{i}\right)^{2}=p-p^{2}=p(1-p)=$ $p q$ : combined with the earlier calculation that $V(X)=n p q$ (assuming that the $n$ trials are independent) it is seen that indeed $V(X)=\sum_{i=1}^{n} V\left(X_{i}\right)$, suggesting that some type of additive property may indeed hold for the variance.

Considering this in full generality, let $X$ and $Y$ be any two random variables on some $S$. We know that $E(X+Y)=E(X)+E(Y)$, but what can be said about $V(X+Y)$ versus $V(X)+V(Y)$ ? Clearly nothing: just take $Y=-X$ for any non-zero random variable with $V(X) \neq 0$. Then $E(Y)=-E(X)$ but $E\left(Y^{2}\right)=E\left((-X)^{2}\right)=$ $E\left(X^{2}\right)$ and $E(Y)^{2}=E(X)^{2}$, thus $V(Y)=E\left(Y^{2}\right)-E(Y)^{2}=E\left(X^{2}\right)-E(X)^{2}=$ $V(X)$ and thus $V(X)+V(Y)=2 V(X) \neq 0$; but $V(X+Y)=V(0)=0$, so additivity of the variance does in general not hold. (Note that, on the other hand, due to $E(X+Y)=E(0)=0$ and $E(X)+E(Y)=E(X)+E(Y)=E(X)-E(X)=0$ the additive property of the expected values does not break down - indeed, this property was proved to hold under all circumstances).

As shown below, the additivity of the variance breaks down in our example because the value of $Y$ is implied by the value of $X$ : clearly $X$ and $Y$ are not independent, for any reasonable notion of independence of random variables (which has not been defined yet). The lack of independence of $X$ and $Y$ is indeed the reason why the additivity does not hold. This becomes obvious when looking at the calculation of $E\left((X+Y)^{2}\right)$ (which is relevant because $V(X+Y)=E((X+$ $\left.\left.Y)^{2}\right)-E(X+Y)^{2}\right)$. Because due to additivity and linearity of expected values

$$
E\left((X+Y)^{2}\right)=E\left(X^{2}+2 X Y+Y^{2}\right)=E\left(X^{2}\right)+2 E(X Y)+E\left(Y^{2}\right)
$$

and

$$
E(X+Y)^{2}=(E(X)+E(Y))^{2}=E(X)^{2}+2 E(X) E(Y)+E(Y)^{2}
$$

we find that

$$
\begin{aligned}
V(X+Y) & =E\left((X+Y)^{2}\right)-E(X+Y)^{2} \\
& =E\left(X^{2}\right)+2 E(X Y)+E\left(Y^{2}\right)-E(X)^{2}-2 E(X) E(Y)-E(Y)^{2} \\
& =E\left(X^{2}\right)-E(X)^{2}+E\left(Y^{2}\right)-E(Y)^{2}+2 E(X Y)-2 E(X) E(Y) \\
& =V(X)+V(Y)+2(E(X Y)-E(X) E(Y))
\end{aligned}
$$

It follows that

$$
\begin{equation*}
V(X+Y)=V(X)+V(Y) \text { if and only if } E(X Y)=E(X) E(Y) \text {. } \tag{1}
\end{equation*}
$$

Thus, we find that additivity of the variance hinges on multiplicativity of expected values. It is discussed below under what circumstances the expected value is indeed multiplicative.

Expected values are in general not multiplicative. Given that, for random variables $X$ and $Y$ on $S$, it is the case that $E(X+Y)=E(X)+E(Y)$ no matter
what, i.e., irrespective of independencies or dependencies of the underlying probability distributions, it would be nice (as argued above - for instance, it would make the variance additive) if expected values are "multiplicative" as well, i.e., if $E(X Y)=E(X) E(Y)$, where the random variable $Z=X Y$ is defined as $Z(s)=$ $X(s) Y(s)$ for $s \in S$; thus $Z(S)=\{z: z=x y \wedge \exists s \in S(X(s)=x \wedge Y(s)=y)\}$.

In general, however, this multiplicative property does not hold. As a trivial example, consider a fair coin toss with outcome heads or tails, and the random variables $X$ and $Y$ on \{heads, tails $\}$ such that $X$ (heads $)=1, X$ (tails) $=0, Y$ (heads $)=0$, and $Y$ (tails) $=1$. It follows that $X^{2}=X$ (check this using the definition), that $Y=1-X$ so that $X+Y=1$, and that $X Y=X(1-X)=X-X^{2}=X-X=0$. Then $E(X)=0 \cdot p(X=0)+1 \cdot p(X=1)=\frac{0}{2}+\frac{1}{2}=\frac{1}{2}, E(Y)=0 \cdot p(Y=$ $0)+1 \cdot p(Y=1)=\frac{0}{2}+\frac{1}{2}=\frac{1}{2}$, and indeed $E(X+Y)=E(X+1-X)=E(1)=$ $1=\frac{1}{2}+\frac{1}{2}=E(X)+E(Y)$, but $E(X Y)=E(0)=0 \neq \frac{1}{4}=\frac{1}{2} \frac{1}{2}=E(X) E(Y)$.

Expected values of independent random variables are multiplicative. Although in general it is not the case that $E(X Y)=E(X) E(Y)$, this multiplicative property holds if the random variables involved are independent, i.e., if $\forall x \in X(S) \forall y \in Y(S)$ it is the case that $p(X=x \wedge Y=y)=p(X=x) p(Y=y)$. To prove that $E(X Y)=E(X) E(Y)$, first use the definition of the expected value to write $E(X Y)=\sum_{r \in X Y(S)} r p(X Y=r)$ and then use that

$$
r p(X Y=r)=\sum_{\substack{r_{1} \in X(S), r_{2} \in Y(S) \\ \text { such that } r_{1} r_{2}=r}} r_{1} r_{2} p\left(X=r_{1} \wedge Y=r_{2}\right)
$$

for $r \in X Y(S)$, so that

$$
\begin{aligned}
E(X Y) & =\sum_{r \in X Y(S)}\left(\sum_{\substack{r_{1} \in X(S), r_{2} \in Y(S) \\
\text { such that } r_{1} r_{2}=r}} r_{1} r_{2} p\left(X=r_{1} \wedge Y=r_{2}\right)\right) \\
& =\sum_{r_{1} \in X(S), r_{2} \in Y(S)} r_{1} r_{2} p\left(X=r_{1} \wedge Y=r_{2}\right) .
\end{aligned}
$$

This explains the first step of the proof given in the book (Theorem 5 on page 486 of the online 7th edition, page 471/472 of the printed global 7th edition, and page 512 of the 8th edition); the remainder of the proof is fully explained in the book.

Note that for the example directly above the property $\forall x \in X(S) \forall y \in Y(S) p(X=$ $x \wedge Y=y)=p(X=x) p(Y=y)$ is violated, because the negation holds: $\exists x \in$ $X(S) \exists y \in Y(S) p(X=x \wedge Y=y) \neq p(X=x) p(Y=y)$ is true because $p(X=1 \wedge Y=1)=0$ whereas $p(X=1) p(Y=1)=\frac{1}{2} \frac{1}{2}=\frac{1}{4}$.

Variances of independent random variables are additive. This statement now follows from statement (1) combined with the multiplicativity of the expected values under the independence condition.

The result that the random variable $X$ that counts the number of successes among $n$ independent Bernoulli trials (each with success and failure probabilities $p$ and $q=1-p$, respectively) has variance $V(X)=n p q$ can now be derived directly, as suggested above, from the fact that a single such Bernoulli trial has variance $p q$.

## Useful to remember:

The most important take away messages are that

$$
E(X+Y)=E(X)+E(Y) \text { is always true }
$$

but that

$$
V(X+Y)=V(X)+V(Y) \text { is not necessarily the case. }
$$

## Loose ends

Geometric distribution. Suppose an experiment has probability $p$ of success (and complementary probability $q=1-p$ of failure); how many experiments do we expect to carry out until a successfull one? One experiment suffices with probability $p$, the number of experiments equals two with probability $q p$, three with probability $q^{2} p$, etc., and the number of experiments equals $k$ with probability $q^{k-1} p$. Let $X$ be the random variable that equals the number of experiments until success, then $p(X=k)=q^{k-1} p$ for integers $k \geq 1$ : this is called the geometric distribution. Of course it must be checked that this is actually a probability distribution, i.e., that $\left(\sum_{k=1}^{\infty} p(X=k)\right)=1$ and that $0 \leq p(X=k) \leq 1$ for all $k \geq 1$ : the two bounds are obvious and the sum follows from $\sum_{k=1}^{\infty} q^{k-1} p=p \sum_{\ell=0}^{\infty} q^{\ell}=\frac{p}{1-q}=\frac{p}{p}=1$.

The expected value $E(X)$ of $X$ is $\sum_{i=0}^{\infty} i \cdot p(X=i)=\sum_{i=0}^{\infty} i q^{i-1} p$. We know that $\sum_{i=0}^{\infty} r^{i}=\frac{1}{1-r}$ for $|r|<1$, so taking the derivative it is found that $\sum_{i=0}^{\infty} i r^{i-1}=$ $\frac{1}{(1-r)^{2}} ;$ it follows that $\sum_{i=0}^{\infty} i q^{i-1}=\frac{1}{(1-q)^{2}}=\frac{1}{p^{2}}$ so that $E(X)=\sum_{i=0}^{\infty} i q^{i-1} p=$ $p \sum_{i=0}^{\infty} i q^{i-1}=\frac{p}{p^{2}}=\frac{1}{p}$. However, this relies on the validity of the step where the derivative is taken (of an infinite series); this is indeed valid, but the same result can be obtained directly too, in the following manner ${ }^{1}$. Let $R=\sum_{i=0}^{\infty} i r^{i-1}$. Because $R=\sum_{i=1}^{\infty} i r^{i-1}=\left(\sum_{i=1}^{\infty}(i-1) r^{i-1}\right)+\left(\sum_{i=1}^{\infty} r^{i-1}\right)=\left(\sum_{\ell=0}^{\infty} \ell r^{\ell}\right)+$ $\left(\sum_{\ell=0}^{\infty} r^{\ell}\right)=r\left(\sum_{\ell=0}^{\infty} \ell r^{\ell-1}\right)+\frac{1}{1-r}=r\left(\sum_{i=0}^{\infty} i r^{i-1}\right)+\frac{1}{1-r}=r R+\frac{1}{1-r}$ it is found that $R(1-r)=\frac{1}{1-r}$ so that $R=\frac{1}{(1-r)^{2}}$.

The variance of the geometric distribution equals $\frac{q}{p^{2}}$. Examples of applications of the geometric distribution can be found below (first solution for $n=4$, and for any $n$ that has a prime factor $>3$ ).

Using a die to make random choices. Given an arbitrary integer $n>0$ and a fair die, how does one select an integer $r$ with $0 \leq r<n$ at random? According to the definition of at random this means that each $r$ must have the same probability of $\frac{1}{n}$ to be selected. Below a few simple examples are given to illustrate the general principle how this problem may be approached; more examples will be given in the exercises (and solutions).

$n=2$ : the single bit that is necessary and sufficient is provided by the parity of the result of rolling a die once. The number of times the die must be rolled is 1 (this is the maximum and the expected value as well).

$n=3$ : the single random value in $\{0,1,2\}$ that is necessary and sufficient is provided by subtracting 1 or 4 from the result $s$ of rolling a die once: $s-1$ if $s \in\{1,2,3\}$ or $s-4$ if $s \in\{4,5,6\}$. The number of times the die must be rolled is 1 (this is the maximum and the expected value as well).

One could also wait until the result $s$ is in $\{1,2,3\}$ and then take $s-1$, but in that case the expected number of times the die must be rolled is 2 (because it becomes a geometric distribution with probability of success $\frac{1}{2}$ ); note that in this case no maximum can be given for the number of times the die must be rolled.

$n=4$ : The same approach as in the previous paragraph (but this time waiting until $s \in\{1,2,3,4\})$ leads to an expected number of rolls of $\frac{3}{2}$ (geometric[^0]distribution with probability of success $\frac{2}{3}$ ), and again with no maximum on the number of rolls.

A more efficient approach is to use $s-1$ as above when $s \in\{1,2,3,4\}$ and to keep the bit $s-5 \in\{0,1\}$ if $s \in\{5,6\}$; in the latter case a second roll then suffices to find the second bit required. This implies that two rolls always suffice, that two rolls are required with probability $\frac{1}{3}$, but that one rolls suffices with probability $\frac{2}{3}$. Using the formula for the expected value of the number of rolls, the expected number of rolls becomes $1 \cdot \frac{2}{3}+2 \cdot \frac{1}{3}=\frac{4}{3}$ (and will never be more than 2), which is less than the earlier $\frac{3}{2}$ (for which there is no maximum on the number of rolls). Note that despite the fact that a die has six different outcomes, and six is greater than the required four, there is no way to get a fair choice that is guaranteed to require just a single roll.

Make sure that it is decided before the die will be rolled, which role will be played by which bit in case $s \in\{5,6\}$ (i.e., if the "second" bit is the most significant or the least significant bit of the two bits that must be selected). $n=5$ : As above, use $s-1$ when $s \in\{1,2,3,4,5\}$, and roll again if $s=6$ : the expected number of rolls if $\frac{6}{5}$ (because it is a geometric distribution) and there is no maximum on the number of rolls.

In this case nothing can be "rescued" from the bad luck case $s=6$ : all one can do is roll again. Note that this is the smallest $n$ for which there is no maximum on the number of rolls. This is due to the fact that 5 is the smallest integer that has a prime factor that does not divide 6: in general (and when using a fair die), a maximum number of rolls can be guaranteed if and only if $n$ has only factors 2 or 3 .

$n=6$ : just take $s-1$ where $s$ is the outcome of a single roll of the die; the die must be rolled just once.

$n=7$ : roll the die twice, with first outcome $s_{1} \in\{1,2,3,4,5,6\}$ of the first roll and outcome $s_{2} \in\{1,2,3,4,5,6\}$ of the second roll. Then $s=6\left(s_{1}-\right.$ $1)+\left(s_{2}-1\right)$ is a random number in the range $\{0,1, \ldots, 35\}$, and $r=$ $s \bmod 7 \in\{0,1,2,3,4,5,6\}$, the remainder of $s$ upon division by 7 , has an almost uniform distribution: $r=0$ occurs with probability $\frac{6}{36}$ and all other $r$-values occur with probability $\frac{5}{36}$ each. To fix this imbalance (in order to make the distribution uniform), "remove" one of the possibilities that leads to $r=0$, for instance $s_{1}=s_{2}=6$, by rolling both dice again (ordered!) if that possibility occurs. Overall, the expected number of rolls becomes $2 \cdot \frac{36}{35}$, and there is no maximum for the number of rolls required.

Note that it would not be correct to reroll only one of the dice if failure occurs $\left(s_{1}=s_{2}=6\right.$ above), say the second one resulting in $\overline{s_{2}}$, and to use the old $s_{1}$-value along with the new value $\overline{s_{2}}$ to compute the random number $6\left(s_{1}-1\right)+\left(\overline{s_{2}}-1\right)$ in the range $\{0,1, \ldots, 35\}$. Why?

$n \geq 8$ : Try to figure out how to "optimally" solve the cases $8 \leq n \leq 12$ (optimal with respect to the smallest expected number of rolls).

$n=31$ : During the lecture we considered the case $n=31$, but shifted our target range from $\{0,1,2, \ldots, 30\}$ to $\{1,2,3, \ldots, 31\}$. Rolling a die twice results in two outcomes, a first outcome $r_{1}$ and a second outcome $r_{2}$, both uniformly distributed over $\{1,2,3,4,5,6\}$. It follows that $r=6\left(r_{1}-1\right)+r_{2}$ is uniformly distributed over $\{1,2,3, \ldots, 36\}$. If $r \leq 31$ we are done (with probability $\frac{31}{36}$ ), else we repeat (with probability $\left.\frac{5}{36}\right)$. It follows from the geometric distribution that on average we need $2 \cdot\left(\frac{31}{36}\right)^{-1}=\frac{72}{31}$ rolls. To find the probability that a particular result $s \in\{1,2,3, \ldots, 31\}$ is obtained, it is found with probability $\frac{1}{36}$ after the first two rolls, then with probability
$\frac{5}{36} \frac{1}{36}$ as a result of the second attempt (namely, probability $\frac{5}{36}$ that a second attempt is necessary and probability $\frac{1}{36}$ that it is found during the second attempt), etc., with probability $\left(\frac{5}{36}\right)^{i-1} \frac{1}{36}$ as a result of the $i$-th attempt, accumulating to a probability $\frac{1}{36} \sum_{j=0}^{\infty}\left(\frac{5}{36}\right)^{j}=\frac{1}{36} \frac{1}{1-\frac{5}{36}}=\frac{1}{31}$, as desired: it follows that the result is uniformly distributed over $\{1,2,3, \ldots, 31\}$.

Replacing the die by a coin: Replacing the fair die by a fair coin with only two possible outcomes, try to figure out how to "optimally" find a random number in $\{0,1,2, \ldots, n-1\}$ for $2 \leq n \leq 12$ (optimal with respect to the smallest expected number of coin tosses).

Next class. We will briefly discuss the birthday paradox and then move to advanced counting. Read section 8.1, (very) quickly glance through section 8.2 , glance through section 8.3 with a bit more attention, and of section 8.4 try to digest "Introduction", "Useful facts about power series", and "Using generating functions to solve recurrence relations", taking note of the existence of Table 1 and its useful contents - some entries you should already be familiar with - while skipping (seventh edition only) "Exponential generating functions" and "Proving identities via generating functions".


[^0]:    ${ }^{1}$ Another way to derive this result can be found on page 5 of the October 16 lecture notes.

