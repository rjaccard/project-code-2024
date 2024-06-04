Mathematical and strong induction can be used to prove a wide range of results: not just equalities, but also inequalities and all kinds of other statements. What induction can, in general, not be used for is to derive the results to be proved: finding those results is quite another matter (for several examples this was shown in earlier lectures).

There are lots of really smart \& tricky proofs that use mathematical induction, some of which you can find in the exercises in the book. Although the subject has already been treated extensively (at Analyse I and during the exercise sessions), below even more (more or less mechanically derived) proofs by mathematical induction are spelled out, ad nauseam. During the lecture only one of the proofs below was presented.

The basis of the induction. If one uses $\mathbf{N}=\{0,1,2, \ldots\}$ as the domain when proving that " $\forall n P(n)$ ", then the first value $n$ for which $P(n)$ must be proved true, and which represents the basis step, must be $n=0$; correspondingly, the inductive step consists of proving that $P(k) \rightarrow P(k+1)$ for all integers $k \geq 0$. In the book mathematical induction is introduced with as basis step the verification (or proof) that $P(1)$ is true and, correspondingly, an induction step consisting of proving that $P(k) \rightarrow P(k+1)$ for all integers $k \geq 1$. The starting point $b \in \mathbf{Z}$ for your induction proofs depends on the result that you want to prove; keep in mind, however, that the corresponding induction step " $P(k) \rightarrow P(k+1)$ " must be proved for all $k \geq b$ where $b$ is the smallest element of the domain of the $n$-values for which $P(n)$ must be proved.

General framework for proofs using mathematical induction. Proving results using induction may look elementary, and indeed it often is elementary, but it turns out that there are many creative ways to get it wrong. You may find the template in the book useful, in the seventh edition right before the exercises of Section 5.1, in the eighth edition in Section 5.1.5: we try to stick to that general framework because it is common to all valid proofs by mathematical induction and simply doing so (i.e., sticking to this framework) already removes a large part of the complexity of deriving a correct proof using mathematical induction.

(1) State the propositional function $P(n)$ to be proved and the domain to be used. Normally $P(n)$ is a formula or statement that (allegedly) holds for all integers $n \geq b$ for some lower bound $b$. It is helpful to write down what the formula or statement $P(n)$ precisely looks like for general $n \geq b$.

(2) State the basis step, i.e., what the formula or statement $P(b)$ looks like, and prove that the formula or statement holds.

(3) State what the inductive step consists of:

(a) State the inductive hypothesis, i.e., the assumption that $P(k)$ holds for an arbitrary integer $k$ in the domain. It is helpful to write down what the formula or statement $P(k)$ precisely looks like and that it is assumed that it holds for the arbitrarily chosen $k$.

(b) State what needs to be proved, namely that $P(k+1)$ holds: it is helpful to write down what the formula or statement $P(k+1)$ precisely looks like and that it must be proved that it holds, under the assumption of the induction hypothesis.

(c) Prove that $P(k+1)$ holds, clearly indicating at what place(s) the induction hypothesis is used (this may be at more than a single point), while making sure that the proof is valid for all values of $k$ in the domain, including $k=b$ : in particular boundary cases can be tricky.

(4) State the conclusion of the inductive step, namely that for any arbitrarily chosen $k$ in the domain it is the case that $P(k+1)$ follows from $P(k)$.

(5) State the overall conclusion based on the correctness of the basis step and the inductive step.

In particular when sticking to this framework, proofs by induction may not exactly be the most exciting part of mathematics. Indeed, often authors just dismissively write "this can be proved by induction", and then omit the proof. Nevertheless, you should be thoroughly familiar with this simple proof technique, which is why there are plenty of examples in these notes.

Proofs using mathematical induction. Below several mathematical induction proofs are presented that, rather rigidly, precisely follow the above framework.

Proving that $n<2^{n}$ for $n \in \mathbf{Z}_{\geq 0}$.

(1) Let $P(n)$ be the proposition

$$
\begin{equation*}
n<2^{n} \tag{1}
\end{equation*}
$$

where $n$ is a nonnegative integer. We want to prove " $\forall n \geq 0 P(n)$ " where $n \in \mathbf{N}=\{0,1,2, \ldots\}$, the set of nonnegative natural numbers. Thus, the domain is $\mathbf{N}$, and we have that $b=0$, with $b$ as above.

(2) The basis step consists of proving that $P(b)$ holds, where $P(b)$ is the statement

$$
\begin{equation*}
0<2^{0} \tag{2}
\end{equation*}
$$

which is derived from statement (1) by replacing $n$ by $b=0$. Because the right hand side of statement (2) evaluates to one, and because one is larger than the left hand side (which is zero), the statement $P(b)$ indeed holds. It follows that the basis step is correct.

(3) The inductive step:

(a) We make the induction hypothesis that $P(k)$ holds for an arbitrary integer $k$ in the domain. Thus, the induction hypothesis is the assumption that for an arbitrary integer $k \geq b=0$ it is the case that

$$
\begin{equation*}
k<2^{k} \tag{3}
\end{equation*}
$$

this statement is derived from statement (1) by replacing $n$ by $k$.

(b) We must prove that $P(k+1)$ holds, i.e., it must be proved that it is the case that

$$
\begin{equation*}
k+1<2^{k+1} \tag{4}
\end{equation*}
$$

this equation is derived from statement (1) by replacing $n$ by $k+1$.

(c) To prove that $P(k+1)$ holds, i.e., that statement (4) is correct, we try to recognize "what we know" (or, actually, assume to be correct), namely the Induction Hypothesis given by statement (3), in what we must prove, namely statement (4). So, we know (or assume) that $k<2^{k}$, and want to show that $k+1<2^{k+1}$. In the present case it is not hard to recognize $k<2^{k}$ in $k+1<2^{k+1}$, because $2^{k+1}=$ $2^{1} \times 2^{k}=2^{k}+2^{k}$, so $k+1<2^{k+1}$ is equivalent to $k+1<2^{k}+2^{k}$ in which $k<2^{k}$ is easily recognized: $k+1<2^{k}+2^{k}$.

Assuming the correctness of the Induction Hypothesis (statement (3) that $\left.k<2^{k}\right)$, it follows that in order to show that $k+1<2^{k+1}$ it suffices to show that $1 \leq 2^{k}$, where $k \geq 0$. We know that that is the case ${ }^{1}$, so $k+1<2^{k+1}$, which is statement (4). Therefore the correctness of statement (4) follows from the Induction Hypothesis (3). This completes the inductive step.

(4) It follows from the inductive step that $P(k+1)$ follows from $P(k)$ for any arbitrarily chosen integer $k \geq b=0$.

(5) Based on the basis step and the inductive step and the principle of mathematical induction, it follows that $\forall n \geq 0 P(n)$.

Sum of squares. Suspecting (based on an independent analysis, for instance using the telescoping method that we have seen several weeks ago) that the sum of the[^0]squares of the integers up to and including $n$ equals $\frac{n(n+1)(2 n+1)}{6}$, here is how that formula can be proved to be correct using mathematical induction.

(1) Let $P(n)$ be the statement

$$
\begin{equation*}
\sum_{i=0}^{n} i^{2}=\frac{n(n+1)(2 n+1)}{6} \tag{5}
\end{equation*}
$$

where $n$ is a nonnegative integer. We want to prove " $\forall n \geq 0 P(n)$ " where $n \in \mathbf{N}=\{0,1,2, \ldots\}$, the set of nonnegative natural numbers. Thus, the domain is $\mathbf{N}$, and we have that $b=0$, with $b$ as above.

(2) The basis step consists of proving that $P(b)$ holds, where $P(b)$ is the statement

$$
\begin{equation*}
\sum_{i=0}^{0} i^{2}=\frac{0(0+1)(2 * 0+1)}{6} \tag{6}
\end{equation*}
$$

which is derived from Equation (5) by replacing $n$ by $b=0$. Because the left hand side and right hand side of Equation (6) both evaluate to zero and are therefore equal, the statement $P(b)$ indeed holds. It follows that the basis step is correct.

(3) The inductive step:

(a) We make the induction hypothesis that $P(k)$ holds for an arbitrary integer $k$ in the domain. Thus, the induction hypothesis is the assumption that for an arbitrary integer $k \geq b=0$ it is the case that

$$
\begin{equation*}
\sum_{i=0}^{k} i^{2}=\frac{k(k+1)(2 k+1)}{6} \tag{7}
\end{equation*}
$$

this equation is derived from Equation (5) by replacing $n$ by $k$.

(b) We must prove that $P(k+1)$ holds, i.e., it must be proved that it is the case that

$$
\begin{equation*}
\sum_{i=0}^{k+1} i^{2}=\frac{(k+1)((k+1)+1)(2(k+1)+1)}{6} \tag{8}
\end{equation*}
$$

this equation is derived from Equation (5) by replacing $n$ by $k+1$.

(c) To prove that $P(k+1)$ holds, i.e., that Equation (8) is correct, we try to recognize "what we know" (or, actually, assume to be correct), namely Equation (7), in what we must prove, namely Equation (8). So, we know (or assume) something about $\sum_{i=0}^{k} i^{2}$, and want to know something about $\sum_{i=0}^{k+1} i^{2}$. Finding the relation between these two is not difficult, because $\sum_{i=0}^{k+1} i^{2}=\left(\sum_{i=0}^{k} i^{2}\right)+(k+1)^{2}$. With the induction hypothesis (Equation (7)) this becomes

$$
\sum_{i=0}^{k+1} i^{2}=\frac{k(k+1)(2 k+1)}{6}+(k+1)^{2}
$$

and therefore we know that as a consequence of the induction hypothesis it is the case that

$$
\begin{equation*}
\sum_{i=0}^{k+1} i^{2}=\frac{k+1}{6}(k(2 k+1)+6(k+1)) \tag{9}
\end{equation*}
$$

Because Equation (8), which must be proved, can trivially be rewritten as

$$
\sum_{i=0}^{k+1} i^{2}=\frac{k+1}{6}(((k+1)+1)(2(k+1)+1))
$$

and because $k(2 k+1)+6(k+1)=2 k^{2}+7 k+6$ and $((k+1)+1)(2(k+1)+$ 1) $=2 k^{2}+7 k+6$ are equal, the correctness of Equation (8) follows from the assumption that Equation (9) is correct (which in turn is based on the induction hypothesis). This completes the inductive step.

(4) It follows from the inductive step that $P(k+1)$ follows from $P(k)$ for any arbitrarily chosen integer $k \geq b=0$.

(5) Based on the basis step and the inductive step and the principle of mathematical induction, it follows that $\forall n \geq 0 P(n)$.

Number of subsets. As shown in the book, mathematical induction can be used to proved that the number of subsets of a finite set $A$ equals $2^{\# A}$. Thus, for finite $A$ the cardinality of the power set $\mathcal{P}(A)$ of $A$ equals $2^{\# A}$.

Alternating sum of $\left(-\frac{1}{2}\right)^{j}$. We use induction to prove that for any integer $n \geq 0$ it is the case that

$$
\sum_{j=0}^{n}\left(-\frac{1}{2}\right)^{j}=\frac{2^{n+1}+(-1)^{n}}{3 \cdot 2^{n}}
$$

(1) Let $P(n)$ be the statement

$$
\begin{equation*}
\sum_{j=0}^{n}\left(-\frac{1}{2}\right)^{j}=\frac{2^{n+1}+(-1)^{n}}{3 \cdot 2^{n}} \tag{10}
\end{equation*}
$$

where $n$ is a nonnegative integer. We want to use mathematical induction to show that " $\forall n \geq 0 P(n)$ ", where $n$ is a nonnegative integer. Thus the domain is the set $\mathbf{N}$ of natural integers and we have that $b=0$, with $b$ as above.

(2) The basis step consists of proving that $P(b)$ holds, where $P(b)$ is the statement

$$
\begin{equation*}
\sum_{j=0}^{0}\left(-\frac{1}{2}\right)^{j}=\frac{2^{0+1}+(-1)^{0}}{3 \cdot 2^{0}} \tag{11}
\end{equation*}
$$

which is derived from Statement (10) by replacing $n$ by $b=0$. Because the right hand side of Statement (11) evaluates to $\frac{2+1}{3 \cdot 1}=\frac{3}{3}=1$ which equals the left hand side $\left(-\frac{1}{2}\right)^{0}=1$ of Statement (11), the statement $P(b)$ indeed holds. It follows that the basis step is correct.

(3) The inductive step:

(a) We make the induction hypothesis that $P(k)$ holds for an arbitrary integer $k$ in the domain. Thus, the induction hypothesis is the assumption that for an arbitrary integer $k \geq b=0$ it is the case that

$$
\begin{equation*}
\sum_{j=0}^{k}\left(-\frac{1}{2}\right)^{j}=\frac{2^{k+1}+(-1)^{k}}{3 \cdot 2^{k}} \tag{12}
\end{equation*}
$$

this statement is derived from Statement (10) by replacing $n$ by $k$.

(b) We must prove that $P(k+1)$ holds, i.e., it must be proved that it is the case that

$$
\begin{equation*}
\sum_{j=0}^{k+1}\left(-\frac{1}{2}\right)^{j}=\frac{2^{k+1+1}+(-1)^{k+1}}{3 \cdot 2^{k+1}} \tag{13}
\end{equation*}
$$

this statement is derived from Statement (14) by replacing $n$ by $k+1$.
(c) To prove that $P(k+1)$ holds, i.e., that Statement (13) is correct, we try to recognize "what we know" (or, actually, assume to be correct), namely Equation (12), in what we must prove, namely Equation (13). So, we know (or assume) something about $\sum_{j=0}^{k}\left(-\frac{1}{2}\right)^{j}$, and want to know something about $\sum_{j=0}^{k+1}\left(-\frac{1}{2}\right)^{j}$. Finding the relation between these two is not difficult, because $\sum_{j=0}^{k+1}\left(-\frac{1}{2}\right)^{j}=\left(\sum_{j=0}^{k}\left(-\frac{1}{2}\right)^{j}\right)+$ $\left(-\frac{1}{2}\right)^{k+1}$. With the induction hypothesis (Equation (12)) this becomes

$$
\sum_{j=0}^{k+1}\left(-\frac{1}{2}\right)^{j}=\frac{2^{k+1}+(-1)^{k}}{3 \cdot 2^{k}}+\left(-\frac{1}{2}\right)^{k+1}
$$

and therefore we know that as a consequence of the induction hypothesis it is the case that

$$
\begin{aligned}
\sum_{j=0}^{k+1}\left(-\frac{1}{2}\right)^{j} & =\frac{2^{k+1}+(-1)^{k}}{3 \cdot 2^{k}}+\frac{(-1)^{k+1}}{2^{k+1}} \\
& =\frac{2^{k+2}+2(-1)^{k}}{3 \cdot 2^{k+1}}+\frac{3(-1)^{k+1}}{3 \cdot 2^{k+1}} \\
& =\frac{2^{k+2}+(-1)^{k+1}}{3 \cdot 2^{k+1}}
\end{aligned}
$$

where we use that $2(-1)^{k}=-2(-1)^{k+1}$. Because the last expression is the same as the right hand side of Equation (13), the correctness of Equation (13) follows. This completes the inductive step.

(4) It follows from the inductive step that $P(k+1)$ follows from $P(k)$ for any arbitrarily chosen integer $k \geq b=0$.

(5) Based on the basis step and the inductive step and the principle of mathematical induction, it follows that $\forall n \geq 0 P(n)$.

Divisibility example. Mathematical induction is a useful and common tool to prove formulas about summations (we will see some important ones later), but can be used to prove a much wider variety of results. During the lecture we saw the example of the divisibility result below.

We say that an integer $m$ is divisible by an integer $q$ if $m=q \ell$ for some integer $\ell$; we write $q \mid m$ and say " $q$ divides $m$ ". Thus $7 \mid 91$ because $91=7 * 13$, but $5 \nmid 91$ : " 5 does not divide $91 "$.

Let $p \geq 1$ be a positive integer. We want to use mathematical induction to show that $p^{2}+p+1$ divides $p^{n+1}+(p+1)^{2 n-1}$ for any integer $n \geq 1$ (note that here we have a starting point different from zero).

(1) Let $P(n)$ be the statement

$$
\begin{equation*}
p^{2}+p+1 \mid p^{n+1}+(p+1)^{2 n-1} \tag{14}
\end{equation*}
$$

where $n$ is a positive integer. We want to prove " $\forall n>0 P(n)$ ", where $n$ is a positive integer. Thus the domain is $\mathbf{N}_{>0}$ and we have that $b=1$, with $b$ as above.

(2) The basis step consists of proving that $P(b)$ holds, where $P(b)$ is the statement

$$
\begin{equation*}
p^{2}+p+1 \mid p^{1+1}+(p+1)^{2-1} \tag{15}
\end{equation*}
$$

which is derived from Statement (14) by replacing $n$ by $b=1$. Because the right hand side of Statement (15) evaluates to $p^{2}+p+1$ which equals the left hand side of Statement (15), the divisibility statement indeed holds. It follows that the basis step is correct.

(3) The inductive step:

(a) We make the induction hypothesis that $P(k)$ holds for an arbitrary integer $k$ in the domain. Thus, the induction hypothesis is the assumption that for an arbitrary integer $k \geq b=1$ it is the case that

$$
\begin{equation*}
p^{2}+p+1 \mid p^{k+1}+(p+1)^{2 k-1} \tag{16}
\end{equation*}
$$

this statement is derived from Statement (14) by replacing $n$ by $k$. Note that due to $k \geq 1$ and thus $2 k-1 \geq 1$ no unpleasant non-integer values will appear.

(b) We must prove that $P(k+1)$ holds, i.e., it must be proved that it is the case that

$$
\begin{equation*}
p^{2}+p+1 \mid p^{k+2}+(p+1)^{2 k+1} \tag{17}
\end{equation*}
$$

this statement is derived from Statement (14) by replacing $n$ by $k+1$.

(c) To prove that $P(k+1)$ holds, i.e., that Statement (17) is correct, we try to recognize "what we know" (or, actually, assume to be correct), namely Statement (16), in what we must prove, namely Statement (17). So, we know (or assume) something about $p^{k+1}+(p+1)^{2 k-1}$ (namely that it is divisible by $p^{2}+p+1$ ), and want to know something about $p^{k+2}+(p+1)^{2 k+1}$ (namely the same: that it is divisible by $\left.p^{2}+p+1\right)$. Finding a relation between these two that is relevant for our "divisibility by $p^{2}+p+1$ " purpose can be done as follows. Because $p^{k+2}=p * p^{k+1}$ we simply try to write our target value $p^{k+2}+(p+1)^{2 k+1}$ as $p\left(p^{k+1}+(p+1)^{2 k-1}\right)+x$ for some $x$ : because due to the induction hypothesis (Statement (16)) we may assume that $p\left(p^{k+1}+(p+1)^{2 k-1}\right)$ is divisible by $p^{2}+p+1$, all that remains to prove that Statement (17) holds is proving that $x$ is divisible by $p^{2}+p+1$. Solving

$$
p^{k+2}+(p+1)^{2 k+1}=p\left(p^{k+1}+(p+1)^{2 k-1}\right)+x
$$

for $x$ fortunately turns out to be a simple matter: the term $p^{k+2}$ on the left hand side cancels due to the identical term $p * p^{k+1}$ on the right hand side, so that

$$
(p+1)^{2 k+1}=p\left((p+1)^{2 k-1}\right)+x
$$

Now $(p+1)^{2 k+1}=(p+1)^{2}(p+1)^{2 k-1}=\left(p^{2}+2 p+1\right)(p+1)^{2 k-1}$ so that it follows that $x=\left(\left(p^{2}+2 p+1\right)-p\right)(p+1)^{2 k-1}$ and therefore that

$$
x=\left(p^{2}+p+1\right)(p+1)^{2 k-1}
$$

It follows that $x$ is divisible by $p^{2}+p+1$, which is all that we still had to prove (underlined above) for Statement (17) to hold. This completes the inductive step. (Note that during the lecture a slightly different (but overall equivalent) line of reasoning was followed.)

(4) It follows from the inductive step that $P(k+1)$ follows from $P(k)$ for any arbitrarily chosen integer $k \geq b=1$.

(5) Based on the basis step and the inductive step and the principle of mathematical induction, it follows that $\forall n>0 P(n)$.

All horses have the same color. This is probably the most popular examples of an incorrect proof using induction, which is why you have seen this example already in Analyse I. It is repeated here, if just to provide an alternative explanation of why the proof is wrong.

Our proposition $P(n)$ is that for any set of $n \geq 1$ horses all horses have the same color. The basis of the induction is proving $P(1)$, which is obviously true because all horses in a set of one horse have the same color.

The induction hypothesis is the assumption that for an arbitrary $k$ in the domain $P(k)$ is true, i.e., for any set consisting of $k \geq 1$ horses all horses have the same color. Given this $k$, we need to prove that $P(k+1)$ is true, i.e., that for any set of $k+1$ horses all horses have the same color.

Let $S$ be any set $S$ of $k+1$ horses, let $S_{1}$ be the same set $S$ with the first horse removed, and let $S_{2}$ be the same set $S$ with the last horse removed, as pictured below:

Because $S_{1}$ is a set consisting of $k$ horses, the induction hypothesis applies and all horses in $S_{1}$ have the same color: it follows that horse number $k+1$ has the same color as horses 2 through $k$. Similarly, because $S_{2}$ is a set consisting of $k$ horses, the induction hypothesis applies and all horses in $S_{2}$ have the same color: it follows that horse number 1 has the same color as horses 2 through $k$. Combining the two statements it follows that both horse 1 and horse $k+1$ have the same color as horses 2 through $k$, and thus that all $k+1$ horses in $S$ have the same color. Thus $P(k+1)$ follows, completing the proof of the induction step.

The problem with the proof is that the "overlapping part" (namely the part horses 2 through $k$ ) is empty for $k=1$, while $k=1$ is a valid value for $k$ (i.e., in the domain). And indeed, this is the only problem with the proof: as soon as one can prove that $P(2)$ holds (our proof of which failed due to the empty overlap between $S_{1}$ and $S_{2}$ ), i.e., that for any set of two horses the two horses have the same color, then indeed it follows that all horses have the same color. It is not uncommon for proofs by induction to fail due to carelessness with the boundary values for $k$.

Another incorrect proof by mathematical induction. Slight oversights in alleged proof by mathematical induction can easily lead to nonsensical results. For instance, and as mentioned in the book, when the basis step is simply omitted it is easy to "prove" that $n=n+1$ for all nonnegative integers $n$. Namely, suppose that for an arbitrary integer $k \geq 0$ it is the case that $k=k+1$ (the inductive hypothesis), then we may add one to both sides to get $k+1=k+2$, and thus $k+1=(k+1)+1$ showing that the statement is true for $k+1$ as well. This week's exercises will contain more nonsensical proofs by induction.

Removing the dots. Mathematical induction allows us to prove many "obvious" results that we have used in earlier lectures and that we just assumed to be true by handwaving. Below a few examples (mentioned during the lecture whenever our arguments relied in some obvious manner on "...", but not treated in detail).

- Let $T_{n}=\sum_{i=0}^{n} i$ and make the substitution $j=n-i$, as we did (or something close to it) in one of the earliest lectures. This substitution would turn $T_{n}=\sum_{i=0}^{n} i$ into $T_{n}=\sum_{j=n}^{0}(n-j)$, which is undesirable because for $n>0$ the first summation index $(n)$ would be larger than the final summation-index (0): for $n>0$ the summation $\sum_{j=n}^{0}(n-j)$ may thus be argued to be an empty sum which is equal to zero; because that clearly leads to nonsense, we just solved this "problem" by silently reversing the
order of the summation, and we safely settled on $T_{n}=\sum_{j=0}^{n}(n-j)$. But we never proved that we can indeed do so.

Assuming that we know that for integers it is the case that $x+y=y+x$, why would it also be the case that $x_{0}+x_{1}+\ldots+x_{n}=x_{n}+\ldots+x_{1}+x_{0}$ ? This is typically something that can be dealt with using mathematical induction - and that is done silently (actually, we should have formally defined $S_{n}=$ $\sum_{i=0}^{n} s_{i}$ as zero if $n<0$ and as $S_{n-1}+s_{n}$ otherwise; this is an example of a recursive definition, more about this later).

Given that we have accepted the definition $S_{n}=\sum_{i=0}^{n} s_{i}=s_{0}+s_{1}+\ldots+$ $s_{n}$ for any $n \geq 0$, there is no reason not to accept the following definition: $\widetilde{\sum}_{j=n}^{0} s_{j}=s_{n}+s_{n-1}+\ldots+s_{1}+s_{0}$ for any $n \geq 0$. With this notation, silently assuming that the order of the summation can be reversed then amounts to assuming that $\widetilde{\sum}_{j=n}^{0} s_{j}=\sum_{i=0}^{n} s_{i}$.

Let $P(n)$ be the propositional function " $\widetilde{\sum}_{j=n}^{0} s_{j}=\sum_{i=0}^{n} s_{i}$ " and let $\mathbf{N}=\{0,1,2, \ldots\}$ be the domain for $n$. We want to prove " $\forall n P(n)$ ". The basis step is proving that $P(0)$ is true: $P(0)$ is the statement " $\widetilde{\sum}_{j=0}^{0} s_{j}=$ $\sum_{i=0}^{0} s_{i} "$, which is true because the left hand side and the right hand side are both defined as $s_{0}$. The basis step is thus correct. For the inductive step, assume that $P(k)$ is true (i.e., that " $\widetilde{\sum}_{j=k}^{0} s_{j}=\sum_{i=0}^{k} s_{i}$ " is true) for an arbitrary $k \geq 0$; it has to be shown that $P(k+1)$ is true (i.e., that " $\left.\widetilde{\sum}_{j=k+1}^{0} s_{j}=\sum_{i=0}^{k+1} s_{i} "\right)$. According to the definition ${\widetilde{\sum_{j=k+1}}}^{0} s_{j}$ equals $s_{k+1}+s_{k}+\ldots+s_{1}+s_{0}$ which can be written as

![](https://cdn.mathpix.com/cropped/2024_05_17_080e33d4d6dd8006197eg-09.jpg?height=101&width=646&top_left_y=1437&top_left_x=705)

and thus as

![](https://cdn.mathpix.com/cropped/2024_05_17_080e33d4d6dd8006197eg-09.jpg?height=104&width=510&top_left_y=1570&top_left_x=773)

(again using the definition). Because $x+y=y+x$ for real values $x, y$, we find that

![](https://cdn.mathpix.com/cropped/2024_05_17_080e33d4d6dd8006197eg-09.jpg?height=107&width=516&top_left_y=1743&top_left_x=770)

Based on the inductive hypothesis " $\widetilde{\sum}_{j=k}^{0} s_{j}=\sum_{i=0}^{k} s_{i}$ " we may now conclude that

![](https://cdn.mathpix.com/cropped/2024_05_17_080e33d4d6dd8006197eg-09.jpg?height=124&width=472&top_left_y=1937&top_left_x=795)

Using the definition $\sum_{i=0}^{k} s_{i}=s_{0}+s_{1}+\ldots+s_{k}$, this leads to

![](https://cdn.mathpix.com/cropped/2024_05_17_080e33d4d6dd8006197eg-09.jpg?height=107&width=650&top_left_y=2122&top_left_x=703)

thus to

![](https://cdn.mathpix.com/cropped/2024_05_17_080e33d4d6dd8006197eg-09.jpg?height=104&width=604&top_left_y=2261&top_left_x=726)

and thus to

$$
\widetilde{\sum}_{j=k+1}^{0} s_{j}=\sum_{i=0}^{k+1} s_{i}
$$

(again using the definition), which proves that $P(k+1)$ is true, thereby completing the inductive step.

Given the correctness of the basis step and the inductive step, we may conclude that $P(n)$ is true for all $n \geq 0$.

- Another example is showing that

$$
M(n) \leq 2^{\ell} M\left(n / 2^{\ell}\right)+\ell n
$$

for any integer $\ell>0$ and any integer $n>0$, given that we have shown that for any $n>0$ it is the case that $M(n) \leq 2 M(n / 2)+n$ (we looked at this expression while analysing merge sort and (the optimal case of) quick sort). The basis step is showing the result for $\ell=1$ and any $n>0$, which amounts to showing that $M(n) \leq 2 M(n / 2)+n$, which is what was given; so the basis step is correct.

As inductive step, assume that

$$
M(n) \leq 2^{k} M\left(n / 2^{k}\right)+k n
$$

for an arbitrary $k \geq 0$ and all $n>0$ (this is the induction hypothesis); we must prove that $M(n) \leq 2^{k+1} M\left(n / 2^{k+1}\right)+(k+1) n$ for all $n>0$. Given the induction hypothesis, we have that $M(n) \leq 2^{k} M\left(n / 2^{k}\right)+k n$ for all $n>0$. We also have that $M(n) \leq 2 M(n / 2)+n$ for any $n>0$, so in particular we know that $M\left(n / 2^{k}\right) \leq 2 M\left(\left(n / 2^{k}\right) / 2\right)+\left(n / 2^{k}\right)$. Using this in $M(n) \leq 2^{k} M\left(n / 2^{k}\right)+k n$ (which is assumed to be true for all $n>0$ ) we find that $M(n) \leq 2^{k}\left(2 M\left(\left(n / 2^{k}\right) / 2\right)+\left(n / 2^{k}\right)\right)+k n=2^{k+1} M\left(n / 2^{k+1}\right)+(k+1) n$ for all $n>0$, which is what we had to prove. This completes the inductive step.

The statement now follows from the correctness of the basis step and the inductive step.

Note that in this example the role that $n$ played in the previous examples is now played by $\ell$, and that the $n$ here is just an independent parameter that can be chosen in any way one sees fit.

Strong induction ${ }^{2}$. Mathematical induction is based on the following tautology:

$$
(P(0) \wedge \forall k[\underline{P(k)} \rightarrow P(k+1)]) \rightarrow \forall n P(n)
$$

Thus, to be able to use mathematical induction we need to be able to prove for any $k$ in the domain that $P(k+1)$ follows from the single (underlined above) assumption $P(k)$. There are many applications where it would be convenient for the proof of $P(k+1)$ if $P(\ell)$ may be assumed to be valid for more values of $\ell<k+1$ than just $\ell=k$. In that case, we can use strong induction, which is the following tautology:

$$
(P(0) \wedge \forall k[\underline{[(\forall \leq k P(\ell))} \rightarrow P(k+1)]) \rightarrow \forall n P(n)
$$

Thus, compared to mathematical induction, the single assumption $P(k)$ is replaced by the (underlined) assumption that " $\forall \ell \leq k P(\ell)$ ", i.e., the combined assumption that $P(\ell)$ holds for all values of $\ell$ that are in the domain and at most $k$.

If " $\forall n P(n)$ " can be proved using mathematical induction (i.e., using "just" the assumption that $P(k)$ holds to prove that $P(k+1)$ holds), then " $\forall n P(n)$ " can obviously be proved using strong induction (i.e., using the assumption that $P(\ell)$ holds for any $\ell \leq k$ ). It is less clear (but not terribly hard to see, cf. $T(n)$ below) that this statement is also valid the other way around: if " $\forall n P(n)$ " can be proved using strong induction, then " $\forall n P(n)$ " can be proved using mathematical induction (using a propositional function different from $P(n)$ though - namely[^1]$T(n)=\bigwedge_{i=b}^{n} P(i)$ : see the example further below). Thus, these two types of induction, "mathematical" and "strong", are in principle equivalent, and both are equivalent to the "well-ordering principle". It is nevertheless convenient to have this other simple proof technique at our disposal as well.

A proof by strong induction follows the same general framework as a proof by mathematical induction, except that the single induction hypothesis is replaced by a conjunction of hypotheses for all integers in the domain that are at most equal to the "arbitrary integer" used in the induction hypothesis (i.e., the $k$ above). Care must be taken, however, with the basis step: in principle it is the same as for mathematical induction, but it is not uncommon that the proof of the inductive step (thus, the proof that the propositional function holds for $k+1$, where $k$ is arbitrary $\geq b$ ) works only for $k \geq b+s$ for some relatively small value of $s \in \mathbf{Z}_{>0}$; if this is the case, $P(b+1), P(b+2), \ldots, P(b+s)$ must be proved separately as well, because the inductive step must be proved for all $k \geq b$. This can be regarded as some kind of extension of the basis step. This "basis step extension", however, is not an intrinsic property of strong induction: it may be required for some proofs by strong induction while being superfluous for others. Refer to the exercises for examples of these basis step extensions.

First strong induction example (not done in class). Let $P(n)$ be the statement that "an integer $n$ is divisible by a prime number". Because $P(1)$ is false (because 1 is divisible only by 1 and 1 is not a prime number), let the domain be $\mathbf{Z}_{>2}$, i.e., all integers that are at least two.

The basis step consists of showing that $P(2)$ is true, which is indeed the case because 2 is divisible by the prime $2: 2=2 \cdot 1$.

The induction hypothesis is assuming that for any $k \geq 2$ it is the case that $P(\ell)$ is true for all integers $\ell$ with $2 \leq \ell \leq k$, i.e., that any integer between 2 and $k$, bounds included, is divisible by a prime number. We must prove that $P(k+1)$ is true, i.e., that $k+1$ is divisible by a prime number. If $k+1$ is a prime number, then $P(k+1)$ is true (and we do not need the induction hypothesis). If $k+1$ is not a prime number, then $k+1$ is composite and can thus be written as the product $k+1=\ell_{1} \cdot \ell_{2}$ of two integers $\ell_{1}$ and $\ell_{2}$ that are both $\geq 2$ and (thus) $<k+1$.

Note that we do not know anything about the primality of $\ell_{1}$ or $\ell_{2}-$ indeed, we are supposed to prove that $k+1$ is divisible by a prime number, and there is no reason why either $\ell_{1}$ or $\ell_{2}$ would have to be prime. But, given that $2 \leq \ell_{1} \leq k$, the induction hypothesis applies to $\ell_{1}$ based on which we may assume that $\ell_{1}$ is divisible by a prime number, i.e., that $\ell_{1}=p \cdot m$ for a prime number $p$ and some integer $m \geq 1$. It follows that $k+1$ is divisible by a prime number (because now $\left.k+1=p \cdot m \cdot \ell_{2}\right)$, thereby showing the correctness of the inductive step. Based on the correctness of the basis step and the inductive step it follows that any integer $n \geq 2$ is divisible by a prime number. Note that in this example there was no reason to use any type of basis step extension (as mentioned above).

Proving the same result using mathematical induction. Let $P(n)$ be as above, with domain $n \in \mathbf{Z}_{>2}$. We want to prove $\forall n P(n)$, but using mathematical induction. Let $T(n)$ be the propositional function $\bigwedge_{i=2}^{n} P(i)$. Then the basis step $T(2)$ is equivalent to $P(2)$ and thus true because $P(2)$ is true. Let $k$ be any integer $\geq 2$ and assume the induction hypothesis that $T(k)=\bigwedge_{i=2}^{k} P(i)$ is true - note that we are making just a single assumption here, though it is indeed a somewhat contrived one. We must prove that $T(k+1)=\bigwedge_{i=2}^{k+1} P(i)$ is true. Given that $T(k+1)=$ $\left(\bigwedge_{i=2}^{k} P(i)\right) \wedge P(k+1)$ and because, due to the induction hypothesis, $T(k)=$ $\bigwedge_{i=2}^{k} P(i)$ is true, all we have to prove is that $T(k+1)$, which equals "true" $\wedge P(k+1)$, is true, i.e., that $P(k+1)$ is true. But that follows as above, either from the validity
of $P(k+1)$ if $k+1$ is a prime number or of the validity of $P\left(\ell_{1}\right)$ (implied by the induction hypothesis; with $\ell_{1}$ as above) otherwise. Given the correctness of the basis step and the inductive step it follows that $\forall n T(n)$. But that implies $\forall n P(n)$. The same trick can be applied to convert any other strong induction proof into a proof that uses just mathematical induction.

## Strong induction and recursion.

Breaking chocolate bars into squares. Given a single piece of chocolate consisting of $n$ squares, we want to break it into $n$ pieces that are each a single square. Each time we break off a piece (always carefully along the lines, never breaking two pieces at the same time, and never breaking a single piece into more than two smaller pieces) we incur a cost of " 1 " (which we may want to interpret as a "step" or as a "break"). We want to minimize our overall cost to break the initial single piece consisting of $n$ squares into $n$ pieces that are just a single square each or, put equivalently, we want to minimize the total number of steps or breaks.

One may wonder if it would be faster to always try to break large pieces into two pieces of about the same size, or if it would be better to always look for "break lines" that are as long as possible, or if, on the contrary, always trying to break off the smallest possible piece or going for a shortest possible break line would be "better" (i.e., overall lead to less work: fewer breaks, fewer steps, smaller cost).

You don't have to mess around with real chocolate to observe that each step (or break) increases the number of pieces by precisely one, irrespective of the sizes of the pieces involved: there is only one piece that will be broken at a time, and each time that is done a single piece will be broken into precisely two pieces, thereby increasing the number of pieces by one. Initially (after zero steps) we have one piece, after one step we have two pieces, after two steps (assuming $n>2$ ) we have three pieces (irrespective of how smart we try to be with the size or shape of the piece that we break or of the pieces that result), etc. Thus: the number of pieces is always one more than the number of steps taken. Because the final number of pieces is $n$, it follows that the number of steps taken is $n-1$. We find that, irrespective of how we proceed, we will always end up making $n-1$ breaks, doing $n-1$ steps, and incur cost $n-1$.

Note that this argument does not depend on the shape of the pieces (triangles, anything) or in what crazy manner one decides to break or cut a piece into smaller parts, as long as each single step breaks or cuts one piece (of any shape) into two new pieces (of any shape): the final number of pieces is one larger than the number of breaks or cuts made. It is important, however, that only a single piece is broken per break.

Actually proving this result using strong induction is straightforward: a piece consisting of one square requires no breaks (this is the basis step), a piece consisting of $k+1$ squares (for an arbitrary integer $k \geq 1$, assuming as (strong) induction hypothesis that $\ell$ squares for any integer $\ell$ with $1 \leq \ell \leq k$ requires $\ell-1$ breaks) is broken at the cost of one break into a piece of $m$ squares and a piece of $k+1-m$ squares, for some integer $m$ with $1 \leq m \leq k$. Breaking the resulting $m$-square piece into $m$ single-square pieces costs $m-1$ breaks (based on the induction hypothesis), and breaking the other resulting piece of $k+1-m$ squares into $k+1-m$ singlesquare pieces costs $k+1-m-1$ breaks (based on the induction hypothesis) so the total number of breaks (to break the $k+1$-square piece into $k+1$ single-square pieces) is $1+m-1+\underline{k+1-m-1}=k$, thus completing the inductive step and showing, with the basis step, that for any positive integer $n$ breaking an $n$-square piece into $n$ single-square pieces requires $n-1$ breaks.

Splitting a piece of rock into smaller pieces. Given a single $n$-kilo piece of rock, we want to split it into $n$ single-kilo pieces by repeatedly splitting pieces of $m>1$ kilos into two pieces of $k$ and $m-k$ kilos (where $k$ is some integer $k$ with $k \geq 1$ and $k<m)$ until there are no pieces left that weigh more than a single kilo. Following the argument seen above (where we saw that the total number of pieces increases by one per split), the number of steps to be taken (i.e., the number of times a piece is split into two pieces) is $n-1$, irrespective of how we proceed (i.e., of how $k$ is chosen per split). Unlike the previous example, however, there is no longer a simple unit cost per split, we assume the existence of a device that cuts a stone of any integer number $m$ of kilos, where $m \in \mathbf{Z}_{>1}$, into two smaller stones of $\ell$ and $m-\ell$ kilos (for any integer $\ell$ with $1 \leq \ell<m)$ at cost $\ell(m-\ell)$ (i.e., the cost is the product of the weights of the resulting parts). It should be understood that this is the definition of the cost function in this case, and that discussion of whether or not the definition is reasonable is irrelevant - it is just an example that does not necessarily have any real-life stone-splitting consequences or relevance. We want to minimize the overall cost to split the $n$-kilo rock into $n$ one-kilo pieces, and prove that our solution is optimal.

As with the chocolate-bar example, it is not a priori obvious if some type of optimal strategy must be found to minimize the overall cost, or if we may proceed in any random manner (as turned out to be the case in the chocolate-example, where the cost is always $n-1$ independent of any "clever" strategy we may want to apply). To get some intuition it is helpful to do a few small examples. Denote by $S(n)$ the minimal cost to split a single $n$-kilo piece of rock into $n$ single-kilo pieces using the above multiplicative cost-function (where the cost of a split is the product of the weights of the two resulting parts). Thus

$$
\begin{equation*}
S(n)=\min _{1 \leq k<n}(k(n-k)+S(k)+S(n-k)) \tag{18}
\end{equation*}
$$

It follows that to find $S(n)$ for $n>1$ we need to know all values $S(\ell)$ for $1 \leq \ell<n$ first, so it makes sense ${ }^{3}$ to calculate the $S(n)$-values from the "bottom up", i.e., starting at $n=1$ We find

$$
\begin{aligned}
S(1) & =0, \\
S(2) & =1 \text { : all we can do is split the } 2 \text {-kilo rock into two } 1 \text {-kilo pieces, at cost } 1 * 1=1, \\
S(3) & =1 *(3-1)+S(1)+S(2)=2+0+1=3, \\
S(4) & =\min (1 *(4-1)+S(1)+S(3), 2 *(4-2)+S(2)+S(2)) \\
& =\min (3+0+3,4+1+1)=\min (6,6) \\
& =6 \text { irrespective of how we decide to make the initial split: } 1+3 \text { or } 2+2, \\
S(5) & =\min (1 *(5-1)+S(1)+S(4), 2 *(5-2)+S(2)+S(3)) \\
& =\min (4+0+6,6+1+3)=\min (10,10) \\
& =10 \text { irrespective of how we decide to make the initial split: } 1+4 \text { or } 2+3, \\
S(6) & =\min (1 *(6-1)+S(1)+S(5), 2 *(6-2)+S(2)+S(4), 3 *(6-3)+S(3)+S(3)) \\
& =\min (5+0+10,8+1+6,9+3+3)=\min (15,15,15) \\
& =15 \text { irrespective of how we decide to make the initial split: } 1+5 \text { or } 2+4 \text { or } 3+3 .
\end{aligned}
$$

Given that we consistently get the same cost, independent of the splitting choices that we make, we are beginning to suspect that (despite the more contrived cost function compared to the chocolate-bar example) there is no optimal strategy to the extent that all strategies are equally good (or bad). Furthermore, the resulting[^2]sequence " $S(1)=0, S(2)=1, S(3)=3, S(4)=6, S(5)=10, S(6)=15$ " may not (yet) but should begin to look familiar: with differences $S(i)-S(i-1)$ that are consistently equal to $i-1$, the values of $S(n)$ seen so far are apparently ${ }^{4}$ all equal to $\sum_{i=1}^{n}(i-1)=\frac{(n-1) n}{2}$.

Thus we suspect that $S(n)=\frac{(n-1) n}{2}$ holds in general (i.e., for $n \in \mathbf{Z}_{\geq 1}$ ). We use strong induction to prove that this is indeed the case. We take the statement that $S(n)=\frac{(n-1) n}{2}$ for $n \in \mathbf{Z}_{\geq 1}$ as our propositional function and note that (based on the examples) the basis step (that $S(1)=\frac{(0-1) 0}{2}=0$ ) is okay. Taking an arbitrary $k \in \mathbf{Z}_{\geq 1}$ we make the assumption that $S(\ell)=\frac{(\ell-1) \ell}{2}$ for all $\ell$ with $1 \leq \ell \leq k$ (this is our (strong) induction hypothesis), and we must prove that $S(k+1)=\frac{k(k+1)}{2}$.

To prove this, what do we know about $S(k+1)$ ? We know for sure (from Equation (18)) that

$$
S(k+1)=\min _{1 \leq \ell \leq k}(\ell(k+1-\ell)+S(\ell)+S(k+1-\ell))
$$

Given our examples above, however, we conjecture that any value for $\ell$ (in the " $\min _{1 \leq \ell \leq k ")}$ will lead to the same result, i.e., that the resulting expression that we get is independent of $\ell$. Taking any $\ell$ with $1 \leq \ell \leq k$ we find that

$$
\ell(k+1-\ell)+S(\ell)+S(k+1-\ell)=\ell(k+1-\ell)+\frac{(\ell-1) \ell}{2}+\frac{(k-\ell)(k+1-\ell)}{2}
$$

where we have used the induction hypothesis twice: once for $S(\ell)=\frac{(\ell-1) \ell}{2}$ and once for $S(k+1-\ell)=\frac{(k-\ell)(k+1-\ell)}{2}$. It follows using simple algebraic manipulations that everything with an $\ell$ in it cancels:

$$
\begin{aligned}
& \ell(k+1-\ell)+\frac{(\ell-1) \ell}{2}+\frac{(k-\ell)(k+1-\ell)}{2}= \\
& k \ell+\ell-\ell^{2}+\frac{\ell^{2}}{2}-\frac{\ell}{2}+\frac{k^{2}}{2}+\frac{k}{2}-\frac{k \ell}{2}-\frac{k \ell}{2}-\frac{\ell}{2}+\frac{\ell^{2}}{2}
\end{aligned}
$$

with only $\frac{k^{2}}{2}+\frac{k}{2}=\frac{k(k+1)}{2}$ remaining. It follows that

$$
\ell(k+1-\ell)+S(\ell)+S(k+1-\ell)=\frac{k(k+1)}{2}
$$

This not just proves our conjecture that the resulting expression is independent of $\ell$ but also shows that indeed the resulting value $S(k+1)$ equals $\frac{k(k+1)}{2}$. This concludes the inductive step. The conclusion that $S(n)=\frac{(n-1) n}{2}$ for $n \in \mathbf{Z}_{\geq 1}$ now follows from the correctness of the basis step and the inductive step.

Combinatorial argument. Often (but not always) a surprisingly easy solution (such as the above independence of the splitting strategy and the simple overall cost $\left.\frac{(n-1) n}{2}\right)$ has a relatively simple explanation that allows the "immediate insight" that the result is correct; it can hardly be argued that the above analysis is simple or provides any insight why the result $\frac{(n-1) n}{2}$ "makes sense", given the problem that we set out to solve, so having an independent argument why the result must be correct could be useful. Such relatively simple explanations (of results that may independently be derived using a mathematical analysis, as for the rock example above) are often referred to as combinatorial arguments.

To find a combinatorial argument for the rock splitting result it helps to consider the analogy with a group of $n$ people that splits into two smaller groups, with each[^3]smaller group splitting again into subgroups, etc., until there are $n$ separate ungrouped individuals left, where each time a group (of, say, $m$ people) splits up (into, say, $k$ and $m-k$ people) each member of the first part of the group (the part containing $k$ people) shakes hands with each member of the other part of the group (the part containing $m-k$ people). This implies that per split of $m$ into " $k \& m-k$ " a total of $k(m-k)$ handshakes takes place because each of the $k$ persons of one part of the group has to shake hands with each of the $m-k$ persons in the other part of the group. The number $k(m-k)$ of handshakes when a group of $m$ splits up into " $k \& m-k$ " corresponds to our rock-splitting cost-function above where splitting an $m$-kilo rock into two pieces of weights $k$ and $m-k$ incurs a cost of $k(m-k)$. It also follows that at the end (when there are $n$ separate un-grouped individuals left) everyone has shaken hands with everyone else precisely once, irrespective of how the groups were split up. Because there are a total of $\frac{(n-1) n}{2}$ handshakes (namely the number of distinct unordered pairs $(x, y)$ with $x \neq y$ among $n$ people) that can take place among $n$ people (and due to the cost-correspondence) that must be the overall rock-splitting cost as well.

Finding such analogies turns out to be very useful when "counting" or when trying to convince yourself that a certain counting result is correct - or not (obviously, it can also be misleading and put you on the wrong track if the argument or analogy fails in some subtle way).

Next class. Read Section 5.3 "Recursion" until (and not including) Lamé's theorem, and Section 5.4 "Recursive Algorithms" (skipping the subsection on Proving Recursive Algorithms Correct), while skipping Section 5.5 entirely. Then we move to counting: to prepare, read sections 6.1, 6.2, and 6.3 (excluding Ramsey).


[^0]:    ${ }^{1}$ If you wish you can prove that $1 \leq 2^{\ell}$ for all integers $\ell \geq 0$ using another proof by induction. But given that it is true for $\ell=0$ combined with the fact that the $2^{\ell}$ on the right hand side is a growing function of $\ell$ whereas the left hand side is a constant, insisting on using induction for this triviality would be overdoing it a bit.

[^1]:    ${ }^{2}$ The next few paragraphs repeat what was already mentioned during the previous lecture; it was also described in the October 30 lecture notes.

[^2]:    ${ }^{3}$ Note that Equation (18) defines $S(n)$ "recursively" in terms of itself, with smaller arguments: this requires that $S(n)$ for the lowest possible $n$-value - the bottom of the recursion - can be found independently. That turns out to be possible indeed, because $S(1)=0$. The observation that determining $S(n)$ requires knowledge of $S(\ell)$ for $\ell<n$ and thus that these values $S(\ell)$ must be systematically calculated first - while keeping them around for future reference! - is an example of dynamic programming.

[^3]:    ${ }^{4}$ Actually, in general not "apparently" at all: there are plenty of other sequences that start with $0,1,3,6,10,15$, as can be checked on the online encyclopedia of integer sequences. The one we choose is the only one that we have seen so far in this class.

