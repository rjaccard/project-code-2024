Sets. Read about sets in Chapter 2, note the correspondence between logical operations and set operations:

$$
\begin{aligned}
& \neg \Longleftrightarrow \text { "complement", denoted by } \bar{A} \text { for a set } A \\
& \wedge \Longleftrightarrow \cap \\
& \vee \Longleftrightarrow \cup \\
& \oplus \Longleftrightarrow \triangle \text { or } \oplus \text { (for sets } \triangle \text { or } \oplus \text { is called the symmetric difference }) \\
& \rightarrow \Longleftrightarrow \subseteq \\
& \leftrightarrow \Longleftrightarrow=
\end{aligned}
$$

and the resulting similarity between membership tables and truth tables.

Make sure you understand that to prove that sets $A$ and $B$ are equal it is not sufficient to prove that $A \subseteq B$ but that one has to prove $B \subseteq A$ as well (where the latter may be denoted as $A \supseteq B$ : here we use the notation of the book, thus with $\subseteq$ and $\supseteq$ to be replaced by $\subset$ and $\supset$ if you are French, cf. footnote in Oct. 2 lecture notes). You should know what a Cartesian product is (already used during the September 18 lecture) and remember that Venn diagrams may be nice to get an idea of what is going on but that a picture (and Venn diagrams are pictures) is never a proof (see below why; picture stolen from the web).

If you are wondering why this Venn diagram does not use circles, as Venn diagrams normally do, you may find it interesting to know that as soon as all possible intersections of more than three sets have to be "pictured" (using a Venn diagram) circles can no longer be used: for four sets circles can capture at most 14 of the 16 intersection possibilities. The picture above (for six sets) is symmetric and can therefore ${ }^{1}$ not be complete while avoiding duplications and misses some of the $2^{6}=64$ possible intersections - can you tell which ones? (Don't waste your time trying to figure this out, and just remember that Venn diagrams are useless for any serious purpose.)

Power sets. Given some set $A$, the power set $\mathcal{P}(A)$ of $A$ is the set of all subsets ${ }^{2}$ of $A$. Thus, the elements of $\mathcal{P}(A)$ are sets, and a set belongs to $\mathcal{P}(A)$ (thus: is an element of $\mathcal{P}(A))$ if and only if it is a subset of $A$.

If $A$ is finite and has $k$ elements (which we may denote by $|A|=k$ or $\# A=k$ (both notations are common, though the book uses just $|A|$ ) and which is called the cardinality of $A$ ), then $\mathcal{P}(A)$ has $2^{k}$ elements: $\# \mathcal{P}(A)=2^{k}$. As already discussed during the September 18 lecture, that is not hard to see: for each of the $k$ elements of $A$ a 1 or 0 bit can be used to indicate the membership (a 1 bit) or not (a 0 bit) of that element in a subset of $A$, so ranging over all $k$ elements we can form $2^{k}$ (and not more) distinct subsets because there are $2^{k}$ distinct $k$-bit strings. This is illustrated below. But, this is not a proof of the fact that $\# \mathcal{P}(A)=2^{k}$ : later we will see how to prove that $\# \mathcal{P}(A)=2^{\# A}$ for finite sets $A$.

When creating the power set of a set, keep in mind that for any set $A$ it is always the case that $\emptyset \subseteq A$ (where $\emptyset$ denotes the empty set) and that also $A \subseteq A$; the statement " $A \subseteq A$ " may be obvious, but " $\emptyset \subseteq A$ " may not be so obvious: it is true because $\forall x \in \emptyset x \in A$ (an example of what was mentioned before, where the " $\forall$ " ranges over an empty set, so it is true no matter what logical expression related to $x$ is involved) thus establishing that $\emptyset \subseteq A$. As a consequence of $\emptyset \subseteq A$ and $A \subseteq A$, it is always that case that $\emptyset \in \mathcal{P}(A)$ and that $A \in \mathcal{P}(A)$; note that these two elements $\emptyset$ and $A$ of $\mathcal{P}(A)$ are the same if $A=\emptyset$; cf. below.

For example, with $A=\{1,2,3\}$ and thus $\# A=3$, we look at 3 -bit strings, identify $1 \in A$ with the left most bit, $2 \in A$ with the middle bit, and $3 \in A$ with the right most bit, and list all 8 possible 3 -bit strings along with the corresponding elements of $A$, the corresponding subsets of $A$ and the resulting elements of the power set $\mathcal{P}(A)$ of $A$ :

| 3-bit <br> string |  | corresponding <br> element(s) of $A$ | corresponding <br> subset of $A$ |  | corresponding <br> element of $\mathcal{P}(A)$ |  |
| ---: | :--- | ---: | :--- | ---: | ---: | ---: |
| 000 | $\Longleftrightarrow$ | nothing in $A$ | $\leftrightarrow$ | $\emptyset \subseteq A$ | $\leftrightarrow$ | $\emptyset \in \mathcal{P}(A)$ |
| 001 | $\Longleftrightarrow$ | $3 \in A$ | $\leftrightarrow$ | $\{3\} \subseteq A$ | $\leftrightarrow$ | $\{3\} \in \mathcal{P}(A)$ |
| 010 | $\Longleftrightarrow$ | $2 \in A$ | $\leftrightarrow$ | $\{2\} \subseteq A$ | $\leftrightarrow$ | $\{2\} \in \mathcal{P}(A)$ |
| 011 | $\Longleftrightarrow$ | $2,3 \in A$ | $\leftrightarrow$ | $\{2,3\} \subseteq A$ | $\leftrightarrow$ | $\{2,3\} \in \mathcal{P}(A)$ |
| 100 | $\Longleftrightarrow$ | $1 \in A$ | $\leftrightarrow$ | $\{1\} \subseteq A$ | $\leftrightarrow$ | $\{1\} \in \mathcal{P}(A)$ |
| 101 | $\Longleftrightarrow$ | $1,3 \in A$ | $\leftrightarrow$ | $\{1,3\} \subseteq A$ | $\leftrightarrow$ | $\{1,3\} \in \mathcal{P}(A)$ |
| 110 | $\Longleftrightarrow$ | $1,2 \in A$ | $\leftrightarrow$ | $\{1,2\} \subseteq A$ | $\leftrightarrow$ | $\{1,2\} \in \mathcal{P}(A)$ |
| 111 | $\Longleftrightarrow$ | $1,2,3 \in A$ | $\leftrightarrow$ | $\{1,2,3\} \subseteq A$ | $\leftrightarrow$ | $\{1,2,3\}=A \in \mathcal{P}(A)$ |

[^0]Because this exhausts all possibilities for the elements of $\mathcal{P}(A)$, we find that

$$
\mathcal{P}(A)=\{\emptyset,\{1\},\{2\},\{3\},\{1,2\},\{1,3\},\{2,3\},\{1,2,3\}\}
$$

and that indeed $\# \mathcal{P}(A)=2^{3}=8$. Note that the element " 1 " of $A$ is very different from the set " $\{1\}$ " which is a subset of $A$ (that contains the element " 1 " of $A$ ) and thus an element of $\mathcal{P}(A)$. Also note that the notation $\emptyset$ chosen to denote the empty set looks somewhat unfortunate and that simply denoting it by an empty set \{\} could at this point be considered preferable (but see another example below ...).

With $A=\emptyset$ we find that $\mathcal{P}(A)=\{\emptyset\}$ : as noted, $\emptyset$ must be an element of $\mathcal{P}(A)$, and as also noted $A$ should be included as an element of $\mathcal{P}(A)$ as well but with $A=\emptyset$, the set $A$ has already been included by putting $\emptyset$ in the power set under construction. The set $A$ has no other subsets than $\emptyset$, so we cannot put anything else in $\mathcal{P}(A)$. Note that with $\# A=0$ (because $A$ is empty) we have that $\# \mathcal{P}(A)$ must be equal to $2^{0}=1$ (due to our earlier unproven counting argument), which is indeed what we found: $\mathcal{P}(A)$ is the set with as sole element the empty set. And, to rub it in yet again, if $A=\emptyset$, then $\# A=0$ because the empty set $\emptyset$ does not contain any elements. Illustrating this as done above, because $\# A=0$ we have to consider zero-bit strings, of which there is only one (namely, the empty string):

$$
-\Longleftrightarrow \text { nothing in } A \quad \leftrightarrow \quad \emptyset \subseteq A \quad \leftrightarrow \quad \emptyset=A \in \mathcal{P}(A)
$$

where above the _ you have to imagine the unique zero-bit string.

Now let $B=\mathcal{P}(A)=\{\emptyset\}$, and consider $\mathcal{P}(B)$. With $\# B=1$ (because $B$ is the set containing as sole element the empty set $\emptyset$ ) we know that $\# \mathcal{P}(B)=2^{1}=2$. We know that $\emptyset \in \mathcal{P}(B)$ and that $B=\{\emptyset\} \in \mathcal{P}(B)$. Because $\emptyset \neq\{\emptyset\}$ (the former is the empty set, the latter is the set containing as its sole element the empty set), these are two distinct sets and thus two distinct elements of $\mathcal{P}(B)$. Given that $\# \mathcal{P}(B)=2$ that is (apparently) all, so we find $\mathcal{P}(B)=\{\emptyset,\{\emptyset\}\}$. Illustrating this as above, we have $\# B=1$ and thus consider 1-bit strings (with the single bit identified with the single element $\emptyset$ of $B$ ):

$$
\begin{aligned}
& 0 \Longleftrightarrow \text { nothing in } B \quad \leftrightarrow \quad \emptyset \subseteq B \quad \leftrightarrow \quad \emptyset \in \mathcal{P}(B) \\
& 1 \Longleftrightarrow \quad \emptyset \in B \quad \leftrightarrow \quad\{\emptyset\} \subseteq B \quad \leftrightarrow \quad\{\emptyset\}=B \in \mathcal{P}(B)
\end{aligned}
$$

which indeed leads to $\mathcal{P}(B)=\{\emptyset,\{\emptyset\}\}$.

In a similar and only slightly more complicated manner we find that for $C=$ $\mathcal{P}(B)=\{\emptyset,\{\emptyset\}\}$ it is the case that

$$
\mathcal{P}(C)=\{\emptyset,\{\emptyset\},\{\{\emptyset\}\},\{\emptyset,\{\emptyset\}\}\}:
$$

because $\# C=2$ we consider 2-bit string, identify the left most bit with $\emptyset \in C$ and the right most bit with $\{\emptyset\} \in C$ and find:

$$
\begin{aligned}
& 00 \Longleftrightarrow \text { nothing in } C \quad \leftrightarrow \quad \emptyset \subseteq C \quad \leftrightarrow \quad \emptyset \in \mathcal{P}(C) \\
& 01 \Longleftrightarrow \quad\{\emptyset\} \in C \quad \leftrightarrow \quad\{\{\emptyset\}\} \subseteq C \quad \leftrightarrow \quad\{\{\emptyset\}\} \in \mathcal{P}(C) \\
& 10 \Leftrightarrow \quad \emptyset \in C \quad \leftrightarrow \quad\{\emptyset\} \subseteq C \quad \leftrightarrow \quad\{\emptyset\} \in \mathcal{P}(C) \\
& 11 \Longleftrightarrow \emptyset, \emptyset \emptyset\} \in C \quad \leftrightarrow \quad\{\emptyset,\{\emptyset\}\} \subseteq C \quad \leftrightarrow \quad\{\emptyset,\{\emptyset\}\}=C \in \mathcal{P}(C)
\end{aligned}
$$

This confirms (after modest reordering) that $\mathcal{P}(C)=\{\emptyset,\{\emptyset\},\{\{\emptyset\}\},\{\emptyset,\{\emptyset\}\}\}$. With $D=\mathcal{P}(C)$ you are invited to contemplate what the elements of $\mathcal{P}(D)$ look like ${ }^{3}$.

Using the 4-bit string correspondence to the 4 elements of $D$ may prove helpful and avoid mishaps with insufficiently many or too many curly braces.

What is this good for? So you understand, or at the very least "see", that when playing around with sets and power sets curly braces are relevant. It is also instructive to see how fast the number of pairs of curly braces grows. When using $\emptyset$ to denote the empty set, it is still 1 in $\mathcal{P}(A), 2$ in $\mathcal{P}(B)$, and 6 in $\mathcal{P}(C)$, it grows to 56 in $\mathcal{P}(D)$ with $\# \mathcal{P}(D)=16$, to $1867776=57 \times 2^{15}$ in $\mathcal{P}(\mathcal{P}(D))$ with $\# \mathcal{P}(\mathcal{P}(D))=2^{16}$, and to a number of 19735 decimal digits for $\mathcal{P}(\mathcal{P}(\mathcal{P}(D)))$ with $\# \mathcal{P}(\mathcal{P}(\mathcal{P}(D)))=2^{2^{16}}$. Later, during "counting", we may see the tools required to figure out a formula for this number of pairs of curly braces.

Sequences. Consult the book for a proper definition of a sequence (a function from the set of the natural numbers, or a bounded set of consecutive non-negative integers, to some other set). Here we just informally introduce sequences over the set of the real numbers (the set of real numbers is denoted by $\mathbf{R}$ ) as lists of real numbers with consecutive indices (starting at 0 , or at 1 , or at anything you like), such as $b_{0}, b_{1}, b_{2}, \ldots$ (if we start at index 0) or $b_{1}, b_{2}, b_{3}, \ldots$ (if we start at index 1), or whatever initial index works best for the context. A sequence may be finite and thus consist of just $n$ elements for some positive integer $n$ (in which case it looks like $b_{0}, b_{1}, b_{2}, \ldots, b_{n-1}$ or $b_{1}, b_{2}, b_{3}, \ldots, b_{n}$, or $\left.b_{m}, b_{m+1}, b_{m+2}, \ldots, b_{m+n-1}\right)$ or it may be infinite and we may write $b_{0}, b_{1}, b_{2}, \ldots$ as above, or $b_{m}, b_{m+1}, b_{m+2}$, $\ldots$ if we insist on starting at index $m$. To denote an element of a sequence, we may use $b_{i}$, or $b_{j}$, or $b_{k}$, or whatever index you find reasonable to use given the context for which you are using the sequence. A sequence may be denoted as $\left(b_{i}\right)_{i=0}^{\infty}$ if it is infinite or $\left(b_{i}\right)_{i=0}^{s}$ if it is finite and has $s+1$ terms. Elements of a sequence are often referred to as terms of the sequence.

There are many interesting infinite integer sequences. Sometimes the "pattern" of the sequence can easily be recognized (such as in $0,3,8,15,24,35,48,63, \ldots$ because it is simply $0 \times 2,1 \times 3,2 \times 4,3 \times 5,4 \times 6,5 \times 7,6 \times 8,7 \times 9, \ldots$ or, if you prefer, the squares minus one - can this be a coincidence?), for other sequences you may have trouble figuring out what the pattern is: check out the on-line encyclopedia of integer sequences (oeis.org) if you need to look up a sequence.

Common sequences. Below we use the set of natural numbers $\mathbf{N}=\{0,1,2, \ldots\}$ as the domain of the indices; this can easily be changed to any other infinite domain of consecutive integers. We revisited constant, arithmetic and geometric "progressions" (which is just another word for sequences), definitions that you have already seen in "Analyse I":

- If there exists a constant $c$ such that for all indices $i$ in the domain it is the case that $c_{i}=c$, then the sequence $\left(c_{i}\right)_{i=0}^{\infty}$ is a constant sequence.
- If there exists a constant $d$ such that for all relevant indices in the domain it is the case that $a_{i+1}-a_{i}=d$ (for some value of the initial term $a_{0}$ ), then the sequence $\left(a_{i}\right)_{i=0}^{\infty}$ is an arithmetic sequence. The number $d$ is the difference between the consecutive terms of the sequence. With $d=0$ we get the constant sequence again.
- If there exists a non-zero constant $r$ such that for all relevant indices in the domain it is the case that $\frac{g_{i+1}}{g_{i}}=r$ (for some non-zero value of the initial term $\left.g_{0}\right)$, then the sequence $\left(g_{i}\right)_{i=0}^{\infty}$ is a geometric sequence. The number $r$ is the ratio of the consecutive terms of the sequence. With $r=1$ we get the constant sequence again.

Recurrence relations. For an arithmetic sequence with difference $d$ it follows that $\underline{a_{n}=a_{n-1}+d}$ for any $n>0$ in the domain. And for a geometric sequence with ratio $r$ it follows that $\underline{g_{n}=r g_{n-1}}$ for any $n>0$ in the domain. Along with definitions of $a_{0}$ and $g_{0}$ these underlined so-called "recurrence relations" fully determine the terms of both sequences. Given these simple recurrence relations, it is easy to see (and it can be proved - but we won't do so yet) that for an arithmetic sequence with difference $d$ it is the case that $a_{n}=n d+a_{0}$, as arithmetic sequences were introduced in class (also in the book the latter is used as the definition, and it is called an arithmetic progression - it all boils down to the same). Similarly it is easy to see (and it can be proved - and again we won't do so yet) that for a geometric sequence with ratio $r$ it is the case that $g_{n}=g_{0} r^{n}$ (as we introduced them in class; again, also in the book this is the way a geometric progression is defined). These expressions for $a_{n}$ and $g_{n}$ are called closed formulas because they allow immediate computation of any term of the sequence, without having to calculate all the earlier terms first. Later in the course we will see how for (some) more complicated recurrence relations - such as $f_{n}=f_{n-1}+f_{n-2}$ for $n \geq 2$ and with $f_{0}=0$ and $f_{1}=1$, the Fibonacci sequence - closed formulas for the terms of the sequence can be derived.

Summations. In this lecture we considered the problem of deriving closed formulas for the sums of the first $n$ (or $n+1$ ) terms of constant, arithmetic, and geometric sequences, and for several other sequences as well: not just because this turns out to lead to useful exercises with the indices of summations, also because the resulting sums are used all over the place, for instance in the analysis of algorithms as we will see later in the course ${ }^{4}$.

Thus, we'd like to compute the sum $c_{0}+c_{1}+c_{2}+\ldots+c_{n-1}+c_{n}$ of the first $n+1$ terms of a constant sequence, the sum $a_{0}+a_{1}+a_{2}+\ldots+a_{n-1}+a_{n}$ of the first $n+1$ terms of an arithmetic sequence, and the sum $g_{0}+g_{1}+g_{2}+\ldots+g_{n-1}+g_{n}$ of the first $n+1$ terms of a geometric sequence; and quite possibly we'd like to compute other cute summations as well. Because such sums occur very often (for instance when you're trying to analyse computer programs, but also in basic counting, statistics, probability theory, etc., and actually all over the place in math), the more concise notations " $\sum_{i=0}^{n} c_{i} "$ ", " $\sum_{i=0}^{n} a_{i} "$ ", and " $\sum_{i=0}^{n} g_{i} "$ ", respectively, are used for them (this is by no means a formal definition of what " $\sum_{i=0}^{n} b_{i}$ " means, but intuitively it is clear enough; later we will see how the definition of the usage of the summation symbol $\sum$ can be done in a formally correct manner). In principle we can let $n$ go to infinity, but of the sequences seen so far that only makes sense for the geometric sequence with ratio $r$ satisfying $|r|<1$; we write $\sum_{i=0}^{\infty} g_{i}$. Although you are already supposed to be familiar with summation manipulations, the following two red remarks may be useful.

Summation indices and their scope. In the summation notation " $\sum_{i=0}^{n} b_{i}$ " the " $i$ " is just a formal index: it may be replaced by any other index, as long as it is done consistently. Thus, for instance, $\sum_{i=0}^{n} b_{i}=\sum_{j=0}^{n} b_{j}=\sum_{k=0}^{n} b_{k}$. But " $\sum_{i=0}^{n} b_{j}$ " does not make sense, unless $j$ is, in that context, some known entity - but if it is, then in $\sum_{i=0}^{n} b_{j}$ the value $b_{j}$ does not depend on the summation index $i$ and can thus be pulled out of the sum, so that $\sum_{i=0}^{n} b_{j}=b_{j} \sum_{i=0}^{n} 1$ which equals $b_{j}(n+1)$ for the simple reason that $\sum_{i=0}^{n} 1=n+1$ (here we are using

that $b_{j}+b_{j}+\ldots+b_{j}=b_{j}(1+1+\ldots+1)$; this can use a real proof). On the other hand, $b_{i}$ cannot be pulled out of the sum $\sum_{i=0}^{n} b_{i}$ because $b_{i}$ depends on the summation index $i$ - which only exists within the scope of the summation symbol, and not before it: $b_{i} \sum_{i=0}^{n} 1$ in normal circumstances does not make sense, and if it makes sense it is an example of very poorly chosen notation (namely, to use $i$ simultaneously as global index value for $b_{\ldots} .$. and as summation index).

Shifting up and down ranges of summation indices. Also note that in $\sum_{i=0}^{n} b_{i}$ one may shift the summation range (here $[0, n]$ ) by any value that one finds convenient, as long as it contains the same number of elements as $[0, n]$ (thus $n+1$ for $[0, n])$ : for instance, if it is more convenient to start the summation at 1 instead of 0 , one simply shifts by one and gets the same sum $\sum_{i=1}^{n+1} b_{i-1}$ which still expresses $b_{0}+b_{1}+\ldots+b_{n}$ - note that the summation variable is shifted up by one, and that the corresponding index $i$ in $b_{i}$ must therefore be shifted down by one to $b_{i-1}$ to make sure that the same sequence elements are included in the sum.

Similarly, without changing the value of the sum one may write $\sum_{i=k}^{n+k} b_{i-k}$ for any integer $k$ and thus also $\sum_{i=-k}^{n-k} b_{i+k}$, or $\sum_{j=-6 \ell}^{n-6 \ell} b_{j+6 \ell}$ (for any $\ell \in \frac{1}{6} \mathbf{Z}$ ), or $\sum_{k=m}^{n+m} b_{k-m}$ (for any $m \in \mathbf{Z}$ ). Just make sure that the choices of summation indices do not cause misunderstanding with other existing variables, and use common sense.

An interesting point was raised in class: if in $\sum_{i=0}^{n} b_{i}$ the term $b_{i}$ is not just a function of $i$ but of $n$ as well, thus $\sum_{i=0}^{n} b_{i}=\sum_{i=0}^{n} f(i, n)$ for some function $f$, then if we change the summation range as above from $[0, n]$ to $[k, n+k]$ and thus the indexed term $b_{i}$ to $b_{i-k}$, does this change the parameter $n$ in the call to $f$ ? Look at the terms that are being summed to convince yourself that $b_{i-k}=f(i-k, n)$ (for the $i$-values in the new range $[k, n+k]$ ) and that the parameter $n$ in the call to $f$ is not affected: $\sum_{i=0}^{n} f(i, n)=\sum_{i=k}^{n+k} f(i-k, n)$.

In class we considered the summation of a constant sequence, the summation of the sequence $a_{i}=\frac{1}{i(i+1)}$ (for $i \geq 1$ ), the geometric sequence, and had a very brief look at the most common summation, that of the arithmetic sequence. To practice a bit more with summations and their indices and ranges, during the next lecture we will see more ways to solve the summation of an arthmetic sequence, and we will have a look at the summation of the non-arithmetic, non-geometric sequence $b_{i}=i r^{i-1}($ for $i \geq 1)$.

Summation of a constant sequence. As already implied by the paragraph above, if there is a constant $c$ such that $c_{i}=c$ for all indices $i$ in the domain $\{0,1,2, \ldots\}$, then $\sum_{i=0}^{n} c$ is just the sum of $n+1$ terms each of which is equal to $c$, so the sum equals $(n+1) c$.

Summation of the sequence $a_{i}=\frac{1}{i(i+1)}$ (for $i \geq 1$ ). This summation introduces the telescoping trick. First note that if we write $\frac{1}{i(i+1)}=\frac{x}{i}+\frac{y}{i+1}$ we get that $\frac{1}{i(i+1)}=$ $\frac{x(i+1)+y i}{i(i+1)}=\frac{x+(x+y) i}{i(i+1)}$. The numerator 1 of $\frac{1}{i(i+1)}$ must be equal to the numerator $x+(x+y) i$ of $\frac{x+(x+y) i}{i(i+1)}$ for all integers $i \geq 1$, thus we find that $x+y=0$ and $x=1$ and thus that $y=-1$. It follows that $\sum_{i=1}^{n} a_{i}=\sum_{i=1}^{n} \frac{1}{i(i+1)}=\sum_{i=1}^{n}\left(\frac{1}{i}-\frac{1}{i+1}\right)$.

Informally, one sees right away that the negative part $-\frac{1}{i+1}$ of the term for $i$ cancels against the positive part $\frac{1}{i+1}$ of the term for $i+1$, so all that remains is the positive part $\frac{1}{1}$ of the term for $i=1$ and the negative part $-\frac{1}{n+1}$ of the last term (for $i=n$ ): this effect is called telescoping. This leads right away to the result that $\sum_{i=1}^{n} a_{i}=\sum_{i=1}^{n} \frac{1}{i(i+1)}=1-\frac{1}{n+1}=\frac{n}{n+1}$.

During the lecture we formally proved the telescoping: $\sum_{i=1}^{n} a_{i}=\sum_{i=1}^{n}\left(\frac{1}{i}-\right.$ $\left.\frac{1}{i+1}\right)=\left(\sum_{i=1}^{n} \frac{1}{i}\right)-\left(\sum_{i=1}^{n} \frac{1}{i+1}\right)$. We pull the first term out of the first summation and the last term out of the second summation, and thus get $\sum_{i=1}^{n} a_{i}=\frac{1}{1}+$ $\left(\sum_{i=2}^{n} \frac{1}{i}\right)-\left(\sum_{i=1}^{n-1} \frac{1}{i+1}\right)-\frac{1}{n+1}$ and therefore $\sum_{i=1}^{n} a_{i}=\frac{1}{1}-\frac{1}{n+1}+\left(\sum_{i=2}^{n} \frac{1}{i}\right)-$ $\left(\sum_{i=1}^{n-1} \frac{1}{i+1}\right)$. The two remaining sums now cancel against each other. During the lecture we showed this by rewriting the second summation as $\sum_{j=2}^{n} \frac{1}{j}$ (which indeed cancels against the first summation after renaming $j$ again as $i$ ). We could also have rewritten the first summation as $\sum_{j=1}^{n-1} \frac{1}{j+1}$ (which indeed cancels against the second summation after renaming $j$ again as $i$ ).

Summation of geometric sequence. As seen above, we may assume that the $i$-th term $g_{i}$ of a geometric sequence equals $g_{0} r^{i}$, for some constant $g_{0}$ and ratio $r$. We are interested in a closed form expression for $\sum_{i=0}^{n} g_{i}$, where for relevant values of $r$ it may even make sense to talk about the value of $\sum_{i=0}^{\infty} g_{i}$. Because

$$
\sum_{i=0}^{n} g_{i}=\sum_{i=0}^{n} g_{0} r^{i}=g_{0} \sum_{i=0}^{n} r^{i}
$$

the value $g_{0}$ is just an uninteresting multiplicative factor, and we omit it (i.e., from now on we assume that $g_{0}=1$; note that the entire sum equals zero if $g_{0}=0$ ). Obviously, the problem is not interesting if $r=1$ : then we get (with $g_{0}=1$ ) that

$$
\sum_{i=0}^{n} g_{i}=\sum_{i=0}^{n} r^{i}=\sum_{i=0}^{n} 1^{i}=\sum_{i=0}^{n} 1=n+1
$$

Also $r=-1$ is not so inspiring: we get 0 is $n$ if odd and 1 if $n$ is even; but the final arguments below work for $r=-1$ as well, so $r=-1$ is not excluded below.

Assuming $r \neq 1$, we'd like to find a closed form expression for $\sum_{i=0}^{n} r^{i}$, i.e., for

$$
r^{0}+r^{1}+\ldots+r^{n-2}+r^{n-1}+r^{n}
$$

But note that we are already very familiar with a similar sum, namely

$$
r^{n}+r^{n-1}+r^{n-2}+\ldots+r^{1}+r^{0}
$$

which is just the same, but in the reverse order (and indeed, these expressions are the same - this can even be proved formally, but we won't worry about that now). How come we are familiar with something like $r^{n}+r^{n-1}+r^{n-2}+\ldots+r^{1}+r^{0}$ ? Just look at the first footnote on page 4 of the October 9 lecture notes (the $k$ there corresponds to $n+1$ here). Or just look at the decimal number $111 \ldots 11$ that consists of $n+1$ ones: that is precisely the same as our expression $r^{n}+r^{n-1}+r^{n-2}+\ldots+r^{1}+r^{0}$ if we assume that $r=10$ (the basis or radix of our decimal number system) because our decimal number $111 \ldots 11$ is just a convenient shorthand notation for

$$
1 \times 10^{n}+1 \times 10^{n-1}+1 \times 10^{n-2}+\ldots+1 \times 10^{1}+1 \times 10^{0}:
$$

that is how the value of a number in decimal notation is defined (and be glad we use the shorthand notation in daily life), where the present case is particularly simple because all the digits are equal to one.

Taking for instance $n=4$, we find the number 11111, and we know that if we multiply it by 9 (which was carefully chosen as $10-1$, i.e., as $r-1$ ) we get, without any effort, 99999, so that if we add one we get 100000 , for which we have the nice closed form expression $10^{5}$ (i.e., $r^{n+1}$ ). We thus found that

$$
(11111 \times 9)+1=10^{5}
$$

and more in general that

$$
(\underbrace{111 \ldots 11}_{n+1 \text { ones }} \times 9)+1=10^{n+1}
$$

or even more in general that

$$
(\underbrace{111 \ldots 11}_{n+1 \text { ones }} \times(r-1))+1=r^{n+1}
$$

where the final $111 \ldots 11$ should be liberally interpreted as a shorthand notation for $r^{n}+r^{n-1}+r^{n-2}+\ldots+r^{1}+r^{0}$ and where we use that 10 was just a placeholder for $r$ and thus that 9 was a placeholder for $r-1$. This final expression leads us to believe that

$$
\underline{\left(r^{n}+r^{n-1}+r^{n-2}+\ldots+r^{1}+r^{0}\right) \times(r-1)}+1=r^{n+1}
$$

and thus that

$$
r^{n}+r^{n-1}+r^{n-2}+\ldots+r^{1}+r^{0}=\frac{r^{n+1}-1}{r-1}
$$

(where you should remember that indeed $r \neq 1$ ). But this is precisely the closed formula for $\sum_{i=0}^{n} r^{i}$ that we were trying to find, so we're done - except we have not proved anything yet other than by intimidation.

To actually prove this result that

$$
\sum_{i=0}^{n} r^{i}=\frac{r^{n+1}-1}{r-1}
$$

if $r \neq 1$, have a look at the underlined part

$$
\left(r^{n}+r^{n-1}+r^{n-2}+\ldots+r^{1}+r^{0}\right) \times(r-1)
$$

of the equation above: apparently we need to prove that this underlined part is equal to $r^{n+1}-1$. Pulling the factor $r-1$ inside the parentheses we get

$$
(r-1) r^{n}+(r-1) r^{n-1}+(r-1) r^{n-2}+\ldots+(r-1) r^{1}+(r-1) r^{0}
$$

and thus

$$
r^{n+1}-r^{n}+r^{n}-r^{n-1}+r^{n-1}-r^{n-2}+\ldots+r^{2}-r^{1}+r^{1}-r^{0} .
$$

This is yet another example of our earlier telescoping sum: all the intermediate terms cancel each other, and all that remains are the first and the last term, i.e., $r^{n+1}-r^{0}$ which in turn is equal to $r^{n+1}-1$ (where we use that $r^{0}=1$ ): we find that indeed the underlined part equals $r^{n+1}-1$, more or less proving what we believed to be the case: "more or less" because we used a somewhat vague handwaving argument involving informal usage of "...". To get a proper proof this argument should be made in a clean manner using summations and index manipulations: that is done in the book, and it is done above as well (while we were telescoping for the calculation of $\left.\sum_{i=1}^{n} \frac{1}{i(i+1)}\right)$, but you may nevertheless try for yourself that you can indeed get this to work. If you have trouble doing this, ask one of the AEs to help you!

In any case, the conclusion is that if $r \neq 1$ then

$$
\sum_{i=0}^{n} r^{i}=\frac{r^{n+1}-1}{r-1}
$$

for any integer $n \geq 0$. It follows that if $|r|<1$ we have that

$$
\sum_{i=0}^{\infty} r^{i}=\frac{1}{1-r}
$$

because for $n \rightarrow \infty$ the term $r^{n+1} \rightarrow 0$.

We also proved the latter result (for $|r|<1$ ) in the following manner. Let $S=\sum_{i=0}^{\infty} r^{i}$, then $S=r^{0}+\sum_{i=1}^{\infty} r^{i}$ (split off the first term) and thus $S=1+$ $\sum_{i=0}^{\infty} r_{i=1}^{i+1}=1+r \sum_{i=0}^{\infty} r^{i}=1+r S$. It follows that $S-r S=1$ and thus that $S=\frac{1}{1-r}$. A student raised the point that we don't know that $S$ exists, which is a valid concern. This can easily be fixed, at little additional effort. Just define, for any integer $n \geq 0$ and any $r \neq 1$ the sum $S_{n}$ as $\sum_{i=0}^{n} r^{i}$, then $S_{n}=r^{0}+\sum_{i=1}^{n} r^{i}$ (split off the first term) and thus $S_{n}=1+\sum_{i=0}^{n-1} r^{i+1}=1+r \sum_{i=0}^{n-1} r^{i}$. The latter sum does not go "far enough" to replace it again by $S_{n}$ (as in the previous, more careless "proof"), thus we add the missing term for $n$ in the sum, and subtract it again: $S_{n}=1+\left(r \sum_{i=0}^{n} r^{i}\right)-r^{n+1}$. It follows that $S_{n}=1+r S_{n}-r^{n+1}$ and thus that $S_{n}=\frac{1-r^{n+1}}{1-r}$. For $|r|<1$ we can now let $n$ go to $\infty$, if desired.

Summation of an arithmetic sequence: difference of squares method. We concluded with a quick telescoping method to compute $T_{n}=\sum_{i=0}^{n} i$. This is a useful approach because it leads to a neat generalization. It was observed that $(i+1)^{2}-i^{2}=2 i+1$ (you should be able to check that this is the case, by calculating $\left.(i+1)^{2}\right)$, so that

$$
\sum_{i=0}^{n}\left((i+1)^{2}-i^{2}\right)=\sum_{i=0}^{n}(2 i+1)
$$

and therefore that

$$
\sum_{i=0}^{n}\left((i+1)^{2}-i^{2}\right)=2 T_{n}+n+1
$$

(because $\left.\sum_{i=0}^{n}(2 i+1)=\sum_{i=0}^{n} 2 i+\sum_{i=0}^{n} 1=2 \sum_{i=0}^{n} i+n+1=2 T_{n}+n+1\right)$. Although the sum $\sum_{i=0}^{n}\left((i+1)^{2}-i^{2}\right)$ on the left hand side looks, at first glance, thoroughly unappealing, it is actually a very simple matter to calculate this sum. Look at its term for $i=n$ : it is $(n+1)^{2}-n^{2}$; and look at its term for $i=n-1$, which is $n^{2}-(n-1)^{2}$. Adding the two, you find that the " $-n^{2}$ " for $i=n$ gets

for $i=n-1$ gets gobbled up by the " $(n-1)^{2}$ " for $i=n-2$, etc: the negative part of each term cancels with the positive part of its predecessor term. This is another example of the telescoping trick: all that remains after "squashing it all together" is the positive part of the term for $i=n$ and the negative term for $i=0$ - which in the present case equals zero. Thus, we find that

$$
\sum_{i=0}^{n}\left((i+1)^{2}-i^{2}\right)=(n+1)^{2}
$$

during the last minute of the lecture I managed to first write $n^{2}$ for the right hand side, which I then corrected to $(n-1)^{2}$ - only after the lecture a student pointed out that it should have been $(n+1)^{2}$, which is indeed the case. Anyway, from the correct version with $(n+1)^{2}$ we find

$$
(n+1)^{2}=2 T_{n}+n+1
$$

and thus

$$
(n+1)^{2}-(n+1)=2 T_{n}
$$

and therefore $(n+1)((n+1)-1)=2 T_{n}$ and finally $\frac{(n+1) n}{2}=T_{n}$.

In class we did not do the telescoping argument more formally by exercising with summation indices. Here is how that would go:

$$
\sum_{i=0}^{n}\left((i+1)^{2}-i^{2}\right)=\sum_{i=0}^{n}(i+1)^{2}-\sum_{i=0}^{n} i^{2}=(n+1)^{2}+\sum_{i=0}^{n-1}(i+1)^{2}-\sum_{i=1}^{n} i^{2}=\ldots
$$

(note that in the final sum the term for $i=0$ is dropped because it is zero). Now, in $\sum_{i=0}^{n-1}(i+1)^{2}$ substitute $j=i+1$ for $i$ (thus $j=1$ if $i=0$ and $j=n$ if $i=n-1$ ), so that $\sum_{i=0}^{n-1}(i+1)^{2}=\sum_{j=1}^{n} j^{2}$, and thus (replacing $j$ by $i$ again) $\sum_{i=0}^{n-1}(i+1)^{2}=\sum_{i=1}^{n} i^{2}$. Using this where we left of with the $\ldots$ we find

$$
\ldots=(n+1)^{2}+\sum_{i=1}^{n} i^{2}-\sum_{i=1}^{n} i^{2}=(n+1)^{2}
$$

which completes the argument: note that the positive term " $+\sum_{i=1}^{n} i^{2 "}$ is cancelled due to the negative but otherwise identical term " $-\sum_{i=1}^{n} i^{2}$ ".

What is particularly nice about this telescoping trick is that it can be used to find an expression in closed form for $\sum_{i=0}^{n} i^{k}$ if closed form expressions are given for $\sum_{i=0}^{n} i^{\ell}$ for $0 \leq \ell<k$. In the exercises you are invited to do this for $k=2$. Note that this summation for $k=2$ does not involve an arithmetic sequence: it is the sum of the first $n+1$ squares, which is not the sum of an arithmetic sequence. Once you have a closed form expression for $\sum_{i=0}^{n} i^{2}$ you can go for the sum $\sum_{i=0}^{n} i^{3}$ of the cubes (for which you have already proved an identity during Analyse I, par récurrence), to the sum $\sum_{i=0}^{n} i^{4}$ of the fourth powers, etc. So, in the exercises you are also invited to do this for $k=3$, and if you like even for $k=4$.

Next lecture. More ways to compute $\sum_{i=0}^{n} i$, how to compute $\sum_{i=1}^{n} i r^{i-1}$, and then we discuss cardinalities and countability, and may start talking about algorithms and consider what we can and cannot calculate.


[^0]:    ${ }^{1}$ This is because it involves six sets and 6 is not a divisor of $2^{6}-2$; if the number of sets is $p$ for a prime $p$ a symmetric picture is not a priori excluded because a prime $p$ always divides $2^{p}-2$.

    ${ }^{2} \mathrm{~A}$ set $B$ is a subset of a set $A$ if $\forall x(x \in B \rightarrow x \in A)$ which, as we have seen, we can also write as $\forall x \in B x \in A$; we write $B \subseteq A$ or $A \supseteq B$. A set $B$ is a proper subset of a set $A$ if $B$ is a subset of $A$ and $\exists x(x \in A \wedge x \notin B)$ which, as we have seen, we can also write as $\exists x \in A x \notin B$; we write $B \subset A$ or $A \supset B$. Note the correspondence with $\leq$ and $<$ and, again, the difference with the French notation.

