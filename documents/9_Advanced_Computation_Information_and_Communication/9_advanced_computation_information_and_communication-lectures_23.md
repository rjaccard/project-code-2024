Towers of Hanoi. A simple, popular example of recurrence relations is determining the minimal number of moves $M_{n}$ to be made to solve the "Towers of Hanoi" puzzle: given $n$ disks of $n$ sizes mounted in decreasing size (from bottom to top, ranging from size $n$ at the bottom to size 1 at the top) on a first peg, they must be moved to a second peg in such a way that per move just the single top disk can be moved from one peg to another peg and such that a disk can only be placed on the bottom or on top of a larger disk but never on top of a smaller disk. Furthermore, just a single auxiliary peg may be used (note that for $n>1$ the problem cannot be solved if there is no auxiliary peg).

Recursive towers of Hanoi solution. If $n=0$, then there is no disk, nothing has to be moved, so $M_{0}=0$. If $n=1$, then there is just one disk, so it can be moved from the first to the second peg in a single move. Thus $M_{1}=1$. For $n>1$ one notes that before the bottom disk can be moved to the second peg (as required to solve the puzzle), the entire stack of disks on top of it must be moved out of the way. Because the bottom disk must go to the bottom position of the second peg, the entire $n-1$-stack on top of it must first be moved from the first peg to the third peg (using the second one, which is initially empty, as auxiliary peg); this will require $M_{n-1}$ moves, followed by a single move for the largest (bottom) disk. Once this is
done, the entire $n-1$-stack that is now mounted on the third peg must be moved to the second one, using the (now empty) first peg as auxiliary peg, which requires again $M_{n-1}$ moves. Overall it is found that $M_{n}=M_{n-1}+1+M_{n-1}=2 M_{n-1}+1$. With $M_{0}=0$ one sees immediately that $M_{n}=2^{n}-1$, which is then trivially proved using induction.

Make sure you understand why all moves in the above approach are allowed (for instance, in the recursion the auxiliary pegs are no longer empty; but they contain only larger disks, so using them is allowed), why it cannot be done in fewer moves, and why this number of moves suffices. How would the recurrence change if the overall cost of the moves must be determined, where the cost of moving a disk of size $k$ (with $k$ ranging over $1,2, \ldots, n$ for the $n$ disks) may be defined to be proportional to the disk's diameter $k$ or to the disk's weight (proportional to $k^{2}$ assuming fixed thickness)?

The above does not give the moves to be made, but these can easily be found using a simple recursive C-function, to be called with hanoi $(5,1,2,3)$ for 5 disks (where " 1 " denotes the first peg that initially contains the disks, "2" denotes the second peg where all disks should be moved, and " 3 " is the third, auxiliary peg):

```
void hanoi( long n, long a, long b, long c) {
    if (n>0){
        hanoi(n-1,a,c,b);
        printf("move disk %ld from peg %ld to peg %ld\n",n,a,b);
        hanoi(n-1,c,b,a);
    }
}
```

Generating functions. Given some recurrence (plus initial conditions) that defines a sequence $a_{0}, a_{1}, \ldots, a_{n}, \ldots$ of real numbers, suppose one wants to find a closed formula for $a_{n}$. What often works is the following approach:

- interpret the sequence $a_{n}$ as the coefficients of the power series expansion $\sum_{i=0}^{\infty} a_{i} x^{i}$ of some function $A(x)$
- use the recurrence relation to derive an alternative expression for $A(x)$; and
- figure out the power series expansion for this alternative expression, the $n$-th coefficient of which must then be equal to $a_{n}$.

For the last step the whole page of power series expansions given in the book may be useful; no need to learn them by heart, though you should know the common ones such as $\frac{1}{1-x}=\sum_{k=0}^{\infty} x^{k}$ and $\frac{1}{(1-x)^{2}}=\sum_{k=0}^{\infty}(k+1) x^{k}$. Note that the formulas given in the book allow simple generalizations such as $\frac{1}{(a-b x)^{2}}=\frac{1}{a^{2}} \sum_{k=0}^{\infty}(k+1)\left(\frac{b}{a} x\right)^{k}$.

Very simple example. As an example of a recurrence that is trivial to solve, let $a_{0}=1$ and $a_{n}=a_{n-1}$ for $n \geq 1$ : we will use a generating function to show the obvious fact that $a_{n}=1$.

From $a_{n}=a_{n-1}$ for $n \geq 1$ it follows, rather obviously, that $a_{i} x^{i}=a_{i-1} x^{i}$ for any $i \geq 1$ and variable $x$, so that

$$
\sum_{i=1}^{\infty} a_{i} x^{i}=\sum_{i=1}^{\infty} a_{i-1} x^{i}
$$

With $A(x)=\sum_{i=0}^{\infty} a_{i} x^{i}=a_{0}+\sum_{i=1}^{\infty} a_{i} x^{i}$ and $a_{0}=1$, the left hand side becomes $A(x)-1$. The right hand side equals $x \sum_{i=1}^{\infty} a_{i-1} x^{i-1}$ and becomes, after a simple shift in the variable, $x \sum_{i=0}^{\infty} a_{i} x^{i}$ which equals $x A(x)$. We conclude that

$$
A(x)-1=x A(x)
$$

so that

$$
A(x)=\frac{1}{1-x} \text {. }
$$

Because $\frac{1}{1-x}=\sum_{k=0}^{\infty} x^{k}$, we find that

$$
\sum_{i=0}^{\infty} a_{i} x^{i}=A(x)=\frac{1}{1-x}=\sum_{i=0}^{\infty} x^{i}
$$

and thus that $a_{i}=1$ for $i \geq 0$.

Another simple example. As another example of a recurrence that is easy to solve, let $a_{0}=1$ and $a_{n}=2 a_{n-1}$ for $n \geq 1$ : we will use a generating function to show what we already know, namely that $a_{n}=2^{n}$.

From $a_{n}=2 a_{n-1}$ for $n \geq 1$ it follows as above that

$$
\sum_{i=1}^{\infty} a_{i} x^{i}=\sum_{i=1}^{\infty} 2 a_{i-1} x^{i}
$$

With $A(x)=\sum_{i=0}^{\infty} a_{i} x^{i}=a_{0}+\sum_{i=1}^{\infty} a_{i} x^{i}$ and $a_{0}=1$, the left hand side becomes $A(x)-1$. The right hand side equals $2 x \sum_{i=1}^{\infty} a_{i-1} x^{i-1}$ and becomes, after a simple shift in the variable, $2 x \sum_{i=0}^{\infty} a_{i} x^{i}$ which equals $2 x A(x)$. We conclude that

$$
A(x)-1=2 x A(x)
$$

so that

$$
A(x)=\frac{1}{1-2 x}
$$

Because $\frac{1}{1-x}=\sum_{k=0}^{\infty} x^{k}$, we find (using one of the "simple generalizations" referred to above) that

$$
\sum_{i=0}^{\infty} a_{i} x^{i}=A(x)=\frac{1}{1-2 x}=\sum_{i=0}^{\infty}(2 x)^{i}=\sum_{i=0}^{\infty} 2^{i} x^{i}
$$

and thus that $a_{i}=2^{i}$ for $i \geq 0$.

Solving the towers of Hanoi with a generating function. Let $M_{0}=0$ and $M_{n}=2 M_{n-1}+1$ for $n>0$. Put $H(x)=\sum_{i=0}^{\infty} M_{i} x^{i}$, then

$$
\begin{aligned}
H(x) & =\sum_{i=1}^{\infty} 2 M_{i-1} x^{i}+\sum_{i=1}^{\infty} x^{i} \\
& =2 \sum_{j=0}^{\infty} M_{j} x^{j+1}+x \sum_{i=0}^{\infty} x^{i} \\
& =2 x \sum_{j=0}^{\infty} M_{j} x^{j}+x \sum_{i=0}^{\infty} x^{i} \\
& =2 x H(x)+\frac{x}{1-x}
\end{aligned}
$$

This implies that $H(x)=\frac{x}{(1-x)(1-2 x)}$. Solving $H(x)=\frac{u}{1-x}+\frac{v}{1-2 x}$ for $u$ and $v$ it is found that $u-2 u x+v-v x=x$ and thus $u=-v$ and $-2 u-v=-2 u+u=1$ so that $u=-1$ and $v=1$. It follows that $H(x)=\frac{1}{1-2 x}-\frac{1}{1-x}$, therefore that

$$
H(x)=\sum_{i=0}^{\infty}(2 x)^{i}-\sum_{i=1}^{\infty} x^{i}
$$

and thus $M_{n}=2^{n}-1$.

Given this, can you find a closed expression for $d_{n}=1.02 d_{n-1}+y$, say with $d_{0}=1$ and for some arbitrary $y>0 ?$

Solving Fibonacci with a generating function. Let $f_{0}=0, f_{1}=1$, and $f_{n}=f_{n-1}+f_{n-2}$ for $n>1$. Put $F(x)=\sum_{i=0}^{\infty} f_{i} x^{i}$, then

$$
\begin{aligned}
F(x) & =f_{0} x^{0}+f_{1} x^{1}+\sum_{i=2}^{\infty} f_{i-1} x^{i}+\sum_{i=2}^{\infty} f_{i-2} x^{i} \\
& =x+\sum_{i=1}^{\infty} f_{i} x^{i+1}+\sum_{i=0}^{\infty} f_{i} x^{i+2}\left(f_{0}=0 \text { so the first summation can start at } i=0\right) \\
& =x+x F(x)+x^{2} F(x)
\end{aligned}
$$

This implies that $F(x)=\frac{-x}{\left(x-\rho_{1}\right)\left(x-\rho_{2}\right)}$ where $\rho_{1}=\frac{-1+\sqrt{5}}{2}$ and $\rho_{2}=\frac{-1-\sqrt{5}}{2}$. Solving $\frac{F(x)}{x}=\frac{-1}{\left(x-\rho_{1}\right)\left(x-\rho_{2}\right)}=\frac{u}{x-\rho_{1}}+\frac{v}{x-\rho_{2}}$ for $u$ and $v$ it is found that $u x-\rho_{2} u+v x-\rho_{1} v=$ -1 and thus $u=-v$ and $-\rho_{2} u+\rho_{1} u=-1$ so that $u=\frac{-1}{\rho_{1}-\rho_{2}}=\frac{-1}{\sqrt{5}}$ and $v=\frac{1}{\sqrt{5}}$. Thus

$$
\begin{aligned}
\frac{F(x)}{x} & =\frac{\frac{-1}{\sqrt{5}}}{x-\rho_{1}}+\frac{\frac{1}{\sqrt{5}}}{x-\rho_{2}} \\
& =\frac{\frac{-1}{\rho_{1} \sqrt{5}}}{\frac{x}{\rho_{1}}-1}+\frac{\frac{1}{\rho_{2} \sqrt{5}}}{\frac{x}{\rho_{2}}-1} \\
& =\frac{1}{\sqrt{5}}\left(\frac{\frac{1}{\rho_{1}}}{1-\frac{x}{\rho_{1}}}-\frac{\frac{1}{\rho_{2}}}{1-\frac{x}{\rho_{2}}}\right)
\end{aligned}
$$

It is found that

$$
\begin{aligned}
F(x) & =\frac{1}{\sqrt{5}}\left(\frac{\frac{x}{\rho_{1}}}{1-\frac{x}{\rho_{1}}}-\frac{\frac{x}{\rho_{2}}}{1-\frac{x}{\rho_{2}}}\right) \\
& =\frac{1}{\sqrt{5}}\left(\sum_{i=1}^{\infty}\left(\frac{x}{\rho_{1}}\right)^{i}-\sum_{i=1}^{\infty}\left(\frac{x}{\rho_{2}}\right)^{i}\right)
\end{aligned}
$$

and thus that $f_{n}=\frac{1}{\sqrt{5}}\left(\left(\frac{1}{\rho_{1}}\right)^{n}-\left(\frac{1}{\rho_{2}}\right)^{n}\right)$ for $n>0$ (which holds for $n=0$ as well). With $\rho_{1}=\frac{-1+\sqrt{5}}{2}=\frac{2}{1+\sqrt{5}}$ and $\rho_{2}=\frac{-1-\sqrt{5}}{2}=\frac{2}{1-\sqrt{5}}$ it follows that $f_{n}=\frac{1}{\sqrt{5}}\left(\left(\frac{1+\sqrt{5}}{2}\right)^{n}-\left(\frac{1-\sqrt{5}}{2}\right)^{n}\right)$ for $n \geq 0$. This is the desired closed form expression for the $n$-th Fibonacci number.

Yet another generating function example. A ternary string is a string that may contain characters " 0 ", " 1 ", or " 2 ". Thus, there are $3^{n}$ ternary strings of length $n$, for any $n \geq 0$ (where for $n=0$ we count the unique empty string).

Let $a_{n}$ denote the number of length $n$ ternary strings that contain an even number of characters " 1 ". This can be counted directly using our familiar combinatorial approach, resulting in an unpleasant looking sum $\sum_{k=0}^{\lfloor n / 2\rfloor} 2^{n-2 k}\binom{n}{2 k}$, so we prefer to find a closed form expression for $a_{n}$ by deriving a recurrence relation for it and solving the recurrence relation using a generating function.

An ad hoc method to find $a_{n}$, not done during the lecture. Before deriving a closed formula for $a_{n}$ using a generating function, note that the set of $3^{n}$ ternary strings of length $n$ are just the radix- 3 representations of all integers in the range from 0 to $3^{n}-1$ (including the bounds: thus an odd number of integers, namely $3^{n}$ ). The ones with an even number of characters " 1 " are just the even ones in that range
(why?). Because there are $\left(1+3^{n}\right) / 2$ even integers in the interval $\left[0,3^{n}-1\right]$ (why?) we immediately find, using this ad hoc observation, that $a_{n}=\left(1+3^{n}\right) / 2$. The method below has the advantage that it is more generally applicable, i.e., also for strings that may contain more than three different characters.

Finding the initial conditions. Because the empty string does not contain any characters, it in particular contains zero characters " 1 ", so that $a_{0}=1$ because zero is even. There are two length 1 strings that contain an even number of characters " 1 ", namely the string " 0 " and the string " 2 " (both of length 1 and both containing zero characters " 1 "), and there are 5 length 2 strings that contain an even number of characters " 1 ", namely the strings " 00 ", " 02 ", " $11 "$ ", " 20 ", " 22 ". Thus, $a_{0}=1, a_{1}=2$, $a_{2}=5$.

Finding a recurrence relation. To find a recurrence for $a_{n+1}$ (i.e., an expression specifying $a_{n+1}$ in terms of $a_{i}$-values for $i \leq n$ ), note that any ternary string $s$ of length $n$ (of which there are $3^{n}$ ) can be followed by a " 0 " (if $s$ contains an even number of characters " 1 ") or by a " 1 " (if $s$ contains an odd number of characters " 1 "), and that there is no other way to find "good" (i.e., with an even number of characters " 1 ") ternary strings of length $n+1$ that end with a " 0 " or a " 1 ". To find the number of good ternary strings of length $n+1$ that end with a " 2 ", note that the length- $n$ part before the final " 2 " must contain an even number of characters " 1 ", thus there are $a_{n}$ good ternary strings of length $n+1$ that end with a " 2 ". Overall it is found that for $n>0$ it is the case that $a_{n+1}=3^{n}+a_{n}=a_{n}+3^{n}$. Note this is indeed correct for $n=1,2: a_{1}=a_{0}+3^{0}=1+1=2$ and $a_{2}=a_{1}+3^{1}=2+3=5$.

Another argument to find the recurrence relation. Another way to find the recurrence for $a_{n+1}$ is by observing that if the last character of a good length $n+1$ ternary string is " 0 ", then there are $a_{n}$ ways to choose the first $n$ characters, and that the same is true if the final character is a " 2 ". If, however the last character is " 1 ", then there must be an odd number of characters " 1 " among the first $n$ characters. There are $3^{n}-a_{n}$ ternary length $n$ strings with an odd number of characters " 1 " because the $3^{n}$ ternary strings of length $n$ can be partitioned into two disjoint sets: the $a_{n}$ strings of length $n$ that have an even number of characters " 1 ", and the others that have an odd number of characters " 1 "; it thus follows that there must be $3^{n}-a_{n}$ of the latter. Overall it is found that $a_{n+1}=2 a_{n}+3^{n}-a_{n}=a_{n}+3^{n}$.

Solving the recurrence relation using a generating function. Let $a_{0}=1$, and $a_{n+1}=a_{n}+3^{n}$ for $n>0$. Put $A(x)=\sum_{i=0}^{\infty} a_{i} x^{i}$, then

$$
\begin{aligned}
A(x) & =a_{0} x^{0}+\sum_{i=1}^{\infty} a_{i} x^{i} \\
& =1+\sum_{j=0}^{\infty} a_{j+1} x^{j+1} \\
& =1+x \sum_{j=0}^{\infty} a_{j+1} x^{j} \\
& =1+x \sum_{j=0}^{\infty}\left(a_{j}+3^{j}\right) x^{j} \\
& =1+x \sum_{j=0}^{\infty} a_{j} x^{j}+x \sum_{j=0}^{\infty} 3^{j} x^{j} \\
& =1+x A(x)+\frac{x}{1-3 x}
\end{aligned}
$$

where for the last step we use the fact that $\sum_{i=0}^{\infty}(3 x)^{i}=\frac{1}{1-3 x}$.

It now follows that $A(x)(1-x)=1+\frac{x}{1-3 x}$ so that, with $1+\frac{x}{1-3 x}=\frac{1-2 x}{1-3 x}$,

$$
A(x)=\frac{1-2 x}{(1-x)(1-3 x)}
$$

Writing $A(x)=\frac{u}{1-x}+\frac{v}{1-3 x}$ and solving this for $u$ and $v$ it is found that $u+v=1$ and $-3 u-v=-2$. It follows that $u=v=\frac{1}{2}$ so that $A(x)=\frac{1}{2}\left(\frac{1}{1-x}+\frac{1}{1-3 x}\right)$. Using $\sum_{i=0}^{\infty} r^{i}=\frac{1}{1-r}$ again (twice), it follows that

$$
A(x)=\frac{1}{2} \sum_{i=0}^{\infty}\left(1+3^{i}\right) x^{i}
$$

and thus that $a_{n}=\frac{1}{2}\left(1+3^{n}\right)$ (confirming the result of the ad hoc method).

Solving recurrence relations in practice. If you need to solve a recurrence relation that you derived or came across otherwise, the most time-efficient method is probably to compute the first 8 -or-so terms and to enter them on www.oeis.org. If a closed form expression exists it will be given there; lots of interesting and possibly relevant background on the sequence may be provided as well.

## Relations

Binary relations. A binary relation from a set $A$ to a set $B$ is any subset of the Cartesian product $A \times B$. If $R$ is a non-empty binary relation, and thus a non-empty subset of $A \times B$, an element of $R$ may be denoted as an ordered pair $(a, b)$ with $a \in A$ and $b \in B$; the fact that $(a, b) \in R$ may also be denoted as $a R b$ (during the lecture we indeed used the notation $a R b$ for $(a, b) \in R$, in these notes the notation $a R b$ will not be used. Refer to Section 9.1 of the book for examples of binary relations.

Each distinct subset of $A \times B$ corresponds to a distinct binary relation. Because the cardinality $|A \times B|$ of the Cartesian product $A \times B$ equals the product $|A||B|$ of the cardinality $|A|$ of $A$ and the cardinality $|B|$ of $B$, there are (assuming finite $A$ and $B$ ) a total of $2^{|A||B|}$ distinct subsets ${ }^{1}$ of $A \times B$ and thus $2^{|A||B|}$ distinct binary relations from $A$ to $B$.

Representing relations. Relations can be represented in several ways: as sets consisting of ordered pairs $(a, b)$ with $a \in A, b \in B$; if $A \neq B$ as bipartite graphs on $|A|+|B|$ vertices with vertex sets $V_{A}=\left\{v_{a} \mid a \in A\right\}$ and $V_{B}=\left\{v_{b} \mid b \in B\right\}$ and an edge between $v_{a} \in V_{A}$ and $v_{b} \in V_{B}$ if and only if the pair $(a, b)$ is in the relation; if $A=B$ as a graph on $|A|$ vertices with vertex set $V_{A}=\left\{v_{a} \mid a \in A\right\}$ and an edge between $v_{a_{1}}$ and $v_{a_{2}}$ if and only if the pair $\left(a_{1}, a_{2}\right)$ is in the relation (note that this graph may contain loops, i.e., edges that connect a vertex to itself); as $|A| \times|B|$-bit-matrices $\left(m_{a, b}\right)_{a \in A, b \in B}$ where $m_{a, b}=1$ if and only if the pair $(a, b)$ is in the relation and $m_{a, b}=0$ otherwise. The latter representation turns out to be particularly useful if computations have to be done with relations.[^0]$n$-Ary relations (briefly mentioned in class). More in general, an $n$-ary relation on sets $A_{1}, A_{2}, \ldots, A_{n}$ is any subset of the Cartesian product $A_{1} \times A_{2} \times A_{3} \times \ldots \times A_{n}$. Elements of an $n$-ary relation may be denoted by ordered $n$-tuples $\left(a_{1}, a_{2}, \ldots, a_{n}\right)$ where $a_{i} \in A_{i}$ for $1 \leq i \leq n$. Refer to Section 9.2 of the book for examples of $n$-ary relations.

Operations on relations. Because relations are "just" sets (namely, subsets, of some Cartesian product), set-operations (such as $\cup, \cap, \backslash$, and taking the complement) may be applied to them, resulting again in, possibly different, relations.

Functions are relations, but not vice versa. A function $f$ from $A$ to $B$ (for sets $A, B)$ is a relation for which it is the case that

$$
\forall a \in A \exists!b \in B(a, b) \in f
$$

The uniqueness of $b$ given $a$ then makes it possible to write " $f(a)=b$ ".

So a function $f$ from $A$ to $B$ is a relation that satisfies properties that a binary relation from $A$ to $B$ in general does not have to satisfy:

(1) there is no $a \in A$ that does not occur in a relation in $f$ : each $a \in A$ occurs in $f$ as first element of an ordered pair.

(2) there is no $a \in A$ that occurs more than once in a relation in $f$ : each $a \in A$ occurs precisely once in $f$ as first element of an ordered pair.

Note that, for finite $A$ and $B$ there are "only" $|B|^{|A|}$ distinct functions from $A$ to $B$ and that indeed $|B|^{|A|}<2^{|A||B|}$ (which can easily be seen by observing that $|B|<2^{|B|}$ or by writing $|B|^{|A|}$ as $\left.2^{\left(\log _{2}(|B|)|A|\right.}\right)$.

Relations on a single set. Given a single set $A$, a relation on $A$ is a binary relation from $A$ to $A$. Thus a relation on $A$ is a subset of the Cartesian product $A \times A=A^{2}$, and elements of a relation on $A$ are ordered pairs $\left(a_{1}, a_{2}\right) \in A \times A$. So if $a_{1} \neq a_{2}$ then $\left(a_{1}, a_{2}\right) \neq\left(a_{2}, a_{1}\right)$ and if for some relation $R$ on $A$ it is the case that $\left(a_{1}, a_{2}\right) \in R$, it does not imply that $\left(a_{2}, a_{1}\right) \in R$; but the latter is the case if $R$ is symmetric - see below.

The most important properties that a relation on a set $A$ may have are:

Reflexivity: a relation $R$ on $A$ is reflexive if for all $a \in A$ it is the case that $(a, a) \in R$ :

$$
\forall a \in A(a, a) \in R .
$$

Symmetry: a relation $R$ on $A$ is symmetric if for all $a, b \in A$ it is the case that if $(a, b) \in R$ then also $(b, a) \in R$ :

$$
\forall a \forall b \in A(a, b) \in R \rightarrow(b, a) \in R
$$

Transitivity: a relation $R$ on $A$ is transitive if for all $a, b, c \in A$ it is the case that if both $(a, b) \in R$ and $(b, c) \in R$ then also $(a, c) \in R$ :

$$
\forall a \forall b \forall c \in A((a, b) \in R \wedge(b, c) \in R) \rightarrow(a, c) \in R
$$

As shown below, these three properties are independent. Another property (not discussed in class) that a relation on a set $A$ may have is the following:

Antisymmetry: a relation $R$ on $A$ is antisymmetric if for all $a, b \in A$ it is the case that if $(a, b) \in R$ and $(b, a) \in R$ then $a=b$ :

$$
\forall a \forall b \in A \quad((a, b) \in R \wedge(b, a) \in R) \rightarrow a=b
$$

Example relations on a single set. Only mentioned in class, but not explicitly shown - make sure though that you understand why each of these examples is (not) reflexive, (not) symmetric, and (not) transitive. Note that, below, $R$ denotes a relation, but that $\mathbf{R}$ denotes the set of the real numbers.

(1) $R=\{(a, b): a, b \in \mathbf{R}, a=2 b\}$ : not reflexive, not symmetric, not transitive;

(2) $R=\{(a, b): a, b \in \mathbf{R}, a>b-1\}$ : reflexive, not symmetric, not transitive;

(3) $R=\{(a, b): a, b \in \mathbf{R}, a b<0\}$ : not reflexive, symmetric, not transitive;

(4) $R=\{(a, b): a, b \in \mathbf{R}, a<b-1\}$ : not reflexive, not symmetric, transitive;

(5) $R=\{(a, b): a, b \in \mathbf{R},|a-b|<1\}$ : reflexive, symmetric, not transitive;

(6) $R=\left\{(a, b): a, b \in \mathbf{N}_{>0}, a \mid b\right\}$ : reflexive, not symmetric, transitive (where "|" denotes "divides");

(7) $R=\{(a, b): a, b \in \mathbf{R}, a b>0\}$ : not reflexive (because $0 \in \mathbf{R}$ but $(0,0) \notin R)$, symmetric, transitive (another example: $R=\emptyset, A \neq \emptyset$ );

(8) $R=\{(a, a): a \in A\}$ : reflexive, symmetric, transitive (another, more interesting, example: $R=\{(a, b): a, b \in \mathbf{N}, a \equiv b \bmod m\}$ where $m$ is an arbitrary positive integer, and where " $a \equiv b \bmod m$ " denotes $m \mid a-b$, i.e., that $a-b$ is an integer multiple of $m$ ).

Equivalence relation. An equivalence relation is a relation that is reflexive, symmetric, and transitive. If $R$ is an equivalence relation on a set $A$, then

- If $(a, b) \in R$, then $a$ and $b$ are called equivalent, denoted by $a \sim b$.
- $[a]_{R}=\{x \in A:(a, x) \in R\}$ is called $a$ 's equivalence class.
- $[a]_{R}$ is denoted $[a]$ if $R$ is clear from the context.
- Any element of $[a]_{R}$ may be chosen as representative of $[a]_{R}$, because, due to the equivalence relation, all elements of $[a]_{R}$ are equivalent anyhow.

An important property of an equivalence relation $R$ (on some set) is the following:

$$
(a, b) \in R \leftrightarrow[a]_{R}=[b]_{R} \quad \leftrightarrow \quad[a]_{R} \cap[b]_{R} \neq \emptyset
$$

We prove these two logical equivalences in three steps by proving the three "only if"s, i.e., the three implications below:

$$
(a, b) \in R \rightarrow[a]_{R}=[b]_{R} \rightarrow[a]_{R} \cap[b]_{R} \neq \emptyset \rightarrow(a, b) \in R
$$

$\rightarrow$ : Given that $(a, b) \in R$, we prove that $[a]_{R}=[b]_{R}$ by showing that the following two inclusions hold: $[a]_{R} \subseteq[b]_{R}$ and that $[a]_{R} \supseteq[b]_{R}$.

proof of $\subseteq$ : Let $c \in[a]_{R}$, then according to the definition of $[a]_{R}$ we have that $(a, c) \in R$. From $(a, b) \in R$ and the symmetry of $R$ it follows that $(b, a) \in R$; with $(a, c) \in R$ it then follows (due to transitivity of $R$ ) that $(b, c) \in R$ and thus that $c \in[b]_{R}$ (due to the definition of $\left.[b]_{R}\right)$. Therefore $[a]_{R} \subseteq[b]_{R}$.

proof of $\supseteq$ : Now let $c \in[b]_{R}$, then according to the definition of $[b]_{R}$ we have that $(b, c) \in R$. Along with $(a, b) \in R$ and the transitivity of $R$ it follows that $(a, c) \in R$ so that $c \in[a]_{R}$ (according to the definition of $[a]_{R}$ ), and we find that $[a]_{R} \supseteq[b]_{R}$.

$\rightarrow$ : If $[a]_{R}=[b]_{R}$ it follows that $[a]_{R} \cap[b]_{R}=[a]_{R}$; it then follows from $(a, a) \in R$ (which itself follows from the reflexivity of $R$ ) and the definition of $[a]_{R}$ that $a \in[a]_{R}$ and thus that $[a]_{R} \neq \emptyset$. Therefore $[a]_{R}=[a]_{R} \cap[b]_{R} \neq \emptyset$.

$\rightarrow:$ If $[a]_{R} \cap[b]_{R} \neq \emptyset$ there is an element $c$ such that $c \in[a]_{R} \cap[b]_{R}$. From $c \in[a]_{R}$ and the definition of $[a]_{R}$ we have that $(a, c) \in R$. From $c \in[b]_{R}$ and the definition of $[b]_{R}$ we have that $(b, c) \in R$. With the symmetry of $R$ it follows that $(c, b) \in R$, so that along with $(a, c) \in R$ and the transitivity of $R$ it follows that $(a, b) \in R$.

Partitions and equivalence relations. It follows that an equivalence relation on $A$ induces a partition ${ }^{2}$ of $A$, and vice versa, a partition of $A$ induces an equivalence relation on $A$ : the collection of equivalence classes is a collection of mutually disjoint non-empty subsets of $A$ the union of which equals $A$ (because each equivalence class is contained in $A$ and thus the union of the equivalence classes is[^1]contained in $A$; and because each element $a$ of $A$ is contained (due to reflexivity) in $[a]_{R}$ and thus contained in the union of equivalence classes); and vice versa, given a partition define an equivalence relation by saying that two elements are equivalent if and only if they belong to the same subset of the partition: check that this is indeed an equivalence relation!

Composition of relations. (This generalizes what we did during the lecture using examples.) Given relation $R$ from $A$ to $B$ and relation $S$ from $B$ to $C$, define the composite relation $S \circ R$ from $A$ to $C$ as the relation consisting of those elements $(a, c)$ with $a \in A, c \in C$ for which there exists an element $b \in B$ such that $(a, b) \in R$ and $(b, c) \in S$. Note that $S \circ R \subseteq A \times C$ and thus $S \circ R$ is indeed a relation from $A$ to $C$. Note the correspondence to matrix multiplication, as also pointed out in class.

With $R$ a relation on $A$ (and thus $R \subseteq A \times A$ ) it is the case that $R \circ R \subseteq A \times A$. We write $R \circ R=R^{2}$, and inductively define the $n$-fold composite $R \circ R \circ R \circ \ldots \circ R=R^{n}$ as $R^{n-1} \circ R$. With $A$ a set of cities and $R$ the relation with $(a, b) \in R$ if there is a non-stop flight from city $a$ to city $b$, the relation $R \circ R=R^{2}$ can be interpreted as the pairs $(a, c)$ so that $c$ can be reached from $a$ in two hops (possibly, but not necessarily, in one hop, namely if $(a, c) \in R$ as well). Similarly $R^{n}$ consists of pairs $(a, z)$ of cities so that city $z$ can be reached from city $a$ in $n$ hops (possibly, but not necessarily, fewer). Thus, it becomes interesting to look at the collection $\bigcup_{i=1}^{n} R^{i}$ of pairs of cities that are at most $n$ hops apart. Because this type of scenario allows various useful applications (reachability in networks is a traditional one - with "big data" the number of applications is virtually unlimited) it leads to a number of relevant questions:

(1) How far do we have to go with $n$ before all cities are covered that can eventually be reached?

(2) How do we calculate which cities can be reached, and what the smallest number of hops would be?

(3) How do we represent $R$ in such a way that the calculations can be performed efficiently?

Transitive relations. These questions are relatively easy to answer if $R$ is transitive, because in that case the powers $R^{n}$ of $R$ for $n>1$ do not contribute anything "new". This is intuitively obvious; more formally, it is a consequence of the following result:

$$
R \text { on } A \text { is transitive } \leftrightarrow R^{n} \subseteq R \text { for } n=1,2,3, \ldots
$$

It follows that transitivity implies that any city that can be reached in $n$ hops can also directly be reached in a single hop, for any $n$.

The proof of the above result consists of two parts, the "if"-part $(\leftarrow)$ and the "only if"-part $(\rightarrow)$ :

"if"-part: We assume that $R^{n} \subseteq R$ for $n=1,2,3, \ldots$ and we have to prove that $R$ is transitive. Thus, assuming that $(a, b) \in R$ and that $(b, c) \in R$ we have to prove that $(a, c) \in R$. But $(a, b) \in R$ and $(b, c) \in R$ implies, according to the definition of $R^{2}=R \circ R$, that $(a, c) \in R^{2}$. Given that $R^{n} \subseteq R$ for $n=1,2,3, \ldots$ it follows in particular that $R^{2} \subseteq R$. Therefore, $(a, c) \in R^{2}$ implies that $(a, c) \in R$, which is what we had to prove.

"only if"-part: We assume that $R$ is transitive and we have to prove that $R^{n} \subseteq R$ for $n=1,2,3, \ldots$ We prove this by mathematical induction. The basis of the induction is reached for $n=1$ and thus requires proving that $R^{1}=R \subseteq R$ : because $R=R$ the basis of the induction is correct. Now assume, as induction hypothesis, that $R^{n} \subseteq R$ for an arbitrary $n \geq 1$. We have to prove that $R^{n+1} \subseteq R$. To prove this it suffices to prove that any
element of $R^{n+1}$ belongs to $R$ as well. Thus, take some $x \in R^{n+1}$ : we must prove that $x \in R$. This $x$ is just a pair in $A \times A$ and can thus be written as $x=(a, c)$ for some $a, c \in A$. Given that $(a, c) \in R^{n+1}$ it follows from the definition $R^{n} \circ R$ of $R^{n+1}$ that there exists an element $b \in A$ such that $(a, b) \in R$ and $(b, c) \in R^{n}$, where $n \geq 1$. According to the induction hypothesis $R^{n} \subseteq R$, thus $(b, c) \in R$. But $R$ is assumed to be transitive, so $(a, b) \in R$ and $(b, c) \in R$ imply that $(a, c) \in R$ and thus that $x \in R$. This completes the proof of the inductive step. Combined with the basis step the proof of the "only if"-part follows.

Because $R$ 's transitivity implies that $R^{n} \subseteq R$ for $n=1,2,3, \ldots$ and thus $\bigcup_{i=1}^{\infty} R^{i} \subseteq$ $R$ and because for any relation $R$ it is the case that $R \subseteq \bigcup_{i=1}^{\infty} R^{i}$, it follows that $R=\bigcup_{i=1}^{\infty} R^{i}$ for transitive $R$, and that at least the first two of the three questions above can easily be answered: $n=1$ suffices and the cities that can be reached from any city immediately follow from $R$. Think about how one would decide if a relation is transitive or not - it can easily be done in $O\left(|A|^{3}\right)$ operations. A convenient representation for $R$ is further discussed below.

Non-transitive relations and transitive closure. Given a relation $R$ on a set $A$ the transitive closure of $R$ is defined as the smallest transitive relation that contains $R$. We have the following result:

$$
\text { the transitive closure of } R \text { equals } R^{c}=\bigcup_{i=1}^{\infty} R^{i}
$$

(which, when applied to transitive $R$ results in $R^{c}=R$ due the the earlier result proved above). Note that we avoid the notation $R^{*}$ from the book. The proof consists of two steps: proving that $R^{c}$ is transitive, and showing that $R^{c}$ is the smallest transitive relation that contains $R$ :

$R^{c}$ is transitive: We need to prove that if $(a, b) \in R^{c}$ and $(b, c) \in R^{c}$ then $(a, c) \in R^{c}$. This is indeed the case, because $(a, b) \in R^{c}$ implies that $(a, b) \in R^{m}$ for some $m>0$ and $(b, c) \in R^{c}$ implies that $(b, c) \in R^{n}$ for some $n>0$. "Concatenating" the length- $n$ path from $b$ to $c$ to the length$m$ path from $a$ to $b$ we get a length- $(m+n)$ path from $a$ to $c$, so that $(a, c) \in R^{m+n}$ and thus $(a, c) \in R^{c}$. Note that this proof is a bit "informal" because $R^{m+n}$ is defined at $R^{m+n-1} \circ R$ and not as $R^{m} \circ R^{n}$ - but this can be fixed at more notational effort.

$R^{c}$ is the smallest transitive relation that contains $R$ : Let $S$ be any transitive relation that contains $R$. If we prove that $R^{c}$ is contained in $S$, then we have proved that indeed $R^{c}$ is the smallest transitive relation that contains $R$. Because $S$ is transitive we have that $S^{n} \subseteq S$ for any integer $n>0$ (because of the result proved above), so that $S^{c} \subseteq S$. From $R \subseteq S$ it follows that $R^{c} \subseteq S^{c}$, which with $S^{c} \subseteq S$ indeed leads to $R^{c} \subseteq S$, i.e., $R^{c}$ is contained in $S$.

Computing $R^{c}$ in a straightforward manner. To get our hands on $R^{c}$ (because it would be a transitive relation from which it can "easily" be seen which cities can be reached from which other cities: in $R^{c}$ that would take just a single "hop" even if it takes any number of hops by using $R$ repeatedly) we must compute

$$
R \cup R^{2} \cup R^{3} \cup R^{4} \cup \ldots \cup R^{k} \cup \ldots
$$

Each of the $R^{i}$ is just a set, so the Us can be taken care of by set-unions: all that remains to be done is figuring out how to compute $R^{k+1}$ from $R$ and $R^{k}$ (for any integer $k>0$ ), and to figure out how far we need to go with $k$. The latter follows easily when we assume that the underlying set $A$ is finite: because we can never
visit more than $|A|$ different cities, $|A|$ steps suffice (and may be necessary, if we have a circular arrangement of the $|A|$ cities), thus $k=|A|$ suffices.

Computing $R^{k+1}$ given $R$ and $R^{k}$ can be done using the definition: $(a, c) \in R^{k+1}$ if there is an element $b \in A$ such that $(a, b) \in R$ and $(b, c) \in R^{k}$. We find that $(a, c) \in R^{k+1}$ (which is a logical statement that is true of false) if and only if

$$
\begin{equation*}
\left.\bigvee_{b \in A}\left((a, b) \in R \wedge(b, c) \in R^{k}\right)\right) \tag{1}
\end{equation*}
$$

(which is also a logical statement that is true or false). At the end of this summary the correspondence between Expression (1) and "ordinary" matrix multiplication (which was used in the examples during the lecture) is further illustrated. Because there are $\Theta\left(|A|^{2}\right)$ pairs $(a, c)$ and $|A|$ distinct values of $b$ to inspect per pair $(a, c)$, the overall effort to compute $R^{k+1}$ given $R$ and $R^{k}$ and using Expression (1) is $\Theta\left(|A|^{3}\right)$. Doing this for $k$ up to $|A|$ implies an overall effort of $\Theta\left(|A|^{4}\right)$ to compute the transitive closure $R^{c}$ of $R$ (where it is assumed that computing each of the set-unions does not take more effort than $\Theta\left(|A|^{3}\right)$ ).

Warshall's algorithm: computing $R^{c}$ in a smart way. Assume again that $A$ is finite, and identify the elements of $A$ with the set of integers $\{1,2, \ldots,|A|\}$.

Consider a pair of integers $(i, j)$ both in $\{1,2, \ldots,|A|\}$ such that $(i, j) \in R^{c}$ : as we want to construct $R^{c}$ we are interested in finding out how to find these pairs $(i, j)$. Given that $(i, j) \in R^{c}$, we observe that the "path" that goes from $i$ to $j$ and that uses some concatenation of relations in $R$, uses just the set $\{1,2, \ldots, k\} \subseteq A$ if and only if

- the path uses just $\{1,2, \ldots, k-1\} \subseteq A$ (i.e., the element $k$ is not needed), or
- the path first goes from $i$ to $k$ (using just the set $\{1,2, \ldots, k-1\} \subseteq A$ as intermediate elements on this first part of the path), followed by a second part that goes from $k$ to $j$ (using again just the set $\{1,2, \ldots, k-1\} \subseteq A$ as intermediate elements on this second part of the path): note that element $k$ if it occurs, occurs only once, because if it occurs more than once the "loop" from $k$ to $k$ can be removed.

Thus, for all pairs $(i, j)$ we can find out if $(i, j)$ belongs to $R^{c}$ by the following iterative approach: first try for all pairs $(i, j)$ if we can go directly from $i$ to $j$ or from $i$ to " 1 " and then from " 1 " to $j$; then, once all paths have been constructed that have " 1 " as maximal intermediate element, try for all pairs $(i, j)$ if we can already go from $i$ to $j$ (directly, or using " 1 " as maximal intermediate element) or if we can go from $i$ to " 2 " and then from " 2 " to $j$, where the latter two paths may again either be direct (in $R$ ) or via " 1 ", etc. This leads to the following method, where the pairs $(i, j)$ will be assigned truth values and will initially be true if and only if $(i, j) \in R$ :

for $k=1$ to $|A|$ do

for $i=1$ to $|A|$ do

for $j=1$ to $|A|$ do $(i, j)$ gets the value $(i, j) \vee((i, k) \wedge(k, j))$

Make sure you understand why the " $(i, j) \vee$ " part is included. This method requires effort $\Theta\left(|A|^{3}\right)$. A simple adaptation leads to all shortest length paths (here we only worry about "reachability" or not), if any, among all pairs of elements of $A$.

Representing $R$. As suggested by the remark above that pairs $(i, j)$ are assigned truth values, we may represent $R$ as an $|A| \times|A|$ bit-matrix $\left(r_{i j}\right)_{i, j=1}^{|A|}$ where the element $r_{i j}$ in the $j$-th column of the $i$-th row of the bit-matrix is " 1 " if and only if $(i, j) \in R$ (and thus " 0 " if and only if $(i, j) \notin R$ ). Make sure that you understand that the relation $R \circ R=R^{2}=S=\left(s_{i j}\right)_{i, j=1}^{|A|}$ can now be computed as the
square of the bit-matrix $\left(r_{i j}\right)_{i, j=1}^{|A|}$ because Expression (1) corresponds to matrix multiplication on logical values, thus with integer addition replaced by " $V$ " and integer multiplication replaced by " $\wedge$ ":

$$
s_{i, j}=\bigvee_{k=1}^{|A|}\left(r_{i, k} \wedge r_{k, j}\right) \text { compared to } y_{i, j}=\sum_{k=1}^{n} x_{i, k} x_{k, j}
$$

(where $X=\left(x_{i, j}\right)_{i, j=1}^{n}$ is a matrix over the real numbers and the expression on the right is the entry $y_{i, j}$ in the $j$-th column of the $i$-th row of the product matrix $\left.X \times X=Y=\left(y_{i, j}\right)_{i, j=1}^{n}\right)$. More in general it follows that $R^{n}$ can be computed as the $n$-th power or the bit-matrix $\left(r_{i j}\right)_{i, j=1}^{|A|}$. Bit-matrix representations of relations also allow easy intersection and union of relations (by doing bit-wise " $\wedge$ " and " $\vee$ ", respectively, on the bit-matrix entries). It also allows easy computation of the reflexive closure of $R$ as $M \vee I$ (where $M=\left(r_{i j}\right)_{i, j=1}^{|A|}$ and $I$ is the $|A| \times|A|$ identity matrix) and of the symmetric closure of $R$ as $M \vee M^{T}$ (where $M^{T}$ denotes the transpose of $M)$ - how would you define the reflexive and symmetric closures of $R$ ?

Next class. The final exam (Jan 24, 2019, 08:15-11:15) covers everything that was discussed during the lectures. So prepare questions about anything we discussed!

A question and answer session for the final exam will - most likely - be organized on Monday January 21, sometime during the afternoon, somewhere on campus. Information will appear on moodle as soon as it is available.


[^0]:    ${ }^{1}$ Here we use the fact that a finite set of cardinality $n$ has $2^{n}$ distinct subsets, as seen on several occasions in previous lectures.

[^1]:    ${ }^{2} A=\bigcup_{i=1}^{k} A_{i}$ is a partition of $A$ if $A_{i} \neq \emptyset$ for $1 \leq i \leq k$ and $A_{i} \cap A_{j}=\emptyset$ for $1 \leq i<j \leq k$.

