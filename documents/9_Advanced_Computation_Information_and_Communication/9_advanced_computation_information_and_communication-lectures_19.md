## Overview of the basics of discrete probability theory

Laplace's definition. Given a finite, non-empty set $S$, suppose there is a procedure that each time it is performed results in a single, arbitrary element of $S$ without giving preference to any element of the set above any other element of the set. Such a procedure is referred to as an experiment, the set $S$ is called the sample space of the experiment, the resulting element the outcome, any $E \subseteq S$ is called an event, and $p(E)=\frac{|E|}{|S|}$ is defined as the probability of $E$ (to occur under the given experiment).

## Simple examples.

- For any finite subset $S \subset \mathbf{Z}$ and positive integer $d$, let $E_{d}(S)=\{s \in S: d \mid s\}$ be the subset of $S$ that consists of the elements of $S$ that are divisible by $d$, and let $E_{d}=E_{d}(S)$ when $S$ is clear from the context. With $S=\{1,2,3,4,5,6\}$ representing the possible outcomes of rolling a fair die once and $E_{2}=\{2,4,6\}$ the subset of even elements of $S$, the probability of rolling an even number is $p\left(E_{2}\right)=\frac{\left|E_{2}\right|}{|S|}=\frac{3}{6}=\frac{1}{2}$. With $E_{3}=\{3,6\}$ the subset of elements of $S$ that are divisible by three, the probability of getting an outcome that is divisible by three is $p\left(E_{3}\right)=\frac{\left|E_{3}\right|}{|S|}=\frac{2}{6}=\frac{1}{3}$. - Similarly, with the experiment consisting of rolling a die until the outcome is $>3$ and thus considering the set of outcomes $T=\{4,5,6\}$, the probability of getting an even outcome becomes $p\left(E_{2}(T)\right)=\frac{\left|E_{2}(T)\right|}{|T|}=\frac{2}{3}$ (because $E_{2}(T)=\{4,6\}$ ), and an outcome that is divisible by three is obtained with probability $p\left(E_{3}(T)\right)=\frac{\left|E_{3}(T)\right|}{|T|}=$ $\frac{1}{3}$ (because $\left.E_{3}(T)=\{6\}\right)$.
- With $S=\{1,2,3,4,5,6\}$ as above and $E_{d}=E_{d}(S)$, the definition $p(E)=\frac{|E|}{|S|}$ immediately leads to the probability $p\left(\overline{E_{3}}\right)=1-p\left(E_{3}\right)=\frac{2}{3}$ for the complementary event $\overline{E_{3}}=S-E_{3}$ to occur, because $\left|\overline{E_{3}}\right|=|S|-\left|E_{3}\right|=6-2=4$ so that $p\left(\overline{E_{3}}\right)=\frac{\left|\overline{E_{3}}\right|}{|S|}=\frac{4}{6}=\frac{2}{3}=\frac{|S|-\left|E_{3}\right|}{|S|}=1-p\left(E_{3}\right)$. Similarly, with $\overline{E_{2}}=S-E_{2}$ and $\left|\overline{E_{2}}\right|=|S|-\left|E_{2}\right|$ we get $p\left(\overline{E_{2}}\right)=\frac{\left|\overline{E_{2}}\right|}{|S|}=\frac{|S|-\left|E_{2}\right|}{|S|}=1-p\left(E_{2}\right)=\frac{1}{2}$.
- In the same notation (and thus in $S$ ), with $\left|E_{2} \cup E_{3}\right|=\left|E_{2}\right|+\left|E_{3}\right|-\left|E_{2} \cap E_{3}\right|$, and $E_{2} \cap E_{3}=\{6\}$ so that $\left|E_{2} \cap E_{3}\right|=1$ and thus $p\left(E_{2} \cap E_{3}\right)=\frac{1}{6}$, it is found
that $p\left(E_{2} \cup E_{3}\right)=\frac{\left|E_{2} \cup E_{3}\right|}{|S|}=\frac{\left|E_{2}\right|+\left|E_{3}\right|-\left|E_{2} \cap E_{3}\right|}{|S|}=p\left(E_{2}\right)+p\left(E_{3}\right)-p\left(E_{2} \cap E_{3}\right)=$ $\frac{1}{2}+\frac{1}{3}-\frac{1}{6}=\frac{2}{3}$.

Similarly, with $T=\{4,5,6\}$ as above, it is found that $p\left(E_{2}(T) \cup E_{3}(T)\right)=$ $p\left(E_{2}(T)\right)+p\left(E_{3}(T)\right)-p\left(E_{2}(T) \cap E_{3}(T)\right)=p\left(E_{2}(T)\right)+p\left(E_{3}(T)\right)-p\left(E_{3}(T)\right)=$ $p\left(E_{2}(T)\right)=\frac{2}{3}$ and, with $U=\{1,2,3,4\}$, that $p\left(E_{2}(U) \cup E_{3}(U)\right)=p\left(E_{2}(U)\right)+$ $p\left(E_{3}(U)\right)-p\left(E_{2}(U) \cap E_{3}(U)\right)=\frac{2}{4}+\frac{1}{4}-\frac{0}{4}=\frac{3}{4}$ (because $E_{2}(U)=\{2,4\}$ and $E_{3}(U)=\{3\}$ so that $\left|E_{2}(U)\right|=2,\left|E_{3}(U)\right|=1$ and $E_{2}(U) \cap E_{3}(U)=\emptyset$ and thus $p\left(E_{2}(U)\right)=\frac{2}{4}, p\left(E_{3}(U)\right)=\frac{1}{4}$ and $\left.p\left(E_{2}(U) \cap E_{3}(U)\right)=\frac{0}{4}\right)$.

Hands of poker. When playing poker with a regular deck of 52 distinct cards (consisting of 4 distinct suits with each suit containing the same 13 kinds) the sample space $S$ consists of all 5 -hands of poker, i.e., the 5 -combinations from a 52-set without replacement. It follows that $|S|=\binom{52}{5}=2598960$ where each of the possible $\binom{52}{5}$ outcomes is unique.

Given $|S|$, Laplace's definition can now be used to compute the probabilities of hands of cards. For instance, if $E$ is the event to get "four of a kind" (note that five of a kind is impossible, because each kind occurs only four times in the deck of cards), we find from $|E|=624$ (see earlier lectures and exercises) that the probability of obtaining four of a kind is $\frac{624}{2598960}$, which is close to 0.00024 , i.e., $0.024 \%$.

The need for a more general definition of probabilities. The above definition of probabilities defined as $\frac{k}{|S|}$ for integers $k$ and with $|S|$ the cardinality of the set of possible outcomes, is too restrictive for many common examples. For instance, define the outcome of an experiment as the sum of the results of throwing two dice (or throwing one die twice). Because the smallest result of a die-throw is 1 and the largest result is 6 , the set of outcomes is $S=\{2,3,4,5,6,7,8,9,10,11,12\}$ with $|S|=11$. To analyse the probabilities, consider the sums of the elements of the 36 ordered pairs ${ }^{1}(i, j)$ of results, each pair occurring with probability $\frac{1}{36}$ :

- outcome 2 (i.e., sum 2 ) occurs only for ordered pair $(1,1)$ and thus occurs with probability $\frac{1}{36}$.
- outcome 3 (i.e., sum 3 ) occurs for ordered pairs $(1,2)$ and $(2,1)$ and thus occurs with probability $\frac{1}{36}+\frac{1}{36}=\frac{1}{18}$.
- outcome 4 (i.e., sum 4$)$ occurs for ordered pairs $(1,3),(2,2)$ and $(3,1)$ and thus occurs with probability $\frac{1}{36}+\frac{1}{36}+\frac{1}{36}=\frac{1}{12}$.
- outcome 5 (i.e., sum 5 ) occurs for ordered pairs $(1,4),(2,3),(3,2)$ and $(4,1)$ and thus occurs with probability $\frac{1}{36}+\frac{1}{36}+\frac{1}{36}+\frac{1}{36}=\frac{1}{9}$.
- ... (finish this calculation and show that the resulting probabilities add up to 1) $\ldots$

Note that in none of these probabilities the number 11 of elements of $S$ plays a role.

Another example, not done in class, considers the ordered pairs of integers $(i, j)$ with $1 \leq i, j \leq 6$ resulting from two consecutive throws with a die (where each of the 36 distinct pairs indeed occurs with probability $\frac{1}{36}$, i.e., the above definition does apply), versus the example of unordered pairs $(i, j)$ of integers $1 \leq i \leq j \leq$ 6 resulting from simultaneously throwing two indistinguishable dice (so that, if distinct $i$ and $j$ are thrown, it cannot be distinguished which of the dice resulted in $i$ and which in $j$ ). For the latter, there are still 36 ways the pair of dice can be thrown, but only 21 distinct outcomes can be distinguished: 6 where $i=j$ and[^0]

15 where $i \neq j$ (because $36-6=30$ of the ordered pairs $(i, j)$ have $i \neq j$, which are indistinguishable as unordered pairs and thus result in $\frac{30}{2}$ distinct outcomes (as unordered pairs) with $i \neq j$; the number 21 can also be obtained as the number of 2-combinations from a 6 -set with replacement, which is $\left.\binom{6+2-1}{2}=\binom{7}{2}=21\right)$. Thus, this latter example results in a sample space $S$ with $|S|=21$. But analyzing the probabilities of the distinct outcomes, none can be expressed as $\frac{k}{|S|}$ for integers $k$ : indeed each of the 6 unordered pairs $(i, i)$ occurs with probability $\frac{1}{36}$, whereas each of the 15 unordered pairs $(i, j)$ with $1 \leq i<j \leq 6$ occurs with probability $\frac{2}{36}=\frac{1}{18}$. Note that $6 \cdot \frac{1}{36}+15 \cdot \frac{1}{18}=1$ so that there are no unaccounted for probabilities.

At the next lecture it will be seen how the above two examples can be handled more elegantly using a random variable. For the moment it suffices to know that the simple-minded probability definition $p(E)=\frac{|E|}{|S|}$ is too restrictive and that a more flexible definition of probability (than Laplace's definition given above) is required. This is achieved by the definition in the next paragraph.

Probability distribution. Given any non-empty countable set $S$ of outcomes a probability distribution on $S$ is any function $p: S \rightarrow \mathbf{R}$ such that $\forall s \in S 0 \leq$ $p(s) \leq 1$ and $\sum_{s \in S} p(s)=1$. Given any $F \subseteq S$ the probability of the event $F$ is then defined as $p(F)=\sum_{s \in F} p(s)$. Complementarity and union work as seen earlier: $p(\bar{F})=1-p(F)$ and $p\left(F_{1} \cup F_{2}\right)=p\left(F_{1}\right)+p\left(F_{2}\right)-p\left(F_{1} \cap F_{2}\right)$; check this.

For the example with a sample space consisting of 21 unordered pairs $(i, j)$ with $1 \leq i \leq j \leq 6$ it now suffices to define $p((i, j))=\frac{1}{18}$ for the fifteen pairs $(i, j)$ with $1 \leq i<j \leq 6$ and $p((i, i))=\frac{1}{36}$ for the remaining six pairs $(i, i)$ with $1 \leq i \leq 6$ (as seen earlier all probabilities sum to one). For the "sum-example" with $|S|=11$, we simply define $p(7-i)=\frac{6-|i|}{36}$ for $-5 \leq i \leq 5$ (or equivalently, if you prefer, $p(2)=p(12)=\frac{1}{36}, p(3)=p(11)=\frac{1}{18}, p(4)=p(10)=\frac{1}{12}, p(5)=p(9)=\frac{1}{9}$, $p(6)=p(8)=\frac{5}{36}$, and $\left.p(7)=\frac{1}{6}\right)$.

For more examples, you may want to derive the probability distributions for the maximum of two dice (which is yet another nice introduction to random variables, as will be discussed later), or for the outcome of three (or more) indistinguishable dice thrown simultaneously.

Uniform distribution, selection at random. The original definition of the probability $p(E)$ of an event $E \subseteq S$ (for a finite, non-empty set $S$ ) as $\frac{|E|}{|S|}$ corresponds to the special case of a uniform distribution where for each element $s \in S$ it is the case that $p(s)=\frac{1}{|S|}$ (and thus $p(s)=\frac{1}{n}$ if $|S|=n$ ). Selecting elements according to the uniform distribution is also referred to as selecting elements at random.

Note that the probability distribution of the sum of two dice is not (at all) uniform, but that the probability distribution of ordered pairs $(i, j)$ with $1 \leq i, j \leq 6$ resulting from two consecutive throws of a single die (or simultaneously throwing two distinguishable dice) is uniform.

Combining probabilities. For two events $A, B$ it is the case that $p(A \cup B)=$ $p(A)+p(B)-p(A \cap B)$ so that, with $\forall s \in S p(s) \geq 0$,

$$
\begin{equation*}
p(A \cup B) \leq p(A)+p(B) \tag{1}
\end{equation*}
$$

With induction the union bound (also known as Boole's inequality) follows: given some non-empty finite sample space $S$ and events $F_{i} \subseteq S$ for $1 \leq i \leq \ell$, then $p\left(\bigcup_{i=1}^{\ell} F_{i}\right) \leq \sum_{i=1}^{\ell} p\left(F_{i}\right)$

Note that

$$
\begin{equation*}
\text { if } A \cap B=\emptyset \text { then } p(A \cup B)=p(A)+p(B) \tag{2}
\end{equation*}
$$

Here it was used that $p(A \cap B)=0$ if $A \cap B=\emptyset$.

But what can be said about $p(A \cap B)$ if $A \cap B \neq \emptyset$ ? It would be nice (and depending on the circumstances intuitively correct) to just be able to say that $p(A \cap B)=p(A) p(B)$ : this may indeed be the case (as in the first example below), but in general it is incorrect (as in the second and third example below):

(1) $S=\{1,2,3,4,5,6\}$

$E_{2}(S)=\{2,4,6\}$ so $p\left(E_{2}(S)\right)=\frac{1}{2} ; E_{3}(S)=\{3,6\}$ so $p\left(E_{3}(S)\right)=\frac{1}{3}$;

$E_{2}(S) \cap E_{3}(S)=\{6\}$ so $p\left(E_{2}(S) \cap E_{3}(S)\right)=\frac{1}{6}=\frac{1}{2} \cdot \frac{1}{3}=p\left(E_{2}(S)\right) p\left(E_{3}(S)\right)$.

(2) $T=\{4,5,6\}$;

$E_{2}(T)=\{4,6\}$ so $p\left(E_{2}(T)\right)=\frac{2}{3} ; E_{3}(T)=\{6\}$ so $p\left(E_{3}(T)\right)=\frac{1}{3}$;

$E_{2}(T) \cap E_{3}(T)=\{6\}$ so $p\left(E_{2}(T) \cap E_{3}(T)\right)=\frac{1}{3} \neq \frac{2}{3} \cdot \frac{1}{3}=p\left(E_{2}(T)\right) p\left(E_{3}(T)\right)$.

(3) $U=\{1,2,3,4\}$

$E_{2}(U)=\{2,4\}$ so $p\left(E_{2}(U)\right)=\frac{1}{2} ; E_{3}(U)=\{3\}$ so $p\left(E_{3}(U)\right)=\frac{1}{4}$;

$E_{2}(U) \cap E_{3}(U)=\emptyset$ so $p\left(E_{2}(U) \cap E_{3}(U)\right)=0 \neq \frac{1}{2} \cdot \frac{1}{4}=p\left(E_{2}(U)\right) p\left(E_{3}(U)\right)$.

Intersecting events. Although, apparently, it is in general not the case that $p(E \cap F)=p(E) p(F)$ for events $E, F$ with $p(E) \neq 0 \neq P(F)$ (cf. second and third example above), and thus the case that $\frac{p(E \cap F)}{p(F)}$ is not equal to $p(E)$, we may nevertheless "hope" that $\frac{p(E \cap F)}{p(F)}$ tells us something about the event $E$, possibly in relation to the event $F$. To get some insight in this matter, consider the second example above with $T=\{4,5,6\}$ (the first example is useless here because there $\frac{p\left(E_{2}(S) \cap E_{3}(S)\right)}{p\left(E_{2}(S)\right)}=p\left(E_{3}(S)\right)$ and so is the third example because there $p\left(E_{2}(U) \cap\right.$ $\left.\left.E_{3}(U)\right)=0\right)$

Let $T=\{4,5,6\}, E_{2}(T)=\{4,6\}, E_{3}(T)=\{6\}, E_{2}(T) \cap E_{3}(T)=\{6\}$ with $p\left(E_{2}(T)\right)=\frac{2}{3}, p\left(E_{3}(T)\right)=\frac{1}{3}$, and $p\left(E_{2}(T) \cap E_{3}(T)\right)=\frac{1}{3}$ as above. Consider the quantity $\frac{p\left(E_{2}(T) \cap E_{3}(T)\right)}{p\left(E_{2}(T)\right)}=\frac{1 / 3}{2 / 3}=\frac{1}{2}$; we have seen already that this result $\frac{1}{2}$ is not equal to $p\left(E_{3}(T)\right)$ (which equals $\frac{1}{3}$ ), but does the " $\frac{1}{2}$ " tell us anything about the probability of the event $E_{3}(T)$ in relation to the event $E_{2}(T)$, as we would hope or expect to find? Indeed it does, because with $E_{2}(T)=\{4,6\}$ and $E_{3}(T)=\{6\}$ the probability of the event $E_{3}(T)$ is indeed $\frac{1}{2}$ if we assume that the sample space $T=\{4,5,6\}$ is replaced by the sample space $E_{2}(T)=\{4,6\}$.

This observation is confirmed by looking at $\frac{p\left(E_{2}(T) \cap E_{3}(T)\right)}{p\left(E_{3}(T)\right)}=\frac{1 / 3}{1 / 3}=1$; this result 1 is not equal to $p\left(E_{2}(T)\right)$ (which equals $\frac{2}{3}$ ) but it is the probability of the event $E_{2}(T)$ if the sample space $T=\{4,5,6\}$ is replaced by the sample space $E_{3}(T)=\{6\}$ : with a sample space consisting of just even elements, the probability is one to draw an even element.

Based on this very limited observation we suspect that it may be the case that the ratio $\frac{p(E \cap F)}{p(F)}$ gives us the probability of the event $E$ under the condition that the sample space is replaced by $F$ - and the resulting probability may or may not be equal to the original $p(E)$. This indeed turns out to be the case, and is captured in the definition below.

Conditional probability. Given any event $F$ with $p(F)>0$ (thus $F \subseteq S$, where $S$ is the set of outcomes, i.e., the sample space) and some event $E$, the probability that the event $E$ occurs while assuming that it is already known that the outcome belongs to the subset $F$ of the original sample space $S$, is called the "conditional probability of $E$ given $F$ ". It is denoted by $p(E \mid F)$ and is defined as

$$
\begin{equation*}
p(E \mid F)=\frac{p(E \cap F)}{p(F)} \tag{3}
\end{equation*}
$$

(assuming that $p(F)>0$ ). In principle this is a definition, so needs no further argumentation. The definition can be argued to be reasonable based on the two examples given above; also, using "the probability that the event $E$ occurs while assuming that it is already known that the outcome belongs to $F$ "', the outcome must belong to $E \cap F$, but because the sample space is "reduced" to $F$, the relevant probability $p(E \cap F)$ must be scaled by $p(F)$.

Independence. Consider $S=\{1,2,3,4,5,6\}$, the event $F=\{1,2,3\}$ with $p(F)=$ $\frac{3}{6}=\frac{1}{2}$ and the events $E_{2}=E_{2}(S)$ with $p\left(E_{2}\right)=\frac{1}{2}$ and $E_{3}=E_{3}(S)$ with $p\left(E_{3}\right)=\frac{1}{3}$ (the latter two as above). Then $p\left(E_{2} \cap F\right)=p\left(E_{3} \cap F\right)=\frac{1}{6}$ and using the definition $p(E \mid F)=\frac{p(E \cap F)}{p(F)}$ it is found that $p\left(E_{2} \mid F\right)=\frac{1 / 6}{1 / 2}=\frac{1}{3}$ and that $p\left(E_{3} \mid F\right)=\frac{1 / 6}{1 / 2}=\frac{1}{3}$. Thus the condition $F$ influences the probability that event $E_{2}$ occurs (changing the "regular" unconditional probability $p\left(E_{2}\right)=\frac{1}{2}$ to a conditional probability $\left.p\left(E_{2} \mid F\right)=\frac{1}{3}\right)$ but does not influence the probability that event $E_{3}$ occurs (the conditional probability $p\left(E_{3} \mid F\right)$ is $\frac{1}{3}$ which is the same as the "regular" unconditional probability $\left.p\left(E_{3}\right)\right)$. Although the latter does not mean that $F$ does not influence $E_{3}$ - because outcome $6 \in E_{3}$ is no longer possible under condition $F$ - we nevertheless say that $F$ and $E_{3}$ are independent events because $p\left(E_{3} \mid F\right)=p\left(E_{3}\right)$; similarly, we say that $E_{2}$ and $F$ are not independent (i.e., dependent) because $p\left(E_{2} \mid F\right) \neq p\left(E_{2}\right)$. Because of Definition (3) this independence condition $p\left(E_{3} \mid F\right)=p\left(E_{3}\right)$ is equivalent to saying that $p\left(E_{3} \cap F\right)=p\left(E_{3}\right) p(F)$; and the dependence condition $p\left(E_{2} \mid F\right) \neq p\left(E_{2}\right)$ that $E_{2}$ and $F$ are not independent is equivalent to saying that $p\left(E_{2} \cap F\right) \neq p\left(E_{2}\right) p(F)$.

One obvious next question is how one can tell if two events are independent or not. Unfortunately, there is no easy answer to that question.

Independence examples. As mentioned above the earlier events $E_{2}$ and $F$ are not independent because $\frac{1}{3}=p\left(E_{2} \mid F\right) \neq p\left(E_{2}\right)=\frac{1}{2}$, in particular $p\left(E_{2} \mid F\right)<p\left(E_{2}\right)$. On the other hand $\frac{2}{3}=p\left(\overline{E_{2}} \mid F\right)>p\left(\overline{E_{2}}\right)=\frac{1}{2}$ : so imposing a condition on an event may leave the probability of the event unchanged (in case of independence), it may increase the probability of the event, or it may decrease the probability of the event.

Intuition is an unreliable guide when trying to decide if two events $E$ and $F$ are independent $(p(E \cap F)=p(E) p(F))$ or not independent $(p(E \cap F) \neq p(E) p(F))$. Indeed, the "same" events may or may not be independent, depending on the underlying sample space. Two examples were given above: $E_{2}(S)$ and $E_{3}(S)$ on $S=\{1,2,3,4,5,6\}$ are independent, but with $S$ replaced by $T=\{4,5,6\}$ events $E_{2}(T)$ and $E_{3}(T)$ are no longer independent and neither are events $E_{2}(U)$ and $E_{3}(U)$ where $U=\{1,2,3,4\}$.

As a more contrived third example, assume that in families of $k$ children each of the $2^{k}$ different gender-distributions of children is equally likely (for example: for $k=3$ each of the eight possibilities $b b b, b b g, b g b, b g g, g b b, g b g, g g b, g g g$ has probability $\frac{1}{8}$ to occur). Let $C_{k}$ be the event that a family with $k$ children has children of both sexes, and let $B_{k}$ be the event that a family with $k$ children has at most one boy. Are $C_{k}$ and $B_{k}$ independent?

- If $k=2$ then $C_{2}=\{b g, g b\}, p\left(C_{2}\right)=\frac{1}{2}, B_{2}=\{b g, g b, g g\}, p\left(B_{2}\right)=\frac{3}{4}$, $C_{2} \cap B_{2}=\{b g, g b\}, p\left(C_{2} \cap B_{2}\right)=\frac{1}{2}, p\left(C_{2}\right) p\left(B_{2}\right)=\frac{1}{2} \cdot \frac{3}{4}=\frac{3}{8} \neq \frac{1}{2}=$ $p\left(C_{2} \cap B_{2}\right)$, so $C_{2}$ and $B_{2}$ are not independent.
- If $k=3$ then $C_{3}=\{b b g, b g b, b g g, g b b, g b g, g g b\}, p\left(C_{3}\right)=\frac{6}{8}=\frac{3}{4}, B_{3}=$ $\{b g g, g b g, g g b, g g g\}, p\left(B_{3}\right)=\frac{4}{8}=\frac{1}{2}, C_{3} \cap B_{3}=\{b g g, g b g, g g b\}, p\left(C_{3} \cap B_{3}\right)=$ $\frac{3}{8}, p\left(C_{3}\right) p\left(B_{3}\right)=\frac{3}{4} \cdot \frac{1}{2}=\frac{3}{8}=p\left(C_{3} \cap B_{3}\right)$, so $C_{3}$ and $B_{3}$ are independent.
- If $k=4$ then $C_{4}=\{b b b g, b b g b, b b g g, b g b b, b g b g, b g g b, b g g g, g b b b, g b b g, g b g b$, $g b g g, g g b b, g g b g, g g g b\}, p\left(C_{4}\right)=\frac{14}{16}=\frac{7}{8}, B_{4}=\{b g g g, g b g g, g g b g, g g g b, g g g g\}$, $p\left(B_{4}\right)=\frac{5}{16}$ (note that we can stop right here: $p\left(C_{4}\right) p\left(B_{4}\right)=\frac{7}{8} \cdot \frac{5}{16}=\frac{35}{128}$ can never be of the form $\frac{m}{16}$ for $m \in \mathbf{Z}$ as would be required for it to be equal to $p\left(C_{4} \cap B_{4}\right)$ as required for independence; we continue only for the sake of completeness), $C_{4} \cap B_{4}=\{b g g g, g b g g, g g b g, g g g b\}, p\left(C_{4} \cap B_{4}\right)=\frac{4}{16}=\frac{1}{4}$, $p\left(C_{4}\right) p\left(B_{4}\right)=\frac{7}{8} \cdot \frac{5}{16}=\frac{35}{128} \neq \frac{4}{16}=p\left(C_{4} \cap B_{4}\right)$, so $C_{4}$ and $B_{4}$ are not independent.

If follows that the same properties (or, rather, events) may or may not be independent depending on the population size, which is not something one would intuitively expect: when trying to decide on independence of events $E$ and $F$ try to find the respective probabilities $p(E), p(F)$, and $p(E \cap F)$ and check if $p(E) p(F)=p(E \cap F)$ or not - but in any case do not assume by default that any two events are independent.

Bayes' theorem. Let $E$ and $F$ be two events with $p(E)>0$ and $p(F)>0$. The definition $p(E \mid F)=\frac{p(E \cap F)}{p(F)}$ implies that $p(E \mid F) p(F)=p(E \cap F)$ and thus also $p(E \cap F)=p(F \mid E) p(E)$. Equating the two it follows that

$$
\begin{equation*}
p(F \mid E)=\frac{p(E \mid F) p(F)}{p(E)} \tag{4}
\end{equation*}
$$

Equation (4) is known as Bayes' theorem: it says that with the right "re-scaling" factor (namely $\frac{p(F)}{p(E)}$, which "removes" the scaling by $F$ and replaces it by the scaling by $E$ ) the "probability of $E$ given $F$ " can be turned into the "probability of $F$ given $E "$.

Because $E \cap F$ and $E \cap \bar{F}$ are disjoint (i.e., $(E \cap F) \cap(E \cap \bar{F})=\emptyset$ ) and $(E \cap F) \cup$ $(E \cap \bar{F})=E$ it is the case that $p(E)=p((E \cap F) \cup(E \cap \bar{F}))=p(E \cap F)+p(E \cap \bar{F})$ so that with $p(E \cap F)=p(E \mid F) p(F)$ and $p(E \cap \bar{F})=p(E \mid \bar{F}) p(\bar{F})$ we find that

$$
\begin{equation*}
p(E)=p(E \mid F) p(F)+p(E \mid \bar{F}) p(\bar{F}) \tag{5}
\end{equation*}
$$

With Equation (4) this leads to the following alternative formulation

$$
p(F \mid E)=\frac{p(E \mid F) p(F)}{p(E \mid F) p(F)+p(E \mid \bar{F}) p(\bar{F})}
$$

of Bayes' theorem.

Applications of Bayes' theorem can be found all over the place and affect everyone. As mentioned in the book a common application is diagnostic tests for diseases. In class we did the example from the book with slightly different numbers. Suppose that in $99.99 \%$ of the randomly selected test cases a certain medical test indeed works correctly: i.e., it tests positive (indicated by "+" below) for $99.99 \%$ of the people that are known to have the disease and tests negative (indicated by "-" below) for $99.99 \%$ of the people that are known not to have the disease. But what does this tell you? If you test positive, what is the chance that you have the disease, and if you test negative, what is the chance that you nevertheless have the disease?

Using $D$ for "definitely has the disease" and the complement $\bar{D}$ for "definitely does not have the disease", we know that $p(+\mid D)=p(-\mid \bar{D})=0.9999$. But what you want to know is $p(D \mid+)$ ("assuming you test positive, what is the chance that you have the disease?") and $p(D \mid-)$ ("assuming you test negative, what is the chance that you nevertheless have the disease?"). From Bayes' theorem it follows that

$$
p(D \mid+)=\frac{p(+\mid D) p(D)}{p(+\mid D) p(D)+p(+\mid \bar{D}) p(\bar{D})} \text { and } p(D \mid-)=\frac{p(-\mid D) p(D)}{p(-\mid D) p(D)+p(-\mid \bar{D}) p(\bar{D})}
$$

With $p(+\mid \bar{D})=1-p(-\mid \bar{D})$ and $p(-\mid D)=1-p(+\mid D)$ it follows that

$$
p(D \mid+)=\frac{0.9999 p(D)}{0.9999 p(D)+0.0001 p(\bar{D})} \text { and } p(D \mid-)=\frac{0.0001 p(D)}{0.0001 p(D)+0.9999 p(\bar{D})}
$$

It follows from these expressions that both $p(D \mid+)$ and $p(D \mid-)$ strongly depend on how common the disease is to begin with: if only one out of every one million people has the disease (i.e., $p(D)=10^{-6}=0.000001$ ), the probability is only about $1 \%$ to have the disease when you test positive:

$$
p(D \mid+)=\frac{0.9999 \cdot 0.000001}{0.9999 \cdot 0.000001+0.0001 \cdot 0.999999} \approx 0.0099
$$

On the other hand if the disease is very common and $99 \%$ of the population has it $(p(D)=0.99)$, then even if you test negative you still have about $1 \%$ chance to have the disease:

$$
p(D \mid-)=\frac{0.0001 \cdot 0.99}{0.0001 \cdot 0.99+0.9999 \cdot 0.01} \approx 0.0098
$$

So, in order to be able to properly interpret the " $99.99 \%$ correctness probabilities", these probabilities need some context.

Other common (and very useful) examples can be found in the book: check them out. Note that the numbers in Example 3 in Section 7.3 are quite different in EPFL context, and that the probabilities there should be regarded as "under the condition not at EPFL".

Next class. (Re)read sections 7.1 through 7.4 (with the exception of Ramsey and the probabilistic method).


[^0]:    ${ }^{1}$ An ordered pair $(i, j)$ has $i$ as its first element and $j$ as its second element. Thus, if $i \neq j$ then the ordered pair $(i, j)$ is distinct from the ordered pair $(j, i)$ (which has $j$ as its first element and $i$ as its second element). The elements of an unordered pair $(i, j)$ on the other hand are not listed in any particular order and the unordered pair $(i, j)$ is considered to be the same as the unordered pair $(j, i)$.

