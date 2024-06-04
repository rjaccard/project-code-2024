Rock splitting revisited. We briefly considered the question why the "cost" of splitting an $n$ kilo piece of rock into $n$ pieces of a single kilo is independent of the strategy used (in the scenario where each piece of $k>1$ (with $k \in \mathbf{Z}$ ) kilos is split into two pieces of $\ell \geq 1$ (with $\ell \in \mathbf{Z}$ ) and $k-\ell$ kilos, as a certain cost per split, until there are $n$ pieces of a single kilo). The answer is that it depends on how the cost function is defined: for the cases seen last time it indeed does not matter how one proceeds, but for another cost function (as seen earlier when discussing quick sort) the overall cost depends on how one proceeds:

Cost 1 per split: Because the number of splits is $n-1$ irrespective of how one proceeds (as argued last time), the overall cost is $n-1$ as well.

Cost $\ell(k-\ell)$ per split: In this case the number of splits is again $n-1$, but the overall cost turns out to be $\frac{n(n-1)}{2}$ irrespective of how one proceeds. The latter was explained using a "combinatorial argument" involving handshakes (cf. Novembr 2 lecture notes).

Cost $\ell+k-\ell=k$ per split: In this case the number of splits is again $n-1$, but the overall cost depends on how one proceeds: if each piece of rock is always (given the conditions that only pieces of an integer number of kilos may be produced) split into two equal (or almost equal) parts, then the overall cost will be $\Theta(n \log (n))$, if for each split one just chips of a piece of a single kilo, then the overall cost will be $\Theta\left(n^{2}\right)$. Refer to the description of quick sort for a further discussion and explanation of these results.

Recursive definitions. Induction builds up from the basis step. Recursion exploits a similar basis step (calling it the bottom of the recursion), but uses it in a different manner, namely by expressing how a large problem can be solved in terms of solutions to one or more smaller problems of the same sort, and repeating this until the "bottom" is reached. We have seen this recursive approach already when defining quick sort and merge sort, where the bottom was that it is easy to sort a list consisting of a single element.

Applications abound, and we constantly encounter them in a natural manner, such as in the solutions to the various stone splitting problems, or in the definition
(that you are already familiar with) of the Fibonacci numbers: $f_{n}=n$ for $n=$ 0,1 and $f_{n}=f_{n-2}+f_{n-1}$ for $n \geq 2$. Recursion can also be used to formally define what we mean by $\sum_{i=0}^{n} x_{i}$. For instance, for lower bound $\ell \in \mathbf{Z}$ and upper bound $u \in \mathbf{Z}$ and, say, $x_{i} \in \mathbf{C}$ for $i \in \mathbf{Z}$, one may define $\sum_{i=\ell}^{u} x_{i}=0$ if $\ell>u$ and otherwise define $\sum_{i=\ell}^{u} x_{i}=\left(\sum_{i=\ell}^{u-1} x_{i}\right)+x_{u}$ (or, if you prefer and in slight variation compared to the book, the latter definition for $\ell \leq u$ can be replaced by $\left.\sum_{i=\ell}^{u} x_{i}=x_{\ell}+\left(\sum_{i=\ell+1}^{u} x_{i}\right)\right)$. Similarly, we can define $\prod_{i=\ell}^{u} x_{i}=1$ if $\ell>u$ and otherwise define $\prod_{i=\ell}^{u} x_{i}=\left(\prod_{i=\ell}^{u-1} x_{i}\right) \cdot x_{u}$ (or, equivalently but differently, $\prod_{i=\ell}^{u} x_{i}=x_{\ell} \cdot\left(\prod_{i=\ell+1}^{u} x_{i}\right)$ if $\left.\ell \leq u\right)$; or we can define $n!=\prod_{i=1}^{n} i$ recursively as $n!=(n-1)!n$ for $n>0$ and else (if $n=0)$ define $n!$ as $\prod_{i=1}^{0} i$ (and thus $0!=1$ ).

Remark on induction versus recursion. Though quite different approaches to proving results and solving problems, induction and recursion have in common that they both in the first place rely on the ability to achieve the desired result for (any number of instances of) the smallest possible version of the problem at hand, with induction extending this ability to problems of any size, and recursion reducing a problem of any size to the smallest possible ones. Thus, the way induction and recursion exploit this "solution to the smallest problem" is completely different:

- In induction it is shown how the solution to a problem instance can always be used (by means of the inductive step) to solve a larger instance, the idea being that if one keeps doing this starting from the (already solved) smallest problem (the basis of the induction or the basis step), all problem sizes can be tackled.
- In recursion it is shown how any larger problem instance can always be solved (by means of the recursive step) by solving one or more smaller subproblems, the idea being that if one keeps doing this, ultimately one reaches (one or more instances of the) the smallest problem (the bottom of the recursion) which one knows how to solve (as in merge sort and quick sort).

Keep in mind that, no matter how smart the inductive or recursive steps may be, without proper "basis of the induction" or "bottom of the recursion" both methods are worthless.

Recursive algorithms. Often recursive definitions can be directly translated into programs, turning recursion into an amazingly powerful programming technique that can be used to quickly produce working prototypes - and that has all the potential to lead to all kinds of unpleasant surprises too, if the pitfalls are not properly understood. We give a few examples (and refer to the book for more).

Summation. Computing the sum $\sum_{i=\ell}^{u} f(i)$ of function values $f(\ell), f(\ell+1), \ldots, f(u)$ (obviously, never do this in practice, but use a simple loop instead):

$$
\operatorname{sum}(f, \ell, u)=\text { if } \ell>u \text { then } 0 \text { else } f(\ell)+\operatorname{sum}(f, \ell+1, u)
$$

where we use the second, alternative definition $\sum_{i=\ell}^{u} x_{i}=x_{\ell}+\left(\sum_{i=\ell+1}^{u} x_{i}\right)$ given above. Note that the actual calculation that will be carried out evaluates the sum
from right to left:

$$
\underbrace{f(\ell) \stackrel{u-\ell+1}{+}(f(\ell+1) \stackrel{u-\ell}{+}(\ldots \stackrel{4}{+}(f(u-2) \stackrel{3}{+}(\underbrace{f(u-1) \stackrel{2}{+}(\underbrace{f(u) \stackrel{1}{+}(0)}_{\text {fecond addition }}))}_{\text {second last addition }} \ldots))}_{\text {last addition }}
$$

with the first addition $\stackrel{1}{+}$ performed first, the second addition $\stackrel{2}{+}$ performed second, etc., until the last addition $\stackrel{u-\ell+1}{+}$ of $f(\ell)$ and the at that point already calculated part $\operatorname{sum}(f, \ell+1, u)$ of the summation.

If we would have used the "regular" definition $\sum_{i=\ell}^{u} x_{i}=\left(\sum_{i=\ell}^{u-1} x_{i}\right)+x_{u}$ our computation would look like

$$
\operatorname{sum}(f, \ell, u)=\text { if } \ell>u \text { then } 0 \text { else } f(u)+\operatorname{sum}(f, \ell, u-1)
$$

and the sum would have been computed from left to right as $((f(\ell) \stackrel{1}{+} f(\ell+1)) \stackrel{2}{+}$ $f(\ell+2)) \stackrel{3}{+} \ldots$. Though equivalent from a mathematical point of view, the two summations may produce entirely different results when performed on a computer - do you know why?

Recursion is a great way to achieve these kinds of effects (though in the example above it is trivially achieved by "reversing the order of the loop"): there are circumstances (as in power ${ }_{\ell}$ below) where this kind of "reversal" serves a useful purpose and where it may be harder to achieve in another way that is as convenient. par Factorial. Computing $n$ ! (as for the sum above, a simple loop would have been much better; below I avoid the book's notation " $n=0$ " to test if $n$ is zero, because it easily leads to (common) C-disasters):

$$
\text { factorial }(n)=\text { if } n \leq 0 \text { then } 1 \text { else } n \cdot \text { factorial }(n-1) \text {. }
$$

Note that, as with the summation example, the multiplication of $n$ and factorial( $n-$ $1)$ is the last multiplication that is carried out during the computation of factorial $(n)$ : for example 6 ! is calculated as

Exponentiation: how not to compute $a^{n}$ (for $a \in \mathbf{R}$ and $n \in \mathbf{Z}_{\geq 0}$ ):

$$
\text { bd_power }(a, n)=\text { if } n \leq 0 \text { then } 1 \text { else } a \cdot \text { bd_power }(a, n-1) \text {. }
$$

This computes, for instance, bd_power $(a, 5)$ as

$$
\begin{aligned}
\text { bd_power }(a, 5)= & a \cdot \text { bd_power }(a, 4) \\
= & a \cdot(a \cdot \text { bd_power }(a, 3)) \\
= & a \cdot(a \cdot(a \cdot \operatorname{bd} \text { _power }(a, 2))) \\
= & a \cdot\left(a \cdot\left(a \cdot\left(a \cdot \operatorname{bd} \_ \text {power }(a, 1)\right)\right)\right) \\
= & a \cdot(a \cdot(a \cdot(a \cdot(a \cdot \text { bd_power }(a, 0))))) \\
& (\text { so far we have not done anything useful yet }) \\
= & a \cdot(a \cdot(a \cdot(a \cdot(a \cdot 1)))) \\
= & a \cdot\left(a \cdot\left(a \cdot\left(a \cdot\left(a^{1}\right)\right)\right)\right) \\
= & a \cdot\left(a \cdot\left(a \cdot\left(a^{2}\right)\right)\right) \\
= & a \cdot\left(a \cdot\left(a^{3}\right)\right) \\
= & a \cdot\left(a^{4}\right) \\
= & a^{5},
\end{aligned}
$$

thus requiring not just time linear in the exponent $n$ but (as the earlier examples) also recursion depth linear in the exponent: given how easy it is to replace this usage of recursion by a loop, using recursion is really a very bad idea - as in all earlier examples. But, unlike the earlier examples, even using a loop to do the calculation in this manner is a bad idea too (unless $n$ is very small), as shown in the next paragraphs.

Exponentiation: a much better approach. The function power $_{\ell}$ below is a first example of a useful application of recursion to quickly get something that works and that is efficient (and that is not outrageously stupid, like the other recursion examples so far). It exploits the fact that at the cost of one squaring and at most one multiplication the exponent $n$ can be halved, thus leading to at least $\log _{2}(n)$ and at most $2 \log _{2}(n)$ (and thus $\left.\Theta(\log (n))\right)$ multiplications, by observing that for odd $n$ one has $a^{n}=a \cdot a^{n-1}$ where $n-1$ is even, and that for even $n>0$ one has $a^{n}=\left(a^{n / 2}\right)^{2}$. The two cases are easily combined in the following recursive exponentiation function:

$$
\operatorname{power}_{\ell}(a, n)=\text { if } n \leq 0 \text { then } 1 \text { else } a^{n \& 1} \cdot\left(\operatorname{power}_{\ell}(a,[n / 2])\right)^{2},
$$

where $n \& 1 \in\{0,1\}$ is zero if and only if $n$ is even and where $[n / 2]$ is the integer part of $n / 2$ (note that here we are not dwelling on programming details on how to deal with the (trivial) computation of $a^{n \& 1}$, how to avoid multiplying by one, or how to compute a square). Use big- $O$ or big- $\Omega$ and such to express (and compare) the number of multiplications carried out by this exponentiation method compared to the earlier example bd_power $(a, n)$. The example below may be helpful.

It is instructive to see how power p $_{\ell}$ carries out an exponentiation by conveniently processing the bits of the exponent $n$ from right to left (by simply looking at the parity of the (recursive) exponent), while doing the actual calculation using the bits of the exponent $n$ from left to right. This is an example of the reversal mentioned above; of course this can also be achieved using a regular loop that avoids the usage of recursion, but recursion allows us to program it very quickly.

For instance for $n=25\left(=_{\mathrm{b}}\right.$ 11001) (denoted $\left.25_{11001}\right)$, the recursion results in

$$
\begin{aligned}
\operatorname{power}_{\ell}\left(a, 25_{11001}\right) & =a \cdot\left(\operatorname{power}_{\ell}\left(a, 12_{1100}\right)\right)^{2} \\
& =a \cdot\left(\left(\operatorname{power}_{\ell}\left(a, 6_{110}\right)\right)^{2}\right)^{2} \\
& =a \cdot\left(\left(\left(\operatorname{power}_{\ell}\left(a, 3_{11}\right)\right)^{2}\right)^{2}\right)^{2} \\
& =a \cdot\left(\left(\left(a \cdot\left(\operatorname{power}_{\ell}\left(a, 1_{1}\right)\right)^{2}\right)^{2}\right)^{2}\right)^{2} \\
& =a \cdot\left(\left(\left(a \cdot\left(a \cdot\left(\operatorname{power}_{\ell}\left(a, 0_{0}\right)\right)^{2}\right)^{2}\right)^{2}\right)^{2}\right)^{2}
\end{aligned}
$$

thus chipping off the bits from the exponent from right to left and resulting in recursion depth equal to the bit-length of the exponent 25.

Once the bottom of the recursion is reached with this final value

$$
a \cdot\left(\left(\left(a \cdot\left(a \cdot\left(\operatorname{power}_{\ell}\left(a, 0_{0}\right)\right)^{2}\right)^{2}\right)^{2}\right)^{2}\right)^{2}
$$

the calculation is actually carried out, where the result is built as $a^{1_{1}}, a^{2_{10}}, a^{3_{11}}$, $a^{6_{110}}, a^{12_{1100}}, a^{24_{11000}}, a^{25_{11001}}$ using the bits of the exponent from left to right:

$$
\begin{aligned}
a \cdot\left(\left(\left(a \cdot\left(a \cdot\left(\operatorname{power}_{\ell}\left(a, 0_{0}\right)\right)^{2}\right)^{2}\right)^{2}\right)^{2}\right)^{2} & =a \cdot\left(\left(\left(a \cdot\left(a \cdot(1)^{2}\right)^{2}\right)^{2}\right)^{2}\right)^{2} \\
& =a \cdot\left(\left(\left(a \cdot\left(a^{1}\right)^{2}\right)^{2}\right)^{2}\right)^{2} \\
& =a \cdot\left(\left(\left(a \cdot a^{2}\right)^{2}\right)^{2}\right)^{2} \\
& =a \cdot\left(\left(\left(a^{3}\right)^{2}\right)^{2}\right)^{2} \\
& =a \cdot\left(\left(a^{6}\right)^{2}\right)^{2} \\
& =a \cdot\left(a^{12}\right)^{2} \\
& =a \cdot a^{24} \\
& =a^{25} .
\end{aligned}
$$

The resulting number of squarings is approximately equal to the bit-length of the exponent, and the number of multiplications (by $a$ ) is equal to the number of onebits (minus one) in the binary representation of the exponent.

Note that even though in the recursion the bits of the exponent are chipped off from right to left, in the actual calculation that is carried out in the recursion the bits are used from left to right. This powering method is therefore referred to as left-to-right exponentiation (hence the subscript " $\ell$ " in power $_{\ell}$ ). Accessing the bits of the exponent from left to right in an iterative non-recursive manner (the way one should program left-to-right exponentiation) requires more cumbersome bit manipulations that can conveniently be avoided using the recursive reversal trick.

Compared to our earlier bd_power $(a, n)$ an enormous speed-up is achieved by power $_{\ell}$ : using bd_power $(a, n)$ for an exponent $n \approx 10^{6}$ would require about a million multiplications, whereas for $\operatorname{power}_{\ell}(a, n)$ fewer than forty multiplications suffice. This is not just a matter of a "convenient speed-up", given that in (ubiquitous) applications one easily has $n \approx 2^{1024}$ (a number of more than 300 decimal digits) or even much larger, it enables applications that would otherwise have been infeasible: the fast left-to-right exponentiation is one of the most important operations in current public key cryptography (where $a$ is not just some regular real or integer number for which $a^{n}$ may become too large or small to even write down, but where $a$ belongs to a finite "group" - details that may be explained next semester in AICC-II).

Searching and sorting. Binary search, quick sort and merge sort are other examples where it is convenient to use recursion (see earlier lectures and section 5.4) - though in particular for binary search it is easily replaced by an iterative approach.

Computing Fibonacci numbers. It gets interesting when we compute fibonacci numbers directly using recursion:

$$
\text { fib }(n)=\text { if } n \leq 1 \text { then } n \text { else fib }(n-2)+\operatorname{fib}(n-1)
$$

Try by hand to see what happens, and try to figure out how to avoid the undesirable effects that you will witness: during the calculation of, for instance, fib(10) a huge recursive tree is built to compute fib(8) (involving, among others, fib(7)), and in the ensuing computation of fib(9) this entire computation of fib(7) and of fib(8) (involving yet another fib(7)) is repeated. This is not just inefficient, it is a major stupidity, and a nice example of the kind of pitfalls one should avoid when blindly using recursion.

Ideally, such mishaps are avoided by replacing the recursion by a simple iterative approach (i.e., a "loop") which, in the present case, would work as follows (and which, clearly, works in time linear in $n$; but which also requires a bit more "thinking" to get right than the disastrously stupid direct recursion approach, because one has to fool around a bit with several variables):

$$
\begin{gathered}
\text { fib }(n)=\text { if } n \leq 1 \text { then } n \quad \text { (i.e., the result if } n \leq 1 \text { ) } \\
\text { else previous } \leftarrow 0, \text { current } \leftarrow 1 \\
\text { for } i=2 \text { to } n \text { do } \\
\text { next } \leftarrow \text { previous }+ \text { current } \\
\text { previous } \leftarrow \text { current } \\
\text { current } \leftarrow \text { next }
\end{gathered}
$$

(contemplate what happens if the previous two lines are reversed)

current (i.e., the result if $n>1$ )

Memoization. There are also examples where iteration is not so easy to achieve; in that case recursion-mishaps (such as witnessed above or as in the - even worse - example below) can be avoided by simple common sense, namely by making sure that one "remembers" values that have been computed and that may be needed again. In their full generality, such on-the-fly "tabulation methods" are referred to as memoization ${ }^{1}$, another example of dynamic programming. For Fibonacci it would work as follows. Let $f[0], f[1], f[2], \ldots$ be a global array with initially "uninitialized" values.

$$
\begin{aligned}
& \text { fibdp }(n)=\text { if } f[n] \text { is not initialized yet } \\
& \text { then if } n \leq 1 \text { then } f[n] \leftarrow n \\
& \text { else } f[n] \leftarrow \text { fibdp }(n-2)+\operatorname{fibdp}(n-1) \\
& f[n] \text { (i.e., the result) }
\end{aligned}
$$

This approach runs in time and worst case recursion depth linear in $n-$ still pretty bad with respect to the recursion depth, but much better than the direct approach; note that the worst case recursion depth is only reached when fibdp $(n)$ is called "from scratch" (i.e., when the entire array $f$ is still uninitialized), but that it is entirely avoided when fibdp $(i)$ is called for $i=0,1,2, \ldots, n$ in succession. More in general, if $m$ is the largest integer for which fibdp $(m)$ has been computed so far, and a call is made to fibdp $(n)$, then no calculation is required if $n \leq m$ (fibdp just[^0]looks up and returns $f[n]$ ), and if $n>m$ the calculation requires recursion depth about $n-m$.

It is a nice exercise to design an efficient (i.e., requiring about $n$ additions) recursive program to compute the $n$-th Fibonacci number that does not need memoization.

More bad ideas. As an aside, try to imagine what would happen if someone had the excruciatingly bad idea to write a recursive program to compute the rock splitting cost $S(n)$ using the recursive definition

$$
S(n)=\min _{1 \leq k<n}(k(n-k)+S(k)+S(n-k))
$$

(as we did, more or less (but with dynamic programming), in the example calculations, and as done in its full recursive, memoization-less stupidity in the C-program below - it does not even take the trouble to stop the loop at $[n / 2] \ldots)$. What can you say about the number of recursive calls (as counted by the ugly global variable calls) made as a function of $n$ when $S(n)$ is calculated in this manner (see example program and output below)?

Next class. Counting: (re)read sections 6.1, 6.2, 6.3.

```
/* real_stupid.c: to compute rock splitting cost */
#include <stdio.h>
long calls;
long s(
{-porg n
    long k;
    calls ++;
    if ( <<=1) return(0)
    cost = (n-1)+s(1)+s(n-1)
        long cost k = k*(n-k)+s(k)+s(n-k)

```

```
}
    return(cost);
main() {
    long n;
        scanf("%1d",&n);
        cal1s==";
    }
gcc -o -o rs real_stupid.c
$./rs
s(10)=45 (required 19683 cal1s)
S(15)=105 (required 4782969 cal1s)
(control C)
```


[^0]:    ${ }^{1}$ As explained on Wikipedia, this is the correct spelling - without an " $\mathrm{r}$ " (copied from Wikipedia): The term "memoization" was coined by Donald Michie in 1968 and is derived from the Latin word "memorandum" ("to be remembered"), usually truncated as "memo" in the English language, and thus carries the meaning of "turning [the results of] a function into something to be remembered." While "memoization" might be confused with "memorization" (because they are etymological cognates), "memoization" has a specialized meaning in computing.

